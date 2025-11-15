# Documentation: turbo.json
**File Path:** `turbo.json`
**Language:** json
**Size:** 1,320 bytes
**Lines:** 57
**Generated:** 2025-11-15T20:37:31.440561Z

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

- **Path:** `turbo.json`
- **Name:** `turbo.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,320 bytes (1.29 KB)
- **Lines of Code:** 57

---

## Original Source

```json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["**/.env.*local", "pnpm-lock.yaml"],
  "globalEnv": [
    "SUPABASE_URL",
    "SUPABASE_ANON_KEY",
    "SUPABASE_TABLE_NAME",
    "SPAM_ASSASSIN_HOST",
    "SPAM_ASSASSIN_PORT"
  ],
  "tasks": {
    "build": {
      "dependsOn": ["^build", "^postbuild"],
      "outputs": ["dist/**"]
    },
    "postbuild": {
      "dependsOn": ["build"],
      "cache": false
    },
    "web#build": {
      "dependsOn": ["^build", "^postbuild"],
      "env": [
        "RESEND_API_KEY",
        "NEXT_PUBLIC_SUPABASE_URL",
        "NEXT_PUBLIC_SUPABASE_ANON_KEY"
      ],
      "outputs": [".next/**", "!.next/cache/**"]
    },
    "@react-email/preview-server#build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!.next/cache/**"]
    },
    "demo#build": {
      "dependsOn": ["^build", "^postbuild"],
      "outputs": [".react-email/**", "!.react-email/.next/cache/**"]
    },
    "react-email#build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "lint": {},
    "//#format": {},
    "//#format:check": {},
    "test": {
      "dependsOn": ["^build"]
    },
    "test:watch": {
      "cache": false
    },
    "dev": {
      "dependsOn": ["^build"],
      "cache": false,
      "persistent": true
    }
  }
}

```

---

## Overview

This is a JSON configuration or data file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 40

- `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- `NEXT_PUBLIC_SUPABASE_URL`
- `RESEND_API_KEY`
- `SPAM_ASSASSIN_HOST`
- `SPAM_ASSASSIN_PORT`
- `SUPABASE_ANON_KEY`
- `SUPABASE_TABLE_NAME`
- `SUPABASE_URL`
- `build`
- `cache`
- `check`
- `demo`
- `dependsOn`
- `dev`
- `dist`
- `email`
- `env`
- `format`
- `globalDependencies`
- `globalEnv`
- `https`
- `json`
- `lint`
- `local`
- `lock`
- `next`
- `outputs`
- `persistent`
- `pnpm`
- `postbuild`
- `preview`
- `react`
- `schema`
- `server`
- `tasks`
- `test`
- `turbo`
- `watch`
- `web`
- `yaml`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

