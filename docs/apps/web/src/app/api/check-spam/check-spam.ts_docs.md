# Documentation: check-spam.ts
**File Path:** `apps/web/src/app/api/check-spam/check-spam.ts`
**Language:** typescript
**Size:** 791 bytes
**Lines:** 29
**Generated:** 2025-11-15T20:37:32.829901Z

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

- **Path:** `apps/web/src/app/api/check-spam/check-spam.ts`
- **Name:** `check-spam.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 791 bytes (0.77 KB)
- **Lines of Code:** 29

---

## Original Source

```typescript
import { parsePointingTableRows } from '@/utils/spam-assassin/parse-pointing-table-rows';
import { sendToSpamd } from '@/utils/spam-assassin/send-to-spamd';

export async function checkSpam(html: string, plainText: string) {
  const response = await sendToSpamd(html, plainText);
  const tableRows = parsePointingTableRows(response);

  const filteredRows = tableRows.filter(
    (row) =>
      !row.description.toLowerCase().includes('header') &&
      !row.ruleName.includes('HEADER') &&
      row.pts !== 0,
  );

  const checks = filteredRows.map((row) => ({
    name: row.ruleName,
    description: row.description,
    points: row.pts,
  }));

  const points = checks.reduce((acc, check) => acc + check.points, 0);

  return {
    checks,
    isSpam: points >= 5.0,
    points,
  };
}

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `checkSpam()`
- `checks()`
- `filteredRows()`
- `points()`
- `response()`
- `tableRows()`

### Dependencies

This file imports/requires:

- `@/utils/spam-assassin/parse-pointing-table-rows`
- `@/utils/spam-assassin/send-to-spamd`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 34

- `acc`
- `assassin`
- `check`
- `checkSpam`
- `checks`
- `description`
- `filter`
- `filteredRows`
- `header`
- `html`
- `includes`
- `isSpam`
- `map`
- `name`
- `parse`
- `parsePointingTableRows`
- `plainText`
- `pointing`
- `points`
- `pts`
- `reduce`
- `response`
- `row`
- `rows`
- `ruleName`
- `send`
- `sendToSpamd`
- `spam`
- `spamd`
- `string`
- `table`
- `tableRows`
- `toLowerCase`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

