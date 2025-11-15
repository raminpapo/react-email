# Documentation: index.spec.ts
**File Path:** `packages/create-email/src/index.spec.ts`
**Language:** typescript
**Size:** 2,060 bytes
**Lines:** 73
**Generated:** 2025-11-15T20:37:32.318166Z

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

- **Path:** `packages/create-email/src/index.spec.ts`
- **Name:** `index.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,060 bytes (2.01 KB)
- **Lines of Code:** 73

---

## Original Source

```typescript
import { spawnSync } from 'node:child_process';
import { existsSync, promises as fs } from 'node:fs';
import path from 'node:path';

describe('automatic setup', () => {
  const starterPath = path.resolve(__dirname, '../.test');
  test.sequential('creation', async () => {
    if (existsSync(starterPath)) {
      await fs.rm(starterPath, { recursive: true });
    }

    const createEmailProcess = spawnSync(
      'node',
      [path.resolve(__dirname, './index.js'), '.test'],
      {
        shell: true,
        cwd: path.resolve(__dirname, '../'),
        stdio: 'pipe',
      },
    );
    if (createEmailProcess.stderr) {
      console.log(createEmailProcess.stderr.toString());
    }
    expect(createEmailProcess.status, 'starter creation should return 0').toBe(
      0,
    );
  });

  test.sequential('install', { timeout: 40_000 }, () => {
    const installProcess = spawnSync('npm', ['install'], {
      shell: true,
      cwd: path.resolve(starterPath),
      stdio: 'pipe',
    });
    if (installProcess.stderr) {
      console.log(installProcess.stderr.toString());
    }
    expect(installProcess.status, 'starter npm install should return 0').toBe(
      0,
    );
  });

  test.sequential('export', () => {
    const exportProcess = spawnSync('npm', ['run export'], {
      shell: true,
      cwd: starterPath,
      stdio: 'pipe',
    });
    if (exportProcess.stderr) {
      console.log(exportProcess.stderr.toString());
    }
    expect(exportProcess.status, 'export should return status code 0').toBe(0);
  });

  test.sequential('type checking', { timeout: 10_000 }, () => {
    const typecheckingProcess = spawnSync('npx', ['tsc'], {
      shell: true,
      cwd: starterPath,
      stdio: 'pipe',
    });
    if (typecheckingProcess.stderr) {
      console.log(typecheckingProcess.stderr.toString());
    }
    if (typecheckingProcess.stdout) {
      console.log(typecheckingProcess.stdout.toString());
    }
    expect(
      typecheckingProcess.status,
      'type checking should return status code 0',
    ).toBe(0);
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `createEmailProcess()`
- `exportProcess()`
- `installProcess()`
- `starterPath()`
- `typecheckingProcess()`

### Dependencies

This file imports/requires:

- `node:child_process`
- `node:fs`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 43

- `__dirname`
- `automatic`
- `checking`
- `child_process`
- `code`
- `console`
- `createEmailProcess`
- `creation`
- `cwd`
- `describe`
- `existsSync`
- `expect`
- `exportProcess`
- `index`
- `install`
- `installProcess`
- `log`
- `node`
- `npm`
- `npx`
- `path`
- `pipe`
- `promises`
- `recursive`
- `resolve`
- `run`
- `sequential`
- `setup`
- `shell`
- `spawnSync`
- `starter`
- `starterPath`
- `status`
- `stderr`
- `stdio`
- `stdout`
- `test`
- `timeout`
- `toBe`
- `toString`
- `tsc`
- `type`
- `typecheckingProcess`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

