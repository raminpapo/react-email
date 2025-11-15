# Documentation: toolbar-button.tsx
**File Path:** `packages/preview-server/src/components/toolbar/toolbar-button.tsx`
**Language:** tsx
**Size:** 1,502 bytes
**Lines:** 53
**Generated:** 2025-11-15T20:37:32.184169Z

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

- **Path:** `packages/preview-server/src/components/toolbar/toolbar-button.tsx`
- **Name:** `toolbar-button.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,502 bytes (1.47 KB)
- **Lines of Code:** 53

---

## Original Source

```tsx
import { motion } from 'framer-motion';
import { cn } from '../../utils';
import { Tooltip } from '../tooltip';

interface ToolbarButtonProps extends React.ComponentProps<'button'> {
  children: React.ReactNode;
  active?: boolean;
  tooltip?: React.ReactNode;
  delayDuration?: number;
}

export const ToolbarButton = ({
  children,
  className,
  active,
  tooltip,
  delayDuration = 500,
  ...props
}: ToolbarButtonProps) => {
  return (
    <Tooltip.Provider>
      <Tooltip delayDuration={delayDuration}>
        <Tooltip.Trigger asChild>
          <button
            type="button"
            {...props}
            className={cn(
              'h-full w-fit font-regular flex text-sm text-slate-10 items-center align-middle justify-center px-1 gap-2 relative',
              'hover:text-slate-12 transition-colors',
              active && 'data-[state=active]:text-cyan-11',
              className,
            )}
          >
            {children}
            {active ? (
              <motion.span
                className="-bottom-px absolute rounded-sm left-0 w-full bg-cyan-11 h-px"
                layoutId="active-toolbar-button"
                transition={{
                  type: 'spring',
                  bounce: 0.2,
                  duration: 0.6,
                }}
              />
            ) : null}
          </button>
        </Tooltip.Trigger>
        {tooltip ? <Tooltip.Content>{tooltip}</Tooltip.Content> : null}
      </Tooltip>
    </Tooltip.Provider>
  );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `ToolbarButton()`

### Interfaces

- `ToolbarButtonProps`

### Dependencies

This file imports/requires:

- `../../utils`
- `../tooltip`
- `framer-motion`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 55

- `ComponentProps`
- `Content`
- `Provider`
- `React`
- `ReactNode`
- `ToolbarButton`
- `ToolbarButtonProps`
- `Tooltip`
- `Trigger`
- `absolute`
- `active`
- `align`
- `asChild`
- `boolean`
- `bottom`
- `bounce`
- `button`
- `center`
- `children`
- `className`
- `colors`
- `cyan`
- `data`
- `delayDuration`
- `duration`
- `extends`
- `fit`
- `flex`
- `font`
- `framer`
- `full`
- `gap`
- `hover`
- `interface`
- `items`
- `justify`
- `layoutId`
- `left`
- `middle`
- `motion`
- `number`
- `props`
- `regular`
- `relative`
- `rounded`
- `slate`
- `span`
- `spring`
- `state`
- `text`
- `toolbar`
- `tooltip`
- `transition`
- `type`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

