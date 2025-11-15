# Documentation: emails.tsx
**File Path:** `packages/preview-server/src/contexts/emails.tsx`
**Language:** tsx
**Size:** 1,728 bytes
**Lines:** 57
**Generated:** 2025-11-15T20:37:32.097632Z

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

- **Path:** `packages/preview-server/src/contexts/emails.tsx`
- **Name:** `emails.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,728 bytes (1.69 KB)
- **Lines of Code:** 57

---

## Original Source

```tsx
'use client';

import { createContext, useContext, useState } from 'react';
import { getEmailsDirectoryMetadataAction } from '../actions/get-emails-directory-metadata-action';
import { isBuilding, isPreviewDevelopment } from '../app/env';
import { useHotreload } from '../hooks/use-hot-reload';
import type { EmailsDirectory } from '../utils/get-emails-directory-metadata';

const EmailsContext = createContext<
  | {
      emailsDirectoryMetadata: EmailsDirectory;
    }
  | undefined
>(undefined);

export const useEmails = () => {
  const providerValue = useContext(EmailsContext);

  if (typeof providerValue === 'undefined') {
    throw new Error(
      'Cannot call `useEmails` outside of an `EmailsContext` provider.',
    );
  }

  return providerValue;
};

export const EmailsProvider = (props: {
  initialEmailsDirectoryMetadata: EmailsDirectory;
  children: React.ReactNode;
}) => {
  const [emailsDirectoryMetadata, setEmailsDirectoryMetadata] =
    useState<EmailsDirectory>(props.initialEmailsDirectoryMetadata);

  if (!isBuilding && !isPreviewDevelopment) {
    // biome-ignore lint/correctness/useHookAtTopLevel: this will not change on runtime so it doesn't violate the rules of hooks
    useHotreload(async () => {
      const metadata = await getEmailsDirectoryMetadataAction(
        props.initialEmailsDirectoryMetadata.absolutePath,
      );
      if (metadata) {
        setEmailsDirectoryMetadata(metadata);
      } else {
        throw new Error(
          'Hot reloading: unable to find the emails directory to update the sidebar',
        );
      }
    });
  }

  return (
    <EmailsContext.Provider value={{ emailsDirectoryMetadata }}>
      {props.children}
    </EmailsContext.Provider>
  );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `EmailsContext()`
- `EmailsProvider()`
- `metadata()`
- `providerValue()`
- `useEmails()`

### Dependencies

This file imports/requires:

- `../actions/get-emails-directory-metadata-action`
- `../app/env`
- `../hooks/use-hot-reload`
- `../utils/get-emails-directory-metadata`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 59

- `Cannot`
- `EmailsContext`
- `EmailsDirectory`
- `EmailsProvider`
- `Error`
- `Hot`
- `Provider`
- `React`
- `ReactNode`
- `absolutePath`
- `action`
- `actions`
- `app`
- `biome`
- `call`
- `change`
- `children`
- `client`
- `correctness`
- `createContext`
- `directory`
- `doesn`
- `emails`
- `emailsDirectoryMetadata`
- `env`
- `find`
- `get`
- `getEmailsDirectoryMetadataAction`
- `hooks`
- `hot`
- `ignore`
- `initialEmailsDirectoryMetadata`
- `isBuilding`
- `isPreviewDevelopment`
- `lint`
- `metadata`
- `outside`
- `props`
- `provider`
- `providerValue`
- `react`
- `reload`
- `reloading`
- `rules`
- `runtime`
- `setEmailsDirectoryMetadata`
- `sidebar`
- `type`
- `unable`
- `update`
- `use`
- `useContext`
- `useEmails`
- `useHookAtTopLevel`
- `useHotreload`
- `useState`
- `utils`
- `value`
- `violate`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

