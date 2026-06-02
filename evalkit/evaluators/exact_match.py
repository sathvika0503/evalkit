from evalkit.evaluators.base import (
    AssertionResult,
    Evaluator,
)


class ExactMatchEvaluator(Evaluator):
    def evaluate(self, output, config):
        passed = output.strip() == str(config.value).strip()

        return AssertionResult(
            passed=passed
        )