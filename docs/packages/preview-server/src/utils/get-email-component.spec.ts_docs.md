# Documentation: get-email-component.spec.ts
**File Path:** `packages/preview-server/src/utils/get-email-component.spec.ts`
**Language:** typescript
**Size:** 1,286 bytes
**Lines:** 44
**Generated:** 2025-11-15T20:37:32.016310Z

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

- **Path:** `packages/preview-server/src/utils/get-email-component.spec.ts`
- **Name:** `get-email-component.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,286 bytes (1.26 KB)
- **Lines of Code:** 44

---

## Original Source

```typescript
import path from 'node:path';
import { getEmailComponent } from './get-email-component';

describe('getEmailComponent()', () => {
  describe('Node internals support', () => {
    test('Request', async () => {
      const result = await getEmailComponent(
        path.resolve(__dirname, './testing/request-response-email.tsx'),
        path.resolve(__dirname, '../../jsx-runtime'),
      );
      if ('error' in result) {
        console.log(result.error);
        expect('error' in result, 'there should be no errors').toBe(false);
      }
    });
  });

  test('with a demo email template', async () => {
    const result = await getEmailComponent(
      path.resolve(__dirname, './testing/vercel-invite-user.tsx'),
      path.resolve(__dirname, '../../jsx-runtime'),
    );

    if ('error' in result) {
      console.log(result.error);
      expect('error' in result).toBe(false);
    } else {
      expect(result.emailComponent).toBeTruthy();
      expect(result.sourceMapToOriginalFile).toBeTruthy();

      const emailHtml = await result.render(
        result.createElement(
          result.emailComponent,
          result.emailComponent.PreviewProps,
        ),
        {
          pretty: true,
        },
      );
      expect(emailHtml).toMatchSnapshot();
    }
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `emailHtml()`
- `result()`

### Dependencies

This file imports/requires:

- `./get-email-component`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 42

- `Node`
- `PreviewProps`
- `Request`
- `__dirname`
- `component`
- `console`
- `createElement`
- `demo`
- `describe`
- `email`
- `emailComponent`
- `emailHtml`
- `error`
- `errors`
- `expect`
- `get`
- `getEmailComponent`
- `internals`
- `invite`
- `jsx`
- `log`
- `node`
- `path`
- `pretty`
- `render`
- `request`
- `resolve`
- `response`
- `result`
- `runtime`
- `sourceMapToOriginalFile`
- `support`
- `template`
- `test`
- `testing`
- `there`
- `toBe`
- `toBeTruthy`
- `toMatchSnapshot`
- `tsx`
- `user`
- `vercel`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

