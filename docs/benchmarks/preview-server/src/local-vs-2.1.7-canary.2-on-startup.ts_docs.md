# Documentation: local-vs-2.1.7-canary.2-on-startup.ts
**File Path:** `benchmarks/preview-server/src/local-vs-2.1.7-canary.2-on-startup.ts`
**Language:** typescript
**Size:** 1,077 bytes
**Lines:** 43
**Generated:** 2025-11-15T20:37:33.220514Z

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

- **Path:** `benchmarks/preview-server/src/local-vs-2.1.7-canary.2-on-startup.ts`
- **Name:** `local-vs-2.1.7-canary.2-on-startup.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,077 bytes (1.05 KB)
- **Lines of Code:** 43

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

  bench
    .add('startup on local', async () => {
      const server = await runServer(pathToLocalCliScript);
      await fetch(`${server.url}/preview/magic-links/notion-magic-link`);
      server.subprocess.kill();
    })
    .add('startup on 2.1.7-canary.2', async () => {
      const server = await runServer(pathToCanaryCliScript);
      await fetch(`${server.url}/preview/magic-links/notion-magic-link`);
      server.subprocess.kill();
    });

  await bench.run();

  await fs.writeFile(
    'startup-bench-results-30-iterations.json',
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
- `pathToCanaryCliScript()`
- `pathToLocalCliScript()`
- `server()`

### Dependencies

This file imports/requires:

- `./utils/run-server`
- `node:fs`
- `node:path`
- `tinybench`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 39

- `Bench`
- `__dirname`
- `add`
- `bench`
- `canary`
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
- `startup`
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

