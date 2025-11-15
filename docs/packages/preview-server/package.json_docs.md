# Documentation: package.json
**File Path:** `packages/preview-server/package.json`
**Language:** json
**Size:** 2,429 bytes
**Lines:** 81
**Generated:** 2025-11-15T20:37:31.755819Z

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

- **Path:** `packages/preview-server/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 2,429 bytes (2.37 KB)
- **Lines of Code:** 81

---

## Original Source

```json
{
  "name": "@react-email/preview-server",
  "version": "5.0.4",
  "description": "A live preview of your emails right in your browser.",
  "scripts": {
    "build": "tsx ./scripts/build-preview-server.mts",
    "caniemail:fetch": "tsx ./scripts/fill-caniemail-data.mts",
    "clean": "rm -rf dist",
    "dev": "tsx ./scripts/dev.mts",
    "dev:seed": "tsx ./scripts/seed.mts",
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "main": "./index.mjs",
  "dependencies": {
    "next": "16.0.1"
  },
  "devDependencies": {
    "@babel/core": "7.26.10",
    "@babel/parser": "7.27.0",
    "@babel/traverse": "7.27.0",
    "@lottiefiles/dotlottie-react": "0.13.3",
    "@radix-ui/colors": "3.0.0",
    "@radix-ui/react-collapsible": "1.1.12",
    "@radix-ui/react-dropdown-menu": "2.1.16",
    "@radix-ui/react-popover": "1.1.15",
    "@radix-ui/react-slot": "1.2.3",
    "@radix-ui/react-tabs": "1.1.13",
    "@radix-ui/react-toggle": "1.1.10",
    "@radix-ui/react-toggle-group": "1.1.11",
    "@radix-ui/react-tooltip": "1.2.8",
    "@react-email/components": "workspace:*",
    "@react-email/tailwind": "workspace:2.0.1",
    "@types/babel__core": "7.20.5",
    "@types/babel__traverse": "7.20.7",
    "@types/css-tree": "2.3.10",
    "@types/fs-extra": "11.0.1",
    "@types/mime-types": "2.1.4",
    "@types/node": "22.14.1",
    "@types/normalize-path": "3.0.2",
    "@types/react": "19.0.10",
    "@types/react-dom": "19.0.4",
    "@types/webpack": "5.28.5",
    "autoprefixer": "10.4.21",
    "clsx": "2.1.1",
    "colorjs.io": "0.5.2",
    "esbuild": "0.25.10",
    "framer-motion": "12.23.22",
    "log-symbols": "4.1.0",
    "module-punycode": "npm:punycode@2.3.1",
    "next-safe-action": "8.0.11",
    "node-html-parser": "7.0.1",
    "ora": "5.4.1",
    "postcss": "8.5.3",
    "pretty-bytes": "6.1.1",
    "prism-react-renderer": "2.4.1",
    "react": "19.0.0",
    "react-dom": "19.0.0",
    "resend": "6.4.0",
    "sharp": "0.34.4",
    "socket.io-client": "4.8.1",
    "sonner": "2.0.3",
    "source-map-js": "1.2.1",
    "stacktrace-parser": "0.1.11",
    "tailwind-merge": "3.2.0",
    "tailwindcss": "3.4.0",
    "typescript": "5.8.3",
    "use-debounce": "10.0.4",
    "zod": "4.1.12"
  },
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/resend/react-email.git",
    "directory": "packages/preview-server"
  },
  "publishConfig": {
    "access": "public"
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

**Total Unique Identifiers:** 113

- `access`
- `action`
- `autoprefixer`
- `babel`
- `babel__core`
- `babel__traverse`
- `browser`
- `build`
- `bytes`
- `caniemail`
- `clean`
- `client`
- `clsx`
- `collapsible`
- `colorjs`
- `colors`
- `com`
- `components`
- `core`
- `css`
- `data`
- `debounce`
- `dependencies`
- `description`
- `dev`
- `devDependencies`
- `directory`
- `dist`
- `dom`
- `dotlottie`
- `dropdown`
- `email`
- `emails`
- `esbuild`
- `extra`
- `fetch`
- `fill`
- `framer`
- `git`
- `github`
- `group`
- `html`
- `https`
- `index`
- `license`
- `live`
- `log`
- `lottiefiles`
- `main`
- `map`
- `menu`
- `merge`
- `mime`
- `mjs`
- `module`
- `motion`
- `mts`
- `name`
- `next`
- `node`
- `normalize`
- `npm`
- `ora`
- `packages`
- `parser`
- `path`
- `popover`
- `postcss`
- `pretty`
- `preview`
- `prism`
- `public`
- `publishConfig`
- `punycode`
- `radix`
- `react`
- `renderer`
- `repository`
- `resend`
- `right`
- `run`
- `safe`
- `scripts`
- `seed`
- `server`
- `sharp`
- `slot`
- `socket`
- `sonner`
- `source`
- `stacktrace`
- `symbols`
- `tabs`
- `tailwind`
- `tailwindcss`
- `test`
- `toggle`
- `tooltip`
- `traverse`
- `tree`
- `tsx`
- `type`
- `types`
- `typescript`
- `url`
- `use`
- `version`
- `vitest`
- `watch`
- `webpack`
- `workspace`
- `your`
- `zod`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

