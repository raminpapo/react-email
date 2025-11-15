# Documentation: sleep.ts
**File Path:** `packages/preview-server/src/utils/sleep.ts`
**Language:** typescript
**Size:** 98 bytes
**Lines:** 4
**Generated:** 2025-11-15T20:37:32.034234Z

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

- **Path:** `packages/preview-server/src/utils/sleep.ts`
- **Name:** `sleep.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 98 bytes (0.10 KB)
- **Lines of Code:** 4

---

## Original Source

```typescript
export function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `sleep()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 5

- `Promise`
- `number`
- `resolve`
- `setTimeout`
- `sleep`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

