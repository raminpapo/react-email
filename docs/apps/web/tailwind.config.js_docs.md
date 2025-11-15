# Documentation: tailwind.config.js
**File Path:** `apps/web/tailwind.config.js`
**Language:** javascript
**Size:** 2,697 bytes
**Lines:** 86
**Generated:** 2025-11-15T20:37:32.795922Z

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

- **Path:** `apps/web/tailwind.config.js`
- **Name:** `tailwind.config.js`
- **Extension:** `.js`
- **Language:** javascript
- **Size:** 2,697 bytes (2.63 KB)
- **Lines of Code:** 86

---

## Original Source

```javascript
const defaultTheme = require('tailwindcss/defaultTheme');
const colors = require('@radix-ui/colors');
const plugin = require('tailwindcss/plugin');

const iOsHeight = plugin(({ addUtilities }) => {
  const supportsTouchRule = '@supports (-webkit-touch-callout: none)';
  const webkitFillAvailable = '-webkit-fill-available';

  const utilities = {
    '.min-h-screen-ios': {
      [supportsTouchRule]: {
        minHeight: webkitFillAvailable,
      },
    },
    '.h-screen-ios': {
      [supportsTouchRule]: {
        height: webkitFillAvailable,
      },
    },
  };

  addUtilities(utilities, ['responsive']);
});

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
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
        sans: ['var(--font-inter)', ...defaultTheme.fontFamily.sans],
        mono: ['var(--font-commit-mono)', ...defaultTheme.fontFamily.mono],
      },
      backgroundImage: {
        gradient:
          'linear-gradient(145.37deg, rgba(255, 255, 255, 0.09) -8.75%, rgba(255, 255, 255, 0.027) 83.95%)',
        gradientHover:
          'linear-gradient(145.37deg, rgba(255, 255, 255, 0.1) -8.75%, rgba(255, 255, 255, 0.057) 83.95%)',
        shine:
          'linear-gradient(45deg, rgba(255,255,255,0) 45%,rgba(255,255,255,1) 50%,rgba(255,255,255,0) 55%,rgba(255,255,255,0) 100%)',
      },
      keyframes: {
        shine: {
          '0%': { backgroundPosition: '0%' },
          '100%': { backgroundPosition: '110%' },
        },
        dash: {
          '0%': { strokeDashoffset: 1000 },
          '100%': { strokeDashoffset: 0 },
        },
      },
    },
  },
  plugins: [iOsHeight],
};

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `colors()`
- `defaultTheme()`
- `iOsHeight()`
- `plugin()`
- `supportsTouchRule()`
- `utilities()`
- `webkitFillAvailable()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 78

- `Config`
- `addUtilities`
- `available`
- `backgroundImage`
- `backgroundPosition`
- `callout`
- `colors`
- `commit`
- `content`
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
- `exports`
- `extend`
- `fill`
- `font`
- `fontFamily`
- `gradient`
- `gradientHover`
- `height`
- `iOsHeight`
- `inter`
- `ios`
- `jsx`
- `keyframes`
- `linear`
- `min`
- `minHeight`
- `module`
- `mono`
- `plugin`
- `plugins`
- `radix`
- `require`
- `responsive`
- `rgba`
- `sans`
- `screen`
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
- `src`
- `strokeDashoffset`
- `supports`
- `supportsTouchRule`
- `tailwindcss`
- `theme`
- `touch`
- `tsx`
- `type`
- `utilities`
- `webkit`
- `webkitFillAvailable`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

