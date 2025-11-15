# Documentation: static-node-modules-for-vm.ts
**File Path:** `packages/preview-server/src/utils/static-node-modules-for-vm.ts`
**Language:** typescript
**Size:** 2,393 bytes
**Lines:** 94
**Generated:** 2025-11-15T20:37:32.036263Z

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

- **Path:** `packages/preview-server/src/utils/static-node-modules-for-vm.ts`
- **Name:** `static-node-modules-for-vm.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,393 bytes (2.34 KB)
- **Lines of Code:** 94

---

## Original Source

```typescript
import assert from 'node:assert';
import asyncHooks from 'node:async_hooks';
import buffer from 'node:buffer';
import childProcess from 'node:child_process';
import cluster from 'node:cluster';
import console from 'node:console';
import constants from 'node:constants';
import crypto from 'node:crypto';
import dgram from 'node:dgram';
import diagnosticsChannel from 'node:diagnostics_channel';
import dns from 'node:dns';
import domain from 'node:domain';
import events from 'node:events';
import fs from 'node:fs';
import fsPromises from 'node:fs/promises';
import http from 'node:http';
import http2 from 'node:http2';
import https from 'node:https';
import inspector from 'node:inspector';
import module from 'node:module';
import net from 'node:net';
import os from 'node:os';
import path from 'node:path';
import perfHooks from 'node:perf_hooks';
import process from 'node:process';
import querystring from 'node:querystring';
import readline from 'node:readline';
import repl from 'node:repl';
import stream from 'node:stream';
import stringDecoder from 'node:string_decoder';
import timers from 'node:timers';
import timersPromises from 'node:timers/promises';
import tls from 'node:tls';
import tty from 'node:tty';
import url from 'node:url';
import util from 'node:util';
import utilTypes from 'node:util/types';
import v8 from 'node:v8';
import vm from 'node:vm';
import workerThreads from 'node:worker_threads';
import zlib from 'node:zlib';
// See https://github.com/resend/react-email/issues/1841#issuecomment-2589985562
import punycode from 'module-punycode';

/**
 * A map of the name of the modules (including `node:` prefixed ones)
 * provided by Node because dynamic requires of them, even on the server
 * will not be resolved properly
 */
export const staticNodeModulesForVM = {
  assert,
  async_hooks: asyncHooks,
  buffer,
  child_process: childProcess,
  cluster,
  console,
  constants,
  crypto,
  dgram,
  diagnostics_channel: diagnosticsChannel,
  dns,
  domain,
  events,
  fs,
  'fs/promises': fsPromises,
  http,
  http2,
  https,
  inspector,
  module,
  net,
  os,
  path,
  perf_hooks: perfHooks,
  process,
  punycode,
  querystring,
  readline,
  repl,
  stream,
  string_decoder: stringDecoder,
  timers,
  'timers/promises': timersPromises,
  tls,
  tty,
  url,
  util,
  'util/types': utilTypes,
  v8,
  vm,
  worker_threads: workerThreads,
  zlib,
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `staticNodeModulesForVM()`

### Dependencies

This file imports/requires:

- `module-punycode`
- `node:assert`
- `node:async_hooks`
- `node:buffer`
- `node:child_process`
- `node:cluster`
- `node:console`
- `node:constants`
- `node:crypto`
- `node:dgram`
- `node:diagnostics_channel`
- `node:dns`
- `node:domain`
- `node:events`
- `node:fs`
- `node:fs/promises`
- `node:http`
- `node:http2`
- `node:https`
- `node:inspector`
- `node:module`
- `node:net`
- `node:os`
- `node:path`
- `node:perf_hooks`
- `node:process`
- `node:querystring`
- `node:readline`
- `node:repl`
- `node:stream`
- `node:string_decoder`
- `node:timers`
- `node:timers/promises`
- `node:tls`
- `node:tty`
- `node:url`
- `node:util`
- `node:util/types`
- `node:v8`
- `node:vm`
- `node:worker_threads`
- `node:zlib`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 72

- `Node`
- `See`
- `assert`
- `asyncHooks`
- `async_hooks`
- `because`
- `buffer`
- `childProcess`
- `child_process`
- `cluster`
- `com`
- `console`
- `constants`
- `crypto`
- `dgram`
- `diagnosticsChannel`
- `diagnostics_channel`
- `dns`
- `domain`
- `dynamic`
- `email`
- `even`
- `events`
- `fsPromises`
- `github`
- `http`
- `http2`
- `https`
- `including`
- `inspector`
- `issuecomment`
- `issues`
- `map`
- `module`
- `modules`
- `name`
- `net`
- `node`
- `ones`
- `path`
- `perfHooks`
- `perf_hooks`
- `prefixed`
- `process`
- `promises`
- `properly`
- `provided`
- `punycode`
- `querystring`
- `react`
- `readline`
- `repl`
- `requires`
- `resend`
- `resolved`
- `server`
- `staticNodeModulesForVM`
- `stream`
- `stringDecoder`
- `string_decoder`
- `them`
- `timers`
- `timersPromises`
- `tls`
- `tty`
- `types`
- `url`
- `util`
- `utilTypes`
- `workerThreads`
- `worker_threads`
- `zlib`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

