# Larkspur roster evaluation bundles

One directory per candidate roster node. Each bundle contains the raw
measurements produced by the review panel:

- `signals.json` -- the only candidate-specific payload
- `eval_config.yaml` -- shared harness settings (identical for every bundle)
- `artifact.bin` -- shared placeholder artefact (identical for every bundle)
- `notes.txt` -- shared boilerplate (identical for every bundle)

No aggregate score or ranking is stored here. Scores are derived with the
lab's prominence rubric in `harness/prominence_rubric.py`.
