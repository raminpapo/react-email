# Documentation: get-element-names.ts
**File Path:** `packages/preview-server/src/utils/caniemail/get-element-names.ts`
**Language:** typescript
**Size:** 586 bytes
**Lines:** 27
**Generated:** 2025-11-15T20:37:32.049334Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/get-element-names.ts`
- **Name:** `get-element-names.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 586 bytes (0.57 KB)
- **Lines of Code:** 27

---

## Original Source

```typescript
export const getElementNames = (title: string, keywords: string | null) => {
  const match = /<(?<elementName>[^>]*)> element/.exec(title);
  if (match) {
    const [_full, elementName] = match;

    if (elementName) {
      return [elementName.toLowerCase()];
    }
  }

  if (keywords !== null && keywords.length > 0) {
    return keywords
      .toLowerCase()
      .split(/\s*,\s*/)
      .map((piece) => piece.trim());
  }

  if (title.split(',').length > 1) {
    return title
      .toLowerCase()
      .split(/\s*,\s*/)
      .map((piece) => piece.trim());
  }

  return [];
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getElementNames()`
- `match()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 15

- `_full`
- `element`
- `elementName`
- `exec`
- `getElementNames`
- `keywords`
- `length`
- `map`
- `match`
- `piece`
- `split`
- `string`
- `title`
- `toLowerCase`
- `trim`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

