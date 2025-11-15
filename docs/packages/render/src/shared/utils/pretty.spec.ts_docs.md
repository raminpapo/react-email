# Documentation: pretty.spec.ts
**File Path:** `packages/render/src/shared/utils/pretty.spec.ts`
**Language:** typescript
**Size:** 658 bytes
**Lines:** 23
**Generated:** 2025-11-15T20:37:31.493852Z

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

- **Path:** `packages/render/src/shared/utils/pretty.spec.ts`
- **Name:** `pretty.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 658 bytes (0.64 KB)
- **Lines of Code:** 23

---

## Original Source

```typescript
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { pretty } from './pretty';

describe('pretty', () => {
  it("prettifies Preview component's complex characters correctly", async () => {
    const stripeHTML = await fs.readFile(
      path.resolve(__dirname, './testing/stripe-email.html'),
      'utf8',
    );

    expect(await pretty(stripeHTML)).toMatchSnapshot();
  });

  test('if mso syntax does not wrap', async () => {
    expect(
      await pretty(
        `<span><!--[if mso]><i style="mso-font-width:100%;mso-text-raise:12" hidden>&#8202;&#8202;</i><![endif]--></span>`,
      ),
    ).toMatchSnapshot();
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `stripeHTML()`

### Dependencies

This file imports/requires:

- `./pretty`
- `node:fs`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 34

- `Preview`
- `__dirname`
- `characters`
- `complex`
- `component`
- `correctly`
- `describe`
- `email`
- `endif`
- `expect`
- `font`
- `hidden`
- `html`
- `mso`
- `node`
- `path`
- `prettifies`
- `pretty`
- `promises`
- `raise`
- `readFile`
- `resolve`
- `span`
- `stripe`
- `stripeHTML`
- `style`
- `syntax`
- `test`
- `testing`
- `text`
- `toMatchSnapshot`
- `utf8`
- `width`
- `wrap`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

