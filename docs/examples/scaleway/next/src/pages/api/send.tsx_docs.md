# Documentation: send.tsx
**File Path:** `examples/scaleway/next/src/pages/api/send.tsx`
**Language:** tsx
**Size:** 829 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:32.667356Z

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

- **Path:** `examples/scaleway/next/src/pages/api/send.tsx`
- **Name:** `send.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 829 bytes (0.81 KB)
- **Lines of Code:** 33

---

## Original Source

```tsx
import { render } from '@react-email/components';
import type { NextApiRequest, NextApiResponse } from 'next';
import { WaitlistEmail } from '../../../transactional/emails/waitlist';
import { scalewayTEM } from '../../lib/scaleway';

const send = async (req: NextApiRequest, res: NextApiResponse) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
    return;
  }

  await scalewayTEM.createEmail({
    from: {
      email: 'you@example.com',
      name: 'You',
    },
    to: [
      {
        email: 'user@gmail.com',
        name: 'User',
      },
    ],
    subject: 'Waitlist',
    html: await render(<WaitlistEmail name="User" />),
    text: '',
  });

  res.status(200).send({ data: 'Email sent successfully' });
};

export default send;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `send()`

### Dependencies

This file imports/requires:

- `../../../transactional/emails/waitlist`
- `../../lib/scaleway`
- `@react-email/components`
- `next`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 42

- `Allow`
- `Allowed`
- `Email`
- `Method`
- `NextApiRequest`
- `NextApiResponse`
- `User`
- `Waitlist`
- `WaitlistEmail`
- `You`
- `com`
- `components`
- `createEmail`
- `data`
- `email`
- `emails`
- `end`
- `example`
- `gmail`
- `html`
- `lib`
- `method`
- `name`
- `next`
- `react`
- `render`
- `req`
- `res`
- `scaleway`
- `scalewayTEM`
- `send`
- `sent`
- `setHeader`
- `status`
- `subject`
- `successfully`
- `text`
- `transactional`
- `type`
- `user`
- `waitlist`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

