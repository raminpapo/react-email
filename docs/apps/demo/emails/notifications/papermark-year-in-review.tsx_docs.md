# Documentation: papermark-year-in-review.tsx
**File Path:** `apps/demo/emails/notifications/papermark-year-in-review.tsx`
**Language:** tsx
**Size:** 9,125 bytes
**Lines:** 232
**Generated:** 2025-11-15T20:37:33.167278Z

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

- **Path:** `apps/demo/emails/notifications/papermark-year-in-review.tsx`
- **Name:** `papermark-year-in-review.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 9,125 bytes (8.91 KB)
- **Lines of Code:** 232

---

## Original Source

```tsx
import {
  Body,
  Column,
  Container,
  Head,
  Heading,
  Hr,
  Html,
  Link,
  Preview,
  Row,
  Section,
  Tailwind,
  Text,
} from '@react-email/components';

interface PapermarkYearInReviewEmailProps {
  year?: number;
  minutesSpentOnDocs?: number;
  uploadedDocuments?: number;
  sharedLinks?: number;
  receivedViews?: number;
  topDocumentName?: string;
  topDocumentViews?: number;
  mostActiveMonth?: string;
  mostActiveMonthViews?: number;
  sharerPercentile?: number;
  viewingLocations?: string[];
}

export default function PapermarkYearInReviewEmail({
  year,
  minutesSpentOnDocs,
  uploadedDocuments,
  sharedLinks,
  receivedViews,
  topDocumentName,
  topDocumentViews,
  mostActiveMonth,
  mostActiveMonthViews,
  sharerPercentile,
  viewingLocations = [],
}: PapermarkYearInReviewEmailProps) {
  return (
    <Html>
      <Head />
      <Preview>See your stats from 2024</Preview>
      <Tailwind>
        <Body className="bg-white font-sans">
          <Container className="mx-auto w-full max-w-[600px] p-0">
            <Section className="p-8 text-center">
              <Text className="mx-0 mt-4 mb-8 p-0 text-center font-normal text-2xl">
                <span className="font-bold tracking-tighter">Papermark</span>
              </Text>
              <Text className="font-normal text-sm uppercase tracking-wider">
                {year} in review
              </Text>
              <Heading className="my-4 font-medium text-4xl leading-tight">
                Your Year with Papermark
              </Heading>
              <Text className="mb-8 text-lg leading-8">
                What a year it&apos;s been! Let&apos;s take a look at how
                you&apos;ve used Papermark to share your important documents.
              </Text>
              <Link
                href="https://www.papermark.com"
                className="inline-flex items-center rounded-full bg-gray-900 px-12 py-4 text-center font-bold text-sm text-white no-underline"
              >
                Share your stats
              </Link>
            </Section>

            <Section className="my-6 rounded-2xl bg-[#fb7a00]/10 bg-[radial-gradient(circle_at_bottom_right,#fb7a00_0%,transparent_60%)] p-8 text-center">
              <Heading className="m-0 font-medium text-3xl text-[#a63b00]">
                Viewers spent
              </Heading>
              <Text className="my-4 font-bold text-7xl text-gray-900 leading-none">
                {minutesSpentOnDocs}
              </Text>
              <Text className="mb-4 font-medium text-3xl text-gray-900">
                minutes on your documents
              </Text>
              <Text className="text-gray-900 text-sm leading-5">
                That&apos;s a lot of engagement! Your documents are resonating
                with your visitors.
              </Text>

              <Hr className="mt-6" style={{ borderColor: '#fb7a00' }} />
              <Heading className="pt-5 font-medium text-gray-900 text-xs uppercase tracking-wider">
                Your activity
              </Heading>
              <Row className="mt-5">
                <Column className="w-1/3 text-center">
                  <Text className="font-medium text-[#a63b00] text-sm">
                    You uploaded
                  </Text>
                  <Text className="my-1 font-bold text-4xl text-gray-900">
                    {uploadedDocuments}
                  </Text>
                  <Text className="text-2xl text-gray-900">documents</Text>
                </Column>
                <Column className="w-1/3 text-center">
                  <Text className="font-medium text-[#a63b00] text-sm">
                    You shared
                  </Text>
                  <Text className="my-1 font-bold text-4xl text-gray-900">
                    {sharedLinks}
                  </Text>
                  <Text className="text-2xl text-gray-900">links</Text>
                </Column>
                <Column className="w-1/3 text-center">
                  <Text className="font-medium text-[#a63b00] text-sm">
                    You received
                  </Text>
                  <Text className="my-1 font-bold text-4xl text-gray-900">
                    {receivedViews}
                  </Text>
                  <Text className="text-2xl text-gray-900">views</Text>
                </Column>
              </Row>
            </Section>

            <Section className="my-6 rounded-2xl bg-[#4b5563]/10 bg-[radial-gradient(circle_at_bottom_right,#4b5563_0%,transparent_60%)] p-8 text-center">
              <Heading className="m-0 font-medium text-3xl text-gray-800">
                Your top document
              </Heading>
              <Text className="my-4 font-bold text-2xl text-gray-900 leading-none">
                &quot;{topDocumentName}&quot;
              </Text>
              <Text className="mb-4 font-medium text-5xl text-gray-900">
                {topDocumentViews} views
              </Text>
              <Text className="text-gray-900 text-sm leading-5">
                This document really caught your visitor&apos;s attention!
              </Text>
            </Section>

            <Section className="my-6 rounded-2xl bg-[#e4c5a0]/10 bg-[radial-gradient(circle_at_bottom_right,#e4c5a0_0%,transparent_60%)] p-8 text-center">
              <Heading className="m-0 font-medium text-3xl text-[#9c7b4a]">
                Your most active month
              </Heading>
              <Text className="my-4 font-bold text-5xl text-gray-900 leading-none">
                {mostActiveMonth}
              </Text>
              <Text className="mb-4 font-medium text-3xl text-gray-900">
                with {mostActiveMonthViews} views
              </Text>
              <Text className="text-gray-900 text-sm leading-5">
                {mostActiveMonth} was your busiest month. What did you share
                that got so much attention?
              </Text>

              <Hr className="mt-6" style={{ borderColor: '#e4c5a0' }} />
              <Heading className="pt-5 font-medium text-gray-900 text-xs uppercase tracking-wider">
                You&apos;re in the top
              </Heading>
              <Text className="my-4 font-bold text-7xl text-gray-900 leading-none">
                {sharerPercentile}%
              </Text>
              <Text className="mb-4 font-medium text-gray-900 text-xl">
                of sharers on Papermark
              </Text>
              <Text className="text-gray-900 text-sm leading-5">
                You&apos;re one of our most active users. Thank you for sharing
                with Papermark!
              </Text>
            </Section>

            <Section className="my-6 rounded-2xl bg-[#10b981]/10 bg-[radial-gradient(circle_at_bottom_right,#10b981_0%,transparent_60%)] p-8 text-center">
              <Heading className="m-0 font-medium text-3xl text-[#065f46]">
                Your documents were viewed from
              </Heading>
              <Row className="mt-4">
                <Column>
                  {viewingLocations.map((location, index) => (
                    <Text
                      key={index}
                      className="rounded-full bg-[#10b981] px-3 py-1 font-medium text-sm text-white"
                      style={{
                        margin: '4px 4px',
                        display: 'inline-block',
                      }}
                    >
                      {location}
                    </Text>
                  ))}
                </Column>
              </Row>
              <Text className="mt-4 text-[#065f46] text-sm leading-5">
                Your documents get attention from all over the world!
              </Text>
            </Section>

            <Section className="pb-6 text-center">
              <Text className="text-gray-900 text-xl leading-8">
                We&apos;re excited to support you next year! <br />
                Happy Holidays from the Papermark team :)
              </Text>
              <Link
                href="https://www.papermark.com"
                className="mt-4 inline-flex items-center rounded-full bg-gray-900 px-12 py-4 text-center font-bold text-sm text-white no-underline"
              >
                Share your stats
              </Link>
              <Link
                href="https://www.papermark.com"
                className="mt-4 block items-center text-center font-bold text-gray-900 text-sm no-underline"
              >
                Go to your dashboard
              </Link>
            </Section>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
}

PapermarkYearInReviewEmail.PreviewProps = {
  year: 2024,
  minutesSpentOnDocs: 1234,
  uploadedDocuments: 25,
  sharedLinks: 50,
  receivedViews: 500,
  topDocumentName: 'Q4 Financial Report',
  topDocumentViews: 150,
  mostActiveMonth: 'September',
  mostActiveMonthViews: 200,
  sharerPercentile: 95,
  viewingLocations: ['United States', 'United Kingdom', 'Germany', 'Japan'],
} satisfies PapermarkYearInReviewEmailProps;

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It exports a default export. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `PapermarkYearInReviewEmail()`

### Interfaces

- `PapermarkYearInReviewEmailProps`

### Dependencies

This file imports/requires:

- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 152

- `Body`
- `Column`
- `Container`
- `Financial`
- `Germany`
- `Happy`
- `Head`
- `Heading`
- `Holidays`
- `Html`
- `Japan`
- `Kingdom`
- `Link`
- `Papermark`
- `PapermarkYearInReviewEmail`
- `PapermarkYearInReviewEmailProps`
- `Preview`
- `PreviewProps`
- `Report`
- `Row`
- `Section`
- `See`
- `September`
- `Share`
- `States`
- `Tailwind`
- `Text`
- `Thank`
- `United`
- `Viewers`
- `What`
- `Year`
- `You`
- `Your`
- `a63b00`
- `active`
- `activity`
- `all`
- `apos`
- `attention`
- `auto`
- `block`
- `bold`
- `borderColor`
- `busiest`
- `caught`
- `center`
- `circle_at_bottom_right`
- `className`
- `com`
- `components`
- `dashboard`
- `display`
- `document`
- `documents`
- `e4c5a0`
- `e4c5a0_0`
- `email`
- `engagement`
- `excited`
- `fb7a00`
- `fb7a00_0`
- `flex`
- `font`
- `full`
- `get`
- `got`
- `gradient`
- `gray`
- `how`
- `href`
- `https`
- `important`
- `index`
- `inline`
- `interface`
- `items`
- `key`
- `leading`
- `links`
- `location`
- `look`
- `lot`
- `map`
- `margin`
- `max`
- `medium`
- `minutes`
- `minutesSpentOnDocs`
- `month`
- `most`
- `mostActiveMonth`
- `mostActiveMonthViews`
- `much`
- `next`
- `normal`
- `number`
- `one`
- `our`
- `over`
- `papermark`
- `quot`
- `radial`
- `react`
- `really`
- `received`
- `receivedViews`
- `resonating`
- `review`
- `rounded`
- `sans`
- `satisfies`
- `share`
- `shared`
- `sharedLinks`
- `sharerPercentile`
- `sharers`
- `sharing`
- `span`
- `spent`
- `stats`
- `string`
- `style`
- `support`
- `take`
- `team`
- `text`
- `tight`
- `tighter`
- `top`
- `topDocumentName`
- `topDocumentViews`
- `tracking`
- `transparent_60`
- `underline`
- `uploaded`
- `uploadedDocuments`
- `uppercase`
- `used`
- `users`
- `viewed`
- `viewingLocations`
- `views`
- `visitor`
- `visitors`
- `white`
- `wider`
- `world`
- `www`
- `year`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

