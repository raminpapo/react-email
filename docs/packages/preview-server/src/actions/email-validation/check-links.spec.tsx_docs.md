# Documentation: check-links.spec.tsx
**File Path:** `packages/preview-server/src/actions/email-validation/check-links.spec.tsx`
**Language:** tsx
**Size:** 2,226 bytes
**Lines:** 114
**Generated:** 2025-11-15T20:37:31.995902Z

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

- **Path:** `packages/preview-server/src/actions/email-validation/check-links.spec.tsx`
- **Name:** `check-links.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,226 bytes (2.17 KB)
- **Lines of Code:** 114

---

## Original Source

```tsx
import { checkLinks, type LinkCheckingResult } from './check-links';

test('checkLinks()', async () => {
  const results: LinkCheckingResult[] = [];
  const html = `<div>
  <a href="/">Root</a>
  <a href="https://resend.com">Resend</a>
  <a href="https://notion.so">Notion</a>
  <a href="http://react.email">React Email unsafe</a>
</div>`;
  const stream = await checkLinks(html);
  const reader = stream.getReader();
  while (true) {
    const { done, value } = await reader.read();
    if (value) {
      results.push(value);
    }
    if (done) {
      break;
    }
  }
  expect(results).toEqual([
    {
      status: 'error',
      codeLocation: {
        line: 2,
        column: 3,
      },
      checks: [
        {
          type: 'syntax',
          passed: false,
        },
      ],
      link: '/',
    },
    {
      status: 'success',
      codeLocation: {
        line: 3,
        column: 3,
      },
      checks: [
        {
          type: 'syntax',
          passed: true,
        },
        {
          type: 'security',
          passed: true,
        },
        {
          type: 'fetch_attempt',
          passed: true,
          metadata: {
            fetchStatusCode: 200,
          },
        },
      ],
      link: 'https://resend.com',
    },
    {
      status: 'warning',
      codeLocation: {
        line: 4,
        column: 3,
      },
      checks: [
        {
          type: 'syntax',
          passed: true,
        },
        {
          type: 'security',
          passed: true,
        },
        {
          type: 'fetch_attempt',
          metadata: {
            fetchStatusCode: 301,
          },
          passed: false,
        },
      ],
      link: 'https://notion.so',
    },
    {
      status: 'warning',
      codeLocation: {
        line: 5,
        column: 3,
      },
      checks: [
        {
          type: 'syntax',
          passed: true,
        },
        {
          type: 'security',
          passed: false,
        },
        {
          type: 'fetch_attempt',
          metadata: {
            fetchStatusCode: 308,
          },
          passed: false,
        },
      ],
      link: 'http://react.email',
    },
  ] satisfies LinkCheckingResult[]);
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `html()`
- `reader()`
- `stream()`

### Type Definitions

- `LinkCheckingResult`

### Dependencies

This file imports/requires:

- `./check-links`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 48

- `Email`
- `LinkCheckingResult`
- `Notion`
- `React`
- `Resend`
- `Root`
- `check`
- `checkLinks`
- `checks`
- `codeLocation`
- `column`
- `com`
- `div`
- `done`
- `email`
- `error`
- `expect`
- `fetchStatusCode`
- `fetch_attempt`
- `getReader`
- `href`
- `html`
- `http`
- `https`
- `line`
- `link`
- `links`
- `metadata`
- `notion`
- `passed`
- `push`
- `react`
- `read`
- `reader`
- `resend`
- `results`
- `satisfies`
- `security`
- `status`
- `stream`
- `success`
- `syntax`
- `test`
- `toEqual`
- `type`
- `unsafe`
- `value`
- `warning`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

