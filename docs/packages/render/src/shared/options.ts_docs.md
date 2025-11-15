# Documentation: options.ts
**File Path:** `packages/render/src/shared/options.ts`
**Language:** typescript
**Size:** 712 bytes
**Lines:** 31
**Generated:** 2025-11-15T20:37:31.491678Z

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

- **Path:** `packages/render/src/shared/options.ts`
- **Name:** `options.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 712 bytes (0.70 KB)
- **Lines of Code:** 31

---

## Original Source

```typescript
import type { HtmlToTextOptions } from 'html-to-text';
import type { pretty } from './utils/pretty';
import type { toPlainText } from './utils/to-plain-text';

export type Options = {
  /**
   * @see {@link pretty}
   */
  pretty?: boolean;
} & (
  | {
      /**
       * @see {@link toPlainText}
       */
      plainText?: false;
    }
  | {
      /**
       * @see {@link toPlainText}
       */
      plainText?: true;
      /**
       * These are options you can pass down directly to the library we use for
       * converting the rendered email's HTML into plain text.
       *
       * @see https://github.com/html-to-text/node-html-to-text
       */
      htmlToTextOptions?: HtmlToTextOptions;
    }
);

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Type Definitions

- `Options`

### Dependencies

This file imports/requires:

- `./utils/pretty`
- `./utils/to-plain-text`
- `html-to-text`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 30

- `HtmlToTextOptions`
- `Options`
- `These`
- `boolean`
- `com`
- `converting`
- `directly`
- `down`
- `email`
- `github`
- `html`
- `htmlToTextOptions`
- `https`
- `into`
- `library`
- `link`
- `node`
- `options`
- `pass`
- `plain`
- `plainText`
- `pretty`
- `rendered`
- `see`
- `text`
- `toPlainText`
- `type`
- `use`
- `utils`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

