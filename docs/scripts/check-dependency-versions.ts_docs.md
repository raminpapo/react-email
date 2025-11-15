# Documentation: check-dependency-versions.ts
**File Path:** `scripts/check-dependency-versions.ts`
**Language:** typescript
**Size:** 1,117 bytes
**Lines:** 45
**Generated:** 2025-11-15T20:37:31.442421Z

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

- **Path:** `scripts/check-dependency-versions.ts`
- **Name:** `check-dependency-versions.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,117 bytes (1.09 KB)
- **Lines of Code:** 45

---

## Original Source

```typescript
import fs from 'node:fs/promises';

(async () => {
  const pkg: {
    dependencies: Record<string, string>;
    devDependencies: Record<string, string>;
  } = JSON.parse(await fs.readFile('package.json', 'utf8'));
  const errors = [];

  function isPinned(version: string) {
    if (version.startsWith('workspace:')) {
      return true;
    }
    if (version.startsWith('npm:')) {
      return true;
    }
    if (/^\d+\.\d+\.\d+(-\S+)?$/.test(version)) {
      return true;
    }
    if (/^[a-z]+:[a-z]+@\d+$/.test(version)) {
      return true;
    }
    return false;
  }

  for (const [dep, version] of Object.entries(pkg.dependencies || {})) {
    if (!isPinned(version)) {
      errors.push(`Dependency "${dep}" is not pinned: "${version}"`);
    }
  }

  for (const [dep, version] of Object.entries(pkg.devDependencies || {})) {
    if (!isPinned(version)) {
      errors.push(`Dev dependency "${dep}" is not pinned: "${version}"`);
    }
  }

  if (errors.length > 0) {
    console.error(`\n${errors.join('\n')}\n`);
    process.exit(1);
  } else {
    console.log('All dependencies are pinned.');
  }
})();

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `errors()`
- `isPinned()`

### Dependencies

This file imports/requires:

- `node:fs/promises`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 35

- `All`
- `Dependency`
- `Dev`
- `Object`
- `Record`
- `console`
- `dep`
- `dependencies`
- `dependency`
- `devDependencies`
- `entries`
- `error`
- `errors`
- `exit`
- `isPinned`
- `join`
- `json`
- `length`
- `log`
- `node`
- `npm`
- `package`
- `parse`
- `pinned`
- `pkg`
- `process`
- `promises`
- `push`
- `readFile`
- `startsWith`
- `string`
- `test`
- `utf8`
- `version`
- `workspace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

