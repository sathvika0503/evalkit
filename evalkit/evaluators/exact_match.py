from evalkit.evaluators.base import Evaluator, AssertionResult


class ExactMatchEvaluator(Evaluator):
    def evaluate(self, output, config):
        passed = output.strip() == str(config.value).strip()

        return AssertionResult(
            passed=passed,
            reason=f"Expected exact match: {config.value}"
        )