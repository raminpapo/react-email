# Documentation: as.ts
**File Path:** `packages/heading/src/utils/as.ts`
**Language:** typescript
**Size:** 630 bytes
**Lines:** 27
**Generated:** 2025-11-15T20:37:32.286843Z

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

- **Path:** `packages/heading/src/utils/as.ts`
- **Name:** `as.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 630 bytes (0.62 KB)
- **Lines of Code:** 27

---

## Original Source

```typescript
export type As<
  DefaultTag extends React.ElementType,
  T1 extends React.ElementType,
  T2 extends React.ElementType = T1,
  T3 extends React.ElementType = T1,
  T4 extends React.ElementType = T1,
  T5 extends React.ElementType = T1,
> =
  | (React.ComponentPropsWithRef<DefaultTag> & {
      as?: DefaultTag;
    })
  | (React.ComponentPropsWithRef<T1> & {
      as: T1;
    })
  | (React.ComponentPropsWithRef<T2> & {
      as: T2;
    })
  | (React.ComponentPropsWithRef<T3> & {
      as: T3;
    })
  | (React.ComponentPropsWithRef<T4> & {
      as: T4;
    })
  | (React.ComponentPropsWithRef<T5> & {
      as: T5;
    });

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Type Definitions

- `As`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 6

- `ComponentPropsWithRef`
- `DefaultTag`
- `ElementType`
- `React`
- `extends`
- `type`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

