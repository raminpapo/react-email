# Documentation: export.spec.ts
**File Path:** `packages/react-email/src/commands/testing/export.spec.ts`
**Language:** typescript
**Size:** 605 bytes
**Lines:** 21
**Generated:** 2025-11-15T20:37:32.600173Z

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

- **Path:** `packages/react-email/src/commands/testing/export.spec.ts`
- **Name:** `export.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 605 bytes (0.59 KB)
- **Lines of Code:** 21

---

## Original Source

```typescript
import fs from 'node:fs';
import path from 'node:path';
import { exportTemplates } from '../export.js';

test('email export', { retry: 3 }, async () => {
  const pathToEmailsDirectory = path.resolve(__dirname, './emails');
  const pathToDumpMarkup = path.resolve(__dirname, './out');
  await exportTemplates(pathToDumpMarkup, pathToEmailsDirectory, {
    silent: true,
    pretty: true,
  });

  expect(fs.existsSync(pathToDumpMarkup)).toBe(true);
  expect(
    await fs.promises.readFile(
      path.resolve(pathToDumpMarkup, './vercel-invite-user.html'),
      'utf8',
    ),
  ).toMatchSnapshot();
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `pathToDumpMarkup()`
- `pathToEmailsDirectory()`

### Dependencies

This file imports/requires:

- `../export.js`
- `node:fs`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 25

- `__dirname`
- `email`
- `emails`
- `existsSync`
- `expect`
- `exportTemplates`
- `html`
- `invite`
- `node`
- `out`
- `path`
- `pathToDumpMarkup`
- `pathToEmailsDirectory`
- `pretty`
- `promises`
- `readFile`
- `resolve`
- `retry`
- `silent`
- `test`
- `toBe`
- `toMatchSnapshot`
- `user`
- `utf8`
- `vercel`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

