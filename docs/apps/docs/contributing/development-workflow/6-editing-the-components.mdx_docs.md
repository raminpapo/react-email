# Documentation: 6-editing-the-components.mdx
**File Path:** `apps/docs/contributing/development-workflow/6-editing-the-components.mdx`
**Language:** Unknown
**Size:** 1,238 bytes
**Lines:** 45
**Generated:** 2025-11-15T20:37:32.729926Z

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

- **Path:** `apps/docs/contributing/development-workflow/6-editing-the-components.mdx`
- **Name:** `6-editing-the-components.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,238 bytes (1.21 KB)
- **Lines of Code:** 45

---

## Original Source

```
---
title: 'Editing the components'
sidebarTitle: '6. Editing the components'
'og:image': 'https://react.email/static/covers/react-email.png'
---

To facilitate developing components, use the built-in [playground](https://github.com/resend/react-email/tree/canary/playground), which automatically hot reloads when you make changes to the components during development.

## 1. Create an email template

Create a new file at `playground/emails/testing.tsx`

```tsx playground/emails/testing.tsx
import { Html, Head, Body, Tailwind, Text } from '@react-email/components';

export default function Testing() {
  return <Tailwind>
    <Html>
      <Head/>

      <Body className="bg-black text-white">
        <Text className="m-0 my-4 bg-cyan-200 text-slate-800">
          This is a testing email template.
        </Text>
      </Body>
    </Html>
  </Tailwind>;
}
```

<Tip>
The `.gitignore` file will ignore all changes in [playground/emails](https://github.com/resend/react-email/tree/canary/playground/emails) so you can test component changes and use cases in example templates without committing them to the repository.
</Tip>

## 2. Run playground server

```sh
pnpm dev
```

## 3. Open in your browser

Go to http://localhost:3000


```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 71

- `Body`
- `Create`
- `Editing`
- `Head`
- `Html`
- `Open`
- `Run`
- `Tailwind`
- `Testing`
- `Text`
- `Tip`
- `all`
- `automatically`
- `black`
- `browser`
- `built`
- `canary`
- `cases`
- `changes`
- `className`
- `com`
- `committing`
- `component`
- `components`
- `covers`
- `cyan`
- `dev`
- `developing`
- `development`
- `during`
- `email`
- `emails`
- `example`
- `facilitate`
- `file`
- `github`
- `gitignore`
- `hot`
- `http`
- `https`
- `ignore`
- `image`
- `localhost`
- `make`
- `playground`
- `png`
- `pnpm`
- `react`
- `reloads`
- `repository`
- `resend`
- `server`
- `sidebarTitle`
- `slate`
- `static`
- `template`
- `templates`
- `test`
- `testing`
- `text`
- `them`
- `title`
- `tree`
- `tsx`
- `use`
- `when`
- `which`
- `white`
- `without`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

