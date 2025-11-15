# Documentation: sanitize-non-inlinable-classes.spec.ts.snap
**File Path:** `packages/tailwind/src/utils/css/__snapshots__/sanitize-non-inlinable-classes.spec.ts.snap`
**Language:** Unknown
**Size:** 2,176 bytes
**Lines:** 8
**Generated:** 2025-11-15T20:37:32.487268Z

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

- **Path:** `packages/tailwind/src/utils/css/__snapshots__/sanitize-non-inlinable-classes.spec.ts.snap`
- **Name:** `sanitize-non-inlinable-classes.spec.ts.snap`
- **Extension:** `.snap`
- **Language:** Unknown
- **Size:** 2,176 bytes (2.12 KB)
- **Lines of Code:** 8

---

## Original Source

```
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`sanitizeNonInlinableClasses() > should css nesting in hover pseudo styles 1`] = `"/*! tailwindcss v4.1.12 | MIT License | https://tailwindcss.com */@layer theme,base,components,utilities;@layer theme{:root,:host{--color-sky-600: oklch(58.8% 0.158 241.966)!important;--color-gray-100: oklch(96.7% 0.003 264.542)!important}}@layer utilities{.hover_text-sky-600{&:hover{@media (hover:hover){color:var(--color-sky-600)!important}}}.sm_focus_outline-none{@media (width>=40rem){&:focus{--tw-outline-style: none!important;outline-style:none!important}}}.md_hover_bg-gray-100{@media (width>=48rem){&:hover{@media (hover:hover){background-color:var(--color-gray-100)!important}}}}.lg_focus_underline{@media (width>=64rem){&:focus{text-decoration-line:underline!important}}}}"`;

exports[`sanitizeNonInlinableClasses() > should handle rules that can be inlined 1`] = `"/*! tailwindcss v4.1.12 | MIT License | https://tailwindcss.com */@layer theme,base,components,utilities;@layer theme{:root,:host{--color-red-300: oklch(80.8% 0.114 19.571)!important;--color-gray-900: oklch(21% 0.034 264.665)!important;--text-lg: 1.125rem!important;--text-lg--line-height: calc(1.75 / 1.125)!important}}@layer utilities{.bg-gray-900{background-color:var(--color-gray-900)}.text-lg{font-size:var(--text-lg);line-height:var(--tw-leading, var(--text-lg--line-height))}.text-red-300{color:var(--color-red-300)}}"`;

exports[`sanitizeNonInlinableClasses() > shuold work with basic media query rules 1`] = `"/*! tailwindcss v4.1.12 | MIT License | https://tailwindcss.com */@layer theme,base,components,utilities;@layer theme{:root,:host{--spacing: 0.25rem!important;--container-lg: 32rem!important;--radius-lg: 0.5rem!important}}@layer utilities{.sm_mx-auto{@media (width>=40rem){margin-inline:auto!important}}.sm_max-w-lg{@media (width>=40rem){max-width:var(--container-lg)!important}}.sm_rounded-lg{@media (width>=40rem){border-radius:var(--radius-lg)!important}}.md_px-10{@media (width>=48rem){padding-inline:calc(var(--spacing)*10)!important}}.md_py-12{@media (width>=48rem){padding-block:calc(var(--spacing)*12)!important}}}"`;

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 72

- `License`
- `Snapshot`
- `Vitest`
- `auto`
- `background`
- `base`
- `basic`
- `block`
- `border`
- `calc`
- `color`
- `com`
- `components`
- `container`
- `css`
- `decoration`
- `dev`
- `exports`
- `focus`
- `font`
- `gray`
- `guide`
- `handle`
- `height`
- `host`
- `hover`
- `hover_text`
- `html`
- `https`
- `important`
- `inline`
- `inlined`
- `layer`
- `leading`
- `lg_focus_underline`
- `line`
- `margin`
- `max`
- `md_hover_bg`
- `md_px`
- `md_py`
- `media`
- `nesting`
- `oklch`
- `outline`
- `padding`
- `pseudo`
- `query`
- `radius`
- `red`
- `root`
- `rules`
- `sanitizeNonInlinableClasses`
- `shuold`
- `size`
- `sky`
- `sm_focus_outline`
- `sm_max`
- `sm_mx`
- `sm_rounded`
- `snapshot`
- `spacing`
- `style`
- `styles`
- `tailwindcss`
- `text`
- `theme`
- `underline`
- `utilities`
- `vitest`
- `width`
- `work`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

