# Documentation: heading.mdx
**File Path:** `apps/docs/components/heading.mdx`
**Language:** Unknown
**Size:** 1,791 bytes
**Lines:** 90
**Generated:** 2025-11-15T20:37:32.774547Z

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

- **Path:** `apps/docs/components/heading.mdx`
- **Name:** `heading.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,791 bytes (1.75 KB)
- **Lines of Code:** 90

---

## Original Source

```
---
title: "Heading"
sidebarTitle: "Heading"
description: "A block of heading text."
"og:image": "https://react.email/static/covers/heading.png"
icon: "h1"
---

import Support from '/snippets/support.mdx'

## Install

Install component from your command line.

<CodeGroup>

```sh npm
npm install @react-email/components -E

# or get the individual package

npm install @react-email/heading -E
```

```sh yarn
yarn add @react-email/components -E

# or get the individual package

yarn add @react-email/heading -E
```

```sh pnpm
pnpm add @react-email/components -E

# or get the individual package

pnpm add @react-email/heading -E
```

</CodeGroup>

## Getting started

Add the component to your email template. Include styles where needed.

```jsx
import { Heading } from "@react-email/components";

const Email = () => {
  return <Heading as="h2">Lorem ipsum</Heading>;
};
```

## Props

<ResponseField name="as" type="string" default="h1">
  Render component as `h1`, `h2`, `h3`, `h4`, `h5` or `h6`.
</ResponseField>

<ResponseField name="m" type="string">
  A shortcut for `margin` CSS property.
</ResponseField>

<ResponseField name="mx" type="string">
  A shortcut for `margin-left` and `margin-right` CSS properties.
</ResponseField>

<ResponseField name="my" type="string">
  A shortcut for `margin-top` and `margin-bottom` CSS properties.
</ResponseField>

<ResponseField name="mt" type="string">
  A shortcut for `margin-top` CSS property.
</ResponseField>

<ResponseField name="mr" type="string">
  A shortcut for `margin-right` CSS property.
</ResponseField>

<ResponseField name="mb" type="string">
  A shortcut for `margin-bottom` CSS property.
</ResponseField>

<ResponseField name="ml" type="string">
  A shortcut for `margin-left` CSS property.
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

**Total Unique Identifiers:** 60

- `Add`
- `CodeGroup`
- `Email`
- `Getting`
- `Heading`
- `Include`
- `Install`
- `Lorem`
- `Props`
- `Render`
- `ResponseField`
- `Support`
- `add`
- `block`
- `bottom`
- `command`
- `component`
- `components`
- `covers`
- `description`
- `email`
- `get`
- `heading`
- `https`
- `icon`
- `image`
- `individual`
- `install`
- `ipsum`
- `jsx`
- `left`
- `line`
- `margin`
- `mdx`
- `name`
- `needed`
- `npm`
- `package`
- `png`
- `pnpm`
- `properties`
- `property`
- `react`
- `right`
- `shortcut`
- `sidebarTitle`
- `snippets`
- `started`
- `static`
- `string`
- `styles`
- `support`
- `template`
- `text`
- `title`
- `top`
- `type`
- `where`
- `yarn`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

