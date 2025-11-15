# Documentation: icon-moon.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-moon.tsx`
**Language:** tsx
**Size:** 464 bytes
**Lines:** 17
**Generated:** 2025-11-15T20:37:32.161144Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-moon.tsx`
- **Name:** `icon-moon.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 464 bytes (0.45 KB)
- **Lines of Code:** 17

---

## Original Source

```tsx
import type { IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconMoon = ({ ...props }: IconProps) => (
  <IconBase {...props}>
    <path
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M20.985 12.486a9 9 0 1 1-9.473-9.472c.405-.022.617.46.402.803a6 6 0 0 0 8.268 8.268c.344-.215.825-.004.803.401"
    />
  </IconBase>
);

IconMoon.displayName = 'IconMoon';

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconMoon()`

### Dependencies

This file imports/requires:

- `./icon-base`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 16

- `IconBase`
- `IconMoon`
- `IconProps`
- `M20`
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

