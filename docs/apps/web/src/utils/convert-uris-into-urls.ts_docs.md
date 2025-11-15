# Documentation: convert-uris-into-urls.ts
**File Path:** `apps/web/src/utils/convert-uris-into-urls.ts`
**Language:** typescript
**Size:** 720 bytes
**Lines:** 22
**Generated:** 2025-11-15T20:37:32.807016Z

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

- **Path:** `apps/web/src/utils/convert-uris-into-urls.ts`
- **Name:** `convert-uris-into-urls.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 720 bytes (0.70 KB)
- **Lines of Code:** 22

---

## Original Source

```typescript
const srcAttributeRegex = /src\s*=\s*"(?<URI>\/static.+)"/g;
const fontsUriFunctionRegex = /url\((?<URI>\/fonts[^)]+)\)/g;
const fontsUriStringRegex = /(?:"|'|`)(?<URI>\/fonts[^"'`]+)(?:"|'|`)/g;

export const convertUrisIntoUrls = (code: string) => {
  srcAttributeRegex.lastIndex = 0;
  fontsUriFunctionRegex.lastIndex = 0;
  fontsUriStringRegex.lastIndex = 0;
  return code
    .replaceAll(
      srcAttributeRegex,
      (_match, uri) => `src="https://react.email${uri}"`,
    )
    .replaceAll(
      fontsUriFunctionRegex,
      (_match, uri) => `url(https://react.email${uri})`,
    )
    .replaceAll(fontsUriStringRegex, (_match, uri: string) =>
      _match.replace(uri, `https://react.email${uri}`),
    );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `convertUrisIntoUrls()`
- `fontsUriFunctionRegex()`
- `fontsUriStringRegex()`
- `srcAttributeRegex()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 18

- `_match`
- `code`
- `convertUrisIntoUrls`
- `email`
- `fonts`
- `fontsUriFunctionRegex`
- `fontsUriStringRegex`
- `https`
- `lastIndex`
- `react`
- `replace`
- `replaceAll`
- `src`
- `srcAttributeRegex`
- `static`
- `string`
- `uri`
- `url`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

