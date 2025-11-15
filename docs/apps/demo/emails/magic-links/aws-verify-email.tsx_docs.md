# Documentation: aws-verify-email.tsx
**File Path:** `apps/demo/emails/magic-links/aws-verify-email.tsx`
**Language:** tsx
**Size:** 3,695 bytes
**Lines:** 108
**Generated:** 2025-11-15T20:37:33.173263Z

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

- **Path:** `apps/demo/emails/magic-links/aws-verify-email.tsx`
- **Name:** `aws-verify-email.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,695 bytes (3.61 KB)
- **Lines of Code:** 108

---

## Original Source

```tsx
import {
  Body,
  Container,
  Head,
  Heading,
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

interface AWSVerifyEmailProps {
  verificationCode?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export default function AWSVerifyEmail({
  verificationCode,
}: AWSVerifyEmailProps) {
  return (
    <Html>
      <Head />
      <Tailwind config={tailwindConfig}>
        <Body className="bg-white font-aws text-[#212121]">
          <Preview>AWS Email Verification</Preview>
          <Container className="p-5 mx-auto bg-[#eee]">
            <Section className="bg-white">
              <Section className="bg-[#252f3d] flex py-5 items-center justify-center">
                <Img
                  src={`${baseUrl}/static/aws-logo.png`}
                  width="75"
                  height="45"
                  alt="AWS's Logo"
                />
              </Section>
              <Section className="py-[25px] px-[35px]">
                <Heading className="text-[#333] text-[20px] font-bold mb-[15px]">
                  Verify your email address
                </Heading>
                <Text className="text-[#333] text-[14px] leading-[24px] mt-6 mb-[14px] mx-0">
                  Thanks for starting the new AWS account creation process. We
                  want to make sure it's really you. Please enter the following
                  verification code when prompted. If you don&apos;t want to
                  create an account, you can ignore this message.
                </Text>
                <Section className="flex items-center justify-center">
                  <Text className="text-[#333] m-0 font-bold text-center text-[14px]">
                    Verification code
                  </Text>

                  <Text className="text-[#333] text-[36px] my-[10px] mx-0 font-bold text-center">
                    {verificationCode}
                  </Text>
                  <Text className="text-[#333] text-[14px] m-0 text-center">
                    (This code is valid for 10 minutes)
                  </Text>
                </Section>
              </Section>
              <Hr />
              <Section className="py-[25px] px-[35px]">
                <Text className="text-[#333] text-[14px] m-0">
                  Amazon Web Services will never email you and ask you to
                  disclose or verify your password, credit card, or banking
                  account number.
                </Text>
              </Section>
            </Section>
            <Text className="text-[#333] text-[12px] my-[24px] mx-0 px-5 py-0">
              This message was produced and distributed by Amazon Web Services,
              Inc., 410 Terry Ave. North, Seattle, WA 98109. © 2022, Amazon Web
              Services, Inc.. All rights reserved. AWS is a registered trademark
              of{' '}
              <Link
                href="https://amazon.com"
                target="_blank"
                className="text-[#2754C5] underline text-[14px]"
              >
                Amazon.com
              </Link>
              , Inc. View our{' '}
              <Link
                href="https://amazon.com"
                target="_blank"
                className="text-[#2754C5] underline text-[14px]"
              >
                privacy policy
              </Link>
              .
            </Text>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
}

AWSVerifyEmail.PreviewProps = {
  verificationCode: '596853',
} satisfies AWSVerifyEmailProps;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `AWSVerifyEmail()`
- `baseUrl()`

### Interfaces

- `AWSVerifyEmailProps`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 112

- `AWSVerifyEmail`
- `AWSVerifyEmailProps`
- `All`
- `Amazon`
- `Ave`
- `Body`
- `Container`
- `Email`
- `Head`
- `Heading`
- `Html`
- `Img`
- `Inc`
- `Link`
- `Logo`
- `North`
- `Please`
- `Preview`
- `PreviewProps`
- `Seattle`
- `Section`
- `Services`
- `Tailwind`
- `Terry`
- `Text`
- `Thanks`
- `VERCEL_URL`
- `Verification`
- `Verify`
- `View`
- `Web`
- `_blank`
- `account`
- `address`
- `alt`
- `amazon`
- `apos`
- `ask`
- `auto`
- `aws`
- `banking`
- `baseUrl`
- `bold`
- `card`
- `center`
- `className`
- `code`
- `com`
- `components`
- `config`
- `create`
- `creation`
- `credit`
- `disclose`
- `distributed`
- `don`
- `eee`
- `email`
- `enter`
- `env`
- `flex`
- `following`
- `font`
- `height`
- `href`
- `https`
- `ignore`
- `interface`
- `items`
- `justify`
- `leading`
- `logo`
- `make`
- `message`
- `minutes`
- `never`
- `number`
- `our`
- `password`
- `png`
- `policy`
- `privacy`
- `process`
- `produced`
- `prompted`
- `react`
- `really`
- `registered`
- `reserved`
- `rights`
- `satisfies`
- `src`
- `starting`
- `static`
- `string`
- `sure`
- `tailwind`
- `tailwindConfig`
- `target`
- `text`
- `trademark`
- `underline`
- `valid`
- `verification`
- `verificationCode`
- `verify`
- `want`
- `when`
- `white`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

