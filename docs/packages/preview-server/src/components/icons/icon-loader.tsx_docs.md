# Documentation: icon-loader.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-loader.tsx`
**Language:** tsx
**Size:** 369 bytes
**Lines:** 17
**Generated:** 2025-11-15T20:37:32.158938Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-loader.tsx`
- **Name:** `icon-loader.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 369 bytes (0.36 KB)
- **Lines of Code:** 17

---

## Original Source

```tsx
import type { IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconLoader = (props: IconProps) => (
  <IconBase
    {...props}
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M21 12a9 9 0 1 1-6.219-8.56" />
  </IconBase>
);

IconLoader.displayName = 'IconLoader';

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconLoader()`

### Dependencies

This file imports/requires:

- `./icon-base`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 16

- `IconBase`
- `IconLoader`
- `IconProps`
- `M21`
- `base`
- `currentColor`
- `displayName`
- `icon`
- `path`
- `props`
- `round`
- `stroke`
- `strokeLinecap`
- `strokeLinejoin`
- `strokeWidth`
- `type`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

