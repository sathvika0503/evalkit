import typer
from evalkit.runner import run_suite

app = typer.Typer()


@app.command()
def run():
    run_suite("examples/summarisation.eval.yaml")


if __name__ == "__main__":
    app()