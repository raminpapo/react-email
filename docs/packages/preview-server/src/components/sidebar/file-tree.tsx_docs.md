# Documentation: file-tree.tsx
**File Path:** `packages/preview-server/src/components/sidebar/file-tree.tsx`
**Language:** tsx
**Size:** 984 bytes
**Lines:** 32
**Generated:** 2025-11-15T20:37:32.189829Z

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

- **Path:** `packages/preview-server/src/components/sidebar/file-tree.tsx`
- **Name:** `file-tree.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 984 bytes (0.96 KB)
- **Lines of Code:** 32

---

## Original Source

```tsx
import * as Collapsible from '@radix-ui/react-collapsible';
import * as React from 'react';
import type { EmailsDirectory } from '../../utils/get-emails-directory-metadata';
import { FileTreeDirectoryChildren } from './file-tree-directory-children';

interface FileTreeProps {
  currentEmailOpenSlug: string | undefined;
  emailsDirectoryMetadata: EmailsDirectory;
}

export const FileTree = ({
  currentEmailOpenSlug,
  emailsDirectoryMetadata,
}: FileTreeProps) => {
  return (
    <div className="flex w-full h-full flex-col lg:w-full lg:min-w-[14.5rem]">
      <nav className="flex flex-grow flex-col p-4 pr-0 pl-0">
        <Collapsible.Root open>
          <React.Suspense>
            <FileTreeDirectoryChildren
              currentEmailOpenSlug={currentEmailOpenSlug}
              emailsDirectoryMetadata={emailsDirectoryMetadata}
              isRoot
              open
            />
          </React.Suspense>
        </Collapsible.Root>
      </nav>
    </div>
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

- `FileTree()`

### Interfaces

- `FileTreeProps`

### Dependencies

This file imports/requires:

- `../../utils/get-emails-directory-metadata`
- `./file-tree-directory-children`
- `@radix-ui/react-collapsible`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 34

- `Collapsible`
- `EmailsDirectory`
- `FileTree`
- `FileTreeDirectoryChildren`
- `FileTreeProps`
- `React`
- `Root`
- `Suspense`
- `children`
- `className`
- `col`
- `collapsible`
- `currentEmailOpenSlug`
- `directory`
- `div`
- `emails`
- `emailsDirectoryMetadata`
- `file`
- `flex`
- `full`
- `get`
- `grow`
- `interface`
- `isRoot`
- `metadata`
- `min`
- `nav`
- `open`
- `radix`
- `react`
- `string`
- `tree`
- `type`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

