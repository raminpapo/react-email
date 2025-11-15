# Documentation: slugify.ts
**File Path:** `apps/web/src/utils/slugify.ts`
**Language:** typescript
**Size:** 169 bytes
**Lines:** 8
**Generated:** 2025-11-15T20:37:32.808145Z

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

- **Path:** `apps/web/src/utils/slugify.ts`
- **Name:** `slugify.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 169 bytes (0.17 KB)
- **Lines of Code:** 8

---

## Original Source

```typescript
export const slugify = (text: string): string =>
  text
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '-')
    .replace(/[^\w-]+/g, '')
    .replace(/--+/g, '-');

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `slugify()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 6

- `replace`
- `slugify`
- `string`
- `text`
- `toLowerCase`
- `trim`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

