# Documentation: markdown.tsx
**File Path:** `packages/markdown/src/markdown.tsx`
**Language:** tsx
**Size:** 7,284 bytes
**Lines:** 239
**Generated:** 2025-11-15T20:37:32.299931Z

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

- **Path:** `packages/markdown/src/markdown.tsx`
- **Name:** `markdown.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 7,284 bytes (7.11 KB)
- **Lines of Code:** 239

---

## Original Source

```tsx
import { marked, Renderer } from 'marked';
import * as React from 'react';
import { type StylesType, styles } from './styles';
import { parseCssInJsToInlineCss } from './utils/parse-css-in-js-to-inline-css';

export type MarkdownProps = Readonly<{
  children: string;
  markdownCustomStyles?: StylesType;
  markdownContainerStyles?: React.CSSProperties;
}>;

export const Markdown = React.forwardRef<HTMLDivElement, MarkdownProps>(
  (
    { children, markdownContainerStyles, markdownCustomStyles, ...props },
    ref,
  ) => {
    const finalStyles = { ...styles, ...markdownCustomStyles };

    const renderer = new Renderer();
    renderer.blockquote = ({ tokens }) => {
      const text = renderer.parser.parse(tokens);

      return `<blockquote${
        parseCssInJsToInlineCss(finalStyles.blockQuote) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.blockQuote)}"`
          : ''
      }>\n${text}</blockquote>\n`;
    };

    renderer.br = () => {
      return `<br${
        parseCssInJsToInlineCss(finalStyles.br) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.br)}"`
          : ''
      } />`;
    };

    // TODO: Support all options
    renderer.code = ({ text }) => {
      text = `${text.replace(/\n$/, '')}\n`;

      return `<pre${
        parseCssInJsToInlineCss(finalStyles.codeBlock) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.codeBlock)}"`
          : ''
      }><code>${text}</code></pre>\n`;
    };

    renderer.codespan = ({ text }) => {
      return `<code${
        parseCssInJsToInlineCss(finalStyles.codeInline) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.codeInline)}"`
          : ''
      }>${text}</code>`;
    };

    renderer.del = ({ tokens }) => {
      const text = renderer.parser.parseInline(tokens);

      return `<del${
        parseCssInJsToInlineCss(finalStyles.strikethrough) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.strikethrough)}"`
          : ''
      }>${text}</del>`;
    };

    renderer.em = ({ tokens }) => {
      const text = renderer.parser.parseInline(tokens);

      return `<em${
        parseCssInJsToInlineCss(finalStyles.italic) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.italic)}"`
          : ''
      }>${text}</em>`;
    };

    renderer.heading = ({ tokens, depth }) => {
      const text = renderer.parser.parseInline(tokens);

      return `<h${depth}${
        parseCssInJsToInlineCss(
          finalStyles[`h${depth}` as keyof StylesType],
        ) !== ''
          ? ` style="${parseCssInJsToInlineCss(
              finalStyles[`h${depth}` as keyof StylesType],
            )}"`
          : ''
      }>${text}</h${depth}>`;
    };

    renderer.hr = () => {
      return `<hr${
        parseCssInJsToInlineCss(finalStyles.hr) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.hr)}"`
          : ''
      } />\n`;
    };

    renderer.image = ({ href, text, title }) => {
      return `<img src="${href.replaceAll('"', '&quot;')}" alt="${text.replaceAll('"', '&quot;')}"${
        title ? ` title="${title}"` : ''
      }${
        parseCssInJsToInlineCss(finalStyles.image) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.image)}"`
          : ''
      }>`;
    };

    renderer.link = ({ href, title, tokens }) => {
      const text = renderer.parser.parseInline(tokens);

      return `<a href="${href}" target="_blank"${
        title ? ` title="${title}"` : ''
      }${
        parseCssInJsToInlineCss(finalStyles.link) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.link)}"`
          : ''
      }>${text}</a>`;
    };

    renderer.listitem = ({ tokens }) => {
      const hasNestedList = tokens.some((token) => token.type === 'list');
      const text = hasNestedList
        ? renderer.parser.parse(tokens)
        : renderer.parser.parseInline(tokens);

      return `<li${
        parseCssInJsToInlineCss(finalStyles.li) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.li)}"`
          : ''
      }>${text}</li>\n`;
    };

    renderer.list = ({ items, ordered, start }) => {
      const type = ordered ? 'ol' : 'ul';
      const startAt = ordered && start !== 1 ? ` start="${start}"` : '';
      const styles = parseCssInJsToInlineCss(
        finalStyles[ordered ? 'ol' : 'ul'],
      );

      return (
        '<' +
        type +
        startAt +
        `${styles !== '' ? ` style="${styles}"` : ''}>\n` +
        items.map((item) => renderer.listitem(item)).join('') +
        '</' +
        type +
        '>\n'
      );
    };

    renderer.paragraph = ({ tokens }) => {
      const text = renderer.parser.parseInline(tokens);

      return `<p${
        parseCssInJsToInlineCss(finalStyles.p) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.p)}"`
          : ''
      }>${text}</p>\n`;
    };

    renderer.strong = ({ tokens }) => {
      const text = renderer.parser.parseInline(tokens);

      return `<strong${
        parseCssInJsToInlineCss(finalStyles.bold) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.bold)}"`
          : ''
      }>${text}</strong>`;
    };

    renderer.table = ({ header, rows }) => {
      const styleTable = parseCssInJsToInlineCss(finalStyles.table);
      const styleThead = parseCssInJsToInlineCss(finalStyles.thead);
      const styleTbody = parseCssInJsToInlineCss(finalStyles.tbody);

      const theadRow = renderer.tablerow({
        text: header.map((cell) => renderer.tablecell(cell)).join(''),
      });

      const tbodyRows = rows
        .map((row) =>
          renderer.tablerow({
            text: row.map((cell) => renderer.tablecell(cell)).join(''),
          }),
        )
        .join('');

      const thead = `<thead${styleThead ? ` style="${styleThead}"` : ''}>\n${theadRow}</thead>`;
      const tbody = `<tbody${styleTbody ? ` style="${styleTbody}"` : ''}>${tbodyRows}</tbody>`;

      return `<table${styleTable ? ` style="${styleTable}"` : ''}>\n${thead}\n${tbody}</table>\n`;
    };

    renderer.tablecell = ({ tokens, align, header }) => {
      const text = renderer.parser.parseInline(tokens);
      const type = header ? 'th' : 'td';
      const tag = align
        ? `<${type} align="${align}"${
            parseCssInJsToInlineCss(finalStyles.td) !== ''
              ? ` style="${parseCssInJsToInlineCss(finalStyles.td)}"`
              : ''
          }>`
        : `<${type}${
            parseCssInJsToInlineCss(finalStyles.td) !== ''
              ? ` style="${parseCssInJsToInlineCss(finalStyles.td)}"`
              : ''
          }>`;
      return `${tag}${text}</${type}>\n`;
    };

    renderer.tablerow = ({ text }) => {
      return `<tr${
        parseCssInJsToInlineCss(finalStyles.tr) !== ''
          ? ` style="${parseCssInJsToInlineCss(finalStyles.tr)}"`
          : ''
      }>\n${text}</tr>\n`;
    };

    return (
      <div
        {...props}
        dangerouslySetInnerHTML={{
          __html: marked.parse(children, {
            renderer,
            async: false,
          }),
        }}
        data-id="react-email-markdown"
        ref={ref}
        style={markdownContainerStyles}
      />
    );
  },
);

Markdown.displayName = 'Markdown';

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Markdown()`
- `finalStyles()`
- `hasNestedList()`
- `renderer()`
- `startAt()`
- `styleTable()`
- `styleTbody()`
- `styleThead()`
- `styles()`
- `tag()`
- `tbody()`
- `tbodyRows()`
- `text()`
- `thead()`
- `theadRow()`
- `type()`

### Type Definitions

- `MarkdownProps`
- `StylesType`

### Dependencies

This file imports/requires:

- `./styles`
- `./utils/parse-css-in-js-to-inline-css`
- `marked`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 97

- `CSSProperties`
- `HTMLDivElement`
- `Markdown`
- `MarkdownProps`
- `React`
- `Readonly`
- `Renderer`
- `StylesType`
- `Support`
- `__html`
- `_blank`
- `align`
- `all`
- `alt`
- `blockQuote`
- `blockquote`
- `bold`
- `cell`
- `children`
- `code`
- `codeBlock`
- `codeInline`
- `codespan`
- `css`
- `dangerouslySetInnerHTML`
- `data`
- `del`
- `depth`
- `displayName`
- `div`
- `email`
- `finalStyles`
- `forwardRef`
- `hasNestedList`
- `header`
- `heading`
- `href`
- `image`
- `img`
- `inline`
- `italic`
- `item`
- `items`
- `join`
- `keyof`
- `link`
- `list`
- `listitem`
- `map`
- `markdown`
- `markdownContainerStyles`
- `markdownCustomStyles`
- `marked`
- `options`
- `ordered`
- `paragraph`
- `parse`
- `parseCssInJsToInlineCss`
- `parseInline`
- `parser`
- `pre`
- `props`
- `quot`
- `react`
- `ref`
- `renderer`
- `replace`
- `replaceAll`
- `row`
- `rows`
- `some`
- `src`
- `start`
- `startAt`
- `strikethrough`
- `string`
- `strong`
- `style`
- `styleTable`
- `styleTbody`
- `styleThead`
- `styles`
- `table`
- `tablecell`
- `tablerow`
- `tag`
- `target`
- `tbody`
- `tbodyRows`
- `text`
- `thead`
- `theadRow`
- `title`
- `token`
- `tokens`
- `type`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

