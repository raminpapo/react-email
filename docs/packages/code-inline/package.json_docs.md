# Documentation: package.json
**File Path:** `packages/code-inline/package.json`
**Language:** json
**Size:** 1,079 bytes
**Lines:** 45
**Generated:** 2025-11-15T20:37:32.237617Z

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

- **Path:** `packages/code-inline/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,079 bytes (1.05 KB)
- **Lines of Code:** 45

---

## Original Source

```json
{
  "name": "@react-email/code-inline",
  "version": "0.0.5",
  "description": "Display a predictable inline code HTML element that works on all email clients",
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
    "clean": "rm -rf dist"
  },
  "engines": {
    "node": ">=22.0.0"
  },
  "publishConfig": {
    "access": "public"
  },
  "peerDependencies": {
    "react": "^18.0 || ^19.0 || ^19.0.0-rc"
  },
  "devDependencies": {
    "@react-email/render": "workspace:*",
    "tsconfig": "workspace:*",
    "typescript": "5.8.3"
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

- `Display`
- `access`
- `all`
- `build`
- `cjs`
- `clean`
- `clients`
- `code`
- `description`
- `devDependencies`
- `dist`
- `dts`
- `element`
- `email`
- `engines`
- `esm`
- `exports`
- `external`
- `files`
- `format`
- `index`
- `inline`
- `license`
- `main`
- `mjs`
- `module`
- `mts`
- `name`
- `node`
- `peerDependencies`
- `predictable`
- `public`
- `publishConfig`
- `react`
- `render`
- `require`
- `scripts`
- `sideEffects`
- `src`
- `tsconfig`
- `tsdown`
- `types`
- `typescript`
- `version`
- `watch`
- `works`
- `workspace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

