from evalkit.evaluators.base import (
    AssertionResult,
    Evaluator,
)


class ContainsEvaluator(Evaluator):
    def evaluate(self, output, config):
        passed = str(config.value) in output

        return AssertionResult(
            passed=passed
        )