# Documentation: create-jsx-runtime.ts
**File Path:** `packages/preview-server/src/utils/create-jsx-runtime.ts`
**Language:** typescript
**Size:** 1,300 bytes
**Lines:** 48
**Generated:** 2025-11-15T20:37:32.015124Z

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

- **Path:** `packages/preview-server/src/utils/create-jsx-runtime.ts`
- **Name:** `create-jsx-runtime.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,300 bytes (1.27 KB)
- **Lines of Code:** 48

---

## Original Source

```typescript
import fs from 'node:fs';
import path from 'node:path';
import esbuild from 'esbuild';

/**
 * Bundles the JSX runtime with the specified {@link cwd}. This is needed because the JSX runtime
 * imports React's which is forcefully the production one if the `NODE_ENV` is set to `production`,
 * even though we want to use the development one.
 *
 * It bundles into `/node_modules/.react-email-jsx-runtime` with the root being the {@link cwd}.
 */
export const createJsxRuntime = async (
  cwd: string,
  originalJsxRuntimePath: string,
) => {
  const jsxRuntimePath = path.join(
    cwd,
    'node_modules',
    '.react-email-jsx-runtime',
  );
  if (!fs.existsSync(jsxRuntimePath)) {
    await fs.promises.mkdir(jsxRuntimePath, {
      recursive: true,
    });
    await fs.promises.writeFile(
      path.join(jsxRuntimePath, 'package.json'),
      '{"type": "commonjs"}',
      'utf8',
    );
  }
  await esbuild.build({
    bundle: true,
    outfile: path.join(jsxRuntimePath, 'jsx-dev-runtime.js'),
    format: 'cjs',
    logLevel: 'silent',
    stdin: {
      resolveDir: cwd,
      sourcefile: 'jsx-dev-runtime.js',
      loader: 'js',
      contents: await fs.promises.readFile(
        path.join(originalJsxRuntimePath, 'jsx-dev-runtime.js'),
      ),
    },
  });

  return jsxRuntimePath;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `createJsxRuntime()`
- `jsxRuntimePath()`

### Dependencies

This file imports/requires:

- `esbuild`
- `node:fs`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 59

- `Bundles`
- `NODE_ENV`
- `React`
- `because`
- `build`
- `bundle`
- `bundles`
- `cjs`
- `commonjs`
- `contents`
- `createJsxRuntime`
- `cwd`
- `dev`
- `development`
- `email`
- `esbuild`
- `even`
- `existsSync`
- `forcefully`
- `format`
- `imports`
- `into`
- `join`
- `json`
- `jsx`
- `jsxRuntimePath`
- `link`
- `loader`
- `logLevel`
- `mkdir`
- `needed`
- `node`
- `node_modules`
- `one`
- `originalJsxRuntimePath`
- `outfile`
- `package`
- `path`
- `production`
- `promises`
- `react`
- `readFile`
- `recursive`
- `resolveDir`
- `root`
- `runtime`
- `set`
- `silent`
- `sourcefile`
- `specified`
- `stdin`
- `string`
- `though`
- `type`
- `use`
- `utf8`
- `want`
- `which`
- `writeFile`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

