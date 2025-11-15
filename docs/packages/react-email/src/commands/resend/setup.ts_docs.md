# Documentation: setup.ts
**File Path:** `packages/react-email/src/commands/resend/setup.ts`
**Language:** typescript
**Size:** 948 bytes
**Lines:** 30
**Generated:** 2025-11-15T20:37:32.597956Z

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

- **Path:** `packages/react-email/src/commands/resend/setup.ts`
- **Name:** `setup.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 948 bytes (0.93 KB)
- **Lines of Code:** 30

---

## Original Source

```typescript
import logSymbols from 'log-symbols';
import prompts from 'prompts';
import { conf } from '../../utils/conf.js';
import { styleText } from '../../utils/style-text.js';

export async function resendSetup() {
  const previousValue = conf.get('resendApiKey');
  if (typeof previousValue === 'string' && previousValue.length > 0) {
    console.info(
      `You already have a Resend API Key configured (${styleText('grey', previousValue.slice(0, 11))}...), continuing will replace it.`,
    );
  }

  const { apiKey } = await prompts({
    type: 'password',
    name: 'apiKey',
    message: 'Enter your API Key (make sure it has "Full Access")',
  });

  if (apiKey?.trim().length > 0) {
    conf.set('resendApiKey', apiKey);
    console.info(
      `${logSymbols.success} Resend integration successfully set up`,
    );
    console.info(
      `You can always remove it with ${styleText('green', 'npx react-email@latest resend reset')}`,
    );
  }
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `previousValue()`
- `resendSetup()`

### Dependencies

This file imports/requires:

- `../../utils/conf.js`
- `../../utils/style-text.js`
- `log-symbols`
- `prompts`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 51

- `Access`
- `Enter`
- `Full`
- `Key`
- `Resend`
- `You`
- `already`
- `always`
- `apiKey`
- `conf`
- `configured`
- `console`
- `continuing`
- `email`
- `get`
- `green`
- `grey`
- `info`
- `integration`
- `latest`
- `length`
- `log`
- `logSymbols`
- `make`
- `message`
- `name`
- `npx`
- `password`
- `previousValue`
- `prompts`
- `react`
- `remove`
- `replace`
- `resend`
- `resendApiKey`
- `resendSetup`
- `reset`
- `set`
- `slice`
- `string`
- `style`
- `styleText`
- `success`
- `successfully`
- `sure`
- `symbols`
- `text`
- `trim`
- `type`
- `utils`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

