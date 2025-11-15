# Documentation: ensure-matching-variants.spec.tsx
**File Path:** `apps/web/components/ensure-matching-variants.spec.tsx`
**Language:** tsx
**Size:** 3,266 bytes
**Lines:** 97
**Generated:** 2025-11-15T20:37:32.961033Z

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

- **Path:** `apps/web/components/ensure-matching-variants.spec.tsx`
- **Name:** `ensure-matching-variants.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,266 bytes (3.19 KB)
- **Lines of Code:** 97

---

## Original Source

```tsx
import { existsSync } from 'node:fs';
import path from 'node:path';
import { pretty, render } from '@react-email/components';
import { parse, stringify } from 'html-to-ast';
import type { Attr, IDoc as Doc } from 'html-to-ast/dist/types';
import postcss from 'postcss';
import { getComponentElement } from '../src/app/components/get-imported-components-for';
import { Layout } from './_components/layout';
import { componentsStructure, getComponentPathFromSlug } from './structure';

type MaybeDoc = ReturnType<typeof parse>[number];

const walkAst = <T extends MaybeDoc>(ast: T[], callback: (doc: T) => void) => {
  for (const doc of ast) {
    callback(doc);
    if (doc.children) {
      walkAst(doc.children as T[], callback);
    }
  }
};

const getStyleObjectFromString = (style: string): Record<string, string> => {
  const obj: Record<string, string> = {};
  const root = postcss.parse(style);
  root.walkDecls((decl) => {
    obj[decl.prop] = decl.value;
  });
  return obj;
};

const sortStyle = (style: string): string => {
  const object = getStyleObjectFromString(style);
  const styleProperties = Object.keys(object).sort();
  return styleProperties.map((prop) => `${prop}:${object[prop]}`).join(';');
};

const getComparableHtml = (html: string): string => {
  const ast = parse(html);
  walkAst(ast, (doc) => {
    const orderedAttributes: Attr = {};
    if (doc.attrs) {
      for (const key of Object.keys(doc.attrs).sort()) {
        orderedAttributes[key] = doc.attrs[key];
      }
      doc.attrs = orderedAttributes;
      if ('style' in doc.attrs) {
        const style = doc.attrs.style as string;
        doc.attrs.style = sortStyle(style);
      }
    }
  });
  return stringify(ast as Doc[]);
};

describe.skip('copy-paste components', () => {
  const components = componentsStructure.flatMap(
    (category) => category.components,
  );
  for (const component of components) {
    // It currently fails due to a Tailwind limitation
    if (component.slug === 'single-button') continue;

    // Tailwind seems to be leaving an empty space as a className
    if (component.slug === 'simple-code-inline') continue;
    if (component.slug === 'code-inline-with-different-colors') continue;

    test(`${component.slug}'s variants should all match`, async () => {
      const componentPath = getComponentPathFromSlug(component.slug);
      const tailwindVariantPath = path.join(componentPath, 'tailwind.tsx');
      const inlineStylesVariantPath = path.join(
        componentPath,
        'inline-styles.tsx',
      );
      if (
        existsSync(tailwindVariantPath) &&
        existsSync(inlineStylesVariantPath)
      ) {
        const tailwindElement = await getComponentElement(tailwindVariantPath);
        const inlineStylesElement = await getComponentElement(
          inlineStylesVariantPath,
        );
        const tailwindHtml = getComparableHtml(
          await pretty(await render(<Layout>{tailwindElement}</Layout>)),
        );
        const inlineStylesHtml = getComparableHtml(
          await pretty(
            await render(
              <Layout withTailwind={false}>{inlineStylesElement}</Layout>,
            ),
          ),
        );
        expect(tailwindHtml).toBe(inlineStylesHtml);
      }
    });
  }
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `ast()`
- `componentPath()`
- `components()`
- `getComparableHtml()`
- `getStyleObjectFromString()`
- `inlineStylesElement()`
- `inlineStylesHtml()`
- `inlineStylesVariantPath()`
- `object()`
- `root()`
- `sortStyle()`
- `style()`
- `styleProperties()`
- `tailwindElement()`
- `tailwindHtml()`
- `tailwindVariantPath()`
- `walkAst()`

### Type Definitions

- `MaybeDoc`

### Dependencies

This file imports/requires:

- `../src/app/components/get-imported-components-for`
- `./_components/layout`
- `./structure`
- `@react-email/components`
- `html-to-ast`
- `html-to-ast/dist/types`
- `node:fs`
- `node:path`
- `postcss`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 103

- `Attr`
- `Doc`
- `IDoc`
- `Layout`
- `MaybeDoc`
- `Object`
- `Record`
- `ReturnType`
- `Tailwind`
- `_components`
- `all`
- `app`
- `ast`
- `attrs`
- `button`
- `callback`
- `category`
- `children`
- `className`
- `code`
- `colors`
- `component`
- `componentPath`
- `components`
- `componentsStructure`
- `copy`
- `currently`
- `decl`
- `describe`
- `different`
- `dist`
- `doc`
- `due`
- `email`
- `empty`
- `existsSync`
- `expect`
- `extends`
- `fails`
- `flatMap`
- `get`
- `getComparableHtml`
- `getComponentElement`
- `getComponentPathFromSlug`
- `getStyleObjectFromString`
- `html`
- `imported`
- `inline`
- `inlineStylesElement`
- `inlineStylesHtml`
- `inlineStylesVariantPath`
- `join`
- `key`
- `keys`
- `layout`
- `leaving`
- `limitation`
- `map`
- `match`
- `node`
- `number`
- `obj`
- `object`
- `orderedAttributes`
- `parse`
- `paste`
- `path`
- `postcss`
- `pretty`
- `prop`
- `react`
- `render`
- `root`
- `seems`
- `simple`
- `single`
- `skip`
- `slug`
- `sort`
- `sortStyle`
- `space`
- `src`
- `string`
- `stringify`
- `structure`
- `style`
- `styleProperties`
- `styles`
- `tailwind`
- `tailwindElement`
- `tailwindHtml`
- `tailwindVariantPath`
- `test`
- `toBe`
- `tsx`
- `type`
- `types`
- `value`
- `variants`
- `void`
- `walkAst`
- `walkDecls`
- `withTailwind`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

