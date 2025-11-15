# Documentation: index.ts
**File Path:** `packages/react-email/src/index.ts`
**Language:** typescript
**Size:** 2,253 bytes
**Lines:** 72
**Generated:** 2025-11-15T20:37:32.521988Z

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

- **Path:** `packages/react-email/src/index.ts`
- **Name:** `index.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,253 bytes (2.20 KB)
- **Lines of Code:** 72

---

## Original Source

```typescript
#!/usr/bin/env node
import { program } from 'commander';
import { build } from './commands/build.js';
import { dev } from './commands/dev.js';
import { exportTemplates } from './commands/export.js';
import { resendReset } from './commands/resend/reset.js';
import { resendSetup } from './commands/resend/setup.js';
import { start } from './commands/start.js';
import { packageJson } from './utils/packageJson.js';

const PACKAGE_NAME = 'react-email';

program
  .name(PACKAGE_NAME)
  .description('A live preview of your emails right in your browser')
  .version(packageJson.version);

program
  .command('dev')
  .description('Starts the preview email development app')
  .option('-d, --dir <path>', 'Directory with your email templates', './emails')
  .option('-p --port <port>', 'Port to run dev server on', '3000')
  .action(dev);

program
  .command('build')
  .description('Copies the preview app for onto .react-email and builds it')
  .option('-d, --dir <path>', 'Directory with your email templates', './emails')
  .option(
    '-p --packageManager <name>',
    'Package name to use on installation on `.react-email`',
    'npm',
  )
  .action(build);

program
  .command('start')
  .description('Runs the built preview app that is inside of ".react-email"')
  .action(start);

program
  .command('export')
  .description('Build the templates to the `out` directory')
  .option('--outDir <path>', 'Output directory', 'out')
  .option('-p, --pretty', 'Pretty print the output', false)
  .option('-t, --plainText', 'Set output format as plain text', false)
  .option('-d, --dir <path>', 'Directory with your email templates', './emails')
  .option(
    '-s, --silent',
    'To, or not to show a spinner with process information',
    false,
  )
  .action(({ outDir, pretty, plainText, silent, dir: srcDir }) =>
    exportTemplates(outDir, srcDir, { silent, plainText, pretty }),
  );

const resend = program.command('resend');

resend
  .command('setup')
  .description(
    'Sets up the integration between the React Email CLI, and your Resend account through an API Key',
  )
  .action(resendSetup);

resend
  .command('reset')
  .description('Deletes your API Key from the React Email configuration')
  .action(resendReset);

program.parse();

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `PACKAGE_NAME()`
- `resend()`

### Dependencies

This file imports/requires:

- `./commands/build.js`
- `./commands/dev.js`
- `./commands/export.js`
- `./commands/resend/reset.js`
- `./commands/resend/setup.js`
- `./commands/start.js`
- `./utils/packageJson.js`
- `commander`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 87

- `Build`
- `Copies`
- `Deletes`
- `Directory`
- `Email`
- `Key`
- `Output`
- `PACKAGE_NAME`
- `Package`
- `Port`
- `Pretty`
- `React`
- `Resend`
- `Runs`
- `Set`
- `Sets`
- `Starts`
- `account`
- `action`
- `app`
- `between`
- `bin`
- `browser`
- `build`
- `builds`
- `built`
- `command`
- `commander`
- `commands`
- `configuration`
- `description`
- `dev`
- `development`
- `dir`
- `directory`
- `email`
- `emails`
- `env`
- `exportTemplates`
- `format`
- `information`
- `inside`
- `installation`
- `integration`
- `live`
- `name`
- `node`
- `npm`
- `onto`
- `option`
- `out`
- `outDir`
- `output`
- `packageJson`
- `packageManager`
- `parse`
- `path`
- `plain`
- `plainText`
- `port`
- `pretty`
- `preview`
- `print`
- `process`
- `program`
- `react`
- `resend`
- `resendReset`
- `resendSetup`
- `reset`
- `right`
- `run`
- `server`
- `setup`
- `show`
- `silent`
- `spinner`
- `srcDir`
- `start`
- `templates`
- `text`
- `through`
- `use`
- `usr`
- `utils`
- `version`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

