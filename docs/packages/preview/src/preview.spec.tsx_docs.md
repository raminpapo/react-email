# Documentation: preview.spec.tsx
**File Path:** `packages/preview/src/preview.spec.tsx`
**Language:** tsx
**Size:** 1,699 bytes
**Lines:** 44
**Generated:** 2025-11-15T20:37:32.264669Z

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

- **Path:** `packages/preview/src/preview.spec.tsx`
- **Name:** `preview.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,699 bytes (1.66 KB)
- **Lines of Code:** 44

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Preview, renderWhiteSpace } from './index';

describe('<Preview> component', () => {
  it('renders correctly', async () => {
    const actualOutput = await render(<Preview>Email preview text</Preview>);
    expect(actualOutput).toMatchSnapshot();
  });

  it('renders correctly with array text', async () => {
    const actualOutputArray = await render(
      <Preview>Email preview text</Preview>,
    );
    expect(actualOutputArray).toMatchSnapshot();
  });

  it('renders correctly with really long text', async () => {
    const longText = 'really long'.repeat(100);
    const actualOutputLong = await render(<Preview>{longText}</Preview>);
    expect(actualOutputLong).toMatchSnapshot();
  });
});

describe('renderWhiteSpace', () => {
  it('renders null when text length is greater than or equal to PREVIEW_MAX_LENGTH (150)', () => {
    const text =
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Tenetur dolore mollitia dignissimos itaque. At excepturi reiciendis iure molestias incidunt. Ab saepe, nostrum dicta dolor maiores tenetur eveniet odio amet ipsum?';
    const html = renderWhiteSpace(text);
    expect(html).toBeNull();
  });

  it('renders white space characters when text length is less than PREVIEW_MAX_LENGTH', () => {
    const text = 'Short text';
    const whiteSpaceCharacters = '\xa0\u200C\u200B\u200D\u200E\u200F\uFEFF';

    const html = renderWhiteSpace(text);
    expect(html).not.toBeNull();

    const actualTextContent = html?.props.children;
    const expectedTextContent = whiteSpaceCharacters.repeat(150 - text.length);
    expect(actualTextContent).toBe(expectedTextContent);
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `actualOutput()`
- `actualOutputArray()`
- `actualOutputLong()`
- `actualTextContent()`
- `expectedTextContent()`
- `html()`
- `longText()`
- `text()`
- `whiteSpaceCharacters()`

### Dependencies

This file imports/requires:

- `./index`
- `@react-email/render`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 74

- `Email`
- `Lorem`
- `PREVIEW_MAX_LENGTH`
- `Preview`
- `Short`
- `Tenetur`
- `actualOutput`
- `actualOutputArray`
- `actualOutputLong`
- `actualTextContent`
- `adipisicing`
- `amet`
- `array`
- `characters`
- `children`
- `component`
- `consectetur`
- `correctly`
- `describe`
- `dicta`
- `dignissimos`
- `dolor`
- `dolore`
- `elit`
- `email`
- `equal`
- `eveniet`
- `excepturi`
- `expect`
- `expectedTextContent`
- `greater`
- `html`
- `incidunt`
- `index`
- `ipsum`
- `itaque`
- `iure`
- `length`
- `less`
- `long`
- `longText`
- `maiores`
- `molestias`
- `mollitia`
- `nostrum`
- `odio`
- `preview`
- `props`
- `react`
- `really`
- `reiciendis`
- `render`
- `renderWhiteSpace`
- `renders`
- `repeat`
- `saepe`
- `sit`
- `space`
- `tenetur`
- `text`
- `than`
- `toBe`
- `toBeNull`
- `toMatchSnapshot`
- `u200B`
- `u200C`
- `u200D`
- `u200E`
- `u200F`
- `uFEFF`
- `when`
- `white`
- `whiteSpaceCharacters`
- `xa0`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

