# Documentation: postmark.mdx
**File Path:** `apps/docs/integrations/postmark.mdx`
**Language:** Unknown
**Size:** 1,785 bytes
**Lines:** 80
**Generated:** 2025-11-15T20:37:32.751405Z

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

- **Path:** `apps/docs/integrations/postmark.mdx`
- **Name:** `postmark.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,785 bytes (1.74 KB)
- **Lines of Code:** 80

---

## Original Source

```
---
title: 'Send email using Postmark'
sidebarTitle: 'Postmark'
description: 'Learn how to send an email using React Email and the Postmark Node.js SDK.'
'og:image': 'https://react.email/static/covers/react-email.png'
---

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [Postmark Node.js SDK](https://www.npmjs.com/package/postmark).

<CodeGroup>

```sh npm
npm install postmark @react-email/components
```

```sh yarn
yarn add postmark @react-email/components
```

```sh pnpm
pnpm add postmark @react-email/components
```

</CodeGroup>

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx
import * as React from 'react';
import { Html, Button } from "@react-email/components";

export function Email(props) {
  const { url } = props;

  return (
    <Html lang="en">
      <Button href={url}>Click me</Button>
    </Html>
  );
}
```

## 3. Convert to HTML and send email

Import the email template you just built, convert into an HTML string, and use the Postmark SDK to send it.

```tsx
import { render } from '@react-email/components';
import postmark from 'postmark';
import { Email } from './email';

const client = new postmark.ServerClient(process.env.POSTMARK_API_KEY);

const emailHtml = await render(<Email url="https://example.com" />);

const options = {
  From: 'you@example.com',
  To: 'user@gmail.com',
  Subject: 'hello world',
  HtmlBody: emailHtml,
};

await client.sendEmail(options);
```

## Try it yourself

<Card
  title="Postmark example"
  icon='arrow-up-right-from-square'
  iconType="duotone"
  href="https://github.com/resend/react-email/tree/main/examples/postmark"
>
  See the full source code.
</Card>

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `./email`
- `@react-email/components`
- `postmark`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 90

- `Button`
- `Card`
- `Click`
- `CodeGroup`
- `Convert`
- `Create`
- `Email`
- `Get`
- `Html`
- `HtmlBody`
- `Install`
- `Learn`
- `Node`
- `POSTMARK_API_KEY`
- `Postmark`
- `React`
- `See`
- `Send`
- `ServerClient`
- `Start`
- `Subject`
- `add`
- `arrow`
- `building`
- `built`
- `client`
- `code`
- `com`
- `components`
- `convert`
- `covers`
- `dependencies`
- `description`
- `duotone`
- `email`
- `emailHtml`
- `env`
- `example`
- `examples`
- `file`
- `full`
- `github`
- `gmail`
- `hello`
- `how`
- `href`
- `https`
- `icon`
- `iconType`
- `image`
- `install`
- `into`
- `jsx`
- `just`
- `lang`
- `main`
- `npm`
- `npmjs`
- `options`
- `package`
- `png`
- `pnpm`
- `postmark`
- `process`
- `props`
- `react`
- `render`
- `resend`
- `right`
- `send`
- `sendEmail`
- `sidebarTitle`
- `source`
- `square`
- `static`
- `string`
- `template`
- `title`
- `tree`
- `tsx`
- `url`
- `use`
- `user`
- `using`
- `world`
- `www`
- `yarn`
- `you`
- `your`
- `yourself`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

