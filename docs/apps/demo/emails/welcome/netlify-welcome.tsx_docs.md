# Documentation: netlify-welcome.tsx
**File Path:** `apps/demo/emails/welcome/netlify-welcome.tsx`
**Language:** tsx
**Size:** 4,951 bytes
**Lines:** 186
**Generated:** 2025-11-15T20:37:33.209459Z

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

- **Path:** `apps/demo/emails/welcome/netlify-welcome.tsx`
- **Name:** `netlify-welcome.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 4,951 bytes (4.83 KB)
- **Lines of Code:** 186

---

## Original Source

```tsx
import {
  Body,
  Button,
  Column,
  Container,
  Head,
  Heading,
  Html,
  Img,
  Link,
  Preview,
  pixelBasedPreset,
  Row,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';
import type * as React from 'react';

interface NetlifyWelcomeEmailProps {
  steps: {
    id: number;
    Description: React.ReactNode;
  }[];
  links: {
    title: string;
    href: string;
  }[];
}

const baseUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : '';

export const NetlifyWelcomeEmail = ({
  steps,
  links,
}: NetlifyWelcomeEmailProps) => {
  return (
    <Html>
      <Head />
      <Tailwind
        config={{
          presets: [pixelBasedPreset],
          theme: {
            extend: {
              colors: {
                brand: '#2250f4',
                offwhite: '#fafbfb',
              },
              spacing: {
                0: '0px',
                20: '20px',
                45: '45px',
              },
            },
          },
        }}
      >
        <Preview>Netlify Welcome</Preview>
        <Body className="bg-offwhite font-sans text-base">
          <Img
            src={`${baseUrl}/static/netlify-logo.png`}
            width="184"
            height="75"
            alt="Netlify"
            className="mx-auto my-20"
          />
          <Container className="bg-white p-45">
            <Heading className="my-0 text-center leading-8">
              Welcome to Netlify
            </Heading>

            <Section>
              <Row>
                <Text className="text-base">
                  Congratulations! You're joining over 3 million developers
                  around the world who use Netlify to build and ship sites,
                  stores, and apps.
                </Text>

                <Text className="text-base">Here's how to get started:</Text>
              </Row>
            </Section>

            <ul>{steps?.map(({ Description }) => Description)}</ul>

            <Section className="text-center">
              <Button className="rounded-lg bg-brand px-[18px] py-3 text-white">
                Go to your dashboard
              </Button>
            </Section>

            <Section className="mt-45">
              <Row>
                {links?.map((link) => (
                  <Column key={link.title}>
                    <Link
                      className="font-bold text-black underline"
                      href={link.href}
                    >
                      {link.title}
                    </Link>{' '}
                    <span className="text-green-500">→</span>
                  </Column>
                ))}
              </Row>
            </Section>
          </Container>

          <Container className="mt-20">
            <Section>
              <Row>
                <Column className="px-20 text-right">
                  <Link>Unsubscribe</Link>
                </Column>
                <Column className="text-left">
                  <Link>Manage Preferences</Link>
                </Column>
              </Row>
            </Section>
            <Text className="mb-45 text-center text-gray-400">
              Netlify, 44 Montgomery Street, Suite 300 San Francisco, CA
            </Text>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
};

NetlifyWelcomeEmail.PreviewProps = {
  steps: [
    {
      id: 1,
      Description: (
        <li className="mb-20" key={1}>
          <strong>Deploy your first project.</strong>{' '}
          <Link>Connect to Git, choose a template</Link>, or manually deploy a
          project you've been working on locally.
        </li>
      ),
    },
    {
      id: 2,
      Description: (
        <li className="mb-20" key={2}>
          <strong>Check your deploy logs.</strong> Find out what's included in
          your build and watch for errors or failed deploys.{' '}
          <Link>Learn how to read your deploy logs</Link>.
        </li>
      ),
    },
    {
      id: 3,
      Description: (
        <li className="mb-20" key={3}>
          <strong>Choose an integration.</strong> Quickly discover, connect, and
          configure the right tools for your project with 150+ integrations to
          choose from. <Link>Explore the Integrations Hub</Link>.
        </li>
      ),
    },
    {
      id: 4,
      Description: (
        <li className="mb-20" key={4}>
          <strong>Set up a custom domain.</strong> You can register a new domain
          and buy it through Netlify or assign a domain you already own to your
          site. <Link>Add a custom domain</Link>.
        </li>
      ),
    },
  ],
  links: [
    {
      title: 'Visit the forums',
      href: 'https://www.netlify.com',
    },
    { title: 'Read the docs', href: 'https://www.netlify.com' },
    { title: 'Contact an expert', href: 'https://www.netlify.com' },
  ],
} satisfies NetlifyWelcomeEmailProps;

export default NetlifyWelcomeEmail;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `NetlifyWelcomeEmail()`
- `baseUrl()`

### Interfaces

- `NetlifyWelcomeEmailProps`

### Dependencies

This file imports/requires:

- `@react-email/components`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 162

- `Add`
- `Body`
- `Button`
- `Check`
- `Choose`
- `Column`
- `Congratulations`
- `Connect`
- `Contact`
- `Container`
- `Deploy`
- `Description`
- `Explore`
- `Find`
- `Francisco`
- `Git`
- `Head`
- `Heading`
- `Here`
- `Html`
- `Hub`
- `Img`
- `Integrations`
- `Learn`
- `Link`
- `Manage`
- `Montgomery`
- `Netlify`
- `NetlifyWelcomeEmail`
- `NetlifyWelcomeEmailProps`
- `Preferences`
- `Preview`
- `PreviewProps`
- `Quickly`
- `React`
- `ReactNode`
- `Read`
- `Row`
- `San`
- `Section`
- `Set`
- `Street`
- `Suite`
- `Tailwind`
- `Text`
- `Unsubscribe`
- `VERCEL_URL`
- `Visit`
- `Welcome`
- `You`
- `already`
- `alt`
- `apps`
- `around`
- `assign`
- `auto`
- `base`
- `baseUrl`
- `black`
- `bold`
- `brand`
- `build`
- `buy`
- `center`
- `choose`
- `className`
- `colors`
- `com`
- `components`
- `config`
- `configure`
- `connect`
- `custom`
- `dashboard`
- `deploy`
- `deploys`
- `developers`
- `discover`
- `docs`
- `domain`
- `email`
- `env`
- `errors`
- `expert`
- `extend`
- `fafbfb`
- `failed`
- `first`
- `font`
- `forums`
- `get`
- `gray`
- `green`
- `height`
- `how`
- `href`
- `https`
- `included`
- `integration`
- `integrations`
- `interface`
- `joining`
- `key`
- `leading`
- `left`
- `link`
- `links`
- `locally`
- `logo`
- `logs`
- `manually`
- `map`
- `million`
- `netlify`
- `number`
- `offwhite`
- `out`
- `over`
- `own`
- `pixelBasedPreset`
- `png`
- `presets`
- `process`
- `project`
- `react`
- `read`
- `register`
- `right`
- `rounded`
- `sans`
- `satisfies`
- `ship`
- `site`
- `sites`
- `spacing`
- `span`
- `src`
- `started`
- `static`
- `steps`
- `stores`
- `string`
- `strong`
- `template`
- `text`
- `theme`
- `through`
- `title`
- `tools`
- `type`
- `underline`
- `use`
- `watch`
- `what`
- `white`
- `who`
- `width`
- `working`
- `world`
- `www`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

