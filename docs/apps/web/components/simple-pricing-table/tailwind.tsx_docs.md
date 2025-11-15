# Documentation: tailwind.tsx
**File Path:** `apps/web/components/simple-pricing-table/tailwind.tsx`
**Language:** tsx
**Size:** 2,673 bytes
**Lines:** 71
**Generated:** 2025-11-15T20:37:33.049375Z

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

- **Path:** `apps/web/components/simple-pricing-table/tailwind.tsx`
- **Name:** `tailwind.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,673 bytes (2.61 KB)
- **Lines of Code:** 71

---

## Original Source

```tsx
import {
  Body,
  Button,
  Container,
  Head,
  Hr,
  Html,
  Preview,
  Section,
  Text,
} from '@react-email/components';
import { Layout } from '../_components/layout';

export const component = (
  <Html>
    <Head />
    <Preview>
      Exclusive Offer Just For You: Unlock Premium Features at $12/month
    </Preview>
    <Body>
      <Container className="bg-white rounded-[12px] mx-auto max-w-[500px] p-[24px]">
        <Section className="bg-white border border-solid border-gray-300 rounded-[12px] text-gray-600 p-[28px] w-full text-left mb-0">
          <Text className="text-indigo-600 text-[12px] leading-[20px] font-semibold tracking-wide mb-[16px] mt-[16px] uppercase">
            Exclusive Offer
          </Text>
          <Text className="text-[30px] font-bold leading-[36px] mb-[12px] mt-0">
            <span className="text-[rgb(16,24,40)]">$12</span>{' '}
            <span className="text-[16px] font-medium leading-[20px]">
              / month
            </span>
          </Text>
          <Text className="text-gray-700 text-[14px] leading-[20px] mt-[16px] mb-[24px]">
            We've handcrafted the perfect plan tailored specifically for your
            needs. Unlock premium features at an unbeatable value.
          </Text>
          <ul className="text-gray-500 text-[14px] leading-[24px] mb-[32px] pl-[14px]">
            {[
              'Manage up to 25 premium products',
              'Grow your audience with 10,000 subscribers',
              'Make data-driven decisions with advanced analytics',
              'Priority support with 24-hour response time',
              'Seamless integration with your favorite tools',
            ].map((feature) => (
              <li key={feature} className="mb-[12px] relative">
                <span className="relative">{feature}</span>
              </li>
            ))}
          </ul>
          <Button
            href="#"
            className="bg-indigo-600 rounded-[8px] box-border text-white inline-block text-[16px] leading-[24px] font-bold tracking-wide mb-[24px] max-w-full p-[14px] text-center w-full"
          >
            Claim Your Special Offer
          </Button>
          <Hr />
          <Text className="text-gray-500 text-[12px] leading-[16px] italic mt-[24px] mb-[6px] text-center">
            Limited time offer - Upgrade now and save 20%
          </Text>
          <Text className="text-gray-500 text-[12px] m-0 leading-[16px] text-center">
            No credit card required. 14-day free trial available.
          </Text>
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

**Total Unique Identifiers:** 101

- `Body`
- `Button`
- `Claim`
- `Container`
- `Exclusive`
- `Features`
- `Grow`
- `Head`
- `Html`
- `Just`
- `Layout`
- `Limited`
- `Make`
- `Manage`
- `Offer`
- `Premium`
- `Preview`
- `Priority`
- `Seamless`
- `Section`
- `Special`
- `Text`
- `Unlock`
- `Upgrade`
- `You`
- `Your`
- `_components`
- `advanced`
- `analytics`
- `audience`
- `auto`
- `available`
- `block`
- `bold`
- `border`
- `box`
- `card`
- `center`
- `className`
- `component`
- `components`
- `credit`
- `data`
- `day`
- `decisions`
- `driven`
- `email`
- `favorite`
- `feature`
- `features`
- `font`
- `free`
- `full`
- `gray`
- `handcrafted`
- `hour`
- `href`
- `indigo`
- `inline`
- `integration`
- `italic`
- `key`
- `layout`
- `leading`
- `left`
- `map`
- `max`
- `medium`
- `month`
- `needs`
- `now`
- `offer`
- `perfect`
- `plan`
- `premium`
- `products`
- `react`
- `relative`
- `required`
- `response`
- `rgb`
- `rounded`
- `save`
- `semibold`
- `solid`
- `span`
- `specifically`
- `subscribers`
- `support`
- `tailored`
- `text`
- `time`
- `tools`
- `tracking`
- `trial`
- `unbeatable`
- `uppercase`
- `value`
- `white`
- `wide`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

