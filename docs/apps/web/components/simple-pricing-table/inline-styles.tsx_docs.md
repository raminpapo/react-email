# Documentation: inline-styles.tsx
**File Path:** `apps/web/components/simple-pricing-table/inline-styles.tsx`
**Language:** tsx
**Size:** 4,585 bytes
**Lines:** 166
**Generated:** 2025-11-15T20:37:33.047549Z

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

- **Path:** `apps/web/components/simple-pricing-table/inline-styles.tsx`
- **Name:** `inline-styles.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,585 bytes (4.48 KB)
- **Lines of Code:** 166

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
      <Container
        style={{
          backgroundColor: 'rgb(255,255,255)',
          borderRadius: '12px',
          marginLeft: 'auto',
          marginRight: 'auto',
          maxWidth: '500px',
          padding: '24px',
        }}
      >
        <Section
          style={{
            backgroundColor: 'rgb(255,255,255)',
            borderColor: 'rgb(209,213,219)',
            borderRadius: '12px',
            borderStyle: 'solid',
            borderWidth: '1px',
            color: 'rgb(75,85,99)',
            marginBottom: '0px',
            padding: '28px',
            textAlign: 'left',
            width: '100%',
          }}
        >
          <Text
            style={{
              color: 'rgb(79,70,229)',
              fontSize: '12px',
              fontWeight: '600',
              letterSpacing: '0.025em',
              lineHeight: '20px',
              marginBottom: '16px',
              textTransform: 'uppercase',
            }}
          >
            Exclusive Offer
          </Text>
          <Text
            style={{
              fontSize: '30px',
              fontWeight: '700',
              lineHeight: '36px',
              marginBottom: '12px',
              marginTop: '0px',
            }}
          >
            <span style={{ color: 'rgb(16,24,40)' }}>$12</span>{' '}
            <span
              style={{
                fontSize: '16px',
                fontWeight: '500',
                lineHeight: '20px',
              }}
            >
              / month
            </span>
          </Text>
          <Text
            style={{
              color: 'rgb(55,65,81)',
              fontSize: '14px',
              lineHeight: '20px',
              marginTop: '16px',
              marginBottom: '24px',
            }}
          >
            We've handcrafted the perfect plan tailored specifically for your
            needs. Unlock premium features at an unbeatable value.
          </Text>
          <ul
            style={{
              color: 'rgb(107,114,128)',
              fontSize: '14px',
              lineHeight: '24px',
              marginBottom: '32px',
              paddingLeft: '14px',
            }}
          >
            {[
              'Manage up to 25 premium products',
              'Grow your audience with 10,000 subscribers',
              'Make data-driven decisions with advanced analytics',
              'Priority support with 24-hour response time',
              'Seamless integration with your favorite tools',
            ].map((feature) => (
              <li style={{ marginBottom: '12px', position: 'relative' }}>
                <span style={{ position: 'relative' }}>{feature}</span>
              </li>
            ))}
          </ul>
          <Button
            href="#"
            style={{
              backgroundColor: 'rgb(79,70,229)',
              borderRadius: '8px',
              boxSizing: 'border-box',
              color: 'rgb(255,255,255)',
              display: 'inline-block',
              fontSize: '16px',
              lineHeight: '24px',
              fontWeight: '700',
              letterSpacing: '0.025em',
              marginBottom: '24px',
              maxWidth: '100%',
              padding: '14px',
              textAlign: 'center',
              width: '100%',
            }}
          >
            Claim Your Special Offer
          </Button>
          <Hr />
          <Text
            style={{
              color: 'rgb(107,114,128)',
              fontSize: '12px',
              lineHeight: '16px',
              fontStyle: 'italic',
              marginTop: '24px',
              marginBottom: '6px',
              textAlign: 'center',
            }}
          >
            Limited time offer - Upgrade now and save 20%
          </Text>
          <Text
            style={{
              color: 'rgb(107,114,128)',
              fontSize: '12px',
              lineHeight: '16px',
              margin: '0px',
              textAlign: 'center',
            }}
          >
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

**Total Unique Identifiers:** 111

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
- `backgroundColor`
- `block`
- `border`
- `borderColor`
- `borderRadius`
- `borderStyle`
- `borderWidth`
- `box`
- `boxSizing`
- `card`
- `center`
- `color`
- `component`
- `components`
- `credit`
- `data`
- `day`
- `decisions`
- `display`
- `driven`
- `email`
- `favorite`
- `feature`
- `features`
- `fontSize`
- `fontStyle`
- `fontWeight`
- `free`
- `handcrafted`
- `hour`
- `href`
- `inline`
- `integration`
- `italic`
- `layout`
- `left`
- `letterSpacing`
- `lineHeight`
- `map`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `maxWidth`
- `month`
- `needs`
- `now`
- `offer`
- `padding`
- `paddingLeft`
- `perfect`
- `plan`
- `position`
- `premium`
- `products`
- `react`
- `relative`
- `required`
- `response`
- `rgb`
- `save`
- `solid`
- `span`
- `specifically`
- `style`
- `subscribers`
- `support`
- `tailored`
- `textAlign`
- `textTransform`
- `time`
- `tools`
- `trial`
- `unbeatable`
- `uppercase`
- `value`
- `width`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

