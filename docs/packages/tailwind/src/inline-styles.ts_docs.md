# Documentation: inline-styles.ts
**File Path:** `packages/tailwind/src/inline-styles.ts`
**Language:** typescript
**Size:** 631 bytes
**Lines:** 22
**Generated:** 2025-11-15T20:37:32.393158Z

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

- **Path:** `packages/tailwind/src/inline-styles.ts`
- **Name:** `inline-styles.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 631 bytes (0.62 KB)
- **Lines of Code:** 22

---

## Original Source

```typescript
import type { StyleSheet } from 'css-tree';
import { extractRulesPerClass } from './utils/css/extract-rules-per-class';
import { getCustomProperties } from './utils/css/get-custom-properties';
import { makeInlineStylesFor } from './utils/css/make-inline-styles-for';

export function inlineStyles(
  styleSheet: StyleSheet,
  classes: string[],
): Record<string, string> {
  const { inlinable: inlinableRules } = extractRulesPerClass(
    styleSheet,
    classes,
  );

  const customProperties = getCustomProperties(styleSheet);

  return makeInlineStylesFor(
    Array.from(inlinableRules.values()),
    customProperties,
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `customProperties()`
- `inlineStyles()`

### Dependencies

This file imports/requires:

- `./utils/css/extract-rules-per-class`
- `./utils/css/get-custom-properties`
- `./utils/css/make-inline-styles-for`
- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 27

- `Array`
- `Record`
- `StyleSheet`
- `classes`
- `css`
- `custom`
- `customProperties`
- `extract`
- `extractRulesPerClass`
- `get`
- `getCustomProperties`
- `inlinable`
- `inlinableRules`
- `inline`
- `inlineStyles`
- `make`
- `makeInlineStylesFor`
- `per`
- `properties`
- `rules`
- `string`
- `styleSheet`
- `styles`
- `tree`
- `type`
- `utils`
- `values`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

