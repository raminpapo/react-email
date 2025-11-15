# Documentation: route.ts
**File Path:** `apps/web/src/app/api/check-spam/route.ts`
**Language:** typescript
**Size:** 806 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:32.831224Z

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

- **Path:** `apps/web/src/app/api/check-spam/route.ts`
- **Name:** `route.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 806 bytes (0.79 KB)
- **Lines of Code:** 33

---

## Original Source

```typescript
import { type NextRequest, NextResponse } from 'next/server';
import { ZodError, z } from 'zod';
import { checkSpam } from './check-spam';

export function OPTIONS() {
  return Promise.resolve(NextResponse.json({}));
}

const bodySchema = z.object({
  html: z.string(),
  plainText: z.string(),
});

export async function POST(req: NextRequest) {
  try {
    const { html, plainText } = bodySchema.parse(await req.json());

    return NextResponse.json(await checkSpam(html, plainText));
  } catch (exception) {
    if (exception instanceof Error) {
      return NextResponse.json(
        { error: exception.message },
        { status: exception instanceof ZodError ? 400 : 500 },
      );
    }

    return NextResponse.json(
      { error: 'Something went wrong' },
      { status: 500 },
    );
  }
}

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `OPTIONS()`
- `POST()`
- `bodySchema()`

### Type Definitions

- `NextRequest`

### Dependencies

This file imports/requires:

- `./check-spam`
- `next/server`
- `zod`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 28

- `Error`
- `NextRequest`
- `NextResponse`
- `Promise`
- `Something`
- `ZodError`
- `bodySchema`
- `check`
- `checkSpam`
- `error`
- `exception`
- `html`
- `json`
- `message`
- `next`
- `object`
- `parse`
- `plainText`
- `req`
- `resolve`
- `server`
- `spam`
- `status`
- `string`
- `type`
- `went`
- `wrong`
- `zod`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

