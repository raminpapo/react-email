# Documentation: tailwind.tsx
**File Path:** `apps/web/components/images-on-horizontal-grid/tailwind.tsx`
**Language:** tsx
**Size:** 2,007 bytes
**Lines:** 65
**Generated:** 2025-11-15T20:37:33.106771Z

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

- **Path:** `apps/web/components/images-on-horizontal-grid/tailwind.tsx`
- **Name:** `tailwind.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,007 bytes (1.96 KB)
- **Lines of Code:** 65

---

## Original Source

```tsx
import { Column, Img, Link, Row, Section, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section className="my-[16px]">
    <Section>
      <Row>
        <Text className="m-0 font-semibold text-[16px] text-indigo-600 leading-[24px]">
          Collections
        </Text>
        <Text className="m-0 mt-[8px] font-semibold text-[24px] text-gray-900 leading-[32px]">
          Bundle & Save
        </Text>
        <Text className="mt-[8px] text-[16px] text-gray-500 leading-[24px]">
          Award-winning grinders and burrs for brewing like a barista at home.
        </Text>
      </Row>
    </Section>
    <Section className="mt-[16px]">
      <Row className="mt-[16px]">
        <Column className="w-1/2 pr-[8px]">
          <Row className="pb-[8px]">
            <td>
              <Link href="#">
                <Img
                  alt="Grinder Collection"
                  className="w-full rounded-[12px] object-cover"
                  height={152}
                  src="/static/grinder-collection.jpg"
                />
              </Link>
            </td>
          </Row>
          <Row className="pt-[8px]">
            <td>
              <Link href="#">
                <Img
                  alt="Bundle Collection"
                  className="w-full rounded-[12px] object-cover"
                  height={152}
                  src="/static/bundle-collection.jpg"
                />
              </Link>
            </td>
          </Row>
        </Column>
        <Column className="w-1/2 py-[8px] pl-[8px]">
          <Link href="#">
            <Img
              alt="Clara French Press"
              className="w-full rounded-[12px] object-cover"
              height={152 + 152 + 8 + 8}
              src="/static/clara-french-press.jpg"
            />
          </Link>
        </Column>
      </Row>
    </Section>
  </Section>
);

export default () => {
  return <Layout>{component}</Layout>;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `component()`

### Dependencies

This file imports/requires:

- `../_components/layout`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 52

- `Award`
- `Bundle`
- `Clara`
- `Collection`
- `Collections`
- `Column`
- `French`
- `Grinder`
- `Img`
- `Layout`
- `Link`
- `Press`
- `Row`
- `Save`
- `Section`
- `Text`
- `_components`
- `alt`
- `barista`
- `brewing`
- `bundle`
- `burrs`
- `clara`
- `className`
- `collection`
- `component`
- `components`
- `cover`
- `email`
- `font`
- `french`
- `full`
- `gray`
- `grinder`
- `grinders`
- `height`
- `home`
- `href`
- `indigo`
- `jpg`
- `layout`
- `leading`
- `like`
- `object`
- `press`
- `react`
- `rounded`
- `semibold`
- `src`
- `static`
- `text`
- `winning`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

