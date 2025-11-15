# Documentation: use-cached-state.ts
**File Path:** `packages/preview-server/src/components/toolbar/use-cached-state.ts`
**Language:** typescript
**Size:** 888 bytes
**Lines:** 37
**Generated:** 2025-11-15T20:37:32.185320Z

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

- **Path:** `packages/preview-server/src/components/toolbar/use-cached-state.ts`
- **Name:** `use-cached-state.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 888 bytes (0.87 KB)
- **Lines of Code:** 37

---

## Original Source

```typescript
import { useSyncExternalStore } from 'react';

export const useCachedState = <T>(key: string) => {
  let value: T | undefined;
  if (
    'localStorage' in global &&
    typeof global.localStorage.getItem === 'function'
  ) {
    const storedValue = global.localStorage.getItem(key);
    if (storedValue !== null && storedValue !== 'undefined') {
      try {
        value = JSON.parse(storedValue) as T;
      } catch (_exception) {
        console.warn(
          'Failed to load stored value for',
          key,
          'with value',
          storedValue,
        );
      }
    }
  }

  return [
    useSyncExternalStore(
      () => () => {},
      () => value,
      () => undefined,
    ),
    function setValue(newValue: T | undefined) {
      if ('localStorage' in global) {
        global.localStorage.setItem(key, JSON.stringify(newValue));
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

- `setValue()`
- `storedValue()`
- `useCachedState()`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 21

- `Failed`
- `_exception`
- `console`
- `getItem`
- `global`
- `key`
- `load`
- `localStorage`
- `newValue`
- `parse`
- `react`
- `setItem`
- `setValue`
- `stored`
- `storedValue`
- `string`
- `stringify`
- `useCachedState`
- `useSyncExternalStore`
- `value`
- `warn`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

