# Documentation: env.ts
**File Path:** `packages/preview-server/src/app/env.ts`
**Language:** typescript
**Size:** 610 bytes
**Lines:** 18
**Generated:** 2025-11-15T20:37:32.081332Z

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

- **Path:** `packages/preview-server/src/app/env.ts`
- **Name:** `env.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 610 bytes (0.60 KB)
- **Lines of Code:** 18

---

## Original Source

```typescript
/** ONLY ACCESSIBLE ON THE SERVER */
export const userProjectLocation = process.env.USER_PROJECT_LOCATION!;

/** ONLY ACCESSIBLE ON THE SERVER */
export const previewServerLocation = process.env.PREVIEW_SERVER_LOCATION!;

/** ONLY ACCESSIBLE ON THE SERVER */
export const emailsDirectoryAbsolutePath =
  process.env.EMAILS_DIR_ABSOLUTE_PATH!;

/** ONLY ACCESSIBLE ON THE SERVER */
export const resendApiKey = process.env.RESEND_API_KEY;

export const isBuilding = process.env.NEXT_PUBLIC_IS_BUILDING === 'true';

export const isPreviewDevelopment =
  process.env.NEXT_PUBLIC_IS_PREVIEW_DEVELOPMENT === 'true';

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `emailsDirectoryAbsolutePath()`
- `isBuilding()`
- `isPreviewDevelopment()`
- `previewServerLocation()`
- `resendApiKey()`
- `userProjectLocation()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 14

- `EMAILS_DIR_ABSOLUTE_PATH`
- `NEXT_PUBLIC_IS_BUILDING`
- `NEXT_PUBLIC_IS_PREVIEW_DEVELOPMENT`
- `PREVIEW_SERVER_LOCATION`
- `RESEND_API_KEY`
- `USER_PROJECT_LOCATION`
- `emailsDirectoryAbsolutePath`
- `env`
- `isBuilding`
- `isPreviewDevelopment`
- `previewServerLocation`
- `process`
- `resendApiKey`
- `userProjectLocation`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

