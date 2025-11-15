# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/article-with-single-author/inline-styles.tsx`
**Language:** tsx
**Size:** 2,958 bytes
**Lines:** 136
**Generated:** 2025-11-15T20:37:32.968911Z

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

- **Path:** `apps/web/components/article-with-single-author/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,958 bytes (2.89 KB)
- **Lines of Code:** 136

---

## Original Source

```tsx
import {
  Column,
  Heading,
  Hr,
  Img,
  Link,
  Row,
  Section,
  Text,
} from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section>
    <Hr
      style={{
        borderColor: 'rgb(209,213,219) !important',
        marginTop: '16px',
        marginBottom: '16px',
      }}
    />
    <Row width={undefined}>
      <Column
        width="48"
        height="48"
        style={{
          display: 'inline-block',
          paddingTop: '5px',
          height: '48px',
          width: '48px',
        }}
      >
        <Img
          alt="Steve Jobs"
          height={48}
          src="/static/steve-jobs.jpg"
          style={{
            borderRadius: '9999px',
            display: 'block',
            height: '48px',
            objectFit: 'cover',
            objectPosition: 'center',
            width: '48px',
          }}
          width={48}
        />
      </Column>
      <Column
        width="120"
        style={{
          paddingLeft: '18px',
          maxWidth: '120px',
        }}
        align="left"
        valign="top"
      >
        <Heading
          as="h3"
          style={{
            color: 'rgb(31,41,55)',
            fontSize: '14px',
            fontWeight: 500,
            lineHeight: '20px',
            margin: '0px',
          }}
        >
          Steve Jobs
        </Heading>
        <Text
          style={{
            color: 'rgb(107,114,128)',
            fontSize: '12px',
            fontWeight: 500,
            lineHeight: '14px',
            margin: '0px',
          }}
        >
          Co-Founder & CEO
        </Text>
        <Row
          align={undefined}
          width={undefined}
          style={{
            marginTop: '4px',
          }}
        >
          <Column width={undefined} valign="middle">
            <Link
              href="#"
              style={{
                height: '12px',
                width: '12px',
              }}
            >
              <Img
                alt="X"
                src="/static/x-icon.png"
                width="12"
                height="12"
                style={{ height: '12px', width: '12px' }}
              />
            </Link>
          </Column>
          <Column
            width={undefined}
            valign="middle"
            style={{
              paddingLeft: '8px',
            }}
          >
            <Link
              href="#"
              style={{
                height: '12px',
                width: '12px',
              }}
            >
              <Img
                alt="LinkedIn"
                src="/static/in-icon.png"
                width="12"
                height="12"
                style={{ height: '12px', width: '12px' }}
              />
            </Link>
          </Column>
        </Row>
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

**Total Unique Identifiers:** 56

- `Column`
- `Founder`
- `Heading`
- `Img`
- `Jobs`
- `Layout`
- `Link`
- `LinkedIn`
- `Row`
- `Section`
- `Steve`
- `Text`
- `_components`
- `align`
- `alt`
- `block`
- `borderColor`
- `borderRadius`
- `center`
- `color`
- `component`
- `components`
- `cover`
- `display`
- `email`
- `fontSize`
- `fontWeight`
- `height`
- `href`
- `icon`
- `important`
- `inline`
- `jobs`
- `jpg`
- `layout`
- `left`
- `lineHeight`
- `margin`
- `marginBottom`
- `marginTop`
- `maxWidth`
- `middle`
- `objectFit`
- `objectPosition`
- `paddingLeft`
- `paddingTop`
- `png`
- `react`
- `rgb`
- `src`
- `static`
- `steve`
- `style`
- `top`
- `valign`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

