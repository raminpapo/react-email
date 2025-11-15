# Documentation: integrations.spec.ts
**File Path:** `packages/tailwind/integrations/integrations.spec.ts`
**Language:** typescript
**Size:** 1,342 bytes
**Lines:** 49
**Generated:** 2025-11-15T20:37:32.365147Z

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

- **Path:** `packages/tailwind/integrations/integrations.spec.ts`
- **Name:** `integrations.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,342 bytes (1.31 KB)
- **Lines of Code:** 49

---

## Original Source

```typescript
import path from 'node:path';
import shell from 'shelljs';

const $ = (command: string, cwd: string = path.resolve(__dirname, '..')) => {
  const executionResult = shell.exec(command, {
    cwd,
    fatal: true,
    silent: true,
  });
  if (executionResult.code !== 0) {
    process.stdout.write(executionResult.stderr);
    process.stderr.write(executionResult.stderr);
  }
  expect(
    executionResult.code,
    `Expected command "${command}" to work properly but it returned a non-zero exit code`,
  ).toBe(0);
};

describe('integrations', () => {
  beforeAll(() => {
    const packageLocation = path.resolve(__dirname, '../');
    $('yalc installations clean @react-email/tailwind', packageLocation);
    $('yalc publish', packageLocation);
  });

  const integrationsLocation = __dirname;

  test(
    "Tailwind works on the Next App's build process",
    { timeout: 65_000 },
    () => {
      const nextAppLocation = path.resolve(integrationsLocation, 'nextjs');
      $('npm install', nextAppLocation);
      $('npm run build', nextAppLocation);
    },
  );

  test(
    "Tailwind works on the Vite App's build process",
    { timeout: 15_000 },
    () => {
      const viteAppLocation = path.resolve(integrationsLocation, 'vite');
      $('npm install', viteAppLocation);
      $('npm run build', viteAppLocation);
    },
  );
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `$()`
- `executionResult()`
- `integrationsLocation()`
- `nextAppLocation()`
- `packageLocation()`
- `viteAppLocation()`

### Dependencies

This file imports/requires:

- `node:path`
- `shelljs`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 54

- `App`
- `Expected`
- `Next`
- `Tailwind`
- `Vite`
- `__dirname`
- `beforeAll`
- `build`
- `clean`
- `code`
- `command`
- `cwd`
- `describe`
- `email`
- `exec`
- `executionResult`
- `exit`
- `expect`
- `fatal`
- `install`
- `installations`
- `integrations`
- `integrationsLocation`
- `nextAppLocation`
- `nextjs`
- `node`
- `non`
- `npm`
- `packageLocation`
- `path`
- `process`
- `properly`
- `publish`
- `react`
- `resolve`
- `returned`
- `run`
- `shell`
- `shelljs`
- `silent`
- `stderr`
- `stdout`
- `string`
- `tailwind`
- `test`
- `timeout`
- `toBe`
- `vite`
- `viteAppLocation`
- `work`
- `works`
- `write`
- `yalc`
- `zero`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

