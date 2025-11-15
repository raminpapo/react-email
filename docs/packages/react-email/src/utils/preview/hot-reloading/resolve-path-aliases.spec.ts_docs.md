# Documentation: resolve-path-aliases.spec.ts
**File Path:** `packages/react-email/src/utils/preview/hot-reloading/resolve-path-aliases.spec.ts`
**Language:** typescript
**Size:** 283 bytes
**Lines:** 12
**Generated:** 2025-11-15T20:37:32.560457Z

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

- **Path:** `packages/react-email/src/utils/preview/hot-reloading/resolve-path-aliases.spec.ts`
- **Name:** `resolve-path-aliases.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 283 bytes (0.28 KB)
- **Lines of Code:** 12

---

## Original Source

```typescript
import path from 'node:path';
import { resolvePathAliases } from './resolve-path-aliases.js';

test('resolveImports()', async () => {
  expect(
    resolvePathAliases(
      ['@/some-file'],
      path.resolve(import.meta.dirname, './test'),
    ),
  ).toEqual(['./some-file']);
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `./resolve-path-aliases.js`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 13

- `aliases`
- `dirname`
- `expect`
- `file`
- `meta`
- `node`
- `path`
- `resolve`
- `resolveImports`
- `resolvePathAliases`
- `some`
- `test`
- `toEqual`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

