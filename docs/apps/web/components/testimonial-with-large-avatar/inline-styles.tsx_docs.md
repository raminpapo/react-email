# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/testimonial-with-large-avatar/inline-styles.tsx`
**Language:** tsx
**Size:** 2,165 bytes
**Lines:** 90
**Generated:** 2025-11-15T20:37:33.017607Z

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

- **Path:** `apps/web/components/testimonial-with-large-avatar/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,165 bytes (2.11 KB)
- **Lines of Code:** 90

---

## Original Source

```tsx
import { Img } from '@react-email/components';
import { ResponsiveColumn, ResponsiveRow } from '@responsive-email/react-email';
import { Layout } from '../_components/layout';

export const component = (
  <ResponsiveRow
    style={{
      marginLeft: '12px',
      marginRight: '12px',
      marginTop: '16px',
      marginBottom: '16px',
      fontSize: '14px',
      color: '#4b5563',
    }}
  >
    <ResponsiveColumn
      style={{
        marginTop: '0',
        marginRight: '24px',
        marginBottom: '24px',
        marginLeft: '0',
        width: '256px',
        overflow: 'hidden',
        borderRadius: '24px',
      }}
    >
      <Img
        src="/static/steve-jobs.jpg"
        width={320}
        height={320}
        alt="Steve Jobs"
        style={{
          height: '320px',
          width: '100%',
          objectFit: 'cover',
          objectPosition: 'center',
        }}
      />
    </ResponsiveColumn>
    <ResponsiveColumn style={{ paddingRight: '24px' }}>
      <p
        style={{
          marginLeft: '0',
          marginRight: '0',
          marginTop: '0',
          marginBottom: '24px',
          textAlign: 'left',
          fontSize: '16px',
          lineHeight: '1.625',
          fontWeight: '300',
          color: '#374151',
        }}
      >
        Design is not just what it looks like and feels like. Design is how it
        works. The people who are crazy enough to think they can change the
        world are the ones who do. Innovation distinguishes between a leader and
        a follower.
      </p>
      <p
        style={{
          marginLeft: '0',
          marginRight: '0',
          marginTop: '0',
          marginBottom: '4px',
          textAlign: 'left',
          fontSize: '16px',
          fontWeight: '600',
          color: '#1f2937',
        }}
      >
        Steve Jobs
      </p>
      <p
        style={{
          margin: '0',
          textAlign: 'left',
          fontSize: '14px',
          color: '#4b5563',
        }}
      >
        Co-founder of Apple
      </p>
    </ResponsiveColumn>
  </ResponsiveRow>
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

**Total Unique Identifiers:** 65

- `Apple`
- `Design`
- `Img`
- `Innovation`
- `Jobs`
- `Layout`
- `ResponsiveColumn`
- `ResponsiveRow`
- `Steve`
- `_components`
- `alt`
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
- `left`
- `like`
- `lineHeight`
- `looks`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `objectFit`
- `objectPosition`
- `ones`
- `overflow`
- `paddingRight`
- `people`
- `react`
- `responsive`
- `src`
- `static`
- `steve`
- `style`
- `textAlign`
- `they`
- `think`
- `what`
- `who`
- `width`
- `works`
- `world`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

