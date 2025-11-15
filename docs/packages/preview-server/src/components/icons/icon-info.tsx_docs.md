# Documentation: icon-info.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-info.tsx`
**Language:** tsx
**Size:** 1,157 bytes
**Lines:** 19
**Generated:** 2025-11-15T20:37:32.156655Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-info.tsx`
- **Name:** `icon-info.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,157 bytes (1.13 KB)
- **Lines of Code:** 19

---

## Original Source

```tsx
import * as React from 'react';
import type { IconElement, IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconInfo = React.forwardRef<IconElement, Readonly<IconProps>>(
  ({ ...props }, forwardedRef) => (
    <IconBase ref={forwardedRef} {...props}>
      <path
        d="M12 4C7.58173 4 4 7.58172 4 12C4 16.4182 7.58173 20 12 20C16.4183 20 20 16.4182 20 12C20 7.58172 16.4183 4 12 4ZM5.14754 12C5.14754 8.21549 8.21551 5.14754 12 5.14754C15.7845 5.14754 18.8525 8.21549 18.8525 12C18.8525 15.7844 15.7845 18.8525 12 18.8525C8.21551 18.8525 5.14754 15.7844 5.14754 12ZM12.906 8.37648C12.906 8.87682 12.5004 9.28243 12 9.28243C11.4997 9.28243 11.0941 8.87682 11.0941 8.37648C11.0941 7.87613 11.4997 7.47053 12 7.47053C12.5004 7.47053 12.906 7.87613 12.906 8.37648ZM10.1883 10.1884H10.7922H12.0002C12.3337 10.1884 12.6041 10.4588 12.6041 10.7924V15.0201H13.2081H13.8121V16.2281H13.2081H12.0002H10.7922H10.1883V15.0201H10.7922H11.3962V11.3963H10.7922H10.1883V10.1884Z"
        fill="currentColor"
        fillRule="evenodd"
        clipRule="evenodd"
      />
    </IconBase>
  ),
);

IconInfo.displayName = 'IconInfo';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconInfo()`

### Dependencies

This file imports/requires:

- `./icon-base`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 22

- `IconBase`
- `IconElement`
- `IconInfo`
- `IconProps`
- `M12`
- `React`
- `Readonly`
- `base`
- `clipRule`
- `currentColor`
- `displayName`
- `evenodd`
- `fill`
- `fillRule`
- `forwardRef`
- `forwardedRef`
- `icon`
- `path`
- `props`
- `react`
- `ref`
- `type`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

