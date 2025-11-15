# Documentation: resend.mdx
**File Path:** `apps/docs/integrations/resend.mdx`
**Language:** Unknown
**Size:** 3,181 bytes
**Lines:** 113
**Generated:** 2025-11-15T20:37:32.752955Z

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

- **Path:** `apps/docs/integrations/resend.mdx`
- **Name:** `resend.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 3,181 bytes (3.11 KB)
- **Lines of Code:** 113

---

## Original Source

```
---
title: 'Send email using Resend'
sidebarTitle: 'Resend'
description: 'Learn how to send an email and set up Templates using React Email and the Resend Node.js SDK.'
'og:image': 'https://react.email/static/covers/react-email.png'
---

##  Send email with Resend
<Tip>Resend was built by the same team that created React Email, which makes this our recommendation to send emails.</Tip>

### 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [Resend Node.js SDK](https://www.npmjs.com/package/resend).

<CodeGroup>

```sh npm
npm install resend @react-email/components
```

```sh yarn
yarn add resend @react-email/components
```

```sh pnpm
pnpm add resend @react-email/components
```

</CodeGroup>

### 2. Create an email using React

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

export default Email;
```

### 3. Send email

<Info>When integrating with other services, you need to convert your React template into HTML before sending. Resend takes care of that for you.</Info>

Import the email template you just built and use the Resend SDK to send it.

```tsx
import { Resend } from 'resend';
import { Email } from './email';

const resend = new Resend('re_123456789');

await resend.emails.send({
  from: 'you@example.com',
  to: 'user@gmail.com',
  subject: 'hello world',
  react: <Email url="https://example.com" />,
});
```

## Set up Templates with Resend

[Resend Templates](https://resend.com/docs/dashboard/templates/introduction) are a great way to collaborate on emails with your team, even if they're not technical. Upload a React Email Template to Resend and your entire team can collaborate in real-time in the visual editor.

Here's how to get started.

### 1. Add your Resend API Key

First, sign up for a [free Resend account](https://resend.com/signup).

Next, set up the Resend integration using the React Email CLI:

```bash
npx react-email@latest resend setup
```

This will prompt you to enter your Resend API Key. To get one, navigate to [API Keys](https://resend.com/api-keys) in your Resend dashboard, click **Create API key**, and ensure that the API Key is scoped to **Full Access**.

Paste the API Key into the terminal and press enter.

### 2. Upload a Template to Resend

Run React Email and visit the **Resend** tab of the toolbar, located at the bottom of the window.

Choose **Upload** or **Bulk Upload** to import your Template to Resend.

<video src="https://cdn.resend.com/posts/react-email-resend-integration.mp4" autoPlay loop playsInline class="extraWidth"></video>

If you want to remove the Resend integration, run `npx react-email@latest resend reset`.


## Try it yourself

<Card
  title="Resend example"
  icon='arrow-up-right-from-square'
  iconType="duotone"
  href="https://github.com/resend/react-email/tree/main/examples/resend"
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
- `react`
- `resend`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 171

- `Access`
- `Add`
- `Bulk`
- `Button`
- `Card`
- `Choose`
- `Click`
- `CodeGroup`
- `Create`
- `Email`
- `First`
- `Full`
- `Get`
- `Here`
- `Html`
- `Info`
- `Install`
- `Key`
- `Keys`
- `Learn`
- `Next`
- `Node`
- `Paste`
- `React`
- `Resend`
- `Run`
- `See`
- `Send`
- `Set`
- `Start`
- `Template`
- `Templates`
- `Tip`
- `Upload`
- `When`
- `account`
- `add`
- `api`
- `arrow`
- `autoPlay`
- `bash`
- `before`
- `bottom`
- `building`
- `built`
- `care`
- `cdn`
- `click`
- `code`
- `collaborate`
- `com`
- `components`
- `convert`
- `covers`
- `created`
- `dashboard`
- `dependencies`
- `description`
- `docs`
- `duotone`
- `editor`
- `email`
- `emails`
- `ensure`
- `enter`
- `entire`
- `even`
- `example`
- `examples`
- `extraWidth`
- `file`
- `free`
- `full`
- `get`
- `github`
- `gmail`
- `great`
- `hello`
- `how`
- `href`
- `https`
- `icon`
- `iconType`
- `image`
- `install`
- `integrating`
- `integration`
- `into`
- `introduction`
- `jsx`
- `just`
- `key`
- `keys`
- `lang`
- `latest`
- `located`
- `loop`
- `main`
- `makes`
- `mp4`
- `navigate`
- `need`
- `npm`
- `npmjs`
- `npx`
- `one`
- `other`
- `our`
- `package`
- `playsInline`
- `png`
- `pnpm`
- `posts`
- `press`
- `prompt`
- `props`
- `re_123456789`
- `react`
- `real`
- `recommendation`
- `remove`
- `resend`
- `reset`
- `right`
- `run`
- `same`
- `scoped`
- `send`
- `sending`
- `services`
- `set`
- `setup`
- `sidebarTitle`
- `sign`
- `signup`
- `source`
- `square`
- `src`
- `started`
- `static`
- `subject`
- `tab`
- `takes`
- `team`
- `technical`
- `template`
- `templates`
- `terminal`
- `they`
- `time`
- `title`
- `toolbar`
- `tree`
- `tsx`
- `url`
- `use`
- `user`
- `using`
- `video`
- `visit`
- `visual`
- `want`
- `way`
- `which`
- `window`
- `world`
- `www`
- `yarn`
- `you`
- `your`
- `yourself`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

