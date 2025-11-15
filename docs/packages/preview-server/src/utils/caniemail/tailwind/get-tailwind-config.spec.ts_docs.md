# Documentation: get-tailwind-config.spec.ts
**File Path:** `packages/preview-server/src/utils/caniemail/tailwind/get-tailwind-config.spec.ts`
**Language:** typescript
**Size:** 844 bytes
**Lines:** 27
**Generated:** 2025-11-15T20:37:32.057564Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/tailwind/get-tailwind-config.spec.ts`
- **Name:** `get-tailwind-config.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 844 bytes (0.82 KB)
- **Lines of Code:** 27

---

## Original Source

```typescript
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { parse } from '@babel/parser';
import { pixelBasedPreset } from '@react-email/components';
import { getTailwindConfig } from './get-tailwind-config';

describe('getTailwindConfig()', () => {
  it('works with email templates that import the tailwind config', async () => {
    const sourcePath = path.resolve(
      __dirname,
      './tests/dummy-email-template.tsx',
    );
    const sourceCode = await fs.readFile(sourcePath, 'utf8');
    const ast = parse(sourceCode, {
      strictMode: false,
      errorRecovery: true,
      sourceType: 'unambiguous',
      plugins: ['jsx', 'typescript', 'decorators'],
    });

    expect(await getTailwindConfig(sourceCode, ast, sourcePath)).toEqual({
      theme: {},
      presets: [pixelBasedPreset],
    });
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
- `sourceCode()`
- `sourcePath()`

### Dependencies

This file imports/requires:

- `./get-tailwind-config`
- `@babel/parser`
- `@react-email/components`
- `node:fs`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 40

- `__dirname`
- `ast`
- `babel`
- `components`
- `config`
- `decorators`
- `describe`
- `dummy`
- `email`
- `errorRecovery`
- `expect`
- `get`
- `getTailwindConfig`
- `jsx`
- `node`
- `parse`
- `parser`
- `path`
- `pixelBasedPreset`
- `plugins`
- `presets`
- `promises`
- `react`
- `readFile`
- `resolve`
- `sourceCode`
- `sourcePath`
- `sourceType`
- `strictMode`
- `tailwind`
- `template`
- `templates`
- `tests`
- `theme`
- `toEqual`
- `tsx`
- `typescript`
- `unambiguous`
- `utf8`
- `works`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

