# Documentation: compatibility.tsx
**File Path:** `packages/preview-server/src/components/toolbar/compatibility.tsx`
**Language:** tsx
**Size:** 3,404 bytes
**Lines:** 114
**Generated:** 2025-11-15T20:37:32.172792Z

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

- **Path:** `packages/preview-server/src/components/toolbar/compatibility.tsx`
- **Name:** `compatibility.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,404 bytes (3.32 KB)
- **Lines of Code:** 114

---

## Original Source

```tsx
import { useRef, useState } from 'react';
import { toast } from 'sonner';
import { nicenames } from '../../actions/email-validation/caniemail-data';
import {
  type CompatibilityCheckingResult,
  checkCompatibility,
} from '../../actions/email-validation/check-compatibility';
import { sanitize } from '../../utils';
import { loadStream } from '../../utils/load-stream';
import { IconWarning } from '../icons/icon-warning';
import { CodePreviewLineLink } from './code-preview-line-link';
import { Results } from './results';

export const useCompatibility = ({
  reactMarkup,
  emailPath,

  initialResults,
}: {
  reactMarkup: string;
  emailPath: string;

  initialResults?: CompatibilityCheckingResult[];
}) => {
  const [results, setResults] = useState(initialResults);

  const [loading, setLoading] = useState(false);
  const isLoadingRef = useRef(false);

  const load = async () => {
    if (isLoadingRef.current) return;
    isLoadingRef.current = true;
    setLoading(true);

    setResults([]);
    let rawResults: CompatibilityCheckingResult[] = [];

    try {
      const stream = await checkCompatibility(reactMarkup, emailPath);
      for await (const result of loadStream(stream)) {
        if (result.status !== 'error') continue;
        setResults((current) => {
          if (!current) {
            return [result];
          }
          rawResults = [...current, result];
          return rawResults;
        });
      }
    } catch (exception) {
      console.error(exception);
      toast.error(JSON.stringify(exception));
    } finally {
      setLoading(false);
      isLoadingRef.current = false;
    }

    return rawResults;
  };

  return [results, { loading, load }] as const;
};

interface CompatibilityProps {
  results: CompatibilityCheckingResult[] | undefined;
}

export const Compatibility = ({ results }: CompatibilityProps) => {
  return (
    <Results>
      {results?.map((result, i) => {
        const statsReportedNotWorking = Object.entries(
          result.statsPerEmailClient,
        ).filter(([, stats]) => stats.status === 'error');
        const unsupportedClientsString = statsReportedNotWorking
          .map(([emailClient]) => nicenames.family[emailClient])
          .join(', ');

        return (
          <Results.Row key={i}>
            <Results.Column>
              <span className="flex text-red-400 uppercase gap-2 items-center">
                <IconWarning />
                {sanitize(result.entry.title)}
              </span>
            </Results.Column>
            <Results.Column>
              {statsReportedNotWorking.length > 0
                ? `Not supported in ${unsupportedClientsString}`
                : null}

              <a
                href={result.entry.url}
                className="underline ml-2 decoration-slate-9 decoration-1 hover:decoration-slate-11 transition-colors hover:text-slate-12"
                rel="noreferrer"
                target="_blank"
              >
                More ↗
              </a>
            </Results.Column>
            <Results.Column className="font-mono text-slate-11 text-right">
              <CodePreviewLineLink
                line={result.location.start.line}
                column={result.location.start.column}
                type="react"
              />
            </Results.Column>
          </Results.Row>
        );
      })}
    </Results>
  );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Compatibility()`
- `isLoadingRef()`
- `load()`
- `statsReportedNotWorking()`
- `stream()`
- `unsupportedClientsString()`
- `useCompatibility()`

### Interfaces

- `CompatibilityProps`

### Type Definitions

- `CompatibilityCheckingResult`

### Dependencies

This file imports/requires:

- `../../actions/email-validation/caniemail-data`
- `../../actions/email-validation/check-compatibility`
- `../../utils`
- `../../utils/load-stream`
- `../icons/icon-warning`
- `./code-preview-line-link`
- `./results`
- `react`
- `sonner`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 98

- `CodePreviewLineLink`
- `Column`
- `Compatibility`
- `CompatibilityCheckingResult`
- `CompatibilityProps`
- `IconWarning`
- `More`
- `Object`
- `Results`
- `Row`
- `_blank`
- `actions`
- `caniemail`
- `center`
- `check`
- `checkCompatibility`
- `className`
- `code`
- `colors`
- `column`
- `compatibility`
- `console`
- `current`
- `data`
- `decoration`
- `email`
- `emailClient`
- `emailPath`
- `entries`
- `entry`
- `error`
- `exception`
- `family`
- `filter`
- `flex`
- `font`
- `gap`
- `hover`
- `href`
- `icon`
- `icons`
- `initialResults`
- `interface`
- `isLoadingRef`
- `items`
- `join`
- `key`
- `length`
- `line`
- `link`
- `load`
- `loadStream`
- `loading`
- `location`
- `map`
- `mono`
- `nicenames`
- `noreferrer`
- `preview`
- `rawResults`
- `react`
- `reactMarkup`
- `red`
- `rel`
- `result`
- `results`
- `right`
- `sanitize`
- `setLoading`
- `setResults`
- `slate`
- `sonner`
- `span`
- `start`
- `stats`
- `statsPerEmailClient`
- `statsReportedNotWorking`
- `status`
- `stream`
- `string`
- `stringify`
- `supported`
- `target`
- `text`
- `title`
- `toast`
- `transition`
- `type`
- `underline`
- `unsupportedClientsString`
- `uppercase`
- `url`
- `useCompatibility`
- `useRef`
- `useState`
- `utils`
- `validation`
- `warning`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

