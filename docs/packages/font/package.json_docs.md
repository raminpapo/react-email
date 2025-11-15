# Documentation: package.json
**File Path:** `packages/font/package.json`
**Language:** json
**Size:** 1,045 bytes
**Lines:** 44
**Generated:** 2025-11-15T20:37:32.270490Z

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

- **Path:** `packages/font/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,045 bytes (1.02 KB)
- **Lines of Code:** 44

---

## Original Source

```json
{
  "name": "@react-email/font",
  "version": "0.0.9",
  "description": "A React Font component to set your fonts",
  "sideEffects": false,
  "main": "./dist/index.js",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.ts",
  "files": [
    "dist/**"
  ],
  "exports": {
    ".": {
      "import": {
        "types": "./dist/index.d.mts",
        "default": "./dist/index.mjs"
      },
      "require": {
        "types": "./dist/index.d.ts",
        "default": "./dist/index.js"
      }
    }
  },
  "license": "MIT",
  "scripts": {
    "build": "tsdown src/index.ts --format esm,cjs --dts --external react",
    "build:watch": "tsdown src/index.ts --format esm,cjs --dts --external react --watch",
    "clean": "rm -rf dist",
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "peerDependencies": {
    "react": "^18.0 || ^19.0 || ^19.0.0-rc"
  },
  "devDependencies": {
    "@react-email/render": "workspace:*",
    "tsconfig": "workspace:*",
    "typescript": "5.8.3"
  },
  "publishConfig": {
    "access": "public"
  }
}

```

---

## Overview

This is a JSON configuration or data file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 47

- `Font`
- `React`
- `access`
- `build`
- `cjs`
- `clean`
- `component`
- `description`
- `devDependencies`
- `dist`
- `dts`
- `email`
- `esm`
- `exports`
- `external`
- `files`
- `font`
- `fonts`
- `format`
- `index`
- `license`
- `main`
- `mjs`
- `module`
- `mts`
- `name`
- `peerDependencies`
- `public`
- `publishConfig`
- `react`
- `render`
- `require`
- `run`
- `scripts`
- `set`
- `sideEffects`
- `src`
- `test`
- `tsconfig`
- `tsdown`
- `types`
- `typescript`
- `version`
- `vitest`
- `watch`
- `workspace`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

