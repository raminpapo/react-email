# Documentation: extract-rules-per-class.ts
**File Path:** `packages/tailwind/src/utils/css/extract-rules-per-class.ts`
**Language:** typescript
**Size:** 1,088 bytes
**Lines:** 39
**Generated:** 2025-11-15T20:37:32.451854Z

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

- **Path:** `packages/tailwind/src/utils/css/extract-rules-per-class.ts`
- **Name:** `extract-rules-per-class.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,088 bytes (1.06 KB)
- **Lines of Code:** 39

---

## Original Source

```typescript
import { type CssNode, type Rule, string, walk } from 'css-tree';
import { isRuleInlinable } from './is-rule-inlinable';

export function extractRulesPerClass(root: CssNode, classes: string[]) {
  const classSet = new Set(classes);

  const inlinableRules = new Map<string, Rule>();
  const nonInlinableRules = new Map<string, Rule>();
  walk(root, {
    visit: 'Rule',
    enter(rule) {
      const selectorClasses: string[] = [];
      walk(rule, {
        visit: 'ClassSelector',
        enter(classSelector) {
          selectorClasses.push(string.decode(classSelector.name));
        },
      });
      if (isRuleInlinable(rule)) {
        for (const className of selectorClasses) {
          if (classSet.has(className)) {
            inlinableRules.set(className, rule);
          }
        }
      } else {
        for (const className of selectorClasses) {
          if (classSet.has(className)) {
            nonInlinableRules.set(className, rule);
          }
        }
      }
    },
  });
  return {
    inlinable: inlinableRules,
    nonInlinable: nonInlinableRules,
  };
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `classSet()`
- `extractRulesPerClass()`
- `inlinableRules()`
- `nonInlinableRules()`

### Type Definitions

- `CssNode`
- `Rule`

### Dependencies

This file imports/requires:

- `./is-rule-inlinable`
- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 29

- `ClassSelector`
- `CssNode`
- `Map`
- `Rule`
- `Set`
- `className`
- `classSelector`
- `classSet`
- `classes`
- `css`
- `decode`
- `enter`
- `extractRulesPerClass`
- `inlinable`
- `inlinableRules`
- `isRuleInlinable`
- `name`
- `nonInlinable`
- `nonInlinableRules`
- `push`
- `root`
- `rule`
- `selectorClasses`
- `set`
- `string`
- `tree`
- `type`
- `visit`
- `walk`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

