# Documentation: heading.spec.tsx
**File Path:** `packages/heading/src/heading.spec.tsx`
**Language:** tsx
**Size:** 884 bytes
**Lines:** 31
**Generated:** 2025-11-15T20:37:32.283715Z

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

- **Path:** `packages/heading/src/heading.spec.tsx`
- **Name:** `heading.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 884 bytes (0.86 KB)
- **Lines of Code:** 31

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Heading } from './index';

describe('render', () => {
  it('renders children correctly', async () => {
    const testMessage = 'Test message';
    const html = await render(<Heading>{testMessage}</Heading>);
    expect(html).toContain(testMessage);
  });

  it('passes style and other props correctly', async () => {
    const style = { backgroundColor: 'red' };
    const html = await render(
      <Heading data-testid="heading-test" style={style}>
        Test
      </Heading>,
    );
    expect(html).toContain('background-color:red');
    expect(html).toContain('data-testid="heading-test"');
  });

  it('renders the <Heading> component', async () => {
    const actualOutput = await render(
      <Heading as="h2" mx={4}>
        Lorem ipsum
      </Heading>,
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

**Total Unique Identifiers:** 32

- `Heading`
- `Lorem`
- `Test`
- `actualOutput`
- `background`
- `backgroundColor`
- `children`
- `color`
- `component`
- `correctly`
- `data`
- `describe`
- `email`
- `expect`
- `heading`
- `html`
- `index`
- `ipsum`
- `message`
- `other`
- `passes`
- `props`
- `react`
- `red`
- `render`
- `renders`
- `style`
- `test`
- `testMessage`
- `testid`
- `toContain`
- `toMatchSnapshot`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

