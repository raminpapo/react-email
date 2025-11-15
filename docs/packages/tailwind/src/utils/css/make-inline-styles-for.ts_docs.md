# Documentation: make-inline-styles-for.ts
**File Path:** `packages/tailwind/src/utils/css/make-inline-styles-for.ts`
**Language:** typescript
**Size:** 2,211 bytes
**Lines:** 71
**Generated:** 2025-11-15T20:37:32.456919Z

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

- **Path:** `packages/tailwind/src/utils/css/make-inline-styles-for.ts`
- **Name:** `make-inline-styles-for.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,211 bytes (2.16 KB)
- **Lines of Code:** 71

---

## Original Source

```typescript
import { type CssNode, type Declaration, generate, walk } from 'css-tree';
import { getReactProperty } from '../compatibility/get-react-property';
import type { CustomProperties } from './get-custom-properties';
import { unwrapValue } from './unwrap-value';

export function makeInlineStylesFor(
  inlinableRules: CssNode[],
  customProperties: CustomProperties,
) {
  const styles: Record<string, string> = {};

  const localVariableDeclarations = new Map<string, Declaration>();
  for (const rule of inlinableRules) {
    walk(rule, {
      visit: 'Declaration',
      enter(declaration) {
        if (declaration.property.startsWith('--')) {
          localVariableDeclarations.set(declaration.property, declaration);
        }
      },
    });
  }

  for (const rule of inlinableRules) {
    walk(rule, {
      visit: 'Function',
      enter(func, funcParentListItem) {
        if (func.name === 'var') {
          let variableName: string | undefined;
          walk(func, {
            visit: 'Identifier',
            enter(identifier) {
              variableName = identifier.name;
              return this.break;
            },
          });
          if (variableName) {
            const definition = localVariableDeclarations.get(variableName);
            if (definition) {
              funcParentListItem.data = unwrapValue(definition.value);
            } else {
              // For most variables tailwindcss defines, they also define a custom
              // property for them with an initial value that we can inline here
              const customProperty = customProperties.get(variableName);
              if (customProperty?.initialValue) {
                funcParentListItem.data = unwrapValue(
                  customProperty.initialValue.value,
                );
              }
            }
          }
        }
      },
    });

    walk(rule, {
      visit: 'Declaration',
      enter(declaration) {
        if (declaration.property.startsWith('--')) {
          return;
        }
        styles[getReactProperty(declaration.property)] =
          generate(declaration.value) +
          (declaration.important ? '!important' : '');
      },
    });
  }

  return styles;
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `customProperty()`
- `definition()`
- `localVariableDeclarations()`
- `makeInlineStylesFor()`

### Type Definitions

- `CssNode`
- `Declaration`

### Dependencies

This file imports/requires:

- `../compatibility/get-react-property`
- `./get-custom-properties`
- `./unwrap-value`
- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 54

- `CssNode`
- `CustomProperties`
- `Declaration`
- `Identifier`
- `Map`
- `Record`
- `also`
- `compatibility`
- `css`
- `custom`
- `customProperties`
- `customProperty`
- `data`
- `declaration`
- `define`
- `defines`
- `definition`
- `enter`
- `func`
- `funcParentListItem`
- `generate`
- `get`
- `getReactProperty`
- `here`
- `identifier`
- `important`
- `initial`
- `initialValue`
- `inlinableRules`
- `inline`
- `localVariableDeclarations`
- `makeInlineStylesFor`
- `most`
- `name`
- `properties`
- `property`
- `react`
- `rule`
- `set`
- `startsWith`
- `string`
- `styles`
- `tailwindcss`
- `them`
- `they`
- `tree`
- `type`
- `unwrap`
- `unwrapValue`
- `value`
- `variableName`
- `variables`
- `visit`
- `walk`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

