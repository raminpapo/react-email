# Documentation: tests.yml
**File Path:** `.github/workflows/tests.yml`
**Language:** yaml
**Size:** 1,146 bytes
**Lines:** 40
**Generated:** 2025-11-15T20:37:32.640795Z

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Original Source](#original-source)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Keywords & Identifiers](#keywords--identifiers)
6. [Related Files](#related-files)

---

## File Metadata

- **Path:** `.github/workflows/tests.yml`
- **Name:** `tests.yml`
- **Extension:** `.yml`
- **Language:** yaml
- **Size:** 1,146 bytes (1.12 KB)
- **Lines of Code:** 40

---

## Original Source

```yaml
name: Tests
on:
  push:
    branches:
      - main
      - canary
  pull_request:
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
permissions: 
  contents: read
  pull-requests: read
jobs:
  tests:
    runs-on: buildjet-4vcpu-ubuntu-2204
    outputs:
      cache-hit: ${{ steps.pnpm-cache.outputs.cache-hit }}
    container:
      image: node:22-slim
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: pnpm setup
        uses: pnpm/action-setup@f2b2b233b538f500472c7274c7012f57857d8ce0
      - name: Install packages
        run: pnpm install --frozen-lockfile
      - name: Run Build
        run: pnpm build
        # We include the environment variables here so that the cache for turborepo
        # is not invalidated and builds are re-ran
        env:
          SPAM_ASSASSIN_HOST: ${{ secrets.SPAM_ASSASSIN_HOST }}
          SPAM_ASSASSIN_PORT: ${{ secrets.SPAM_ASSASSIN_PORT }}
      - name: Run Tests
        run: pnpm test
        env:
          SPAM_ASSASSIN_HOST: ${{ secrets.SPAM_ASSASSIN_HOST }}
          SPAM_ASSASSIN_PORT: ${{ secrets.SPAM_ASSASSIN_PORT }}

```

---

## Overview

This is a YAML configuration file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 62

- `Build`
- `Checkout`
- `Install`
- `Run`
- `SPAM_ASSASSIN_HOST`
- `SPAM_ASSASSIN_PORT`
- `Tests`
- `action`
- `actions`
- `branches`
- `build`
- `buildjet`
- `builds`
- `cache`
- `canary`
- `cancel`
- `checkout`
- `concurrency`
- `container`
- `contents`
- `env`
- `environment`
- `f2b2b233b538f500472c7274c7012f57857d8ce0`
- `frozen`
- `github`
- `group`
- `here`
- `hit`
- `image`
- `include`
- `install`
- `invalidated`
- `jobs`
- `lockfile`
- `main`
- `name`
- `node`
- `outputs`
- `packages`
- `permissions`
- `pnpm`
- `progress`
- `pull`
- `pull_request`
- `push`
- `ran`
- `read`
- `ref`
- `requests`
- `run`
- `runs`
- `secrets`
- `setup`
- `slim`
- `steps`
- `test`
- `tests`
- `turborepo`
- `ubuntu`
- `uses`
- `variables`
- `workflow`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

