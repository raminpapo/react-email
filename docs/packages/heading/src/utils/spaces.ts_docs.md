# Documentation: spaces.ts
**File Path:** `packages/heading/src/utils/spaces.ts`
**Language:** typescript
**Size:** 1,489 bytes
**Lines:** 65
**Generated:** 2025-11-15T20:37:32.287918Z

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

- **Path:** `packages/heading/src/utils/spaces.ts`
- **Name:** `spaces.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,489 bytes (1.45 KB)
- **Lines of Code:** 65

---

## Original Source

```typescript
import type React from 'react';

type MarginCSSProperty =
  | 'margin'
  | 'marginLeft'
  | 'marginRight'
  | 'marginTop'
  | 'marginBottom';

type MarginStyles = Partial<Pick<React.CSSProperties, MarginCSSProperty>>;

export interface Margin {
  m?: number | string;
  mx?: number | string;
  my?: number | string;
  mt?: number | string;
  mr?: number | string;
  mb?: number | string;
  ml?: number | string;
}

export const withMargin = (props: Margin): MarginStyles => {
  const candidates = [
    withSpace(props.m, ['margin']),
    withSpace(props.mx, ['marginLeft', 'marginRight']),
    withSpace(props.my, ['marginTop', 'marginBottom']),
    withSpace(props.mt, ['marginTop']),
    withSpace(props.mr, ['marginRight']),
    withSpace(props.mb, ['marginBottom']),
    withSpace(props.ml, ['marginLeft']),
  ];

  const mergedStyles: MarginStyles = {};

  for (const style of candidates) {
    if (Object.keys(style).length > 0) {
      Object.assign(mergedStyles, style);
    }
  }

  return mergedStyles;
};

export const withSpace = (
  value: number | string | undefined,
  properties: MarginCSSProperty[],
) => {
  const styles: MarginStyles = {};

  if (value === undefined) {
    return styles;
  }

  // Check to ensure string value is a valid number
  if (Number.isNaN(Number.parseFloat(String(value)))) {
    return styles;
  }

  for (const property of properties) {
    styles[property] = `${value}px` as React.CSSProperties[MarginCSSProperty];
  }

  return styles;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `candidates()`
- `withMargin()`
- `withSpace()`

### Interfaces

- `Margin`

### Type Definitions

- `MarginCSSProperty`
- `MarginStyles`
- `React`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 38

- `CSSProperties`
- `Check`
- `Margin`
- `MarginCSSProperty`
- `MarginStyles`
- `Number`
- `Object`
- `Partial`
- `Pick`
- `React`
- `String`
- `assign`
- `candidates`
- `ensure`
- `interface`
- `isNaN`
- `keys`
- `length`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `mergedStyles`
- `number`
- `parseFloat`
- `properties`
- `property`
- `props`
- `react`
- `string`
- `style`
- `styles`
- `type`
- `valid`
- `value`
- `withMargin`
- `withSpace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

