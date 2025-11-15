# Documentation: render.tsx
**File Path:** `packages/render/src/edge/render.tsx`
**Language:** tsx
**Size:** 1,301 bytes
**Lines:** 46
**Generated:** 2025-11-15T20:37:31.476126Z

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

- **Path:** `packages/render/src/edge/render.tsx`
- **Name:** `render.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,301 bytes (1.27 KB)
- **Lines of Code:** 46

---

## Original Source

```tsx
import { Suspense } from 'react';
import { pretty } from '../node';
import type { Options } from '../shared/options';
import { readStream } from '../shared/read-stream.browser';
import { toPlainText } from '../shared/utils/to-plain-text';
import { importReactDom } from './import-react-dom';

export const render = async (
  element: React.ReactElement,
  options?: Options,
) => {
  const suspendedElement = <Suspense>{element}</Suspense>;
  const reactDOMServer = await importReactDom().then(
    // This is because react-dom/server is CJS
    (m) => m.default,
  );

  const html = await new Promise<string>((resolve, reject) => {
    reactDOMServer
      .renderToReadableStream(suspendedElement, {
        onError(error: unknown) {
          reject(error);
        },
        progressiveChunkSize: Number.POSITIVE_INFINITY,
      })
      .then(readStream)
      .then(resolve)
      .catch(reject);
  });

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
- `html()`
- `reactDOMServer()`
- `render()`
- `suspendedElement()`

### Dependencies

This file imports/requires:

- `../node`
- `../shared/options`
- `../shared/read-stream.browser`
- `../shared/utils/to-plain-text`
- `./import-react-dom`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 52

- `Number`
- `Options`
- `POSITIVE_INFINITY`
- `Promise`
- `React`
- `ReactElement`
- `Suspense`
- `Transitional`
- `W3C`
- `because`
- `browser`
- `doctype`
- `document`
- `dom`
- `dtd`
- `element`
- `error`
- `html`
- `htmlToTextOptions`
- `http`
- `importReactDom`
- `node`
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
- `unknown`
- `utils`
- `www`
- `xhtml1`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

