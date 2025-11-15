# Documentation: dropbox-reset-password.tsx
**File Path:** `apps/demo/emails/reset-password/dropbox-reset-password.tsx`
**Language:** tsx
**Size:** 2,844 bytes
**Lines:** 86
**Generated:** 2025-11-15T20:37:33.213655Z

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

- **Path:** `apps/demo/emails/reset-password/dropbox-reset-password.tsx`
- **Name:** `dropbox-reset-password.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,844 bytes (2.78 KB)
- **Lines of Code:** 86

---

## Original Source

```tsx
import {
  Body,
  Button,
  Container,
  Head,
  Html,
  Img,
  Link,
  Preview,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';
import tailwindConfig from '../tailwind.config';

interface DropboxResetPasswordEmailProps {
  userFirstname?: string;
  resetPasswordLink?: string;
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const DropboxResetPasswordEmail = ({
  userFirstname,
  resetPasswordLink,
}: DropboxResetPasswordEmailProps) => {
  return (
    <Html>
      <Head />
      <Tailwind config={tailwindConfig}>
        <Body className="bg-[#f6f9fc] py-2.5">
          <Preview>Dropbox reset your password</Preview>
          <Container className="bg-white border border-solid border-[#f0f0f0] p-[45px]">
            <Img
              src={`${baseUrl}/static/dropbox-logo.png`}
              width="40"
              height="33"
              alt="Dropbox"
            />
            <Section>
              <Text className="text-base font-dropbox font-light text-[#404040] leading-[26px]">
                Hi {userFirstname},
              </Text>
              <Text className="text-base font-dropbox font-light text-[#404040] leading-[26px]">
                Someone recently requested a password change for your Dropbox
                account. If this was you, you can set a new password here:
              </Text>
              <Button
                className="bg-[#007ee6] rounded text-white text-[15px] no-underline text-center font-dropbox-sans block w-[210px] py-[14px] px-[7px]"
                href={resetPasswordLink}
              >
                Reset password
              </Button>
              <Text className="text-base font-dropbox font-light text-[#404040] leading-[26px]">
                If you don&apos;t want to change your password or didn&apos;t
                request this, just ignore and delete this message.
              </Text>
              <Text className="text-base font-dropbox font-light text-[#404040] leading-[26px]">
                To keep your account secure, please don&apos;t forward this
                email to anyone. See our Help Center for{' '}
                <Link className="underline" href={resetPasswordLink}>
                  more security tips.
                </Link>
              </Text>
              <Text className="text-base font-dropbox font-light text-[#404040] leading-[26px]">
                Happy Dropboxing!
              </Text>
            </Section>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
};

DropboxResetPasswordEmail.PreviewProps = {
  userFirstname: 'Alan',
  resetPasswordLink: 'https://www.dropbox.com',
} as DropboxResetPasswordEmailProps;

DropboxResetPasswordEmail.tailwindConfig = tailwindConfig;

export default DropboxResetPasswordEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `DropboxResetPasswordEmail()`
- `baseUrl()`

### Interfaces

- `DropboxResetPasswordEmailProps`

### Dependencies

This file imports/requires:

- `../tailwind.config`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 93

- `Alan`
- `Body`
- `Button`
- `Center`
- `Container`
- `Dropbox`
- `DropboxResetPasswordEmail`
- `DropboxResetPasswordEmailProps`
- `Dropboxing`
- `Happy`
- `Head`
- `Help`
- `Html`
- `Img`
- `Link`
- `Preview`
- `PreviewProps`
- `Reset`
- `Section`
- `See`
- `Someone`
- `Tailwind`
- `Text`
- `VERCEL_URL`
- `account`
- `alt`
- `anyone`
- `apos`
- `base`
- `baseUrl`
- `block`
- `border`
- `center`
- `change`
- `className`
- `com`
- `components`
- `config`
- `delete`
- `didn`
- `don`
- `dropbox`
- `email`
- `env`
- `f0f0f0`
- `f6f9fc`
- `font`
- `forward`
- `height`
- `here`
- `href`
- `https`
- `ignore`
- `interface`
- `just`
- `keep`
- `leading`
- `light`
- `logo`
- `message`
- `more`
- `our`
- `password`
- `please`
- `png`
- `process`
- `react`
- `recently`
- `request`
- `requested`
- `reset`
- `resetPasswordLink`
- `rounded`
- `sans`
- `secure`
- `security`
- `set`
- `solid`
- `src`
- `static`
- `string`
- `tailwind`
- `tailwindConfig`
- `text`
- `tips`
- `underline`
- `userFirstname`
- `want`
- `white`
- `width`
- `www`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

