# Documentation: tailwind.tsx
**File Path:** `apps/web/components/footer-with-two-columns/tailwind.tsx`
**Language:** tsx
**Size:** 1,940 bytes
**Lines:** 64
**Generated:** 2025-11-15T20:37:33.062782Z

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

- **Path:** `apps/web/components/footer-with-two-columns/tailwind.tsx`
- **Name:** `tailwind.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,940 bytes (1.89 KB)
- **Lines of Code:** 64

---

## Original Source

```tsx
import { Column, Img, Link, Row, Section, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section>
    <Row>
      <Column colSpan={4}>
        <Img
          alt="React Email logo"
          height="42"
          src="/static/logo-without-background.png"
        />
        <Text className="my-[8px] font-semibold text-[16px] text-gray-900 leading-[24px]">
          Acme corporation
        </Text>
        <Text className="mt-[4px] mb-[0px] text-[16px] text-gray-500 leading-[24px]">
          Think different
        </Text>
      </Column>
      <Column align="left" className="table-cell align-bottom">
        <Row className="table-cell h-[44px] w-[56px] align-bottom">
          <Column className="pr-[8px]">
            <Link href="#">
              <Img
                alt="Facebook"
                height="36"
                src="/static/facebook-logo.png"
                width="36"
              />
            </Link>
          </Column>
          <Column className="pr-[8px]">
            <Link href="#">
              <Img alt="X" height="36" src="/static/x-logo.png" width="36" />
            </Link>
          </Column>
          <Column>
            <Link href="#">
              <Img
                alt="Instagram"
                height="36"
                src="/static/instagram-logo.png"
                width="36"
              />
            </Link>
          </Column>
        </Row>
        <Row>
          <Text className="my-[8px] font-semibold text-[16px] text-gray-500 leading-[24px]">
            123 Main Street Anytown, CA 12345
          </Text>
          <Text className="mt-[4px] mb-[0px] font-semibold text-[16px] text-gray-500 leading-[24px]">
            mail@example.com +123456789
          </Text>
        </Row>
      </Column>
    </Row>
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

**Total Unique Identifiers:** 51

- `Acme`
- `Anytown`
- `Column`
- `Email`
- `Facebook`
- `Img`
- `Instagram`
- `Layout`
- `Link`
- `Main`
- `React`
- `Row`
- `Section`
- `Street`
- `Text`
- `Think`
- `_components`
- `align`
- `alt`
- `background`
- `bottom`
- `cell`
- `className`
- `colSpan`
- `com`
- `component`
- `components`
- `corporation`
- `different`
- `email`
- `example`
- `facebook`
- `font`
- `gray`
- `height`
- `href`
- `instagram`
- `layout`
- `leading`
- `left`
- `logo`
- `mail`
- `png`
- `react`
- `semibold`
- `src`
- `static`
- `table`
- `text`
- `width`
- `without`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

