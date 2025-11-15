# Documentation: spotlight.tsx
**File Path:** `apps/web/src/components/spotlight.tsx`
**Language:** tsx
**Size:** 1,153 bytes
**Lines:** 44
**Generated:** 2025-11-15T20:37:32.913794Z

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

- **Path:** `apps/web/src/components/spotlight.tsx`
- **Name:** `spotlight.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,153 bytes (1.13 KB)
- **Lines of Code:** 44

---

## Original Source

```tsx
'use client';

import classNames from 'classnames';
import { motion, useMotionTemplate, useMotionValue } from 'framer-motion';
import type { MouseEvent, ReactNode } from 'react';

interface SpotlightProps {
  children: ReactNode;
  className?: string;
}

export function Spotlight({ children, className }: SpotlightProps) {
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  const handleMouseMove = ({ currentTarget, clientX, clientY }: MouseEvent) => {
    const { left, top } = currentTarget.getBoundingClientRect();

    mouseX.set(clientX - left);
    mouseY.set(clientY - top);
  };

  const background = useMotionTemplate`
    radial-gradient(
      12rem circle at ${mouseX}px ${mouseY}px,
      rgba(37, 174, 186, 30%),
      transparent 80%
    )
  `;

  return (
    <div
      className={classNames('overflow-hidden', className)}
      onMouseMove={handleMouseMove}
    >
      {children}
      <motion.div
        className="-inset-px pointer-events-none absolute opacity-0 mix-blend-color-dodge transition duration-300 group-hover:opacity-100 max-md:hidden"
        style={{ background }}
      />
    </div>
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

- `Spotlight()`
- `background()`
- `handleMouseMove()`
- `mouseX()`
- `mouseY()`

### Interfaces

- `SpotlightProps`

### Dependencies

This file imports/requires:

- `classnames`
- `framer-motion`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 53

- `MouseEvent`
- `ReactNode`
- `Spotlight`
- `SpotlightProps`
- `absolute`
- `background`
- `blend`
- `children`
- `circle`
- `className`
- `classNames`
- `classnames`
- `client`
- `clientX`
- `clientY`
- `color`
- `currentTarget`
- `div`
- `dodge`
- `duration`
- `events`
- `framer`
- `getBoundingClientRect`
- `gradient`
- `group`
- `handleMouseMove`
- `hidden`
- `hover`
- `inset`
- `interface`
- `left`
- `max`
- `mix`
- `motion`
- `mouseX`
- `mouseY`
- `onMouseMove`
- `opacity`
- `overflow`
- `pointer`
- `radial`
- `react`
- `rgba`
- `set`
- `string`
- `style`
- `top`
- `transition`
- `transparent`
- `type`
- `use`
- `useMotionTemplate`
- `useMotionValue`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

