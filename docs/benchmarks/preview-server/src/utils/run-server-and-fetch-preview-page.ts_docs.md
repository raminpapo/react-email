# Documentation: run-server-and-fetch-preview-page.ts
**File Path:** `benchmarks/preview-server/src/utils/run-server-and-fetch-preview-page.ts`
**Language:** typescript
**Size:** 1,169 bytes
**Lines:** 41
**Generated:** 2025-11-15T20:37:33.222851Z

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

- **Path:** `benchmarks/preview-server/src/utils/run-server-and-fetch-preview-page.ts`
- **Name:** `run-server-and-fetch-preview-page.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,169 bytes (1.14 KB)
- **Lines of Code:** 41

---

## Original Source

```typescript
import { spawn } from 'node:child_process';
import path from 'node:path';

const decoder = new TextDecoder();

export function runServerAndFetchPreviewPage(pathToCliScript: string) {
  return new Promise<void>((resolve, reject) => {
    const node = spawn('node', [pathToCliScript, 'dev'], {
      cwd: path.resolve(__dirname, '../../../../apps/demo'),
    });

    node.stdout.on('data', (data) => {
      const content = decoder.decode(data);
      if (content.includes('Running preview at')) {
        const url = /http:\/\/localhost:[\d]+/.exec(content)?.[0];
        if (url) {
          fetch(`${url}/preview/magic-links/notion-magic-link`)
            .then(async () => {
              node.kill();
              resolve();
            })
            .catch(() => {
              node.kill();
              reject();
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
- `runServerAndFetchPreviewPage()`
- `url()`

### Dependencies

This file imports/requires:

- `node:child_process`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 46

- `Error`
- `Promise`
- `Running`
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
- `fetch`
- `http`
- `includes`
- `kill`
- `line`
- `link`
- `links`
- `localhost`
- `magic`
- `maybe`
- `node`
- `non`
- `notion`
- `path`
- `pathToCliScript`
- `preview`
- `reject`
- `resolve`
- `runServerAndFetchPreviewPage`
- `same`
- `spawn`
- `stdout`
- `string`
- `then`
- `url`
- `void`
- `way`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

