# Documentation: read-stream.ts
**File Path:** `packages/render/src/node/read-stream.ts`
**Language:** typescript
**Size:** 1,521 bytes
**Lines:** 54
**Generated:** 2025-11-15T20:37:31.508744Z

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

- **Path:** `packages/render/src/node/read-stream.ts`
- **Name:** `read-stream.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,521 bytes (1.49 KB)
- **Lines of Code:** 54

---

## Original Source

```typescript
import { Writable } from 'node:stream';
import type {
  PipeableStream,
  ReactDOMServerReadableStream,
} from 'react-dom/server.browser';

export const readStream = async (
  stream: PipeableStream | ReactDOMServerReadableStream,
) => {
  let result = '';
  // Create a single TextDecoder instance to handle streaming properly
  // This fixes issues with multi-byte characters (e.g., CJK) being split across chunks
  const decoder = new TextDecoder('utf-8');

  if ('pipeTo' in stream) {
    // means it's a readable stream
    const writableStream = new WritableStream({
      write(chunk: BufferSource) {
        // Use stream: true to handle multi-byte characters split across chunks
        result += decoder.decode(chunk, { stream: true });
      },
      close() {
        // Flush any remaining bytes
        result += decoder.decode();
      },
    });
    await stream.pipeTo(writableStream);
  } else {
    const writable = new Writable({
      write(chunk: BufferSource, _encoding, callback) {
        // Use stream: true to handle multi-byte characters split across chunks
        result += decoder.decode(chunk, { stream: true });

        callback();
      },
      final(callback) {
        // Flush any remaining bytes
        result += decoder.decode();
        callback();
      },
    });
    stream.pipe(writable);

    await new Promise<void>((resolve, reject) => {
      writable.on('error', reject);
      writable.on('close', () => {
        resolve();
      });
    });
  }

  return result;
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
- `readStream()`
- `result()`
- `writable()`
- `writableStream()`

### Dependencies

This file imports/requires:

- `node:stream`
- `react-dom/server.browser`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 54

- `BufferSource`
- `Create`
- `Flush`
- `PipeableStream`
- `Promise`
- `ReactDOMServerReadableStream`
- `TextDecoder`
- `Use`
- `Writable`
- `WritableStream`
- `_encoding`
- `across`
- `any`
- `browser`
- `byte`
- `bytes`
- `callback`
- `characters`
- `chunk`
- `chunks`
- `close`
- `decode`
- `decoder`
- `dom`
- `error`
- `final`
- `fixes`
- `handle`
- `instance`
- `issues`
- `means`
- `multi`
- `node`
- `pipe`
- `pipeTo`
- `properly`
- `react`
- `readStream`
- `readable`
- `reject`
- `remaining`
- `resolve`
- `result`
- `server`
- `single`
- `split`
- `stream`
- `streaming`
- `type`
- `utf`
- `void`
- `writable`
- `writableStream`
- `write`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

