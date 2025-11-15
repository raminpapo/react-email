# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/title-three-cards-in-a-row/inline-styles.tsx`
**Language:** tsx
**Size:** 6,038 bytes
**Lines:** 250
**Generated:** 2025-11-15T20:37:33.093382Z

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

- **Path:** `apps/web/components/title-three-cards-in-a-row/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 6,038 bytes (5.90 KB)
- **Lines of Code:** 250

---

## Original Source

```tsx
import { Button, Img, Row, Section, Text } from '@react-email/components';
import { ResponsiveColumn, ResponsiveRow } from '@responsive-email/react-email';
import { Layout } from '../_components/layout';

export const component = (
  <Section style={{ marginTop: 16, marginBottom: 16 }}>
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
    <ResponsiveRow style={{ marginTop: 16 }}>
      <ResponsiveColumn
        style={{
          textAlign: 'left',
          paddingRight: 4,
          paddingTop: 16,
          paddingBottom: 16,
        }}
      >
        <Img
          alt="Braun Analogue Clock"
          height={180}
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
      </ResponsiveColumn>
      <ResponsiveColumn
        style={{
          textAlign: 'left',
          paddingRight: 4,
          paddingLeft: 4,
          paddingTop: 16,
          paddingBottom: 16,
        }}
      >
        <Img
          alt="Braun Wall Clock"
          height={180}
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
            lineHeight: '28px',
            fontWeight: 600,
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
          The original easy to read dial layout.
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
      </ResponsiveColumn>
      <ResponsiveColumn
        style={{
          paddingTop: 16,
          paddingBottom: 16,
          paddingLeft: 4,
          textAlign: 'left',
        }}
      >
        <Img
          alt="Braun Classic Watch"
          height={180}
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
      </ResponsiveColumn>
    </ResponsiveRow>
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
- `@responsive-email/react-email`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 79

- `Analogue`
- `Braun`
- `Button`
- `Buy`
- `Classic`
- `Clock`
- `Dieter`
- `Functional`
- `Img`
- `Layout`
- `Products`
- `Rams`
- `ResponsiveColumn`
- `ResponsiveRow`
- `Row`
- `Section`
- `Text`
- `Thoughtful`
- `Timing`
- `Wall`
- `Watch`
- `_components`
- `alt`
- `analogue`
- `backgroundColor`
- `borderRadius`
- `braun`
- `built`
- `classic`
- `clock`
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
- `easy`
- `email`
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
- `marginTop`
- `objectFit`
- `original`
- `over`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `principles`
- `react`
- `read`
- `responsive`
- `rgb`
- `simply`
- `src`
- `static`
- `style`
- `textAlign`
- `three`
- `wall`
- `watch`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

