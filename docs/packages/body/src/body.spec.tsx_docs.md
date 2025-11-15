# Documentation: body.spec.tsx
**File Path:** `packages/body/src/body.spec.tsx`
**Language:** tsx
**Size:** 1,245 bytes
**Lines:** 39
**Generated:** 2025-11-15T20:37:31.540207Z

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

- **Path:** `packages/body/src/body.spec.tsx`
- **Name:** `body.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,245 bytes (1.22 KB)
- **Lines of Code:** 39

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Body } from './index';
import { marginProperties } from './margin-properties';

describe('<Body> component', () => {
  it('renders children correctly', async () => {
    const testMessage = 'Test message';
    const html = await render(<Body>{testMessage}</Body>);
    expect(html).toContain(testMessage);
  });

  it('passes style and other props correctly', async () => {
    const style = { backgroundColor: 'red' };
    const html = await render(
      <Body data-testid="body-test" style={style}>
        Test
      </Body>,
    );
    expect(html).toContain('style="background-color:red"');
    expect(html).toContain('data-testid="body-test"');
  });

  it('renders correctly', async () => {
    const actualOutput = await render(<Body>Lorem ipsum</Body>);
    expect(actualOutput).toMatchSnapshot();
  });

  describe('margin resetting behavior', () => {
    for (const property of marginProperties) {
      it(`should reset the ${property} property when it comes from props`, async () => {
        const actualOutput = await render(
          <Body style={{ [property]: 10 }}>Random text</Body>,
        );
        expect(actualOutput).toMatchSnapshot();
      });
    }
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
- `./margin-properties`
- `@react-email/render`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 43

- `Body`
- `Lorem`
- `Random`
- `Test`
- `actualOutput`
- `background`
- `backgroundColor`
- `behavior`
- `body`
- `children`
- `color`
- `comes`
- `component`
- `correctly`
- `data`
- `describe`
- `email`
- `expect`
- `html`
- `index`
- `ipsum`
- `margin`
- `marginProperties`
- `message`
- `other`
- `passes`
- `properties`
- `property`
- `props`
- `react`
- `red`
- `render`
- `renders`
- `reset`
- `resetting`
- `style`
- `test`
- `testMessage`
- `testid`
- `text`
- `toContain`
- `toMatchSnapshot`
- `when`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

