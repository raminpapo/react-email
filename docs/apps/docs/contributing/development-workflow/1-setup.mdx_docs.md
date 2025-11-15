# Documentation: 1-setup.mdx
**File Path:** `apps/docs/contributing/development-workflow/1-setup.mdx`
**Language:** Unknown
**Size:** 1,627 bytes
**Lines:** 44
**Generated:** 2025-11-15T20:37:32.722834Z

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

- **Path:** `apps/docs/contributing/development-workflow/1-setup.mdx`
- **Name:** `1-setup.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 1,627 bytes (1.59 KB)
- **Lines of Code:** 44

---

## Original Source

```
---
title: 'Setup'
sidebarTitle: '1. Setup'
'og:image': 'https://react.email/static/covers/react-email.png'
description: 'Things you will need to do beforehand to setup the project'
---

Before you can start developing, you will need to get the project setup.

<Info>
To contribute to the project, you must use **Node 18** or higher.
</Info>

<Steps>
  <Step title="Clone the repository">
    ```bash
    git clone https://github.com/resend/react-email
    ```
  </Step>
  <Step title={<>Enable <a href="https://pnpm.io/">pnpm</a> through <a href="https://github.com/nodejs/corepack">corepack</a></>}>
    ```bash inside of react-email
    corepack enable
    corepack prepare pnpm@latest --activate
    ```
  </Step>
  <Step title="Install all the dependencies">
    ```bash inside of react-email
    pnpm install
    ```
  </Step>
  <Step title="Link email-dev CLI globally">
    ```bash inside of react-email
    pnpm link ./packages/react-email/dev -g
    ```
    <Note>
    Linking the CLI globally runs the CLI's source code when you use the `email-dev` command, avoiding the need to rebuild the CLI.
    </Note>
  </Step>
</Steps>

If you plan to contribute to the docs, view our [Writing docs](/contributing/development-workflow/5-writing-docs) guide for additional setup.

If you have any trouble, please [reach out on GitHub Discussions](https://github.com/resend/react-email/discussions) or consider [opening up an issue on GitHub](https://github.com/resend/react-email/issues/new?assignees=&labels=Type%3A+Bug&projects=&template=1.bug_report.yml) after reading the [issue guidelines](/contributing/opening-issues).

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 100

- `Before`
- `Bug`
- `Clone`
- `Discussions`
- `Enable`
- `GitHub`
- `Info`
- `Install`
- `Link`
- `Linking`
- `Node`
- `Note`
- `Setup`
- `Step`
- `Steps`
- `Things`
- `Type`
- `Writing`
- `activate`
- `additional`
- `after`
- `all`
- `any`
- `assignees`
- `avoiding`
- `bash`
- `beforehand`
- `bug_report`
- `clone`
- `code`
- `com`
- `command`
- `consider`
- `contribute`
- `contributing`
- `corepack`
- `covers`
- `dependencies`
- `description`
- `dev`
- `developing`
- `development`
- `discussions`
- `docs`
- `email`
- `enable`
- `get`
- `git`
- `github`
- `globally`
- `guide`
- `guidelines`
- `higher`
- `href`
- `https`
- `image`
- `inside`
- `install`
- `issue`
- `issues`
- `labels`
- `latest`
- `link`
- `must`
- `need`
- `nodejs`
- `opening`
- `our`
- `out`
- `packages`
- `plan`
- `please`
- `png`
- `pnpm`
- `prepare`
- `project`
- `projects`
- `reach`
- `react`
- `reading`
- `rebuild`
- `repository`
- `resend`
- `runs`
- `setup`
- `sidebarTitle`
- `source`
- `start`
- `static`
- `template`
- `through`
- `title`
- `trouble`
- `use`
- `view`
- `when`
- `workflow`
- `writing`
- `yml`
- `you`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

