from evalkit.schema import Assertion

from evalkit.evaluators.contains import ContainsEvaluator
from evalkit.evaluators.exact_match import ExactMatchEvaluator
from evalkit.evaluators.regex import RegexEvaluator


def test_exact_match():
    evaluator = ExactMatchEvaluator()

    result = evaluator.evaluate(
        "Paris",
        Assertion(
            type="exact_match",
            value="Paris",
        ),
    )

    assert result.passed is True


def test_contains():
    evaluator = ContainsEvaluator()

    result = evaluator.evaluate(
        "The Eiffel Tower was completed in 1889",
        Assertion(
            type="contains",
            value="1889",
        ),
    )

    assert result.passed is True


def test_regex():
    evaluator = RegexEvaluator()

    result = evaluator.evaluate(
        "Year: 1889",
        Assertion(
            type="regex",
            value=r"\d{4}",
        ),
    )

    assert result.passed is True