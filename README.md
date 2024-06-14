# Poetry Plugin : Check for Yanked Packages <!-- omit in toc -->

This is a plugin for the [Poetry](https://python-poetry.org/) dependency
management tool that adds a new command to check if any of the dependencies in
the `pyproject.toml` file have been yanked.

This plugin was written to learn how to write a Poetry plugin and to scratch an
itch I had for a tool like this. I have more [ideas](TODO.md) for features and
improvements, and I welcome any [contributions](CONTRIBUTING.md) or suggestions.

- [Installation](#installation)
- [Usage](#usage)
  - [Available options](#available-options)
  - [Configuration](#configuration)
- [Development setup and Contributing](#development-setup-and-contributing)
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

When you check for yanked packages, the plugin will download the latest
metadata for each package in the `poetry.lock` file and check if any of them are
yanked. If any are found, the command will return a non-zero exit code and list
the yanked packages along with the reason for the yank. Once a specific package
verison has been checked, it will be cached for a period of time (default 1 day)
to minimize the number of requests to PyPI (and speed up future runs).

> [!NOTE]
> This plugin uses the `poetry.lock` file to determine the exact versions of
> the dependencies to check, so it will also check for any yanked dependencies
> of the dependencies you have specified in the `pyproject.toml` file.

```bash
poetry check-yanked
```

The command will return a non-zero exit code if any dependencies have been
yanked along with a list of the yanked dependencies and the reason for the yank.

### Available options

- `--full` - Check each project dependency package again, even if it is already
  in the cache.
- `--refresh` - Refesh the entire cache and exit, no not check for yanked
  packages.
- `--quiet` - Don't show any output, just return a non-zero exit code if any
  dependencies are yanked.
- `--verbose` - Show more detailed output, including each dependency and it's
  yank status.

### Configuration

At this time, the only configuration option is the cache timeout, which is set
to 1 day by default. This can be changed by adding a `[tool.check-yanked]`
section to the `pyproject.toml` file with a `cache_expiry` key. This value is
in seconds. and the default is 86400 (1 day). Future versions of the plugin will
offer pre-defined cache times (e.g. 1 hour, 1 day, 1 week, etc.) as well as the
ability to disable the cache entirely.

```toml
[tool.check-yanked]
cache_expiry = 3600 # 1 hour
```

## Development setup and Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md) for full instructions on how to set up
the project for development, and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for
the project code of conduct.

## License

This project is released under the terms of the MIT license.

## Credits

The original Python boilerplate for this package was created using
[Pymaker](https://github.com/seapagan/py-maker) by [Grant
Ramsay](https://github.com/seapagan)
