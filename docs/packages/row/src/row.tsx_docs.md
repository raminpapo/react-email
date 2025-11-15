# Documentation: row.tsx
**File Path:** `packages/row/src/row.tsx`
**Language:** tsx
**Size:** 663 bytes
**Lines:** 32
**Generated:** 2025-11-15T20:37:32.207175Z

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

- **Path:** `packages/row/src/row.tsx`
- **Name:** `row.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 663 bytes (0.65 KB)
- **Lines of Code:** 32

---

## Original Source

```tsx
import * as React from 'react';

export type RowProps = Readonly<
  React.ComponentPropsWithoutRef<'table'> & {
    children: React.ReactNode;
  }
>;

export const Row = React.forwardRef<HTMLTableElement, RowProps>(
  ({ children, style, ...props }, ref) => {
    return (
      <table
        align="center"
        width="100%"
        border={0}
        cellPadding="0"
        cellSpacing="0"
        role="presentation"
        {...props}
        ref={ref}
        style={style}
      >
        <tbody style={{ width: '100%' }}>
          <tr style={{ width: '100%' }}>{children}</tr>
        </tbody>
      </table>
    );
  },
);

Row.displayName = 'Row';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Row()`

### Type Definitions

- `RowProps`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 25

- `ComponentPropsWithoutRef`
- `HTMLTableElement`
- `React`
- `ReactNode`
- `Readonly`
- `Row`
- `RowProps`
- `align`
- `border`
- `cellPadding`
- `cellSpacing`
- `center`
- `children`
- `displayName`
- `forwardRef`
- `presentation`
- `props`
- `react`
- `ref`
- `role`
- `style`
- `table`
- `tbody`
- `type`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

