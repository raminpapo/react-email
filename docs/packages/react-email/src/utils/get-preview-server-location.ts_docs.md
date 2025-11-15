# Documentation: get-preview-server-location.ts
**File Path:** `packages/react-email/src/utils/get-preview-server-location.ts`
**Language:** typescript
**Size:** 1,581 bytes
**Lines:** 51
**Generated:** 2025-11-15T20:37:32.529903Z

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

- **Path:** `packages/react-email/src/utils/get-preview-server-location.ts`
- **Name:** `get-preview-server-location.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,581 bytes (1.54 KB)
- **Lines of Code:** 51

---

## Original Source

```typescript
import path from 'node:path';
import url from 'node:url';
import { createJiti } from 'jiti';
import { addDevDependency } from 'nypm';
import prompts from 'prompts';
import { packageJson } from './packageJson.js';

const ensurePreviewServerInstalled = async (
  message: string,
): Promise<never> => {
  const response = await prompts({
    type: 'confirm',
    name: 'installPreviewServer',
    message,
    initial: true,
  });
  if (response.installPreviewServer) {
    console.log('Installing "@react-email/preview-server"');
    await addDevDependency(
      `@react-email/preview-server@${packageJson.version}`,
    );
    process.exit(0);
  } else {
    process.exit(0);
  }
};

export const getPreviewServerLocation = async () => {
  const usersProject = createJiti(process.cwd());
  let previewServerLocation!: string;
  try {
    previewServerLocation = path.dirname(
      url.fileURLToPath(usersProject.esmResolve('@react-email/preview-server')),
    );
  } catch (_exception) {
    await ensurePreviewServerInstalled(
      'To run the preview server, the package "@react-email/preview-server" must be installed. Would you like to install it?',
    );
  }
  const { version } = await usersProject.import<{
    version: string;
  }>('@react-email/preview-server');
  if (version !== packageJson.version) {
    await ensurePreviewServerInstalled(
      `To run the preview server, the version of "@react-email/preview-server" must match the version of "react-email" (${packageJson.version}). Would you like to install it?`,
    );
  }

  return previewServerLocation;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `ensurePreviewServerInstalled()`
- `getPreviewServerLocation()`
- `response()`
- `usersProject()`

### Dependencies

This file imports/requires:

- `./packageJson.js`
- `jiti`
- `node:path`
- `node:url`
- `nypm`
- `prompts`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 46

- `Installing`
- `Promise`
- `_exception`
- `addDevDependency`
- `confirm`
- `console`
- `createJiti`
- `cwd`
- `dirname`
- `email`
- `ensurePreviewServerInstalled`
- `esmResolve`
- `exit`
- `fileURLToPath`
- `getPreviewServerLocation`
- `initial`
- `install`
- `installPreviewServer`
- `installed`
- `jiti`
- `like`
- `log`
- `match`
- `message`
- `must`
- `name`
- `never`
- `node`
- `nypm`
- `package`
- `packageJson`
- `path`
- `preview`
- `previewServerLocation`
- `process`
- `prompts`
- `react`
- `response`
- `run`
- `server`
- `string`
- `type`
- `url`
- `usersProject`
- `version`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

