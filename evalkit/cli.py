import typer
import yaml

app = typer.Typer()

@app.command()
def run():
    with open("examples/basic_eval.yaml", "r") as file:
        data = yaml.safe_load(file)

    print("Prompt:", data["prompt"])
    print("Expected:", data["expected"])

    if data["expected"] == "4":
        print("PASS")
    else:
        print("FAIL")

if __name__ == "__main__":
    app()