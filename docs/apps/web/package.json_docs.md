# Documentation: package.json
**File Path:** `apps/web/package.json`
**Language:** json
**Size:** 1,783 bytes
**Lines:** 62
**Generated:** 2025-11-15T20:37:32.793673Z

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

- **Path:** `apps/web/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,783 bytes (1.74 KB)
- **Lines of Code:** 62

---

## Original Source

```json
{
  "name": "web",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "test:watch": "vitest --bail 1",
    "test": "vitest run --bail 1",
    "components:dev": "email-dev dev -d ./components",
    "components:build": "email-dev build -d ./components"
  },
  "dependencies": {
    "@babel/parser": "7.27.0",
    "@babel/preset-typescript": "7.27.0",
    "@babel/traverse": "7.27.0",
    "@radix-ui/react-popover": "1.1.15",
    "@react-email/components": "workspace:*",
    "@react-email/render": "workspace:*",
    "@react-three/drei": "^9.120.3",
    "@react-three/fiber": "^9.0.0",
    "@responsive-email/react-email": "0.0.4",
    "@supabase/supabase-js": "2.49.4",
    "@vercel/analytics": "1.5.0",
    "email-dev": "workspace:*",
    "framer-motion": "12.23.22",
    "lucide-react": "^0.544.0",
    "next": "16.0.1",
    "prism-react-renderer": "2.4.1",
    "react": "^19",
    "react-dom": "^19",
    "resend": "4.3.0",
    "sonner": "2.0.3",
    "three": "^0.170.0",
    "vaul": "1.1.2"
  },
  "devDependencies": {
    "@next/env": "15.3.1",
    "@radix-ui/colors": "3.0.0",
    "@radix-ui/react-select": "2.2.6",
    "@radix-ui/react-slot": "1.2.3",
    "@radix-ui/react-tabs": "^1.1.0",
    "@radix-ui/react-tooltip": "1.2.8",
    "@react-email/preview-server": "workspace:*",
    "@types/babel__core": "7.20.5",
    "@types/babel__traverse": "7.20.7",
    "@types/node": "^22.0.0",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "autoprefixer": "10.4.21",
    "classnames": "2.5.1",
    "html-to-ast": "0.0.6",
    "postcss": "8.5.3",
    "tailwindcss": "3.4.3",
    "tsconfig": "workspace:*",
    "typescript": "5.8.3",
    "webpack": "5.99.6",
    "zod": "3.24.3"
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

**Total Unique Identifiers:** 65

- `analytics`
- `ast`
- `autoprefixer`
- `babel`
- `babel__core`
- `babel__traverse`
- `bail`
- `build`
- `classnames`
- `colors`
- `components`
- `dependencies`
- `dev`
- `devDependencies`
- `dom`
- `drei`
- `email`
- `env`
- `fiber`
- `framer`
- `html`
- `lucide`
- `motion`
- `name`
- `next`
- `node`
- `parser`
- `popover`
- `postcss`
- `preset`
- `preview`
- `prism`
- `private`
- `radix`
- `react`
- `render`
- `renderer`
- `resend`
- `responsive`
- `run`
- `scripts`
- `select`
- `server`
- `slot`
- `sonner`
- `start`
- `supabase`
- `tabs`
- `tailwindcss`
- `test`
- `three`
- `tooltip`
- `traverse`
- `tsconfig`
- `types`
- `typescript`
- `vaul`
- `vercel`
- `version`
- `vitest`
- `watch`
- `web`
- `webpack`
- `workspace`
- `zod`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

