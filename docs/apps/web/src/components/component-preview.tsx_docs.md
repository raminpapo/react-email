# Documentation: component-preview.tsx
**File Path:** `apps/web/src/components/component-preview.tsx`
**Language:** tsx
**Size:** 1,573 bytes
**Lines:** 61
**Generated:** 2025-11-15T20:37:32.893324Z

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

- **Path:** `apps/web/src/components/component-preview.tsx`
- **Name:** `component-preview.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,573 bytes (1.54 KB)
- **Lines of Code:** 61

---

## Original Source

```tsx
import classNames from 'classnames';
import * as React from 'react';

interface ComponentPreviewProps {
  activeView: string;
  className?: string;
  html: string;
}

export function ComponentPreview({
  activeView,
  className,
  html,
}: ComponentPreviewProps) {
  const iframeRef = React.useRef<HTMLIFrameElement>(null);

  React.useEffect(() => {
    const handleResize = () => {
      if (iframeRef.current) {
        const iframeDocument = iframeRef.current.contentDocument;
        if (iframeDocument) {
          const body = iframeDocument.body;
          const htmlFrame = iframeDocument.documentElement;
          const height = Math.max(
            body.scrollHeight,
            body.offsetHeight,
            htmlFrame.clientHeight,
            htmlFrame.scrollHeight,
            htmlFrame.offsetHeight,
          );
          iframeRef.current.style.height = `${height + 20}px`;
        }
      }
    };

    const iframe = iframeRef.current;
    if (iframe) {
      iframe.addEventListener('load', handleResize);

      handleResize();

      return () => {
        iframe.removeEventListener('load', handleResize);
      };
    }
  }, []);

  return (
    <iframe
      className={classNames(
        'relative z-[2] m-auto flex h-fit overflow-y-hidden rounded-md bg-zinc-200 transition-none duration-300 ease-[cubic-bezier(.36,.66,.6,1)] [transition-behavior:allow-discrete]',
        activeView === 'mobile' ? 'w-[22.5rem]' : 'w-full',
        className,
      )}
      ref={iframeRef}
      srcDoc={html}
      title="Component preview"
    />
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

- `ComponentPreview()`
- `body()`
- `handleResize()`
- `height()`
- `htmlFrame()`
- `iframe()`
- `iframeDocument()`
- `iframeRef()`

### Interfaces

- `ComponentPreviewProps`

### Dependencies

This file imports/requires:

- `classnames`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 56

- `Component`
- `ComponentPreview`
- `ComponentPreviewProps`
- `HTMLIFrameElement`
- `Math`
- `React`
- `activeView`
- `addEventListener`
- `allow`
- `auto`
- `behavior`
- `bezier`
- `body`
- `className`
- `classNames`
- `classnames`
- `clientHeight`
- `contentDocument`
- `cubic`
- `current`
- `discrete`
- `documentElement`
- `duration`
- `ease`
- `fit`
- `flex`
- `full`
- `handleResize`
- `height`
- `hidden`
- `html`
- `htmlFrame`
- `iframe`
- `iframeDocument`
- `iframeRef`
- `interface`
- `load`
- `max`
- `mobile`
- `offsetHeight`
- `overflow`
- `preview`
- `react`
- `ref`
- `relative`
- `removeEventListener`
- `rounded`
- `scrollHeight`
- `srcDoc`
- `string`
- `style`
- `title`
- `transition`
- `useEffect`
- `useRef`
- `zinc`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

