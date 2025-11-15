# Documentation: nodemailer.mdx
**File Path:** `apps/docs/integrations/nodemailer.mdx`
**Language:** Unknown
**Size:** 1,883 bytes
**Lines:** 88
**Generated:** 2025-11-15T20:37:32.747467Z

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

- **Path:** `apps/docs/integrations/nodemailer.mdx`
- **Name:** `nodemailer.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,883 bytes (1.84 KB)
- **Lines of Code:** 88

---

## Original Source

```
---
title: 'Send email using Nodemailer'
sidebarTitle: 'Nodemailer'
description: 'Learn how to send an email using React Email and Nodemailer.'
'og:image': 'https://react.email/static/covers/react-email.png'
---

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) and [nodemailer](https://www.npmjs.com/package/nodemailer) packages.

<CodeGroup>

```sh npm
npm install nodemailer @react-email/components
```

```sh yarn
yarn add nodemailer @react-email/components
```

```sh pnpm
pnpm add nodemailer @react-email/components
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

Import the email template you just built, convert into a HTML string, and use the Nodemailer SDK to send it.

```tsx
import { render } from '@react-email/components';
import nodemailer from 'nodemailer';
import { Email } from './email';

const transporter = nodemailer.createTransport({
  host: 'smtp.forwardemail.net',
  port: 465,
  secure: true,
  auth: {
    user: 'my_user',
    pass: 'my_password',
  },
});

const emailHtml = await render(<Email url="https://example.com" />);

const options = {
  from: 'you@example.com',
  to: 'user@gmail.com',
  subject: 'hello world',
  html: emailHtml,
};

await transporter.sendMail(options);
```

## Try it yourself

<Card
  title="Nodemailer example"
  icon='arrow-up-right-from-square'
  iconType="duotone"
  href="https://github.com/resend/react-email/tree/main/examples/nodemailer"
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
- `nodemailer`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 97

- `Button`
- `Card`
- `Click`
- `CodeGroup`
- `Convert`
- `Create`
- `Email`
- `Get`
- `Html`
- `Install`
- `Learn`
- `Nodemailer`
- `React`
- `See`
- `Send`
- `Start`
- `add`
- `arrow`
- `auth`
- `building`
- `built`
- `code`
- `com`
- `components`
- `convert`
- `covers`
- `createTransport`
- `dependencies`
- `description`
- `duotone`
- `email`
- `emailHtml`
- `example`
- `examples`
- `file`
- `forwardemail`
- `full`
- `github`
- `gmail`
- `hello`
- `host`
- `how`
- `href`
- `html`
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
- `my_password`
- `my_user`
- `net`
- `nodemailer`
- `npm`
- `npmjs`
- `options`
- `package`
- `packages`
- `pass`
- `png`
- `pnpm`
- `port`
- `props`
- `react`
- `render`
- `resend`
- `right`
- `secure`
- `send`
- `sendMail`
- `sidebarTitle`
- `smtp`
- `source`
- `square`
- `static`
- `string`
- `subject`
- `template`
- `title`
- `transporter`
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

