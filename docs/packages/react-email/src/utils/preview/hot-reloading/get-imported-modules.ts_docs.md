# Documentation: get-imported-modules.ts
**File Path:** `packages/react-email/src/utils/preview/hot-reloading/get-imported-modules.ts`
**Language:** typescript
**Size:** 1,377 bytes
**Lines:** 50
**Generated:** 2025-11-15T20:37:32.559168Z

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

- **Path:** `packages/react-email/src/utils/preview/hot-reloading/get-imported-modules.ts`
- **Name:** `get-imported-modules.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,377 bytes (1.34 KB)
- **Lines of Code:** 50

---

## Original Source

```typescript
import { parse } from '@babel/parser';

import traverseModule from '@babel/traverse';

const traverse =
  // we keep this check here so that this still works with the dev:preview
  // script's use of tsx
  typeof traverseModule === 'function'
    ? traverseModule
    : traverseModule.default;

export const getImportedModules = (contents: string) => {
  const importedPaths: string[] = [];
  const parsedContents = parse(contents, {
    sourceType: 'unambiguous',
    strictMode: false,
    errorRecovery: true,
    plugins: ['jsx', 'typescript', 'decorators'],
  });

  traverse(parsedContents, {
    ImportDeclaration({ node }) {
      importedPaths.push(node.source.value);
    },
    ExportAllDeclaration({ node }) {
      importedPaths.push(node.source.value);
    },
    ExportNamedDeclaration({ node }) {
      if (node.source) {
        importedPaths.push(node.source.value);
      }
    },
    TSExternalModuleReference({ node }) {
      importedPaths.push(node.expression.value);
    },
    CallExpression({ node }) {
      if ('name' in node.callee && node.callee.name === 'require') {
        if (node.arguments.length === 1) {
          const importPathNode = node.arguments[0]!;
          if (importPathNode!.type === 'StringLiteral') {
            importedPaths.push(importPathNode.value);
          }
        }
      }
    },
  });

  return importedPaths;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getImportedModules()`
- `importPathNode()`
- `parsedContents()`
- `traverse()`

### Dependencies

This file imports/requires:

- `@babel/parser`
- `@babel/traverse`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 46

- `CallExpression`
- `ExportAllDeclaration`
- `ExportNamedDeclaration`
- `ImportDeclaration`
- `StringLiteral`
- `TSExternalModuleReference`
- `arguments`
- `babel`
- `callee`
- `check`
- `contents`
- `decorators`
- `dev`
- `errorRecovery`
- `expression`
- `getImportedModules`
- `here`
- `importPathNode`
- `importedPaths`
- `jsx`
- `keep`
- `length`
- `name`
- `node`
- `parse`
- `parsedContents`
- `parser`
- `plugins`
- `preview`
- `push`
- `require`
- `script`
- `source`
- `sourceType`
- `still`
- `strictMode`
- `string`
- `traverse`
- `traverseModule`
- `tsx`
- `type`
- `typescript`
- `unambiguous`
- `use`
- `value`
- `works`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

