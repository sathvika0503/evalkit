import typer
from rich.console import Console
from rich.table import Table

from evalkit.runner import run_suite
from evalkit.history import list_runs
from evalkit.compare import compare_runs
from evalkit.reporting import generate_html_report

app = typer.Typer()
console = Console()


@app.command()
def run(
    path: str,
    report: str | None = None,
):
    results = run_suite(path)

    table = Table(title="EvalKit Results")
    table.add_column("Case ID")
    table.add_column("Status")
    table.add_column("Assertions")

    for result in results:
        status = "[green]PASS[/green]" if result.passed else "[red]FAIL[/red]"

        table.add_row(
            result.case_id,
            status,
            f"{result.passed_assertions}/{result.total_assertions}",
        )

    console.print(table)

    passed = sum(r.passed for r in results)

    console.print()
    console.print(f"[bold]Summary[/bold]")
    console.print(f"Passed: [green]{passed}[/green]/{len(results)} cases")

    if report:
        generate_html_report(results, report)
        console.print(f"[green]Report written to {report}[/green]")


@app.command()
def history():
    runs = list_runs()

    table = Table(title="EvalKit Run History")
    table.add_column("Run ID")
    table.add_column("Suite")
    table.add_column("Passed")
    table.add_column("Score")
    table.add_column("Git SHA")

    for run in runs:
        table.add_row(
            run.id,
            run.suite,
            f"{run.passed}/{run.total}",
            f"{run.score:.2%}",
            str(run.git_sha),
        )

    console.print(table)


@app.command()
def compare(base_id: str, head_id: str):
    result = compare_runs(base_id, head_id)

    base = result["base"]
    head = result["head"]

    table = Table(title="EvalKit Run Comparison")
    table.add_column("Metric")
    table.add_column("Base")
    table.add_column("Head")

    table.add_row("Run ID", base.id, head.id)
    table.add_row("Suite", base.suite, head.suite)
    table.add_row("Score", f"{base.score:.2%}", f"{head.score:.2%}")
    table.add_row("Git SHA", str(base.git_sha), str(head.git_sha))

    console.print(table)

    diff = result["score_change"]
    color = "green" if diff >= 0 else "red"

    console.print()
    console.print(f"Difference: [{color}]{diff:.2%}[/{color}]")


if __name__ == "__main__":
    app()