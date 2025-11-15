# Documentation: next.config.mjs
**File Path:** `packages/preview-server/next.config.mjs`
**Language:** Unknown
**Size:** 577 bytes
**Lines:** 16
**Generated:** 2025-11-15T20:37:31.754871Z

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

- **Path:** `packages/preview-server/next.config.mjs`
- **Name:** `next.config.mjs`
- **Extension:** `.mjs`
- **Language:** Unknown
- **Size:** 577 bytes (0.56 KB)
- **Lines of Code:** 16

---

## Original Source

```
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  serverExternalPackages: ['esbuild'],
  // Noticed an issue with typescript transpilation when going from Next 14.1.1 to 14.1.2
  // and I narrowed that down into this PR https://github.com/vercel/next.js/pull/62005
  //
  // What is probably happening is that it's noticing the files for the app are somewhere inside of a `node_modules` and automatically opt-outs of SWC's transpilation.
  //
  // TODO: Open an issue on Nextjs about this.
  transpilePackages: ['react-email'],
};

export default nextConfig;

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 39

- `Next`
- `NextConfig`
- `Nextjs`
- `Noticed`
- `Open`
- `What`
- `about`
- `app`
- `automatically`
- `com`
- `down`
- `email`
- `esbuild`
- `files`
- `github`
- `going`
- `happening`
- `https`
- `inside`
- `into`
- `issue`
- `narrowed`
- `next`
- `nextConfig`
- `node_modules`
- `noticing`
- `opt`
- `outs`
- `probably`
- `pull`
- `react`
- `serverExternalPackages`
- `somewhere`
- `transpilation`
- `transpilePackages`
- `type`
- `typescript`
- `vercel`
- `when`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

