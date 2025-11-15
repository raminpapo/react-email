# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/multiple-headings/inline-styles.tsx`
**Language:** tsx
**Size:** 729 bytes
**Lines:** 30
**Generated:** 2025-11-15T20:37:33.082432Z

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

- **Path:** `apps/web/components/multiple-headings/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 729 bytes (0.71 KB)
- **Lines of Code:** 30

---

## Original Source

```tsx
import { Heading } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <>
    <Heading as="h1" style={{ textAlign: 'center' }}>
      Jordan Walke
    </Heading>
    <Heading as="h2" style={{ textAlign: 'center' }}>
      Andrew Clark
    </Heading>
    <Heading as="h3" style={{ textAlign: 'center' }}>
      Dan Abramov
    </Heading>
    <Heading as="h4" style={{ textAlign: 'center' }}>
      Jason Bonta
    </Heading>
    <Heading as="h5" style={{ textAlign: 'center' }}>
      Joe Savona
    </Heading>
    <Heading as="h6" style={{ textAlign: 'center' }}>
      Josh Story
    </Heading>
  </>
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

**Total Unique Identifiers:** 23

- `Abramov`
- `Andrew`
- `Bonta`
- `Clark`
- `Dan`
- `Heading`
- `Jason`
- `Joe`
- `Jordan`
- `Josh`
- `Layout`
- `Savona`
- `Story`
- `Walke`
- `_components`
- `center`
- `component`
- `components`
- `email`
- `layout`
- `react`
- `style`
- `textAlign`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

