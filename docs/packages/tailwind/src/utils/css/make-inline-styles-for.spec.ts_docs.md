# Documentation: make-inline-styles-for.spec.ts
**File Path:** `packages/tailwind/src/utils/css/make-inline-styles-for.spec.ts`
**Language:** typescript
**Size:** 878 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:32.455646Z

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

- **Path:** `packages/tailwind/src/utils/css/make-inline-styles-for.spec.ts`
- **Name:** `make-inline-styles-for.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 878 bytes (0.86 KB)
- **Lines of Code:** 33

---

## Original Source

```typescript
import { parse, type StyleSheet } from 'css-tree';
import { makeInlineStylesFor } from './make-inline-styles-for';

describe('makeInlineStylesFor()', async () => {
  it('works in simple use case', () => {
    const tailwindStyles = parse(`
      .bg-red-500 { background-color: #f56565; }
      .w-full { width: 100%; }
    `) as StyleSheet;

    expect(
      makeInlineStylesFor(tailwindStyles.children.toArray()),
    ).toMatchSnapshot();
  });

  it('does basic local variable resolution', () => {
    const tailwindStyles = parse(`
      .btn {
        --btn-bg: #3490dc;
        --btn-text: #fff;
        background-color: var(--btn-bg);
        color: var(--btn-text);
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
      }
    `) as StyleSheet;

    expect(
      makeInlineStylesFor(tailwindStyles.children.toArray()),
    ).toMatchSnapshot();
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `tailwindStyles()`

### Type Definitions

- `StyleSheet`

### Dependencies

This file imports/requires:

- `./make-inline-styles-for`
- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 34

- `StyleSheet`
- `background`
- `basic`
- `border`
- `btn`
- `children`
- `color`
- `css`
- `describe`
- `expect`
- `f56565`
- `fff`
- `full`
- `inline`
- `local`
- `make`
- `makeInlineStylesFor`
- `padding`
- `parse`
- `radius`
- `red`
- `resolution`
- `simple`
- `styles`
- `tailwindStyles`
- `text`
- `toArray`
- `toMatchSnapshot`
- `tree`
- `type`
- `use`
- `variable`
- `width`
- `works`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

