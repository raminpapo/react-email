# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/checkout/inline-styles.tsx`
**Language:** tsx
**Size:** 6,444 bytes
**Lines:** 249
**Generated:** 2025-11-15T20:37:33.127375Z

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

- **Path:** `apps/web/components/checkout/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 6,444 bytes (6.29 KB)
- **Lines of Code:** 249

---

## Original Source

```tsx
import {
  Button,
  Column,
  Heading,
  Img,
  Row,
  Section,
  Text,
} from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section style={{ paddingTop: 16, paddingBottom: 16, textAlign: 'center' }}>
    <Heading
      as="h1"
      style={{
        fontSize: 30,
        lineHeight: '36px',
        marginBottom: '0px',
        fontWeight: 600,
      }}
    >
      You left something in your cart
    </Heading>
    <Section
      style={{
        padding: 16,
        paddingTop: '0px',
        marginTop: 16,
        marginBottom: 16,
        borderRadius: 8,
        borderWidth: 1,
        borderStyle: 'solid',
        borderColor: 'rgb(229,231,235)',
      }}
    >
      <table style={{ marginBottom: 16 }} width="100%">
        <tr>
          <th
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            &nbsp;
          </th>
          <th
            align="left"
            colSpan={6}
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              color: 'rgb(107,114,128)',
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Text style={{ fontWeight: 600 }}>Product</Text>
          </th>
          <th
            align="center"
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              color: 'rgb(107,114,128)',
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Text style={{ fontWeight: 600 }}>Quantity</Text>
          </th>
          <th
            align="center"
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              color: 'rgb(107,114,128)',
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Text style={{ fontWeight: 600 }}>Price</Text>
          </th>
        </tr>
        <tr>
          <td
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Img
              alt="Braun Classic Watch"
              height={110}
              src="/static/braun-classic-watch.jpg"
              style={{
                objectFit: 'cover',
                borderRadius: 8,
              }}
            />
          </td>
          <td
            align="left"
            colSpan={6}
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Text>Classic Watch</Text>
          </td>
          <td
            align="center"
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Text>1</Text>
          </td>
          <td
            align="center"
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Text>$210.00</Text>
          </td>
        </tr>
        <tr>
          <td
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Img
              alt="Braun Analogue Clock"
              height={110}
              src="/static/braun-analogue-clock.jpg"
              style={{
                objectFit: 'cover',
                borderRadius: 8,
              }}
            />
          </td>
          <td
            align="left"
            colSpan={6}
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Text>Analogue Clock</Text>
          </td>
          <td
            align="center"
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Text>1</Text>
          </td>
          <td
            align="center"
            style={{
              paddingTop: 8,
              paddingBottom: 8,
              borderWidth: '0px',
              borderBottomWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
            }}
          >
            <Text>$40.00</Text>
          </td>
        </tr>
      </table>
      <Row>
        <Column align="center">
          <Button
            href="https://react.email"
            style={{
              width: '100%',
              boxSizing: 'border-box',
              paddingLeft: 12,
              paddingRight: 12,
              borderRadius: 8,
              textAlign: 'center',
              backgroundColor: 'rgb(79,70,229)',
              paddingTop: 12,
              paddingBottom: 12,
              fontWeight: 600,
              color: 'rgb(255,255,255)',
            }}
          >
            Checkout
          </Button>
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

**Total Unique Identifiers:** 72

- `Analogue`
- `Braun`
- `Button`
- `Checkout`
- `Classic`
- `Clock`
- `Column`
- `Heading`
- `Img`
- `Layout`
- `Price`
- `Product`
- `Quantity`
- `Row`
- `Section`
- `Text`
- `Watch`
- `You`
- `_components`
- `align`
- `alt`
- `analogue`
- `backgroundColor`
- `border`
- `borderBottomWidth`
- `borderColor`
- `borderRadius`
- `borderStyle`
- `borderWidth`
- `box`
- `boxSizing`
- `braun`
- `cart`
- `center`
- `classic`
- `clock`
- `colSpan`
- `color`
- `component`
- `components`
- `cover`
- `email`
- `fontSize`
- `fontWeight`
- `height`
- `href`
- `https`
- `jpg`
- `layout`
- `left`
- `lineHeight`
- `marginBottom`
- `marginTop`
- `nbsp`
- `objectFit`
- `padding`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `react`
- `rgb`
- `solid`
- `something`
- `src`
- `static`
- `style`
- `table`
- `textAlign`
- `watch`
- `width`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

