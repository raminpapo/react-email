# Documentation: create-dependency-graph.spec.ts.snap
**File Path:** `packages/react-email/src/cli/utils/preview/hot-reloading/__snapshots__/create-dependency-graph.spec.ts.snap`
**Language:** Unknown
**Size:** 4,736 bytes
**Lines:** 69
**Generated:** 2025-11-15T20:37:32.577068Z

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

- **Path:** `packages/react-email/src/cli/utils/preview/hot-reloading/__snapshots__/create-dependency-graph.spec.ts.snap`
- **Name:** `create-dependency-graph.spec.ts.snap`
- **Extension:** `.snap`
- **Language:** Unknown
- **Size:** 4,736 bytes (4.62 KB)
- **Lines of Code:** 69

---

## Original Source

```
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`createDependencyGraph() > should have the right initial value for the dependency graph 1`] = `
{
  "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/data-to-import.json": {
    "dependencyPaths": [],
    "dependentPaths": [
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/general-importing-file.ts",
    ],
    "moduleDependencies": [],
    "path": "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/data-to-import.json",
  },
  "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-a.ts": {
    "dependencyPaths": [
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-b.ts",
    ],
    "dependentPaths": [
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-b.ts",
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/general-importing-file.ts",
    ],
    "moduleDependencies": [],
    "path": "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-a.ts",
  },
  "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-b.ts": {
    "dependencyPaths": [
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-a.ts",
    ],
    "dependentPaths": [
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-a.ts",
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/general-importing-file.ts",
    ],
    "moduleDependencies": [],
    "path": "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-b.ts",
  },
  "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/general-importing-file.ts": {
    "dependencyPaths": [
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/outer.ts",
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/data-to-import.json",
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-a.ts",
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/file-b.ts",
    ],
    "dependentPaths": [],
    "moduleDependencies": [
      "node:os",
      "node:path",
    ],
    "path": "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/general-importing-file.ts",
  },
  "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/outer-dependency.ts": {
    "dependencyPaths": [],
    "dependentPaths": [
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/outer.ts",
    ],
    "moduleDependencies": [],
    "path": "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/outer-dependency.ts",
  },
  "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/outer.ts": {
    "dependencyPaths": [
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/outer-dependency.ts",
    ],
    "dependentPaths": [
      "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/inner/general-importing-file.ts",
    ],
    "moduleDependencies": [],
    "path": "/home/gabriel/Projects/resend/react-email/packages/react-email/src/cli/utils/preview/hot-reloading/test/dependency-graph/outer.ts",
  },
}
`;

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 41

- `Projects`
- `Snapshot`
- `Vitest`
- `cli`
- `createDependencyGraph`
- `data`
- `dependency`
- `dependencyPaths`
- `dependentPaths`
- `dev`
- `email`
- `exports`
- `file`
- `gabriel`
- `general`
- `graph`
- `guide`
- `home`
- `hot`
- `html`
- `https`
- `importing`
- `initial`
- `inner`
- `json`
- `moduleDependencies`
- `node`
- `outer`
- `packages`
- `path`
- `preview`
- `react`
- `reloading`
- `resend`
- `right`
- `snapshot`
- `src`
- `test`
- `utils`
- `value`
- `vitest`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

