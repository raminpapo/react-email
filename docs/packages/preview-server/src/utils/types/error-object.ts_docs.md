# Documentation: error-object.ts
**File Path:** `packages/preview-server/src/utils/types/error-object.ts`
**Language:** typescript
**Size:** 272 bytes
**Lines:** 12
**Generated:** 2025-11-15T20:37:32.067113Z

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

- **Path:** `packages/preview-server/src/utils/types/error-object.ts`
- **Name:** `error-object.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 272 bytes (0.27 KB)
- **Lines of Code:** 12

---

## Original Source

```typescript
/**
 * An object that mimics the structure of the Error class,
 * we just can't use the Error class here because server actions can't
 * return classes
 */
export interface ErrorObject {
  name: string;
  stack: string | undefined;
  cause?: unknown;
  message: string;
}

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Interfaces

- `ErrorObject`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 19

- `Error`
- `ErrorObject`
- `actions`
- `because`
- `cause`
- `classes`
- `here`
- `interface`
- `just`
- `message`
- `mimics`
- `name`
- `object`
- `server`
- `stack`
- `string`
- `structure`
- `unknown`
- `use`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

