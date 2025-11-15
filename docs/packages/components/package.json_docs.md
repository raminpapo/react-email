# Documentation: package.json
**File Path:** `packages/components/package.json`
**Language:** json
**Size:** 2,137 bytes
**Lines:** 75
**Generated:** 2025-11-15T20:37:32.503666Z

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

- **Path:** `packages/components/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 2,137 bytes (2.09 KB)
- **Lines of Code:** 75

---

## Original Source

```json
{
  "name": "@react-email/components",
  "version": "1.0.1",
  "description": "A collection of all components React Email.",
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
    "directory": "packages/components"
  },
  "keywords": [
    "react",
    "email"
  ],
  "engines": {
    "node": ">=22.0.0"
  },
  "dependencies": {
    "@react-email/body": "workspace:0.2.0",
    "@react-email/button": "workspace:0.2.0",
    "@react-email/code-block": "workspace:0.2.0",
    "@react-email/code-inline": "workspace:0.0.5",
    "@react-email/column": "workspace:0.0.13",
    "@react-email/container": "workspace:0.0.15",
    "@react-email/font": "workspace:0.0.9",
    "@react-email/head": "workspace:0.0.12",
    "@react-email/heading": "workspace:0.0.15",
    "@react-email/hr": "workspace:0.0.11",
    "@react-email/html": "workspace:0.0.11",
    "@react-email/img": "workspace:0.0.11",
    "@react-email/link": "workspace:0.0.12",
    "@react-email/markdown": "workspace:0.0.17",
    "@react-email/preview": "workspace:0.0.13",
    "@react-email/render": "workspace:2.0.0",
    "@react-email/row": "workspace:0.0.12",
    "@react-email/section": "workspace:0.0.16",
    "@react-email/tailwind": "workspace:2.0.1",
    "@react-email/text": "workspace:0.1.5"
  },
  "peerDependencies": {
    "react": "^18.0 || ^19.0 || ^19.0.0-rc"
  },
  "devDependencies": {
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

**Total Unique Identifiers:** 75

- `Email`
- `React`
- `access`
- `all`
- `block`
- `body`
- `build`
- `button`
- `cjs`
- `clean`
- `code`
- `collection`
- `column`
- `com`
- `components`
- `container`
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
- `font`
- `format`
- `git`
- `github`
- `head`
- `heading`
- `html`
- `https`
- `img`
- `index`
- `inline`
- `keywords`
- `license`
- `link`
- `main`
- `markdown`
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
- `render`
- `repository`
- `require`
- `resend`
- `row`
- `scripts`
- `section`
- `sideEffects`
- `src`
- `tailwind`
- `text`
- `tsconfig`
- `tsdown`
- `type`
- `types`
- `typescript`
- `url`
- `version`
- `watch`
- `workspace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

