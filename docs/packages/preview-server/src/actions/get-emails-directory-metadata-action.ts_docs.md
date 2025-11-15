# Documentation: get-emails-directory-metadata-action.ts
**File Path:** `packages/preview-server/src/actions/get-emails-directory-metadata-action.ts`
**Language:** typescript
**Size:** 579 bytes
**Lines:** 20
**Generated:** 2025-11-15T20:37:31.781734Z

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

- **Path:** `packages/preview-server/src/actions/get-emails-directory-metadata-action.ts`
- **Name:** `get-emails-directory-metadata-action.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 579 bytes (0.57 KB)
- **Lines of Code:** 20

---

## Original Source

```typescript
'use server';

import type { EmailsDirectory } from '../utils/get-emails-directory-metadata';
import { getEmailsDirectoryMetadata } from '../utils/get-emails-directory-metadata';

export const getEmailsDirectoryMetadataAction = async (
  absolutePathToEmailsDirectory: string,
  keepFileExtensions = false,
  isSubDirectory = false,

  baseDirectoryPath = absolutePathToEmailsDirectory,
): Promise<EmailsDirectory | undefined> => {
  return getEmailsDirectoryMetadata(
    absolutePathToEmailsDirectory,
    keepFileExtensions,
    isSubDirectory,
    baseDirectoryPath,
  );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getEmailsDirectoryMetadataAction()`

### Dependencies

This file imports/requires:

- `../utils/get-emails-directory-metadata`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 17

- `EmailsDirectory`
- `Promise`
- `absolutePathToEmailsDirectory`
- `baseDirectoryPath`
- `directory`
- `emails`
- `get`
- `getEmailsDirectoryMetadata`
- `getEmailsDirectoryMetadataAction`
- `isSubDirectory`
- `keepFileExtensions`
- `metadata`
- `server`
- `string`
- `type`
- `use`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

