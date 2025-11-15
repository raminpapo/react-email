# Documentation: package.json
**File Path:** `packages/preview/package.json`
**Language:** json
**Size:** 1,299 bytes
**Lines:** 56
**Generated:** 2025-11-15T20:37:32.260674Z

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

- **Path:** `packages/preview/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,299 bytes (1.27 KB)
- **Lines of Code:** 56

---

## Original Source

```json
{
  "name": "@react-email/preview",
  "version": "0.0.13",
  "description": "A preview text that will be displayed in the inbox of the recipient",
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
    "directory": "packages/preview"
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

**Total Unique Identifiers:** 58

- `access`
- `build`
- `cjs`
- `clean`
- `com`
- `description`
- `devDependencies`
- `directory`
- `displayed`
- `dist`
- `dts`
- `email`
- `engines`
- `esm`
- `exports`
- `external`
- `files`
- `format`
- `git`
- `github`
- `https`
- `inbox`
- `index`
- `keywords`
- `license`
- `main`
- `mjs`
- `module`
- `mts`
- `name`
- `node`
- `packages`
- `peerDependencies`
- `preview`
- `public`
- `publishConfig`
- `react`
- `recipient`
- `render`
- `repository`
- `require`
- `resend`
- `run`
- `scripts`
- `sideEffects`
- `src`
- `test`
- `text`
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

