# Documentation: get-imported-modules.spec.ts
**File Path:** `packages/react-email/src/utils/preview/hot-reloading/get-imported-modules.spec.ts`
**Language:** typescript
**Size:** 3,169 bytes
**Lines:** 152
**Generated:** 2025-11-15T20:37:32.557541Z

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

- **Path:** `packages/react-email/src/utils/preview/hot-reloading/get-imported-modules.spec.ts`
- **Name:** `get-imported-modules.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 3,169 bytes (3.09 KB)
- **Lines of Code:** 152

---

## Original Source

```typescript
import { promises as fs } from 'node:fs';
import { getImportedModules } from './get-imported-modules.js';

vi.mock('@babel/traverse', async () => {
  const traverse = await vi.importActual('@babel/traverse');
  return { default: traverse };
});

describe('getImportedModules()', () => {
  it('works with this test file', async () => {
    const contents = await fs.readFile(import.meta.filename, 'utf8');

    expect(getImportedModules(contents)).toEqual([
      'node:fs',
      './get-imported-modules.js',
    ]);
  });

  it('works with direct exports', () => {
    const contents = `export * from './component-a';
    export { ComponentB } from './component-b'; 

    import { ComponentC } from './component-c';
    export { ComponentC }`;
    expect(getImportedModules(contents)).toEqual([
      './component-a',
      './component-b',
      './component-c',
    ]);
  });

  it('works with regular imports and double quotes', () => {
    const contents = `import {
  Body,
  Button,
  Container,
  Column,
  Head,
  Heading,
  Hr,
  Html,
  Img,
  Link,
  Preview,
  Row,
  Section,
  Text,
} from "@react-email/components";
import { Tailwind } from "@react-email/tailwind";
import { Component } from '../../my-component';

import * as React from "react";
    `;
    expect(getImportedModules(contents)).toEqual([
      '@react-email/components',
      '@react-email/tailwind',
      '../../my-component',
      'react',
    ]);
  });

  it('works with regular imports and single quotes', () => {
    const contents = `import {
  Body,
  Button,
  Container,
  Column,
  Head,
  Heading,
  Hr,
  Html,
  Img,
  Link,
  Preview,
  Row,
  Section,
  Text,
} from '@react-email/components';
import { Tailwind } from '@react-email/tailwind';
import { Component } from '../../my-component';

import * as React from 'react';
    `;
    expect(getImportedModules(contents)).toEqual([
      '@react-email/components',
      '@react-email/tailwind',
      '../../my-component',
      'react',
    ]);
  });

  it('works with commonjs require with double quotes', () => {
    const contents = `const {
  Body,
  Button,
  Container,
  Column,
  Head,
  Heading,
  Hr,
  Html,
  Img,
  Link,
  Preview,
  Row,
  Section,
  Text,
} = require("@react-email/components");
const { Tailwind } = require("@react-email/tailwind");
const { Component } = require("../../my-component");

const React = require("react");
    `;
    expect(getImportedModules(contents)).toEqual([
      '@react-email/components',
      '@react-email/tailwind',
      '../../my-component',
      'react',
    ]);
  });

  it('works with commonjs require with single quotes', () => {
    const contents = `const {
  Body,
  Button,
  Container,
  Column,
  Head,
  Heading,
  Hr,
  Html,
  Img,
  Link,
  Preview,
  Row,
  Section,
  Text,
} = require('@react-email/components');
const { Tailwind } = require('@react-email/tailwind');
const { Component } = require('../../my-component');

const React = require('react');
    `;
    expect(getImportedModules(contents)).toEqual([
      '@react-email/components',
      '@react-email/tailwind',
      '../../my-component',
      'react',
    ]);
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `React()`
- `contents()`
- `traverse()`

### Dependencies

This file imports/requires:

- `../../my-component`
- `./component-a`
- `./component-b`
- `./component-c`
- `./get-imported-modules.js`
- `@react-email/components`
- `@react-email/tailwind`
- `node:fs`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 53

- `Body`
- `Button`
- `Column`
- `Component`
- `ComponentB`
- `ComponentC`
- `Container`
- `Head`
- `Heading`
- `Html`
- `Img`
- `Link`
- `Preview`
- `React`
- `Row`
- `Section`
- `Tailwind`
- `Text`
- `babel`
- `commonjs`
- `component`
- `components`
- `contents`
- `describe`
- `direct`
- `double`
- `email`
- `expect`
- `exports`
- `file`
- `filename`
- `get`
- `getImportedModules`
- `importActual`
- `imported`
- `imports`
- `meta`
- `mock`
- `modules`
- `node`
- `promises`
- `quotes`
- `react`
- `readFile`
- `regular`
- `require`
- `single`
- `tailwind`
- `test`
- `toEqual`
- `traverse`
- `utf8`
- `works`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

