# Documentation: escape-class-name.spec.ts
**File Path:** `packages/tailwind/src/utils/compatibility/escape-class-name.spec.ts`
**Language:** typescript
**Size:** 601 bytes
**Lines:** 18
**Generated:** 2025-11-15T20:37:32.417248Z

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

- **Path:** `packages/tailwind/src/utils/compatibility/escape-class-name.spec.ts`
- **Name:** `escape-class-name.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 601 bytes (0.59 KB)
- **Lines of Code:** 18

---

## Original Source

```typescript
import { escapeClassName } from './escape-class-name';

describe('escapeClassName function', () => {
  it('escapes the first character properly', () => {
    expect(escapeClassName('[min-height-')).toBe('\\[min-height-');
  });

  it('does not escape an already escaped first-character', () => {
    expect(escapeClassName('\\[min-height-')).toBe('\\[min-height-');
  });

  it('escapes `min-height-[calc(25px+100%-20%*2/4)]` correctly', () => {
    expect(escapeClassName('min-height-[calc(25px+100%-20%*2/4)]')).toBe(
      'min-height-\\[calc\\(25px\\+100\\%-20\\%\\*2\\/4\\)\\]',
    );
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `./escape-class-name`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 16

- `already`
- `calc`
- `character`
- `correctly`
- `describe`
- `escape`
- `escapeClassName`
- `escaped`
- `escapes`
- `expect`
- `first`
- `height`
- `min`
- `name`
- `properly`
- `toBe`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

