# Documentation: get-object-variables.ts
**File Path:** `packages/preview-server/src/utils/caniemail/ast/get-object-variables.ts`
**Language:** typescript
**Size:** 1,612 bytes
**Lines:** 62
**Generated:** 2025-11-15T20:37:32.051706Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/ast/get-object-variables.ts`
- **Name:** `get-object-variables.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,612 bytes (1.57 KB)
- **Lines of Code:** 62

---

## Original Source

```typescript
import type { Node } from '@babel/traverse';
import traverse from '@babel/traverse';
import type { AST } from '../../../actions/email-validation/check-compatibility';

export interface Position {
  line: number;
  column: number;
  index: number;
}

export const convertLocationIntoObject = (
  location: SourceLocation,
): SourceLocation => {
  return {
    start: {
      line: location.start.line,
      column: location.start.column,
      index: location.start.index,
    },
    end: {
      line: location.end.line,
      column: location.end.column,
      index: location.end.index,
    },
    filename: location.filename,
    identifierName: location.identifierName,
  };
};

export interface SourceLocation {
  start: Position;
  end: Position;
  filename: string;
  identifierName: string | undefined | null;
}

type ObjectProperty = Node & { type: 'ObjectProperty' };

export type ObjectVariables = Record<string, ObjectProperty[]>;

export const getObjectVariables = (ast: AST) => {
  const objectVariables: ObjectVariables = {};
  traverse(ast, {
    ObjectExpression(nodePath) {
      if (nodePath.parent.type === 'VariableDeclarator') {
        if (nodePath.parent.id.type === 'Identifier') {
          const variableName = nodePath.parent.id.name;
          const properties: ObjectProperty[] = [];
          for (const property of nodePath.node.properties) {
            if (property.type === 'ObjectProperty') {
              properties.push(property);
            }
          }
          objectVariables[variableName] = properties;
        }
      }
    },
  });

  return objectVariables;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `convertLocationIntoObject()`
- `getObjectVariables()`
- `variableName()`

### Interfaces

- `Position`
- `SourceLocation`

### Type Definitions

- `ObjectProperty`
- `ObjectVariables`

### Dependencies

This file imports/requires:

- `../../../actions/email-validation/check-compatibility`
- `@babel/traverse`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 40

- `Identifier`
- `Node`
- `ObjectExpression`
- `ObjectProperty`
- `ObjectVariables`
- `Position`
- `Record`
- `SourceLocation`
- `VariableDeclarator`
- `actions`
- `ast`
- `babel`
- `check`
- `column`
- `compatibility`
- `convertLocationIntoObject`
- `email`
- `end`
- `filename`
- `getObjectVariables`
- `identifierName`
- `index`
- `interface`
- `line`
- `location`
- `name`
- `node`
- `nodePath`
- `number`
- `objectVariables`
- `parent`
- `properties`
- `property`
- `push`
- `start`
- `string`
- `traverse`
- `type`
- `validation`
- `variableName`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

