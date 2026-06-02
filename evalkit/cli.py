import typer
from evalkit.runner import run_suite

app = typer.Typer()

@app.command()
def run(path: str):
    run_suite(path)

if __name__ == "__main__":
    app()