# Documentation: payment-overdue.tsx
**File Path:** `packages/preview-server/scripts/utils/default-seed/communications/payment-overdue.tsx`
**Language:** tsx
**Size:** 2,328 bytes
**Lines:** 83
**Generated:** 2025-11-15T20:37:31.768881Z

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

- **Path:** `packages/preview-server/scripts/utils/default-seed/communications/payment-overdue.tsx`
- **Name:** `payment-overdue.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,328 bytes (2.27 KB)
- **Lines of Code:** 83

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

interface PaymentOverdueProps {
  customerName: string;
  amount: string;
  dueDate: string;
  invoiceLink: string;
}

export default function PaymentOverdue({
  customerName,
  amount,
  dueDate,
  invoiceLink,
}: PaymentOverdueProps) {
  return (
    <Html>
      <Head />
      <Tailwind>
        <Body className="bg-black text-white">
          <Preview>Payment of {amount} is overdue - Action required</Preview>
          <Container className="mx-auto">
            <Heading className="font-bold text-center my-[48px] text-[32px]">
              Payment Overdue
            </Heading>
            <Text>Dear {customerName},</Text>
            <Text>
              We noticed that your payment of {amount} was due on {dueDate} and
              has not been received yet.
            </Text>
            <Text>
              To avoid any service interruption, please process your payment as
              soon as possible.
            </Text>
            <Text className="mb-6">
              You can view and pay your invoice by clicking the button below:
            </Text>
            <Row className="w-full">
              <Column className="w-full">
                <Button
                  href={invoiceLink}
                  className="bg-cyan-300 text-[20px] font-bold text-[#404040] w-full text-center border border-solid border-cyan-900 py-[8px] rounded-[8px]"
                >
                  Pay Now
                </Button>
              </Column>
            </Row>
            <Text className="mt-6">
              If you have already made this payment, please disregard this
              message.
            </Text>
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

PaymentOverdue.PreviewProps = {
  customerName: 'Jane Smith',
  amount: '$99.00',
  dueDate: 'June 1st, 2024',
  invoiceLink: 'https://react.email/invoice/123',
} satisfies PaymentOverdueProps;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `PaymentOverdue()`

### Interfaces

- `PaymentOverdueProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 82

- `Action`
- `Body`
- `Button`
- `City`
- `Column`
- `Container`
- `Dear`
- `Email`
- `Head`
- `Heading`
- `Html`
- `Jane`
- `June`
- `Now`
- `Overdue`
- `Pay`
- `Payment`
- `PaymentOverdue`
- `PaymentOverdueProps`
- `Preview`
- `PreviewProps`
- `React`
- `Row`
- `Smith`
- `Tailwind`
- `Text`
- `You`
- `already`
- `amount`
- `any`
- `auto`
- `avoid`
- `below`
- `black`
- `bold`
- `border`
- `borderTopColor`
- `button`
- `center`
- `className`
- `clicking`
- `components`
- `customerName`
- `cyan`
- `disregard`
- `due`
- `dueDate`
- `email`
- `font`
- `full`
- `href`
- `https`
- `interface`
- `interruption`
- `invoice`
- `invoiceLink`
- `made`
- `message`
- `noticed`
- `overdue`
- `pay`
- `payment`
- `please`
- `possible`
- `process`
- `react`
- `received`
- `required`
- `rounded`
- `satisfies`
- `service`
- `solid`
- `soon`
- `string`
- `style`
- `team`
- `text`
- `view`
- `white`
- `yet`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

