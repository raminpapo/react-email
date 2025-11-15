# Documentation: get-code-location-from-ast-element.ts
**File Path:** `packages/preview-server/src/actions/email-validation/get-code-location-from-ast-element.ts`
**Language:** typescript
**Size:** 431 bytes
**Lines:** 19
**Generated:** 2025-11-15T20:37:31.998746Z

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

- **Path:** `packages/preview-server/src/actions/email-validation/get-code-location-from-ast-element.ts`
- **Name:** `get-code-location-from-ast-element.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 431 bytes (0.42 KB)
- **Lines of Code:** 19

---

## Original Source

```typescript
import type { HTMLElement } from 'node-html-parser';
import { getLineAndColumnFromOffset } from '../../utils/get-line-and-column-from-offset';

export interface CodeLocation {
  line: number;
  column: number;
}

export const getCodeLocationFromAstElement = (
  ast: HTMLElement,
  html: string,
): CodeLocation => {
  const [line, column] = getLineAndColumnFromOffset(ast.range[0], html);
  return {
    line,
    column,
  };
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getCodeLocationFromAstElement()`

### Interfaces

- `CodeLocation`

### Dependencies

This file imports/requires:

- `../../utils/get-line-and-column-from-offset`
- `node-html-parser`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 18

- `CodeLocation`
- `HTMLElement`
- `ast`
- `column`
- `get`
- `getCodeLocationFromAstElement`
- `getLineAndColumnFromOffset`
- `html`
- `interface`
- `line`
- `node`
- `number`
- `offset`
- `parser`
- `range`
- `string`
- `type`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

