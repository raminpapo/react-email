# Documentation: template.tsx
**File Path:** `apps/web/src/components/template.tsx`
**Language:** tsx
**Size:** 2,075 bytes
**Lines:** 83
**Generated:** 2025-11-15T20:37:32.916590Z

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

- **Path:** `apps/web/src/components/template.tsx`
- **Name:** `template.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,075 bytes (2.03 KB)
- **Lines of Code:** 83

---

## Original Source

```tsx
'use client';

import classNames from 'classnames';
import type { ImageLoader } from 'next/image';
import Image from 'next/image';
import Link from 'next/link';
import * as React from 'react';
import { Heading } from './heading';
import { Text } from './text';

interface TemplateProps {
  path: string;
  name: string;
  className?: string;
  author: string;
}

const DEMO_EMAIL_PREVIEW_BASE_URL = 'https://demo.react.email/preview';
const DEFAULT_IMAGE = '/static/covers/react-email.png';

const imageLoader: ImageLoader = ({ src, width, quality }) => {
  return `${src}?w=${width}&q=${quality || 75}`;
};

export function Template({
  className,
  path,
  name,
  author,
  ...props
}: TemplateProps) {
  const emailName = path.split('/').pop();
  if (!path || !emailName) {
    throw new Error('Cannot have an empty path for an Example!');
  }

  const [imageSrc, setImageSrc] = React.useState(`/examples/${emailName}.png`);

  const handleImageError = () => {
    setImageSrc(DEFAULT_IMAGE);
  };

  return (
    <Link
      className={classNames(
        'flex w-full flex-col rounded-md border border-slate-6 bg-gradient backdrop-blur-[20px] focus:outline-none focus:ring-2',
        'hover:bg-gradientHover',
        'focus:bg-gradientHover focus:ring-white/20',
        className,
      )}
      href={`${DEMO_EMAIL_PREVIEW_BASE_URL}/${path}`}
      target="_blank"
      {...props}
    >
      <Image
        alt={name}
        className="rounded-t-md"
        height="300"
        loader={imageLoader}
        onError={handleImageError}
        priority
        src={imageSrc}
        width="450"
      />
      <div className="p-4">
        <Heading size="2" weight="medium">
          {name}
        </Heading>
        <div className="mt-2 flex flex-row gap-2">
          <Image
            alt={author}
            className="rounded-full text-ellipsis overflow-hidden"
            height="24"
            src={`/examples/authors/${author}.png`}
            width="24"
          />
          <Text>{author}</Text>
        </div>
      </div>
    </Link>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `DEFAULT_IMAGE()`
- `DEMO_EMAIL_PREVIEW_BASE_URL()`
- `Template()`
- `emailName()`
- `handleImageError()`

### Interfaces

- `TemplateProps`

### Dependencies

This file imports/requires:

- `./heading`
- `./text`
- `classnames`
- `next/image`
- `next/link`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 84

- `Cannot`
- `DEFAULT_IMAGE`
- `DEMO_EMAIL_PREVIEW_BASE_URL`
- `Error`
- `Example`
- `Heading`
- `Image`
- `ImageLoader`
- `Link`
- `React`
- `Template`
- `TemplateProps`
- `Text`
- `_blank`
- `alt`
- `author`
- `authors`
- `backdrop`
- `blur`
- `border`
- `className`
- `classNames`
- `classnames`
- `client`
- `col`
- `covers`
- `demo`
- `div`
- `ellipsis`
- `email`
- `emailName`
- `empty`
- `examples`
- `flex`
- `focus`
- `full`
- `gap`
- `gradient`
- `gradientHover`
- `handleImageError`
- `heading`
- `height`
- `hidden`
- `hover`
- `href`
- `https`
- `image`
- `imageLoader`
- `imageSrc`
- `interface`
- `link`
- `loader`
- `medium`
- `name`
- `next`
- `onError`
- `outline`
- `overflow`
- `path`
- `png`
- `pop`
- `preview`
- `priority`
- `props`
- `quality`
- `react`
- `ring`
- `rounded`
- `row`
- `setImageSrc`
- `size`
- `slate`
- `split`
- `src`
- `static`
- `string`
- `target`
- `text`
- `type`
- `use`
- `useState`
- `weight`
- `white`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

