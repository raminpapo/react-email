# Documentation: is-component.ts
**File Path:** `packages/tailwind/src/utils/react/is-component.ts`
**Language:** typescript
**Size:** 1,064 bytes
**Lines:** 37
**Generated:** 2025-11-15T20:37:32.412114Z

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

- **Path:** `packages/tailwind/src/utils/react/is-component.ts`
- **Name:** `is-component.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,064 bytes (1.04 KB)
- **Lines of Code:** 37

---

## Original Source

```typescript
import { Body } from '@react-email/body';
import { Button } from '@react-email/button';
import { CodeBlock } from '@react-email/code-block';
import { CodeInline } from '@react-email/code-inline';
import { Container } from '@react-email/container';
import { Heading } from '@react-email/heading';
import { Hr } from '@react-email/hr';
import { Img } from '@react-email/img';
import { Link } from '@react-email/link';
import { Preview } from '@react-email/preview';
import { Text } from '@react-email/text';

const componentsToTreatAsElements: React.ReactElement['type'][] = [
  Body,
  Button,
  CodeBlock,
  CodeInline,
  Container,
  Heading,
  Hr,
  Img,
  Link,
  Preview,
  Text,
];

export const isComponent = (
  element: React.ReactElement,
): element is React.ReactElement<unknown, React.FC<unknown>> => {
  return (
    (typeof element.type === 'function' ||
      // @ts-expect-error - we know this is a component that may have a render function
      element.type.render !== undefined) &&
    !componentsToTreatAsElements.includes(element.type)
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

- `isComponent()`

### Dependencies

This file imports/requires:

- `@react-email/body`
- `@react-email/button`
- `@react-email/code-block`
- `@react-email/code-inline`
- `@react-email/container`
- `@react-email/heading`
- `@react-email/hr`
- `@react-email/img`
- `@react-email/link`
- `@react-email/preview`
- `@react-email/text`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 36

- `Body`
- `Button`
- `CodeBlock`
- `CodeInline`
- `Container`
- `Heading`
- `Img`
- `Link`
- `Preview`
- `React`
- `ReactElement`
- `Text`
- `block`
- `body`
- `button`
- `code`
- `component`
- `componentsToTreatAsElements`
- `container`
- `element`
- `email`
- `error`
- `expect`
- `heading`
- `img`
- `includes`
- `inline`
- `isComponent`
- `know`
- `link`
- `preview`
- `react`
- `render`
- `text`
- `type`
- `unknown`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

