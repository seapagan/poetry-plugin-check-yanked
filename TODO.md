# TODO

- Add pre-commit integration - ensure it only works on changed `popetry.lock`
  files for it will be slow on large projects
- Offer to update any yanked packages to the latest version, or show a list of
  newer versions
- Add caching. use `PickleDB` to store the package info locally.
