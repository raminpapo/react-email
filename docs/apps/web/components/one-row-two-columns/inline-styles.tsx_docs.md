# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/one-row-two-columns/inline-styles.tsx`
**Language:** tsx
**Size:** 1,073 bytes
**Lines:** 56
**Generated:** 2025-11-15T20:37:33.110325Z

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

- **Path:** `apps/web/components/one-row-two-columns/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,073 bytes (1.05 KB)
- **Lines of Code:** 56

---

## Original Source

```tsx
import { Column, Row } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <>
    <Row cellSpacing={8}>
      <Column
        align="center"
        style={{
          width: '50%',
          height: 40,
          backgroundColor: 'rgb(52,211,153,0.6)',
        }}
      >
        1/2
      </Column>
      <Column
        align="center"
        style={{
          width: '50%',
          height: 40,
          backgroundColor: 'rgb(34,211,238,0.6)',
        }}
      >
        1/2
      </Column>
    </Row>
    <Row>
      <Column
        align="center"
        style={{
          width: '33.333333%',
          height: 40,
          backgroundColor: 'rgb(244,114,182,0.6)',
        }}
      >
        1/3
      </Column>
      <Column
        align="center"
        style={{
          width: '66.666667%',
          height: 40,
          backgroundColor: 'rgb(192,132,252,0.6)',
        }}
      >
        2/3
      </Column>
    </Row>
  </>
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

**Total Unique Identifiers:** 17

- `Column`
- `Layout`
- `Row`
- `_components`
- `align`
- `backgroundColor`
- `cellSpacing`
- `center`
- `component`
- `components`
- `email`
- `height`
- `layout`
- `react`
- `rgb`
- `style`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

