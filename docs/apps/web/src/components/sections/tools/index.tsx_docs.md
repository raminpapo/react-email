# Documentation: index.tsx
**File Path:** `apps/web/src/components/sections/tools/index.tsx`
**Language:** tsx
**Size:** 1,148 bytes
**Lines:** 36
**Generated:** 2025-11-15T20:37:32.942289Z

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

- **Path:** `apps/web/src/components/sections/tools/index.tsx`
- **Name:** `index.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,148 bytes (1.12 KB)
- **Lines of Code:** 36

---

## Original Source

```tsx
import Image from 'next/image';

import { Heading } from '@/components/heading';
import { Text } from '@/components/text';
import { InteractiveDemo } from './interactive-demo';

const ToolsSection = () => {
  return (
    <section className="relative text-center space-y-16 sm:space-y-24 max-md:mt-44 max-md:mb-24 my-56 max-md:px-4">
      <div className="space-y-8">
        <div className="max-w-full text-center space-y-6">
          <Heading size="8" weight="medium" className="text-white/80">
            Built-in deliverability tools
          </Heading>
          <div className="sm:px-20 md:max-w-2xl md:mx-auto">
            <Text size="5" className="opacity-70">
              Before you hit “send”, check how your email is doing with a set of
              tools to help you build better emails.
            </Text>
          </div>
        </div>
      </div>
      <InteractiveDemo />
      <Image
        alt=""
        className="pointer-events-none absolute inset-0 -top-40 z-[3] select-none mix-blend-lighten"
        fill
        priority
        src="/static/bg.png"
      />
    </section>
  );
};

export default ToolsSection;

```

---

## Overview

This is a JavaScript/TypeScript file. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `ToolsSection()`

### Dependencies

This file imports/requires:

- `./interactive-demo`
- `@/components/heading`
- `@/components/text`
- `next/image`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 58

- `Before`
- `Built`
- `Heading`
- `Image`
- `InteractiveDemo`
- `Text`
- `ToolsSection`
- `absolute`
- `alt`
- `auto`
- `better`
- `blend`
- `build`
- `center`
- `check`
- `className`
- `components`
- `deliverability`
- `demo`
- `div`
- `doing`
- `email`
- `emails`
- `events`
- `fill`
- `full`
- `heading`
- `help`
- `hit`
- `how`
- `image`
- `inset`
- `interactive`
- `lighten`
- `max`
- `medium`
- `mix`
- `next`
- `opacity`
- `png`
- `pointer`
- `priority`
- `relative`
- `section`
- `select`
- `send`
- `set`
- `size`
- `space`
- `src`
- `static`
- `text`
- `tools`
- `top`
- `weight`
- `white`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

