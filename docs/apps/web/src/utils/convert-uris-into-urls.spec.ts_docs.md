# Documentation: convert-uris-into-urls.spec.ts
**File Path:** `apps/web/src/utils/convert-uris-into-urls.spec.ts`
**Language:** typescript
**Size:** 1,278 bytes
**Lines:** 74
**Generated:** 2025-11-15T20:37:32.805821Z

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

- **Path:** `apps/web/src/utils/convert-uris-into-urls.spec.ts`
- **Name:** `convert-uris-into-urls.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,278 bytes (1.25 KB)
- **Lines of Code:** 74

---

## Original Source

```typescript
import { convertUrisIntoUrls } from './convert-uris-into-urls';

describe('convertUrisIntoUrls()', () => {
  it('works with src attributes', () => {
    expect(
      convertUrisIntoUrls(`
const MyComp = () => {
  return <Img src="/static/my-image.png"/>;
}

<html>
  <head>...</head>
  <body>
    <img src="/static/my-image.png">
  </body>
</html>
`),
    ).toBe(`
const MyComp = () => {
  return <Img src="https://react.email/static/my-image.png"/>;
}

<html>
  <head>...</head>
  <body>
    <img src="https://react.email/static/my-image.png">
  </body>
</html>
`);
  });

  it('works with url() function calls for fonts in styles', () => {
    expect(
      convertUrisIntoUrls(`
const MyComp = () => {
  return <style dangerouslySetInnerHTML={{ __html: '
.my-class {
  font-family: url(/fonts/my-font);
}
' }}>;
}

<html>
  <head>
    <style>
      .my-class {
        font-family: url(/fonts/my-font);
      }
    </style>
  </head>
</html>
`),
    ).toBe(`
const MyComp = () => {
  return <style dangerouslySetInnerHTML={{ __html: '
.my-class {
  font-family: url(https://react.email/fonts/my-font);
}
' }}>;
}

<html>
  <head>
    <style>
      .my-class {
        font-family: url(https://react.email/fonts/my-font);
      }
    </style>
  </head>
</html>
`);
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `MyComp()`

### Dependencies

This file imports/requires:

- `./convert-uris-into-urls`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 32

- `Img`
- `MyComp`
- `__html`
- `attributes`
- `body`
- `calls`
- `convert`
- `convertUrisIntoUrls`
- `dangerouslySetInnerHTML`
- `describe`
- `email`
- `expect`
- `family`
- `font`
- `fonts`
- `head`
- `html`
- `https`
- `image`
- `img`
- `into`
- `png`
- `react`
- `src`
- `static`
- `style`
- `styles`
- `toBe`
- `uris`
- `url`
- `urls`
- `works`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

