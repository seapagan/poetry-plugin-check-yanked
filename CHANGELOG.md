# Changelog

This is an auto-generated log of all the changes that have been made to the
project since the first release, with the latest changes at the top.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased](https://github.com/seapagan/poetry-plugin-check-yanked/tree/HEAD)


These are the changes that have been merged to the repository since the last
release. If you want to try out these changes, you can install the latest
version from the main branch by running:

```console
$ pip install git+https://github.com/seapagan/github-changelog-md
```

or, if using poetry:

```console
$ poetry add git+https://github.com/seapagan/github-changelog-md
```
Everything in this section will be included in the next official release.


**Merged Pull Requests**

- Fix some lint issues ([#26](https://github.com/seapagan/poetry-plugin-check-yanked/pull/26)) by [seapagan](https://github.com/seapagan)

[`Full Changelog`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.3.0...HEAD) | [`Diff`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.3.0...HEAD.diff) | [`Patch`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.3.0...HEAD.patch)

## [v0.3.0](https://github.com/seapagan/poetry-plugin-check-yanked/releases/tag/v0.3.0) (June 24, 2024)

**New Features**

- Catch missing `poetry.lock` file ([#22](https://github.com/seapagan/poetry-plugin-check-yanked/pull/22)) by [seapagan](https://github.com/seapagan)
- Add an option to hide the progress bar while still showing other output ([#21](https://github.com/seapagan/poetry-plugin-check-yanked/pull/21)) by [seapagan](https://github.com/seapagan)
- Add a GitHub action configuration ([#19](https://github.com/seapagan/poetry-plugin-check-yanked/pull/19)) by [seapagan](https://github.com/seapagan)

**Documentation**

- Document the GitHub Action functionality ([#20](https://github.com/seapagan/poetry-plugin-check-yanked/pull/20)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump types-requests from 2.32.0.20240602 to 2.32.0.20240622 ([#18](https://github.com/seapagan/poetry-plugin-check-yanked/pull/18)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump ruff from 0.4.9 to 0.4.10 ([#17](https://github.com/seapagan/poetry-plugin-check-yanked/pull/17)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump faker from 25.8.0 to 25.9.1 ([#16](https://github.com/seapagan/poetry-plugin-check-yanked/pull/16)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump github-changelog-md from 0.9.3 to 0.9.4 ([#15](https://github.com/seapagan/poetry-plugin-check-yanked/pull/15)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.2.2...v0.3.0) | [`Diff`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.2.2...v0.3.0.diff) | [`Patch`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.2.2...v0.3.0.patch)

## [v0.2.2](https://github.com/seapagan/poetry-plugin-check-yanked/releases/tag/v0.2.2) (June 18, 2024)


**Security Update**

- Updates `urllib3` to fix a MODERATE severity security issue.


**Dependency Updates**

- Bump urllib3 from 2.2.1 to 2.2.2 ([#13](https://github.com/seapagan/poetry-plugin-check-yanked/pull/13)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.2.1...v0.2.2) | [`Diff`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.2.1...v0.2.2.diff) | [`Patch`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.2.1...v0.2.2.patch)

## [v0.2.1](https://github.com/seapagan/poetry-plugin-check-yanked/releases/tag/v0.2.1) (June 17, 2024)

**Bug Fixes**

- Fix plugin description spanning lines ([#11](https://github.com/seapagan/poetry-plugin-check-yanked/pull/11)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump mkdocs-material from 9.5.26 to 9.5.27 ([#10](https://github.com/seapagan/poetry-plugin-check-yanked/pull/10)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump ruff from 0.4.8 to 0.4.9 ([#9](https://github.com/seapagan/poetry-plugin-check-yanked/pull/9)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.2.0...v0.2.1) | [`Diff`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.2.0...v0.2.1.diff) | [`Patch`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.2.0...v0.2.1.patch)

## [v0.2.0](https://github.com/seapagan/poetry-plugin-check-yanked/releases/tag/v0.2.0) (June 14, 2024)

**New Features**

- Implement caching to store the yanked status of already checked libraries. ([#6](https://github.com/seapagan/poetry-plugin-check-yanked/pull/6)) by [seapagan](https://github.com/seapagan)

**Documentation**

- Add a basic documentation site ([#7](https://github.com/seapagan/poetry-plugin-check-yanked/pull/7)) by [seapagan](https://github.com/seapagan)

[`Full Changelog`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.1.1...v0.2.0) | [`Diff`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.1.1...v0.2.0.diff) | [`Patch`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.1.1...v0.2.0.patch)

## [v0.1.1](https://github.com/seapagan/poetry-plugin-check-yanked/releases/tag/v0.1.1) (June 11, 2024)

A quick release to lower the required version of Poetry to 1.6.0 and add PyPI trove classifiers
[`Full Changelog`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.1.0...v0.1.1) | [`Diff`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.1.0...v0.1.1.diff) | [`Patch`](https://github.com/seapagan/poetry-plugin-check-yanked/compare/v0.1.0...v0.1.1.patch)

## [v0.1.0](https://github.com/seapagan/poetry-plugin-check-yanked/releases/tag/v0.1.0) (June 11, 2024)

This is the first release.

---
*This changelog was generated using [github-changelog-md](http://changelog.seapagan.net/) by [Seapagan](https://github.com/seapagan)*
