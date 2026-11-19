"""A local judge for judge_answers.py: an open-weights model served by Ollama on this machine.

Model ids start with "ollama/", e.g. ollama/qwen3.8:27b-mlx. Same prompt and rubric as the Claude and OpenRouter
judges, no API key, no cost. The model reasons before it answers (think: true), so a call takes about one to three
minutes on a laptop.

Memory: a 27-31B model takes most of a 32 GB machine. To keep it out of swap, judge_answers.py makes one call at a
time with a local judge, and this module refuses to start while another Ollama model is loaded (unload it with
`ollama stop <name>`).
"""
import json
import time
import urllib.error
import urllib.request

OLLAMA = "http://localhost:11434"
PREFIX = "ollama/"
NUM_CTX = 16_384  # the judge prompt plus a 2,000-word answer fits in about 5,000 tokens
TIMEOUT = 900


def is_local(model: str) -> bool:
    return model.startswith(PREFIX)


def name(model: str) -> str:
    return model[len(PREFIX):]


def _get(path: str, opener=urllib.request.urlopen) -> dict:
    with opener(urllib.request.Request(OLLAMA + path), timeout=30) as r:
        return json.loads(r.read().decode())


def check_ready(model: str, opener=urllib.request.urlopen) -> None:
    """The model is installed, and no other model is loaded next to it (two would push a 32 GB machine into swap)."""
    try:
        tags = {m["name"] for m in _get("/api/tags", opener)["models"]}
        loaded = [m["name"] for m in _get("/api/ps", opener).get("models", [])]
    except (urllib.error.URLError, OSError) as e:
        raise SystemExit(f"Ollama is not reachable at {OLLAMA} ({e}): start it, then rerun") from None
    if name(model) not in tags:
        raise SystemExit(f"{name(model)} is not installed in Ollama (installed: {', '.join(sorted(tags)) or 'none'})")
    others = [m for m in loaded if m != name(model)]
    if others:
        raise SystemExit(f"another model is loaded ({', '.join(others)}): run `ollama stop <name>` first, so two models "
                         "never share memory")


def call_local(prompt: str, model: str, opener=urllib.request.urlopen, tries: int = 2) -> dict:
    """One judgement: the Claude judges' prompt, the model reasons, then replies with the JSON scores."""
    from judge_answers import SYSTEM, parse_scores  # here, not at the top: judge_answers imports this module
    body = {"model": name(model), "stream": False, "think": True, "keep_alive": "10m", "options": {"num_ctx": NUM_CTX},
            "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}]}
    data = json.dumps(body).encode()
    for attempt in range(tries):
        try:
            req = urllib.request.Request(OLLAMA + "/api/chat", data=data, headers={"Content-Type": "application/json"})
            with opener(req, timeout=TIMEOUT) as r:
                reply = json.loads(r.read().decode())
            return {**parse_scores(reply["message"]["content"]), "costUsd": 0.0}
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt == tries - 1:
                raise RuntimeError(f"Ollama call failed: {e}") from None
            time.sleep(5)
