# Documentation: link.mdx
**File Path:** `apps/docs/components/link.mdx`
**Language:** Unknown
**Size:** 1,194 bytes
**Lines:** 66
**Generated:** 2025-11-15T20:37:32.779488Z

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

- **Path:** `apps/docs/components/link.mdx`
- **Name:** `link.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,194 bytes (1.17 KB)
- **Lines of Code:** 66

---

## Original Source

```
---
title: "Link"
sidebarTitle: "Link"
description: "A hyperlink to web pages, email addresses, or anything else a URL can address."
"og:image": "https://react.email/static/covers/link.png"
icon: "link"
---

import Support from '/snippets/support.mdx'

## Install

Install component from your command line.

<CodeGroup>

```sh npm
npm install @react-email/components -E

# or get the individual package

npm install @react-email/link -E
```

```sh yarn
yarn add @react-email/components -E

# or get the individual package

yarn add @react-email/link -E
```

```sh pnpm
pnpm add @react-email/components -E

# or get the individual package

pnpm add @react-email/link -E
```

</CodeGroup>

## Getting started

Add the component to your email template. Include styles where needed.

```jsx
import { Link } from "@react-email/components";

const Email = () => {
  return <Link href="https://example.com">Example</Link>;
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

**Total Unique Identifiers:** 66

- `Add`
- `CodeGroup`
- `Email`
- `Example`
- `Getting`
- `Include`
- `Install`
- `Link`
- `Props`
- `ResponseField`
- `Specify`
- `Support`
- `_blank`
- `add`
- `address`
- `addresses`
- `anything`
- `attribute`
- `button`
- `clicked`
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
- `hyperlink`
- `icon`
- `image`
- `individual`
- `install`
- `jsx`
- `line`
- `link`
- `mdx`
- `name`
- `needed`
- `npm`
- `package`
- `pages`
- `png`
- `pnpm`
- `react`
- `required`
- `sidebarTitle`
- `snippets`
- `started`
- `static`
- `string`
- `styles`
- `support`
- `target`
- `template`
- `title`
- `triggered`
- `type`
- `web`
- `when`
- `where`
- `yarn`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

