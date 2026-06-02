from abc import ABC, abstractmethod
from dataclasses import dataclass

from evalkit.schema import Assertion


@dataclass
class AssertionResult:
    passed: bool
    score: float | None = None
    reason: str | None = None


class Evaluator(ABC):
    @abstractmethod
    def evaluate(
        self,
        output: str,
        config: Assertion,
    ) -> AssertionResult:
        pass