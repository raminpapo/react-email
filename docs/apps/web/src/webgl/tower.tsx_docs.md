# Documentation: tower.tsx
**File Path:** `apps/web/src/webgl/tower.tsx`
**Language:** tsx
**Size:** 3,874 bytes
**Lines:** 146
**Generated:** 2025-11-15T20:37:32.881735Z

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

- **Path:** `apps/web/src/webgl/tower.tsx`
- **Name:** `tower.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 3,874 bytes (3.78 KB)
- **Lines of Code:** 146

---

## Original Source

```tsx
'use client';

import { PerspectiveCamera } from '@react-three/drei';
import { useFrame, useThree } from '@react-three/fiber';
import { useEffect, useRef, useState } from 'react';
import type { Group } from 'three';
import { useCollageTexture } from '@/hooks/useCollageTexture';
import { Billboard } from '@/webgl/Billboard';
import { View } from '@/webgl/View';

const COUNT = 12;
const GAP = 3.5;
const IMAGES = [
  { url: '/static/components/0.jpeg' },
  { url: '/static/components/1.jpeg' },
  { url: '/static/components/2.jpeg' },
  { url: '/static/components/3.jpeg' },
  { url: '/static/components/4.jpeg' },
  { url: '/static/components/0.jpeg' },
  { url: '/static/components/1.jpeg' },
  { url: '/static/components/2.jpeg' },
  { url: '/static/components/3.jpeg' },
  { url: '/static/components/4.jpeg' },
];

function Loader() {
  return (
    <div className="w-full h-full flex items-center justify-center">
      <div className="text-white/30">Loading...</div>
    </div>
  );
}

function SpinnableTower({ texture, dimensions }: any) {
  const groupRef = useRef<Group>(null);
  const { size } = useThree();
  const [isDragging, setIsDragging] = useState(false);
  const velocity = useRef(0);
  const lastX = useRef(0);
  const rotationY = useRef(0.5);

  // Apply rotation with damping
  useFrame((_state, delta) => {
    if (!groupRef.current) return;

    if (!isDragging) {
      // Apply velocity and damping
      rotationY.current += velocity.current * delta;
      velocity.current *= 0.95; // Damping factor
    }

    groupRef.current.rotation.y = rotationY.current;
  });

  useEffect(() => {
    if (!isDragging) return;

    const handlePointerMove = (e: PointerEvent) => {
      const deltaX = e.clientX - lastX.current;
      const rotationDelta = (deltaX / size.width) * Math.PI * 2;

      rotationY.current += rotationDelta;
      velocity.current = rotationDelta * 60; // Store velocity for momentum

      lastX.current = e.clientX;
    };

    const handlePointerUp = () => {
      setIsDragging(false);
      document.body.style.cursor = '';
    };

    window.addEventListener('pointermove', handlePointerMove);
    window.addEventListener('pointerup', handlePointerUp);

    return () => {
      window.removeEventListener('pointermove', handlePointerMove);
      window.removeEventListener('pointerup', handlePointerUp);
      document.body.style.cursor = '';
    };
  }, [isDragging, size.width]);

  const handlePointerDown = (e: any) => {
    e.stopPropagation();
    setIsDragging(true);
    lastX.current = e.clientX;
    velocity.current = 0;
  };

  const handlePointerEnter = () => {
    if (!isDragging) {
      document.body.style.cursor = 'grab';
    }
  };

  const handlePointerLeave = () => {
    if (!isDragging) {
      document.body.style.cursor = '';
    }
  };

  return (
    <group
      ref={groupRef}
      rotation={[-0.2, 0.5, 0.2]}
      position={[5, 0, 0]}
      scale={1}
      onPointerDown={handlePointerDown}
      onPointerEnter={handlePointerEnter}
      onPointerLeave={handlePointerLeave}
    >
      {Array.from({ length: COUNT }).map((_, index) => [
        <Billboard
          key={`billboard-${index}`}
          radius={4}
          rotation={[0, index * Math.PI * 0.5, 0.25]}
          position={[0, (index - (Math.ceil(COUNT / 2) - 1)) * GAP, 0]}
          texture={texture}
          dimensions={dimensions}
        />,
      ])}
    </group>
  );
}

export function Tower() {
  const { texture, dimensions, isLoading } = useCollageTexture(IMAGES);

  if (isLoading) return <Loader />;

  if (!texture) return null;

  return (
    <View className="w-full h-full">
      <PerspectiveCamera
        makeDefault
        fov={7}
        position={[0, 0, 70]}
        near={0.01}
        far={100000}
      />
      <SpinnableTower texture={texture} dimensions={dimensions} />
    </View>
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

- `COUNT()`
- `GAP()`
- `IMAGES()`
- `Loader()`
- `SpinnableTower()`
- `Tower()`
- `deltaX()`
- `groupRef()`
- `handlePointerDown()`
- `handlePointerEnter()`
- `handlePointerLeave()`
- `handlePointerMove()`
- `handlePointerUp()`
- `lastX()`
- `rotationDelta()`
- `rotationY()`
- `velocity()`

### Dependencies

This file imports/requires:

- `@/hooks/useCollageTexture`
- `@/webgl/Billboard`
- `@/webgl/View`
- `@react-three/drei`
- `@react-three/fiber`
- `react`
- `three`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 98

- `Apply`
- `Array`
- `Billboard`
- `Damping`
- `Group`
- `Loader`
- `Loading`
- `Math`
- `PerspectiveCamera`
- `PointerEvent`
- `SpinnableTower`
- `Store`
- `Tower`
- `View`
- `_state`
- `addEventListener`
- `any`
- `billboard`
- `body`
- `ceil`
- `center`
- `className`
- `client`
- `clientX`
- `components`
- `current`
- `cursor`
- `damping`
- `delta`
- `deltaX`
- `dimensions`
- `div`
- `document`
- `drei`
- `factor`
- `far`
- `fiber`
- `flex`
- `fov`
- `full`
- `grab`
- `group`
- `groupRef`
- `handlePointerDown`
- `handlePointerEnter`
- `handlePointerLeave`
- `handlePointerMove`
- `handlePointerUp`
- `hooks`
- `index`
- `isDragging`
- `isLoading`
- `items`
- `jpeg`
- `justify`
- `key`
- `lastX`
- `length`
- `makeDefault`
- `map`
- `momentum`
- `near`
- `onPointerDown`
- `onPointerEnter`
- `onPointerLeave`
- `pointermove`
- `pointerup`
- `position`
- `radius`
- `react`
- `ref`
- `removeEventListener`
- `rotation`
- `rotationDelta`
- `rotationY`
- `scale`
- `setIsDragging`
- `size`
- `static`
- `stopPropagation`
- `style`
- `text`
- `texture`
- `three`
- `type`
- `url`
- `use`
- `useCollageTexture`
- `useEffect`
- `useFrame`
- `useRef`
- `useState`
- `useThree`
- `velocity`
- `webgl`
- `white`
- `width`
- `window`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

