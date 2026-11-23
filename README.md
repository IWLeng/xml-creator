# xml-creator

## Python syntax checks

The rules files in `libraries/` are downloaded from `main` and executed by `XML_Library_Implementation` at runtime, so a single syntax error there breaks the tool for every user. Two checks guard against this; both run the same script, [`.github/scripts/check_python_syntax.py`](.github/scripts/check_python_syntax.py), which parses every tracked `.py` file (without running it) and reports any parse errors.

### Local pre-push hook (one-time setup per clone)

Git does not install hooks automatically when you clone, so each person needs to enable it once:

1. Make sure Python 3 is installed and on your `PATH` (`python --version`).
2. From the repo root, point Git at the shared hooks folder:
   ```
   git config core.hooksPath .githooks
   ```
3. Confirm it is set:
   ```
   git config core.hooksPath
   ```
   This should print `.githooks`.

From now on, every `git push` first checks all Python files. If any file fails to parse, the push is blocked and you'll see the file, line and error, for example:

```
libraries/Hyatt/rules_library_hyatt.py:12:10: SyntaxError: '(' was never closed
    (r'\bSuite\b', r'<lang xml:lang="en-US">Suite</lang>'
             ^

pre-push: push blocked - fix the Python parse errors above (or use --no-verify).
```

Fix the error, commit, and push again. In a genuine emergency you can skip the hook with `git push --no-verify`. The GitHub Action below will still catch the error.

To run the check by hand at any time:

```
python .github/scripts/check_python_syntax.py
```

### GitHub Action (runs on GitHub)

[`.github/workflows/python-syntax-check.yml`](.github/workflows/python-syntax-check.yml) runs the same check on GitHub's servers, so errors are caught even if someone hasn't set up the local hook or used `--no-verify`.

- **When it runs:** on every push to any branch, and on every pull request (when it's opened and each time new commits are added). For a pull request from a branch in this repo, you'll therefore see it run twice, once for the push and once for the PR.
- **Where to see results:** the **Actions** tab, and the checks section at the bottom of each pull request. Parse errors are also shown as inline annotations on the affected lines in the PR's **Files changed** view.
- **What a failure means:** at least one Python file doesn't parse. Open the failed run to see which file and line.

> **Maintainers:** to stop broken code from being merged, enable branch protection on `main` (Settings → Branches) and add **Python syntax check** as a required status check.

### What the check does *not* catch

It only finds syntax/parse errors. It won't catch problems that appear only when the script runs, such as misspelled function names, missing imports, or invalid regex patterns in the rules files.
