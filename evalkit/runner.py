from evalkit.schema import load_spec
from evalkit.evaluators import REGISTRY
from evalkit.providers.mock import MockProvider
from evalkit.results import CaseResult


def run_suite(path: str):
    spec = load_spec(path)

    print(f"\nRunning suite: {spec.suite}")
    print(f"Model: {spec.model}\n")

    provider = MockProvider()

    results = []

    for case in spec.cases:
        print(f"Case: {case.id}")

        output = provider.generate(
            case.prompt.format(input=case.input or "")
        )

        passed_assertions = 0
        total_assertions = len(case.assertions)

        for assertion in case.assertions:
            evaluator_cls = REGISTRY[assertion.type]
            evaluator = evaluator_cls()

            result = evaluator.evaluate(output, assertion)

            status = "PASS" if result.passed else "FAIL"

            print(f"  [{status}] {assertion.type}")

            if result.reason:
                print(f"      {result.reason}")

            if result.passed:
                passed_assertions += 1

        case_result = CaseResult(
            case_id=case.id,
            passed=passed_assertions == total_assertions,
            total_assertions=total_assertions,
            passed_assertions=passed_assertions,
        )

        results.append(case_result)

    print("\nFinished.\n")
    passed_cases = sum(r.passed for r in results)
    print("Summary")
    print(f"Passed: {passed_cases}/{len(results)} cases")

    return results