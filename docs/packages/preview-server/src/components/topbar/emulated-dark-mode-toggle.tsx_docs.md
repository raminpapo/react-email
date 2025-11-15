# Documentation: emulated-dark-mode-toggle.tsx
**File Path:** `packages/preview-server/src/components/topbar/emulated-dark-mode-toggle.tsx`
**Language:** tsx
**Size:** 1,877 bytes
**Lines:** 59
**Generated:** 2025-11-15T20:37:32.195117Z

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

- **Path:** `packages/preview-server/src/components/topbar/emulated-dark-mode-toggle.tsx`
- **Name:** `emulated-dark-mode-toggle.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,877 bytes (1.83 KB)
- **Lines of Code:** 59

---

## Original Source

```tsx
import * as Toggle from '@radix-ui/react-toggle';
import { cn } from '../../utils';
import { IconMoon } from '../icons/icon-moon';
import { IconSun } from '../icons/icon-sun';
import { Tooltip } from '../tooltip';

interface EmulatedDarkModeToggleProps {
  enabled: boolean;
  onChange: (enabled: boolean) => unknown;
}

export const EmulatedDarkModeToggle = ({
  enabled,
  onChange,
}: EmulatedDarkModeToggleProps) => {
  return (
    <Tooltip>
      <Tooltip.Trigger asChild>
        <Toggle.Root
          value="dark"
          className={cn(
            'relative w-9 h-9 flex items-center justify-center border border-slate-6 text-sm rounded-lg transition duration-200 ease-in-out',
            'text-slate-11 hover:text-slate-12 aria-pressed:bg-slate-4',
          )}
          pressed={enabled}
          onPressedChange={() => onChange(!enabled)}
        >
          <div className="relative w-5 h-5">
            <div
              className={cn(
                'absolute inset-0 flex items-center justify-center transition-all duration-300 ease-in-out',
                enabled
                  ? 'opacity-0 scale-50 rotate-90'
                  : 'opacity-100 scale-100 rotate-0',
              )}
            >
              <IconMoon />
            </div>
            <div
              className={cn(
                'absolute inset-0 flex items-center justify-center transition-all duration-300 ease-in-out',
                enabled
                  ? 'opacity-100 scale-100 rotate-0'
                  : 'opacity-0 scale-50 -rotate-90',
              )}
            >
              <IconSun />
            </div>
          </div>
        </Toggle.Root>
      </Tooltip.Trigger>
      <Tooltip.Content>
        When enabled, inverts colors in the preview emulating what email clients
        do in dark mode.
      </Tooltip.Content>
    </Tooltip>
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

- `EmulatedDarkModeToggle()`

### Interfaces

- `EmulatedDarkModeToggleProps`

### Dependencies

This file imports/requires:

- `../../utils`
- `../icons/icon-moon`
- `../icons/icon-sun`
- `../tooltip`
- `@radix-ui/react-toggle`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 60

- `Content`
- `EmulatedDarkModeToggle`
- `EmulatedDarkModeToggleProps`
- `IconMoon`
- `IconSun`
- `Root`
- `Toggle`
- `Tooltip`
- `Trigger`
- `When`
- `absolute`
- `all`
- `aria`
- `asChild`
- `boolean`
- `border`
- `center`
- `className`
- `clients`
- `colors`
- `dark`
- `div`
- `duration`
- `ease`
- `email`
- `emulating`
- `enabled`
- `flex`
- `hover`
- `icon`
- `icons`
- `inset`
- `interface`
- `inverts`
- `items`
- `justify`
- `mode`
- `moon`
- `onChange`
- `onPressedChange`
- `opacity`
- `out`
- `pressed`
- `preview`
- `radix`
- `react`
- `relative`
- `rotate`
- `rounded`
- `scale`
- `slate`
- `sun`
- `text`
- `toggle`
- `tooltip`
- `transition`
- `unknown`
- `utils`
- `value`
- `what`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

