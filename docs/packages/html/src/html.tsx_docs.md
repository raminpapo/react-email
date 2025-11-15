# Documentation: html.tsx
**File Path:** `packages/html/src/html.tsx`
**Language:** tsx
**Size:** 356 bytes
**Lines:** 14
**Generated:** 2025-11-15T20:37:32.342139Z

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

- **Path:** `packages/html/src/html.tsx`
- **Name:** `html.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 356 bytes (0.35 KB)
- **Lines of Code:** 14

---

## Original Source

```tsx
import * as React from 'react';

export type HtmlProps = Readonly<React.ComponentPropsWithoutRef<'html'>>;

export const Html = React.forwardRef<HTMLHtmlElement, HtmlProps>(
  ({ children, lang = 'en', dir = 'ltr', ...props }, ref) => (
    <html {...props} dir={dir} lang={lang} ref={ref}>
      {children}
    </html>
  ),
);

Html.displayName = 'Html';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Html()`

### Type Definitions

- `HtmlProps`

### Dependencies

This file imports/requires:

- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 17

- `ComponentPropsWithoutRef`
- `HTMLHtmlElement`
- `Html`
- `HtmlProps`
- `React`
- `Readonly`
- `children`
- `dir`
- `displayName`
- `forwardRef`
- `html`
- `lang`
- `ltr`
- `props`
- `react`
- `ref`
- `type`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

