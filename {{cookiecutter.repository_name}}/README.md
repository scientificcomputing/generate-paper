# {{cookiecutter.project_name}}


# Supplementary code for the paper: {{cookiecutter.project_name}}


This repository contains supplementary code for the paper
> {{ cookiecutter.full_name }}.
> Title of paper, Journal of ..., volume, page, url

Source code is available at < https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.repository_name}}>

## Abstract
Provide the abstract of the paper

## Getting started

{%- if cookiecutter.use_docker|lower == "y" %}
We provide a pre-build Docker image which can be used to run the the code in this repository. First thing you need to do is to ensure that you have [docker installed](https://docs.docker.com/get-docker/).

To start an interactive docker container you can execute the following command

```bash
docker run --rm -it ghcr.io/{{ cookiecutter.github_username}}/{{ cookiecutter.repository_name}}:latest
```
{% endif %}

### Pre-processing
Add steps for pre-processing, ...


### Running simulation
Add steps for running simulations, ...


### Postprocessing
Add steps for postprocessing / reproducing figures and tables in the paper, ...


## Having issues
If you have any troubles please file and issue in the GitHub repository.
