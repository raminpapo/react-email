# Documentation: section.mdx
**File Path:** `apps/docs/components/section.mdx`
**Language:** Unknown
**Size:** 1,319 bytes
**Lines:** 73
**Generated:** 2025-11-15T20:37:32.784392Z

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

- **Path:** `apps/docs/components/section.mdx`
- **Name:** `section.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,319 bytes (1.29 KB)
- **Lines of Code:** 73

---

## Original Source

```
---
title: "Section"
sidebarTitle: "Section"
description: "Display a section that can also be formatted using rows and columns."
"og:image": "https://react.email/static/covers/section.png"
icon: "rectangles-mixed"
---

import Support from '/snippets/support.mdx'

## Install

Install component from your command line.

<CodeGroup>

```sh npm
npm install @react-email/components -E

# or get the individual package

npm install @react-email/section -E
```

```sh yarn
yarn add @react-email/components -E

# or get the individual package

yarn add @react-email/section -E
```

```sh pnpm
pnpm add @react-email/components -E

# or get the individual package

pnpm add @react-email/section -E
```

</CodeGroup>

## Getting started

Add the component to your email template. Include styles where needed.

```jsx
import { Section, Column, Row, Text } from "@react-email/components";

const Email = () => {
  return (
    {/* A simple `section` */}
    <Section>
      <Text>Hello World</Text>
    </Section>

    {/* Formatted with `rows` and `columns` */}
     <Section>
      <Row>
        <Column>Column 1, Row 1</Column>
        <Column>Column 2, Row 1</Column>
      </Row>
      <Row>
        <Column>Column 1, Row 2</Column>
        <Column>Column 2, Row 2</Column>
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

**Total Unique Identifiers:** 57

- `Add`
- `CodeGroup`
- `Column`
- `Display`
- `Email`
- `Formatted`
- `Getting`
- `Hello`
- `Include`
- `Install`
- `Row`
- `Section`
- `Support`
- `Text`
- `World`
- `add`
- `also`
- `columns`
- `command`
- `component`
- `components`
- `covers`
- `description`
- `email`
- `formatted`
- `get`
- `https`
- `icon`
- `image`
- `individual`
- `install`
- `jsx`
- `line`
- `mdx`
- `mixed`
- `needed`
- `npm`
- `package`
- `png`
- `pnpm`
- `react`
- `rectangles`
- `rows`
- `section`
- `sidebarTitle`
- `simple`
- `snippets`
- `started`
- `static`
- `styles`
- `support`
- `template`
- `title`
- `using`
- `where`
- `yarn`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

