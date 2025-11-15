# Documentation: grid.tsx
**File Path:** `apps/web/src/illustrations/grid.tsx`
**Language:** tsx
**Size:** 1,181 bytes
**Lines:** 19
**Generated:** 2025-11-15T20:37:32.862045Z

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

- **Path:** `apps/web/src/illustrations/grid.tsx`
- **Name:** `grid.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,181 bytes (1.15 KB)
- **Lines of Code:** 19

---

## Original Source

```tsx
import { MoveDownRightIcon } from 'lucide-react';

const IllustrationGrid: React.FC = () => (
  <div className="relative grid aspect-square w-[24%] grid-cols-2 grid-rows-2 items-center gap-2 rounded-md bg-[#0F0F10] bg-gradient-to-b from-transparent via-black/20 to-black/20 p-2 shadow-sm transition-transform duration-150 ease-[cubic-bezier(.42,0,.58,1.8)] md:group-hover:skew-x-2">
    <div className="col-span-1 h-full rounded-sm bg-slate-3" />
    <div className="col-span-1 h-full rounded-sm bg-gradient-to-l bg-slate-3 from-slate-1 to-slate-3" />
    <div className="col-span-1 h-full rounded-sm bg-gradient-to-b bg-slate-3 from-slate-3 to-slate-1" />
    <div className="relative col-span-1 h-full rounded-sm border-[#2EBDC9] border-[.1875rem] bg-slate-4 text-[#25AEBA] shadow-[0px_0px_9px_4px_rgba(37,174,186,0.10)] transition-transform duration-150 ease-[cubic-bezier(.42,0,.58,1.8)] group-hover:translate-x-1 group-hover:translate-y-1 group-hover:scale-125">
      <MoveDownRightIcon
        className="absolute top-[calc(100%-.125rem)] left-[calc(100%-.125rem)]"
        size={14}
        strokeWidth={4}
      />
    </div>
  </div>
);

export default IllustrationGrid;

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

**Total Unique Identifiers:** 45

- `IllustrationGrid`
- `MoveDownRightIcon`
- `React`
- `absolute`
- `aspect`
- `bezier`
- `black`
- `border`
- `calc`
- `center`
- `className`
- `col`
- `cols`
- `cubic`
- `div`
- `duration`
- `ease`
- `full`
- `gap`
- `gradient`
- `grid`
- `group`
- `hover`
- `items`
- `left`
- `lucide`
- `react`
- `relative`
- `rounded`
- `rows`
- `scale`
- `shadow`
- `size`
- `skew`
- `slate`
- `span`
- `square`
- `strokeWidth`
- `text`
- `top`
- `transform`
- `transition`
- `translate`
- `transparent`
- `via`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

