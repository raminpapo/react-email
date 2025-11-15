# Documentation: code-preview-line-link.tsx
**File Path:** `packages/preview-server/src/components/toolbar/code-preview-line-link.tsx`
**Language:** tsx
**Size:** 865 bytes
**Lines:** 40
**Generated:** 2025-11-15T20:37:32.171168Z

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

- **Path:** `packages/preview-server/src/components/toolbar/code-preview-line-link.tsx`
- **Name:** `code-preview-line-link.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 865 bytes (0.84 KB)
- **Lines of Code:** 40

---

## Original Source

```tsx
import Link from 'next/link';
import { useSearchParams } from 'next/navigation';

interface CodePreviewLineLinkProps {
  line: number;
  column: number;

  type: 'react' | 'html';
}

export const CodePreviewLineLink = ({
  line,
  type,
}: CodePreviewLineLinkProps) => {
  const searchParams = useSearchParams();

  const newSearchParams = new URLSearchParams(searchParams);
  newSearchParams.set('view', 'source');
  if (type === 'html') {
    newSearchParams.set('lang', 'markup');
  } else if (type === 'react') {
    newSearchParams.set('lang', 'jsx');
  }

  const fragmentIdentifier = `#L${line}`;

  return (
    <Link
      href={{
        search: newSearchParams.toString(),
        hash: fragmentIdentifier,
      }}
      scroll={false}
      className="appearance-none underline mx-2"
    >
      L{line.toString().padStart(2, '0')}
    </Link>
  );
};

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `CodePreviewLineLink()`
- `fragmentIdentifier()`
- `newSearchParams()`
- `searchParams()`

### Interfaces

- `CodePreviewLineLinkProps`

### Dependencies

This file imports/requires:

- `next/link`
- `next/navigation`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 33

- `CodePreviewLineLink`
- `CodePreviewLineLinkProps`
- `Link`
- `URLSearchParams`
- `appearance`
- `className`
- `column`
- `fragmentIdentifier`
- `hash`
- `href`
- `html`
- `interface`
- `jsx`
- `lang`
- `line`
- `link`
- `markup`
- `navigation`
- `newSearchParams`
- `next`
- `number`
- `padStart`
- `react`
- `scroll`
- `search`
- `searchParams`
- `set`
- `source`
- `toString`
- `type`
- `underline`
- `useSearchParams`
- `view`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

