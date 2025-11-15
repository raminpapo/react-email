# Documentation: with-tailwind.tsx
**File Path:** `benchmarks/tailwind-component/src/emails/with-tailwind.tsx`
**Language:** tsx
**Size:** 6,778 bytes
**Lines:** 199
**Generated:** 2025-11-15T20:37:33.238763Z

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

- **Path:** `benchmarks/tailwind-component/src/emails/with-tailwind.tsx`
- **Name:** `with-tailwind.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 6,778 bytes (6.62 KB)
- **Lines of Code:** 199

---

## Original Source

```tsx
import {
  Body,
  Column,
  Container,
  Head,
  Hr,
  Html,
  Img,
  Link,
  Preview,
  Row,
  Section,
  Text,
} from '@react-email/components';
import type { TailwindProps } from '../../../../packages/tailwind/dist';

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const GooglePlayPolicyUpdateEmailWithTailwind = ({
  Tailwind,
}: {
  Tailwind: React.FC<TailwindProps>;
}) => (
  <Tailwind
    config={{
      theme: {
        extend: {
          fontFamily: {
            main: '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif',
          },
        },
      },
    }}
  >
    <Html>
      <Head />
      <Preview>Google Play developers</Preview>
      <Body className="bg-[#dbddde] font-main">
        <Container className="mx-auto my-7 w-[610px] overflow-hidden rounded-md bg-white">
          <Section>
            <Row>
              <Column>
                <Img
                  alt="Google Play developers header blue transparent"
                  className="-mt-[1px]"
                  height="28"
                  src={`${baseUrl}/static/google-play-header.png`}
                  width="305"
                />
                <Img
                  alt="Google Play"
                  className="px-10 py-0"
                  height="31"
                  src={`${baseUrl}/static/google-play-logo.png`}
                  width="155"
                />
              </Column>
            </Row>
          </Section>

          <Section className="px-10 py-0">
            <Hr className="mx-0 my-5 border-[#e8eaed]" />
            <Text className="text-[#004dcf] text-sm leading-6">
              DEVELOPER UPDATE
            </Text>
            <Text className="text-sm leading-5">
              Hello Google Play Developer,
            </Text>
            <Text className="text-sm leading-5">
              We strive to make Google Play a safe and trusted experience for
              users.
            </Text>
            <Text className="text-sm leading-5">
              We've added clarifications to our{' '}
              <Link
                className="text-[#004dcf] text-sm leading-5"
                href="https://notifications.google.com"
              >
                Target API Level policy
              </Link>
              . Because this is a clarification, our enforcement standards and
              practices for this policy remain the same.
            </Text>
          </Section>
          <Section className="pl-10">
            <Text className="text-sm leading-5">
              We’re noting exceptions to the{' '}
              <Link
                className="text-[#004dcf] text-sm leading-5"
                href="https://notifications.google.com"
              >
                Target API Level policy
              </Link>
              , which can be found in our updated{' '}
              <Link
                className="text-[#004dcf] text-sm leading-5"
                href="https://notifications.google.com"
              >
                Help Center article.
              </Link>
              These exceptions include permanently private apps and apps that
              target automotive or wearables form factors and are bundled within
              the same package.{' '}
              <Link
                className="text-[#004dcf] text-sm leading-5"
                href="https://notifications.google.com"
              >
                Learn more
              </Link>
            </Text>
          </Section>
          <Section className="px-10 py-0">
            <Text className="text-sm leading-5">
              We’re also extending the deadline to give you more time to adjust
              to these changes. Now, apps that target API level 29 or below will
              start experiencing reduced distribution starting{' '}
              <b>Jan 31, 2023</b> instead of Nov 1, 2022. If you need more time
              to update your app, you can request an extension to keep your app
              discoverable to all users until May 1, 2023.
            </Text>
            <Hr className="mx-0 my-5 border-[#e8eaed]" />
          </Section>

          <Section className="px-10 py-0">
            <Text className="text-sm leading-5">Thank you,</Text>
            <Text className="text-[#3c4043] text-xl leading-5">
              The Google Play team
            </Text>
          </Section>

          <Section className="w-[90%] overflow-hidden rounded-md bg-[#f0fcff] pl-5">
            <Row>
              <Text className="text-sm leading-5">Connect with us</Text>
            </Row>
            <Row
              align="left"
              style={{
                width: '84px',
                float: 'left',
              }}
            >
              <Column style={{ paddingRight: '4px' }}>
                <Link href="https://notifications.google.com">
                  <Img
                    height="28"
                    src={`${baseUrl}/static/google-play-chat.png`}
                    width="28"
                  />
                </Link>
              </Column>
              <Column style={{ paddingRight: '4px' }}>
                <Link href="https://notifications.google.com">
                  <Img
                    height="28"
                    src={`${baseUrl}/static/google-play-icon.png`}
                    width="28"
                  />
                </Link>
              </Column>
              <Column style={{ paddingRight: '4px' }}>
                <Link href="https://notifications.google.com">
                  <Img
                    height="28"
                    src={`${baseUrl}/static/google-play-academy.png`}
                    width="28"
                  />
                </Link>
              </Column>
            </Row>
            <Row>
              <Img
                height="48"
                src={`${baseUrl}/static/google-play-footer.png`}
                width="540"
              />
            </Row>
          </Section>

          <Section className="!pt-7 px-10 py-0">
            <Text className="margin-0 text-center text-[#3c4043] text-xs leading-5">
              © 2022 Google LLC 1600 Amphitheatre Parkway, Mountain View, CA
              94043, USA
            </Text>
            <Text className="margin-0 text-center text-[#3c4043] text-xs leading-5">
              You have received this mandatory email service announcement to
              update you about important changes to your Google Play Developer
              account.
            </Text>
          </Section>
        </Container>
      </Body>
    </Html>
  </Tailwind>
);

export default GooglePlayPolicyUpdateEmailWithTailwind;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `GooglePlayPolicyUpdateEmailWithTailwind()`
- `baseUrl()`

### Dependencies

This file imports/requires:

- `../../../../packages/tailwind/dist`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 176

- `Amphitheatre`
- `Because`
- `BlinkMacSystemFont`
- `Body`
- `Cantarell`
- `Center`
- `Column`
- `Connect`
- `Container`
- `Developer`
- `Google`
- `GooglePlayPolicyUpdateEmailWithTailwind`
- `Head`
- `Hello`
- `Help`
- `Helvetica`
- `Html`
- `Img`
- `Jan`
- `Learn`
- `Level`
- `Link`
- `Mountain`
- `Neue`
- `Nov`
- `Now`
- `Oxygen`
- `Parkway`
- `Play`
- `Preview`
- `React`
- `Roboto`
- `Row`
- `Sans`
- `Section`
- `Segoe`
- `Tailwind`
- `TailwindProps`
- `Target`
- `Text`
- `Thank`
- `These`
- `Ubuntu`
- `VERCEL_URL`
- `View`
- `You`
- `about`
- `academy`
- `account`
- `added`
- `adjust`
- `align`
- `all`
- `also`
- `alt`
- `announcement`
- `app`
- `apple`
- `apps`
- `article`
- `auto`
- `automotive`
- `baseUrl`
- `below`
- `blue`
- `border`
- `bundled`
- `center`
- `changes`
- `chat`
- `clarification`
- `clarifications`
- `className`
- `com`
- `components`
- `config`
- `dbddde`
- `deadline`
- `developers`
- `discoverable`
- `dist`
- `distribution`
- `e8eaed`
- `email`
- `enforcement`
- `env`
- `exceptions`
- `experience`
- `experiencing`
- `extend`
- `extending`
- `extension`
- `f0fcff`
- `factors`
- `float`
- `font`
- `fontFamily`
- `footer`
- `form`
- `found`
- `give`
- `google`
- `header`
- `height`
- `hidden`
- `href`
- `https`
- `icon`
- `important`
- `include`
- `instead`
- `keep`
- `leading`
- `left`
- `level`
- `logo`
- `main`
- `make`
- `mandatory`
- `margin`
- `more`
- `need`
- `notifications`
- `noting`
- `our`
- `overflow`
- `package`
- `packages`
- `paddingRight`
- `permanently`
- `play`
- `png`
- `policy`
- `practices`
- `private`
- `process`
- `react`
- `received`
- `reduced`
- `remain`
- `request`
- `rounded`
- `safe`
- `same`
- `sans`
- `serif`
- `service`
- `src`
- `standards`
- `start`
- `starting`
- `static`
- `strive`
- `style`
- `system`
- `tailwind`
- `target`
- `team`
- `text`
- `theme`
- `these`
- `time`
- `transparent`
- `trusted`
- `type`
- `until`
- `update`
- `updated`
- `users`
- `wearables`
- `which`
- `white`
- `width`
- `within`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

