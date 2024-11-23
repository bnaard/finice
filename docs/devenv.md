# Development Environment

## Initial set-up

The following outlines the steps to set up the initial environment. This is based on the [Cookiecutter Template](https://fpgmaas.github.io/cookiecutter-uv/tutorial/), but deviates in several steps.

### 1. Install `uv`

Install `uv` according to the [official installation instructions](https://uv.readthedocs.io/en/latest/installation.html#installation). For example for MacOS and Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. New Github repository

Create a new repository on Github with the same name as this project. Give it a name that only contains alphanumeric characters and optionally -. DO NOT check any boxes under the option Initialize this repository with.

### 3. Clone repository

Go to the directory in which you would like to create the project directory for your new project and clone the repository:

```bash
git clone git@github.com:bnaard/finice.git
```

### 4. Create a temporary template project

In the same directory in which you just cloned your repository into, create a temp directory and run the following command. During the execution, you will be asked for a project name. Make sure, you assign the same project name as you named the repository you just cloned:

```bash
mkdir tmp
cd tmp
uvx cookiecutter https://github.com/fpgmaas/cookiecutter-uv.git
```

For an explanation of the prompt arguments, see the [cookiecutter-uv tutorial](https://fpgmaas.github.io/cookiecutter-uv/tutorial/).

### 5. Copy template files

Copy the contents of the template project into your project directory and clean up the tmp directory:

```bash
cd ../../finice
cp -r ../tmp/finice .
rm -fr ../tmp/finice
```

### 6. Upload project to Github

In the project directory, run:

```bash
git add .
git commit -m "init commit"
git push
```

### 7. Set Up Development Environment

To initialize the CI/CD pipeline, install the environment and the pre-commit hooks with:

```bash
uvx make install
```

This will generate the `uv.lock` file.

### 8. Run the pre-commit hooks

Run the pre-commit hooks with:

```bash
uvx pre-commit run -a
```

This will automatically format the code and check for errors.

### 9. Commit the changes

Commit the changes with:

```bash
git add .
git commit -m 'Fix formatting issues'
git push
```

### 10. Sign up to codecov.io

If you enabled code coverage with codecov for your project, you can sign up with your Github account at [Codecov](https://about.codecov.io/language/python/). Local codecoverage checks with `pytest` will work independent of your Codecov account.

### 11. Configure repository secrets

If you want to deploy your project to PyPI using the Github Actions, you will have to set some repository secrets. For instructions on how to do that, see [Publishing to PyPi](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi)

### 12. Enable documentation

To enable documentation on Github, first navigate to `Settings > Actions > General` in your repository, and under `Workflow permissions` select `Read and write permissions`.

## Available commands

The template environment provided by the `cookiecuter-uv`-template allows you to run the follwoing commands:

- `uvx make install`: Install the environment and the pre-commit hooks
- `uvx pre-commit run -a`: Run the pre-commit hooks
- `uvx make check`: Run code quality tools
- `uvx make test`: Test the code with pytest
- `uvx make build`: Build wheel file
- `uvx make clean-build`: Clean build artifacts
- `uvx make docs`: Build documentation

## Releases

### Triggering a new release

To trigger a new release, navigate to your repository on Github, click `Releases` on the right, and then select `Draft a new release`.

Give your release a title, and add a new tag in the form `*.*.*` where the `*`'s are alphanumeric. To finish, press `Publish release`.

!!! note
This project follows the rules of [semantic versioning](https://semver.org/).

### Enable documentation

Navigate to `Settings > Code and Automation > Pages`. If you succesfully created a new release, you should see a notification saying `Your site is ready to be published at https://<author_github_handle>.github.io/<project_name>/`.

To finalize deploying documentation, under `Source`, select the branch `gh-pages`.

## Virtual Environment

### Creating virtual environment

Create the virtual environment and pin Python version 3.13:

```bash
uv venv
uv python pin 3.13
```

### Installing dependencies

Install the dependencies with:

```bash
uv add nicegui
uv add typer
uv add sqlmodel
uv add --dev pytest
uv add --dev pytest-asyncio
```

### Initial project layout

The project layout starts with the recommendation from [NiceGUI's modular test-setup](https://nicegui.io/documentation/project_structure#modular). Fixtures are separately defined in `conftest.py`. After following the description, run `uv run finice.py` to start the application.

For convenience, add the following to `Makefile`:

```makefile
.PHONY: run
run: ## Run the application
    @uv run python3 finice.py
```

This allows to run `uvx make run` to start the application.

As the testing of NiceGUI needs to be `async`, add the following to `pyproject.toml`:

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

Run `uvx make test` to check that the tests pass.

Before committing changes to Github, make sure to check the follwoing lines in `pyproject.toml`:

```toml
[tool.setuptools]
py-modules = ["app"]
...
[tool.mypy]
files = ["app"]
...
[tool.coverage.run]
branch = true
source = ["app"]
```

Check, if a commit works by running the pre-commit-hooks manually:

```bash
uvx make check
```

## References

- [uv](https://uv.readthedocs.io/en/latest/)
- [Cookiecutter Template](https://fpgmaas.github.io/cookiecutter-uv/tutorial/)
- [NiceGUI modular project structure](https://nicegui.io/documentation/project_structure#modular)
