# Documentation: extract-rules-per-class.spec.ts.snap
**File Path:** `packages/tailwind/src/utils/css/__snapshots__/extract-rules-per-class.spec.ts.snap`
**Language:** Unknown
**Size:** 1,033 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:32.478238Z

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

- **Path:** `packages/tailwind/src/utils/css/__snapshots__/extract-rules-per-class.spec.ts.snap`
- **Name:** `extract-rules-per-class.spec.ts.snap`
- **Extension:** `.snap`
- **Language:** Unknown
- **Size:** 1,033 bytes (1.01 KB)
- **Lines of Code:** 33

---

## Original Source

```
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`extractRulesPerClass() > handles a mix of inlinable and non-inlinable utilities 1`] = `
{
  "bg-red-500": ".bg-red-500{background-color:var(--color-red-500)}",
  "text-center": ".text-center{text-align:center}",
  "w-full": ".w-full{width:100%}",
}
`;

exports[`extractRulesPerClass() > handles a mix of inlinable and non-inlinable utilities 2`] = `
{
  "lg:w-1/2": ".lg\\:w-1\\/2{@media (width>=64rem){width:calc(1/2*100%)}}",
}
`;

exports[`extractRulesPerClass() > handles non-inlinable utilities 1`] = `{}`;

exports[`extractRulesPerClass() > handles non-inlinable utilities 2`] = `
{
  "lg:w-1/2": ".lg\\:w-1\\/2{@media (width>=64rem){width:calc(1/2*100%)}}",
}
`;

exports[`extractRulesPerClass() > works with just inlinable utilities 1`] = `
{
  "bg-red-500": ".bg-red-500{background-color:var(--color-red-500)}",
  "text-center": ".text-center{text-align:center}",
}
`;

exports[`extractRulesPerClass() > works with just inlinable utilities 2`] = `{}`;

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 27

- `Snapshot`
- `Vitest`
- `align`
- `background`
- `calc`
- `center`
- `color`
- `dev`
- `exports`
- `extractRulesPerClass`
- `full`
- `guide`
- `handles`
- `html`
- `https`
- `inlinable`
- `just`
- `media`
- `mix`
- `non`
- `red`
- `snapshot`
- `text`
- `utilities`
- `vitest`
- `width`
- `works`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

