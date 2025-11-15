# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/header-and-three-centered-paragraphs/inline-styles.tsx`
**Language:** tsx
**Size:** 3,679 bytes
**Lines:** 160
**Generated:** 2025-11-15T20:37:33.005616Z

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

- **Path:** `apps/web/components/header-and-three-centered-paragraphs/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,679 bytes (3.59 KB)
- **Lines of Code:** 160

---

## Original Source

```tsx
import { Column, Img, Row, Section, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section
    style={{
      marginTop: 16,
      marginBottom: 16,
    }}
  >
    <Row>
      <Text
        style={{
          margin: '0px',
          fontSize: 24,
          lineHeight: '32px',
          fontWeight: 600,
          color: 'rgb(17,24,39)',
        }}
      >
        Modern Comfort
      </Text>
      <Text
        style={{
          marginTop: 8,
          fontSize: 16,
          lineHeight: '24px',
          color: 'rgb(107,114,128)',
        }}
      >
        Experience contemporary bliss with our sleek and cozy furniture
        collection, designed for optimal comfort and style
      </Text>
    </Row>
    <Row style={{ marginTop: 16 }}>
      <Column
        align="center"
        style={{
          width: '33.333333%',
          paddingRight: 12,
          verticalAlign: 'baseline',
        }}
      >
        <Img
          alt="heart icon"
          height="48"
          src="/static/heart-icon.png"
          width="48"
        />
        <Text
          style={{
            margin: '0px',
            marginTop: 16,
            fontSize: 20,
            lineHeight: '24px',
            fontWeight: 600,
            color: 'rgb(17,24,39)',
          }}
        >
          Timeless Charm
        </Text>
        <Text
          style={{
            marginBottom: '0px',
            marginTop: 8,
            fontSize: 16,
            lineHeight: '24px',
            color: 'rgb(107,114,128)',
          }}
        >
          Classic designs that never go out of style. Experience enduring
          elegance
        </Text>
      </Column>
      <Column
        align="center"
        style={{
          width: '33.333333%',
          paddingLeft: 12,
          verticalAlign: 'baseline',
        }}
      >
        <Img
          alt="rocket icon"
          height="48"
          src="/static/rocket-icon.png"
          width="48"
        />
        <Text
          style={{
            margin: '0px',
            marginTop: 16,
            fontSize: 20,
            lineHeight: '28px',
            fontWeight: 600,
            color: 'rgb(17,24,39)',
          }}
        >
          Functional Beauty
        </Text>
        <Text
          style={{
            marginBottom: '0px',
            marginTop: 8,
            fontSize: 16,
            lineHeight: '24px',
            color: 'rgb(107,114,128)',
          }}
        >
          Seamlessly blending form and function. Furniture that enhances your
          everyday life.
        </Text>
      </Column>
      <Column
        align="center"
        style={{
          width: '33.333333%',
          paddingLeft: 12,
          verticalAlign: 'baseline',
        }}
      >
        <Img
          alt="megaphone icon"
          height="48"
          src="/static/megaphone-icon.png"
          width="48"
        />
        <Text
          style={{
            margin: '0px',
            marginTop: 16,
            fontSize: 20,
            lineHeight: '28px',
            fontWeight: 600,
            color: 'rgb(17,24,39)',
          }}
        >
          Endless Comfort
        </Text>
        <Text
          style={{
            marginBottom: '0px',
            marginTop: 8,
            fontSize: 16,
            lineHeight: '24px',
            color: 'rgb(107,114,128)',
          }}
        >
          Sink into pure relaxation. Discover furniture that embraces your
          well-being.
        </Text>
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

**Total Unique Identifiers:** 76

- `Beauty`
- `Charm`
- `Classic`
- `Column`
- `Comfort`
- `Discover`
- `Endless`
- `Experience`
- `Functional`
- `Furniture`
- `Img`
- `Layout`
- `Modern`
- `Row`
- `Seamlessly`
- `Section`
- `Sink`
- `Text`
- `Timeless`
- `_components`
- `align`
- `alt`
- `baseline`
- `blending`
- `bliss`
- `center`
- `collection`
- `color`
- `comfort`
- `component`
- `components`
- `contemporary`
- `cozy`
- `designed`
- `designs`
- `elegance`
- `email`
- `embraces`
- `enduring`
- `enhances`
- `everyday`
- `fontSize`
- `fontWeight`
- `form`
- `furniture`
- `heart`
- `height`
- `icon`
- `into`
- `layout`
- `life`
- `lineHeight`
- `margin`
- `marginBottom`
- `marginTop`
- `megaphone`
- `never`
- `optimal`
- `our`
- `out`
- `paddingLeft`
- `paddingRight`
- `png`
- `pure`
- `react`
- `relaxation`
- `rgb`
- `rocket`
- `sleek`
- `src`
- `static`
- `style`
- `verticalAlign`
- `well`
- `width`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

