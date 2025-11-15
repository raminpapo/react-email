# Documentation: tsconfig.json
**File Path:** `packages/tailwind/integrations/nextjs/tsconfig.json`
**Language:** json
**Size:** 602 bytes
**Lines:** 28
**Generated:** 2025-11-15T20:37:32.371666Z

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

- **Path:** `packages/tailwind/integrations/nextjs/tsconfig.json`
- **Name:** `tsconfig.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 602 bytes (0.59 KB)
- **Lines of Code:** 28

---

## Original Source

```json
{
  "compilerOptions": {
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    },
    "target": "ES2017"
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}

```

---

## Overview

This is a JSON configuration or data file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 31

- `ES2017`
- `allowJs`
- `bundler`
- `compilerOptions`
- `dom`
- `env`
- `esModuleInterop`
- `esnext`
- `exclude`
- `include`
- `incremental`
- `isolatedModules`
- `iterable`
- `jsx`
- `lib`
- `module`
- `moduleResolution`
- `name`
- `next`
- `noEmit`
- `node_modules`
- `paths`
- `plugins`
- `preserve`
- `resolveJsonModule`
- `skipLibCheck`
- `src`
- `strict`
- `target`
- `tsx`
- `types`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

