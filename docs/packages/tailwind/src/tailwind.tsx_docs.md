# Documentation: tailwind.tsx
**File Path:** `packages/tailwind/src/tailwind.tsx`
**Language:** tsx
**Size:** 5,284 bytes
**Lines:** 171
**Generated:** 2025-11-15T20:37:32.401741Z

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

- **Path:** `packages/tailwind/src/tailwind.tsx`
- **Name:** `tailwind.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 5,284 bytes (5.16 KB)
- **Lines of Code:** 171

---

## Original Source

```tsx
import { type CssNode, generate, List, type StyleSheet } from 'css-tree';
import * as React from 'react';
import type { Config } from 'tailwindcss';
import { useSuspensedPromise } from './hooks/use-suspended-promise';
import { sanitizeStyleSheet } from './sanitize-stylesheet';
import { extractRulesPerClass } from './utils/css/extract-rules-per-class';
import { getCustomProperties } from './utils/css/get-custom-properties';
import { sanitizeNonInlinableRules } from './utils/css/sanitize-non-inlinable-rules';
import { mapReactTree } from './utils/react/map-react-tree';
import { cloneElementWithInlinedStyles } from './utils/tailwindcss/clone-element-with-inlined-styles';
import { setupTailwind } from './utils/tailwindcss/setup-tailwind';

export type TailwindConfig = Omit<Config, 'content'>;

export interface TailwindProps {
  children: React.ReactNode;
  config?: TailwindConfig;
}

export interface EmailElementProps {
  children?: React.ReactNode;
  className?: string;
  style?: React.CSSProperties;
}

export const pixelBasedPreset: TailwindConfig = {
  theme: {
    extend: {
      fontSize: {
        xs: ['12px', { lineHeight: '16px' }],
        sm: ['14px', { lineHeight: '20px' }],
        base: ['16px', { lineHeight: '24px' }],
        lg: ['18px', { lineHeight: '28px' }],
        xl: ['20px', { lineHeight: '28px' }],
        '2xl': ['24px', { lineHeight: '32px' }],
        '3xl': ['30px', { lineHeight: '36px' }],
        '4xl': ['36px', { lineHeight: '36px' }],
        '5xl': ['48px', { lineHeight: '1' }],
        '6xl': ['60px', { lineHeight: '1' }],
        '7xl': ['72px', { lineHeight: '1' }],
        '8xl': ['96px', { lineHeight: '1' }],
        '9xl': ['144px', { lineHeight: '1' }],
      },
      spacing: {
        px: '1px',
        0: '0',
        0.5: '2px',
        1: '4px',
        1.5: '6px',
        2: '8px',
        2.5: '10px',
        3: '12px',
        3.5: '14px',
        4: '16px',
        5: '20px',
        6: '24px',
        7: '28px',
        8: '32px',
        9: '36px',
        10: '40px',
        11: '44px',
        12: '48px',
        14: '56px',
        16: '64px',
        20: '80px',
        24: '96px',
        28: '112px',
        32: '128px',
        36: '144px',
        40: '160px',
        44: '176px',
        48: '192px',
        52: '208px',
        56: '224px',
        60: '240px',
        64: '256px',
        72: '288px',
        80: '320px',
        96: '384px',
      },
    },
  },
};

export function Tailwind({ children, config }: TailwindProps) {
  const tailwindSetup = useSuspensedPromise(
    () => setupTailwind(config ?? {}),
    JSON.stringify(config, (_key, value) =>
      typeof value === 'function' ? value.toString() : value,
    ),
  );
  let classesUsed: string[] = [];

  let mappedChildren: React.ReactNode = mapReactTree(children, (node) => {
    if (React.isValidElement<EmailElementProps>(node)) {
      if (node.props.className) {
        const classes = node.props.className?.split(/\s+/);
        classesUsed = [...classesUsed, ...classes];
        tailwindSetup.addUtilities(classes);
      }
    }

    return node;
  });

  const styleSheet = tailwindSetup.getStyleSheet();
  sanitizeStyleSheet(styleSheet);

  const { inlinable: inlinableRules, nonInlinable: nonInlinableRules } =
    extractRulesPerClass(styleSheet, classesUsed);

  const customProperties = getCustomProperties(styleSheet);

  const nonInlineStyles: StyleSheet = {
    type: 'StyleSheet',
    children: new List<CssNode>().fromArray(
      Array.from(nonInlinableRules.values()),
    ),
  };
  sanitizeNonInlinableRules(nonInlineStyles);

  const hasNonInlineStylesToApply = nonInlinableRules.size > 0;
  let appliedNonInlineStyles = false as boolean;

  mappedChildren = mapReactTree(mappedChildren, (node) => {
    if (React.isValidElement<EmailElementProps>(node)) {
      const elementWithInlinedStyles = cloneElementWithInlinedStyles(
        node,
        inlinableRules,
        nonInlinableRules,
        customProperties,
      );

      if (elementWithInlinedStyles.type === 'head') {
        appliedNonInlineStyles = true;

        const styleElement = <style>{generate(nonInlineStyles)}</style>;

        return React.cloneElement(
          elementWithInlinedStyles,
          elementWithInlinedStyles.props,
          styleElement,
          elementWithInlinedStyles.props.children,
        );
      }

      return elementWithInlinedStyles;
    }

    return node;
  });

  if (hasNonInlineStylesToApply && !appliedNonInlineStyles) {
    throw new Error(
      `You are trying to use the following Tailwind classes that cannot be inlined: ${Array.from(
        nonInlinableRules.keys(),
      ).join(' ')}.
For the media queries to work properly on rendering, they need to be added into a <style> tag inside of a <head> tag,
the Tailwind component tried finding a <head> element but just wasn't able to find it.

Make sure that you have a <head> element at some point inside of the <Tailwind> component at any depth. 
This can also be our <Head> component.

If you do already have a <head> element at some depth, 
please file a bug https://github.com/resend/react-email/issues/new?assignees=&labels=Type%3A+Bug&projects=&template=1.bug_report.yml.`,
    );
  }

  return mappedChildren;
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Tailwind()`
- `appliedNonInlineStyles()`
- `classes()`
- `customProperties()`
- `elementWithInlinedStyles()`
- `hasNonInlineStylesToApply()`
- `styleElement()`
- `styleSheet()`
- `tailwindSetup()`

### Interfaces

- `EmailElementProps`
- `TailwindProps`

### Type Definitions

- `CssNode`
- `StyleSheet`
- `TailwindConfig`

### Dependencies

This file imports/requires:

- `./hooks/use-suspended-promise`
- `./sanitize-stylesheet`
- `./utils/css/extract-rules-per-class`
- `./utils/css/get-custom-properties`
- `./utils/css/sanitize-non-inlinable-rules`
- `./utils/react/map-react-tree`
- `./utils/tailwindcss/clone-element-with-inlined-styles`
- `./utils/tailwindcss/setup-tailwind`
- `css-tree`
- `react`
- `tailwindcss`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 146

- `Array`
- `Bug`
- `CSSProperties`
- `Config`
- `CssNode`
- `EmailElementProps`
- `Error`
- `Head`
- `List`
- `Make`
- `Omit`
- `React`
- `ReactNode`
- `StyleSheet`
- `Tailwind`
- `TailwindConfig`
- `TailwindProps`
- `Type`
- `You`
- `_key`
- `able`
- `addUtilities`
- `added`
- `already`
- `also`
- `any`
- `appliedNonInlineStyles`
- `assignees`
- `base`
- `boolean`
- `bug`
- `bug_report`
- `cannot`
- `children`
- `className`
- `classes`
- `classesUsed`
- `clone`
- `cloneElement`
- `cloneElementWithInlinedStyles`
- `com`
- `component`
- `config`
- `content`
- `css`
- `custom`
- `customProperties`
- `depth`
- `element`
- `elementWithInlinedStyles`
- `email`
- `extend`
- `extract`
- `extractRulesPerClass`
- `file`
- `find`
- `finding`
- `following`
- `fontSize`
- `fromArray`
- `generate`
- `get`
- `getCustomProperties`
- `getStyleSheet`
- `github`
- `hasNonInlineStylesToApply`
- `head`
- `hooks`
- `https`
- `inlinable`
- `inlinableRules`
- `inlined`
- `inside`
- `interface`
- `into`
- `isValidElement`
- `issues`
- `join`
- `just`
- `keys`
- `labels`
- `lineHeight`
- `map`
- `mapReactTree`
- `mappedChildren`
- `media`
- `need`
- `node`
- `non`
- `nonInlinable`
- `nonInlinableRules`
- `nonInlineStyles`
- `our`
- `per`
- `pixelBasedPreset`
- `please`
- `point`
- `projects`
- `promise`
- `properly`
- `properties`
- `props`
- `queries`
- `react`
- `rendering`
- `resend`
- `rules`
- `sanitize`
- `sanitizeNonInlinableRules`
- `sanitizeStyleSheet`
- `setup`
- `setupTailwind`
- `size`
- `some`
- `spacing`
- `split`
- `string`
- `stringify`
- `style`
- `styleElement`
- `styleSheet`
- `styles`
- `stylesheet`
- `sure`
- `suspended`
- `tag`
- `tailwind`
- `tailwindSetup`
- `tailwindcss`
- `template`
- `theme`
- `they`
- `toString`
- `tree`
- `tried`
- `trying`
- `type`
- `use`
- `useSuspensedPromise`
- `utils`
- `value`
- `values`
- `wasn`
- `work`
- `yml`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

