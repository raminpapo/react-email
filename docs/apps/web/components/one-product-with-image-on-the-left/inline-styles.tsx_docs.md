# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/one-product-with-image-on-the-left/inline-styles.tsx`
**Language:** tsx
**Size:** 2,477 bytes
**Lines:** 89
**Generated:** 2025-11-15T20:37:32.986221Z

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

- **Path:** `apps/web/components/one-product-with-image-on-the-left/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,477 bytes (2.42 KB)
- **Lines of Code:** 89

---

## Original Source

```tsx
import { Button, Img, Section, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section style={{ marginTop: 16, marginBottom: 16 }}>
    <table style={{ width: '100%' }}>
      <tbody style={{ width: '100%' }}>
        <tr style={{ width: '100%' }}>
          <td
            style={{
              width: '50%',
              paddingRight: 32,
              boxSizing: 'border-box',
            }}
          >
            <Img
              alt="Braun Vintage"
              height={220}
              src="/static/braun-vintage.jpg"
              style={{
                borderRadius: 8,
                width: '100%',
                objectFit: 'cover',
              }}
            />
          </td>
          <td style={{ width: '50%', verticalAlign: 'baseline' }}>
            <Text
              style={{
                margin: '0px',
                marginTop: 8,
                fontSize: 20,
                lineHeight: '28px',
                fontWeight: 600,
                color: 'rgb(17,24,39)',
              }}
            >
              Great Timepiece
            </Text>
            <Text
              style={{
                marginTop: 8,
                fontSize: 16,
                lineHeight: '24px',
                color: 'rgb(107,114,128)',
              }}
            >
              Renowned for their minimalist design and high functionality,
              celebrating the principles of simplicity and clarity.
            </Text>
            <Text
              style={{
                marginTop: 8,
                fontSize: 18,
                lineHeight: '28px',
                fontWeight: 600,
                color: 'rgb(17,24,39)',
              }}
            >
              $120.00
            </Text>
            <Button
              href="https://react.email"
              style={{
                width: '75%',
                borderRadius: 8,
                backgroundColor: 'rgb(79,70,229)',
                paddingTop: 12,
                paddingBottom: 12,
                paddingLeft: 16,
                paddingRight: 16,
                textAlign: 'center',
                fontWeight: 600,
                color: 'rgb(255,255,255)',
              }}
            >
              Buy
            </Button>
          </td>
        </tr>
      </tbody>
    </table>
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
- `Great`
- `Img`
- `Layout`
- `Renowned`
- `Section`
- `Text`
- `Timepiece`
- `Vintage`
- `_components`
- `alt`
- `backgroundColor`
- `baseline`
- `border`
- `borderRadius`
- `box`
- `boxSizing`
- `braun`
- `celebrating`
- `center`
- `clarity`
- `color`
- `component`
- `components`
- `cover`
- `design`
- `email`
- `fontSize`
- `fontWeight`
- `functionality`
- `height`
- `high`
- `href`
- `https`
- `jpg`
- `layout`
- `lineHeight`
- `margin`
- `marginBottom`
- `marginTop`
- `minimalist`
- `objectFit`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `principles`
- `react`
- `rgb`
- `simplicity`
- `src`
- `static`
- `style`
- `table`
- `tbody`
- `textAlign`
- `their`
- `verticalAlign`
- `vintage`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

