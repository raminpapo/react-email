# Documentation: load-stream.ts
**File Path:** `packages/preview-server/src/utils/load-stream.ts`
**Language:** typescript
**Size:** 294 bytes
**Lines:** 16
**Generated:** 2025-11-15T20:37:32.028558Z

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

- **Path:** `packages/preview-server/src/utils/load-stream.ts`
- **Name:** `load-stream.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 294 bytes (0.29 KB)
- **Lines of Code:** 16

---

## Original Source

```typescript
export async function* loadStream<T>(stream: ReadableStream<T>) {
  const reader = stream.getReader();
  try {
    while (true) {
      const { value, done } = await reader.read();
      if (done) {
        break;
      }

      yield value;
    }
  } finally {
    reader.releaseLock();
  }
}

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `reader()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 9

- `ReadableStream`
- `done`
- `getReader`
- `loadStream`
- `read`
- `reader`
- `releaseLock`
- `stream`
- `value`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

