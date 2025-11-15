# Documentation: page.tsx
**File Path:** `apps/web/src/app/page.tsx`
**Language:** tsx
**Size:** 886 bytes
**Lines:** 26
**Generated:** 2025-11-15T20:37:32.822586Z

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

- **Path:** `apps/web/src/app/page.tsx`
- **Name:** `page.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 886 bytes (0.87 KB)
- **Lines of Code:** 26

---

## Original Source

```tsx
import { Footer } from '@/components/footer';
import HeroSection from '@/components/sections/hero';
import IntegrationSection from '@/components/sections/integration';
import PatternsSection from '@/components/sections/patterns';
import PlaygroundSection from '@/components/sections/playground';
import PrimitivesSection from '@/components/sections/primitives';
import TestimonialSection from '@/components/sections/testimonial';
import ToolsSection from '@/components/sections/tools';

const Home = () => (
  <main className="overflow-x-clip">
    <HeroSection />
    <div className="relative mx-auto flex flex-col justify-between px-2 md:max-w-7xl md:px-4">
      <PlaygroundSection />
      <TestimonialSection />
      <PatternsSection />
      <PrimitivesSection />
      <ToolsSection />
      <IntegrationSection />
      <Footer />
    </div>
  </main>
);

export default Home;

```

---

## Overview

This is a JavaScript/TypeScript file. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Home()`

### Dependencies

This file imports/requires:

- `@/components/footer`
- `@/components/sections/hero`
- `@/components/sections/integration`
- `@/components/sections/patterns`
- `@/components/sections/playground`
- `@/components/sections/primitives`
- `@/components/sections/testimonial`
- `@/components/sections/tools`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 31

- `Footer`
- `HeroSection`
- `Home`
- `IntegrationSection`
- `PatternsSection`
- `PlaygroundSection`
- `PrimitivesSection`
- `TestimonialSection`
- `ToolsSection`
- `auto`
- `between`
- `className`
- `clip`
- `col`
- `components`
- `div`
- `flex`
- `footer`
- `hero`
- `integration`
- `justify`
- `main`
- `max`
- `overflow`
- `patterns`
- `playground`
- `primitives`
- `relative`
- `sections`
- `testimonial`
- `tools`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

