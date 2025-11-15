# Documentation: stripe-welcome-email.tsx
**File Path:** `apps/web/src/app/api/check-spam/testing/stripe-welcome-email.tsx`
**Language:** tsx
**Size:** 3,997 bytes
**Lines:** 149
**Generated:** 2025-11-15T20:37:32.835632Z

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

- **Path:** `apps/web/src/app/api/check-spam/testing/stripe-welcome-email.tsx`
- **Name:** `stripe-welcome-email.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,997 bytes (3.90 KB)
- **Lines of Code:** 149

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
  Text,
} from '@react-email/components';

const baseUrl = 'https://react-email-demo-iiiiiiiii-users-projects.vercel.app';

export const StripeWelcomeEmail = () => (
  <Html>
    <Head />
    <Body style={main}>
      <Preview>You're now ready to make live transactions with Stripe!</Preview>
      <Container style={container}>
        <Section style={box}>
          <Img
            src={`${baseUrl}/static/stripe-logo.png`}
            width="49"
            height="21"
            alt="Stripe"
          />
          <Hr style={hr} />
          <Text style={paragraph}>
            Thanks for submitting your account information. You're now ready to
            make live transactions with Stripe!
          </Text>
          <Text style={paragraph}>
            You can view your payments and a variety of other information about
            your account right from your dashboard.
          </Text>
          <Button style={button} href="https://dashboard.stripe.com/login">
            View your Stripe Dashboard
          </Button>
          <Hr style={hr} />
          <Text style={paragraph}>
            If you haven't finished your integration, you might find our{' '}
            <Link style={anchor} href="https://stripe.com/docs">
              docs
            </Link>{' '}
            handy.
          </Text>
          <Text style={paragraph}>
            Once you're ready to start accepting payments, you'll just need to
            use your live{' '}
            <Link
              style={anchor}
              href="https://dashboard.stripe.com/login?redirect=%2Fapikeys"
            >
              API keys
            </Link>{' '}
            instead of your test API keys. Your account can simultaneously be
            used for both test and live requests, so you can continue testing
            while accepting live payments. Check out our{' '}
            <Link style={anchor} href="https://stripe.com/docs/dashboard">
              tutorial about account basics
            </Link>
            .
          </Text>
          <Text style={paragraph}>
            Finally, we've put together a{' '}
            <Link
              style={anchor}
              href="https://stripe.com/docs/checklist/website"
            >
              quick checklist
            </Link>{' '}
            to ensure your website conforms to card network standards.
          </Text>
          <Text style={paragraph}>
            We'll be here to help you with any step along the way. You can find
            answers to most questions and get in touch with us on our{' '}
            <Link style={anchor} href="https://support.stripe.com/">
              support site
            </Link>
            .
          </Text>
          <Text style={paragraph}>— The Stripe team</Text>
          <Hr style={hr} />
          <Text style={footer}>
            Stripe, 354 Oyster Point Blvd, South San Francisco, CA 94080
          </Text>
        </Section>
      </Container>
    </Body>
  </Html>
);

export default StripeWelcomeEmail;

const main = {
  backgroundColor: '#f6f9fc',
  fontFamily:
    '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif',
};

const container = {
  backgroundColor: '#ffffff',
  margin: '0 auto',
  padding: '20px 0 48px',
  marginBottom: '64px',
};

const box = {
  padding: '0 48px',
};

const hr = {
  borderColor: '#e6ebf1',
  margin: '20px 0',
};

const paragraph = {
  color: '#525f7f',

  fontSize: '16px',
  lineHeight: '24px',
  textAlign: 'left' as const,
};

const anchor = {
  color: '#556cd6',
};

const button = {
  backgroundColor: '#656ee8',
  borderRadius: '5px',
  color: '#fff',
  fontSize: '16px',
  fontWeight: 'bold',
  textDecoration: 'none',
  textAlign: 'center' as const,
  display: 'block',
  padding: '10px',
};

const footer = {
  color: '#8898aa',
  fontSize: '12px',
  lineHeight: '16px',
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `StripeWelcomeEmail()`
- `anchor()`
- `baseUrl()`
- `box()`
- `button()`
- `container()`
- `footer()`
- `hr()`
- `main()`
- `paragraph()`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 153

- `BlinkMacSystemFont`
- `Blvd`
- `Body`
- `Button`
- `Check`
- `Container`
- `Dashboard`
- `Francisco`
- `Head`
- `Helvetica`
- `Html`
- `Img`
- `Link`
- `Neue`
- `Once`
- `Oyster`
- `Point`
- `Preview`
- `Roboto`
- `San`
- `Section`
- `Segoe`
- `South`
- `Stripe`
- `StripeWelcomeEmail`
- `Text`
- `Thanks`
- `Ubuntu`
- `View`
- `You`
- `Your`
- `about`
- `accepting`
- `account`
- `along`
- `alt`
- `anchor`
- `answers`
- `any`
- `app`
- `apple`
- `auto`
- `backgroundColor`
- `baseUrl`
- `basics`
- `block`
- `bold`
- `borderColor`
- `borderRadius`
- `both`
- `box`
- `button`
- `card`
- `center`
- `checklist`
- `color`
- `com`
- `components`
- `conforms`
- `container`
- `dashboard`
- `demo`
- `display`
- `docs`
- `e6ebf1`
- `email`
- `ensure`
- `f6f9fc`
- `fff`
- `ffffff`
- `find`
- `finished`
- `fontFamily`
- `fontSize`
- `fontWeight`
- `footer`
- `get`
- `handy`
- `haven`
- `height`
- `help`
- `here`
- `href`
- `https`
- `iiiiiiiii`
- `information`
- `instead`
- `integration`
- `just`
- `keys`
- `left`
- `lineHeight`
- `live`
- `login`
- `logo`
- `main`
- `make`
- `margin`
- `marginBottom`
- `most`
- `need`
- `network`
- `now`
- `other`
- `our`
- `out`
- `padding`
- `paragraph`
- `payments`
- `png`
- `projects`
- `put`
- `questions`
- `quick`
- `react`
- `ready`
- `redirect`
- `requests`
- `right`
- `sans`
- `serif`
- `simultaneously`
- `site`
- `src`
- `standards`
- `start`
- `static`
- `step`
- `stripe`
- `style`
- `submitting`
- `support`
- `system`
- `team`
- `test`
- `testing`
- `textAlign`
- `textDecoration`
- `together`
- `touch`
- `transactions`
- `tutorial`
- `use`
- `used`
- `users`
- `variety`
- `vercel`
- `view`
- `way`
- `website`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

