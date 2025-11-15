# Documentation: linting.ts
**File Path:** `packages/preview-server/src/utils/linting.ts`
**Language:** typescript
**Size:** 1,479 bytes
**Lines:** 61
**Generated:** 2025-11-15T20:37:32.027504Z

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

- **Path:** `packages/preview-server/src/utils/linting.ts`
- **Name:** `linting.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,479 bytes (1.44 KB)
- **Lines of Code:** 61

---

## Original Source

```typescript
import { checkImages } from '../actions/email-validation/check-images';
import { checkLinks } from '../actions/email-validation/check-links';
import type { LintingRow } from '../components/toolbar/linter';
import { loadStream } from './load-stream';

export interface LintingSource<T> {
  getStream(): Promise<ReadableStream<T>>;
  mapValue(value: NoInfer<T>): LintingRow | undefined;
}

function createSource<T>(source: LintingSource<T>): LintingSource<T> {
  return source;
}

export function getLintingSources(
  markup: string,

  urlBase: string,
): LintingSource<unknown>[] {
  return [
    createSource({
      getStream() {
        return checkImages(markup, urlBase);
      },
      mapValue(result) {
        if (result && result.status !== 'success') {
          return {
            result: result,
            source: 'image',
          };
        }
      },
    }),
    createSource({
      getStream() {
        return checkLinks(markup);
      },
      mapValue(result) {
        if (result && result.status !== 'success') {
          return {
            result: result,
            source: 'link',
          };
        }
      },
    }),
  ];
}

export async function* loadLintingRowsFrom(sources: LintingSource<unknown>[]) {
  for await (const source of sources) {
    const stream = await source.getStream();
    for await (const value of loadStream(stream)) {
      const row = source.mapValue(value);
      if (row) {
        yield row;
      }
    }
  }
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getLintingSources()`
- `row()`
- `stream()`

### Interfaces

- `LintingSource`

### Dependencies

This file imports/requires:

- `../actions/email-validation/check-images`
- `../actions/email-validation/check-links`
- `../components/toolbar/linter`
- `./load-stream`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 39

- `LintingRow`
- `LintingSource`
- `NoInfer`
- `Promise`
- `ReadableStream`
- `actions`
- `check`
- `checkImages`
- `checkLinks`
- `components`
- `createSource`
- `email`
- `getLintingSources`
- `getStream`
- `image`
- `images`
- `interface`
- `link`
- `links`
- `linter`
- `load`
- `loadLintingRowsFrom`
- `loadStream`
- `mapValue`
- `markup`
- `result`
- `row`
- `source`
- `sources`
- `status`
- `stream`
- `string`
- `success`
- `toolbar`
- `type`
- `unknown`
- `urlBase`
- `validation`
- `value`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

