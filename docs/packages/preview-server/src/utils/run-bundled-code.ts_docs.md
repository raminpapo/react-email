# Documentation: run-bundled-code.ts
**File Path:** `packages/preview-server/src/utils/run-bundled-code.ts`
**Language:** typescript
**Size:** 2,472 bytes
**Lines:** 87
**Generated:** 2025-11-15T20:37:32.031798Z

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

- **Path:** `packages/preview-server/src/utils/run-bundled-code.ts`
- **Name:** `run-bundled-code.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,472 bytes (2.41 KB)
- **Lines of Code:** 87

---

## Original Source

```typescript
import path from 'node:path';
import vm from 'node:vm';
import { err, ok, type Result } from './result';
import { staticNodeModulesForVM } from './static-node-modules-for-vm';

export const createContext = (filename: string): vm.Context => {
  return new Proxy(
    {
      module: {
        exports: {},
      },
      __filename: filename,
      __dirname: path.dirname(filename),
      require: (specifiedModule: string) => {
        let m = specifiedModule;
        if (specifiedModule.startsWith('node:')) {
          m = m.split(':')[1]!;
        }

        if (m in staticNodeModulesForVM) {
          return staticNodeModulesForVM[m];
        }

        return require(`${specifiedModule}`) as unknown;
        // this string templating was necessary to not have
        // webpack warnings like:
        //
        // Import trace for requested module:
        // ./src/utils/get-email-component.tsx
        // ./src/app/page.tsx
        //  ⚠ ./src/utils/get-email-component.tsx
        // Critical dependency: the request of a dependency is an expression
      },
    },
    {
      get(target, property: string) {
        if (property in target) {
          return target[property];
        }

        return globalThis[property as keyof typeof globalThis];
      },
      has(target, property: string) {
        return property in target || property in globalThis;
      },
      set(target, property, value) {
        target[property] = value;
        return true;
      },
      getOwnPropertyDescriptor(target, property) {
        return (
          Object.getOwnPropertyDescriptor(target, property) ??
          Object.getOwnPropertyDescriptor(globalThis, property)
        );
      },
      ownKeys(target) {
        const keys = new Set([
          ...Reflect.ownKeys(globalThis),
          ...Reflect.ownKeys(target),
        ]);
        return Array.from(keys);
      },
      defineProperty(target, property, descriptor) {
        Object.defineProperty(target, property, descriptor);
        return true;
      },
      deleteProperty(target, property) {
        return delete target[property];
      },
    },
  );
};

export const runBundledCode = (
  code: string,
  filename: string,
  fakeContext: vm.Context = createContext(filename),
): Result<unknown, unknown> => {
  try {
    vm.runInNewContext(code, fakeContext, { filename });
  } catch (exception) {
    return err(exception);
  }

  return ok(fakeContext.module.exports as unknown);
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `createContext()`
- `keys()`
- `m()`
- `runBundledCode()`

### Type Definitions

- `Result`

### Dependencies

This file imports/requires:

- `./result`
- `./static-node-modules-for-vm`
- `node:path`
- `node:vm`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 65

- `Array`
- `Context`
- `Critical`
- `Object`
- `Proxy`
- `Reflect`
- `Result`
- `Set`
- `__dirname`
- `__filename`
- `app`
- `code`
- `component`
- `createContext`
- `defineProperty`
- `delete`
- `deleteProperty`
- `dependency`
- `descriptor`
- `dirname`
- `email`
- `err`
- `exception`
- `exports`
- `expression`
- `fakeContext`
- `filename`
- `get`
- `getOwnPropertyDescriptor`
- `globalThis`
- `keyof`
- `keys`
- `like`
- `module`
- `modules`
- `necessary`
- `node`
- `ownKeys`
- `page`
- `path`
- `property`
- `request`
- `requested`
- `require`
- `result`
- `runBundledCode`
- `runInNewContext`
- `set`
- `specifiedModule`
- `split`
- `src`
- `startsWith`
- `static`
- `staticNodeModulesForVM`
- `string`
- `target`
- `templating`
- `trace`
- `tsx`
- `type`
- `unknown`
- `utils`
- `value`
- `warnings`
- `webpack`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

