# Documentation: get-css-functions.ts
**File Path:** `packages/preview-server/src/utils/caniemail/get-css-functions.ts`
**Language:** typescript
**Size:** 696 bytes
**Lines:** 26
**Generated:** 2025-11-15T20:37:32.044175Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/get-css-functions.ts`
- **Name:** `get-css-functions.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 696 bytes (0.68 KB)
- **Lines of Code:** 26

---

## Original Source

```typescript
export function getCssFunctions(title: string) {
  if (/^[a-zA-Z]\(\)$/.test(title.trim())) {
    return [title.replace('()', '')];
  }

  // ex: lch(), oklch(), lab(), oklab()
  // this regex avoids matching entries that are for CSS properties listed
  // separated by commas as well
  if (/^(?:[^(),]+?\(\),?)*$/.test(title.trim())) {
    return title
      .split(/\s*,\s*/)
      .map((functionCallWithoutParameters) =>
        functionCallWithoutParameters.replace('()', ''),
      );
  }

  // ex: CSS calc() function
  if (/^CSS [a-z]+\(\) function$/.test(title.trim())) {
    return [
      title.replace('CSS ', '').replace(' function', '').replace('()', ''),
    ];
  }

  return [];
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getCssFunctions()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 23

- `avoids`
- `calc`
- `commas`
- `entries`
- `functionCallWithoutParameters`
- `getCssFunctions`
- `lab`
- `lch`
- `listed`
- `map`
- `matching`
- `oklab`
- `oklch`
- `properties`
- `regex`
- `replace`
- `separated`
- `split`
- `string`
- `test`
- `title`
- `trim`
- `well`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

