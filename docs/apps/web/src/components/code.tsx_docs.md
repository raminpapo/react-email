# Documentation: code.tsx
**File Path:** `apps/web/src/components/code.tsx`
**Language:** tsx
**Size:** 3,563 bytes
**Lines:** 117
**Generated:** 2025-11-15T20:37:32.889675Z

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

- **Path:** `apps/web/src/components/code.tsx`
- **Name:** `code.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,563 bytes (3.48 KB)
- **Lines of Code:** 117

---

## Original Source

```tsx
'use client';

import classNames from 'classnames';
import { Highlight } from 'prism-react-renderer';
import * as React from 'react';
import { CopyCode } from './copy-code';

interface CodeProps {
  children: string;
  className?: string;
  language?: string;
}

const theme = {
  plain: {
    color: '#EDEDEF',
    fontSize: 13,
    fontFamily: 'CommitMono, monospace',
  },
  styles: [
    {
      types: ['comment'],
      style: {
        color: '#706F78',
      },
    },
    {
      types: ['atrule', 'keyword', 'attr-name', 'selector'],
      style: {
        color: '#7E7D86',
      },
    },
    {
      types: ['punctuation', 'operator'],
      style: {
        color: '#706F78',
      },
    },
    {
      types: ['class-name', 'function', 'tag', 'key-white'],
      style: {
        color: '#EDEDEF',
      },
    },
  ],
};

export function Code({ children, className, language = 'html' }: CodeProps) {
  const value = children.trim();

  return (
    <Highlight code={value} language={language} theme={theme}>
      {({ tokens, getLineProps, getTokenProps }) => (
        <pre
          className={classNames(
            'relative inline-flex h-11 w-full items-center overflow-auto whitespace-pre rounded-xl border border-slate-6 pr-11 pl-4 font-mono text-sm backdrop-blur-md',
            className,
          )}
          style={{
            lineHeight: '130%',
            background:
              'linear-gradient(145.37deg, rgba(255, 255, 255, 0.09) -8.75%, rgba(255, 255, 255, 0.027) 83.95%)',
            boxShadow: 'rgb(0 0 0 / 10%) 0rem .3125rem 1.875rem -0.3125rem',
          }}
        >
          <CopyCode
            code={value}
            className="absolute right-1 shadow-none hover:text-white hover:[&_svg]:text-white enabled:hover:!bg-transparent focus:ring-0"
          />

          <div
            className="absolute top-0 right-0 h-px w-[12.5rem]"
            style={{
              background:
                'linear-gradient(90deg, rgba(56, 189, 248, 0) 0%, rgba(56, 189, 248, 0) 0%, rgba(232, 232, 232, 0.2) 33.02%, rgba(143, 143, 143, 0.6719) 64.41%, rgba(236, 72, 153, 0) 98.93%)',
            }}
          />
          {tokens.map((line, i) => {
            return (
              <div
                {...getLineProps({ line, key: i })}
                className={classNames('whitespace-pre', {
                  "before:mr-2 before:text-slate-11 before:content-['$']":
                    language === 'bash' && tokens.length === 1,
                })}
                key={i}
              >
                {line.map((token, key) => {
                  const isException =
                    token.content === 'from' && line[key + 1]?.content === ':';
                  const newTypes = isException
                    ? [...token.types, 'key-white']
                    : token.types;
                  token.types = newTypes;

                  return (
                    <React.Fragment key={key}>
                      <span {...getTokenProps({ token, key })} key={key} />
                    </React.Fragment>
                  );
                })}
              </div>
            );
          })}
          <div
            className="absolute bottom-0 left-0 h-px w-[12.5rem]"
            style={{
              background:
                'linear-gradient(90deg, rgba(56, 189, 248, 0) 0%, rgba(56, 189, 248, 0) 0%, rgba(232, 232, 232, 0.2) 33.02%, rgba(143, 143, 143, 0.6719) 64.41%, rgba(236, 72, 153, 0) 98.93%)',
            }}
          />
        </pre>
      )}
    </Highlight>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Code()`
- `isException()`
- `newTypes()`
- `theme()`
- `value()`

### Interfaces

- `CodeProps`

### Dependencies

This file imports/requires:

- `./copy-code`
- `classnames`
- `prism-react-renderer`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 95

- `Code`
- `CodeProps`
- `CommitMono`
- `CopyCode`
- `Fragment`
- `Highlight`
- `React`
- `_svg`
- `absolute`
- `atrule`
- `attr`
- `auto`
- `backdrop`
- `background`
- `bash`
- `before`
- `blur`
- `border`
- `bottom`
- `boxShadow`
- `center`
- `children`
- `className`
- `classNames`
- `classnames`
- `client`
- `code`
- `color`
- `comment`
- `content`
- `copy`
- `div`
- `enabled`
- `flex`
- `focus`
- `font`
- `fontFamily`
- `fontSize`
- `full`
- `getLineProps`
- `getTokenProps`
- `gradient`
- `hover`
- `html`
- `inline`
- `interface`
- `isException`
- `items`
- `key`
- `keyword`
- `language`
- `left`
- `length`
- `line`
- `lineHeight`
- `linear`
- `map`
- `mono`
- `monospace`
- `name`
- `newTypes`
- `operator`
- `overflow`
- `plain`
- `pre`
- `prism`
- `punctuation`
- `react`
- `relative`
- `renderer`
- `rgb`
- `rgba`
- `right`
- `ring`
- `rounded`
- `selector`
- `shadow`
- `slate`
- `span`
- `string`
- `style`
- `styles`
- `tag`
- `text`
- `theme`
- `token`
- `tokens`
- `top`
- `transparent`
- `trim`
- `types`
- `use`
- `value`
- `white`
- `whitespace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

