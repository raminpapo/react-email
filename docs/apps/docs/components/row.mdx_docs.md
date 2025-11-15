# Documentation: row.mdx
**File Path:** `apps/docs/components/row.mdx`
**Language:** Unknown
**Size:** 1,086 bytes
**Lines:** 68
**Generated:** 2025-11-15T20:37:32.783233Z

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

- **Path:** `apps/docs/components/row.mdx`
- **Name:** `row.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,086 bytes (1.06 KB)
- **Lines of Code:** 68

---

## Original Source

```
---
title: "Row"
sidebarTitle: "Row"
description: "Display a row that separates content areas horizontally in your email."
"og:image": "https://react.email/static/covers/row.png"
icon: "table-rows"
---

import Support from '/snippets/support.mdx'

## Install

Install component from your command line.

<CodeGroup>

```sh npm
npm install @react-email/components -E

# or get the individual package

npm install @react-email/row -E
```

```sh yarn
yarn add @react-email/components -E

# or get the individual package

yarn add @react-email/row -E
```

```sh pnpm
pnpm add @react-email/components -E

# or get the individual package

pnpm add @react-email/row -E
```

</CodeGroup>

## Getting started

Add the component to your email template. Include styles where needed.

```jsx
import { Row, Column, Section } from "@react-email/components";

const Email = () => {
  return (
    <Section>
      <Row>
        <Column>A</Column>
      </Row>
      <Row>
        <Column>B</Column>
      </Row>
      <Row>
        <Column>C</Column>
      </Row>
    </Section>
  );
};
```

<Support/>

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `/snippets/support.mdx`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 51

- `Add`
- `CodeGroup`
- `Column`
- `Display`
- `Email`
- `Getting`
- `Include`
- `Install`
- `Row`
- `Section`
- `Support`
- `add`
- `areas`
- `command`
- `component`
- `components`
- `content`
- `covers`
- `description`
- `email`
- `get`
- `horizontally`
- `https`
- `icon`
- `image`
- `individual`
- `install`
- `jsx`
- `line`
- `mdx`
- `needed`
- `npm`
- `package`
- `png`
- `pnpm`
- `react`
- `row`
- `rows`
- `separates`
- `sidebarTitle`
- `snippets`
- `started`
- `static`
- `styles`
- `support`
- `table`
- `template`
- `title`
- `where`
- `yarn`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

