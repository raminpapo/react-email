# Documentation: render.mdx
**File Path:** `apps/docs/utilities/render.mdx`
**Language:** Unknown
**Size:** 4,123 bytes
**Lines:** 141
**Generated:** 2025-11-15T20:37:32.763296Z

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

- **Path:** `apps/docs/utilities/render.mdx`
- **Name:** `render.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 4,123 bytes (4.03 KB)
- **Lines of Code:** 141

---

## Original Source

```
---
title: 'Render'
sidebarTitle: 'Render'
description: 'Transform React components into HTML email templates.'
'og:image': 'https://react.email/static/covers/render.png'
---

## 1. Install dependencies

Install package from your command line.

<CodeGroup>

```sh npm
npm install @react-email/render -E
```

```sh yarn
yarn add @react-email/render -E
```

```sh pnpm
pnpm add @react-email/render -E
```

</CodeGroup>

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```jsx email.jsx
import * as React from 'react';
import { Html, Button, Hr, Text } from "@react-email/components";

export function MyTemplate(props) {
  return (
    <Html lang="en">
      <Text>Some title</Text>
      <Hr />
      <Button href="https://example.com">Click me</Button>
    </Html>
  );
}

export default MyTemplate;
```

## 3. Convert to HTML

Import an existing React component and convert into a HTML string.

<Info>You can use the `pretty` function to beautify the output.</Info>

```jsx
import { MyTemplate } from './email';
import { render, pretty } from '@react-email/render';

const html = await pretty(await render(<MyTemplate />));

console.log(html);
```

This will generate the following output:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en">
  <p style="font-size:14px;line-height:24px;margin:16px 0">Some title</p>
  <hr style="width:100%;border:none;border-top:1px solid #eaeaea" />
  <a href="https://example.com" target="_blank" style="line-height:100%;text-decoration:none;display:inline-block;max-width:100%;padding:0px 0px">
    <span>
      <!--[if mso]>
        <i style="letter-spacing: undefinedpx;mso-font-width:-100%;mso-text-raise:0" hidden>&nbsp;</i>
      <![endif]-->
    </span>
    <span style="max-width:100%;display:inline-block;line-height:120%;text-decoration:none;text-transform:none;mso-padding-alt:0px;mso-text-raise:0">Click me</span>
    <span>
      <!--[if mso]>
        <i style="letter-spacing: undefinedpx;mso-font-width:-100%" hidden>&nbsp;</i>
      <![endif]-->
    </span>
  </a>
</html>
```

<Danger>
    When running in the browser, to properly support Safari and browsers running on iOS, you will
    need to polyfill the [ReadableByteStreamController API](https://developer.mozilla.org/en-US/docs/Web/API/ReadableByteStreamController#browser_compatibility).

    We recommend [npm i web-streams-polyfill](https://www.npmjs.com/package/web-streams-polyfill). It can be applied as follows in some sort of root file for your website:

    ```jsx
    import "web-streams-polyfill/polyfill";
    ```
</Danger>

## 4. Convert to Plain Text

Plain text versions of emails are important because they ensure that the message can be read by the recipient even if they are unable to view the HTML version of the email.

This is important because not all email clients and devices can display HTML email, and some recipients may have chosen to disable HTML email for security or accessibility reasons.

Here's how to convert a React component into plain text.

<Warning>
The `plainText` option in the `render` function is deprecated since [@react-email/render@1.2.0](https://github.com/resend/react-email/releases/tag/%40react-email%2Frender%401.2.0). Use the `toPlainText` function instead.
</Warning>

```jsx
import { MyTemplate } from './email';
import { toPlainText, render } from '@react-email/render';

const html = await render(<MyTemplate />);
const text = toPlainText(html);

console.log(text);
```

This will generate the following output:

```
Some title

---

Click me [https://example.com]
```

## Options

<ResponseField name="pretty" type="boolean" deprecated>
  Beautify HTML output
</ResponseField>
<ResponseField name="plainText" type="boolean" deprecated>
  Generate plain text version
</ResponseField>
<ResponseField name="htmlToTextOptions" type="HtmlToTextOptions">
  `html-to-text` [options](https://github.com/html-to-text/node-html-to-text/tree/master/packages/html-to-text#options) used for rendering
</ResponseField>

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `./email`
- `@react-email/components`
- `@react-email/render`
- `react`
- `web-streams-polyfill/polyfill`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 184

- `Beautify`
- `Button`
- `Click`
- `CodeGroup`
- `Convert`
- `Create`
- `Danger`
- `Generate`
- `Here`
- `Html`
- `HtmlToTextOptions`
- `Info`
- `Install`
- `MyTemplate`
- `Options`
- `Plain`
- `React`
- `ReadableByteStreamController`
- `Render`
- `ResponseField`
- `Safari`
- `Some`
- `Start`
- `Text`
- `Transform`
- `Transitional`
- `Use`
- `W3C`
- `Warning`
- `Web`
- `When`
- `You`
- `_blank`
- `accessibility`
- `add`
- `all`
- `alt`
- `applied`
- `beautify`
- `because`
- `block`
- `boolean`
- `border`
- `browser`
- `browser_compatibility`
- `browsers`
- `building`
- `chosen`
- `clients`
- `com`
- `command`
- `component`
- `components`
- `console`
- `convert`
- `covers`
- `decoration`
- `dependencies`
- `deprecated`
- `description`
- `developer`
- `devices`
- `disable`
- `display`
- `docs`
- `dtd`
- `eaeaea`
- `email`
- `emails`
- `endif`
- `ensure`
- `even`
- `example`
- `existing`
- `file`
- `following`
- `follows`
- `font`
- `generate`
- `github`
- `height`
- `hidden`
- `how`
- `href`
- `html`
- `htmlToTextOptions`
- `http`
- `https`
- `iOS`
- `image`
- `important`
- `inline`
- `install`
- `instead`
- `into`
- `jsx`
- `lang`
- `letter`
- `line`
- `log`
- `margin`
- `master`
- `max`
- `message`
- `mozilla`
- `mso`
- `name`
- `nbsp`
- `need`
- `node`
- `npm`
- `npmjs`
- `option`
- `options`
- `org`
- `output`
- `package`
- `packages`
- `padding`
- `plain`
- `plainText`
- `png`
- `pnpm`
- `polyfill`
- `pretty`
- `properly`
- `props`
- `raise`
- `react`
- `read`
- `reasons`
- `recipient`
- `recipients`
- `recommend`
- `releases`
- `render`
- `rendering`
- `resend`
- `root`
- `running`
- `security`
- `sidebarTitle`
- `since`
- `size`
- `solid`
- `some`
- `sort`
- `spacing`
- `span`
- `static`
- `streams`
- `string`
- `style`
- `support`
- `tag`
- `target`
- `template`
- `templates`
- `text`
- `they`
- `title`
- `toPlainText`
- `top`
- `transform`
- `transitional`
- `tree`
- `tsx`
- `type`
- `unable`
- `undefinedpx`
- `use`
- `used`
- `using`
- `version`
- `versions`
- `view`
- `web`
- `website`
- `width`
- `www`
- `xhtml1`
- `yarn`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

