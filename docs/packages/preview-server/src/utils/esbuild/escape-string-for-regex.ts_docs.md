# Documentation: escape-string-for-regex.ts
**File Path:** `packages/preview-server/src/utils/esbuild/escape-string-for-regex.ts`
**Language:** typescript
**Size:** 136 bytes
**Lines:** 4
**Generated:** 2025-11-15T20:37:32.071971Z

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

- **Path:** `packages/preview-server/src/utils/esbuild/escape-string-for-regex.ts`
- **Name:** `escape-string-for-regex.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 136 bytes (0.13 KB)
- **Lines of Code:** 4

---

## Original Source

```typescript
export function escapeStringForRegex(string: string) {
  return string.replace(/[|\\{}()[\]^$+*?.]/g, '\\$&').replace(/-/g, '\\x2d');
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `escapeStringForRegex()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 4

- `escapeStringForRegex`
- `replace`
- `string`
- `x2d`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

