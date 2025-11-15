# Documentation: hr.tsx
**File Path:** `packages/hr/src/hr.tsx`
**Language:** tsx
**Size:** 407 bytes
**Lines:** 21
**Generated:** 2025-11-15T20:37:32.233263Z

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

- **Path:** `packages/hr/src/hr.tsx`
- **Name:** `hr.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 407 bytes (0.40 KB)
- **Lines of Code:** 21

---

## Original Source

```tsx
import * as React from 'react';

export type HrProps = Readonly<React.ComponentPropsWithoutRef<'hr'>>;

export const Hr = React.forwardRef<HTMLHRElement, HrProps>(
  ({ style, ...props }, ref) => (
    <hr
      {...props}
      ref={ref}
      style={{
        width: '100%',
        border: 'none',
        borderTop: '1px solid #eaeaea',
        ...style,
      }}
    />
  ),
);

Hr.displayName = 'Hr';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Hr()`

### Type Definitions

- `HrProps`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 17

- `ComponentPropsWithoutRef`
- `HTMLHRElement`
- `HrProps`
- `React`
- `Readonly`
- `border`
- `borderTop`
- `displayName`
- `eaeaea`
- `forwardRef`
- `props`
- `react`
- `ref`
- `solid`
- `style`
- `type`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

