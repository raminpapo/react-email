# Documentation: page.tsx
**File Path:** `apps/web/src/app/templates/page.tsx`
**Language:** tsx
**Size:** 4,174 bytes
**Lines:** 159
**Generated:** 2025-11-15T20:37:32.844476Z

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

- **Path:** `apps/web/src/app/templates/page.tsx`
- **Name:** `page.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,174 bytes (4.08 KB)
- **Lines of Code:** 159

---

## Original Source

```tsx
import type { Metadata } from 'next';
import Image from 'next/image';
import { PageWrapper } from '@/components/page-wrapper';
import { Anchor } from '../../components/anchor';
import { Heading } from '../../components/heading';
import { PageTransition } from '../../components/page-transition';
import { Template } from '../../components/template';
import { Text } from '../../components/text';

const items = [
  {
    path: 'magic-links/aws-verify-email',
    name: 'AWS / Verify Email',
    author: 'thecodeinfluencer',
  },
  {
    path: 'notifications/github-access-token',
    name: 'GitHub / Access Token',
    author: 'bruno88cabral',
  },
  {
    path: 'receipts/apple-receipt',
    name: 'Apple / Receipt',
    author: 'relferreira',
  },
  {
    path: 'receipts/nike-receipt',
    name: 'Nike / Receipt',
    author: 'camillegachido',
  },
  {
    path: 'newsletters/stack-overflow-tips',
    name: 'Stack Overflow / Tips',
    author: 'bruno88cabral',
  },
  {
    path: 'magic-links/slack-confirm',
    name: 'Slack / Confirm Email',
    author: 'c0dr',
  },
  {
    path: 'reset-password/twitch-reset-password',
    name: 'Twitch / Reset Password',
    author: 'EmersonGarrido',
  },
  {
    path: 'magic-links/raycast-magic-link',
    name: 'Raycast / Magic Link',
    author: 'abhinandanwadwa',
  },
  {
    path: 'notifications/yelp-recent-login',
    name: 'Yelp / Recent Login',
    author: 'EmersonGarrido',
  },
  {
    path: 'magic-links/linear-login-code',
    name: 'Linear / Login Code',
    author: 'Rychillie',
  },
  {
    path: 'newsletters/google-play-policy-update',
    name: 'Google Play / Policy Update',
    author: 'EmersonGarrido',
  },
  {
    path: 'reviews/airbnb-review',
    name: 'Airbnb / Review',
    author: 'joaom00',
  },
  {
    path: 'reset-password/dropbox-reset-password',
    name: 'Dropbox / Reset Password',
    author: 'ribeiroevandro',
  },
  {
    path: 'welcome/koala-welcome',
    name: 'Koala / Welcome',
    author: 'nettofarah',
  },
  {
    path: 'notifications/vercel-invite-user',
    name: 'Vercel / Invite User',
    author: 'zenorocha',
  },
  {
    path: 'welcome/stripe-welcome',
    name: 'Stripe / Welcome',
    author: 'zenorocha',
  },
  {
    path: 'magic-links/notion-magic-link',
    name: 'Notion / Magic Link',
    author: 'bukinoshita',
  },
  {
    path: 'magic-links/plaid-verify-identity',
    name: 'Plaid / Verify Identity',
    author: 'zenorocha',
  },
];

const description = 'Open source templates built with React Email';

export const metadata: Metadata = {
  title: 'Templates — React Email',
  description,
};

export default function Templates() {
  return (
    <PageWrapper>
      <Image
        alt=""
        className="pointer-events-none absolute inset-0 z-[3] select-none mix-blend-lighten"
        fill
        priority
        src="/static/bg.png"
      />
      <PageTransition
        className="mx-auto flex max-w-3xl flex-col justify-center px-1 py-10 md:px-0"
        key="about"
        tag="main"
      >
        <div className="mb-12 text-pretty px-6 md:max-w-[46rem] md:px-0 md:text-center">
          <Heading className="text-white" weight="medium" size="6">
            Templates
          </Heading>
          <Text as="p" className="mt-4 text-slate-11" size="2">
            {description}.
          </Text>
          <Text as="p" className="mt-2 text-slate-11" size="2">
            Recreate an{' '}
            <Anchor
              href="https://github.com/resend/react-email/issues?q=is%3Aissue+is%3Aopen+label%3A%22app%3A+demo%22"
              target="_blank"
            >
              existing email
            </Anchor>{' '}
            or submit a{' '}
            <Anchor
              href="https://github.com/resend/react-email/tree/main/demo"
              target="_blank"
            >
              pull request
            </Anchor>{' '}
            to add your template here.
          </Text>
        </div>
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2">
          {items.map((item) => (
            <Template key={item.path} {...item} />
          ))}
        </div>
      </PageTransition>
    </PageWrapper>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Templates()`
- `description()`
- `items()`

### Dependencies

This file imports/requires:

- `../../components/anchor`
- `../../components/heading`
- `../../components/page-transition`
- `../../components/template`
- `../../components/text`
- `@/components/page-wrapper`
- `next`
- `next/image`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 187

- `Access`
- `Airbnb`
- `Anchor`
- `Apple`
- `Code`
- `Confirm`
- `Dropbox`
- `Email`
- `EmersonGarrido`
- `GitHub`
- `Google`
- `Heading`
- `Identity`
- `Image`
- `Invite`
- `Koala`
- `Linear`
- `Link`
- `Login`
- `Magic`
- `Metadata`
- `Nike`
- `Notion`
- `Open`
- `Overflow`
- `PageTransition`
- `PageWrapper`
- `Password`
- `Plaid`
- `Play`
- `Policy`
- `Raycast`
- `React`
- `Receipt`
- `Recent`
- `Recreate`
- `Reset`
- `Review`
- `Rychillie`
- `Slack`
- `Stack`
- `Stripe`
- `Template`
- `Templates`
- `Text`
- `Tips`
- `Token`
- `Twitch`
- `Update`
- `User`
- `Vercel`
- `Verify`
- `Welcome`
- `Yelp`
- `_blank`
- `abhinandanwadwa`
- `about`
- `absolute`
- `access`
- `add`
- `airbnb`
- `alt`
- `anchor`
- `apple`
- `author`
- `auto`
- `aws`
- `blend`
- `bruno88cabral`
- `built`
- `bukinoshita`
- `c0dr`
- `camillegachido`
- `center`
- `className`
- `code`
- `col`
- `cols`
- `com`
- `components`
- `confirm`
- `demo`
- `description`
- `div`
- `dropbox`
- `email`
- `events`
- `existing`
- `fill`
- `flex`
- `gap`
- `github`
- `google`
- `grid`
- `heading`
- `here`
- `href`
- `https`
- `identity`
- `image`
- `inset`
- `invite`
- `issues`
- `item`
- `items`
- `joaom00`
- `justify`
- `key`
- `koala`
- `label`
- `lighten`
- `linear`
- `link`
- `links`
- `login`
- `magic`
- `main`
- `map`
- `max`
- `medium`
- `metadata`
- `mix`
- `name`
- `nettofarah`
- `newsletters`
- `next`
- `nike`
- `notifications`
- `notion`
- `overflow`
- `page`
- `password`
- `path`
- `plaid`
- `play`
- `png`
- `pointer`
- `policy`
- `pretty`
- `priority`
- `pull`
- `raycast`
- `react`
- `receipt`
- `receipts`
- `recent`
- `relferreira`
- `request`
- `resend`
- `reset`
- `review`
- `reviews`
- `ribeiroevandro`
- `select`
- `size`
- `slack`
- `slate`
- `source`
- `src`
- `stack`
- `static`
- `stripe`
- `submit`
- `tag`
- `target`
- `template`
- `templates`
- `text`
- `thecodeinfluencer`
- `tips`
- `title`
- `token`
- `transition`
- `tree`
- `twitch`
- `type`
- `update`
- `user`
- `vercel`
- `verify`
- `weight`
- `welcome`
- `white`
- `wrapper`
- `yelp`
- `your`
- `zenorocha`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

