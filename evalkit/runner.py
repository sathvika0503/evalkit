from evalkit.schema import load_spec
from evalkit.evaluators import REGISTRY


def run_suite(path: str):
    spec = load_spec(path)

    print(f"\nRunning suite: {spec.suite}")
    print(f"Model: {spec.model}\n")

    for case in spec.cases:
        print(f"Case: {case.id}")

        # temporary mock output
        output = "The Eiffel Tower was completed in 1889."

        for assertion in case.assertions:
            evaluator_cls = REGISTRY[assertion.type]
            evaluator = evaluator_cls()

            result = evaluator.evaluate(output, assertion)

            status = "PASS" if result.passed else "FAIL"
            print(f"  [{status}] {assertion.type}")

    print("\nFinished.\n")