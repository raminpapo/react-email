# Documentation: styles.ts
**File Path:** `packages/markdown/src/styles.ts`
**Language:** typescript
**Size:** 2,453 bytes
**Lines:** 131
**Generated:** 2025-11-15T20:37:32.301775Z

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

- **Path:** `packages/markdown/src/styles.ts`
- **Name:** `styles.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,453 bytes (2.40 KB)
- **Lines of Code:** 131

---

## Original Source

```typescript
const emptyStyle = {};

const baseHeaderStyles = {
  fontWeight: '500',
  paddingTop: 20,
};

const h1 = {
  ...baseHeaderStyles,
  fontSize: '2.5rem',
};

const h2 = {
  ...baseHeaderStyles,
  fontSize: '2rem',
};
const h3 = {
  ...baseHeaderStyles,
  fontSize: '1.75rem',
};
const h4 = {
  ...baseHeaderStyles,
  fontSize: '1.5rem',
};
const h5 = {
  ...baseHeaderStyles,
  fontSize: '1.25rem',
};
const h6 = {
  ...baseHeaderStyles,
  fontSize: '1rem',
};

const bold = {
  fontWeight: 'bold',
};

const italic = {
  fontStyle: 'italic',
};

const blockQuote = {
  background: '#f9f9f9',
  borderLeft: '10px solid #ccc',
  margin: '1.5em 10px',
  padding: '1em 10px',
};

const codeInline = {
  color: '#212529',
  fontSize: '87.5%',
  display: 'inline',
  background: ' #f8f8f8',
  fontFamily: 'SFMono-Regular,Menlo,Monaco,Consolas,monospace',
};

const codeBlock = {
  ...codeInline,
  display: 'block',
  paddingTop: 10,
  paddingRight: 10,
  paddingLeft: 10,
  paddingBottom: 1,
  marginBottom: 20,
  background: ' #f8f8f8',
};

const link = {
  color: '#007bff',
  textDecoration: 'underline',
  backgroundColor: 'transparent',
};

export type StylesType = {
  h1?: React.CSSProperties;
  h2?: React.CSSProperties;
  h3?: React.CSSProperties;
  h4?: React.CSSProperties;
  h5?: React.CSSProperties;
  h6?: React.CSSProperties;
  blockQuote?: React.CSSProperties;
  bold?: React.CSSProperties;
  italic?: React.CSSProperties;
  link?: React.CSSProperties;
  codeBlock?: React.CSSProperties;
  codeInline?: React.CSSProperties;
  p?: React.CSSProperties;
  li?: React.CSSProperties;
  ul?: React.CSSProperties;
  ol?: React.CSSProperties;
  image?: React.CSSProperties;
  br?: React.CSSProperties;
  hr?: React.CSSProperties;
  table?: React.CSSProperties;
  thead?: React.CSSProperties;
  tbody?: React.CSSProperties;
  tr?: React.CSSProperties;
  th?: React.CSSProperties;
  td?: React.CSSProperties;
  strikethrough?: React.CSSProperties;
};

export const styles: StylesType = {
  h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  blockQuote,
  bold,
  italic,
  link,
  codeBlock: { ...codeBlock, wordWrap: 'break-word' },
  codeInline: { ...codeInline, wordWrap: 'break-word' },
  p: emptyStyle,
  li: emptyStyle,
  ul: emptyStyle,
  ol: emptyStyle,
  image: emptyStyle,
  br: emptyStyle,
  hr: emptyStyle,
  table: emptyStyle,
  thead: emptyStyle,
  tbody: emptyStyle,
  th: emptyStyle,
  td: emptyStyle,
  tr: emptyStyle,
  strikethrough: emptyStyle,
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `baseHeaderStyles()`
- `blockQuote()`
- `bold()`
- `codeBlock()`
- `codeInline()`
- `emptyStyle()`
- `h1()`
- `h2()`
- `h3()`
- `h4()`
- `h5()`
- `h6()`
- `italic()`
- `link()`

### Type Definitions

- `StylesType`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 51

- `CSSProperties`
- `Consolas`
- `Menlo`
- `Monaco`
- `React`
- `Regular`
- `SFMono`
- `StylesType`
- `background`
- `backgroundColor`
- `baseHeaderStyles`
- `block`
- `blockQuote`
- `bold`
- `borderLeft`
- `ccc`
- `codeBlock`
- `codeInline`
- `color`
- `display`
- `emptyStyle`
- `f8f8f8`
- `f9f9f9`
- `fontFamily`
- `fontSize`
- `fontStyle`
- `fontWeight`
- `image`
- `inline`
- `italic`
- `link`
- `margin`
- `marginBottom`
- `monospace`
- `padding`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `solid`
- `strikethrough`
- `styles`
- `table`
- `tbody`
- `textDecoration`
- `thead`
- `transparent`
- `type`
- `underline`
- `word`
- `wordWrap`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

