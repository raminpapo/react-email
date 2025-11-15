# Documentation: benchmark-0.0.17-vs-local-version.tsx
**File Path:** `benchmarks/tailwind-component/src/benchmark-0.0.17-vs-local-version.tsx`
**Language:** tsx
**Size:** 895 bytes
**Lines:** 36
**Generated:** 2025-11-15T20:37:33.234445Z

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

- **Path:** `benchmarks/tailwind-component/src/benchmark-0.0.17-vs-local-version.tsx`
- **Name:** `benchmark-0.0.17-vs-local-version.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 895 bytes (0.87 KB)
- **Lines of Code:** 36

---

## Original Source

```tsx
import { writeFileSync } from 'node:fs';
import { render } from '@react-email/render';
import { Tailwind as LocalTailwind } from '@react-email/tailwind';
import { Tailwind as VersionSeventeenTailwind } from 'tailwind-0.0.17';
import { Bench } from 'tinybench';
import EmailWithTailwind from './emails/with-tailwind.js';

const main = async () => {
  const bench = new Bench({
    iterations: 100,
  });

  bench
    .add('local', async () => {
      await render(<EmailWithTailwind Tailwind={LocalTailwind} />);
    })
    .add('0.0.17', async () => {
      await render(<EmailWithTailwind Tailwind={VersionSeventeenTailwind} />);
    });

  await bench.run();

  return bench;
};

main()
  .then((bench) => {
    writeFileSync(
      'bench-results-100-iterations.json',
      JSON.stringify(bench.results),
      'utf-8',
    );
    console.table(bench.table());
  })
  .catch(console.error);

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `bench()`
- `main()`

### Dependencies

This file imports/requires:

- `./emails/with-tailwind.js`
- `@react-email/render`
- `@react-email/tailwind`
- `node:fs`
- `tailwind-0.0.17`
- `tinybench`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 27

- `Bench`
- `EmailWithTailwind`
- `LocalTailwind`
- `Tailwind`
- `VersionSeventeenTailwind`
- `add`
- `bench`
- `console`
- `email`
- `emails`
- `error`
- `iterations`
- `json`
- `local`
- `main`
- `node`
- `react`
- `render`
- `results`
- `run`
- `stringify`
- `table`
- `tailwind`
- `then`
- `tinybench`
- `utf`
- `writeFileSync`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

