import logging
from pathlib import Path
import typing
import platform
import importlib.util
import shutil

log = logging.getLogger(__name__)

import nox

## Set nox options
if importlib.util.find_spec("uv"):
    nox.options.default_venv_backend = "uv|virtualenv"
else:
    nox.options.default_venv_backend = "virtualenv"
nox.options.reuse_existing_virtualenvs = True
nox.options.error_on_external_run = False
nox.options.error_on_missing_interpreters = False
# nox.options.report = True

## Get tuple of Python ver ('maj', 'min', 'mic')
PY_VER_TUPLE: tuple[str, str, str] = platform.python_version_tuple()
## Dynamically set Python version
DEFAULT_PYTHON: str = f"{PY_VER_TUPLE[0]}.{PY_VER_TUPLE[1]}"


@nox.session(name="cleanup-sandbox")
def cleanup_sandbox(session: nox.Session):
    if Path("./sandbox").exists():
        log.info("Cleaning up sandbox/")

        try:
            shutil.rmtree("./sandbox")
        except Exception as exc:
            msg = f"({type(exc)}) Error removing path 'sandbox/'. Details: {exc}"
            log.error(msg)

            return

    else:
        log.warning(f"Path sandbox/ does not exist. Creating.")

    try:
        Path("./sandbox").mkdir(parents=True, exist_ok=True)
    except Exception as exc:
        msg = f"({type(exc)}) Error creating sandbox/ directory. Details: {exc}"
        log.error(msg)


@nox.session(name="install-cookiecutter-sandbox")
def install_cookiecutter_sandbox(session: nox.Session):
    session.install("cookiecutter")

    log.info("Starting cookiecutter template render")
    answer_prompts = input("Answer project creation prompts (Y/N)? ")
    answer_prompts = answer_prompts.strip().lower()

    match answer_prompts:
        case "y" | "yes":
            session.run("cookiecutter", ".", "--output-dir=sandbox/")
        case "n" | "no":
            session.run("cookiecutter", ".", "--no-input", "--output-dir=sandbox/")
        case _:
            log.error(f"Invalid choice: {answer_prompts}. Must by 'Y' or 'N'.")

            return
