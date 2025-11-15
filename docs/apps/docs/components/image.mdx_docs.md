# Documentation: image.mdx
**File Path:** `apps/docs/components/image.mdx`
**Language:** Unknown
**Size:** 1,563 bytes
**Lines:** 81
**Generated:** 2025-11-15T20:37:32.778230Z

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

- **Path:** `apps/docs/components/image.mdx`
- **Name:** `image.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,563 bytes (1.53 KB)
- **Lines of Code:** 81

---

## Original Source

```
---
title: "Image"
sidebarTitle: "Image"
description: "Display an image in your email."
"og:image": "https://react.email/static/covers/img.png"
icon: "image"
---

import Support from '/snippets/support.mdx'

## Install

Install component from your command line.

<CodeGroup>

```sh npm
npm install @react-email/components -E

# or get the individual package

npm install @react-email/img -E
```

```sh yarn
yarn add @react-email/components -E

# or get the individual package

yarn add @react-email/img -E
```

```sh pnpm
pnpm add @react-email/components -E

# or get the individual package

pnpm add @react-email/img -E
```

</CodeGroup>

## Getting started

Add the component to your email template. Include styles where needed.

```jsx
import { Img } from "@react-email/components";

const Email = () => {
  return <Img src="cat.jpg" alt="Cat" width="300" height="300" />;
};
```

<Tip>
  All email clients can display `.png`, `.gif`, and `.jpg` images.
  Unfortunately, `.svg` images are not well supported, regardless of how they're
  referenced, so avoid using these. See [Can I
  Email](https://www.caniemail.com/features/image-svg/) for more information.
</Tip>

## Props

<ResponseField name="alt" type="string">
  Alternate description for an image
</ResponseField>

<ResponseField name="src" type="string">
  The path to the image
</ResponseField>

<ResponseField name="width" type="string">
  The width of an image in pixels
</ResponseField>

<ResponseField name="height" type="string">
  The height of an image in pixels
</ResponseField>

<Support/>

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `/snippets/support.mdx`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 83

- `Add`
- `All`
- `Alternate`
- `Cat`
- `CodeGroup`
- `Display`
- `Email`
- `Getting`
- `Image`
- `Img`
- `Include`
- `Install`
- `Props`
- `ResponseField`
- `See`
- `Support`
- `Tip`
- `Unfortunately`
- `add`
- `alt`
- `avoid`
- `caniemail`
- `cat`
- `clients`
- `com`
- `command`
- `component`
- `components`
- `covers`
- `description`
- `display`
- `email`
- `features`
- `get`
- `gif`
- `height`
- `how`
- `https`
- `icon`
- `image`
- `images`
- `img`
- `individual`
- `information`
- `install`
- `jpg`
- `jsx`
- `line`
- `mdx`
- `more`
- `name`
- `needed`
- `npm`
- `package`
- `path`
- `pixels`
- `png`
- `pnpm`
- `react`
- `referenced`
- `regardless`
- `sidebarTitle`
- `snippets`
- `src`
- `started`
- `static`
- `string`
- `styles`
- `support`
- `supported`
- `svg`
- `template`
- `these`
- `they`
- `title`
- `type`
- `using`
- `well`
- `where`
- `width`
- `www`
- `yarn`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

