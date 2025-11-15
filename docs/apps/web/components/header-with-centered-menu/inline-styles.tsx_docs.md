# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/header-with-centered-menu/inline-styles.tsx`
**Language:** tsx
**Size:** 2,014 bytes
**Lines:** 82
**Generated:** 2025-11-15T20:37:33.001705Z

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

- **Path:** `apps/web/components/header-with-centered-menu/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,014 bytes (1.97 KB)
- **Lines of Code:** 82

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
      <Column align="center">
        <Img
          alt="React Email logo"
          height="42"
          src="/static/logo-without-background.png"
        />
      </Column>
    </Row>
    <Row style={{ marginTop: 40 }}>
      <Column align="center">
        <table>
          <tr>
            <td style={{ paddingRight: 8, paddingLeft: 8 }}>
              <Link
                href="#"
                style={{
                  color: 'rgb(75,85,99)',
                  textDecoration: 'none',
                }}
              >
                About
              </Link>
            </td>
            <td style={{ paddingRight: 8, paddingLeft: 8 }}>
              <Link
                href="#"
                style={{
                  color: 'rgb(75,85,99)',
                  textDecoration: 'none',
                }}
              >
                Blog
              </Link>
            </td>
            <td style={{ paddingRight: 8, paddingLeft: 8 }}>
              <Link
                href="#"
                style={{
                  color: 'rgb(75,85,99)',
                  textDecoration: 'none',
                }}
              >
                Company
              </Link>
            </td>
            <td style={{ paddingRight: 8, paddingLeft: 8 }}>
              <Link
                href="#"
                style={{
                  color: 'rgb(75,85,99)',
                  textDecoration: 'none',
                }}
              >
                Features
              </Link>
            </td>
          </tr>
        </table>
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

**Total Unique Identifiers:** 40

- `About`
- `Blog`
- `Column`
- `Company`
- `Email`
- `Features`
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
- `center`
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
- `src`
- `static`
- `style`
- `table`
- `textDecoration`
- `without`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

