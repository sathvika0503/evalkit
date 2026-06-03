from evalkit.schema import Assertion
from evalkit.evaluators.llm_judge import LLMJudgeEvaluator


def test_llm_judge():
    evaluator = LLMJudgeEvaluator()

    assertion = Assertion(
        type="llm_judge",
        rubric="Answer should be helpful",
        threshold=0.7,
    )

    result = evaluator.evaluate(
        "This is a helpful answer.",
        assertion,
    )

    assert result.passed is True
    assert result.score == 1.0