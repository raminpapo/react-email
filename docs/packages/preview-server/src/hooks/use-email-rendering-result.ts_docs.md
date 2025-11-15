# Documentation: use-email-rendering-result.ts
**File Path:** `packages/preview-server/src/hooks/use-email-rendering-result.ts`
**Language:** typescript
**Size:** 1,763 bytes
**Lines:** 59
**Generated:** 2025-11-15T20:37:32.003731Z

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

- **Path:** `packages/preview-server/src/hooks/use-email-rendering-result.ts`
- **Name:** `use-email-rendering-result.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,763 bytes (1.72 KB)
- **Lines of Code:** 59

---

## Original Source

```typescript
import { useState } from 'react';
import { getEmailPathFromSlug } from '../actions/get-email-path-from-slug';
import {
  type EmailRenderingResult,
  renderEmailByPath,
} from '../actions/render-email-by-path';
import { isBuilding, isPreviewDevelopment } from '../app/env';
import { useEmails } from '../contexts/emails';
import { containsEmailTemplate } from '../utils/contains-email-template';
import { useHotreload } from './use-hot-reload';

export const useEmailRenderingResult = (
  emailPath: string,
  serverEmailRenderedResult: EmailRenderingResult,
) => {
  const [renderingResult, setRenderingResult] = useState(
    serverEmailRenderedResult,
  );

  const { emailsDirectoryMetadata } = useEmails();

  if (!isBuilding && !isPreviewDevelopment) {
    // biome-ignore lint/correctness/useHookAtTopLevel: This is fine since isBuilding does not change at runtime
    useHotreload(async (changes) => {
      for await (const change of changes) {
        const relativePathForChangedFile =
          // ex: apple-receipt.tsx
          // it will be the path relative to the emails directory, so it is already
          // going to be equivalent to the slug
          change.filename;

        if (
          !containsEmailTemplate(
            relativePathForChangedFile,
            emailsDirectoryMetadata,
          )
        ) {
          continue;
        }

        const pathForChangedEmail = await getEmailPathFromSlug(
          relativePathForChangedFile,
        );

        const newRenderingResult = await renderEmailByPath(
          pathForChangedEmail,
          true,
        );

        if (pathForChangedEmail === emailPath) {
          setRenderingResult(newRenderingResult);
        }
      }
    });
  }

  return renderingResult;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `newRenderingResult()`
- `pathForChangedEmail()`
- `relativePathForChangedFile()`
- `useEmailRenderingResult()`

### Type Definitions

- `EmailRenderingResult`

### Dependencies

This file imports/requires:

- `../actions/get-email-path-from-slug`
- `../actions/render-email-by-path`
- `../app/env`
- `../contexts/emails`
- `../utils/contains-email-template`
- `./use-hot-reload`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 56

- `EmailRenderingResult`
- `actions`
- `already`
- `app`
- `apple`
- `biome`
- `change`
- `changes`
- `contains`
- `containsEmailTemplate`
- `contexts`
- `correctness`
- `directory`
- `email`
- `emailPath`
- `emails`
- `emailsDirectoryMetadata`
- `env`
- `equivalent`
- `filename`
- `fine`
- `get`
- `getEmailPathFromSlug`
- `going`
- `hot`
- `ignore`
- `isBuilding`
- `isPreviewDevelopment`
- `lint`
- `newRenderingResult`
- `path`
- `pathForChangedEmail`
- `react`
- `receipt`
- `relative`
- `relativePathForChangedFile`
- `reload`
- `render`
- `renderEmailByPath`
- `renderingResult`
- `runtime`
- `serverEmailRenderedResult`
- `setRenderingResult`
- `since`
- `slug`
- `string`
- `template`
- `tsx`
- `type`
- `use`
- `useEmailRenderingResult`
- `useEmails`
- `useHookAtTopLevel`
- `useHotreload`
- `useState`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

