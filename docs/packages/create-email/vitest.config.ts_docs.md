# Documentation: vitest.config.ts
**File Path:** `packages/create-email/vitest.config.ts`
**Language:** typescript
**Size:** 210 bytes
**Lines:** 10
**Generated:** 2025-11-15T20:37:32.315262Z

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

- **Path:** `packages/create-email/vitest.config.ts`
- **Name:** `vitest.config.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 210 bytes (0.21 KB)
- **Lines of Code:** 10

---

## Original Source

```typescript
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'happy-dom',
    exclude: ['.test/**/*', 'template/**/*', '**/node_modules'],
  },
});

```

---

## Overview

This is a JavaScript/TypeScript file. It exports a default export. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `vitest/config`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 11

- `config`
- `defineConfig`
- `dom`
- `environment`
- `exclude`
- `globals`
- `happy`
- `node_modules`
- `template`
- `test`
- `vitest`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

