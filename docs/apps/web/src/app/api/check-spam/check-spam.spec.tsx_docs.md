# Documentation: check-spam.spec.tsx
**File Path:** `apps/web/src/app/api/check-spam/check-spam.spec.tsx`
**Language:** tsx
**Size:** 1,165 bytes
**Lines:** 33
**Generated:** 2025-11-15T20:37:32.827939Z

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

- **Path:** `apps/web/src/app/api/check-spam/check-spam.spec.tsx`
- **Name:** `check-spam.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 1,165 bytes (1.14 KB)
- **Lines of Code:** 33

---

## Original Source

```tsx
import { render } from '@react-email/components';
import { checkSpam } from './check-spam';
import { StripeWelcomeEmail } from './testing/stripe-welcome-email';

describe('checkSpam()', { timeout: 10_000 }, () => {
  test('with most spammy email', async () => {
    const template = (
      <html lang="en">
        <body>
          This email is spam. We sell rolexss for cheap. Get your viagra. We
          also sell weight loss pills today. Money back guaranteed. sEnd me $500
          and I'll send you back $700. don't tell anyone. Send this email to ten
          friends
        </body>
      </html>
    );
    const html = await render(template);
    // const plainText = await render(template, { plainText: true });
    const plainText = 'Completely different content from the original';

    expect(await checkSpam(html, plainText)).toMatchSnapshot();
  });

  test('with stripe email template using true base url', async () => {
    const html = await render(<StripeWelcomeEmail />);
    const plainText = await render(<StripeWelcomeEmail />, {
      plainText: true,
    });

    expect(await checkSpam(html, plainText)).toMatchSnapshot();
  });
});

```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `html()`
- `plainText()`
- `template()`

### Dependencies

This file imports/requires:

- `./check-spam`
- `./testing/stripe-welcome-email`
- `@react-email/components`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 53

- `Completely`
- `Get`
- `Money`
- `Send`
- `StripeWelcomeEmail`
- `also`
- `anyone`
- `back`
- `base`
- `body`
- `cheap`
- `check`
- `checkSpam`
- `components`
- `content`
- `describe`
- `different`
- `don`
- `email`
- `expect`
- `friends`
- `guaranteed`
- `html`
- `lang`
- `loss`
- `most`
- `original`
- `pills`
- `plainText`
- `react`
- `render`
- `rolexss`
- `sEnd`
- `sell`
- `send`
- `spam`
- `spammy`
- `stripe`
- `tell`
- `template`
- `ten`
- `test`
- `testing`
- `timeout`
- `toMatchSnapshot`
- `today`
- `url`
- `using`
- `viagra`
- `weight`
- `welcome`
- `you`
- `your`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

