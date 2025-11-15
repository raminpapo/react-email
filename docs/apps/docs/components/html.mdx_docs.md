# Documentation: html.mdx
**File Path:** `apps/docs/components/html.mdx`
**Language:** Unknown
**Size:** 1,275 bytes
**Lines:** 71
**Generated:** 2025-11-15T20:37:32.776976Z

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

- **Path:** `apps/docs/components/html.mdx`
- **Name:** `html.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,275 bytes (1.25 KB)
- **Lines of Code:** 71

---

## Original Source

```
---
title: "HTML"
sidebarTitle: "HTML"
description: "A React html component to wrap emails."
"og:image": "https://react.email/static/covers/html.png"
icon: "file-code"
---

import Support from '/snippets/support.mdx'

## Install

Install component from your command line.

<CodeGroup>

```sh npm
npm install @react-email/components -E

# or get the individual package

npm install @react-email/html -E
```

```sh yarn
yarn add @react-email/components -E

# or get the individual package

yarn add @react-email/html -E
```

```sh pnpm
pnpm add @react-email/components -E

# or get the individual package

pnpm add @react-email/html -E
```

</CodeGroup>

## Getting started

Add the component to your email template. Include styles where needed.

```jsx
import { Html, Button } from "@react-email/components";

const Email = () => {
  return (
    <Html lang="en" dir="ltr">
      <Button href="https://example.com" style={{ color: "#61dafb" }}>
        Click me
      </Button>
    </Html>
  );
};
```

## Props

<ResponseField name="lang" type="string" default="en">
  Identify the language of text content on the email
</ResponseField>
<ResponseField name="dir" type="string" default="ltr">
  Identify the direction of text content on the email
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

**Total Unique Identifiers:** 67

- `Add`
- `Button`
- `Click`
- `CodeGroup`
- `Email`
- `Getting`
- `Html`
- `Identify`
- `Include`
- `Install`
- `Props`
- `React`
- `ResponseField`
- `Support`
- `add`
- `code`
- `color`
- `com`
- `command`
- `component`
- `components`
- `content`
- `covers`
- `description`
- `dir`
- `direction`
- `email`
- `emails`
- `example`
- `file`
- `get`
- `href`
- `html`
- `https`
- `icon`
- `image`
- `individual`
- `install`
- `jsx`
- `lang`
- `language`
- `line`
- `ltr`
- `mdx`
- `name`
- `needed`
- `npm`
- `package`
- `png`
- `pnpm`
- `react`
- `sidebarTitle`
- `snippets`
- `started`
- `static`
- `string`
- `style`
- `styles`
- `support`
- `template`
- `text`
- `title`
- `type`
- `where`
- `wrap`
- `yarn`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

