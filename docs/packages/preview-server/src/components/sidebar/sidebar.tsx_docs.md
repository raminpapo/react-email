# Documentation: sidebar.tsx
**File Path:** `packages/preview-server/src/components/sidebar/sidebar.tsx`
**Language:** tsx
**Size:** 1,198 bytes
**Lines:** 44
**Generated:** 2025-11-15T20:37:32.192084Z

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

- **Path:** `packages/preview-server/src/components/sidebar/sidebar.tsx`
- **Name:** `sidebar.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,198 bytes (1.17 KB)
- **Lines of Code:** 44

---

## Original Source

```tsx
'use client';
import { clsx } from 'clsx';
import { useEmails } from '../../contexts/emails';
import { cn } from '../../utils';
import { Logo } from '../logo';
import { FileTree } from './file-tree';

interface SidebarProps {
  className?: string;
  currentEmailOpenSlug?: string;
}

export const Sidebar = ({ className, currentEmailOpenSlug }: SidebarProps) => {
  const { emailsDirectoryMetadata } = useEmails();

  return (
    <aside
      className={cn(
        'overflow-hidden',
        'lg:static lg:z-auto lg:max-h-screen lg:w-[16rem]',
        className,
      )}
    >
      <div className="flex w-full h-full overflow-hidden flex-col border-slate-6 border-r">
        <div
          className={clsx(
            'hidden min-h-14 flex-shrink items-center py-2 px-3 lg:flex border-b border-slate-4',
          )}
        >
          <h2>
            <Logo />
          </h2>
        </div>
        <div className="relative grow w-full h-full overflow-y-auto overflow-x-hidden px-4 pb-3">
          <FileTree
            currentEmailOpenSlug={currentEmailOpenSlug}
            emailsDirectoryMetadata={emailsDirectoryMetadata}
          />
        </div>
      </div>
    </aside>
  );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Sidebar()`

### Interfaces

- `SidebarProps`

### Dependencies

This file imports/requires:

- `../../contexts/emails`
- `../../utils`
- `../logo`
- `./file-tree`
- `clsx`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 38

- `FileTree`
- `Logo`
- `Sidebar`
- `SidebarProps`
- `aside`
- `auto`
- `border`
- `center`
- `className`
- `client`
- `clsx`
- `col`
- `contexts`
- `currentEmailOpenSlug`
- `div`
- `emails`
- `emailsDirectoryMetadata`
- `file`
- `flex`
- `full`
- `grow`
- `hidden`
- `interface`
- `items`
- `logo`
- `max`
- `min`
- `overflow`
- `relative`
- `screen`
- `shrink`
- `slate`
- `static`
- `string`
- `tree`
- `use`
- `useEmails`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

