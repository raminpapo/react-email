# Documentation: utils.ts
**File Path:** `apps/web/src/components/sections/playground/utils.ts`
**Language:** typescript
**Size:** 4,694 bytes
**Lines:** 124
**Generated:** 2025-11-15T20:37:32.959018Z

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

- **Path:** `apps/web/src/components/sections/playground/utils.ts`
- **Name:** `utils.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 4,694 bytes (4.58 KB)
- **Lines of Code:** 124

---

## Original Source

```typescript
export const tailwindCSSCode = `import { Body, Button, Container, Head, Heading, Html, Img, Preview, Section, Tailwind, Text } from '@react-email/components';

interface WelcomeEmailProps {
  username?: string;
  company?: string;
}

const WelcomeEmail = ({
  username = 'Nicole',
  company = 'Helix',
}: WelcomeEmailProps) => {
  const previewText = \`Welcome to \${company}, \${username}!\`;

  return (
    <Html>
      <Head />
      <Preview>{previewText}</Preview>
      <Tailwind>
        <Body className="bg-black m-auto font-sans">
          <Container className="mb-10 mx-auto p-5 max-w-[465px]">
            <Section className="mt-10">
              <Img
                src={\`https://example.com/brand/example-logo.png\`}
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
              <Button
                className="py-2.5 px-5 bg-white rounded-md text-black text-sm font-semibold no-underline text-center"
                href={\`https://example.com/get-started\`}
              >
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

export default WelcomeEmail;`;

export const cssCode = `import { Body, Button, Container, Head, Heading, Html, Img, Preview, Section, Tailwind, Text } from '@react-email/components';

interface WelcomeEmailProps {
  username?: string;
  company?: string;
}

const WelcomeEmail = ({
  username = 'Nicole',
  company = 'Helix',
}: WelcomeEmailProps) => {
  const previewText = \`Welcome to \${company}, \${username}!\`;

  return (
    <Html>
      <Head />
      <Preview>{previewText}</Preview>
      <Tailwind>
        <Body style={{ backgroundColor: 'black', margin: 'auto', fontFamily: 'var(--font-sans)' }}>
          <Container style={{ marginBottom: '40px', marginLeft: 'auto', marginRight: 'auto', padding: '20px', width: '465px' }}>
            <Section style={{ marginTop: '40px' }}>
              <Img
                src={\`https://example.com/brand/example-logo.png\`}
                width="60"
                height="60"
                alt="Logo Example"
                style={{ margin: '0', marginLeft: 'auto', marginRight: 'auto' }}
              />
            </Section>
            <Heading style={{ fontSize: '24px', color: 'white', fontWeight: 'normal', textAlign: 'center', margin: '0', marginTop: '32px', marginLeft: '0', marginRight: '0' }}>
              Welcome to <strong>{company}</strong>, {username}!
            </Heading>
            <Text style={{ textAlign: 'start', fontSize: '14px', color: 'white' }}>
              Hello {username},
            </Text>
            <Text style={{ textAlign: 'start', fontSize: '14px', color: 'white', lineHeight: '1.625' }}>
              We're excited to have you onboard at <strong>{company}</strong>.
              We hope you enjoy your journey with us. If you have any questions
              or need assistance, feel free to reach out.
            </Text>
            <Section style={{ textAlign: 'center', marginTop: '32px', marginBottom: '32px' }}>
              <Button
                style={{ padding: '10px 20px', backgroundColor: 'white', borderRadius: '6px', color: 'black', fontSize: '14px', fontWeight: 'semibold', textDecoration: 'none', textAlign: 'center' }}
                href={\`https://example.com/get-started\`}
              >
                Get Started
              </Button>
            </Section>
            <Text style={{ textAlign: 'start', fontSize: '14px', color: 'white' }}>
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

export default WelcomeEmail;`;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `WelcomeEmail()`
- `cssCode()`
- `previewText()`
- `tailwindCSSCode()`

### Interfaces

- `WelcomeEmailProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 94

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
- `any`
- `assistance`
- `auto`
- `backgroundColor`
- `black`
- `borderRadius`
- `brand`
- `center`
- `className`
- `color`
- `com`
- `company`
- `components`
- `cssCode`
- `email`
- `enjoy`
- `example`
- `excited`
- `feel`
- `font`
- `fontFamily`
- `fontSize`
- `fontWeight`
- `free`
- `get`
- `height`
- `hope`
- `href`
- `https`
- `interface`
- `journey`
- `leading`
- `lineHeight`
- `logo`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `max`
- `need`
- `normal`
- `onboard`
- `out`
- `padding`
- `png`
- `previewText`
- `questions`
- `reach`
- `react`
- `relaxed`
- `rounded`
- `sans`
- `semibold`
- `src`
- `start`
- `started`
- `string`
- `strong`
- `style`
- `tailwindCSSCode`
- `text`
- `textAlign`
- `textDecoration`
- `underline`
- `username`
- `white`
- `width`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

