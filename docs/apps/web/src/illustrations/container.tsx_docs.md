# Documentation: container.tsx
**File Path:** `apps/web/src/illustrations/container.tsx`
**Language:** tsx
**Size:** 871 bytes
**Lines:** 20
**Generated:** 2025-11-15T20:37:32.853000Z

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

- **Path:** `apps/web/src/illustrations/container.tsx`
- **Name:** `container.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 871 bytes (0.85 KB)
- **Lines of Code:** 20

---

## Original Source

```tsx
import { ChevronLeftIcon, ChevronRightIcon } from 'lucide-react';

const IllustrationContainer: React.FC = () => (
  <div className="relative flex w-[40%] items-center rounded-full bg-[#0F0F10] bg-gradient-to-b from-transparent via-black/20 to-black/20 p-3 shadow-sm transition-transform duration-150 ease-[cubic-bezier(.42,0,.58,1.8)] md:group-hover:skew-x-2">
    <ChevronLeftIcon
      className="translate-x-2 transition-transform duration-150 ease-[cubic-bezier(.42,0,.58,1.8)] group-hover:translate-x-0"
      size={14}
      strokeWidth={4}
    />
    <div className="h-1 shrink grow basis-0 rounded-sm bg-slate-8" />
    <ChevronRightIcon
      className="-translate-x-2 transition-transform duration-150 ease-[cubic-bezier(.42,0,.58,1.8)] group-hover:translate-x-0"
      size={14}
      strokeWidth={4}
    />
  </div>
);

export default IllustrationContainer;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `lucide-react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 35

- `ChevronLeftIcon`
- `ChevronRightIcon`
- `IllustrationContainer`
- `React`
- `basis`
- `bezier`
- `black`
- `center`
- `className`
- `cubic`
- `div`
- `duration`
- `ease`
- `flex`
- `full`
- `gradient`
- `group`
- `grow`
- `hover`
- `items`
- `lucide`
- `react`
- `relative`
- `rounded`
- `shadow`
- `shrink`
- `size`
- `skew`
- `slate`
- `strokeWidth`
- `transform`
- `transition`
- `translate`
- `transparent`
- `via`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

