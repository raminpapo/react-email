# Documentation: parse-css-in-js-to-inline-css.ts
**File Path:** `packages/markdown/src/utils/parse-css-in-js-to-inline-css.ts`
**Language:** typescript
**Size:** 1,601 bytes
**Lines:** 74
**Generated:** 2025-11-15T20:37:32.303240Z

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

- **Path:** `packages/markdown/src/utils/parse-css-in-js-to-inline-css.ts`
- **Name:** `parse-css-in-js-to-inline-css.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,601 bytes (1.56 KB)
- **Lines of Code:** 74

---

## Original Source

```typescript
function camelToKebabCase(str: string): string {
  return str.replace(/([a-z0-9])([A-Z])/g, '$1-$2').toLowerCase();
}

function escapeQuotes(value: unknown) {
  if (typeof value === 'string' && value.includes('"')) {
    return value.replace(/"/g, '&#x27;');
  }
  return value;
}

export function parseCssInJsToInlineCss(
  cssProperties: React.CSSProperties | undefined,
): string {
  if (!cssProperties) return '';

  const numericalCssProperties = [
    'width',
    'height',
    'margin',
    'marginTop',
    'marginRight',
    'marginBottom',
    'marginLeft',
    'padding',
    'paddingTop',
    'paddingRight',
    'paddingBottom',
    'paddingLeft',
    'borderWidth',
    'borderTopWidth',
    'borderRightWidth',
    'borderBottomWidth',
    'borderLeftWidth',
    'outlineWidth',
    'top',
    'right',
    'bottom',
    'left',
    'fontSize',
    'letterSpacing',
    'wordSpacing',
    'maxWidth',
    'minWidth',
    'maxHeight',
    'minHeight',
    'borderRadius',
    'borderTopLeftRadius',
    'borderTopRightRadius',
    'borderBottomLeftRadius',
    'borderBottomRightRadius',
    'textIndent',
    'gridColumnGap',
    'gridRowGap',
    'gridGap',
    'translateX',
    'translateY',
  ];

  return Object.entries(cssProperties)
    .map(([property, value]) => {
      if (
        typeof value === 'number' &&
        numericalCssProperties.includes(property)
      ) {
        return `${camelToKebabCase(property)}:${value}px`;
      }

      const escapedValue = escapeQuotes(value);
      return `${camelToKebabCase(property)}:${escapedValue}`;
    })
    .join(';');
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `camelToKebabCase()`
- `escapeQuotes()`
- `escapedValue()`
- `numericalCssProperties()`
- `parseCssInJsToInlineCss()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 62

- `CSSProperties`
- `Object`
- `React`
- `borderBottomLeftRadius`
- `borderBottomRightRadius`
- `borderBottomWidth`
- `borderLeftWidth`
- `borderRadius`
- `borderRightWidth`
- `borderTopLeftRadius`
- `borderTopRightRadius`
- `borderTopWidth`
- `borderWidth`
- `bottom`
- `camelToKebabCase`
- `cssProperties`
- `entries`
- `escapeQuotes`
- `escapedValue`
- `fontSize`
- `gridColumnGap`
- `gridGap`
- `gridRowGap`
- `height`
- `includes`
- `join`
- `left`
- `letterSpacing`
- `map`
- `margin`
- `marginBottom`
- `marginLeft`
- `marginRight`
- `marginTop`
- `maxHeight`
- `maxWidth`
- `minHeight`
- `minWidth`
- `number`
- `numericalCssProperties`
- `outlineWidth`
- `padding`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `parseCssInJsToInlineCss`
- `property`
- `replace`
- `right`
- `str`
- `string`
- `textIndent`
- `toLowerCase`
- `top`
- `translateX`
- `translateY`
- `unknown`
- `value`
- `width`
- `wordSpacing`
- `x27`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

