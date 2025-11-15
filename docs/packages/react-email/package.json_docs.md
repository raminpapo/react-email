# Documentation: package.json
**File Path:** `packages/react-email/package.json`
**Language:** json
**Size:** 1,391 bytes
**Lines:** 60
**Generated:** 2025-11-15T20:37:32.516525Z

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

- **Path:** `packages/react-email/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,391 bytes (1.36 KB)
- **Lines of Code:** 60

---

## Original Source

```json
{
  "name": "react-email",
  "version": "5.0.4",
  "description": "A live preview of your emails right in your browser.",
  "bin": {
    "email": "./dist/index.js"
  },
  "type": "module",
  "scripts": {
    "build": "tsdown",
    "build:watch": "tsdown --watch src",
    "clean": "rm -rf dist",
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/resend/react-email.git",
    "directory": "packages/react-email"
  },
  "keywords": [
    "react",
    "email"
  ],
  "engines": {
    "node": ">=22.0.0"
  },
  "dependencies": {
    "@babel/parser": "^7.27.0",
    "@babel/traverse": "^7.27.0",
    "chokidar": "^4.0.3",
    "commander": "^13.0.0",
    "conf": "^15.0.2",
    "debounce": "^2.0.0",
    "esbuild": "^0.25.0",
    "glob": "^11.0.0",
    "jiti": "2.4.2",
    "log-symbols": "^7.0.0",
    "mime-types": "^3.0.0",
    "normalize-path": "^3.0.0",
    "nypm": "0.6.0",
    "ora": "^8.0.0",
    "prompts": "2.4.2",
    "socket.io": "^4.8.1",
    "tsconfig-paths": "4.2.0"
  },
  "devDependencies": {
    "@react-email/components": "workspace:*",
    "@types/babel__core": "7.20.5",
    "@types/babel__traverse": "7.20.7",
    "@types/mime-types": "2.1.4",
    "@types/prompts": "2.4.9",
    "next": "16.0.1",
    "react": "19.0.0",
    "react-dom": "19.0.0",
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

**Total Unique Identifiers:** 69

- `babel`
- `babel__core`
- `babel__traverse`
- `bin`
- `browser`
- `build`
- `chokidar`
- `clean`
- `com`
- `commander`
- `components`
- `conf`
- `debounce`
- `dependencies`
- `description`
- `devDependencies`
- `directory`
- `dist`
- `dom`
- `email`
- `emails`
- `engines`
- `esbuild`
- `git`
- `github`
- `glob`
- `https`
- `index`
- `jiti`
- `keywords`
- `license`
- `live`
- `log`
- `mime`
- `module`
- `name`
- `next`
- `node`
- `normalize`
- `nypm`
- `ora`
- `packages`
- `parser`
- `path`
- `paths`
- `preview`
- `prompts`
- `react`
- `repository`
- `resend`
- `right`
- `run`
- `scripts`
- `socket`
- `src`
- `symbols`
- `test`
- `traverse`
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
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

