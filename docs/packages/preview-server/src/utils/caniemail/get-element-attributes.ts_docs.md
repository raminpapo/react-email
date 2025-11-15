# Documentation: get-element-attributes.ts
**File Path:** `packages/preview-server/src/utils/caniemail/get-element-attributes.ts`
**Language:** typescript
**Size:** 158 bytes
**Lines:** 8
**Generated:** 2025-11-15T20:37:32.048342Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/get-element-attributes.ts`
- **Name:** `get-element-attributes.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 158 bytes (0.15 KB)
- **Lines of Code:** 8

---

## Original Source

```typescript
export function getElementAttributes(title: string) {
  if (title.endsWith(' attribute')) {
    return [title.replace(' attribute', '')];
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

- `getElementAttributes()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 6

- `attribute`
- `endsWith`
- `getElementAttributes`
- `replace`
- `string`
- `title`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

