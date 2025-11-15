# Documentation: button.spec.tsx
**File Path:** `packages/button/src/button.spec.tsx`
**Language:** tsx
**Size:** 1,462 bytes
**Lines:** 48
**Generated:** 2025-11-15T20:37:32.217745Z

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

- **Path:** `packages/button/src/button.spec.tsx`
- **Name:** `button.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,462 bytes (1.43 KB)
- **Lines of Code:** 48

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Button } from './index';

describe('<Button> component', () => {
  it('renders children correctly', async () => {
    const testMessage = 'Test message';
    const html = await render(<Button>{testMessage}</Button>);
    expect(html).toContain(testMessage);
  });

  it('passes style and other props correctly', async () => {
    const style = { backgroundColor: 'red' };
    const html = await render(
      <Button data-testid="button-test" style={style}>
        Test
      </Button>,
    );
    expect(html).toContain('background-color:red');
    expect(html).toContain('data-testid="button-test"');
  });

  it('renders correctly  with padding values from style prop', async () => {
    const actualOutput = await render(
      <Button href="https://example.com" style={{ padding: '12px 20px' }} />,
    );
    expect(actualOutput).toMatchSnapshot();
  });

  it('renders the <Button> component with no padding value', async () => {
    const actualOutput = await render(<Button href="https://example.com" />);
    expect(actualOutput).toMatchSnapshot();
  });

  it('allows users to overwrite style props', async () => {
    const actualOutput = await render(
      <Button
        style={{
          lineHeight: '150%',
          display: 'block',
          textDecoration: 'underline red',
          maxWidth: '50%',
        }}
      />,
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

**Total Unique Identifiers:** 47

- `Button`
- `Test`
- `actualOutput`
- `allows`
- `background`
- `backgroundColor`
- `block`
- `button`
- `children`
- `color`
- `com`
- `component`
- `correctly`
- `data`
- `describe`
- `display`
- `email`
- `example`
- `expect`
- `href`
- `html`
- `https`
- `index`
- `lineHeight`
- `maxWidth`
- `message`
- `other`
- `overwrite`
- `padding`
- `passes`
- `prop`
- `props`
- `react`
- `red`
- `render`
- `renders`
- `style`
- `test`
- `testMessage`
- `testid`
- `textDecoration`
- `toContain`
- `toMatchSnapshot`
- `underline`
- `users`
- `value`
- `values`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

