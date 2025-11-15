# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/header-with-side-menu/inline-styles.tsx`
**Language:** tsx
**Size:** 1,457 bytes
**Lines:** 58
**Generated:** 2025-11-15T20:37:32.989058Z

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

- **Path:** `apps/web/components/header-with-side-menu/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,457 bytes (1.42 KB)
- **Lines of Code:** 58

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
      marginTop: 40,
      marginBottom: 40,
    }}
  >
    <Row>
      <Column style={{ width: '80%' }}>
        <Img
          alt="React Email logo"
          height="42"
          src="/static/logo-without-background.png"
        />
      </Column>
      <Column align="right">
        <Row align="right">
          <Column style={{ paddingLeft: 8, paddingRight: 8 }}>
            <Link
              href="#"
              style={{ color: 'rgb(75,85,99)', textDecoration: 'none' }}
            >
              About
            </Link>
          </Column>
          <Column style={{ paddingLeft: 8, paddingRight: 8 }}>
            <Link
              href="#"
              style={{ color: 'rgb(75,85,99)', textDecoration: 'none' }}
            >
              Company
            </Link>
          </Column>
          <Column style={{ paddingLeft: 8, paddingRight: 8 }}>
            <Link
              href="#"
              style={{ color: 'rgb(75,85,99)', textDecoration: 'none' }}
            >
              Blog
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

**Total Unique Identifiers:** 39

- `About`
- `Blog`
- `Column`
- `Company`
- `Email`
- `Img`
- `Layout`
- `Link`
- `React`
- `Row`
- `Section`
- `_components`
- `align`
- `alt`
- `background`
- `color`
- `component`
- `components`
- `email`
- `height`
- `href`
- `layout`
- `logo`
- `marginBottom`
- `marginTop`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `png`
- `react`
- `rgb`
- `right`
- `src`
- `static`
- `style`
- `textDecoration`
- `width`
- `without`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

