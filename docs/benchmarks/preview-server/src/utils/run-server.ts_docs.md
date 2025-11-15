# Documentation: run-server.ts
**File Path:** `benchmarks/preview-server/src/utils/run-server.ts`
**Language:** typescript
**Size:** 1,103 bytes
**Lines:** 41
**Generated:** 2025-11-15T20:37:33.224033Z

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

- **Path:** `benchmarks/preview-server/src/utils/run-server.ts`
- **Name:** `run-server.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,103 bytes (1.08 KB)
- **Lines of Code:** 41

---

## Original Source

```typescript
import { type ChildProcessWithoutNullStreams, spawn } from 'node:child_process';
import path from 'node:path';

const decoder = new TextDecoder();

export interface Server {
  subprocess: ChildProcessWithoutNullStreams;
  url: string;
}

export function runServer(pathToCliScript: string) {
  return new Promise<Server>((resolve, reject) => {
    const node = spawn('node', [pathToCliScript, 'dev'], {
      cwd: path.resolve(__dirname, '../../../../apps/demo'),
    });

    node.stdout.on('data', (data) => {
      const content = decoder.decode(data);
      if (content.includes('Running preview at')) {
        const url = /http:\/\/localhost:[\d]+/.exec(content)?.[0];
        if (url) {
          resolve({
            subprocess: node,
            url,
          });
        } else {
          node.kill();
          reject(
            new Error(
              'URL was non existant in the same line, maybe we changed the way this is displayed?',
              {
                cause: { content, pathToCliScript },
              },
            ),
          );
        }
      }
    });
  });
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `content()`
- `decoder()`
- `node()`
- `runServer()`
- `url()`

### Interfaces

- `Server`

### Type Definitions

- `ChildProcessWithoutNullStreams`

### Dependencies

This file imports/requires:

- `node:child_process`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 44

- `ChildProcessWithoutNullStreams`
- `Error`
- `Promise`
- `Running`
- `Server`
- `TextDecoder`
- `__dirname`
- `apps`
- `cause`
- `changed`
- `child_process`
- `content`
- `cwd`
- `data`
- `decode`
- `decoder`
- `demo`
- `dev`
- `displayed`
- `exec`
- `existant`
- `http`
- `includes`
- `interface`
- `kill`
- `line`
- `localhost`
- `maybe`
- `node`
- `non`
- `path`
- `pathToCliScript`
- `preview`
- `reject`
- `resolve`
- `runServer`
- `same`
- `spawn`
- `stdout`
- `string`
- `subprocess`
- `type`
- `url`
- `way`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

