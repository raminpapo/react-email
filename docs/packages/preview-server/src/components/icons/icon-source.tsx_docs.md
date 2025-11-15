# Documentation: icon-source.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-source.tsx`
**Language:** tsx
**Size:** 569 bytes
**Lines:** 20
**Generated:** 2025-11-15T20:37:32.164455Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-source.tsx`
- **Name:** `icon-source.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 569 bytes (0.56 KB)
- **Lines of Code:** 20

---

## Original Source

```tsx
import * as React from 'react';
import type { IconElement, IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconSource = React.forwardRef<IconElement, Readonly<IconProps>>(
  ({ ...props }, forwardedRef) => (
    <IconBase ref={forwardedRef} {...props}>
      <path
        d="M17.4 15L21 11.5L17.4 8M6.6 8L3 11.5L6.6 15M14.25 4.5L9.75 18.5"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
    </IconBase>
  ),
);

IconSource.displayName = 'IconSource';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconSource()`

### Dependencies

This file imports/requires:

- `./icon-base`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 23

- `IconBase`
- `IconElement`
- `IconProps`
- `IconSource`
- `M17`
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

