from .exact_match import ExactMatchEvaluator
from .contains import ContainsEvaluator
from .regex import RegexEvaluator

REGISTRY = {
    "exact_match": ExactMatchEvaluator,
    "contains": ContainsEvaluator,
    "regex": RegexEvaluator,
}