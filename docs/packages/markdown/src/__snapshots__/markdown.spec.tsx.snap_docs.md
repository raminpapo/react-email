# Documentation: markdown.spec.tsx.snap
**File Path:** `packages/markdown/src/__snapshots__/markdown.spec.tsx.snap`
**Language:** Unknown
**Size:** 5,443 bytes
**Lines:** 69
**Generated:** 2025-11-15T20:37:32.304979Z

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

- **Path:** `packages/markdown/src/__snapshots__/markdown.spec.tsx.snap`
- **Name:** `markdown.spec.tsx.snap`
- **Extension:** `.snap`
- **Language:** Unknown
- **Size:** 5,443 bytes (5.32 KB)
- **Lines of Code:** 69

---

## Original Source

```
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`<Markdown> component renders correctly > renders links in the correct format for browsers 1`] = `
"<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><!--$--><div data-id="react-email-markdown"><p>Link to <a href="https://react.email" target="_blank" style="color:#007bff;text-decoration:underline;background-color:transparent">React-email</a></p>
</div><!--/$-->"
`;

exports[`<Markdown> component renders correctly > renders lists in the correct format for browsers 1`] = `
"<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><!--$--><div data-id="react-email-markdown"><h1 style="font-weight:500;padding-top:20px;font-size:2.5rem">Below is a list</h1><ul>
<li>Item One</li>
<li>Item Two</li>
<li>Item Three</li>
</ul>
</div><!--/$-->"
`;

exports[`<Markdown> component renders correctly > renders nested lists in the correct format for browsers 1`] = `
"<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><!--$--><div data-id="react-email-markdown"><ul>
<li><p>parent list item</p>
<ul>
<li>nested list item 1</li>
<li>nested list item 2</li>
</ul>
</li>
<li><p>another parent item</p>
<ol>
<li>nested ordered item 1</li>
<li>nested ordered item 2</li>
</ol>
</li>
</ul>
</div><!--/$-->"
`;

exports[`<Markdown> component renders correctly > renders text in the correct format for browsers 1`] = `
"<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><!--$--><div data-id="react-email-markdown"><p><strong style="font:700 23px / 32px &#x27;Roobert PRO&#x27;, system-ui, sans-serif;background:url(&#x27;path/to/image&#x27;)">This is sample bold text in markdown</strong> and <em style="font-style:italic">this is italic text</em></p>
</div><!--/$-->"
`;

exports[`<Markdown> component renders correctly > renders the headers in the correct format for browsers 1`] = `"<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><!--$--><div data-id="react-email-markdown"><h1 style="font-weight:500;padding-top:20px;font-size:2.5rem">Heading 1!</h1><h2 style="font-weight:500;padding-top:20px;font-size:2rem">Heading 2!</h2><h3 style="font-weight:500;padding-top:20px;font-size:1.75rem">Heading 3!</h3><h4 style="font-weight:500;padding-top:20px;font-size:1.5rem">Heading 4!</h4><h5 style="font-weight:500;padding-top:20px;font-size:1.25rem">Heading 5!</h5><h6 style="font-weight:500;padding-top:20px;font-size:1rem">Heading 6!</h6></div><!--/$-->"`;

exports[`<Markdown> component renders correctly > renders the markdown in the correct format for browsers 1`] = `
"<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><!--$--><div data-id="react-email-markdown"><h1 style="font-weight:500;padding-top:20px;font-size:2.5rem">Markdown Test Document</h1><p>This is a <strong style="font-weight:bold">test document</strong> to check the capabilities of a Markdown parser.</p>
<h2 style="font-weight:500;padding-top:20px;font-size:2rem">Headings</h2><h3 style="font-weight:500;padding-top:20px;font-size:1.75rem">Third-Level Heading</h3><h4 style="font-weight:500;padding-top:20px;font-size:1.5rem">Fourth-Level Heading</h4><h5 style="font-weight:500;padding-top:20px;font-size:1.25rem">Fifth-Level Heading</h5><h6 style="font-weight:500;padding-top:20px;font-size:1rem">Sixth-Level Heading</h6><h2 style="font-weight:500;padding-top:20px;font-size:2rem">Text Formatting</h2><p>This is some <strong style="font-weight:bold">bold text</strong> and this is some <em style="font-style:italic">italic text</em>. You can also use <del>strikethrough</del> and <code style="color:#212529;font-size:87.5%;display:inline;background: #f8f8f8;font-family:SFMono-Regular,Menlo,Monaco,Consolas,monospace;word-wrap:break-word">inline code</code>.</p>
<h2 style="font-weight:500;padding-top:20px;font-size:2rem">Lists</h2><ol>
<li>Ordered List Item 1</li>
<li>Ordered List Item 2</li>
<li>Ordered List Item 3</li>
</ol>
<ul>
<li>Unordered List Item 1</li>
<li>Unordered List Item 2</li>
<li>Unordered List Item 3</li>
</ul>
<h2 style="font-weight:500;padding-top:20px;font-size:2rem">Links</h2><p><a href="https://www.markdownguide.org" target="_blank" style="color:#007bff;text-decoration:underline;background-color:transparent">Markdown Guide</a></p>
<h2 style="font-weight:500;padding-top:20px;font-size:2rem">Images</h2><p><img src="https://markdown-here.com/img/icon256.png" alt="Markdown Logo"></p>
<h2 style="font-weight:500;padding-top:20px;font-size:2rem">Blockquotes</h2><blockquote style="background:#f9f9f9;border-left:10px solid #ccc;margin:1.5em 10px;padding:1em 10px">
<p>This is a blockquote.</p>
<ul>
<li>Author</li>
</ul>
</blockquote>
<h2 style="font-weight:500;padding-top:20px;font-size:2rem">Code Blocks</h2><pre style="color:#212529;font-size:87.5%;display:block;background: #f8f8f8;font-family:SFMono-Regular,Menlo,Monaco,Consolas,monospace;padding-top:10px;padding-right:10px;padding-left:10px;padding-bottom:1px;margin-bottom:20px;word-wrap:break-word"><code>function greet(name) {
console.log(\`Hello, \${name}!\`);
}
</code></pre>
</div><!--/$-->"
`;

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 143

- `Author`
- `Below`
- `Blockquotes`
- `Blocks`
- `Code`
- `Consolas`
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
- `Menlo`
- `Monaco`
- `One`
- `Ordered`
- `React`
- `Regular`
- `Roobert`
- `SFMono`
- `Sixth`
- `Snapshot`
- `Test`
- `Text`
- `Third`
- `Three`
- `Transitional`
- `Two`
- `Unordered`
- `Vitest`
- `W3C`
- `You`
- `_blank`
- `also`
- `alt`
- `another`
- `background`
- `block`
- `blockquote`
- `bold`
- `border`
- `bottom`
- `browsers`
- `capabilities`
- `ccc`
- `check`
- `code`
- `color`
- `com`
- `component`
- `console`
- `correct`
- `correctly`
- `data`
- `decoration`
- `del`
- `dev`
- `display`
- `div`
- `document`
- `dtd`
- `email`
- `exports`
- `f8f8f8`
- `f9f9f9`
- `family`
- `font`
- `format`
- `greet`
- `guide`
- `headers`
- `here`
- `href`
- `html`
- `http`
- `https`
- `icon256`
- `image`
- `img`
- `inline`
- `italic`
- `item`
- `left`
- `links`
- `list`
- `lists`
- `log`
- `margin`
- `markdown`
- `markdownguide`
- `monospace`
- `name`
- `nested`
- `ordered`
- `org`
- `padding`
- `parent`
- `parser`
- `path`
- `png`
- `pre`
- `react`
- `renders`
- `right`
- `sample`
- `sans`
- `serif`
- `size`
- `snapshot`
- `solid`
- `some`
- `src`
- `strikethrough`
- `strong`
- `style`
- `system`
- `target`
- `test`
- `text`
- `top`
- `transitional`
- `transparent`
- `underline`
- `url`
- `use`
- `vitest`
- `weight`
- `word`
- `wrap`
- `www`
- `x27`
- `xhtml1`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

