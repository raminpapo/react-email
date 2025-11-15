# Documentation: tailwind.tsx
**File Path:** `apps/web/components/customer-reviews/tailwind.tsx`
**Language:** tsx
**Size:** 4,747 bytes
**Lines:** 130
**Generated:** 2025-11-15T20:37:33.031577Z

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

- **Path:** `apps/web/components/customer-reviews/tailwind.tsx`
- **Name:** `tailwind.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,747 bytes (4.64 KB)
- **Lines of Code:** 130

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
      <Container className="mx-auto max-w-[400px] rounded-[8px] bg-white px-[42px] py-[24px]">
        <Section>
          <Heading as="h1" className="text-[24px] leading-[32px]">
            Customer Reviews
          </Heading>
          <div className="mt-[12px] flex flex-col">
            <Text className="hidden">4 out of 5 stars</Text>
          </div>
          <Section className="my-[24px]">
            <Heading as="h2" className="hidden">
              Review data
            </Heading>
            <dl className="m-0">
              {[
                { rating: 5, count: 1019 },
                { rating: 4, count: 162 },
                { rating: 3, count: 97 },
                { rating: 2, count: 199 },
                { rating: 1, count: 147 },
              ].map(({ count, rating }) => (
                <Row
                  key={rating}
                  className="text-[14px] leading-[20px]"
                  align="center"
                >
                  <Column align="center" valign="middle">
                    <Row>
                      <Column>
                        <dt>
                          <Row>
                            <Column width={undefined}>
                              <Text className="w-[12px] font-medium text-gray-500">
                                {rating}
                                <span className="hidden"> star reviews</span>
                              </Text>
                            </Column>
                            <Column
                              width="264"
                              height="12"
                              className="w-[264px] h-[12px] pl-[12px]"
                              aria-hidden="true"
                              valign="middle"
                            >
                              <Row
                                width="264"
                                className="w-[264px] h-[12px] bg-gray-100 border-gray-200 border border-solid rounded-[6px]"
                              >
                                <Column
                                  height="12"
                                  className="h-[12px] bg-indigo-600 rounded-[6px]"
                                  width={(count / 1624) * 264}
                                  style={{
                                    width: `${(count / 1624) * 264}px`,
                                  }}
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
                      <Column width="100%" className="w-full">
                        <dd className="ml-[12px] text-right font-medium text-gray-500 text-[12px] [font-variant-numeric:tabular-nums] leading-none">
                          {Math.round((count / 1624) * 100)}%
                        </dd>
                      </Column>
                    </Row>
                  </Column>
                </Row>
              ))}
            </dl>
            <Text className="mt-[14px] text-center text-gray-500 text-[12px] leading-[24px]">
              Based on <span className="font-semibold">1624</span> Reviews
            </Text>
          </Section>
          <Hr />
          <Section className="mt-[30px]">
            <Heading
              as="h3"
              className="mb-[12px] font-medium text-gray-900 text-[18px] leading-[24px]"
            >
              Share your thoughts
            </Heading>
            <Text className="m-0 text-gray-500 text-[14px] leading-[20px]">
              If you’ve used this product, share your thoughts with other
              customers
            </Text>
            <Button
              href="#"
              className="mt-[26px] mb-[24px] inline-block w-full rounded-[8px] bg-indigo-600 p-[12px] text-center box-border font-semibold text-white"
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

**Total Unique Identifiers:** 81

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
- `block`
- `border`
- `box`
- `center`
- `className`
- `col`
- `component`
- `components`
- `count`
- `customers`
- `data`
- `div`
- `email`
- `flex`
- `font`
- `full`
- `gray`
- `height`
- `hidden`
- `href`
- `indigo`
- `inline`
- `key`
- `layout`
- `leading`
- `map`
- `max`
- `medium`
- `middle`
- `numeric`
- `nums`
- `other`
- `out`
- `product`
- `rating`
- `react`
- `review`
- `reviews`
- `right`
- `round`
- `rounded`
- `semibold`
- `share`
- `solid`
- `span`
- `star`
- `stars`
- `style`
- `tabular`
- `text`
- `thoughts`
- `used`
- `valign`
- `variant`
- `white`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

