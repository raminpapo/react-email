# Documentation: register-spinner-autostopping.ts
**File Path:** `packages/preview-server/src/utils/register-spinner-autostopping.ts`
**Language:** typescript
**Size:** 553 bytes
**Lines:** 29
**Generated:** 2025-11-15T20:37:32.029453Z

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

- **Path:** `packages/preview-server/src/utils/register-spinner-autostopping.ts`
- **Name:** `register-spinner-autostopping.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 553 bytes (0.54 KB)
- **Lines of Code:** 29

---

## Original Source

```typescript
import logSymbols from 'log-symbols';
import type { Ora } from 'ora';

const spinners = new Set<Ora>();

process.on('SIGINT', () => {
  spinners.forEach((spinner) => {
    if (spinner.isSpinning) {
      spinner.stop();
    }
  });
});

process.on('exit', (code) => {
  if (code !== 0) {
    spinners.forEach((spinner) => {
      if (spinner.isSpinning) {
        spinner.stopAndPersist({
          symbol: logSymbols.error,
        });
      }
    });
  }
});

export const registerSpinnerAutostopping = (spinner: Ora) => {
  spinners.add(spinner);
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `registerSpinnerAutostopping()`
- `spinners()`

### Dependencies

This file imports/requires:

- `log-symbols`
- `ora`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 20

- `Ora`
- `Set`
- `add`
- `code`
- `error`
- `exit`
- `forEach`
- `isSpinning`
- `log`
- `logSymbols`
- `ora`
- `process`
- `registerSpinnerAutostopping`
- `spinner`
- `spinners`
- `stop`
- `stopAndPersist`
- `symbol`
- `symbols`
- `type`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

