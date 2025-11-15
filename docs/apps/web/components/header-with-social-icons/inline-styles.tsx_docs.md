# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/header-with-social-icons/inline-styles.tsx`
**Language:** tsx
**Size:** 1,718 bytes
**Lines:** 72
**Generated:** 2025-11-15T20:37:33.072528Z

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

- **Path:** `apps/web/components/header-with-social-icons/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,718 bytes (1.68 KB)
- **Lines of Code:** 72

---

## Original Source

```tsx
import { Column, Img, Link, Row, Section } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section
    style={{
      paddingTop: 40,
      paddingBottom: 40,
      paddingLeft: 32,
      paddingRight: 32,
    }}
  >
    <Row>
      <Column style={{ width: '80%' }}>
        <Img
          alt="React Email logo"
          width="42"
          height="42"
          src="/static/logo-without-background.png"
        />
      </Column>
      <Column align="right">
        <Row align="right">
          <Column>
            <Link href="#">
              <Img
                alt="X"
                height="36"
                src="/static/x-logo.png"
                style={{
                  marginLeft: 4,
                  marginRight: 4,
                }}
                width="36"
              />
            </Link>
          </Column>
          <Column>
            <Link href="#">
              <Img
                alt="Instagram"
                height="36"
                src="/static/instagram-logo.png"
                style={{
                  marginLeft: 4,
                  marginRight: 4,
                }}
                width="36"
              />
            </Link>
          </Column>
          <Column>
            <Link href="#">
              <Img
                alt="Facebook"
                height="36"
                src="/static/facebook-logo.png"
                style={{ marginLeft: 4, marginRight: 4 }}
                width="36"
              />
            </Link>
          </Column>
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

**Total Unique Identifiers:** 37

- `Column`
- `Email`
- `Facebook`
- `Img`
- `Instagram`
- `Layout`
- `Link`
- `React`
- `Row`
- `Section`
- `_components`
- `align`
- `alt`
- `background`
- `component`
- `components`
- `email`
- `facebook`
- `height`
- `href`
- `instagram`
- `layout`
- `logo`
- `marginLeft`
- `marginRight`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `png`
- `react`
- `right`
- `src`
- `static`
- `style`
- `width`
- `without`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

