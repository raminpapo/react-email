# Documentation: start-dev-server.ts
**File Path:** `packages/react-email/src/utils/preview/start-dev-server.ts`
**Language:** typescript
**Size:** 6,489 bytes
**Lines:** 237
**Generated:** 2025-11-15T20:37:32.549867Z

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

- **Path:** `packages/react-email/src/utils/preview/start-dev-server.ts`
- **Name:** `start-dev-server.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 6,489 bytes (6.34 KB)
- **Lines of Code:** 237

---

## Original Source

```typescript
import http from 'node:http';
import path from 'node:path';
import url from 'node:url';
import { createJiti } from 'jiti';
import logSymbols from 'log-symbols';
import ora from 'ora';
import { registerSpinnerAutostopping } from '../../utils/register-spinner-autostopping.js';
import { conf } from '../conf.js';
import { getPreviewServerLocation } from '../get-preview-server-location.js';
import { packageJson } from '../packageJson.js';
import { styleText } from '../style-text.js';
import { getEnvVariablesForPreviewApp } from './get-env-variables-for-preview-app.js';
import { serveStaticFile } from './serve-static-file.js';

let devServer: http.Server | undefined;

const safeAsyncServerListen = (server: http.Server, port: number) => {
  return new Promise<{ portAlreadyInUse: boolean }>((resolve) => {
    server.listen(port, () => {
      resolve({ portAlreadyInUse: false });
    });

    server.on('error', (e: NodeJS.ErrnoException) => {
      if (e.code === 'EADDRINUSE') {
        resolve({ portAlreadyInUse: true });
      }
    });
  });
};

export const startDevServer = async (
  emailsDirRelativePath: string,
  staticBaseDirRelativePath: string,
  port: number,
): Promise<http.Server> => {
  const [majorNodeVersion] = process.versions.node.split('.');
  if (majorNodeVersion && Number.parseInt(majorNodeVersion, 10) < 20) {
    console.error(
      ` ${logSymbols.error}  Node ${majorNodeVersion} is not supported. Please upgrade to Node 20 or higher.`,
    );
    process.exit(1);
  }

  const previewServerLocation = await getPreviewServerLocation();
  const previewServer = createJiti(previewServerLocation);

  devServer = http.createServer((req, res) => {
    if (!req.url) {
      res.end(404);
      return;
    }

    const parsedUrl = url.parse(req.url, true);

    // Never cache anything to avoid
    res.setHeader(
      'Cache-Control',
      'no-cache, max-age=0, must-revalidate, no-store',
    );
    res.setHeader('Pragma', 'no-cache');
    res.setHeader('Expires', '-1');

    try {
      if (
        parsedUrl.path?.includes('static/') &&
        !parsedUrl.path.includes('_next/static/')
      ) {
        void serveStaticFile(res, parsedUrl, staticBaseDirRelativePath);
      } else if (!isNextReady) {
        void nextReadyPromise.then(() =>
          nextHandleRequest?.(req, res, parsedUrl),
        );
      } else {
        void nextHandleRequest?.(req, res, parsedUrl);
      }
    } catch (e) {
      console.error('caught error', e);

      res.writeHead(500);
      res.end();
    }
  });

  const { portAlreadyInUse } = await safeAsyncServerListen(devServer, port);

  if (!portAlreadyInUse) {
    console.log(
      styleText('greenBright', `    React Email ${packageJson.version}`),
    );
    console.log(`    Running preview at:          http://localhost:${port}\n`);
  } else {
    const nextPortToTry = port + 1;
    console.warn(
      ` ${logSymbols.warning} Port ${port} is already in use, trying ${nextPortToTry}`,
    );
    return startDevServer(
      emailsDirRelativePath,
      staticBaseDirRelativePath,
      nextPortToTry,
    );
  }

  devServer.on('close', async () => {
    await app.close();
  });

  devServer.on('error', (e: NodeJS.ErrnoException) => {
    spinner.stopAndPersist({
      symbol: logSymbols.error,
      text: `Preview Server had an error: ${e}`,
    });
    process.exit(1);
  });

  const spinner = ora({
    text: 'Getting react-email preview server ready...\n',
    prefixText: ' ',
  }).start();

  registerSpinnerAutostopping(spinner);
  const timeBeforeNextReady = performance.now();

  // these environment variables are used on the next app
  // this is the most reliable way of communicating these paths through
  process.env = {
    NODE_ENV: 'development',
    ...(process.env as Omit<NodeJS.ProcessEnv, 'NODE_ENV'> & {
      NODE_ENV?: NodeJS.ProcessEnv['NODE_ENV'];
    }),
    ...getEnvVariablesForPreviewApp(
      // If we don't do normalization here, stuff like https://github.com/resend/react-email/issues/1354 happens.
      path.normalize(emailsDirRelativePath),
      previewServerLocation,
      process.cwd(),
      conf.get('resendApiKey'),
    ),
  };

  const next = await previewServer.import<typeof import('next')['default']>(
    'next',
    {
      default: true,
    },
  );

  const app = next({
    // passing in env here does not get the environment variables there
    dev: false,
    conf: {
      images: {
        // This is to avoid the warning with sharp
        unoptimized: true,
      },
    },
    hostname: 'localhost',
    port,
    dir: previewServerLocation,
  });

  let isNextReady = false;
  const nextReadyPromise = app.prepare();
  try {
    await nextReadyPromise;
  } catch (exception) {
    spinner.stopAndPersist({
      symbol: logSymbols.error,
      text: ` Preview Server had an error: ${exception}`,
    });
    process.exit(1);
  }
  isNextReady = true;

  const nextHandleRequest:
    | ReturnType<typeof app.getRequestHandler>
    | undefined = app.getRequestHandler();

  const secondsToNextReady = (
    (performance.now() - timeBeforeNextReady) /
    1000
  ).toFixed(1);

  spinner.stopAndPersist({
    text: `Ready in ${secondsToNextReady}s\n`,
    symbol: logSymbols.success,
  });

  return devServer;
};

// based on https://stackoverflow.com/a/14032965
const makeExitHandler =
  (
    options?:
      | { shouldKillProcess: false }
      | { shouldKillProcess: true; killWithErrorCode: boolean },
  ) =>
  (codeSignalOrError: number | NodeJS.Signals | Error) => {
    if (typeof devServer !== 'undefined') {
      console.log('\nshutting down dev server');
      devServer.close();
      devServer = undefined;
    }

    if (codeSignalOrError instanceof Error) {
      console.error(codeSignalOrError);
    }

    if (options?.shouldKillProcess) {
      process.exit(options.killWithErrorCode ? 1 : 0);
    }
  };

// do something when app is closing
process.on('exit', makeExitHandler());

// catches ctrl+c event
process.on(
  'SIGINT',
  makeExitHandler({ shouldKillProcess: true, killWithErrorCode: false }),
);

//  catches "kill pid" (for example: nodemon restart)
process.on(
  'SIGUSR1',
  makeExitHandler({ shouldKillProcess: true, killWithErrorCode: false }),
);
process.on(
  'SIGUSR2',
  makeExitHandler({ shouldKillProcess: true, killWithErrorCode: false }),
);

// catches uncaught exceptions
process.on(
  'uncaughtException',
  makeExitHandler({ shouldKillProcess: true, killWithErrorCode: true }),
);

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `app()`
- `isNextReady()`
- `makeExitHandler()`
- `next()`
- `nextPortToTry()`
- `nextReadyPromise()`
- `parsedUrl()`
- `previewServer()`
- `previewServerLocation()`
- `safeAsyncServerListen()`
- `secondsToNextReady()`
- `spinner()`
- `startDevServer()`
- `timeBeforeNextReady()`

### Dependencies

This file imports/requires:

- `../../utils/register-spinner-autostopping.js`
- `../conf.js`
- `../get-preview-server-location.js`
- `../packageJson.js`
- `../style-text.js`
- `./get-env-variables-for-preview-app.js`
- `./serve-static-file.js`
- `jiti`
- `log-symbols`
- `node:http`
- `node:path`
- `node:url`
- `ora`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 192

- `Cache`
- `Control`
- `Email`
- `ErrnoException`
- `Error`
- `Expires`
- `Getting`
- `NODE_ENV`
- `Never`
- `Node`
- `NodeJS`
- `Number`
- `Omit`
- `Please`
- `Port`
- `Pragma`
- `Preview`
- `ProcessEnv`
- `Promise`
- `React`
- `Ready`
- `ReturnType`
- `Running`
- `SIGUSR1`
- `SIGUSR2`
- `Server`
- `Signals`
- `_next`
- `age`
- `already`
- `anything`
- `app`
- `autostopping`
- `avoid`
- `based`
- `boolean`
- `cache`
- `catches`
- `caught`
- `close`
- `closing`
- `code`
- `codeSignalOrError`
- `com`
- `communicating`
- `conf`
- `console`
- `createJiti`
- `createServer`
- `ctrl`
- `cwd`
- `dev`
- `devServer`
- `development`
- `dir`
- `don`
- `down`
- `email`
- `emailsDirRelativePath`
- `end`
- `env`
- `environment`
- `error`
- `event`
- `example`
- `exception`
- `exceptions`
- `exit`
- `file`
- `get`
- `getEnvVariablesForPreviewApp`
- `getPreviewServerLocation`
- `getRequestHandler`
- `github`
- `greenBright`
- `happens`
- `here`
- `higher`
- `hostname`
- `http`
- `https`
- `images`
- `includes`
- `isNextReady`
- `issues`
- `jiti`
- `kill`
- `killWithErrorCode`
- `like`
- `listen`
- `localhost`
- `location`
- `log`
- `logSymbols`
- `majorNodeVersion`
- `makeExitHandler`
- `max`
- `most`
- `must`
- `next`
- `nextHandleRequest`
- `nextPortToTry`
- `nextReadyPromise`
- `node`
- `nodemon`
- `normalization`
- `normalize`
- `now`
- `nshutting`
- `number`
- `options`
- `ora`
- `packageJson`
- `parse`
- `parseInt`
- `parsedUrl`
- `passing`
- `path`
- `paths`
- `performance`
- `pid`
- `port`
- `portAlreadyInUse`
- `prefixText`
- `prepare`
- `preview`
- `previewServer`
- `previewServerLocation`
- `process`
- `react`
- `ready`
- `register`
- `registerSpinnerAutostopping`
- `reliable`
- `req`
- `res`
- `resend`
- `resendApiKey`
- `resolve`
- `restart`
- `revalidate`
- `safeAsyncServerListen`
- `secondsToNextReady`
- `serve`
- `serveStaticFile`
- `server`
- `setHeader`
- `sharp`
- `shouldKillProcess`
- `something`
- `spinner`
- `split`
- `stackoverflow`
- `start`
- `startDevServer`
- `static`
- `staticBaseDirRelativePath`
- `stopAndPersist`
- `store`
- `string`
- `stuff`
- `style`
- `styleText`
- `success`
- `supported`
- `symbol`
- `symbols`
- `text`
- `then`
- `there`
- `these`
- `through`
- `timeBeforeNextReady`
- `toFixed`
- `trying`
- `uncaught`
- `uncaughtException`
- `unoptimized`
- `upgrade`
- `url`
- `use`
- `used`
- `utils`
- `variables`
- `version`
- `versions`
- `void`
- `warn`
- `warning`
- `way`
- `when`
- `writeHead`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

