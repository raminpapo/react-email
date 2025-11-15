# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/article-with-image/inline-styles.tsx`
**Language:** tsx
**Size:** 1,915 bytes
**Lines:** 78
**Generated:** 2025-11-15T20:37:33.041108Z

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

- **Path:** `apps/web/components/article-with-image/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,915 bytes (1.87 KB)
- **Lines of Code:** 78

---

## Original Source

```tsx
import { Button, Heading, Img, Section, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section style={{ marginTop: 16, marginBottom: 16 }}>
    <Img
      alt="Herman Miller Chair"
      height="320"
      src="/static/herman-miller-chair.jpg"
      style={{
        width: '100%',
        borderRadius: 12,
        objectFit: 'cover',
      }}
    />
    <Section
      style={{
        marginTop: 32,
        textAlign: 'center',
      }}
    >
      <Text
        style={{
          marginTop: 16,
          marginBottom: 16,
          fontSize: 18,
          lineHeight: '28px',
          fontWeight: 600,
          color: 'rgb(79,70,229)',
        }}
      >
        Our new article
      </Text>
      <Heading
        as="h1"
        style={{
          margin: '0px',
          marginTop: 8,
          fontSize: 36,
          lineHeight: '36px',
          fontWeight: 600,
          color: 'rgb(17,24,39)',
        }}
      >
        Designing with Furniture
      </Heading>
      <Text
        style={{ fontSize: 16, lineHeight: '24px', color: 'rgb(107,114,128)' }}
      >
        Unleash your inner designer as we explore how furniture plays a vital
        role in creating stunning interiors, offering insights into choosing the
        right pieces, arranging them harmoniously, and infusing your space with
        personality.
      </Text>
      <Button
        href="https://react.email"
        style={{
          marginTop: 16,
          borderRadius: 8,
          backgroundColor: 'rgb(79,70,229)',
          paddingLeft: 40,
          paddingRight: 40,
          paddingTop: 12,
          paddingBottom: 12,
          fontWeight: 600,
          color: 'rgb(255,255,255)',
        }}
      >
        Read more
      </Button>
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

**Total Unique Identifiers:** 76

- `Button`
- `Chair`
- `Designing`
- `Furniture`
- `Heading`
- `Herman`
- `Img`
- `Layout`
- `Miller`
- `Our`
- `Read`
- `Section`
- `Text`
- `Unleash`
- `_components`
- `alt`
- `arranging`
- `article`
- `backgroundColor`
- `borderRadius`
- `center`
- `chair`
- `choosing`
- `color`
- `component`
- `components`
- `cover`
- `creating`
- `designer`
- `email`
- `explore`
- `fontSize`
- `fontWeight`
- `furniture`
- `harmoniously`
- `height`
- `herman`
- `how`
- `href`
- `https`
- `infusing`
- `inner`
- `insights`
- `interiors`
- `into`
- `jpg`
- `layout`
- `lineHeight`
- `margin`
- `marginBottom`
- `marginTop`
- `miller`
- `more`
- `objectFit`
- `offering`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `personality`
- `pieces`
- `plays`
- `react`
- `rgb`
- `right`
- `role`
- `space`
- `src`
- `static`
- `stunning`
- `style`
- `textAlign`
- `them`
- `vital`
- `width`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

