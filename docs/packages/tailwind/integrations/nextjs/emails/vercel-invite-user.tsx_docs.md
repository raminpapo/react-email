# Documentation: vercel-invite-user.tsx
**File Path:** `packages/tailwind/integrations/nextjs/emails/vercel-invite-user.tsx`
**Language:** tsx
**Size:** 4,889 bytes
**Lines:** 152
**Generated:** 2025-11-15T20:37:32.376114Z

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

- **Path:** `packages/tailwind/integrations/nextjs/emails/vercel-invite-user.tsx`
- **Name:** `vercel-invite-user.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,889 bytes (4.77 KB)
- **Lines of Code:** 152

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
  Img,
  Link,
  Preview,
  Row,
  Section,
  Text,
} from '@react-email/components';
import { Tailwind } from '@react-email/tailwind';

interface VercelInviteUserEmailProps {
  username?: string;
  userImage?: string;
  invitedByUsername?: string;
  invitedByEmail?: string;
  teamName?: string;
  teamImage?: string;
  inviteLink?: string;
  inviteFromIp?: string;
  inviteFromLocation?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const VercelInviteUserEmail = ({
  username,
  userImage,
  invitedByUsername,
  invitedByEmail,
  teamName,
  teamImage,
  inviteLink,
  inviteFromIp,
  inviteFromLocation,
}: VercelInviteUserEmailProps) => {
  const previewText = `Join ${invitedByUsername} on Vercel`;

  return (
    <Html>
      <Head />
      <Preview>{previewText}</Preview>
      <Tailwind>
        <Body className="mx-auto my-auto bg-white px-2 font-sans">
          <Container className="mx-auto my-[40px] max-w-[465px] rounded border border-[#eaeaea] border-solid p-[20px]">
            <Section className="mt-[32px]">
              <Img
                src={`${baseUrl}/static/vercel-logo.png`}
                width="40"
                height="37"
                alt="Vercel"
                className="mx-auto my-0"
              />
            </Section>
            <Heading className="mx-0 my-[30px] p-0 text-center font-normal text-[24px] text-black">
              Join <strong>{teamName}</strong> on <strong>Vercel</strong>
            </Heading>
            <Text className="text-[14px] text-black leading-[24px]">
              Hello {username},
            </Text>
            <Text className="text-[14px] text-black leading-[24px]">
              <strong>{invitedByUsername}</strong> (
              <Link
                href={`mailto:${invitedByEmail}`}
                className="text-blue-600 no-underline"
              >
                {invitedByEmail}
              </Link>
              ) has invited you to the <strong>{teamName}</strong> team on{' '}
              <strong>Vercel</strong>.
            </Text>
            <Section>
              <Row>
                <Column align="right">
                  <Img
                    className="rounded-full"
                    src={userImage}
                    width="64"
                    height="64"
                  />
                </Column>
                <Column align="center">
                  <Img
                    src={`${baseUrl}/static/vercel-arrow.png`}
                    width="12"
                    height="9"
                    alt="invited you to"
                  />
                </Column>
                <Column align="left">
                  <Img
                    className="rounded-full"
                    src={teamImage}
                    width="64"
                    height="64"
                  />
                </Column>
              </Row>
            </Section>
            <Section className="mt-[32px] mb-[32px] text-center">
              <Button
                className="rounded bg-[#000000] px-5 py-3 text-center font-semibold text-[12px] text-white no-underline"
                href={inviteLink}
              >
                Join the team
              </Button>
            </Section>
            <Text className="text-[14px] text-black leading-[24px]">
              or copy and paste this URL into your browser:{' '}
              <Link href={inviteLink} className="text-blue-600 no-underline">
                {inviteLink}
              </Link>
            </Text>
            <Hr className="mx-0 my-[26px] w-full border border-[#eaeaea] border-solid" />
            <Text className="text-[#666666] text-[12px] leading-[24px]">
              This invitation was intended for{' '}
              <span className="text-black">{username}</span>. This invite was
              sent from <span className="text-black">{inviteFromIp}</span>{' '}
              located in{' '}
              <span className="text-black">{inviteFromLocation}</span>. If you
              were not expecting this invitation, you can ignore this email. If
              you are concerned about your account's safety, please reply to
              this email to get in touch with us.
            </Text>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
};

VercelInviteUserEmail.PreviewProps = {
  username: 'alanturing',
  userImage: `${baseUrl}/static/vercel-user.png`,
  invitedByUsername: 'Alan',
  invitedByEmail: 'alan.turing@example.com',
  teamName: 'Enigma',
  teamImage: `${baseUrl}/static/vercel-team.png`,
  inviteLink: 'https://vercel.com/teams/invite/foo',
  inviteFromIp: '204.13.186.218',
  inviteFromLocation: 'São Paulo, Brazil',
} as VercelInviteUserEmailProps;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `VercelInviteUserEmail()`
- `baseUrl()`
- `previewText()`

### Interfaces

- `VercelInviteUserEmailProps`

### Dependencies

This file imports/requires:

- `@react-email/components`
- `@react-email/tailwind`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 111

- `Alan`
- `Body`
- `Brazil`
- `Button`
- `Column`
- `Container`
- `Enigma`
- `Head`
- `Heading`
- `Hello`
- `Html`
- `Img`
- `Join`
- `Link`
- `Paulo`
- `Preview`
- `PreviewProps`
- `Row`
- `Section`
- `Tailwind`
- `Text`
- `VERCEL_URL`
- `Vercel`
- `VercelInviteUserEmail`
- `VercelInviteUserEmailProps`
- `about`
- `account`
- `alan`
- `alanturing`
- `align`
- `alt`
- `arrow`
- `auto`
- `baseUrl`
- `black`
- `blue`
- `border`
- `browser`
- `center`
- `className`
- `com`
- `components`
- `concerned`
- `copy`
- `eaeaea`
- `email`
- `env`
- `example`
- `expecting`
- `font`
- `foo`
- `full`
- `get`
- `height`
- `href`
- `https`
- `ignore`
- `intended`
- `interface`
- `into`
- `invitation`
- `invite`
- `inviteFromIp`
- `inviteFromLocation`
- `inviteLink`
- `invited`
- `invitedByEmail`
- `invitedByUsername`
- `leading`
- `left`
- `located`
- `logo`
- `mailto`
- `max`
- `normal`
- `paste`
- `please`
- `png`
- `previewText`
- `process`
- `react`
- `reply`
- `right`
- `rounded`
- `safety`
- `sans`
- `semibold`
- `sent`
- `solid`
- `span`
- `src`
- `static`
- `string`
- `strong`
- `tailwind`
- `team`
- `teamImage`
- `teamName`
- `teams`
- `text`
- `touch`
- `turing`
- `underline`
- `user`
- `userImage`
- `username`
- `vercel`
- `white`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

