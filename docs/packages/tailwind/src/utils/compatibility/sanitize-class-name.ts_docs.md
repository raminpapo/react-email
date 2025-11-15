# Documentation: sanitize-class-name.ts
**File Path:** `packages/tailwind/src/utils/compatibility/sanitize-class-name.ts`
**Language:** typescript
**Size:** 912 bytes
**Lines:** 37
**Generated:** 2025-11-15T20:37:32.422093Z

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

- **Path:** `packages/tailwind/src/utils/compatibility/sanitize-class-name.ts`
- **Name:** `sanitize-class-name.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 912 bytes (0.89 KB)
- **Lines of Code:** 37

---

## Original Source

```typescript
const digitToNameMap = {
  '0': 'zero',
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine',
} as const;

/**
 * Replaces special characters to avoid problems on email clients.
 *
 * @param className - This should not come with any escaped charcters, it should come the same
 * as is on the `className` attribute on React elements.
 */
export function sanitizeClassName(className: string) {
  return className
    .replaceAll('+', 'plus')
    .replaceAll('[', '')
    .replaceAll('%', 'pc')
    .replaceAll(']', '')
    .replaceAll('(', '')
    .replaceAll(')', '')
    .replaceAll('!', 'imprtnt')
    .replaceAll('>', 'gt')
    .replaceAll('<', 'lt')
    .replaceAll('=', 'eq')
    .replace(/^[0-9]/, (digit) => {
      return digitToNameMap[digit as keyof typeof digitToNameMap];
    })
    .replace(/[^a-zA-Z0-9\-_]/g, '_');
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `digitToNameMap()`
- `sanitizeClassName()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 36

- `React`
- `Replaces`
- `any`
- `attribute`
- `avoid`
- `characters`
- `charcters`
- `className`
- `clients`
- `come`
- `digit`
- `digitToNameMap`
- `eight`
- `elements`
- `email`
- `escaped`
- `five`
- `four`
- `imprtnt`
- `keyof`
- `nine`
- `one`
- `param`
- `plus`
- `problems`
- `replace`
- `replaceAll`
- `same`
- `sanitizeClassName`
- `seven`
- `six`
- `special`
- `string`
- `three`
- `two`
- `zero`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

