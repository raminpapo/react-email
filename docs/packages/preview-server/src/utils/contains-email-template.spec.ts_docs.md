# Documentation: contains-email-template.spec.ts
**File Path:** `packages/preview-server/src/utils/contains-email-template.spec.ts`
**Language:** typescript
**Size:** 4,079 bytes
**Lines:** 137
**Generated:** 2025-11-15T20:37:32.010222Z

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

- **Path:** `packages/preview-server/src/utils/contains-email-template.spec.ts`
- **Name:** `contains-email-template.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 4,079 bytes (3.98 KB)
- **Lines of Code:** 137

---

## Original Source

```typescript
import {
  containsEmailTemplate,
  removeFilenameExtension,
} from './contains-email-template';
import type { EmailsDirectory } from './get-emails-directory-metadata';

describe('removeFilenameExtension()', () => {
  it('works with a single .', () => {
    expect(removeFilenameExtension('email-template.tsx')).toBe(
      'email-template',
    );
  });

  it('works with an example test file', () => {
    expect(removeFilenameExtension('email-template.spec.tsx')).toBe(
      'email-template.spec',
    );
  });

  it('does nothing when there is no extension', () => {
    expect(removeFilenameExtension('email-template')).toBe('email-template');
  });
});

describe('containsEmailTemplate()', () => {
  const directory: EmailsDirectory = {
    absolutePath: '/fake/path/emails',
    directoryName: 'emails',
    relativePath: '',
    emailFilenames: [],
    subDirectories: [
      {
        absolutePath: '/fake/path/emails/magic-links',
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
        subDirectories: [
          {
            absolutePath: '/fake/path/emails/magic-links/resend',
            directoryName: 'resend',
            emailFilenames: ['verify-email'],
            relativePath: 'magic-links/resend',
            subDirectories: [],
          },
        ],
      },
      {
        absolutePath: '/fake/path/emails/first/second',
        directoryName: 'first/second',
        relativePath: 'first/second',
        emailFilenames: ['email'],
        subDirectories: [],
      },
      {
        absolutePath: '/fake/path/emails/newsletters',
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
        absolutePath: '/fake/path/emails/notifications',
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
        absolutePath: '/fake/path/emails/receipts',
        directoryName: 'receipts',
        relativePath: 'receipts',
        emailFilenames: ['apple-receipt', 'nike-receipt'],
        subDirectories: [],
      },
      {
        absolutePath: '/fake/path/emails/reset-password',
        directoryName: 'reset-password',
        relativePath: 'reset-password',
        emailFilenames: ['dropbox-reset-password', 'twitch-reset-password'],
        subDirectories: [],
      },
      {
        absolutePath: '/fake/path/emails/reviews',
        directoryName: 'reviews',
        relativePath: 'reviews',
        emailFilenames: ['airbnb-review', 'amazon-review'],
        subDirectories: [],
      },
      {
        absolutePath: '/fake/path/emails/welcome',
        directoryName: 'welcome',
        relativePath: 'welcome',
        emailFilenames: ['koala-welcome', 'netlify-welcome', 'stripe-welcome'],
        subDirectories: [],
      },
    ],
  };

  it('works with collapsed email directory', () => {
    expect(containsEmailTemplate('first/second/email', directory)).toBe(true);
  });

  it('works with email inside a single sub directory', () => {
    expect(containsEmailTemplate('welcome/koala-welcome', directory)).toBe(
      true,
    );
    expect(containsEmailTemplate('welcome/missing-template', directory)).toBe(
      false,
    );
  });

  it('works with email inside a second sub directory', () => {
    expect(
      containsEmailTemplate('magic-links/resend/verify-email', directory),
    ).toBe(true);
    expect(
      containsEmailTemplate('magic-links/resend/missing-template', directory),
    ).toBe(false);
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `./contains-email-template`
- `./get-emails-directory-metadata`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 90

- `EmailsDirectory`
- `absolutePath`
- `access`
- `airbnb`
- `amazon`
- `apple`
- `aws`
- `challengers`
- `code`
- `codepen`
- `collapsed`
- `confirm`
- `contains`
- `containsEmailTemplate`
- `describe`
- `directory`
- `directoryName`
- `dropbox`
- `email`
- `emailFilenames`
- `emails`
- `example`
- `expect`
- `extension`
- `fake`
- `file`
- `first`
- `get`
- `github`
- `google`
- `identity`
- `inside`
- `invite`
- `koala`
- `linear`
- `link`
- `links`
- `login`
- `magic`
- `metadata`
- `missing`
- `netlify`
- `newsletters`
- `nike`
- `nothing`
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
- `removeFilenameExtension`
- `resend`
- `reset`
- `review`
- `reviews`
- `second`
- `single`
- `slack`
- `spec`
- `stack`
- `stripe`
- `sub`
- `subDirectories`
- `template`
- `test`
- `there`
- `tips`
- `toBe`
- `token`
- `tsx`
- `twitch`
- `type`
- `update`
- `user`
- `vercel`
- `verify`
- `welcome`
- `when`
- `works`
- `year`
- `yelp`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

