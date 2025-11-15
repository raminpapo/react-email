# Documentation: docs.json
**File Path:** `apps/docs/docs.json`
**Language:** json
**Size:** 4,455 bytes
**Lines:** 160
**Generated:** 2025-11-15T20:37:32.707775Z

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

- **Path:** `apps/docs/docs.json`
- **Name:** `docs.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 4,455 bytes (4.35 KB)
- **Lines of Code:** 160

---

## Original Source

```json
{
  "$schema": "https://mintlify.com/docs.json",
  "theme": "mint",
  "name": "React Email",
  "colors": {
    "primary": "#06BCEE",
    "light": "#81D7F7",
    "dark": "#06A6D1"
  },
  "contextual": {
    "options": ["copy", "chatgpt", "claude"]
  },
  "favicon": "/favicon.png",
  "navigation": {
    "anchors": [
      {
        "anchor": "Documentation",
        "icon": "book-open",
        "groups": [
          {
            "group": "Overview",
            "pages": [
              "introduction",
              "changelog",
              "roadmap",
              "cli",
              "deployment"
            ]
          },
          {
            "group": "Getting Started",
            "pages": [
              "getting-started/automatic-setup",
              "getting-started/manual-setup",
              {
                "group": "Monorepo Setup",
                "icon": "diagram-project",
                "pages": [
                  "getting-started/monorepo-setup/npm",
                  "getting-started/monorepo-setup/pnpm",
                  "getting-started/monorepo-setup/yarn",
                  "getting-started/monorepo-setup/bun"
                ]
              },
              "getting-started/migrating-to-react-email",
              "getting-started/updating-react-email"
            ]
          },
          {
            "group": "Components",
            "pages": [
              "components/html",
              "components/head",
              "components/button",
              "components/container",
              "components/code-block",
              "components/code-inline",
              "components/column",
              "components/row",
              "components/font",
              "components/heading",
              "components/hr",
              "components/image",
              "components/link",
              "components/markdown",
              "components/preview",
              "components/section",
              "components/tailwind",
              "components/text"
            ]
          },
          {
            "group": "Utilities",
            "pages": ["utilities/render"]
          },
          {
            "group": "Integrations",
            "pages": [
              "integrations/overview",
              "integrations/resend",
              "integrations/nodemailer",
              "integrations/sendgrid",
              "integrations/postmark",
              "integrations/aws-ses",
              "integrations/mailersend",
              "integrations/scaleway",
              "integrations/plunk"
            ]
          },
          {
            "group": "Contributing",
            "pages": [
              "contributing/introduction",
              "contributing/opening-issues",
              "contributing/opening-pull-requests",
              "contributing/codebase-overview",
              {
                "group": "Development workflow",
                "icon": "arrow-progress",
                "pages": [
                  "contributing/development-workflow/1-setup",
                  "contributing/development-workflow/2-running-tests",
                  "contributing/development-workflow/3-linting",
                  "contributing/development-workflow/4-building",
                  "contributing/development-workflow/5-writing-docs",
                  "contributing/development-workflow/6-editing-the-components"
                ]
              }
            ]
          }
        ]
      }
    ],
    "global": {
      "anchors": [
        {
          "anchor": "Components",
          "href": "https://react.email/components",
          "icon": "grid-2-plus"
        },
        {
          "anchor": "Templates",
          "href": "https://demo.react.email/preview/notifications/vercel-invite-user",
          "icon": "arrow-pointer"
        },
        {
          "anchor": "GitHub",
          "href": "https://github.com/resend/react-email",
          "icon": "github"
        }
      ]
    }
  },
  "logo": {
    "light": "/logo/light.svg",
    "dark": "/logo/dark.svg"
  },
  "appearance": {
    "default": "dark",
    "strict": true
  },
  "background": {
    "image": "/images/background.png",
    "color": {
      "dark": "#111111"
    }
  },
  "navbar": {
    "primary": {
      "type": "github",
      "href": "https://github.com/resend/react-email"
    }
  },
  "integrations": {
    "ga4": {
      "measurementId": "G-2LXLLQLM5D"
    }
  }
}

```

---

## Overview

This is a JSON configuration or data file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 135

- `Components`
- `Contributing`
- `Development`
- `Documentation`
- `Email`
- `Getting`
- `GitHub`
- `Integrations`
- `Monorepo`
- `Overview`
- `React`
- `Setup`
- `Started`
- `Templates`
- `Utilities`
- `anchor`
- `anchors`
- `appearance`
- `arrow`
- `automatic`
- `aws`
- `background`
- `block`
- `book`
- `building`
- `bun`
- `button`
- `changelog`
- `chatgpt`
- `claude`
- `cli`
- `code`
- `codebase`
- `color`
- `colors`
- `column`
- `com`
- `components`
- `container`
- `contextual`
- `contributing`
- `copy`
- `dark`
- `demo`
- `deployment`
- `development`
- `diagram`
- `docs`
- `editing`
- `email`
- `favicon`
- `font`
- `ga4`
- `getting`
- `github`
- `global`
- `grid`
- `group`
- `groups`
- `head`
- `heading`
- `href`
- `html`
- `https`
- `icon`
- `image`
- `images`
- `inline`
- `integrations`
- `introduction`
- `invite`
- `issues`
- `json`
- `light`
- `link`
- `linting`
- `logo`
- `mailersend`
- `manual`
- `markdown`
- `measurementId`
- `migrating`
- `mint`
- `mintlify`
- `monorepo`
- `name`
- `navbar`
- `navigation`
- `nodemailer`
- `notifications`
- `npm`
- `open`
- `opening`
- `options`
- `overview`
- `pages`
- `plunk`
- `plus`
- `png`
- `pnpm`
- `pointer`
- `postmark`
- `preview`
- `primary`
- `progress`
- `project`
- `pull`
- `react`
- `render`
- `requests`
- `resend`
- `roadmap`
- `row`
- `running`
- `scaleway`
- `schema`
- `section`
- `sendgrid`
- `ses`
- `setup`
- `started`
- `strict`
- `svg`
- `tailwind`
- `tests`
- `text`
- `theme`
- `type`
- `updating`
- `user`
- `utilities`
- `vercel`
- `workflow`
- `writing`
- `yarn`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

