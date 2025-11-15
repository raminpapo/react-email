# Documentation: text.tsx
**File Path:** `apps/web/src/components/text.tsx`
**Language:** tsx
**Size:** 1,629 bytes
**Lines:** 75
**Generated:** 2025-11-15T20:37:32.918139Z

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

- **Path:** `apps/web/src/components/text.tsx`
- **Name:** `text.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,629 bytes (1.59 KB)
- **Lines of Code:** 75

---

## Original Source

```tsx
import classNames from 'classnames';
import type { As } from '../utils/as';
import { unreachable } from '../utils/unreachable';

type TextSize = '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9';
type TextColor = 'gray' | 'white';

interface TextOwnProps {
  size?: TextSize;
  color?: TextColor;
  ref?: React.RefObject<HTMLParagraphElement>;
}

type TextProps = As<'span', 'div', 'p'> & TextOwnProps;

export function Text({
  as: Tag = 'span',
  size = '2',
  color = 'gray',
  className,
  children,
  ref,
  ...props
}: TextProps) {
  return (
    <Tag
      className={classNames(
        className,
        getSizesClassNames(size),
        getColorClassNames(color),
      )}
      {...props}
      ref={ref}
    >
      {children}
    </Tag>
  );
}

const getSizesClassNames = (size: TextSize) => {
  switch (size) {
    case '1':
      return 'text-xs';
    case '2':
      return 'text-sm';
    case '3':
      return 'text-base';
    case '4':
      return 'text-base sm:text-lg';
    case '5':
      return ['text-[17px]', 'md:text-xl tracking-[-0.16px]'];
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

const getColorClassNames = (color: TextColor) => {
  switch (color) {
    case 'white':
      return 'text-slate-12';
    case 'gray':
      return 'text-slate-11';
    default:
      return unreachable(color);
  }
};

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

### Interfaces

- `TextOwnProps`

### Type Definitions

- `TextColor`
- `TextProps`
- `TextSize`

### Dependencies

This file imports/requires:

- `../utils/as`
- `../utils/unreachable`
- `classnames`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 32

- `HTMLParagraphElement`
- `React`
- `RefObject`
- `Tag`
- `Text`
- `TextColor`
- `TextOwnProps`
- `TextProps`
- `TextSize`
- `base`
- `children`
- `className`
- `classNames`
- `classnames`
- `color`
- `div`
- `getColorClassNames`
- `getSizesClassNames`
- `gray`
- `interface`
- `leading`
- `props`
- `ref`
- `size`
- `slate`
- `span`
- `text`
- `tracking`
- `type`
- `unreachable`
- `utils`
- `white`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

