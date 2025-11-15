# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/testimonial-simple-centered/inline-styles.tsx`
**Language:** tsx
**Size:** 2,123 bytes
**Lines:** 91
**Generated:** 2025-11-15T20:37:33.144611Z

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

- **Path:** `apps/web/components/testimonial-simple-centered/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,123 bytes (2.07 KB)
- **Lines of Code:** 91

---

## Original Source

```tsx
import { Column, Img, Row, Section } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section
    style={{
      textAlign: 'center',
      fontSize: '14px',
      lineHeight: '20px',
      color: '#4b5563',
    }}
  >
    <p
      style={{
        margin: 0,
        fontSize: '16px',
        lineHeight: '24px',
        fontWeight: 300,
        color: '#1f2937',
      }}
    >
      Design is not just what it looks like and feels like. Design is how it
      works. The people who are crazy enough to think they can change the world
      are the ones who do. Innovation distinguishes between a leader and a
      follower.
    </p>
    <Row
      style={{
        marginTop: '32px',
      }}
      width={undefined}
      align="center"
    >
      <Column valign="middle">
        <div
          style={{
            height: '32px',
            width: '32px',
            borderRadius: '9999px',
            overflow: 'hidden',
            backgroundColor: '#4b5563',
          }}
        >
          <Img
            src="/static/steve-jobs.jpg"
            width={32}
            height={32}
            alt="Steve Jobs"
            style={{ height: '100%', width: '100%', objectFit: 'cover' }}
          />
        </div>
      </Column>
      <Column valign="middle">
        <p
          style={{
            margin: 0,
            marginLeft: '12px',
            fontSize: '14px',
            lineHeight: '20px',
            fontWeight: 600,
            color: '#111827',
            marginRight: 8,
          }}
        >
          Steve Jobs
        </p>
      </Column>
      <Column valign="middle">
        <span style={{ fontSize: '14px', lineHeight: '20px', marginRight: 8 }}>
          •
        </span>
      </Column>
      <Column valign="middle">
        <p
          style={{
            margin: 0,
            fontSize: '14px',
            lineHeight: '20px',
          }}
        >
          Co-founder of Apple
        </p>
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

**Total Unique Identifiers:** 67

- `Apple`
- `Column`
- `Design`
- `Img`
- `Innovation`
- `Jobs`
- `Layout`
- `Row`
- `Section`
- `Steve`
- `_components`
- `align`
- `alt`
- `backgroundColor`
- `between`
- `borderRadius`
- `center`
- `change`
- `color`
- `component`
- `components`
- `cover`
- `crazy`
- `distinguishes`
- `div`
- `email`
- `enough`
- `feels`
- `follower`
- `fontSize`
- `fontWeight`
- `founder`
- `height`
- `hidden`
- `how`
- `jobs`
- `jpg`
- `just`
- `layout`
- `leader`
- `like`
- `lineHeight`
- `looks`
- `margin`
- `marginLeft`
- `marginRight`
- `marginTop`
- `middle`
- `objectFit`
- `ones`
- `overflow`
- `people`
- `react`
- `span`
- `src`
- `static`
- `steve`
- `style`
- `textAlign`
- `they`
- `think`
- `valign`
- `what`
- `who`
- `width`
- `works`
- `world`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

