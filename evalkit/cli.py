import typer

app = typer.Typer()

@app.command()
def hello():
    print("EvalKit running")

if __name__ == "__main__":
    app()