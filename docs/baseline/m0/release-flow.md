# M0 Gitea release flow

The Gitea workflow at [`.gitea/workflows/release.yml`](../../../.gitea/workflows/release.yml) uses the shared [`constructorfleet/release-please`](https://gitea.home.prettybaked.com/constructorfleet/release-please) action, pinned to tag `v17.1.3` (source commit `fd1647b055d8c30f12bcea1923e263ef021657e6`). Gitea Actions uses the `self:` action prefix to fetch that action from this instance.

## Workflow behavior

- Every push and pull request runs the Python quality job on Python 3.12. It installs the project editable with `pytest==8.4.2`, then runs `python -m pytest -q`.
- Only a push to `main` checks for an unpublished version in `CHANGELOG.md`. If the version's `vX.Y.Z` tag is absent, the release action runs in `release` mode after the quality job succeeds.
- If no release is pending, the workflow checks commits since the latest semantic version tag. It skips planning unless it finds a release-worthy Conventional Commit (`feat`, `feature`, `fix`, `perf`, a breaking-change marker, or `Release-As`).
- On release-worthy commits, the action maintains a `release-please--branches--main` release PR using the initial version `0.1.0` and `v`-prefixed tags.
- The action updates `CHANGELOG.md`, but this Gitea action does not update Python's `pyproject.toml`. After the action creates or updates the release PR branch, `.gitea/scripts/sync_project_version.py` copies the computed version to `[project].version` and pushes that change to the same release branch. Focused tests cover field isolation, idempotency, invalid versions, and missing version fields.
- The release action creates or syncs the Gitea release from the matching changelog section. Build and package/registry publication remain project-owned and are not performed here.

## Secret and prerequisites

Configure a repository secret named `GITEA_TOKEN` with permission to read the repository, push the release branch, create/update pull requests, and create/sync releases. The workflow never stores a token in the repository. The Gitea Actions runner must provide Python 3.12, Node.js 24, npm, Git, and access to this Gitea instance. `setup-python` and `setup-node` install the runtime versions before their jobs use them.

## Validation status

The YAML parses, embedded Bash scripts pass `bash -n`, and `actionlint` accepts the workflow using Gitea's documented `self:` reference and GitHub-compatible context aliases. The Python version-sync tests and full Python test suite run locally. A live release action run still requires the configured `GITEA_TOKEN` secret and a Gitea Actions runner; local checks do not claim that the remote action created a PR or release.
