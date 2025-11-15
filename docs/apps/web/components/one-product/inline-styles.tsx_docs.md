# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/one-product/inline-styles.tsx`
**Language:** tsx
**Size:** 1,969 bytes
**Lines:** 84
**Generated:** 2025-11-15T20:37:32.991423Z

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

- **Path:** `apps/web/components/one-product/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,969 bytes (1.92 KB)
- **Lines of Code:** 84

---

## Original Source

```tsx
import { Button, Heading, Img, Section, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section style={{ marginTop: 16, marginBottom: 16 }}>
    <Img
      alt="Braun Collection"
      height={320}
      src="/static/braun-collection.jpg"
      style={{
        width: '100%',
        borderRadius: 12,
        objectFit: 'cover',
      }}
    />
    <Section style={{ marginTop: 32, textAlign: 'center' }}>
      <Text
        style={{
          marginTop: 16,
          fontSize: 18,
          lineHeight: '28px',
          fontWeight: 600,
          color: 'rgb(79,70,229)',
        }}
      >
        Classic Watches
      </Text>
      <Heading
        as="h1"
        style={{
          fontSize: 36,
          lineHeight: '40px',
          fontWeight: 600,
          letterSpacing: 0.4,
          color: 'rgb(17,24,39)',
        }}
      >
        Elegant Comfort
      </Heading>
      <Text
        style={{
          marginTop: 8,
          fontSize: 16,
          lineHeight: '24px',
          color: 'rgb(107,114,128)',
        }}
      >
        Dieter Rams’ work has an outstanding quality which distinguishes it from
        the vast majority of industrial design of the entire 20th Century.
      </Text>
      <Text
        style={{
          fontSize: 16,
          lineHeight: '24px',
          fontWeight: 600,
          color: 'rgb(17,24,39)',
        }}
      >
        $210.00
      </Text>
      <Button
        href="https://react.email"
        style={{
          marginTop: 16,
          borderRadius: 8,
          backgroundColor: 'rgb(79,70,229)',
          paddingLeft: 24,
          paddingRight: 24,
          paddingTop: 12,
          paddingBottom: 12,
          fontWeight: 600,
          color: 'rgb(255,255,255)',
        }}
      >
        Buy now
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

**Total Unique Identifiers:** 62

- `Braun`
- `Button`
- `Buy`
- `Century`
- `Classic`
- `Collection`
- `Comfort`
- `Dieter`
- `Elegant`
- `Heading`
- `Img`
- `Layout`
- `Rams`
- `Section`
- `Text`
- `Watches`
- `_components`
- `alt`
- `backgroundColor`
- `borderRadius`
- `braun`
- `center`
- `collection`
- `color`
- `component`
- `components`
- `cover`
- `design`
- `distinguishes`
- `email`
- `entire`
- `fontSize`
- `fontWeight`
- `height`
- `href`
- `https`
- `industrial`
- `jpg`
- `layout`
- `letterSpacing`
- `lineHeight`
- `majority`
- `marginBottom`
- `marginTop`
- `now`
- `objectFit`
- `outstanding`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `quality`
- `react`
- `rgb`
- `src`
- `static`
- `style`
- `textAlign`
- `vast`
- `which`
- `width`
- `work`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

