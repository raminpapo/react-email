# Documentation: index.tsx
**File Path:** `examples/scaleway/node/src/index.tsx`
**Language:** tsx
**Size:** 1,225 bytes
**Lines:** 58
**Generated:** 2025-11-15T20:37:32.661762Z

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

- **Path:** `examples/scaleway/node/src/index.tsx`
- **Name:** `index.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,225 bytes (1.20 KB)
- **Lines of Code:** 58

---

## Original Source

```tsx
import { render } from '@react-email/components';
import { createClient, TransactionalEmail } from '@scaleway/sdk';
import { Email } from './email.js';

const client = createClient({
  accessKey: process.env.ACCESS_KEY,
  secretKey: process.env.SECRET_KEY,
  defaultProjectId: process.env.PROJECT_ID,
  defaultRegion: 'fr-par',
  defaultZone: 'fr-par-1',
});

const transactionalEmailClient = new TransactionalEmail.v1alpha1.API(client);

const sender = {
  email: 'react-email@transactional.email.fr',
  subject: 'TEST',
  name: 'Team',
};

const userInvited = {
  email: 'XXXX@scaleway.com',
  name: 'TEST',
  teamName: 'Team',
};

const userInvitedBy = {
  email: 'XXXX@scaleway.com',
  name: 'TEST',
  teamName: 'Team',
};

const emailHtml = await render(
  <Email
    invitedByEmail={userInvitedBy.email}
    invitedByUsername={userInvitedBy.name}
    teamName={userInvited.teamName}
    url="https://www.scaleway.com/"
    username={userInvited.name}
  />,
);

await transactionalEmailClient.createEmail({
  from: {
    email: sender.email,
    name: sender.name,
  },
  to: [
    {
      email: userInvited.email,
      name: userInvited.name,
    },
  ],
  subject: sender.subject,
  text: '',
  html: emailHtml,
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `client()`
- `emailHtml()`
- `sender()`
- `transactionalEmailClient()`
- `userInvited()`
- `userInvitedBy()`

### Dependencies

This file imports/requires:

- `./email.js`
- `@react-email/components`
- `@scaleway/sdk`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 42

- `ACCESS_KEY`
- `Email`
- `PROJECT_ID`
- `SECRET_KEY`
- `Team`
- `TransactionalEmail`
- `accessKey`
- `client`
- `com`
- `components`
- `createClient`
- `createEmail`
- `defaultProjectId`
- `defaultRegion`
- `defaultZone`
- `email`
- `emailHtml`
- `env`
- `html`
- `https`
- `invitedByEmail`
- `invitedByUsername`
- `name`
- `par`
- `process`
- `react`
- `render`
- `scaleway`
- `sdk`
- `secretKey`
- `sender`
- `subject`
- `teamName`
- `text`
- `transactional`
- `transactionalEmailClient`
- `url`
- `userInvited`
- `userInvitedBy`
- `username`
- `v1alpha1`
- `www`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

