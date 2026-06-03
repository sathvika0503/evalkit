from .exact_match import ExactMatchEvaluator
from .contains import ContainsEvaluator
from .regex import RegexEvaluator
from .llm_judge import LLMJudgeEvaluator

REGISTRY = {
    "exact_match": ExactMatchEvaluator,
    "contains": ContainsEvaluator,
    "regex": RegexEvaluator,
    "llm_judge": LLMJudgeEvaluator,
}