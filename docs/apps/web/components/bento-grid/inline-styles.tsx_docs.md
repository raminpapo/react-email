# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/bento-grid/inline-styles.tsx`
**Language:** tsx
**Size:** 5,149 bytes
**Lines:** 181
**Generated:** 2025-11-15T20:37:33.123570Z

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

- **Path:** `apps/web/components/bento-grid/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 5,149 bytes (5.03 KB)
- **Lines of Code:** 181

---

## Original Source

```tsx
import {
  Body,
  Column,
  Container,
  Head,
  Heading,
  Html,
  Img,
  Link,
  Preview,
  Row,
  Section,
  Text,
} from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Html>
    <Head />
    <Preview>Coffee Storage</Preview>
    <Body>
      <Container
        style={{
          backgroundColor: 'rgb(255,255,255)',
          borderRadius: '8px',
          marginLeft: 'auto',
          marginRight: 'auto',
          maxWidth: '900px',
          overflow: 'hidden',
          padding: '0px',
        }}
      >
        <Section>
          <Row
            style={{
              backgroundColor: 'rgb(41,37,36)',
              borderCollapse: 'separate',
              borderSpacing: '24px',
              margin: '0px',
              tableLayout: 'fixed',
              width: '100%',
            }}
          >
            <Column style={{ paddingLeft: '12px' }}>
              <Heading
                as="h1"
                style={{
                  color: 'rgb(255,255,255)',
                  fontSize: '28px',
                  fontWeight: '700',
                  marginBottom: '10px',
                }}
              >
                Coffee Storage
              </Heading>
              <Text
                style={{
                  color: 'rgb(255,255,255,0.6)',
                  fontSize: '14px',
                  lineHeight: '20px',
                  margin: '0px',
                }}
              >
                Keep your coffee fresher for longer with innovative technology.
              </Text>
              <Link
                href="#"
                style={{
                  color: 'rgb(255,255,255,0.8)',
                  display: 'block',
                  fontSize: '14px',
                  lineHeight: '20px',
                  fontWeight: '600',
                  marginTop: '12px',
                  textDecorationLine: 'none',
                }}
              >
                Shop now →
              </Link>
            </Column>
            <Column style={{ width: '42%', height: '250px' }}>
              <Img
                src="/static/coffee-bean-storage.jpg"
                alt="Coffee Bean Storage"
                style={{
                  borderRadius: '4px',
                  height: '100%',
                  marginRight: '-6px',
                  objectFit: 'cover',
                  objectPosition: 'center',
                  width: '100%',
                }}
              />
            </Column>
          </Row>
        </Section>
        <Section
          style={{
            marginBottom: '24px',
          }}
        >
          <Row
            style={{
              borderCollapse: 'separate',
              borderSpacing: '12px',
              tableLayout: 'fixed',
              width: '100%',
            }}
          >
            {[
              {
                imageUrl: '/static/atmos-vacuum-canister.jpg',
                altText: 'Auto-Sealing Vacuum Canister',
                title: 'Auto-Sealing Vacuum Canister',
                description:
                  'A container that automatically creates an airtight seal with a button press.',
                linkUrl: '#',
              },
              {
                imageUrl: '/static/vacuum-canister-clear-glass-bundle.jpg',
                altText: '3-Pack Vacuum Containers',
                title: '3-Pack Vacuum Containers',
                description:
                  'Keep your coffee fresher for longer with this set of high-performance vacuum containers.',
                linkUrl: '#',
              },
            ].map((product) => (
              <Column
                key={product.title}
                style={{
                  marginLeft: 'auto',
                  marginRight: 'auto',
                  maxWidth: '180px',
                }}
              >
                <Img
                  src={product.imageUrl}
                  alt={product.altText}
                  style={{
                    borderRadius: '4px',
                    marginBottom: '18px',
                    width: '100%',
                  }}
                />
                <div>
                  <Heading
                    as="h2"
                    style={{
                      fontSize: '14px',
                      lineHeight: '20px',
                      fontWeight: '700',
                      marginBottom: '8px',
                    }}
                  >
                    {product.title}
                  </Heading>
                  <Text
                    style={{
                      color: 'rgb(107,114,128)',
                      fontSize: '12px',
                      lineHeight: '20px',
                      margin: '0px',
                      paddingRight: '12px',
                    }}
                  >
                    {product.description}
                  </Text>
                </div>
              </Column>
            ))}
          </Row>
        </Section>
      </Container>
    </Body>
  </Html>
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

**Total Unique Identifiers:** 104

- `Auto`
- `Bean`
- `Body`
- `Canister`
- `Coffee`
- `Column`
- `Container`
- `Containers`
- `Head`
- `Heading`
- `Html`
- `Img`
- `Keep`
- `Layout`
- `Link`
- `Pack`
- `Preview`
- `Row`
- `Sealing`
- `Section`
- `Shop`
- `Storage`
- `Text`
- `Vacuum`
- `_components`
- `airtight`
- `alt`
- `altText`
- `atmos`
- `auto`
- `automatically`
- `backgroundColor`
- `bean`
- `block`
- `borderCollapse`
- `borderRadius`
- `borderSpacing`
- `bundle`
- `button`
- `canister`
- `center`
- `clear`
- `coffee`
- `color`
- `component`
- `components`
- `container`
- `containers`
- `cover`
- `creates`
- `description`
- `display`
- `div`
- `email`
- `fixed`
- `fontSize`
- `fontWeight`
- `fresher`
- `glass`
- `height`
- `hidden`
- `high`
- `href`
- `imageUrl`
- `innovative`
- `jpg`
- `key`
- `layout`
- `lineHeight`
- `linkUrl`
- `longer`
- `map`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `maxWidth`
- `now`
- `objectFit`
- `objectPosition`
- `overflow`
- `padding`
- `paddingLeft`
- `paddingRight`
- `performance`
- `press`
- `product`
- `react`
- `rgb`
- `seal`
- `separate`
- `set`
- `src`
- `static`
- `storage`
- `style`
- `tableLayout`
- `technology`
- `textDecorationLine`
- `title`
- `vacuum`
- `width`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

