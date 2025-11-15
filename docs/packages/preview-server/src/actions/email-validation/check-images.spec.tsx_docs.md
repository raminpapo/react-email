# Documentation: check-images.spec.tsx
**File Path:** `packages/preview-server/src/actions/email-validation/check-images.spec.tsx`
**Language:** tsx
**Size:** 630 bytes
**Lines:** 22
**Generated:** 2025-11-15T20:37:31.992552Z

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

- **Path:** `packages/preview-server/src/actions/email-validation/check-images.spec.tsx`
- **Name:** `check-images.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 630 bytes (0.62 KB)
- **Lines of Code:** 22

---

## Original Source

```tsx
import { checkImages, type ImageCheckingResult } from './check-images';

test('checkImages()', async () => {
  const results: ImageCheckingResult[] = [];
  const html = `<div>
  <img src="https://cdn.resend.com/brand/resend-icon-black.png" />,
  <img src="/static/codepen-challengers.png" alt="codepen challenges" />,
</div>`;
  const stream = await checkImages(html, 'https://demo.react.email');
  const reader = stream.getReader();
  while (true) {
    const { done, value } = await reader.read();
    if (value) {
      results.push(value);
    }
    if (done) {
      break;
    }
  }
  expect(results).toMatchSnapshot();
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `html()`
- `reader()`
- `stream()`

### Type Definitions

- `ImageCheckingResult`

### Dependencies

This file imports/requires:

- `./check-images`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 36

- `ImageCheckingResult`
- `alt`
- `black`
- `brand`
- `cdn`
- `challengers`
- `challenges`
- `check`
- `checkImages`
- `codepen`
- `com`
- `demo`
- `div`
- `done`
- `email`
- `expect`
- `getReader`
- `html`
- `https`
- `icon`
- `images`
- `img`
- `png`
- `push`
- `react`
- `read`
- `reader`
- `resend`
- `results`
- `src`
- `static`
- `stream`
- `test`
- `toMatchSnapshot`
- `type`
- `value`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

