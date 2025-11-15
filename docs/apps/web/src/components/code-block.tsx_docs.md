# Documentation: code-block.tsx
**File Path:** `apps/web/src/components/code-block.tsx`
**Language:** tsx
**Size:** 3,402 bytes
**Lines:** 121
**Generated:** 2025-11-15T20:37:32.888190Z

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

- **Path:** `apps/web/src/components/code-block.tsx`
- **Name:** `code-block.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,402 bytes (3.32 KB)
- **Lines of Code:** 121

---

## Original Source

```tsx
import classNames from 'classnames';
import type { Language } from 'prism-react-renderer';
import { Highlight } from 'prism-react-renderer';
import * as React from 'react';

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

interface CodeBlockProps {
  children: string;
  className?: string;
  codeClassName?: string;
  language?: Language;
  isGradientLine?: boolean;
}

export const CodeBlock: React.FC<Readonly<CodeBlockProps>> = ({
  children,
  language = 'html',
  className,
  codeClassName,
  isGradientLine = true,
}) => {
  const value = children.trim();

  return (
    <Highlight code={value} language={language} theme={theme}>
      {({ tokens, getLineProps, getTokenProps }) => (
        <>
          {isGradientLine && (
            <div
              className="absolute top-0 right-0 h-px w-[12.5rem]"
              style={{
                background:
                  'linear-gradient(90deg, rgba(56, 189, 248, 0) 0%, rgba(56, 189, 248, 0) 0%, rgba(232, 232, 232, 0.2) 33.02%, rgba(143, 143, 143, 0.6719) 64.41%, rgba(236, 72, 153, 0) 98.93%)',
              }}
            />
          )}

          <pre className={classNames('p-4 font-mono', className)}>
            {tokens.map((line, i) => {
              const { key: _, ...lineProps } = getLineProps({ line, key: i });

              return (
                <div
                  key={i}
                  {...lineProps}
                  className={classNames('whitespace-pre', codeClassName, {
                    "before:mr-2 before:text-slate-11 before:content-['$']":
                      language === 'bash' && tokens.length === 1,
                  })}
                >
                  {line.map((token, key) => {
                    const { key: _, ...tokenProps } = getTokenProps({
                      token,
                      key,
                    });

                    const isException =
                      token.content === 'from' &&
                      line[key + 1]?.content === ':';
                    token.types = isException
                      ? [...token.types, 'key-white']
                      : token.types;

                    return (
                      <React.Fragment key={key}>
                        <span {...tokenProps} />
                      </React.Fragment>
                    );
                  })}
                </div>
              );
            })}
          </pre>
          {isGradientLine && (
            <div
              className="absolute bottom-0 left-0 h-px w-[12.5rem]"
              style={{
                background:
                  'linear-gradient(90deg, rgba(56, 189, 248, 0) 0%, rgba(56, 189, 248, 0) 0%, rgba(232, 232, 232, 0.2) 33.02%, rgba(143, 143, 143, 0.6719) 64.41%, rgba(236, 72, 153, 0) 98.93%)',
              }}
            />
          )}
        </>
      )}
    </Highlight>
  );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `isException()`
- `theme()`
- `value()`

### Interfaces

- `CodeBlockProps`

### Dependencies

This file imports/requires:

- `classnames`
- `prism-react-renderer`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 76

- `CodeBlock`
- `CodeBlockProps`
- `CommitMono`
- `Fragment`
- `Highlight`
- `Language`
- `React`
- `Readonly`
- `absolute`
- `atrule`
- `attr`
- `background`
- `bash`
- `before`
- `boolean`
- `bottom`
- `children`
- `className`
- `classNames`
- `classnames`
- `code`
- `codeClassName`
- `color`
- `comment`
- `content`
- `div`
- `font`
- `fontFamily`
- `fontSize`
- `getLineProps`
- `getTokenProps`
- `gradient`
- `html`
- `interface`
- `isException`
- `isGradientLine`
- `key`
- `keyword`
- `language`
- `left`
- `length`
- `line`
- `lineProps`
- `linear`
- `map`
- `mono`
- `monospace`
- `name`
- `operator`
- `plain`
- `pre`
- `prism`
- `punctuation`
- `react`
- `renderer`
- `rgba`
- `right`
- `selector`
- `slate`
- `span`
- `string`
- `style`
- `styles`
- `tag`
- `text`
- `theme`
- `token`
- `tokenProps`
- `tokens`
- `top`
- `trim`
- `type`
- `types`
- `value`
- `white`
- `whitespace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

