# Documentation: topbar.tsx
**File Path:** `apps/web/src/components/topbar.tsx`
**Language:** tsx
**Size:** 712 bytes
**Lines:** 29
**Generated:** 2025-11-15T20:37:32.921896Z

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

- **Path:** `apps/web/src/components/topbar.tsx`
- **Name:** `topbar.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 712 bytes (0.70 KB)
- **Lines of Code:** 29

---

## Original Source

```tsx
import classNames from 'classnames';
import Link from 'next/link';
import type * as React from 'react';
import { Logo } from './logo';
import { Menu } from './menu';

export function Topbar({
  className,
  ...props
}: Omit<React.ComponentProps<'header'>, 'children'>) {
  return (
    <header
      className={classNames(
        'relative z-50 flex items-center justify-between py-8 px-6 md:px-8',
        className,
      )}
      {...props}
    >
      <Link
        className="-ml-[.375rem] flex scroll-m-2 rounded-md pr-[.375rem] transition-colors focus:outline-none focus-visible:ring focus-visible:ring-slate-4"
        href="/"
      >
        <Logo />
      </Link>
      <Menu />
    </header>
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

- `Topbar()`

### Dependencies

This file imports/requires:

- `./logo`
- `./menu`
- `classnames`
- `next/link`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 35

- `ComponentProps`
- `Link`
- `Logo`
- `Menu`
- `Omit`
- `React`
- `Topbar`
- `between`
- `center`
- `children`
- `className`
- `classNames`
- `classnames`
- `colors`
- `flex`
- `focus`
- `header`
- `href`
- `items`
- `justify`
- `link`
- `logo`
- `menu`
- `next`
- `outline`
- `props`
- `react`
- `relative`
- `ring`
- `rounded`
- `scroll`
- `slate`
- `transition`
- `type`
- `visible`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

