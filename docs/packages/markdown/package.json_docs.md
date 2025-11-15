# Documentation: package.json
**File Path:** `packages/markdown/package.json`
**Language:** json
**Size:** 1,352 bytes
**Lines:** 60
**Generated:** 2025-11-15T20:37:32.293458Z

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

- **Path:** `packages/markdown/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,352 bytes (1.32 KB)
- **Lines of Code:** 60

---

## Original Source

```json
{
  "name": "@react-email/markdown",
  "version": "0.0.17",
  "description": "Convert Markdown to valid React Email template code.",
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
  "scripts": {
    "build": "tsdown src/index.ts --format esm,cjs --dts --external react",
    "build:watch": "tsdown src/index.ts --format esm,cjs --dts --external react --watch",
    "clean": "rm -rf dist",
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "keywords": [
    "react",
    "email",
    "markdown"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/resend/react-email.git",
    "directory": "packages/markdown"
  },
  "engines": {
    "node": ">=22.0.0"
  },
  "publishConfig": {
    "access": "public"
  },
  "license": "MIT",
  "dependencies": {
    "marked": "^15.0.12"
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

**Total Unique Identifiers:** 63

- `Convert`
- `Email`
- `Markdown`
- `React`
- `access`
- `build`
- `cjs`
- `clean`
- `code`
- `com`
- `dependencies`
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
- `markdown`
- `marked`
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
- `template`
- `test`
- `tsconfig`
- `tsdown`
- `type`
- `types`
- `typescript`
- `url`
- `valid`
- `version`
- `vitest`
- `watch`
- `workspace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

