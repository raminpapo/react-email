# Documentation: tsdown.config.ts
**File Path:** `packages/render/tsdown.config.ts`
**Language:** typescript
**Size:** 425 bytes
**Lines:** 23
**Generated:** 2025-11-15T20:37:31.470483Z

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

- **Path:** `packages/render/tsdown.config.ts`
- **Name:** `tsdown.config.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 425 bytes (0.42 KB)
- **Lines of Code:** 23

---

## Original Source

```typescript
import { defineConfig } from 'tsdown';

export default defineConfig([
  {
    dts: true,
    entry: ['./src/node/index.ts'],
    outDir: './dist/node',
    format: ['cjs', 'esm'],
  },
  {
    dts: true,
    entry: ['./src/browser/index.ts'],
    outDir: './dist/browser',
    format: ['cjs', 'esm'],
  },
  {
    dts: true,
    entry: ['./src/edge/index.ts'],
    outDir: './dist/edge',
    format: ['cjs', 'esm'],
  },
]);

```

---

## Overview

This is a JavaScript/TypeScript file. It exports a default export. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `tsdown`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 14

- `browser`
- `cjs`
- `defineConfig`
- `dist`
- `dts`
- `edge`
- `entry`
- `esm`
- `format`
- `index`
- `node`
- `outDir`
- `src`
- `tsdown`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

