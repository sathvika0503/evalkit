# EvalKit 

> A lightweight, open-source test harness for LLM outputs. Write assertions in YAML, run them in CI, and track regressions across commits.

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ECSoC 2026](https://img.shields.io/badge/ECSoC-2026-purple.svg)]()

---

## Why EvalKit?

Every team building with LLMs eventually asks:

**Did this prompt change break something?**

EvalKit helps solve that by making LLM outputs testable.

It gives:

* **YAML-based test specs** — prompts + assertions in one file
* **Multiple assertion types** — exact match, contains, regex
* **CLI runner** — run tests quickly from terminal
* **CI integration** — fail builds automatically on regression
* **Regression tracking** — compare outputs across commits
* **Multi-model support** — OpenAI, Anthropic, Gemini

---

## Quickstart

Install:

```bash
pip install evalkit
```

Create a YAML test file:

```yaml
suite: summarisation-v1
model: gpt-4o-mini

cases:
  - id: sum-001
    prompt: "Summarise in one sentence: {input}"
    input: "The Eiffel Tower was built in 1889."

    assertions:
      - type: contains
        value: "1889"
```

Run:

```bash
evalkit run examples/basic_eval.yaml
```

Example output:

```txt
Prompt: What is 2 + 2?
Expected: 4
PASS
```

---

## Installation

Python 3.10+

From source:

```bash
git clone https://github.com/sathvika0503/evalkit.git
cd evalkit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python evalkit/cli.py
```

---

## Assertion types

| Type          | Purpose                |
| ------------- | ---------------------- |
| `exact_match` | Output equals expected |
| `contains`    | Output contains value  |
| `regex`       | Match regex            |
| `json_schema` | Validate JSON          |
| `llm_judge`   | LLM scoring            |

---

## CLI commands

```bash
evalkit run examples/basic_eval.yaml
evalkit history
evalkit compare
```

---

## Project structure

```txt
evalkit/
├── evalkit/
│   ├── cli.py
│   ├── runner.py
│   ├── evaluators/
│   └── providers/
├── examples/
├── tests/
└── README.md
```

---

## Contributing

Contributions are welcome.

Ideas:

* Add new evaluators
* Improve CLI
* Add more providers
* Better reporting

---

## License

MIT

Built for **Elite Coders Summer of Code (ECSoC) 2026**
