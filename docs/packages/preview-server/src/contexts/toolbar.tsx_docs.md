# Documentation: toolbar.tsx
**File Path:** `packages/preview-server/src/contexts/toolbar.tsx`
**Language:** tsx
**Size:** 772 bytes
**Lines:** 36
**Generated:** 2025-11-15T20:37:32.100288Z

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

- **Path:** `packages/preview-server/src/contexts/toolbar.tsx`
- **Name:** `toolbar.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 772 bytes (0.75 KB)
- **Lines of Code:** 36

---

## Original Source

```tsx
'use client';

import { createContext, use } from 'react';

const ToolbarContext = createContext<
  | {
      hasSetupResendIntegration: boolean;
    }
  | undefined
>(undefined);

interface ToolbarProviderProps {
  hasApiKey: boolean;
  children: React.ReactNode;
}

export function ToolbarProvider({ hasApiKey, children }: ToolbarProviderProps) {
  return (
    <ToolbarContext.Provider value={{ hasSetupResendIntegration: hasApiKey }}>
      {children}
    </ToolbarContext.Provider>
  );
}

export const useToolbarContext = () => {
  const previewContext = use(ToolbarContext);

  if (typeof previewContext === 'undefined') {
    throw new Error(
      'Cannot call `useToolbarContext` outside of a `ToolbarContext` provider.',
    );
  }

  return previewContext;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `ToolbarContext()`
- `ToolbarProvider()`
- `previewContext()`
- `useToolbarContext()`

### Interfaces

- `ToolbarProviderProps`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 23

- `Cannot`
- `Error`
- `Provider`
- `React`
- `ReactNode`
- `ToolbarContext`
- `ToolbarProvider`
- `ToolbarProviderProps`
- `boolean`
- `call`
- `children`
- `client`
- `createContext`
- `hasApiKey`
- `hasSetupResendIntegration`
- `interface`
- `outside`
- `previewContext`
- `provider`
- `react`
- `use`
- `useToolbarContext`
- `value`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

