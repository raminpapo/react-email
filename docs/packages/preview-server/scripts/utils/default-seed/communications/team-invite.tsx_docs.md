# Documentation: team-invite.tsx
**File Path:** `packages/preview-server/scripts/utils/default-seed/communications/team-invite.tsx`
**Language:** tsx
**Size:** 2,125 bytes
**Lines:** 79
**Generated:** 2025-11-15T20:37:31.770427Z

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

- **Path:** `packages/preview-server/scripts/utils/default-seed/communications/team-invite.tsx`
- **Name:** `team-invite.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,125 bytes (2.08 KB)
- **Lines of Code:** 79

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

interface TeamInviteProps {
  inviterName: string;
  teamName: string;
  inviteLink: string;
  role: string;
}

export default function TeamInvite({
  inviterName,
  teamName,
  inviteLink,
  role,
}: TeamInviteProps) {
  return (
    <Html>
      <Head />
      <Tailwind>
        <Body className="bg-black text-white">
          <Preview>
            {inviterName} has invited you to join {teamName} on React Email
          </Preview>
          <Container className="mx-auto">
            <Heading className="font-bold text-center my-[48px] text-[32px]">
              You've been invited!
            </Heading>
            <Text>
              {inviterName} has invited you to join {teamName} as a {role}.
            </Text>
            <Text>
              React Email helps teams collaborate on email templates and manage
              their email campaigns effectively.
            </Text>
            <Text className="mb-6">
              Click the button below to accept the invitation and get started:
            </Text>
            <Row className="w-full">
              <Column className="w-full">
                <Button
                  href={inviteLink}
                  className="bg-cyan-300 text-[20px] font-bold text-[#404040] w-full text-center border border-solid border-cyan-900 py-[8px] rounded-[8px]"
                >
                  Accept Invitation
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

TeamInvite.PreviewProps = {
  inviterName: 'John Doe',
  teamName: 'Marketing Team',
  inviteLink: 'https://react.email/join/team/123',
  role: 'Editor',
} satisfies TeamInviteProps;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `TeamInvite()`

### Interfaces

- `TeamInviteProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 71

- `Accept`
- `Body`
- `Button`
- `City`
- `Click`
- `Column`
- `Container`
- `Doe`
- `Editor`
- `Email`
- `Head`
- `Heading`
- `Html`
- `Invitation`
- `John`
- `Marketing`
- `Preview`
- `PreviewProps`
- `React`
- `Row`
- `Tailwind`
- `Team`
- `TeamInvite`
- `TeamInviteProps`
- `Text`
- `You`
- `accept`
- `auto`
- `below`
- `black`
- `bold`
- `border`
- `borderTopColor`
- `button`
- `campaigns`
- `center`
- `className`
- `collaborate`
- `components`
- `cyan`
- `effectively`
- `email`
- `font`
- `full`
- `get`
- `helps`
- `href`
- `https`
- `interface`
- `invitation`
- `inviteLink`
- `invited`
- `inviterName`
- `join`
- `manage`
- `react`
- `role`
- `rounded`
- `satisfies`
- `solid`
- `started`
- `string`
- `style`
- `team`
- `teamName`
- `teams`
- `templates`
- `text`
- `their`
- `white`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

