# Documentation: code-example.tsx
**File Path:** `apps/web/src/components/sections/playground/code-example.tsx`
**Language:** tsx
**Size:** 2,133 bytes
**Lines:** 73
**Generated:** 2025-11-15T20:37:32.952880Z

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

- **Path:** `apps/web/src/components/sections/playground/code-example.tsx`
- **Name:** `code-example.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,133 bytes (2.08 KB)
- **Lines of Code:** 73

---

## Original Source

```tsx
import {
  Body,
  Button,
  Container,
  Head,
  Heading,
  Html,
  Img,
  Preview,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';

const WelcomeEmail = ({
  username = 'Nicole',
  company = 'Helix',
}: WelcomeEmailProps) => {
  const previewText = `Welcome to ${company}, ${username}!`;

  return (
    <Html>
      <Head />
      <Preview>{previewText}</Preview>
      <Tailwind>
        <Body className="m-auto bg-black font-sans antialiased">
          <Container className="mb-10 mx-auto p-5 max-w-[465px]">
            <Section className="mt-10">
              <Img
                src={`${baseUrl}/brand/example-logo.png`}
                width="60"
                height="60"
                alt="Logo Example"
                className="my-0 mx-auto"
              />
            </Section>
            <Heading className="text-2xl text-white font-normal text-center p-0 my-8 mx-0">
              Welcome to <strong>{company}</strong>, {username}!
            </Heading>
            <Text className="text-start text-sm text-white">
              Hello {username},
            </Text>
            <Text className="text-start text-sm text-white leading-relaxed">
              We're excited to have you onboard at <strong>{company}</strong>.
              We hope you enjoy your journey with us. If you have any questions
              or need assistance, feel free to reach out.
            </Text>
            <Section className="text-center mt-[32px] mb-[32px]">
              <Button className="py-2.5 px-5 bg-white rounded-md text-black text-sm font-semibold no-underline text-center pointer-events-none select-none">
                Get Started
              </Button>
            </Section>
            <Text className="text-start text-sm text-white">
              Cheers,
              <br />
              The {company} Team
            </Text>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
};

interface WelcomeEmailProps {
  username?: string;
  company?: string;
}

const baseUrl = process.env.URL ? `https://${process.env.URL}` : '';

export default WelcomeEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `WelcomeEmail()`
- `baseUrl()`
- `previewText()`

### Interfaces

- `WelcomeEmailProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 79

- `Body`
- `Button`
- `Cheers`
- `Container`
- `Example`
- `Get`
- `Head`
- `Heading`
- `Helix`
- `Hello`
- `Html`
- `Img`
- `Logo`
- `Nicole`
- `Preview`
- `Section`
- `Started`
- `Tailwind`
- `Team`
- `Text`
- `Welcome`
- `WelcomeEmail`
- `WelcomeEmailProps`
- `alt`
- `antialiased`
- `any`
- `assistance`
- `auto`
- `baseUrl`
- `black`
- `brand`
- `center`
- `className`
- `company`
- `components`
- `email`
- `enjoy`
- `env`
- `events`
- `example`
- `excited`
- `feel`
- `font`
- `free`
- `height`
- `hope`
- `https`
- `interface`
- `journey`
- `leading`
- `logo`
- `max`
- `need`
- `normal`
- `onboard`
- `out`
- `png`
- `pointer`
- `previewText`
- `process`
- `questions`
- `reach`
- `react`
- `relaxed`
- `rounded`
- `sans`
- `select`
- `semibold`
- `src`
- `start`
- `string`
- `strong`
- `text`
- `underline`
- `username`
- `white`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

