from pydantic import BaseModel
import yaml


class Assertion(BaseModel):
    type: str
    value: str | float | None = None
    rubric: str | None = None
    threshold: float = 0.7


class TestCase(BaseModel):
    id: str
    prompt: str
    input: str | None = None
    assertions: list[Assertion]


class EvalSuite(BaseModel):
    suite: str
    provider: str = "mock"
    model: str
    temperature: float = 0
    cases: list[TestCase]


def load_spec(path: str) -> EvalSuite:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return EvalSuite.model_validate(data)