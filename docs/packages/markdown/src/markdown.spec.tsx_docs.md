# Documentation: markdown.spec.tsx
**File Path:** `packages/markdown/src/markdown.spec.tsx`
**Language:** tsx
**Size:** 2,871 bytes
**Lines:** 131
**Generated:** 2025-11-15T20:37:32.297955Z

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

- **Path:** `packages/markdown/src/markdown.spec.tsx`
- **Name:** `markdown.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,871 bytes (2.80 KB)
- **Lines of Code:** 131

---

## Original Source

```tsx
import { render } from '@react-email/render';
import { Markdown } from './markdown';

describe('<Markdown> component renders correctly', () => {
  it('renders the markdown in the correct format for browsers', async () => {
    const actualOutput = await render(
      <Markdown>
        {`# Markdown Test Document

This is a **test document** to check the capabilities of a Markdown parser.

## Headings

### Third-Level Heading

#### Fourth-Level Heading

##### Fifth-Level Heading

###### Sixth-Level Heading

## Text Formatting

This is some **bold text** and this is some *italic text*. You can also use ~~strikethrough~~ and \`inline code\`.

## Lists

1. Ordered List Item 1
2. Ordered List Item 2
3. Ordered List Item 3

- Unordered List Item 1
- Unordered List Item 2
- Unordered List Item 3

## Links

[Markdown Guide](https://www.markdownguide.org)

## Images

![Markdown Logo](https://markdown-here.com/img/icon256.png)

## Blockquotes

> This is a blockquote.
> - Author

## Code Blocks

\`\`\`javascript
function greet(name) {
console.log(\`Hello, $\{name}!\`);
}
\`\`\``}
      </Markdown>,
    );
    expect(actualOutput).toMatchSnapshot();
  });

  it('renders the headers in the correct format for browsers', async () => {
    const actualOutput = await render(
      <Markdown>
        {`
# Heading 1!
## Heading 2!
### Heading 3!
#### Heading 4!
##### Heading 5!
###### Heading 6!
       `}
      </Markdown>,
    );
    expect(actualOutput).toMatchSnapshot();
  });

  it('renders text in the correct format for browsers', async () => {
    const actualOutput = await render(
      <Markdown
        markdownCustomStyles={{
          bold: {
            font: '700 23px / 32px "Roobert PRO", system-ui, sans-serif',
            background: 'url("path/to/image")',
          },
        }}
      >
        **This is sample bold text in markdown** and *this is italic text*
      </Markdown>,
    );
    expect(actualOutput).toMatchSnapshot();
  });

  it('renders links in the correct format for browsers', async () => {
    const actualOutput = await render(
      <Markdown>Link to [React-email](https://react.email)</Markdown>,
    );
    expect(actualOutput).toMatchSnapshot();
  });

  it('renders lists in the correct format for browsers', async () => {
    const actualOutput = await render(
      <Markdown>
        {`
# Below is a list 

- Item One
- Item Two
- Item Three
       `}
      </Markdown>,
    );
    expect(actualOutput).toMatchSnapshot();
  });

  it('renders nested lists in the correct format for browsers', async () => {
    const actualOutput = await render(
      <Markdown>
        {`
- parent list item
    - nested list item 1
    - nested list item 2
- another parent item
    1. nested ordered item 1
    2. nested ordered item 2
       `}
      </Markdown>,
    );
    expect(actualOutput).toMatchSnapshot();
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `actualOutput()`
- `greet()`

### Dependencies

This file imports/requires:

- `./markdown`
- `@react-email/render`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 96

- `Author`
- `Below`
- `Blockquotes`
- `Blocks`
- `Code`
- `Document`
- `Fifth`
- `Formatting`
- `Fourth`
- `Guide`
- `Heading`
- `Headings`
- `Hello`
- `Images`
- `Item`
- `Level`
- `Link`
- `Links`
- `List`
- `Lists`
- `Logo`
- `Markdown`
- `One`
- `Ordered`
- `React`
- `Roobert`
- `Sixth`
- `Test`
- `Text`
- `Third`
- `Three`
- `Two`
- `Unordered`
- `You`
- `actualOutput`
- `also`
- `another`
- `background`
- `blockquote`
- `bold`
- `browsers`
- `capabilities`
- `check`
- `code`
- `com`
- `component`
- `console`
- `correct`
- `correctly`
- `describe`
- `document`
- `email`
- `expect`
- `font`
- `format`
- `greet`
- `headers`
- `here`
- `https`
- `icon256`
- `image`
- `img`
- `inline`
- `italic`
- `item`
- `javascript`
- `links`
- `list`
- `lists`
- `log`
- `markdown`
- `markdownCustomStyles`
- `markdownguide`
- `name`
- `nested`
- `ordered`
- `org`
- `parent`
- `parser`
- `path`
- `png`
- `react`
- `render`
- `renders`
- `sample`
- `sans`
- `serif`
- `some`
- `strikethrough`
- `system`
- `test`
- `text`
- `toMatchSnapshot`
- `url`
- `use`
- `www`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

