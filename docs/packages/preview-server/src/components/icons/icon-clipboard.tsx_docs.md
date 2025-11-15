# Documentation: icon-clipboard.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-clipboard.tsx`
**Language:** tsx
**Size:** 1,336 bytes
**Lines:** 41
**Generated:** 2025-11-15T20:37:32.145392Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-clipboard.tsx`
- **Name:** `icon-clipboard.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,336 bytes (1.30 KB)
- **Lines of Code:** 41

---

## Original Source

```tsx
import * as React from 'react';
import type { IconElement, IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconClipboard = React.forwardRef<IconElement, Readonly<IconProps>>(
  ({ ...props }, forwardedRef) => (
    <IconBase ref={forwardedRef} {...props}>
      <path
        d="M9 6.75H7.75C6.64543 6.75 5.75 7.64543 5.75 8.75V17.25C5.75 18.3546 6.64543 19.25 7.75 19.25H16.25C17.3546 19.25 18.25 18.3546 18.25 17.25V8.75C18.25 7.64543 17.3546 6.75 16.25 6.75H15"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
      <path
        d="M14 8.25H10C9.44772 8.25 9 7.80228 9 7.25V5.75C9 5.19772 9.44772 4.75 10 4.75H14C14.5523 4.75 15 5.19772 15 5.75V7.25C15 7.80228 14.5523 8.25 14 8.25Z"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
      <path
        d="M9.75 12.25H14.25"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
      <path
        d="M9.75 15.25H14.25"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
    </IconBase>
  ),
);

IconClipboard.displayName = 'IconClipboard';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconClipboard()`

### Dependencies

This file imports/requires:

- `./icon-base`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 23

- `IconBase`
- `IconClipboard`
- `IconElement`
- `IconProps`
- `M14`
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

