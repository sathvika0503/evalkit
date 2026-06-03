import subprocess


def get_git_sha() -> str | None:
    try:
        return (
            subprocess.check_output(
                ["git", "rev-parse", "--short", "HEAD"]
            )
            .decode()
            .strip()
        )
    except Exception:
        return None
