# Documentation: renderring-utilities-exporter.ts
**File Path:** `packages/preview-server/src/utils/esbuild/renderring-utilities-exporter.ts`
**Language:** typescript
**Size:** 2,370 bytes
**Lines:** 65
**Generated:** 2025-11-15T20:37:32.073249Z

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

- **Path:** `packages/preview-server/src/utils/esbuild/renderring-utilities-exporter.ts`
- **Name:** `renderring-utilities-exporter.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,370 bytes (2.31 KB)
- **Lines of Code:** 65

---

## Original Source

```typescript
import { promises as fs } from 'node:fs';
import path from 'node:path';
import type { Loader, PluginBuild, ResolveOptions } from 'esbuild';
import { escapeStringForRegex } from './escape-string-for-regex';

/**
 * Made to export the `render` function out of the user's email template
 * so that issues like https://github.com/resend/react-email/issues/649 don't
 * happen.
 *
 * This also exports the `createElement` from the user's React version as well
 * to avoid mismatches.
 *
 * This avoids multiple versions of React being involved, i.e., the version
 * in the CLI vs. the version the user has on their emails.
 */
export const renderingUtilitiesExporter = (emailTemplates: string[]) => ({
  name: 'rendering-utilities-exporter',
  setup: async (b: PluginBuild) => {
    const filterOptions = await Promise.all(
      emailTemplates.map(async (emailPath) =>
        escapeStringForRegex(await fs.realpath(emailPath)),
      ),
    );
    b.onLoad(
      {
        filter: new RegExp(filterOptions.join('|')),
      },
      async ({ path: pathToFile }) => {
        return {
          contents: `${await fs.readFile(pathToFile, 'utf8')};
          export { render } from 'react-email-module-that-will-export-render'
          export { createElement as reactEmailCreateReactElement } from 'react';
        `,
          loader: path.extname(pathToFile).slice(1) as Loader,
        };
      },
    );

    b.onResolve(
      { filter: /^react-email-module-that-will-export-render$/ },
      async (args) => {
        const options: ResolveOptions = {
          kind: 'import-statement',
          importer: args.importer,
          resolveDir: args.resolveDir,
          namespace: args.namespace,
        };
        let result = await b.resolve('@react-email/render', options);
        if (result.errors.length === 0) {
          return result;
        }

        // If @react-email/render does not exist, resolve to @react-email/components
        result = await b.resolve('@react-email/components', options);
        if (result.errors.length > 0 && result.errors[0]) {
          result.errors[0].text =
            "Failed trying to import `render` from either `@react-email/render` or `@react-email/components` to be able to render your email template.\n Maybe you don't have either of them installed?";
        }
        return result;
      },
    );
  },
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `filterOptions()`
- `renderingUtilitiesExporter()`
- `result()`

### Dependencies

This file imports/requires:

- `./escape-string-for-regex`
- `esbuild`
- `node:fs`
- `node:path`
- `react`
- `react-email-module-that-will-export-render`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 91

- `Failed`
- `Loader`
- `Made`
- `Maybe`
- `PluginBuild`
- `Promise`
- `React`
- `RegExp`
- `ResolveOptions`
- `able`
- `all`
- `also`
- `args`
- `avoid`
- `avoids`
- `com`
- `components`
- `contents`
- `createElement`
- `don`
- `either`
- `email`
- `emailPath`
- `emailTemplates`
- `emails`
- `errors`
- `esbuild`
- `escape`
- `escapeStringForRegex`
- `exist`
- `exporter`
- `exports`
- `extname`
- `filter`
- `filterOptions`
- `github`
- `happen`
- `https`
- `importer`
- `installed`
- `involved`
- `issues`
- `join`
- `kind`
- `length`
- `like`
- `loader`
- `map`
- `mismatches`
- `module`
- `multiple`
- `name`
- `namespace`
- `node`
- `onLoad`
- `onResolve`
- `options`
- `out`
- `path`
- `pathToFile`
- `promises`
- `react`
- `reactEmailCreateReactElement`
- `readFile`
- `realpath`
- `regex`
- `render`
- `rendering`
- `renderingUtilitiesExporter`
- `resend`
- `resolve`
- `resolveDir`
- `result`
- `setup`
- `slice`
- `statement`
- `string`
- `template`
- `text`
- `their`
- `them`
- `trying`
- `type`
- `user`
- `utf8`
- `utilities`
- `version`
- `versions`
- `well`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

