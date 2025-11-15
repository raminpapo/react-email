# Documentation: preview.tsx
**File Path:** `packages/preview-server/src/app/preview/[...slug]/preview.tsx`
**Language:** tsx
**Size:** 8,309 bytes
**Lines:** 243
**Generated:** 2025-11-15T20:37:32.095468Z

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

- **Path:** `packages/preview-server/src/app/preview/[...slug]/preview.tsx`
- **Name:** `preview.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 8,309 bytes (8.11 KB)
- **Lines of Code:** 243

---

## Original Source

```tsx
'use client';

import { usePathname, useRouter, useSearchParams } from 'next/navigation';
import { useState } from 'react';
import { flushSync } from 'react-dom';
import { Toaster } from 'sonner';
import { useDebouncedCallback } from 'use-debounce';
import { Topbar } from '../../../components';
import { CodeContainer } from '../../../components/code-container';
import {
  makeIframeDocumentBubbleEvents,
  ResizableWrapper,
} from '../../../components/resizable-wrapper';
import { Send } from '../../../components/send';
import { useToolbarState } from '../../../components/toolbar';
import { Tooltip } from '../../../components/tooltip';
import { ActiveViewToggleGroup } from '../../../components/topbar/active-view-toggle-group';
import { EmulatedDarkModeToggle } from '../../../components/topbar/emulated-dark-mode-toggle';
import { ViewSizeControls } from '../../../components/topbar/view-size-controls';
import { usePreviewContext } from '../../../contexts/preview';
import { useClampedState } from '../../../hooks/use-clamped-state';
import { cn } from '../../../utils';
import { EmailFrame } from './email-frame';
import { ErrorOverlay } from './error-overlay';

interface PreviewProps extends React.ComponentProps<'div'> {
  emailTitle: string;
}

const Preview = ({ emailTitle, className, ...props }: PreviewProps) => {
  const { renderingResult, renderedEmailMetadata } = usePreviewContext();

  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const isDarkModeEnabled = searchParams.get('dark') !== null;
  const activeView = searchParams.get('view') ?? 'preview';
  const activeLang = searchParams.get('lang') ?? 'tsx';

  const handleDarkModeChange = (enabled: boolean) => {
    const params = new URLSearchParams(searchParams);
    if (enabled) {
      params.set('dark', '');
    } else {
      params.delete('dark');
    }
    router.push(`${pathname}?${params.toString()}${location.hash}`);
  };

  const handleViewChange = (view: string) => {
    const params = new URLSearchParams(searchParams);
    params.set('view', view);
    router.push(`${pathname}?${params.toString()}${location.hash}`);
  };

  const handleLangChange = (lang: string) => {
    const params = new URLSearchParams(searchParams);
    params.set('view', 'source');
    params.set('lang', lang);
    const isSameLang = searchParams.get('lang') === lang;
    router.push(
      `${pathname}?${params.toString()}${isSameLang ? location.hash : ''}`,
    );
  };

  const hasRenderingMetadata = typeof renderedEmailMetadata !== 'undefined';
  const hasErrors = 'error' in renderingResult;

  const [maxWidth, setMaxWidth] = useState(Number.POSITIVE_INFINITY);
  const [maxHeight, setMaxHeight] = useState(Number.POSITIVE_INFINITY);
  const minWidth = 220;
  const minHeight = minWidth * 1.6;
  const storedWidth = searchParams.get('width');
  const storedHeight = searchParams.get('height');
  const [width, setWidth] = useClampedState(
    storedWidth ? Number.parseInt(storedWidth, 10) : 1024,
    minWidth,
    maxWidth,
  );
  const [height, setHeight] = useClampedState(
    storedHeight ? Number.parseInt(storedHeight, 10) : 600,
    minHeight,
    maxHeight,
  );

  const handleSaveViewSize = useDebouncedCallback(() => {
    const params = new URLSearchParams(searchParams);
    params.set('width', width.toString());
    params.set('height', height.toString());
    router.push(`${pathname}?${params.toString()}${location.hash}`);
  }, 300);

  const { toggled: toolbarToggled } = useToolbarState();

  return (
    <>
      <Topbar emailTitle={emailTitle}>
        {activeView === 'preview' ? (
          <>
            <EmulatedDarkModeToggle
              enabled={isDarkModeEnabled}
              onChange={(enabled) => handleDarkModeChange(enabled)}
            />
            <ViewSizeControls
              setViewHeight={(height) => {
                setHeight(height);
                flushSync(() => {
                  handleSaveViewSize();
                });
              }}
              setViewWidth={(width) => {
                setWidth(width);
                flushSync(() => {
                  handleSaveViewSize();
                });
              }}
              viewHeight={height}
              viewWidth={width}
              minWidth={minWidth}
              minHeight={minHeight}
            />
          </>
        ) : null}
        <ActiveViewToggleGroup
          activeView={activeView}
          setActiveView={handleViewChange}
        />
        {hasRenderingMetadata ? (
          <div className="flex justify-end">
            <Send markup={renderedEmailMetadata.markup} />
          </div>
        ) : null}
      </Topbar>

      <div
        {...props}
        className={cn(
          'h-[calc(100%-3.5rem-2.375rem)] will-change-[height] flex p-4 transition-[height] duration-300 relative',
          activeView === 'preview' && 'bg-gray-200',
          activeView === 'preview' && isDarkModeEnabled && 'bg-gray-400',
          toolbarToggled && 'h-[calc(100%-3.5rem-13rem)]',
          className,
        )}
        ref={(element) => {
          const observer = new ResizeObserver((entry) => {
            const [elementEntry] = entry;
            if (elementEntry) {
              setMaxWidth(elementEntry.contentRect.width);
              setMaxHeight(elementEntry.contentRect.height);
            }
          });

          if (element) {
            observer.observe(element);
          }

          return () => {
            observer.disconnect();
          };
        }}
      >
        {hasErrors ? <ErrorOverlay error={renderingResult.error} /> : null}

        {hasRenderingMetadata ? (
          <>
            {activeView === 'preview' && (
              <ResizableWrapper
                minHeight={minHeight}
                minWidth={minWidth}
                maxHeight={maxHeight}
                maxWidth={maxWidth}
                height={height}
                onResizeEnd={() => {
                  handleSaveViewSize();
                }}
                onResize={(value, direction) => {
                  const isHorizontal =
                    direction === 'east' || direction === 'west';
                  if (isHorizontal) {
                    setWidth(Math.round(value));
                  } else {
                    setHeight(Math.round(value));
                  }
                }}
                width={width}
              >
                <EmailFrame
                  className="max-h-full rounded-lg bg-white [color-scheme:auto]"
                  darkMode={isDarkModeEnabled}
                  markup={renderedEmailMetadata.markup}
                  width={width}
                  height={height}
                  title={emailTitle}
                  ref={(iframe) => {
                    if (!iframe) return;

                    return makeIframeDocumentBubbleEvents(iframe);
                  }}
                />
              </ResizableWrapper>
            )}

            {activeView === 'source' && (
              <div className="h-full w-full">
                <div className="m-auto h-full flex max-w-3xl p-6">
                  <Tooltip.Provider>
                    <CodeContainer
                      activeLang={activeLang}
                      basename={renderedEmailMetadata.basename}
                      markups={[
                        {
                          language: 'tsx',
                          extension: renderedEmailMetadata.extname,
                          content: renderedEmailMetadata.reactMarkup,
                        },
                        {
                          language: 'html',
                          content: renderedEmailMetadata.prettyMarkup,
                        },
                        {
                          language: 'markdown',
                          extension: 'md',
                          content: renderedEmailMetadata.plainText,
                        },
                      ]}
                      setActiveLang={handleLangChange}
                    />
                  </Tooltip.Provider>
                </div>
              </div>
            )}
          </>
        ) : null}

        <Toaster />
      </div>
    </>
  );
};

export default Preview;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `Preview()`
- `activeLang()`
- `activeView()`
- `handleDarkModeChange()`
- `handleLangChange()`
- `handleSaveViewSize()`
- `handleViewChange()`
- `hasErrors()`
- `hasRenderingMetadata()`
- `isDarkModeEnabled()`
- `isHorizontal()`
- `isSameLang()`
- `minHeight()`
- `minWidth()`
- `observer()`
- `params()`
- `pathname()`
- `router()`
- `searchParams()`
- `storedHeight()`
- `storedWidth()`

### Interfaces

- `PreviewProps`

### Dependencies

This file imports/requires:

- `../../../components`
- `../../../components/code-container`
- `../../../components/resizable-wrapper`
- `../../../components/send`
- `../../../components/toolbar`
- `../../../components/tooltip`
- `../../../components/topbar/active-view-toggle-group`
- `../../../components/topbar/emulated-dark-mode-toggle`
- `../../../components/topbar/view-size-controls`
- `../../../contexts/preview`
- `../../../hooks/use-clamped-state`
- `../../../utils`
- `./email-frame`
- `./error-overlay`
- `next/navigation`
- `react`
- `react-dom`
- `sonner`
- `use-debounce`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 171

- `ActiveViewToggleGroup`
- `CodeContainer`
- `ComponentProps`
- `EmailFrame`
- `EmulatedDarkModeToggle`
- `ErrorOverlay`
- `Math`
- `Number`
- `POSITIVE_INFINITY`
- `Preview`
- `PreviewProps`
- `Provider`
- `React`
- `ResizableWrapper`
- `ResizeObserver`
- `Send`
- `Toaster`
- `Tooltip`
- `Topbar`
- `URLSearchParams`
- `ViewSizeControls`
- `active`
- `activeLang`
- `activeView`
- `auto`
- `basename`
- `boolean`
- `calc`
- `change`
- `clamped`
- `className`
- `client`
- `code`
- `color`
- `components`
- `container`
- `content`
- `contentRect`
- `contexts`
- `controls`
- `dark`
- `darkMode`
- `debounce`
- `delete`
- `direction`
- `disconnect`
- `div`
- `dom`
- `duration`
- `east`
- `element`
- `elementEntry`
- `email`
- `emailTitle`
- `emulated`
- `enabled`
- `end`
- `entry`
- `error`
- `extends`
- `extension`
- `extname`
- `flex`
- `flushSync`
- `frame`
- `full`
- `get`
- `gray`
- `group`
- `handleDarkModeChange`
- `handleLangChange`
- `handleSaveViewSize`
- `handleViewChange`
- `hasErrors`
- `hasRenderingMetadata`
- `hash`
- `height`
- `hooks`
- `html`
- `iframe`
- `interface`
- `isDarkModeEnabled`
- `isHorizontal`
- `isSameLang`
- `justify`
- `lang`
- `language`
- `location`
- `makeIframeDocumentBubbleEvents`
- `markdown`
- `markup`
- `markups`
- `max`
- `maxHeight`
- `maxWidth`
- `minHeight`
- `minWidth`
- `mode`
- `navigation`
- `next`
- `observe`
- `observer`
- `onChange`
- `onResize`
- `onResizeEnd`
- `overlay`
- `params`
- `parseInt`
- `pathname`
- `plainText`
- `prettyMarkup`
- `preview`
- `props`
- `push`
- `react`
- `reactMarkup`
- `ref`
- `relative`
- `renderedEmailMetadata`
- `renderingResult`
- `resizable`
- `round`
- `rounded`
- `router`
- `scheme`
- `searchParams`
- `send`
- `set`
- `setActiveLang`
- `setActiveView`
- `setHeight`
- `setMaxHeight`
- `setMaxWidth`
- `setViewHeight`
- `setViewWidth`
- `setWidth`
- `size`
- `sonner`
- `source`
- `state`
- `storedHeight`
- `storedWidth`
- `string`
- `title`
- `toString`
- `toggle`
- `toggled`
- `toolbar`
- `toolbarToggled`
- `tooltip`
- `topbar`
- `transition`
- `tsx`
- `use`
- `useClampedState`
- `useDebouncedCallback`
- `usePathname`
- `usePreviewContext`
- `useRouter`
- `useSearchParams`
- `useState`
- `useToolbarState`
- `utils`
- `value`
- `view`
- `viewHeight`
- `viewWidth`
- `west`
- `white`
- `width`
- `wrapper`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

