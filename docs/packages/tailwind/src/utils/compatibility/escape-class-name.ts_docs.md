# Documentation: escape-class-name.ts
**File Path:** `packages/tailwind/src/utils/compatibility/escape-class-name.ts`
**Language:** typescript
**Size:** 613 bytes
**Lines:** 19
**Generated:** 2025-11-15T20:37:32.418573Z

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

- **Path:** `packages/tailwind/src/utils/compatibility/escape-class-name.ts`
- **Name:** `escape-class-name.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 613 bytes (0.60 KB)
- **Lines of Code:** 19

---

## Original Source

```typescript
/**
 * Escapes all characters that may not be accepted on
 * CSS selectors by using the regex "[^a-zA-Z0-9\-_]".
 *
 * Also does a bit more trickery to avoid escaping already
 * escaped characters.
 */
export function escapeClassName(className: string) {
  return className.replace(
    /*      we need this look ahead capturing group to avoid using negative look behinds */
    /([^\\]|^)(?=([^a-zA-Z0-9\-_]))/g,
    (match, prefixCharacter: string, characterToEscape: string) => {
      if (prefixCharacter === '' && characterToEscape === '\\') return match;

      return `${prefixCharacter}\\`;
    },
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `escapeClassName()`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 29

- `Also`
- `Escapes`
- `accepted`
- `ahead`
- `all`
- `already`
- `avoid`
- `behinds`
- `bit`
- `capturing`
- `characterToEscape`
- `characters`
- `className`
- `escapeClassName`
- `escaped`
- `escaping`
- `group`
- `look`
- `match`
- `more`
- `need`
- `negative`
- `prefixCharacter`
- `regex`
- `replace`
- `selectors`
- `string`
- `trickery`
- `using`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

