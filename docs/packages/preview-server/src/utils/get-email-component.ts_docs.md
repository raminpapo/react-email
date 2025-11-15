# Documentation: get-email-component.ts
**File Path:** `packages/preview-server/src/utils/get-email-component.ts`
**Language:** typescript
**Size:** 4,679 bytes
**Lines:** 155
**Generated:** 2025-11-15T20:37:32.017836Z

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

- **Path:** `packages/preview-server/src/utils/get-email-component.ts`
- **Name:** `get-email-component.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 4,679 bytes (4.57 KB)
- **Lines of Code:** 155

---

## Original Source

```typescript
import path from 'node:path';
import type { render } from '@react-email/components';
import { type BuildFailure, build, type OutputFile } from 'esbuild';
import type React from 'react';
import type { RawSourceMap } from 'source-map-js';
import { z } from 'zod';
import { convertStackWithSourceMap } from './convert-stack-with-sourcemap';
import { renderingUtilitiesExporter } from './esbuild/renderring-utilities-exporter';
import { isErr } from './result';
import { createContext, runBundledCode } from './run-bundled-code';
import type { EmailTemplate as EmailComponent } from './types/email-template';
import type { ErrorObject } from './types/error-object';

const EmailComponentModule = z.object({
  default: z.any(),
  render: z.function(),
  reactEmailCreateReactElement: z.function(),
});

export const getEmailComponent = async (
  emailPath: string,
  jsxRuntimePath: string,
): Promise<
  | {
      emailComponent: EmailComponent;

      createElement: typeof React.createElement;

      /**
       * Renders the HTML with `data-source-file`/`data-source-line` attributes that should only be
       * used internally in the preview server and never shown to the user.
       */
      renderWithReferences: typeof render;
      render: typeof render;

      sourceMapToOriginalFile: RawSourceMap;
    }
  | { error: ErrorObject }
> => {
  let outputFiles: OutputFile[];
  try {
    const buildData = await build({
      bundle: true,
      entryPoints: [emailPath],
      plugins: [renderingUtilitiesExporter([emailPath])],
      platform: 'node',
      write: false,

      jsxDev: true,
      jsxImportSource: jsxRuntimePath,

      format: 'cjs',
      jsx: 'automatic',
      logLevel: 'silent',
      // allows for using jsx on a .js file
      loader: {
        '.js': 'jsx',
      },
      outdir: 'stdout', // just a stub for esbuild, it won't actually write to this folder
      sourcemap: 'external',
    });
    outputFiles = buildData.outputFiles;
  } catch (exception) {
    const buildFailure = exception as BuildFailure;
    return {
      error: {
        message: buildFailure.message,
        stack: buildFailure.stack,
        name: buildFailure.name,
        cause: buildFailure.cause,
      },
    };
  }

  const sourceMapFile = outputFiles[0]!;
  const bundledEmailFile = outputFiles[1]!;
  const builtEmailCode = bundledEmailFile.text;

  const sourceMapToEmail = JSON.parse(sourceMapFile.text) as RawSourceMap;
  // because it will have a path like <tsconfigLocation>/stdout/email.js.map
  sourceMapToEmail.sourceRoot = path.resolve(sourceMapFile.path, '../..');
  sourceMapToEmail.sources = sourceMapToEmail.sources.map((source) =>
    path.resolve(sourceMapFile.path, '..', source),
  );

  const context = createContext(emailPath);
  context.shouldIncludeSourceReference = false;
  const runningResult = runBundledCode(builtEmailCode, emailPath, context);

  if (isErr(runningResult)) {
    const { error } = runningResult;
    if (error instanceof Error) {
      error.stack &&= error.stack.split('at Script.runInContext (node:vm')[0];

      return {
        error: {
          name: error.name,
          message: error.message,
          stack: convertStackWithSourceMap(
            error.stack,
            emailPath,
            sourceMapToEmail,
          ),
          cause: error.cause,
        },
      };
    }

    throw error;
  }

  const parseResult = EmailComponentModule.safeParse(runningResult.value);

  if (parseResult.error) {
    return {
      error: {
        name: 'Error',
        message: `The email component at ${emailPath} does not contain the expected exports`,
        stack: new Error().stack,
        cause: parseResult.error,
      },
    };
  }

  if (typeof parseResult.data.default !== 'function') {
    return {
      error: {
        name: 'Error',
        message: `The email component at ${emailPath} does not contain a default exported function`,
        stack: new Error().stack,
        cause: parseResult.error,
      },
    };
  }

  const { data: componentModule } = parseResult;

  const typedRender = componentModule.render as typeof render;

  return {
    emailComponent: componentModule.default as EmailComponent,
    renderWithReferences: (async (...args: Parameters<typeof render>) => {
      context.shouldIncludeSourceReference = true;
      const renderingResult = await typedRender(...args);
      context.shouldIncludeSourceReference = false;
      return renderingResult;
    }) as typeof render,
    render: typedRender,
    createElement:
      componentModule.reactEmailCreateReactElement as typeof React.createElement,

    sourceMapToOriginalFile: sourceMapToEmail,
  };
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `EmailComponentModule()`
- `buildData()`
- `buildFailure()`
- `builtEmailCode()`
- `bundledEmailFile()`
- `context()`
- `getEmailComponent()`
- `parseResult()`
- `renderingResult()`
- `runningResult()`
- `sourceMapFile()`
- `sourceMapToEmail()`
- `typedRender()`

### Type Definitions

- `BuildFailure`
- `OutputFile`
- `React`

### Dependencies

This file imports/requires:

- `./convert-stack-with-sourcemap`
- `./esbuild/renderring-utilities-exporter`
- `./result`
- `./run-bundled-code`
- `./types/email-template`
- `./types/error-object`
- `@react-email/components`
- `esbuild`
- `node:path`
- `react`
- `source-map-js`
- `zod`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 126

- `BuildFailure`
- `EmailComponent`
- `EmailComponentModule`
- `EmailTemplate`
- `Error`
- `ErrorObject`
- `OutputFile`
- `Parameters`
- `Promise`
- `RawSourceMap`
- `React`
- `Renders`
- `Script`
- `actually`
- `allows`
- `any`
- `args`
- `attributes`
- `automatic`
- `because`
- `build`
- `buildData`
- `buildFailure`
- `builtEmailCode`
- `bundle`
- `bundled`
- `bundledEmailFile`
- `cause`
- `cjs`
- `code`
- `component`
- `componentModule`
- `components`
- `contain`
- `context`
- `convert`
- `convertStackWithSourceMap`
- `createContext`
- `createElement`
- `data`
- `email`
- `emailComponent`
- `emailPath`
- `entryPoints`
- `error`
- `esbuild`
- `exception`
- `expected`
- `exported`
- `exporter`
- `exports`
- `external`
- `file`
- `folder`
- `format`
- `getEmailComponent`
- `internally`
- `isErr`
- `jsx`
- `jsxDev`
- `jsxImportSource`
- `jsxRuntimePath`
- `just`
- `like`
- `line`
- `loader`
- `logLevel`
- `map`
- `message`
- `name`
- `never`
- `node`
- `object`
- `only`
- `outdir`
- `outputFiles`
- `parse`
- `parseResult`
- `path`
- `platform`
- `plugins`
- `preview`
- `react`
- `reactEmailCreateReactElement`
- `render`
- `renderWithReferences`
- `renderingResult`
- `renderingUtilitiesExporter`
- `renderring`
- `resolve`
- `result`
- `run`
- `runBundledCode`
- `runInContext`
- `runningResult`
- `safeParse`
- `server`
- `shouldIncludeSourceReference`
- `shown`
- `silent`
- `source`
- `sourceMapFile`
- `sourceMapToEmail`
- `sourceMapToOriginalFile`
- `sourceRoot`
- `sourcemap`
- `sources`
- `split`
- `stack`
- `stdout`
- `string`
- `stub`
- `template`
- `text`
- `tsconfigLocation`
- `type`
- `typedRender`
- `types`
- `used`
- `user`
- `using`
- `utilities`
- `value`
- `won`
- `write`
- `zod`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

