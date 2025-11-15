# Documentation: serve-static-file.ts
**File Path:** `packages/react-email/src/utils/preview/serve-static-file.ts`
**Language:** typescript
**Size:** 1,491 bytes
**Lines:** 52
**Generated:** 2025-11-15T20:37:32.547895Z

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

- **Path:** `packages/react-email/src/utils/preview/serve-static-file.ts`
- **Name:** `serve-static-file.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,491 bytes (1.46 KB)
- **Lines of Code:** 52

---

## Original Source

```typescript
import { existsSync, promises as fs } from 'node:fs';
import type http from 'node:http';
import path from 'node:path';
import type url from 'node:url';
import { lookup } from 'mime-types';

export const serveStaticFile = async (
  res: http.ServerResponse,
  parsedUrl: url.UrlWithParsedQuery,
  staticDirRelativePath: string,
) => {
  const pathname = parsedUrl.pathname!.replace('/static', './static');
  const ext = path.parse(pathname).ext;

  const staticBaseDir = path.resolve(process.cwd(), staticDirRelativePath);
  const fileAbsolutePath = path.resolve(staticBaseDir, pathname);
  if (!fileAbsolutePath.startsWith(staticBaseDir)) {
    res.statusCode = 403;
    res.end();
    return;
  }

  try {
    const fileHandle = await fs.open(fileAbsolutePath, 'r');

    const fileData = await fs.readFile(fileHandle);

    // if the file is found, set Content-type and send data
    res.setHeader('Content-type', lookup(ext) || 'text/plain');
    res.end(fileData);

    fileHandle.close();
  } catch (exception) {
    if (!existsSync(fileAbsolutePath)) {
      res.statusCode = 404;
      res.end();
    } else {
      const sanitizedFilePath = fileAbsolutePath.replace(/\n|\r/g, '');
      console.error(
        `Could not read file at %s to be served, here's the exception:`,
        sanitizedFilePath,
        exception,
      );

      res.statusCode = 500;
      res.end(
        'Could not read file to be served! Check your terminal for more information.',
      );
    }
  }
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `ext()`
- `fileAbsolutePath()`
- `fileData()`
- `fileHandle()`
- `pathname()`
- `sanitizedFilePath()`
- `serveStaticFile()`
- `staticBaseDir()`

### Dependencies

This file imports/requires:

- `mime-types`
- `node:fs`
- `node:http`
- `node:path`
- `node:url`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 56

- `Check`
- `Content`
- `ServerResponse`
- `UrlWithParsedQuery`
- `close`
- `console`
- `cwd`
- `data`
- `end`
- `error`
- `exception`
- `existsSync`
- `ext`
- `file`
- `fileAbsolutePath`
- `fileData`
- `fileHandle`
- `found`
- `here`
- `http`
- `information`
- `lookup`
- `mime`
- `more`
- `node`
- `open`
- `parse`
- `parsedUrl`
- `path`
- `pathname`
- `plain`
- `process`
- `promises`
- `read`
- `readFile`
- `replace`
- `res`
- `resolve`
- `sanitizedFilePath`
- `send`
- `serveStaticFile`
- `served`
- `set`
- `setHeader`
- `startsWith`
- `static`
- `staticBaseDir`
- `staticDirRelativePath`
- `statusCode`
- `string`
- `terminal`
- `text`
- `type`
- `types`
- `url`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

