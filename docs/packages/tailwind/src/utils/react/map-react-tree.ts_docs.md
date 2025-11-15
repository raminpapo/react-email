# Documentation: map-react-tree.ts
**File Path:** `packages/tailwind/src/utils/react/map-react-tree.ts`
**Language:** typescript
**Size:** 2,045 bytes
**Lines:** 56
**Generated:** 2025-11-15T20:37:32.415542Z

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

- **Path:** `packages/tailwind/src/utils/react/map-react-tree.ts`
- **Name:** `map-react-tree.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 2,045 bytes (2.00 KB)
- **Lines of Code:** 56

---

## Original Source

```typescript
import React from 'react';
import { isComponent } from './is-component';

/**
 * A function made for deep mapping a React tree from a node, even through its components.
 * For all the components it finds, it renders them by directly calling them. This has a few issues
 * with hooks, and the only solution is `renderAsync` here, which will probably be done in the future.
 *
 * @param process - The callback that will be called every time a new element has been reached.
 *
 * For components, this is going to be called, most of the time, two times. This is because the best
 * approach is to process *both* before rendering the components (i.e. on the props.children of a component element)
 * and after rendering them because the children themselves might have been modified in the component's
 * rendering.
 */
export function mapReactTree(
  value: React.ReactNode,
  process: (node: React.ReactNode) => React.ReactNode,
): React.ReactNode {
  const mapped = React.Children.map(value, (node) => {
    if (React.isValidElement<{ children?: React.ReactNode }>(node)) {
      const newProps = { ...node.props };

      if (node.props.children && !isComponent(node)) {
        newProps.children = mapReactTree(node.props.children, process);
      }

      const processed = process(
        React.cloneElement(node, newProps, newProps.children),
      );

      if (
        React.isValidElement<{ children?: React.ReactNode }>(processed) &&
        isComponent(processed)
      ) {
        const OriginalComponent =
          typeof processed.type === 'object'
            ? // @ts-expect-error - we know this is a component with a render function
              (processed.type.render as React.FC)
            : (processed.type as React.FC);

        const rendered = OriginalComponent(processed.props);
        const mappedRenderedNode = mapReactTree(rendered, process);

        return mappedRenderedNode;
      }

      return processed;
    }

    return process(node);
  });

  return mapped && mapped.length === 1 ? mapped[0] : mapped;
}

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `OriginalComponent()`
- `mapReactTree()`
- `mapped()`
- `mappedRenderedNode()`
- `newProps()`
- `processed()`
- `rendered()`

### Dependencies

This file imports/requires:

- `./is-component`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 73

- `Children`
- `OriginalComponent`
- `React`
- `ReactNode`
- `after`
- `all`
- `approach`
- `because`
- `before`
- `best`
- `both`
- `callback`
- `called`
- `calling`
- `children`
- `cloneElement`
- `component`
- `components`
- `deep`
- `directly`
- `done`
- `element`
- `error`
- `even`
- `every`
- `expect`
- `few`
- `finds`
- `future`
- `going`
- `here`
- `hooks`
- `isComponent`
- `isValidElement`
- `issues`
- `its`
- `know`
- `length`
- `made`
- `map`
- `mapReactTree`
- `mapped`
- `mappedRenderedNode`
- `mapping`
- `modified`
- `most`
- `newProps`
- `node`
- `object`
- `only`
- `param`
- `probably`
- `process`
- `processed`
- `props`
- `reached`
- `react`
- `render`
- `renderAsync`
- `rendered`
- `rendering`
- `renders`
- `solution`
- `them`
- `themselves`
- `through`
- `time`
- `times`
- `tree`
- `two`
- `type`
- `value`
- `which`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

