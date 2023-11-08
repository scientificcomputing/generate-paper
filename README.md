# Template repository for Papers

Repository using [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) for project templates.

## Installation
To use this repository, you need to install cookiecutter. This can be done with `pip`
```bash
python3 -m pip install cookiecutter
```
For other installation options, see: [Cookiecutter installation](https://cookiecutter.readthedocs.io/en/stable/installation.html)

You also need to have `git` installed on your system, see:
[Download git](https://git-scm.com/downloads) for more information.

## Usage
To use this repository with cookiecutter you can call:
```bash
cookiecutter gh:scientificcomputing/generate-paper
```
and fill out the list of options.

# Options for cookiecutter
The following options are available when using the cookiecutter:

1. __Full Name__: Used in LICENSE and CITATION.cff.
2. __github\_username__: Will be used to to generate links to the documentation
3. __project\_name__: Used as header of documentation and in CITATION.cff
4. __repository\_name__: Name of the repository
5. __version__: The initial version of the software.
6. __open\_source\_license__: Choose a open source license for your code
7. __use_pre_commit__: Set up [pre-commit hooks](https://pre-commit.com) that will run some checks
8. __require_fenics__: Does your paper require FEniCS?
9. __require_fenicsx__: Does your paper require FEniCSx?
