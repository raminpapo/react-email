# Documentation: get-used-style-properties.spec.ts
**File Path:** `packages/preview-server/src/utils/caniemail/ast/get-used-style-properties.spec.ts`
**Language:** typescript
**Size:** 3,198 bytes
**Lines:** 120
**Generated:** 2025-11-15T20:37:32.053169Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/ast/get-used-style-properties.spec.ts`
- **Name:** `get-used-style-properties.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 3,198 bytes (3.12 KB)
- **Lines of Code:** 120

---

## Original Source

```typescript
import { parse } from '@babel/parser';
import { getObjectVariables } from './get-object-variables';
import { getUsedStyleProperties } from './get-used-style-properties';

describe('getUsedStyleProperties()', async () => {
  it('handles styles defined as an object in another variable', async () => {
    const reactCode = `
<Button style={buttonStyle}>Click me</Button>

const buttonStyle = {
  borderRadius: '5px',
};
`;
    const ast = parse(reactCode, {
      strictMode: false,
      errorRecovery: true,
      sourceType: 'unambiguous',
      plugins: ['jsx', 'typescript', 'decorators'],
    });
    const objectVariables = getObjectVariables(ast);
    expect(
      await getUsedStyleProperties(ast, reactCode, '', objectVariables),
    ).toMatchInlineSnapshot(`
      [
        {
          "location": SourceLocation {
            "end": Position {
              "column": 21,
              "index": 91,
              "line": 5,
            },
            "filename": undefined,
            "identifierName": undefined,
            "start": Position {
              "column": 2,
              "index": 72,
              "line": 5,
            },
          },
          "name": "borderRadius",
          "value": "5px",
        },
      ]
    `);
  });

  it('handles styles defined inline in the attribute', async () => {
    const reactCode = `
<Button style={{ borderRadius: '5px', "color": "#fff", padding: 10 }}>Click me</Button>
`;
    const ast = parse(reactCode, {
      strictMode: false,
      errorRecovery: true,
      sourceType: 'unambiguous',
      plugins: ['jsx', 'typescript', 'decorators'],
    });
    const objectVariables = getObjectVariables(ast);
    expect(
      await getUsedStyleProperties(ast, reactCode, '', objectVariables),
    ).toMatchInlineSnapshot(`
      [
        {
          "location": SourceLocation {
            "end": Position {
              "column": 36,
              "index": 37,
              "line": 2,
            },
            "filename": undefined,
            "identifierName": undefined,
            "start": Position {
              "column": 17,
              "index": 18,
              "line": 2,
            },
          },
          "name": "borderRadius",
          "value": "5px",
        },
        {
          "location": SourceLocation {
            "end": Position {
              "column": 53,
              "index": 54,
              "line": 2,
            },
            "filename": undefined,
            "identifierName": undefined,
            "start": Position {
              "column": 38,
              "index": 39,
              "line": 2,
            },
          },
          "name": "color",
          "value": "#fff",
        },
        {
          "location": SourceLocation {
            "end": Position {
              "column": 66,
              "index": 67,
              "line": 2,
            },
            "filename": undefined,
            "identifierName": undefined,
            "start": Position {
              "column": 55,
              "index": 56,
              "line": 2,
            },
          },
          "name": "padding",
          "value": "10",
        },
      ]
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

- `ast()`
- `buttonStyle()`
- `objectVariables()`
- `reactCode()`

### Dependencies

This file imports/requires:

- `./get-object-variables`
- `./get-used-style-properties`
- `@babel/parser`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 51

- `Button`
- `Click`
- `Position`
- `SourceLocation`
- `another`
- `ast`
- `attribute`
- `babel`
- `borderRadius`
- `buttonStyle`
- `color`
- `column`
- `decorators`
- `defined`
- `describe`
- `end`
- `errorRecovery`
- `expect`
- `fff`
- `filename`
- `get`
- `getObjectVariables`
- `getUsedStyleProperties`
- `handles`
- `identifierName`
- `index`
- `inline`
- `jsx`
- `line`
- `location`
- `name`
- `object`
- `objectVariables`
- `padding`
- `parse`
- `parser`
- `plugins`
- `properties`
- `reactCode`
- `sourceType`
- `start`
- `strictMode`
- `style`
- `styles`
- `toMatchInlineSnapshot`
- `typescript`
- `unambiguous`
- `used`
- `value`
- `variable`
- `variables`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

