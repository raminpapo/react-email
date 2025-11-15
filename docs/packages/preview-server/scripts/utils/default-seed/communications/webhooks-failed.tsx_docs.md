# Documentation: webhooks-failed.tsx
**File Path:** `packages/preview-server/scripts/utils/default-seed/communications/webhooks-failed.tsx`
**Language:** tsx
**Size:** 2,309 bytes
**Lines:** 90
**Generated:** 2025-11-15T20:37:31.771914Z

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

- **Path:** `packages/preview-server/scripts/utils/default-seed/communications/webhooks-failed.tsx`
- **Name:** `webhooks-failed.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,309 bytes (2.25 KB)
- **Lines of Code:** 90

---

## Original Source

```tsx
import {
  Body,
  CodeBlock,
  Container,
  Head,
  Heading,
  Hr,
  Html,
  Preview,
  Tailwind,
  Text,
  vesper,
} from '@react-email/components';

interface WebhooksFailedProps {
  date: string;
  error: {
    error: string;
    timestamp: string;
    webhookId: string;
    details: {
      reason: string;
      retryCount: number;
      lastAttempt: string;
    };
  };
}

export default function WebhooksFailed({ date, error }: WebhooksFailedProps) {
  return (
    <Html>
      <Head />
      <Tailwind>
        <Body className="bg-black text-white">
          <Preview>Some webhooks failed to deliver at {date}</Preview>
          <Container className="mx-auto">
            <Heading className="font-bold text-center text-[32px]">
              Failed webhook attempt
            </Heading>
            <Text>
              We encountered an issue with some of our webhooks. Please check
              the logs for more details. Here is the data for the error:
            </Text>
            <CodeBlock
              code={JSON.stringify(error, null, 2)}
              language="json"
              theme={vesper}
              style={{
                padding: '16px',
                borderRadius: '8px',
              }}
              lineNumbers
            />
            <Text className="mb-6">
              If you have any questions or need assistance, please reach out to
              us at{' '}
              <a
                href="mailto:support@react.email"
                className="text-cyan-300 underline"
              >
                support@react.email
              </a>
              .
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

WebhooksFailed.PreviewProps = {
  date: 'June 4th, 202',
  error: {
    error: 'Webhook delivery failed',
    timestamp: '2023-10-01T12:00:00Z',
    webhookId: 'wh_1234567890',
    details: {
      reason: 'Network error',
      retryCount: 3,
      lastAttempt: '2023-10-01T12:05:00Z',
    },
  },
} satisfies WebhooksFailedProps;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `WebhooksFailed()`

### Interfaces

- `WebhooksFailedProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 85

- `Body`
- `City`
- `CodeBlock`
- `Container`
- `Email`
- `Failed`
- `Head`
- `Heading`
- `Here`
- `Html`
- `June`
- `Network`
- `Please`
- `Preview`
- `PreviewProps`
- `React`
- `Some`
- `Tailwind`
- `Text`
- `Webhook`
- `WebhooksFailed`
- `WebhooksFailedProps`
- `any`
- `assistance`
- `attempt`
- `auto`
- `black`
- `bold`
- `borderRadius`
- `borderTopColor`
- `center`
- `check`
- `className`
- `code`
- `components`
- `cyan`
- `data`
- `date`
- `deliver`
- `delivery`
- `details`
- `email`
- `encountered`
- `error`
- `failed`
- `font`
- `href`
- `interface`
- `issue`
- `json`
- `language`
- `lastAttempt`
- `lineNumbers`
- `logs`
- `mailto`
- `more`
- `need`
- `number`
- `our`
- `out`
- `padding`
- `please`
- `questions`
- `reach`
- `react`
- `reason`
- `retryCount`
- `satisfies`
- `some`
- `string`
- `stringify`
- `style`
- `support`
- `team`
- `text`
- `theme`
- `timestamp`
- `underline`
- `vesper`
- `webhook`
- `webhookId`
- `webhooks`
- `wh_1234567890`
- `white`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

