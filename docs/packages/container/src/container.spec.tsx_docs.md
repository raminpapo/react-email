# Documentation: container.spec.tsx
**File Path:** `packages/container/src/container.spec.tsx`
**Language:** tsx
**Size:** 974 bytes
**Lines:** 32
**Generated:** 2025-11-15T20:37:32.247036Z

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

- **Path:** `packages/container/src/container.spec.tsx`
- **Name:** `container.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 974 bytes (0.95 KB)
- **Lines of Code:** 32

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Container } from './index';

describe('<Container> component', () => {
  it('renders children correctly', async () => {
    const testMessage = 'Test message';
    const html = await render(<Container>{testMessage}</Container>);
    expect(html).toContain(testMessage);
  });

  it('passes style and other props correctly', async () => {
    const style = { maxWidth: 300, backgroundColor: 'red' };
    const html = await render(
      <Container data-testid="container-test" style={style}>
        Test
      </Container>,
    );
    expect(html).toContain('style="max-width:300px;background-color:red"');
    expect(html).toContain('data-testid="container-test"');
  });

  it('renders correctly', async () => {
    const container = await render(
      <Container style={{ maxWidth: '300px' }}>
        <button type="button">Hi</button>
      </Container>,
    );

    expect(container).toMatchSnapshot();
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

- `container()`
- `html()`
- `style()`
- `testMessage()`

### Dependencies

This file imports/requires:

- `./index`
- `@react-email/render`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 34

- `Container`
- `Test`
- `background`
- `backgroundColor`
- `button`
- `children`
- `color`
- `component`
- `container`
- `correctly`
- `data`
- `describe`
- `email`
- `expect`
- `html`
- `index`
- `max`
- `maxWidth`
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
- `type`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

