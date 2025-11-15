# Documentation: manual-setup.mdx
**File Path:** `apps/docs/getting-started/manual-setup.mdx`
**Language:** Unknown
**Size:** 2,154 bytes
**Lines:** 120
**Generated:** 2025-11-15T20:37:32.732649Z

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

- **Path:** `apps/docs/getting-started/manual-setup.mdx`
- **Name:** `manual-setup.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 2,154 bytes (2.10 KB)
- **Lines of Code:** 120

---

## Original Source

```
---
title: "Manual Setup"
sidebarTitle: "Manual Setup"
description: "Create a brand-new folder with packages powered by React Email."
"og:image": "https://react.email/static/covers/react-email.png"
icon: "hammer"
---

import NextSteps from '/snippets/next-steps.mdx'

<Note>Are you using monorepos? Then we recommend you follow our [monorepos setup](/getting-started/monorepo-setup/choose-package-manager).</Note>

## 1. Create directory

Create a new folder called `react-email-starter` and initialize a new npm project:

```sh
mkdir react-email-starter
cd react-email-starter
npm init
```

## 2. Install dependencies

Install the React Email package locally and a few components.

<CodeGroup>

```sh npm
npm install react-email -D -E
npm install @react-email/components react react-dom -E
```

```sh yarn
yarn add react-email -D -E
yarn add @react-email/components react react-dom -E
```

```sh pnpm
pnpm add react-email -D -E
pnpm add @react-email/components react react-dom -E
```

```sh bun
bun add react-email -D -E
bun add @react-email/components react react-dom -E
```

</CodeGroup>

## 3. Add scripts

Include the following script in your `package.json` file.

```json package.json
{
  "scripts": {
    "dev": "email dev"
  }
}
```

## 4. Write an email template

Create a new folder called `emails`, create a file inside called `my-email.tsx`, and add the following code:

```jsx emails/my-email.tsx
import { Button, Html } from "@react-email/components";
import * as React from "react";

export default function Email() {
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
```

## 5. Run locally

Start the development server.

<CodeGroup>

```sh npm
npm run dev
```

```sh yarn
yarn dev
```

```sh pnpm
pnpm dev
```

```sh bun
bun dev
```

</CodeGroup>

## 6. See changes live

Visit [localhost:3000](http://localhost:3000) and edit the `index.tsx` file to see the changes.

<Frame>
  <img alt="Local Development" src="/images/local-dev.jpg" />
</Frame>

## 7. Next steps

<NextSteps/>

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `/snippets/next-steps.mdx`
- `@react-email/components`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 113

- `Add`
- `Button`
- `Click`
- `CodeGroup`
- `Create`
- `Development`
- `Email`
- `Frame`
- `Html`
- `Include`
- `Install`
- `Local`
- `Manual`
- `Next`
- `NextSteps`
- `Note`
- `React`
- `Run`
- `See`
- `Setup`
- `Start`
- `Then`
- `Visit`
- `Write`
- `add`
- `alt`
- `background`
- `brand`
- `bun`
- `called`
- `changes`
- `choose`
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
- `directory`
- `dom`
- `edit`
- `email`
- `emails`
- `example`
- `few`
- `fff`
- `file`
- `folder`
- `follow`
- `following`
- `getting`
- `hammer`
- `href`
- `http`
- `https`
- `icon`
- `image`
- `images`
- `img`
- `index`
- `init`
- `initialize`
- `inside`
- `install`
- `jpg`
- `json`
- `jsx`
- `live`
- `local`
- `localhost`
- `locally`
- `manager`
- `mdx`
- `mkdir`
- `monorepo`
- `monorepos`
- `next`
- `npm`
- `our`
- `package`
- `packages`
- `padding`
- `png`
- `pnpm`
- `powered`
- `project`
- `react`
- `recommend`
- `run`
- `script`
- `scripts`
- `see`
- `server`
- `setup`
- `sidebarTitle`
- `snippets`
- `src`
- `started`
- `starter`
- `static`
- `steps`
- `style`
- `template`
- `title`
- `tsx`
- `using`
- `yarn`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

