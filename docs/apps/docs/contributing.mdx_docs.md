# Documentation: contributing.mdx
**File Path:** `apps/docs/contributing.mdx`
**Language:** Unknown
**Size:** 4,510 bytes
**Lines:** 96
**Generated:** 2025-11-15T20:37:32.704624Z

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

- **Path:** `apps/docs/contributing.mdx`
- **Name:** `contributing.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 4,510 bytes (4.40 KB)
- **Lines of Code:** 96

---

## Original Source

```
---
title: 'Contributing'
sidebarTitle: 'Old Contributing'
description: 'Wanna help? Awesome! There are many ways you can contribute.'
'og:image': 'https://react.email/static/covers/react-email.png'
icon: 'code-pull-request'
---

import LocalDev from '/snippets/localdev.mdx'

## Improving the docs

Documentation is extremely important and takes a fair deal of time and effort to write and keep updated. Everything is written in [Markdown](https://www.markdownguide.org/) to facilitate the process of contributing.

<Accordion title="Docs Setup Guide" icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
    >
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
    </svg>
}>

## Docs Setup Guide

1. Clone the repository:

```sh
git clone https://github.com/resend/react-email.git
```

2. Install all dependencies:

```sh
pnpm install
```

3. Navigate to the `apps/docs` folder:

```sh
cd apps/docs
```

4. Run the development server:

```sh
pnpm dev
```

5. Make your changes under the `apps/docs` folder and see a live preview at [localhost:3000](http://localhost:3000).

6. Submit a pull request.

</Accordion>

## Building new components

We're open to expanding the catalog of components to cover as many use cases as possible. We suggest to open an issue for discussion first to make sure your idea is aligned with the project goals.

<Accordion title="Components Setup Guide" icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
    >
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
    </svg>
}>

## Components Setup Guide

<LocalDev />

4. Add a new folder under `packages` and build your component.

5. Don't forget to add tests.

6. Submit a pull request.

</Accordion>

## Opening issues

Open an issue to report bugs or to propose new features.

- **Reporting bugs**: describe the bug as clearly as you can, including steps to reproduce, what happened and what you were expecting to happen. Also include browser version, OS and other related software's (npm, Node.js, etc) versions when applicable.

- **Suggesting features**: explain the proposed feature, what it should do, why it is useful, how users should use it. Give us as much info as possible so it will be easier to discuss, access and implement the proposed feature. When you're unsure about a certain aspect of the feature, feel free to leave it open for others to discuss and find an appropriate solution.

## Proposing pull requests

Pull requests are very welcome. Note that if you are going to propose drastic changes, be sure to open an issue for discussion first, to make sure that your PR will be accepted before you spend effort coding it.

- **Forking the repository**: clone it locally and create a branch for your proposed bug fix or new feature. Avoid working directly on the main branch.

- **Making changes**: implement your bug fix or feature, write tests to cover it and make sure all tests are passing. Then commit your changes, push your bug fix/feature branch to the origin (your forked repo) and open a pull request to the upstream (the repository you originally forked)'s main branch.

```

---

## Overview



---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `/snippets/localdev.mdx`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 200

- `Accordion`
- `Add`
- `Also`
- `Avoid`
- `Awesome`
- `Building`
- `Clone`
- `Components`
- `Contributing`
- `Docs`
- `Documentation`
- `Don`
- `Everything`
- `Forking`
- `Give`
- `Guide`
- `Improving`
- `Install`
- `LocalDev`
- `M12`
- `Make`
- `Making`
- `Markdown`
- `Navigate`
- `Node`
- `Note`
- `Old`
- `Open`
- `Opening`
- `Proposing`
- `Pull`
- `Reporting`
- `Run`
- `Setup`
- `Submit`
- `Suggesting`
- `Then`
- `There`
- `Wanna`
- `When`
- `about`
- `accepted`
- `access`
- `add`
- `aligned`
- `all`
- `applicable`
- `appropriate`
- `apps`
- `aspect`
- `before`
- `branch`
- `browser`
- `bug`
- `bugs`
- `build`
- `cases`
- `catalog`
- `certain`
- `changes`
- `clearly`
- `clone`
- `code`
- `coding`
- `com`
- `commit`
- `component`
- `components`
- `contribute`
- `contributing`
- `cover`
- `covers`
- `create`
- `deal`
- `dependencies`
- `describe`
- `description`
- `dev`
- `development`
- `directly`
- `discuss`
- `discussion`
- `docs`
- `drastic`
- `easier`
- `effort`
- `email`
- `etc`
- `expanding`
- `expecting`
- `explain`
- `extremely`
- `facilitate`
- `fair`
- `feature`
- `features`
- `feel`
- `find`
- `first`
- `fix`
- `folder`
- `forget`
- `forked`
- `free`
- `git`
- `github`
- `goals`
- `going`
- `happen`
- `happened`
- `help`
- `how`
- `http`
- `https`
- `icon`
- `idea`
- `image`
- `implement`
- `important`
- `include`
- `including`
- `info`
- `install`
- `issue`
- `issues`
- `keep`
- `leave`
- `live`
- `localdev`
- `localhost`
- `locally`
- `main`
- `make`
- `many`
- `markdownguide`
- `mdx`
- `much`
- `npm`
- `open`
- `org`
- `origin`
- `originally`
- `other`
- `others`
- `packages`
- `passing`
- `path`
- `png`
- `pnpm`
- `possible`
- `preview`
- `process`
- `project`
- `propose`
- `proposed`
- `pull`
- `push`
- `react`
- `related`
- `repo`
- `report`
- `repository`
- `reproduce`
- `request`
- `requests`
- `resend`
- `see`
- `server`
- `sidebarTitle`
- `snippets`
- `software`
- `solution`
- `spend`
- `static`
- `steps`
- `suggest`
- `sure`
- `svg`
- `takes`
- `tests`
- `time`
- `title`
- `under`
- `unsure`
- `updated`
- `upstream`
- `use`
- `useful`
- `users`
- `version`
- `versions`
- `very`
- `viewBox`
- `ways`
- `welcome`
- `what`
- `when`
- `why`
- `working`
- `write`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

