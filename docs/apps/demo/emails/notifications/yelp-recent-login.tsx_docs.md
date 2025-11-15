# Documentation: yelp-recent-login.tsx
**File Path:** `apps/demo/emails/notifications/yelp-recent-login.tsx`
**Language:** tsx
**Size:** 4,235 bytes
**Lines:** 139
**Generated:** 2025-11-15T20:37:33.171541Z

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

- **Path:** `apps/demo/emails/notifications/yelp-recent-login.tsx`
- **Name:** `yelp-recent-login.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,235 bytes (4.14 KB)
- **Lines of Code:** 139

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
  Html,
  Img,
  Preview,
  Row,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';
import tailwindConfig from '../tailwind.config';

interface YelpRecentLoginEmailProps {
  userFirstName?: string;
  loginDate?: Date;
  loginDevice?: string;
  loginLocation?: string;
  loginIp?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const YelpRecentLoginEmail = ({
  userFirstName,
  loginDate,
  loginDevice,
  loginLocation,
  loginIp,
}: YelpRecentLoginEmailProps) => {
  const formattedDate = new Intl.DateTimeFormat('en', {
    dateStyle: 'long',
    timeStyle: 'short',
  }).format(loginDate);

  return (
    <Html>
      <Tailwind config={tailwindConfig}>
        <Head />
        <Body className="bg-white font-yelp">
          <Preview>Yelp recent login</Preview>
          <Container>
            <Section className="px-5 py-[30px]">
              <Img src={`${baseUrl}/static/yelp-logo.png`} alt="Yelp logo" />
            </Section>

            <Section className="border border-solid border-black/10 rounded overflow-hidden">
              <Row>
                <Img
                  className="max-w-full"
                  width={620}
                  src={`${baseUrl}/static/yelp-header.png`}
                  alt="Yelp header illustration"
                />
              </Row>

              <Row className="p-5 pb-0">
                <Column>
                  <Heading className="text-[32px] font-bold text-center">
                    Hi {userFirstName},
                  </Heading>
                  <Heading
                    as="h2"
                    className="text-[26px] font-bold text-center"
                  >
                    We noticed a recent login to your Yelp account.
                  </Heading>

                  <Text className="text-base">
                    <b>Time: </b>
                    {formattedDate}
                  </Text>
                  <Text className="text-base -mt-[5px]">
                    <b>Device: </b>
                    {loginDevice}
                  </Text>
                  <Text className="text-base -mt-[5px]">
                    <b>Location: </b>
                    {loginLocation}
                  </Text>
                  <Text className="text-black/50 text-sm leading-[24px] -mt-[5px]">
                    *Approximate geographic location based on IP address:
                    {loginIp}
                  </Text>

                  <Text className="text-base">
                    If this was you, there's nothing else you need to do.
                  </Text>
                  <Text className="text-base -mt-[5px]">
                    If this wasn't you or if you have additional questions,
                    please see our support page.
                  </Text>
                </Column>
              </Row>
              <Row className="p-5 pt-0">
                <Column className="text-center" colSpan={2}>
                  <Button className="bg-[#e00707] rounded border border-solid border-black/10 text-white font-bold cursor-pointer inline-block px-[30px] py-3 no-underline">
                    Learn More
                  </Button>
                </Column>
              </Row>
            </Section>

            <Section className="pt-[45px]">
              <Img
                className="max-w-full"
                width={620}
                src={`${baseUrl}/static/yelp-footer.png`}
                alt="Yelp footer decoration"
              />
            </Section>

            <Text className="text-center text-xs leading-[24px] text-black/70">
              © 2022 | Yelp Inc., 350 Mission Street, San Francisco, CA 94105,
              U.S.A. | www.yelp.com
            </Text>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
};

YelpRecentLoginEmail.PreviewProps = {
  userFirstName: 'Alan',
  loginDate: new Date('September 7, 2022, 10:58 am'),
  loginDevice: 'Chrome on Mac OS X',
  loginLocation: 'Upland, California, United States',
  loginIp: '47.149.53.167',
} as YelpRecentLoginEmailProps;

export default YelpRecentLoginEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `YelpRecentLoginEmail()`
- `baseUrl()`
- `formattedDate()`

### Interfaces

- `YelpRecentLoginEmailProps`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 120

- `Alan`
- `Approximate`
- `Body`
- `Button`
- `California`
- `Chrome`
- `Column`
- `Container`
- `Date`
- `DateTimeFormat`
- `Device`
- `Francisco`
- `Head`
- `Heading`
- `Html`
- `Img`
- `Inc`
- `Intl`
- `Learn`
- `Location`
- `Mac`
- `Mission`
- `More`
- `Preview`
- `PreviewProps`
- `Row`
- `San`
- `Section`
- `September`
- `States`
- `Street`
- `Tailwind`
- `Text`
- `Time`
- `United`
- `Upland`
- `VERCEL_URL`
- `Yelp`
- `YelpRecentLoginEmail`
- `YelpRecentLoginEmailProps`
- `account`
- `additional`
- `address`
- `alt`
- `base`
- `baseUrl`
- `based`
- `black`
- `block`
- `bold`
- `border`
- `center`
- `className`
- `colSpan`
- `com`
- `components`
- `config`
- `cursor`
- `dateStyle`
- `decoration`
- `e00707`
- `email`
- `env`
- `font`
- `footer`
- `format`
- `formattedDate`
- `full`
- `geographic`
- `header`
- `hidden`
- `https`
- `illustration`
- `inline`
- `interface`
- `leading`
- `location`
- `login`
- `loginDate`
- `loginDevice`
- `loginIp`
- `loginLocation`
- `logo`
- `long`
- `max`
- `need`
- `nothing`
- `noticed`
- `our`
- `overflow`
- `page`
- `please`
- `png`
- `pointer`
- `process`
- `questions`
- `react`
- `recent`
- `rounded`
- `see`
- `short`
- `solid`
- `src`
- `static`
- `string`
- `support`
- `tailwind`
- `tailwindConfig`
- `text`
- `there`
- `timeStyle`
- `underline`
- `userFirstName`
- `wasn`
- `white`
- `width`
- `www`
- `yelp`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

