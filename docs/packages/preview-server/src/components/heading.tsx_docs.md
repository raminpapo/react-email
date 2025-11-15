# Documentation: heading.tsx
**File Path:** `packages/preview-server/src/components/heading.tsx`
**Language:** tsx
**Size:** 2,418 bytes
**Lines:** 114
**Generated:** 2025-11-15T20:37:32.120690Z

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

- **Path:** `packages/preview-server/src/components/heading.tsx`
- **Name:** `heading.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,418 bytes (2.36 KB)
- **Lines of Code:** 114

---

## Original Source

```tsx
import * as SlotPrimitive from '@radix-ui/react-slot';
import * as React from 'react';
import { type As, cn, unreachable } from '../utils';

export type HeadingSize =
  | '1'
  | '2'
  | '3'
  | '4'
  | '5'
  | '6'
  | '7'
  | '8'
  | '9'
  | '10';
export type HeadingColor = 'white' | 'gray';
export type HeadingWeight = 'medium' | 'bold';

interface HeadingOwnProps {
  size?: HeadingSize;
  color?: HeadingColor;
  weight?: HeadingWeight;
}

type HeadingProps = As<'h1', 'h2', 'h3', 'h4', 'h5', 'h6'> & HeadingOwnProps;

export const Heading = React.forwardRef<
  HTMLHeadingElement,
  Readonly<HeadingProps>
>(
  (
    {
      as: Tag = 'h1',
      size = '3',
      className,
      color = 'white',
      children,
      weight = 'bold',
      ...props
    },
    forwardedRef,
  ) => (
    <SlotPrimitive.Slot
      className={cn(
        className,
        getSizesClassNames(size),
        getColorClassNames(color),
        getWeightClassNames(weight),
      )}
      ref={forwardedRef}
      {...props}
    >
      <Tag>{children}</Tag>
    </SlotPrimitive.Slot>
  ),
);

const getSizesClassNames = (size: HeadingSize | undefined) => {
  switch (size) {
    case '1':
      return 'text-xs';
    case '2':
      return 'text-sm';
    case undefined:
    case '3':
      return 'text-base';
    case '4':
      return 'text-lg';
    case '5':
      return 'text-xl tracking-[-0.16px]';
    case '6':
      return 'text-2xl tracking-[-0.288px]';
    case '7':
      return 'text-[28px] leading-[34px] tracking-[-0.416px]';
    case '8':
      return 'text-[35px] leading-[42px] tracking-[-0.64px]';
    case '9':
      return 'text-6xl leading-[73px] tracking-[-0.896px]';
    case '10':
      return [
        'text-[38px] leading-[46px]',
        'md:text-[70px] md:leading-[85px] tracking-[-1.024px;]',
      ];
    default:
      return unreachable(size);
  }
};

const getColorClassNames = (color: HeadingColor | undefined) => {
  switch (color) {
    case 'gray':
      return 'text-slate-11';
    case 'white':
    case undefined:
      return 'text-slate-12';
    default:
      return unreachable(color);
  }
};

const getWeightClassNames = (weight: HeadingWeight | undefined) => {
  switch (weight) {
    case 'medium':
      return 'font-medium';
    case 'bold':
    case undefined:
      return 'font-bold';
    default:
      return unreachable(weight);
  }
};

Heading.displayName = 'Heading';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Heading()`
- `getColorClassNames()`
- `getSizesClassNames()`
- `getWeightClassNames()`

### Interfaces

- `HeadingOwnProps`

### Type Definitions

- `As`
- `HeadingColor`
- `HeadingProps`
- `HeadingSize`
- `HeadingWeight`

### Dependencies

This file imports/requires:

- `../utils`
- `@radix-ui/react-slot`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 42

- `HTMLHeadingElement`
- `Heading`
- `HeadingColor`
- `HeadingOwnProps`
- `HeadingProps`
- `HeadingSize`
- `HeadingWeight`
- `React`
- `Readonly`
- `Slot`
- `SlotPrimitive`
- `Tag`
- `base`
- `bold`
- `children`
- `className`
- `color`
- `displayName`
- `font`
- `forwardRef`
- `forwardedRef`
- `getColorClassNames`
- `getSizesClassNames`
- `getWeightClassNames`
- `gray`
- `interface`
- `leading`
- `medium`
- `props`
- `radix`
- `react`
- `ref`
- `size`
- `slate`
- `slot`
- `text`
- `tracking`
- `type`
- `unreachable`
- `utils`
- `weight`
- `white`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

