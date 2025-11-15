# Documentation: js-email-detection.spec.ts
**File Path:** `packages/preview-server/src/utils/js-email-detection.spec.ts`
**Language:** typescript
**Size:** 923 bytes
**Lines:** 25
**Generated:** 2025-11-15T20:37:32.025510Z

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

- **Path:** `packages/preview-server/src/utils/js-email-detection.spec.ts`
- **Name:** `js-email-detection.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 923 bytes (0.90 KB)
- **Lines of Code:** 25

---

## Original Source

```typescript
import path from 'node:path';
import { getEmailsDirectoryMetadata } from './get-emails-directory-metadata';

describe('JavaScript Email Detection', async () => {
  const testingDir = path.resolve(__dirname, 'testing');
  const emailsMetadata = await getEmailsDirectoryMetadata(testingDir, true);

  it('detects JavaScript files with ES6 export default syntax', async () => {
    expect(emailsMetadata).toBeDefined();
    expect(emailsMetadata?.emailFilenames).toContain(
      'js-email-export-default.js',
    );
  });

  it('detects JavaScript files with CommonJS module.exports', async () => {
    expect(emailsMetadata).toBeDefined();
    expect(emailsMetadata?.emailFilenames).toContain('js-email-test.js');
  });

  it('detects MDX-style JavaScript files with named exports', async () => {
    expect(emailsMetadata).toBeDefined();
    expect(emailsMetadata?.emailFilenames).toContain('mdx-email-test.js');
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `emailsMetadata()`
- `testingDir()`

### Dependencies

This file imports/requires:

- `./get-emails-directory-metadata`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 32

- `CommonJS`
- `Detection`
- `ES6`
- `Email`
- `JavaScript`
- `__dirname`
- `describe`
- `detects`
- `directory`
- `email`
- `emailFilenames`
- `emails`
- `emailsMetadata`
- `expect`
- `exports`
- `files`
- `get`
- `getEmailsDirectoryMetadata`
- `mdx`
- `metadata`
- `module`
- `named`
- `node`
- `path`
- `resolve`
- `style`
- `syntax`
- `test`
- `testing`
- `testingDir`
- `toBeDefined`
- `toContain`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

