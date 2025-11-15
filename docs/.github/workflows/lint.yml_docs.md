# Documentation: lint.yml
**File Path:** `.github/workflows/lint.yml`
**Language:** yaml
**Size:** 654 bytes
**Lines:** 30
**Generated:** 2025-11-15T20:37:32.634835Z

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

- **Path:** `.github/workflows/lint.yml`
- **Name:** `lint.yml`
- **Extension:** `.yml`
- **Language:** yaml
- **Size:** 654 bytes (0.64 KB)
- **Lines of Code:** 30

---

## Original Source

```yaml
name: Lint
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
  lint:
    runs-on: buildjet-2vcpu-ubuntu-2204
    container:
      image: node:22-slim
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: pnpm setup
        uses: pnpm/action-setup@f2b2b233b538f500472c7274c7012f57857d8ce0
      - name: Install packages
        run: pnpm install --frozen-lockfile
      - name: Run Lint
        run: pnpm lint
        env:
          SKIP_ENV_VALIDATION: true

```

---

## Overview

This is a YAML configuration file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 46

- `Checkout`
- `Install`
- `Lint`
- `Run`
- `SKIP_ENV_VALIDATION`
- `action`
- `actions`
- `branches`
- `buildjet`
- `canary`
- `cancel`
- `checkout`
- `concurrency`
- `container`
- `contents`
- `env`
- `f2b2b233b538f500472c7274c7012f57857d8ce0`
- `frozen`
- `github`
- `group`
- `image`
- `install`
- `jobs`
- `lint`
- `lockfile`
- `main`
- `name`
- `node`
- `packages`
- `permissions`
- `pnpm`
- `progress`
- `pull`
- `pull_request`
- `push`
- `read`
- `ref`
- `requests`
- `run`
- `runs`
- `setup`
- `slim`
- `steps`
- `ubuntu`
- `uses`
- `workflow`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

