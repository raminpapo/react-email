# Documentation: footer.tsx
**File Path:** `apps/web/src/components/footer.tsx`
**Language:** tsx
**Size:** 769 bytes
**Lines:** 29
**Generated:** 2025-11-15T20:37:32.899191Z

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

- **Path:** `apps/web/src/components/footer.tsx`
- **Name:** `footer.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 769 bytes (0.75 KB)
- **Lines of Code:** 29

---

## Original Source

```tsx
import Image from 'next/image';
import { Anchor } from './anchor';
import { Text } from './text';

export function Footer() {
  return (
    <footer className="flex min-h-20 items-center justify-center text-center">
      <Text className="inline-flex items-center gap-2">
        Brought to you by{' '}
        <Anchor
          className="inline-flex items-center gap-2"
          href="https://go.resend.com/react-email"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            alt=""
            className="inline-block rounded-full border border-slate-7"
            height="20"
            src="/brand/resend.png"
            width="20"
          />
          Resend
        </Anchor>
      </Text>
    </footer>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Footer()`

### Dependencies

This file imports/requires:

- `./anchor`
- `./text`
- `next/image`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 42

- `Anchor`
- `Brought`
- `Footer`
- `Image`
- `Resend`
- `Text`
- `_blank`
- `alt`
- `anchor`
- `block`
- `border`
- `brand`
- `center`
- `className`
- `com`
- `email`
- `flex`
- `footer`
- `full`
- `gap`
- `height`
- `href`
- `https`
- `image`
- `inline`
- `items`
- `justify`
- `min`
- `next`
- `noopener`
- `noreferrer`
- `png`
- `react`
- `rel`
- `resend`
- `rounded`
- `slate`
- `src`
- `target`
- `text`
- `width`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

