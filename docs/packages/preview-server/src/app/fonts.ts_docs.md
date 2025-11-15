# Documentation: fonts.ts
**File Path:** `packages/preview-server/src/app/fonts.ts`
**Language:** typescript
**Size:** 765 bytes
**Lines:** 40
**Generated:** 2025-11-15T20:37:32.082387Z

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

- **Path:** `packages/preview-server/src/app/fonts.ts`
- **Name:** `fonts.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 765 bytes (0.75 KB)
- **Lines of Code:** 40

---

## Original Source

```typescript
import { Inter } from 'next/font/google';
import Local from 'next/font/local';

export const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
});

export const sfMono = Local({
  src: [
    {
      path: './fonts/SFMono/SFMonoLight.otf',
      weight: '300',
    },
    {
      path: './fonts/SFMono/SFMonoRegular.otf',
      weight: '400',
    },
    {
      path: './fonts/SFMono/SFMonoMedium.otf',
      weight: '500',
    },
    {
      path: './fonts/SFMono/SFMonoSemibold.otf',
      weight: '600',
    },
    {
      path: './fonts/SFMono/SFMonoBold.otf',
      weight: '700',
    },
    {
      path: './fonts/SFMono/SFMonoHeavy.otf',
      weight: '800',
    },
  ],
  variable: '--font-sf-mono',
  display: 'swap',
});

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `inter()`
- `sfMono()`

### Dependencies

This file imports/requires:

- `next/font/google`
- `next/font/local`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 26

- `Inter`
- `Local`
- `SFMono`
- `SFMonoBold`
- `SFMonoHeavy`
- `SFMonoLight`
- `SFMonoMedium`
- `SFMonoRegular`
- `SFMonoSemibold`
- `display`
- `font`
- `fonts`
- `google`
- `inter`
- `latin`
- `local`
- `mono`
- `next`
- `otf`
- `path`
- `sfMono`
- `src`
- `subsets`
- `swap`
- `variable`
- `weight`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

