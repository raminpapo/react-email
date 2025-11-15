# Documentation: seed.mts
**File Path:** `packages/preview-server/scripts/seed.mts`
**Language:** Unknown
**Size:** 876 bytes
**Lines:** 30
**Generated:** 2025-11-15T20:37:31.765908Z

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

- **Path:** `packages/preview-server/scripts/seed.mts`
- **Name:** `seed.mts`
- **Extension:** `.mts`
- **Language:** Unknown
- **Size:** 876 bytes (0.86 KB)
- **Lines of Code:** 30

---

## Original Source

```
import { existsSync, promises as fs } from 'node:fs';
import path from 'node:path';
import url from 'node:url';

const filename = url.fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);

const previewServerRoot = path.resolve(dirname, '..');
const emailsDirectoryPath = path.join(previewServerRoot, 'emails');

const seedPath = path.join(dirname, './utils/default-seed/');

if (existsSync(emailsDirectoryPath)) {
  console.info(
    'Deleting all files inside the emails directory (except for .gitkeep)',
  );
  const files = await fs.readdir(emailsDirectoryPath);
  for await (const file of files) {
    if (file === '.gitkeep') {
      continue;
    }
    await fs.rm(file, { recursive: true, force: true });
  }
}

console.info('Copying over the defalt seed to the emails directory');
await fs.cp(seedPath, emailsDirectoryPath, {
  recursive: true,
});

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `node:fs`
- `node:path`
- `node:url`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 33

- `Copying`
- `Deleting`
- `all`
- `console`
- `defalt`
- `directory`
- `dirname`
- `emails`
- `emailsDirectoryPath`
- `except`
- `existsSync`
- `file`
- `fileURLToPath`
- `filename`
- `files`
- `force`
- `gitkeep`
- `info`
- `inside`
- `join`
- `meta`
- `node`
- `over`
- `path`
- `previewServerRoot`
- `promises`
- `readdir`
- `recursive`
- `resolve`
- `seed`
- `seedPath`
- `url`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

