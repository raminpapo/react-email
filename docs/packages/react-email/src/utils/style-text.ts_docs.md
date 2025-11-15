# Documentation: style-text.ts
**File Path:** `packages/react-email/src/utils/style-text.ts`
**Language:** typescript
**Size:** 381 bytes
**Lines:** 12
**Generated:** 2025-11-15T20:37:32.534649Z

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

- **Path:** `packages/react-email/src/utils/style-text.ts`
- **Name:** `style-text.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 381 bytes (0.37 KB)
- **Lines of Code:** 12

---

## Original Source

```typescript
/**
 * Centralized fallback for Node versions (<20.12.0) without util.styleText.
 * Returns the original text when styleText is unavailable.
 */
import * as nodeUtil from 'node:util';

type StyleTextFunction = typeof nodeUtil.styleText;

export const styleText: StyleTextFunction = (nodeUtil as any).styleText
  ? (nodeUtil as any).styleText
  : (_: string, text: string) => text;

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Type Definitions

- `StyleTextFunction`

### Dependencies

This file imports/requires:

- `node:util`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 18

- `Centralized`
- `Node`
- `Returns`
- `StyleTextFunction`
- `any`
- `fallback`
- `node`
- `nodeUtil`
- `original`
- `string`
- `styleText`
- `text`
- `type`
- `unavailable`
- `util`
- `versions`
- `when`
- `without`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

