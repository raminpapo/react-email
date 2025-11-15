# Documentation: compute-margins.spec.ts
**File Path:** `packages/text/src/utils/compute-margins.spec.ts`
**Language:** typescript
**Size:** 1,454 bytes
**Lines:** 68
**Generated:** 2025-11-15T20:37:31.452166Z

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

- **Path:** `packages/text/src/utils/compute-margins.spec.ts`
- **Name:** `compute-margins.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,454 bytes (1.42 KB)
- **Lines of Code:** 68

---

## Original Source

```typescript
import { computeMargins } from './compute-margins';

describe('parseMargins()', () => {
  it('works with numeric and text margins', () => {
    expect(computeMargins({ margin: 24 })).toEqual({
      marginTop: 24,
      marginRight: 24,
      marginBottom: 24,
      marginLeft: 24,
    });

    expect(computeMargins({ margin: '24px' })).toEqual({
      marginTop: '24px',
      marginRight: '24px',
      marginBottom: '24px',
      marginLeft: '24px',
    });

    expect(computeMargins({ margin: '24px', marginTop: 10 })).toEqual({
      marginTop: 10,
      marginRight: '24px',
      marginBottom: '24px',
      marginLeft: '24px',
    });
  });

  it('computes the margins according to the order of styles', () => {
    expect(
      computeMargins({
        margin: 0,
        marginBottom: '1rem',
      }),
    ).toEqual({
      marginTop: 0,
      marginRight: 0,
      marginLeft: 0,
      marginBottom: '1rem',
    });

    expect(
      computeMargins({
        marginBottom: '1rem',
        margin: 0,
      }),
    ).toEqual({
      marginTop: 0,
      marginRight: 0,
      marginLeft: 0,
      marginBottom: 0,
    });

    expect(
      computeMargins({
        marginTop: '2rem',
        marginLeft: '10px',
        margin: '3em',
        marginRight: '9px',
        marginBottom: '1px',
      }),
    ).toEqual({
      marginTop: '3em',
      marginLeft: '3em',
      marginRight: '9px',
      marginBottom: '1px',
    });
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `./compute-margins`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 19

- `according`
- `compute`
- `computeMargins`
- `computes`
- `describe`
- `expect`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `margins`
- `numeric`
- `order`
- `parseMargins`
- `styles`
- `text`
- `toEqual`
- `works`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

