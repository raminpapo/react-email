# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/survey-section/inline-styles.tsx`
**Language:** tsx
**Size:** 1,969 bytes
**Lines:** 89
**Generated:** 2025-11-15T20:37:32.998813Z

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

- **Path:** `apps/web/components/survey-section/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,969 bytes (1.92 KB)
- **Lines of Code:** 89

---

## Original Source

```tsx
import {
  Button,
  Column,
  Heading,
  Row,
  Section,
  Text,
} from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Section
    style={{
      textAlign: 'center',
      paddingTop: 16,
      paddingBottom: 16,
    }}
  >
    <Text
      style={{
        marginTop: 8,
        marginBottom: 8,
        fontSize: 18,
        lineHeight: '28px',
        fontWeight: 600,
        color: 'rgb(79,70,229)',
      }}
    >
      Your opinion matters
    </Text>
    <Heading
      as="h1"
      style={{
        margin: '0px',
        marginTop: 8,
        fontSize: 30,
        lineHeight: '36px',
        fontWeight: 600,
        color: 'rgb(17,24,39)',
      }}
    >
      We want to hear you
    </Heading>
    <Text
      style={{
        fontSize: 16,
        lineHeight: '24px',
        color: 'rgb(55,65,81)',
      }}
    >
      How would you rate your experience using our product in a scale from 1 to
      5?
    </Text>
    <Row>
      <Column align="center">
        <table>
          <tr>
            {[1, 2, 3, 4, 5].map((number) => (
              <td align="center" key={number} style={{ padding: 4 }}>
                <Button
                  // Replace with the proper URL that saves the selected number
                  href="https://react.email"
                  style={{
                    height: 20,
                    width: 20,
                    borderRadius: 8,
                    borderWidth: 1,
                    borderStyle: 'solid',
                    borderColor: 'rgb(79,70,229)',
                    padding: 8,
                    fontWeight: 600,
                    color: 'rgb(79,70,229)',
                  }}
                >
                  {number}
                </Button>
              </td>
            ))}
          </tr>
        </table>
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

**Total Unique Identifiers:** 59

- `Button`
- `Column`
- `Heading`
- `How`
- `Layout`
- `Replace`
- `Row`
- `Section`
- `Text`
- `Your`
- `_components`
- `align`
- `borderColor`
- `borderRadius`
- `borderStyle`
- `borderWidth`
- `center`
- `color`
- `component`
- `components`
- `email`
- `experience`
- `fontSize`
- `fontWeight`
- `hear`
- `height`
- `href`
- `https`
- `key`
- `layout`
- `lineHeight`
- `map`
- `margin`
- `marginBottom`
- `marginTop`
- `matters`
- `number`
- `opinion`
- `our`
- `padding`
- `paddingBottom`
- `paddingTop`
- `product`
- `proper`
- `rate`
- `react`
- `rgb`
- `saves`
- `scale`
- `selected`
- `solid`
- `style`
- `table`
- `textAlign`
- `using`
- `want`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

