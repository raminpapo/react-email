# Documentation: tailwind.tsx
**File Path:** `apps/web/components/download-buttons/tailwind.tsx`
**Language:** tsx
**Size:** 1,410 bytes
**Lines:** 50
**Generated:** 2025-11-15T20:37:33.136961Z

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

- **Path:** `apps/web/components/download-buttons/tailwind.tsx`
- **Name:** `tailwind.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,410 bytes (1.38 KB)
- **Lines of Code:** 50

---

## Original Source

```tsx
import { Button, Column, Img, Row, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Row>
    <Column align="center">
      <Row>
        <Text className="font-bold text-[18px] text-indigo-500 leading-[28px]">
          Try now
        </Text>
        <Text className="text-gray-900">
          The app all cheese enthusiasts have been waiting for
        </Text>
      </Row>
      <Row>
        <td align="center">
          <table>
            <tr>
              <td className="pr-[16px]">
                <Button href="https://react.email">
                  <Img
                    alt="Get it on Google Play button"
                    width={182.5}
                    height={54}
                    src="/static/get-it-on-google-play.png"
                  />
                </Button>
              </td>
              <td className="pl-[16px]">
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

**Total Unique Identifiers:** 48

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
- `bold`
- `button`
- `center`
- `cheese`
- `className`
- `component`
- `components`
- `download`
- `email`
- `enthusiasts`
- `font`
- `get`
- `google`
- `gray`
- `height`
- `href`
- `https`
- `indigo`
- `layout`
- `leading`
- `now`
- `play`
- `png`
- `react`
- `src`
- `static`
- `store`
- `table`
- `text`
- `waiting`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

