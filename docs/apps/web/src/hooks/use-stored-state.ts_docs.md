# Documentation: use-stored-state.ts
**File Path:** `apps/web/src/hooks/use-stored-state.ts`
**Language:** typescript
**Size:** 554 bytes
**Lines:** 25
**Generated:** 2025-11-15T20:37:32.801037Z

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

- **Path:** `apps/web/src/hooks/use-stored-state.ts`
- **Name:** `use-stored-state.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 554 bytes (0.54 KB)
- **Lines of Code:** 25

---

## Original Source

```typescript
import * as React from 'react';

export const useStoredState = <T extends string | undefined>(
  key: string,
  defaultValue: T,
): [state: T, setState: (newValue: T) => void] => {
  const [state, setState] = React.useState<T>(defaultValue);
  React.useEffect(() => {
    const storedValue = localStorage.getItem(key);
    if (storedValue) {
      setState(storedValue as T);
    }
  }, [key]);

  return [
    state,
    (newValue) => {
      if (newValue) {
        localStorage.setItem(key, newValue);
      }
      setState(newValue);
    },
  ];
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `storedValue()`
- `useStoredState()`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 17

- `React`
- `defaultValue`
- `extends`
- `getItem`
- `key`
- `localStorage`
- `newValue`
- `react`
- `setItem`
- `setState`
- `state`
- `storedValue`
- `string`
- `useEffect`
- `useState`
- `useStoredState`
- `void`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

