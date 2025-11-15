# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/avatars-rounded/inline-styles.tsx`
**Language:** tsx
**Size:** 1,530 bytes
**Lines:** 68
**Generated:** 2025-11-15T20:37:33.108044Z

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

- **Path:** `apps/web/components/avatars-rounded/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,530 bytes (1.49 KB)
- **Lines of Code:** 68

---

## Original Source

```tsx
import { Column, Img, Row } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Row>
    <Column align="center">
      <Img
        src="https://github.com/zenorocha.png?size=100"
        alt="Zeno Rocha"
        width="30"
        height="30"
        style={{
          display: 'inline-block',
          width: '30px',
          height: '30px',
          borderRadius: '6px',
        }}
      />
    </Column>
    <Column align="center">
      <Img
        src="https://github.com/zenorocha.png?size=100"
        alt="Zeno Rocha"
        width="42"
        height="42"
        style={{
          display: 'inline-block',
          width: '42px',
          height: '42px',
          borderRadius: '6px',
        }}
      />
    </Column>
    <Column align="center">
      <Img
        src="https://github.com/zenorocha.png?size=100"
        alt="Zeno Rocha"
        width="54"
        height="54"
        style={{
          display: 'inline-block',
          width: '54px',
          height: '54px',
          borderRadius: '6px',
        }}
      />
    </Column>
    <Column align="center">
      <Img
        src="https://github.com/zenorocha.png?size=100"
        alt="Zeno Rocha"
        width="66"
        height="66"
        style={{
          display: 'inline-block',
          width: '66px',
          height: '66px',
          borderRadius: '6px',
        }}
      />
    </Column>
  </Row>
);

export default () => {
  return <Layout>{component}</Layout>;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `component()`

### Dependencies

This file imports/requires:

- `../_components/layout`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 29

- `Column`
- `Img`
- `Layout`
- `Rocha`
- `Row`
- `Zeno`
- `_components`
- `align`
- `alt`
- `block`
- `borderRadius`
- `center`
- `com`
- `component`
- `components`
- `display`
- `email`
- `github`
- `height`
- `https`
- `inline`
- `layout`
- `png`
- `react`
- `size`
- `src`
- `style`
- `width`
- `zenorocha`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

