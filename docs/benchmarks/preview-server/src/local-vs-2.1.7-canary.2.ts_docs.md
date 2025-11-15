# Documentation: local-vs-2.1.7-canary.2.ts
**File Path:** `benchmarks/preview-server/src/local-vs-2.1.7-canary.2.ts`
**Language:** typescript
**Size:** 1,217 bytes
**Lines:** 47
**Generated:** 2025-11-15T20:37:33.221632Z

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

- **Path:** `benchmarks/preview-server/src/local-vs-2.1.7-canary.2.ts`
- **Name:** `local-vs-2.1.7-canary.2.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,217 bytes (1.19 KB)
- **Lines of Code:** 47

---

## Original Source

```typescript
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { Bench } from 'tinybench';
import { runServer } from './utils/run-server';

const pathToCanaryCliScript = path.resolve(
  __dirname,
  '../',
  './node_modules/react-email-2.1.7-canary.2/cli/index.js',
);

const pathToLocalCliScript = path.resolve(
  __dirname,
  '../',
  './node_modules/react-email/dist/cli/index.js',
);

(async () => {
  const bench = new Bench({
    iterations: 30,
  });

  const localServer = await runServer(pathToLocalCliScript);
  const canaryServer = await runServer(pathToCanaryCliScript);
  bench
    .add('local', async () => {
      await fetch(`${localServer.url}/preview/magic-links/notion-magic-link`);
    })
    .add('2.1.7-canary.2', async () => {
      await fetch(`${canaryServer.url}/preview/magic-links/notion-magic-link`);
    });

  await fetch(`${localServer.url}/preview/magic-links/notion-magic-link`);
  await fetch(`${canaryServer.url}/preview/magic-links/notion-magic-link`);

  await bench.run();

  localServer.subprocess.kill();
  canaryServer.subprocess.kill();

  await fs.writeFile(
    'bench-results-30-iterations.json',
    JSON.stringify(bench.results),
    'utf8',
  );
})();

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `bench()`
- `canaryServer()`
- `localServer()`
- `pathToCanaryCliScript()`
- `pathToLocalCliScript()`

### Dependencies

This file imports/requires:

- `./utils/run-server`
- `node:fs`
- `node:path`
- `tinybench`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 40

- `Bench`
- `__dirname`
- `add`
- `bench`
- `canary`
- `canaryServer`
- `cli`
- `dist`
- `email`
- `fetch`
- `index`
- `iterations`
- `json`
- `kill`
- `link`
- `links`
- `local`
- `localServer`
- `magic`
- `node`
- `node_modules`
- `notion`
- `path`
- `pathToCanaryCliScript`
- `pathToLocalCliScript`
- `preview`
- `promises`
- `react`
- `resolve`
- `results`
- `run`
- `runServer`
- `server`
- `stringify`
- `subprocess`
- `tinybench`
- `url`
- `utf8`
- `utils`
- `writeFile`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

