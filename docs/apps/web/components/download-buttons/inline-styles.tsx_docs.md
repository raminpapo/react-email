# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/download-buttons/inline-styles.tsx`
**Language:** tsx
**Size:** 1,575 bytes
**Lines:** 61
**Generated:** 2025-11-15T20:37:33.135782Z

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

- **Path:** `apps/web/components/download-buttons/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,575 bytes (1.54 KB)
- **Lines of Code:** 61

---

## Original Source

```tsx
import { Button, Column, Img, Row, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Row>
    <Column align="center">
      <Row>
        <Text
          style={{
            color: 'rgb(99,102,241)',
            fontWeight: 700,
            fontSize: 18,
            lineHeight: '28px',
          }}
        >
          Try now
        </Text>
        <Text
          style={{
            color: 'rgb(17,24,39)',
          }}
        >
          The app all cheese enthusiasts have been waiting for
        </Text>
      </Row>
      <Row>
        <td align="center">
          <table>
            <tr>
              <td style={{ paddingRight: 16 }}>
                <Button href="https://react.email">
                  <Img
                    alt="Get it on Google Play button"
                    width={182.5}
                    height={54}
                    src="/static/get-it-on-google-play.png"
                  />
                </Button>
              </td>
              <td style={{ paddingLeft: 16 }}>
                <Button href="https://react.email">
                  <Img
                    alt="Download on the App Store button"
                    width={164}
                    height={54}
                    src="/static/download-on-the-app-store.png"
                  />
                </Button>
              </td>
            </tr>
          </table>
        </td>
      </Row>
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

**Total Unique Identifiers:** 49

- `App`
- `Button`
- `Column`
- `Download`
- `Get`
- `Google`
- `Img`
- `Layout`
- `Play`
- `Row`
- `Store`
- `Text`
- `_components`
- `align`
- `all`
- `alt`
- `app`
- `button`
- `center`
- `cheese`
- `color`
- `component`
- `components`
- `download`
- `email`
- `enthusiasts`
- `fontSize`
- `fontWeight`
- `get`
- `google`
- `height`
- `href`
- `https`
- `layout`
- `lineHeight`
- `now`
- `paddingLeft`
- `paddingRight`
- `play`
- `png`
- `react`
- `rgb`
- `src`
- `static`
- `store`
- `style`
- `table`
- `waiting`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

