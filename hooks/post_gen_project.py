from pathlib import Path
import shutil

REMOVE_PATHS = [
    {%- if cookiecutter.use_pre_commit|lower != "y" %}
    '.pre-commit-config.yaml',
    '.github/workflows/pre-commit.yml'
    'cspell.config.yaml',
    ".cspell_dict.txt",
    {% endif %}
    {%- if cookiecutter.use_conda|lower != "y" %}
    'evironment.yml',
    {% endif %}
    {%- if cookiecutter.use_docker|lower != "y" %}
    'docker',
    '.github/workflows/docker-image.yml'
    {% endif %}
]


for path in REMOVE_PATHS:
    path = Path(path.strip())
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)
