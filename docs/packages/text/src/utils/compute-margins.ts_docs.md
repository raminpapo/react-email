# Documentation: compute-margins.ts
**File Path:** `packages/text/src/utils/compute-margins.ts`
**Language:** typescript
**Size:** 2,414 bytes
**Lines:** 103
**Generated:** 2025-11-15T20:37:31.453291Z

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

- **Path:** `packages/text/src/utils/compute-margins.ts`
- **Name:** `compute-margins.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,414 bytes (2.36 KB)
- **Lines of Code:** 103

---

## Original Source

```typescript
type MarginType = string | number | undefined;

interface MarginProperties {
  margin?: MarginType;
  marginTop?: MarginType;
  marginRight?: MarginType;
  marginBottom?: MarginType;
  marginLeft?: MarginType;
}

interface MarginResult {
  marginTop: MarginType;
  marginRight: MarginType;
  marginBottom: MarginType;
  marginLeft: MarginType;
}

function parseMarginValue(value: MarginType): MarginResult {
  if (typeof value === 'number')
    return {
      marginTop: value,
      marginBottom: value,
      marginLeft: value,
      marginRight: value,
    };

  if (typeof value === 'string') {
    const values = value.toString().trim().split(/\s+/);

    if (values.length === 1) {
      return {
        marginTop: values[0],
        marginBottom: values[0],
        marginLeft: values[0],
        marginRight: values[0],
      };
    }

    if (values.length === 2) {
      return {
        marginTop: values[0],
        marginRight: values[1],
        marginBottom: values[0],
        marginLeft: values[1],
      };
    }

    if (values.length === 3) {
      return {
        marginTop: values[0],
        marginRight: values[1],
        marginBottom: values[2],
        marginLeft: values[1],
      };
    }

    if (values.length === 4) {
      return {
        marginTop: values[0],
        marginRight: values[1],
        marginBottom: values[2],
        marginLeft: values[3],
      };
    }
  }

  return {
    marginTop: undefined,
    marginBottom: undefined,
    marginLeft: undefined,
    marginRight: undefined,
  };
}

/**
 * Parses all the values out of a margin string to get the value for all margin props in the four margin properties
 * @example e.g. "10px" =\> mt: "10px", mr: "10px", mb: "10px", ml: "10px"
 */
export function computeMargins(properties: MarginProperties): MarginResult {
  let result: MarginResult = {
    marginTop: undefined,
    marginRight: undefined,
    marginBottom: undefined,
    marginLeft: undefined,
  };

  for (const [key, value] of Object.entries(properties)) {
    if (key === 'margin') {
      result = parseMarginValue(value);
    } else if (key === 'marginTop') {
      result.marginTop = value;
    } else if (key === 'marginRight') {
      result.marginRight = value;
    } else if (key === 'marginBottom') {
      result.marginBottom = value;
    } else if (key === 'marginLeft') {
      result.marginLeft = value;
    }
  }

  return result;
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `computeMargins()`
- `parseMarginValue()`
- `values()`

### Interfaces

- `MarginProperties`
- `MarginResult`

### Type Definitions

- `MarginType`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 32

- `MarginProperties`
- `MarginResult`
- `MarginType`
- `Object`
- `Parses`
- `all`
- `computeMargins`
- `entries`
- `example`
- `four`
- `get`
- `interface`
- `key`
- `length`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `number`
- `out`
- `parseMarginValue`
- `properties`
- `props`
- `result`
- `split`
- `string`
- `toString`
- `trim`
- `type`
- `value`
- `values`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

