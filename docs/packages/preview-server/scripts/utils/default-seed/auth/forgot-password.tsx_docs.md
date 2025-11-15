# Documentation: forgot-password.tsx
**File Path:** `packages/preview-server/scripts/utils/default-seed/auth/forgot-password.tsx`
**Language:** tsx
**Size:** 1,988 bytes
**Lines:** 72
**Generated:** 2025-11-15T20:37:31.774873Z

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

- **Path:** `packages/preview-server/scripts/utils/default-seed/auth/forgot-password.tsx`
- **Name:** `forgot-password.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,988 bytes (1.94 KB)
- **Lines of Code:** 72

---

## Original Source

```tsx
import {
  Body,
  Button,
  Column,
  Container,
  Head,
  Heading,
  Hr,
  Html,
  Preview,
  Row,
  Tailwind,
  Text,
} from '@react-email/components';

interface ForgotPasswordProps {
  resetLink: string;
  expiryTime: string;
}

export default function ForgotPassword({
  resetLink,
  expiryTime,
}: ForgotPasswordProps) {
  return (
    <Html>
      <Head />
      <Tailwind>
        <Body className="bg-black text-white">
          <Preview>Reset your React Email password</Preview>
          <Container className="mx-auto">
            <Heading className="font-bold text-center my-[48px] text-[32px]">
              Reset Your Password
            </Heading>
            <Text>
              We received a request to reset your password for your React Email
              account.
            </Text>
            <Text>
              Click the button below to create a new password. This link will
              expire in {expiryTime}.
            </Text>
            <Text className="mb-6">
              If you didn't request this, you can safely ignore this email.
            </Text>
            <Row className="w-full">
              <Column className="w-full">
                <Button
                  href={resetLink}
                  className="bg-cyan-300 text-[20px] font-bold text-[#404040] w-full text-center border border-solid border-cyan-900 py-[8px] rounded-[8px]"
                >
                  Reset Password
                </Button>
              </Column>
            </Row>
            <Text className="mt-6">- React Email team</Text>
            <Hr style={{ borderTopColor: '#404040' }} />
            <Text className="text-[#606060] font-bold">
              React Email, 999 React St, Email City, EC 12345
            </Text>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
}

ForgotPassword.PreviewProps = {
  resetLink: 'https://react.email/reset-password/123',
  expiryTime: '1 hour',
} satisfies ForgotPasswordProps;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `ForgotPassword()`

### Interfaces

- `ForgotPasswordProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 63

- `Body`
- `Button`
- `City`
- `Click`
- `Column`
- `Container`
- `Email`
- `ForgotPassword`
- `ForgotPasswordProps`
- `Head`
- `Heading`
- `Html`
- `Password`
- `Preview`
- `PreviewProps`
- `React`
- `Reset`
- `Row`
- `Tailwind`
- `Text`
- `Your`
- `account`
- `auto`
- `below`
- `black`
- `bold`
- `border`
- `borderTopColor`
- `button`
- `center`
- `className`
- `components`
- `create`
- `cyan`
- `didn`
- `email`
- `expire`
- `expiryTime`
- `font`
- `full`
- `hour`
- `href`
- `https`
- `ignore`
- `interface`
- `link`
- `password`
- `react`
- `received`
- `request`
- `reset`
- `resetLink`
- `rounded`
- `safely`
- `satisfies`
- `solid`
- `string`
- `style`
- `team`
- `text`
- `white`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

