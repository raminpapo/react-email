# Documentation: deployment.mdx
**File Path:** `apps/docs/deployment.mdx`
**Language:** Unknown
**Size:** 945 bytes
**Lines:** 39
**Generated:** 2025-11-15T20:37:32.706333Z

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

- **Path:** `apps/docs/deployment.mdx`
- **Name:** `deployment.mdx`
- **Extension:** `.mdx`
- **Language:** Unknown
- **Size:** 945 bytes (0.92 KB)
- **Lines of Code:** 39

---

## Original Source

```
---
title: "Deployment"
sidebarTitle: "Deployment"
description: "How to deploy the `email dev` preview server to Vercel"
"og:image": "https://react.email/static/covers/react-email.png"
icon: "rocket"
---

<Steps>
  <Step title="Add 'build' script to ./package.json">
    ```diff
     {
       "scripts": {
    +    "build": "email build"
       }
     }
    ```
  </Step>
  <Step title="Change 'Framework Preset' on Vercel's project settings to Next.js">
    You also need to add "next" on `devDependencies` to work properly:

    ```diff
     {
       "devDependencies": {
    +    "next": "*",
       }
     }
    ```

    This is a limitation on Vercel's Next Framework Preset.
  </Step>
  <Step title="Change 'Output Directory' to .react-email/.next">
    In the end, your settings should look like this:

    <Frame>
      <img alt="Proper Vercel settings" src="/images/preview-server-vercel-settings.png" />
    </Frame>
  </Step>
</Steps>
```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 56

- `Add`
- `Change`
- `Deployment`
- `Directory`
- `Frame`
- `Framework`
- `How`
- `Next`
- `Output`
- `Preset`
- `Proper`
- `Step`
- `Steps`
- `Vercel`
- `You`
- `add`
- `also`
- `alt`
- `build`
- `covers`
- `deploy`
- `description`
- `dev`
- `devDependencies`
- `diff`
- `email`
- `end`
- `https`
- `icon`
- `image`
- `images`
- `img`
- `json`
- `like`
- `limitation`
- `look`
- `need`
- `next`
- `package`
- `png`
- `preview`
- `project`
- `properly`
- `react`
- `rocket`
- `script`
- `scripts`
- `server`
- `settings`
- `sidebarTitle`
- `src`
- `static`
- `title`
- `vercel`
- `work`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

