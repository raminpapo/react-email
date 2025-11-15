# Documentation: resolve-calc-expressions.ts
**File Path:** `packages/tailwind/src/utils/css/resolve-calc-expressions.ts`
**Language:** typescript
**Size:** 4,944 bytes
**Lines:** 148
**Generated:** 2025-11-15T20:37:32.464315Z

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

- **Path:** `packages/tailwind/src/utils/css/resolve-calc-expressions.ts`
- **Name:** `resolve-calc-expressions.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 4,944 bytes (4.83 KB)
- **Lines of Code:** 148

---

## Original Source

```typescript
import { type CssNode, walk } from 'css-tree';

/**
 * Intentionally only resolves `*` and `/` operations without dealing with parenthesis, because this is the only thing required to run Tailwind v4
 */
export function resolveCalcExpressions(node: CssNode) {
  walk(node, {
    visit: 'Function',
    enter(func, funcListItem) {
      if (func.name === 'calc') {
        /*
          [
            { type: 'Dimension', loc: null, value: '0.25', unit: 'rem' },
            { type: 'Operator', loc: null, value: '*' },
            { type: 'Number', loc: null, value: '2' }
            { type: 'Percentage', loc: null, value: '2' }
          ]
        */
        func.children.forEach((child, item) => {
          const left = item.prev;
          const right = item.next;
          if (
            left &&
            right &&
            child.type === 'Operator' &&
            (left.data.type === 'Dimension' ||
              left.data.type === 'Number' ||
              left.data.type === 'Percentage') &&
            (right.data.type === 'Dimension' ||
              right.data.type === 'Number' ||
              right.data.type === 'Percentage')
          ) {
            if (child.value === '*' || child.value === '/') {
              const value = (() => {
                if (child.value === '*') {
                  return String(
                    Number.parseFloat(left.data.value) *
                      Number.parseFloat(right.data.value),
                  );
                }
                if (right.data.value === '0') {
                  return '0';
                }
                return String(
                  Number.parseFloat(left.data.value) /
                    Number.parseFloat(right.data.value),
                );
              })();
              if (
                left.data.type === 'Dimension' &&
                right.data.type === 'Number'
              ) {
                item.data = {
                  type: 'Dimension',
                  unit: left.data.unit,
                  value,
                };
                func.children.remove(left);
                func.children.remove(right);
              } else if (
                left.data.type === 'Number' &&
                right.data.type === 'Dimension'
              ) {
                item.data = {
                  type: 'Dimension',
                  unit: right.data.unit,
                  value,
                };
                func.children.remove(left);
                func.children.remove(right);
              } else if (
                left.data.type === 'Number' &&
                right.data.type === 'Number'
              ) {
                item.data = {
                  type: 'Number',
                  value,
                };
                func.children.remove(left);
                func.children.remove(right);
              } else if (
                left.data.type === 'Dimension' &&
                right.data.type === 'Dimension' &&
                left.data.unit === right.data.unit
              ) {
                if (child.value === '/') {
                  item.data = {
                    type: 'Number',
                    value,
                  };
                } else {
                  item.data = {
                    type: 'Dimension',
                    unit: left.data.unit,
                    value,
                  };
                }
                func.children.remove(left);
                func.children.remove(right);
              } else if (
                left.data.type === 'Percentage' &&
                right.data.type === 'Number'
              ) {
                item.data = {
                  type: 'Percentage',
                  value,
                };
                func.children.remove(left);
                func.children.remove(right);
              } else if (
                left.data.type === 'Number' &&
                right.data.type === 'Percentage'
              ) {
                item.data = {
                  type: 'Percentage',
                  value,
                };
                func.children.remove(left);
                func.children.remove(right);
              } else if (
                left.data.type === 'Percentage' &&
                right.data.type === 'Percentage'
              ) {
                if (child.value === '/') {
                  item.data = {
                    type: 'Number',
                    value,
                  };
                } else {
                  item.data = {
                    type: 'Percentage',
                    value,
                  };
                }
                func.children.remove(left);
                func.children.remove(right);
              }
            }
          }
        });
        if (func.children.size === 1 && func.children.first) {
          funcListItem.data = func.children.first;
        }
      }
    },
  });
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `left()`
- `resolveCalcExpressions()`
- `right()`
- `value()`

### Type Definitions

- `CssNode`

### Dependencies

This file imports/requires:

- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 47

- `CssNode`
- `Dimension`
- `Intentionally`
- `Number`
- `Operator`
- `Percentage`
- `String`
- `Tailwind`
- `because`
- `calc`
- `child`
- `children`
- `css`
- `data`
- `dealing`
- `enter`
- `first`
- `forEach`
- `func`
- `funcListItem`
- `item`
- `left`
- `loc`
- `name`
- `next`
- `node`
- `only`
- `operations`
- `parenthesis`
- `parseFloat`
- `prev`
- `rem`
- `remove`
- `required`
- `resolveCalcExpressions`
- `resolves`
- `right`
- `run`
- `size`
- `thing`
- `tree`
- `type`
- `unit`
- `value`
- `visit`
- `walk`
- `without`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

