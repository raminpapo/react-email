# Documentation: cli.mdx
**File Path:** `apps/docs/cli.mdx`
**Language:** Unknown
**Size:** 7,353 bytes
**Lines:** 206
**Generated:** 2025-11-15T20:37:32.701987Z

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

- **Path:** `apps/docs/cli.mdx`
- **Name:** `cli.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 7,353 bytes (7.18 KB)
- **Lines of Code:** 206

---

## Original Source

```
---
title: "CLI"
sidebarTitle: "CLI"
description: "After installing the React Email package (or cloning a starter), you can start using the command line interface (CLI)."
"og:image": "https://react.email/static/covers/react-email.png"
icon: "square-terminal"
---

## `email dev`

Starts a local development server that will watch your files and automatically rebuild
your email template when you make changes.

**Options**

<ResponseField name="--dir" type="string" default="emails">
  Change the directory of your email templates.
</ResponseField>
<ResponseField name="--port" type="string" default="3000">
  Port to run dev server on
</ResponseField>

**F.A.Q**

<AccordionGroup>
  <Accordion title="Where can I place my static files for previewing?">
    Almost always you will need to have static files in your emails, and seeing
    them on the preview server without having to first host on a CDN is very helpful.

    We do allow for this, and currently, you can place your files inside a `static`
    directory inside your `emails` directory.

    This does adjust to your `--dir` option, so if your `emails` directory was inside
    `./src/emails`, you would place your static files inside `./src/emails/static`.

    These static files are directly served from our preview server by looking into the
    requests made into it that end with `/static` (i.e. `http://localhost:3000/static/...`) and serving the files at that point,
    this also allows for you to have images inside your emails like so:

    ```jsx
    export default function Email(props) {
      return (
        <div>
          <img src="/static/email-logo.png" />
        </div>
      );
    }
    ```

    <Info>
      This does not mean your images are hosted for you to send the emails.

        If you do send the rendered email, and you are trying to link to an image,
        or some other asset inside `emails/static`, they will not load on the email that was sent.

        We recommend that you use a different source link to your files depending on whether you're
        running in production or not. Here's an example

        ```jsx
        const baseURL = process.env.NODE_ENV === "production" ? "https://cdn.com" : "";

        export default function Email(props) {
          return (
            <div>
              <img src={`${baseURL}/static/email-logo.png`} />
            </div>
          );
        }
        ```

        You can refer to our [demo emails source code](https://demo.react.email/preview/notifications/vercel-invite-user)
        for an example of how we do this with our demo deploy on Vercel.
    </Info>

  </Accordion>
  <Accordion title="How can I define props specific to the email's preview?">
    Considering that you are already default exporting the React component
    that will render as your email template, you can just define a `PreviewProps` with it as follows:

    ```jsx Email template
    export default function Email(props) {
      return (
        <div>
          <a src={props.source}>click here if you want candy 👀</a>
        </div>
      );
    }

    Email.PreviewProps = {
      source: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    };
    ```

    And then, when opening this email's preview, the `PreviewProps` will be used as props into Email.
    So, in a nutshell, it will render the same as if you were to do:

    ```jsx Another file
    import Email from "./path-to-my-email";

    <Email {...Email.PreviewProps} />;
    ```

  </Accordion>
  <Accordion title="How to make the preview server ignore directories?">
    Once the preview server has started and is now open on `localhost`, the preview server
    reads recursively down into all of your files and directories. This can be disabled
    from a directory down by prefixing it with `_`, e.g. `components -> _components`.

    So if you wanted to make components for your emails, you could have a file structure as follows:

    ```bash
    my-project
    ├── emails
    │   ├── _components
    │   │   └── this-is-not-going-to-appear-in-the-sidebar.tsx
    │   ├── email.tsx
    │   └── static
    ├── package.json
    └── tsconfig.json
    ```

    Then the only file that will be shown on the preview server is going to be your `email.tsx`.

  </Accordion>
  <Accordion title="The heuristics for files to be considered emails">
    To avoid uncanny files appearing in the sidebar of the preview server,
    we account for two heuristics to determine weather or not we should
    include it:

    1. If a file has `.js, .jsx or .tsx` as their file extension
    2. If the file contains a `export default` expression by matching with the regex<br/>
      `/\bexport\s*default\b/gm`

    These can certainly fail as they are only heuristics, so if you do find
    any issues with these, feel free to open an [issue](https://github.com/resend/react-email/issues).

  </Accordion>
</AccordionGroup>

## `email build`

Copies the preview app for onto `.react-email` and builds it.

<ResponseField name="--dir" type="string" default="emails">
  Change the directory of your email templates.
</ResponseField>
<ResponseField name="--packageManager" type="string" default="npm">
  Package manager to use on the installation of `.react-email`.
</ResponseField>

## `email start`

Runs the built preview app that is inside `.react-email`.

## `email export`

Generates the plain HTML files of your emails into a `out` directory.

<Info>
  A very common misconception is to assume that `email export` is the default or primary way of rendering
  email templates.

  The primary and preferable way is always going to be the [render](/utilities/render) utility,
  by passing in the needed data through props, on the exact moment of sending the email.

  `email export` is a secondary way meant for situations where React Email cannot be used optimally.
  With this secondary way, comes significant drawbacks, mainly the need for manual templating, which
  could be done easily with the `render` utility. It being a secondary way, we would strongly recommend
  you don't use it unless you really are forced into it.

  As an example, two cases where `email export` makes itself necessary include:
  - When the email content must be processed by a backend in a language other than JavaScript.
  - When the platform handling email, such as Shopify, forces you into manual templating.

  You also should not have to worry about `render`'s performance, as typically, the introduced
  time in rendering is going to be milliseconds when compared to manual templating.
</Info>

**Options**

<ResponseField name="--outDir" type="string" default="out">
  Change the output directory.
</ResponseField>
<ResponseField name="--pretty" type="boolean" default="false">
  Minify or prettify the generated HTML file.
</ResponseField>
<ResponseField name="--plainText" type="boolean" default="false">
  Set output format as plain text.
</ResponseField>
<ResponseField name="--dir" type="string" default="emails">
  Change the directory of your email templates.
</ResponseField>

## `email help <cmd>`

Shows all the options for a specific command.

## `email resend setup`

Sets up a configuration in your home directory with your Resend API Key by prompting interactively.

## `email resend reset`

Removes your API Key from the configuration in your home directory.


```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `./path-to-my-email`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 200

- `Accordion`
- `AccordionGroup`
- `After`
- `Almost`
- `Another`
- `Change`
- `Considering`
- `Copies`
- `Email`
- `Generates`
- `Here`
- `How`
- `Info`
- `JavaScript`
- `Key`
- `Minify`
- `NODE_ENV`
- `Once`
- `Options`
- `Package`
- `Port`
- `PreviewProps`
- `React`
- `Removes`
- `Resend`
- `ResponseField`
- `Runs`
- `Set`
- `Sets`
- `Shopify`
- `Shows`
- `Starts`
- `Then`
- `These`
- `Vercel`
- `When`
- `Where`
- `You`
- `_components`
- `about`
- `account`
- `adjust`
- `all`
- `allow`
- `allows`
- `already`
- `also`
- `always`
- `any`
- `app`
- `appear`
- `appearing`
- `asset`
- `assume`
- `automatically`
- `avoid`
- `backend`
- `baseURL`
- `bash`
- `bexport`
- `boolean`
- `build`
- `builds`
- `built`
- `candy`
- `cannot`
- `cases`
- `cdn`
- `certainly`
- `changes`
- `click`
- `cloning`
- `cmd`
- `code`
- `com`
- `comes`
- `command`
- `common`
- `compared`
- `component`
- `components`
- `configuration`
- `considered`
- `contains`
- `content`
- `covers`
- `currently`
- `dQw4w9WgXcQ`
- `data`
- `define`
- `demo`
- `depending`
- `deploy`
- `description`
- `determine`
- `dev`
- `development`
- `different`
- `dir`
- `directly`
- `directories`
- `directory`
- `disabled`
- `div`
- `don`
- `done`
- `down`
- `drawbacks`
- `easily`
- `email`
- `emails`
- `end`
- `env`
- `exact`
- `example`
- `exporting`
- `expression`
- `extension`
- `fail`
- `feel`
- `file`
- `files`
- `find`
- `first`
- `follows`
- `forced`
- `forces`
- `format`
- `free`
- `generated`
- `github`
- `going`
- `handling`
- `having`
- `help`
- `helpful`
- `here`
- `heuristics`
- `home`
- `host`
- `hosted`
- `how`
- `http`
- `https`
- `icon`
- `ignore`
- `image`
- `images`
- `img`
- `include`
- `inside`
- `installation`
- `installing`
- `interactively`
- `interface`
- `into`
- `introduced`
- `invite`
- `issue`
- `issues`
- `itself`
- `json`
- `jsx`
- `just`
- `language`
- `like`
- `line`
- `link`
- `load`
- `local`
- `localhost`
- `logo`
- `looking`
- `made`
- `mainly`
- `make`
- `makes`
- `manager`
- `manual`
- `matching`
- `mean`
- `meant`
- `milliseconds`
- `misconception`
- `moment`
- `must`
- `name`
- `necessary`
- `need`
- `needed`
- `notifications`
- `now`
- `npm`
- `nutshell`
- `only`
- `onto`
- `open`
- `opening`
- `optimally`
- `option`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

