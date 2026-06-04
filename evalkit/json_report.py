import json


def write_json_report(results, output_path: str):
    data = {
        "total_cases": len(results),
        "passed_cases": sum(result.passed for result in results),
        "cases": [
            {
                "case_id": result.case_id,
                "passed": result.passed,
                "passed_assertions": result.passed_assertions,
                "total_assertions": result.total_assertions,
            }
            for result in results
        ],
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)