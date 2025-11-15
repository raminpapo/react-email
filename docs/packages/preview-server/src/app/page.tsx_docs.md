# Documentation: page.tsx
**File Path:** `packages/preview-server/src/app/page.tsx`
**Language:** tsx
**Size:** 1,537 bytes
**Lines:** 45
**Generated:** 2025-11-15T20:37:32.085787Z

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

- **Path:** `packages/preview-server/src/app/page.tsx`
- **Name:** `page.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,537 bytes (1.50 KB)
- **Lines of Code:** 45

---

## Original Source

```tsx
import path from 'node:path';
import Image from 'next/image';
import Link from 'next/link';
import { Button, Heading, Text } from '../components';
import CodeSnippet from '../components/code-snippet';
import { Shell } from '../components/shell';
import { emailsDirectoryAbsolutePath } from './env';
import logo from './logo.png';

export default function Home() {
  const baseEmailsDirectoryName = path.basename(emailsDirectoryAbsolutePath);

  return (
    <Shell>
      <div className="w-full h-full flex items-center justify-center p-8">
        <div className="-mt-10 relative max-w-lg flex flex-col items-center gap-3 text-center">
          <Image
            alt="React Email Icon"
            className="mb-8"
            height={144}
            src={logo}
            style={{
              borderRadius: 34,
              boxShadow: '0 .625rem 12.5rem 1.25rem #2B7CA080',
            }}
            width={141}
          />
          <Heading as="h2" size="6" weight="medium">
            Welcome to React Email
          </Heading>
          <Text as="p">
            To start developing your emails, you can create a<br />
            <CodeSnippet>.jsx</CodeSnippet> or <CodeSnippet>.tsx</CodeSnippet>{' '}
            file under your <CodeSnippet>{baseEmailsDirectoryName}</CodeSnippet>{' '}
            folder.
          </Text>
          <Button asChild className="mt-3" size="3">
            <Link href="https://react.email/docs">Check the docs</Link>
          </Button>
        </div>
      </div>
    </Shell>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Home()`
- `baseEmailsDirectoryName()`

### Dependencies

This file imports/requires:

- `../components`
- `../components/code-snippet`
- `../components/shell`
- `./env`
- `./logo.png`
- `next/image`
- `next/link`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 67

- `Button`
- `Check`
- `CodeSnippet`
- `Email`
- `Heading`
- `Home`
- `Icon`
- `Image`
- `Link`
- `React`
- `Shell`
- `Text`
- `Welcome`
- `alt`
- `asChild`
- `baseEmailsDirectoryName`
- `basename`
- `borderRadius`
- `boxShadow`
- `center`
- `className`
- `code`
- `col`
- `components`
- `create`
- `developing`
- `div`
- `docs`
- `email`
- `emails`
- `emailsDirectoryAbsolutePath`
- `env`
- `file`
- `flex`
- `folder`
- `full`
- `gap`
- `height`
- `href`
- `https`
- `image`
- `items`
- `jsx`
- `justify`
- `link`
- `logo`
- `max`
- `medium`
- `next`
- `node`
- `path`
- `png`
- `react`
- `relative`
- `shell`
- `size`
- `snippet`
- `src`
- `start`
- `style`
- `text`
- `tsx`
- `under`
- `weight`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

