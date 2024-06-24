# Check for yanked packages in your Poetry project

This is a simple plugin for the [Poetry](https://python-poetry.org/) dependency
management tool.

This plugin adds a new command to Poetry, `check-yanked`, which can be used to
check if any of the dependencies in the project lock file `poetry.lock` have
been yanked from PyPI by their maintainers. There is usually a pretty good
reason for a package to be yanked, so it's a good idea to check for yanked
packages in your project.

It will download the latest metadata for each package in the `poetry.lock` file
and cache it for a period of time (default 1 day) to minimize the number of
requests to PyPI (and speed up future runs).

!!! note

    Since this plugin uses the `poetry.lock` file to determine the exact
    versions of the dependencies to check, it will also check for any yanked
    dependencies of your project dependencies specified in the `pyproject.toml`
    file.

This plugin could be added to a pre-commit hook to check for yanked packages
before running any other checks or tests.
!!! tip

    There is also a GitHub Action for this plugin that can be run automatically
    to ensure that all dependencies are up-to-date and not yanked.

This plugin was written to learn how to write a Poetry plugin and to scratch an
itch I had for a tool like this. I have more [ideas](todo.md) for features and
improvements, and I welcome any [contributions](contributing.md) or suggestions.
