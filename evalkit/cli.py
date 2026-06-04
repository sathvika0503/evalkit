import typer

from evalkit.runner import run_suite
from evalkit.history import list_runs
from evalkit.compare import compare_runs
from evalkit.reporting import generate_html_report

app = typer.Typer()


@app.command()
def run(
    path: str,
    report: str | None = None,
):
    results = run_suite(path)

    passed = sum(r.passed for r in results)

    print("\nSummary")
    print(f"Passed: {passed}/{len(results)} cases")

    if report:
        generate_html_report(results, report)
        print(f"Report written to {report}")


@app.command()
def history():
    runs = list_runs()

    for run in runs:
        print(
            f"{run.id} | {run.suite} | {run.passed}/{run.total} | {run.score:.2%} | {run.git_sha}"
        )


@app.command()
def compare(base_id: str, head_id: str):
    result = compare_runs(base_id, head_id)

    base = result["base"]
    head = result["head"]

    print(f"Base Run : {base.id}")
    print(f"Head Run : {head.id}")
    print()

    print(
        f"Score Change: "
        f"{base.score:.2%} -> {head.score:.2%}"
    )

    print(
        f"Difference: "
        f"{result['score_change']:.2%}"
    )


if __name__ == "__main__":
    app()