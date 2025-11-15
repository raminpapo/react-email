# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/avatars-with-text/inline-styles.tsx`
**Language:** tsx
**Size:** 1,698 bytes
**Lines:** 64
**Generated:** 2025-11-15T20:37:33.014154Z

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

- **Path:** `apps/web/components/avatars-with-text/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,698 bytes (1.66 KB)
- **Lines of Code:** 64

---

## Original Source

```tsx
import { Column, Img, Link, Row } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Row>
    <Column align="center">
      <Link href="https://github.com/zehfernandes">
        <Row
          style={{
            width: 'auto',
            tableLayout: 'fixed',
            borderCollapse: 'collapse',
            borderSpacing: 0,
          }}
        >
          <Column
            style={{
              height: '44px',
              width: '44px',
              overflow: 'hidden',
              borderRadius: '9999px',
              padding: 0,
              textAlign: 'center',
              verticalAlign: 'middle',
              lineHeight: '0px',
            }}
          >
            <Img
              src="https://github.com/zehfernandes.png?size=100"
              width="36"
              height="36"
              alt="Zeh Fernandes"
              style={{
                height: '100%',
                width: '100%',
                objectFit: 'cover',
                objectPosition: 'center',
              }}
            />
          </Column>
          <Column
            style={{
              paddingLeft: '12px',
              fontSize: '14px',
              lineHeight: '20px',
              fontWeight: 500,
              color: '#6b7280',
            }}
          >
            <p style={{ margin: 0, color: '#374151' }}>Zeh Fernandes</p>
            <p style={{ margin: 0, fontSize: '12px', lineHeight: '14px' }}>
              Founding Designer
            </p>
          </Column>
        </Row>
      </Link>
    </Column>
  </Row>
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

**Total Unique Identifiers:** 51

- `Column`
- `Designer`
- `Fernandes`
- `Founding`
- `Img`
- `Layout`
- `Link`
- `Row`
- `Zeh`
- `_components`
- `align`
- `alt`
- `auto`
- `borderCollapse`
- `borderRadius`
- `borderSpacing`
- `center`
- `collapse`
- `color`
- `com`
- `component`
- `components`
- `cover`
- `email`
- `fixed`
- `fontSize`
- `fontWeight`
- `github`
- `height`
- `hidden`
- `href`
- `https`
- `layout`
- `lineHeight`
- `margin`
- `middle`
- `objectFit`
- `objectPosition`
- `overflow`
- `padding`
- `paddingLeft`
- `png`
- `react`
- `size`
- `src`
- `style`
- `tableLayout`
- `textAlign`
- `verticalAlign`
- `width`
- `zehfernandes`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

