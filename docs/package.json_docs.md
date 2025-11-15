# Documentation: package.json
**File Path:** `package.json`
**Language:** json
**Size:** 1,254 bytes
**Lines:** 41
**Generated:** 2025-11-15T20:37:31.334764Z

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

- **Path:** `package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,254 bytes (1.22 KB)
- **Lines of Code:** 41

---

## Original Source

```json
{
  "name": "react-email-monorepo",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "build": "turbo run build",
    "canary:enter": "changeset pre enter canary",
    "canary:exit": "changeset pre exit",
    "lint": "biome check",
    "lint:fix": "biome check --write .",
    "release": "turbo run build --filter=./packages/* && pnpm changeset publish",
    "test": "turbo run test",
    "test:watch": "turbo run test:watch",
    "version": "changeset version && pnpm install --no-frozen-lockfile && pnpm lint:fix"
  },
  "devDependencies": {
    "@biomejs/biome": "2.3.3",
    "@changesets/cli": "2.29.7",
    "@types/node": "22.14.1",
    "@types/react": "19.0.1",
    "@types/react-dom": "19.0.1",
    "happy-dom": "18.0.1",
    "pkg-pr-new": "0.0.54",
    "tsconfig": "workspace:*",
    "tsdown": "0.15.12",
    "tsx": "4.20.3",
    "turbo": "2.5.8",
    "vite": "6.3.6",
    "vitest": "3.2.4"
  },
  "pnpm": {
    "overrides": {
      "react": "^19.0.0",
      "react-dom": "^19.0.0",
      "@types/react": "^19.0.1",
      "@types/react-dom": "^19.0.1"
    }
  },
  "packageManager": "pnpm@10.20.0+sha512.cf9998222162dd85864d0a8102e7892e7ba4ceadebbf5a31f9c2fce48dfce317a9c53b9f6464d1ef9042cba2e02ae02a9f7c143a2b438cd93c91840f0192b9dd"
}

```

---

## Overview

This is a JSON configuration or data file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 49

- `biome`
- `biomejs`
- `build`
- `canary`
- `cf9998222162dd85864d0a8102e7892e7ba4ceadebbf5a31f9c2fce48dfce317a9c53b9f6464d1ef9042cba2e02ae02a9f7c143a2b438cd93c91840f0192b9dd`
- `changeset`
- `changesets`
- `check`
- `cli`
- `devDependencies`
- `dom`
- `email`
- `enter`
- `exit`
- `filter`
- `fix`
- `frozen`
- `happy`
- `install`
- `lint`
- `lockfile`
- `monorepo`
- `name`
- `node`
- `overrides`
- `packageManager`
- `packages`
- `pkg`
- `pnpm`
- `pre`
- `private`
- `publish`
- `react`
- `release`
- `run`
- `scripts`
- `sha512`
- `test`
- `tsconfig`
- `tsdown`
- `tsx`
- `turbo`
- `types`
- `version`
- `vite`
- `vitest`
- `watch`
- `workspace`
- `write`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

