# Documentation: dev.mts
**File Path:** `packages/preview-server/scripts/dev.mts`
**Language:** Unknown
**Size:** 1,470 bytes
**Lines:** 58
**Generated:** 2025-11-15T20:37:31.763649Z

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

- **Path:** `packages/preview-server/scripts/dev.mts`
- **Name:** `dev.mts`
- **Extension:** `.mts`
- **Language:** Unknown
- **Size:** 1,470 bytes (1.44 KB)
- **Lines of Code:** 58

---

## Original Source

```
import child_process from 'node:child_process';
import { promises as fs } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import url from 'node:url';
import logSymbols from 'log-symbols';

console.info(
  '  ',
  logSymbols.warning,
  'This is only running the development server for the UI, this does not run the CLI part of the preview server.',
  os.EOL,
);

const filename = url.fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);

const previewServerRoot = path.resolve(dirname, '..');
const emailsDirectoryPath = path.join(previewServerRoot, 'emails');

const envPath = path.join(previewServerRoot, '.env.local');

await fs.writeFile(
  envPath,
  `EMAILS_DIR_RELATIVE_PATH=./emails
EMAILS_DIR_ABSOLUTE_PATH=${emailsDirectoryPath}
USER_PROJECT_LOCATION=${previewServerRoot}
PREVIEW_SERVER_LOCATION=${previewServerRoot}
NEXT_PUBLIC_IS_PREVIEW_DEVELOPMENT=true`,
  'utf8',
);

const webServerProcess = child_process.spawn('next', ['dev'], {
  cwd: previewServerRoot,
  shell: true,
  stdio: 'inherit',
});

webServerProcess.on('exit', async () => {
  await fs.rm(envPath);
});

process.on('SIGINT', () => {
  webServerProcess.kill('SIGINT');
});
process.on('SIGUSR1', () => {
  webServerProcess.kill('SIGUSR1');
});
process.on('SIGUSR2', () => {
  webServerProcess.kill('SIGUSR2');
});
process.on('uncaughtExceptionMonitor', () => {
  webServerProcess.kill();
});
process.on('exit', () => {
  webServerProcess.kill();
});

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `log-symbols`
- `node:child_process`
- `node:fs`
- `node:os`
- `node:path`
- `node:url`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 51

- `EMAILS_DIR_ABSOLUTE_PATH`
- `EMAILS_DIR_RELATIVE_PATH`
- `NEXT_PUBLIC_IS_PREVIEW_DEVELOPMENT`
- `PREVIEW_SERVER_LOCATION`
- `SIGUSR1`
- `SIGUSR2`
- `USER_PROJECT_LOCATION`
- `child_process`
- `console`
- `cwd`
- `dev`
- `development`
- `dirname`
- `emails`
- `emailsDirectoryPath`
- `env`
- `envPath`
- `exit`
- `fileURLToPath`
- `filename`
- `info`
- `inherit`
- `join`
- `kill`
- `local`
- `log`
- `logSymbols`
- `meta`
- `next`
- `node`
- `only`
- `part`
- `path`
- `preview`
- `previewServerRoot`
- `process`
- `promises`
- `resolve`
- `run`
- `running`
- `server`
- `shell`
- `spawn`
- `stdio`
- `symbols`
- `uncaughtExceptionMonitor`
- `url`
- `utf8`
- `warning`
- `webServerProcess`
- `writeFile`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

