# Documentation: sanitize.ts
**File Path:** `packages/preview-server/src/utils/sanitize.ts`
**Language:** typescript
**Size:** 167 bytes
**Lines:** 7
**Generated:** 2025-11-15T20:37:32.033128Z

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

- **Path:** `packages/preview-server/src/utils/sanitize.ts`
- **Name:** `sanitize.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 167 bytes (0.16 KB)
- **Lines of Code:** 7

---

## Original Source

```typescript
/**
 * Sanitizes text by replacing underscores and hyphens with spaces
 */
export const sanitize = (text: string): string => {
  return text.replace(/[_-]/g, ' ');
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `sanitize()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 9

- `Sanitizes`
- `hyphens`
- `replace`
- `replacing`
- `sanitize`
- `spaces`
- `string`
- `text`
- `underscores`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

