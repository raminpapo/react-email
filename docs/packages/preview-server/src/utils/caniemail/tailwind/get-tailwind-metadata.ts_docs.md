# Documentation: get-tailwind-metadata.ts
**File Path:** `packages/preview-server/src/utils/caniemail/tailwind/get-tailwind-metadata.ts`
**Language:** typescript
**Size:** 1,048 bytes
**Lines:** 45
**Generated:** 2025-11-15T20:37:32.061899Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/tailwind/get-tailwind-metadata.ts`
- **Name:** `get-tailwind-metadata.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,048 bytes (1.02 KB)
- **Lines of Code:** 45

---

## Original Source

```typescript
import traverse from '@babel/traverse';
import { setupTailwind, type TailwindSetup } from '@react-email/tailwind';
import type { AST } from '../../../actions/email-validation/check-compatibility';
import { getTailwindConfig, type TailwindConfig } from './get-tailwind-config';

export const getTailwindMetadata = async (
  ast: AST,
  sourceCode: string,
  sourcePath: string,
): Promise<
  | {
      hasTailwind: false;
    }
  | {
      hasTailwind: true;
      config: TailwindConfig;
      tailwindSetup: TailwindSetup;
    }
> => {
  let hasTailwind = false as boolean;
  traverse(ast, {
    JSXOpeningElement(path) {
      if (
        path.node.name.type === 'JSXIdentifier' &&
        path.node.name.name === 'Tailwind'
      ) {
        hasTailwind = true;
      }
    },
  });

  if (!hasTailwind) {
    return { hasTailwind: false };
  }

  const config = await getTailwindConfig(sourceCode, ast, sourcePath);
  const tailwindSetup = await setupTailwind(config);

  return {
    hasTailwind: true,
    config,
    tailwindSetup,
  };
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `config()`
- `getTailwindMetadata()`
- `hasTailwind()`
- `tailwindSetup()`

### Type Definitions

- `TailwindConfig`
- `TailwindSetup`

### Dependencies

This file imports/requires:

- `../../../actions/email-validation/check-compatibility`
- `./get-tailwind-config`
- `@babel/traverse`
- `@react-email/tailwind`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 31

- `JSXIdentifier`
- `JSXOpeningElement`
- `Promise`
- `Tailwind`
- `TailwindConfig`
- `TailwindSetup`
- `actions`
- `ast`
- `babel`
- `boolean`
- `check`
- `compatibility`
- `config`
- `email`
- `get`
- `getTailwindConfig`
- `getTailwindMetadata`
- `hasTailwind`
- `name`
- `node`
- `path`
- `react`
- `setupTailwind`
- `sourceCode`
- `sourcePath`
- `string`
- `tailwind`
- `tailwindSetup`
- `traverse`
- `type`
- `validation`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

