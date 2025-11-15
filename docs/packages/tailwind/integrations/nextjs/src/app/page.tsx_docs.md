# Documentation: page.tsx
**File Path:** `packages/tailwind/integrations/nextjs/src/app/page.tsx`
**Language:** tsx
**Size:** 292 bytes
**Lines:** 8
**Generated:** 2025-11-15T20:37:32.374353Z

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

- **Path:** `packages/tailwind/integrations/nextjs/src/app/page.tsx`
- **Name:** `page.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 292 bytes (0.29 KB)
- **Lines of Code:** 8

---

## Original Source

```tsx
import { render } from '@react-email/components';
import { VercelInviteUserEmail } from '../../emails/vercel-invite-user';

export default async function Home() {
  const emailHtml = await render(<VercelInviteUserEmail />);
  return <div dangerouslySetInnerHTML={{ __html: emailHtml }} />;
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Home()`
- `emailHtml()`

### Dependencies

This file imports/requires:

- `../../emails/vercel-invite-user`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 14

- `Home`
- `VercelInviteUserEmail`
- `__html`
- `components`
- `dangerouslySetInnerHTML`
- `div`
- `email`
- `emailHtml`
- `emails`
- `invite`
- `react`
- `render`
- `user`
- `vercel`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

