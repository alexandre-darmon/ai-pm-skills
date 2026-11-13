import contextlib
import io
import json
import os
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

import openrouter
from judge_answers import PROMPT, SYSTEM, run_judge
from judge_answers import main as judge_main
from test_human_rating import make_repo

KEY = "sk-or-test-not-a-real-key"
CHAT_REPLY = '{"sound": 5, "actionable": 4, "honest_about_unknowns": 3, "risk_aware": 2, "specific": 1, "meets_goal": 4, "weakest_point": "w"}'


def jev_reply(score=2.0):
    return {"model": "typesafe/jev-1.14-20261101", "usage": {"input_tokens": 900, "output_tokens": 60, "cost": 0.00004},
            "answers": {k: {"type": "score", "score": score, "confidence": 0.9} for k in [*openrouter.RUBRIC, "meets_goal"]}}


class FakeSend:
    def __init__(self, reply):
        self.reply, self.calls = reply, []

    def __call__(self, path, body):
        self.calls.append((path, body))
        return self.reply


class FakeJev:
    """Stands in for call_jev: records the items it gets, answers 3 everywhere."""
    takes_item = True

    def __init__(self):
        self.items = []

    def __call__(self, item, model):
        self.items.append(item)
        return {**{k: 3.0 for k in [*openrouter.RUBRIC, "meets_goal"]}, "weakest_point": "", "longContext": False, "costUsd": 0.0001}


class Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def http_error(code, body=b'{"error": "x"}'):
    return urllib.error.HTTPError("https://openrouter.ai", code, "err", {}, io.BytesIO(body))


class RubricTest(unittest.TestCase):
    def test_same_rubric_and_system_as_the_claude_judges(self):
        self.assertEqual(openrouter.SYSTEM, SYSTEM)
        for criterion, text in openrouter.RUBRIC.items():
            self.assertIn(f"- {criterion}: {text}\n", PROMPT)

    def test_folder_names_and_kinds(self):
        self.assertEqual(openrouter.dir_name("typesafe/jev-1.14"), "typesafe--jev-1.14")
        self.assertEqual(openrouter.dir_name("claude-haiku-5-5"), "claude-haiku-5-5")
        self.assertTrue(openrouter.is_decision("typesafe/jev-1.14"))
        self.assertFalse(openrouter.is_decision("openai/gpt-x"))
        self.assertIs(openrouter.caller("typesafe/jev-1.14"), openrouter.call_jev)
        self.assertIs(openrouter.caller("openai/gpt-x"), openrouter.call_chat)

    def test_moving_aliases_are_refused(self):
        for model in ("~typesafe/jev-latest", "typesafe/jev-latest", "openai/gpt-x:free"):
            with self.assertRaises(SystemExit):
                openrouter.check_model(model)


class PostTest(unittest.TestCase):
    def setUp(self):  # never read the developer's real .env in a test
        patcher = mock.patch("openrouter.ENV_FILE", Path(tempfile.gettempdir()) / "no-such-dir" / ".env")
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_key_from_the_env_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = Path(tmp) / ".env"
            env.write_text("# comment\nOTHER=1\nexport OPENROUTER_API_KEY=\"sk-or-file\"\n")
            with mock.patch.dict(os.environ, {}, clear=True):
                self.assertEqual(openrouter.api_key(env), "sk-or-file")
            with mock.patch.dict(os.environ, {"OPENROUTER_API_KEY": "sk-or-env"}):
                self.assertEqual(openrouter.api_key(env), "sk-or-env")  # the environment wins
            env.write_text("")
            with mock.patch.dict(os.environ, {}, clear=True), self.assertRaises(SystemExit):
                openrouter.api_key(env)

    def test_missing_key_stops_before_any_call(self):
        opener = mock.Mock()
        with mock.patch.dict(os.environ, {}, clear=True), self.assertRaises(SystemExit) as stop:
            openrouter.post("/v1/chat/completions", {}, opener=opener)
        self.assertIn("OPENROUTER_API_KEY", str(stop.exception))
        opener.assert_not_called()

    def test_retries_rate_limits_then_returns(self):
        seen, sleeps = [], []

        def opener(req, timeout):
            seen.append(req)
            if len(seen) < 3:
                raise http_error(429)
            return Response(b'{"ok": 1}')

        with mock.patch.dict(os.environ, {"OPENROUTER_API_KEY": KEY}):
            self.assertEqual(openrouter.post("/alpha/decisions", {"a": 1}, opener=opener, sleep=sleeps.append), {"ok": 1})
        self.assertEqual(len(seen), 3)
        self.assertEqual(len(sleeps), 2)
        self.assertEqual(seen[0].full_url, "https://openrouter.ai/api/alpha/decisions")
        self.assertEqual(seen[0].get_header("Authorization"), f"Bearer {KEY}")

    def test_a_client_error_is_not_retried_and_never_shows_the_key(self):
        calls = []

        def opener(req, timeout):
            calls.append(req)
            raise http_error(400, b'{"error": "bad model"}')

        with mock.patch.dict(os.environ, {"OPENROUTER_API_KEY": KEY}), self.assertRaises(RuntimeError) as err:
            openrouter.post("/v1/chat/completions", {}, opener=opener, sleep=lambda s: None)
        self.assertEqual(len(calls), 1)
        self.assertIn("400", str(err.exception))
        self.assertNotIn(KEY, str(err.exception))

    def test_gives_up_after_the_last_try(self):
        with mock.patch.dict(os.environ, {"OPENROUTER_API_KEY": KEY}), self.assertRaises(RuntimeError):
            openrouter.post("/x", {}, tries=2, opener=mock.Mock(side_effect=http_error(503)), sleep=lambda s: None)


class CallTest(unittest.TestCase):
    def test_chat_judge_gets_the_same_prompt_and_keeps_no_data(self):
        send = FakeSend({"choices": [{"message": {"content": "```json\n" + CHAT_REPLY + "\n```"}}], "usage": {"cost": 0.002}})
        out = openrouter.call_chat("the prompt", "openai/gpt-x", send=send)
        path, body = send.calls[0]
        self.assertEqual(path, "/v1/chat/completions")
        self.assertEqual(body["messages"], [{"role": "system", "content": SYSTEM}, {"role": "user", "content": "the prompt"}])
        self.assertEqual(body["provider"], {"data_collection": "deny"})
        self.assertEqual((out["sound"], out["specific"], out["weakest_point"], out["costUsd"]), (5, 1, "w", 0.002))

    def test_chat_judge_error_reply_raises(self):
        with self.assertRaises(RuntimeError):
            openrouter.call_chat("p", "openai/gpt-x", send=FakeSend({"error": {"message": "no endpoint"}}))

    def test_jev_gets_only_the_request_goal_and_answer(self):
        item = {"request": "R", "goal": "G", "answer": "A", "arm": "with", "case": "c-001", "id": "x", "regex": 1.0}
        send = FakeSend(jev_reply(2.5))
        out = openrouter.call_jev(item, "typesafe/jev-1.14", send=send)
        path, body = send.calls[0]
        self.assertEqual(path, "/alpha/decisions")
        self.assertEqual(set(body), {"model", "state", "questions"})
        self.assertEqual(body["state"], {"request": "R", "goal": "G", "answer": "A"})  # never the arm or the regex score
        self.assertEqual(set(body["questions"]), {*openrouter.RUBRIC, "meets_goal"})
        for q in body["questions"].values():
            self.assertEqual((q["type"], q["criteria"]), ("score", openrouter.LEVELS))
        self.assertEqual(out["sound"], 3.5)  # level index 2.5 -> 3.5 on 1-5
        self.assertEqual((out["weakest_point"], out["costUsd"], out["longContext"]), ("", 0.00004, False))

    def test_jev_reply_out_of_range_or_missing_raises(self):
        item = {"request": "R", "goal": "G", "answer": "A"}
        with self.assertRaises(openrouter.BilledError):
            openrouter.call_jev(item, "typesafe/jev-1.14", send=FakeSend(jev_reply(4.5)))
        reply = jev_reply()
        del reply["answers"]["specific"]
        with self.assertRaises(openrouter.BilledError):
            openrouter.call_jev(item, "typesafe/jev-1.14", send=FakeSend(reply))

    def test_a_billed_reply_that_cannot_be_read_keeps_its_cost(self):
        send = FakeSend({"choices": [{"message": {"content": "no json here"}}], "usage": {"cost": 0.003}})
        with self.assertRaises(openrouter.BilledError) as err:
            openrouter.call_chat("p", "openai/gpt-x", send=send)
        self.assertEqual(err.exception.costUsd, 0.003)
        bad = jev_reply(9.0)
        with self.assertRaises(openrouter.BilledError) as err:
            openrouter.call_jev({"request": "R", "goal": "G", "answer": "A"}, "typesafe/jev-1.14", send=FakeSend(bad))
        self.assertEqual(err.exception.costUsd, 0.00004)

        def failing(prompt, model):
            raise openrouter.BilledError("unreadable", 0.003)
        results = run_judge([{"request": "R", "goal": "G", "answer": "A"}], "openai/gpt-x", 2, 1, failing)
        self.assertEqual([r["costUsd"] for _, r in results], [0.003, 0.003])
        self.assertTrue(all("error" in r for _, r in results))

    def test_long_answers_are_flagged(self):
        self.assertTrue(openrouter.long_context({"request": "R", "goal": "G", "answer": "x" * 33_000}))
        self.assertFalse(openrouter.long_context({"request": "R", "goal": "G", "answer": "x" * 10_000}))


class JudgeMainTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        make_repo(self.root)
        patcher = mock.patch("openrouter.ENV_FILE", self.root / ".env")  # absent: never the developer's real key
        patcher.start()
        self.addCleanup(patcher.stop)

    def tearDown(self):
        self.tmp.cleanup()

    def run_main(self, *argv, call=None):
        out = io.StringIO()
        kwargs = {"call": call} if call else {}
        with contextlib.redirect_stdout(out):
            code = judge_main(["--recorded", "--passes", "1", "-j", "1", *argv], root=self.root, **kwargs)
        return code, out.getvalue()

    def test_jev_files_go_to_a_one_level_folder_and_say_what_judged(self):
        fake = FakeJev()
        code, _ = self.run_main("--model", "typesafe/jev-1.14", "skills/alpha", call=fake)
        self.assertEqual(code, 0)
        written = json.loads((self.root / "baselines/judge/typesafe--jev-1.14/alpha.json").read_text())
        self.assertEqual((written["judgeModel"], written["provider"], written["judgeKind"], written["answerSet"]),
                         ("typesafe/jev-1.14", "openrouter", "decision", "recorded"))
        self.assertEqual(len(fake.items), len(written["answers"]))
        self.assertAlmostEqual(written["answers"][0]["judge"], 0.5)  # 3 on 1-5

    def test_a_limit_trial_says_so_in_its_file(self):
        self.run_main("--model", "typesafe/jev-1.14", "--limit", "2", "skills/alpha", call=FakeJev())
        written = json.loads((self.root / "baselines/judge/typesafe--jev-1.14/alpha.json").read_text())
        self.assertEqual((written["limit"], len(written["answers"])), (2, 2))

    def test_legal_skills_are_never_judged(self):
        fake = FakeJev()
        code, printed = self.run_main("--model", "typesafe/jev-1.14", "skills/lex", call=fake)
        self.assertEqual((code, fake.items), (0, []))
        self.assertIn("lex: legal, never judged", printed)

    def test_legal_skills_are_judged_only_on_request(self):
        fake = FakeJev()
        code, _ = self.run_main("--model", "typesafe/jev-1.14", "--include-legal", "skills/lex", call=fake)
        written = json.loads((self.root / "baselines/judge/typesafe--jev-1.14/lex.json").read_text())
        self.assertEqual((code, written["legal"], len(fake.items) > 0), (0, True, True))

    def test_dry_run_needs_no_key_and_a_real_run_needs_one(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            code, printed = self.run_main("--dry-run", "--model", "typesafe/jev-1.14", "skills/alpha")
            self.assertEqual(code, 0)
            self.assertIn("calls to typesafe/jev-1.14", printed)
            with mock.patch("openrouter.post") as post, self.assertRaises(SystemExit):
                self.run_main("--model", "typesafe/jev-1.14", "skills/alpha")
            post.assert_not_called()
        self.assertFalse((self.root / "baselines/judge/typesafe--jev-1.14").exists())

    def test_an_alias_is_refused_before_any_call(self):
        with mock.patch.dict(os.environ, {"OPENROUTER_API_KEY": KEY}), mock.patch("openrouter.post") as post, self.assertRaises(SystemExit):
            self.run_main("--model", "~typesafe/jev-latest", "skills/alpha")
        post.assert_not_called()


if __name__ == "__main__":
    unittest.main()
