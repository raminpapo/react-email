# Documentation: get-tailwind-metadata.spec.ts
**File Path:** `packages/preview-server/src/utils/caniemail/tailwind/get-tailwind-metadata.spec.ts`
**Language:** typescript
**Size:** 813 bytes
**Lines:** 26
**Generated:** 2025-11-15T20:37:32.060694Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/tailwind/get-tailwind-metadata.spec.ts`
- **Name:** `get-tailwind-metadata.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 813 bytes (0.79 KB)
- **Lines of Code:** 26

---

## Original Source

```typescript
import fs from 'node:fs/promises';
import path from 'node:path';
import { parse } from '@babel/parser';
import { getTailwindMetadata } from './get-tailwind-metadata';

describe('getTailwindMetadata()', () => {
  test('with the netlify-welcome demo email', async () => {
    const emailPath = path.resolve(
      __dirname,
      '../../../../../../apps/demo/emails/welcome/netlify-welcome.tsx',
    );
    const reactCode = await fs.readFile(emailPath, 'utf8');
    const ast = parse(reactCode, {
      strictMode: false,
      errorRecovery: true,
      sourceType: 'unambiguous',
      plugins: ['jsx', 'typescript', 'decorators'],
    });

    const tailwindMetadata = getTailwindMetadata(ast, reactCode, emailPath);

    expect(tailwindMetadata).toBeDefined();
    // console.log(tailwindMetadata);
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `ast()`
- `emailPath()`
- `reactCode()`
- `tailwindMetadata()`

### Dependencies

This file imports/requires:

- `./get-tailwind-metadata`
- `@babel/parser`
- `node:fs/promises`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 39

- `__dirname`
- `apps`
- `ast`
- `babel`
- `console`
- `decorators`
- `demo`
- `describe`
- `email`
- `emailPath`
- `emails`
- `errorRecovery`
- `expect`
- `get`
- `getTailwindMetadata`
- `jsx`
- `log`
- `metadata`
- `netlify`
- `node`
- `parse`
- `parser`
- `path`
- `plugins`
- `promises`
- `reactCode`
- `readFile`
- `resolve`
- `sourceType`
- `strictMode`
- `tailwind`
- `tailwindMetadata`
- `test`
- `toBeDefined`
- `tsx`
- `typescript`
- `unambiguous`
- `utf8`
- `welcome`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

