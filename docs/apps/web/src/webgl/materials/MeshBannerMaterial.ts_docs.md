# Documentation: MeshBannerMaterial.ts
**File Path:** `apps/web/src/webgl/materials/MeshBannerMaterial.ts`
**Language:** typescript
**Size:** 1,268 bytes
**Lines:** 43
**Generated:** 2025-11-15T20:37:32.883296Z

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

- **Path:** `apps/web/src/webgl/materials/MeshBannerMaterial.ts`
- **Name:** `MeshBannerMaterial.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,268 bytes (1.24 KB)
- **Lines of Code:** 43

---

## Original Source

```typescript
import { extend } from '@react-three/fiber';
import * as THREE from 'three';

interface MeshBannerMaterialParameters
  extends THREE.MeshBasicMaterialParameters {
  backfaceRepeatX?: number;
}

export class MeshBannerMaterial extends THREE.MeshBasicMaterial {
  backfaceRepeatX: number;

  constructor(parameters: MeshBannerMaterialParameters = {}) {
    super(parameters);

    this.backfaceRepeatX = parameters.backfaceRepeatX ?? 1.0;
  }

  onBeforeCompile = (shader: THREE.Shader) => {
    shader.uniforms.repeatX = { value: this.backfaceRepeatX };
    shader.fragmentShader = shader.fragmentShader
      .replace(
        '#include <common>',
        /* glsl */ `#include <common>
                uniform float repeatX;

                vec3 pal( in float t, in vec3 a, in vec3 b, in vec3 c, in vec3 d ) {
                    return a + b*cos( 6.28318*(c*t+d) );
                }
            `,
      )
      .replace(
        '#include <color_fragment>',
        /* glsl */ `#include <color_fragment>
                if (!gl_FrontFacing) {
                    diffuseColor.rgb = pal( vMapUv.x * repeatX, vec3(0.0,0.2,0.3),vec3(0.0,0.2,0.3),vec3(1.0,1.0,1.0),vec3(0.0,0.0,0.0) );
                }
            `,
      );
  };
}

extend({ MeshBannerMaterial });

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Classes

The following classes are defined:

- `MeshBannerMaterial`

### Interfaces

- `MeshBannerMaterialParameters`

### Dependencies

This file imports/requires:

- `@react-three/fiber`
- `three`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 35

- `MeshBannerMaterial`
- `MeshBannerMaterialParameters`
- `MeshBasicMaterial`
- `MeshBasicMaterialParameters`
- `Shader`
- `backfaceRepeatX`
- `color_fragment`
- `common`
- `constructor`
- `cos`
- `diffuseColor`
- `extend`
- `extends`
- `fiber`
- `float`
- `fragmentShader`
- `glsl`
- `include`
- `interface`
- `number`
- `onBeforeCompile`
- `pal`
- `parameters`
- `react`
- `repeatX`
- `replace`
- `rgb`
- `shader`
- `super`
- `three`
- `uniform`
- `uniforms`
- `vMapUv`
- `value`
- `vec3`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

