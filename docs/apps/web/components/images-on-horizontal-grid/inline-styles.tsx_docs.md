# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/images-on-horizontal-grid/inline-styles.tsx`
**Language:** tsx
**Size:** 2,811 bytes
**Lines:** 108
**Generated:** 2025-11-15T20:37:33.105433Z

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

- **Path:** `apps/web/components/images-on-horizontal-grid/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,811 bytes (2.75 KB)
- **Lines of Code:** 108

---

## Original Source

```tsx
import { Column, Img, Link, Row, Section, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section style={{ marginTop: 16, marginBottom: 16 }}>
    <Section>
      <Row>
        <Text
          style={{
            margin: '0px',
            fontSize: 16,
            lineHeight: '24px',
            fontWeight: 600,
            color: 'rgb(79,70,229)',
          }}
        >
          Collections
        </Text>
        <Text
          style={{
            margin: '0px',
            marginTop: 8,
            fontSize: 24,
            lineHeight: '32px',
            fontWeight: 600,
            color: 'rgb(17,24,39)',
          }}
        >
          Bundle & Save
        </Text>
        <Text
          style={{
            marginTop: 8,
            fontSize: 16,
            lineHeight: '24px',
            color: 'rgb(107,114,128)',
          }}
        >
          Award-winning grinders and burrs for brewing like a barista at home.
        </Text>
      </Row>
    </Section>
    <Section style={{ marginTop: 16 }}>
      <Row style={{ marginTop: 16 }}>
        <Column style={{ width: '50%', paddingRight: 8 }}>
          <Row style={{ paddingBottom: 8 }}>
            <td>
              <Link href="#">
                <Img
                  alt="Grinder Collection"
                  height={152}
                  src="/static/grinder-collection.jpg"
                  style={{
                    width: '100%',
                    borderRadius: 12,
                    objectFit: 'cover',
                  }}
                />
              </Link>
            </td>
          </Row>
          <Row style={{ paddingTop: 8 }}>
            <td>
              <Link href="#">
                <Img
                  alt="Bundle Collection"
                  height={152}
                  src="/static/bundle-collection.jpg"
                  style={{
                    width: '100%',
                    borderRadius: 12,
                    objectFit: 'cover',
                  }}
                />
              </Link>
            </td>
          </Row>
        </Column>
        <Column
          style={{
            width: '50%',
            paddingLeft: 8,
            paddingTop: 8,
            paddingBottom: 8,
          }}
        >
          <Link href="#">
            <Img
              alt="Clara French Press"
              height={152 + 152 + 8 + 8}
              src="/static/clara-french-press.jpg"
              style={{
                width: '100%',
                borderRadius: 12,
                objectFit: 'cover',
              }}
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

**Total Unique Identifiers:** 58

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
- `borderRadius`
- `brewing`
- `bundle`
- `burrs`
- `clara`
- `collection`
- `color`
- `component`
- `components`
- `cover`
- `email`
- `fontSize`
- `fontWeight`
- `french`
- `grinder`
- `grinders`
- `height`
- `home`
- `href`
- `jpg`
- `layout`
- `like`
- `lineHeight`
- `margin`
- `marginBottom`
- `marginTop`
- `objectFit`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `press`
- `react`
- `rgb`
- `src`
- `static`
- `style`
- `width`
- `winning`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

