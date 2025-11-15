# Documentation: get-emails-directory-metadata.spec.ts
**File Path:** `packages/preview-server/src/utils/get-emails-directory-metadata.spec.ts`
**Language:** typescript
**Size:** 2,554 bytes
**Lines:** 83
**Generated:** 2025-11-15T20:37:32.019546Z

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

- **Path:** `packages/preview-server/src/utils/get-emails-directory-metadata.spec.ts`
- **Name:** `get-emails-directory-metadata.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,554 bytes (2.49 KB)
- **Lines of Code:** 83

---

## Original Source

```typescript
import path from 'node:path';
import { getEmailsDirectoryMetadata } from './get-emails-directory-metadata';

test('getEmailsDirectoryMetadata on demo emails', async () => {
  const emailsDirectoryPath = path.resolve(
    __dirname,
    '../../../../apps/demo/emails',
  );
  expect(await getEmailsDirectoryMetadata(emailsDirectoryPath)).toEqual({
    absolutePath: emailsDirectoryPath,
    directoryName: 'emails',
    relativePath: '',
    emailFilenames: [],
    subDirectories: [
      {
        absolutePath: `${emailsDirectoryPath}/magic-links`,
        directoryName: 'magic-links',
        relativePath: 'magic-links',
        emailFilenames: [
          'aws-verify-email',
          'linear-login-code',
          'notion-magic-link',
          'plaid-verify-identity',
          'raycast-magic-link',
          'slack-confirm',
        ],
        subDirectories: [],
      },
      {
        absolutePath: `${emailsDirectoryPath}/newsletters`,
        directoryName: 'newsletters',
        relativePath: 'newsletters',
        emailFilenames: [
          'codepen-challengers',
          'google-play-policy-update',
          'stack-overflow-tips',
        ],
        subDirectories: [],
      },
      {
        absolutePath: `${emailsDirectoryPath}/notifications`,
        directoryName: 'notifications',
        relativePath: 'notifications',
        emailFilenames: [
          'github-access-token',
          'papermark-year-in-review',
          'vercel-invite-user',
          'yelp-recent-login',
        ],
        subDirectories: [],
      },
      {
        absolutePath: `${emailsDirectoryPath}/receipts`,
        directoryName: 'receipts',
        relativePath: 'receipts',
        emailFilenames: ['apple-receipt', 'nike-receipt'],
        subDirectories: [],
      },
      {
        absolutePath: `${emailsDirectoryPath}/reset-password`,
        directoryName: 'reset-password',
        relativePath: 'reset-password',
        emailFilenames: ['dropbox-reset-password', 'twitch-reset-password'],
        subDirectories: [],
      },
      {
        absolutePath: `${emailsDirectoryPath}/reviews`,
        directoryName: 'reviews',
        relativePath: 'reviews',
        emailFilenames: ['airbnb-review', 'amazon-review'],
        subDirectories: [],
      },
      {
        absolutePath: `${emailsDirectoryPath}/welcome`,
        directoryName: 'welcome',
        relativePath: 'welcome',
        emailFilenames: ['koala-welcome', 'netlify-welcome', 'stripe-welcome'],
        subDirectories: [],
      },
    ],
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `emailsDirectoryPath()`

### Dependencies

This file imports/requires:

- `./get-emails-directory-metadata`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 72

- `__dirname`
- `absolutePath`
- `access`
- `airbnb`
- `amazon`
- `apple`
- `apps`
- `aws`
- `challengers`
- `code`
- `codepen`
- `confirm`
- `demo`
- `directory`
- `directoryName`
- `dropbox`
- `email`
- `emailFilenames`
- `emails`
- `emailsDirectoryPath`
- `expect`
- `get`
- `getEmailsDirectoryMetadata`
- `github`
- `google`
- `identity`
- `invite`
- `koala`
- `linear`
- `link`
- `links`
- `login`
- `magic`
- `metadata`
- `netlify`
- `newsletters`
- `nike`
- `node`
- `notifications`
- `notion`
- `overflow`
- `papermark`
- `password`
- `path`
- `plaid`
- `play`
- `policy`
- `raycast`
- `receipt`
- `receipts`
- `recent`
- `relativePath`
- `reset`
- `resolve`
- `review`
- `reviews`
- `slack`
- `stack`
- `stripe`
- `subDirectories`
- `test`
- `tips`
- `toEqual`
- `token`
- `twitch`
- `update`
- `user`
- `vercel`
- `verify`
- `welcome`
- `year`
- `yelp`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

