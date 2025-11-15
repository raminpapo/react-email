# Documentation: scaleway.ts
**File Path:** `examples/scaleway/next/src/lib/scaleway.ts`
**Language:** typescript
**Size:** 346 bytes
**Lines:** 12
**Generated:** 2025-11-15T20:37:32.666077Z

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

- **Path:** `examples/scaleway/next/src/lib/scaleway.ts`
- **Name:** `scaleway.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 346 bytes (0.34 KB)
- **Lines of Code:** 12

---

## Original Source

```typescript
import { createClient, TransactionalEmail } from '@scaleway/sdk';

const client = createClient({
  accessKey: process.env.ACCESS_KEY,
  secretKey: process.env.SECRET_KEY,
  defaultProjectId: process.env.PROJECT_ID,
  defaultRegion: 'fr-par',
  defaultZone: 'fr-par-1',
});

export const scalewayTEM = new TransactionalEmail.v1alpha1.API(client);

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `client()`
- `scalewayTEM()`

### Dependencies

This file imports/requires:

- `@scaleway/sdk`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 18

- `ACCESS_KEY`
- `PROJECT_ID`
- `SECRET_KEY`
- `TransactionalEmail`
- `accessKey`
- `client`
- `createClient`
- `defaultProjectId`
- `defaultRegion`
- `defaultZone`
- `env`
- `par`
- `process`
- `scaleway`
- `scalewayTEM`
- `sdk`
- `secretKey`
- `v1alpha1`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

