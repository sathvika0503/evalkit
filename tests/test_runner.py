from evalkit.runner import run_suite


def test_runner_returns_results():
    results = run_suite(
        "examples/summarisation.eval.yaml"
    )

    assert len(results) == 1
    assert results[0].passed is True