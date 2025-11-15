# Documentation: package.json
**File Path:** `benchmarks/tailwind-component/package.json`
**Language:** json
**Size:** 1,205 bytes
**Lines:** 38
**Generated:** 2025-11-15T20:37:33.229875Z

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

- **Path:** `benchmarks/tailwind-component/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 1,205 bytes (1.18 KB)
- **Lines of Code:** 38

---

## Original Source

```json
{
  "name": "@benchmarks/tailwind-component",
  "private": true,
  "main": "dist/benchmark.js",
  "version": "0.0.0",
  "scripts": {
    "with-vs-without": "tsx ./src/benchmark-with-vs-without",
    "0.0.17-vs-local": "tsx --max-old-space-size=256 ./src/benchmark-0.0.17-vs-local-version",
    "0.0.12-vs-local": "tsx ./src/benchmark-0.0.12-vs-local-version",
    "flamegraph-render-tailwind": "tsx --prof ./src/tailwind-render && node --prof-process --preprocess -j isolate*.log | flamebearer"
  },
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/resend/react-email.git",
    "directory": "benchmarks/tailwind-component"
  },
  "engines": {
    "node": ">=22.0.0"
  },
  "dependencies": {
    "@react-email/components": "workspace:*",
    "@react-email/render": "workspace:*",
    "@react-email/tailwind": "workspace:*",
    "react": "19.0.0",
    "react-dom": "19.0.0",
    "tailwind-0.0.12": "npm:@react-email/tailwind@0.0.12",
    "tailwind-0.0.17": "npm:@react-email/tailwind@0.0.17",
    "tinybench": "3.1.0"
  },
  "devDependencies": {
    "@biomejs/biome": "2.0.0",
    "flamebearer": "1.1.3",
    "tsconfig": "workspace:*",
    "typescript": "5.8.3"
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

**Total Unique Identifiers:** 51

- `benchmark`
- `benchmarks`
- `biome`
- `biomejs`
- `com`
- `component`
- `components`
- `dependencies`
- `devDependencies`
- `directory`
- `dist`
- `dom`
- `email`
- `engines`
- `flamebearer`
- `flamegraph`
- `git`
- `github`
- `https`
- `isolate`
- `license`
- `local`
- `log`
- `main`
- `max`
- `name`
- `node`
- `npm`
- `old`
- `preprocess`
- `private`
- `process`
- `prof`
- `react`
- `render`
- `repository`
- `resend`
- `scripts`
- `size`
- `space`
- `src`
- `tailwind`
- `tinybench`
- `tsconfig`
- `tsx`
- `type`
- `typescript`
- `url`
- `version`
- `without`
- `workspace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

