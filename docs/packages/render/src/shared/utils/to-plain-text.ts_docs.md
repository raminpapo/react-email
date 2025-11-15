# Documentation: to-plain-text.ts
**File Path:** `packages/render/src/shared/utils/to-plain-text.ts`
**Language:** typescript
**Size:** 534 bytes
**Lines:** 23
**Generated:** 2025-11-15T20:37:31.496497Z

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

- **Path:** `packages/render/src/shared/utils/to-plain-text.ts`
- **Name:** `to-plain-text.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 534 bytes (0.52 KB)
- **Lines of Code:** 23

---

## Original Source

```typescript
import {
  convert,
  type HtmlToTextOptions,
  type SelectorDefinition,
} from 'html-to-text';

export const plainTextSelectors: SelectorDefinition[] = [
  { selector: 'img', format: 'skip' },
  { selector: '[data-skip-in-text=true]', format: 'skip' },
  {
    selector: 'a',
    options: { linkBrackets: false, hideLinkHrefIfSameAsText: true },
  },
];

export function toPlainText(html: string, options?: HtmlToTextOptions) {
  return convert(html, {
    selectors: plainTextSelectors,
    wordwrap: false,
    ...options,
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

- `toPlainText()`

### Type Definitions

- `HtmlToTextOptions`
- `SelectorDefinition`

### Dependencies

This file imports/requires:

- `html-to-text`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 19

- `HtmlToTextOptions`
- `SelectorDefinition`
- `convert`
- `data`
- `format`
- `hideLinkHrefIfSameAsText`
- `html`
- `img`
- `linkBrackets`
- `options`
- `plainTextSelectors`
- `selector`
- `selectors`
- `skip`
- `string`
- `text`
- `toPlainText`
- `type`
- `wordwrap`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

