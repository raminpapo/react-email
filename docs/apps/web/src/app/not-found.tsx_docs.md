# Documentation: not-found.tsx
**File Path:** `apps/web/src/app/not-found.tsx`
**Language:** tsx
**Size:** 1,167 bytes
**Lines:** 37
**Generated:** 2025-11-15T20:37:32.821233Z

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

- **Path:** `apps/web/src/app/not-found.tsx`
- **Name:** `not-found.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,167 bytes (1.14 KB)
- **Lines of Code:** 37

---

## Original Source

```tsx
import { PageTransition } from '@/components/page-transition';
import { PageWrapper } from '@/components/page-wrapper';

export const metadata = {
  title: '404 Not found',
  alternates: {
    canonical: '/not-found',
  },
};

export default function NotFound() {
  return (
    <PageWrapper>
      <div className="pointer-events-none absolute inset-0 flex justify-center">
        <div className="hidden h-full w-full max-w-7xl grid-cols-2 gap-4 px-4 lg:grid">
          <div className="border-r-slate-3 border-l border-l-slate-4" />
          <div className="border-r border-r-slate-4" />
        </div>
      </div>
      <PageTransition
        className="flex w-full flex-col items-center justify-center gap-2 px-8 pt-16 pb-10 text-center"
        key="not-found"
        tag="main"
      >
        <h1 className="font-bold text-2xl text-slate-12 uppercase italic">
          <span className="font-mono">404</span> <br />
          Not Found
        </h1>
        <div className="mt-1 leading-loose">
          <p>This page does not exist.</p>
          <p>Please check the URL and try again.</p>
        </div>
      </PageTransition>
    </PageWrapper>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `NotFound()`
- `metadata()`

### Dependencies

This file imports/requires:

- `@/components/page-transition`
- `@/components/page-wrapper`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 48

- `Found`
- `NotFound`
- `PageTransition`
- `PageWrapper`
- `Please`
- `absolute`
- `again`
- `alternates`
- `bold`
- `border`
- `canonical`
- `center`
- `check`
- `className`
- `col`
- `cols`
- `components`
- `div`
- `events`
- `exist`
- `flex`
- `font`
- `found`
- `full`
- `gap`
- `grid`
- `hidden`
- `inset`
- `italic`
- `items`
- `justify`
- `key`
- `leading`
- `loose`
- `main`
- `max`
- `metadata`
- `mono`
- `page`
- `pointer`
- `slate`
- `span`
- `tag`
- `text`
- `title`
- `transition`
- `uppercase`
- `wrapper`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

