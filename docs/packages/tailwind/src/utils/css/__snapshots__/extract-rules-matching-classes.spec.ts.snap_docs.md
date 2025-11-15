# Documentation: extract-rules-matching-classes.spec.ts.snap
**File Path:** `packages/tailwind/src/utils/css/__snapshots__/extract-rules-matching-classes.spec.ts.snap`
**Language:** Unknown
**Size:** 818 bytes
**Lines:** 24
**Generated:** 2025-11-15T20:37:32.477040Z

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

- **Path:** `packages/tailwind/src/utils/css/__snapshots__/extract-rules-matching-classes.spec.ts.snap`
- **Name:** `extract-rules-matching-classes.spec.ts.snap`
- **Extension:** `.snap`
- **Language:** Unknown
- **Size:** 818 bytes (0.80 KB)
- **Lines of Code:** 24

---

## Original Source

```
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`extractRulesMatchingClasses() > should work just inlinable utilities 1`] = `
{
  "bg-red-500": ".bg-red-500{background-color:rgb(250.6,43.8,54.3)}",
  "text-center": ".text-center{text-align:center}",
}
`;

exports[`extractRulesMatchingClasses() > should work with a mix of inlinable and non-inlinable utilities 1`] = `
{
  "bg-red-500": ".bg-red-500{background-color:rgb(250.6,43.8,54.3)}",
  "lg:w-1/2": ".lg_w-1_2{@media (width>=64rem){width:calc(0.5*100%)!important}}",
  "text-center": ".text-center{text-align:center}",
  "w-full": ".w-full{width:100%}",
}
`;

exports[`extractRulesMatchingClasses() > should work with non-inlinable utilities 1`] = `
{
  "lg:w-1/2": ".lg_w-1_2{@media (width>=64rem){width:calc(0.5*100%)!important}}",
}
`;

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 29

- `Snapshot`
- `Vitest`
- `align`
- `background`
- `calc`
- `center`
- `color`
- `dev`
- `exports`
- `extractRulesMatchingClasses`
- `full`
- `guide`
- `html`
- `https`
- `important`
- `inlinable`
- `just`
- `lg_w`
- `media`
- `mix`
- `non`
- `red`
- `rgb`
- `snapshot`
- `text`
- `utilities`
- `vitest`
- `width`
- `work`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

