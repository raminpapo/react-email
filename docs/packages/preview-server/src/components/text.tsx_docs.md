# Documentation: text.tsx
**File Path:** `packages/preview-server/src/components/text.tsx`
**Language:** tsx
**Size:** 2,336 bytes
**Lines:** 100
**Generated:** 2025-11-15T20:37:32.131118Z

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

- **Path:** `packages/preview-server/src/components/text.tsx`
- **Name:** `text.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,336 bytes (2.28 KB)
- **Lines of Code:** 100

---

## Original Source

```tsx
import * as SlotPrimitive from '@radix-ui/react-slot';
import * as React from 'react';
import { type As, cn, unreachable } from '../utils';

export type TextSize = '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9';
export type TextColor = 'gray' | 'white';
export type TextTransform = 'uppercase' | 'lowercase' | 'capitalize';
export type TextWeight = 'normal' | 'medium';

interface TextOwnProps {
  size?: TextSize;
  color?: TextColor;
  transform?: TextTransform;
  weight?: TextWeight;
}

type TextProps = As<'span', 'div', 'p'> & TextOwnProps;

export const Text = React.forwardRef<HTMLSpanElement, Readonly<TextProps>>(
  (
    {
      as: Tag = 'span',
      size = '2',
      color = 'gray',
      transform,
      weight = 'normal',
      className,
      children,
      ...props
    },
    forwardedRef,
  ) => (
    <SlotPrimitive.Slot
      className={cn(
        className,
        transform,
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

const getSizesClassNames = (size: TextSize | undefined) => {
  switch (size) {
    case '1':
      return 'text-xs';
    case undefined:
    case '2':
      return 'text-sm';
    case '3':
      return 'text-base';
    case '4':
      return 'text-lg';
    case '5':
      return ['text-17px', 'md:text-xl tracking-[-0.16px]'];
    case '6':
      return 'text-2xl tracking-[-0.288px]';
    case '7':
      return 'text-[28px] leading-[34px] tracking-[-0.416px]';
    case '8':
      return 'text-[35px] leading-[42px] tracking-[-0.64px]';
    case '9':
      return 'text-6xl leading-[73px] tracking-[-0.896px]';
    default:
      return unreachable(size);
  }
};

const getColorClassNames = (color: TextColor | undefined) => {
  switch (color) {
    case 'white':
      return 'text-slate-12';
    case undefined:
    case 'gray':
      return 'text-slate-11';
    default:
      return unreachable(color);
  }
};

const getWeightClassNames = (weight: TextWeight | undefined) => {
  switch (weight) {
    case undefined:
    case 'normal':
      return 'font-normal';
    case 'medium':
      return 'font-medium';
    default:
      return unreachable(weight);
  }
};

Text.displayName = 'Text';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Text()`
- `getColorClassNames()`
- `getSizesClassNames()`
- `getWeightClassNames()`

### Interfaces

- `TextOwnProps`

### Type Definitions

- `As`
- `TextColor`
- `TextProps`
- `TextSize`
- `TextTransform`
- `TextWeight`

### Dependencies

This file imports/requires:

- `../utils`
- `@radix-ui/react-slot`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 49

- `HTMLSpanElement`
- `React`
- `Readonly`
- `Slot`
- `SlotPrimitive`
- `Tag`
- `Text`
- `TextColor`
- `TextOwnProps`
- `TextProps`
- `TextSize`
- `TextTransform`
- `TextWeight`
- `base`
- `capitalize`
- `children`
- `className`
- `color`
- `displayName`
- `div`
- `font`
- `forwardRef`
- `forwardedRef`
- `getColorClassNames`
- `getSizesClassNames`
- `getWeightClassNames`
- `gray`
- `interface`
- `leading`
- `lowercase`
- `medium`
- `normal`
- `props`
- `radix`
- `react`
- `ref`
- `size`
- `slate`
- `slot`
- `span`
- `text`
- `tracking`
- `transform`
- `type`
- `unreachable`
- `uppercase`
- `utils`
- `weight`
- `white`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

