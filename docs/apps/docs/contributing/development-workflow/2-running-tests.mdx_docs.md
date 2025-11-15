# Documentation: 2-running-tests.mdx
**File Path:** `apps/docs/contributing/development-workflow/2-running-tests.mdx`
**Language:** Unknown
**Size:** 1,444 bytes
**Lines:** 27
**Generated:** 2025-11-15T20:37:32.724274Z

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

- **Path:** `apps/docs/contributing/development-workflow/2-running-tests.mdx`
- **Name:** `2-running-tests.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,444 bytes (1.41 KB)
- **Lines of Code:** 27

---

## Original Source

```
---
title: 'Running tests'
sidebarTitle: '2. Running tests'
'og:image': 'https://react.email/static/covers/react-email.png'
description: 'Everything you need to know about our testing setup and strategy'
---

For testing, we use [vitest](https://vitest.dev/). We prefer to define globals and run tests under the `happy-dom` environment.

<Note>
The `@react-email/render` package's `renderAsync` does a fair bit of magic to simulate `edge` and other environments that are not supported by `happy-dom`. For this use case, we override the [environment on a per-file basis](https://vitest.dev/guide/environment#environments-for-specific-files) for its tests
</Note>

We do not strictly enforce testing coverage, but encourage it. A good rule of thumb is that if you need to simulate use
cases to check whether a specific portion of code works, you should split it into a function with a matching unit test.

After you have gone through the [setup](/contributing/development-workflow/1-setup) run
`pnpm test` inside any package. This will run the tests only once. We have two
scripts defined on our packages for testing:

- `pnpm test`: Runs all the tests once. If you run it on the root, it will run the
  tests for all packages using
  [turborepo](/contributing/codebase-overview#turborepo)
- `pnpm test:watch`: Runs all the tests and watches for changes. Vitest
  automatically only runs the tests that are affected by the code you've
  changed.

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 100

- `After`
- `Everything`
- `Note`
- `Running`
- `Runs`
- `Vitest`
- `about`
- `affected`
- `all`
- `any`
- `automatically`
- `basis`
- `bit`
- `cases`
- `changed`
- `changes`
- `check`
- `code`
- `codebase`
- `contributing`
- `coverage`
- `covers`
- `define`
- `defined`
- `description`
- `dev`
- `development`
- `dom`
- `edge`
- `email`
- `encourage`
- `enforce`
- `environment`
- `environments`
- `fair`
- `file`
- `files`
- `globals`
- `gone`
- `good`
- `guide`
- `happy`
- `https`
- `image`
- `inside`
- `into`
- `its`
- `know`
- `magic`
- `matching`
- `need`
- `once`
- `only`
- `other`
- `our`
- `override`
- `overview`
- `package`
- `packages`
- `per`
- `png`
- `pnpm`
- `portion`
- `prefer`
- `react`
- `render`
- `renderAsync`
- `root`
- `rule`
- `run`
- `runs`
- `scripts`
- `setup`
- `sidebarTitle`
- `simulate`
- `specific`
- `split`
- `static`
- `strategy`
- `strictly`
- `supported`
- `test`
- `testing`
- `tests`
- `through`
- `thumb`
- `title`
- `turborepo`
- `two`
- `under`
- `unit`
- `use`
- `using`
- `vitest`
- `watch`
- `watches`
- `whether`
- `workflow`
- `works`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

