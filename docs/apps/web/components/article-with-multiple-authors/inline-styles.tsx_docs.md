# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/article-with-multiple-authors/inline-styles.tsx`
**Language:** tsx
**Size:** 4,162 bytes
**Lines:** 157
**Generated:** 2025-11-15T20:37:33.058447Z

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

- **Path:** `apps/web/components/article-with-multiple-authors/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,162 bytes (4.06 KB)
- **Lines of Code:** 157

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
import { Fragment } from 'react/jsx-runtime';
import { Layout } from '../_components/layout';

export const component = (
  <Section>
    <Hr
      style={{
        borderColor: 'rgb(209,213,219) !important',
        marginTop: '16px',
        marginBottom: '0px',
      }}
    />
    <Section>
      {[
        {
          name: 'Steve Jobs',
          title: 'Co-Founder & CEO',
          imgSrc: '/static/steve-jobs.jpg',
          showDivider: true,
        },
        {
          name: 'Steve Wozniak',
          title: 'Co-Founder & CTO',
          imgSrc: '/static/steve-wozniak.jpg',
          showDivider: false,
        },
      ].map((author) => (
        <Fragment key={author.name}>
          <Row
            align="left"
            width="288"
            style={{ marginTop: '16px', width: '288px' }}
          >
            <Column
              width="48"
              height="48"
              style={{
                paddingTop: '5px',
                height: '48px',
                width: '48px',
                textAlign: 'left',
              }}
            >
              <Img
                alt={author.name}
                height={48}
                src={author.imgSrc}
                style={{
                  borderRadius: '9999px',
                  display: 'block',
                  objectFit: 'cover',
                  objectPosition: 'center',
                }}
                width={48}
              />
            </Column>
            <Column
              width="100%"
              style={{
                paddingLeft: '18px',
                width: '100%',
                textAlign: 'left',
                verticalAlign: 'top',
              }}
            >
              <Heading
                as="h3"
                style={{
                  color: 'rgb(17,24,39)',
                  fontSize: '14px',
                  fontWeight: 500,
                  lineHeight: '20px',
                  margin: '0px',
                }}
              >
                {author.name}
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
                {author.title}
              </Text>
              <Row width={undefined} style={{ paddingTop: '8px' }} align="left">
                <Column width="12" height="12">
                  <Link
                    href="#"
                    style={{
                      height: '12px',
                      width: '12px',
                    }}
                  >
                    <Img
                      alt="X"
                      height={12}
                      src="/static/x-icon.png"
                      width={12}
                    />
                  </Link>
                </Column>
                <Column width="12" height="12" style={{ paddingLeft: 8 }}>
                  <Link
                    href="#"
                    style={{
                      height: '12px',
                      width: '12px',
                    }}
                  >
                    <Img
                      alt="LinkedIn"
                      height={12}
                      src="/static/in-icon.png"
                      width={12}
                    />
                  </Link>
                </Column>
              </Row>
            </Column>
          </Row>
          {author.showDivider ? (
            <Hr
              style={{
                border: 'none',
                backgroundColor: 'rgb(209,213,219)',
                display: 'inline-block',
                float: 'left',
                height: '58px',
                marginRight: '16px',
                width: '1px',
              }}
            />
          ) : null}
        </Fragment>
      ))}
    </Section>
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
- `react/jsx-runtime`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 71

- `Column`
- `Founder`
- `Fragment`
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
- `Wozniak`
- `_components`
- `align`
- `alt`
- `author`
- `backgroundColor`
- `block`
- `border`
- `borderColor`
- `borderRadius`
- `center`
- `color`
- `component`
- `components`
- `cover`
- `display`
- `email`
- `float`
- `fontSize`
- `fontWeight`
- `height`
- `href`
- `icon`
- `imgSrc`
- `important`
- `inline`
- `jobs`
- `jpg`
- `jsx`
- `key`
- `layout`
- `left`
- `lineHeight`
- `map`
- `margin`
- `marginBottom`
- `marginRight`
- `marginTop`
- `name`
- `objectFit`
- `objectPosition`
- `paddingLeft`
- `paddingTop`
- `png`
- `react`
- `rgb`
- `runtime`
- `showDivider`
- `src`
- `static`
- `steve`
- `style`
- `textAlign`
- `title`
- `top`
- `verticalAlign`
- `width`
- `wozniak`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

