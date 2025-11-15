# Documentation: send.ts
**File Path:** `examples/resend/src/pages/api/send.ts`
**Language:** typescript
**Size:** 702 bytes
**Lines:** 27
**Generated:** 2025-11-15T20:37:32.674045Z

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

- **Path:** `examples/resend/src/pages/api/send.ts`
- **Name:** `send.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 702 bytes (0.69 KB)
- **Lines of Code:** 27

---

## Original Source

```typescript
import type { NextApiRequest, NextApiResponse } from 'next';
import { WaitlistEmail } from '../../../transactional/emails/waitlist';
import { resend } from '../../lib/resend';

const send = async (req: NextApiRequest, res: NextApiResponse) => {
  const { method } = req;

  switch (method) {
    case 'GET': {
      const data = await resend.emails.send({
        from: 'bu@resend.dev',
        to: 'delivered@resend.dev',
        subject: 'Waitlist',
        react: WaitlistEmail({ name: 'Bu' }),
      });

      res.status(200).send(data);
      break;
    }
    default:
      res.setHeader('Allow', ['GET']);
      res.status(405).end(`Method ${method} Not Allowed`);
  }
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

- `data()`
- `send()`

### Dependencies

This file imports/requires:

- `../../../transactional/emails/waitlist`
- `../../lib/resend`
- `next`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 27

- `Allow`
- `Allowed`
- `Method`
- `NextApiRequest`
- `NextApiResponse`
- `Waitlist`
- `WaitlistEmail`
- `data`
- `delivered`
- `dev`
- `emails`
- `end`
- `lib`
- `method`
- `name`
- `next`
- `react`
- `req`
- `res`
- `resend`
- `send`
- `setHeader`
- `status`
- `subject`
- `transactional`
- `type`
- `waitlist`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

