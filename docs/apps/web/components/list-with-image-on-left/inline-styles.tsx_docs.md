# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/list-with-image-on-left/inline-styles.tsx`
**Language:** tsx
**Size:** 5,284 bytes
**Lines:** 187
**Generated:** 2025-11-15T20:37:33.089425Z

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

- **Path:** `apps/web/components/list-with-image-on-left/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 5,284 bytes (5.16 KB)
- **Lines of Code:** 187

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
    <Preview>How Our Service Works: 5 Simple Steps</Preview>
    <Body
      style={{
        backgroundColor: 'rgb(255,255,255)',
      }}
    >
      <Container
        style={{
          backgroundColor: 'rgb(255,255,255)',
          borderRadius: '8px',
          marginLeft: 'auto',
          marginRight: 'auto',
          maxWidth: '600px',
          paddingLeft: '24px',
          paddingRight: '24px',
          paddingTop: '24px',
          paddingBottom: '0px',
        }}
      >
        <Heading
          as="h1"
          style={{
            fontSize: '24px',
            lineHeight: '32px',
            marginBottom: '42px',
            textAlign: 'center',
          }}
        >
          How Our Service Works: 5 Simple Steps
        </Heading>
        {[
          {
            number: 1,
            imageUrl: '/static/stagg-eletric-kettle.jpg',
            title: 'Start Your Search',
            description:
              'Search for the products you need or upload your list of requirements.',
            learnMoreLink: '#',
          },
          {
            number: 2,
            imageUrl: '/static/atmos-vacuum-canister.jpg',
            title: 'Compare & Save',
            description:
              'Compare prices and offers from different suppliers to find the best deals.',
            learnMoreLink: '#',
          },
          {
            number: 3,
            imageUrl: '/static/bundle-collection.jpg',
            title: 'Build Your Cart',
            description:
              'Select your desired items and add them to your shopping cart.',
            learnMoreLink: '#',
          },
          {
            number: 4,
            imageUrl: '/static/clara-french-press.jpg',
            title: 'Enjoy The Benefits',
            description:
              'Receive your products and enjoy the savings and convenience of our service.',
            learnMoreLink: '#',
          },
        ].map((step) => (
          <Section
            style={{
              marginBottom: '30px',
            }}
          >
            <Row style={{ marginBottom: '24px' }}>
              <Column
                width="40%"
                style={{ width: '40%', paddingRight: '24px' }}
              >
                <Img
                  src={step.imageUrl}
                  width="100%"
                  height="168"
                  alt={`Step image - ${step.number}`}
                  style={{
                    borderRadius: '4px',
                    display: 'block',
                    objectFit: 'cover',
                    objectPosition: 'center',
                    width: '100%',
                  }}
                />
              </Column>
              <Column
                width="60%"
                style={{ width: '60%', paddingRight: '24px' }}
              >
                <Row
                  width="24"
                  style={{
                    width: 24,
                    height: 24,
                    marginBottom: 18,
                  }}
                  align={undefined}
                >
                  <Column
                    width="24"
                    height="24"
                    style={{
                      borderRadius: '9999px',
                      height: 24,
                      width: 24,
                      backgroundColor: 'rgb(79,70,229)',
                      color: 'rgb(255,255,255)',
                      fontWeight: 600,
                      fontSize: 12,
                      lineHeight: 1,
                    }}
                    align="center"
                    valign="middle"
                  >
                    {step.number}
                  </Column>
                </Row>
                <Heading
                  as="h2"
                  style={{
                    fontSize: '20px',
                    fontWeight: '700',
                    lineHeight: '1',
                    marginBottom: '8px',
                    marginTop: '0px',
                  }}
                >
                  {step.title}
                </Heading>
                <Text
                  style={{
                    color: 'rgb(107,114,128)',
                    fontSize: '14px',
                    lineHeight: '24px',
                    margin: '0px',
                  }}
                >
                  {step.description}
                </Text>
                <Link
                  href={step.learnMoreLink}
                  style={{
                    color: 'rgb(79,70,229)',
                    display: 'block',
                    fontSize: '14px',
                    fontWeight: '600',
                    marginTop: '12px',
                    textDecorationLine: 'none',
                  }}
                >
                  Learn more →
                </Link>
              </Column>
            </Row>
          </Section>
        ))}
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

**Total Unique Identifiers:** 120

- `Benefits`
- `Body`
- `Build`
- `Cart`
- `Column`
- `Compare`
- `Container`
- `Enjoy`
- `Head`
- `Heading`
- `How`
- `Html`
- `Img`
- `Layout`
- `Learn`
- `Link`
- `Our`
- `Preview`
- `Receive`
- `Row`
- `Save`
- `Search`
- `Section`
- `Select`
- `Service`
- `Simple`
- `Start`
- `Step`
- `Steps`
- `Text`
- `Works`
- `Your`
- `_components`
- `add`
- `align`
- `alt`
- `atmos`
- `auto`
- `backgroundColor`
- `best`
- `block`
- `borderRadius`
- `bundle`
- `canister`
- `cart`
- `center`
- `clara`
- `collection`
- `color`
- `component`
- `components`
- `convenience`
- `cover`
- `deals`
- `description`
- `desired`
- `different`
- `display`
- `eletric`
- `email`
- `enjoy`
- `find`
- `fontSize`
- `fontWeight`
- `french`
- `height`
- `href`
- `image`
- `imageUrl`
- `items`
- `jpg`
- `kettle`
- `layout`
- `learnMoreLink`
- `lineHeight`
- `list`
- `map`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `maxWidth`
- `middle`
- `more`
- `need`
- `number`
- `objectFit`
- `objectPosition`
- `offers`
- `our`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `press`
- `prices`
- `products`
- `react`
- `requirements`
- `rgb`
- `savings`
- `service`
- `shopping`
- `src`
- `stagg`
- `static`
- `step`
- `style`
- `suppliers`
- `textAlign`
- `textDecorationLine`
- `them`
- `title`
- `upload`
- `vacuum`
- `valign`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

