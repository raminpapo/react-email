# Documentation: useCollageTexture.ts
**File Path:** `apps/web/src/hooks/useCollageTexture.ts`
**Language:** typescript
**Size:** 1,615 bytes
**Lines:** 75
**Generated:** 2025-11-15T20:37:32.802197Z

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

- **Path:** `apps/web/src/hooks/useCollageTexture.ts`
- **Name:** `useCollageTexture.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,615 bytes (1.58 KB)
- **Lines of Code:** 75

---

## Original Source

```typescript
import { useCallback, useEffect, useState } from 'react';
import { getCanvasTexture } from '@/webgl/getCanvasTexture';

interface CollageImage {
  url: string;
}

interface CollageOptions {
  gap?: number;
  canvasHeight?: number;
  canvasWidth?: number;
  axis?: 'x' | 'y';
}

interface TextureResult {
  texture: any;
  dimensions: {
    width: number;
    height: number;
    aspectRatio: number;
  };
}

export function useCollageTexture(
  images: CollageImage[],
  options: CollageOptions = {},
) {
  const [textureResults, setTextureResults] = useState<TextureResult | null>(
    null,
  );
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  const {
    gap = 0,
    canvasHeight = 512,
    canvasWidth = 512,
    axis = 'x',
  } = options;

  const createTexture = useCallback(async () => {
    try {
      setIsLoading(true);
      setError(null);
      const result = await getCanvasTexture({
        images,
        gap,
        canvasHeight,
        canvasWidth,
        canvas: undefined,
        ctx: undefined,
        axis,
      });
      setTextureResults(result);
    } catch (err) {
      setError(
        err instanceof Error ? err : new Error('Failed to create texture'),
      );
    } finally {
      setIsLoading(false);
    }
  }, [images, gap, canvasHeight, canvasWidth, axis]);

  useEffect(() => {
    if (images.length > 0) createTexture();
  }, [images.length, createTexture]);

  return {
    texture: textureResults?.texture || null,
    dimensions: textureResults?.dimensions || null,
    isLoading,
    error,
  };
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `createTexture()`
- `result()`
- `useCollageTexture()`

### Interfaces

- `CollageImage`
- `CollageOptions`
- `TextureResult`

### Dependencies

This file imports/requires:

- `@/webgl/getCanvasTexture`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 41

- `CollageImage`
- `CollageOptions`
- `Error`
- `Failed`
- `TextureResult`
- `any`
- `aspectRatio`
- `axis`
- `canvas`
- `canvasHeight`
- `canvasWidth`
- `create`
- `createTexture`
- `ctx`
- `dimensions`
- `err`
- `error`
- `gap`
- `getCanvasTexture`
- `height`
- `images`
- `interface`
- `isLoading`
- `length`
- `number`
- `options`
- `react`
- `result`
- `setError`
- `setIsLoading`
- `setTextureResults`
- `string`
- `texture`
- `textureResults`
- `url`
- `useCallback`
- `useCollageTexture`
- `useEffect`
- `useState`
- `webgl`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

