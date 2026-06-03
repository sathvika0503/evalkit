import typer

from evalkit.runner import run_suite

app = typer.Typer()


@app.command()
def run(path: str):
    results = run_suite(path)

    passed = sum(r.passed for r in results)

    print("\nSummary")
    print(f"Passed: {passed}/{len(results)} cases")


if __name__ == "__main__":
    app()