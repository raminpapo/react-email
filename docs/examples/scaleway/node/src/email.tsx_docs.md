# Documentation: email.tsx
**File Path:** `examples/scaleway/node/src/email.tsx`
**Language:** tsx
**Size:** 1,349 bytes
**Lines:** 59
**Generated:** 2025-11-15T20:37:32.660490Z

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

- **Path:** `examples/scaleway/node/src/email.tsx`
- **Name:** `email.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,349 bytes (1.32 KB)
- **Lines of Code:** 59

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
  Section,
  Text,
} from '@react-email/components';
import type { FC } from 'react';

interface EmailProps {
  url: string;
  username: string;
  invitedByUsername: string;
  teamName: string;
  invitedByEmail: string;
}

export const Email: FC<Readonly<EmailProps>> = ({
  invitedByUsername,
  username,
  teamName,
  invitedByEmail,
}) => {
  const previewText = `Production INCIDENT ${invitedByUsername} on Scaleway`;
  return (
    <Html lang="en">
      <Head />
      <Preview>{previewText}</Preview>
      <Body>
        <Container>
          <Section>
            <Img
              src="https://www-uploads.scaleway.com/Logos_Image_4ce23fe78a.webp"
              width="400"
              height="200"
              alt="Scaleway"
            />
          </Section>
          <Heading>
            Join <strong>{teamName}</strong> on <strong>Scaleway</strong>
          </Heading>
          <Text>Hello {username},</Text>
          <Text>
            <strong>{invitedByUsername}</strong> (
            <Link href={`mailto:${invitedByEmail}`}>{invitedByEmail}</Link>) has
            invited you to the <strong>{teamName}</strong> team on{' '}
            <strong>Scaleway</strong>.
          </Text>
        </Container>
      </Body>
    </Html>
  );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `previewText()`

### Interfaces

- `EmailProps`

### Dependencies

This file imports/requires:

- `@react-email/components`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 46

- `Body`
- `Container`
- `Email`
- `EmailProps`
- `Head`
- `Heading`
- `Hello`
- `Html`
- `Img`
- `Join`
- `Link`
- `Preview`
- `Production`
- `Readonly`
- `Scaleway`
- `Section`
- `Text`
- `alt`
- `com`
- `components`
- `email`
- `height`
- `href`
- `https`
- `interface`
- `invited`
- `invitedByEmail`
- `invitedByUsername`
- `lang`
- `mailto`
- `previewText`
- `react`
- `scaleway`
- `src`
- `string`
- `strong`
- `team`
- `teamName`
- `type`
- `uploads`
- `url`
- `username`
- `webp`
- `width`
- `www`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

