# Documentation: icon-check.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-check.tsx`
**Language:** tsx
**Size:** 538 bytes
**Lines:** 20
**Generated:** 2025-11-15T20:37:32.144268Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-check.tsx`
- **Name:** `icon-check.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 538 bytes (0.53 KB)
- **Lines of Code:** 20

---

## Original Source

```tsx
import * as React from 'react';
import type { IconElement, IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconCheck = React.forwardRef<IconElement, Readonly<IconProps>>(
  ({ ...props }, forwardedRef) => (
    <IconBase ref={forwardedRef} {...props}>
      <path
        d="M16.25 8.75L10.406 15.25L7.75 12.75"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
    </IconBase>
  ),
);

IconCheck.displayName = 'IconCheck';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconCheck()`

### Dependencies

This file imports/requires:

- `./icon-base`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 23

- `IconBase`
- `IconCheck`
- `IconElement`
- `IconProps`
- `M16`
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

