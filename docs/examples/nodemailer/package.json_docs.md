# Documentation: package.json
**File Path:** `examples/nodemailer/package.json`
**Language:** json
**Size:** 614 bytes
**Lines:** 28
**Generated:** 2025-11-15T20:37:32.677076Z

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

- **Path:** `examples/nodemailer/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 614 bytes (0.60 KB)
- **Lines of Code:** 28

---

## Original Source

```json
{
  "name": "react-email-with-nodemailer",
  "license": "MIT",
  "private": true,
  "sideEffects": false,
  "type": "module",
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
    "@react-email/components": "^0.0.36",
    "nodemailer": "^6",
    "react": "^19",
    "react-dom": "^19"
  },
  "devDependencies": {
    "@types/nodemailer": "^6",
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

**Total Unique Identifiers:** 31

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
- `nodemailer`
- `private`
- `react`
- `scripts`
- `sideEffects`
- `src`
- `target`
- `tsdown`
- `tsx`
- `type`
- `types`
- `typescript`
- `watch`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

