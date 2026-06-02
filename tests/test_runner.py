from evalkit.runner import run_suite


def test_runner_executes():
    run_suite("examples/summarisation.eval.yaml")