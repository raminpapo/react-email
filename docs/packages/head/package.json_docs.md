# Documentation: package.json
**File Path:** `packages/head/package.json`
**Language:** json
**Size:** 1,283 bytes
**Lines:** 56
**Generated:** 2025-11-15T20:37:32.347507Z

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

- **Path:** `packages/head/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,283 bytes (1.25 KB)
- **Lines of Code:** 56

---

## Original Source

```json
{
  "name": "@react-email/head",
  "version": "0.0.12",
  "description": "Contains head components such as style and meta elements.",
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
  "repository": {
    "type": "git",
    "url": "https://github.com/resend/react-email.git",
    "directory": "packages/head"
  },
  "keywords": [
    "react",
    "email"
  ],
  "engines": {
    "node": ">=22.0.0"
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

**Total Unique Identifiers:** 60

- `Contains`
- `access`
- `build`
- `cjs`
- `clean`
- `com`
- `components`
- `description`
- `devDependencies`
- `directory`
- `dist`
- `dts`
- `elements`
- `email`
- `engines`
- `esm`
- `exports`
- `external`
- `files`
- `format`
- `git`
- `github`
- `head`
- `https`
- `index`
- `keywords`
- `license`
- `main`
- `meta`
- `mjs`
- `module`
- `mts`
- `name`
- `node`
- `packages`
- `peerDependencies`
- `public`
- `publishConfig`
- `react`
- `render`
- `repository`
- `require`
- `resend`
- `run`
- `scripts`
- `sideEffects`
- `src`
- `style`
- `such`
- `test`
- `tsconfig`
- `tsdown`
- `type`
- `types`
- `typescript`
- `url`
- `version`
- `vitest`
- `watch`
- `workspace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

