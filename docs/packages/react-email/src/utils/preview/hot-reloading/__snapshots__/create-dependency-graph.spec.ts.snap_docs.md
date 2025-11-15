# Documentation: create-dependency-graph.spec.ts.snap
**File Path:** `packages/react-email/src/utils/preview/hot-reloading/__snapshots__/create-dependency-graph.spec.ts.snap`
**Language:** Unknown
**Size:** 1,470 bytes
**Lines:** 69
**Generated:** 2025-11-15T20:37:32.564855Z

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

- **Path:** `packages/react-email/src/utils/preview/hot-reloading/__snapshots__/create-dependency-graph.spec.ts.snap`
- **Name:** `create-dependency-graph.spec.ts.snap`
- **Extension:** `.snap`
- **Language:** Unknown
- **Size:** 1,470 bytes (1.44 KB)
- **Lines of Code:** 69

---

## Original Source

```
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`createDependencyGraph() > should have the right initial value for the dependency graph 1`] = `
{
  "../outer.ts": {
    "dependencyPaths": [
      "outer-dependency.ts",
    ],
    "dependentPaths": [
      "general-importing-file.ts",
    ],
    "moduleDependencies": [],
    "path": "../outer.ts",
  },
  "data-to-import.json": {
    "dependencyPaths": [],
    "dependentPaths": [
      "general-importing-file.ts",
    ],
    "moduleDependencies": [],
    "path": "data-to-import.json",
  },
  "file-a.ts": {
    "dependencyPaths": [
      "file-b.ts",
    ],
    "dependentPaths": [
      "file-b.ts",
      "general-importing-file.ts",
    ],
    "moduleDependencies": [],
    "path": "file-a.ts",
  },
  "file-b.ts": {
    "dependencyPaths": [
      "file-a.ts",
    ],
    "dependentPaths": [
      "file-a.ts",
      "general-importing-file.ts",
    ],
    "moduleDependencies": [],
    "path": "file-b.ts",
  },
  "general-importing-file.ts": {
    "dependencyPaths": [
      "../outer.ts",
      "data-to-import.json",
      "file-a.ts",
      "file-b.ts",
    ],
    "dependentPaths": [],
    "moduleDependencies": [
      "node:os",
      "node:path",
    ],
    "path": "general-importing-file.ts",
  },
  "outer-dependency.ts": {
    "dependencyPaths": [],
    "dependentPaths": [
      "../outer.ts",
    ],
    "moduleDependencies": [],
    "path": "outer-dependency.ts",
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

**Total Unique Identifiers:** 26

- `Snapshot`
- `Vitest`
- `createDependencyGraph`
- `data`
- `dependency`
- `dependencyPaths`
- `dependentPaths`
- `dev`
- `exports`
- `file`
- `general`
- `graph`
- `guide`
- `html`
- `https`
- `importing`
- `initial`
- `json`
- `moduleDependencies`
- `node`
- `outer`
- `path`
- `right`
- `snapshot`
- `value`
- `vitest`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

