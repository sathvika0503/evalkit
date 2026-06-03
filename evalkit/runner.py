from evalkit.schema import load_spec
from evalkit.evaluators import REGISTRY
from evalkit.providers import PROVIDERS
from evalkit.results import CaseResult
from evalkit.store import create_run


def run_suite(path: str):
    spec = load_spec(path)

    provider_cls = PROVIDERS[spec.provider]

    if spec.provider == "mock":
        provider = provider_cls()
    else:
        provider = provider_cls(spec.model)

    results = []

    for case in spec.cases:
        output = provider.generate(
            case.prompt.format(input=case.input or "")
        )

        total_assertions = len(case.assertions)
        passed_assertions = 0

        for assertion in case.assertions:
            evaluator_cls = REGISTRY[assertion.type]
            evaluator = evaluator_cls()

            result = evaluator.evaluate(
                output,
                assertion,
            )

            if result.passed:
                passed_assertions += 1

        results.append(
            CaseResult(
                case_id=case.id,
                passed=passed_assertions == total_assertions,
                total_assertions=total_assertions,
                passed_assertions=passed_assertions,
            )
        )

    passed_cases = sum(result.passed for result in results)
    total_cases = len(results)

    run = create_run(
        suite=spec.suite,
        passed=passed_cases,
        total=total_cases,
    )

    print(f"\nRun ID: {run.id}")
    print(f"Git SHA: {run.git_sha}")
    print(f"Score: {run.score:.2%}")

    return results