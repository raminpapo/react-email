# Documentation: globals.css
**File Path:** `apps/web/src/styles/globals.css`
**Language:** css
**Size:** 492 bytes
**Lines:** 31
**Generated:** 2025-11-15T20:37:32.799768Z

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

- **Path:** `apps/web/src/styles/globals.css`
- **Name:** `globals.css`
- **Extension:** `.css`
- **Language:** css
- **Size:** 492 bytes (0.48 KB)
- **Lines of Code:** 31

---

## Original Source

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

[color-scheme="dark"] {
  color-scheme: dark;
}

@media (prefers-reduced-motion: no-preference) {
  * {
    scroll-behavior: smooth;
  }
}

#root,
#__next {
  isolation: isolate;
}

.text-gradient {
  background: linear-gradient(
    to right bottom,
    #fff 30%,
    color-mix(in srgb, #fff 50%, transparent)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: unset;
}

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 33

- `__next`
- `background`
- `base`
- `behavior`
- `bottom`
- `clip`
- `color`
- `components`
- `dark`
- `fff`
- `fill`
- `gradient`
- `isolate`
- `isolation`
- `linear`
- `media`
- `mix`
- `motion`
- `preference`
- `prefers`
- `reduced`
- `right`
- `root`
- `scheme`
- `scroll`
- `smooth`
- `srgb`
- `tailwind`
- `text`
- `transparent`
- `unset`
- `utilities`
- `webkit`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

