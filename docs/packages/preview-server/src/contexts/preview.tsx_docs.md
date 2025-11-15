# Documentation: preview.tsx
**File Path:** `packages/preview-server/src/contexts/preview.tsx`
**Language:** tsx
**Size:** 2,251 bytes
**Lines:** 92
**Generated:** 2025-11-15T20:37:32.099034Z

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

- **Path:** `packages/preview-server/src/contexts/preview.tsx`
- **Name:** `preview.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,251 bytes (2.20 KB)
- **Lines of Code:** 92

---

## Original Source

```tsx
'use client';
import { useRouter } from 'next/navigation';
import { createContext, useContext } from 'react';
import type {
  EmailRenderingResult,
  RenderedEmailMetadata,
} from '../actions/render-email-by-path';
import { isBuilding, isPreviewDevelopment } from '../app/env';
import { useEmailRenderingResult } from '../hooks/use-email-rendering-result';
import { useHotreload } from '../hooks/use-hot-reload';
import { useRenderingMetadata } from '../hooks/use-rendering-metadata';

export const PreviewContext = createContext<
  | {
      renderedEmailMetadata: RenderedEmailMetadata | undefined;
      renderingResult: EmailRenderingResult;

      emailSlug: string;
      emailPath: string;
    }
  | undefined
>(undefined);

interface PreviewProvider {
  emailSlug: string;
  emailPath: string;

  serverRenderingResult: EmailRenderingResult;

  children: React.ReactNode;
}

export const PreviewProvider = ({
  emailSlug,
  emailPath,
  serverRenderingResult,
  children,
}: PreviewProvider) => {
  const router = useRouter();

  const renderingResult = useEmailRenderingResult(
    emailPath,
    serverRenderingResult,
  );

  const renderedEmailMetadata = useRenderingMetadata(
    emailPath,
    renderingResult,
    serverRenderingResult,
  );

  if (!isBuilding && !isPreviewDevelopment) {
    // biome-ignore lint/correctness/useHookAtTopLevel: this will not change on runtime so it doesn't violate the rules of hooks
    useHotreload((changes) => {
      const changeForThisEmail = changes.find((change) =>
        change.filename.includes(emailSlug),
      );

      if (typeof changeForThisEmail !== 'undefined') {
        if (changeForThisEmail.event === 'unlink') {
          router.push('/');
        }
      }
    });
  }

  return (
    <PreviewContext.Provider
      value={{
        emailPath,
        emailSlug,
        renderedEmailMetadata,
        renderingResult,
      }}
    >
      {children}
    </PreviewContext.Provider>
  );
};

export const usePreviewContext = () => {
  const previewContext = useContext(PreviewContext);

  if (typeof previewContext === 'undefined') {
    throw new Error(
      'Cannot call `usePreviewContext` outside of an `PreviewContext` provider.',
    );
  }

  return previewContext;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `PreviewContext()`
- `PreviewProvider()`
- `changeForThisEmail()`
- `previewContext()`
- `renderedEmailMetadata()`
- `renderingResult()`
- `router()`
- `usePreviewContext()`

### Interfaces

- `PreviewProvider`

### Dependencies

This file imports/requires:

- `../actions/render-email-by-path`
- `../app/env`
- `../hooks/use-email-rendering-result`
- `../hooks/use-hot-reload`
- `../hooks/use-rendering-metadata`
- `next/navigation`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 68

- `Cannot`
- `EmailRenderingResult`
- `Error`
- `PreviewContext`
- `PreviewProvider`
- `Provider`
- `React`
- `ReactNode`
- `RenderedEmailMetadata`
- `actions`
- `app`
- `biome`
- `call`
- `change`
- `changeForThisEmail`
- `changes`
- `children`
- `client`
- `correctness`
- `createContext`
- `doesn`
- `email`
- `emailPath`
- `emailSlug`
- `env`
- `event`
- `filename`
- `find`
- `hooks`
- `hot`
- `ignore`
- `includes`
- `interface`
- `isBuilding`
- `isPreviewDevelopment`
- `lint`
- `metadata`
- `navigation`
- `next`
- `outside`
- `path`
- `previewContext`
- `provider`
- `push`
- `react`
- `reload`
- `render`
- `renderedEmailMetadata`
- `rendering`
- `renderingResult`
- `result`
- `router`
- `rules`
- `runtime`
- `serverRenderingResult`
- `string`
- `type`
- `unlink`
- `use`
- `useContext`
- `useEmailRenderingResult`
- `useHookAtTopLevel`
- `useHotreload`
- `usePreviewContext`
- `useRenderingMetadata`
- `useRouter`
- `value`
- `violate`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

