# Installation

This is a [Poetry](https://python-poetry.org/){:target="_blank"} plugin so it
needs to be installed via Poetry. If you haven't already installed Poetry, you
can find instructions on how to do so in the [Poetry
documentation](https://python-poetry.org/docs/#installation){:target="_blank"}.

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
