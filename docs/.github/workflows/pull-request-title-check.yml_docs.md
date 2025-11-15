# Documentation: pull-request-title-check.yml
**File Path:** `.github/workflows/pull-request-title-check.yml`
**Language:** yaml
**Size:** 515 bytes
**Lines:** 21
**Generated:** 2025-11-15T20:37:32.637827Z

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

- **Path:** `.github/workflows/pull-request-title-check.yml`
- **Name:** `pull-request-title-check.yml`
- **Extension:** `.yml`
- **Language:** yaml
- **Size:** 515 bytes (0.50 KB)
- **Lines of Code:** 21

---

## Original Source

```yaml
name: Pull Request Title Check
on:
  pull_request:
    types: [opened, edited, synchronize]
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
permissions:
  pull-requests: read
jobs:
  pull-request-title-check:
    runs-on: buildjet-2vcpu-ubuntu-2204
    container:
      image: node:22-slim
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Check pull request title
        run: |
          npx tsx ./scripts/pull-request-title-check.ts

```

---

## Overview

This is a YAML configuration file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 42

- `Check`
- `Checkout`
- `Pull`
- `Request`
- `Title`
- `actions`
- `buildjet`
- `cancel`
- `check`
- `checkout`
- `code`
- `concurrency`
- `container`
- `edited`
- `github`
- `group`
- `image`
- `jobs`
- `name`
- `node`
- `npx`
- `opened`
- `permissions`
- `progress`
- `pull`
- `pull_request`
- `read`
- `ref`
- `request`
- `requests`
- `run`
- `runs`
- `scripts`
- `slim`
- `steps`
- `synchronize`
- `title`
- `tsx`
- `types`
- `ubuntu`
- `uses`
- `workflow`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

