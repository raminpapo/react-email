# Documentation: icon-bug.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-bug.tsx`
**Language:** tsx
**Size:** 730 bytes
**Lines:** 20
**Generated:** 2025-11-15T20:37:32.141933Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-bug.tsx`
- **Name:** `icon-bug.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 730 bytes (0.71 KB)
- **Lines of Code:** 20

---

## Original Source

```tsx
import { forwardRef } from 'react';
import type { IconElement, IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconBug = forwardRef<IconElement, IconProps>((props, ref) => (
  <IconBase {...props} ref={ref}>
    <g
      fill="none"
      stroke="currentColor"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth="2"
    >
      <path d="m8 2l1.88 1.88m4.24 0L16 2M9 7.13v-1a3.003 3.003 0 1 1 6 0v1" />
      <path d="M12 20c-3.3 0-6-2.7-6-6v-3a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v3c0 3.3-2.7 6-6 6m0 0v-9" />
      <path d="M6.53 9C4.6 8.8 3 7.1 3 5m3 8H2m1 8c0-2.1 1.7-3.9 3.8-4M20.97 5c0 2.1-1.6 3.8-3.5 4M22 13h-4m-.8 4c2.1.1 3.8 1.9 3.8 4" />
    </g>
  </IconBase>
));

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconBug()`

### Dependencies

This file imports/requires:

- `./icon-base`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 20

- `IconBase`
- `IconBug`
- `IconElement`
- `IconProps`
- `M12`
- `base`
- `currentColor`
- `fill`
- `forwardRef`
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

