# Documentation: html.spec.tsx
**File Path:** `packages/html/src/html.spec.tsx`
**Language:** tsx
**Size:** 742 bytes
**Lines:** 25
**Generated:** 2025-11-15T20:37:32.341096Z

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

- **Path:** `packages/html/src/html.spec.tsx`
- **Name:** `html.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 742 bytes (0.72 KB)
- **Lines of Code:** 25

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Html } from './index';

describe('<Html> component', () => {
  it('renders children correctly', async () => {
    const testMessage = 'Test message';
    const html = await render(<Html>{testMessage}</Html>);
    expect(html).toContain(testMessage);
  });

  it('passes props correctly', async () => {
    const html = await render(
      <Html data-testid="html-test" dir="rtl" lang="fr" />,
    );
    expect(html).toContain('lang="fr"');
    expect(html).toContain('dir="rtl"');
    expect(html).toContain('data-testid="html-test"');
  });

  it('renders correctly', async () => {
    const actualOutput = await render(<Html />);
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
- `testMessage()`

### Dependencies

This file imports/requires:

- `./index`
- `@react-email/render`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 26

- `Html`
- `Test`
- `actualOutput`
- `children`
- `component`
- `correctly`
- `data`
- `describe`
- `dir`
- `email`
- `expect`
- `html`
- `index`
- `lang`
- `message`
- `passes`
- `props`
- `react`
- `render`
- `renders`
- `rtl`
- `test`
- `testMessage`
- `testid`
- `toContain`
- `toMatchSnapshot`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

