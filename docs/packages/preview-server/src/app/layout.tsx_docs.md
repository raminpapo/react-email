# Documentation: layout.tsx
**File Path:** `packages/preview-server/src/app/layout.tsx`
**Language:** tsx
**Size:** 1,293 bytes
**Lines:** 47
**Generated:** 2025-11-15T20:37:32.084505Z

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

- **Path:** `packages/preview-server/src/app/layout.tsx`
- **Name:** `layout.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,293 bytes (1.26 KB)
- **Lines of Code:** 47

---

## Original Source

```tsx
import './globals.css';

import type { Metadata } from 'next';
import { EmailsProvider } from '../contexts/emails';
import { getEmailsDirectoryMetadata } from '../utils/get-emails-directory-metadata';
import { emailsDirectoryAbsolutePath } from './env';
import { inter, sfMono } from './fonts';

export const metadata: Metadata = {
  title: 'React Email',
};

export const dynamic = 'force-dynamic';

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const emailsDirectoryMetadata = await getEmailsDirectoryMetadata(
    emailsDirectoryAbsolutePath,
  );

  if (typeof emailsDirectoryMetadata === 'undefined') {
    throw new Error(
      `Could not find the emails directory specified under ${emailsDirectoryAbsolutePath}!`,
    );
  }

  return (
    <html
      className={`${inter.variable} ${sfMono.variable} font-sans`}
      lang="en"
    >
      <body className="relative h-screen bg-black text-slate-11 leading-loose selection:bg-cyan-5 selection:text-cyan-12">
        <div className="bg-gradient-to-t from-slate-3 flex flex-col">
          <EmailsProvider
            initialEmailsDirectoryMetadata={emailsDirectoryMetadata}
          >
            {children}
          </EmailsProvider>
        </div>
      </body>
    </html>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `RootLayout()`
- `dynamic()`
- `emailsDirectoryMetadata()`

### Dependencies

This file imports/requires:

- `../contexts/emails`
- `../utils/get-emails-directory-metadata`
- `./env`
- `./fonts`
- `./globals.css`
- `next`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 52

- `Email`
- `EmailsProvider`
- `Error`
- `Metadata`
- `React`
- `ReactNode`
- `RootLayout`
- `black`
- `body`
- `children`
- `className`
- `col`
- `contexts`
- `css`
- `cyan`
- `directory`
- `div`
- `dynamic`
- `emails`
- `emailsDirectoryAbsolutePath`
- `emailsDirectoryMetadata`
- `env`
- `find`
- `flex`
- `font`
- `fonts`
- `force`
- `get`
- `getEmailsDirectoryMetadata`
- `globals`
- `gradient`
- `html`
- `initialEmailsDirectoryMetadata`
- `inter`
- `lang`
- `leading`
- `loose`
- `metadata`
- `next`
- `relative`
- `sans`
- `screen`
- `selection`
- `sfMono`
- `slate`
- `specified`
- `text`
- `title`
- `type`
- `under`
- `utils`
- `variable`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

