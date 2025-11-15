# Documentation: pretty.ts
**File Path:** `packages/render/src/shared/utils/pretty.ts`
**Language:** typescript
**Size:** 2,515 bytes
**Lines:** 101
**Generated:** 2025-11-15T20:37:31.495127Z

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

- **Path:** `packages/render/src/shared/utils/pretty.ts`
- **Name:** `pretty.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,515 bytes (2.46 KB)
- **Lines of Code:** 101

---

## Original Source

```typescript
import type { Options, Plugin } from 'prettier';
import type { builders } from 'prettier/doc';
import * as html from 'prettier/plugins/html';
import { format } from 'prettier/standalone';

interface HtmlNode {
  type: 'element' | 'text' | 'ieConditionalComment';
  name?: string;
  sourceSpan: {
    start: { file: unknown[]; offset: number; line: number; col: number };
    end: { file: unknown[]; offset: number; line: number; col: number };
    details: null;
  };
  parent?: HtmlNode;
}

function recursivelyMapDoc(
  doc: builders.Doc,
  callback: (innerDoc: string | builders.DocCommand) => builders.Doc,
): builders.Doc {
  if (Array.isArray(doc)) {
    return doc.map((innerDoc) => recursivelyMapDoc(innerDoc, callback));
  }

  if (typeof doc === 'object') {
    if (doc.type === 'group') {
      return {
        ...doc,
        contents: recursivelyMapDoc(doc.contents, callback),
        expandedStates: recursivelyMapDoc(
          doc.expandedStates,
          callback,
        ) as builders.Doc[],
      };
    }

    if ('contents' in doc) {
      return {
        ...doc,
        contents: recursivelyMapDoc(doc.contents, callback),
      };
    }

    if ('parts' in doc) {
      return {
        ...doc,
        parts: recursivelyMapDoc(doc.parts, callback) as builders.Doc[],
      };
    }

    if (doc.type === 'if-break') {
      return {
        ...doc,
        breakContents: recursivelyMapDoc(doc.breakContents, callback),
        flatContents: recursivelyMapDoc(doc.flatContents, callback),
      };
    }
  }

  return callback(doc);
}

const modifiedHtml = { ...html } as Plugin;
if (modifiedHtml.printers) {
  const previousPrint = modifiedHtml.printers.html.print;
  modifiedHtml.printers.html.print = (path, options, print, args) => {
    const node = path.getNode() as HtmlNode;

    const rawPrintingResult = previousPrint(path, options, print, args);

    if (node.type === 'ieConditionalComment') {
      const printingResult = recursivelyMapDoc(rawPrintingResult, (doc) => {
        if (typeof doc === 'object' && doc.type === 'line') {
          return doc.soft ? '' : ' ';
        }

        return doc;
      });

      return printingResult;
    }

    return rawPrintingResult;
  };
}

const defaults: Options = {
  endOfLine: 'lf',
  tabWidth: 2,
  plugins: [modifiedHtml],
  bracketSameLine: true,
  parser: 'html',
};

export const pretty = (str: string, options: Options = {}) => {
  return format(str.replaceAll('\0', ''), {
    ...defaults,
    ...options,
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

- `modifiedHtml()`
- `node()`
- `pretty()`
- `previousPrint()`
- `printingResult()`
- `rawPrintingResult()`
- `recursivelyMapDoc()`

### Interfaces

- `HtmlNode`

### Dependencies

This file imports/requires:

- `prettier`
- `prettier/doc`
- `prettier/plugins/html`
- `prettier/standalone`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 63

- `Array`
- `Doc`
- `DocCommand`
- `HtmlNode`
- `Options`
- `Plugin`
- `args`
- `bracketSameLine`
- `breakContents`
- `builders`
- `callback`
- `col`
- `contents`
- `defaults`
- `details`
- `doc`
- `element`
- `end`
- `endOfLine`
- `expandedStates`
- `file`
- `flatContents`
- `format`
- `getNode`
- `group`
- `html`
- `ieConditionalComment`
- `innerDoc`
- `interface`
- `isArray`
- `line`
- `map`
- `modifiedHtml`
- `name`
- `node`
- `number`
- `object`
- `offset`
- `options`
- `parent`
- `parser`
- `parts`
- `path`
- `plugins`
- `prettier`
- `pretty`
- `previousPrint`
- `print`
- `printers`
- `printingResult`
- `rawPrintingResult`
- `recursivelyMapDoc`
- `replaceAll`
- `soft`
- `sourceSpan`
- `standalone`
- `start`
- `str`
- `string`
- `tabWidth`
- `text`
- `type`
- `unknown`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

