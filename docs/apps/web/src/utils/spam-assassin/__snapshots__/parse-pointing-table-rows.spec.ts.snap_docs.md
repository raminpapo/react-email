# Documentation: parse-pointing-table-rows.spec.ts.snap
**File Path:** `apps/web/src/utils/spam-assassin/__snapshots__/parse-pointing-table-rows.spec.ts.snap`
**Language:** Unknown
**Size:** 4,521 bytes
**Lines:** 192
**Generated:** 2025-11-15T20:37:32.817588Z

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

- **Path:** `apps/web/src/utils/spam-assassin/__snapshots__/parse-pointing-table-rows.spec.ts.snap`
- **Name:** `parse-pointing-table-rows.spec.ts.snap`
- **Extension:** `.snap`
- **Language:** Unknown
- **Size:** 4,521 bytes (4.42 KB)
- **Lines of Code:** 192

---

## Original Source

```
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`parsePointingTableRows() > works with a multiline description 1`] = `
[
  {
    "description": "Informational: message has no Received headers",
    "pts": -0,
    "ruleName": "NO_RECEIVED",
  },
  {
    "description": "Missing Message-Id: header",
    "pts": 0.1,
    "ruleName": "MISSING_MID",
  },
  {
    "description": "Missing Date: header",
    "pts": 1.4,
    "ruleName": "MISSING_DATE",
  },
  {
    "description": "Missing From: header",
    "pts": 1,
    "ruleName": "MISSING_FROM",
  },
  {
    "description": "Missing Subject: header",
    "pts": 1.8,
    "ruleName": "MISSING_SUBJECT",
  },
  {
    "description": "Missing To: header",
    "pts": 1.2,
    "ruleName": "MISSING_HEADERS",
  },
  {
    "description": "Informational: message was not relayed via SMTP",
    "pts": -0,
    "ruleName": "NO_RELAYS",
  },
  {
    "description": "ADMINISTRATOR NOTICE: The query to URIBL was blocked. See http://wiki.apache.org/spamassassin/DnsBlocklists#dnsbl-block for more information. [URI: stripe.com]",
    "pts": 0,
    "ruleName": "URIBL_BLOCKED",
  },
  {
    "description": "BODY: HTML included in message",
    "pts": 0,
    "ruleName": "HTML_MESSAGE",
  },
  {
    "description": "Message appears to be missing most RFC-822 headers",
    "pts": 0,
    "ruleName": "NO_HEADERS_MESSAGE",
  },
  {
    "description": "High bit body and no message ID header",
    "pts": 3.9,
    "ruleName": "DOS_BODY_HIGH_NO_MID",
  },
]
`;

exports[`parsePointingTableRows() > works with names that exceed the column length 1`] = `
[
  {
    "description": "Missing Date: header",
    "pts": 1.4,
    "ruleName": "MISSING_DATE",
  },
  {
    "description": "Missing From: header",
    "pts": 1,
    "ruleName": "MISSING_FROM",
  },
  {
    "description": "Missing Message-Id: header",
    "pts": 0.1,
    "ruleName": "MISSING_MID",
  },
  {
    "description": "Informational: message has no Received headers",
    "pts": -0,
    "ruleName": "NO_RECEIVED",
  },
  {
    "description": "Missing Subject: header",
    "pts": 1.8,
    "ruleName": "MISSING_SUBJECT",
  },
  {
    "description": "ADMINISTRATOR NOTICE: The query to dbl.spamhaus.org was blocked due to usage of an open resolver. See https://www.spamhaus.org/returnc/pub/ [URI: app.papermark.io]",
    "pts": 0,
    "ruleName": "URIBL_DBL_BLOCKED_OPENDNS",
  },
  {
    "description": "Missing To: header",
    "pts": 1.2,
    "ruleName": "MISSING_HEADERS",
  },
  {
    "description": "Informational: message was not relayed via SMTP",
    "pts": -0,
    "ruleName": "NO_RELAYS",
  },
  {
    "description": "BODY: HTML included in message",
    "pts": 0,
    "ruleName": "HTML_MESSAGE",
  },
  {
    "description": "Message appears to be missing most RFC-822 headers",
    "pts": 0,
    "ruleName": "NO_HEADERS_MESSAGE",
  },
  {
    "description": "High bit body and no message ID header",
    "pts": 3.7,
    "ruleName": "DOS_BODY_HIGH_NO_MID",
  },
  {
    "description": "Invisible text + long lines",
    "pts": 2.1,
    "ruleName": "FONT_INVIS_LONG_LINE",
  },
  {
    "description": "HTML hidden text - word obfuscation?",
    "pts": 0.8,
    "ruleName": "HTML_TEXT_INVISIBLE_FONT",
  },
]
`;

exports[`parsePointingTableRows() > works with spammy emails 1`] = `
[
  {
    "description": "Missing Subject: header",
    "pts": 1.8,
    "ruleName": "MISSING_SUBJECT",
  },
  {
    "description": "Missing Date: header",
    "pts": 1.4,
    "ruleName": "MISSING_DATE",
  },
  {
    "description": "Missing Message-Id: header",
    "pts": 0.1,
    "ruleName": "MISSING_MID",
  },
  {
    "description": "Missing From: header",
    "pts": 1,
    "ruleName": "MISSING_FROM",
  },
  {
    "description": "Informational: message has no Received headers",
    "pts": -0,
    "ruleName": "NO_RECEIVED",
  },
  {
    "description": "Missing To: header",
    "pts": 1.2,
    "ruleName": "MISSING_HEADERS",
  },
  {
    "description": "Informational: message was not relayed via SMTP",
    "pts": -0,
    "ruleName": "NO_RELAYS",
  },
  {
    "description": "BODY: Money back guarantee",
    "pts": 2.5,
    "ruleName": "MONEY_BACK",
  },
  {
    "description": "BODY: HTML included in message",
    "pts": 0,
    "ruleName": "HTML_MESSAGE",
  },
  {
    "description": "Message appears to be missing most RFC-822 headers",
    "pts": 0,
    "ruleName": "NO_HEADERS_MESSAGE",
  },
  {
    "description": "Refers to an erectile drug",
    "pts": 2.2,
    "ruleName": "DRUGS_ERECTILE",
  },
]
`;

```

---

## Overview



---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 94

- `DOS_BODY_HIGH_NO_MID`
- `DRUGS_ERECTILE`
- `Date`
- `DnsBlocklists`
- `FONT_INVIS_LONG_LINE`
- `HTML_MESSAGE`
- `HTML_TEXT_INVISIBLE_FONT`
- `High`
- `Informational`
- `Invisible`
- `MISSING_DATE`
- `MISSING_FROM`
- `MISSING_HEADERS`
- `MISSING_MID`
- `MISSING_SUBJECT`
- `MONEY_BACK`
- `Message`
- `Missing`
- `Money`
- `NO_HEADERS_MESSAGE`
- `NO_RECEIVED`
- `NO_RELAYS`
- `Received`
- `Refers`
- `See`
- `Snapshot`
- `Subject`
- `URIBL_BLOCKED`
- `URIBL_DBL_BLOCKED_OPENDNS`
- `Vitest`
- `apache`
- `app`
- `appears`
- `back`
- `bit`
- `block`
- `blocked`
- `body`
- `column`
- `com`
- `dbl`
- `description`
- `dev`
- `dnsbl`
- `drug`
- `due`
- `emails`
- `erectile`
- `exceed`
- `exports`
- `guarantee`
- `guide`
- `header`
- `headers`
- `hidden`
- `html`
- `http`
- `https`
- `included`
- `information`
- `length`
- `lines`
- `long`
- `message`
- `missing`
- `more`
- `most`
- `multiline`
- `names`
- `obfuscation`
- `open`
- `org`
- `papermark`
- `parsePointingTableRows`
- `pts`
- `pub`
- `query`
- `relayed`
- `resolver`
- `returnc`
- `ruleName`
- `snapshot`
- `spamassassin`
- `spamhaus`
- `spammy`
- `stripe`
- `text`
- `usage`
- `via`
- `vitest`
- `wiki`
- `word`
- `works`
- `www`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

