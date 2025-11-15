# Documentation: sanitize-non-inlinable-rules.ts
**File Path:** `packages/tailwind/src/utils/css/sanitize-non-inlinable-rules.ts`
**Language:** typescript
**Size:** 1,088 bytes
**Lines:** 36
**Generated:** 2025-11-15T20:37:32.474775Z

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

- **Path:** `packages/tailwind/src/utils/css/sanitize-non-inlinable-rules.ts`
- **Name:** `sanitize-non-inlinable-rules.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,088 bytes (1.06 KB)
- **Lines of Code:** 36

---

## Original Source

```typescript
import { type CssNode, string, walk } from 'css-tree';
import { sanitizeClassName } from '../compatibility/sanitize-class-name';
import { isRuleInlinable } from './is-rule-inlinable';

/**
 * This function goes through a few steps to ensure the best email client support and
 * to ensure that media queries and pseudo classes are applied correctly alongside
 * the inline styles.
 *
 * What it does:
 * 1. Converts all declarations in all rules into important ones
 * 2. Sanitizes class selectors of all non-inlinable rules
 */
export function sanitizeNonInlinableRules(node: CssNode) {
  walk(node, {
    visit: 'Rule',
    enter(rule) {
      if (!isRuleInlinable(rule)) {
        walk(rule.prelude, (node) => {
          if (node.type === 'ClassSelector') {
            const unescapedClassName = string.decode(node.name);
            node.name = sanitizeClassName(unescapedClassName);
          }
        });

        walk(rule, {
          visit: 'Declaration',
          enter(declaration) {
            declaration.important = true;
          },
        });
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

- `sanitizeNonInlinableRules()`
- `unescapedClassName()`

### Type Definitions

- `CssNode`

### Dependencies

This file imports/requires:

- `../compatibility/sanitize-class-name`
- `./is-rule-inlinable`
- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 53

- `ClassSelector`
- `Converts`
- `CssNode`
- `Declaration`
- `Rule`
- `Sanitizes`
- `What`
- `all`
- `alongside`
- `applied`
- `best`
- `classes`
- `client`
- `compatibility`
- `correctly`
- `css`
- `declaration`
- `declarations`
- `decode`
- `email`
- `ensure`
- `enter`
- `few`
- `goes`
- `important`
- `inlinable`
- `inline`
- `into`
- `isRuleInlinable`
- `media`
- `name`
- `node`
- `non`
- `ones`
- `prelude`
- `pseudo`
- `queries`
- `rule`
- `rules`
- `sanitize`
- `sanitizeClassName`
- `sanitizeNonInlinableRules`
- `selectors`
- `steps`
- `string`
- `styles`
- `support`
- `through`
- `tree`
- `type`
- `unescapedClassName`
- `visit`
- `walk`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

