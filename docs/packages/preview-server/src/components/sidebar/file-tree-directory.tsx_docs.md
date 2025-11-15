# Documentation: file-tree-directory.tsx
**File Path:** `packages/preview-server/src/components/sidebar/file-tree-directory.tsx`
**Language:** tsx
**Size:** 2,862 bytes
**Lines:** 93
**Generated:** 2025-11-15T20:37:32.188457Z

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

- **Path:** `packages/preview-server/src/components/sidebar/file-tree-directory.tsx`
- **Name:** `file-tree-directory.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,862 bytes (2.79 KB)
- **Lines of Code:** 93

---

## Original Source

```tsx
'use client';
import * as Collapsible from '@radix-ui/react-collapsible';
import * as React from 'react';
import { cn } from '../../utils';
import type { EmailsDirectory } from '../../utils/get-emails-directory-metadata';
import { Heading } from '../heading';
import { IconArrowDown } from '../icons/icon-arrow-down';
import { IconFolder } from '../icons/icon-folder';
import { IconFolderOpen } from '../icons/icon-folder-open';
import { FileTreeDirectoryChildren } from './file-tree-directory-children';

interface SidebarDirectoryProps {
  emailsDirectoryMetadata: EmailsDirectory;
  className?: string;
  currentEmailOpenSlug?: string;
}

const persistedOpenDirectories = new Set<string>();

export const FileTreeDirectory = ({
  emailsDirectoryMetadata: directoryMetadata,
  className,
  currentEmailOpenSlug,
}: SidebarDirectoryProps) => {
  const doesDirectoryContainCurrentEmailOpen = currentEmailOpenSlug
    ? currentEmailOpenSlug.includes(directoryMetadata.relativePath)
    : false;

  const isEmpty =
    directoryMetadata.emailFilenames.length === 0 &&
    directoryMetadata.subDirectories.length === 0;

  const [open, setOpen] = React.useState(
    persistedOpenDirectories.has(directoryMetadata.absolutePath) ||
      doesDirectoryContainCurrentEmailOpen,
  );

  return (
    <Collapsible.Root
      className={cn('group', className)}
      onOpenChange={(isOpening) => {
        if (isOpening) {
          persistedOpenDirectories.add(directoryMetadata.absolutePath);
        } else {
          persistedOpenDirectories.delete(directoryMetadata.absolutePath);
        }

        setOpen(isOpening);
      }}
      open={open}
    >
      <Collapsible.Trigger
        className={cn(
          'mt-1 mb-1.5 flex w-full items-center text-start justify-between gap-2 font-medium text-[14px]',
          {
            'cursor-pointer': !isEmpty,
          },
        )}
      >
        {open ? (
          <IconFolderOpen className="w-[20px]" height="20" width="20" />
        ) : (
          <IconFolder height="20" width="20" />
        )}
        <Heading
          as="h3"
          className="transition grow w-[calc(100%-40px)] truncate duration-200 ease-in-out hover:text-slate-12"
          color="gray"
          size="2"
          weight="medium"
        >
          {directoryMetadata.directoryName}
        </Heading>
        {!isEmpty ? (
          <IconArrowDown
            width="20"
            height="20"
            className="ml-auto opacity-60 transition-transform data-[open=true]:rotate-180"
            data-open={open}
          />
        ) : null}
      </Collapsible.Trigger>
      {!isEmpty ? (
        <FileTreeDirectoryChildren
          currentEmailOpenSlug={currentEmailOpenSlug}
          emailsDirectoryMetadata={directoryMetadata}
          open={open}
        />
      ) : null}
    </Collapsible.Root>
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

- `FileTreeDirectory()`
- `doesDirectoryContainCurrentEmailOpen()`
- `isEmpty()`
- `persistedOpenDirectories()`

### Interfaces

- `SidebarDirectoryProps`

### Dependencies

This file imports/requires:

- `../../utils`
- `../../utils/get-emails-directory-metadata`
- `../heading`
- `../icons/icon-arrow-down`
- `../icons/icon-folder`
- `../icons/icon-folder-open`
- `./file-tree-directory-children`
- `@radix-ui/react-collapsible`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 90

- `Collapsible`
- `EmailsDirectory`
- `FileTreeDirectory`
- `FileTreeDirectoryChildren`
- `Heading`
- `IconArrowDown`
- `IconFolder`
- `IconFolderOpen`
- `React`
- `Root`
- `Set`
- `SidebarDirectoryProps`
- `Trigger`
- `absolutePath`
- `add`
- `arrow`
- `auto`
- `between`
- `calc`
- `center`
- `children`
- `className`
- `client`
- `collapsible`
- `color`
- `currentEmailOpenSlug`
- `cursor`
- `data`
- `delete`
- `directory`
- `directoryMetadata`
- `directoryName`
- `doesDirectoryContainCurrentEmailOpen`
- `down`
- `duration`
- `ease`
- `emailFilenames`
- `emails`
- `emailsDirectoryMetadata`
- `file`
- `flex`
- `folder`
- `font`
- `full`
- `gap`
- `get`
- `gray`
- `group`
- `grow`
- `heading`
- `height`
- `hover`
- `icon`
- `icons`
- `includes`
- `interface`
- `isEmpty`
- `isOpening`
- `items`
- `justify`
- `length`
- `medium`
- `metadata`
- `onOpenChange`
- `opacity`
- `open`
- `out`
- `persistedOpenDirectories`
- `pointer`
- `radix`
- `react`
- `relativePath`
- `rotate`
- `setOpen`
- `size`
- `slate`
- `start`
- `string`
- `subDirectories`
- `text`
- `transform`
- `transition`
- `tree`
- `truncate`
- `type`
- `use`
- `useState`
- `utils`
- `weight`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

