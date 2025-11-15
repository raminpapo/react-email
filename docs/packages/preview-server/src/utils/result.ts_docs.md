# Documentation: result.ts
**File Path:** `packages/preview-server/src/utils/result.ts`
**Language:** typescript
**Size:** 1,353 bytes
**Lines:** 50
**Generated:** 2025-11-15T20:37:32.030498Z

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

- **Path:** `packages/preview-server/src/utils/result.ts`
- **Name:** `result.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,353 bytes (1.32 KB)
- **Lines of Code:** 50

---

## Original Source

```typescript
type Ok<T, _E> = {
  value: T;
};
type Error<_T, E> = {
  error: E;
};

/**
 * Do not destructure this object, it is meant to have all fields together
 * in the same object
 */
export type Result<T, E> = Ok<T, E> | Error<T, E>;

export function isErr<T, E>(result: Result<T, E>): result is Error<T, E> {
  return 'error' in result;
}

export function isOk<T, E>(result: Result<T, E>): result is Ok<T, E> {
  return 'value' in result && !('error' in result);
}

export function mapResult<T, E, B>(
  result: Result<T, E>,
  callback: (value: T) => B,
): Result<B, E> {
  if (isOk(result)) {
    return ok(callback(result.value));
  }

  return result;
}

export function ok<T, E>(value: NoInfer<T>): Ok<T, E>;
// biome-ignore lint/suspicious/noConfusingVoidType: This is required for void return types on functions that can still error
export function ok<_T extends void = void, E = never>(value: void): Ok<void, E>;
export function ok<T, E>(value: NoInfer<T>): Ok<T, E> {
  return {
    value,
  };
}

export function err<T, E>(error: NoInfer<E>): Error<T, E>;
// biome-ignore lint/suspicious/noConfusingVoidType: This is required for void return types on functions that can still error
export function err<T, _E extends void = void>(error: void): Error<T, void>;
export function err<T, E>(error: NoInfer<E>): Error<T, E> {
  return {
    error,
  };
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Type Definitions

- `Error`
- `Ok`
- `Result`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 31

- `Error`
- `NoInfer`
- `Result`
- `all`
- `biome`
- `callback`
- `destructure`
- `err`
- `error`
- `extends`
- `fields`
- `functions`
- `ignore`
- `isErr`
- `isOk`
- `lint`
- `mapResult`
- `meant`
- `never`
- `noConfusingVoidType`
- `object`
- `required`
- `result`
- `same`
- `still`
- `suspicious`
- `together`
- `type`
- `types`
- `value`
- `void`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

