import yaml

def run_eval(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    prompt = data["prompt"]
    expected = data["expected"]

    print("Prompt:", prompt)
    print("Expected:", expected)

    if expected == "4":
        print("PASS")
    else:
        print("FAIL")