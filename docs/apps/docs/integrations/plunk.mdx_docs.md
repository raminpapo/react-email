# Documentation: plunk.mdx
**File Path:** `apps/docs/integrations/plunk.mdx`
**Language:** Unknown
**Size:** 1,721 bytes
**Lines:** 79
**Generated:** 2025-11-15T20:37:32.749984Z

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

- **Path:** `apps/docs/integrations/plunk.mdx`
- **Name:** `plunk.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,721 bytes (1.68 KB)
- **Lines of Code:** 79

---

## Original Source

```
---
title: "Send email using Plunk"
sidebarTitle: "Plunk"
description: "Learn how to send an email using React Email and the Plunk Node.js SDK."
"og:image": "https://react.email/static/covers/react-email.png"
---

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [Plunk Node.js SDK](https://www.npmjs.com/package/@plunk/node).

<CodeGroup>

```sh npm
npm install @plunk/node @react-email/components
```

```sh yarn
yarn add @plunk/node @react-email/components
```

```sh pnpm
pnpm add @plunk/node @react-email/components
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

export default Email;
```

## 3. Convert to HTML and send email

Import the email template you just built, convert into an HTML string, and use the Plunk SDK to send it.

```tsx
import Plunk from "@plunk/node";
import { render } from "@react-email/components";
import { Email } from "./email";

const plunk = new Plunk(process.env.PLUNK_API_KEY);

const emailHtml = await render(<Email url="https://example.com" />);

plunk.emails.send({
  to: "hello@useplunk.com",
  subject: "Hello world",
  body: emailHtml,
});
```

## Try it yourself

<Card
  title="Plunk example"
  icon="arrow-up-right-from-square"
  iconType="duotone"
  href="https://github.com/resend/react-email/tree/main/examples/plunk"
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
- `@plunk/node`
- `@react-email/components`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 88

- `Button`
- `Card`
- `Click`
- `CodeGroup`
- `Convert`
- `Create`
- `Email`
- `Get`
- `Hello`
- `Html`
- `Install`
- `Learn`
- `Node`
- `PLUNK_API_KEY`
- `Plunk`
- `React`
- `See`
- `Send`
- `Start`
- `add`
- `arrow`
- `body`
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
- `emails`
- `env`
- `example`
- `examples`
- `file`
- `full`
- `github`
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
- `node`
- `npm`
- `npmjs`
- `package`
- `plunk`
- `png`
- `pnpm`
- `process`
- `props`
- `react`
- `render`
- `resend`
- `right`
- `send`
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
- `useplunk`
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

