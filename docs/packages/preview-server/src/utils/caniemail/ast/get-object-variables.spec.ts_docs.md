# Documentation: get-object-variables.spec.ts
**File Path:** `packages/preview-server/src/utils/caniemail/ast/get-object-variables.spec.ts`
**Language:** typescript
**Size:** 483 bytes
**Lines:** 20
**Generated:** 2025-11-15T20:37:32.050359Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/ast/get-object-variables.spec.ts`
- **Name:** `get-object-variables.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 483 bytes (0.47 KB)
- **Lines of Code:** 20

---

## Original Source

```typescript
import { parse } from '@babel/parser';
import { getObjectVariables } from './get-object-variables';

test('getObjectVariables()', () => {
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
  expect(getObjectVariables(ast)).toMatchSnapshot();
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
- `reactCode()`

### Dependencies

This file imports/requires:

- `./get-object-variables`
- `@babel/parser`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 25

- `Button`
- `Click`
- `ast`
- `babel`
- `borderRadius`
- `buttonStyle`
- `decorators`
- `errorRecovery`
- `expect`
- `get`
- `getObjectVariables`
- `jsx`
- `object`
- `parse`
- `parser`
- `plugins`
- `reactCode`
- `sourceType`
- `strictMode`
- `style`
- `test`
- `toMatchSnapshot`
- `typescript`
- `unambiguous`
- `variables`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

