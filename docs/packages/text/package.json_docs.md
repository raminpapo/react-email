# Documentation: package.json
**File Path:** `packages/text/package.json`
**Language:** json
**Size:** 1,266 bytes
**Lines:** 56
**Generated:** 2025-11-15T20:37:31.446589Z

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

- **Path:** `packages/text/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,266 bytes (1.24 KB)
- **Lines of Code:** 56

---

## Original Source

```json
{
  "name": "@react-email/text",
  "version": "0.1.5",
  "description": "A block of text separated by blank spaces",
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
    "directory": "packages/text"
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
- `blank`
- `block`
- `build`
- `cjs`
- `clean`
- `com`
- `description`
- `devDependencies`
- `directory`
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
- `public`
- `publishConfig`
- `react`
- `render`
- `repository`
- `require`
- `resend`
- `run`
- `scripts`
- `separated`
- `sideEffects`
- `spaces`
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

