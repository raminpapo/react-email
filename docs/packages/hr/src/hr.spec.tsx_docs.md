# Documentation: hr.spec.tsx
**File Path:** `packages/hr/src/hr.spec.tsx`
**Language:** tsx
**Size:** 616 bytes
**Lines:** 21
**Generated:** 2025-11-15T20:37:32.232358Z

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

- **Path:** `packages/hr/src/hr.spec.tsx`
- **Name:** `hr.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 616 bytes (0.60 KB)
- **Lines of Code:** 21

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Hr } from './index';

describe('<Hr> component', () => {
  it('passes styles and other props correctly', async () => {
    const style = {
      width: '50%',
      borderColor: 'black',
    };
    const html = await render(<Hr data-testid="hr-test" style={style} />);
    expect(html).toContain('width:50%');
    expect(html).toContain('border-color:black');
    expect(html).toContain('data-testid="hr-test"');
  });

  it('renders correctly', async () => {
    const actualOutput = await render(<Hr />);
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

**Total Unique Identifiers:** 26

- `actualOutput`
- `black`
- `border`
- `borderColor`
- `color`
- `component`
- `correctly`
- `data`
- `describe`
- `email`
- `expect`
- `html`
- `index`
- `other`
- `passes`
- `props`
- `react`
- `render`
- `renders`
- `style`
- `styles`
- `test`
- `testid`
- `toContain`
- `toMatchSnapshot`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

