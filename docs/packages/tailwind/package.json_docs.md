# Documentation: package.json
**File Path:** `packages/tailwind/package.json`
**Language:** json
**Size:** 2,879 bytes
**Lines:** 119
**Generated:** 2025-11-15T20:37:32.358324Z

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

- **Path:** `packages/tailwind/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 2,879 bytes (2.81 KB)
- **Lines of Code:** 119

---

## Original Source

```json
{
  "name": "@react-email/tailwind",
  "version": "2.0.1",
  "description": "A React component to wrap emails with Tailwind CSS",
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
        "types": "./dist/index.d.ts",
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
    "build": "tsdown",
    "build:watch": "tsdown --watch",
    "clean": "rm -rf dist",
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/resend/react-email.git",
    "directory": "packages/tailwind"
  },
  "keywords": [
    "react",
    "email",
    "tailwind"
  ],
  "engines": {
    "node": ">=22.0.0"
  },
  "peerDependencies": {
    "react": "^18.0 || ^19.0 || ^19.0.0-rc",
    "@react-email/body": "workspace:*",
    "@react-email/button": "workspace:*",
    "@react-email/code-block": "workspace:*",
    "@react-email/code-inline": "workspace:*",
    "@react-email/container": "workspace:*",
    "@react-email/heading": "workspace:*",
    "@react-email/hr": "workspace:*",
    "@react-email/img": "workspace:*",
    "@react-email/link": "workspace:*",
    "@react-email/preview": "workspace:*",
    "@react-email/text": "workspace:*"
  },
  "peerDependenciesMeta": {
    "@react-email/button": {
      "optional": true
    },
    "@react-email/body": {
      "optional": true
    },
    "@react-email/code-block": {
      "optional": true
    },
    "@react-email/code-inline": {
      "optional": true
    },
    "@react-email/container": {
      "optional": true
    },
    "@react-email/heading": {
      "optional": true
    },
    "@react-email/hr": {
      "optional": true
    },
    "@react-email/img": {
      "optional": true
    },
    "@react-email/link": {
      "optional": true
    },
    "@react-email/preview": {
      "optional": true
    }
  },
  "devDependencies": {
    "@react-email/button": "workspace:^",
    "@react-email/head": "workspace:*",
    "@react-email/heading": "workspace:*",
    "@react-email/hr": "workspace:*",
    "@react-email/html": "workspace:*",
    "@react-email/link": "workspace:*",
    "@react-email/render": "workspace:*",
    "@responsive-email/react-email": "0.0.4",
    "@types/css-tree": "2.3.10",
    "@types/shelljs": "0.8.15",
    "@vitejs/plugin-react": "4.4.1",
    "css-tree": "3.1.0",
    "react-dom": "^19",
    "shelljs": "0.9.2",
    "tsconfig": "workspace:*",
    "typescript": "5.8.3",
    "vite": "6.3.6",
    "vite-plugin-dts": "4.5.3",
    "yalc": "1.0.0-pre.53"
  },
  "publishConfig": {
    "access": "public"
  },
  "dependencies": {
    "tailwindcss": "^4.1.12"
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

**Total Unique Identifiers:** 80

- `React`
- `Tailwind`
- `access`
- `block`
- `body`
- `build`
- `button`
- `clean`
- `code`
- `com`
- `component`
- `container`
- `css`
- `dependencies`
- `description`
- `devDependencies`
- `directory`
- `dist`
- `dom`
- `dts`
- `email`
- `emails`
- `engines`
- `exports`
- `files`
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
- `mjs`
- `module`
- `name`
- `node`
- `optional`
- `packages`
- `peerDependencies`
- `peerDependenciesMeta`
- `plugin`
- `pre`
- `preview`
- `public`
- `publishConfig`
- `react`
- `render`
- `repository`
- `require`
- `resend`
- `responsive`
- `run`
- `scripts`
- `shelljs`
- `sideEffects`
- `tailwind`
- `tailwindcss`
- `test`
- `text`
- `tree`
- `tsconfig`
- `tsdown`
- `type`
- `types`
- `typescript`
- `url`
- `version`
- `vite`
- `vitejs`
- `vitest`
- `watch`
- `workspace`
- `wrap`
- `yalc`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

