# Documentation: send.tsx
**File Path:** `packages/preview-server/src/components/send.tsx`
**Language:** tsx
**Size:** 4,907 bytes
**Lines:** 142
**Generated:** 2025-11-15T20:37:32.127795Z

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

- **Path:** `packages/preview-server/src/components/send.tsx`
- **Name:** `send.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,907 bytes (4.79 KB)
- **Lines of Code:** 142

---

## Original Source

```tsx
import * as Popover from '@radix-ui/react-popover';
import * as React from 'react';
import { toast } from 'sonner';
import { Button } from './button';
import { Text } from './text';

export const Send = ({ markup }: { markup: string }) => {
  const [to, setTo] = React.useState('');
  const [subject, setSubject] = React.useState('Testing React Email');
  const [isSending, setIsSending] = React.useState(false);
  const [isPopOverOpen, setIsPopOverOpen] = React.useState(false);

  const onFormSubmit = async (e: React.FormEvent) => {
    try {
      e.preventDefault();
      setIsSending(true);

      const response = await fetch('https://react.email/api/send/test', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          to,
          subject,
          html: markup,
        }),
      });

      if (response.ok) {
        toast.success('Email sent! Check your inbox.');
      } else {
        if (response.status === 429) {
          const { error } = (await response.json()) as { error: string };
          toast.error(error);
        } else {
          toast.error('Something went wrong. Please try again.');
        }
      }
    } catch (_exception) {
      toast.error('Something went wrong. Please try again.');
    } finally {
      setIsSending(false);
    }
  };

  const toId = React.useId();
  const subjectId = React.useId();

  return (
    <Popover.Root
      onOpenChange={() => {
        if (!isPopOverOpen) {
          document.body.classList.add('popup-open');
          setIsPopOverOpen(true);
        } else {
          document.body.classList.remove('popup-open');
          setIsPopOverOpen(false);
        }
      }}
      open={isPopOverOpen}
    >
      <Popover.Trigger asChild>
        <button
          className="box-border flex h-5 w-20 items-center justify-center self-center rounded-lg border border-slate-6 bg-slate-2 px-4 py-4 text-center font-sans text-sm text-slate-11 outline-none transition duration-300 ease-in-out hover:border-slate-10 hover:text-slate-12"
          type="submit"
        >
          Send
        </button>
      </Popover.Trigger>
      <Popover.Anchor />
      <Popover.Portal>
        <Popover.Content
          align="end"
          className="-mt-10 w-80 rounded-lg border border-slate-6 bg-black/70 p-3 text-slate-11 shadow-md backdrop-blur-lg font-sans"
          sideOffset={48}
        >
          <form className="mt-1" onSubmit={(e) => void onFormSubmit(e)}>
            <label
              className="mb-2 block text-xs uppercase text-slate-10"
              htmlFor={toId}
            >
              Recipient
            </label>
            <input
              autoFocus
              className="mb-3 w-full appearance-none rounded-lg border border-slate-6 bg-slate-3 px-2 py-1 text-sm text-slate-12 placeholder-slate-10 outline-none transition duration-300 ease-in-out focus:ring-1 focus:ring-slate-10"
              defaultValue={to}
              id={toId}
              onChange={(e) => {
                setTo(e.target.value);
              }}
              placeholder="you@example.com"
              required
              type="email"
            />
            <label
              className="mb-2 mt-1 block text-xs uppercase text-slate-10"
              htmlFor={subjectId}
            >
              Subject
            </label>
            <input
              className="mb-3 w-full appearance-none rounded-lg border border-slate-6 bg-slate-3 px-2 py-1 text-sm text-slate-12 placeholder-slate-10 outline-none transition duration-300 ease-in-out focus:ring-1 focus:ring-slate-10"
              defaultValue={subject}
              id={subjectId}
              onChange={(e) => {
                setSubject(e.target.value);
              }}
              placeholder="My Email"
              required
              type="text"
            />
            <input
              className="appearance-none checked:bg-blue-500"
              type="checkbox"
            />
            <div className="mt-3 flex items-center justify-between">
              <Text className="inline-block" size="1">
                Powered by{' '}
                <a
                  className="text-white/85 transition duration-300 ease-in-out hover:text-slate-12"
                  href="https://go.resend.com/react-email"
                  rel="noreferrer"
                  target="_blank"
                >
                  Resend
                </a>
              </Text>
              <Button
                className="disabled:border-transparent disabled:bg-slate-11"
                disabled={subject.length === 0 || to.length === 0 || isSending}
                type="submit"
              >
                Send
              </Button>
            </div>
          </form>
        </Popover.Content>
      </Popover.Portal>
    </Popover.Root>
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

- `Send()`
- `onFormSubmit()`
- `response()`
- `subjectId()`
- `toId()`

### Dependencies

This file imports/requires:

- `./button`
- `./text`
- `@radix-ui/react-popover`
- `react`
- `sonner`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 139

- `Anchor`
- `Button`
- `Check`
- `Content`
- `Email`
- `FormEvent`
- `Please`
- `Popover`
- `Portal`
- `Powered`
- `React`
- `Recipient`
- `Resend`
- `Root`
- `Send`
- `Something`
- `Subject`
- `Testing`
- `Text`
- `Trigger`
- `Type`
- `_blank`
- `_exception`
- `add`
- `again`
- `align`
- `api`
- `appearance`
- `application`
- `asChild`
- `autoFocus`
- `backdrop`
- `between`
- `black`
- `block`
- `blue`
- `blur`
- `body`
- `border`
- `box`
- `button`
- `center`
- `checkbox`
- `checked`
- `classList`
- `className`
- `com`
- `defaultValue`
- `disabled`
- `div`
- `document`
- `duration`
- `ease`
- `email`
- `end`
- `error`
- `example`
- `fetch`
- `flex`
- `focus`
- `font`
- `form`
- `full`
- `headers`
- `hover`
- `href`
- `html`
- `htmlFor`
- `https`
- `inbox`
- `inline`
- `input`
- `isPopOverOpen`
- `isSending`
- `items`
- `json`
- `justify`
- `label`
- `length`
- `markup`
- `method`
- `noreferrer`
- `onChange`
- `onFormSubmit`
- `onOpenChange`
- `onSubmit`
- `open`
- `out`
- `outline`
- `placeholder`
- `popover`
- `popup`
- `preventDefault`
- `radix`
- `react`
- `rel`
- `remove`
- `required`
- `resend`
- `response`
- `ring`
- `rounded`
- `sans`
- `send`
- `sent`
- `setIsPopOverOpen`
- `setIsSending`
- `setSubject`
- `setTo`
- `shadow`
- `sideOffset`
- `size`
- `slate`
- `sonner`
- `status`
- `string`
- `stringify`
- `subject`
- `subjectId`
- `submit`
- `success`
- `target`
- `test`
- `text`
- `toId`
- `toast`
- `transition`
- `transparent`
- `type`
- `uppercase`
- `useId`
- `useState`
- `value`
- `void`
- `went`
- `white`
- `wrong`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

