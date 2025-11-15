# Documentation: img.spec.tsx
**File Path:** `packages/img/src/img.spec.tsx`
**Language:** tsx
**Size:** 812 bytes
**Lines:** 29
**Generated:** 2025-11-15T20:37:31.460707Z

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

- **Path:** `packages/img/src/img.spec.tsx`
- **Name:** `img.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 812 bytes (0.79 KB)
- **Lines of Code:** 29

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Img } from './index';

describe('<Img> component', () => {
  it('passes style and other props correctly', async () => {
    const style = { backgroundColor: 'red', border: 'solid 1px black' };
    const html = await render(
      <Img
        alt="Cat"
        data-testid="img-test"
        height="300"
        src="cat.jpg"
        style={style}
        width="300"
      />,
    );
    expect(html).toContain('background-color:red');
    expect(html).toContain('border:solid 1px black');
    expect(html).toContain('data-testid="img-test"');
  });

  it('renders correctly', async () => {
    const actualOutput = await render(
      <Img alt="Cat" height="300" src="cat.jpg" width="300" />,
    );
    expect(actualOutput).toMatchSnapshot();
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
- `html()`
- `style()`

### Dependencies

This file imports/requires:

- `./index`
- `@react-email/render`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 36

- `Cat`
- `Img`
- `actualOutput`
- `alt`
- `background`
- `backgroundColor`
- `black`
- `border`
- `cat`
- `color`
- `component`
- `correctly`
- `data`
- `describe`
- `email`
- `expect`
- `height`
- `html`
- `img`
- `index`
- `jpg`
- `other`
- `passes`
- `props`
- `react`
- `red`
- `render`
- `renders`
- `solid`
- `src`
- `style`
- `test`
- `testid`
- `toContain`
- `toMatchSnapshot`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

