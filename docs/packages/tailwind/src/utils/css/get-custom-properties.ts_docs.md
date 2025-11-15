# Documentation: get-custom-properties.ts
**File Path:** `packages/tailwind/src/utils/css/get-custom-properties.ts`
**Language:** typescript
**Size:** 1,374 bytes
**Lines:** 50
**Generated:** 2025-11-15T20:37:32.453288Z

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

- **Path:** `packages/tailwind/src/utils/css/get-custom-properties.ts`
- **Name:** `get-custom-properties.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,374 bytes (1.34 KB)
- **Lines of Code:** 50

---

## Original Source

```typescript
import { type CssNode, type Declaration, generate, walk } from 'css-tree';

export interface CustomProperty {
  syntax?: Declaration;
  inherits?: Declaration;
  initialValue?: Declaration;
}

export type CustomProperties = Map<string, CustomProperty>;

export function getCustomProperties(node: CssNode) {
  const customProperties = new Map<string, CustomProperty>();

  walk(node, {
    visit: 'Atrule',
    enter(atrule) {
      if (atrule.name === 'property' && atrule.prelude) {
        const prelude = generate(atrule.prelude);
        if (prelude.startsWith('--')) {
          let syntax: Declaration | undefined;
          let inherits: Declaration | undefined;
          let initialValue: Declaration | undefined;
          walk(atrule, {
            visit: 'Declaration',
            enter(declaration) {
              if (declaration.property === 'syntax') {
                syntax = declaration;
              }
              if (declaration.property === 'inherits') {
                inherits = declaration;
              }
              if (declaration.property === 'initial-value') {
                initialValue = declaration;
              }
            },
          });

          customProperties.set(prelude, {
            syntax,
            inherits,
            initialValue,
          });
        }
      }
    },
  });

  return customProperties;
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
- `getCustomProperties()`
- `prelude()`

### Interfaces

- `CustomProperty`

### Type Definitions

- `CssNode`
- `CustomProperties`
- `Declaration`

### Dependencies

This file imports/requires:

- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 30

- `Atrule`
- `CssNode`
- `CustomProperties`
- `CustomProperty`
- `Declaration`
- `Map`
- `atrule`
- `css`
- `customProperties`
- `declaration`
- `enter`
- `generate`
- `getCustomProperties`
- `inherits`
- `initial`
- `initialValue`
- `interface`
- `name`
- `node`
- `prelude`
- `property`
- `set`
- `startsWith`
- `string`
- `syntax`
- `tree`
- `type`
- `value`
- `visit`
- `walk`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

