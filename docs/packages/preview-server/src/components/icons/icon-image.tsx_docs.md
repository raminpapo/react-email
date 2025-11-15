# Documentation: icon-image.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-image.tsx`
**Language:** tsx
**Size:** 576 bytes
**Lines:** 20
**Generated:** 2025-11-15T20:37:32.155530Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-image.tsx`
- **Name:** `icon-image.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 576 bytes (0.56 KB)
- **Lines of Code:** 20

---

## Original Source

```tsx
import { forwardRef } from 'react';
import type { IconElement, IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconImage = forwardRef<IconElement, IconProps>((props, ref) => (
  <IconBase {...props} ref={ref}>
    <g
      fill="none"
      stroke="currentColor"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth="2"
    >
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />
      <circle cx="9" cy="9" r="2" />
      <path d="m21 15l-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
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

- `IconImage()`

### Dependencies

This file imports/requires:

- `./icon-base`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 24

- `IconBase`
- `IconElement`
- `IconImage`
- `IconProps`
- `base`
- `circle`
- `currentColor`
- `fill`
- `forwardRef`
- `height`
- `icon`
- `m21`
- `path`
- `props`
- `react`
- `rect`
- `ref`
- `round`
- `stroke`
- `strokeLinecap`
- `strokeLinejoin`
- `strokeWidth`
- `type`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

