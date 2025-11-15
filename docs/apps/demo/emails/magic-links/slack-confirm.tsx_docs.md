# Documentation: slack-confirm.tsx
**File Path:** `apps/demo/emails/magic-links/slack-confirm.tsx`
**Language:** tsx
**Size:** 4,761 bytes
**Lines:** 160
**Generated:** 2025-11-15T20:37:33.182655Z

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

- **Path:** `apps/demo/emails/magic-links/slack-confirm.tsx`
- **Name:** `slack-confirm.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,761 bytes (4.65 KB)
- **Lines of Code:** 160

---

## Original Source

```tsx
import {
  Body,
  Column,
  Container,
  Head,
  Heading,
  Html,
  Img,
  Link,
  Preview,
  Row,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';
import tailwindConfig from '../tailwind.config';

interface SlackConfirmEmailProps {
  validationCode?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const SlackConfirmEmail = ({
  validationCode,
}: SlackConfirmEmailProps) => (
  <Html>
    <Head />
    <Tailwind config={tailwindConfig}>
      <Body className="bg-white font-slack mx-auto my-0">
        <Preview>Confirm your email address</Preview>
        <Container className="mx-auto my-0 py-0 px-5">
          <Section className="mt-8">
            <Img
              src={`${baseUrl}/static/slack-logo.png`}
              width="120"
              height="36"
              alt="Slack"
            />
          </Section>
          <Heading className="text-[#1d1c1d] text-4xl font-bold my-[30px] mx-0 p-0 leading-[42px]">
            Confirm your email address
          </Heading>
          <Text className="text-xl mb-7.5">
            Your confirmation code is below - enter it in your open browser
            window and we'll help you get signed in.
          </Text>

          <Section className="bg-[rgb(245,244,245)] rounded mb-[30px] py-10 px-[10px]">
            <Text className="text-3xl leading-[24px] text-center align-middle">
              {validationCode}
            </Text>
          </Section>

          <Text className="text-black text-sm leading-6">
            If you didn't request this email, there's nothing to worry about,
            you can safely ignore it.
          </Text>

          <Section>
            <Row className="mb-8 pl-2 pr-2">
              <Column className="w-2/3">
                <Img
                  src={`${baseUrl}/static/slack-logo.png`}
                  width="120"
                  height="36"
                  alt="Slack"
                />
              </Column>
              <Column align="right">
                <Link href="/">
                  <Img
                    src={`${baseUrl}/static/slack-twitter.png`}
                    width="32"
                    height="32"
                    alt="Slack"
                    className="inline ml-2"
                  />
                </Link>
                <Link href="/">
                  <Img
                    src={`${baseUrl}/static/slack-facebook.png`}
                    width="32"
                    height="32"
                    alt="Slack"
                    className="inline ml-2"
                  />
                </Link>
                <Link href="/">
                  <Img
                    src={`${baseUrl}/static/slack-linkedin.png`}
                    width="32"
                    height="32"
                    alt="Slack"
                    className="inline ml-2"
                  />
                </Link>
              </Column>
            </Row>
          </Section>

          <Section>
            <Link
              className="text-[#b7b7b7] underline"
              href="https://slackhq.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              Our blog
            </Link>
            &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
            <Link
              className="text-[#b7b7b7] underline"
              href="https://slack.com/legal"
              target="_blank"
              rel="noopener noreferrer"
            >
              Policies
            </Link>
            &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
            <Link
              className="text-[#b7b7b7] underline"
              href="https://slack.com/help"
              target="_blank"
              rel="noopener noreferrer"
            >
              Help center
            </Link>
            &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
            <Link
              className="text-[#b7b7b7] underline"
              href="https://slack.com/community"
              target="_blank"
              rel="noopener noreferrer"
              data-auth="NotApplicable"
              data-linkindex="6"
            >
              Slack Community
            </Link>
            <Text className="text-xs leading-[15px] text-left mb-[50px] text-[#b7b7b7]">
              ©2022 Slack Technologies, LLC, a Salesforce company. <br />
              500 Howard Street, San Francisco, CA 94105, USA <br />
              <br />
              All rights reserved.
            </Text>
          </Section>
        </Container>
      </Body>
    </Tailwind>
  </Html>
);

SlackConfirmEmail.PreviewProps = {
  validationCode: 'DJZ-TLX',
} as SlackConfirmEmailProps;

export default SlackConfirmEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `SlackConfirmEmail()`
- `baseUrl()`

### Interfaces

- `SlackConfirmEmailProps`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 113

- `All`
- `Body`
- `Column`
- `Community`
- `Confirm`
- `Container`
- `Francisco`
- `Head`
- `Heading`
- `Help`
- `Howard`
- `Html`
- `Img`
- `Link`
- `NotApplicable`
- `Our`
- `Policies`
- `Preview`
- `PreviewProps`
- `Row`
- `Salesforce`
- `San`
- `Section`
- `Slack`
- `SlackConfirmEmail`
- `SlackConfirmEmailProps`
- `Street`
- `Tailwind`
- `Technologies`
- `Text`
- `VERCEL_URL`
- `Your`
- `_blank`
- `about`
- `address`
- `align`
- `alt`
- `auth`
- `auto`
- `b7b7b7`
- `baseUrl`
- `below`
- `black`
- `blog`
- `bold`
- `browser`
- `center`
- `className`
- `code`
- `com`
- `community`
- `company`
- `components`
- `config`
- `confirmation`
- `data`
- `didn`
- `email`
- `enter`
- `env`
- `facebook`
- `font`
- `get`
- `height`
- `help`
- `href`
- `https`
- `ignore`
- `inline`
- `interface`
- `leading`
- `left`
- `legal`
- `linkedin`
- `linkindex`
- `logo`
- `middle`
- `nbsp`
- `noopener`
- `noreferrer`
- `nothing`
- `open`
- `png`
- `process`
- `react`
- `rel`
- `request`
- `reserved`
- `rgb`
- `right`
- `rights`
- `rounded`
- `safely`
- `signed`
- `slack`
- `slackhq`
- `src`
- `static`
- `string`
- `tailwind`
- `tailwindConfig`
- `target`
- `text`
- `there`
- `twitter`
- `underline`
- `validationCode`
- `white`
- `width`
- `window`
- `worry`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

