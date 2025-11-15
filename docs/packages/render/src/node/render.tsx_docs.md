# Documentation: render.tsx
**File Path:** `packages/render/src/node/render.tsx`
**Language:** tsx
**Size:** 1,604 bytes
**Lines:** 54
**Generated:** 2025-11-15T20:37:31.515034Z

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

- **Path:** `packages/render/src/node/render.tsx`
- **Name:** `render.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,604 bytes (1.57 KB)
- **Lines of Code:** 54

---

## Original Source

```tsx
import { Suspense } from 'react';
import type { Options } from '../shared/options';
import { pretty } from '../shared/utils/pretty';
import { toPlainText } from '../shared/utils/to-plain-text';
import { readStream } from './read-stream';

export const render = async (node: React.ReactNode, options?: Options) => {
  const suspendedElement = <Suspense>{node}</Suspense>;
  const reactDOMServer = await import('react-dom/server').then(
    // This is beacuse react-dom/server is CJS
    (m) => m.default,
  );

  let html!: string;
  if (
    Object.hasOwn(reactDOMServer, 'renderToReadableStream') &&
    typeof WritableStream !== 'undefined'
  ) {
    html = await readStream(
      await reactDOMServer.renderToReadableStream(suspendedElement, {
        progressiveChunkSize: Number.POSITIVE_INFINITY,
      }),
    );
  } else {
    await new Promise<void>((resolve, reject) => {
      const stream = reactDOMServer.renderToPipeableStream(suspendedElement, {
        async onAllReady() {
          html = await readStream(stream);
          resolve();
        },
        onError(error) {
          reject(error as Error);
        },
        progressiveChunkSize: Number.POSITIVE_INFINITY,
      });
    });
  }

  if (options?.plainText) {
    return toPlainText(html, options.htmlToTextOptions);
  }

  const doctype =
    '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">';

  const document = `${doctype}${html.replace(/<!DOCTYPE.*?>/, '')}`;

  if (options?.pretty) {
    return pretty(document);
  }

  return document;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `doctype()`
- `document()`
- `reactDOMServer()`
- `render()`
- `stream()`
- `suspendedElement()`

### Dependencies

This file imports/requires:

- `../shared/options`
- `../shared/utils/pretty`
- `../shared/utils/to-plain-text`
- `./read-stream`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 55

- `Error`
- `Number`
- `Object`
- `Options`
- `POSITIVE_INFINITY`
- `Promise`
- `React`
- `ReactNode`
- `Suspense`
- `Transitional`
- `W3C`
- `WritableStream`
- `beacuse`
- `doctype`
- `document`
- `dom`
- `dtd`
- `error`
- `hasOwn`
- `html`
- `htmlToTextOptions`
- `http`
- `node`
- `onAllReady`
- `onError`
- `options`
- `org`
- `plain`
- `plainText`
- `pretty`
- `progressiveChunkSize`
- `react`
- `reactDOMServer`
- `read`
- `readStream`
- `reject`
- `render`
- `renderToPipeableStream`
- `renderToReadableStream`
- `replace`
- `resolve`
- `server`
- `shared`
- `stream`
- `string`
- `suspendedElement`
- `text`
- `then`
- `toPlainText`
- `transitional`
- `type`
- `utils`
- `void`
- `www`
- `xhtml1`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

