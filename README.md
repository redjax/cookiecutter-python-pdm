# Python + PDM Cookiecutter

A Python cookiecutter template using [pdm](https://pdm-project.org) for dependency & project management.

## Usage

### With cookiecutter cli

#### + From a location on the file system

(Example:  `c:\git\cookiecutter-templates\cookiecutter-python-pdm`):

```shell
cookiecutter c:\git\cookiecutter-templates\cookiecutter-python-pdm --output-dir=some/path/to/project
```

#### + Skip cookiecutter creation prompts

Skip prompts & render template using defaults defined in [`cookiecutter.json`](./cookiecutter.json):

```shell
cookiecutter c:\git\cookiecutter-templates\cookiecutter-python-pdm --no-input
```

#### + Install from a git(hub) repository

```shell
cookiecutter gh:<user>/cookiecutter-python-pdm

## OR
cookiecutter https://github.com/<user>/cookiecutter-python-pdm
```

### With nox

The included [`noxfile.py`](./noxfile.py) has sessions for running cookiecutter commands.

#### + Guided prompt to create new project from cookiecutter template

```shell
nox -s new-cookiecutter-project
```

#### + Install cookiecutter template in local `./sandbox/` directory:

```shell
nox -s install-cookiecutter-sandbox
```

#### + Cleanup (delete & recreate) the `./sandbox/` directory:

```shell
nox -s cleanup-sandbox
```

