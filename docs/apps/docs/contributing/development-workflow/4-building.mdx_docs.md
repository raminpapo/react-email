# Documentation: 4-building.mdx
**File Path:** `apps/docs/contributing/development-workflow/4-building.mdx`
**Language:** Unknown
**Size:** 1,318 bytes
**Lines:** 28
**Generated:** 2025-11-15T20:37:32.727235Z

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

- **Path:** `apps/docs/contributing/development-workflow/4-building.mdx`
- **Name:** `4-building.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,318 bytes (1.29 KB)
- **Lines of Code:** 28

---

## Original Source

```
---
title: "Building"
sidebarTitle: "4. Building"
"og:image": "https://react.email/static/covers/react-email.png"
description: "How we build each package before publishing"
---

We use [tsup](https://github.com/egoist/tsup) to build most packages. (The only exception for this is the `@react-email/tailwind` package which currently uses `vite` due to a few issues with `tsup` and `tailwindcss`'s bundling.)

To build a package run:

```bash package/* (ex: package/render)
pnpm build
```

Building in each package will run `tsup` with a few settings, typically `src/index.ts --format esm,cjs --dts --external react`.
Tsup handles building both [ESM](https://nodejs.org/api/esm.html) and
[CJS](https://nodejs.org/docs/latest/api/modules.html) versions along with the type definitions exported from the entry point, `src/index.ts`, without bundling `react`, which can cause issues.

### Why build before publishing?

We build most of the packages before publishing for a few reasons:

1. All the exported types can be imported from the same place the JavaScript is imported
2. We have proper [CommonJS](https://nodejs.org/docs/latest/api/modules.html#modules-commonjs-modules)
and [ES Modules](https://nodejs.org/api/esm.html#modules-ecmascript-modules) support
3. Code that isn't exported is not published or downloaded

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 87

- `All`
- `Building`
- `Code`
- `CommonJS`
- `How`
- `JavaScript`
- `Modules`
- `Tsup`
- `Why`
- `along`
- `api`
- `bash`
- `before`
- `both`
- `build`
- `building`
- `bundling`
- `cause`
- `cjs`
- `com`
- `commonjs`
- `covers`
- `currently`
- `definitions`
- `description`
- `docs`
- `downloaded`
- `dts`
- `due`
- `each`
- `ecmascript`
- `egoist`
- `email`
- `entry`
- `esm`
- `exception`
- `exported`
- `external`
- `few`
- `format`
- `github`
- `handles`
- `html`
- `https`
- `image`
- `imported`
- `index`
- `isn`
- `issues`
- `latest`
- `modules`
- `most`
- `nodejs`
- `only`
- `org`
- `package`
- `packages`
- `place`
- `png`
- `pnpm`
- `point`
- `proper`
- `published`
- `publishing`
- `react`
- `reasons`
- `render`
- `run`
- `same`
- `settings`
- `sidebarTitle`
- `src`
- `static`
- `support`
- `tailwind`
- `tailwindcss`
- `title`
- `tsup`
- `type`
- `types`
- `typically`
- `use`
- `uses`
- `versions`
- `vite`
- `which`
- `without`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

