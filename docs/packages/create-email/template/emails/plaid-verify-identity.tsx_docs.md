# Documentation: plaid-verify-identity.tsx
**File Path:** `packages/create-email/template/emails/plaid-verify-identity.tsx`
**Language:** tsx
**Size:** 3,456 bytes
**Lines:** 158
**Generated:** 2025-11-15T20:37:32.329562Z

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

- **Path:** `packages/create-email/template/emails/plaid-verify-identity.tsx`
- **Name:** `plaid-verify-identity.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,456 bytes (3.38 KB)
- **Lines of Code:** 158

---

## Original Source

```tsx
import {
  Body,
  Container,
  Head,
  Heading,
  Html,
  Img,
  Link,
  Section,
  Text,
} from '@react-email/components';

interface PlaidVerifyIdentityEmailProps {
  validationCode?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const PlaidVerifyIdentityEmail = ({
  validationCode,
}: PlaidVerifyIdentityEmailProps) => (
  <Html>
    <Head />
    <Body style={main}>
      <Container style={container}>
        <Img
          src={`${baseUrl}/static/plaid-logo.png`}
          width="212"
          height="88"
          alt="Plaid"
          style={logo}
        />
        <Text style={tertiary}>Verify Your Identity</Text>
        <Heading style={secondary}>
          Enter the following code to finish linking Venmo.
        </Heading>
        <Section style={codeContainer}>
          <Text style={code}>{validationCode}</Text>
        </Section>
        <Text style={paragraph}>Not expecting this email?</Text>
        <Text style={paragraph}>
          Contact{' '}
          <Link href="mailto:login@plaid.com" style={link}>
            login@plaid.com
          </Link>{' '}
          if you did not request this code.
        </Text>
      </Container>
      <Text style={footer}>Securely powered by Plaid.</Text>
    </Body>
  </Html>
);

PlaidVerifyIdentityEmail.PreviewProps = {
  validationCode: '144833',
} as PlaidVerifyIdentityEmailProps;

export default PlaidVerifyIdentityEmail;

const main = {
  backgroundColor: '#ffffff',
  fontFamily: 'HelveticaNeue,Helvetica,Arial,sans-serif',
};

const container = {
  backgroundColor: '#ffffff',
  border: '1px solid #eee',
  borderRadius: '5px',
  boxShadow: '0 5px 10px rgba(20,50,70,.2)',
  marginTop: '20px',
  maxWidth: '360px',
  margin: '0 auto',
  padding: '68px 0 130px',
};

const logo = {
  margin: '0 auto',
};

const tertiary = {
  color: '#0a85ea',
  fontSize: '11px',
  fontWeight: 700,
  fontFamily: 'HelveticaNeue,Helvetica,Arial,sans-serif',
  height: '16px',
  letterSpacing: '0',
  lineHeight: '16px',
  margin: '16px 8px 8px 8px',
  textTransform: 'uppercase' as const,
  textAlign: 'center' as const,
};

const secondary = {
  color: '#000',
  display: 'inline-block',
  fontFamily: 'HelveticaNeue-Medium,Helvetica,Arial,sans-serif',
  fontSize: '20px',
  fontWeight: 500,
  lineHeight: '24px',
  marginBottom: '0',
  marginTop: '0',
  textAlign: 'center' as const,
};

const codeContainer = {
  background: 'rgba(0,0,0,.05)',
  borderRadius: '4px',
  margin: '16px auto 14px',
  verticalAlign: 'middle',
  width: '280px',
};

const code = {
  color: '#000',
  display: 'inline-block',
  fontFamily: 'HelveticaNeue-Bold',
  fontSize: '32px',
  fontWeight: 700,
  letterSpacing: '6px',
  lineHeight: '40px',
  paddingBottom: '8px',
  paddingTop: '8px',
  margin: '0 auto',
  width: '100%',
  textAlign: 'center' as const,
};

const paragraph = {
  color: '#444',
  fontSize: '15px',
  fontFamily: 'HelveticaNeue,Helvetica,Arial,sans-serif',
  letterSpacing: '0',
  lineHeight: '23px',
  padding: '0 40px',
  margin: '0',
  textAlign: 'center' as const,
};

const link = {
  color: '#444',
  textDecoration: 'underline',
};

const footer = {
  color: '#000',
  fontSize: '12px',
  fontWeight: 800,
  letterSpacing: '0',
  lineHeight: '23px',
  margin: '0',
  marginTop: '20px',
  fontFamily: 'HelveticaNeue,Helvetica,Arial,sans-serif',
  textAlign: 'center' as const,
  textTransform: 'uppercase' as const,
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `PlaidVerifyIdentityEmail()`
- `baseUrl()`
- `code()`
- `codeContainer()`
- `container()`
- `footer()`
- `link()`
- `logo()`
- `main()`
- `paragraph()`
- `secondary()`
- `tertiary()`

### Interfaces

- `PlaidVerifyIdentityEmailProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 101

- `Arial`
- `Body`
- `Bold`
- `Contact`
- `Container`
- `Enter`
- `Head`
- `Heading`
- `Helvetica`
- `HelveticaNeue`
- `Html`
- `Identity`
- `Img`
- `Link`
- `Medium`
- `Plaid`
- `PlaidVerifyIdentityEmail`
- `PlaidVerifyIdentityEmailProps`
- `PreviewProps`
- `Section`
- `Securely`
- `Text`
- `VERCEL_URL`
- `Venmo`
- `Verify`
- `Your`
- `alt`
- `auto`
- `background`
- `backgroundColor`
- `baseUrl`
- `block`
- `border`
- `borderRadius`
- `boxShadow`
- `center`
- `code`
- `codeContainer`
- `color`
- `com`
- `components`
- `container`
- `display`
- `eee`
- `email`
- `env`
- `expecting`
- `ffffff`
- `finish`
- `following`
- `fontFamily`
- `fontSize`
- `fontWeight`
- `footer`
- `height`
- `href`
- `https`
- `inline`
- `interface`
- `letterSpacing`
- `lineHeight`
- `link`
- `linking`
- `login`
- `logo`
- `mailto`
- `main`
- `margin`
- `marginBottom`
- `marginTop`
- `maxWidth`
- `middle`
- `padding`
- `paddingBottom`
- `paddingTop`
- `paragraph`
- `plaid`
- `png`
- `powered`
- `process`
- `react`
- `request`
- `rgba`
- `sans`
- `secondary`
- `serif`
- `solid`
- `src`
- `static`
- `string`
- `style`
- `tertiary`
- `textAlign`
- `textDecoration`
- `textTransform`
- `underline`
- `uppercase`
- `validationCode`
- `verticalAlign`
- `width`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

