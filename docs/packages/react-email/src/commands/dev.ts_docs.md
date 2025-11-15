# Documentation: dev.ts
**File Path:** `packages/react-email/src/commands/dev.ts`
**Language:** typescript
**Size:** 736 bytes
**Lines:** 28
**Generated:** 2025-11-15T20:37:32.592228Z

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

- **Path:** `packages/react-email/src/commands/dev.ts`
- **Name:** `dev.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 736 bytes (0.72 KB)
- **Lines of Code:** 28

---

## Original Source

```typescript
import fs from 'node:fs';
import { setupHotreloading, startDevServer } from '../utils/index.js';

interface Args {
  dir: string;
  port: string;
}

export const dev = async ({ dir: emailsDirRelativePath, port }: Args) => {
  try {
    if (!fs.existsSync(emailsDirRelativePath)) {
      console.error(`Missing ${emailsDirRelativePath} folder`);
      process.exit(1);
    }

    const devServer = await startDevServer(
      emailsDirRelativePath,
      emailsDirRelativePath, // defaults to ./emails/static for the static files that are served to the preview
      Number.parseInt(port, 10),
    );

    await setupHotreloading(devServer, emailsDirRelativePath);
  } catch (error) {
    console.log(error);
    process.exit(1);
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

- `dev()`
- `devServer()`

### Interfaces

- `Args`

### Dependencies

This file imports/requires:

- `../utils/index.js`
- `node:fs`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 29

- `Args`
- `Missing`
- `Number`
- `console`
- `defaults`
- `dev`
- `devServer`
- `dir`
- `emails`
- `emailsDirRelativePath`
- `error`
- `existsSync`
- `exit`
- `files`
- `folder`
- `index`
- `interface`
- `log`
- `node`
- `parseInt`
- `port`
- `preview`
- `process`
- `served`
- `setupHotreloading`
- `startDevServer`
- `static`
- `string`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

