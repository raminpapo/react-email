# Documentation: get-line-and-column-from-offset.spec.ts
**File Path:** `packages/preview-server/src/utils/get-line-and-column-from-offset.spec.ts`
**Language:** typescript
**Size:** 483 bytes
**Lines:** 12
**Generated:** 2025-11-15T20:37:32.022571Z

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

- **Path:** `packages/preview-server/src/utils/get-line-and-column-from-offset.spec.ts`
- **Name:** `get-line-and-column-from-offset.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 483 bytes (0.47 KB)
- **Lines of Code:** 12

---

## Original Source

```typescript
import { getLineAndColumnFromOffset } from './get-line-and-column-from-offset';

test('getLineAndColumnFromOffset()', () => {
  const content = `export default function MyEmail() {
  return <div className="testing classes to make sure this is not removed" id="my-div" aria-label="my beautiful div">
    inside the div, should also stay unchanged
  </div>;
}`;
  const offset = content.indexOf('className');
  expect(getLineAndColumnFromOffset(offset, content)).toEqual([2, 15]);
});

```

---

## Overview

This is a JavaScript/TypeScript file. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `MyEmail()`
- `content()`
- `offset()`

### Dependencies

This file imports/requires:

- `./get-line-and-column-from-offset`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 25

- `MyEmail`
- `also`
- `aria`
- `beautiful`
- `className`
- `classes`
- `column`
- `content`
- `div`
- `expect`
- `get`
- `getLineAndColumnFromOffset`
- `indexOf`
- `inside`
- `label`
- `line`
- `make`
- `offset`
- `removed`
- `stay`
- `sure`
- `test`
- `testing`
- `toEqual`
- `unchanged`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

