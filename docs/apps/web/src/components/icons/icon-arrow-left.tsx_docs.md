# Documentation: icon-arrow-left.tsx
**File Path:** `apps/web/src/components/icons/icon-arrow-left.tsx`
**Language:** tsx
**Size:** 708 bytes
**Lines:** 27
**Generated:** 2025-11-15T20:37:32.923062Z

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

- **Path:** `apps/web/src/components/icons/icon-arrow-left.tsx`
- **Name:** `icon-arrow-left.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 708 bytes (0.69 KB)
- **Lines of Code:** 27

---

## Original Source

```tsx
import * as React from 'react';
import type { IconElement, IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconArrowLeft = React.forwardRef<IconElement, Readonly<IconProps>>(
  ({ ...props }, forwardedRef) => (
    <IconBase ref={forwardedRef} {...props}>
      <path
        d="M10.25 6.75L4.75 12L10.25 17.25"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
      <path
        d="M19.25 12H5"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
    </IconBase>
  ),
);

IconArrowLeft.displayName = 'IconArrowLeft';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconArrowLeft()`

### Dependencies

This file imports/requires:

- `./icon-base`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 24

- `IconArrowLeft`
- `IconBase`
- `IconElement`
- `IconProps`
- `M10`
- `M19`
- `React`
- `Readonly`
- `base`
- `currentColor`
- `displayName`
- `forwardRef`
- `forwardedRef`
- `icon`
- `path`
- `props`
- `react`
- `ref`
- `round`
- `stroke`
- `strokeLinecap`
- `strokeLinejoin`
- `strokeWidth`
- `type`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

