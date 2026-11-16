# pytestgen Action demo

This repository shows how to use [pytestgen](https://github.com/ark2016/mipt-9-pytestGen) as an external GitHub Action. A maintainer labels a same-repository pull request `gen-tests`. The workflow starts a CPU model, posts a coverage report and uploads passing candidate tests. No provider account or API key is needed.

See [the workflow](.github/workflows/pytestgen.yml) and the [example PR](../../pull/1). It runs on trusted changes only.
