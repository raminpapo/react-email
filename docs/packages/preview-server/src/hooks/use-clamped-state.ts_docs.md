# Documentation: use-clamped-state.ts
**File Path:** `packages/preview-server/src/hooks/use-clamped-state.ts`
**Language:** typescript
**Size:** 667 bytes
**Lines:** 25
**Generated:** 2025-11-15T20:37:32.002641Z

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

- **Path:** `packages/preview-server/src/hooks/use-clamped-state.ts`
- **Name:** `use-clamped-state.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 667 bytes (0.65 KB)
- **Lines of Code:** 25

---

## Original Source

```typescript
import { useState } from 'react';

const clamp = (v: number, min: number, max: number) => {
  return Math.min(Math.max(v, min), max);
};

export const useClampedState = (initial: number, min: number, max: number) => {
  const [v, setV] = useState(initial);

  return [
    clamp(v, min, max),
    (valueOrFunction: number | ((v: number) => number)) => {
      if (typeof valueOrFunction === 'function') {
        setV((value: number) => {
          const currentValue = clamp(value, min, max);

          return clamp(valueOrFunction(currentValue), min, max);
        });
      } else {
        setV(clamp(valueOrFunction, min, max));
      }
    },
  ] as const;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `clamp()`
- `currentValue()`
- `useClampedState()`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 13

- `Math`
- `clamp`
- `currentValue`
- `initial`
- `max`
- `min`
- `number`
- `react`
- `setV`
- `useClampedState`
- `useState`
- `value`
- `valueOrFunction`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

