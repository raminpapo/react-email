# Documentation: is-rule-inlinable.ts
**File Path:** `packages/tailwind/src/utils/css/is-rule-inlinable.ts`
**Language:** typescript
**Size:** 410 bytes
**Lines:** 16
**Generated:** 2025-11-15T20:37:32.454501Z

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

- **Path:** `packages/tailwind/src/utils/css/is-rule-inlinable.ts`
- **Name:** `is-rule-inlinable.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 410 bytes (0.40 KB)
- **Lines of Code:** 16

---

## Original Source

```typescript
import { find, type Rule } from 'css-tree';

export function isRuleInlinable(rule: Rule): boolean {
  const hasAtRuleInside = find(rule, (node) => node.type === 'Atrule') !== null;

  const hasPseudoSelector =
    find(
      rule,
      (node) =>
        node.type === 'PseudoClassSelector' ||
        node.type === 'PseudoElementSelector',
    ) !== null;

  return !hasAtRuleInside && !hasPseudoSelector;
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `hasAtRuleInside()`
- `hasPseudoSelector()`
- `isRuleInlinable()`

### Type Definitions

- `Rule`

### Dependencies

This file imports/requires:

- `css-tree`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 14

- `Atrule`
- `PseudoClassSelector`
- `PseudoElementSelector`
- `Rule`
- `boolean`
- `css`
- `find`
- `hasAtRuleInside`
- `hasPseudoSelector`
- `isRuleInlinable`
- `node`
- `rule`
- `tree`
- `type`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

