# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/article-with-image-on-right/inline-styles.tsx`
**Language:** tsx
**Size:** 2,025 bytes
**Lines:** 85
**Generated:** 2025-11-15T20:37:33.043809Z

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

- **Path:** `apps/web/components/article-with-image-on-right/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,025 bytes (1.98 KB)
- **Lines of Code:** 85

---

## Original Source

```tsx
import { Img, Link, Section, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section
    style={{ marginTop: '16px', textAlign: 'center', marginBottom: '16px' }}
  >
    <Section
      style={{
        display: 'inline-block',
        textAlign: 'left',
        width: '100%',
        maxWidth: 250,
        verticalAlign: 'top',
      }}
    >
      <Text
        style={{
          margin: '0px',
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
          marginTop: '8px',
          fontSize: 20,
          lineHeight: '28px',
          fontWeight: 600,
          color: 'rgb(17,24,39)',
        }}
      >
        Versatile Comfort
      </Text>
      <Text
        style={{
          marginTop: 8,
          fontSize: 16,
          lineHeight: '24px',
          color: 'rgb(107,114,128)',
        }}
      >
        Experience ultimate comfort and versatility with our furniture
        collection, designed to adapt to your ever-changing needs.
      </Text>
      <Link
        href="https://react.email"
        style={{ color: 'rgb(79,70,229)', textDecorationLine: 'underline' }}
      >
        Read more
      </Link>
    </Section>
    <Section
      style={{
        display: 'inline-block',
        marginTop: 8,
        marginBottom: 8,
        width: '100%',
        maxWidth: 220,
        verticalAlign: 'top',
      }}
    >
      <Img
        alt="An aesthetic picture taken of an Iphone, flowers, glasses and a card that reads 'Gucci, bloom' coming out of a leathered bag with a ziper"
        height={220}
        src="/static/versatile-comfort.jpg"
        style={{
          borderRadius: 8,
          objectFit: 'cover',
        }}
        width={220}
      />
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

- `Comfort`
- `Experience`
- `Gucci`
- `Img`
- `Iphone`
- `Layout`
- `Link`
- `Read`
- `Section`
- `Text`
- `Versatile`
- `What`
- `_components`
- `adapt`
- `aesthetic`
- `alt`
- `bag`
- `block`
- `bloom`
- `borderRadius`
- `card`
- `center`
- `changing`
- `collection`
- `color`
- `comfort`
- `coming`
- `component`
- `components`
- `cover`
- `designed`
- `display`
- `email`
- `ever`
- `flowers`
- `fontSize`
- `fontWeight`
- `furniture`
- `glasses`
- `height`
- `href`
- `https`
- `inline`
- `jpg`
- `layout`
- `leathered`
- `left`
- `lineHeight`
- `margin`
- `marginBottom`
- `marginTop`
- `maxWidth`
- `more`
- `needs`
- `objectFit`
- `our`
- `out`
- `picture`
- `react`
- `reads`
- `rgb`
- `src`
- `static`
- `style`
- `taken`
- `textAlign`
- `textDecorationLine`
- `top`
- `ultimate`
- `underline`
- `versatile`
- `versatility`
- `verticalAlign`
- `width`
- `your`
- `ziper`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

