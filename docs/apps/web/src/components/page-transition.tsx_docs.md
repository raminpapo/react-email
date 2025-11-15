# Documentation: page-transition.tsx
**File Path:** `apps/web/src/components/page-transition.tsx`
**Language:** tsx
**Size:** 1,050 bytes
**Lines:** 46
**Generated:** 2025-11-15T20:37:32.908137Z

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

- **Path:** `apps/web/src/components/page-transition.tsx`
- **Name:** `page-transition.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,050 bytes (1.03 KB)
- **Lines of Code:** 46

---

## Original Source

```tsx
'use client';

import classNames from 'classnames';
import type { HTMLMotionProps, SVGMotionProps } from 'framer-motion';
import { AnimatePresence, motion } from 'framer-motion';

type MotionComponentType = keyof typeof motion;

interface PageTransitionProps {
  tag?: MotionComponentType;
  children: React.ReactNode;
  className?: string;
  key: string;
}

export function PageTransition({
  tag = 'div',
  children,
  className = '',
  key,
}: PageTransitionProps) {
  const MotionComponent = motion[
    tag as MotionComponentType
  ] as React.ComponentType<HTMLMotionProps<'div'> | SVGMotionProps<'svg'>>;

  return (
    <AnimatePresence mode="wait">
      <MotionComponent
        animate={{
          opacity: 1,
          y: 0,
        }}
        className={classNames('relative z-[2] w-full', className)}
        initial={{
          opacity: 0,
          y: 4,
        }}
        key={key}
        transition={{ duration: 0.3, ease: [0.36, 0.66, 0.6, 1] }}
      >
        {children}
      </MotionComponent>
    </AnimatePresence>
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

- `MotionComponent()`
- `PageTransition()`

### Interfaces

- `PageTransitionProps`

### Type Definitions

- `MotionComponentType`

### Dependencies

This file imports/requires:

- `classnames`
- `framer-motion`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 36

- `AnimatePresence`
- `ComponentType`
- `HTMLMotionProps`
- `MotionComponent`
- `MotionComponentType`
- `PageTransition`
- `PageTransitionProps`
- `React`
- `ReactNode`
- `SVGMotionProps`
- `animate`
- `children`
- `className`
- `classNames`
- `classnames`
- `client`
- `div`
- `duration`
- `ease`
- `framer`
- `full`
- `initial`
- `interface`
- `key`
- `keyof`
- `mode`
- `motion`
- `opacity`
- `relative`
- `string`
- `svg`
- `tag`
- `transition`
- `type`
- `use`
- `wait`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

