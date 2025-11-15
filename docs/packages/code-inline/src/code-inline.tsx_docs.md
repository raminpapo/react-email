# Documentation: code-inline.tsx
**File Path:** `packages/code-inline/src/code-inline.tsx`
**Language:** tsx
**Size:** 1,644 bytes
**Lines:** 59
**Generated:** 2025-11-15T20:37:32.240657Z

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

- **Path:** `packages/code-inline/src/code-inline.tsx`
- **Name:** `code-inline.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,644 bytes (1.61 KB)
- **Lines of Code:** 59

---

## Original Source

```tsx
import * as React from 'react';

type RootProps = React.ComponentPropsWithoutRef<'code'> &
  React.ComponentPropsWithoutRef<'span'>;

export type CodeInlineProps = Readonly<RootProps>;

/**
 * If you are sending emails for users that have the Orange.fr email client,
 * beware that this component will only work when you have a head containing meta tags.
 */
export const CodeInline = React.forwardRef<HTMLSpanElement, CodeInlineProps>(
  ({ children, ...props }, ref) => {
    return (
      <>
        {/* 
    This style tag is targeted at fixing an issue for the Orange.fr email client
    See:
    - https://www.caniemail.com/features/html-code/
    - https://www.howtotarget.email/#2019-03-26-freenet-2

    On that email client, the head and html elements are removed, making the meta tag a sibling of them
    allowing us to use a selector on them. Also <style> tags are supported on it.
    */}
        <style>{`
        meta ~ .cino {
          display: none !important;
          opacity: 0 !important;
        }

        meta ~ .cio {
          display: block !important;
        }
      `}</style>

        {/* Does not render on Orange.fr */}
        <code
          {...props}
          className={`${props.className ? props.className : ''} cino`}
        >
          {children}
        </code>

        {/* Renders only on Orange.fr */}
        <span
          {...props}
          className={`${props.className ? props.className : ''} cio`}
          ref={ref}
          style={{ display: 'none', ...props.style }}
        >
          {children}
        </span>
      </>
    );
  },
);

CodeInline.displayName = 'CodeInline';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `CodeInline()`

### Type Definitions

- `CodeInlineProps`
- `RootProps`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 65

- `Also`
- `CodeInline`
- `CodeInlineProps`
- `ComponentPropsWithoutRef`
- `HTMLSpanElement`
- `Orange`
- `React`
- `Readonly`
- `Renders`
- `RootProps`
- `See`
- `allowing`
- `beware`
- `block`
- `caniemail`
- `children`
- `cino`
- `cio`
- `className`
- `client`
- `code`
- `com`
- `component`
- `containing`
- `display`
- `displayName`
- `elements`
- `email`
- `emails`
- `features`
- `fixing`
- `forwardRef`
- `freenet`
- `head`
- `howtotarget`
- `html`
- `https`
- `important`
- `issue`
- `making`
- `meta`
- `only`
- `opacity`
- `props`
- `react`
- `ref`
- `removed`
- `render`
- `selector`
- `sending`
- `sibling`
- `span`
- `style`
- `supported`
- `tag`
- `tags`
- `targeted`
- `them`
- `type`
- `use`
- `users`
- `when`
- `work`
- `www`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

