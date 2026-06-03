import typer

from evalkit.runner import run_suite
from evalkit.history import list_runs

app = typer.Typer()


@app.command()
def run(path: str):
    results = run_suite(path)

    passed = sum(r.passed for r in results)

    print("\nSummary")
    print(f"Passed: {passed}/{len(results)} cases")


@app.command()
def history():
    runs = list_runs()

    for run in runs:
        print(
            f"{run.id} | {run.suite} | {run.passed}/{run.total} | {run.score:.2%} | {run.git_sha}"
        )


if __name__ == "__main__":
    app()