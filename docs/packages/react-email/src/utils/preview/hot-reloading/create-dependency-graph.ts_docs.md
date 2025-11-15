# Documentation: create-dependency-graph.ts
**File Path:** `packages/react-email/src/utils/preview/hot-reloading/create-dependency-graph.ts`
**Language:** typescript
**Size:** 11,294 bytes
**Lines:** 344
**Generated:** 2025-11-15T20:37:32.554837Z

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

- **Path:** `packages/react-email/src/utils/preview/hot-reloading/create-dependency-graph.ts`
- **Name:** `create-dependency-graph.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 11,294 bytes (11.03 KB)
- **Lines of Code:** 344

---

## Original Source

```typescript
import { existsSync, promises as fs, statSync } from 'node:fs';
import path from 'node:path';
import type { EventName } from 'chokidar/handler.js';
import { getImportedModules } from './get-imported-modules.js';
import { resolvePathAliases } from './resolve-path-aliases.js';

interface Module {
  path: string;

  dependencyPaths: string[];
  dependentPaths: string[];

  moduleDependencies: string[];
}

export type DependencyGraph = Record</* path to module */ string, Module>;

const readAllFilesInsideDirectory = async (directory: string) => {
  let allFilePaths: string[] = [];

  const topLevelDirents = await fs.readdir(directory, { withFileTypes: true });

  for await (const dirent of topLevelDirents) {
    const pathToDirent = path.join(directory, dirent.name);
    if (dirent.isDirectory()) {
      allFilePaths = allFilePaths.concat(
        await readAllFilesInsideDirectory(pathToDirent),
      );
    } else {
      allFilePaths.push(pathToDirent);
    }
  }

  return allFilePaths;
};

const javascriptExtensions = ['.js', '.ts', '.jsx', '.tsx', '.mjs', '.cjs'];

const isJavascriptModule = (filePath: string) => {
  const extensionName = path.extname(filePath);

  return javascriptExtensions.includes(extensionName);
};

const checkFileExtensionsUntilItExists = (
  pathWithoutExtension: string,
): string | undefined => {
  if (existsSync(`${pathWithoutExtension}.ts`)) {
    return `${pathWithoutExtension}.ts`;
  }

  if (existsSync(`${pathWithoutExtension}.tsx`)) {
    return `${pathWithoutExtension}.tsx`;
  }

  if (existsSync(`${pathWithoutExtension}.js`)) {
    return `${pathWithoutExtension}.js`;
  }

  if (existsSync(`${pathWithoutExtension}.jsx`)) {
    return `${pathWithoutExtension}.jsx`;
  }

  if (existsSync(`${pathWithoutExtension}.mjs`)) {
    return `${pathWithoutExtension}.mjs`;
  }

  if (existsSync(`${pathWithoutExtension}.cjs`)) {
    return `${pathWithoutExtension}.cjs`;
  }
};

/**
 * Creates a stateful dependency graph that is structured in a way that you can get
 * the dependents of a module from its path.
 *
 * Stateful in the sense that it provides a `getter` and an "`updater`". The updater
 * will receive changes to the files, that can be perceived through some file watching mechanism,
 * so that it doesn't need to recompute the entire dependency graph but only the parts changed.
 */
export const createDependencyGraph = async (directory: string) => {
  const filePaths = await readAllFilesInsideDirectory(directory);
  const modulePaths = filePaths.filter(isJavascriptModule);
  const graph: DependencyGraph = Object.fromEntries(
    modulePaths.map((path) => [
      path,
      {
        path,
        dependencyPaths: [],
        dependentPaths: [],
        moduleDependencies: [],
      },
    ]),
  );

  const getDependencyPaths = async (filePath: string) => {
    const contents = await fs.readFile(filePath, 'utf8');
    const importedPaths = isJavascriptModule(filePath)
      ? resolvePathAliases(getImportedModules(contents), path.dirname(filePath))
      : [];
    const importedPathsRelativeToDirectory = importedPaths.map(
      (dependencyPath) => {
        const isModulePath = !dependencyPath.startsWith('.');

        /*
          path.isAbsolute will return false if the path looks like JavaScript module imports
          e.g. path.isAbsolute('react-dom/server') will return false, but for our purposes this
          path is not a relative one.
        */
        if (isModulePath || path.isAbsolute(dependencyPath)) {
          return dependencyPath;
        }

        let pathToDependencyFromDirectory = path.resolve(
          /*
            path.resolve resolves paths differently from what imports on javascript do.

            So if we wouldn't do this, for an email at "/path/to/email.tsx" with a dependency path of "./other-email" 
            would end up going into /path/to/email.tsx/other-email instead of /path/to/other-email which is the
            one the import is meant to go to
          */
          path.dirname(filePath),
          dependencyPath,
        );

        let isDirectory = false;
        try {
          // will throw if the the file is not existent
          isDirectory = statSync(pathToDependencyFromDirectory).isDirectory();
        } catch (_) {}
        if (isDirectory) {
          const pathToSubDirectory = pathToDependencyFromDirectory;
          const pathWithExtension = checkFileExtensionsUntilItExists(
            `${pathToSubDirectory}/index`,
          );
          if (pathWithExtension) {
            pathToDependencyFromDirectory = pathWithExtension;
          } else {
            console.warn(
              `Could not find index file for directory at ${pathToDependencyFromDirectory}. This is probably going to cause issues with both hot reloading and your code.`,
            );
          }
        }

        const extension = path.extname(pathToDependencyFromDirectory);
        const pathWithEnsuredExtension = (() => {
          if (
            extension.length > 0 &&
            existsSync(pathToDependencyFromDirectory)
          ) {
            return pathToDependencyFromDirectory;
          }
          if (javascriptExtensions.includes(extension)) {
            return checkFileExtensionsUntilItExists(
              pathToDependencyFromDirectory.replace(extension, ''),
            );
          }
          return checkFileExtensionsUntilItExists(
            pathToDependencyFromDirectory,
          );
        })();

        if (pathWithEnsuredExtension) {
          pathToDependencyFromDirectory = pathWithEnsuredExtension;
        } else {
          console.warn(
            `Could not find file at ${pathToDependencyFromDirectory}`,
          );
        }

        return pathToDependencyFromDirectory;
      },
    );

    const moduleDependencies = importedPathsRelativeToDirectory.filter(
      (dependencyPath) =>
        !dependencyPath.startsWith('.') && !path.isAbsolute(dependencyPath),
    );

    const nonNodeModuleImportPathsRelativeToDirectory =
      importedPathsRelativeToDirectory.filter(
        (dependencyPath) =>
          dependencyPath.startsWith('.') || path.isAbsolute(dependencyPath),
      );

    return {
      dependencyPaths: nonNodeModuleImportPathsRelativeToDirectory,
      moduleDependencies,
    };
  };

  const updateModuleDependenciesInGraph = async (moduleFilePath: string) => {
    if (graph[moduleFilePath] === undefined) {
      graph[moduleFilePath] = {
        path: moduleFilePath,
        dependencyPaths: [],
        dependentPaths: [],
        moduleDependencies: [],
      };
    }

    const { moduleDependencies, dependencyPaths: newDependencyPaths } =
      await getDependencyPaths(moduleFilePath);

    graph[moduleFilePath].moduleDependencies = moduleDependencies;

    // we go through these to remove the ones that don't exist anymore
    for (const dependencyPath of graph[moduleFilePath].dependencyPaths) {
      // Looping through only the ones that were on the dependencyPaths but are not
      // in the newDependencyPaths
      if (newDependencyPaths.includes(dependencyPath)) continue;

      const dependencyModule = graph[dependencyPath];
      if (dependencyModule !== undefined) {
        dependencyModule.dependentPaths =
          dependencyModule.dependentPaths.filter(
            (dependentPath) => dependentPath !== moduleFilePath,
          );
      }
    }

    graph[moduleFilePath].dependencyPaths = newDependencyPaths;

    for await (const dependencyPath of newDependencyPaths) {
      if (graph[dependencyPath] === undefined) {
        /*
          This import path might have not been initialized as it can be outside
          of the original directory we looked into.
        */
        await updateModuleDependenciesInGraph(dependencyPath);
      }

      const dependencyModule = graph[dependencyPath];

      if (dependencyModule === undefined) {
        throw new Error(
          `Loading the dependency path ${dependencyPath} did not initialize it at all. This is a bug in React Email.`,
        );
      }

      if (!dependencyModule.dependentPaths.includes(moduleFilePath)) {
        dependencyModule.dependentPaths.push(moduleFilePath);
      }
    }
  };

  for (const filePath of modulePaths) {
    await updateModuleDependenciesInGraph(filePath);
  }

  const removeModuleFromGraph = (filePath: string) => {
    const module = graph[filePath];
    if (module) {
      for (const dependencyPath of module.dependencyPaths) {
        if (graph[dependencyPath]) {
          graph[dependencyPath]!.dependentPaths = graph[
            dependencyPath
          ]!.dependentPaths.filter(
            (dependentPath) => dependentPath !== filePath,
          );
        }
      }
      delete graph[filePath];
    }
  };

  return [
    graph,
    async (event: EventName, pathToModified: string) => {
      switch (event) {
        case 'change':
          if (isJavascriptModule(pathToModified)) {
            await updateModuleDependenciesInGraph(pathToModified);
          }
          break;
        case 'add':
          if (isJavascriptModule(pathToModified)) {
            await updateModuleDependenciesInGraph(pathToModified);
          }
          break;
        case 'addDir': {
          const filesInsideAddedDirectory =
            await readAllFilesInsideDirectory(pathToModified);
          const modulesInsideAddedDirectory =
            filesInsideAddedDirectory.filter(isJavascriptModule);
          for await (const filePath of modulesInsideAddedDirectory) {
            await updateModuleDependenciesInGraph(filePath);
          }
          break;
        }
        case 'unlink':
          if (isJavascriptModule(pathToModified)) {
            removeModuleFromGraph(pathToModified);
          }
          break;
        case 'unlinkDir': {
          const filesInsideDeletedDirectory =
            await readAllFilesInsideDirectory(pathToModified);
          const modulesInsideDeletedDirectory =
            filesInsideDeletedDirectory.filter(isJavascriptModule);
          for await (const filePath of modulesInsideDeletedDirectory) {
            removeModuleFromGraph(filePath);
          }
          break;
        }
      }
    },
    {
      /**
       * Resolves all modules that depend on the specified module, directly or indirectly.
       *
       * @param pathToModule - The path to the module whose dependents we want to find
       * @returns An array of paths to all modules that depend on the specified module
       */
      resolveDependentsOf: function resolveDependentsOf(
        pathToModule: string,
      ): string[] {
        const dependentPaths = new Set<string>();
        const stack: string[] = [pathToModule];

        while (stack.length > 0) {
          const currentPath = stack.pop()!;
          const moduleEntry = graph[currentPath];

          if (!moduleEntry) continue;

          for (const dependentPath of moduleEntry.dependentPaths) {
            if (
              dependentPaths.has(dependentPath) ||
              dependentPath === pathToModule
            )
              continue;

            dependentPaths.add(dependentPath);
            stack.push(dependentPath);
          }
        }

        return [...dependentPaths.values()];
      },
    },
  ] as const;
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `checkFileExtensionsUntilItExists()`
- `contents()`
- `createDependencyGraph()`
- `currentPath()`
- `dependencyModule()`
- `dependentPaths()`
- `extension()`
- `extensionName()`
- `filePaths()`
- `filesInsideAddedDirectory()`
- `filesInsideDeletedDirectory()`
- `getDependencyPaths()`
- `importedPaths()`
- `importedPathsRelativeToDirectory()`
- `isDirectory()`
- `isJavascriptModule()`
- `isModulePath()`
- `javascriptExtensions()`
- `module()`
- `moduleDependencies()`
- `moduleEntry()`
- `modulePaths()`
- `modulesInsideAddedDirectory()`
- `modulesInsideDeletedDirectory()`
- `nonNodeModuleImportPathsRelativeToDirectory()`
- `pathToDependencyFromDirectory()`
- `pathToDirent()`
- `pathToSubDirectory()`
- `pathWithEnsuredExtension()`
- `pathWithExtension()`
- `readAllFilesInsideDirectory()`
- `removeModuleFromGraph()`
- `resolveDependentsOf()`
- `topLevelDirents()`
- `updateModuleDependenciesInGraph()`

### Interfaces

- `Module`

### Type Definitions

- `DependencyGraph`

### Dependencies

This file imports/requires:

- `./get-imported-modules.js`
- `./resolve-path-aliases.js`
- `chokidar/handler.js`
- `node:fs`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 198

- `Creates`
- `DependencyGraph`
- `Email`
- `Error`
- `EventName`
- `JavaScript`
- `Loading`
- `Looping`
- `Module`
- `Object`
- `React`
- `Record`
- `Resolves`
- `Set`
- `Stateful`
- `add`
- `addDir`
- `aliases`
- `all`
- `allFilePaths`
- `anymore`
- `array`
- `both`
- `bug`
- `cause`
- `change`
- `changed`
- `changes`
- `checkFileExtensionsUntilItExists`
- `chokidar`
- `cjs`
- `code`
- `concat`
- `console`
- `contents`
- `createDependencyGraph`
- `currentPath`
- `delete`
- `depend`
- `dependency`
- `dependencyModule`
- `dependencyPath`
- `dependencyPaths`
- `dependentPath`
- `dependentPaths`
- `dependents`
- `differently`
- `directly`
- `directory`
- `dirent`
- `dirname`
- `doesn`
- `dom`
- `don`
- `email`
- `end`
- `entire`
- `event`
- `exist`
- `existent`
- `existsSync`
- `extension`
- `extensionName`
- `extname`
- `file`
- `filePath`
- `filePaths`
- `files`
- `filesInsideAddedDirectory`
- `filesInsideDeletedDirectory`
- `filter`
- `find`
- `fromEntries`
- `get`
- `getDependencyPaths`
- `getImportedModules`
- `getter`
- `going`
- `graph`
- `handler`
- `hot`
- `imported`
- `importedPaths`
- `importedPathsRelativeToDirectory`
- `imports`
- `includes`
- `index`
- `indirectly`
- `initialize`
- `initialized`
- `instead`
- `interface`
- `into`
- `isAbsolute`
- `isDirectory`
- `isJavascriptModule`
- `isModulePath`
- `issues`
- `its`
- `javascript`
- `javascriptExtensions`
- `join`
- `jsx`
- `length`
- `like`
- `looked`
- `looks`
- `map`
- `meant`
- `mechanism`
- `mjs`
- `module`
- `moduleDependencies`
- `moduleEntry`
- `moduleFilePath`
- `modulePaths`
- `modules`
- `modulesInsideAddedDirectory`
- `modulesInsideDeletedDirectory`
- `name`
- `need`
- `newDependencyPaths`
- `node`
- `nonNodeModuleImportPathsRelativeToDirectory`
- `one`
- `ones`
- `only`
- `original`
- `other`
- `our`
- `outside`
- `param`
- `parts`
- `path`
- `pathToDependencyFromDirectory`
- `pathToDirent`
- `pathToModified`
- `pathToModule`
- `pathToSubDirectory`
- `pathWithEnsuredExtension`
- `pathWithExtension`
- `pathWithoutExtension`
- `paths`
- `perceived`
- `pop`
- `probably`
- `promises`
- `provides`
- `purposes`
- `push`
- `react`
- `readAllFilesInsideDirectory`
- `readFile`
- `readdir`
- `receive`
- `recompute`
- `relative`
- `reloading`
- `remove`
- `removeModuleFromGraph`
- `replace`
- `resolve`
- `resolveDependentsOf`
- `resolvePathAliases`
- `resolves`
- `returns`
- `sense`
- `server`
- `some`
- `specified`
- `stack`
- `startsWith`
- `statSync`
- `stateful`
- `string`
- `structured`
- `these`
- `through`
- `topLevelDirents`
- `tsx`
- `type`
- `unlink`
- `unlinkDir`
- `updateModuleDependenciesInGraph`
- `updater`
- `utf8`
- `values`
- `want`
- `warn`
- `watching`
- `way`
- `what`
- `which`
- `whose`
- `withFileTypes`
- `wouldn`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

