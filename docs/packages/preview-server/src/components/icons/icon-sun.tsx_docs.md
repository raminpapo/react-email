# Documentation: icon-sun.tsx
**File Path:** `packages/preview-server/src/components/icons/icon-sun.tsx`
**Language:** tsx
**Size:** 1,576 bytes
**Lines:** 75
**Generated:** 2025-11-15T20:37:32.166781Z

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

- **Path:** `packages/preview-server/src/components/icons/icon-sun.tsx`
- **Name:** `icon-sun.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,576 bytes (1.54 KB)
- **Lines of Code:** 75

---

## Original Source

```tsx
import type { IconProps } from './icon-base';
import { IconBase } from './icon-base';

export const IconSun = ({ ...props }: IconProps) => (
  <IconBase {...props}>
    <circle
      cx="12"
      cy="12"
      r="4"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
    <path
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M12 2v2"
    />
    <path
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M12 20v2"
    />
    <path
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      d="m4.93 4.93 1.41 1.41"
    />
    <path
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      d="m17.66 17.66 1.41 1.41"
    />
    <path
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M2 12h2"
    />
    <path
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M20 12h2"
    />
    <path
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      d="m6.34 17.66-1.41 1.41"
    />
    <path
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      d="m19.07 4.93-1.41 1.41"
    />
  </IconBase>
);

IconSun.displayName = 'IconSun';

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `IconSun()`

### Dependencies

This file imports/requires:

- `./icon-base`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 20

- `IconBase`
- `IconProps`
- `IconSun`
- `M12`
- `M20`
- `base`
- `circle`
- `currentColor`
- `displayName`
- `icon`
- `m17`
- `m19`
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

