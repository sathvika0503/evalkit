from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from sqlmodel import Field, Session, SQLModel, create_engine

from evalkit.git_utils import get_git_sha


engine = create_engine("sqlite:///evalkit.db")


class EvalRun(SQLModel, table=True):
    id: str = Field(
        default_factory=lambda: str(uuid4()),
        primary_key=True,
    )

    suite: str
    passed: int
    total: int
    timestamp: str
    git_sha: Optional[str] = None
    score: float = 0.0


def init_db():
    SQLModel.metadata.create_all(engine)


def create_run(suite: str, passed: int, total: int) -> EvalRun:
    init_db()

    score = passed / total if total else 0.0

    run = EvalRun(
        suite=suite,
        passed=passed,
        total=total,
        timestamp=datetime.now(timezone.utc).isoformat(),
        git_sha=get_git_sha(),
        score=score,
    )

    with Session(engine) as session:
        session.add(run)
        session.commit()
        session.refresh(run)

    return run