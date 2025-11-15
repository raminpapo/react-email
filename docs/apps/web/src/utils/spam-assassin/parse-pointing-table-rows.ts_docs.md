# Documentation: parse-pointing-table-rows.ts
**File Path:** `apps/web/src/utils/spam-assassin/parse-pointing-table-rows.ts`
**Language:** typescript
**Size:** 2,055 bytes
**Lines:** 78
**Generated:** 2025-11-15T20:37:32.814445Z

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

- **Path:** `apps/web/src/utils/spam-assassin/parse-pointing-table-rows.ts`
- **Name:** `parse-pointing-table-rows.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,055 bytes (2.01 KB)
- **Lines of Code:** 78

---

## Original Source

```typescript
export const parsePointingTableRows = (response: string) => {
  const tableHeader =
    /pts\s+rule\s+name\s+description\s+(?<ptsWidth>-+) (?<ruleNameWidth>-+) (?<descriptionWidth>-+) *(?:\r\n|\n|\r)*/;
  const tableStartMatch = response.match(tableHeader);

  if (
    tableStartMatch === null ||
    tableStartMatch.index === undefined ||
    tableStartMatch.groups === undefined
  ) {
    throw new Error('Could not find spam checking points table');
  }

  const ptsWidth = tableStartMatch.groups.ptsWidth!.length;
  const columnsRegex = new RegExp(
    `^(?<pts>.{${ptsWidth}}) (?<ruleName>.+?) (?<description>.+}|.+$)`,
  );

  interface Row {
    pts: number;
    ruleName: string;
    description: string;
  }

  const rows: Row[] = [];

  const responseFromTableStart = response.slice(
    tableStartMatch.index + tableStartMatch[0].length,
  );
  let currentRow: Row | undefined;
  for (const line of responseFromTableStart.split(/\r\n|\n|\r/)) {
    if (line.trim().length === 0) break;

    const match = line.match(columnsRegex);

    // This means the description column was done with multi columns.
    if (currentRow && line.startsWith('  ')) {
      currentRow.description += ` ${line.trimStart()}`;
      continue;
    }

    if (match?.groups === undefined) {
      throw new Error('Could not match the columns in the row', {
        cause: {
          line,
          match,
        },
      });
    }
    const pts = match.groups.pts!;
    const ruleName = match.groups.ruleName!.trim();
    const description = match.groups.description!;

    if (currentRow) {
      rows.push(currentRow);
    }
    const parsedPoints = Number.parseFloat(pts);
    if (Number.isNaN(parsedPoints)) {
      throw new Error('could not parse points to insert into rows array', {
        cause: {
          line,
          match,
        },
      });
    }
    currentRow = {
      pts: parsedPoints,
      ruleName: ruleName.trim(),
      description: description.trim(),
    };
  }
  if (currentRow) {
    rows.push(currentRow);
  }

  return rows;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `columnsRegex()`
- `description()`
- `match()`
- `parsePointingTableRows()`
- `parsedPoints()`
- `pts()`
- `ptsWidth()`
- `responseFromTableStart()`
- `ruleName()`
- `tableHeader()`
- `tableStartMatch()`

### Interfaces

- `Row`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 53

- `Error`
- `Number`
- `RegExp`
- `Row`
- `array`
- `cause`
- `checking`
- `column`
- `columns`
- `columnsRegex`
- `currentRow`
- `description`
- `descriptionWidth`
- `done`
- `find`
- `groups`
- `index`
- `insert`
- `interface`
- `into`
- `isNaN`
- `length`
- `line`
- `match`
- `means`
- `multi`
- `name`
- `number`
- `parse`
- `parseFloat`
- `parsePointingTableRows`
- `parsedPoints`
- `points`
- `pts`
- `ptsWidth`
- `push`
- `response`
- `responseFromTableStart`
- `row`
- `rows`
- `rule`
- `ruleName`
- `ruleNameWidth`
- `slice`
- `spam`
- `split`
- `startsWith`
- `string`
- `table`
- `tableHeader`
- `tableStartMatch`
- `trim`
- `trimStart`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

