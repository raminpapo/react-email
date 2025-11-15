# Documentation: package.json
**File Path:** `packages/code-block/package.json`
**Language:** json
**Size:** 1,337 bytes
**Lines:** 58
**Generated:** 2025-11-15T20:37:31.548690Z

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

- **Path:** `packages/code-block/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,337 bytes (1.31 KB)
- **Lines of Code:** 58

---

## Original Source

```json
{
  "name": "@react-email/code-block",
  "version": "0.2.0",
  "description": "Display code with a selected theme and regex highlighting using Prism.js",
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
  "repository": {
    "type": "git",
    "url": "https://github.com/resend/react-email.git",
    "directory": "packages/code-block"
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
    "@types/prismjs": "1.26.5",
    "tsconfig": "workspace:*",
    "typescript": "5.8.3"
  },
  "publishConfig": {
    "access": "public"
  },
  "dependencies": {
    "prismjs": "^1.30.0"
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

**Total Unique Identifiers:** 61

- `Display`
- `Prism`
- `access`
- `block`
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
- `highlighting`
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
- `prismjs`
- `public`
- `publishConfig`
- `react`
- `regex`
- `render`
- `repository`
- `require`
- `resend`
- `scripts`
- `selected`
- `sideEffects`
- `src`
- `theme`
- `tsconfig`
- `tsdown`
- `type`
- `types`
- `typescript`
- `url`
- `using`
- `version`
- `watch`
- `workspace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

