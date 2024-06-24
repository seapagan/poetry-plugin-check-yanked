# GitHub Action

There is now also a GitHub Action for this plugin that can be run for all pull-requests to ensure that all dependencies are up-to-date and not yanked.

See the repository for the
[check-yanked-packages](https://github.com/seapagan/check-yanked-packages){:target="_blank"}
action for full details.

This action is a simple wrapper around the `check-yanked` command provided by
this plugin. It will run the `check-yanked` command and fail the build if any
yanked packages are found.

```yaml
name: Check for Yanked Packages

on: [push, pull_request]

jobs:
  check-yanked:
    runs-on: ubuntu-latest

    steps:
      - name: Run poetry check-yanked
        uses: seapagan/check-yanked-packages@v1
```

It can also be added to an existing workflow like this:

```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      # other steps...

      - name: Run poetry check-yanked
        uses: seapagan/check-yanked-packages@v1
```

If you run the `actions/setup-python` and/or `actions/checkout` actions before
this action, it will use the version of Python installed by that action and the
`poetry.lock` file in the root of the repository by default. It will not try to
install Python or checkout the repository again. Convereley, if you do not run
those actions, it will automatically run them for you.

## Options

There are currently two options available for this action:

- `path` - The path to the directory containing the `poetry.lock` file. This
  defaults to the root of the repository.
- `python-version` - The version of Python to use when running the action. This
  defaults to the latest version of Python 3.x available on the runner.

!!! note

    If you are using the `actions/setup-python` action manually, the
    `python-version` for **this** action will be **ignored**, and the version of
    Python installed by `actions/setup-python` will be used instead.

These are both optional, and can be set in the workflow file like so:

```yaml
- name: Run poetry check-yanked
  uses: seapagan/check-yanked-packages@v1
  with:
    python-version: '3.10'
    path: 'path/to/directory'
```
