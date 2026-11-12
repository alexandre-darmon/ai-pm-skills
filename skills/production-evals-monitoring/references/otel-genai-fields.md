# Trace fields for online evals (OpenTelemetry GenAI)

What a production trace must carry so that evaluators can score it and a quality drop can be traced to a cause. Names checked on 2026-11-09 in the OpenTelemetry GenAI semantic conventions, which now live in their own repository (github.com/open-telemetry/semantic-conventions-genai). Every attribute below has **Development** status: names can still change, so the plan pins the convention version it follows.

## Standard attributes and events

| Need | Field | Note |
| --- | --- | --- |
| Which model was asked, which one answered | `gen_ai.request.model`, `gen_ai.response.model` | Alert when the answering model's value changes: a silent provider update shows here first |
| Provider | `gen_ai.provider.name` | |
| What the span does | `gen_ai.operation.name` | well-known values include `chat`, `retrieval`, `embeddings`, `execute_tool`, `invoke_agent` |
| Prompt template | `gen_ai.prompt.name`, `gen_ai.prompt.version` | ties a quality change to a prompt release |
| Conversation | `gen_ai.conversation.id` | joins turns, the outcome event and the evaluation results |
| Agent | `gen_ai.agent.name`, `gen_ai.agent.version` | |
| Retrieval | `gen_ai.data_source.id`, `gen_ai.retrieval.documents` (ids and scores, opt-in), `gen_ai.retrieval.query.text` (opt-in) | lets a faithfulness judge see what the model was given; ties failures to a knowledge base |
| Tools | `gen_ai.tool.name`, `gen_ai.tool.call.id`, `gen_ai.tool.call.arguments` and `gen_ai.tool.call.result` (opt-in), `error.type` | tool error rate is a 100% deterministic check |
| Tokens | `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens` | cost, owned by `assistant-kpis-cost-per-outcome` |
| End of generation | `gen_ai.response.id`, `gen_ai.response.finish_reasons` | truncation shows as a finish reason |
| Content | `gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions` | opt-in content capture (`OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT`); the conventions treat it as sensitive and allow storing it outside the trace by reference |
| Evaluation result | event `gen_ai.evaluation.result`: `gen_ai.evaluation.name` (required), `gen_ai.evaluation.score.value`, `gen_ai.evaluation.score.label`, `gen_ai.evaluation.explanation`, `error.type` | parented to the span it judges, or carries `gen_ai.response.id` when the span id is not available |

## Custom attributes (no convention at verification)

Put them in your own namespace (e.g. `app.`), documented in the plan:

- question class and the classifier and taxonomy versions (`conversation-analysis`);
- knowledge-base snapshot id;
- evaluator version: judge model, rubric version, pass threshold. Without it, a judge change looks like a quality change;
- sample stratum: random-by-class or oversample (low confidence, escalation, thumbs-down, new request). Only the random stratum feeds a class rate;
- masking version and whether the evaluated text was masked;
- the outcome event (`outcome_id`, `result`, ...), owned by `assistant-kpis-cost-per-outcome`.

## AI Act link

For a high-risk system, art. 12(2) asks logs to record events relevant to identifying risks and substantial modifications, to post-market monitoring (art. 72) and to deployer monitoring (art. 26(5)). These fields are the plan's answer; counsel says whether they suffice.
