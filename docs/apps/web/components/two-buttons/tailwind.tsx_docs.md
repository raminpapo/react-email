# Documentation: tailwind.tsx
**File Path:** `apps/web/components/two-buttons/tailwind.tsx`
**Language:** tsx
**Size:** 960 bytes
**Lines:** 32
**Generated:** 2025-11-15T20:37:33.009902Z

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

- **Path:** `apps/web/components/two-buttons/tailwind.tsx`
- **Name:** `tailwind.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 960 bytes (0.94 KB)
- **Lines of Code:** 32

---

## Original Source

```tsx
import { Button, Column, Row } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Row>
    <Column align="center">
      <Row>
        <td align="center" className="w-1/2 pr-[16px]" colSpan={1}>
          <Button
            className="box-border w-full rounded-[8px] bg-indigo-600 px-[20px] py-[12px] text-center font-semibold text-white"
            href="https://react.email"
          >
            Login
          </Button>
        </td>
        <td align="center" className="w-1/2 pl-[16px]" colSpan={1}>
          <Button
            className="box-border w-full rounded-[8px] border border-gray-200 border-solid bg-white px-[20px] py-[12px] text-center font-semibold text-gray-900"
            href="https://react.email"
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

**Total Unique Identifiers:** 29

- `Button`
- `Column`
- `Layout`
- `Login`
- `Row`
- `Sign`
- `_components`
- `align`
- `border`
- `box`
- `center`
- `className`
- `colSpan`
- `component`
- `components`
- `email`
- `font`
- `full`
- `gray`
- `href`
- `https`
- `indigo`
- `layout`
- `react`
- `rounded`
- `semibold`
- `solid`
- `text`
- `white`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

