# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/article-with-image-as-background/inline-styles.tsx`
**Language:** tsx
**Size:** 2,479 bytes
**Lines:** 92
**Generated:** 2025-11-15T20:37:33.011172Z

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

- **Path:** `apps/web/components/article-with-image-as-background/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,479 bytes (2.42 KB)
- **Lines of Code:** 92

---

## Original Source

```tsx
import { Button, Heading, Text } from '@react-email/components';
import { Layout } from '../_components/layout';

// Notes for future exploration on finding a way to do this inside of
// Desktop Outlook:
// - https://backgrounds.cm/
// - use VML https://learn.microsoft.com/en-us/windows/win32/vml/msdn-online-vml-fill-element

export const component = (
  <table
    align="center"
    border={0}
    cellPadding="0"
    cellSpacing="0"
    role="presentation"
    style={{
      height: 424,
      marginTop: 16,
      marginBottom: 16,
      borderRadius: 12,
      backgroundColor: 'rgb(37,99,235)',
      // This url must be in quotes for Yahoo
      backgroundImage: "url('/static/my-image.png')",
      backgroundSize: '100% 100%',
    }}
    width="100%"
  >
    <tbody>
      <tr>
        <td align="center" style={{ padding: 40, textAlign: 'center' }}>
          <Text
            style={{
              margin: '0px',
              fontWeight: 600,
              color: 'rgb(229,231,235)',
            }}
          >
            New article
          </Text>
          <Heading
            as="h1"
            style={{
              margin: '0px',
              marginTop: 4,
              fontWeight: 700,
              color: 'rgb(255,255,255)',
            }}
          >
            Artful Accents
          </Heading>
          <Text
            style={{
              margin: '0px',
              marginTop: 8,
              fontSize: 16,
              lineHeight: '24px',
              color: 'rgb(255,255,255)',
            }}
          >
            Uncover the power of accent furniture in transforming your space
            with subtle touches of style, personality, and functionality, as we
            explore the art of curating captivating accents.
          </Text>
          <Button
            href="https://react.email"
            style={{
              marginTop: 24,
              borderRadius: 8,
              borderWidth: 1,
              borderStyle: 'solid',
              borderColor: 'rgb(229,231,235)',
              backgroundColor: 'rgb(255,255,255)',
              paddingLeft: 40,
              paddingRight: 40,
              paddingTop: 12,
              paddingBottom: 12,
              fontWeight: 600,
              color: 'rgb(17,24,39)',
            }}
          >
            Read more
          </Button>
        </td>
      </tr>
    </tbody>
  </table>
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

**Total Unique Identifiers:** 94

- `Accents`
- `Artful`
- `Button`
- `Desktop`
- `Heading`
- `Layout`
- `Notes`
- `Outlook`
- `Read`
- `Text`
- `Uncover`
- `Yahoo`
- `_components`
- `accent`
- `accents`
- `align`
- `art`
- `article`
- `backgroundColor`
- `backgroundImage`
- `backgroundSize`
- `backgrounds`
- `border`
- `borderColor`
- `borderRadius`
- `borderStyle`
- `borderWidth`
- `captivating`
- `cellPadding`
- `cellSpacing`
- `center`
- `color`
- `com`
- `component`
- `components`
- `curating`
- `element`
- `email`
- `exploration`
- `explore`
- `fill`
- `finding`
- `fontSize`
- `fontWeight`
- `functionality`
- `furniture`
- `future`
- `height`
- `href`
- `https`
- `image`
- `inside`
- `layout`
- `learn`
- `lineHeight`
- `margin`
- `marginBottom`
- `marginTop`
- `microsoft`
- `more`
- `msdn`
- `must`
- `online`
- `padding`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `personality`
- `png`
- `power`
- `presentation`
- `quotes`
- `react`
- `rgb`
- `role`
- `solid`
- `space`
- `static`
- `style`
- `subtle`
- `table`
- `tbody`
- `textAlign`
- `touches`
- `transforming`
- `url`
- `use`
- `vml`
- `way`
- `width`
- `win32`
- `windows`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

