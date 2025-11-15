# Documentation: topbar.tsx
**File Path:** `packages/preview-server/src/components/topbar.tsx`
**Language:** tsx
**Size:** 1,780 bytes
**Lines:** 60
**Generated:** 2025-11-15T20:37:32.138365Z

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

- **Path:** `packages/preview-server/src/components/topbar.tsx`
- **Name:** `topbar.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,780 bytes (1.74 KB)
- **Lines of Code:** 60

---

## Original Source

```tsx
'use client';

import { use } from 'react';
import { cn } from '../utils';
import { Heading } from './heading';
import { IconHideSidebar } from './icons/icon-hide-sidebar';
import { ShellContext } from './shell';
import { Tooltip } from './tooltip';

interface TopbarProps extends React.ComponentProps<'header'> {
  emailTitle: string;
  children: React.ReactNode;
}

export const Topbar = ({
  emailTitle,
  children,
  className,
  ...props
}: TopbarProps) => {
  const { toggleSidebar } = use(ShellContext)!;

  return (
    <Tooltip.Provider>
      <header
        {...props}
        className={cn(
          'flex h-14 items-center justify-between gap-3 border-slate-6 border-b px-3 py-2',
          className,
        )}
      >
        <div className="flex w-fit items-center gap-3">
          <Tooltip>
            <Tooltip.Trigger asChild>
              <button
                className="hidden rounded-lg px-2 py-2 text-slate-11 transition duration-200 ease-in-out hover:bg-slate-5 hover:text-slate-12 lg:flex"
                onClick={() => {
                  toggleSidebar();
                }}
                type="button"
              >
                <IconHideSidebar height={20} width={20} />
              </button>
            </Tooltip.Trigger>
            <Tooltip.Content>Show/hide sidebar</Tooltip.Content>
          </Tooltip>
          <div className="hidden items-center overflow-hidden text-center lg:flex">
            <Heading as="h2" className="truncate" size="2" weight="medium">
              {emailTitle}
            </Heading>
          </div>
        </div>
        <div className="flex w-full items-center justify-between gap-3 lg:w-fit lg:justify-start">
          {children}
        </div>
      </header>
    </Tooltip.Provider>
  );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Topbar()`

### Interfaces

- `TopbarProps`

### Dependencies

This file imports/requires:

- `../utils`
- `./heading`
- `./icons/icon-hide-sidebar`
- `./shell`
- `./tooltip`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 64

- `ComponentProps`
- `Content`
- `Heading`
- `IconHideSidebar`
- `Provider`
- `React`
- `ReactNode`
- `ShellContext`
- `Show`
- `Tooltip`
- `Topbar`
- `TopbarProps`
- `Trigger`
- `asChild`
- `between`
- `border`
- `button`
- `center`
- `children`
- `className`
- `client`
- `div`
- `duration`
- `ease`
- `emailTitle`
- `extends`
- `fit`
- `flex`
- `full`
- `gap`
- `header`
- `heading`
- `height`
- `hidden`
- `hide`
- `hover`
- `icon`
- `icons`
- `interface`
- `items`
- `justify`
- `medium`
- `onClick`
- `out`
- `overflow`
- `props`
- `react`
- `rounded`
- `shell`
- `sidebar`
- `size`
- `slate`
- `start`
- `string`
- `text`
- `toggleSidebar`
- `tooltip`
- `transition`
- `truncate`
- `type`
- `use`
- `utils`
- `weight`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

