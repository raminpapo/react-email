# Documentation: get-css-property-names.ts
**File Path:** `packages/preview-server/src/utils/caniemail/get-css-property-names.ts`
**Language:** typescript
**Size:** 847 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:32.045242Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/get-css-property-names.ts`
- **Name:** `get-css-property-names.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 847 bytes (0.83 KB)
- **Lines of Code:** 33

---

## Original Source

```typescript
import { allCssProperties } from './all-css-properties';

export const getCssPropertyNames = (title: string, keywords: string | null) => {
  if (allCssProperties.includes(title.replace(' property', '')))
    return [title.replace(' property', '')];

  if (title.split('&').length > 1) {
    return title
      .split(/\s*&\s*/)
      .map((piece) => piece.trim())
      .filter((possiblePropertyName) =>
        allCssProperties.includes(possiblePropertyName),
      );
  }

  if (title.split(',').length > 1) {
    return title
      .split(/\s*,\s*/)
      .map((piece) => piece.trim())
      .filter((possiblePropertyName) =>
        allCssProperties.includes(possiblePropertyName),
      );
  }

  if (keywords) {
    return keywords
      .split(/\s*,\s*/)
      .filter((keyword) => allCssProperties.includes(keyword));
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

- `getCssPropertyNames()`

### Dependencies

This file imports/requires:

- `./all-css-properties`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 19

- `all`
- `allCssProperties`
- `css`
- `filter`
- `getCssPropertyNames`
- `includes`
- `keyword`
- `keywords`
- `length`
- `map`
- `piece`
- `possiblePropertyName`
- `properties`
- `property`
- `replace`
- `split`
- `string`
- `title`
- `trim`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

