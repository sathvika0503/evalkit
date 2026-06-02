from evalkit.evaluators.contains import ContainsEvaluator
from evalkit.evaluators.exact_match import ExactMatchEvaluator
from evalkit.evaluators.regex import RegexEvaluator


REGISTRY = {
    "exact_match": ExactMatchEvaluator,
    "contains": ContainsEvaluator,
    "regex": RegexEvaluator,
}