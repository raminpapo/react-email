# Documentation: page-wrapper.tsx
**File Path:** `apps/web/src/components/page-wrapper.tsx`
**Language:** tsx
**Size:** 511 bytes
**Lines:** 22
**Generated:** 2025-11-15T20:37:32.909835Z

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

- **Path:** `apps/web/src/components/page-wrapper.tsx`
- **Name:** `page-wrapper.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 511 bytes (0.50 KB)
- **Lines of Code:** 22

---

## Original Source

```tsx
import { Footer } from '@/components/footer';

interface PageWrapperProps {
  children: React.ReactNode;
  className?: string;
}

/**
 * Reusable page wrapper with Topbar and Footer for internal pages
 */
export function PageWrapper({ children, className = '' }: PageWrapperProps) {
  return (
    <div
      className={`relative mx-auto flex min-h-[100dvh] flex-col justify-between px-2 md:max-w-7xl md:px-4 ${className}`}
      vaul-drawer-wrapper=""
    >
      {children}
      <Footer />
    </div>
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

- `PageWrapper()`

### Interfaces

- `PageWrapperProps`

### Dependencies

This file imports/requires:

- `@/components/footer`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 28

- `Footer`
- `PageWrapper`
- `PageWrapperProps`
- `React`
- `ReactNode`
- `Reusable`
- `Topbar`
- `auto`
- `between`
- `children`
- `className`
- `col`
- `components`
- `div`
- `drawer`
- `flex`
- `footer`
- `interface`
- `internal`
- `justify`
- `max`
- `min`
- `page`
- `pages`
- `relative`
- `string`
- `vaul`
- `wrapper`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

