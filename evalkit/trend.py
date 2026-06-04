from sqlmodel import Session, select

from evalkit.store import EvalRun, engine, init_db


def get_recent_runs(limit: int = 10):
    init_db()

    with Session(engine) as session:
        runs = session.exec(
            select(EvalRun).order_by(EvalRun.timestamp.desc())
        ).all()

    return runs[:limit]