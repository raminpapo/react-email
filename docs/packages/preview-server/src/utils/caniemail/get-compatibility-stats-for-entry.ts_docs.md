# Documentation: get-compatibility-stats-for-entry.ts
**File Path:** `packages/preview-server/src/utils/caniemail/get-compatibility-stats-for-entry.ts`
**Language:** typescript
**Size:** 3,599 bytes
**Lines:** 119
**Generated:** 2025-11-15T20:37:32.042760Z

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

- **Path:** `packages/preview-server/src/utils/caniemail/get-compatibility-stats-for-entry.ts`
- **Name:** `get-compatibility-stats-for-entry.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 3,599 bytes (3.51 KB)
- **Lines of Code:** 119

---

## Original Source

```typescript
import type {
  EmailClient,
  Platform,
  SupportEntry,
} from '../../actions/email-validation/check-compatibility';

export type SupportStatus = DetailedSupportStatus['status'];

export type DetailedSupportStatus =
  | {
      status: 'success';
    }
  | {
      status: 'error';
    }
  | {
      status: 'warning';
      notes: string;
    };

type EmailClientStats = {
  status: SupportStatus;
  perPlatform: Partial<Record<Platform, DetailedSupportStatus>>;
};

export type CompatibilityStats = {
  status: SupportStatus;
  perEmailClient: Partial<Record<EmailClient, EmailClientStats>>;
};

const noteNumbersRegex = /#(?<noteNumber>\d+)/g;

export const getCompatibilityStatsForEntry = (
  entry: SupportEntry,
  emailClients: EmailClient[],
) => {
  const stats: CompatibilityStats = {
    status: 'success',
    perEmailClient: {},
  };
  for (const emailClient of emailClients) {
    const rawStats = entry.stats[emailClient];
    if (rawStats) {
      const emailClientStats: EmailClientStats = {
        status: 'success',
        perPlatform: {},
      };

      for (const [platform, statusPerVersion] of Object.entries(rawStats)) {
        const latestStatus = statusPerVersion[statusPerVersion.length - 1];
        if (latestStatus === undefined)
          throw new Error(
            'Cannot load in status because there are none recorded for this platform/email client',
            {
              cause: {
                latestStatus,
                statusPerVersion,
                platform,
                emailClient,
                supportEntry: entry,
              },
            },
          );
        const statusString = latestStatus[Object.keys(latestStatus)[0]!]!;
        if (statusString.startsWith('u')) continue;
        if (statusString.startsWith('a')) {
          const notes: string[] = [];
          noteNumbersRegex.lastIndex = 0;
          for (const match of statusString.matchAll(noteNumbersRegex)) {
            if (match.groups?.noteNumber) {
              const { noteNumber } = match.groups;
              const note =
                entry.notes_by_num?.[Number.parseInt(noteNumber, 10)];
              if (note) {
                notes.push(note);
              }
              // else if (isInternalDev) {
              //   console.warn(
              //     'Could not get note by the number for a support entry',
              //     {
              //       platform,
              //       statusString,
              //       note,
              //     },
              //   );
              // }
            }
          }
          if (emailClientStats.status === 'success')
            emailClientStats.status = 'warning';
          if (stats.status === 'success') stats.status = 'warning';
          emailClientStats.perPlatform[platform as Platform] = {
            status: 'warning',
            notes:
              notes.length === 1
                ? notes[0]!
                : notes.map((note) => `- ${note}`).join('\n'),
          };
        } else if (statusString.startsWith('y')) {
          emailClientStats.perPlatform[platform as Platform] = {
            status: 'success',
          };
        } else if (statusString.startsWith('n')) {
          if (emailClientStats.status !== 'error')
            emailClientStats.status = 'error';
          if (stats.status !== 'error') stats.status = 'error';
          emailClientStats.perPlatform[platform as Platform] = {
            status: 'error',
          };
        }
      }

      stats.perEmailClient[emailClient] = emailClientStats;
    }
  }

  return stats;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `getCompatibilityStatsForEntry()`
- `latestStatus()`
- `note()`
- `noteNumbersRegex()`
- `rawStats()`
- `statusString()`

### Type Definitions

- `CompatibilityStats`
- `DetailedSupportStatus`
- `EmailClientStats`
- `SupportStatus`

### Dependencies

This file imports/requires:

- `../../actions/email-validation/check-compatibility`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 67

- `Cannot`
- `CompatibilityStats`
- `DetailedSupportStatus`
- `EmailClient`
- `EmailClientStats`
- `Error`
- `Number`
- `Object`
- `Partial`
- `Platform`
- `Record`
- `SupportEntry`
- `SupportStatus`
- `actions`
- `because`
- `cause`
- `check`
- `client`
- `compatibility`
- `console`
- `email`
- `emailClient`
- `emailClientStats`
- `emailClients`
- `entries`
- `entry`
- `error`
- `get`
- `getCompatibilityStatsForEntry`
- `groups`
- `isInternalDev`
- `join`
- `keys`
- `lastIndex`
- `latestStatus`
- `length`
- `load`
- `map`
- `match`
- `matchAll`
- `note`
- `noteNumber`
- `noteNumbersRegex`
- `notes`
- `notes_by_num`
- `number`
- `parseInt`
- `perEmailClient`
- `perPlatform`
- `platform`
- `push`
- `rawStats`
- `recorded`
- `startsWith`
- `stats`
- `status`
- `statusPerVersion`
- `statusString`
- `string`
- `success`
- `support`
- `supportEntry`
- `there`
- `type`
- `validation`
- `warn`
- `warning`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

