# Documentation: github-access-token.tsx
**File Path:** `apps/demo/emails/notifications/github-access-token.tsx`
**Language:** tsx
**Size:** 2,348 bytes
**Lines:** 82
**Generated:** 2025-11-15T20:37:33.165261Z

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

- **Path:** `apps/demo/emails/notifications/github-access-token.tsx`
- **Name:** `github-access-token.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,348 bytes (2.29 KB)
- **Lines of Code:** 82

---

## Original Source

```tsx
import {
  Body,
  Button,
  Container,
  Head,
  Html,
  Img,
  Link,
  Preview,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';
import tailwindConfig from '../tailwind.config';

interface GithubAccessTokenEmailProps {
  username?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const GithubAccessTokenEmail = ({
  username,
}: GithubAccessTokenEmailProps) => (
  <Html>
    <Head />
    <Tailwind config={tailwindConfig}>
      <Body className="bg-white text-[#24292e] font-github">
        <Preview>
          A fine-grained personal access token has been added to your account
        </Preview>
        <Container className="max-w-[480px] mx-auto my-0 pt-5 pb-12 px-0">
          <Img
            src={`${baseUrl}/static/github.png`}
            width="32"
            height="32"
            alt="Github"
          />

          <Text className="text-[24px] leading-[1.25]">
            <strong>@{username}</strong>, a personal access was created on your
            account.
          </Text>

          <Section className="p-6 border border-solid border-[#dedede] rounded-[5px] text-center">
            <Text className="mb-[10px] mt-0 text-left">
              Hey <strong>{username}</strong>!
            </Text>
            <Text className="mb-[10px] mt-0 text-left">
              A fine-grained personal access token (<Link>resend</Link>) was
              recently added to your account.
            </Text>

            <Button className="text-sm bg-[#28a745] text-white leading-normal rounded-lg py-3 px-6">
              View your token
            </Button>
          </Section>
          <Text className="text-center">
            <Link className="text-[#0366d6] text-[12px]">
              Your security audit log
            </Link>{' '}
            ・{' '}
            <Link className="text-[#0366d6] text-[12px]">Contact support</Link>
          </Text>

          <Text className="text-[#6a737d] text-xs leading-[24px] text-center mt-[60px] mb-4">
            GitHub, Inc. ・88 Colin P Kelly Jr Street ・San Francisco, CA 94107
          </Text>
        </Container>
      </Body>
    </Tailwind>
  </Html>
);

GithubAccessTokenEmail.PreviewProps = {
  username: 'alanturing',
} as GithubAccessTokenEmailProps;

export default GithubAccessTokenEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `GithubAccessTokenEmail()`
- `baseUrl()`

### Interfaces

- `GithubAccessTokenEmailProps`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 78

- `Body`
- `Button`
- `Colin`
- `Contact`
- `Container`
- `Francisco`
- `GitHub`
- `Github`
- `GithubAccessTokenEmail`
- `GithubAccessTokenEmailProps`
- `Head`
- `Hey`
- `Html`
- `Img`
- `Inc`
- `Kelly`
- `Link`
- `Preview`
- `PreviewProps`
- `San`
- `Section`
- `Street`
- `Tailwind`
- `Text`
- `VERCEL_URL`
- `View`
- `Your`
- `access`
- `account`
- `added`
- `alanturing`
- `alt`
- `audit`
- `auto`
- `baseUrl`
- `border`
- `center`
- `className`
- `components`
- `config`
- `created`
- `dedede`
- `email`
- `env`
- `fine`
- `font`
- `github`
- `grained`
- `height`
- `https`
- `interface`
- `leading`
- `left`
- `log`
- `max`
- `normal`
- `personal`
- `png`
- `process`
- `react`
- `recently`
- `resend`
- `rounded`
- `security`
- `solid`
- `src`
- `static`
- `string`
- `strong`
- `support`
- `tailwind`
- `tailwindConfig`
- `text`
- `token`
- `username`
- `white`
- `width`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

