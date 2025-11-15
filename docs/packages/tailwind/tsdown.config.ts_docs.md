# Documentation: tsdown.config.ts
**File Path:** `packages/tailwind/tsdown.config.ts`
**Language:** typescript
**Size:** 1,160 bytes
**Lines:** 41
**Generated:** 2025-11-15T20:37:32.363054Z

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

- **Path:** `packages/tailwind/tsdown.config.ts`
- **Name:** `tsdown.config.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,160 bytes (1.13 KB)
- **Lines of Code:** 41

---

## Original Source

```typescript
import { createRequire } from 'node:module';
import url from 'node:url';
import { defineConfig } from 'tsdown/config';

export default defineConfig({
  entry: './src/index.ts',
  format: ['cjs', 'esm'],
  dts: true,
  noExternal: ['css-tree'],
  plugins: [
    {
      name: 'hoist-create-require-imports',
      async transform(code, id, meta) {
        if (id.includes('css-tree')) {
          const localizedRequire = createRequire(url.pathToFileURL(id));

          return {
            code: code
              .replaceAll("import { createRequire } from 'module';", '')
              .replaceAll(
                /(const|var|let)\s+require\s*=\s*createRequire\s*\([^)]*\)\s*;?/g,
                '',
              )
              .replaceAll(
                /require\s*\(\s*(['"])([^)]+?\.json)\1\s*\)/gm,
                (_match, _quote, jsonSpecifier) => {
                  return JSON.stringify(
                    localizedRequire(localizedRequire.resolve(jsonSpecifier)),
                    null,
                    2,
                  );
                },
              ),
            ...meta,
          };
        }
      },
    },
  ],
});

```

---

## Overview

This is a JavaScript/TypeScript file. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `localizedRequire()`

### Dependencies

This file imports/requires:

- `module`
- `node:module`
- `node:url`
- `tsdown/config`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 36

- `_match`
- `_quote`
- `cjs`
- `code`
- `config`
- `create`
- `createRequire`
- `css`
- `defineConfig`
- `dts`
- `entry`
- `esm`
- `format`
- `hoist`
- `imports`
- `includes`
- `index`
- `json`
- `jsonSpecifier`
- `localizedRequire`
- `meta`
- `module`
- `name`
- `noExternal`
- `node`
- `pathToFileURL`
- `plugins`
- `replaceAll`
- `require`
- `resolve`
- `src`
- `stringify`
- `transform`
- `tree`
- `tsdown`
- `url`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

