# Documentation: heading.tsx
**File Path:** `packages/heading/src/heading.tsx`
**Language:** tsx
**Size:** 690 bytes
**Lines:** 30
**Generated:** 2025-11-15T20:37:32.284850Z

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

- **Path:** `packages/heading/src/heading.tsx`
- **Name:** `heading.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 690 bytes (0.67 KB)
- **Lines of Code:** 30

---

## Original Source

```tsx
import * as React from 'react';
import type { As } from './utils/as';
import type { Margin } from './utils/spaces';
import { withMargin } from './utils/spaces';

export type HeadingAs = As<'h1', 'h2', 'h3', 'h4', 'h5', 'h6'>;
export type HeadingProps = HeadingAs & Margin;

export const Heading = React.forwardRef<
  HTMLHeadingElement,
  Readonly<HeadingProps>
>(
  (
    { as: Tag = 'h1', children, style, m, mx, my, mt, mr, mb, ml, ...props },
    ref,
  ) => {
    return (
      <Tag
        {...props}
        ref={ref}
        style={{ ...withMargin({ m, mx, my, mt, mr, mb, ml }), ...style }}
      >
        {children}
      </Tag>
    );
  },
);

Heading.displayName = 'Heading';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Heading()`

### Type Definitions

- `HeadingAs`
- `HeadingProps`

### Dependencies

This file imports/requires:

- `./utils/as`
- `./utils/spaces`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 19

- `HTMLHeadingElement`
- `Heading`
- `HeadingAs`
- `HeadingProps`
- `Margin`
- `React`
- `Readonly`
- `Tag`
- `children`
- `displayName`
- `forwardRef`
- `props`
- `react`
- `ref`
- `spaces`
- `style`
- `type`
- `utils`
- `withMargin`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

