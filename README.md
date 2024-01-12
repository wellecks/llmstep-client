# `llmstep`: [L]LM proofstep suggestions in Lean

`llmstep` is a Lean 4 tactic for suggesting proof steps using a language model.

## Use `llmstep` in a project
1. In `lakefile.lean`:
```lean
require llmstep from git
  "https://github.com/wellecks/llmstep-client"
```

2. Set `LLMSTEP_HOST` and `LLMSTEP_PORT` environment variables in VS Code.

Run `lake update` and `lake build`. Then `import LLMstep` in a file and call the tactic (e.g., `llmstep ""`).


#### Citation

Paper: [[paper](https://mathai2023.github.io/papers/40.pdf)]

Please cite:
```
@article{welleck2023llmstep,
    title={LLMSTEP: LLM proofstep suggestions in Lean},
    author={Sean Welleck and Rahul Saha},
    journal={arXiv preprint arXiv:2310.18457},
    year={2023}
}
```
