# Documentation: jsx-dev-runtime.js
**File Path:** `packages/preview-server/jsx-runtime/jsx-dev-runtime.js`
**Language:** javascript
**Size:** 718 bytes
**Lines:** 25
**Generated:** 2025-11-15T20:37:31.778156Z

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

- **Path:** `packages/preview-server/jsx-runtime/jsx-dev-runtime.js`
- **Name:** `jsx-dev-runtime.js`
- **Extension:** `.js`
- **Language:** javascript
- **Size:** 718 bytes (0.70 KB)
- **Lines of Code:** 25

---

## Original Source

```javascript
// This hack is necessary because React forces the use of the non-dev JSX runtime
// when NODE_ENV is set to 'production', which would break the data-source references
// we need for stack traces in the preview server.
import ReactJSXDevRuntime from 'react/jsx-dev-runtime';

export function jsxDEV(type, props, key, isStaticChildren, source, self) {
  const newProps = { ...props };

  if (source && shouldIncludeSourceReference) {
    newProps['data-source-file'] = source.fileName;
    newProps['data-source-line'] = source.lineNumber;
  }

  return ReactJSXDevRuntime.jsxDEV(
    type,
    newProps,
    key,
    isStaticChildren,
    source,
    self,
  );
}

export const Fragment = ReactJSXDevRuntime.Fragment;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Fragment()`
- `jsxDEV()`
- `newProps()`

### Dependencies

This file imports/requires:

- `react/jsx-dev-runtime`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 37

- `Fragment`
- `NODE_ENV`
- `React`
- `ReactJSXDevRuntime`
- `because`
- `data`
- `dev`
- `file`
- `fileName`
- `forces`
- `hack`
- `isStaticChildren`
- `jsx`
- `jsxDEV`
- `key`
- `line`
- `lineNumber`
- `necessary`
- `need`
- `newProps`
- `non`
- `preview`
- `production`
- `props`
- `react`
- `references`
- `runtime`
- `server`
- `set`
- `shouldIncludeSourceReference`
- `source`
- `stack`
- `traces`
- `type`
- `use`
- `when`
- `which`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

