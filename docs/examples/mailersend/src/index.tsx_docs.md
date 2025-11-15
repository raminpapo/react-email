# Documentation: index.tsx
**File Path:** `examples/mailersend/src/index.tsx`
**Language:** tsx
**Size:** 632 bytes
**Lines:** 21
**Generated:** 2025-11-15T20:37:32.688023Z

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

- **Path:** `examples/mailersend/src/index.tsx`
- **Name:** `index.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 632 bytes (0.62 KB)
- **Lines of Code:** 21

---

## Original Source

```tsx
import { render } from '@react-email/components';
import { EmailParams, MailerSend, Recipient, Sender } from 'mailersend';
import { Email } from './email';

const mailerSend = new MailerSend({
  apiKey: process.env.MAILERSEND_API_KEY || '',
});

const emailHtml = await render(<Email url="https://example.com" />);

const sentFrom = new Sender('you@yourdomain.com', 'Your name');
const recipients = [new Recipient('your@client.com', 'Your Client')];

const emailParams = new EmailParams()
  .setFrom(sentFrom)
  .setTo(recipients)
  .setSubject('This is a Subject')
  .setHtml(emailHtml);

await mailerSend.email.send(emailParams);

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `emailHtml()`
- `emailParams()`
- `mailerSend()`
- `recipients()`
- `sentFrom()`

### Dependencies

This file imports/requires:

- `./email`
- `@react-email/components`
- `mailersend`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 36

- `Client`
- `Email`
- `EmailParams`
- `MAILERSEND_API_KEY`
- `MailerSend`
- `Recipient`
- `Sender`
- `Subject`
- `Your`
- `apiKey`
- `client`
- `com`
- `components`
- `email`
- `emailHtml`
- `emailParams`
- `env`
- `example`
- `https`
- `mailerSend`
- `mailersend`
- `name`
- `process`
- `react`
- `recipients`
- `render`
- `send`
- `sentFrom`
- `setFrom`
- `setHtml`
- `setSubject`
- `setTo`
- `url`
- `you`
- `your`
- `yourdomain`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

