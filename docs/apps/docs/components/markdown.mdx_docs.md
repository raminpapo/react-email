# Documentation: markdown.mdx
**File Path:** `apps/docs/components/markdown.mdx`
**Language:** Unknown
**Size:** 1,956 bytes
**Lines:** 89
**Generated:** 2025-11-15T20:37:32.780766Z

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

- **Path:** `apps/docs/components/markdown.mdx`
- **Name:** `markdown.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,956 bytes (1.91 KB)
- **Lines of Code:** 89

---

## Original Source

```
---
title: "Markdown"
sidebarTitle: "Markdown"
description: "A Markdown component that converts markdown to valid react-email template code"
"og:image": "https://react.email/static/covers/markdown.png"
icon: "file-code"
---

import Support from '/snippets/support.mdx'

## Install

Install component from your command line.

<CodeGroup>

```sh npm
npm install @react-email/components -E

# or get the individual package

npm install @react-email/markdown -E
```

```sh yarn
yarn add @react-email/components -E

# or get the individual package

yarn add @react-email/markdown -E
```

```sh pnpm
pnpm add @react-email/components -E

# or get the individual package

pnpm add @react-email/markdown -E
```

</CodeGroup>

## Getting started

Add the component to your email template. Include styles where needed.

```jsx
import { Markdown, Html } from "@react-email/components";

const Email = () => {
  return (
    <Html lang="en" dir="ltr">
      <Markdown
        markdownCustomStyles={{
          h1: { color: "red" },
          h2: { color: "blue" },
          codeInline: { background: "grey" },
        }}
        markdownContainerStyles={{
          padding: "12px",
          border: "solid 1px black",
        }}
      >{`# Hello, World!`}</Markdown>

      {/* OR */}

      <Markdown children={`# This is a ~~strikethrough~~`} />
    </Html>
  );
};
```

## Props

<ResponseField name="children" type="string">
  Contains the markdown content that will be rendered in the email template
</ResponseField>
<ResponseField name="markdownContainerStyles" type="object" default="{}">
  Provide custom styles for the containing div that wraps the markdown content
</ResponseField>
<ResponseField name="markdownCustomStyles" type="object" default="{}">
  Provide custom styles for the corresponding html element (p, h1, h2, etc.)
  <Info>
    Note: Passing a custom style for an element overrides the default styles.
  </Info>
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

**Total Unique Identifiers:** 89

- `Add`
- `CodeGroup`
- `Contains`
- `Email`
- `Getting`
- `Hello`
- `Html`
- `Include`
- `Info`
- `Install`
- `Markdown`
- `Note`
- `Passing`
- `Props`
- `Provide`
- `ResponseField`
- `Support`
- `World`
- `add`
- `background`
- `black`
- `blue`
- `border`
- `children`
- `code`
- `codeInline`
- `color`
- `command`
- `component`
- `components`
- `containing`
- `content`
- `converts`
- `corresponding`
- `covers`
- `custom`
- `description`
- `dir`
- `div`
- `element`
- `email`
- `etc`
- `file`
- `get`
- `grey`
- `html`
- `https`
- `icon`
- `image`
- `individual`
- `install`
- `jsx`
- `lang`
- `line`
- `ltr`
- `markdown`
- `markdownContainerStyles`
- `markdownCustomStyles`
- `mdx`
- `name`
- `needed`
- `npm`
- `object`
- `overrides`
- `package`
- `padding`
- `png`
- `pnpm`
- `react`
- `red`
- `rendered`
- `sidebarTitle`
- `snippets`
- `solid`
- `started`
- `static`
- `strikethrough`
- `string`
- `style`
- `styles`
- `support`
- `template`
- `title`
- `type`
- `valid`
- `where`
- `wraps`
- `yarn`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

