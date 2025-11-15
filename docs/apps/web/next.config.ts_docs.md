# Documentation: next.config.ts
**File Path:** `apps/web/next.config.ts`
**Language:** typescript
**Size:** 1,220 bytes
**Lines:** 49
**Generated:** 2025-11-15T20:37:32.792520Z

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

- **Path:** `apps/web/next.config.ts`
- **Name:** `next.config.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,220 bytes (1.19 KB)
- **Lines of Code:** 49

---

## Original Source

```typescript
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  serverExternalPackages: ['@react-email/components', '@react-email/render'],
  async redirects() {
    return [
      {
        source: '/examples',
        destination: '/templates',
        permanent: true,
      },
    ];
  },
  async rewrites() {
    return [
      {
        source: '/docs',
        destination: 'https://react-email.mintlify.dev/docs',
      },
      {
        source: '/docs/:match*',
        destination: 'https://react-email.mintlify.dev/docs/:match*',
      },
    ];
  },
  async headers() {
    return [
      {
        source: '/api/:path*',
        headers: [
          { key: 'Access-Control-Allow-Credentials', value: 'true' },
          { key: 'Access-Control-Allow-Origin', value: '*' },
          {
            key: 'Access-Control-Allow-Methods',
            value: 'GET,OPTIONS,PATCH,DELETE,POST,PUT',
          },
          {
            key: 'Access-Control-Allow-Headers',
            value:
              'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version',
          },
        ],
      },
    ];
  },
};

export default nextConfig;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Dependencies

This file imports/requires:

- `next`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 43

- `Accept`
- `Access`
- `Allow`
- `Api`
- `Content`
- `Control`
- `Credentials`
- `Date`
- `Headers`
- `Length`
- `MD5`
- `Methods`
- `NextConfig`
- `Origin`
- `Requested`
- `Token`
- `Type`
- `Version`
- `api`
- `components`
- `destination`
- `dev`
- `docs`
- `email`
- `examples`
- `headers`
- `https`
- `key`
- `match`
- `mintlify`
- `next`
- `nextConfig`
- `path`
- `permanent`
- `react`
- `redirects`
- `render`
- `rewrites`
- `serverExternalPackages`
- `source`
- `templates`
- `type`
- `value`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

