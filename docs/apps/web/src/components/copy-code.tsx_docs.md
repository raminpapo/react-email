# Documentation: copy-code.tsx
**File Path:** `apps/web/src/components/copy-code.tsx`
**Language:** tsx
**Size:** 2,303 bytes
**Lines:** 79
**Generated:** 2025-11-15T20:37:32.898000Z

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

- **Path:** `apps/web/src/components/copy-code.tsx`
- **Name:** `copy-code.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 2,303 bytes (2.25 KB)
- **Lines of Code:** 79

---

## Original Source

```tsx
import classNames from 'classnames';
import { AnimatePresence, motion } from 'framer-motion';
import { CheckIcon, ClipboardIcon } from 'lucide-react';
import { useState } from 'react';
import { IconButton } from './icon-button';

export const CopyCode = ({
  code,
  className,
}: {
  code: string;
  className?: string;
}) => {
  const [isCopied, setIsCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);

    setIsCopied(true);

    setTimeout(() => {
      setIsCopied(false);
    }, 1500);
  };

  return (
    <IconButton
      onKeyUp={(event) => {
        event.preventDefault();

        if (event.key === 'Enter') {
          handleCopy();
        }
      }}
      disabled={isCopied}
      onClick={handleCopy}
      className={classNames(
        'p-2.5 flex items-center justify-center rounded-xl duration-200',
        'shadow-[0px_32px_64px_-16px_transparent,0px_16px_32px_-8px_transparent,0px_8px_16px_-4px_transparent,0px_4px_8px_-2px_transparent,0px_-8px_16px_-1px_transparent,0px_2px_4px_-1px_transparent,0px_0px_0px_1px_transparent,inset_0px_0px_0px_1px_rgba(255,255,255,0.1),inset_0px_1px_0px_rgb(255,255,255,0.15)] enabled:hover:bg-zinc-900/80',
        className,
      )}
    >
      <AnimatePresence mode="popLayout" initial={false}>
        {isCopied ? (
          <motion.span
            key="copied"
            className="ml-px"
            initial={{ scale: 0 }}
            animate={{ scale: 1, filter: 'blur(0)' }}
            exit={{ scale: 0, filter: 'blur(2px)' }}
            transition={{
              type: 'spring',
              bounce: 0,
              duration: 0.3,
            }}
          >
            <CheckIcon className="size-4 text-slate-12" />
          </motion.span>
        ) : (
          <motion.span
            key="copy"
            className="ml-px"
            initial={{ scale: 0 }}
            animate={{ scale: 1, filter: 'blur(0)' }}
            exit={{ scale: 0, filter: 'blur(2px)' }}
            transition={{
              type: 'spring',
              bounce: 0,
              duration: 0.3,
            }}
          >
            <ClipboardIcon className="size-4 text-slate-11 transition-colors" />
          </motion.span>
        )}
      </AnimatePresence>
    </IconButton>
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

- `CopyCode()`
- `handleCopy()`

### Dependencies

This file imports/requires:

- `./icon-button`
- `classnames`
- `framer-motion`
- `lucide-react`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 62

- `AnimatePresence`
- `CheckIcon`
- `ClipboardIcon`
- `CopyCode`
- `Enter`
- `IconButton`
- `animate`
- `blur`
- `bounce`
- `button`
- `center`
- `className`
- `classNames`
- `classnames`
- `clipboard`
- `code`
- `colors`
- `copied`
- `copy`
- `disabled`
- `duration`
- `enabled`
- `event`
- `exit`
- `filter`
- `flex`
- `framer`
- `handleCopy`
- `hover`
- `icon`
- `initial`
- `inset_0px_0px_0px_1px_rgba`
- `inset_0px_1px_0px_rgb`
- `isCopied`
- `items`
- `justify`
- `key`
- `lucide`
- `mode`
- `motion`
- `navigator`
- `onClick`
- `onKeyUp`
- `popLayout`
- `preventDefault`
- `react`
- `rounded`
- `scale`
- `setIsCopied`
- `setTimeout`
- `shadow`
- `size`
- `slate`
- `span`
- `spring`
- `string`
- `text`
- `transition`
- `type`
- `useState`
- `writeText`
- `zinc`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

