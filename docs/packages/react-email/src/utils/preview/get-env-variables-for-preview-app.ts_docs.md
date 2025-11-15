# Documentation: get-env-variables-for-preview-app.ts
**File Path:** `packages/react-email/src/utils/preview/get-env-variables-for-preview-app.ts`
**Language:** typescript
**Size:** 485 bytes
**Lines:** 17
**Generated:** 2025-11-15T20:37:32.545412Z

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

- **Path:** `packages/react-email/src/utils/preview/get-env-variables-for-preview-app.ts`
- **Name:** `get-env-variables-for-preview-app.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 485 bytes (0.47 KB)
- **Lines of Code:** 17

---

## Original Source

```typescript
import path from 'node:path';

export const getEnvVariablesForPreviewApp = (
  relativePathToEmailsDirectory: string,
  previewServerLocation: string,
  cwd: string,
  resendApiKey?: string,
) => {
  return {
    EMAILS_DIR_RELATIVE_PATH: relativePathToEmailsDirectory,
    EMAILS_DIR_ABSOLUTE_PATH: path.resolve(cwd, relativePathToEmailsDirectory),
    PREVIEW_SERVER_LOCATION: previewServerLocation,
    USER_PROJECT_LOCATION: cwd,
    RESEND_API_KEY: resendApiKey,
  } as const;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getEnvVariablesForPreviewApp()`

### Dependencies

This file imports/requires:

- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 14

- `EMAILS_DIR_ABSOLUTE_PATH`
- `EMAILS_DIR_RELATIVE_PATH`
- `PREVIEW_SERVER_LOCATION`
- `RESEND_API_KEY`
- `USER_PROJECT_LOCATION`
- `cwd`
- `getEnvVariablesForPreviewApp`
- `node`
- `path`
- `previewServerLocation`
- `relativePathToEmailsDirectory`
- `resendApiKey`
- `resolve`
- `string`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

