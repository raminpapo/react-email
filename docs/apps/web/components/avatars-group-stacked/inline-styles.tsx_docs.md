# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/avatars-group-stacked/inline-styles.tsx`
**Language:** tsx
**Size:** 3,105 bytes
**Lines:** 137
**Generated:** 2025-11-15T20:37:33.065191Z

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

- **Path:** `apps/web/components/avatars-group-stacked/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,105 bytes (3.03 KB)
- **Lines of Code:** 137

---

## Original Source

```tsx
import { Column, Img, Row } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Row
    width={undefined}
    style={{
      tableLayout: 'fixed',
      borderCollapse: 'collapse',
      borderSpacing: 0,
    }}
  >
    <Column
      width="44"
      height="44"
      style={{
        height: '44px',
        width: '44px',
        padding: 0,
        textAlign: 'center',
        verticalAlign: 'middle',
        lineHeight: '0px',
      }}
    >
      <div
        style={{
          boxSizing: 'border-box',
          height: '100%',
          width: '100%',
          overflow: 'hidden',
          borderRadius: '9999px',
          border: '4px solid white',
          backgroundColor: '#030712',
        }}
      >
        <Img
          src="https://github.com/bukinoshita.png?size=100"
          alt="Bu Kinoshita"
          width="40"
          height="40"
          style={{
            display: 'inline-block',
            height: '100%',
            width: '100%',
            objectFit: 'cover',
            objectPosition: 'center',
          }}
        />
      </div>
    </Column>
    <Column
      width="44"
      height="44"
      style={{
        position: 'relative',
        left: '-12px',
        height: '44px',
        width: '44px',
        padding: 0,
        textAlign: 'center',
        verticalAlign: 'middle',
        lineHeight: '0px',
      }}
    >
      <div
        style={{
          boxSizing: 'border-box',
          height: '100%',
          width: '100%',
          overflow: 'hidden',
          borderRadius: '9999px',
          border: '4px solid white',
          backgroundColor: '#030712',
        }}
      >
        <Img
          src="https://github.com/bukinoshita.png?size=100"
          alt="Bu Kinoshita"
          width="40"
          height="40"
          style={{
            display: 'inline-block',
            height: '100%',
            width: '100%',
            objectFit: 'cover',
            objectPosition: 'center',
          }}
        />
      </div>
    </Column>
    <Column
      width="44"
      height="44"
      style={{
        position: 'relative',
        left: '-24px',
        height: '44px',
        width: '44px',
        padding: 0,
        textAlign: 'center',
        verticalAlign: 'middle',
        lineHeight: '0px',
      }}
    >
      <div
        style={{
          boxSizing: 'border-box',
          height: '100%',
          width: '100%',
          overflow: 'hidden',
          borderRadius: '9999px',
          border: '4px solid white',
          backgroundColor: '#030712',
        }}
      >
        <Img
          src="https://github.com/bukinoshita.png?size=100"
          alt="Bu Kinoshita"
          width="40"
          height="40"
          style={{
            display: 'inline-block',
            height: '100%',
            width: '100%',
            objectFit: 'cover',
            objectPosition: 'center',
          }}
        />
      </div>
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

**Total Unique Identifiers:** 52

- `Column`
- `Img`
- `Kinoshita`
- `Layout`
- `Row`
- `_components`
- `alt`
- `backgroundColor`
- `block`
- `border`
- `borderCollapse`
- `borderRadius`
- `borderSpacing`
- `box`
- `boxSizing`
- `bukinoshita`
- `center`
- `collapse`
- `com`
- `component`
- `components`
- `cover`
- `display`
- `div`
- `email`
- `fixed`
- `github`
- `height`
- `hidden`
- `https`
- `inline`
- `layout`
- `left`
- `lineHeight`
- `middle`
- `objectFit`
- `objectPosition`
- `overflow`
- `padding`
- `png`
- `position`
- `react`
- `relative`
- `size`
- `solid`
- `src`
- `style`
- `tableLayout`
- `textAlign`
- `verticalAlign`
- `white`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

