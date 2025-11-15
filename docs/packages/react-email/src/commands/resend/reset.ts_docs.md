# Documentation: reset.ts
**File Path:** `packages/react-email/src/commands/resend/reset.ts`
**Language:** typescript
**Size:** 232 bytes
**Lines:** 9
**Generated:** 2025-11-15T20:37:32.596874Z

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

- **Path:** `packages/react-email/src/commands/resend/reset.ts`
- **Name:** `reset.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 232 bytes (0.23 KB)
- **Lines of Code:** 9

---

## Original Source

```typescript
import logSymbols from 'log-symbols';
import { conf } from '../../utils/conf.js';

export async function resendReset() {
  conf.delete('resendApiKey');

  console.info(`${logSymbols.success} Resend API Key successfully deleted`);
}

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `resendReset()`

### Dependencies

This file imports/requires:

- `../../utils/conf.js`
- `log-symbols`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 15

- `Key`
- `Resend`
- `conf`
- `console`
- `delete`
- `deleted`
- `info`
- `log`
- `logSymbols`
- `resendApiKey`
- `resendReset`
- `success`
- `successfully`
- `symbols`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

