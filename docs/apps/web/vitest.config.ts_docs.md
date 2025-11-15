# Documentation: vitest.config.ts
**File Path:** `apps/web/vitest.config.ts`
**Language:** typescript
**Size:** 434 bytes
**Lines:** 25
**Generated:** 2025-11-15T20:37:32.797945Z

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

- **Path:** `apps/web/vitest.config.ts`
- **Name:** `vitest.config.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 434 bytes (0.42 KB)
- **Lines of Code:** 25

---

## Original Source

```typescript
import path from 'node:path';
import { loadEnvConfig } from '@next/env';
import { defineConfig } from 'vitest/config';

loadEnvConfig(__dirname, true);

export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom',
  },
  esbuild: {
    tsconfigRaw: {
      compilerOptions: {
        jsx: 'react-jsx',
      },
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `@next/env`
- `node:path`
- `vitest/config`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 21

- `__dirname`
- `alias`
- `compilerOptions`
- `config`
- `defineConfig`
- `env`
- `environment`
- `esbuild`
- `globals`
- `jsdom`
- `jsx`
- `loadEnvConfig`
- `next`
- `node`
- `path`
- `react`
- `resolve`
- `src`
- `test`
- `tsconfigRaw`
- `vitest`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

