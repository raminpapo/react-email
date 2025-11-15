# Documentation: use-scroll.tsx
**File Path:** `apps/web/src/utils/use-scroll.tsx`
**Language:** tsx
**Size:** 768 bytes
**Lines:** 32
**Generated:** 2025-11-15T20:37:32.810234Z

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

- **Path:** `apps/web/src/utils/use-scroll.tsx`
- **Name:** `use-scroll.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 768 bytes (0.75 KB)
- **Lines of Code:** 32

---

## Original Source

```tsx
import React from 'react';

export const useScroll = () => {
  const [isScrolling, setIsScrolling] = React.useState(false);

  React.useEffect(() => {
    let scrollTimeout: NodeJS.Timeout;

    const handleScroll = () => {
      document.body.classList.add('scrolling');
      setIsScrolling(true);

      clearTimeout(scrollTimeout);

      scrollTimeout = setTimeout(() => {
        document.body.classList.remove('scrolling');
        setIsScrolling(false);
      }, 150);
    };

    window.addEventListener('scroll', handleScroll, { passive: true });

    return () => {
      window.removeEventListener('scroll', handleScroll);
      clearTimeout(scrollTimeout);
      document.body.classList.remove('scrolling');
    };
  }, []);

  return { isScrolling };
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `handleScroll()`
- `useScroll()`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 24

- `NodeJS`
- `React`
- `Timeout`
- `add`
- `addEventListener`
- `body`
- `classList`
- `clearTimeout`
- `document`
- `handleScroll`
- `isScrolling`
- `passive`
- `react`
- `remove`
- `removeEventListener`
- `scroll`
- `scrollTimeout`
- `scrolling`
- `setIsScrolling`
- `setTimeout`
- `useEffect`
- `useScroll`
- `useState`
- `window`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

