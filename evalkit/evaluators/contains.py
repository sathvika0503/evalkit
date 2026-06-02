from evalkit.evaluators.base import Evaluator, AssertionResult


class ContainsEvaluator(Evaluator):
    def evaluate(self, output, config):
        passed = str(config.value) in output

        return AssertionResult(
            passed=passed,
            reason=f"Expected '{config.value}' in output"
        )