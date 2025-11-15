# Documentation: export.ts
**File Path:** `packages/react-email/src/commands/export.ts`
**Language:** typescript
**Size:** 6,015 bytes
**Lines:** 205
**Generated:** 2025-11-15T20:37:32.593895Z

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

- **Path:** `packages/react-email/src/commands/export.ts`
- **Name:** `export.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 6,015 bytes (5.87 KB)
- **Lines of Code:** 205

---

## Original Source

```typescript
import fs, { unlinkSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import path from 'node:path';
import url from 'node:url';
import type { Options } from '@react-email/components';
import { type BuildFailure, build } from 'esbuild';
import { glob } from 'glob';
import logSymbols from 'log-symbols';
import normalize from 'normalize-path';
import ora, { type Ora } from 'ora';
import type React from 'react';
import { renderingUtilitiesExporter } from '../utils/esbuild/renderring-utilities-exporter.js';
import {
  type EmailsDirectory,
  getEmailsDirectoryMetadata,
} from '../utils/get-emails-directory-metadata.js';
import { tree } from '../utils/index.js';
import { registerSpinnerAutostopping } from '../utils/register-spinner-autostopping.js';

const getEmailTemplatesFromDirectory = (emailDirectory: EmailsDirectory) => {
  const templatePaths = [] as string[];
  for (const filename of emailDirectory.emailFilenames) {
    templatePaths.push(path.join(emailDirectory.absolutePath, filename));
  }
  for (const directory of emailDirectory.subDirectories) {
    templatePaths.push(...getEmailTemplatesFromDirectory(directory));
  }

  return templatePaths;
};

type ExportTemplatesOptions = Options & {
  silent?: boolean;
  pretty?: boolean;
};

const filename = url.fileURLToPath(import.meta.url);

const require = createRequire(filename);

/*
  This first builds all the templates using esbuild and then puts the output in the `.js`
  files. Then these `.js` files are imported dynamically and rendered to `.html` files
  using the `render` function.
 */
export const exportTemplates = async (
  pathToWhereEmailMarkupShouldBeDumped: string,
  emailsDirectoryPath: string,
  options: ExportTemplatesOptions,
) => {
  /* Delete the out directory if it already exists */
  if (fs.existsSync(pathToWhereEmailMarkupShouldBeDumped)) {
    fs.rmSync(pathToWhereEmailMarkupShouldBeDumped, { recursive: true });
  }

  let spinner: Ora | undefined;
  if (!options.silent) {
    spinner = ora('Preparing files...\n').start();
    registerSpinnerAutostopping(spinner);
  }

  const emailsDirectoryMetadata = await getEmailsDirectoryMetadata(
    path.resolve(process.cwd(), emailsDirectoryPath),
    true,
  );

  if (typeof emailsDirectoryMetadata === 'undefined') {
    if (spinner) {
      spinner.stopAndPersist({
        symbol: logSymbols.error,
        text: `Could not find the directory at ${emailsDirectoryPath}`,
      });
    }
    return;
  }

  const allTemplates = getEmailTemplatesFromDirectory(emailsDirectoryMetadata);

  try {
    await build({
      bundle: true,
      entryPoints: allTemplates,
      format: 'cjs',
      jsx: 'automatic',
      loader: { '.js': 'jsx' },
      logLevel: 'silent',
      outExtension: { '.js': '.cjs' },
      outdir: pathToWhereEmailMarkupShouldBeDumped,
      platform: 'node',
      plugins: [renderingUtilitiesExporter(allTemplates)],
      write: true,
    });
  } catch (exception) {
    if (spinner) {
      spinner.stopAndPersist({
        symbol: logSymbols.error,
        text: 'Failed to build emails',
      });
    }

    const buildFailure = exception as BuildFailure;
    console.error(`\n${buildFailure.message}`);

    process.exit(1);
  }

  if (spinner) {
    spinner.succeed();
  }

  const allBuiltTemplates = glob.sync(
    normalize(`${pathToWhereEmailMarkupShouldBeDumped}/**/*.cjs`),
    {
      absolute: true,
    },
  );

  for await (const template of allBuiltTemplates) {
    try {
      if (spinner) {
        spinner.text = `rendering ${template.split('/').pop()}`;
        spinner.render();
      }
      delete require.cache[template];
      const emailModule = require(template) as {
        default: React.FC;
        render: (
          element: React.ReactElement,
          options: Record<string, unknown>,
        ) => Promise<string>;
        reactEmailCreateReactElement: typeof React.createElement;
      };
      const rendered = await emailModule.render(
        emailModule.reactEmailCreateReactElement(emailModule.default, {}),
        options,
      );
      const htmlPath = template.replace(
        '.cjs',
        options.plainText ? '.txt' : '.html',
      );
      writeFileSync(htmlPath, rendered);
      unlinkSync(template);
    } catch (exception) {
      if (spinner) {
        spinner.stopAndPersist({
          symbol: logSymbols.error,
          text: `failed when rendering ${template.split('/').pop()}`,
        });
      }
      console.error(exception);
      process.exit(1);
    }
  }
  if (spinner) {
    spinner.succeed('Rendered all files');
    spinner.text = 'Copying static files';
    spinner.render();
  }

  // ex: emails/static
  const staticDirectoryPath = path.join(emailsDirectoryPath, 'static');

  if (fs.existsSync(staticDirectoryPath)) {
    const pathToDumpStaticFilesInto = path.join(
      pathToWhereEmailMarkupShouldBeDumped,
      'static',
    );
    // cp('-r', ...) will copy *inside* of the static directory if it exists
    // causing a duplication of static files, so we need to delete ir first
    if (fs.existsSync(pathToDumpStaticFilesInto))
      await fs.promises.rm(pathToDumpStaticFilesInto, { recursive: true });

    try {
      await fs.promises.cp(staticDirectoryPath, pathToDumpStaticFilesInto, {
        recursive: true,
      });
    } catch (exception) {
      console.error(exception);
      if (spinner) {
        spinner.stopAndPersist({
          symbol: logSymbols.error,
          text: 'Failed to copy static files',
        });
      }
      console.error(
        `Something went wrong while copying the file to ${pathToWhereEmailMarkupShouldBeDumped}/static, ${exception}`,
      );
      process.exit(1);
    }
  }

  if (spinner && !options.silent) {
    spinner.succeed();

    const fileTree = await tree(pathToWhereEmailMarkupShouldBeDumped, 4);

    console.log(fileTree);

    spinner.stopAndPersist({
      symbol: logSymbols.success,
      text: 'Successfully exported emails',
    });
  }
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `allBuiltTemplates()`
- `allTemplates()`
- `buildFailure()`
- `emailModule()`
- `emailsDirectoryMetadata()`
- `exportTemplates()`
- `fileTree()`
- `filename()`
- `getEmailTemplatesFromDirectory()`
- `htmlPath()`
- `pathToDumpStaticFilesInto()`
- `rendered()`
- `require()`
- `staticDirectoryPath()`
- `templatePaths()`

### Type Definitions

- `BuildFailure`
- `EmailsDirectory`
- `ExportTemplatesOptions`
- `Ora`
- `React`

### Dependencies

This file imports/requires:

- `../utils/esbuild/renderring-utilities-exporter.js`
- `../utils/get-emails-directory-metadata.js`
- `../utils/index.js`
- `../utils/register-spinner-autostopping.js`
- `@react-email/components`
- `esbuild`
- `glob`
- `log-symbols`
- `node:fs`
- `node:module`
- `node:path`
- `node:url`
- `normalize-path`
- `ora`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 159

- `BuildFailure`
- `Copying`
- `Delete`
- `EmailsDirectory`
- `ExportTemplatesOptions`
- `Failed`
- `Options`
- `Ora`
- `Preparing`
- `Promise`
- `React`
- `ReactElement`
- `Record`
- `Rendered`
- `Something`
- `Successfully`
- `Then`
- `absolute`
- `absolutePath`
- `all`
- `allBuiltTemplates`
- `allTemplates`
- `already`
- `automatic`
- `autostopping`
- `boolean`
- `build`
- `buildFailure`
- `builds`
- `bundle`
- `cache`
- `causing`
- `cjs`
- `components`
- `console`
- `copy`
- `copying`
- `createElement`
- `createRequire`
- `cwd`
- `delete`
- `directory`
- `duplication`
- `dynamically`
- `element`
- `email`
- `emailDirectory`
- `emailFilenames`
- `emailModule`
- `emails`
- `emailsDirectoryMetadata`
- `emailsDirectoryPath`
- `entryPoints`
- `error`
- `esbuild`
- `exception`
- `exists`
- `existsSync`
- `exit`
- `exportTemplates`
- `exported`
- `exporter`
- `failed`
- `file`
- `fileTree`
- `fileURLToPath`
- `filename`
- `files`
- `find`
- `first`
- `format`
- `get`
- `getEmailTemplatesFromDirectory`
- `getEmailsDirectoryMetadata`
- `glob`
- `html`
- `htmlPath`
- `imported`
- `index`
- `inside`
- `join`
- `jsx`
- `loader`
- `log`
- `logLevel`
- `logSymbols`
- `message`
- `meta`
- `metadata`
- `module`
- `need`
- `node`
- `normalize`
- `options`
- `ora`
- `out`
- `outExtension`
- `outdir`
- `output`
- `path`
- `pathToDumpStaticFilesInto`
- `pathToWhereEmailMarkupShouldBeDumped`
- `plainText`
- `platform`
- `plugins`
- `pop`
- `pretty`
- `process`
- `promises`
- `push`
- `puts`
- `react`
- `reactEmailCreateReactElement`
- `recursive`
- `register`
- `registerSpinnerAutostopping`
- `render`
- `rendered`
- `rendering`
- `renderingUtilitiesExporter`
- `renderring`
- `replace`
- `require`
- `resolve`
- `rmSync`
- `silent`
- `spinner`
- `split`
- `start`
- `static`
- `staticDirectoryPath`
- `stopAndPersist`
- `string`
- `subDirectories`
- `succeed`
- `success`
- `symbol`
- `symbols`
- `sync`
- `template`
- `templatePaths`
- `templates`
- `text`
- `then`
- `these`
- `tree`
- `txt`
- `type`
- `unknown`
- `unlinkSync`
- `url`
- `using`
- `utilities`
- `utils`
- `went`
- `when`
- `write`
- `writeFileSync`
- `wrong`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

