# Documentation: build.ts
**File Path:** `packages/react-email/src/commands/build.ts`
**Language:** typescript
**Size:** 8,430 bytes
**Lines:** 297
**Generated:** 2025-11-15T20:37:32.589969Z

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

- **Path:** `packages/react-email/src/commands/build.ts`
- **Name:** `build.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 8,430 bytes (8.23 KB)
- **Lines of Code:** 297

---

## Original Source

```typescript
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import logSymbols from 'log-symbols';
import ora from 'ora';
import {
  type EmailsDirectory,
  getEmailsDirectoryMetadata,
} from '../utils/get-emails-directory-metadata.js';
import { getPreviewServerLocation } from '../utils/get-preview-server-location.js';
import { registerSpinnerAutostopping } from '../utils/register-spinner-autostopping.js';

interface Args {
  dir: string;
  packageManager: string;
}

const buildPreviewApp = (absoluteDirectory: string) => {
  return new Promise<void>((resolve, reject) => {
    const nextBuild = spawn('npm', ['run', 'build'], {
      cwd: absoluteDirectory,
      shell: true,
    });
    nextBuild.stdout.pipe(process.stdout);
    nextBuild.stderr.pipe(process.stderr);

    nextBuild.on('close', (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(
          new Error(
            `Unable to build the Next app and it exited with code: ${code}`,
          ),
        );
      }
    });
  });
};

const npmInstall = async (
  builtPreviewAppPath: string,
  packageManager: string,
) => {
  return new Promise<void>((resolve, reject) => {
    const childProc = spawn(
      packageManager,
      [
        'install',
        packageManager === 'deno' ? '' : '--include=dev',
        packageManager === 'deno' ? '--quiet' : '--silent',
      ],
      {
        cwd: builtPreviewAppPath,
        shell: true,
      },
    );
    childProc.stdout.pipe(process.stdout);
    childProc.stderr.pipe(process.stderr);
    childProc.on('close', (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(
          new Error(
            `Unable to install the dependencies and it exited with code: ${code}`,
          ),
        );
      }
    });
  });
};

const setNextEnvironmentVariablesForBuild = async (
  emailsDirRelativePath: string,
  builtPreviewAppPath: string,
) => {
  const nextConfigContents = `
import path from 'path';
const emailsDirRelativePath = path.normalize('${emailsDirRelativePath}');
const userProjectLocation = '${process.cwd().replace(/\\/g, '/')}';
/** @type {import('next').NextConfig} */
const nextConfig = {
  env: {
    NEXT_PUBLIC_IS_BUILDING: 'true',
    EMAILS_DIR_RELATIVE_PATH: emailsDirRelativePath,
    EMAILS_DIR_ABSOLUTE_PATH: path.resolve(userProjectLocation, emailsDirRelativePath),
    PREVIEW_SERVER_LOCATION: '${builtPreviewAppPath.replace(/\\/g, '/')}',
    USER_PROJECT_LOCATION: userProjectLocation
  },
  serverExternalPackages: ['esbuild'],
  typescript: {
    ignoreBuildErrors: true
  },
  experimental: {
    webpackBuildWorker: true
  },
}

export default nextConfig`;

  await fs.promises.writeFile(
    path.resolve(builtPreviewAppPath, './next.config.mjs'),
    nextConfigContents,
    'utf8',
  );
};

const getEmailSlugsFromEmailDirectory = (
  emailDirectory: EmailsDirectory,
  emailsDirectoryAbsolutePath: string,
) => {
  const directoryPathRelativeToEmailsDirectory = emailDirectory.absolutePath
    .replace(emailsDirectoryAbsolutePath, '')
    .trim();

  const slugs = [] as Array<string>[];
  for (const filename of emailDirectory.emailFilenames) {
    slugs.push(
      path
        .join(directoryPathRelativeToEmailsDirectory, filename)
        .split(path.sep)
        // sometimes it gets empty segments due to trailing slashes
        .filter((segment) => segment.length > 0),
    );
  }
  for (const directory of emailDirectory.subDirectories) {
    slugs.push(
      ...getEmailSlugsFromEmailDirectory(
        directory,
        emailsDirectoryAbsolutePath,
      ),
    );
  }

  return slugs;
};

// we do this because otherwise it won't be able to find the emails
// after build
const forceSSGForEmailPreviews = async (
  emailsDirPath: string,
  builtPreviewAppPath: string,
) => {
  const emailDirectoryMetadata = (await getEmailsDirectoryMetadata(
    emailsDirPath,
  ))!;

  const parameters = getEmailSlugsFromEmailDirectory(
    emailDirectoryMetadata,
    emailsDirPath,
  ).map((slug) => ({ slug }));

  const removeForceDynamic = async (filePath: string) => {
    const contents = await fs.promises.readFile(filePath, 'utf8');

    await fs.promises.writeFile(
      filePath,
      contents.replace("export const dynamic = 'force-dynamic';", ''),
      'utf8',
    );
  };
  await removeForceDynamic(
    path.resolve(builtPreviewAppPath, './src/app/layout.tsx'),
  );
  await removeForceDynamic(
    path.resolve(builtPreviewAppPath, './src/app/preview/[...slug]/page.tsx'),
  );

  await fs.promises.appendFile(
    path.resolve(builtPreviewAppPath, './src/app/preview/[...slug]/page.tsx'),
    `

export function generateStaticParams() { 
  return Promise.resolve(
    ${JSON.stringify(parameters)}
  );
}`,
    'utf8',
  );
};

const updatePackageJson = async (builtPreviewAppPath: string) => {
  const packageJsonPath = path.resolve(builtPreviewAppPath, './package.json');
  const packageJson = JSON.parse(
    await fs.promises.readFile(packageJsonPath, 'utf8'),
  ) as {
    name: string;
    scripts: Record<string, string>;
    dependencies: Record<string, string>;
    devDependencies: Record<string, string>;
  };
  // Turbopack has some errors with the imports in @react-email/tailwind
  packageJson.scripts.build = 'next build --webpack';
  packageJson.scripts.start = 'next start';
  delete packageJson.scripts.postbuild;

  packageJson.name = 'preview-server';

  for (const [dependency, version] of Object.entries(
    packageJson.devDependencies,
  )) {
    packageJson.devDependencies[dependency] = version.replace('workspace:', '');
  }

  delete packageJson.devDependencies['@react-email/components'];
  delete packageJson.scripts.prepare;

  await fs.promises.writeFile(
    packageJsonPath,
    JSON.stringify(packageJson),
    'utf8',
  );
};

export const build = async ({
  dir: emailsDirRelativePath,
  packageManager,
}: Args) => {
  try {
    const previewServerLocation = await getPreviewServerLocation();

    const spinner = ora({
      text: 'Starting build process...',
      prefixText: '  ',
    }).start();
    registerSpinnerAutostopping(spinner);

    spinner.text = `Checking if ${emailsDirRelativePath} folder exists`;
    if (!fs.existsSync(emailsDirRelativePath)) {
      process.exit(1);
    }

    const emailsDirPath = path.join(process.cwd(), emailsDirRelativePath);
    const staticPath = path.join(emailsDirPath, 'static');

    const builtPreviewAppPath = path.join(process.cwd(), '.react-email');

    if (fs.existsSync(builtPreviewAppPath)) {
      spinner.text = 'Deleting pre-existing `.react-email` folder';
      await fs.promises.rm(builtPreviewAppPath, { recursive: true });
    }

    spinner.text = 'Copying preview app from CLI to `.react-email`';
    await fs.promises.cp(previewServerLocation, builtPreviewAppPath, {
      recursive: true,
      filter: (source: string) => {
        // do not copy the CLI files
        return (
          !/(\/|\\)cli(\/|\\)?/.test(source) &&
          !/(\/|\\)\.next(\/|\\)?/.test(source) &&
          !/(\/|\\)\.turbo(\/|\\)?/.test(source) &&
          !/(\/|\\)node_modules(\/|\\)?$/.test(source)
        );
      },
    });

    if (fs.existsSync(staticPath)) {
      spinner.text =
        'Copying `static` folder into `.react-email/public/static`';
      const builtStaticDirectory = path.resolve(
        builtPreviewAppPath,
        './public/static',
      );
      await fs.promises.cp(staticPath, builtStaticDirectory, {
        recursive: true,
      });
    }

    spinner.text =
      'Setting Next environment variables for preview app to work properly';
    await setNextEnvironmentVariablesForBuild(
      emailsDirRelativePath,
      builtPreviewAppPath,
    );

    spinner.text = 'Setting server side generation for the email preview pages';
    await forceSSGForEmailPreviews(emailsDirPath, builtPreviewAppPath);

    spinner.text = "Updating package.json's build and start scripts";
    await updatePackageJson(builtPreviewAppPath);

    spinner.text = 'Installing dependencies on `.react-email`';
    await npmInstall(builtPreviewAppPath, packageManager);

    spinner.stopAndPersist({
      text: 'Successfully prepared `.react-email` for `next build`',
      symbol: logSymbols.success,
    });

    await buildPreviewApp(builtPreviewAppPath);
  } catch (error) {
    console.log(error);
    process.exit(1);
  }
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `build()`
- `buildPreviewApp()`
- `builtPreviewAppPath()`
- `builtStaticDirectory()`
- `childProc()`
- `contents()`
- `directoryPathRelativeToEmailsDirectory()`
- `dynamic()`
- `emailDirectoryMetadata()`
- `emailsDirPath()`
- `emailsDirRelativePath()`
- `forceSSGForEmailPreviews()`
- `generateStaticParams()`
- `getEmailSlugsFromEmailDirectory()`
- `nextBuild()`
- `nextConfig()`
- `nextConfigContents()`
- `npmInstall()`
- `packageJson()`
- `packageJsonPath()`
- `parameters()`
- `previewServerLocation()`
- `removeForceDynamic()`
- `setNextEnvironmentVariablesForBuild()`
- `slugs()`
- `spinner()`
- `staticPath()`
- `updatePackageJson()`
- `userProjectLocation()`

### Interfaces

- `Args`

### Type Definitions

- `EmailsDirectory`

### Dependencies

This file imports/requires:

- `../utils/get-emails-directory-metadata.js`
- `../utils/get-preview-server-location.js`
- `../utils/register-spinner-autostopping.js`
- `log-symbols`
- `node:child_process`
- `node:fs`
- `node:path`
- `ora`
- `path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 200

- `Args`
- `Array`
- `Checking`
- `Copying`
- `Deleting`
- `EMAILS_DIR_ABSOLUTE_PATH`
- `EMAILS_DIR_RELATIVE_PATH`
- `EmailsDirectory`
- `Error`
- `Installing`
- `NEXT_PUBLIC_IS_BUILDING`
- `Next`
- `NextConfig`
- `Object`
- `PREVIEW_SERVER_LOCATION`
- `Promise`
- `Record`
- `Setting`
- `Starting`
- `Successfully`
- `Turbopack`
- `USER_PROJECT_LOCATION`
- `Unable`
- `Updating`
- `able`
- `absoluteDirectory`
- `absolutePath`
- `after`
- `app`
- `appendFile`
- `autostopping`
- `because`
- `build`
- `buildPreviewApp`
- `builtPreviewAppPath`
- `builtStaticDirectory`
- `childProc`
- `child_process`
- `cli`
- `close`
- `code`
- `components`
- `config`
- `console`
- `contents`
- `copy`
- `cwd`
- `delete`
- `deno`
- `dependencies`
- `dependency`
- `dev`
- `devDependencies`
- `dir`
- `directory`
- `directoryPathRelativeToEmailsDirectory`
- `due`
- `dynamic`
- `email`
- `emailDirectory`
- `emailDirectoryMetadata`
- `emailFilenames`
- `emails`
- `emailsDirPath`
- `emailsDirRelativePath`
- `emailsDirectoryAbsolutePath`
- `empty`
- `entries`
- `env`
- `environment`
- `error`
- `errors`
- `esbuild`
- `existing`
- `exists`
- `existsSync`
- `exit`
- `exited`
- `experimental`
- `filePath`
- `filename`
- `files`
- `filter`
- `find`
- `folder`
- `force`
- `forceSSGForEmailPreviews`
- `generateStaticParams`
- `generation`
- `get`
- `getEmailSlugsFromEmailDirectory`
- `getEmailsDirectoryMetadata`
- `getPreviewServerLocation`
- `gets`
- `ignoreBuildErrors`
- `imports`
- `include`
- `install`
- `interface`
- `into`
- `join`
- `json`
- `layout`
- `length`
- `location`
- `log`
- `logSymbols`
- `map`
- `metadata`
- `mjs`
- `name`
- `next`
- `nextBuild`
- `nextConfig`
- `nextConfigContents`
- `node`
- `node_modules`
- `normalize`
- `npm`
- `npmInstall`
- `ora`
- `otherwise`
- `package`
- `packageJson`
- `packageJsonPath`
- `packageManager`
- `page`
- `pages`
- `parameters`
- `parse`
- `path`
- `pipe`
- `postbuild`
- `pre`
- `prefixText`
- `prepare`
- `prepared`
- `preview`
- `previewServerLocation`
- `process`
- `promises`
- `properly`
- `public`
- `push`
- `quiet`
- `react`
- `readFile`
- `recursive`
- `register`
- `registerSpinnerAutostopping`
- `reject`
- `removeForceDynamic`
- `replace`
- `resolve`
- `run`
- `scripts`
- `segment`
- `segments`
- `sep`
- `server`
- `serverExternalPackages`
- `setNextEnvironmentVariablesForBuild`
- `shell`
- `side`
- `silent`
- `slashes`
- `slug`
- `slugs`
- `some`
- `sometimes`
- `source`
- `spawn`
- `spinner`
- `split`
- `src`
- `start`
- `static`
- `staticPath`
- `stderr`
- `stdout`
- `stopAndPersist`
- `string`
- `stringify`
- `subDirectories`
- `success`
- `symbol`
- `symbols`
- `tailwind`
- `test`
- `text`
- `trailing`
- `trim`
- `tsx`
- `turbo`
- `type`
- `typescript`
- `updatePackageJson`
- `userProjectLocation`
- `utf8`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

