# Documentation: get-css-unit.ts
**File Path:** `packages/preview-server/src/utils/caniemail/get-css-unit.ts`
**Language:** typescript
**Size:** 125 bytes
**Lines:** 4
**Generated:** 2025-11-15T20:37:32.047389Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/get-css-unit.ts`
- **Name:** `get-css-unit.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 125 bytes (0.12 KB)
- **Lines of Code:** 4

---

## Original Source

```typescript
export const getCssUnit = (title: string) => {
  return title.endsWith(' unit') ? title.replace(' unit', '') : undefined;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getCssUnit()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 6

- `endsWith`
- `getCssUnit`
- `replace`
- `string`
- `title`
- `unit`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

