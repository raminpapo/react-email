# Documentation: page.tsx
**File Path:** `packages/preview-server/src/app/preview/[...slug]/page.tsx`
**Language:** tsx
**Size:** 5,099 bytes
**Lines:** 162
**Generated:** 2025-11-15T20:37:32.092521Z

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

- **Path:** `packages/preview-server/src/app/preview/[...slug]/page.tsx`
- **Name:** `page.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 5,099 bytes (4.98 KB)
- **Lines of Code:** 162

---

## Original Source

```tsx
import path from 'node:path';
import { redirect } from 'next/navigation';
import { Suspense } from 'react';
import {
  type CompatibilityCheckingResult,
  checkCompatibility,
} from '../../../actions/email-validation/check-compatibility';
import { getEmailPathFromSlug } from '../../../actions/get-email-path-from-slug';
import { renderEmailByPath } from '../../../actions/render-email-by-path';
import { Shell } from '../../../components/shell';
import { Toolbar } from '../../../components/toolbar';
import type { LintingRow } from '../../../components/toolbar/linter';
import type { SpamCheckingResult } from '../../../components/toolbar/spam-assassin';
import { PreviewProvider } from '../../../contexts/preview';
import { ToolbarProvider } from '../../../contexts/toolbar';
import { getEmailsDirectoryMetadata } from '../../../utils/get-emails-directory-metadata';
import { getLintingSources, loadLintingRowsFrom } from '../../../utils/linting';
import { loadStream } from '../../../utils/load-stream';
import {
  emailsDirectoryAbsolutePath,
  isBuilding,
  resendApiKey,
} from '../../env';
import Preview from './preview';

export const dynamicParams = true;

export const dynamic = 'force-dynamic';

export interface PreviewParams {
  slug: string[];
}

export default async function Page({
  params: paramsPromise,
}: {
  params: Promise<PreviewParams>;
}) {
  const params = await paramsPromise;
  // will come in here as segments of a relative path to the email
  // ex: ['authentication', 'verify-password.tsx']
  const slug = decodeURIComponent(params.slug.join('/'));
  const emailsDirMetadata = await getEmailsDirectoryMetadata(
    emailsDirectoryAbsolutePath,
  );

  if (typeof emailsDirMetadata === 'undefined') {
    throw new Error(
      `Could not find the emails directory specified under ${emailsDirectoryAbsolutePath}!

This is most likely not an issue with the preview server. Maybe there was a typo on the "--dir" flag?`,
    );
  }

  let emailPath: string;
  try {
    emailPath = await getEmailPathFromSlug(slug);
  } catch (exception) {
    if (exception instanceof Error) {
      console.warn(exception.message);
      redirect('/');
    }
    throw exception;
  }

  const serverEmailRenderingResult = await renderEmailByPath(emailPath);

  let spamCheckingResult: SpamCheckingResult | undefined;
  let lintingRows: LintingRow[] | undefined;
  let compatibilityCheckingResults: CompatibilityCheckingResult[] | undefined;

  if (isBuilding) {
    if ('error' in serverEmailRenderingResult) {
      throw new Error(serverEmailRenderingResult.error.message, {
        cause: serverEmailRenderingResult.error,
      });
    }
    const lintingSources = getLintingSources(
      serverEmailRenderingResult.prettyMarkup,
      '',
    );
    lintingRows = [];
    for await (const row of loadLintingRowsFrom(lintingSources)) {
      lintingRows.push(row);
    }
    lintingRows.sort((a, b) => {
      if (a.result.status === 'error' && b.result.status === 'warning') {
        return -1;
      }

      if (a.result.status === 'warning' && b.result.status === 'error') {
        return 1;
      }

      return 0;
    });
    compatibilityCheckingResults = [];
    for await (const result of loadStream(
      await checkCompatibility(
        serverEmailRenderingResult.reactMarkup,
        emailPath,
      ),
    )) {
      compatibilityCheckingResults.push(result);
    }

    const response = await fetch('https://react.email/api/check-spam', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        html: serverEmailRenderingResult.prettyMarkup,
        plainText: serverEmailRenderingResult.plainText,
      }),
    });
    const responseBody = (await response.json()) as
      | { error: string }
      | SpamCheckingResult;
    if ('error' in responseBody) {
      throw new Error(`Failed doing Spam Check. ${responseBody.error}`, {
        cause: responseBody,
      });
    }

    spamCheckingResult = responseBody;
  }

  return (
    <PreviewProvider
      emailSlug={slug}
      emailPath={emailPath}
      serverRenderingResult={serverEmailRenderingResult}
    >
      <Shell currentEmailOpenSlug={slug}>
        {/* This suspense is so that this page doesn't throw warnings */}
        {/* on the build of the preview server de-opting into         */}
        {/* client-side rendering on build                            */}
        <Suspense>
          <Preview emailTitle={path.basename(emailPath)} />

          <ToolbarProvider hasApiKey={(resendApiKey ?? '').trim().length > 0}>
            <Toolbar
              serverLintingRows={lintingRows}
              serverSpamCheckingResult={spamCheckingResult}
              serverCompatibilityResults={compatibilityCheckingResults}
            />
          </ToolbarProvider>
        </Suspense>
      </Shell>
    </PreviewProvider>
  );
}

export async function generateMetadata({
  params,
}: {
  params: Promise<PreviewParams>;
}) {
  const { slug } = await params;

  return { title: `${path.basename(slug.join('/'))} — React Email` };
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Page()`
- `dynamic()`
- `dynamicParams()`
- `emailsDirMetadata()`
- `generateMetadata()`
- `lintingSources()`
- `params()`
- `response()`
- `responseBody()`
- `serverEmailRenderingResult()`
- `slug()`

### Interfaces

- `PreviewParams`

### Type Definitions

- `CompatibilityCheckingResult`

### Dependencies

This file imports/requires:

- `../../../actions/email-validation/check-compatibility`
- `../../../actions/get-email-path-from-slug`
- `../../../actions/render-email-by-path`
- `../../../components/shell`
- `../../../components/toolbar`
- `../../../components/toolbar/linter`
- `../../../components/toolbar/spam-assassin`
- `../../../contexts/preview`
- `../../../contexts/toolbar`
- `../../../utils/get-emails-directory-metadata`
- `../../../utils/linting`
- `../../../utils/load-stream`
- `../../env`
- `./preview`
- `next/navigation`
- `node:path`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 148

- `Check`
- `CompatibilityCheckingResult`
- `Content`
- `Email`
- `Error`
- `Failed`
- `LintingRow`
- `Maybe`
- `Page`
- `Preview`
- `PreviewParams`
- `PreviewProvider`
- `Promise`
- `React`
- `Shell`
- `Spam`
- `SpamCheckingResult`
- `Suspense`
- `Toolbar`
- `ToolbarProvider`
- `Type`
- `actions`
- `api`
- `application`
- `assassin`
- `authentication`
- `basename`
- `body`
- `build`
- `cause`
- `check`
- `checkCompatibility`
- `client`
- `come`
- `compatibility`
- `compatibilityCheckingResults`
- `components`
- `console`
- `contexts`
- `currentEmailOpenSlug`
- `decodeURIComponent`
- `dir`
- `directory`
- `doesn`
- `doing`
- `dynamic`
- `dynamicParams`
- `email`
- `emailPath`
- `emailSlug`
- `emailTitle`
- `emails`
- `emailsDirMetadata`
- `emailsDirectoryAbsolutePath`
- `env`
- `error`
- `exception`
- `fetch`
- `find`
- `flag`
- `force`
- `generateMetadata`
- `get`
- `getEmailPathFromSlug`
- `getEmailsDirectoryMetadata`
- `getLintingSources`
- `hasApiKey`
- `headers`
- `here`
- `html`
- `https`
- `interface`
- `into`
- `isBuilding`
- `issue`
- `join`
- `json`
- `length`
- `likely`
- `linter`
- `linting`
- `lintingRows`
- `lintingSources`
- `load`
- `loadLintingRowsFrom`
- `loadStream`
- `message`
- `metadata`
- `method`
- `most`
- `navigation`
- `next`
- `node`
- `opting`
- `page`
- `params`
- `paramsPromise`
- `password`
- `path`
- `plainText`
- `prettyMarkup`
- `preview`
- `push`
- `react`
- `reactMarkup`
- `redirect`
- `relative`
- `render`
- `renderEmailByPath`
- `rendering`
- `resendApiKey`
- `response`
- `responseBody`
- `result`
- `row`
- `segments`
- `server`
- `serverCompatibilityResults`
- `serverEmailRenderingResult`
- `serverLintingRows`
- `serverRenderingResult`
- `serverSpamCheckingResult`
- `shell`
- `side`
- `slug`
- `sort`
- `spam`
- `spamCheckingResult`
- `specified`
- `status`
- `stream`
- `string`
- `stringify`
- `suspense`
- `there`
- `title`
- `toolbar`
- `trim`
- `tsx`
- `type`
- `typo`
- `under`
- `utils`
- `validation`
- `verify`
- `warn`
- `warning`
- `warnings`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

