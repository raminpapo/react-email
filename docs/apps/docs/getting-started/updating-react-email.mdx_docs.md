# Documentation: updating-react-email.mdx
**File Path:** `apps/docs/getting-started/updating-react-email.mdx`
**Language:** Unknown
**Size:** 1,313 bytes
**Lines:** 26
**Generated:** 2025-11-15T20:37:32.735342Z

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

- **Path:** `apps/docs/getting-started/updating-react-email.mdx`
- **Name:** `updating-react-email.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,313 bytes (1.28 KB)
- **Lines of Code:** 26

---

## Original Source

```
---
title: 'Updating React Email'
sidebarTitle: 'Updating React Email'
description: 'How to update from React Email 4.0 to 5.0'
'og:image': 'https://react.email/static/covers/react-email.png'
icon: 'arrow-up-wide-short'
---

import NextSteps from '/snippets/next-steps.mdx';

## Update from React Email 4.0 to 5.0

1. Update your React Email packages: `npm install @react-email/components@latest react-email@latest`.
2. Replace all `renderAsync` uses with `render`.

Make sure you update `@react-email/components` alongside `react-email`. The compatibility checker now only supports Tailwind 4, so you need to update both in sync.

### Tailwind 4

This update includes Tailwind 4 via `@react-email/components@latest`. Some utilities have changed since Tailwind 3—review their [upgrade guide](https://tailwindcss.com/docs/upgrade-guide#changes-from-v3) to adjust your code if needed.

Tailwind 4 also changes how classes are handled in components. Previously, passing `className` added an equivalent inlined `style` prop, which caused confusion and performance issues. Now, styles are only inlined on elements, not components. If you were merging utilities with the `style` prop, consider using [tailwind-merge](https://github.com/dcastil/tailwind-merge) instead.

The configuration remains in the `config` prop.


```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `/snippets/next-steps.mdx`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 97

- `Email`
- `How`
- `Make`
- `NextSteps`
- `Now`
- `Previously`
- `React`
- `Replace`
- `Some`
- `Tailwind`
- `Update`
- `Updating`
- `added`
- `adjust`
- `all`
- `alongside`
- `also`
- `arrow`
- `both`
- `caused`
- `changed`
- `changes`
- `checker`
- `className`
- `classes`
- `code`
- `com`
- `compatibility`
- `components`
- `config`
- `configuration`
- `confusion`
- `consider`
- `covers`
- `dcastil`
- `description`
- `docs`
- `elements`
- `email`
- `equivalent`
- `github`
- `guide`
- `handled`
- `how`
- `https`
- `icon`
- `image`
- `includes`
- `inlined`
- `install`
- `instead`
- `issues`
- `latest`
- `mdx`
- `merge`
- `merging`
- `need`
- `needed`
- `next`
- `now`
- `npm`
- `only`
- `packages`
- `passing`
- `performance`
- `png`
- `prop`
- `react`
- `remains`
- `render`
- `renderAsync`
- `review`
- `short`
- `sidebarTitle`
- `since`
- `snippets`
- `static`
- `steps`
- `style`
- `styles`
- `supports`
- `sure`
- `sync`
- `tailwind`
- `tailwindcss`
- `their`
- `title`
- `update`
- `upgrade`
- `uses`
- `using`
- `utilities`
- `via`
- `which`
- `wide`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

