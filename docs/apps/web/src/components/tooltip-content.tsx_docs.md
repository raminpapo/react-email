# Documentation: tooltip-content.tsx
**File Path:** `apps/web/src/components/tooltip-content.tsx`
**Language:** tsx
**Size:** 798 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:32.919397Z

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

- **Path:** `apps/web/src/components/tooltip-content.tsx`
- **Name:** `tooltip-content.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 798 bytes (0.78 KB)
- **Lines of Code:** 33

---

## Original Source

```tsx
import * as TooltipPrimitive from '@radix-ui/react-tooltip';

type ContentElement = React.ComponentRef<typeof TooltipPrimitive.Content>;
type ContentProps = Omit<
  React.ComponentPropsWithoutRef<typeof TooltipPrimitive.Content>,
  'sideOffset'
> & {
  sideOffset?: number;
  ref?: React.RefObject<ContentElement>;
};

export type TooltipProps = ContentProps;

export function TooltipContent({
  sideOffset = 6,
  children,
  ref,
  ...props
}: TooltipProps) {
  return (
    <TooltipPrimitive.Portal>
      <TooltipPrimitive.Content
        {...props}
        className="z-20 rounded-md border border-slate-6 bg-black px-3 py-2 text-white text-xs"
        ref={ref}
        sideOffset={sideOffset}
      >
        {children}
      </TooltipPrimitive.Content>
    </TooltipPrimitive.Portal>
  );
}

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

- `@radix-ui/react-tooltip`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 28

- `ComponentPropsWithoutRef`
- `ComponentRef`
- `Content`
- `ContentElement`
- `ContentProps`
- `Omit`
- `Portal`
- `React`
- `RefObject`
- `TooltipContent`
- `TooltipPrimitive`
- `TooltipProps`
- `black`
- `border`
- `children`
- `className`
- `number`
- `props`
- `radix`
- `react`
- `ref`
- `rounded`
- `sideOffset`
- `slate`
- `text`
- `tooltip`
- `type`
- `white`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

