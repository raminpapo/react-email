# Documentation: tsconfig.json
**File Path:** `apps/web/tsconfig.json`
**Language:** json
**Size:** 349 bytes
**Lines:** 18
**Generated:** 2025-11-15T20:37:32.797047Z

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

- **Path:** `apps/web/tsconfig.json`
- **Name:** `tsconfig.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 349 bytes (0.34 KB)
- **Lines of Code:** 18

---

## Original Source

```json
{
  "extends": "tsconfig/nextjs.json",
  "compilerOptions": {
    "target": "ES2018",
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./src/*"] },
    "types": ["vitest/globals"]
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    "next.config.ts"
  ],
  "exclude": ["node_modules"]
}

```

---

## Overview

This is a JSON configuration or data file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 21

- `ES2018`
- `compilerOptions`
- `config`
- `env`
- `exclude`
- `extends`
- `globals`
- `include`
- `json`
- `name`
- `next`
- `nextjs`
- `node_modules`
- `paths`
- `plugins`
- `src`
- `target`
- `tsconfig`
- `tsx`
- `types`
- `vitest`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

