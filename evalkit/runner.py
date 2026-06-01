from evalkit.schema import load_spec


def run_eval(path: str):
    spec = load_spec(path)

    print("Suite:", spec.suite)
    print("Model:", spec.model)
    print()

    for case in spec.cases:
        print("Case:", case.id)

        output = case.prompt.format(
            input=case.input or ""
        )

        print("Prompt:", output)

        passed = False

        for assertion in case.assertions:
            if assertion.type == "contains":
                if str(assertion.value) in output:
                    passed = True

        if passed:
            print("PASS")
        else:
            print("FAIL")

        print()