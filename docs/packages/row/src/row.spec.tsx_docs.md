# Documentation: row.spec.tsx
**File Path:** `packages/row/src/row.spec.tsx`
**Language:** tsx
**Size:** 813 bytes
**Lines:** 27
**Generated:** 2025-11-15T20:37:32.206136Z

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

- **Path:** `packages/row/src/row.spec.tsx`
- **Name:** `row.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 813 bytes (0.79 KB)
- **Lines of Code:** 27

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Row } from './index';

describe('<Row> component', () => {
  it('renders children correctly', async () => {
    const testMessage = 'Test message';
    const html = await render(<Row>{testMessage}</Row>);
    expect(html).toContain(testMessage);
  });

  it('passes style and other props correctly', async () => {
    const style = { backgroundColor: 'red' };
    const html = await render(
      <Row data-testid="row-test" style={style}>
        Test
      </Row>,
    );
    expect(html).toContain('style="background-color:red"');
    expect(html).toContain('data-testid="row-test"');
  });

  it('renders correctly', async () => {
    const actualOutput = await render(<Row children={undefined} />);
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

**Total Unique Identifiers:** 30

- `Row`
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
- `html`
- `index`
- `message`
- `other`
- `passes`
- `props`
- `react`
- `red`
- `render`
- `renders`
- `row`
- `style`
- `test`
- `testMessage`
- `testid`
- `toContain`
- `toMatchSnapshot`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

