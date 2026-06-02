from evalkit.runner import run_suite


def test_suite_summary():
    results = run_suite(
        "examples/summarisation.eval.yaml"
    )

    passed = sum(r.passed for r in results)

    assert passed == 1
    assert len(results) == 1