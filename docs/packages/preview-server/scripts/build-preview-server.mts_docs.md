# Documentation: build-preview-server.mts
**File Path:** `packages/preview-server/scripts/build-preview-server.mts`
**Language:** Unknown
**Size:** 685 bytes
**Lines:** 30
**Generated:** 2025-11-15T20:37:31.762667Z

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

- **Path:** `packages/preview-server/scripts/build-preview-server.mts`
- **Name:** `build-preview-server.mts`
- **Extension:** `.mts`
- **Language:** Unknown
- **Size:** 685 bytes (0.67 KB)
- **Lines of Code:** 30

---

## Original Source

```
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';

const filename = url.fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);

const nextBuildProcess = spawn('pnpm', ['next', 'build'], {
  detached: true,
  shell: true,
  stdio: 'inherit',
  cwd: path.resolve(dirname, '../'),
});

process.on('SIGINT', () => {
  nextBuildProcess.kill('SIGINT');
});

nextBuildProcess.on('exit', (code) => {
  if (code !== 0) {
    console.error(`next build failed with exit code ${code}`);
    process.exit(code);
  }

  fs.rmSync(path.resolve(dirname, '../.next/cache'), {
    recursive: true,
  });
});

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `node:child_process`
- `node:fs`
- `node:path`
- `node:url`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 29

- `build`
- `cache`
- `child_process`
- `code`
- `console`
- `cwd`
- `detached`
- `dirname`
- `error`
- `exit`
- `failed`
- `fileURLToPath`
- `filename`
- `inherit`
- `kill`
- `meta`
- `next`
- `nextBuildProcess`
- `node`
- `path`
- `pnpm`
- `process`
- `recursive`
- `resolve`
- `rmSync`
- `shell`
- `spawn`
- `stdio`
- `url`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

