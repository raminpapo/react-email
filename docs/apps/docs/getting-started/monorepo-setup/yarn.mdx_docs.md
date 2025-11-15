# Documentation: yarn.mdx
**File Path:** `apps/docs/getting-started/monorepo-setup/yarn.mdx`
**Language:** Unknown
**Size:** 2,774 bytes
**Lines:** 109
**Generated:** 2025-11-15T20:37:32.742778Z

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

- **Path:** `apps/docs/getting-started/monorepo-setup/yarn.mdx`
- **Name:** `yarn.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 2,774 bytes (2.71 KB)
- **Lines of Code:** 109

---

## Original Source

```
---
title: 'Setting up for yarn workspaces'
sidebarTitle: 'yarn'
description: 'Configure React Email on a yarn monorepo'
'og:image': 'https://react.email/static/covers/react-email.png'
---

<Note>
  This is a guide intended at users of [yarn modern](https://yarnpkg.com/getting-started/qa#why-should-you-upgrade-to-yarn-modern). 
  For those who are using [yarn classic](https://www.npmjs.com/package/yarn) (`1.x`), you can do something similar to the 
  [pnpm guide](/getting-started/monorepo-setup/pnpm).
</Note>

## 1. Create transactional workspace

Create a new folder called `transactional` inside of where you keep workspace packages (generally `./packages/*`).

Include a new `package.json` and do not forget to add this to the `workspaces` of your monorepo's `package.json`.

<Card
  title="React Email + Turborepo + yarn example"
  icon="arrow-up-right-from-square"
  href="https://github.com/resend/react-email-turborepo-yarn-example"
>
  See the full source code
</Card>

## 2. Set linker either to `node-modules` or to `pnpm`

Currently, React Email can only work with yarn's `node-modules` and `pnpm` [install modes](https://yarnpkg.com/features/linkers)
so you will need to set it to one of these two on your `.yarnrc.yml` file:

```yml .yarnrc.yml
nodeLinker: node-modules
```

## 3. Install dependencies

Install React Email in the `transactional` workspace.

```sh packages/transactional
yarn add react-email -D -E
yarn add @react-email/components react react-dom -E
```

## 4. Add scripts

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

## 5. Write your emails

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

## 6. Run preview server

Start the email previews development server:

```sh packages/transactional
yarn dev
```

## 7. See changes live

Visit [localhost:3000](http://localhost:3000) and edit the `emails/MyEmail.tsx` file to see the changes.

<Frame>
  <img alt="Local Development" src="/images/local-dev.jpg" />
</Frame>

## 8. Try it yourself

<Card
  title="React Email + Turborepo + yarn example"
  icon="arrow-up-right-from-square"
  href="https://github.com/resend/react-email-turborepo-yarn-example"
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

**Total Unique Identifiers:** 137

- `Add`
- `Button`
- `Card`
- `Click`
- `Configure`
- `Create`
- `Currently`
- `Development`
- `Email`
- `Frame`
- `Html`
- `Include`
- `Install`
- `Local`
- `MyEmail`
- `Note`
- `React`
- `Run`
- `See`
- `Set`
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
- `classic`
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
- `either`
- `email`
- `emails`
- `example`
- `features`
- `fff`
- `file`
- `folder`
- `following`
- `forget`
- `full`
- `generally`
- `getting`
- `github`
- `guide`
- `href`
- `http`
- `https`
- `icon`
- `image`
- `images`
- `img`
- `inside`
- `install`
- `intended`
- `jpg`
- `json`
- `jsx`
- `keep`
- `linker`
- `linkers`
- `live`
- `local`
- `localhost`
- `modern`
- `modes`
- `modules`
- `monorepo`
- `need`
- `node`
- `nodeLinker`
- `npmjs`
- `one`
- `only`
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
- `set`
- `setup`
- `sidebarTitle`
- `similar`
- `something`
- `source`
- `square`
- `src`
- `started`
- `static`
- `style`
- `these`
- `those`
- `title`
- `transactional`
- `tsx`
- `turborepo`
- `two`
- `upgrade`
- `users`
- `using`
- `where`
- `who`
- `why`
- `work`
- `workspace`
- `workspaces`
- `www`
- `yarn`
- `yarnpkg`
- `yarnrc`
- `yml`
- `you`
- `your`
- `yourself`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

