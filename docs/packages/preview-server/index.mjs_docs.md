# Documentation: index.mjs
**File Path:** `packages/preview-server/index.mjs`
**Language:** Unknown
**Size:** 490 bytes
**Lines:** 18
**Generated:** 2025-11-15T20:37:31.752403Z

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

- **Path:** `packages/preview-server/index.mjs`
- **Name:** `index.mjs`
- **Extension:** `.mjs`
- **Language:** Unknown
- **Size:** 490 bytes (0.48 KB)
- **Lines of Code:** 18

---

## Original Source

```
/**
 * this file is required so that import.meta.resolve and require.resolve can properly can find the module for this package
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import url from 'node:url';

const filename = url.fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);
const packageJson = JSON.parse(
  await fs.readFile(path.join(dirname, 'package.json'), 'utf-8'),
);

/**
 * @type {string}
 */
export const version = packageJson.version;

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `node:fs/promises`
- `node:path`
- `node:url`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 25

- `dirname`
- `file`
- `fileURLToPath`
- `filename`
- `find`
- `join`
- `json`
- `meta`
- `module`
- `node`
- `package`
- `packageJson`
- `parse`
- `path`
- `promises`
- `properly`
- `readFile`
- `require`
- `required`
- `resolve`
- `string`
- `type`
- `url`
- `utf`
- `version`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

