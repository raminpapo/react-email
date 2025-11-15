# Documentation: readme.md
**File Path:** `packages/markdown/readme.md`
**Language:** markdown
**Size:** 3,703 bytes
**Lines:** 93
**Generated:** 2025-11-15T20:37:32.294675Z

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

- **Path:** `packages/markdown/readme.md`
- **Name:** `readme.md`
- **Extension:** `.md`
- **Language:** markdown
- **Size:** 3,703 bytes (3.62 KB)
- **Lines of Code:** 93

---

## Original Source

```markdown
![React Email Markdown cover](https://react.email/static/covers/markdown.png)

<div align="center"><strong>@react-email/markdown</strong></div>
<div align="center">Convert Markdown to valid React Email template code.</div>
<br />
<div align="center">
<a href="https://react.email">Website</a> 
<span> · </span>
<a href="https://react.email">Documentation</a> 
<span> · </span>
<a href="https://react.email">Twitter</a>
</div>

## Install

Install component from your command line.

#### With yarn

```sh
yarn add @react-email/markdown -E
```

#### With npm

```sh
npm install @react-email/markdown -E
```

## Getting started

Add the component around your email body content.

```jsx
import { Markdown } from "@react-email/markdown";
import { Html } from "@react-email/html";

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
```

## Props

### `children` field

- **Type**: string

Contains the markdown content that will be rendered in the email template.

### `markdownCustomStyles` field

- **Type**: object
- **Default**: `{}`

Provide custom styles for the corresponding HTML element (e.g., p, h1, h2, etc.).

### `markdownContainerStyles` field

- **Type**: object
- **Default**: `{}`

Provide custom styles for the containing `div` that wraps the markdown content.

## Support

This component was tested using the most popular email clients.

| <img src="https://react.email/static/icons/gmail.svg" width="48px" height="48px" alt="Gmail logo"> | <img src="https://react.email/static/icons/apple-mail.svg" width="48px" height="48px" alt="Apple Mail"> | <img src="https://react.email/static/icons/outlook.svg" width="48px" height="48px" alt="Outlook logo"> | <img src="https://react.email/static/icons/yahoo-mail.svg" width="48px" height="48px" alt="Yahoo! Mail logo"> | <img src="https://react.email/static/icons/hey.svg" width="48px" height="48px" alt="HEY logo"> | <img src="https://react.email/static/icons/superhuman.svg" width="48px" height="48px" alt="Superhuman logo"> |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Gmail ✔                                                                                           | Apple Mail ✔                                                                                           | Outlook ✔                                                                                             | Yahoo! Mail ✔                                                                                                | HEY ✔                                                                                         | Superhuman ✔                                                                                                |

## License

MIT License

```

---

## Overview

This is a Markdown documentation file. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `@react-email/html`
- `@react-email/markdown`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 104

- `Add`
- `Apple`
- `Contains`
- `Convert`
- `Documentation`
- `Email`
- `Getting`
- `Gmail`
- `Hello`
- `Html`
- `Install`
- `License`
- `Mail`
- `Markdown`
- `Outlook`
- `Props`
- `Provide`
- `React`
- `Superhuman`
- `Support`
- `Twitter`
- `Type`
- `Website`
- `World`
- `Yahoo`
- `add`
- `align`
- `alt`
- `apple`
- `around`
- `background`
- `black`
- `blue`
- `body`
- `border`
- `center`
- `children`
- `clients`
- `code`
- `codeInline`
- `color`
- `command`
- `component`
- `containing`
- `content`
- `corresponding`
- `cover`
- `covers`
- `custom`
- `dir`
- `div`
- `element`
- `email`
- `etc`
- `field`
- `gmail`
- `grey`
- `height`
- `hey`
- `href`
- `html`
- `https`
- `icons`
- `img`
- `install`
- `jsx`
- `lang`
- `line`
- `logo`
- `ltr`
- `mail`
- `markdown`
- `markdownContainerStyles`
- `markdownCustomStyles`
- `most`
- `npm`
- `object`
- `outlook`
- `padding`
- `png`
- `popular`
- `react`
- `red`
- `rendered`
- `solid`
- `span`
- `src`
- `started`
- `static`
- `strikethrough`
- `string`
- `strong`
- `styles`
- `superhuman`
- `svg`
- `template`
- `tested`
- `using`
- `valid`
- `width`
- `wraps`
- `yahoo`
- `yarn`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

