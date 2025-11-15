# Documentation: preview-release.yml
**File Path:** `.github/workflows/preview-release.yml`
**Language:** yaml
**Size:** 1,134 bytes
**Lines:** 35
**Generated:** 2025-11-15T20:37:32.636859Z

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

- **Path:** `.github/workflows/preview-release.yml`
- **Name:** `preview-release.yml`
- **Extension:** `.yml`
- **Language:** yaml
- **Size:** 1,134 bytes (1.11 KB)
- **Lines of Code:** 35

---

## Original Source

```yaml
name: Preview Release
on: 
  pull_request:
permissions:
  contents: read
  pull-requests: write
concurrency: ${{ github.workflow }}-${{ github.ref }}
jobs:
  preview-release:
    runs-on: buildjet-4vcpu-ubuntu-2204
    permissions: 
      contents: write
      pull-requests: write
    container:
      image: node:22
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v4
      - name: pnpm setup
        uses: pnpm/action-setup@f2b2b233b538f500472c7274c7012f57857d8ce0
      - name: Install packages
        run: pnpm install --frozen-lockfile
      - name: Run Build
        run: pnpm turbo run build --filter=./packages/*
      - name: Find changed packages
        id: changed_packages
        uses: tj-actions/changed-files@212f9a7760ad2b8eb511185b841f3725a62c2ae0
        with:
          files: packages/**
          dir_names: true
          dir_names_max_depth: 2
      - name: Publish changed packages to pkg.pr.new
        if: steps.changed_packages.outputs.all_changed_and_modified_files != ''
        run: pnpm dlx pkg-pr-new publish ${{ steps.changed_packages.outputs.all_changed_and_modified_files }}

```

---

## Overview

This is a YAML configuration file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 56

- `Build`
- `Checkout`
- `Find`
- `Install`
- `Preview`
- `Publish`
- `Release`
- `Repo`
- `Run`
- `action`
- `actions`
- `all_changed_and_modified_files`
- `build`
- `buildjet`
- `changed`
- `changed_packages`
- `checkout`
- `concurrency`
- `container`
- `contents`
- `dir_names`
- `dir_names_max_depth`
- `dlx`
- `f2b2b233b538f500472c7274c7012f57857d8ce0`
- `files`
- `filter`
- `frozen`
- `github`
- `image`
- `install`
- `jobs`
- `lockfile`
- `name`
- `node`
- `outputs`
- `packages`
- `permissions`
- `pkg`
- `pnpm`
- `preview`
- `publish`
- `pull`
- `pull_request`
- `read`
- `ref`
- `release`
- `requests`
- `run`
- `runs`
- `setup`
- `steps`
- `turbo`
- `ubuntu`
- `uses`
- `workflow`
- `write`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

