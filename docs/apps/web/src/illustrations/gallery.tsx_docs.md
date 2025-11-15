# Documentation: gallery.tsx
**File Path:** `apps/web/src/illustrations/gallery.tsx`
**Language:** tsx
**Size:** 1,948 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:32.860703Z

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

- **Path:** `apps/web/src/illustrations/gallery.tsx`
- **Name:** `gallery.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,948 bytes (1.90 KB)
- **Lines of Code:** 33

---

## Original Source

```tsx
import { ImageIcon } from 'lucide-react';

const IllustrationGallery: React.FC = () => (
  <div className="relative flex h-full w-full items-stretch gap-2 overflow-visible">
    <div className="flex h-max shrink grow basis-0 flex-col items-end gap-2 overflow-visible pb-2">
      <div className="aspect-square w-[30%] rounded-sm bg-[#0F0F10] bg-gradient-to-b from-transparent via-black/20 to-black/20 p-2 shadow-sm">
        <div className="h-full w-full rounded-sm bg-slate-3" />
      </div>
      <div className="aspect-square w-[30%] rounded-sm bg-[#0F0F10] bg-gradient-to-b from-transparent via-black/20 to-black/20 p-2 shadow-sm">
        <div className="flex h-full w-full items-center justify-center rounded-sm bg-slate-3 transition-colors md:group-hover:bg-slate-4">
          <ImageIcon className="opacity-5 transition-opacity md:group-hover:opacity-20" />
        </div>
      </div>
      <div className="aspect-square w-[30%] rounded-sm bg-[#0F0F10] bg-gradient-to-b from-transparent via-black/20 to-black/20 p-2 shadow-sm">
        <div className="h-full w-full rounded-sm bg-slate-3" />
      </div>
    </div>
    <div className="flex h-max shrink grow basis-0 flex-col items-start gap-2 overflow-visible pt-2">
      <div className="aspect-square w-[30%] rounded-sm bg-[#0F0F10] bg-gradient-to-b from-transparent via-black/20 to-black/20 p-2 shadow-sm">
        <div className="h-full w-full rounded-sm bg-slate-3" />
      </div>
      <div className="aspect-square w-[30%] rounded-sm bg-[#0F0F10] bg-gradient-to-b from-transparent via-black/20 to-black/20 p-2 shadow-sm">
        <div className="h-full w-full rounded-sm bg-slate-3" />
      </div>
      <div className="aspect-square w-[30%] rounded-sm bg-[#0F0F10] bg-gradient-to-b from-transparent via-black/20 to-black/20 p-2 shadow-sm">
        <div className="h-full w-full rounded-sm bg-slate-3" />
      </div>
    </div>
  </div>
);

export default IllustrationGallery;

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

**Total Unique Identifiers:** 38

- `IllustrationGallery`
- `ImageIcon`
- `React`
- `aspect`
- `basis`
- `black`
- `center`
- `className`
- `col`
- `colors`
- `div`
- `end`
- `flex`
- `full`
- `gap`
- `gradient`
- `group`
- `grow`
- `hover`
- `items`
- `justify`
- `lucide`
- `max`
- `opacity`
- `overflow`
- `react`
- `relative`
- `rounded`
- `shadow`
- `shrink`
- `slate`
- `square`
- `start`
- `stretch`
- `transition`
- `transparent`
- `via`
- `visible`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

