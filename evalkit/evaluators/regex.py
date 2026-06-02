import re

from evalkit.evaluators.base import Evaluator, AssertionResult


class RegexEvaluator(Evaluator):
    def evaluate(self, output, config):
        passed = bool(re.search(str(config.value), output))

        return AssertionResult(
            passed=passed,
            reason=f"Regex pattern: {config.value}"
        )