# Documentation: plaid-verify-identity.tsx
**File Path:** `apps/demo/emails/magic-links/plaid-verify-identity.tsx`
**Language:** tsx
**Size:** 2,611 bytes
**Lines:** 76
**Generated:** 2025-11-15T20:37:33.179005Z

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

- **Path:** `apps/demo/emails/magic-links/plaid-verify-identity.tsx`
- **Name:** `plaid-verify-identity.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,611 bytes (2.55 KB)
- **Lines of Code:** 76

---

## Original Source

```tsx
import {
  Body,
  Container,
  Head,
  Heading,
  Html,
  Img,
  Link,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';
import tailwindConfig from '../tailwind.config';

interface PlaidVerifyIdentityEmailProps {
  validationCode?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const PlaidVerifyIdentityEmail = ({
  validationCode,
}: PlaidVerifyIdentityEmailProps) => (
  <Html>
    <Head />
    <Tailwind config={tailwindConfig}>
      <Body className="bg-white font-plaid">
        <Container className="bg-white border border-solid border-[#eee] rounded shadow-[rgba(20,50,70,.2)] shadow-md mt-5 max-w-[360px] mx-auto my-0 pt-[68px] px-0 pb-[130px]">
          <Img
            src={`${baseUrl}/static/plaid-logo.png`}
            width="212"
            height="88"
            alt="Plaid"
            className="mx-auto my-0"
          />
          <Text className="text-[#0a85ea] text-[11px] font-bold h-4 tracking-[0] leading-[16px] mt-4 mb-2 mx-2 uppercase text-center">
            Verify Your Identity
          </Text>
          <Heading className="text-black font-medium font-[HelveticaNeue-Medium,Helvetica,Arial,sans-serif] inline-block text-[20px] leading-[24px] my-0 text-center">
            Enter the following code to finish linking Venmo.
          </Heading>
          <Section className="bg-[rgba(0,0,0,.05)] rounded mx-auto font-[HelveticaNeue-Bold] mt-4 mb-3.5 align-middle w-[280px]">
            <Text className="text-black text-[32px] font-bold tracking-[6px] leading-10 py-2 mx-auto my-0 block text-center">
              {validationCode}
            </Text>
          </Section>
          <Text className="text-[#444] text-[15px] leading-[23px] tracking-[0] py-0 px-10 m-0 text-center">
            Not expecting this email?
          </Text>
          <Text className="text-[#444] text-[15px] leading-[23px] tracking-[0] py-0 px-10 m-0 text-center">
            Contact{' '}
            <Link
              href="mailto:login@plaid.com"
              className="text-[#444] underline"
            >
              login@plaid.com
            </Link>{' '}
            if you did not request this code.
          </Text>
        </Container>
        <Text className="text-black text-xs font-extrabold tracking-[0] leading-[23px] m-0 mt-5 text-center uppercase">
          Securely powered by Plaid.
        </Text>
      </Body>
    </Tailwind>
  </Html>
);

PlaidVerifyIdentityEmail.PreviewProps = {
  validationCode: '144833',
} as PlaidVerifyIdentityEmailProps;

export default PlaidVerifyIdentityEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `PlaidVerifyIdentityEmail()`
- `baseUrl()`

### Interfaces

- `PlaidVerifyIdentityEmailProps`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 87

- `Arial`
- `Body`
- `Bold`
- `Contact`
- `Container`
- `Enter`
- `Head`
- `Heading`
- `Helvetica`
- `HelveticaNeue`
- `Html`
- `Identity`
- `Img`
- `Link`
- `Medium`
- `Plaid`
- `PlaidVerifyIdentityEmail`
- `PlaidVerifyIdentityEmailProps`
- `PreviewProps`
- `Section`
- `Securely`
- `Tailwind`
- `Text`
- `VERCEL_URL`
- `Venmo`
- `Verify`
- `Your`
- `align`
- `alt`
- `auto`
- `baseUrl`
- `black`
- `block`
- `bold`
- `border`
- `center`
- `className`
- `code`
- `com`
- `components`
- `config`
- `eee`
- `email`
- `env`
- `expecting`
- `extrabold`
- `finish`
- `following`
- `font`
- `height`
- `href`
- `https`
- `inline`
- `interface`
- `leading`
- `linking`
- `login`
- `logo`
- `mailto`
- `max`
- `medium`
- `middle`
- `plaid`
- `png`
- `powered`
- `process`
- `react`
- `request`
- `rgba`
- `rounded`
- `sans`
- `serif`
- `shadow`
- `solid`
- `src`
- `static`
- `string`
- `tailwind`
- `tailwindConfig`
- `text`
- `tracking`
- `underline`
- `uppercase`
- `validationCode`
- `white`
- `width`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

