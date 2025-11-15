# Documentation: anchor.tsx
**File Path:** `apps/web/src/components/anchor.tsx`
**Language:** tsx
**Size:** 515 bytes
**Lines:** 20
**Generated:** 2025-11-15T20:37:32.885636Z

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

- **Path:** `apps/web/src/components/anchor.tsx`
- **Name:** `anchor.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 515 bytes (0.50 KB)
- **Lines of Code:** 20

---

## Original Source

```tsx
import classNames from 'classnames';
import type * as React from 'react';

export function Anchor({ className, ...props }: React.ComponentProps<'a'>) {
  return (
    <a
      className={classNames(
        'rounded-sm outline-none transition-transform duration-200 ease-in-out',
        'hover:-translate-y-1',
        'focus:ring-2 focus:ring-white/20 focus:ring-offset-4 focus:ring-offset-black',
        'text-slate-12',
        className,
      )}
      {...props}
    >
      {props.children}
    </a>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Anchor()`

### Dependencies

This file imports/requires:

- `classnames`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 26

- `Anchor`
- `ComponentProps`
- `React`
- `black`
- `children`
- `className`
- `classNames`
- `classnames`
- `duration`
- `ease`
- `focus`
- `hover`
- `offset`
- `out`
- `outline`
- `props`
- `react`
- `ring`
- `rounded`
- `slate`
- `text`
- `transform`
- `transition`
- `translate`
- `type`
- `white`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

