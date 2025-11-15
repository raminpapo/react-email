# Documentation: stripe-welcome.tsx
**File Path:** `apps/demo/emails/welcome/stripe-welcome.tsx`
**Language:** tsx
**Size:** 4,265 bytes
**Lines:** 119
**Generated:** 2025-11-15T20:37:33.211738Z

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

- **Path:** `apps/demo/emails/welcome/stripe-welcome.tsx`
- **Name:** `stripe-welcome.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,265 bytes (4.17 KB)
- **Lines of Code:** 119

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
  Img,
  Link,
  Preview,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';
import tailwindConfig from '../tailwind.config';

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const StripeWelcomeEmail = () => (
  <Html>
    <Head />
    <Tailwind config={tailwindConfig}>
      <Body className="bg-[#f6f9fc] font-stripe">
        <Preview>
          You're now ready to make live transactions with Stripe!
        </Preview>
        <Container className="bg-white mx-auto py-5 pb-12 mb-16">
          <Section className="px-12">
            <Img
              src={`${baseUrl}/static/stripe-logo.png`}
              width="49"
              height="21"
              alt="Stripe"
            />
            <Hr className="border-[#e6ebf1] my-5" />
            <Text className="text-[#525f7f] text-base leading-6 text-left">
              Thanks for submitting your account information. You're now ready
              to make live transactions with Stripe!
            </Text>
            <Text className="text-[#525f7f] text-base leading-6 text-left">
              You can view your payments and a variety of other information
              about your account right from your dashboard.
            </Text>
            <Button
              className="bg-[#656ee8] rounded-[3px] text-white text-[16px] font-bold no-underline text-center block p-[10px]"
              href="https://dashboard.stripe.com/login"
            >
              View your Stripe Dashboard
            </Button>
            <Hr className="border-[#e6ebf1] my-5" />
            <Text className="text-[#525f7f] text-base leading-6 text-left">
              If you haven't finished your integration, you might find our{' '}
              <Link
                className="text-[#556cd6]"
                href="https://docs.stripe.com/dashboard/basics"
              >
                docs
              </Link>{' '}
              handy.
            </Text>
            <Text className="text-[#525f7f] text-base leading-6 text-left">
              Once you're ready to start accepting payments, you'll just need to
              use your live{' '}
              <Link
                className="text-[#556cd6]"
                href="https://dashboard.stripe.com/login?redirect=%2Fapikeys"
              >
                API keys
              </Link>{' '}
              instead of your test API keys. Your account can simultaneously be
              used for both test and live requests, so you can continue testing
              while accepting live payments. Check out our{' '}
              <Link
                className="text-[#556cd6]"
                href="https://docs.stripe.com/dashboard/basics"
              >
                tutorial about account basics
              </Link>
              .
            </Text>
            <Text className="text-[#525f7f] text-base leading-6 text-left">
              Finally, we've put together a{' '}
              <Link
                className="text-[#556cd6]"
                href="https://docs.stripe.com/get-started/checklist/website"
              >
                quick checklist
              </Link>{' '}
              to ensure your website conforms to card network standards.
            </Text>
            <Text className="text-[#525f7f] text-base leading-6 text-left">
              We'll be here to help you with any step along the way. You can
              find answers to most questions and get in touch with us on our{' '}
              <Link
                className="text-[#556cd6]"
                href="https://support.stripe.com"
              >
                support site
              </Link>
              .
            </Text>
            <Text className="text-[#525f7f] text-base leading-6 text-left">
              — The Stripe team
            </Text>
            <Hr className="border-[#e6ebf1] my-5" />
            <Text className="text-[#8898aa] text-xs leading-4">
              Stripe, 354 Oyster Point Blvd, South San Francisco, CA 94080
            </Text>
          </Section>
        </Container>
      </Body>
    </Tailwind>
  </Html>
);

export default StripeWelcomeEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `StripeWelcomeEmail()`
- `baseUrl()`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 130

- `Blvd`
- `Body`
- `Button`
- `Check`
- `Container`
- `Dashboard`
- `Francisco`
- `Head`
- `Html`
- `Img`
- `Link`
- `Once`
- `Oyster`
- `Point`
- `Preview`
- `San`
- `Section`
- `South`
- `Stripe`
- `StripeWelcomeEmail`
- `Tailwind`
- `Text`
- `Thanks`
- `VERCEL_URL`
- `View`
- `You`
- `Your`
- `about`
- `accepting`
- `account`
- `along`
- `alt`
- `answers`
- `any`
- `auto`
- `base`
- `baseUrl`
- `basics`
- `block`
- `bold`
- `border`
- `both`
- `card`
- `center`
- `checklist`
- `className`
- `com`
- `components`
- `config`
- `conforms`
- `dashboard`
- `docs`
- `e6ebf1`
- `email`
- `ensure`
- `env`
- `f6f9fc`
- `find`
- `finished`
- `font`
- `get`
- `handy`
- `haven`
- `height`
- `help`
- `here`
- `href`
- `https`
- `information`
- `instead`
- `integration`
- `just`
- `keys`
- `leading`
- `left`
- `live`
- `login`
- `logo`
- `make`
- `most`
- `need`
- `network`
- `now`
- `other`
- `our`
- `out`
- `payments`
- `png`
- `process`
- `put`
- `questions`
- `quick`
- `react`
- `ready`
- `redirect`
- `requests`
- `right`
- `rounded`
- `simultaneously`
- `site`
- `src`
- `standards`
- `start`
- `started`
- `static`
- `step`
- `stripe`
- `submitting`
- `support`
- `tailwind`
- `tailwindConfig`
- `team`
- `test`
- `testing`
- `text`
- `together`
- `touch`
- `transactions`
- `tutorial`
- `underline`
- `use`
- `used`
- `variety`
- `view`
- `way`
- `website`
- `white`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

