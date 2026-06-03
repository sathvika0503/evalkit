import json

from evalkit.evaluators.base import Evaluator, AssertionResult


class LLMJudgeEvaluator(Evaluator):
    def evaluate(self, output, assertion):
        score = 1.0
        reason = "Mock judge evaluation"

        passed = score >= assertion.threshold

        return AssertionResult(
            passed=passed,
            score=score,
            reason=reason,
        )