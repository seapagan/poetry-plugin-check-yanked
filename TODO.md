# TODO

- Add pre-commit integration - ensure it only works on changed `poetry.lock`
  files for it will be slow on large projects
- Offer to update any yanked packages to the latest version, or show a list of
  newer versions
- add option to clear the cache, either all of it or just for a specific package
- list all yanked packages in the cache
- flag to always use the cache, even if it has expired
- add defined expiry periods for the config file = "1h","1d", "1w", "1m", etc.
  Make the suffix apply to the period as well so you can have "1h", "2h",
  "3h",etc

## Taking this further

Write a non-poetry version that can be used with any project that has a
supported lock file, and a way of determining if a project is 'yanked' or not:

- `uv.lock` file
- `requirements.txt` file
- `Pipfile`
- yarn.lock
- package-lock.json
- Gemfile.lock
- cargo.lock
- etc?
