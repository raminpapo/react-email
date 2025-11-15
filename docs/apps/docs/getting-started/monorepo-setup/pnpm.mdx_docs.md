# Documentation: pnpm.mdx
**File Path:** `apps/docs/getting-started/monorepo-setup/pnpm.mdx`
**Language:** Unknown
**Size:** 2,110 bytes
**Lines:** 93
**Generated:** 2025-11-15T20:37:32.741114Z

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

- **Path:** `apps/docs/getting-started/monorepo-setup/pnpm.mdx`
- **Name:** `pnpm.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 2,110 bytes (2.06 KB)
- **Lines of Code:** 93

---

## Original Source

```
---
title: 'Setting up for pnpm workspaces'
sidebarTitle: 'pnpm'
description: 'Configure React Email on a pnpm monorepo'
'og:image': 'https://react.email/static/covers/react-email.png'
---

## 1. Create workspace

Create a new folder called `transactional` inside of where you keep workspace packages (generally `./packages/*`) and 
in there setup a new `package.json` and do not forget to add this to your `pnpm-workspace.yaml`.

<Card
  title="React Email + Turborepo + pnpm example"
  icon="arrow-up-right-from-square"
  href="https://github.com/resend/react-email-turborepo-pnpm-example"
>
  See the full source code
</Card>

## 2. Install dependencies

Install React Email in the `transactional` workspace.

```sh packages/transactional
pnpm add react-email -D -E
pnpm add @react-email/components react react-dom -E
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
pnpm dev
```

## 6. See changes live

Visit [localhost:3000](http://localhost:3000) and edit the `emails/MyEmail.tsx` file to see the changes.

<Frame>
  <img alt="Local Development" src="/images/local-dev.jpg" />
</Frame>

## 7. Try it yourself

<Card
  title="React Email + Turborepo + pnpm example"
  icon="arrow-up-right-from-square"
  href="https://github.com/resend/react-email-turborepo-pnpm-example"
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

**Total Unique Identifiers:** 100

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
- `jpg`
- `json`
- `jsx`
- `keep`
- `live`
- `local`
- `localhost`
- `monorepo`
- `package`
- `packages`
- `padding`
- `png`
- `pnpm`
- `preview`
- `previews`
- `react`
- `resend`
- `right`
- `script`
- `scripts`
- `see`
- `server`
- `setup`
- `sidebarTitle`
- `source`
- `square`
- `src`
- `static`
- `style`
- `there`
- `title`
- `transactional`
- `tsx`
- `turborepo`
- `where`
- `workspace`
- `workspaces`
- `yaml`
- `you`
- `your`
- `yourself`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

