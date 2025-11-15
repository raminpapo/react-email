# Documentation: mdx-email-test.js
**File Path:** `packages/preview-server/src/utils/testing/mdx-email-test.js`
**Language:** javascript
**Size:** 2,546 bytes
**Lines:** 129
**Generated:** 2025-11-15T20:37:32.076925Z

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

- **Path:** `packages/preview-server/src/utils/testing/mdx-email-test.js`
- **Name:** `mdx-email-test.js`
- **Extension:** `.js`
- **Language:** javascript
- **Size:** 2,546 bytes (2.49 KB)
- **Lines of Code:** 129

---

## Original Source

```javascript
import { Button, Html } from '@react-email/components';
import { useMDXComponents as _provideComponents } from 'react';
import {
  Fragment as _Fragment,
  jsxDEV as _jsxDEV,
} from 'react/jsx-dev-runtime';

const MDXLayout = function Email2() {
  return _jsxDEV(
    Html,
    {
      children: _jsxDEV(
        Button,
        {
          href: 'https://example.com',
          style: {
            background: '#000',
            color: '#fff',
            padding: '12px 20px',
          },
          children: 'Click me',
        },
        void 0,
        false,
        {
          fileName:
            '/Users/david/src/silencia-ai/silencia/proto/emails-raw/em1.mdx',
          lineNumber: 7,
          columnNumber: 7,
        },
        this,
      ),
    },
    void 0,
    false,
    {
      fileName:
        '/Users/david/src/silencia-ai/silencia/proto/emails-raw/em1.mdx',
      lineNumber: 6,
      columnNumber: 5,
    },
    this,
  );
};

function _createMdxContent(props) {
  const _components = {
    h1: 'h1',
    ..._provideComponents(),
    ...props.components,
  };
  return _jsxDEV(
    _Fragment,
    {
      children: [
        _jsxDEV(
          _components.h1,
          {
            children: 'Hello!',
          },
          void 0,
          false,
          {
            fileName:
              '/Users/david/src/silencia-ai/silencia/proto/emails-raw/em1.mdx',
            lineNumber: 17,
            columnNumber: 1,
          },
          this,
        ),
        '\n',
        _jsxDEV(
          Email,
          {},
          void 0,
          false,
          {
            fileName:
              '/Users/david/src/silencia-ai/silencia/proto/emails-raw/em1.mdx',
            lineNumber: 19,
            columnNumber: 1,
          },
          this,
        ),
      ],
    },
    void 0,
    true,
    {
      fileName:
        '/Users/david/src/silencia-ai/silencia/proto/emails-raw/em1.mdx',
      lineNumber: 1,
      columnNumber: 1,
    },
    this,
  );
}

function MDXContent(props = {}) {
  return _jsxDEV(
    MDXLayout,
    {
      ...props,
      children: _jsxDEV(
        _createMdxContent,
        {
          ...props,
        },
        void 0,
        false,
        {
          fileName:
            '/Users/david/src/silencia-ai/silencia/proto/emails-raw/em1.mdx',
        },
        this,
      ),
    },
    void 0,
    false,
    {
      fileName:
        '/Users/david/src/silencia-ai/silencia/proto/emails-raw/em1.mdx',
    },
    this,
  );
}

export { MDXContent as default };

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Email2()`
- `MDXContent()`
- `MDXLayout()`
- `_components()`
- `_createMdxContent()`

### Dependencies

This file imports/requires:

- `@react-email/components`
- `react`
- `react/jsx-dev-runtime`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 42

- `Button`
- `Click`
- `Email`
- `Email2`
- `Fragment`
- `Hello`
- `Html`
- `MDXContent`
- `MDXLayout`
- `Users`
- `_components`
- `background`
- `children`
- `color`
- `columnNumber`
- `com`
- `components`
- `david`
- `dev`
- `em1`
- `email`
- `emails`
- `example`
- `fff`
- `fileName`
- `href`
- `https`
- `jsx`
- `jsxDEV`
- `lineNumber`
- `mdx`
- `padding`
- `props`
- `proto`
- `raw`
- `react`
- `runtime`
- `silencia`
- `src`
- `style`
- `useMDXComponents`
- `void`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

