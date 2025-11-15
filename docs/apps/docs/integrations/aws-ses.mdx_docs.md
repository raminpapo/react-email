# Documentation: aws-ses.mdx
**File Path:** `apps/docs/integrations/aws-ses.mdx`
**Language:** Unknown
**Size:** 2,101 bytes
**Lines:** 93
**Generated:** 2025-11-15T20:37:32.744463Z

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

- **Path:** `apps/docs/integrations/aws-ses.mdx`
- **Name:** `aws-ses.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 2,101 bytes (2.05 KB)
- **Lines of Code:** 93

---

## Original Source

```
---
title: 'Send email using AWS SES'
sidebarTitle: 'AWS SES'
description: 'Learn how to send an email using React Email and the AWS SES Node.js SDK.'
'og:image': 'https://react.email/static/covers/react-email.png'
---

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [AWS SES Node.js SDK](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-ses/).

<CodeGroup>

```sh npm
npm install @aws-sdk/client-ses @react-email/components
```

```sh yarn
yarn add @aws-sdk/client-ses @react-email/components
```

```sh pnpm
pnpm add @aws-sdk/client-ses @react-email/components
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

Import the email template you just built, convert into an HTML string, and use the AWS SES SDK to send it.

```tsx
import type { SendEmailCommandInput } from "@aws-sdk/client-ses";
import { render } from '@react-email/components';
import { SES } from '@aws-sdk/client-ses';
import { Email } from './email';

const ses = new SES({ region: process.env.AWS_SES_REGION })

const emailHtml = await render(<Email url="https://example.com" />);

const params: SendEmailCommandInput = {
  Source: 'you@example.com',
  Destination: {
    ToAddresses: ['user@gmail.com'],
  },
  Message: {
    Body: {
      Html: {
        Charset: 'UTF-8',
        Data: emailHtml,
      },
    },
    Subject: {
      Charset: 'UTF-8',
      Data: 'hello world',
    },
  },
};

await ses.sendEmail(params);
```

## Try it yourself

<Card
  title="AWS SES example"
  icon='arrow-up-right-from-square'
  iconType="duotone"
  href="https://github.com/resend/react-email/tree/main/examples/aws-ses"
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
- `@aws-sdk/client-ses`
- `@react-email/components`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 104

- `AWSJavaScriptSDK`
- `AWS_SES_REGION`
- `Body`
- `Button`
- `Card`
- `Charset`
- `Click`
- `CodeGroup`
- `Convert`
- `Create`
- `Data`
- `Destination`
- `Email`
- `Get`
- `Html`
- `Install`
- `Learn`
- `Message`
- `Node`
- `React`
- `See`
- `Send`
- `SendEmailCommandInput`
- `Source`
- `Start`
- `Subject`
- `ToAddresses`
- `add`
- `amazon`
- `arrow`
- `aws`
- `building`
- `built`
- `client`
- `clients`
- `code`
- `com`
- `components`
- `convert`
- `covers`
- `dependencies`
- `description`
- `docs`
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
- `latest`
- `main`
- `npm`
- `npmjs`
- `package`
- `params`
- `png`
- `pnpm`
- `process`
- `props`
- `react`
- `region`
- `render`
- `resend`
- `right`
- `sdk`
- `send`
- `sendEmail`
- `ses`
- `sidebarTitle`
- `source`
- `square`
- `static`
- `string`
- `template`
- `title`
- `tree`
- `tsx`
- `type`
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

