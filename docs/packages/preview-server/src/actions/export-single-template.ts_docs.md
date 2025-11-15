# Documentation: export-single-template.ts
**File Path:** `packages/preview-server/src/actions/export-single-template.ts`
**Language:** typescript
**Size:** 869 bytes
**Lines:** 37
**Generated:** 2025-11-15T20:37:31.779293Z

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

- **Path:** `packages/preview-server/src/actions/export-single-template.ts`
- **Name:** `export-single-template.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 869 bytes (0.85 KB)
- **Lines of Code:** 37

---

## Original Source

```typescript
'use server';

import { Resend } from 'resend';
import { z } from 'zod';
import { resendApiKey } from '../app/env';
import { baseActionClient } from './safe-action';

export const exportSingleTemplate = baseActionClient
  .metadata({
    actionName: 'exportSingleTemplate',
  })
  .inputSchema(
    z.object({
      name: z.string(),
      html: z.string(),
    }),
  )
  .action(async ({ parsedInput }) => {
    const resend = new Resend(resendApiKey);

    const response = await resend.templates.create({
      name: parsedInput.name,
      html: parsedInput.html,
    });

    if (response.error) {
      console.error('Error creating single template', response.error);
      return { name: parsedInput.name, status: 'failed' as const };
    }

    return {
      name: parsedInput.name,
      status: 'succeeded' as const,
      id: response.data.id,
    };
  });

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `exportSingleTemplate()`
- `resend()`
- `response()`

### Dependencies

This file imports/requires:

- `../app/env`
- `./safe-action`
- `resend`
- `zod`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 33

- `Error`
- `Resend`
- `action`
- `actionName`
- `app`
- `baseActionClient`
- `console`
- `create`
- `creating`
- `data`
- `env`
- `error`
- `exportSingleTemplate`
- `failed`
- `html`
- `inputSchema`
- `metadata`
- `name`
- `object`
- `parsedInput`
- `resend`
- `resendApiKey`
- `response`
- `safe`
- `server`
- `single`
- `status`
- `string`
- `succeeded`
- `template`
- `templates`
- `use`
- `zod`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

