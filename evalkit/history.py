from sqlmodel import Session, select

from evalkit.store import EvalRun, engine, init_db


def list_runs():
    init_db()

    with Session(engine) as session:
        runs = session.exec(
            select(EvalRun).order_by(EvalRun.timestamp.desc())
        ).all()

    return runs