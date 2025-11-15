# Documentation: hero.tsx
**File Path:** `apps/web/src/components/sections/hero.tsx`
**Language:** tsx
**Size:** 3,341 bytes
**Lines:** 85
**Generated:** 2025-11-15T20:37:32.930030Z

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

- **Path:** `apps/web/src/components/sections/hero.tsx`
- **Name:** `hero.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,341 bytes (3.26 KB)
- **Lines of Code:** 85

---

## Original Source

```tsx
'use client';

import { ArrowRightIcon } from 'lucide-react';
import dynamic from 'next/dynamic';
import Image from 'next/image';
import Link from 'next/link';
import { Button } from '@/components/button';
import { Code } from '@/components/code';
import { Heading } from '@/components/heading';
import { Text } from '@/components/text';

// Dynamically import Tower component to avoid SSR issues with Three.js
const Tower = dynamic(() => import('@/webgl/tower').then((mod) => mod.Tower), {
  ssr: false,
});

const HeroSection = () => {
  return (
    <>
      {/* Right Column - Tower */}
      <div className="w-[100dvw] h-[100dvh] max-lg:hidden z-[0] absolute right-0 top-0">
        <div className="w-full h-full">
          <Tower />
          <div
            className="absolute inset-0 pointer-events-none"
            style={{
              background:
                'radial-gradient(circle at center right, transparent 0%, rgba(0, 0, 0, 0.6) 40%, rgba(0, 0, 0, 0.95) 60%, #000 80%), linear-gradient(175deg, transparent 60%, black 97%), linear-gradient(to bottom, rgba(0, 0, 0, .8) 5%, transparent 30%)',
            }}
          />
        </div>
      </div>

      <section className="flex flex-col h-[calc(100dvh-11.5rem)] lg:max-w-7xl mx-auto max-lg:items-center justify-center relative w-full pt-12 lg:pt-0 pointer-events-none">
        <Image
          alt=""
          className="pointer-events-none absolute inset-0 -top-40 z-[3] scale-150 select-none mix-blend-lighten lg:opacity-30"
          fill
          priority
          src="/static/bg.png"
        />

        {/* Left Column - Content */}
        <div className="w-full lg:w-[44rem] z-10 px-4 lg:px-12 pointer-events-auto">
          <div className="mb-8 flex justify-center lg:justify-start">
            <Image
              alt="React Email Logo"
              height="100"
              src="/brand/logo.png"
              width="100"
            />
          </div>
          <Heading
            className="text-white/80 relative mb-8 text-center lg:text-left before:absolute before:top-0 before:left-0 before:w-full before:animate-[shine_1.5s_ease-in-out] before:bg-[length:225%] before:bg-shine before:bg-clip-text before:text-transparent before:content-['The_next_generation_of_writing_emails'] before:select-none before:pointer-events-none text-balance"
            weight="medium"
            size="10"
          >
            The next generation of writing emails
          </Heading>
          <div className="max-w-xl max-lg:mx-auto text-center lg:text-left">
            <Text size="5" className="text-pretty">
              React Email is a next-generation collection of unstyled components
              for creating beautiful emails using React, Tailwind, and
              TypeScript.
            </Text>
          </div>
          <div className="mt-10 flex items-center justify-center lg:justify-start gap-4 flex-wrap">
            <Button asChild size="4">
              <Link href="/components">
                Explore components
                <ArrowRightIcon size={16} />
              </Link>
            </Button>
            <Code className="lg:!inline-flex hidden max-w-max">
              npx create-email@latest
            </Code>
          </div>
        </div>
      </section>
    </>
  );
};

export default HeroSection;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `HeroSection()`
- `Tower()`

### Dependencies

This file imports/requires:

- `@/components/button`
- `@/components/code`
- `@/components/heading`
- `@/components/text`
- `lucide-react`
- `next/dynamic`
- `next/image`
- `next/link`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 121

- `ArrowRightIcon`
- `Button`
- `Code`
- `Column`
- `Content`
- `Dynamically`
- `Email`
- `Explore`
- `Heading`
- `HeroSection`
- `Image`
- `Left`
- `Link`
- `Logo`
- `React`
- `Right`
- `Tailwind`
- `Text`
- `Three`
- `Tower`
- `TypeScript`
- `absolute`
- `alt`
- `animate`
- `asChild`
- `auto`
- `avoid`
- `background`
- `balance`
- `beautiful`
- `before`
- `black`
- `blend`
- `bottom`
- `brand`
- `button`
- `calc`
- `center`
- `circle`
- `className`
- `client`
- `clip`
- `code`
- `col`
- `collection`
- `component`
- `components`
- `content`
- `create`
- `creating`
- `div`
- `dynamic`
- `email`
- `emails`
- `events`
- `fill`
- `flex`
- `full`
- `gap`
- `generation`
- `gradient`
- `heading`
- `height`
- `hidden`
- `href`
- `image`
- `inline`
- `inset`
- `issues`
- `items`
- `justify`
- `latest`
- `left`
- `length`
- `lighten`
- `linear`
- `link`
- `logo`
- `lucide`
- `max`
- `medium`
- `mix`
- `mod`
- `next`
- `npx`
- `opacity`
- `out`
- `png`
- `pointer`
- `pretty`
- `priority`
- `radial`
- `react`
- `relative`
- `rgba`
- `right`
- `scale`
- `section`
- `select`
- `shine`
- `shine_1`
- `size`
- `src`
- `ssr`
- `start`
- `static`
- `style`
- `text`
- `then`
- `top`
- `tower`
- `transparent`
- `unstyled`
- `use`
- `using`
- `webgl`
- `weight`
- `white`
- `width`
- `wrap`
- `writing`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

