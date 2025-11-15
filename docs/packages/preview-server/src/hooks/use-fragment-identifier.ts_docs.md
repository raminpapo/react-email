# Documentation: use-fragment-identifier.ts
**File Path:** `packages/preview-server/src/hooks/use-fragment-identifier.ts`
**Language:** typescript
**Size:** 441 bytes
**Lines:** 15
**Generated:** 2025-11-15T20:37:32.004870Z

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

- **Path:** `packages/preview-server/src/hooks/use-fragment-identifier.ts`
- **Name:** `use-fragment-identifier.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 441 bytes (0.43 KB)
- **Lines of Code:** 15

---

## Original Source

```typescript
import { usePathname, useSearchParams } from 'next/navigation';
import { useEffect, useState } from 'react';

export const useFragmentIdentifier = () => {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const [fragmentIdentifier, setFragmentIdentifier] = useState<string>();

  useEffect(() => {
    setFragmentIdentifier(global.location?.hash);
  }, [pathname, searchParams]);

  return fragmentIdentifier;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `pathname()`
- `searchParams()`
- `useFragmentIdentifier()`

### Dependencies

This file imports/requires:

- `next/navigation`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 16

- `fragmentIdentifier`
- `global`
- `hash`
- `location`
- `navigation`
- `next`
- `pathname`
- `react`
- `searchParams`
- `setFragmentIdentifier`
- `string`
- `useEffect`
- `useFragmentIdentifier`
- `usePathname`
- `useSearchParams`
- `useState`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

