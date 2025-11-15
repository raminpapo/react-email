# Documentation: sanitize-non-inlinable-rules.spec.ts
**File Path:** `packages/tailwind/src/utils/css/sanitize-non-inlinable-rules.spec.ts`
**Language:** typescript
**Size:** 1,360 bytes
**Lines:** 46
**Generated:** 2025-11-15T20:37:32.473447Z

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

- **Path:** `packages/tailwind/src/utils/css/sanitize-non-inlinable-rules.spec.ts`
- **Name:** `sanitize-non-inlinable-rules.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,360 bytes (1.33 KB)
- **Lines of Code:** 46

---

## Original Source

```typescript
import { generate } from 'css-tree';
import { setupTailwind } from '../tailwindcss/setup-tailwind';
import { sanitizeNonInlinableRules } from './sanitize-non-inlinable-rules';

describe('sanitizeNonInlinableRules()', () => {
  it('inlines rules that can be inlined', async () => {
    const tailwind = await setupTailwind({});
    tailwind.addUtilities(['bg-gray-900', 'text-red-300', 'text-lg']);
    const stylesheet = tailwind.getStyleSheet();

    sanitizeNonInlinableRules(stylesheet);
    expect(generate(stylesheet)).toMatchSnapshot();
  });

  it('handles CSS nesting in hover pseudo styles', async () => {
    const tailwind = await setupTailwind({});
    tailwind.addUtilities([
      'hover:text-sky-600',
      'sm:focus:outline-none',
      'md:hover:bg-gray-100',
      'lg:focus:underline',
    ]);

    const stylesheet = tailwind.getStyleSheet();

    sanitizeNonInlinableRules(stylesheet);
    expect(generate(stylesheet)).toMatchSnapshot();
  });

  it('supports basic media query rules', async () => {
    const tailwind = await setupTailwind({});
    tailwind.addUtilities([
      'sm:mx-auto',
      'sm:max-w-lg',
      'sm:rounded-lg',
      'md:px-10',
      'md:py-12',
    ]);
    const stylesheet = tailwind.getStyleSheet();

    sanitizeNonInlinableRules(stylesheet);

    expect(generate(stylesheet)).toMatchSnapshot();
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

- `stylesheet()`
- `tailwind()`

### Dependencies

This file imports/requires:

- `../tailwindcss/setup-tailwind`
- `./sanitize-non-inlinable-rules`
- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 39

- `addUtilities`
- `auto`
- `basic`
- `css`
- `describe`
- `expect`
- `focus`
- `generate`
- `getStyleSheet`
- `gray`
- `handles`
- `hover`
- `inlinable`
- `inlined`
- `inlines`
- `max`
- `media`
- `nesting`
- `non`
- `outline`
- `pseudo`
- `query`
- `red`
- `rounded`
- `rules`
- `sanitize`
- `sanitizeNonInlinableRules`
- `setup`
- `setupTailwind`
- `sky`
- `styles`
- `stylesheet`
- `supports`
- `tailwind`
- `tailwindcss`
- `text`
- `toMatchSnapshot`
- `tree`
- `underline`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

