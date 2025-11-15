# Documentation: Billboard.tsx
**File Path:** `apps/web/src/webgl/Billboard.tsx`
**Language:** tsx
**Size:** 1,404 bytes
**Lines:** 49
**Generated:** 2025-11-15T20:37:32.877235Z

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

- **Path:** `apps/web/src/webgl/Billboard.tsx`
- **Name:** `Billboard.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,404 bytes (1.37 KB)
- **Lines of Code:** 49

---

## Original Source

```tsx
'use client';

import { useFrame } from '@react-three/fiber';
import { useRef } from 'react';
import * as THREE from 'three';

import '@/webgl/materials/MeshImageMaterial';

function setupCylinderTextureMapping(texture, dimensions, radius, height) {
  const cylinderCircumference = 2 * Math.PI * radius;
  const cylinderHeight = height;
  const cylinderAspectRatio = cylinderCircumference / cylinderHeight;

  if (dimensions.aspectRatio > cylinderAspectRatio) {
    // Canvas is wider than cylinder proportionally
    texture.repeat.x = cylinderAspectRatio / dimensions.aspectRatio;
    texture.repeat.y = 1;
    texture.offset.x = (1 - texture.repeat.x) / 2;
  } else {
    // Canvas is taller than cylinder proportionally
    texture.repeat.x = 1;
    texture.repeat.y = dimensions.aspectRatio / cylinderAspectRatio;
  }

  // Center the texture
  texture.offset.y = (1 - texture.repeat.y) / 2;
}

export function Billboard({ texture, dimensions, radius = 5, ...props }) {
  const ref = useRef(null);

  setupCylinderTextureMapping(texture, dimensions, radius, 2);

  useFrame((_state, delta) => {
    if (texture) texture.offset.x += delta * 0.001;
  });

  return (
    <mesh ref={ref} {...props}>
      <cylinderGeometry args={[radius, radius, 2, 100, 1, true]} />
      <meshImageMaterial
        map={texture}
        side={THREE.DoubleSide}
        toneMapped={false}
      />
    </mesh>
  );
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Billboard()`
- `cylinderAspectRatio()`
- `cylinderCircumference()`
- `cylinderHeight()`
- `ref()`
- `setupCylinderTextureMapping()`

### Dependencies

This file imports/requires:

- `@/webgl/materials/MeshImageMaterial`
- `@react-three/fiber`
- `react`
- `three`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 42

- `Billboard`
- `Canvas`
- `Center`
- `DoubleSide`
- `Math`
- `MeshImageMaterial`
- `_state`
- `args`
- `aspectRatio`
- `client`
- `cylinder`
- `cylinderAspectRatio`
- `cylinderCircumference`
- `cylinderGeometry`
- `cylinderHeight`
- `delta`
- `dimensions`
- `fiber`
- `height`
- `map`
- `materials`
- `mesh`
- `meshImageMaterial`
- `offset`
- `proportionally`
- `props`
- `radius`
- `react`
- `ref`
- `repeat`
- `setupCylinderTextureMapping`
- `side`
- `taller`
- `texture`
- `than`
- `three`
- `toneMapped`
- `use`
- `useFrame`
- `useRef`
- `webgl`
- `wider`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

