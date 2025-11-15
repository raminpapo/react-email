# Documentation: resolve-calc-expressions.spec.ts
**File Path:** `packages/tailwind/src/utils/css/resolve-calc-expressions.spec.ts`
**Language:** typescript
**Size:** 924 bytes
**Lines:** 31
**Generated:** 2025-11-15T20:37:32.462820Z

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

- **Path:** `packages/tailwind/src/utils/css/resolve-calc-expressions.spec.ts`
- **Name:** `resolve-calc-expressions.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 924 bytes (0.90 KB)
- **Lines of Code:** 31

---

## Original Source

```typescript
import { generate, parse } from 'css-tree';
import { resolveCalcExpressions } from './resolve-calc-expressions';

describe('resolveCalcExpressions()', () => {
  it('resolves spacing calc expressions from tailwind v4', () => {
    const root = parse(`
.px-3{padding-inline:calc(0.25rem*3)}
.py-2{padding-block:calc(0.25rem*2)}
  `);
    resolveCalcExpressions(root);
    expect(generate(root)).toMatchSnapshot();
  });

  it('resolves calc expressions repeating decimals', () => {
    const root = parse(`
      .w-1/3 { width: calc(0.3333333333333333*100%); }
    `);
    resolveCalcExpressions(root);
    expect(generate(root)).toMatchSnapshot();
  });

  it('does not modify complex calc expressions', () => {
    const root = parse(`
.px-3{padding-inline:calc(0.25rem*(3 + 1px))}
.py-2{padding-block:calc(0.25rem*(2 + 1px))}
  `);
    resolveCalcExpressions(root);
    expect(generate(root)).toMatchSnapshot();
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

- `root()`

### Dependencies

This file imports/requires:

- `./resolve-calc-expressions`
- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 23

- `block`
- `calc`
- `complex`
- `css`
- `decimals`
- `describe`
- `expect`
- `expressions`
- `generate`
- `inline`
- `modify`
- `padding`
- `parse`
- `repeating`
- `resolve`
- `resolveCalcExpressions`
- `resolves`
- `root`
- `spacing`
- `tailwind`
- `toMatchSnapshot`
- `tree`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

