# Documentation: text.spec.tsx
**File Path:** `packages/text/src/text.spec.tsx`
**Language:** tsx
**Size:** 885 bytes
**Lines:** 28
**Generated:** 2025-11-15T20:37:31.450167Z

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

- **Path:** `packages/text/src/text.spec.tsx`
- **Name:** `text.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 885 bytes (0.86 KB)
- **Lines of Code:** 28

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Text } from './index';

describe('<Text> component', () => {
  it('renders children correctly', async () => {
    const testMessage = 'Test message';
    const html = await render(<Text>{testMessage}</Text>);
    expect(html).toMatchSnapshot();
  });

  it("gives priority to the user's style", async () => {
    const style = { margin: '12px', marginTop: '0px' };
    const html = await render(<Text style={style} />);
    expect(html).toMatchSnapshot();
  });

  it('passes style and other props correctly', async () => {
    const style = { fontSize: '16px' };
    const html = await render(<Text style={style}>Test</Text>);
    expect(html).toMatchSnapshot();
  });

  it('renders correctly', async () => {
    const actualOutput = await render(<Text>Lorem ipsum</Text>);
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

**Total Unique Identifiers:** 29

- `Lorem`
- `Test`
- `Text`
- `actualOutput`
- `children`
- `component`
- `correctly`
- `describe`
- `email`
- `expect`
- `fontSize`
- `gives`
- `html`
- `index`
- `ipsum`
- `margin`
- `marginTop`
- `message`
- `other`
- `passes`
- `priority`
- `props`
- `react`
- `render`
- `renders`
- `style`
- `testMessage`
- `toMatchSnapshot`
- `user`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

