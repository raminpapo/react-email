# Documentation: extract-rules-per-class.spec.ts
**File Path:** `packages/tailwind/src/utils/css/extract-rules-per-class.spec.ts`
**Language:** typescript
**Size:** 1,929 bytes
**Lines:** 62
**Generated:** 2025-11-15T20:37:32.450210Z

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

- **Path:** `packages/tailwind/src/utils/css/extract-rules-per-class.spec.ts`
- **Name:** `extract-rules-per-class.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,929 bytes (1.88 KB)
- **Lines of Code:** 62

---

## Original Source

```typescript
import { generate, type Rule } from 'css-tree';
import { setupTailwind } from '../tailwindcss/setup-tailwind';
import { extractRulesPerClass } from './extract-rules-per-class';

describe('extractRulesPerClass()', async () => {
  function convertToComparable(map: Map<string, Rule>): Record<string, string> {
    return Object.fromEntries(map.entries().map(([k, v]) => [k, generate(v)]));
  }

  it('works with just inlinable utilities', async () => {
    const tailwind = await setupTailwind({});
    const classes = ['text-center', 'bg-red-500'];
    tailwind.addUtilities(classes);

    const stylesheet = tailwind.getStyleSheet();

    const { inlinable, nonInlinable } = extractRulesPerClass(
      stylesheet,
      classes,
    );

    expect(convertToComparable(inlinable)).toMatchSnapshot();
    expect(convertToComparable(nonInlinable)).toMatchSnapshot();
  });

  it('handles non-inlinable utilities', async () => {
    const tailwind = await setupTailwind({});
    const classes = ['lg:w-1/2'];
    tailwind.addUtilities(classes);

    const stylesheet = tailwind.getStyleSheet();

    const { inlinable, nonInlinable } = extractRulesPerClass(
      stylesheet,
      classes,
    );

    expect(convertToComparable(inlinable)).toMatchSnapshot();
    expect(convertToComparable(nonInlinable)).toMatchSnapshot();
  });

  it('handles a mix of inlinable and non-inlinable utilities', async () => {
    const tailwind = await setupTailwind({});
    const classes = [
      'text-center',
      'bg-red-500',
      'some-other-class', // should be ignored
      'w-full',
      'lg:w-1/2',
    ];
    tailwind.addUtilities(classes);

    const stylesheet = tailwind.getStyleSheet();
    const { inlinable, nonInlinable } = extractRulesPerClass(
      stylesheet,
      classes,
    );
    expect(convertToComparable(inlinable)).toMatchSnapshot();
    expect(convertToComparable(nonInlinable)).toMatchSnapshot();
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

- `classes()`
- `convertToComparable()`
- `stylesheet()`
- `tailwind()`

### Type Definitions

- `Rule`

### Dependencies

This file imports/requires:

- `../tailwindcss/setup-tailwind`
- `./extract-rules-per-class`
- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 43

- `Map`
- `Object`
- `Record`
- `Rule`
- `addUtilities`
- `center`
- `classes`
- `convertToComparable`
- `css`
- `describe`
- `entries`
- `expect`
- `extract`
- `extractRulesPerClass`
- `fromEntries`
- `full`
- `generate`
- `getStyleSheet`
- `handles`
- `ignored`
- `inlinable`
- `just`
- `map`
- `mix`
- `non`
- `nonInlinable`
- `other`
- `per`
- `red`
- `rules`
- `setup`
- `setupTailwind`
- `some`
- `string`
- `stylesheet`
- `tailwind`
- `tailwindcss`
- `text`
- `toMatchSnapshot`
- `tree`
- `type`
- `utilities`
- `works`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

