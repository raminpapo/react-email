# Documentation: npm.mdx
**File Path:** `apps/docs/getting-started/monorepo-setup/npm.mdx`
**Language:** Unknown
**Size:** 2,132 bytes
**Lines:** 94
**Generated:** 2025-11-15T20:37:32.739545Z

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

- **Path:** `apps/docs/getting-started/monorepo-setup/npm.mdx`
- **Name:** `npm.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 2,132 bytes (2.08 KB)
- **Lines of Code:** 94

---

## Original Source

```
---
title: 'Setting up for npm workspaces'
sidebarTitle: 'npm'
description: 'Configure React Email on a npm monorepo'
'og:image': 'https://react.email/static/covers/react-email.png'
---

## 1. Create workspace

Create a new folder called `transactional` inside of where you keep workspace packages (generally `./packages/*`).

Include a new `package.json` and do not forget to add this to the `workspaces` of your monorepo's `package.json`.

<Card 
  title="React Email + Turborepo + npm example" 
  icon="arrow-up-right-from-square" 
  href="https://github.com/resend/react-email-turborepo-npm-example"
>
  See the full source code
</Card>

## 2. Install dependencies

Install React Email in the `transactional` workspace.

```sh packages/transactional
npm install react-email -D -E
npm install @react-email/components react react-dom -E
```

## 3. Add scripts

Include the following script in your `package.json` file.

```json packages/transactional/package.json
{
  // ...
  "scripts": {
    "dev": "email dev"
  }
  // ...
}
```

## 4. Write your emails

Create a new folder called `emails`, create a file inside called `MyEmail.tsx` and add the following example code:

```jsx packages/transactional/emails/MyEmail.tsx
import { Button, Html } from "@react-email/components";
import * as React from "react";

export const MyEmail = () => {
  return (
    <Html>
      <Button
        href="https://example.com"
        style={{ background: "#000", color: "#fff", padding: "12px 20px" }}
      >
        Click me
      </Button>
    </Html>
  );
}

export default MyEmail;
```

## 5. Run preview server

Start the email previews development server:

```sh packages/transactional
npm run dev
```

## 6. See changes live

Visit [localhost:3000](http://localhost:3000) and edit the `emails/MyEmail.tsx` file to see the changes.

<Frame>
  <img alt="Local Development" src="/images/local-dev.jpg" />
</Frame>

## 7. Try it yourself

<Card 
  title="React Email + Turborepo + npm example" 
  icon="arrow-up-right-from-square" 
  href="https://github.com/resend/react-email-turborepo-npm-example"
>
  See the full source code
</Card>

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `@react-email/components`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 99

- `Add`
- `Button`
- `Card`
- `Click`
- `Configure`
- `Create`
- `Development`
- `Email`
- `Frame`
- `Html`
- `Include`
- `Install`
- `Local`
- `MyEmail`
- `React`
- `Run`
- `See`
- `Setting`
- `Start`
- `Turborepo`
- `Visit`
- `Write`
- `add`
- `alt`
- `arrow`
- `background`
- `called`
- `changes`
- `code`
- `color`
- `com`
- `components`
- `covers`
- `create`
- `dependencies`
- `description`
- `dev`
- `development`
- `dom`
- `edit`
- `email`
- `emails`
- `example`
- `fff`
- `file`
- `folder`
- `following`
- `forget`
- `full`
- `generally`
- `github`
- `href`
- `http`
- `https`
- `icon`
- `image`
- `images`
- `img`
- `inside`
- `install`
- `jpg`
- `json`
- `jsx`
- `keep`
- `live`
- `local`
- `localhost`
- `monorepo`
- `npm`
- `package`
- `packages`
- `padding`
- `png`
- `preview`
- `previews`
- `react`
- `resend`
- `right`
- `run`
- `script`
- `scripts`
- `see`
- `server`
- `sidebarTitle`
- `source`
- `square`
- `src`
- `static`
- `style`
- `title`
- `transactional`
- `tsx`
- `turborepo`
- `where`
- `workspace`
- `workspaces`
- `you`
- `your`
- `yourself`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

