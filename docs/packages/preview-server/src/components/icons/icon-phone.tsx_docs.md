# Documentation: icon-phone.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-phone.tsx`
**Language:** tsx
**Size:** 857 bytes
**Lines:** 27
**Generated:** 2025-11-15T20:37:32.162284Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-phone.tsx`
- **Name:** `icon-phone.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 857 bytes (0.84 KB)
- **Lines of Code:** 27

---

## Original Source

```tsx
import * as React from 'react';
import type { IconElement, IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconPhone = React.forwardRef<IconElement, Readonly<IconProps>>(
  ({ ...props }, forwardedRef) => (
    <IconBase ref={forwardedRef} {...props}>
      <path
        d="M6.75 6.75C6.75 5.64543 7.64543 4.75 8.75 4.75H15.25C16.3546 4.75 17.25 5.64543 17.25 6.75V17.25C17.25 18.3546 16.3546 19.25 15.25 19.25H8.75C7.64543 19.25 6.75 18.3546 6.75 17.25V6.75Z"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
      <path
        d="M12.25 16.75H11.75"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
      />
    </IconBase>
  ),
);

IconPhone.displayName = 'IconPhone';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconPhone()`

### Dependencies

This file imports/requires:

- `./icon-base`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 23

- `IconBase`
- `IconElement`
- `IconPhone`
- `IconProps`
- `M12`
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

