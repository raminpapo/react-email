# Documentation: send-to-spamd.ts
**File Path:** `apps/web/src/utils/spam-assassin/send-to-spamd.ts`
**Language:** typescript
**Size:** 2,069 bytes
**Lines:** 88
**Generated:** 2025-11-15T20:37:32.815903Z

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

- **Path:** `apps/web/src/utils/spam-assassin/send-to-spamd.ts`
- **Name:** `send-to-spamd.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,069 bytes (2.02 KB)
- **Lines of Code:** 88

---

## Original Source

```typescript
import crypto from 'node:crypto';
import net from 'node:net';

const host = process.env.SPAM_ASSASSIN_HOST;
const port = process.env.SPAM_ASSASSIN_PORT;
const timeout = 10_000;

export const sendToSpamd = (html: string, plainText: string) => {
  return new Promise<string>((resolve, reject) => {
    if (!host || !port) {
      reject(
        new Error('Host and port for spam assassin must be specified', {
          cause: {
            host,
            port,
            html,
            plainText,
          },
        }),
      );
      return;
    }

    const connection = net.createConnection({
      host,
      port: Number.parseInt(port, 10),
    });
    connection.setTimeout(timeout, () => {
      reject(
        new Error('Timed out trying to connect to spamc', {
          cause: {
            port,
            host,
          },
        }),
      );
    });

    connection.on('connect', () => {
      const boundary = `Part_${crypto.randomBytes(16).toString('hex')}`;
      const message = [
        'MIME-Version: 1.0',
        `Content-Type: multipart/alternative; boundary="${boundary}"`,
        '',
        `--${boundary}`,
        'Content-Type: text/html; charset="UTF-8"',
        `Content-Length: ${Buffer.byteLength(html.trim())}`,
        '',
        html.trim(),
        '',
        `--${boundary}`,
        'Content-Type: text/plain; charset="UTF-8"',
        `Content-Length: ${Buffer.byteLength(plainText.trim())}`,
        '',
        plainText.trim(),
        '',
        `--${boundary}--`,
        '',
      ].join('\r\n');

      const command = [
        'PROCESS SPAMC/1.5',
        `Content-length: ${Buffer.byteLength(message)}`,
        '',
        message,
      ].join('\r\n');

      connection.write(command);
    });

    connection.on('error', (error) => {
      reject(error);
    });

    let response = '';

    connection.on('data', (buffer) => {
      response += buffer.toString('utf8');
    });

    connection.on('close', (hadError) => {
      if (hadError) return;

      resolve(response);
    });
  });
};

```

---

## Overview

This is a JavaScript/TypeScript file. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `boundary()`
- `command()`
- `connection()`
- `host()`
- `message()`
- `port()`
- `response()`
- `sendToSpamd()`
- `timeout()`

### Dependencies

This file imports/requires:

- `node:crypto`
- `node:net`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 62

- `Buffer`
- `Content`
- `Error`
- `Host`
- `Length`
- `Number`
- `Promise`
- `SPAM_ASSASSIN_HOST`
- `SPAM_ASSASSIN_PORT`
- `Timed`
- `Type`
- `Version`
- `alternative`
- `assassin`
- `boundary`
- `buffer`
- `byteLength`
- `cause`
- `charset`
- `close`
- `command`
- `connect`
- `connection`
- `createConnection`
- `crypto`
- `data`
- `env`
- `error`
- `hadError`
- `hex`
- `host`
- `html`
- `join`
- `length`
- `message`
- `multipart`
- `must`
- `net`
- `node`
- `out`
- `parseInt`
- `plain`
- `plainText`
- `port`
- `process`
- `randomBytes`
- `reject`
- `resolve`
- `response`
- `sendToSpamd`
- `setTimeout`
- `spam`
- `spamc`
- `specified`
- `string`
- `text`
- `timeout`
- `toString`
- `trim`
- `trying`
- `utf8`
- `write`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

