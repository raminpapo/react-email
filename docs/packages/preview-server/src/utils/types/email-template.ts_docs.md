# Documentation: email-template.ts
**File Path:** `packages/preview-server/src/utils/types/email-template.ts`
**Language:** typescript
**Size:** 267 bytes
**Lines:** 9
**Generated:** 2025-11-15T20:37:32.066114Z

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

- **Path:** `packages/preview-server/src/utils/types/email-template.ts`
- **Name:** `email-template.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 267 bytes (0.26 KB)
- **Lines of Code:** 9

---

## Original Source

```typescript
export interface EmailTemplate {
  (props: Record<string, unknown> | Record<string, never>): React.ReactNode;
  PreviewProps?: Record<string, unknown>;
}

export const isEmailTemplate = (val: unknown): val is EmailTemplate => {
  return typeof val === 'function';
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `isEmailTemplate()`

### Interfaces

- `EmailTemplate`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 12

- `EmailTemplate`
- `PreviewProps`
- `React`
- `ReactNode`
- `Record`
- `interface`
- `isEmailTemplate`
- `never`
- `props`
- `string`
- `unknown`
- `val`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

