# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/footer-with-two-columns/inline-styles.tsx`
**Language:** tsx
**Size:** 2,698 bytes
**Lines:** 109
**Generated:** 2025-11-15T20:37:33.061402Z

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

- **Path:** `apps/web/components/footer-with-two-columns/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,698 bytes (2.63 KB)
- **Lines of Code:** 109

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
        <Text
          style={{
            marginTop: 8,
            marginBottom: 8,
            fontSize: 16,
            lineHeight: '24px',
            fontWeight: 600,
            color: 'rgb(17,24,39)',
          }}
        >
          Acme corporation
        </Text>
        <Text
          style={{
            marginTop: 4,
            marginBottom: '0px',
            fontSize: 16,
            lineHeight: '24px',
            color: 'rgb(107,114,128)',
          }}
        >
          Think different
        </Text>
      </Column>
      <Column
        align="left"
        style={{ display: 'table-cell', verticalAlign: 'bottom' }}
      >
        <Row
          style={{
            display: 'table-cell',
            height: 44,
            width: 56,
            verticalAlign: 'bottom',
          }}
        >
          <Column style={{ paddingRight: 8 }}>
            <Link href="#">
              <Img
                alt="Facebook"
                height="36"
                src="/static/facebook-logo.png"
                width="36"
              />
            </Link>
          </Column>
          <Column style={{ paddingRight: 8 }}>
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
          <Text
            style={{
              marginTop: 8,
              marginBottom: 8,
              fontSize: 16,
              lineHeight: '24px',
              fontWeight: 600,
              color: 'rgb(107,114,128)',
            }}
          >
            123 Main Street Anytown, CA 12345
          </Text>
          <Text
            style={{
              marginTop: 4,
              marginBottom: '0px',
              fontSize: 16,
              lineHeight: '24px',
              fontWeight: 600,
              color: 'rgb(107,114,128)',
            }}
          >
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

**Total Unique Identifiers:** 56

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
- `colSpan`
- `color`
- `com`
- `component`
- `components`
- `corporation`
- `different`
- `display`
- `email`
- `example`
- `facebook`
- `fontSize`
- `fontWeight`
- `height`
- `href`
- `instagram`
- `layout`
- `left`
- `lineHeight`
- `logo`
- `mail`
- `marginBottom`
- `marginTop`
- `paddingRight`
- `png`
- `react`
- `rgb`
- `src`
- `static`
- `style`
- `table`
- `verticalAlign`
- `width`
- `without`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

