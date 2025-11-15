# Documentation: button.tsx
**File Path:** `packages/preview-server/src/components/button.tsx`
**Language:** tsx
**Size:** 2,587 bytes
**Lines:** 102
**Generated:** 2025-11-15T20:37:32.113872Z

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

- **Path:** `packages/preview-server/src/components/button.tsx`
- **Name:** `button.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,587 bytes (2.53 KB)
- **Lines of Code:** 102

---

## Original Source

```tsx
'use client';
import { DotLottieReact } from '@lottiefiles/dotlottie-react';
import * as SlotPrimitive from '@radix-ui/react-slot';
import type * as React from 'react';
import animatedLoadIcon from '../animated-icons-data/load.json';
import { cn } from '../utils/cn';
import { unreachable } from '../utils/unreachable';

type RootProps = React.ComponentProps<'button'>;

type Appearance = 'white' | 'gradient';
type Size = '1' | '2' | '3' | '4';

interface ButtonProps extends RootProps {
  asChild?: boolean;
  appearance?: Appearance;
  size?: Size;
  loading?: boolean;
}

export const Button = ({
  asChild,
  appearance = 'white',
  className,
  children,
  size = '2',
  loading,
  ref,
  ...props
}: ButtonProps) => {
  const Root = asChild ? SlotPrimitive.Slot : 'button';

  return (
    <Root
      ref={ref}
      type="button"
      {...props}
      className={cn(
        getSize(size),
        getAppearance(appearance),
        'inline-flex items-center justify-center gap-2 border font-medium',
        className,
      )}
      aria-disabled={loading}
    >
      <span
        className={cn(
          '-ml-7 opacity-0 transition-opacity duration-200',
          loading && 'opacity-100',
        )}
      >
        <DotLottieReact
          data={animatedLoadIcon}
          autoplay={false}
          className="h-5 w-5"
          loop={true}
        />
      </span>
      <SlotPrimitive.Slottable>{children}</SlotPrimitive.Slottable>
    </Root>
  );
};

Button.displayName = 'Button';

const getAppearance = (appearance: Appearance | undefined) => {
  switch (appearance) {
    case undefined:
    case 'white':
      return [
        'border-white bg-white text-black transition-colors duration-200 ease-in-out',
        'hover:bg-white/90',
        'focus:bg-white/90 focus:outline-none focus:ring-2 focus:ring-white/20',
        'mt-2 mb-2 aria-disabled:border-transparent aria-disabled:bg-slate-11',
      ];
    case 'gradient':
      return [
        'bg-gradient border-[#34343A] backdrop-blur-[1.25rem]',
        'hover:bg-gradientHover',
        'focus:bg-gradientHover focus:outline-none focus:ring-2 focus:ring-white/20',
      ];
    default:
      unreachable(appearance);
  }
};

const getSize = (size: Size | undefined) => {
  switch (size) {
    case '1':
      return '';
    case undefined:
    case '2':
      return 'text-[.875rem] h-8 px-3 rounded-md gap-2';
    case '3':
      return 'text-[.875rem] h-10 px-4 rounded-md gap-2';
    case '4':
      return 'text-base h-11 px-4 rounded-md gap-2';
    default:
      unreachable(size);
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

- `Button()`
- `Root()`
- `getAppearance()`
- `getSize()`

### Interfaces

- `ButtonProps`

### Type Definitions

- `Appearance`
- `RootProps`
- `Size`

### Dependencies

This file imports/requires:

- `../animated-icons-data/load.json`
- `../utils/cn`
- `../utils/unreachable`
- `@lottiefiles/dotlottie-react`
- `@radix-ui/react-slot`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 78

- `Appearance`
- `Button`
- `ButtonProps`
- `ComponentProps`
- `DotLottieReact`
- `React`
- `Root`
- `RootProps`
- `Size`
- `Slot`
- `SlotPrimitive`
- `Slottable`
- `animated`
- `animatedLoadIcon`
- `appearance`
- `aria`
- `asChild`
- `autoplay`
- `backdrop`
- `base`
- `black`
- `blur`
- `boolean`
- `border`
- `button`
- `center`
- `children`
- `className`
- `client`
- `colors`
- `data`
- `disabled`
- `displayName`
- `dotlottie`
- `duration`
- `ease`
- `extends`
- `flex`
- `focus`
- `font`
- `gap`
- `getAppearance`
- `getSize`
- `gradient`
- `gradientHover`
- `hover`
- `icons`
- `inline`
- `interface`
- `items`
- `json`
- `justify`
- `load`
- `loading`
- `loop`
- `lottiefiles`
- `medium`
- `opacity`
- `out`
- `outline`
- `props`
- `radix`
- `react`
- `ref`
- `ring`
- `rounded`
- `size`
- `slate`
- `slot`
- `span`
- `text`
- `transition`
- `transparent`
- `type`
- `unreachable`
- `use`
- `utils`
- `white`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

