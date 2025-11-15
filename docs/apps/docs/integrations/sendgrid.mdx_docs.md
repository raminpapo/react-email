# Documentation: sendgrid.mdx
**File Path:** `apps/docs/integrations/sendgrid.mdx`
**Language:** Unknown
**Size:** 1,780 bytes
**Lines:** 80
**Generated:** 2025-11-15T20:37:32.756603Z

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

- **Path:** `apps/docs/integrations/sendgrid.mdx`
- **Name:** `sendgrid.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,780 bytes (1.74 KB)
- **Lines of Code:** 80

---

## Original Source

```
---
title: "Send email using SendGrid"
sidebarTitle: "SendGrid"
description: "Learn how to send an email using React Email and the SendGrid Node.js SDK."
"og:image": "https://react.email/static/covers/react-email.png"
---

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [SendGrid Node.js SDK](https://www.npmjs.com/package/@sendgrid/mail).

<CodeGroup>

```sh npm
npm install @sendgrid/mail @react-email/components
```

```sh yarn
yarn add @sendgrid/mail @react-email/components
```

```sh pnpm
pnpm add @sendgrid/mail @react-email/components
```

</CodeGroup>

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx
import * as React from "react";
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

Import the email template you just built, convert into an HTML string, and use the SendGrid SDK to send it.

```tsx
import { render } from "@react-email/components";
import sendgrid from "@sendgrid/mail";
import { Email } from "./email";

sendgrid.setApiKey(process.env.SENDGRID_API_KEY);

const emailHtml = await render(<Email url="https://example.com" />);

const options = {
  from: "you@example.com",
  to: "user@gmail.com",
  subject: "hello world",
  html: emailHtml,
};

sendgrid.send(options);
```

## Try it yourself

<Card
  title="SendGrid example"
  icon="arrow-up-right-from-square"
  iconType="duotone"
  href="https://github.com/resend/react-email/tree/main/examples/sendgrid"
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
- `@sendgrid/mail`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 89

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
- `Node`
- `React`
- `SENDGRID_API_KEY`
- `See`
- `Send`
- `SendGrid`
- `Start`
- `add`
- `arrow`
- `building`
- `built`
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
- `mail`
- `main`
- `npm`
- `npmjs`
- `options`
- `package`
- `png`
- `pnpm`
- `process`
- `props`
- `react`
- `render`
- `resend`
- `right`
- `send`
- `sendgrid`
- `setApiKey`
- `sidebarTitle`
- `source`
- `square`
- `static`
- `string`
- `subject`
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

