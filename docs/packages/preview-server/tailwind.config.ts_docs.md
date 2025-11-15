# Documentation: tailwind.config.ts
**File Path:** `packages/preview-server/tailwind.config.ts`
**Language:** typescript
**Size:** 3,058 bytes
**Lines:** 100
**Generated:** 2025-11-15T20:37:31.759498Z

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

- **Path:** `packages/preview-server/tailwind.config.ts`
- **Name:** `tailwind.config.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 3,058 bytes (2.99 KB)
- **Lines of Code:** 100

---

## Original Source

```typescript
import * as colors from '@radix-ui/colors';
import type { Config } from 'tailwindcss';

import { fontFamily } from 'tailwindcss/defaultTheme';
import plugin from 'tailwindcss/plugin';

const numberInputArrowHide = plugin(({ addUtilities }) => {
  addUtilities({
    '.arrow-hide': {
      appearance: 'textfield',
      '&::-webkit-inner-spin-button': {
        appearance: 'none',
        margin: '0px',
      },
      '&::-webkit-outer-spin-button': {
        appearance: 'none',
        margin: '0px',
      },
    },
  });
});

const config: Config = {
  content: {
    // needs to be relative because tailwind will find the content
    // by default based on the process's cwd
    relative: true,
    files: [
      './src/components/**/*.{js,ts,jsx,tsx,mdx}',
      './src/app/**/*.{js,ts,jsx,tsx,mdx}',
    ],
  },
  theme: {
    extend: {
      backgroundImage: {
        gradient:
          'linear-gradient(145.37deg, rgba(255, 255, 255, 0.09) -8.75%, rgba(255, 255, 255, 0.027) 83.95%)',
        gradientHover:
          'linear-gradient(145.37deg, rgba(255, 255, 255, 0.1) -8.75%, rgba(255, 255, 255, 0.057) 83.95%)',
        shine:
          'linear-gradient(45deg, rgba(255,255,255,0) 45%,rgba(255,255,255,1) 50%,rgba(255,255,255,0) 55%,rgba(255,255,255,0) 100%)',
      },
      colors: {
        cyan: {
          1: colors.cyanDarkA.cyanA1,
          2: colors.cyanDarkA.cyanA2,
          3: colors.cyanDarkA.cyanA3,
          4: colors.cyanDarkA.cyanA4,
          5: colors.cyanDarkA.cyanA5,
          6: colors.cyanDarkA.cyanA6,
          7: colors.cyanDarkA.cyanA7,
          8: colors.cyanDarkA.cyanA8,
          9: colors.cyanDarkA.cyanA9,
          10: colors.cyanDarkA.cyanA10,
          11: colors.cyanDarkA.cyanA11,
          12: colors.cyanDarkA.cyanA12,
        },
        slate: {
          1: colors.slateDarkA.slateA1,
          2: colors.slateDarkA.slateA2,
          3: colors.slateDarkA.slateA3,
          4: colors.slateDarkA.slateA4,
          5: colors.slateDarkA.slateA5,
          6: colors.slateDarkA.slateA6,
          7: colors.slateDarkA.slateA7,
          8: colors.slateDarkA.slateA8,
          9: colors.slateDarkA.slateA9,
          10: colors.slateDarkA.slateA10,
          11: colors.slateDarkA.slateA11,
          12: colors.slateDarkA.slateA12,
        },
      },
      fontFamily: {
        sans: ['var(--font-inter)', ...fontFamily.sans],
        mono: ['var(--font-sf-mono)', ...fontFamily.mono],
      },
      keyframes: {
        shine: {
          '0%': { backgroundPosition: '-100%' },
          '100%': { backgroundPosition: '100%' },
        },
        dash: {
          '0%': { strokeDashoffset: '1000' },
          '100%': { strokeDashoffset: '0' },
        },
        spin: {
          '0%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(360deg)' },
        },
      },
      animation: {
        'spin-slow': 'spin 3s linear infinite',
        'spin-fast': 'spin 1.5s linear infinite',
      },
    },
  },
  plugins: [numberInputArrowHide],
};
export default config;

```

---

## Overview

This is a JavaScript/TypeScript file. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `numberInputArrowHide()`

### Dependencies

This file imports/requires:

- `@radix-ui/colors`
- `tailwindcss`
- `tailwindcss/defaultTheme`
- `tailwindcss/plugin`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 88

- `Config`
- `addUtilities`
- `animation`
- `app`
- `appearance`
- `arrow`
- `backgroundImage`
- `backgroundPosition`
- `based`
- `because`
- `button`
- `colors`
- `components`
- `config`
- `content`
- `cwd`
- `cyan`
- `cyanA1`
- `cyanA10`
- `cyanA11`
- `cyanA12`
- `cyanA2`
- `cyanA3`
- `cyanA4`
- `cyanA5`
- `cyanA6`
- `cyanA7`
- `cyanA8`
- `cyanA9`
- `cyanDarkA`
- `dash`
- `defaultTheme`
- `extend`
- `fast`
- `files`
- `find`
- `font`
- `fontFamily`
- `gradient`
- `gradientHover`
- `hide`
- `infinite`
- `inner`
- `inter`
- `jsx`
- `keyframes`
- `linear`
- `margin`
- `mdx`
- `mono`
- `needs`
- `numberInputArrowHide`
- `outer`
- `plugin`
- `plugins`
- `process`
- `radix`
- `relative`
- `rgba`
- `rotate`
- `sans`
- `shine`
- `slate`
- `slateA1`
- `slateA10`
- `slateA11`
- `slateA12`
- `slateA2`
- `slateA3`
- `slateA4`
- `slateA5`
- `slateA6`
- `slateA7`
- `slateA8`
- `slateA9`
- `slateDarkA`
- `slow`
- `spin`
- `src`
- `strokeDashoffset`
- `tailwind`
- `tailwindcss`
- `textfield`
- `theme`
- `transform`
- `tsx`
- `type`
- `webkit`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

