# Documentation: three.d.ts
**File Path:** `apps/web/src/types/three.d.ts`
**Language:** typescript
**Size:** 314 bytes
**Lines:** 13
**Generated:** 2025-11-15T20:37:32.803565Z

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

- **Path:** `apps/web/src/types/three.d.ts`
- **Name:** `three.d.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 314 bytes (0.31 KB)
- **Lines of Code:** 13

---

## Original Source

```typescript
import * as THREE from 'three';

declare module '@react-three/fiber' {
  interface ThreeElements {
    meshBannerMaterial: Partial<THREE.MeshBasicMaterialParameters> & {
      backfaceRepeatX?: number;
      map?: THREE.Texture;
      'map-anisotropy'?: number;
      'map-repeat'?: [number, number];
    };
  }
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Interfaces

- `ThreeElements`

### Dependencies

This file imports/requires:

- `three`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 16

- `MeshBasicMaterialParameters`
- `Partial`
- `Texture`
- `ThreeElements`
- `anisotropy`
- `backfaceRepeatX`
- `declare`
- `fiber`
- `interface`
- `map`
- `meshBannerMaterial`
- `module`
- `number`
- `react`
- `repeat`
- `three`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

