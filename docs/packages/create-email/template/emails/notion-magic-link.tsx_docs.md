# Documentation: notion-magic-link.tsx
**File Path:** `packages/create-email/template/emails/notion-magic-link.tsx`
**Language:** tsx
**Size:** 3,614 bytes
**Lines:** 150
**Generated:** 2025-11-15T20:37:32.327514Z

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

- **Path:** `packages/create-email/template/emails/notion-magic-link.tsx`
- **Name:** `notion-magic-link.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,614 bytes (3.53 KB)
- **Lines of Code:** 150

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
  Preview,
  Text,
} from '@react-email/components';

interface NotionMagicLinkEmailProps {
  loginCode?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const NotionMagicLinkEmail = ({
  loginCode,
}: NotionMagicLinkEmailProps) => (
  <Html>
    <Head />
    <Preview>Log in with this magic link</Preview>
    <Body style={main}>
      <Container style={container}>
        <Heading style={h1}>Login</Heading>
        <Link
          href="https://notion.so"
          target="_blank"
          style={{
            ...link,
            display: 'block',
            marginBottom: '16px',
          }}
        >
          Click here to log in with this magic link
        </Link>
        <Text style={{ ...text, marginBottom: '14px' }}>
          Or, copy and paste this temporary login code:
        </Text>
        <code style={code}>{loginCode}</code>
        <Text
          style={{
            ...text,
            color: '#ababab',
            marginTop: '14px',
            marginBottom: '16px',
          }}
        >
          If you didn&apos;t try to login, you can safely ignore this email.
        </Text>
        <Text
          style={{
            ...text,
            color: '#ababab',
            marginTop: '12px',
            marginBottom: '38px',
          }}
        >
          Hint: You can set a permanent password in Settings & members → My
          account.
        </Text>
        <Img
          src={`${baseUrl}/static/notion-logo.png`}
          width="32"
          height="32"
          alt="Notion's Logo"
        />
        <Text style={footer}>
          <Link
            href="https://notion.so"
            target="_blank"
            style={{ ...link, color: '#898989' }}
          >
            Notion.so
          </Link>
          , the all-in-one-workspace
          <br />
          for your notes, tasks, wikis, and databases.
        </Text>
      </Container>
    </Body>
  </Html>
);

NotionMagicLinkEmail.PreviewProps = {
  loginCode: 'sparo-ndigo-amurt-secan',
} as NotionMagicLinkEmailProps;

export default NotionMagicLinkEmail;

const main = {
  backgroundColor: '#ffffff',
};

const container = {
  paddingLeft: '12px',
  paddingRight: '12px',
  margin: '0 auto',
};

const h1 = {
  color: '#333',
  fontFamily:
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",
  fontSize: '24px',
  fontWeight: 'bold',
  margin: '40px 0',
  padding: '0',
};

const link = {
  color: '#2754C5',
  fontFamily:
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",
  fontSize: '14px',
  textDecoration: 'underline',
};

const text = {
  color: '#333',
  fontFamily:
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",
  fontSize: '14px',
  margin: '24px 0',
};

const footer = {
  color: '#898989',
  fontFamily:
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",
  fontSize: '12px',
  lineHeight: '22px',
  marginTop: '12px',
  marginBottom: '24px',
};

const code = {
  display: 'inline-block',
  padding: '16px 4.5%',
  width: '90.5%',
  backgroundColor: '#f4f4f4',
  borderRadius: '5px',
  border: '1px solid #eee',
  color: '#333',
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `NotionMagicLinkEmail()`
- `baseUrl()`
- `code()`
- `container()`
- `footer()`
- `h1()`
- `link()`
- `main()`
- `text()`

### Interfaces

- `NotionMagicLinkEmailProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 119

- `BlinkMacSystemFont`
- `Body`
- `Cantarell`
- `Click`
- `Container`
- `Droid`
- `Fira`
- `Head`
- `Heading`
- `Helvetica`
- `Hint`
- `Html`
- `Img`
- `Link`
- `Log`
- `Login`
- `Logo`
- `Neue`
- `Notion`
- `NotionMagicLinkEmail`
- `NotionMagicLinkEmailProps`
- `Oxygen`
- `Preview`
- `PreviewProps`
- `Roboto`
- `Sans`
- `Segoe`
- `Settings`
- `Text`
- `Ubuntu`
- `VERCEL_URL`
- `You`
- `_blank`
- `ababab`
- `account`
- `all`
- `alt`
- `amurt`
- `apos`
- `apple`
- `auto`
- `backgroundColor`
- `baseUrl`
- `block`
- `bold`
- `border`
- `borderRadius`
- `code`
- `color`
- `components`
- `container`
- `copy`
- `databases`
- `didn`
- `display`
- `eee`
- `email`
- `env`
- `f4f4f4`
- `ffffff`
- `fontFamily`
- `fontSize`
- `fontWeight`
- `footer`
- `height`
- `here`
- `href`
- `https`
- `ignore`
- `inline`
- `interface`
- `lineHeight`
- `link`
- `log`
- `login`
- `loginCode`
- `logo`
- `magic`
- `main`
- `margin`
- `marginBottom`
- `marginTop`
- `members`
- `ndigo`
- `notes`
- `notion`
- `one`
- `padding`
- `paddingLeft`
- `paddingRight`
- `password`
- `paste`
- `permanent`
- `png`
- `process`
- `react`
- `safely`
- `sans`
- `secan`
- `serif`
- `set`
- `solid`
- `sparo`
- `src`
- `static`
- `string`
- `style`
- `system`
- `target`
- `tasks`
- `temporary`
- `text`
- `textDecoration`
- `underline`
- `width`
- `wikis`
- `workspace`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

