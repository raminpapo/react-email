# Documentation: button.mdx
**File Path:** `apps/docs/components/button.mdx`
**Language:** Unknown
**Size:** 1,457 bytes
**Lines:** 78
**Generated:** 2025-11-15T20:37:32.765070Z

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

- **Path:** `apps/docs/components/button.mdx`
- **Name:** `button.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,457 bytes (1.42 KB)
- **Lines of Code:** 78

---

## Original Source

```
---
title: "Button"
sidebarTitle: "Button"
description: "A link that is styled to look like a button."
"og:image": "https://react.email/static/covers/button.png"
icon: "b"
---

import Support from '/snippets/support.mdx'

<Info>
  Semantics: Quite often in the email world we talk about buttons, when actually
  we mean links. Behind the scenes this is a `<a>` tag, that is styled like a `<button>` tag.
</Info>

## Install

Install component from your command line.

<CodeGroup>

```sh npm
npm install @react-email/components -E

# or get the individual package

npm install @react-email/button -E
```

```sh yarn
yarn add @react-email/components -E

# or get the individual package

yarn add @react-email/button -E
```

```sh pnpm
pnpm add @react-email/components -E

# or get the individual package

pnpm add @react-email/button -E
```

</CodeGroup>

## Getting started

Add the component to your email template. Include styles where needed.

```jsx
import { Button } from "@react-email/components";

const Email = () => {
  return (
    <Button
      href="https://example.com"
      style={{ color: "#61dafb", padding: "10px 20px" }}
    >
      Click me
    </Button>
  );
};
```

## Props

<ResponseField name="href" type="string" required>
  Link to be triggered when the button is clicked
</ResponseField>

<ResponseField name="target" type="string" default="_blank">
  Specify the target attribute for the button link
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

**Total Unique Identifiers:** 81

- `Add`
- `Behind`
- `Button`
- `Click`
- `CodeGroup`
- `Email`
- `Getting`
- `Include`
- `Info`
- `Install`
- `Link`
- `Props`
- `Quite`
- `ResponseField`
- `Semantics`
- `Specify`
- `Support`
- `_blank`
- `about`
- `actually`
- `add`
- `attribute`
- `button`
- `buttons`
- `clicked`
- `color`
- `com`
- `command`
- `component`
- `components`
- `covers`
- `description`
- `email`
- `example`
- `get`
- `href`
- `https`
- `icon`
- `image`
- `individual`
- `install`
- `jsx`
- `like`
- `line`
- `link`
- `links`
- `look`
- `mdx`
- `mean`
- `name`
- `needed`
- `npm`
- `often`
- `package`
- `padding`
- `png`
- `pnpm`
- `react`
- `required`
- `scenes`
- `sidebarTitle`
- `snippets`
- `started`
- `static`
- `string`
- `style`
- `styled`
- `styles`
- `support`
- `tag`
- `talk`
- `target`
- `template`
- `title`
- `triggered`
- `type`
- `when`
- `where`
- `world`
- `yarn`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

