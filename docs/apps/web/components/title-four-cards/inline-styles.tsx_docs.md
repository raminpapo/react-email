# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/title-four-cards/inline-styles.tsx`
**Language:** tsx
**Size:** 8,257 bytes
**Lines:** 332
**Generated:** 2025-11-15T20:37:33.117703Z

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

- **Path:** `apps/web/components/title-four-cards/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 8,257 bytes (8.06 KB)
- **Lines of Code:** 332

---

## Original Source

```tsx
import {
  Button,
  Column,
  Hr,
  Img,
  Row,
  Section,
  Text,
} from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section style={{ marginTop: 16, marginBottom: 16 }}>
    <Section>
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
          Timing Products
        </Text>
        <Text
          style={{
            marginTop: 8,
            fontSize: 16,
            lineHeight: '24px',
            color: 'rgb(107,114,128)',
          }}
        >
          Dieter Rams consistently implemented his design principles over the
          course of over three decades as the Braun design leader.
        </Text>
      </Row>
      <Row style={{ marginTop: 16 }}>
        <Column
          align="left"
          colSpan={1}
          style={{ width: '50%', paddingRight: 8 }}
        >
          <Img
            alt="Braun Wall Clock"
            height={250}
            src="/static/braun-wall-clock.jpg"
            style={{
              width: '100%',
              borderRadius: 8,
              objectFit: 'cover',
            }}
          />
          <Text
            style={{
              margin: '0px',
              marginTop: 24,
              fontSize: 20,
              fontWeight: 600,
              lineHeight: '28px',
              color: 'rgb(17,24,39)',
            }}
          >
            Wall Clock
          </Text>
          <Text
            style={{
              margin: '0px',
              marginTop: 16,
              fontSize: 16,
              lineHeight: '24px',
              color: 'rgb(107,114,128)',
            }}
          >
            Easy to read dial layout.
          </Text>
          <Text
            style={{
              margin: '0px',
              marginTop: 8,
              fontSize: 16,
              lineHeight: '24px',
              fontWeight: 600,
              color: 'rgb(17,24,39)',
            }}
          >
            $45.00
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
            Buy
          </Button>
        </Column>
        <Column
          align="left"
          colSpan={1}
          style={{ width: '50%', paddingLeft: 8 }}
        >
          <Img
            alt="Braun Wireless Alarm"
            height={250}
            src="/static/braun-wireless-alarm.jpg"
            style={{
              width: '100%',
              borderRadius: 8,
              objectFit: 'cover',
            }}
          />
          <Text
            style={{
              margin: '0px',
              marginTop: 24,
              fontSize: 20,
              lineHeight: '28px',
              fontWeight: 600,
              color: 'rgb(17,24,39)',
            }}
          >
            Wireless Alarm
          </Text>
          <Text
            style={{
              margin: '0px',
              marginTop: 16,
              fontSize: 16,
              lineHeight: '24px',
              color: 'rgb(107,114,128)',
            }}
          >
            Designed with a focus on function.
          </Text>
          <Text
            style={{
              margin: '0px',
              marginTop: 8,
              fontSize: 16,
              lineHeight: '24px',
              fontWeight: 600,
              color: 'rgb(17,24,39)',
            }}
          >
            $50.00
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
            Buy
          </Button>
        </Column>
      </Row>
    </Section>
    <Hr
      style={{
        marginLeft: '0px',
        marginRight: '0px',
        marginTop: 24,
        marginBottom: 24,
        width: '100%',
        borderWidth: 1,
        borderStyle: 'solid',
        borderColor: 'rgb(229,231,235)',
      }}
    />
    <Section>
      <Row>
        <Column
          align="left"
          colSpan={1}
          style={{ width: '50%', paddingRight: 8 }}
        >
          <Img
            alt="Braun Classic Watch"
            height={250}
            src="/static/braun-classic-watch.jpg"
            style={{
              width: '100%',
              borderRadius: 8,
              objectFit: 'cover',
            }}
          />
          <Text
            style={{
              margin: '0px',
              marginTop: 24,
              fontSize: 20,
              lineHeight: '28px',
              fontWeight: 600,
              color: 'rgb(17,24,39)',
            }}
          >
            Classic Watch
          </Text>
          <Text
            style={{
              margin: '0px',
              marginTop: 16,
              fontSize: 16,
              lineHeight: '24px',
              color: 'rgb(107,114,128)',
            }}
          >
            Functional, classic, and built to last.
          </Text>
          <Text
            style={{
              margin: '0px',
              marginTop: 8,
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
            Buy
          </Button>
        </Column>
        <Column
          align="left"
          colSpan={1}
          style={{ width: '50%', paddingLeft: 8 }}
        >
          <Img
            alt="Braun Analogue Clock"
            height={250}
            src="/static/braun-analogue-clock.jpg"
            style={{
              width: '100%',
              borderRadius: 8,
              objectFit: 'cover',
            }}
          />
          <Text
            style={{
              margin: '0px',
              marginTop: 24,
              fontSize: 20,
              lineHeight: '28px',
              fontWeight: 600,
              color: 'rgb(17,24,39)',
            }}
          >
            Analogue Clock
          </Text>
          <Text
            style={{
              margin: '0px',
              marginTop: 16,
              fontSize: 16,
              lineHeight: '24px',
              color: 'rgb(107,114,128)',
            }}
          >
            Thoughtful and simply designed.
          </Text>
          <Text
            style={{
              margin: '0px',
              marginTop: 8,
              fontSize: 16,
              lineHeight: '24px',
              fontWeight: 600,
              color: 'rgb(17,24,39)',
            }}
          >
            $40.00
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
            Buy
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

**Total Unique Identifiers:** 89

- `Alarm`
- `Analogue`
- `Braun`
- `Button`
- `Buy`
- `Classic`
- `Clock`
- `Column`
- `Designed`
- `Dieter`
- `Easy`
- `Functional`
- `Img`
- `Layout`
- `Products`
- `Rams`
- `Row`
- `Section`
- `Text`
- `Thoughtful`
- `Timing`
- `Wall`
- `Watch`
- `Wireless`
- `_components`
- `alarm`
- `align`
- `alt`
- `analogue`
- `backgroundColor`
- `borderColor`
- `borderRadius`
- `borderStyle`
- `borderWidth`
- `braun`
- `built`
- `classic`
- `clock`
- `colSpan`
- `color`
- `component`
- `components`
- `consistently`
- `course`
- `cover`
- `decades`
- `design`
- `designed`
- `dial`
- `email`
- `focus`
- `fontSize`
- `fontWeight`
- `height`
- `his`
- `href`
- `https`
- `implemented`
- `jpg`
- `last`
- `layout`
- `leader`
- `left`
- `lineHeight`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `objectFit`
- `over`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `principles`
- `react`
- `read`
- `rgb`
- `simply`
- `solid`
- `src`
- `static`
- `style`
- `three`
- `wall`
- `watch`
- `width`
- `wireless`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

