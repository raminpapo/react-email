# Documentation: koala-welcome.tsx
**File Path:** `apps/demo/emails/welcome/koala-welcome.tsx`
**Language:** tsx
**Size:** 2,039 bytes
**Lines:** 78
**Generated:** 2025-11-15T20:37:33.207694Z

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

- **Path:** `apps/demo/emails/welcome/koala-welcome.tsx`
- **Name:** `koala-welcome.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,039 bytes (1.99 KB)
- **Lines of Code:** 78

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
  Preview,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';
import tailwindConfig from '../tailwind.config';

interface KoalaWelcomeEmailProps {
  userFirstname: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const KoalaWelcomeEmail = ({
  userFirstname,
}: KoalaWelcomeEmailProps) => (
  <Html>
    <Head />
    <Tailwind config={tailwindConfig}>
      <Body className="bg-white font-koala">
        <Preview>
          The sales intelligence platform that helps you uncover qualified
          leads.
        </Preview>
        <Container className="mx-auto py-5 pb-12">
          <Img
            src={`${baseUrl}/static/koala-logo.png`}
            width="170"
            height="50"
            alt="Koala"
            className="mx-auto"
          />
          <Text className="text-[16px] leading-[26px]">
            Hi {userFirstname},
          </Text>
          <Text className="text-[16px] leading-[26px]">
            Welcome to Koala, the sales intelligence platform that helps you
            uncover qualified leads and close deals faster.
          </Text>
          <Section className="text-center">
            <Button
              className="bg-[#5F51E8] rounded-[3px] text-white text-[16px] no-underline text-center block p-3"
              href="https://getkoala.com"
            >
              Get started
            </Button>
          </Section>
          <Text className="text-[16px] leading-[26px]">
            Best,
            <br />
            The Koala team
          </Text>
          <Hr className="border-[#cccccc] my-5" />
          <Text className="text-[#8898aa] text-[12px]">
            470 Noor Ave STE B #1148, South San Francisco, CA 94080
          </Text>
        </Container>
      </Body>
    </Tailwind>
  </Html>
);

KoalaWelcomeEmail.PreviewProps = {
  userFirstname: 'Alan',
} as KoalaWelcomeEmailProps;

export default KoalaWelcomeEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `KoalaWelcomeEmail()`
- `baseUrl()`

### Interfaces

- `KoalaWelcomeEmailProps`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 73

- `Alan`
- `Ave`
- `Best`
- `Body`
- `Button`
- `Container`
- `Francisco`
- `Get`
- `Head`
- `Html`
- `Img`
- `Koala`
- `KoalaWelcomeEmail`
- `KoalaWelcomeEmailProps`
- `Noor`
- `Preview`
- `PreviewProps`
- `San`
- `Section`
- `South`
- `Tailwind`
- `Text`
- `VERCEL_URL`
- `Welcome`
- `alt`
- `auto`
- `baseUrl`
- `block`
- `border`
- `cccccc`
- `center`
- `className`
- `close`
- `com`
- `components`
- `config`
- `deals`
- `email`
- `env`
- `faster`
- `font`
- `getkoala`
- `height`
- `helps`
- `href`
- `https`
- `intelligence`
- `interface`
- `koala`
- `leading`
- `leads`
- `logo`
- `platform`
- `png`
- `process`
- `qualified`
- `react`
- `rounded`
- `sales`
- `src`
- `started`
- `static`
- `string`
- `tailwind`
- `tailwindConfig`
- `team`
- `text`
- `uncover`
- `underline`
- `userFirstname`
- `white`
- `width`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

