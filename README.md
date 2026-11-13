# Prompt Library

демо-реконструкция подхода на синтетических данных

36 original prompt specifications across 10 categories. Four extraction prompts include few-shot
examples with fictional assets. Each entry has an ID, semantic version, system contract and focus.
Compose a request by joining system + focus, then supplying examples and source as separate data messages.
Do not ask models to reveal hidden reasoning; require checkable evidence instead.

`npx promptfoo eval -c promptfooconfig.yaml` runs three regression cases against an installed local
Ollama model. Requires Node, promptfoo and a running model server. This live-model test was not run
in the offline package; configuration is not evidence of model performance. API key local-only is a
nonsecret local-server marker, not a credential. Change prompts with a changelog and rerun fixtures.
MIT.

## Validation coverage

`python -m unittest discover -s tests -v` verifies catalog structure, versions and the grounding of extraction examples. These are specification checks, not model evaluations. The promptfoo configuration currently exercises only the classification prompt with three cases; the other categories have no live-model regression coverage yet. Variants share a base contract and add a focus instruction; 36 entries does not mean 36 independent experiments.

Offline regression checks also run through `.github/workflows/checks.yml` on push and pull request. No model credentials are required.
