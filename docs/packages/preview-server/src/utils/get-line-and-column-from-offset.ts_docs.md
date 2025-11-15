# Documentation: get-line-and-column-from-offset.ts
**File Path:** `packages/preview-server/src/utils/get-line-and-column-from-offset.ts`
**Language:** typescript
**Size:** 339 bytes
**Lines:** 12
**Generated:** 2025-11-15T20:37:32.023576Z

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

- **Path:** `packages/preview-server/src/utils/get-line-and-column-from-offset.ts`
- **Name:** `get-line-and-column-from-offset.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 339 bytes (0.33 KB)
- **Lines of Code:** 12

---

## Original Source

```typescript
export const getLineAndColumnFromOffset = (
  offset: number,
  content: string,
): [line: number, column: number] => {
  const lineBreaks = [...content.slice(0, offset).matchAll(/\n|\r|\r\n/g)];

  const line = lineBreaks.length + 1;
  const column = offset - (lineBreaks[lineBreaks.length - 1]?.index ?? 0);

  return [line, column];
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `column()`
- `getLineAndColumnFromOffset()`
- `line()`
- `lineBreaks()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 12

- `column`
- `content`
- `getLineAndColumnFromOffset`
- `index`
- `length`
- `line`
- `lineBreaks`
- `matchAll`
- `number`
- `offset`
- `slice`
- `string`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

