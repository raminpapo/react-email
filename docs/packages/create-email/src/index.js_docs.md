# Documentation: index.js
**File Path:** `packages/create-email/src/index.js`
**Language:** javascript
**Size:** 2,778 bytes
**Lines:** 105
**Generated:** 2025-11-15T20:37:32.316493Z

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

- **Path:** `packages/create-email/src/index.js`
- **Name:** `index.js`
- **Extension:** `.js`
- **Language:** javascript
- **Size:** 2,778 bytes (2.71 KB)
- **Lines of Code:** 105

---

## Original Source

```javascript
#!/usr/bin/env node

import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Command } from 'commander';
import fse from 'fs-extra';
import logSymbols from 'log-symbols';
import ora from 'ora';
import { tree } from './tree.js';

const filename = fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);

const packageJson = JSON.parse(
  fse.readFileSync(path.resolve(dirname, '../package.json'), 'utf8'),
);

const getLatestVersionOfTag = async (packageName, tag) => {
  const response = await fetch(
    `https://registry.npmjs.org/${packageName}/${tag}`,
  );
  const data = await response.json();

  if (typeof data === 'string' && data.startsWith('version not found')) {
    console.error(`Tag ${tag} does not exist for ${packageName}.`);
    process.exit(1);
  }

  const { version } = data;

  if (!/^\d+\.\d+\.\d+.*$/.test(version)) {
    console.error('Invalid version received, something has gone very wrong.');
  }

  return version;
};

const init = async (name, { tag }) => {
  let projectPath = name;

  if (!projectPath) {
    projectPath = path.join(process.cwd(), 'react-email-starter');
  }

  if (typeof projectPath === 'string') {
    projectPath = projectPath.trim();
  }

  const templatePath = path.resolve(dirname, '../template');
  const resolvedProjectPath = path.resolve(projectPath);

  if (fse.existsSync(resolvedProjectPath)) {
    console.error(`Project called ${projectPath} already exists!`);
    process.exit(1);
  }

  const spinner = ora({
    text: 'Preparing files...\n',
  }).start();

  fse.copySync(templatePath, resolvedProjectPath, {
    recursive: true,
  });
  const templatePackageJsonPath = path.resolve(
    resolvedProjectPath,
    './package.json',
  );
  const templatePackageJson = fse.readFileSync(templatePackageJsonPath, 'utf8');
  fse.writeFileSync(
    templatePackageJsonPath,
    templatePackageJson
      .replace(
        'INSERT_COMPONENTS_VERSION',
        await getLatestVersionOfTag('@react-email/components', tag),
      )
      .replaceAll(
        'INSERT_REACT_EMAIL_VERSION',
        await getLatestVersionOfTag('react-email', tag),
      ),
    'utf8',
  );

  spinner.stopAndPersist({
    symbol: logSymbols.success,
    text: 'React Email Starter files ready',
  });

  console.info(
    await tree(resolvedProjectPath, 4, (dirent) => {
      return !path
        .join(dirent.parentPath, dirent.name)
        .includes('node_modules');
    }),
  );
};

new Command()
  .name(packageJson.name)
  .version(packageJson.version)
  .description('The easiest way to get started with React Email')
  .arguments('[dir]', 'Path to initialize the project')
  .option('-t, --tag <tag>', 'Tag of React Email versions to use', 'latest')
  .action(init)
  .parse(process.argv);

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `data()`
- `dirname()`
- `filename()`
- `getLatestVersionOfTag()`
- `init()`
- `packageJson()`
- `projectPath()`
- `resolvedProjectPath()`
- `response()`
- `spinner()`
- `templatePackageJson()`
- `templatePackageJsonPath()`
- `templatePath()`

### Dependencies

This file imports/requires:

- `./tree.js`
- `commander`
- `fs-extra`
- `log-symbols`
- `node:path`
- `node:url`
- `ora`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 113

- `Command`
- `Email`
- `INSERT_COMPONENTS_VERSION`
- `INSERT_REACT_EMAIL_VERSION`
- `Invalid`
- `Path`
- `Preparing`
- `Project`
- `React`
- `Starter`
- `Tag`
- `action`
- `already`
- `arguments`
- `argv`
- `bin`
- `called`
- `commander`
- `components`
- `console`
- `copySync`
- `cwd`
- `data`
- `description`
- `dir`
- `dirent`
- `dirname`
- `easiest`
- `email`
- `env`
- `error`
- `exist`
- `exists`
- `existsSync`
- `exit`
- `extra`
- `fetch`
- `fileURLToPath`
- `filename`
- `files`
- `found`
- `fse`
- `get`
- `getLatestVersionOfTag`
- `gone`
- `https`
- `includes`
- `info`
- `init`
- `initialize`
- `join`
- `json`
- `latest`
- `log`
- `logSymbols`
- `meta`
- `name`
- `node`
- `node_modules`
- `npmjs`
- `option`
- `ora`
- `org`
- `package`
- `packageJson`
- `packageName`
- `parentPath`
- `parse`
- `path`
- `process`
- `project`
- `projectPath`
- `react`
- `readFileSync`
- `ready`
- `received`
- `recursive`
- `registry`
- `replace`
- `replaceAll`
- `resolve`
- `resolvedProjectPath`
- `response`
- `something`
- `spinner`
- `start`
- `started`
- `starter`
- `startsWith`
- `stopAndPersist`
- `string`
- `success`
- `symbol`
- `symbols`
- `tag`
- `template`
- `templatePackageJson`
- `templatePackageJsonPath`
- `templatePath`
- `test`
- `text`
- `tree`
- `trim`
- `url`
- `use`
- `usr`
- `utf8`
- `version`
- `versions`
- `very`
- `way`
- `writeFileSync`
- `wrong`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

