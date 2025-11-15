# Documentation: pin-dependencies-check.yml
**File Path:** `.github/workflows/pin-dependencies-check.yml`
**Language:** yaml
**Size:** 526 bytes
**Lines:** 24
**Generated:** 2025-11-15T20:37:32.635806Z

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

- **Path:** `.github/workflows/pin-dependencies-check.yml`
- **Name:** `pin-dependencies-check.yml`
- **Extension:** `.yml`
- **Language:** yaml
- **Size:** 526 bytes (0.51 KB)
- **Lines of Code:** 24

---

## Original Source

```yaml
name: Pin Dependencies Check
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
  pin-dependencies-check:
    runs-on: buildjet-2vcpu-ubuntu-2204
    container:
      image: node:22-slim
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Check for pinned dependencies
        run: npx tsx ./scripts/check-dependency-versions.ts

```

---

## Overview

This is a YAML configuration file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 44

- `Check`
- `Checkout`
- `Dependencies`
- `Pin`
- `actions`
- `branches`
- `buildjet`
- `canary`
- `cancel`
- `check`
- `checkout`
- `concurrency`
- `container`
- `contents`
- `dependencies`
- `dependency`
- `github`
- `group`
- `image`
- `jobs`
- `main`
- `name`
- `node`
- `npx`
- `permissions`
- `pin`
- `pinned`
- `progress`
- `pull`
- `pull_request`
- `push`
- `read`
- `ref`
- `requests`
- `run`
- `runs`
- `scripts`
- `slim`
- `steps`
- `tsx`
- `ubuntu`
- `uses`
- `versions`
- `workflow`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

