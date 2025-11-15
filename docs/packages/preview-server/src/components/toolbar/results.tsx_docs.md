# Documentation: results.tsx
**File Path:** `packages/preview-server/src/components/toolbar/results.tsx`
**Language:** tsx
**Size:** 898 bytes
**Lines:** 53
**Generated:** 2025-11-15T20:37:32.181114Z

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

- **Path:** `packages/preview-server/src/components/toolbar/results.tsx`
- **Name:** `results.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 898 bytes (0.88 KB)
- **Lines of Code:** 53

---

## Original Source

```tsx
import { cn } from '../../utils';

export const Results = ({
  children,
  className,
  ...props
}: React.ComponentProps<'table'>) => {
  return (
    <table
      {...props}
      className={cn(
        'group relative w-full border-collapse text-left text-slate-10 text-sm',
        className,
      )}
    >
      <tbody>{children}</tbody>
    </table>
  );
};

Results.Row = ({
  children,
  className,
  ...props
}: React.ComponentProps<'tr'>) => {
  return (
    <tr
      className={cn(
        'border-collapse align-bottom border-slate-6 border-b last:border-b-0',
        className,
      )}
      {...props}
    >
      {children}
    </tr>
  );
};

Results.Column = ({
  children,
  className,
  ...props
}: React.ComponentProps<'td'>) => {
  return (
    <td
      className={cn('py-1.5 align-bottom font-regular', className)}
      {...props}
    >
      {children}
    </td>
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

- `Results()`

### Dependencies

This file imports/requires:

- `../../utils`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 24

- `Column`
- `ComponentProps`
- `React`
- `Results`
- `Row`
- `align`
- `border`
- `bottom`
- `children`
- `className`
- `collapse`
- `font`
- `full`
- `group`
- `last`
- `left`
- `props`
- `regular`
- `relative`
- `slate`
- `table`
- `tbody`
- `text`
- `utils`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

