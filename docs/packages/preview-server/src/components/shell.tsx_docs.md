# Documentation: shell.tsx
**File Path:** `packages/preview-server/src/components/shell.tsx`
**Language:** tsx
**Size:** 3,090 bytes
**Lines:** 96
**Generated:** 2025-11-15T20:37:32.129588Z

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

- **Path:** `packages/preview-server/src/components/shell.tsx`
- **Name:** `shell.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,090 bytes (3.02 KB)
- **Lines of Code:** 96

---

## Original Source

```tsx
'use client';

import * as React from 'react';
import { cn } from '../utils';
import { Logo } from './logo';
import { Sidebar } from './sidebar';

interface ShellProps {
  children: React.ReactNode;
  currentEmailOpenSlug?: string;
}

interface ShellContextValue {
  sidebarToggled: boolean;
  toggleSidebar: () => void;
}

export const ShellContext = React.createContext<ShellContextValue | undefined>(
  undefined,
);

export const Shell = ({ children, currentEmailOpenSlug }: ShellProps) => {
  const [sidebarToggled, setSidebarToggled] = React.useState(true);

  return (
    <ShellContext.Provider
      value={{
        toggleSidebar: () => setSidebarToggled((v) => !v),
        sidebarToggled,
      }}
    >
      <div
        className={
          'flex h-[4.375rem] items-center justify-between border-slate-6 border-b px-6 lg:hidden'
        }
      >
        <div className="flex h-[4.375rem] items-center">
          <Logo />
        </div>
        <button
          className="flex h-6 w-6 items-center justify-center rounded text-white"
          onClick={() => {
            setSidebarToggled((v) => !v);
          }}
          type="button"
        >
          <svg
            fill="none"
            height="16"
            stroke="white"
            viewBox="0 0 15 15"
            width="16"
            xmlns="http://www.w3.org/2000/svg"
          >
            <title>Menu</title>
            <path
              clipRule="evenodd"
              d="M1.5 3C1.22386 3 1 3.22386 1 3.5C1 3.77614 1.22386 4 1.5 4H13.5C13.7761 4 14 3.77614 14 3.5C14 3.22386 13.7761 3 13.5 3H1.5ZM1 7.5C1 7.22386 1.22386 7 1.5 7H13.5C13.7761 7 14 7.22386 14 7.5C14 7.77614 13.7761 8 13.5 8H1.5C1.22386 8 1 7.77614 1 7.5ZM1 11.5C1 11.2239 1.22386 11 1.5 11H13.5C13.7761 11 14 11.2239 14 11.5C14 11.7761 13.7761 12 13.5 12H1.5C1.22386 12 1 11.7761 1 11.5Z"
              fill="currentColor"
              fillRule="evenodd"
            />
          </svg>
        </button>
      </div>
      <div className="w-[100dvw] flex h-[calc(100dvh-4.375rem)] lg:h-[100dvh]">
        <React.Suspense>
          <Sidebar
            className={cn(
              'fixed top-[4.375rem] left-0 z-[9999] h-full max-h-full w-full max-w-full will-change-auto [transition:width_0.2s_ease-in-out]',
              'lg:static lg:inline-block lg:z-auto lg:max-h-full lg:w-[16rem]',
              {
                '-translate-x-full lg:translate-x-0': sidebarToggled,
                'lg:w-0': !sidebarToggled,
              },
            )}
            currentEmailOpenSlug={currentEmailOpenSlug}
          />
        </React.Suspense>
        <main
          className={cn(
            'inline-block relative overflow-hidden will-change-[width]',
            'w-full h-full',
            '[transition:width_0.2s_ease-in-out,_transform_0.2s_ease-in-out]',
            {
              'lg:w-[calc(100%-16rem)]': sidebarToggled,
              'opacity-0 lg:opacity-100': !sidebarToggled,
            },
          )}
        >
          {children}
        </main>
      </div>
    </ShellContext.Provider>
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

- `Shell()`
- `ShellContext()`

### Interfaces

- `ShellContextValue`
- `ShellProps`

### Dependencies

This file imports/requires:

- `../utils`
- `./logo`
- `./sidebar`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 81

- `Logo`
- `Menu`
- `Provider`
- `React`
- `ReactNode`
- `Shell`
- `ShellContext`
- `ShellContextValue`
- `ShellProps`
- `Sidebar`
- `Suspense`
- `_transform_0`
- `auto`
- `between`
- `block`
- `boolean`
- `border`
- `button`
- `calc`
- `center`
- `change`
- `children`
- `className`
- `client`
- `clipRule`
- `createContext`
- `currentColor`
- `currentEmailOpenSlug`
- `div`
- `evenodd`
- `fill`
- `fillRule`
- `fixed`
- `flex`
- `full`
- `height`
- `hidden`
- `http`
- `inline`
- `interface`
- `items`
- `justify`
- `left`
- `logo`
- `main`
- `max`
- `onClick`
- `opacity`
- `org`
- `out`
- `overflow`
- `path`
- `react`
- `relative`
- `rounded`
- `setSidebarToggled`
- `sidebar`
- `sidebarToggled`
- `slate`
- `static`
- `string`
- `stroke`
- `svg`
- `text`
- `title`
- `toggleSidebar`
- `top`
- `transition`
- `translate`
- `type`
- `use`
- `useState`
- `utils`
- `value`
- `viewBox`
- `void`
- `white`
- `width`
- `width_0`
- `www`
- `xmlns`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

