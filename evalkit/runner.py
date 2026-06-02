from evalkit.schema import load_spec
from evalkit.evaluators import REGISTRY
from evalkit.providers import PROVIDERS


def run_suite(path: str, provider_name: str = "mock"):
    spec = load_spec(path)

    print(f"\nRunning suite: {spec.suite}")
    print(f"Model: {spec.model}\n")

    provider_cls = PROVIDERS[provider_name]

    if provider_name == "openai":
        provider = provider_cls(spec.model)
    else:
        provider = provider_cls()

    total = 0
    passed = 0

    for case in spec.cases:
        print(f"Case: {case.id}")

        output = provider.generate(
            case.prompt.format(input=case.input or "")
        )

        for assertion in case.assertions:
            evaluator_cls = REGISTRY[assertion.type]
            evaluator = evaluator_cls()

            result = evaluator.evaluate(output, assertion)

            total += 1

            if result.passed:
                passed += 1

            status = "PASS" if result.passed else "FAIL"

            print(f"  [{status}] {assertion.type}")

            if result.reason:
                print(f"      {result.reason}")

    print("\nSummary")
    print(f"Passed: {passed}/{total} assertions")