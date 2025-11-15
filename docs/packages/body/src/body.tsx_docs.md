# Documentation: body.tsx
**File Path:** `packages/body/src/body.tsx`
**Language:** tsx
**Size:** 1,587 bytes
**Lines:** 49
**Generated:** 2025-11-15T20:37:31.541444Z

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

- **Path:** `packages/body/src/body.tsx`
- **Name:** `body.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,587 bytes (1.55 KB)
- **Lines of Code:** 49

---

## Original Source

```tsx
import * as React from 'react';
import { marginProperties } from './margin-properties';

export type BodyProps = Readonly<React.HtmlHTMLAttributes<HTMLBodyElement>>;

export const Body = React.forwardRef<HTMLBodyElement, BodyProps>(
  ({ children, style, ...props }, ref) => {
    const bodyStyle: Record<string, string | number | undefined> = {
      background: style?.background,
      backgroundColor: style?.backgroundColor,
    };
    if (style) {
      for (const property of marginProperties) {
        // We reset the margin if the user sets it, this mimics the
        // same behavior that would happen if this was only using the body.
        // This avoids the incoming margin summing up with the margin
        // defined by the email client on the body, or by the browser itself
        bodyStyle[property] = style[property] !== undefined ? 0 : undefined;
      }
    }
    return (
      <body {...props} style={bodyStyle} ref={ref}>
        <table
          border={0}
          width="100%"
          cellPadding="0"
          cellSpacing="0"
          role="presentation"
          align="center"
        >
          <tbody>
            <tr>
              {/*
                Yahoo and AOL remove all styles of the body element while converting it to a div,
                so we need to apply them to to an inner cell.

                See https://github.com/resend/react-email/issues/662.
              */}
              <td style={style}>{children}</td>
            </tr>
          </tbody>
        </table>
      </body>
    );
  },
);

Body.displayName = 'Body';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Body()`

### Type Definitions

- `BodyProps`

### Dependencies

This file imports/requires:

- `./margin-properties`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 70

- `Body`
- `BodyProps`
- `HTMLBodyElement`
- `HtmlHTMLAttributes`
- `React`
- `Readonly`
- `Record`
- `See`
- `Yahoo`
- `align`
- `all`
- `apply`
- `avoids`
- `background`
- `backgroundColor`
- `behavior`
- `body`
- `bodyStyle`
- `border`
- `browser`
- `cell`
- `cellPadding`
- `cellSpacing`
- `center`
- `children`
- `client`
- `com`
- `converting`
- `defined`
- `displayName`
- `div`
- `element`
- `email`
- `forwardRef`
- `github`
- `happen`
- `https`
- `incoming`
- `inner`
- `issues`
- `itself`
- `margin`
- `marginProperties`
- `mimics`
- `need`
- `number`
- `only`
- `presentation`
- `properties`
- `property`
- `props`
- `react`
- `ref`
- `remove`
- `resend`
- `reset`
- `role`
- `same`
- `sets`
- `string`
- `style`
- `styles`
- `summing`
- `table`
- `tbody`
- `them`
- `type`
- `user`
- `using`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

