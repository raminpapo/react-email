# Documentation: MeshImageMaterial.ts
**File Path:** `apps/web/src/webgl/materials/MeshImageMaterial.ts`
**Language:** typescript
**Size:** 901 bytes
**Lines:** 32
**Generated:** 2025-11-15T20:37:32.884459Z

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

- **Path:** `apps/web/src/webgl/materials/MeshImageMaterial.ts`
- **Name:** `MeshImageMaterial.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 901 bytes (0.88 KB)
- **Lines of Code:** 32

---

## Original Source

```typescript
import { extend } from '@react-three/fiber';
import * as THREE from 'three';

export class MeshImageMaterial extends THREE.MeshBasicMaterial {
  constructor(parameters: THREE.MeshBasicMaterialParameters = {}) {
    super(parameters);
  }
  onBeforeCompile = (shader: THREE.Shader) => {
    shader.fragmentShader = shader.fragmentShader.replace(
      '#include <color_fragment>',
      /* glsl */ `#include <color_fragment>
                if (!gl_FrontFacing) {
                    vec3 blackCol = vec3(0.0);
                    diffuseColor.rgb = mix(diffuseColor.rgb, blackCol, 0.86);
                }
            `,
    );
  };
}

extend({ MeshImageMaterial });

// Extend ThreeElements to include our custom material
declare module '@react-three/fiber' {
  interface ThreeElements {
    meshImageMaterial: THREE.Object3DNode<
      MeshImageMaterial,
      typeof MeshImageMaterial
    >;
  }
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Classes

The following classes are defined:

- `MeshImageMaterial`

### Interfaces

- `ThreeElements`

### Dependencies

This file imports/requires:

- `@react-three/fiber`
- `three`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 34

- `Extend`
- `MeshBasicMaterial`
- `MeshBasicMaterialParameters`
- `MeshImageMaterial`
- `Object3DNode`
- `Shader`
- `ThreeElements`
- `blackCol`
- `color_fragment`
- `constructor`
- `custom`
- `declare`
- `diffuseColor`
- `extend`
- `extends`
- `fiber`
- `fragmentShader`
- `glsl`
- `include`
- `interface`
- `material`
- `meshImageMaterial`
- `mix`
- `module`
- `onBeforeCompile`
- `our`
- `parameters`
- `react`
- `replace`
- `rgb`
- `shader`
- `super`
- `three`
- `vec3`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

