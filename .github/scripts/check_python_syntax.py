"""Fail if any tracked Python file in the repo has a syntax/parse error.

Used by both the GitHub Actions workflow and the local pre-push hook.
Exit code 0 = all files parse, 1 = at least one file failed.
"""
import ast
import os
import subprocess
import sys
from pathlib import Path

IN_ACTIONS = os.environ.get("GITHUB_ACTIONS") == "true"


def tracked_python_files(repo_root: Path) -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "*.py"],
        cwd=repo_root, capture_output=True, text=True, check=True,
    ).stdout
    return [repo_root / line for line in out.splitlines() if line.strip()]


def main() -> int:
    repo_root = Path(
        subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    )

    files = tracked_python_files(repo_root)
    errors = 0
    for path in files:
        rel = path.relative_to(repo_root).as_posix()
        try:
            source = path.read_bytes()
            ast.parse(source, filename=rel)
        except SyntaxError as e:
            errors += 1
            print(f"{rel}:{e.lineno}:{e.offset}: {e.__class__.__name__}: {e.msg}")
            if e.text:
                print(f"    {e.text.rstrip()}")
                if e.offset:
                    print(f"    {' ' * (e.offset - 1)}^")
            if IN_ACTIONS:  # inline annotation on the PR diff
                print(f"::error file={rel},line={e.lineno or 1},col={e.offset or 1}::{e.msg}")
        except (UnicodeDecodeError, ValueError) as e:
            errors += 1
            print(f"{rel}: could not parse: {e}")
            if IN_ACTIONS:
                print(f"::error file={rel}::{e}")

    if errors:
        print(f"\n{errors} of {len(files)} Python file(s) failed to parse.")
        return 1
    print(f"All {len(files)} Python file(s) parse OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
