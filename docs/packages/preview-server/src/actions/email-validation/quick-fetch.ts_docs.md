# Documentation: quick-fetch.ts
**File Path:** `packages/preview-server/src/actions/email-validation/quick-fetch.ts`
**Language:** typescript
**Size:** 401 bytes
**Lines:** 15
**Generated:** 2025-11-15T20:37:31.999801Z

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

- **Path:** `packages/preview-server/src/actions/email-validation/quick-fetch.ts`
- **Name:** `quick-fetch.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 401 bytes (0.39 KB)
- **Lines of Code:** 15

---

## Original Source

```typescript
import type { IncomingMessage } from 'node:http';
import http from 'node:http';
import https from 'node:https';

export const quickFetch = (url: URL) => {
  return new Promise<IncomingMessage>((resolve, reject) => {
    const caller = url.protocol === 'https:' ? https : http;
    caller
      .get(url, (res) => {
        resolve(res);
      })
      .on('error', (error) => reject(error));
  });
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `caller()`
- `quickFetch()`

### Dependencies

This file imports/requires:

- `node:http`
- `node:https`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 15

- `IncomingMessage`
- `Promise`
- `caller`
- `error`
- `get`
- `http`
- `https`
- `node`
- `protocol`
- `quickFetch`
- `reject`
- `res`
- `resolve`
- `type`
- `url`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

