# Documentation: fill-caniemail-data.mts
**File Path:** `packages/preview-server/scripts/fill-caniemail-data.mts`
**Language:** Unknown
**Size:** 1,137 bytes
**Lines:** 32
**Generated:** 2025-11-15T20:37:31.764786Z

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

- **Path:** `packages/preview-server/scripts/fill-caniemail-data.mts`
- **Name:** `fill-caniemail-data.mts`
- **Extension:** `.mts`
- **Language:** Unknown
- **Size:** 1,137 bytes (1.11 KB)
- **Lines of Code:** 32

---

## Original Source

```
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const caniemailDataURL =
  'https://www.caniemail.com/api/data-ordered.json';

const responseFromCaniemail = await fetch(caniemailDataURL);
if (!responseFromCaniemail.ok) {
  throw new Error(
    `Could not get the data from Caniemail and there is no cached data under your temporary folder to fallback for. 

This could be happneing for the following reasons:
- You don't have internet connectivity
- Caniemail is down
- Caniemail changed from where to fetch their data from, which means we need to fix this. If this is the case, please open up an issue.`,
  );
}

const response = await responseFromCaniemail.json();

const __dirname = path.dirname(fileURLToPath(import.meta.url));

await fs.writeFile(
  path.resolve(__dirname, '../src/actions/email-validation/caniemail-data.ts'),
  `import type { SupportEntry } from "./check-compatibility";

export const nicenames = ${JSON.stringify(response.nicenames, null, 2)};

export const supportEntries: SupportEntry[] = ${JSON.stringify(response.data, null, 2)}`,
);

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `./check-compatibility`
- `node:fs`
- `node:path`
- `node:url`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 61

- `Caniemail`
- `Error`
- `SupportEntry`
- `You`
- `__dirname`
- `actions`
- `api`
- `cached`
- `caniemail`
- `caniemailDataURL`
- `changed`
- `check`
- `com`
- `compatibility`
- `connectivity`
- `data`
- `dirname`
- `don`
- `down`
- `email`
- `fallback`
- `fetch`
- `fileURLToPath`
- `fix`
- `folder`
- `following`
- `get`
- `happneing`
- `https`
- `internet`
- `issue`
- `json`
- `means`
- `meta`
- `need`
- `nicenames`
- `node`
- `open`
- `ordered`
- `path`
- `please`
- `promises`
- `reasons`
- `resolve`
- `response`
- `responseFromCaniemail`
- `src`
- `stringify`
- `supportEntries`
- `temporary`
- `their`
- `there`
- `type`
- `under`
- `url`
- `validation`
- `where`
- `which`
- `writeFile`
- `www`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

