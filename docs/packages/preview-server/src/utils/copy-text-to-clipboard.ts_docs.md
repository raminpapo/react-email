# Documentation: copy-text-to-clipboard.ts
**File Path:** `packages/preview-server/src/utils/copy-text-to-clipboard.ts`
**Language:** typescript
**Size:** 176 bytes
**Lines:** 8
**Generated:** 2025-11-15T20:37:32.014043Z

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

- **Path:** `packages/preview-server/src/utils/copy-text-to-clipboard.ts`
- **Name:** `copy-text-to-clipboard.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 176 bytes (0.17 KB)
- **Lines of Code:** 8

---

## Original Source

```typescript
export const copyTextToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text);
  } catch {
    throw new Error('Not able to copy');
  }
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `copyTextToClipboard()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 9

- `Error`
- `able`
- `clipboard`
- `copy`
- `copyTextToClipboard`
- `navigator`
- `string`
- `text`
- `writeText`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

