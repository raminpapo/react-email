# Documentation: utils.spec.ts
**File Path:** `packages/heading/src/utils/utils.spec.ts`
**Language:** typescript
**Size:** 2,099 bytes
**Lines:** 71
**Generated:** 2025-11-15T20:37:32.289169Z

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

- **Path:** `packages/heading/src/utils/utils.spec.ts`
- **Name:** `utils.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,099 bytes (2.05 KB)
- **Lines of Code:** 71

---

## Original Source

```typescript
import type { Margin } from './spaces';
import { withMargin, withSpace } from './spaces';

describe('withMargin', () => {
  it('returns an empty object for empty input', () => {
    const marginProps: Margin = {};
    const result = withMargin(marginProps);
    expect(result).toEqual({});
  });

  it('applies margin to the top', () => {
    const marginProps: Margin = { mt: '10' };
    const result = withMargin(marginProps);
    expect(result).toEqual({ marginTop: '10px' });
  });

  it('applies margin to the left and right', () => {
    const marginProps: Margin = { mx: '20' };
    const result = withMargin(marginProps);
    expect(result).toEqual({ marginLeft: '20px', marginRight: '20px' });
  });

  it('applies margin to the top and bottom', () => {
    const marginProps: Margin = { my: '15' };
    const result = withMargin(marginProps);
    expect(result).toEqual({
      marginBottom: '15px',
      marginTop: '15px',
    });
  });

  it('applies margin to all sides', () => {
    const marginProps: Margin = { m: '25' };
    const result = withMargin(marginProps);
    expect(result).toEqual({
      margin: '25px',
    });
  });

  it('applies margin to specified sides when provided', () => {
    const marginProps: Margin = { mt: '5', mr: '10', mb: '15', ml: '20' };
    const result = withMargin(marginProps);
    expect(result).toEqual({
      marginBottom: '15px',
      marginLeft: '20px',
      marginRight: '10px',
      marginTop: '5px',
    });
  });

  it('ignores invalid margin values', () => {
    const marginProps: Margin = { m: 'invalid', mt: '5', mx: 'valid' };
    const result = withMargin(marginProps);
    expect(result).toEqual({
      marginTop: '5px',
    });
  });
});

describe('withSpace', () => {
  it('returns an empty object for undefined value', () => {
    const result = withSpace(undefined, ['margin']);
    expect(result).toEqual({});
  });

  it('applies space to the specified properties', () => {
    const result = withSpace(15, ['marginTop', 'marginLeft']);
    expect(result).toEqual({ marginTop: '15px', marginLeft: '15px' });
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `result()`

### Dependencies

This file imports/requires:

- `./spaces`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 36

- `Margin`
- `all`
- `applies`
- `bottom`
- `describe`
- `empty`
- `expect`
- `ignores`
- `input`
- `invalid`
- `left`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginProps`
- `marginRight`
- `marginTop`
- `object`
- `properties`
- `provided`
- `result`
- `returns`
- `right`
- `sides`
- `space`
- `spaces`
- `specified`
- `toEqual`
- `top`
- `type`
- `valid`
- `value`
- `values`
- `when`
- `withMargin`
- `withSpace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

