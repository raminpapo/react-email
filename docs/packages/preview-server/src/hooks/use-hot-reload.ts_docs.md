# Documentation: use-hot-reload.ts
**File Path:** `packages/preview-server/src/hooks/use-hot-reload.ts`
**Language:** typescript
**Size:** 791 bytes
**Lines:** 32
**Generated:** 2025-11-15T20:37:32.005978Z

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

- **Path:** `packages/preview-server/src/hooks/use-hot-reload.ts`
- **Name:** `use-hot-reload.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 791 bytes (0.77 KB)
- **Lines of Code:** 32

---

## Original Source

```typescript
'use client';

import { useEffect, useRef } from 'react';
import { io, type Socket } from 'socket.io-client';
import type { HotReloadChange } from '../utils/types/hot-reload-change';

/**
 * Hook that detects any "reload" event sent from the CLI's web socket
 * and calls the received parameter callback
 */
export const useHotreload = (
  onShouldReload: (changes: HotReloadChange[]) => void,
) => {
  const socketRef = useRef<Socket | null>(null);

  useEffect(() => {
    if (!socketRef.current) {
      socketRef.current = io();
    }
    const socket = socketRef.current;

    socket.on('reload', (changes: HotReloadChange[]) => {
      console.debug('Reloading...');
      void onShouldReload(changes);
    });

    return () => {
      socket.off();
    };
  }, [onShouldReload]);
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `socket()`
- `socketRef()`
- `useHotreload()`

### Type Definitions

- `Socket`

### Dependencies

This file imports/requires:

- `../utils/types/hot-reload-change`
- `react`
- `socket.io-client`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 34

- `Hook`
- `HotReloadChange`
- `Reloading`
- `Socket`
- `any`
- `callback`
- `calls`
- `change`
- `changes`
- `client`
- `console`
- `current`
- `debug`
- `detects`
- `event`
- `hot`
- `off`
- `onShouldReload`
- `parameter`
- `react`
- `received`
- `reload`
- `sent`
- `socket`
- `socketRef`
- `type`
- `types`
- `use`
- `useEffect`
- `useHotreload`
- `useRef`
- `utils`
- `void`
- `web`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

