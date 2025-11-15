# Documentation: setup-tailwind.spec.ts
**File Path:** `packages/tailwind/src/utils/tailwindcss/setup-tailwind.spec.ts`
**Language:** typescript
**Size:** 430 bytes
**Lines:** 15
**Generated:** 2025-11-15T20:37:32.425776Z

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

- **Path:** `packages/tailwind/src/utils/tailwindcss/setup-tailwind.spec.ts`
- **Name:** `setup-tailwind.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 430 bytes (0.42 KB)
- **Lines of Code:** 15

---

## Original Source

```typescript
import { generate } from 'css-tree';
import { setupTailwind } from './setup-tailwind';

test('setupTailwind() and addUtilities()', async () => {
  const { addUtilities, getStyleSheet } = await setupTailwind({});

  addUtilities(['text-red-500', 'sm:bg-blue-300', 'bg-slate-900']);

  expect(generate(getStyleSheet())).toMatchSnapshot();

  addUtilities(['bg-red-100']);

  expect(generate(getStyleSheet())).toMatchSnapshot();
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `./setup-tailwind`
- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 15

- `addUtilities`
- `blue`
- `css`
- `expect`
- `generate`
- `getStyleSheet`
- `red`
- `setup`
- `setupTailwind`
- `slate`
- `tailwind`
- `test`
- `text`
- `toMatchSnapshot`
- `tree`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

