# Documentation: font.mdx
**File Path:** `apps/docs/components/font.mdx`
**Language:** Unknown
**Size:** 2,235 bytes
**Lines:** 97
**Generated:** 2025-11-15T20:37:32.772041Z

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

- **Path:** `apps/docs/components/font.mdx`
- **Name:** `font.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 2,235 bytes (2.18 KB)
- **Lines of Code:** 97

---

## Original Source

```
---
title: "Font"
sidebarTitle: "Font"
description: "A React Font component to set your fonts."
"og:image": "https://react.email/static/covers/font.png"
icon: "book-font"
---

import Support from '/snippets/support.mdx'

## Install

Install component from your command line.

<CodeGroup>

```sh npm
npm install @react-email/components -E

# or get the individual package

npm install @react-email/font -E
```

```sh yarn
yarn add @react-email/components -E

# or get the individual package

yarn add @react-email/font -E
```

```sh pnpm
pnpm add @react-email/components -E

# or get the individual package

pnpm add @react-email/font -E
```

</CodeGroup>

## Getting started

Add the component to your email template. This applies your font to all tags inside your email.
Note, that not all email clients supports web fonts, this is why it is important to configure your `fallbackFontFamily`.
To view all email clients that supports web fonts [see](https://www.caniemail.com/features/css-at-font-face/)

```jsx
import { Font, Head, Html } from "@react-email/components";

const Email = () => {
  return (
    <Html lang="en">
      <Head>
        <Font
          fontFamily="Roboto"
          fallbackFontFamily="Verdana"
          webFont={{
            url: "https://fonts.gstatic.com/s/roboto/v27/KFOmCnqEu92Fr1Mu4mxKKTU1Kg.woff2",
            format: "woff2",
          }}
          fontWeight={400}
          fontStyle="normal"
        />
      </Head>
    </Html>
  );
};
```

## Props

<ResponseField name="fontFamily" type="string">
  The font family you want to use. If the webFont property is configured, this
  should contain the name of that font
</ResponseField>

<ResponseField name="fallbackFontFamily" type="string">
  The fallback font family the system should you, if web fonts are not supported
  or the chosen font is not installed on the system.
</ResponseField>

<ResponseField name="webFont" type="{url: string, format: string} | undefined">
  The webFont the supported email client should use
</ResponseField>

<ResponseField name="fontWeight" type="number | string">
  The weight of the font
</ResponseField>

<ResponseField name="fontStyle" type="string">
  The style of the font
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

**Total Unique Identifiers:** 100

- `Add`
- `CodeGroup`
- `Email`
- `Font`
- `Getting`
- `Head`
- `Html`
- `Install`
- `KFOmCnqEu92Fr1Mu4mxKKTU1Kg`
- `Note`
- `Props`
- `React`
- `ResponseField`
- `Roboto`
- `Support`
- `Verdana`
- `add`
- `all`
- `applies`
- `book`
- `caniemail`
- `chosen`
- `client`
- `clients`
- `com`
- `command`
- `component`
- `components`
- `configure`
- `configured`
- `contain`
- `covers`
- `css`
- `description`
- `email`
- `face`
- `fallback`
- `fallbackFontFamily`
- `family`
- `features`
- `font`
- `fontFamily`
- `fontStyle`
- `fontWeight`
- `fonts`
- `format`
- `get`
- `gstatic`
- `https`
- `icon`
- `image`
- `important`
- `individual`
- `inside`
- `install`
- `installed`
- `jsx`
- `lang`
- `line`
- `mdx`
- `name`
- `normal`
- `npm`
- `number`
- `package`
- `png`
- `pnpm`
- `property`
- `react`
- `roboto`
- `see`
- `set`
- `sidebarTitle`
- `snippets`
- `started`
- `static`
- `string`
- `style`
- `support`
- `supported`
- `supports`
- `system`
- `tags`
- `template`
- `title`
- `type`
- `url`
- `use`
- `v27`
- `view`
- `want`
- `web`
- `webFont`
- `weight`
- `why`
- `woff2`
- `www`
- `yarn`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

