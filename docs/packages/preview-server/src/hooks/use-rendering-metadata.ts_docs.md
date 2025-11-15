# Documentation: use-rendering-metadata.ts
**File Path:** `packages/preview-server/src/hooks/use-rendering-metadata.ts`
**Language:** typescript
**Size:** 1,169 bytes
**Lines:** 37
**Generated:** 2025-11-15T20:37:32.007107Z

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

- **Path:** `packages/preview-server/src/hooks/use-rendering-metadata.ts`
- **Name:** `use-rendering-metadata.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,169 bytes (1.14 KB)
- **Lines of Code:** 37

---

## Original Source

```typescript
import { useEffect } from 'react';
import type {
  EmailRenderingResult,
  RenderedEmailMetadata,
} from '../actions/render-email-by-path';

const lastRenderingMetadataPerEmailPath = {} as Record<
  string,
  RenderedEmailMetadata
>;

/**
 * Returns the rendering metadata if the given `renderingResult`
 * does not error. If it does error it returns the last value it had for the hook.
 */
export const useRenderingMetadata = (
  emailPath: string,
  renderingResult: EmailRenderingResult,
  serverRenderingMetadata: EmailRenderingResult,
): RenderedEmailMetadata | undefined => {
  useEffect(() => {
    if ('markup' in renderingResult) {
      lastRenderingMetadataPerEmailPath[emailPath] = renderingResult;
    } else if (
      typeof serverRenderingMetadata !== 'undefined' &&
      'markup' in serverRenderingMetadata &&
      typeof lastRenderingMetadataPerEmailPath[emailPath] === 'undefined'
    ) {
      lastRenderingMetadataPerEmailPath[emailPath] = serverRenderingMetadata;
    }
  }, [renderingResult, emailPath, serverRenderingMetadata]);

  return 'error' in renderingResult
    ? lastRenderingMetadataPerEmailPath[emailPath]
    : renderingResult;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `lastRenderingMetadataPerEmailPath()`
- `useRenderingMetadata()`

### Dependencies

This file imports/requires:

- `../actions/render-email-by-path`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 26

- `EmailRenderingResult`
- `Record`
- `RenderedEmailMetadata`
- `Returns`
- `actions`
- `email`
- `emailPath`
- `error`
- `given`
- `hook`
- `last`
- `lastRenderingMetadataPerEmailPath`
- `markup`
- `metadata`
- `path`
- `react`
- `render`
- `rendering`
- `renderingResult`
- `returns`
- `serverRenderingMetadata`
- `string`
- `type`
- `useEffect`
- `useRenderingMetadata`
- `value`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

