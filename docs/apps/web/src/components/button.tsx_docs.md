# Documentation: button.tsx
**File Path:** `apps/web/src/components/button.tsx`
**Language:** tsx
**Size:** 1,916 bytes
**Lines:** 76
**Generated:** 2025-11-15T20:37:32.886783Z

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

- **Path:** `apps/web/src/components/button.tsx`
- **Name:** `button.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,916 bytes (1.87 KB)
- **Lines of Code:** 76

---

## Original Source

```tsx
import { Slot } from '@radix-ui/react-slot';
import classNames from 'classnames';
import { unreachable } from '../utils/unreachable';

type Appearance = 'white' | 'gradient';
type Size = '1' | '2' | '3' | '4' | '5';

interface ButtonProps extends React.ComponentProps<'button'> {
  asChild?: boolean;
  appearance?: Appearance;
  size?: Size;
}

export function Button({
  asChild,
  appearance = 'white',
  className,
  children,
  size = '2',
  ...props
}: ButtonProps) {
  const Comp = asChild ? Slot : 'button';

  return (
    <Comp
      className={classNames(
        getSize(size),
        getAppearance(appearance),
        'inline-flex items-center justify-center border font-medium',
        className,
      )}
      type="button"
      {...props}
    >
      {children}
    </Comp>
  );
}

const getAppearance = (appearance: Appearance) => {
  switch (appearance) {
    case 'white':
      return [
        'bg-white text-black',
        'hover:bg-white/90',
        'focus-visible:ring-slate-10 focus-visible:bg-white/90 focus-visible:outline-none focus-visible:ring-2',
        'selection:text-black',
      ];
    case 'gradient':
      return [
        'bg-gradient border-[#34343A] backdrop-blur-[1.25rem]',
        'hover:bg-gradientHover',
        'focus-visible:bg-gradientHover focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/20',
      ];
    default:
      unreachable(appearance);
  }
};

const getSize = (size: Size) => {
  switch (size) {
    case '1':
      return '';
    case '2':
      return 'h-8 gap-2 rounded-xl px-3 text-[.875rem] transition-colors';
    case '3':
      return 'h-10 gap-2 rounded-xl px-4 text-[.875rem] transition-colors';
    case '4':
      return 'h-11 gap-2 rounded-xl px-4 text-base transition-colors';
    case '5':
      return 'h-12 gap-2 rounded-xl px-4 text-base transition-colors';
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
- `Comp()`
- `getAppearance()`
- `getSize()`

### Interfaces

- `ButtonProps`

### Type Definitions

- `Appearance`
- `Size`

### Dependencies

This file imports/requires:

- `../utils/unreachable`
- `@radix-ui/react-slot`
- `classnames`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 55

- `Appearance`
- `Button`
- `ButtonProps`
- `Comp`
- `ComponentProps`
- `React`
- `Size`
- `Slot`
- `appearance`
- `asChild`
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
- `classNames`
- `classnames`
- `colors`
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
- `inline`
- `interface`
- `items`
- `justify`
- `medium`
- `outline`
- `props`
- `radix`
- `react`
- `ring`
- `rounded`
- `selection`
- `size`
- `slate`
- `slot`
- `text`
- `transition`
- `type`
- `unreachable`
- `utils`
- `visible`
- `white`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

