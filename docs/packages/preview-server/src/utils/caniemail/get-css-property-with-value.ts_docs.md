# Documentation: get-css-property-with-value.ts
**File Path:** `packages/preview-server/src/utils/caniemail/get-css-property-with-value.ts`
**Language:** typescript
**Size:** 383 bytes
**Lines:** 15
**Generated:** 2025-11-15T20:37:32.046331Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/get-css-property-with-value.ts`
- **Name:** `get-css-property-with-value.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 383 bytes (0.37 KB)
- **Lines of Code:** 15

---

## Original Source

```typescript
const propertyRegex =
  /(?<propertyName>[a-z-]+)\s*:\s*(?<propertyValue>[a-zA-Z\-0-9()+*/_ ]+)/;

export const getCssPropertyWithValue = (title: string) => {
  const match = propertyRegex.exec(title.trim());
  if (match) {
    const [_full, propertyName, propertyValue] = match;
    return {
      name: propertyName!,
      value: propertyValue!,
    };
  }
  return undefined;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getCssPropertyWithValue()`
- `match()`
- `propertyRegex()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 12

- `_full`
- `exec`
- `getCssPropertyWithValue`
- `match`
- `name`
- `propertyName`
- `propertyRegex`
- `propertyValue`
- `string`
- `title`
- `trim`
- `value`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

