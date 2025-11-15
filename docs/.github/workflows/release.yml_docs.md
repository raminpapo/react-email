# Documentation: release.yml
**File Path:** `.github/workflows/release.yml`
**Language:** yaml
**Size:** 1,136 bytes
**Lines:** 36
**Generated:** 2025-11-15T20:37:32.639752Z

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

- **Path:** `.github/workflows/release.yml`
- **Name:** `release.yml`
- **Extension:** `.yml`
- **Language:** yaml
- **Size:** 1,136 bytes (1.11 KB)
- **Lines of Code:** 36

---

## Original Source

```yaml
name: Release
on:
  push:
    branches:
      - main
concurrency: ${{ github.workflow }}-${{ github.ref }}
jobs:
  release:
    runs-on: buildjet-4vcpu-ubuntu-2204
    permissions: 
      contents: write
      pull-requests: write
    container:
      image: node:22
    steps:
      - name: Checkout Repo
        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8
      - run: git config --global --add safe.directory $GITHUB_WORKSPACE
      - name: pnpm setup
        uses: pnpm/action-setup@f2b2b233b538f500472c7274c7012f57857d8ce0
      - name: Install packages
        run: pnpm install --frozen-lockfile
      - name: Exit prerelease mode
        # This step errors if it is not in prerelease mode
        continue-on-error: true
        run: pnpm canary:exit
      - name: Create "version packages" pull request or publish release
        uses: changesets/action@v1.5.3
        with:
          version: pnpm run version
          publish: pnpm run release
          title: "chore(root): version packages"
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}

```

---

## Overview

This is a YAML configuration file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 65

- `Checkout`
- `Create`
- `Exit`
- `GITHUB_TOKEN`
- `GITHUB_WORKSPACE`
- `Install`
- `NPM_TOKEN`
- `Release`
- `Repo`
- `action`
- `actions`
- `add`
- `branches`
- `buildjet`
- `canary`
- `changesets`
- `checkout`
- `chore`
- `concurrency`
- `config`
- `container`
- `contents`
- `directory`
- `env`
- `error`
- `errors`
- `exit`
- `f2b2b233b538f500472c7274c7012f57857d8ce0`
- `frozen`
- `git`
- `github`
- `global`
- `image`
- `install`
- `jobs`
- `lockfile`
- `main`
- `mode`
- `name`
- `node`
- `packages`
- `permissions`
- `pnpm`
- `prerelease`
- `publish`
- `pull`
- `push`
- `ref`
- `release`
- `request`
- `requests`
- `root`
- `run`
- `runs`
- `safe`
- `secrets`
- `setup`
- `step`
- `steps`
- `title`
- `ubuntu`
- `uses`
- `version`
- `workflow`
- `write`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

