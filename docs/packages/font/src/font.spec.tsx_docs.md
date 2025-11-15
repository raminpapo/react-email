# Documentation: font.spec.tsx
**File Path:** `packages/font/src/font.spec.tsx`
**Language:** tsx
**Size:** 1,354 bytes
**Lines:** 50
**Generated:** 2025-11-15T20:37:32.273863Z

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

- **Path:** `packages/font/src/font.spec.tsx`
- **Name:** `font.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,354 bytes (1.32 KB)
- **Lines of Code:** 50

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Font } from './index';

describe('<Font> component', () => {
  it('renders with default props', async () => {
    const html = await render(
      <Font fallbackFontFamily="Helvetica" fontFamily="Arial" />,
    );

    expect(html).toContain('font-style: normal;');
    expect(html).toContain('font-weight: 400;');
    expect(html).toContain("font-family: 'Arial';");
  });

  it('renders with webFont prop', async () => {
    const webFont = {
      url: 'example.com/font.woff',
      format: 'woff',
    } as const;

    const html = await render(
      <Font
        fallbackFontFamily="Helvetica"
        fontFamily="Example"
        webFont={webFont}
      />,
    );

    expect(html).toContain("font-family: 'Example';");
    expect(html).toContain(
      `src: url(${webFont.url}) format('${webFont.format}');`,
    );
  });

  it('renders with multiple fallback fonts', async () => {
    const html = await render(
      <Font fallbackFontFamily={['Helvetica', 'Verdana']} fontFamily="Arial" />,
    );

    expect(html).toContain("font-family: 'Arial', Helvetica, Verdana;");
  });

  it('renders correctly', async () => {
    const actualOutput = await render(
      <Font fallbackFontFamily="Verdana" fontFamily="Roboto" />,
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
- `webFont()`

### Dependencies

This file imports/requires:

- `./index`
- `@react-email/render`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 38

- `Arial`
- `Example`
- `Font`
- `Helvetica`
- `Roboto`
- `Verdana`
- `actualOutput`
- `com`
- `component`
- `correctly`
- `describe`
- `email`
- `example`
- `expect`
- `fallback`
- `fallbackFontFamily`
- `family`
- `font`
- `fontFamily`
- `fonts`
- `format`
- `html`
- `index`
- `multiple`
- `normal`
- `prop`
- `props`
- `react`
- `render`
- `renders`
- `src`
- `style`
- `toContain`
- `toMatchSnapshot`
- `url`
- `webFont`
- `weight`
- `woff`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

