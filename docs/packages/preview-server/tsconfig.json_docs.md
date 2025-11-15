# Documentation: tsconfig.json
**File Path:** `packages/preview-server/tsconfig.json`
**Language:** json
**Size:** 1,184 bytes
**Lines:** 48
**Generated:** 2025-11-15T20:37:31.760712Z

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

- **Path:** `packages/preview-server/tsconfig.json`
- **Name:** `tsconfig.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,184 bytes (1.16 KB)
- **Lines of Code:** 48

---

## Original Source

```json
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "display": "Next.js",
  "compilerOptions": {
    "composite": false,
    "downlevelIteration": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "inlineSources": false,
    "isolatedModules": true,
    "moduleResolution": "node",
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "preserveWatchOutput": true,
    "skipLibCheck": true,
    "strictNullChecks": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "allowJs": true,
    "declaration": false,
    "declarationMap": false,
    "incremental": false,
    "jsx": "react-jsx",
    "lib": ["dom", "dom.iterable", "esnext", "ESNext.AsyncIterable"],
    "noEmit": true,
    "strict": false,
    "target": "ESNext",
    "module": "CommonJS",
    "noUncheckedIndexedAccess": true,
    "resolveJsonModule": true,
    "types": ["vitest/globals"],
    "outDir": "dist"
  },
  "include": [
    "next-env.d.ts",
    "tailwind-internals.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts",
    "next.config.mjs"
  ],
  "exclude": [".next", "dist", "node_modules"]
}

```

---

## Overview

This is a JSON configuration or data file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 59

- `AsyncIterable`
- `CommonJS`
- `ESNext`
- `Next`
- `allowJs`
- `compilerOptions`
- `composite`
- `config`
- `declaration`
- `declarationMap`
- `dev`
- `display`
- `dist`
- `dom`
- `downlevelIteration`
- `env`
- `esModuleInterop`
- `esnext`
- `exclude`
- `forceConsistentCasingInFileNames`
- `globals`
- `https`
- `include`
- `incremental`
- `inlineSources`
- `internals`
- `isolatedModules`
- `iterable`
- `json`
- `jsx`
- `lib`
- `mjs`
- `module`
- `moduleResolution`
- `name`
- `next`
- `noEmit`
- `noUncheckedIndexedAccess`
- `noUnusedLocals`
- `noUnusedParameters`
- `node`
- `node_modules`
- `org`
- `outDir`
- `plugins`
- `preserveWatchOutput`
- `react`
- `resolveJsonModule`
- `schema`
- `schemastore`
- `skipLibCheck`
- `strict`
- `strictNullChecks`
- `tailwind`
- `target`
- `tsconfig`
- `tsx`
- `types`
- `vitest`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

