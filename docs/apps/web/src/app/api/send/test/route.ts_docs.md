# Documentation: route.ts
**File Path:** `apps/web/src/app/api/send/test/route.ts`
**Language:** typescript
**Size:** 1,967 bytes
**Lines:** 70
**Generated:** 2025-11-15T20:37:32.825890Z

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

- **Path:** `apps/web/src/app/api/send/test/route.ts`
- **Name:** `route.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,967 bytes (1.92 KB)
- **Lines of Code:** 70

---

## Original Source

```typescript
import { createClient } from '@supabase/supabase-js';
import { type NextRequest, NextResponse } from 'next/server';
import { Resend } from 'resend';
import { z } from 'zod';

export function OPTIONS() {
  return Promise.resolve(NextResponse.json({}));
}

const bodySchema = z.object({
  to: z.string(),
  subject: z.string(),
  html: z.string(),
});

export async function POST(req: NextRequest) {
  const resend = new Resend(process.env.RESEND_API_KEY);
  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseKey = process.env.SUPABASE_ANON_KEY;
  const supabaseTable = process.env.SUPABASE_TABLE_NAME;
  if (!supabaseUrl || !supabaseKey || !supabaseTable) {
    throw new Error('Supabase URL and key are required');
  }

  const supabase = createClient(supabaseUrl, supabaseKey);

  try {
    const { to, subject, html } = bodySchema.parse(await req.json());

    const ip = req.headers.get('x-vercel-forwarded-for');
    const latitude = req.headers.get('x-vercel-ip-latitude');
    const longitude = req.headers.get('x-vercel-ip-longitude');
    const city = req.headers.get('x-vercel-ip-city');
    const country = req.headers.get('x-vercel-ip-country');
    const countryRegion = req.headers.get('x-vercel-ip-country-region');

    const savePromise = supabase.from(supabaseTable).insert({
      to: [to],
      subject,
      html,
      ip,
      latitude,
      longitude,
      city,
      country,
      country_region: countryRegion,
    });

    const sendPromise = resend.emails.send({
      from: 'React Email <preview@react.email>',
      to: [to],
      subject,
      html,
    });

    await Promise.all([savePromise, sendPromise]);

    return NextResponse.json({ message: 'Test email sent' });
  } catch (error) {
    if (error instanceof Error) {
      return NextResponse.json({ error: error.message }, { status: 500 });
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

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `OPTIONS()`
- `POST()`
- `bodySchema()`
- `city()`
- `country()`
- `countryRegion()`
- `ip()`
- `latitude()`
- `longitude()`
- `resend()`
- `savePromise()`
- `sendPromise()`
- `supabase()`
- `supabaseKey()`
- `supabaseTable()`
- `supabaseUrl()`

### Type Definitions

- `NextRequest`

### Dependencies

This file imports/requires:

- `@supabase/supabase-js`
- `next/server`
- `resend`
- `zod`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 63

- `Email`
- `Error`
- `NextRequest`
- `NextResponse`
- `Promise`
- `RESEND_API_KEY`
- `React`
- `Resend`
- `SUPABASE_ANON_KEY`
- `SUPABASE_TABLE_NAME`
- `SUPABASE_URL`
- `Something`
- `Supabase`
- `Test`
- `all`
- `bodySchema`
- `city`
- `country`
- `countryRegion`
- `country_region`
- `createClient`
- `email`
- `emails`
- `env`
- `error`
- `forwarded`
- `get`
- `headers`
- `html`
- `insert`
- `json`
- `key`
- `latitude`
- `longitude`
- `message`
- `next`
- `object`
- `parse`
- `preview`
- `process`
- `react`
- `region`
- `req`
- `required`
- `resend`
- `resolve`
- `savePromise`
- `send`
- `sendPromise`
- `sent`
- `server`
- `status`
- `string`
- `subject`
- `supabase`
- `supabaseKey`
- `supabaseTable`
- `supabaseUrl`
- `type`
- `vercel`
- `went`
- `wrong`
- `zod`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

