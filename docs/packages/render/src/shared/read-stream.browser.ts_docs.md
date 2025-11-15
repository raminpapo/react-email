# Documentation: read-stream.browser.ts
**File Path:** `packages/render/src/shared/read-stream.browser.ts`
**Language:** typescript
**Size:** 801 bytes
**Lines:** 35
**Generated:** 2025-11-15T20:37:31.492739Z

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

- **Path:** `packages/render/src/shared/read-stream.browser.ts`
- **Name:** `read-stream.browser.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 801 bytes (0.78 KB)
- **Lines of Code:** 35

---

## Original Source

```typescript
import type { ReactDOMServerReadableStream } from 'react-dom/server.browser';

const decoder = new TextDecoder('utf-8');

export const readStream = async (stream: ReactDOMServerReadableStream) => {
  const chunks: Uint8Array[] = [];

  const writableStream = new WritableStream({
    write(chunk: Uint8Array) {
      chunks.push(chunk);
    },
    abort(reason) {
      throw new Error('Stream aborted', {
        cause: {
          reason,
        },
      });
    },
  });
  await stream.pipeTo(writableStream);

  let length = 0;
  chunks.forEach((item) => {
    length += item.length;
  });
  const mergedChunks = new Uint8Array(length);
  let offset = 0;
  chunks.forEach((item) => {
    mergedChunks.set(item, offset);
    offset += item.length;
  });

  return decoder.decode(mergedChunks);
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `decoder()`
- `length()`
- `mergedChunks()`
- `offset()`
- `readStream()`
- `writableStream()`

### Dependencies

This file imports/requires:

- `react-dom/server.browser`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 32

- `Error`
- `ReactDOMServerReadableStream`
- `Stream`
- `TextDecoder`
- `Uint8Array`
- `WritableStream`
- `abort`
- `aborted`
- `browser`
- `cause`
- `chunk`
- `chunks`
- `decode`
- `decoder`
- `dom`
- `forEach`
- `item`
- `length`
- `mergedChunks`
- `offset`
- `pipeTo`
- `push`
- `react`
- `readStream`
- `reason`
- `server`
- `set`
- `stream`
- `type`
- `utf`
- `writableStream`
- `write`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

