# Documentation: component-view.tsx
**File Path:** `apps/web/src/components/component-view.tsx`
**Language:** tsx
**Size:** 5,360 bytes
**Lines:** 144
**Generated:** 2025-11-15T20:37:32.894960Z

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

- **Path:** `apps/web/src/components/component-view.tsx`
- **Name:** `component-view.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 5,360 bytes (5.23 KB)
- **Lines of Code:** 144

---

## Original Source

```tsx
'use client';

import * as Tabs from '@radix-ui/react-tabs';
import { TooltipProvider } from '@radix-ui/react-tooltip';
import classNames from 'classnames';
import * as React from 'react';
import { convertUrisIntoUrls } from '@/utils/convert-uris-into-urls';
import type { ImportedComponent } from '../app/components/get-imported-components-for';
import { ComponentCodeView } from './component-code-view';
import { ComponentPreview } from './component-preview';
import { IconMonitor } from './icons/icon-monitor';
import { IconPhone } from './icons/icon-phone';
import { IconSource } from './icons/icon-source';
import { Send } from './send';
import { TabTrigger } from './tab-trigger';
import { Tooltip, TooltipContent, TooltipTrigger } from './tooltip';

interface ComponentViewProps {
  component: ImportedComponent;
  className?: string;
}

type ActiveView = 'code' | 'desktop' | 'mobile';

const TabTriggetWithTooltip = ({
  tooltip,
  children,
  activeView,
  layoutId,
  value,
}: {
  tooltip: string;
  layoutId: string;
  children: React.ReactNode;
  activeView: string;
  value: string;
}) => (
  <Tooltip>
    <TooltipTrigger asChild>
      <TabTrigger
        className="w-9 !px-0 flex items-center justify-center"
        activeView={activeView}
        layoutId={layoutId}
        value={value}
      >
        {children}
      </TabTrigger>
    </TooltipTrigger>
    <TooltipContent>{tooltip}</TooltipContent>
  </Tooltip>
);

const TabContent: React.FC<{
  value: ActiveView;
  children: React.ReactNode;
  className?: string;
}> = ({ value, children, className = '' }) => (
  <Tabs.Content
    className={`relative m-4 mx-2 h-fit scroll-m-2 overflow-hidden rounded-2xl border border-slate-4 transition-colors focus:outline-none focus:ring focus:ring-slate-8 md:mx-8 ${className}`}
    value={value}
  >
    {children}
  </Tabs.Content>
);

export function ComponentView({ component, className }: ComponentViewProps) {
  const [activeView, setActiveView] = React.useState<ActiveView>('desktop');

  React.useEffect(() => {
    setActiveView(activeView);
  }, []);

  return (
    <Tabs.Root
      className="relative mb-8 flex w-full flex-col gap-2 md:mb-12"
      defaultValue={activeView}
      onValueChange={(value: string) => {
        setActiveView(value as ActiveView);
      }}
    >
      <TooltipProvider>
        <div
          className={classNames(
            'relative flex w-full items-center gap-6 px-6 pb-3 md:px-8',
            className,
          )}
        >
          <h2 className="shrink grow basis-0 text-pretty font-semibold text-lg text-slate-12 md:text-xl">
            {component.title}
          </h2>
          <Tabs.List className="relative flex w-fit items-center overflow-hidden p-1 text-xs">
            <TabTriggetWithTooltip
              activeView={activeView}
              layoutId={`${component.slug}-view`}
              tooltip="Desktop"
              value="desktop"
            >
              <IconMonitor />
            </TabTriggetWithTooltip>
            <TabTriggetWithTooltip
              activeView={activeView}
              layoutId={`${component.slug}-view`}
              tooltip="Mobile"
              value="mobile"
            >
              <IconPhone />
            </TabTriggetWithTooltip>
            <TabTriggetWithTooltip
              activeView={activeView}
              layoutId={`${component.slug}-view`}
              tooltip="Code"
              value="code"
            >
              <IconSource />
            </TabTriggetWithTooltip>
            <Send
              className="ml-2"
              markup={convertUrisIntoUrls(component.code.html).replace(
                /height\s*:\s*100vh;?/,
                '',
              )}
              defaultSubject={component.title}
            />
          </Tabs.List>
          <div className="absolute right-0 bottom-0 h-px w-[100dvw] bg-slate-4" />
        </div>
        <div className="relative h-fit w-full transition-all duration-300 ease-[cubic-bezier(.36,.66,.6,1)] [transition-behavior:allow-discrete]">
          <TabContent value="desktop" className="min-h-[228px]">
            <div className="absolute inset-0 bg-[radial-gradient(#091A21_.0313rem,transparent_.0313rem),_radial-gradient(#091A21_.0313rem,transparent_.0313rem)] bg-transparent opacity-30 transition-all duration-300 ease-[cubic-bezier(.36,.66,.6,1)] [background-position:0_0,.625rem_.625rem] [background-size:1.25rem_1.25rem] [height:calc-size(auto)] [transition-behavior:allow-discrete]" />
            <ComponentPreview activeView="desktop" html={component.code.html} />
          </TabContent>
          <TabContent value="mobile" className="min-h-[228px]">
            <div className="absolute inset-0 bg-[radial-gradient(#091A21_.0313rem,transparent_.0313rem),_radial-gradient(#091A21_.0313rem,transparent_.0313rem)] bg-transparent opacity-30 transition-all duration-300 ease-[cubic-bezier(.36,.66,.6,1)] [background-position:0_0,.625rem_.625rem] [background-size:1.25rem_1.25rem] [height:calc-size(auto)] [transition-behavior:allow-discrete]" />
            <ComponentPreview activeView="mobile" html={component.code.html} />
          </TabContent>
          <TabContent value="code">
            <ComponentCodeView component={component} />
          </TabContent>
        </div>
      </TooltipProvider>
    </Tabs.Root>
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

- `ComponentView()`
- `TabTriggetWithTooltip()`

### Interfaces

- `ComponentViewProps`

### Type Definitions

- `ActiveView`

### Dependencies

This file imports/requires:

- `../app/components/get-imported-components-for`
- `./component-code-view`
- `./component-preview`
- `./icons/icon-monitor`
- `./icons/icon-phone`
- `./icons/icon-source`
- `./send`
- `./tab-trigger`
- `./tooltip`
- `@/utils/convert-uris-into-urls`
- `@radix-ui/react-tabs`
- `@radix-ui/react-tooltip`
- `classnames`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 131

- `ActiveView`
- `Code`
- `ComponentCodeView`
- `ComponentPreview`
- `ComponentView`
- `ComponentViewProps`
- `Content`
- `Desktop`
- `IconMonitor`
- `IconPhone`
- `IconSource`
- `ImportedComponent`
- `List`
- `Mobile`
- `React`
- `ReactNode`
- `Root`
- `Send`
- `TabContent`
- `TabTrigger`
- `TabTriggetWithTooltip`
- `Tabs`
- `Tooltip`
- `TooltipContent`
- `TooltipProvider`
- `TooltipTrigger`
- `_radial`
- `absolute`
- `activeView`
- `all`
- `allow`
- `app`
- `asChild`
- `auto`
- `background`
- `basis`
- `behavior`
- `bezier`
- `border`
- `bottom`
- `calc`
- `center`
- `children`
- `className`
- `classNames`
- `classnames`
- `client`
- `code`
- `col`
- `colors`
- `component`
- `components`
- `convert`
- `convertUrisIntoUrls`
- `cubic`
- `defaultSubject`
- `defaultValue`
- `desktop`
- `discrete`
- `div`
- `duration`
- `ease`
- `fit`
- `flex`
- `focus`
- `font`
- `full`
- `gap`
- `get`
- `gradient`
- `grow`
- `height`
- `hidden`
- `html`
- `icon`
- `icons`
- `imported`
- `inset`
- `interface`
- `into`
- `items`
- `justify`
- `layoutId`
- `markup`
- `min`
- `mobile`
- `monitor`
- `onValueChange`
- `opacity`
- `outline`
- `overflow`
- `phone`
- `position`
- `pretty`
- `preview`
- `radial`
- `radix`
- `react`
- `relative`
- `replace`
- `right`
- `ring`
- `rounded`
- `scroll`
- `semibold`
- `send`
- `setActiveView`
- `shrink`
- `size`
- `slate`
- `slug`
- `source`
- `string`
- `tab`
- `tabs`
- `text`
- `title`
- `tooltip`
- `transition`
- `transparent`
- `transparent_`
- `trigger`
- `type`
- `uris`
- `urls`
- `use`
- `useEffect`
- `useState`
- `utils`
- `value`
- `view`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

