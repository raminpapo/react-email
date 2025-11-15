# Documentation: pull-request-title-check.ts
**File Path:** `scripts/pull-request-title-check.ts`
**Language:** typescript
**Size:** 782 bytes
**Lines:** 28
**Generated:** 2025-11-15T20:37:31.443506Z

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

- **Path:** `scripts/pull-request-title-check.ts`
- **Name:** `pull-request-title-check.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 782 bytes (0.76 KB)
- **Lines of Code:** 28

---

## Original Source

```typescript
import fs from 'node:fs';

const eventPath = process.env.GITHUB_EVENT_PATH;
if (!eventPath) {
  throw new Error(
    'GITHUB_EVENT_PATH environment variable is not set. This script is only meant to run in during a Github workflow.',
  );
}

const eventJson = JSON.parse(fs.readFileSync(eventPath, 'utf8'));
const { title } = eventJson.pull_request;

const validTypeRegex =
  /^(feat|fix|chore|refactor)(\([a-zA-Z0-9-]+\))?:\s[a-z].*$/;

if (!validTypeRegex.test(title)) {
  console.error(
    `pull request title does not follow the required format.
example: "type: description of the change"

- type: "feat", "fix", "chore", or "refactor"
- first letter of the title after the 'type' needs to be lowercased`,
  );
  process.exit(1);
}

console.info('pull request title is valid');

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `eventJson()`
- `eventPath()`
- `validTypeRegex()`

### Dependencies

This file imports/requires:

- `node:fs`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 47

- `Error`
- `GITHUB_EVENT_PATH`
- `Github`
- `after`
- `change`
- `chore`
- `console`
- `description`
- `during`
- `env`
- `environment`
- `error`
- `eventJson`
- `eventPath`
- `example`
- `exit`
- `feat`
- `first`
- `fix`
- `follow`
- `format`
- `info`
- `letter`
- `lowercased`
- `meant`
- `needs`
- `node`
- `only`
- `parse`
- `process`
- `pull`
- `pull_request`
- `readFileSync`
- `refactor`
- `request`
- `required`
- `run`
- `script`
- `set`
- `test`
- `title`
- `type`
- `utf8`
- `valid`
- `validTypeRegex`
- `variable`
- `workflow`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

