# Documentation: file-tree-directory-children.tsx
**File Path:** `packages/preview-server/src/components/sidebar/file-tree-directory-children.tsx`
**Language:** tsx
**Size:** 6,007 bytes
**Lines:** 143
**Generated:** 2025-11-15T20:37:32.186705Z

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

- **Path:** `packages/preview-server/src/components/sidebar/file-tree-directory-children.tsx`
- **Name:** `file-tree-directory-children.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 6,007 bytes (5.87 KB)
- **Lines of Code:** 143

---

## Original Source

```tsx
import * as Collapsible from '@radix-ui/react-collapsible';
import { AnimatePresence, LayoutGroup, motion } from 'framer-motion';
import Link from 'next/link';
import { useRouter, useSearchParams } from 'next/navigation';
import * as React from 'react';
import { cn } from '../../utils';
import type { EmailsDirectory } from '../../utils/get-emails-directory-metadata';
import { IconFile } from '../icons/icon-file';
import { FileTreeDirectory } from './file-tree-directory';

export const FileTreeDirectoryChildren = (props: {
  emailsDirectoryMetadata: EmailsDirectory;
  currentEmailOpenSlug?: string;
  open: boolean;
  isRoot?: boolean;
}) => {
  const searchParams = useSearchParams();
  const router = useRouter();

  const id = React.useId();

  return (
    <AnimatePresence initial={false}>
      {props.open ? (
        <Collapsible.Content
          asChild
          className="relative overflow-y-hidden pl-1"
          forceMount
        >
          <motion.div
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            initial={{ opacity: 0, height: 0 }}
          >
            {props.isRoot ? null : (
              <div className="line absolute left-2.5 h-full w-px bg-slate-6" />
            )}
            <div className="flex flex-col truncate">
              <LayoutGroup id={`sidebar-${id}`}>
                {props.emailsDirectoryMetadata.subDirectories.map(
                  (subDirectory) => (
                    <FileTreeDirectory
                      className="p-0 data-[state=open]:mb-2"
                      currentEmailOpenSlug={props.currentEmailOpenSlug}
                      emailsDirectoryMetadata={subDirectory}
                      key={subDirectory.absolutePath}
                    />
                  ),
                )}
                {props.emailsDirectoryMetadata.emailFilenames.map(
                  (emailFilename, index) => {
                    const emailSlug = props.isRoot
                      ? emailFilename
                      : `${props.emailsDirectoryMetadata.relativePath}/${emailFilename}`;

                    const removeExtensionFrom = (path: string) => {
                      if (
                        path.split('.').pop() === 'tsx' ||
                        path.split('.').pop() === 'jsx' ||
                        path.split('.').pop() === 'js'
                      ) {
                        return path.split('.').slice(0, -1).join('.');
                      }

                      return path;
                    };
                    const isCurrentPage = props.currentEmailOpenSlug
                      ? removeExtensionFrom(props.currentEmailOpenSlug) ===
                        emailSlug
                      : false;

                    return (
                      <Link
                        href={{
                          pathname: `/preview/${emailSlug}`,
                          search: searchParams.toString(),
                        }}
                        onMouseOver={() => {
                          router.prefetch(
                            `/preview/${emailSlug}?${searchParams.toString()}`,
                          );
                        }}
                        key={emailSlug}
                      >
                        <motion.span
                          animate={{ x: 0, opacity: 1 }}
                          className={cn(
                            'relative flex h-8 w-full items-center text-start gap-2 rounded-md align-middle text-slate-11 text-sm transition-colors duration-100 ease-[cubic-bezier(.6,.12,.34,.96)]',
                            props.isRoot ? undefined : 'pl-3',
                            {
                              'text-cyan-11': isCurrentPage,
                              'hover:text-slate-12':
                                props.currentEmailOpenSlug !== emailSlug,
                            },
                          )}
                          initial={{ x: -10 + -index * 1.5, opacity: 0 }}
                          transition={{
                            x: { delay: 0.03 * index, duration: 0.2 },
                            opacity: { delay: 0.03 * index, duration: 0.2 },
                          }}
                        >
                          {isCurrentPage ? (
                            <motion.span
                              animate={{ opacity: 1 }}
                              className="absolute inset-0 rounded-md bg-cyan-5 opacity-0 transition-all duration-200 ease-[cubic-bezier(.6,.12,.34,.96)]"
                              exit={{ opacity: 0 }}
                              initial={{ opacity: 0 }}
                            >
                              {props.isRoot ? null : (
                                <motion.div
                                  className="absolute top-1 left-[0.4rem] inset-0 h-6 w-px rounded-sm bg-cyan-11"
                                  layoutId="active-file"
                                  transition={{
                                    type: 'spring',
                                    bounce: 0.2,
                                    duration: 0.6,
                                  }}
                                />
                              )}
                            </motion.span>
                          ) : null}
                          <IconFile
                            className="h-5 w-5"
                            height="20"
                            width="20"
                          />
                          <span className="truncate w-[calc(100%-1.25rem)]">
                            {emailFilename}
                          </span>
                        </motion.span>
                      </Link>
                    );
                  },
                )}
              </LayoutGroup>
            </div>
          </motion.div>
        </Collapsible.Content>
      ) : null}
    </AnimatePresence>
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

- `FileTreeDirectoryChildren()`
- `emailSlug()`
- `id()`
- `isCurrentPage()`
- `removeExtensionFrom()`
- `router()`
- `searchParams()`

### Dependencies

This file imports/requires:

- `../../utils`
- `../../utils/get-emails-directory-metadata`
- `../icons/icon-file`
- `./file-tree-directory`
- `@radix-ui/react-collapsible`
- `framer-motion`
- `next/link`
- `next/navigation`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 117

- `AnimatePresence`
- `Collapsible`
- `Content`
- `EmailsDirectory`
- `FileTreeDirectory`
- `FileTreeDirectoryChildren`
- `IconFile`
- `LayoutGroup`
- `Link`
- `React`
- `absolute`
- `absolutePath`
- `active`
- `align`
- `all`
- `animate`
- `asChild`
- `auto`
- `bezier`
- `boolean`
- `bounce`
- `calc`
- `center`
- `className`
- `col`
- `collapsible`
- `colors`
- `cubic`
- `currentEmailOpenSlug`
- `cyan`
- `data`
- `delay`
- `directory`
- `div`
- `duration`
- `ease`
- `emailFilename`
- `emailFilenames`
- `emailSlug`
- `emails`
- `emailsDirectoryMetadata`
- `exit`
- `file`
- `flex`
- `forceMount`
- `framer`
- `full`
- `gap`
- `get`
- `height`
- `hidden`
- `hover`
- `href`
- `icon`
- `icons`
- `index`
- `initial`
- `inset`
- `isCurrentPage`
- `isRoot`
- `items`
- `join`
- `jsx`
- `key`
- `layoutId`
- `left`
- `line`
- `link`
- `map`
- `metadata`
- `middle`
- `motion`
- `navigation`
- `next`
- `onMouseOver`
- `opacity`
- `open`
- `overflow`
- `path`
- `pathname`
- `pop`
- `prefetch`
- `preview`
- `props`
- `radix`
- `react`
- `relative`
- `relativePath`
- `removeExtensionFrom`
- `rounded`
- `router`
- `search`
- `searchParams`
- `sidebar`
- `slate`
- `slice`
- `span`
- `split`
- `spring`
- `start`
- `state`
- `string`
- `subDirectories`
- `subDirectory`
- `text`
- `toString`
- `top`
- `transition`
- `tree`
- `truncate`
- `tsx`
- `type`
- `useId`
- `useRouter`
- `useSearchParams`
- `utils`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

