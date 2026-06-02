import re

from evalkit.evaluators.base import (
    AssertionResult,
    Evaluator,
)


class RegexEvaluator(Evaluator):
    def evaluate(self, output, config):
        passed = bool(
            re.search(
                str(config.value),
                output,
            )
        )

        return AssertionResult(
            passed=passed
        )