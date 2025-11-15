# Documentation: benchmark-with-vs-without.tsx
**File Path:** `benchmarks/tailwind-component/src/benchmark-with-vs-without.tsx`
**Language:** tsx
**Size:** 832 bytes
**Lines:** 31
**Generated:** 2025-11-15T20:37:33.235725Z

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

- **Path:** `benchmarks/tailwind-component/src/benchmark-with-vs-without.tsx`
- **Name:** `benchmark-with-vs-without.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 832 bytes (0.81 KB)
- **Lines of Code:** 31

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Tailwind as CurrentTailwind } from '@react-email/tailwind';
import { Bench } from 'tinybench';
import EmailWithTailwind from './emails/with-tailwind.js';
import EmailWithoutTailwind from './emails/without-tailwind.js';

// import like this instead of installing from the workspace
// to still be able to test versions that are already published

async function main() {
  const bench = new Bench({ time: 100 });

  bench
    .add('without tailwind', async () => {
      await render(<EmailWithoutTailwind />);
    })
    .add('with current tailwind', async () => {
      await render(<EmailWithTailwind Tailwind={CurrentTailwind} />);
    });

  await bench.run();

  return bench;
}

main()
  .then((bench) => {
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
- `./emails/without-tailwind.js`
- `@react-email/render`
- `@react-email/tailwind`
- `tinybench`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 32

- `Bench`
- `CurrentTailwind`
- `EmailWithTailwind`
- `EmailWithoutTailwind`
- `Tailwind`
- `able`
- `add`
- `already`
- `bench`
- `console`
- `current`
- `email`
- `emails`
- `error`
- `installing`
- `instead`
- `like`
- `main`
- `published`
- `react`
- `render`
- `run`
- `still`
- `table`
- `tailwind`
- `test`
- `then`
- `time`
- `tinybench`
- `versions`
- `without`
- `workspace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

