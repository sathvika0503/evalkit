from sqlmodel import Session, select

from evalkit.store import EvalRun, engine


def get_run(run_id: str):
    with Session(engine) as session:
        return session.exec(
            select(EvalRun).where(EvalRun.id == run_id)
        ).first()


def compare_runs(base_id: str, head_id: str):
    base = get_run(base_id)
    head = get_run(head_id)

    if not base:
        raise ValueError(f"Run not found: {base_id}")

    if not head:
        raise ValueError(f"Run not found: {head_id}")

    return {
        "base": base,
        "head": head,
        "score_change": head.score - base.score,
    }