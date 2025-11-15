# Documentation: package.json
**File Path:** `examples/postmark/package.json`
**Language:** json
**Size:** 579 bytes
**Lines:** 27
**Generated:** 2025-11-15T20:37:32.654329Z

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

- **Path:** `examples/postmark/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 579 bytes (0.57 KB)
- **Lines of Code:** 27

---

## Original Source

```json
{
  "name": "react-email-with-postmark",
  "license": "MIT",
  "private": true,
  "type": "module",
  "sideEffects": false,
  "main": "./dist/index.js",
  "files": [
    "dist/**"
  ],
  "scripts": {
    "build": "tsdown src/index.tsx --format esm --target node20",
    "dev": "tsdown src/index.tsx --format esm --target node20 --watch",
    "clean": "rm -rf dist"
  },
  "dependencies": {
    "postmark": "^3",
    "@react-email/components": "^0.0.36",
    "react": "^19",
    "react-dom": "^19"
  },
  "devDependencies": {
    "tsdown": "^0.15.1",
    "typescript": "^5"
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

**Total Unique Identifiers:** 30

- `build`
- `clean`
- `components`
- `dependencies`
- `dev`
- `devDependencies`
- `dist`
- `dom`
- `email`
- `esm`
- `files`
- `format`
- `index`
- `license`
- `main`
- `module`
- `name`
- `node20`
- `postmark`
- `private`
- `react`
- `scripts`
- `sideEffects`
- `src`
- `target`
- `tsdown`
- `tsx`
- `type`
- `typescript`
- `watch`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

