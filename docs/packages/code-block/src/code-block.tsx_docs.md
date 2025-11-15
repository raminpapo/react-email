# Documentation: code-block.tsx
**File Path:** `packages/code-block/src/code-block.tsx`
**Language:** tsx
**Size:** 3,383 bytes
**Lines:** 133
**Generated:** 2025-11-15T20:37:31.552543Z

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

- **Path:** `packages/code-block/src/code-block.tsx`
- **Name:** `code-block.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,383 bytes (3.30 KB)
- **Lines of Code:** 133

---

## Original Source

```tsx
import * as React from 'react';
import type { PrismLanguage } from './languages-available';
import { Prism } from './prism';
import type { Theme } from './themes';

export interface CodeBlockProps extends React.ComponentPropsWithoutRef<'pre'> {
  lineNumbers?: boolean;

  /**
   * This applies a certain font family on all elements render in this component,
   * it is mostly meant to override a global font that has already been used with
   * our `<Font>` component
   */
  fontFamily?: string;

  theme: Theme;
  language: PrismLanguage;
  code: string;
}

const stylesForToken = (token: Prism.Token, theme: Theme) => {
  let styles = { ...theme[token.type] };

  const aliases = Array.isArray(token.alias) ? token.alias : [token.alias];

  for (const alias of aliases) {
    styles = { ...styles, ...theme[alias] };
  }

  return styles;
};

const CodeBlockLine = ({
  token,
  theme,
  inheritedStyles,
}: {
  token: string | Prism.Token;
  theme: Theme;
  inheritedStyles?: React.CSSProperties;
}) => {
  if (token instanceof Prism.Token) {
    const styleForToken = {
      ...inheritedStyles,
      ...stylesForToken(token, theme),
    };

    if (token.content instanceof Prism.Token) {
      return (
        <span style={styleForToken}>
          <CodeBlockLine theme={theme} token={token.content} />
        </span>
      );
    }
    if (typeof token.content === 'string') {
      return <span style={styleForToken}>{token.content}</span>;
    }
    return (
      <>
        {token.content.map((subToken, i) => (
          <CodeBlockLine
            inheritedStyles={styleForToken}
            key={i}
            theme={theme}
            token={subToken}
          />
        ))}
      </>
    );
  }

  return (
    <span style={inheritedStyles}>
      {token.replaceAll(' ', '\xA0\u200D\u200B')}
    </span>
  );
};

export const CodeBlock = React.forwardRef<HTMLPreElement, CodeBlockProps>(
  ({ code, fontFamily, lineNumbers, theme, language, ...rest }, ref) => {
    const languageGrammar = Prism.languages[language];
    if (typeof languageGrammar === 'undefined') {
      throw new Error(
        `CodeBlock: There is no language defined on Prism called ${language}`,
      );
    }

    const lines = code.split(/\r\n|\r|\n/gm);
    const tokensPerLine = lines.map((line) =>
      Prism.tokenize(line, languageGrammar),
    );

    return (
      <pre
        {...rest}
        ref={ref}
        style={{ ...theme.base, width: '100%', ...rest.style }}
      >
        <code>
          {tokensPerLine.map((tokensForLine, lineIndex) => (
            <React.Fragment key={lineIndex}>
              {lineNumbers ? (
                <span
                  style={{
                    width: '2em',
                    height: '1em',
                    display: 'inline-block',
                    fontFamily: fontFamily,
                  }}
                >
                  {lineIndex + 1}
                </span>
              ) : null}

              {tokensForLine.map((token, i) => (
                <CodeBlockLine
                  inheritedStyles={{ fontFamily: fontFamily }}
                  key={i}
                  theme={theme}
                  token={token}
                />
              ))}
              <br />
            </React.Fragment>
          ))}
        </code>
      </pre>
    );
  },
);

CodeBlock.displayName = 'CodeBlock';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `CodeBlock()`
- `CodeBlockLine()`
- `aliases()`
- `languageGrammar()`
- `lines()`
- `styleForToken()`
- `styles()`
- `stylesForToken()`
- `tokensPerLine()`

### Interfaces

- `CodeBlockProps`

### Dependencies

This file imports/requires:

- `./languages-available`
- `./prism`
- `./themes`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 85

- `Array`
- `CSSProperties`
- `CodeBlock`
- `CodeBlockLine`
- `CodeBlockProps`
- `ComponentPropsWithoutRef`
- `Error`
- `Font`
- `Fragment`
- `HTMLPreElement`
- `Prism`
- `PrismLanguage`
- `React`
- `Theme`
- `There`
- `Token`
- `alias`
- `aliases`
- `all`
- `already`
- `applies`
- `available`
- `base`
- `block`
- `boolean`
- `called`
- `certain`
- `code`
- `component`
- `content`
- `defined`
- `display`
- `displayName`
- `elements`
- `extends`
- `family`
- `font`
- `fontFamily`
- `forwardRef`
- `global`
- `height`
- `inheritedStyles`
- `inline`
- `interface`
- `isArray`
- `key`
- `language`
- `languageGrammar`
- `languages`
- `line`
- `lineIndex`
- `lineNumbers`
- `lines`
- `map`
- `meant`
- `mostly`
- `our`
- `override`
- `pre`
- `prism`
- `react`
- `ref`
- `render`
- `replaceAll`
- `rest`
- `span`
- `split`
- `string`
- `style`
- `styleForToken`
- `styles`
- `stylesForToken`
- `subToken`
- `theme`
- `themes`
- `token`
- `tokenize`
- `tokensForLine`
- `tokensPerLine`
- `type`
- `u200B`
- `u200D`
- `used`
- `width`
- `xA0`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

