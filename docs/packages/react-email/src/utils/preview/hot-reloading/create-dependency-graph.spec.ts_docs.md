# Documentation: create-dependency-graph.spec.ts
**File Path:** `packages/react-email/src/utils/preview/hot-reloading/create-dependency-graph.spec.ts`
**Language:** typescript
**Size:** 4,891 bytes
**Lines:** 147
**Generated:** 2025-11-15T20:37:32.552251Z

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

- **Path:** `packages/react-email/src/utils/preview/hot-reloading/create-dependency-graph.spec.ts`
- **Name:** `create-dependency-graph.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 4,891 bytes (4.78 KB)
- **Lines of Code:** 147

---

## Original Source

```typescript
import { existsSync, promises as fs } from 'node:fs';
import path from 'node:path';
import {
  createDependencyGraph,
  type DependencyGraph,
} from './create-dependency-graph.js';

const testingDiretctory = path.join(__dirname, './test/dependency-graph/inner');

const pathToTemporaryFile = path.join(
  testingDiretctory,
  './.temporary-file.ts',
);

vi.mock('@babel/traverse', async () => {
  const traverse = await vi.importActual('@babel/traverse');
  return { default: traverse };
});

describe('createDependencyGraph()', async () => {
  if (existsSync(pathToTemporaryFile)) {
    await fs.rm(pathToTemporaryFile);
  }

  const [dependencyGraph, updateDependencyGraph, { resolveDependentsOf }] =
    await createDependencyGraph(testingDiretctory);

  const toAbsolute = (relativePath: string) => {
    return path.resolve(testingDiretctory, relativePath);
  };

  it.sequential(
    'should resolve dependents when there are circular dependencies',
    async () => {
      expect(resolveDependentsOf(toAbsolute('file-a.ts'))).toEqual([
        toAbsolute('file-b.ts'),
        toAbsolute('general-importing-file.ts'),
      ]);
    },
  );

  it.sequential(
    'should have the right initial value for the dependency graph',
    () => {
      const relativePathDependencyGraph = Object.fromEntries(
        Object.entries(dependencyGraph).map(([key, value]) => {
          return [
            path.relative(testingDiretctory, key),
            {
              path: path.relative(testingDiretctory, value.path),
              dependentPaths: value.dependentPaths.map((p) =>
                path.relative(testingDiretctory, p),
              ),
              dependencyPaths: value.dependencyPaths.map((p) =>
                path.relative(testingDiretctory, p),
              ),
              moduleDependencies: value.moduleDependencies,
            },
          ];
        }),
      );
      expect(relativePathDependencyGraph).toMatchSnapshot();
    },
  );

  it.sequential('should work when adding a new file', async () => {
    await fs.writeFile(
      pathToTemporaryFile,
      `
import {} from './file-a';
import {} from './file-b';
import {} from './general-importing-file';
`,
      'utf8',
    );
    await updateDependencyGraph('add', pathToTemporaryFile);
    expect(dependencyGraph[pathToTemporaryFile]).toEqual({
      path: pathToTemporaryFile,
      dependentPaths: [],
      dependencyPaths: [
        toAbsolute('file-a.ts'),
        toAbsolute('file-b.ts'),
        toAbsolute('general-importing-file.ts'),
      ],
      moduleDependencies: [],
    } satisfies DependencyGraph[number]);
    expect(dependencyGraph[toAbsolute('file-a.ts')]?.dependentPaths).toContain(
      pathToTemporaryFile,
    );
    expect(dependencyGraph[toAbsolute('file-b.ts')]?.dependentPaths).toContain(
      pathToTemporaryFile,
    );
    expect(
      dependencyGraph[toAbsolute('general-importing-file.ts')]?.dependentPaths,
    ).toContain(pathToTemporaryFile);
  });

  it.sequential('should work when updating a file', async () => {
    await fs.writeFile(
      pathToTemporaryFile,
      `
import {} from './file-a';
import {} from './file-b';
`,
      'utf8',
    );
    await updateDependencyGraph('change', pathToTemporaryFile);
    expect(
      dependencyGraph[pathToTemporaryFile],
      'changed file to have updated dependencyPaths',
    ).toEqual({
      path: pathToTemporaryFile,
      dependentPaths: [],
      dependencyPaths: [toAbsolute('file-a.ts'), toAbsolute('file-b.ts')],
      moduleDependencies: [],
    } satisfies DependencyGraph[number]);
    expect(dependencyGraph[toAbsolute('file-a.ts')]?.dependentPaths).toContain(
      pathToTemporaryFile,
    );
    expect(dependencyGraph[toAbsolute('file-b.ts')]?.dependentPaths).toContain(
      pathToTemporaryFile,
    );
    expect(
      dependencyGraph[toAbsolute('general-importing-file.ts')]?.dependentPaths,
      'when removing dependency on a file, the dependency should have its dependents updated to not have the testing file again',
    ).not.toContain(pathToTemporaryFile);
  });

  it.sequential('should work when unlinking a file', async () => {
    await fs.rm(pathToTemporaryFile);
    await updateDependencyGraph('unlink', pathToTemporaryFile);
    expect(dependencyGraph[pathToTemporaryFile]).toBeUndefined();
    expect(
      dependencyGraph[toAbsolute('file-a.ts')]?.dependentPaths,
      "should remove itself from dependents once it's unlinked",
    ).not.toContain(pathToTemporaryFile);
    expect(
      dependencyGraph[toAbsolute('file-b.ts')]?.dependentPaths,
      "should remove itself from dependents once it's unlinked",
    ).not.toContain(pathToTemporaryFile);
    expect(
      dependencyGraph[toAbsolute('general-importing-file.ts')]?.dependentPaths,
      "should remove itself from dependents once it's unlinked",
    ).not.toContain(pathToTemporaryFile);
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `pathToTemporaryFile()`
- `relativePathDependencyGraph()`
- `testingDiretctory()`
- `toAbsolute()`
- `traverse()`

### Type Definitions

- `DependencyGraph`

### Dependencies

This file imports/requires:

- `./create-dependency-graph.js`
- `./file-a`
- `./file-b`
- `./general-importing-file`
- `node:fs`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 77

- `DependencyGraph`
- `Object`
- `__dirname`
- `add`
- `adding`
- `again`
- `babel`
- `change`
- `changed`
- `circular`
- `create`
- `createDependencyGraph`
- `dependencies`
- `dependency`
- `dependencyGraph`
- `dependencyPaths`
- `dependentPaths`
- `dependents`
- `describe`
- `entries`
- `existsSync`
- `expect`
- `file`
- `fromEntries`
- `general`
- `graph`
- `importActual`
- `importing`
- `initial`
- `inner`
- `its`
- `itself`
- `join`
- `key`
- `map`
- `mock`
- `moduleDependencies`
- `node`
- `number`
- `once`
- `path`
- `pathToTemporaryFile`
- `promises`
- `relative`
- `relativePath`
- `relativePathDependencyGraph`
- `remove`
- `removing`
- `resolve`
- `resolveDependentsOf`
- `right`
- `satisfies`
- `sequential`
- `string`
- `temporary`
- `test`
- `testing`
- `testingDiretctory`
- `there`
- `toAbsolute`
- `toBeUndefined`
- `toContain`
- `toEqual`
- `toMatchSnapshot`
- `traverse`
- `type`
- `unlink`
- `unlinked`
- `unlinking`
- `updateDependencyGraph`
- `updated`
- `updating`
- `utf8`
- `value`
- `when`
- `work`
- `writeFile`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

