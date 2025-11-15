# Documentation: check-spam.spec.tsx.snap
**File Path:** `apps/web/src/app/api/check-spam/__snapshots__/check-spam.spec.tsx.snap`
**Language:** Unknown
**Size:** 674 bytes
**Lines:** 34
**Generated:** 2025-11-15T20:37:32.832563Z

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

- **Path:** `apps/web/src/app/api/check-spam/__snapshots__/check-spam.spec.tsx.snap`
- **Name:** `check-spam.spec.tsx.snap`
- **Extension:** `.snap`
- **Language:** Unknown
- **Size:** 674 bytes (0.66 KB)
- **Lines of Code:** 34

---

## Original Source

```
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`checkSpam() > with most spammy email 1`] = `
{
  "checks": [
    {
      "description": "BODY: Money back guarantee",
      "name": "MONEY_BACK",
      "points": 2.5,
    },
    {
      "description": "BODY: HTML and text parts are different",
      "name": "MPART_ALT_DIFF",
      "points": 0.7,
    },
    {
      "description": "Refers to an erectile drug",
      "name": "DRUGS_ERECTILE",
      "points": 2.2,
    },
  ],
  "isSpam": true,
  "points": 5.4,
}
`;

exports[`checkSpam() > with stripe email template using true base url 1`] = `
{
  "checks": [],
  "isSpam": false,
  "points": 0,
}
`;

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 35

- `DRUGS_ERECTILE`
- `MONEY_BACK`
- `MPART_ALT_DIFF`
- `Money`
- `Refers`
- `Snapshot`
- `Vitest`
- `back`
- `base`
- `checkSpam`
- `checks`
- `description`
- `dev`
- `different`
- `drug`
- `email`
- `erectile`
- `exports`
- `guarantee`
- `guide`
- `html`
- `https`
- `isSpam`
- `most`
- `name`
- `parts`
- `points`
- `snapshot`
- `spammy`
- `stripe`
- `template`
- `text`
- `url`
- `using`
- `vitest`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

