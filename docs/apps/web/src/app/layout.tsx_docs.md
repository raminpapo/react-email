# Documentation: layout.tsx
**File Path:** `apps/web/src/app/layout.tsx`
**Language:** tsx
**Size:** 2,580 bytes
**Lines:** 111
**Generated:** 2025-11-15T20:37:32.819456Z

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

- **Path:** `apps/web/src/app/layout.tsx`
- **Name:** `layout.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,580 bytes (2.52 KB)
- **Lines of Code:** 111

---

## Original Source

```tsx
import { Analytics } from '@vercel/analytics/react';
import type { Metadata } from 'next';
import '@/styles/globals.css';
import localFont from 'next/font/local';
import { Topbar } from '@/components/topbar';

const inter = localFont({
  display: 'swap',
  preload: true,
  src: '../../public/fonts/inter/inter.ttf',
  variable: '--font-inter',
  weight: '400 700',
});

const commitMono = localFont({
  display: 'swap',
  preload: true,
  src: [
    {
      path: '../../public/fonts/commit-mono/commit-mono-regular.ttf',
      style: 'normal',
      weight: '400',
    },
    {
      path: '../../public/fonts/commit-mono/commit-mono-italic.ttf',
      style: 'italic',
      weight: '400',
    },
  ],
  variable: '--font-commit-mono',
});

export const metadata: Metadata = {
  metadataBase: new URL('https://react.email'),
  title: {
    default: 'React Email',
    template: '%s • React Email',
  },
  description:
    'A collection of high-quality, unstyled components for creating beautiful emails using React and TypeScript.',
  authors: {
    name: 'Resend Team',
  },
  icons: {
    apple: '/meta/apple-touch-icon.png',
    icon: [
      {
        sizes: 'any',
        url: '/meta/favicon.ico',
      },
      {
        type: 'image/svg+xml',
        url: '/meta/favicon.svg',
      },
    ],
  },
  openGraph: {
    description:
      'A collection of high-quality, unstyled components for creating beautiful emails using React and TypeScript.',
    images: [
      {
        url: '/meta/cover.png',
      },
    ],
    locale: 'en_US',
    siteName: 'React Email',
    title: 'React Email',
    type: 'website',
    url: 'https://react.email',
  },
  twitter: {
    card: 'summary_large_image',
    images: 'https://react.email/static/cover.png',
  },
  alternates: {
    canonical: '/',
  },
};

export const viewport = {
  themeColor: '#25AEBA',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      className={`${inter.variable} ${commitMono.variable} antialiased`}
      lang="en"
      color-scheme="dark"
    >
      <head>
        <script src="/js/web-streams-polyfill.js" />
      </head>
      <body
        suppressHydrationWarning={true}
        className="h-screen-ios overflow-x-hidden bg-black font-sans text-slate-11 text-sm selection:bg-cyan-5 selection:text-cyan-12"
      >
        <div className="relative mx-auto flex flex-col justify-between px-2 md:max-w-7xl md:px-4">
          <Topbar />
        </div>
        {children}
        <Analytics />
      </body>
    </html>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `RootLayout()`
- `commitMono()`
- `inter()`
- `viewport()`

### Dependencies

This file imports/requires:

- `@/components/topbar`
- `@/styles/globals.css`
- `@vercel/analytics/react`
- `next`
- `next/font/local`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 119

- `Analytics`
- `Email`
- `Metadata`
- `React`
- `ReactNode`
- `Resend`
- `RootLayout`
- `Team`
- `Topbar`
- `TypeScript`
- `alternates`
- `analytics`
- `antialiased`
- `any`
- `apple`
- `authors`
- `auto`
- `beautiful`
- `between`
- `black`
- `body`
- `canonical`
- `card`
- `children`
- `className`
- `col`
- `collection`
- `color`
- `commit`
- `commitMono`
- `components`
- `cover`
- `creating`
- `css`
- `cyan`
- `dark`
- `description`
- `display`
- `div`
- `email`
- `emails`
- `favicon`
- `flex`
- `font`
- `fonts`
- `globals`
- `head`
- `hidden`
- `high`
- `html`
- `https`
- `ico`
- `icon`
- `icons`
- `image`
- `images`
- `inter`
- `ios`
- `italic`
- `justify`
- `lang`
- `local`
- `localFont`
- `locale`
- `max`
- `meta`
- `metadata`
- `metadataBase`
- `mono`
- `name`
- `next`
- `normal`
- `openGraph`
- `overflow`
- `path`
- `png`
- `polyfill`
- `preload`
- `public`
- `quality`
- `react`
- `regular`
- `relative`
- `sans`
- `scheme`
- `screen`
- `script`
- `selection`
- `siteName`
- `sizes`
- `slate`
- `src`
- `static`
- `streams`
- `style`
- `styles`
- `summary_large_image`
- `suppressHydrationWarning`
- `svg`
- `swap`
- `template`
- `text`
- `themeColor`
- `title`
- `topbar`
- `touch`
- `ttf`
- `twitter`
- `type`
- `unstyled`
- `url`
- `using`
- `variable`
- `vercel`
- `viewport`
- `web`
- `website`
- `weight`
- `xml`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

