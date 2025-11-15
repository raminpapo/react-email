# Documentation: scaleway.mdx
**File Path:** `apps/docs/integrations/scaleway.mdx`
**Language:** Unknown
**Size:** 2,471 bytes
**Lines:** 113
**Generated:** 2025-11-15T20:37:32.754851Z

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

- **Path:** `apps/docs/integrations/scaleway.mdx`
- **Name:** `scaleway.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 2,471 bytes (2.41 KB)
- **Lines of Code:** 113

---

## Original Source

```
---
title: "Send email using Scaleway Transactional Email"
sidebarTitle: "Scaleway"
description: "Learn how to send an email using React Email and the Scaleway Node.js SDK."
"og:image": "https://react.email/static/covers/react-email.png"
---

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [Scaleway Node.js SDK](https://www.npmjs.com/package/@scaleway/sdk).

<CodeGroup>

```sh npm
npm install @scaleway/sdk @react-email/components
```

```sh yarn
yarn add @scaleway/sdk @react-email/components
```

```sh pnpm
pnpm add @scaleway/sdk @react-email/components
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

Import the email template you just built, convert into an HTML string, and use the Scaleway SDK to send it.

```tsx
import { render } from "@react-email/components";
import { TransactionalEmail, createClient } from "@scaleway/sdk";
import { Email } from "./email";

const client = createClient({
  accessKey: process.env.ACCESS_KEY,
  secretKey: process.env.SECRET_KEY,
  defaultProjectId: process.env.PROJECT_ID,
  defaultRegion: "fr-par",
  defaultZone: "fr-par-1",
});

const transactionalEmailClient = new TransactionalEmail.v1alpha1.API(client);

const emailHtml = await render(<Email url="https://example.com" />);

const sender = {
  email: "react-email@transactional.email.fr",
  subject: "TEST",
  name: "Team",
};

const userInvited = {
  email: "XXXX@scaleway.com",
  name: "TEST",
  teamName: "Team",
};

const userInvitedBy = {
  email: "XXXX@scaleway.com",
  name: "TEST",
  teamName: "Team",
};

transactionalEmailClient.createEmail({
  from: {
    email: sender.email,
    name: sender.name,
  },
  to: [
    {
      email: userInvited.email,
      name: userInvited.name,
    },
  ],
  subject: sender.subject,
  text: null,
  html: emailHtml,
});
```

## Try it yourself

<Card
  title="Scaleway Transactional Email"
  icon="arrow-up-right-from-square"
  iconType="duotone"
  href="https://github.com/resend/react-email/tree/main/examples/scaleway"
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
- `@scaleway/sdk`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 106

- `ACCESS_KEY`
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
- `PROJECT_ID`
- `React`
- `SECRET_KEY`
- `Scaleway`
- `See`
- `Send`
- `Start`
- `Team`
- `Transactional`
- `TransactionalEmail`
- `accessKey`
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
- `createClient`
- `createEmail`
- `defaultProjectId`
- `defaultRegion`
- `defaultZone`
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
- `name`
- `npm`
- `npmjs`
- `package`
- `par`
- `png`
- `pnpm`
- `process`
- `props`
- `react`
- `render`
- `resend`
- `right`
- `scaleway`
- `sdk`
- `secretKey`
- `send`
- `sender`
- `sidebarTitle`
- `source`
- `square`
- `static`
- `string`
- `subject`
- `teamName`
- `template`
- `text`
- `title`
- `transactional`
- `transactionalEmailClient`
- `tree`
- `tsx`
- `url`
- `use`
- `userInvited`
- `userInvitedBy`
- `using`
- `v1alpha1`
- `www`
- `yarn`
- `you`
- `your`
- `yourself`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

