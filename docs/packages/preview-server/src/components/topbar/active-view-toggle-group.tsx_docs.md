# Documentation: active-view-toggle-group.tsx
**File Path:** `packages/preview-server/src/components/topbar/active-view-toggle-group.tsx`
**Language:** tsx
**Size:** 2,989 bytes
**Lines:** 87
**Generated:** 2025-11-15T20:37:32.193563Z

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

- **Path:** `packages/preview-server/src/components/topbar/active-view-toggle-group.tsx`
- **Name:** `active-view-toggle-group.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,989 bytes (2.92 KB)
- **Lines of Code:** 87

---

## Original Source

```tsx
import * as ToggleGroup from '@radix-ui/react-toggle-group';
import { motion } from 'framer-motion';
import { cn } from '../../utils';
import { tabTransition } from '../../utils/constants';
import { IconMonitor } from '../icons/icon-monitor';
import { IconSource } from '../icons/icon-source';
import { Tooltip } from '../tooltip';

interface ActiveViewToggleGroupProps {
  activeView: string;
  setActiveView: (view: string) => void;
}

export const ActiveViewToggleGroup = ({
  activeView,
  setActiveView,
}: ActiveViewToggleGroupProps) => {
  return (
    <ToggleGroup.Root
      aria-label="View mode"
      className="lg:absolute lg:left-1/2 lg:-translate-x-1/2 inline-block items-center bg-slate-2 border border-slate-6 rounded-md overflow-hidden h-[36px]"
      onValueChange={(value) => {
        if (value) setActiveView(value);
      }}
      type="single"
      value={activeView}
    >
      <ToggleGroup.Item value="preview">
        <Tooltip>
          <Tooltip.Trigger asChild>
            <div
              className={cn(
                'w-9 flex items-center py-2 transition ease-in-out duration-200 relative hover:text-slate-12',
                {
                  'text-slate-11': activeView !== 'preview',
                  'text-slate-12': activeView === 'preview',
                },
              )}
            >
              {activeView === 'preview' && (
                <motion.span
                  animate={{ opacity: 1 }}
                  className="absolute left-0 right-0 top-0 bottom-0 bg-slate-4"
                  exit={{ opacity: 0 }}
                  initial={{ opacity: 0 }}
                  layoutId="topbar-tabs"
                  transition={tabTransition}
                />
              )}
              <IconMonitor className="m-auto" />
            </div>
          </Tooltip.Trigger>
          <Tooltip.Content>Preview</Tooltip.Content>
        </Tooltip>
      </ToggleGroup.Item>
      <ToggleGroup.Item value="source">
        <Tooltip>
          <Tooltip.Trigger asChild>
            <div
              className={cn(
                'w-9 flex  py-2 transition ease-in-out duration-200 relative hover:text-slate-12',
                {
                  'text-slate-11': activeView !== 'source',
                  'text-slate-12': activeView === 'source',
                },
              )}
            >
              {activeView === 'source' && (
                <motion.span
                  animate={{ opacity: 1 }}
                  className="absolute left-0 right-0 top-0 bottom-0 bg-slate-4"
                  exit={{ opacity: 0 }}
                  initial={{ opacity: 0 }}
                  layoutId="topbar-tabs"
                  transition={tabTransition}
                />
              )}
              <IconSource className="m-auto" />
            </div>
          </Tooltip.Trigger>
          <Tooltip.Content>Code</Tooltip.Content>
        </Tooltip>
      </ToggleGroup.Item>
    </ToggleGroup.Root>
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

- `ActiveViewToggleGroup()`

### Interfaces

- `ActiveViewToggleGroupProps`

### Dependencies

This file imports/requires:

- `../../utils`
- `../../utils/constants`
- `../icons/icon-monitor`
- `../icons/icon-source`
- `../tooltip`
- `@radix-ui/react-toggle-group`
- `framer-motion`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 76

- `ActiveViewToggleGroup`
- `ActiveViewToggleGroupProps`
- `Code`
- `Content`
- `IconMonitor`
- `IconSource`
- `Item`
- `Preview`
- `Root`
- `ToggleGroup`
- `Tooltip`
- `Trigger`
- `View`
- `absolute`
- `activeView`
- `animate`
- `aria`
- `asChild`
- `auto`
- `block`
- `border`
- `bottom`
- `center`
- `className`
- `constants`
- `div`
- `duration`
- `ease`
- `exit`
- `flex`
- `framer`
- `group`
- `hidden`
- `hover`
- `icon`
- `icons`
- `initial`
- `inline`
- `interface`
- `items`
- `label`
- `layoutId`
- `left`
- `mode`
- `monitor`
- `motion`
- `onValueChange`
- `opacity`
- `out`
- `overflow`
- `preview`
- `radix`
- `react`
- `relative`
- `right`
- `rounded`
- `setActiveView`
- `single`
- `slate`
- `source`
- `span`
- `string`
- `tabTransition`
- `tabs`
- `text`
- `toggle`
- `tooltip`
- `top`
- `topbar`
- `transition`
- `translate`
- `type`
- `utils`
- `value`
- `view`
- `void`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

