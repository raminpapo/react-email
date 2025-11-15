# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/article-with-two-cards/inline-styles.tsx`
**Language:** tsx
**Size:** 3,874 bytes
**Lines:** 155
**Generated:** 2025-11-15T20:37:33.132645Z

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

- **Path:** `apps/web/components/article-with-two-cards/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,874 bytes (3.78 KB)
- **Lines of Code:** 155

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
          fontSize: 20,
          lineHeight: '28px',
          fontWeight: 600,
          color: 'rgb(17,24,39)',
        }}
      >
        Elevate Outdoor Living
      </Text>
      <Text
        style={{
          marginTop: 8,
          fontSize: 16,
          lineHeight: '24px',
          color: 'rgb(107,114,128)',
        }}
      >
        Take your outdoor space to new heights with our premium outdoor
        furniture, designed to elevate your alfresco experience.
      </Text>
    </Row>
    <Row
      style={{
        marginTop: 16,
      }}
    >
      <Column
        colSpan={1}
        style={{
          width: '50%',
          verticalAlign: 'baseline',
          paddingRight: 8,
          boxSizing: 'border-box',
        }}
      >
        <Img
          alt="A picture of a pink background with varios items laid out. Shoes, lipstick, sunglasses, some leafs and part of a purse."
          height="180"
          src="/static/outdoor-living.jpg"
          style={{
            width: '100%',
            borderRadius: 8,
            objectFit: 'cover',
          }}
        />
        <Text
          style={{
            fontSize: 16,
            lineHeight: '24px',
            fontWeight: 600,
            color: 'rgb(79,70,229)',
          }}
        >
          What's new
        </Text>
        <Text
          style={{
            margin: '0px',
            fontSize: 20,
            lineHeight: '28px',
            fontWeight: 600,
            color: 'rgb(17,24,39)',
          }}
        >
          Multifunctional Marvels
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
          Discover the innovative world of multifunctional furniture, where
          style meets practicality, offering creative solutions for maximizing
          space and enhancing functionality in your home
        </Text>
      </Column>
      <Column
        colSpan={1}
        style={{
          width: '50%',
          verticalAlign: 'baseline',
          paddingLeft: 8,
          boxSizing: 'border-box',
        }}
      >
        <Img
          alt="A picture of a pink background with varios items laid out. Shoes, lipstick, sunglasses, some leafs and part of a purse."
          height="180"
          src="/static/outdoor-living.jpg"
          style={{
            width: '100%',
            borderRadius: 8,
            objectFit: 'cover',
          }}
        />
        <Text
          style={{
            fontSize: 16,
            lineHeight: '24px',
            fontWeight: 600,
            color: 'rgb(79,70,229)',
          }}
        >
          What's new
        </Text>
        <Text
          style={{
            margin: '0px',
            fontSize: 20,
            lineHeight: '28px',
            fontWeight: 600,
            color: 'rgb(17,24,39)',
          }}
        >
          Timeless Classics
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
          Step into the world of timeless classics as we explore iconic
          furniture pieces that have stood the test of time, adding enduring
          elegance and sophistication to any interior
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

**Total Unique Identifiers:** 103

- `Classics`
- `Column`
- `Discover`
- `Elevate`
- `Img`
- `Layout`
- `Living`
- `Marvels`
- `Multifunctional`
- `Outdoor`
- `Row`
- `Section`
- `Shoes`
- `Step`
- `Take`
- `Text`
- `Timeless`
- `What`
- `_components`
- `adding`
- `alfresco`
- `alt`
- `any`
- `background`
- `baseline`
- `border`
- `borderRadius`
- `box`
- `boxSizing`
- `classics`
- `colSpan`
- `color`
- `component`
- `components`
- `cover`
- `creative`
- `designed`
- `elegance`
- `elevate`
- `email`
- `enduring`
- `enhancing`
- `experience`
- `explore`
- `fontSize`
- `fontWeight`
- `functionality`
- `furniture`
- `height`
- `heights`
- `home`
- `iconic`
- `innovative`
- `interior`
- `into`
- `items`
- `jpg`
- `laid`
- `layout`
- `leafs`
- `lineHeight`
- `lipstick`
- `living`
- `margin`
- `marginBottom`
- `marginTop`
- `maximizing`
- `meets`
- `multifunctional`
- `objectFit`
- `offering`
- `our`
- `out`
- `outdoor`
- `paddingLeft`
- `paddingRight`
- `part`
- `picture`
- `pieces`
- `pink`
- `practicality`
- `premium`
- `purse`
- `react`
- `rgb`
- `solutions`
- `some`
- `sophistication`
- `space`
- `src`
- `static`
- `stood`
- `style`
- `sunglasses`
- `test`
- `time`
- `timeless`
- `varios`
- `verticalAlign`
- `where`
- `width`
- `world`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

