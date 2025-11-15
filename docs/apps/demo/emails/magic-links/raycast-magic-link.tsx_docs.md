# Documentation: raycast-magic-link.tsx
**File Path:** `apps/demo/emails/magic-links/raycast-magic-link.tsx`
**Language:** tsx
**Size:** 2,367 bytes
**Lines:** 84
**Generated:** 2025-11-15T20:37:33.180678Z

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

- **Path:** `apps/demo/emails/magic-links/raycast-magic-link.tsx`
- **Name:** `raycast-magic-link.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,367 bytes (2.31 KB)
- **Lines of Code:** 84

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

interface RaycastMagicLinkEmailProps {
  magicLink?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const RaycastMagicLinkEmail = ({
  magicLink,
}: RaycastMagicLinkEmailProps) => (
  <Html>
    <Head />
    <Tailwind config={tailwindConfig}>
      <Body className="bg-white font-raycast">
        <Preview>Log in with this magic link.</Preview>
        <Container className="mx-auto my-0 pt-5 px-[25px] pb-12 bg-[url('/static/raycast-bg.png')] [background-position:bottom] [background-repeat:no-repeat]">
          <Img
            src={`${baseUrl}/static/raycast-logo.png`}
            width={48}
            height={48}
            alt="Raycast"
          />
          <Heading className="text-[28px] font-bold mt-12">
            🪄 Your magic link
          </Heading>
          <Section className="my-6 mx-0">
            <Text className="text-base leading-6.5">
              <Link className="text-[#FF6363]" href={magicLink}>
                👉 Click here to sign in 👈
              </Link>
            </Text>
            <Text className="text-base leading-6.5">
              If you didn't request this, please ignore this email.
            </Text>
          </Section>
          <Text className="text-base leading-6.5">
            Best,
            <br />- Raycast Team
          </Text>
          <Hr className="border-[#dddddd] mt-12" />
          <Img
            src={`${baseUrl}/static/raycast-logo.png`}
            width={32}
            height={32}
            style={{
              WebkitFilter: 'grayscale(100%)',
            }}
            className="[filter:grayscale(100%)] my-5 mx-0"
          />
          <Text className="text-[#8898aa] text-xs leading-6 ml-1">
            Raycast Technologies Inc.
          </Text>
          <Text className="text-[#8898aa] text-xs leading-6 ml-1">
            2093 Philadelphia Pike #3222, Claymont, DE 19703
          </Text>
        </Container>
      </Body>
    </Tailwind>
  </Html>
);

RaycastMagicLinkEmail.PreviewProps = {
  magicLink: 'https://raycast.com',
} as RaycastMagicLinkEmailProps;

export default RaycastMagicLinkEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `RaycastMagicLinkEmail()`
- `baseUrl()`

### Interfaces

- `RaycastMagicLinkEmailProps`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 78

- `Best`
- `Body`
- `Claymont`
- `Click`
- `Container`
- `FF6363`
- `Head`
- `Heading`
- `Html`
- `Img`
- `Inc`
- `Link`
- `Log`
- `Philadelphia`
- `Pike`
- `Preview`
- `PreviewProps`
- `Raycast`
- `RaycastMagicLinkEmail`
- `RaycastMagicLinkEmailProps`
- `Section`
- `Tailwind`
- `Team`
- `Technologies`
- `Text`
- `VERCEL_URL`
- `WebkitFilter`
- `Your`
- `alt`
- `auto`
- `background`
- `base`
- `baseUrl`
- `bold`
- `border`
- `bottom`
- `className`
- `com`
- `components`
- `config`
- `dddddd`
- `didn`
- `email`
- `env`
- `filter`
- `font`
- `grayscale`
- `height`
- `here`
- `href`
- `https`
- `ignore`
- `interface`
- `leading`
- `link`
- `logo`
- `magic`
- `magicLink`
- `please`
- `png`
- `position`
- `process`
- `raycast`
- `react`
- `repeat`
- `request`
- `sign`
- `src`
- `static`
- `string`
- `style`
- `tailwind`
- `tailwindConfig`
- `text`
- `url`
- `white`
- `width`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

