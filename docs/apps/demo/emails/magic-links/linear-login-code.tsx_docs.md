# Documentation: linear-login-code.tsx
**File Path:** `apps/demo/emails/magic-links/linear-login-code.tsx`
**Language:** tsx
**Size:** 2,300 bytes
**Lines:** 79
**Generated:** 2025-11-15T20:37:33.175060Z

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

- **Path:** `apps/demo/emails/magic-links/linear-login-code.tsx`
- **Name:** `linear-login-code.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,300 bytes (2.25 KB)
- **Lines of Code:** 79

---

## Original Source

```tsx
import {
  Body,
  Button,
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

interface LinearLoginCodeEmailProps {
  validationCode?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const LinearLoginCodeEmail = ({
  validationCode,
}: LinearLoginCodeEmailProps) => (
  <Html>
    <Head />
    <Tailwind config={tailwindConfig}>
      <Body className="bg-white font-linear">
        <Preview>Your login code for Linear</Preview>
        <Container className="mx-auto my-0 max-w-[560px] px-0 pt-5 pb-12">
          <Img
            src={`${baseUrl}/static/linear-logo.png`}
            width="42"
            height="42"
            alt="Linear"
            className="rounded-3xl w-[42px] h-[42px]"
          />
          <Heading className="text-[24px] tracking-[-0.5px] leading-[1.3] font-normal text-[#484848] pt-[17px] px-0 pb-0">
            Your login code for Linear
          </Heading>
          <Section className="py-[27px] px-0">
            <Button
              className="bg-[#5e6ad2] rounded font-semibold text-white text-[15px] no-underline text-center block py-[11px] px-[23px]"
              href="https://linear.app"
            >
              Login to Linear
            </Button>
          </Section>
          <Text className="mb-[15px] mx-0 mt-0 leading-[1.4] text-[15px] text-[#3c4149]">
            This link and code will only be valid for the next 5 minutes. If the
            link does not work, you can use the login verification code
            directly:
          </Text>
          <code className="font-mono font-bold px-1 py-px bg-[#dfe1e4] text-[#3c4149] text-[21px] tracking-[-0.3px] rounded">
            {validationCode}
          </code>
          <Hr className="border-[#dfe1e4] mt-[42px] mb-[26px]" />
          <Link
            href="https://linear.app"
            className="text-[#b4becc] text-[14px]"
          >
            Linear
          </Link>
        </Container>
      </Body>
    </Tailwind>
  </Html>
);

LinearLoginCodeEmail.PreviewProps = {
  validationCode: 'tt226-5398x',
} as LinearLoginCodeEmailProps;

export default LinearLoginCodeEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `LinearLoginCodeEmail()`
- `baseUrl()`

### Interfaces

- `LinearLoginCodeEmailProps`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 74

- `Body`
- `Button`
- `Container`
- `Head`
- `Heading`
- `Html`
- `Img`
- `Linear`
- `LinearLoginCodeEmail`
- `LinearLoginCodeEmailProps`
- `Link`
- `Login`
- `Preview`
- `PreviewProps`
- `Section`
- `Tailwind`
- `Text`
- `VERCEL_URL`
- `Your`
- `alt`
- `app`
- `auto`
- `b4becc`
- `baseUrl`
- `block`
- `bold`
- `border`
- `center`
- `className`
- `code`
- `components`
- `config`
- `dfe1e4`
- `directly`
- `email`
- `env`
- `font`
- `height`
- `href`
- `https`
- `interface`
- `leading`
- `linear`
- `link`
- `login`
- `logo`
- `max`
- `minutes`
- `mono`
- `next`
- `normal`
- `only`
- `png`
- `process`
- `react`
- `rounded`
- `semibold`
- `src`
- `static`
- `string`
- `tailwind`
- `tailwindConfig`
- `text`
- `tracking`
- `tt226`
- `underline`
- `use`
- `valid`
- `validationCode`
- `verification`
- `white`
- `width`
- `work`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

