# Documentation: link.spec.tsx
**File Path:** `packages/link/src/link.spec.tsx`
**Language:** tsx
**Size:** 1,063 bytes
**Lines:** 36
**Generated:** 2025-11-15T20:37:32.628468Z

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

- **Path:** `packages/link/src/link.spec.tsx`
- **Name:** `link.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,063 bytes (1.04 KB)
- **Lines of Code:** 36

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Link } from './index';

describe('<Link> component', () => {
  it('renders children correctly', async () => {
    const testMessage = 'Test message';
    const html = await render(
      <Link href="https://example.com">{testMessage}</Link>,
    );
    expect(html).toContain(testMessage);
  });

  it('passes style and other props correctly', async () => {
    const style = { color: 'red' };
    const html = await render(
      <Link data-testid="link-test" href="https://example.com" style={style}>
        Test
      </Link>,
    );
    expect(html).toContain('color:red');
    expect(html).toContain('data-testid="link-test"');
  });

  it('opens in a new tab', async () => {
    const html = await render(<Link href="https://example.com">Test</Link>);
    expect(html).toContain(`target="_blank"`);
  });

  it('renders correctly', async () => {
    const actualOutput = await render(
      <Link href="https://example.com">Example</Link>,
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
- `testMessage()`

### Dependencies

This file imports/requires:

- `./index`
- `@react-email/render`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 37

- `Example`
- `Link`
- `Test`
- `_blank`
- `actualOutput`
- `children`
- `color`
- `com`
- `component`
- `correctly`
- `data`
- `describe`
- `email`
- `example`
- `expect`
- `href`
- `html`
- `https`
- `index`
- `link`
- `message`
- `opens`
- `other`
- `passes`
- `props`
- `react`
- `red`
- `render`
- `renders`
- `style`
- `tab`
- `target`
- `test`
- `testMessage`
- `testid`
- `toContain`
- `toMatchSnapshot`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

