# Documentation: feedback.tsx
**File Path:** `apps/web/src/illustrations/feedback.tsx`
**Language:** tsx
**Size:** 1,213 bytes
**Lines:** 24
**Generated:** 2025-11-15T20:37:32.857981Z

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

- **Path:** `apps/web/src/illustrations/feedback.tsx`
- **Name:** `feedback.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,213 bytes (1.18 KB)
- **Lines of Code:** 24

---

## Original Source

```tsx
import { MousePointer2Icon } from 'lucide-react';

const IllustrationFeedback: React.FC = () => (
  <div className="relative flex w-[40%] translate-y-3 flex-col gap-4 rounded-md bg-[#0F0F10] bg-gradient-to-b from-transparent via-black/20 to-black/20 p-4 shadow-sm transition-transform duration-150 ease-[cubic-bezier(.42,0,.58,1.8)] md:group-hover:skew-x-2">
    <div className="flex flex-col gap-1">
      <div className="h-2 w-[90%] rounded-sm bg-slate-5" />
      <div className="h-2 w-[66%] rounded-sm bg-slate-5" />
    </div>
    <div className="flex items-center gap-2">
      <div className="h-2 shrink-0 grow basis-0 rounded-sm bg-[#25AEBA]" />
      <div className="h-2 shrink-0 grow basis-0 rounded-sm bg-[#25AEBA]" />
      <div className="h-2 shrink-0 grow basis-0 rounded-sm bg-[#25AEBA]" />
      <div className="h-2 shrink-0 grow basis-0 rounded-sm bg-[#25AEBA]" />
    </div>
    <MousePointer2Icon
      className="-bottom-4 group-hover:-translate-y-3 absolute right-[40%] rotate-[60deg] transition-transform duration-150 ease-[cubic-bezier(.42,0,.58,1.8)] group-hover:translate-x-3"
      fill="currentColor"
      stroke="currentColor"
    />
  </div>
);

export default IllustrationFeedback;

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

**Total Unique Identifiers:** 40

- `IllustrationFeedback`
- `MousePointer2Icon`
- `React`
- `absolute`
- `basis`
- `bezier`
- `black`
- `bottom`
- `center`
- `className`
- `col`
- `cubic`
- `currentColor`
- `div`
- `duration`
- `ease`
- `fill`
- `flex`
- `gap`
- `gradient`
- `group`
- `grow`
- `hover`
- `items`
- `lucide`
- `react`
- `relative`
- `right`
- `rotate`
- `rounded`
- `shadow`
- `shrink`
- `skew`
- `slate`
- `stroke`
- `transform`
- `transition`
- `translate`
- `transparent`
- `via`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

