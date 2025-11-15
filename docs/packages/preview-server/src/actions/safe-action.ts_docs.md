# Documentation: safe-action.ts
**File Path:** `packages/preview-server/src/actions/safe-action.ts`
**Language:** typescript
**Size:** 420 bytes
**Lines:** 16
**Generated:** 2025-11-15T20:37:31.785221Z

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

- **Path:** `packages/preview-server/src/actions/safe-action.ts`
- **Name:** `safe-action.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 420 bytes (0.41 KB)
- **Lines of Code:** 16

---

## Original Source

```typescript
import {
  createSafeActionClient,
  DEFAULT_SERVER_ERROR_MESSAGE,
} from 'next-safe-action';
import { z } from 'zod';

export const baseActionClient = createSafeActionClient({
  defineMetadataSchema() {
    return z.object({ actionName: z.string() });
  },
  handleServerError(error, options) {
    console.error(`Action error: ${options.metadata.actionName}`, error);
    return DEFAULT_SERVER_ERROR_MESSAGE;
  },
});

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `baseActionClient()`

### Dependencies

This file imports/requires:

- `next-safe-action`
- `zod`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 17

- `Action`
- `DEFAULT_SERVER_ERROR_MESSAGE`
- `action`
- `actionName`
- `baseActionClient`
- `console`
- `createSafeActionClient`
- `defineMetadataSchema`
- `error`
- `handleServerError`
- `metadata`
- `next`
- `object`
- `options`
- `safe`
- `string`
- `zod`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

