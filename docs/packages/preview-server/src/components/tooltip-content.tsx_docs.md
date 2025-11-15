# Documentation: tooltip-content.tsx
**File Path:** `packages/preview-server/src/components/tooltip-content.tsx`
**Language:** tsx
**Size:** 898 bytes
**Lines:** 32
**Generated:** 2025-11-15T20:37:32.136066Z

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

- **Path:** `packages/preview-server/src/components/tooltip-content.tsx`
- **Name:** `tooltip-content.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 898 bytes (0.88 KB)
- **Lines of Code:** 32

---

## Original Source

```tsx
import * as TooltipPrimitive from '@radix-ui/react-tooltip';
import * as React from 'react';
import { cn } from '../utils';

type ContentElement = React.ComponentRef<typeof TooltipPrimitive.Content>;
type ContentProps = React.ComponentPropsWithoutRef<
  typeof TooltipPrimitive.Content
>;

export type TooltipProps = ContentProps;

export const TooltipContent = React.forwardRef<
  ContentElement,
  Readonly<TooltipProps>
>(({ sideOffset = 6, children, ...props }, forwardedRef) => (
  <TooltipPrimitive.Portal>
    <TooltipPrimitive.Content
      {...props}
      className={cn(
        'z-20 rounded-md border border-slate-6 bg-black px-3 py-2 text-white text-xs',
        'font-sans max-w-60',
      )}
      ref={forwardedRef}
      sideOffset={sideOffset}
    >
      {children}
    </TooltipPrimitive.Content>
  </TooltipPrimitive.Portal>
));

TooltipContent.displayName = 'TooltipContent';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `TooltipContent()`

### Type Definitions

- `ContentElement`
- `ContentProps`
- `TooltipProps`

### Dependencies

This file imports/requires:

- `../utils`
- `@radix-ui/react-tooltip`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 33

- `ComponentPropsWithoutRef`
- `ComponentRef`
- `Content`
- `ContentElement`
- `ContentProps`
- `Portal`
- `React`
- `Readonly`
- `TooltipContent`
- `TooltipPrimitive`
- `TooltipProps`
- `black`
- `border`
- `children`
- `className`
- `displayName`
- `font`
- `forwardRef`
- `forwardedRef`
- `max`
- `props`
- `radix`
- `react`
- `ref`
- `rounded`
- `sans`
- `sideOffset`
- `slate`
- `text`
- `tooltip`
- `type`
- `utils`
- `white`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

