# Documentation: page.tsx
**File Path:** `apps/web/src/app/components/[slug]/page.tsx`
**Language:** tsx
**Size:** 3,481 bytes
**Lines:** 104
**Generated:** 2025-11-15T20:37:32.842167Z

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

- **Path:** `apps/web/src/app/components/[slug]/page.tsx`
- **Name:** `page.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,481 bytes (3.40 KB)
- **Lines of Code:** 104

---

## Original Source

```tsx
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Toaster } from 'sonner';
import { Heading } from '@/components/heading';
import { PageWrapper } from '@/components/page-wrapper';
import { componentsStructure } from '../../../../components/structure';
import { ComponentsView } from '../../../components/components-view';
import { IconArrowLeft } from '../../../components/icons/icon-arrow-left';
import { PageTransition } from '../../../components/page-transition';
import { slugify } from '../../../utils/slugify';
import { getImportedComponentsFor } from '../get-imported-components-for';

interface ComponentPageParams {
  params: Promise<{
    slug: string;
  }>;
}

export const dynamic = 'force-static';

export const generateStaticParams = async () => {
  return componentsStructure.map((category) => ({
    params: { slug: slugify(category.name) },
  }));
};

export const generateMetadata = async ({
  params,
}: {
  params: Promise<{ slug: string }>;
}) => {
  const { slug: rawSlug } = await params;
  const slug = decodeURIComponent(rawSlug);
  const foundCategory = componentsStructure.find(
    (category) => slugify(category.name) === slug,
  );

  if (!foundCategory) {
    notFound();
  }

  return {
    title: `${foundCategory.name} Components - React Email`,
    description: foundCategory.description,
    openGraph: {
      title: `${foundCategory.name} Components - React Email`,
      description: foundCategory.description,
      images: [
        {
          url: 'https://react.email/static/covers/patterns.png',
        },
      ],
    },
    alternates: {
      canonical: `/components/${rawSlug}`,
    },
  };
};

export default async function ComponentPage({ params }: ComponentPageParams) {
  const { slug: rawSlug } = await params;
  const slug = decodeURIComponent(rawSlug);
  const foundCategory = componentsStructure.find(
    (category) => slugify(category.name) === slug,
  );

  if (!foundCategory) {
    return <p>Component category not found.</p>;
  }

  const importedComponents = await getImportedComponentsFor(foundCategory);
  return (
    <PageWrapper>
      <div className="pointer-events-none absolute inset-0 flex justify-center">
        <div className="hidden h-full w-full max-w-7xl grid-cols-2 gap-4 px-4 lg:grid">
          <div className="border-r-slate-3 border-l border-l-slate-4" />
          <div className="border-r border-r-slate-4" />
        </div>
      </div>
      <PageTransition className="pb-10" key="about" tag="main">
        <div className="flex w-full flex-col gap-4 px-6 pt-16 pb-10 md:px-8">
          <div className="flex flex-inline">
            <Link
              className="-ml-2 flex scroll-m-2 items-center justify-center gap-2 self-start rounded-md px-2 py-1 text-slate-11 transition-colors duration-200 ease-in-out hover:text-slate-12 focus:bg-slate-6 focus:outline-none focus:ring focus:ring-slate-3"
              href="/components"
            >
              <IconArrowLeft className="mt-[.0625rem]" size={14} />
              <span>Back</span>
            </Link>
          </div>
          <Heading size="6" weight="medium" className="text-slate-12">
            {foundCategory.name}
          </Heading>
        </div>
        <div className="relative flex w-full flex-col gap-4 border-slate-4 border-y pt-3">
          <ComponentsView components={importedComponents} />
        </div>
      </PageTransition>

      <Toaster />
    </PageWrapper>
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

- `ComponentPage()`
- `dynamic()`
- `foundCategory()`
- `generateMetadata()`
- `generateStaticParams()`
- `importedComponents()`
- `slug()`

### Interfaces

- `ComponentPageParams`

### Dependencies

This file imports/requires:

- `../../../../components/structure`
- `../../../components/components-view`
- `../../../components/icons/icon-arrow-left`
- `../../../components/page-transition`
- `../../../utils/slugify`
- `../get-imported-components-for`
- `@/components/heading`
- `@/components/page-wrapper`
- `next/link`
- `next/navigation`
- `sonner`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 110

- `Back`
- `Component`
- `ComponentPage`
- `ComponentPageParams`
- `Components`
- `ComponentsView`
- `Email`
- `Heading`
- `IconArrowLeft`
- `Link`
- `PageTransition`
- `PageWrapper`
- `Promise`
- `React`
- `Toaster`
- `about`
- `absolute`
- `alternates`
- `arrow`
- `border`
- `canonical`
- `category`
- `center`
- `className`
- `col`
- `colors`
- `cols`
- `components`
- `componentsStructure`
- `covers`
- `decodeURIComponent`
- `description`
- `div`
- `duration`
- `dynamic`
- `ease`
- `email`
- `events`
- `find`
- `flex`
- `focus`
- `force`
- `found`
- `foundCategory`
- `full`
- `gap`
- `generateMetadata`
- `generateStaticParams`
- `get`
- `getImportedComponentsFor`
- `grid`
- `heading`
- `hidden`
- `hover`
- `href`
- `https`
- `icon`
- `icons`
- `images`
- `imported`
- `importedComponents`
- `inline`
- `inset`
- `interface`
- `items`
- `justify`
- `key`
- `left`
- `link`
- `main`
- `map`
- `max`
- `medium`
- `name`
- `navigation`
- `next`
- `notFound`
- `openGraph`
- `out`
- `outline`
- `page`
- `params`
- `patterns`
- `png`
- `pointer`
- `rawSlug`
- `react`
- `relative`
- `ring`
- `rounded`
- `scroll`
- `size`
- `slate`
- `slug`
- `slugify`
- `sonner`
- `span`
- `start`
- `static`
- `string`
- `structure`
- `tag`
- `text`
- `title`
- `transition`
- `url`
- `utils`
- `view`
- `weight`
- `wrapper`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

