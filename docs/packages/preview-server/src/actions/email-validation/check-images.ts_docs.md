# Documentation: check-images.ts
**File Path:** `packages/preview-server/src/actions/email-validation/check-images.ts`
**Language:** typescript
**Size:** 4,126 bytes
**Lines:** 161
**Generated:** 2025-11-15T20:37:31.993915Z

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

- **Path:** `packages/preview-server/src/actions/email-validation/check-images.ts`
- **Name:** `check-images.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 4,126 bytes (4.03 KB)
- **Lines of Code:** 161

---

## Original Source

```typescript
'use server';

import type { IncomingMessage } from 'node:http';
import { parse } from 'node-html-parser';
import {
  type CodeLocation,
  getCodeLocationFromAstElement,
} from './get-code-location-from-ast-element';
import { quickFetch } from './quick-fetch';

export type ImageCheck = { passed: boolean } & (
  | {
      type: 'accessibility';
      metadata: {
        alt: string | undefined;
      };
    }
  | {
      type: 'fetch_attempt';
      metadata: {
        fetchStatusCode: number | undefined;
      };
    }
  | {
      type: 'image_size';
      metadata: {
        byteCount: number | undefined;
      };
    }
  | {
      type: 'syntax';
    }
  | {
      type: 'security';
    }
);

export interface ImageCheckingResult {
  status: 'success' | 'warning' | 'error';
  source: string;
  codeLocation: CodeLocation;
  checks: ImageCheck[];
}

const getResponseSizeInBytes = async (res: IncomingMessage) => {
  let totalBytes = 0;
  for await (const chunk of res) {
    totalBytes += chunk.byteLength;
  }
  return totalBytes;
};

export const checkImages = async (code: string, base: string) => {
  const ast = parse(code);

  const readableStream = new ReadableStream<ImageCheckingResult>({
    async start(controller) {
      const images = ast.querySelectorAll('img');
      for await (const image of images) {
        const rawSource = image.attributes.src;
        if (!rawSource) continue;

        const source = rawSource?.startsWith('/')
          ? `${base}${rawSource}`
          : rawSource;

        const result: ImageCheckingResult = {
          source: rawSource,
          codeLocation: getCodeLocationFromAstElement(image, code),
          status: 'success',
          checks: [],
        };

        const alt = image.attributes.alt;
        result.checks.push({
          passed: alt !== undefined,
          type: 'accessibility',
          metadata: {
            alt,
          },
        });
        if (alt === undefined) {
          result.status = 'warning';
        }

        try {
          const url = new URL(source);
          result.checks.push({
            passed: true,
            type: 'syntax',
          });

          if (rawSource.startsWith('http://')) {
            result.checks.push({
              passed: false,
              type: 'security',
            });
            result.status = 'warning';
          } else {
            result.checks.push({
              passed: true,
              type: 'security',
            });
          }

          let res: IncomingMessage | undefined;
          try {
            res = await quickFetch(url);
            const hasSucceeded =
              res.statusCode?.toString().startsWith('2') ?? false;
            result.checks.push({
              type: 'fetch_attempt',
              passed: hasSucceeded,
              metadata: {
                fetchStatusCode: res.statusCode,
              },
            });
            if (!hasSucceeded) {
              result.status = res.statusCode?.toString().startsWith('3')
                ? 'warning'
                : 'error';
            }

            const responseSizeBytes = await getResponseSizeInBytes(res);
            result.checks.push({
              type: 'image_size',
              passed: responseSizeBytes < 1_048_576, // 1024 x 1024 bytes
              metadata: {
                byteCount: responseSizeBytes,
              },
            });
            if (responseSizeBytes > 1_048_576 && result.status !== 'error') {
              result.status = 'warning';
            }
          } catch (_exception) {
            result.checks.push({
              type: 'fetch_attempt',
              passed: false,
              metadata: {
                fetchStatusCode: undefined,
              },
            });
            result.status = 'error';
          }
        } catch (_exception) {
          result.checks.push({
            passed: false,
            type: 'syntax',
          });
          result.status = 'error';
        }

        controller.enqueue(result);
      }
      controller.close();
    },
  });

  return readableStream;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `alt()`
- `ast()`
- `checkImages()`
- `getResponseSizeInBytes()`
- `hasSucceeded()`
- `images()`
- `rawSource()`
- `readableStream()`
- `responseSizeBytes()`
- `source()`
- `totalBytes()`
- `url()`

### Interfaces

- `ImageCheckingResult`

### Type Definitions

- `CodeLocation`
- `ImageCheck`

### Dependencies

This file imports/requires:

- `./get-code-location-from-ast-element`
- `./quick-fetch`
- `node-html-parser`
- `node:http`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 72

- `CodeLocation`
- `ImageCheck`
- `ImageCheckingResult`
- `IncomingMessage`
- `ReadableStream`
- `_exception`
- `accessibility`
- `alt`
- `ast`
- `attributes`
- `base`
- `boolean`
- `byteCount`
- `byteLength`
- `bytes`
- `checkImages`
- `checks`
- `chunk`
- `close`
- `code`
- `codeLocation`
- `controller`
- `element`
- `enqueue`
- `error`
- `fetch`
- `fetchStatusCode`
- `fetch_attempt`
- `get`
- `getCodeLocationFromAstElement`
- `getResponseSizeInBytes`
- `hasSucceeded`
- `html`
- `http`
- `image`
- `image_size`
- `images`
- `img`
- `interface`
- `location`
- `metadata`
- `node`
- `number`
- `parse`
- `parser`
- `passed`
- `push`
- `querySelectorAll`
- `quick`
- `quickFetch`
- `rawSource`
- `readableStream`
- `res`
- `responseSizeBytes`
- `result`
- `security`
- `server`
- `source`
- `src`
- `start`
- `startsWith`
- `status`
- `statusCode`
- `string`
- `success`
- `syntax`
- `toString`
- `totalBytes`
- `type`
- `url`
- `use`
- `warning`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

