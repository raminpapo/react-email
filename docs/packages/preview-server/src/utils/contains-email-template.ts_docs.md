# Documentation: contains-email-template.ts
**File Path:** `packages/preview-server/src/utils/contains-email-template.ts`
**Language:** typescript
**Size:** 1,319 bytes
**Lines:** 51
**Generated:** 2025-11-15T20:37:32.011681Z

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

- **Path:** `packages/preview-server/src/utils/contains-email-template.ts`
- **Name:** `contains-email-template.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,319 bytes (1.29 KB)
- **Lines of Code:** 51

---

## Original Source

```typescript
import type { EmailsDirectory } from './get-emails-directory-metadata';

export const removeFilenameExtension = (filename: string): string => {
  const parts = filename.split('.');

  if (parts.length > 1) {
    return parts.slice(0, -1).join('.');
  }

  return filename;
};

export const containsEmailTemplate = (
  relativeEmailPath: string,
  directory: EmailsDirectory,
) => {
  const emailPathSegments = relativeEmailPath
    .replace(directory.relativePath, '')
    .split('/')
    .filter(Boolean);

  return containsEmailPathSegments(emailPathSegments, directory);
};

const containsEmailPathSegments = (
  relativeEmailSegments: string[],
  directory: EmailsDirectory,
) => {
  if (relativeEmailSegments.length === 1) {
    const emailFilename = removeFilenameExtension(relativeEmailSegments[0]!);
    return directory.emailFilenames.includes(emailFilename);
  }

  const remainingPath = relativeEmailSegments.join('/');

  for (const subDirectory of directory.subDirectories) {
    if (remainingPath.startsWith(subDirectory.directoryName)) {
      const matchedSegments = subDirectory.directoryName
        .split('/')
        .filter(Boolean).length;

      return containsEmailPathSegments(
        relativeEmailSegments.slice(matchedSegments),
        subDirectory,
      );
    }
  }

  return false;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `containsEmailPathSegments()`
- `containsEmailTemplate()`
- `emailFilename()`
- `emailPathSegments()`
- `matchedSegments()`
- `parts()`
- `remainingPath()`
- `removeFilenameExtension()`

### Dependencies

This file imports/requires:

- `./get-emails-directory-metadata`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 32

- `Boolean`
- `EmailsDirectory`
- `containsEmailPathSegments`
- `containsEmailTemplate`
- `directory`
- `directoryName`
- `emailFilename`
- `emailFilenames`
- `emailPathSegments`
- `emails`
- `filename`
- `filter`
- `get`
- `includes`
- `join`
- `length`
- `matchedSegments`
- `metadata`
- `parts`
- `relativeEmailPath`
- `relativeEmailSegments`
- `relativePath`
- `remainingPath`
- `removeFilenameExtension`
- `replace`
- `slice`
- `split`
- `startsWith`
- `string`
- `subDirectories`
- `subDirectory`
- `type`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

