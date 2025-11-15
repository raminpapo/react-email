# Documentation: get-react-property.ts
**File Path:** `packages/tailwind/src/utils/compatibility/get-react-property.ts`
**Language:** typescript
**Size:** 398 bytes
**Lines:** 16
**Generated:** 2025-11-15T20:37:32.419856Z

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

- **Path:** `packages/tailwind/src/utils/compatibility/get-react-property.ts`
- **Name:** `get-react-property.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 398 bytes (0.39 KB)
- **Lines of Code:** 16

---

## Original Source

```typescript
import { fromDashCaseToCamelCase } from '../text/from-dash-case-to-camel-case';

export function getReactProperty(prop: string) {
  const modifiedProp = prop.toLowerCase();

  if (modifiedProp.startsWith('--')) {
    return modifiedProp;
  }

  if (modifiedProp.startsWith('-ms-')) {
    return fromDashCaseToCamelCase(modifiedProp.slice(1));
  }

  return fromDashCaseToCamelCase(modifiedProp);
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getReactProperty()`
- `modifiedProp()`

### Dependencies

This file imports/requires:

- `../text/from-dash-case-to-camel-case`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 11

- `camel`
- `dash`
- `fromDashCaseToCamelCase`
- `getReactProperty`
- `modifiedProp`
- `prop`
- `slice`
- `startsWith`
- `string`
- `text`
- `toLowerCase`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

