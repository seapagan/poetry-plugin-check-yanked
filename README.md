# Poetry Plugin : Check for Yanked Packages <!-- omit in toc -->

This is a plugin for the [Poetry](https://python-poetry.org/) dependency
management tool that adds a new command to check if any of the dependencies in
the `pyproject.toml` file have been yanked.

- [Installation](#installation)
- [Usage](#usage)
  - [Available options](#available-options)
- [Development setup and Contributing](#development-setup-and-contributing)
  - [Task Runner](#task-runner)
  - [Linting](#linting)
  - [Pre-commit](#pre-commit)
- [License](#license)
- [Credits](#credits)

## Installation

The easiest way to install this Poetry plugin is via the `self add` command of
Poetry.

```bash
poetry self add poetry-plugin-check-yanked
```

If you used `pipx` to install Poetry you can add the plugin via the `pipx
inject` command.

```bash
pipx inject poetry poetry-plugin-check-yanked
```

Otherwise, if you used `pip` to install Poetry you can add the plugin packages
via the `pip install` command.

```bash
pip install poetry-plugin-check-yanked
```

## Usage

The plugin adds a new command to Poetry, `check-yanked`, which can be used to
check if any of the dependencies in the `pyproject.toml` file have been yanked
from PyPI by their maintainers. There is usually a pretty good reason for a
package to be yanked, so it's a good idea to check for yanked packages in your
project.

```bash
poetry check-yanked
```

The command will return a non-zero exit code if any dependencies have been
yanked along with a list of the yanked dependencies and the reason for the yank.

### Available options

- `--quiet` - Don't show any output, just return a non-zero exit code if any
  dependencies are yanked.
- `--verbose` - Show more detailed output, including each dependency and it's
  yank status.

## Development setup and Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md) for full instructions on how to set up
the project for development, and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for
the project code of conduct.

Install the dependencies using Poetry:

```console
$ poetry install
```

Then, activate the virtual environment:

```console
$ poetry shell
```

Now, you can start to code the meat of your application.

### Task Runner

The task-runner [Poe the Poet](https://poethepoet.natn.io/) is installed
as a development dependency which allows us to run simple tasks (similar to
`npm` scripts).

These are run (from within the virtual environment) using the `poe` command and
then the script name, for example:

```console
$ poe pre
```

See the [Task Runner](https://py-maker.seapagan.net/tasks/) section in the
documentation for more details and a list of available tasks.

These are defined in the `pyproject.toml` file in the `[tool.poe.tasks]`
section. Take a look at this file if you want to add or remove tasks.

### Linting

The generated project includes [Ruff](https://docs.astral.sh/ruff/) for linting
and code style formatting. [Mypy](http://mypy-lang.org/) is installed for type
checking. These are set quite strictly by default, but you can edit the tools
configuration in the `pyproject.toml` file.

### Pre-commit

There is a [pre-commit](https://pre-commit.com/) configuration provided to run
some checks on the code before it is committed.  This is a great tool to help
keep your code clean.

To install pre-commit, run the following command from inside your venv:

```console
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

## License

This project is released under the terms of the MIT license.

## Credits

The original Python boilerplate for this package was created using
[Pymaker](https://github.com/seapagan/py-maker) by [Grant
Ramsay](https://github.com/seapagan)
