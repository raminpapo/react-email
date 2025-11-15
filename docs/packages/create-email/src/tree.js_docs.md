# Documentation: tree.js
**File Path:** `packages/create-email/src/tree.js`
**Language:** javascript
**Size:** 2,195 bytes
**Lines:** 79
**Generated:** 2025-11-15T20:37:32.319625Z

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

- **Path:** `packages/create-email/src/tree.js`
- **Name:** `tree.js`
- **Extension:** `.js`
- **Language:** javascript
- **Size:** 2,195 bytes (2.14 KB)
- **Lines of Code:** 79

---

## Original Source

```javascript
// copied from packages/react-email/src/cli/utils/tree.ts
// with removed types of course
import { promises as fs } from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const SYMBOLS = {
  BRANCH: '├── ',
  EMPTY: '',
  INDENT: '    ',
  LAST_BRANCH: '└── ',
  VERTICAL: '│   ',
};

const getTreeLines = async (dirPath, depth, filter, currentDepth = 0) => {
  const base = process.cwd();
  const dirFullpath = path.resolve(base, dirPath);
  const dirname = path.basename(dirFullpath);
  let lines = [dirname];

  const dirStat = await fs.stat(dirFullpath);
  if (dirStat.isDirectory() && currentDepth < depth) {
    const childDirents = await fs.readdir(dirFullpath, { withFileTypes: true });

    childDirents.sort((a, b) => {
      // orders directories before files
      if (a.isDirectory() && b.isFile()) {
        return -1;
      }
      if (a.isFile() && b.isDirectory()) {
        return 1;
      }

      // orders by name because they are the same type
      // either directory & directory
      // or file & file
      return b.name > a.name ? -1 : 1;
    });

    for (let i = 0; i < childDirents.length; i++) {
      const dirent = childDirents[i];
      const isLast = i === childDirents.length - 1;

      const branchingSymbol = isLast ? SYMBOLS.LAST_BRANCH : SYMBOLS.BRANCH;
      const verticalSymbol = isLast ? SYMBOLS.INDENT : SYMBOLS.VERTICAL;

      if (filter?.(dirent) === false) {
        continue;
      }

      if (dirent.isFile()) {
        lines.push(`${branchingSymbol}${dirent.name}`);
      } else {
        const pathToDirectory = path.join(dirFullpath, dirent.name);
        const treeLinesForSubDirectory = await getTreeLines(
          pathToDirectory,
          depth,
          filter,
          currentDepth + 1,
        );
        lines = lines.concat(
          treeLinesForSubDirectory.map((line, index) =>
            index === 0
              ? `${branchingSymbol}${line}`
              : `${verticalSymbol}${line}`,
          ),
        );
      }
    }
  }

  return lines;
};

export const tree = async (dirPath, depth, filter) => {
  const lines = await getTreeLines(dirPath, depth, filter);
  return lines.join(os.EOL);
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `SYMBOLS()`
- `base()`
- `branchingSymbol()`
- `childDirents()`
- `dirFullpath()`
- `dirStat()`
- `dirent()`
- `dirname()`
- `getTreeLines()`
- `i()`
- `isLast()`
- `lines()`
- `pathToDirectory()`
- `tree()`
- `treeLinesForSubDirectory()`
- `verticalSymbol()`

### Dependencies

This file imports/requires:

- `node:fs`
- `node:os`
- `node:path`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 61

- `LAST_BRANCH`
- `base`
- `basename`
- `because`
- `before`
- `branchingSymbol`
- `childDirents`
- `cli`
- `concat`
- `copied`
- `course`
- `currentDepth`
- `cwd`
- `depth`
- `dirFullpath`
- `dirPath`
- `dirStat`
- `directories`
- `directory`
- `dirent`
- `dirname`
- `either`
- `email`
- `file`
- `files`
- `filter`
- `getTreeLines`
- `index`
- `isDirectory`
- `isFile`
- `isLast`
- `join`
- `length`
- `line`
- `lines`
- `map`
- `name`
- `node`
- `orders`
- `packages`
- `path`
- `pathToDirectory`
- `process`
- `promises`
- `push`
- `react`
- `readdir`
- `removed`
- `resolve`
- `same`
- `sort`
- `src`
- `stat`
- `they`
- `tree`
- `treeLinesForSubDirectory`
- `type`
- `types`
- `utils`
- `verticalSymbol`
- `withFileTypes`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

