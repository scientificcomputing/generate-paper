
import os

REMOVE_PATHS = [
    {%- if cookiecutter.use_pre_commit|lower != "y" %}
    '.pre-commit-config.yaml',
    '.github/workflows/pre-commit.yml'
    {% endif %}
]


for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
