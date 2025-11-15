# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/customer-reviews/inline-styles.tsx`
**Language:** tsx
**Size:** 7,223 bytes
**Lines:** 217
**Generated:** 2025-11-15T20:37:33.029389Z

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

- **Path:** `apps/web/components/customer-reviews/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 7,223 bytes (7.05 KB)
- **Lines of Code:** 217

---

## Original Source

```tsx
import {
  Body,
  Button,
  Column,
  Container,
  Head,
  Heading,
  Hr,
  Html,
  Preview,
  Row,
  Section,
  Text,
} from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Html>
    <Head />
    <Preview>Customer Reviews</Preview>
    <Body>
      <Container
        style={{
          backgroundColor: 'rgb(255,255,255)',
          borderRadius: '8px',
          marginLeft: 'auto',
          marginRight: 'auto',
          maxWidth: '400px',
          paddingLeft: '42px',
          paddingRight: '42px',
          paddingTop: '24px',
          paddingBottom: '24px',
        }}
      >
        <Section>
          <Heading as="h1" style={{ fontSize: '24px', lineHeight: '32px' }}>
            Customer Reviews
          </Heading>
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              marginTop: '12px',
            }}
          >
            <Text style={{ display: 'none' }}>4 out of 5 stars</Text>
          </div>
          <Section style={{ marginTop: '24px', marginBottom: '24px' }}>
            <Heading as="h2" style={{ display: 'none' }}>
              Review data
            </Heading>
            <dl style={{ margin: '0px' }}>
              {[
                { rating: 5, count: 1019 },
                { rating: 4, count: 162 },
                { rating: 3, count: 97 },
                { rating: 2, count: 199 },
                { rating: 1, count: 147 },
              ].map(({ count, rating }) => (
                <Row
                  align="center"
                  key={rating}
                  style={{
                    fontSize: '14px',
                    lineHeight: '20px',
                  }}
                >
                  <Column align="center" valign="middle">
                    <Row>
                      <Column>
                        <dt>
                          <Row>
                            <Column width={undefined}>
                              <Text
                                style={{
                                  color: 'rgb(107,114,128)',
                                  fontWeight: '500',
                                  width: '12px',
                                }}
                              >
                                {rating}
                                <span style={{ display: 'none' }}>
                                  {' '}
                                  star reviews
                                </span>
                              </Text>
                            </Column>
                            <Column
                              width="264"
                              height="12"
                              style={{
                                width: 264,
                                height: 12,
                                paddingLeft: 12,
                              }}
                              aria-hidden="true"
                              valign="middle"
                            >
                              <Row
                                aria-hidden="true"
                                width="264"
                                style={{
                                  width: 264,
                                  height: 12,
                                  backgroundColor: 'rgb(243,244,246)',
                                  border: '1px solid rgb(229,231,235)',
                                  borderRadius: 6,
                                }}
                              >
                                <Column
                                  height="12"
                                  style={{
                                    backgroundColor: 'rgb(79,70,229)',
                                    borderRadius: 6,
                                    height: 12,
                                    width: `${(count / 1624) * 264}px`,
                                  }}
                                  width={(count / 1624) * 264}
                                />
                                <Column
                                  width={(1 - count / 1624) * 264}
                                  style={{
                                    width: `${(1 - count / 1624) * 264}px`,
                                  }}
                                />
                              </Row>
                            </Column>
                          </Row>
                        </dt>
                      </Column>
                      <Column width="100%" style={{ width: '100%' }}>
                        <dd
                          style={{
                            color: 'rgb(107,114,128)',
                            fontSize: '12px',
                            fontVariantNumeric: 'tabular-nums',
                            fontWeight: '500',
                            lineHeight: '1',
                            marginLeft: 12,
                            textAlign: 'right',
                          }}
                        >
                          {Math.round((count / 1624) * 100)}%
                        </dd>
                      </Column>
                    </Row>
                  </Column>
                </Row>
              ))}
            </dl>
            <Text
              style={{
                color: 'rgb(107,114,128)',
                fontSize: '12px',
                lineHeight: '24px',
                marginTop: '14px',
                textAlign: 'center',
              }}
            >
              Based on <span style={{ fontWeight: '600' }}>1624</span> Reviews
            </Text>
          </Section>
          <Hr />
          <Section style={{ marginTop: '30px' }}>
            <Heading
              as="h3"
              style={{
                color: 'rgb(17,24,39)',
                fontSize: '18px',
                fontWeight: '500',
                lineHeight: '24px',
                marginBottom: '12px',
              }}
            >
              Share your thoughts
            </Heading>
            <Text
              style={{
                color: 'rgb(107,114,128)',
                fontSize: '14px',
                lineHeight: '20px',
                margin: '0px',
              }}
            >
              If you’ve used this product, share your thoughts with other
              customers
            </Text>
            <Button
              href="#"
              style={{
                backgroundColor: 'rgb(79,70,229)',
                borderRadius: '8px',
                boxSizing: 'border-box',
                color: 'rgb(255,255,255)',
                display: 'inline-block',
                fontWeight: '600',
                marginTop: '26px',
                marginBottom: '24px',
                maxWidth: '100%',
                padding: '12px',
                textAlign: 'center',
                width: '100%',
              }}
            >
              Write a review
            </Button>
          </Section>
        </Section>
      </Container>
    </Body>
  </Html>
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

**Total Unique Identifiers:** 90

- `Based`
- `Body`
- `Button`
- `Column`
- `Container`
- `Customer`
- `Head`
- `Heading`
- `Html`
- `Layout`
- `Math`
- `Preview`
- `Review`
- `Reviews`
- `Row`
- `Section`
- `Share`
- `Text`
- `Write`
- `_components`
- `align`
- `aria`
- `auto`
- `backgroundColor`
- `block`
- `border`
- `borderRadius`
- `box`
- `boxSizing`
- `center`
- `color`
- `column`
- `component`
- `components`
- `count`
- `customers`
- `data`
- `display`
- `div`
- `email`
- `flex`
- `flexDirection`
- `fontSize`
- `fontVariantNumeric`
- `fontWeight`
- `height`
- `hidden`
- `href`
- `inline`
- `key`
- `layout`
- `lineHeight`
- `map`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `maxWidth`
- `middle`
- `nums`
- `other`
- `out`
- `padding`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `product`
- `rating`
- `react`
- `review`
- `reviews`
- `rgb`
- `right`
- `round`
- `share`
- `solid`
- `span`
- `star`
- `stars`
- `style`
- `tabular`
- `textAlign`
- `thoughts`
- `used`
- `valign`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

