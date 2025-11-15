# Documentation: setup-tailwind.ts
**File Path:** `packages/tailwind/src/utils/tailwindcss/setup-tailwind.ts`
**Language:** typescript
**Size:** 2,075 bytes
**Lines:** 83
**Generated:** 2025-11-15T20:37:32.427083Z

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

- **Path:** `packages/tailwind/src/utils/tailwindcss/setup-tailwind.ts`
- **Name:** `setup-tailwind.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,075 bytes (2.03 KB)
- **Lines of Code:** 83

---

## Original Source

```typescript
import { parse, type StyleSheet } from 'css-tree';
import { compile } from 'tailwindcss';
import type { TailwindConfig } from '../../tailwind';
import indexCss from './tailwind-stylesheets/index';
import preflightCss from './tailwind-stylesheets/preflight';
import themeCss from './tailwind-stylesheets/theme';
import utilitiesCss from './tailwind-stylesheets/utilities';

export type TailwindSetup = Awaited<ReturnType<typeof setupTailwind>>;

export async function setupTailwind(config: TailwindConfig) {
  const baseCss = `
@layer theme, base, components, utilities;
@import "tailwindcss/theme.css" layer(theme);
@import "tailwindcss/utilities.css" layer(utilities);
@config;
`;
  const compiler = await compile(baseCss, {
    async loadModule(id, base, resourceHint) {
      if (resourceHint === 'config') {
        return {
          path: id,
          base: base,
          module: config,
        };
      }

      throw new Error(
        `NO-OP: should we implement support for ${resourceHint}?`,
      );
    },
    polyfills: 0, // All
    async loadStylesheet(id, base) {
      if (id === 'tailwindcss') {
        return {
          base,
          path: 'tailwindcss/index.css',
          content: indexCss,
        };
      }

      if (id === 'tailwindcss/preflight.css') {
        return {
          base,
          path: id,
          content: preflightCss,
        };
      }

      if (id === 'tailwindcss/theme.css') {
        return {
          base,
          path: id,
          content: themeCss,
        };
      }

      if (id === 'tailwindcss/utilities.css') {
        return {
          base,
          path: id,
          content: utilitiesCss,
        };
      }

      throw new Error(
        'stylesheet not supported, you can only import the ones from tailwindcss',
      );
    },
  });

  let css: string = baseCss;

  return {
    addUtilities: function addUtilities(candidates: string[]): void {
      css = compiler.build(candidates);
    },
    getStyleSheet: function getCss() {
      return parse(css) as StyleSheet;
    },
  };
}

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `addUtilities()`
- `baseCss()`
- `compiler()`
- `getCss()`
- `setupTailwind()`

### Type Definitions

- `StyleSheet`
- `TailwindSetup`

### Dependencies

This file imports/requires:

- `../../tailwind`
- `./tailwind-stylesheets/index`
- `./tailwind-stylesheets/preflight`
- `./tailwind-stylesheets/theme`
- `./tailwind-stylesheets/utilities`
- `css-tree`
- `tailwindcss`
- `tailwindcss/theme.css`
- `tailwindcss/utilities.css`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 51

- `All`
- `Awaited`
- `Error`
- `ReturnType`
- `StyleSheet`
- `TailwindConfig`
- `TailwindSetup`
- `addUtilities`
- `base`
- `baseCss`
- `build`
- `candidates`
- `compile`
- `compiler`
- `components`
- `config`
- `content`
- `css`
- `getCss`
- `getStyleSheet`
- `implement`
- `index`
- `indexCss`
- `layer`
- `loadModule`
- `loadStylesheet`
- `module`
- `ones`
- `only`
- `parse`
- `path`
- `polyfills`
- `preflight`
- `preflightCss`
- `resourceHint`
- `setupTailwind`
- `string`
- `stylesheet`
- `stylesheets`
- `support`
- `supported`
- `tailwind`
- `tailwindcss`
- `theme`
- `themeCss`
- `tree`
- `type`
- `utilities`
- `utilitiesCss`
- `void`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

