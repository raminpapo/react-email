# Documentation: snake-to-camel.ts
**File Path:** `packages/preview-server/src/utils/snake-to-camel.ts`
**Language:** typescript
**Size:** 158 bytes
**Lines:** 6
**Generated:** 2025-11-15T20:37:32.035152Z

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

- **Path:** `packages/preview-server/src/utils/snake-to-camel.ts`
- **Name:** `snake-to-camel.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 158 bytes (0.15 KB)
- **Lines of Code:** 6

---

## Original Source

```typescript
export function snakeToCamel(snakeStr: string) {
  return snakeStr
    .toLowerCase()
    .replace(/-+([a-z])/g, (_match, letter) => letter.toUpperCase());
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `snakeToCamel()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 8

- `_match`
- `letter`
- `replace`
- `snakeStr`
- `snakeToCamel`
- `string`
- `toLowerCase`
- `toUpperCase`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

