from evalkit.schema import load_spec
from evalkit.evaluators import REGISTRY
from evalkit.providers.mock import MockProvider


def run_suite(path: str):
    spec = load_spec(path)

    print(f"\nRunning suite: {spec.suite}")
    print(f"Model: {spec.model}\n")

    provider = MockProvider()

    for case in spec.cases:
        print(f"Case: {case.id}")

        output = provider.generate(
            case.prompt.format(input=case.input or "")
        )

        for assertion in case.assertions:
            evaluator_cls = REGISTRY[assertion.type]
            evaluator = evaluator_cls()

            result = evaluator.evaluate(output, assertion)

            status = "PASS" if result.passed else "FAIL"

            print(f"  [{status}] {assertion.type}")

            if result.reason:
                print(f"      {result.reason}")

    print("\nFinished.\n")