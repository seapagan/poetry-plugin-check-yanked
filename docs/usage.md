# Usage

Usage is pretty simple. Just run the `check-yanked` command from the root of
your project. The plugin will download the latest metadata for each package in
the `poetry.lock` file and check if any of them are yanked. If any are found,
the command will return a non-zero exit code and list the yanked packages along
with the reason for the yank. Once a specific package version has been checked,
it will be cached for a period of time (default 1 day though this can be
configured).

```bash
poetry check-yanked
```

The command will return a non-zero exit code if any dependencies have been
yanked along with a list of the yanked dependencies and the reason for the yank.

## Available options

- `--full` - Check each project dependency package again, even if it is already
  in the cache.
- `--refresh` - Refesh the entire cache and exit, no not check for yanked
  packages.
- `--quiet` - Don't show any output, just return a non-zero exit code if any
  dependencies are yanked.
- `--verbose` - Show more detailed output, including each dependency and it's
  yank status.

## Configuration

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
