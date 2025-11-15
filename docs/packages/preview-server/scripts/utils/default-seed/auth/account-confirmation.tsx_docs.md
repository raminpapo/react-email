# Documentation: account-confirmation.tsx
**File Path:** `packages/preview-server/scripts/utils/default-seed/auth/account-confirmation.tsx`
**Language:** tsx
**Size:** 1,946 bytes
**Lines:** 69
**Generated:** 2025-11-15T20:37:31.773438Z

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

- **Path:** `packages/preview-server/scripts/utils/default-seed/auth/account-confirmation.tsx`
- **Name:** `account-confirmation.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,946 bytes (1.90 KB)
- **Lines of Code:** 69

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

interface AccountConfirmationProps {
  confirmLink: string;
  expiryTime: string;
}

export default function AccountConfirmation({
  confirmLink,
  expiryTime,
}: AccountConfirmationProps) {
  return (
    <Html>
      <Head />
      <Tailwind>
        <Body className="bg-black text-white">
          <Preview>Confirm your React Email account</Preview>
          <Container className="mx-auto">
            <Heading className="font-bold text-center my-[48px] text-[32px]">
              Welcome to React Email!
            </Heading>
            <Text>
              Thank you for signing up! To complete your registration and start
              using React Email, please confirm your email address.
            </Text>
            <Text className="mb-6">
              Click the button below to verify your email. This link will expire
              in {expiryTime}.
            </Text>
            <Row className="w-full">
              <Column className="w-full">
                <Button
                  href={confirmLink}
                  className="bg-cyan-300 text-[20px] font-bold text-[#404040] w-full text-center border border-solid border-cyan-900 py-[8px] rounded-[8px]"
                >
                  Confirm Email
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

AccountConfirmation.PreviewProps = {
  confirmLink: 'https://react.email/confirm/123',
  expiryTime: '24 hours',
} satisfies AccountConfirmationProps;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `AccountConfirmation()`

### Interfaces

- `AccountConfirmationProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 64

- `AccountConfirmation`
- `AccountConfirmationProps`
- `Body`
- `Button`
- `City`
- `Click`
- `Column`
- `Confirm`
- `Container`
- `Email`
- `Head`
- `Heading`
- `Html`
- `Preview`
- `PreviewProps`
- `React`
- `Row`
- `Tailwind`
- `Text`
- `Thank`
- `Welcome`
- `account`
- `address`
- `auto`
- `below`
- `black`
- `bold`
- `border`
- `borderTopColor`
- `button`
- `center`
- `className`
- `complete`
- `components`
- `confirm`
- `confirmLink`
- `cyan`
- `email`
- `expire`
- `expiryTime`
- `font`
- `full`
- `hours`
- `href`
- `https`
- `interface`
- `link`
- `please`
- `react`
- `registration`
- `rounded`
- `satisfies`
- `signing`
- `solid`
- `start`
- `string`
- `style`
- `team`
- `text`
- `using`
- `verify`
- `white`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

