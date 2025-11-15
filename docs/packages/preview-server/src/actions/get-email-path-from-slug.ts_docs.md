# Documentation: get-email-path-from-slug.ts
**File Path:** `packages/preview-server/src/actions/get-email-path-from-slug.ts`
**Language:** typescript
**Size:** 1,097 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:31.780659Z

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

- **Path:** `packages/preview-server/src/actions/get-email-path-from-slug.ts`
- **Name:** `get-email-path-from-slug.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,097 bytes (1.07 KB)
- **Lines of Code:** 33

---

## Original Source

```typescript
'use server';

import fs from 'node:fs';
import path from 'node:path';
import { cache } from 'react';
import { emailsDirectoryAbsolutePath } from '../app/env';

export const getEmailPathFromSlug = cache(async (slug: string) => {
  if (['.tsx', '.jsx', '.ts', '.js'].includes(path.extname(slug)))
    return path.join(emailsDirectoryAbsolutePath, slug);

  const pathWithoutExtension = path.join(emailsDirectoryAbsolutePath, slug);

  if (fs.existsSync(`${pathWithoutExtension}.tsx`)) {
    return `${pathWithoutExtension}.tsx`;
  }
  if (fs.existsSync(`${pathWithoutExtension}.jsx`)) {
    return `${pathWithoutExtension}.jsx`;
  }
  if (fs.existsSync(`${pathWithoutExtension}.ts`)) {
    return `${pathWithoutExtension}.ts`;
  }
  if (fs.existsSync(`${pathWithoutExtension}.js`)) {
    return `${pathWithoutExtension}.js`;
  }

  throw new Error(
    `Could not find your email file based on the slug (${slug}) by guessing the file extension. Tried .tsx, .jsx, .ts and .js.

    This is most likely not an issue with the preview server. It most likely is that the email doesn't exist.`,
  );
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getEmailPathFromSlug()`
- `pathWithoutExtension()`

### Dependencies

This file imports/requires:

- `../app/env`
- `node:fs`
- `node:path`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 34

- `Error`
- `Tried`
- `app`
- `based`
- `cache`
- `doesn`
- `email`
- `emailsDirectoryAbsolutePath`
- `env`
- `exist`
- `existsSync`
- `extension`
- `extname`
- `file`
- `find`
- `getEmailPathFromSlug`
- `guessing`
- `includes`
- `issue`
- `join`
- `jsx`
- `likely`
- `most`
- `node`
- `path`
- `pathWithoutExtension`
- `preview`
- `react`
- `server`
- `slug`
- `string`
- `tsx`
- `use`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

