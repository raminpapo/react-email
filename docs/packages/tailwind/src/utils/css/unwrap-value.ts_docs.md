# Documentation: unwrap-value.ts
**File Path:** `packages/tailwind/src/utils/css/unwrap-value.ts`
**Language:** typescript
**Size:** 221 bytes
**Lines:** 10
**Generated:** 2025-11-15T20:37:32.475950Z

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

- **Path:** `packages/tailwind/src/utils/css/unwrap-value.ts`
- **Name:** `unwrap-value.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 221 bytes (0.22 KB)
- **Lines of Code:** 10

---

## Original Source

```typescript
import type { Raw, Value } from 'css-tree';

export function unwrapValue(value: Value | Raw) {
  if (value.type === 'Value' && value.children.size === 1) {
    return value.children.first ?? value;
  }

  return value;
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `unwrapValue()`

### Dependencies

This file imports/requires:

- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 10

- `Raw`
- `Value`
- `children`
- `css`
- `first`
- `size`
- `tree`
- `type`
- `unwrapValue`
- `value`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

