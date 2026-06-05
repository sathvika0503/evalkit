# EvalKit

Lightweight LLM evaluation framework for testing prompts, models, and AI systems using YAML-defined test suites.

---

## Features

### Evaluation Framework

* YAML-based evaluation suites
* Exact Match evaluator
* Contains evaluator
* Regex evaluator
* LLM-as-a-Judge evaluator

### Providers

* Mock provider
* OpenAI provider
* OpenRouter provider

### Reporting

* Rich terminal output
* HTML reports
* JSON reports

### Run Tracking

* SQLite-backed run history
* Git SHA tracking
* Run comparison
* Trend analysis

### CI/CD

* GitHub Actions integration
* Failing evaluations return non-zero exit codes
* Automated testing on push and pull request

---

## Installation

```bash
pip install -e .
```

---

## Quick Start

Run an evaluation suite:

```bash
evalkit run examples/summarisation.eval.yaml
```

Generate an HTML report:

```bash
evalkit run examples/summarisation.eval.yaml --report report.html
```

Generate a JSON report:

```bash
evalkit run examples/summarisation.eval.yaml --json results.json
```

View run history:

```bash
evalkit history
```

Compare two runs:

```bash
evalkit compare RUN_ID_1 RUN_ID_2
```

---

## Example Evaluation Suite

```yaml
suite: summarisation-v1
provider: mock
model: mock

cases:
  - id: sum-001
    prompt: "Summarise: {input}"
    input: "The Eiffel Tower..."
    assertions:
      - type: contains
        value: "1889"
```

---

## Architecture

```text
YAML Suite
    ↓
Provider
    ↓
Model Output
    ↓
Evaluators
    ↓
SQLite Storage
    ↓
Reports
```

---

## Example Outputs

### Evaluation Results

Rich terminal output showing pass/fail status for every test case.

### Run History

Track previous evaluation runs and associated Git commits.

### Run Comparison

Compare evaluation performance across different runs.

### HTML Reports

Generate shareable evaluation reports.

---

## CI/CD

GitHub Actions automatically runs:

* Unit tests
* Evaluation suites
* Regression checks

on every push and pull request.

---

## Roadmap

### Completed

* YAML evaluation suites
* Multiple evaluators
* SQLite storage
* HTML reports
* JSON reports
* GitHub Actions CI
* Run comparison
* Trend tracking

### Planned

* Multi-model benchmarking
* Interactive dashboards
* Visualization charts
* Additional model providers
* PyPI release

---

## License

MIT License
