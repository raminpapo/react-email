# Documentation: clone-element-with-inlined-styles.ts
**File Path:** `packages/tailwind/src/utils/tailwindcss/clone-element-with-inlined-styles.ts`
**Language:** typescript
**Size:** 1,719 bytes
**Lines:** 59
**Generated:** 2025-11-15T20:37:32.424400Z

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

- **Path:** `packages/tailwind/src/utils/tailwindcss/clone-element-with-inlined-styles.ts`
- **Name:** `clone-element-with-inlined-styles.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,719 bytes (1.68 KB)
- **Lines of Code:** 59

---

## Original Source

```typescript
import type { Rule } from 'css-tree';
import React from 'react';
import type { EmailElementProps } from '../../tailwind';
import { sanitizeClassName } from '../compatibility/sanitize-class-name';
import type { CustomProperties } from '../css/get-custom-properties';
import { makeInlineStylesFor } from '../css/make-inline-styles-for';
import { isComponent } from '../react/is-component';

export function cloneElementWithInlinedStyles(
  element: React.ReactElement<EmailElementProps>,
  inlinableRules: Map<string, Rule>,
  nonInlinableRules: Map<string, Rule>,
  customProperties: CustomProperties,
) {
  const propsToOverwrite: Partial<EmailElementProps> = {};

  if (element.props.className && !isComponent(element)) {
    const classes = element.props.className.trim().split(/\s+/);

    const residualClasses: string[] = [];

    const rules: Rule[] = [];
    for (const className of classes) {
      const rule = inlinableRules.get(className);
      if (rule) {
        rules.push(rule);
      } else {
        residualClasses.push(className);
      }
    }

    const styles = makeInlineStylesFor(rules, customProperties);
    propsToOverwrite.style = {
      ...styles,
      ...element.props.style,
    };

    if (residualClasses.length > 0) {
      propsToOverwrite.className = residualClasses
        .map((className) => {
          if (nonInlinableRules.has(className)) {
            return sanitizeClassName(className);
          }
          return className;
        })
        .join(' ');
    } else {
      propsToOverwrite.className = undefined;
    }
  }

  const newProps = {
    ...element.props,
    ...propsToOverwrite,
  };

  return React.cloneElement(element, newProps, newProps.children);
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `classes()`
- `cloneElementWithInlinedStyles()`
- `newProps()`
- `rule()`
- `styles()`

### Dependencies

This file imports/requires:

- `../../tailwind`
- `../compatibility/sanitize-class-name`
- `../css/get-custom-properties`
- `../css/make-inline-styles-for`
- `../react/is-component`
- `css-tree`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 48

- `CustomProperties`
- `EmailElementProps`
- `Map`
- `Partial`
- `React`
- `ReactElement`
- `Rule`
- `children`
- `className`
- `classes`
- `cloneElement`
- `cloneElementWithInlinedStyles`
- `compatibility`
- `component`
- `css`
- `custom`
- `customProperties`
- `element`
- `get`
- `inlinableRules`
- `inline`
- `isComponent`
- `join`
- `length`
- `make`
- `makeInlineStylesFor`
- `map`
- `name`
- `newProps`
- `nonInlinableRules`
- `properties`
- `props`
- `propsToOverwrite`
- `push`
- `react`
- `residualClasses`
- `rule`
- `rules`
- `sanitize`
- `sanitizeClassName`
- `split`
- `string`
- `style`
- `styles`
- `tailwind`
- `tree`
- `trim`
- `type`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

