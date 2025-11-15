# Documentation: sitemap.ts
**File Path:** `apps/web/src/app/sitemap.ts`
**Language:** typescript
**Size:** 254 bytes
**Lines:** 11
**Generated:** 2025-11-15T20:37:32.824729Z

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

- **Path:** `apps/web/src/app/sitemap.ts`
- **Name:** `sitemap.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 254 bytes (0.25 KB)
- **Lines of Code:** 11

---

## Original Source

```typescript
const Sitemap = async () => {
  const routes = ['', '/components', '/examples'].map((route) => ({
    url: `https://react.email${route}`,
    lastModified: new Date().toISOString().split('T')[0],
  }));

  return [...routes];
};

export default Sitemap;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Sitemap()`
- `routes()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 14

- `Date`
- `Sitemap`
- `components`
- `email`
- `examples`
- `https`
- `lastModified`
- `map`
- `react`
- `route`
- `routes`
- `split`
- `toISOString`
- `url`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

