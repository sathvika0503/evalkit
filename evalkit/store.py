from sqlmodel import SQLModel, Field
from uuid import uuid4


class EvalRun(SQLModel, table=True):
    id: str = Field(
        default_factory=lambda: str(uuid4()),
        primary_key=True,
    )

    suite: str
    passed: int
    total: int