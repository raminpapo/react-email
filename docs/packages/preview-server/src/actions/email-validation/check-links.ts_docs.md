# Documentation: check-links.ts
**File Path:** `packages/preview-server/src/actions/email-validation/check-links.ts`
**Language:** typescript
**Size:** 2,889 bytes
**Lines:** 114
**Generated:** 2025-11-15T20:37:31.997340Z

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

- **Path:** `packages/preview-server/src/actions/email-validation/check-links.ts`
- **Name:** `check-links.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,889 bytes (2.82 KB)
- **Lines of Code:** 114

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

export type LinkCheck = { passed: boolean } & (
  | {
      type: 'fetch_attempt';
      metadata: {
        fetchStatusCode: number | undefined;
      };
    }
  | {
      type: 'syntax';
    }
  | {
      type: 'security';
    }
);

export interface LinkCheckingResult {
  status: 'success' | 'warning' | 'error';
  link: string;
  codeLocation: CodeLocation;
  checks: LinkCheck[];
}

export const checkLinks = async (code: string) => {
  const ast = parse(code);

  const readableStream = new ReadableStream<LinkCheckingResult>({
    async start(controller) {
      const anchors = ast.querySelectorAll('a');
      for await (const anchor of anchors) {
        const link = anchor.attributes.href;
        if (!link) continue;
        if (link.startsWith('mailto:')) continue;

        const result: LinkCheckingResult = {
          link,
          codeLocation: getCodeLocationFromAstElement(anchor, code),
          status: 'success',
          checks: [],
        };

        try {
          const url = new URL(link);
          result.checks.push({
            passed: true,
            type: 'syntax',
          });

          if (link.startsWith('http://')) {
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

- `anchors()`
- `ast()`
- `checkLinks()`
- `hasSucceeded()`
- `link()`
- `readableStream()`
- `url()`

### Interfaces

- `LinkCheckingResult`

### Type Definitions

- `CodeLocation`
- `LinkCheck`

### Dependencies

This file imports/requires:

- `./get-code-location-from-ast-element`
- `./quick-fetch`
- `node-html-parser`
- `node:http`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 60

- `CodeLocation`
- `IncomingMessage`
- `LinkCheck`
- `LinkCheckingResult`
- `ReadableStream`
- `_exception`
- `anchor`
- `anchors`
- `ast`
- `attributes`
- `boolean`
- `checkLinks`
- `checks`
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
- `hasSucceeded`
- `href`
- `html`
- `http`
- `interface`
- `link`
- `location`
- `mailto`
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
- `readableStream`
- `res`
- `result`
- `security`
- `server`
- `start`
- `startsWith`
- `status`
- `statusCode`
- `string`
- `success`
- `syntax`
- `toString`
- `type`
- `url`
- `use`
- `warning`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

