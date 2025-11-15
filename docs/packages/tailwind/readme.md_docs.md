# Documentation: readme.md
**File Path:** `packages/tailwind/readme.md`
**Language:** markdown
**Size:** 5,688 bytes
**Lines:** 127
**Generated:** 2025-11-15T20:37:32.360070Z

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

- **Path:** `packages/tailwind/readme.md`
- **Name:** `readme.md`
- **Extension:** `.md`
- **Language:** markdown
- **Size:** 5,688 bytes (5.55 KB)
- **Lines of Code:** 127

---

## Original Source

```markdown
![React Email Tailwind cover](https://react.email/static/covers/tailwind.png)

<div align="center"><strong>@react-email/tailwind</strong></div>
<div align="center">A React component to wrap emails with Tailwind CSS.</div>
<br />
<div align="center">
<a href="https://react.email">Website</a> 
<span> · </span>
<a href="https://react.email">Documentation</a> 
<span> · </span>
<a href="https://react.email">Twitter</a>
</div>

## Install

Install component from your command line.

#### With yarn

```sh
yarn add @react-email/tailwind -E
```

#### With npm

```sh
npm install @react-email/tailwind -E
```

## Getting started

Add the component around your email body content.

```jsx
import { Button } from "@react-email/button";
import { Tailwind } from "@react-email/tailwind";

const Email = () => {
  return (
    <Tailwind
      config={{
        theme: {
          extend: {
            colors: {
              "custom-color": "#ff0000",
            },
          },
        },
      }}
    >
      <Button
        href="https://example.com"
        className="text-custom-color bg-white mx-auto"
      >
        Click me
      </Button>
    </Tailwind>
  );
};
```

## Contributing notes

These are some things you will need to keep in mind if you are improving the Tailwind component
with things that might influence certain decisions we have made for better
email client support that have been made also in the past by other contributors but not documented
which ended up causing us to have these problems and need to rediscover the best decisions again.

### The inlining of all styles

This is one of the most important because this is not one of the use cases this is
the main focus point of using the Tailwind component. The support for defining styles with tags
and using [classes is not the best](https://www.caniemail.com/features/html-style/).

This though can't be used the same for media queries so we do append the media queries
and the class names associated with them on a `<style>` tag on the `<head>` element.

### The treatment for Tailwind's CSS variables

Emails don't really have great support for CSS variables,
so we needed to use a custom postcss plugin alongisde Tailwind to resolve
all of these variables. When the plugin finds a CSS Variable that it cannot resolve,
it leaves it without any changes.

### The treatment for media query class names

For media queries we have made more than one decision that are for the better. The first one
and most important is sanitizing the media query class names on the `<style>` tag to avoid
needing to escape the class names which does cause problems.

### RGB syntax color changes

For the best support two things were taken into account here. First thing is that
the syntax using spaces, which Tailwind generally uses, is not really supported,
neither for `rgb` nor for `rgba`, so we do a pass through Tailwind's generated
styles to change the syntax into using commas instead of spaces.

Second thing is that both `rgba` and using `/` for defining the color's opacity
are not very well supported, but passing in the opacity as a fourth parameter of `rgb()`
is what is mostly supported so we also account for that.

This has an effect like the following:

```CSS
rgb(255 255 255 / 1) -> rgb(255,255,255)
rgb(212 213 102 / 0.2) -> rgb(212,213,102,0.2)
```

### Defining the styles on the React `style` prop

This is something that comes a bit at the risk of performance but it is a safer way of doing this.
The reason this is safer is because certain components of ours or even custom ones may modify the
way styles are applied and defining it directly on the rendered HTML would cause unexpected behavior
on that.

## Support

This component was tested using the most popular email clients.

| <img src="https://react.email/static/icons/gmail.svg" width="48px" height="48px" alt="Gmail logo"> | <img src="https://react.email/static/icons/apple-mail.svg" width="48px" height="48px" alt="Apple Mail"> | <img src="https://react.email/static/icons/outlook.svg" width="48px" height="48px" alt="Outlook logo"> | <img src="https://react.email/static/icons/yahoo-mail.svg" width="48px" height="48px" alt="Yahoo! Mail logo"> | <img src="https://react.email/static/icons/hey.svg" width="48px" height="48px" alt="HEY logo"> | <img src="https://react.email/static/icons/superhuman.svg" width="48px" height="48px" alt="Superhuman logo"> |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Gmail ✔                                                                                           | Apple Mail ✔                                                                                           | Outlook ✔                                                                                             | Yahoo! Mail ✔                                                                                                | HEY ✔                                                                                         | Superhuman ✔                                                                                                |

## License

MIT License

```

---

## Overview

This is a Markdown documentation file. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `@react-email/button`
- `@react-email/tailwind`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 200

- `Add`
- `Apple`
- `Button`
- `Click`
- `Contributing`
- `Defining`
- `Documentation`
- `Email`
- `Emails`
- `First`
- `Getting`
- `Gmail`
- `Install`
- `License`
- `Mail`
- `Outlook`
- `React`
- `Second`
- `Superhuman`
- `Support`
- `Tailwind`
- `These`
- `Twitter`
- `Variable`
- `Website`
- `When`
- `Yahoo`
- `account`
- `add`
- `again`
- `align`
- `all`
- `alongisde`
- `also`
- `alt`
- `any`
- `append`
- `apple`
- `applied`
- `around`
- `associated`
- `auto`
- `avoid`
- `because`
- `behavior`
- `best`
- `better`
- `bit`
- `body`
- `both`
- `button`
- `caniemail`
- `cannot`
- `cases`
- `cause`
- `causing`
- `center`
- `certain`
- `change`
- `changes`
- `className`
- `classes`
- `client`
- `clients`
- `color`
- `colors`
- `com`
- `comes`
- `command`
- `commas`
- `component`
- `components`
- `config`
- `content`
- `contributors`
- `cover`
- `covers`
- `custom`
- `decision`
- `decisions`
- `defining`
- `directly`
- `div`
- `documented`
- `doing`
- `don`
- `effect`
- `element`
- `email`
- `emails`
- `ended`
- `escape`
- `even`
- `example`
- `extend`
- `features`
- `ff0000`
- `finds`
- `first`
- `focus`
- `following`
- `fourth`
- `generally`
- `generated`
- `gmail`
- `great`
- `head`
- `height`
- `here`
- `hey`
- `href`
- `html`
- `https`
- `icons`
- `img`
- `important`
- `improving`
- `influence`
- `inlining`
- `install`
- `instead`
- `into`
- `jsx`
- `keep`
- `leaves`
- `like`
- `line`
- `logo`
- `made`
- `mail`
- `main`
- `media`
- `mind`
- `modify`
- `more`
- `most`
- `mostly`
- `names`
- `need`
- `needed`
- `needing`
- `neither`
- `nor`
- `notes`
- `npm`
- `one`
- `ones`
- `opacity`
- `other`
- `ours`
- `outlook`
- `parameter`
- `pass`
- `passing`
- `past`
- `performance`
- `plugin`
- `png`
- `point`
- `popular`
- `postcss`
- `problems`
- `prop`
- `queries`
- `query`
- `react`
- `really`
- `reason`
- `rediscover`
- `rendered`
- `resolve`
- `rgb`
- `rgba`
- `risk`
- `safer`
- `same`
- `sanitizing`
- `some`
- `something`
- `spaces`
- `span`
- `src`
- `started`
- `static`
- `strong`
- `style`
- `styles`
- `superhuman`
- `support`
- `supported`
- `svg`
- `syntax`
- `tag`
- `tags`
- `tailwind`
- `taken`
- `tested`
- `text`
- `than`
- `them`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

