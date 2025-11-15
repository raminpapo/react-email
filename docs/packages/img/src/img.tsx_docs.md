# Documentation: img.tsx
**File Path:** `packages/img/src/img.tsx`
**Language:** tsx
**Size:** 536 bytes
**Lines:** 26
**Generated:** 2025-11-15T20:37:31.461812Z

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

- **Path:** `packages/img/src/img.tsx`
- **Name:** `img.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 536 bytes (0.52 KB)
- **Lines of Code:** 26

---

## Original Source

```tsx
import * as React from 'react';

export type ImgProps = Readonly<React.ComponentPropsWithoutRef<'img'>>;

export const Img = React.forwardRef<HTMLImageElement, ImgProps>(
  ({ alt, src, width, height, style, ...props }, ref) => (
    <img
      {...props}
      alt={alt}
      height={height}
      ref={ref}
      src={src}
      style={{
        display: 'block',
        outline: 'none',
        border: 'none',
        textDecoration: 'none',
        ...style,
      }}
      width={width}
    />
  ),
);

Img.displayName = 'Img';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Img()`

### Type Definitions

- `ImgProps`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 23

- `ComponentPropsWithoutRef`
- `HTMLImageElement`
- `Img`
- `ImgProps`
- `React`
- `Readonly`
- `alt`
- `block`
- `border`
- `display`
- `displayName`
- `forwardRef`
- `height`
- `img`
- `outline`
- `props`
- `react`
- `ref`
- `src`
- `style`
- `textDecoration`
- `type`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

