# Documentation: mailersend.mdx
**File Path:** `apps/docs/integrations/mailersend.mdx`
**Language:** Unknown
**Size:** 2,027 bytes
**Lines:** 86
**Generated:** 2025-11-15T20:37:32.745952Z

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

- **Path:** `apps/docs/integrations/mailersend.mdx`
- **Name:** `mailersend.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 2,027 bytes (1.98 KB)
- **Lines of Code:** 86

---

## Original Source

```
---
title: 'Send email using MailerSend'
sidebarTitle: 'MailerSend'
description: 'Learn how to send an email using React Email and the MailerSend Node.js SDK.'
'og:image': 'https://react.email/static/covers/react-email.png'
---

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [MailerSend Node.js SDK](https://www.npmjs.com/package/mailersend).

<CodeGroup>

```sh npm
npm install mailersend @react-email/components
```

```sh yarn
yarn add mailersend @react-email/components
```

```sh pnpm
pnpm add mailersend @react-email/components
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

Import the email template you just built, convert into an HTML string, and use the MailerSend SDK to send it.

```tsx
import { render } from '@react-email/components';
import { MailerSend, EmailParams, Sender, Recipient } from "mailersend";
import { Email } from './email';

const mailerSend = new MailerSend({
  apiKey: process.env.MAILERSEND_API_KEY || '',
});

const emailHtml = await render(<Email url="https://example.com" />);

const sentFrom = new Sender("you@yourdomain.com", "Your name");
const recipients = [
  new Recipient("your@client.com", "Your Client")
];

const emailParams = new EmailParams()
  .setFrom(sentFrom)
  .setTo(recipients)
  .setSubject("This is a Subject")
  .setHtml(emailHtml)

await mailerSend.email.send(emailParams);
```

## Try it yourself

<Card
  title="MailerSend example"
  icon='arrow-up-right-from-square'
  iconType="duotone"
  href="https://github.com/resend/react-email/tree/main/examples/mailersend"
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
- `mailersend`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 98

- `Button`
- `Card`
- `Click`
- `Client`
- `CodeGroup`
- `Convert`
- `Create`
- `Email`
- `EmailParams`
- `Get`
- `Html`
- `Install`
- `Learn`
- `MAILERSEND_API_KEY`
- `MailerSend`
- `Node`
- `React`
- `Recipient`
- `See`
- `Send`
- `Sender`
- `Start`
- `Subject`
- `Your`
- `add`
- `apiKey`
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
- `emailParams`
- `env`
- `example`
- `examples`
- `file`
- `full`
- `github`
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
- `mailerSend`
- `mailersend`
- `main`
- `name`
- `npm`
- `npmjs`
- `package`
- `png`
- `pnpm`
- `process`
- `props`
- `react`
- `recipients`
- `render`
- `resend`
- `right`
- `send`
- `sentFrom`
- `setFrom`
- `setHtml`
- `setSubject`
- `setTo`
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
- `using`
- `www`
- `yarn`
- `you`
- `your`
- `yourdomain`
- `yourself`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

