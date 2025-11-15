# Documentation: package.json
**File Path:** `packages/render/package.json`
**Language:** json
**Size:** 3,467 bytes
**Lines:** 137
**Generated:** 2025-11-15T20:37:31.467879Z

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

- **Path:** `packages/render/package.json`
- **Name:** `package.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 3,467 bytes (3.39 KB)
- **Lines of Code:** 137

---

## Original Source

```json
{
  "name": "@react-email/render",
  "version": "2.0.0",
  "description": "Transform React components into HTML email templates",
  "sideEffects": false,
  "main": "./dist/browser/index.js",
  "module": "./dist/browser/index.mjs",
  "types": "./dist/browser/index.d.ts",
  "files": [
    "dist/**"
  ],
  "exports": {
    ".": {
      "workerd": {
        "import": {
          "types": "./dist/edge/index.d.mts",
          "default": "./dist/edge/index.mjs"
        },
        "require": {
          "types": "./dist/edge/index.d.ts",
          "default": "./dist/edge/index.js"
        }
      },
      "deno": {
        "import": {
          "types": "./dist/browser/index.d.mts",
          "default": "./dist/browser/index.mjs"
        },
        "require": {
          "types": "./dist/browser/index.d.ts",
          "default": "./dist/browser/index.js"
        }
      },
      "worker": {
        "import": {
          "types": "./dist/browser/index.d.mts",
          "default": "./dist/browser/index.mjs"
        },
        "require": {
          "types": "./dist/browser/index.d.ts",
          "default": "./dist/browser/index.js"
        }
      },
      "edge-light": {
        "import": {
          "types": "./dist/edge/index.d.mts",
          "default": "./dist/edge/index.mjs"
        },
        "require": {
          "types": "./dist/edge/index.d.ts",
          "default": "./dist/edge/index.js"
        }
      },
      "convex": {
        "import": {
          "types": "./dist/edge/index.d.mts",
          "default": "./dist/edge/index.mjs"
        },
        "require": {
          "types": "./dist/edge/index.d.ts",
          "default": "./dist/edge/index.js"
        }
      },
      "node": {
        "import": {
          "types": "./dist/node/index.d.mts",
          "default": "./dist/node/index.mjs"
        },
        "require": {
          "types": "./dist/node/index.d.ts",
          "default": "./dist/node/index.js"
        }
      },
      "browser": {
        "import": {
          "types": "./dist/browser/index.d.mts",
          "default": "./dist/browser/index.mjs"
        },
        "require": {
          "types": "./dist/browser/index.d.ts",
          "default": "./dist/browser/index.js"
        }
      },
      "default": {
        "import": {
          "types": "./dist/node/index.d.mts",
          "default": "./dist/node/index.mjs"
        },
        "require": {
          "types": "./dist/node/index.d.ts",
          "default": "./dist/node/index.js"
        }
      }
    }
  },
  "license": "MIT",
  "scripts": {
    "build": "tsdown",
    "build:watch": "tsdown --watch",
    "clean": "rm -rf dist",
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/resend/react-email.git",
    "directory": "packages/render"
  },
  "keywords": [
    "react",
    "email"
  ],
  "engines": {
    "node": ">=22.0.0"
  },
  "dependencies": {
    "html-to-text": "^9.0.5",
    "prettier": "^3.5.3"
  },
  "peerDependencies": {
    "react": "^18.0 || ^19.0 || ^19.0.0-rc",
    "react-dom": "^18.0 || ^19.0 || ^19.0.0-rc"
  },
  "devDependencies": {
    "@edge-runtime/vm": "5.0.0",
    "@types/html-to-text": "9.0.4",
    "@types/react": "npm:types-react@19.0.0-rc.1",
    "@types/react-dom": "npm:types-react-dom@19.0.0",
    "jsdom": "26.1.0",
    "tsconfig": "workspace:*",
    "typescript": "5.8.3"
  },
  "publishConfig": {
    "access": "public"
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

**Total Unique Identifiers:** 67

- `React`
- `Transform`
- `access`
- `browser`
- `build`
- `clean`
- `com`
- `components`
- `convex`
- `deno`
- `dependencies`
- `description`
- `devDependencies`
- `directory`
- `dist`
- `dom`
- `edge`
- `email`
- `engines`
- `exports`
- `files`
- `git`
- `github`
- `html`
- `https`
- `index`
- `into`
- `jsdom`
- `keywords`
- `license`
- `light`
- `main`
- `mjs`
- `module`
- `mts`
- `name`
- `node`
- `npm`
- `packages`
- `peerDependencies`
- `prettier`
- `public`
- `publishConfig`
- `react`
- `render`
- `repository`
- `require`
- `resend`
- `run`
- `runtime`
- `scripts`
- `sideEffects`
- `templates`
- `test`
- `text`
- `tsconfig`
- `tsdown`
- `type`
- `types`
- `typescript`
- `url`
- `version`
- `vitest`
- `watch`
- `worker`
- `workerd`
- `workspace`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

