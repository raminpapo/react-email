# Documentation: button.tsx
**File Path:** `packages/button/src/button.tsx`
**Language:** tsx
**Size:** 3,304 bytes
**Lines:** 113
**Generated:** 2025-11-15T20:37:32.219064Z

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

- **Path:** `packages/button/src/button.tsx`
- **Name:** `button.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,304 bytes (3.23 KB)
- **Lines of Code:** 113

---

## Original Source

```tsx
import * as React from 'react';
import { parsePadding } from './utils/parse-padding';
import { pxToPt } from './utils/px-to-pt';

export type ButtonProps = Readonly<React.ComponentPropsWithoutRef<'a'>>;

const maxFontWidth = 5;

/**
 * Computes a msoFontWidth \<= 5 and a count of space characters that,
 * when applied, end up being as close to `expectedWidth` as possible.
 */
function computeFontWidthAndSpaceCount(expectedWidth: number) {
  if (expectedWidth === 0) return [0, 0] as const;

  let smallestSpaceCount = 0;

  const computeRequiredFontWidth = () => {
    if (smallestSpaceCount > 0) {
      return expectedWidth / smallestSpaceCount / 2;
    }

    return Number.POSITIVE_INFINITY;
  };

  while (computeRequiredFontWidth() > maxFontWidth) {
    smallestSpaceCount++;
  }

  return [computeRequiredFontWidth(), smallestSpaceCount] as const;
}

declare module 'react' {
  interface CSSProperties {
    msoPaddingAlt?: string | number | undefined;
    msoTextRaise?: string | number | undefined;
  }
}

export const Button = React.forwardRef<HTMLAnchorElement, ButtonProps>(
  ({ children, style, target = '_blank', ...props }, ref) => {
    const { paddingTop, paddingRight, paddingBottom, paddingLeft } =
      parsePadding(style ?? {});

    const y = (paddingTop ?? 0) + (paddingBottom ?? 0);
    const textRaise = pxToPt(y);

    const [plFontWidth, plSpaceCount] = computeFontWidthAndSpaceCount(
      paddingLeft ?? 0,
    );
    const [prFontWidth, prSpaceCount] = computeFontWidthAndSpaceCount(
      paddingRight ?? 0,
    );

    return (
      <a
        {...props}
        ref={ref}
        style={{
          lineHeight: '100%',
          textDecoration: 'none',
          display: 'inline-block',
          maxWidth: '100%',
          msoPaddingAlt: '0px',
          ...style,
          paddingTop,
          paddingRight,
          paddingBottom,
          paddingLeft,
        }}
        target={target}
      >
        <span
          dangerouslySetInnerHTML={{
            // The `&#8202;` is as close to `1px` of an empty character as we can get, then, we use the `mso-font-width`
            // to scale it according to what padding the developer wants. `mso-font-width` also does not allow for percentages
            // >= 500% so we need to add extra spaces accordingly.
            //
            // See https://github.com/resend/react-email/issues/1512 for why we do not use letter-spacing instead.
            __html: `<!--[if mso]><i style="mso-font-width:${
              plFontWidth * 100
            }%;mso-text-raise:${textRaise}" hidden>${'&#8202;'.repeat(
              plSpaceCount,
            )}</i><![endif]-->`,
          }}
        />
        <span
          style={{
            maxWidth: '100%',
            display: 'inline-block',
            lineHeight: '120%',
            msoPaddingAlt: '0px',
            msoTextRaise: pxToPt(paddingBottom),
          }}
        >
          {children}
        </span>
        <span
          dangerouslySetInnerHTML={{
            __html: `<!--[if mso]><i style="mso-font-width:${
              prFontWidth * 100
            }%" hidden>${'&#8202;'.repeat(
              prSpaceCount,
            )}&#8203;</i><![endif]-->`,
          }}
        />
      </a>
    );
  },
);

Button.displayName = 'Button';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Button()`
- `computeFontWidthAndSpaceCount()`
- `computeRequiredFontWidth()`
- `maxFontWidth()`
- `smallestSpaceCount()`
- `textRaise()`
- `y()`

### Interfaces

- `CSSProperties`

### Type Definitions

- `ButtonProps`

### Dependencies

This file imports/requires:

- `./utils/parse-padding`
- `./utils/px-to-pt`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 101

- `Button`
- `ButtonProps`
- `CSSProperties`
- `ComponentPropsWithoutRef`
- `Computes`
- `HTMLAnchorElement`
- `Number`
- `POSITIVE_INFINITY`
- `React`
- `Readonly`
- `See`
- `__html`
- `_blank`
- `according`
- `accordingly`
- `add`
- `allow`
- `also`
- `applied`
- `block`
- `character`
- `characters`
- `children`
- `close`
- `com`
- `computeFontWidthAndSpaceCount`
- `computeRequiredFontWidth`
- `count`
- `dangerouslySetInnerHTML`
- `declare`
- `developer`
- `display`
- `displayName`
- `email`
- `empty`
- `end`
- `endif`
- `expectedWidth`
- `extra`
- `font`
- `forwardRef`
- `get`
- `github`
- `hidden`
- `https`
- `inline`
- `instead`
- `interface`
- `issues`
- `letter`
- `lineHeight`
- `maxFontWidth`
- `maxWidth`
- `module`
- `mso`
- `msoFontWidth`
- `msoPaddingAlt`
- `msoTextRaise`
- `need`
- `number`
- `padding`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `parse`
- `parsePadding`
- `percentages`
- `plFontWidth`
- `plSpaceCount`
- `possible`
- `prFontWidth`
- `prSpaceCount`
- `props`
- `pxToPt`
- `raise`
- `react`
- `ref`
- `repeat`
- `resend`
- `scale`
- `smallestSpaceCount`
- `space`
- `spaces`
- `spacing`
- `span`
- `string`
- `style`
- `target`
- `text`
- `textDecoration`
- `textRaise`
- `then`
- `type`
- `use`
- `utils`
- `wants`
- `what`
- `when`
- `why`
- `width`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

