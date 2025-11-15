# Documentation: resolve-path-aliases.ts
**File Path:** `packages/react-email/src/utils/preview/hot-reloading/resolve-path-aliases.ts`
**Language:** typescript
**Size:** 796 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:32.561505Z

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

- **Path:** `packages/react-email/src/utils/preview/hot-reloading/resolve-path-aliases.ts`
- **Name:** `resolve-path-aliases.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 796 bytes (0.78 KB)
- **Lines of Code:** 33

---

## Original Source

```typescript
import path from 'node:path';
import { createMatchPath, loadConfig } from 'tsconfig-paths';

export const resolvePathAliases = (
  importPaths: string[],
  projectPath: string,
) => {
  const configLoadResult = loadConfig(projectPath);

  if (configLoadResult.resultType === 'success') {
    const matchPath = createMatchPath(
      configLoadResult.absoluteBaseUrl,
      configLoadResult.paths,
    );
    return importPaths.map((importedPath) => {
      const unaliasedPath = matchPath(importedPath, undefined, undefined, [
        '.tsx',
        '.ts',
        '.js',
        '.jsx',
        '.cjs',
        '.mjs',
      ]);
      if (unaliasedPath) {
        return `./${path.relative(projectPath, unaliasedPath)}`;
      }
      return importedPath;
    });
  }

  return importPaths;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `configLoadResult()`
- `matchPath()`
- `resolvePathAliases()`
- `unaliasedPath()`

### Dependencies

This file imports/requires:

- `node:path`
- `tsconfig-paths`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 23

- `absoluteBaseUrl`
- `cjs`
- `configLoadResult`
- `createMatchPath`
- `importPaths`
- `importedPath`
- `jsx`
- `loadConfig`
- `map`
- `matchPath`
- `mjs`
- `node`
- `path`
- `paths`
- `projectPath`
- `relative`
- `resolvePathAliases`
- `resultType`
- `string`
- `success`
- `tsconfig`
- `tsx`
- `unaliasedPath`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

