def generate_html_report(results, output_path: str):
    passed = sum(result.passed for result in results)
    total = len(results)

    rows = ""

    for result in results:
        status = "PASS" if result.passed else "FAIL"

        rows += f"""
        <tr>
            <td>{result.case_id}</td>
            <td>{status}</td>
            <td>{result.passed_assertions}/{result.total_assertions}</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>EvalKit Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}

            th {{
                background-color: #f4f4f4;
            }}
        </style>
    </head>
    <body>
        <h1>EvalKit Report</h1>
        <p><strong>Passed:</strong> {passed}/{total} cases</p>

        <table>
            <thead>
                <tr>
                    <th>Case ID</th>
                    <th>Status</th>
                    <th>Assertions</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html)