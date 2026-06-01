import typer
from evalkit.runner import run_eval

app = typer.Typer()


@app.command()
def run():
    run_eval("examples/summarisation.eval.yaml")


if __name__ == "__main__":
    app()