# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/two-buttons/inline-styles.tsx`
**Language:** tsx
**Size:** 1,725 bytes
**Lines:** 67
**Generated:** 2025-11-15T20:37:33.008668Z

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

- **Path:** `apps/web/components/two-buttons/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,725 bytes (1.68 KB)
- **Lines of Code:** 67

---

## Original Source

```tsx
import { Button, Column, Row } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Row>
    <Column align="center">
      <Row>
        <td
          align="center"
          colSpan={1}
          style={{ paddingRight: 16, width: '50%' }}
        >
          <Button
            href="https://react.email"
            style={{
              width: '100%',
              boxSizing: 'border-box',
              paddingLeft: 20,
              paddingRight: 20,
              paddingTop: 12,
              paddingBottom: 12,
              borderRadius: 8,
              backgroundColor: 'rgb(79,70,229)',
              textAlign: 'center',
              fontWeight: 600,
              color: 'rgb(255,255,255)',
            }}
          >
            Login
          </Button>
        </td>
        <td
          align="center"
          colSpan={1}
          style={{ paddingLeft: 16, width: '50%' }}
        >
          <Button
            href="https://react.email"
            style={{
              width: '100%',
              boxSizing: 'border-box',
              paddingLeft: 20,
              paddingRight: 20,
              paddingTop: 12,
              paddingBottom: 12,
              borderRadius: 8,
              borderWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
              textAlign: 'center',
              backgroundColor: 'rgb(255,255,255)',
              fontWeight: 600,
              color: 'rgb(17,24,39)',
            }}
          >
            Sign up
          </Button>
        </td>
      </Row>
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

**Total Unique Identifiers:** 36

- `Button`
- `Column`
- `Layout`
- `Login`
- `Row`
- `Sign`
- `_components`
- `align`
- `backgroundColor`
- `border`
- `borderColor`
- `borderRadius`
- `borderStyle`
- `borderWidth`
- `box`
- `boxSizing`
- `center`
- `colSpan`
- `color`
- `component`
- `components`
- `email`
- `fontWeight`
- `href`
- `https`
- `layout`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `react`
- `rgb`
- `solid`
- `style`
- `textAlign`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

