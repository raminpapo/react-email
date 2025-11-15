# Documentation: hot-reload-change.ts
**File Path:** `packages/preview-server/src/utils/types/hot-reload-change.ts`
**Language:** typescript
**Size:** 194 bytes
**Lines:** 14
**Generated:** 2025-11-15T20:37:32.068017Z

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

- **Path:** `packages/preview-server/src/utils/types/hot-reload-change.ts`
- **Name:** `hot-reload-change.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 194 bytes (0.19 KB)
- **Lines of Code:** 14

---

## Original Source

```typescript
export interface HotReloadChange {
  filename: string;
  event:
    | 'all'
    | 'ready'
    | 'add'
    | 'change'
    | 'addDir'
    | 'unlink'
    | 'unlinkDir'
    | 'raw'
    | 'error';
}

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Interfaces

- `HotReloadChange`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 14

- `HotReloadChange`
- `add`
- `addDir`
- `all`
- `change`
- `error`
- `event`
- `filename`
- `interface`
- `raw`
- `ready`
- `string`
- `unlink`
- `unlinkDir`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

