# Documentation: caniemail-data.ts
**File Path:** `packages/preview-server/src/actions/email-validation/caniemail-data.ts`
**Language:** typescript
**Size:** 1,549,497 bytes
**Lines:** 86,441
**Generated:** 2025-11-15T20:37:31.876576Z

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

- **Path:** `packages/preview-server/src/actions/email-validation/caniemail-data.ts`
- **Name:** `caniemail-data.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 1,549,497 bytes (1513.18 KB)
- **Lines of Code:** 86,441

---

## Original Source

*Note: File is large (1513.18 KB). Showing first 10,000 lines.*

```typescript
import type { SupportEntry } from "./check-compatibility";

export const nicenames = {
  "family": {
    "gmail": "Gmail",
    "outlook": "Outlook",
    "yahoo": "Yahoo! Mail",
    "apple-mail": "Apple Mail",
    "aol": "AOL",
    "thunderbird": "Mozilla Thunderbird",
    "microsoft": "Microsoft",
    "samsung-email": "Samsung Email",
    "sfr": "SFR",
    "orange": "Orange",
    "protonmail": "ProtonMail",
    "hey": "HEY",
    "mail-ru": "Mail.ru",
    "fastmail": "Fastmail",
    "laposte": "LaPoste.net",
    "t-online-de": "T-online.de",
    "free-fr": "Free.fr",
    "gmx": "GMX",
    "web-de": "WEB.DE",
    "ionos-1and1": "1&1",
    "rainloop": "RainLoop",
    "wp-pl": "WP.pl"
  },
  "platform": {
    "desktop-app": "Desktop",
    "desktop-webmail": "Desktop Webmail",
    "mobile-webmail": "Mobile Webmail",
    "webmail": "Webmail",
    "ios": "iOS",
    "android": "Android",
    "windows": "Windows",
    "macos": "macOS",
    "windows-mail": "Windows Mail",
    "outlook-com": "Outlook.com"
  },
  "support": {
    "supported": "Supported",
    "mitigated": "Partially supported",
    "unsupported": "Not supported",
    "unknown": "Support unknown",
    "mixed": "Mixed support"
  },
  "category": {
    "html": "HTML",
    "css": "CSS",
    "image": "Image formats",
    "others": "Others"
  }
};

export const supportEntries: SupportEntry[] = [
  {
    "slug": "amp",
    "title": "AMP for Email",
    "description": "Support for rendering emails in the AMP format.",
    "url": "https://www.caniemail.com/features/amp/",
    "category": "others",
    "tags": [],
    "keywords": "amp4email",
    "last_test_date": "2020-03-31",
    "test_url": "https://www.caniemail.com/tests/amp.html",
    "test_results_url": null,
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "n"
          }
        ],
        "ios": [
          {
            "13.1": "n"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2020-04": "y"
          },
          {
            "2022-02": "y #1"
          }
        ],
        "ios": [
          {
            "2020-04": "y"
          }
        ],
        "android": [
          {
            "2020-04": "y"
          }
        ],
        "mobile-webmail": [
          {
            "2020-04": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2020-01": "n"
          },
          {
            "2021-03": "n"
          }
        ],
        "ios": [
          {
            "2020-01": "n"
          }
        ],
        "android": [
          {
            "2020-01": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2019-10": "n"
          }
        ],
        "macos": [
          {
            "2019-10": "n"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2020-01": "n"
          }
        ],
        "ios": [
          {
            "2019-10": "n"
          }
        ],
        "android": [
          {
            "2019-10": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-10": "y"
          },
          {
            "2021-01": "y"
          },
          {
            "2022-02": "y #1"
          }
        ],
        "ios": [
          {
            "2019-10": "n"
          },
          {
            "2022-12": "y"
          }
        ],
        "android": [
          {
            "2019-10": "n"
          },
          {
            "2022-12": "y"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-10": "n"
          }
        ],
        "ios": [
          {
            "2019-10": "n"
          }
        ],
        "android": [
          {
            "2019-10": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "n"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2020-01": "n"
          }
        ],
        "ios": [
          {
            "2020-01": "n"
          }
        ],
        "android": [
          {
            "2020-01": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "68.4": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "n"
          }
        ],
        "ios": [
          {
            "2020-03": "n"
          }
        ],
        "android": [
          {
            "2020-03": "n"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "n"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "n"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "n"
          }
        ]
      },
      "free-fr": {
        "desktop-webmail": [
          {
            "2022-12": "n"
          }
        ]
      },
      "t-online-de": {
        "desktop-webmail": [
          {
            "2022-12": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "n"
          }
        ],
        "android": [
          {
            "2022-06": "n"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "n"
          }
        ],
        "android": [
          {
            "2022-06": "n"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "android": [
          {
            "2022-06": "n"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Supported on compatible browsers. Refer to ‘supported platforms’ links listed below under resources."
    }
  },
  {
    "slug": "bimi",
    "title": "BIMI",
    "description": "BIMI (Brand Indicators for Message Identification) is a specification allowing for the display of brand logos next to authenticated e-mails.",
    "url": "https://www.caniemail.com/features/bimi/",
    "category": "others",
    "tags": [],
    "keywords": "bimi, logo, brand",
    "last_test_date": "2022-12-29",
    "test_url": "https://www.caniemail.com",
    "test_results_url": null,
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "15": "n"
          },
          {
            "16": "y"
          }
        ],
        "ios": [
          {
            "15": "n"
          },
          {
            "16": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2023-01": "y"
          }
        ],
        "ios": [
          {
            "2023-01": "y"
          }
        ],
        "android": [
          {
            "2023-01": "y"
          }
        ],
        "mobile-webmail": [
          {
            "2023-01": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2023-01": "n"
          }
        ],
        "ios": [
          {
            "2023-01": "n"
          }
        ],
        "android": [
          {
            "2023-01": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2023-01": "n"
          }
        ],
        "macos": [
          {
            "16.56": "n"
          }
        ],
        "outlook-com": [
          {
            "2023-01": "n"
          }
        ],
        "ios": [
          {
            "2023-01": "n"
          }
        ],
        "android": [
          {
            "2023-01": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "6.0": "n"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2023-01": "n"
          }
        ],
        "ios": [
          {
            "2023-01": "n"
          }
        ],
        "android": [
          {
            "2023-01": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "78.14": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2023-01": "n"
          }
        ],
        "ios": [
          {
            "2023-01": "n"
          }
        ],
        "android": [
          {
            "2023-01": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2023-01": "y"
          }
        ],
        "ios": [
          {
            "2023-01": "y"
          }
        ],
        "android": [
          {
            "2023-01": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2023-01": "n"
          }
        ],
        "ios": [
          {
            "2023-01": "n"
          }
        ],
        "android": [
          {
            "2023-01": "n"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2023-01": "n"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2023-01": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2023-01": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2022-08": "y"
          }
        ]
      },
      "free-fr": {
        "desktop-webmail": [
          {
            "2023-01": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2023-01": "n"
          }
        ]
      },
      "t-online-de": {
        "desktop-webmail": [
          {
            "2023-01": "n"
          }
        ]
      }
    },
    "notes": "Data based on email clients providers own declarations.",
    "notes_by_num": null
  },
  {
    "slug": "css-accent-color",
    "title": "accent-color",
    "description": "",
    "url": "https://www.caniemail.com/features/css-accent-color/",
    "category": "css",
    "tags": [],
    "keywords": "accent,color",
    "last_test_date": "2023-12-19",
    "test_url": "https://www.caniemail.com/tests/css-accent-color.html",
    "test_results_url": "https://testi.at/proj/LAzSmlkimAnFmnrtPjPuPjpT1rO",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "16": "n"
          },
          {
            "17": "n"
          },
          {
            "18": "n"
          },
          {
            "19": "n"
          },
          {
            "20": "n"
          },
          {
            "21": "y"
          }
        ],
        "ios": [
          {
            "11": "n"
          },
          {
            "12": "n"
          },
          {
            "13": "n"
          },
          {
            "14": "y #1"
          },
          {
            "15": "y #1"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2022-07": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          },
          {
            "2021": "n"
          }
        ],
        "windows-mail": [
          {
            "2022-07": "n"
          }
        ],
        "macos": [
          {
            "2022-07": "n"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "2022-07": "y #1"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2022-07": "y #1"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Supports `accent-color` but rendering depends on browser support."
    }
  },
  {
    "slug": "css-align-items",
    "title": "align-items",
    "description": "",
    "url": "https://www.caniemail.com/features/css-align-items/",
    "category": "css",
    "tags": [],
    "keywords": "align,items,flexbox,grid",
    "last_test_date": "2023-12-19",
    "test_url": "https://www.caniemail.com/tests/css-align-items.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/FvYneb1dhiR4we6rAOf4AC02oFa6ksA0sTWxbEjgmt6Mg/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "11": "y"
          },
          {
            "12": "y"
          },
          {
            "13": "y"
          }
        ],
        "ios": [
          {
            "11": "y"
          },
          {
            "12": "y"
          },
          {
            "13": "y"
          },
          {
            "14": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2020-12": "n"
          }
        ],
        "ios": [
          {
            "2020-12": "n"
          }
        ],
        "android": [
          {
            "2020-12": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2020-12": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2021-02": "y"
          },
          {
            "2021-03": "n"
          }
        ],
        "ios": [
          {
            "2021-03": "y"
          },
          {
            "2024-04": "n"
          }
        ],
        "android": [
          {
            "2021-03": "y"
          },
          {
            "2024-04": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2020-12": "n"
          }
        ],
        "macos": [
          {
            "2020-12": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2020-12": "y"
          }
        ],
        "ios": [
          {
            "2020-12": "y"
          }
        ],
        "android": [
          {
            "4.2048.4": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2020-12": "n"
          }
        ],
        "ios": [
          {
            "2021-03": "n"
          }
        ],
        "android": [
          {
            "6.16.2.1519779": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2020-12": "n"
          }
        ],
        "ios": [
          {
            "2021-03": "n"
          }
        ],
        "android": [
          {
            "2021-03": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "6.1.31.2": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2021-03": "y"
          }
        ],
        "ios": [
          {
            "2021-03": "y"
          }
        ],
        "android": [
          {
            "2021-03": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "2020-12": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2021-03": "y"
          }
        ],
        "ios": [
          {
            "2021-03": "y"
          }
        ],
        "android": [
          {
            "2021-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2021-03": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-12": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y #1"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Supported. But a default style of `margin:auto` is applied on every element and can prevent the expected result."
    }
  },
  {
    "slug": "css-animation",
    "title": "animation",
    "description": "Tests for the shorthand `animation` property and its longhand equivalents.",
    "url": "https://www.caniemail.com/features/css-animation/",
    "category": "css",
    "tags": [],
    "keywords": "keyframes",
    "last_test_date": "2023-12-19",
    "test_url": "https://www.caniemail.com/tests/css-animation.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/u4oWccYOFNNyTagHs2NSUZqJYQ3MssrqDMocBnRa35hf7/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "13": "y"
          }
        ],
        "ios": [
          {
            "13": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2021-05": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2021-05": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2021-05": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "n"
          },
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2021-05": "n"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2021-05": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "6.1": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2021-05": "a #1"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "78.10": "y"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2021-05": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2021-05": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2021-05": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2021-05": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2021-05": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "a #1"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "a #2"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Buggy. Animation properties are supported but `@keyframes` are incorrectly prefixed.",
      "2": "Partial. Only supports from and to keyframes. Does not support % keyframes"
    }
  },
  {
    "slug": "css-aspect-ratio",
    "title": "aspect-ratio",
    "description": "Sets a preferred aspect ratio for the element",
    "url": "https://www.caniemail.com/features/css-aspect-ratio/",
    "category": "css",
    "tags": [],
    "keywords": "ratio",
    "last_test_date": "2023-12-19",
    "test_url": "https://www.caniemail.com/tests/css-aspect-ratio.html",
    "test_results_url": "https://testi.at/proj/Mv0IO0vs3vTgRQuJ8IzyBfD6",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "14": "n"
          },
          {
            "15.0": "y"
          }
        ],
        "ios": [
          {
            "11": "n"
          },
          {
            "12": "n"
          },
          {
            "13": "n"
          },
          {
            "14": "n"
          },
          {
            "15": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2021-10": "n"
          }
        ],
        "ios": [
          {
            "2021-10": "n"
          }
        ],
        "android": [
          {
            "2021-10": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2021-10": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2021-10": "n"
          }
        ],
        "ios": [
          {
            "2021-10": "n"
          }
        ],
        "android": [
          {
            "2021-10": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2021-10": "n"
          }
        ],
        "macos": [
          {
            "2021-10": "n"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2021-10": "n"
          },
          {
            "2023-12": "n"
          }
        ],
        "ios": [
          {
            "2021-10": "n"
          }
        ],
        "android": [
          {
            "2021-10": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2021-10": "n"
          }
        ],
        "ios": [
          {
            "2021-10": "n"
          }
        ],
        "android": [
          {
            "6.37": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2021-10": "n"
          }
        ],
        "ios": [
          {
            "2021-10": "n"
          }
        ],
        "android": [
          {
            "2021-10": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "2021-10": "n"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2021-11": "y"
          }
        ],
        "ios": [
          {
            "2021-11": "y #1"
          }
        ],
        "android": [
          {
            "2021-11": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "78.10.2": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2021-11": "y"
          }
        ],
        "ios": [
          {
            "2021-11": "y #1"
          }
        ],
        "android": [
          {
            "2021-11": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2021-11": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2021-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-11": "n"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-10": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Requires iOS 15."
    }
  },
  {
    "slug": "css-at-font-face",
    "title": "@font-face",
    "description": "`@font-face` in CSS allows to include your own fonts inside an email.",
    "url": "https://www.caniemail.com/features/css-at-font-face/",
    "category": "css",
    "tags": [],
    "keywords": "font face, web fonts, google fonts",
    "last_test_date": "2023-12-19",
    "test_url": "https://www.caniemail.com/tests/css-font-face.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/veY9MhuhgFeF1ly5crrhTXawfLJSwxgpYi27OElI7iSoc/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.2": "y"
          }
        ],
        "ios": [
          {
            "10.3": "y"
          },
          {
            "12.3.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-07": "n #6"
          }
        ],
        "ios": [
          {
            "2019-07": "n"
          }
        ],
        "android": [
          {
            "2019-07": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-05": "a #2"
          },
          {
            "2021-03": "n #7"
          },
          {
            "2024-03": "n"
          }
        ],
        "ios": [
          {
            "2019-07": "y"
          },
          {
            "2024-03": "n"
          }
        ],
        "android": [
          {
            "2019-07": "a #1"
          },
          {
            "2024-04": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "a #3"
          },
          {
            "2007": "a #4 #5"
          },
          {
            "2010": "a #4 #5"
          },
          {
            "2013": "a #4 #5"
          },
          {
            "2016": "a #4 #5"
          },
          {
            "2019": "a #4"
          }
        ],
        "windows-mail": [
          {
            "2020-01": "n"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2019-07": "n"
          },
          {
            "2023-12": "n"
          }
        ],
        "ios": [
          {
            "2.51.1": "y"
          },
          {
            "3.29.0": "n"
          }
        ],
        "android": [
          {
            "2019-07": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "6.0": "y #8"
          },
          {
            "2021-11": "y #8"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-07": "a #2"
          },
          {
            "2025-07": "n"
          }
        ],
        "ios": [
          {
            "2019-07": "n"
          }
        ],
        "android": [
          {
            "2019-07": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.7": "y"
          },
          {
            "78.5": "y"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2020-01": "n"
          }
        ],
        "ios": [
          {
            "2020-01": "n"
          }
        ],
        "android": [
          {
            "2020-01": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-07": "n"
          }
        ],
        "ios": [
          {
            "2019-07": "n"
          }
        ],
        "android": [
          {
            "2019-07": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "n"
          }
        ],
        "ios": [
          {
            "2020-03": "n"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "n"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "a #2"
          },
          {
            "2025-07": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "n"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "n"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "n"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. Only supported through a `<link>` tag.",
      "2": "Partial. Only supported directly through a `<style>` tag.",
      "3": "Buggy. Support depends on the version of IE installed.",
      "4": "Partial. The declaration is supported but distant fonts are ignored.",
      "5": "Buggy. Elements using a font declared with `@font-face` ignore the font stack and fall back to Times New Roman. Use `mso-generic-font-family` and `mso-font-alt` to control the fallback.",
      "6": "Not supported. Roboto and Google Sans can be used, but only because they're embedded with the webmail's own styles.",
      "7": "Not supported. The `@font-face` declaration is kept but the `src` property is removed.",
      "8": "Not supported when using a Microsoft email address; outlook, live, hotmail, etc."
    }
  },
  {
    "slug": "css-at-import",
    "title": "@import",
    "description": "This is the description of the `@import` property.",
    "url": "https://www.caniemail.com/features/css-at-import/",
    "category": "css",
    "tags": [],
    "keywords": "css, style",
    "last_test_date": "2019-02-28",
    "test_url": "https://www.caniemail.com/tests/css-placement.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/6vV9sx4RoRsdnkZBDjLWwSC18VcUQzJY00tlj2NVSxKKv/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "n"
          },
          {
            "2021-03": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2023-12": "n"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2023-12": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "y"
          },
          {
            "2010": "y"
          },
          {
            "2013": "y"
          },
          {
            "2016": "y"
          },
          {
            "2019": "y"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "y"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "n"
          },
          {
            "2023-12": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.8": "y"
          },
          {
            "78.5": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2020-01": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "n"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "n"
          },
          {
            "2025-07": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "n"
          }
        ],
        "android": [
          {
            "2019-08": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "n"
          }
        ],
        "ios": [
          {
            "2020-03": "n"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "n"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "n"
          },
          {
            "2025-07": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "n"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "n"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "n"
          }
        ]
      },
      "wp-pl": {
        "desktop-webmail": [
          {
            "2023-12": "n"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": null
  },
  {
    "slug": "css-at-keyframes",
    "title": "@keyframes",
    "description": "",
    "url": "https://www.caniemail.com/features/css-at-keyframes/",
    "category": "css",
    "tags": [],
    "keywords": "animation",
    "last_test_date": "2021-05-25",
    "test_url": "https://www.caniemail.com/tests/css-animation.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/u4oWccYOFNNyTagHs2NSUZqJYQ3MssrqDMocBnRa35hf7/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "13": "y"
          }
        ],
        "ios": [
          {
            "13": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2021-05": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2021-05": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2021-05": "n #1"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "n"
          },
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2021-05": "n"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2021-05": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "6.1": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2021-05": "a #1"
          },
          {
            "2025-07": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "78.10": "y"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2021-05": "y"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2021-05": "y"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2021-05": "n"
          }
        ],
        "ios": [
          {
            "2021-05": "n"
          }
        ],
        "android": [
          {
            "2021-05": "n"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2021-05": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2021-05": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "a #1"
          },
          {
            "2025-07": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "a #2"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Not supported. The `@keyframes` declaration is kept but values are incorrectly prefixed.",
      "2": "Partial. Only supports from and to keyframes. Does not support % keyframes"
    }
  },
  {
    "slug": "css-at-media-device-pixel-ratio",
    "title": "@media (-webkit-device-pixel-ratio)",
    "description": "",
    "url": "https://www.caniemail.com/features/css-at-media-device-pixel-ratio/",
    "category": "css",
    "tags": [],
    "keywords": "media queries, media query, media feature",
    "last_test_date": "2019-08-20",
    "test_url": "https://www.caniemail.com/tests/css-media.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/hMLCNCSKZYHkLgLOpIWltlnYjtagbNsrwzMxalc2VbghN/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.3": "y"
          }
        ],
        "ios": [
          {
            "10.3": "y"
          },
          {
            "12.2": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-08": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "n"
          }
        ],
        "android": [
          {
            "2019-08": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y #1"
          },
          {
            "2021-03": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "n"
          },
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2020-01": "n"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2025-07": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "n"
          }
        ],
        "android": [
          {
            "2019-08": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.3": "n"
          },
          {
            "78.5": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-08": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "n"
          }
        ],
        "android": [
          {
            "2019-08": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "n"
          }
        ],
        "ios": [
          {
            "2020-03": "n"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          },
          {
            "2025-07": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Buggy. The first rule inside a media query is not prefixed."
    }
  },
  {
    "slug": "css-at-media-hover",
    "title": "@media (hover), @media (any-hover)",
    "description": "This media query tests whether the user's input device[s] (i.e mouse, trackpad etc.) can hover over elements",
    "url": "https://www.caniemail.com/features/css-at-media-hover/",
    "category": "css",
    "tags": [
      "accessibility"
    ],
    "keywords": "media, media query, hover, any-hover",
    "last_test_date": "2022-08-29",
    "test_url": "https://www.caniemail.com/tests/css-media-hover.html",
    "test_results_url": "https://testi.at/proj/onECpNVH8Dhv7BSLPXUbQ4s0O",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "2022-08": "y"
          }
        ],
        "ios": [
          {
            "2022-08": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2022-08": "n"
          }
        ],
        "ios": [
          {
            "2022-08": "n"
          }
        ],
        "android": [
          {
            "2022-08": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2022-08": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2022-08": "u"
          }
        ],
        "ios": [
          {
            "2022-08": "u"
          }
        ],
        "android": [
          {
            "2022-08": "u"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2022-08": "n"
          }
        ],
        "windows-mail": [
          {
            "2022-08": "n"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2022-08": "y"
          }
        ],
        "ios": [
          {
            "2022-08": "y"
          }
        ],
        "android": [
          {
            "2022-08": "y"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "10": "y"
          },
          {
            "11": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2024-03": "y"
          },
          {
            "2025-07": "n"
          }
        ],
        "ios": [
          {
            "2024-03": "n"
          }
        ],
        "android": [
          {
            "2024-03": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "2022-08": "u"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2022-08": "n"
          }
        ],
        "ios": [
          {
            "2022-08": "n"
          }
        ],
        "android": [
          {
            "2022-08": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2022-08": "n"
          }
        ],
        "ios": [
          {
            "2022-08": "n"
          }
        ],
        "android": [
          {
            "2022-08": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2022-08": "y"
          }
        ],
        "ios": [
          {
            "2022-08": "y"
          }
        ],
        "android": [
          {
            "2022-08": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2022-08": "u"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2022-08": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2022-08": "u"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2022-08": "u"
          },
          {
            "2025-07": "n"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": null
  },
  {
    "slug": "css-at-media-orientation",
    "title": "@media (orientation)",
    "description": "",
    "url": "https://www.caniemail.com/features/css-at-media-orientation/",
    "category": "css",
    "tags": [],
    "keywords": "media queries, media query, media feature, portrait, landscape",
    "last_test_date": "2019-08-20",
    "test_url": "https://www.caniemail.com/tests/css-media.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/hMLCNCSKZYHkLgLOpIWltlnYjtagbNsrwzMxalc2VbghN/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.3": "y"
          }
        ],
        "ios": [
          {
            "10.3": "n"
          },
          {
            "12": "y"
          },
          {
            "13": "y"
          },
          {
            "15": "y"
          },
          {
            "18.3.2": "a #2"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2025-04": "n"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y #1"
          },
          {
            "2021-03": "y"
          },
          {
            "2024-04": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "n"
          },
          {
            "2024-04": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "y"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "n"
          },
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2020-01": "n"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "n"
          },
          {
            "6.0": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2025-07": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "n"
          }
        ],
        "android": [
          {
            "2019-08": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.3": "y"
          },
          {
            "78.5": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-08": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "n"
          }
        ],
        "android": [
          {
            "2019-08": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "n"
          }
        ],
        "ios": [
          {
            "2020-03": "n"
          }
        ],
        "android": [
          {
            "2020-03": "n"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          },
          {
            "2025-07": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Buggy. The first rule inside a media query is not prefixed.",
      "2": "Partial. `orientation:portrait` is not supported."
    }
  },
  {
    "slug": "css-at-media-prefers-color-scheme",
    "title": "@media (prefers-color-scheme)",
    "description": "This media query allows to theme for system light and dark mode.",
    "url": "https://www.caniemail.com/features/css-at-media-prefers-color-scheme/",
    "category": "css",
    "tags": [
      "accessibility"
    ],
    "keywords": "media queries, media query, media feature, dark mode, light mode",
    "last_test_date": "2023-03-08",
    "test_url": "https://www.caniemail.com/tests/css-media-prefers-color-scheme.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/CBhafIa5yXDRKQKbV442rVFISXim84wMgXaoCqVFD8VTe/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.3": "n"
          },
          {
            "12.4": "y"
          },
          {
            "16.0": "y"
          }
        ],
        "ios": [
          {
            "12.2": "n"
          },
          {
            "13.0": "y"
          },
          {
            "16.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2020-01": "n"
          },
          {
            "2022-12": "n"
          }
        ],
        "ios": [
          {
            "2020-01": "n"
          },
          {
            "2022-12": "n"
          }
        ],
        "android": [
          {
            "2020-01": "n"
          },
          {
            "2022-12": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          },
          {
            "2022-12": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "y"
          },
          {
            "2022-12": "y"
          },
          {
            "2024-04": "y"
          }
        ],
        "ios": [
          {
            "2020-01": "n"
          },
          {
            "2022-12": "y"
          },
          {
            "2024-04": "y"
          }
        ],
        "android": [
          {
            "2020-01": "n"
          },
          {
            "2022-12": "n"
          },
          {
            "2024-04": "y"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "n"
          },
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2020-01": "n"
          }
        ],
        "macos": [
          {
            "2019": "y"
          },
          {
            "16.70": "y #3"
          },
          {
            "16.80": "y #3"
          }
        ],
        "outlook-com": [
          {
            "2019-07": "y"
          },
          {
            "2022-12": "y #3"
          }
        ],
        "ios": [
          {
            "2020-01": "y"
          },
          {
            "2022-12": "y #3"
          }
        ],
        "android": [
          {
            "2020-01": "n"
          },
          {
            "2022-12": "n #3"
          },
          {
            "2023-03": "y #3"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "6.0": "n"
          },
          {
            "6.1": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2022-12": "y"
          },
          {
            "2025-07": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "n"
          },
          {
            "2022-12": "n"
          }
        ],
        "android": [
          {
            "2019-08": "n"
          },
          {
            "2022-12": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.8": "n"
          },
          {
            "68.4": "y"
          },
          {
            "78.5": "n"
          },
          {
            "91.13": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2020-01": "n #1"
          }
        ],
        "ios": [
          {
            "2020-01": "n #1"
          }
        ],
        "android": [
          {
            "2020-01": "n #1"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2020-01": "n #1"
          },
          {
            "2022-12": "n #6"
          }
        ],
        "ios": [
          {
            "2020-01": "n #1"
          },
          {
            "2022-12": "n"
          }
        ],
        "android": [
          {
            "2020-01": "n #1"
          },
          {
            "2022-12": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "n"
          },
          {
            "2022-12": "n"
          }
        ],
        "ios": [
          {
            "2020-03": "n"
          }
        ],
        "android": [
          {
            "2020-03": "n"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          },
          {
            "2022-12": "n #5"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "n"
          },
          {
            "2022-12": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "n #2"
          },
          {
            "2022-12": "y #4"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          },
          {
            "2022-12": "y"
          },
          {
            "2025-07": "n"
          }
        ]
      },
      "free-fr": {
        "desktop-webmail": [
          {
            "2022-12": "y"
          }
        ]
      },
      "t-online-de": {
        "desktop-webmail": [
          {
            "2022-12": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Not supported. `@media (prefers-color-scheme)` is transformed into `@media ( _filtered_a )`.",
      "2": "Not supported. `@media (prefers-color-scheme:dark)` is transformed into `@media none`.",
      "3": "Additional custom `data` attributes (`data-ogsc`, `data-ogac`, `data-ogsb`, `data-ogab`) are added when viewing an email in dark mode. See [this article](https://www.hteumeuleu.com/2021/emails-react-outlook-com-dark-mode/) for examples.",
      "4": "`@media (prefers-color-scheme:dark)` is transformed into `@media all` at run time if it applies.",
      "5": "Not supported. `@media (prefers-color-scheme:dark)` is transformed into `@media (false)`",
      "6": "Not supported. `@media (prefers-color-scheme:dark)` is transformed into `@media ()`"
    }
  },
  {
    "slug": "css-at-media-prefers-reduced-motion",
    "title": "@media (prefers-reduced-motion)",
    "description": "",
    "url": "https://www.caniemail.com/features/css-at-media-prefers-reduced-motion/",
    "category": "css",
    "tags": [
      "accessibility",
      "performance"
    ],
    "keywords": "media queries, media query, media feature, prefers-reduced-motion, animation, accessibility",
    "last_test_date": "2021-02-20",
    "test_url": "https://www.caniemail.com/tests/css-media-prefers-reduced-motion.html",
    "test_results_url": "https://testi.at/proj/e3GT3l1CxqBUoE3u9keC4WLf5",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "11": "y"
          },
          {
            "12": "y"
          },
          {
            "13": "y"
          }
        ],
        "ios": [
          {
            "11": "y"
          },
          {
            "12": "y"
          },
          {
            "13": "y"
          },
          {
            "14": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2020-12": "n"
          }
        ],
        "ios": [
          {
            "2020-12": "n"
          }
        ],
        "android": [
          {
            "2020-12": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2020-12": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2021-02": "y"
          },
          {
            "2021-03": "y"
          }
        ],
        "ios": [
          {
            "2021-02": "y"
          }
        ],
        "android": [
          {
            "2021-02": "y"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "16005.13426.20316.0": "n"
          }
        ],
        "macos": [
          {
            "2020-12": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2020-12": "y"
          }
        ],
        "ios": [
          {
            "2020-12": "y"
          }
        ],
        "android": [
          {
            "4.2048.4": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2020-12": "n"
          }
        ],
        "ios": [
          {
            "2021-02": "n"
          }
        ],
        "android": [
          {
            "6.16.2.1519779": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2020-12": "n"
          }
        ],
        "ios": [
          {
            "2021-02": "n"
          }
        ],
        "android": [
          {
            "2021-02": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "6.1.31.2": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2021-02": "y"
          }
        ],
        "ios": [
          {
            "2021-02": "n"
          }
        ],
        "android": [
          {
            "2021-02": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "78.7": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2021-02": "a #2"
          }
        ],
        "ios": [
          {
            "2021-02": "a #2"
          }
        ],
        "android": [
          {
            "2021-02": "a #2"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2021-02": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2021-02": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "n #1"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          },
          {
            "2025-07": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Not supported. `@media (prefers-reduced-motion:reduce)` is transformed into `@media none`.",
      "2": "Partially supported. Not supported on `picture`."
    }
  },
  {
    "slug": "css-at-media",
    "title": "@media",
    "description": "",
    "url": "https://www.caniemail.com/features/css-at-media/",
    "category": "css",
    "tags": [],
    "keywords": "media queries, media query, media feature",
    "last_test_date": "2023-12-13",
    "test_url": "https://www.caniemail.com/tests/css-media.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/hMLCNCSKZYHkLgLOpIWltlnYjtagbNsrwzMxalc2VbghN/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.3": "y"
          }
        ],
        "ios": [
          {
            "10.3": "y"
          },
          {
            "12.2": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-08": "a #1 #7"
          },
          {
            "2020-01": "a #7"
          }
        ],
        "ios": [
          {
            "2019-08": "a #1 #6 #7"
          },
          {
            "2020-01": "a #6 #7"
          }
        ],
        "android": [
          {
            "2019-08": "a #1 #6 #7"
          },
          {
            "2022-07": "a #6 #7"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y #5"
          },
          {
            "2021-03": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "a #1"
          },
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2020-01": "n"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "a #1 #10"
          }
        ],
        "outlook-com": [
          {
            "2019-08": "a #1"
          },
          {
            "2023-12": "a #1 #10"
          }
        ],
        "ios": [
          {
            "2019-08": "a #1"
          }
        ],
        "android": [
          {
            "2019-08": "a #1"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0": "y"
          },
          {
            "6.1.90.16": "a #9"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2025-07": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "n"
          }
        ],
        "android": [
          {
            "2019-08": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.3": "y"
          },
          {
            "78.5": "n"
          },
          {
            "102.11": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-08": "a #1 #2"
          },
          {
            "2020-01": "a #2"
          }
        ],
        "ios": [
          {
            "2019-08": "a #1 #2"
          },
          {
            "2020-01": "a #2"
          }
        ],
        "android": [
          {
            "2019-08": "a #1 #2 #3"
          },
          {
            "2020-01": "a #2 #3"
          },
          {
            "2025-06": "a #2"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "a #1 #2"
          },
          {
            "2020-01": "a #2"
          }
        ],
        "ios": [
          {
            "2019-02": "a #1 #2"
          },
          {
            "2020-01": "a #2"
          }
        ],
        "android": [
          {
            "2019-02": "a #1 #2"
          },
          {
            "2020-01": "a #2"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "n"
          },
          {
            "2023-05": "a #8"
          }
        ],
        "ios": [
          {
            "2020-03": "n"
          },
          {
            "2023-05": "a #8"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "a #1 #7"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          },
          {
            "2025-07": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "y #1"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "y #1"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. Does not support nested media queries.",
      "2": "Partial. Only supports `screen`, `min-width`, `max-width`, `min-height` and `max-height` based media queries.",
      "3": "Buggy. Requires a double `<head>` hack to work.",
      "4": "Partial. Does not support simple `@media {}` declarations.",
      "5": "Buggy. The first rule inside a media query is not prefixed.",
      "6": "Partial. Not supported with non Google accounts.",
      "7": "Partial. Does not support height based media queries.",
      "8": "Partial. Does not support landscape media query.",
      "9": "Partial. Not supported with Hotmail/Outlook accounts.",
      "10": "Partial. Nested media queries are removed."
    }
  },
  {
    "slug": "css-at-supports",
    "title": "@supports",
    "description": null,
    "url": "https://www.caniemail.com/features/css-at-supports/",
    "category": "css",
    "tags": [],
    "keywords": "feature queries",
    "last_test_date": "2020-05-25",
    "test_url": "https://www.caniemail.com/tests/css-at-supports.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/No78GouZXTsxEZCD6z4Hn2frAvg3tHBw1SRAP8SwPKsZ5/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "13": "y"
          }
        ],
        "ios": [
          {
            "13": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2020-05": "n"
          }
        ],
        "ios": [
          {
            "2020-05": "n"
          }
        ],
        "android": [
          {
            "2020-05": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2020-05": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2020-05": "y"
          },
          {
            "2021-03": "y"
          }
        ],
        "ios": [
          {
            "2020-05": "y"
          }
        ],
        "android": [
          {
            "2020-05": "y"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "n"
          },
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2020-05": "n"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2020-05": "n"
          }
        ],
        "ios": [
          {
            "2020-05": "n"
          }
        ],
        "android": [
          {
            "2020-05": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "6.0": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2020-05": "y"
          },
          {
            "2025-07": "n"
          }
        ],
        "ios": [
          {
            "2020-05": "n"
          }
        ],
        "android": [
          {
            "2020-05": "n"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "68.7": "y"
          },
          {
            "78.5": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2020-05": "y #1"
          }
        ],
        "ios": [
          {
            "2020-05": "y #1"
          }
        ],
        "android": [
          {
            "2020-05": "y #1"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2020-05": "y #1"
          }
        ],
        "ios": [
          {
            "2020-05": "y #1"
          }
        ],
        "android": [
          {
            "2020-05": "y #1"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-05": "n"
          }
        ],
        "ios": [
          {
            "2020-05": "n"
          }
        ],
        "android": [
          {
            "2020-05": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "n"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "n #2"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          },
          {
            "2025-07": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Properties not supported by the client are replaced by `_filtered_a` inside the parenthesis.",
      "2": "Not supported. `@supports` is transformed into `@media not all`."
    }
  },
  {
    "slug": "css-backdrop-filter",
    "title": "backdrop-filter",
    "description": "Lets you apply graphical effects such as blurring or color shifting to the area behind an element.",
    "url": "https://www.caniemail.com/features/css-backdrop-filter/",
    "category": "css",
    "tags": [],
    "keywords": "filter",
    "last_test_date": "2024-01-17",
    "test_url": "https://www.caniemail.com/tests/css-backdrop-filter.html",
    "test_results_url": "https://testi.at/proj/p4r7t9n30o7nh7vvfpn",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10": "y #1"
          },
          {
            "11": "u"
          },
          {
            "12": "u"
          },
          {
            "13": "y #1"
          }
        ],
        "ios": [
          {
            "11": "n"
          },
          {
            "12": "n"
          },
          {
            "13": "y #1"
          },
          {
            "14": "y #1"
          },
          {
            "15": "y #1"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2024-01": "n"
          }
        ],
        "ios": [
          {
            "2024-01": "n"
          }
        ],
        "android": [
          {
            "2024-01": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2024-01": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2024-01": "u"
          }
        ],
        "ios": [
          {
            "2024-01": "n"
          }
        ],
        "android": [
          {
            "2024-01": "u"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          },
          {
            "2021": "n"
          }
        ],
        "windows-mail": [
          {
            "2024-01": "n"
          }
        ],
        "macos": [
          {
            "2024-01": "y"
          }
        ],
        "outlook-com": [
          {
            "2024-01": "n"
          }
        ],
        "ios": [
          {
            "2024-01": "n"
          }
        ],
        "android": [
          {
            "2024-01": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2024-01": "n"
          }
        ],
        "ios": [
          {
            "2024-01": "n"
          }
        ],
        "android": [
          {
            "2024-01": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2024-01": "n"
          }
        ],
        "ios": [
          {
            "2024-01": "n"
          }
        ],
        "android": [
          {
            "2024-01": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "2024-01": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2024-03": "y"
          }
        ],
        "ios": [
          {
            "2024-03": "y"
          }
        ],
        "android": [
          {
            "2024-03": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "2024-01": "u"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2024-01": "u"
          }
        ],
        "ios": [
          {
            "2024-01": "u"
          }
        ],
        "android": [
          {
            "2024-01": "u"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2024-01": "u"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2024-01": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2024-01": "u"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2024-01": "u"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2024-01": "n"
          }
        ],
        "ios": [
          {
            "2024-01": "u"
          }
        ],
        "android": [
          {
            "2024-01": "u"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2024-01": "n"
          }
        ],
        "ios": [
          {
            "2024-01": "u"
          }
        ],
        "android": [
          {
            "2024-01": "u"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2024-01": "u"
          }
        ],
        "android": [
          {
            "2024-01": "u"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Works with prefix `-webkit`"
    }
  },
  {
    "slug": "css-background-blend-mode",
    "title": "background-blend-mode",
    "description": "",
    "url": "https://www.caniemail.com/features/css-background-blend-mode/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2019-02-28",
    "test_url": "https://www.caniemail.com/tests/css-background.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/oxaaoE6R3ur4T9fAPzVsQ3G2R7p1c9axDm7LLgC3cKw0F/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "a #1"
          }
        ],
        "android": [
          {
            "2019-02": "a #1"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "n"
          },
          {
            "2024-04": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "n"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0.04.6": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5.0": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. Not supported with non Google accounts."
    }
  },
  {
    "slug": "css-background-clip",
    "title": "background-clip",
    "description": "",
    "url": "https://www.caniemail.com/features/css-background-clip/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2019-02-28",
    "test_url": "https://www.caniemail.com/tests/css-background.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/oxaaoE6R3ur4T9fAPzVsQ3G2R7p1c9axDm7LLgC3cKw0F/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "a #1"
          }
        ],
        "android": [
          {
            "2019-02": "a #1"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "n"
          },
          {
            "2024-04": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "n"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0.04.6": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5.0": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. Not supported with non Google accounts. But it can be used in the `background` shorthand property instead."
    }
  },
  {
    "slug": "css-background-color",
    "title": "background-color",
    "description": "",
    "url": "https://www.caniemail.com/features/css-background-color/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2019-02-28",
    "test_url": "https://www.caniemail.com/tests/css-background.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/oxaaoE6R3ur4T9fAPzVsQ3G2R7p1c9axDm7LLgC3cKw0F/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "y"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "a #1"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2021-10": "a #1"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2021-10": "a #1"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "y"
          },
          {
            "2007": "y"
          },
          {
            "2010": "y"
          },
          {
            "2013": "y"
          },
          {
            "2016": "y"
          },
          {
            "2019": "y"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "y"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0.04.6": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5.0": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "a #1"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "a #1"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Buggy. Only supports [color keywords from CSS Level 1](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#color_keywords)."
    }
  },
  {
    "slug": "css-background-image",
    "title": "background-image",
    "description": "",
    "url": "https://www.caniemail.com/features/css-background-image/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2023-07-24",
    "test_url": "https://www.caniemail.com/tests/css-background.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/04SuPXr8tEGhWRlJ2Us6dA8BzgREpyxHYEmSBeyNuWyWo/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          },
          {
            "2023-07": "a #6"
          },
          {
            "2023-08": "y"
          }
        ],
        "ios": [
          {
            "2018-09": "a #1"
          },
          {
            "2018-10": "y"
          },
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2018-09": "a #1"
          },
          {
            "2018-10": "y"
          },
          {
            "2019-02": "y"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "y"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "y"
          },
          {
            "2024-04": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "y"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n #5"
          },
          {
            "2010": "n #5"
          },
          {
            "2013": "n #5"
          },
          {
            "2016": "n #5"
          },
          {
            "2019": "n #5"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "n"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "a #3 #4"
          },
          {
            "2021-10": "a #3"
          }
        ],
        "ios": [
          {
            "2019-02": "a #3 #4"
          },
          {
            "2021-10": "a #3"
          }
        ],
        "android": [
          {
            "2019-02": "a #3 #4"
          },
          {
            "2021-10": "a #3"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "a #3 #4"
          },
          {
            "2021-10": "a #3"
          }
        ],
        "ios": [
          {
            "2019-02": "a #3 #4"
          },
          {
            "2021-10": "a #3"
          }
        ],
        "android": [
          {
            "2019-02": "a #3 #4"
          },
          {
            "2021-10": "a #3"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "a #2"
          },
          {
            "6.0.04.6": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5.0": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "t-online-de": {
        "desktop-webmail": [
          {
            "2021-11": "n"
          }
        ]
      },
      "free-fr": {
        "desktop-webmail": [
          {
            "2021-11": "n"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "a #3"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "a #3"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. Not supported with non Google accounts.",
      "2": "Buggy. Requires at least one `<img>` element in the email to download all images.",
      "3": "Partial. Does not support multiple values. The comma between two values is removed.",
      "4": "Partial. Images URL must be between quotes.",
      "5": "Background images can be used in VML. See [backgrounds.cm](https://backgrounds.cm/) and [VML documentation](https://docs.microsoft.com/en-us/windows/win32/vml/web-workshop---how-to-use-vml-on-web-pages-----fill--element).",
      "6": "Partial and buggy. Removes the entire `style` attribute or `<style>` tag when a `url()` function with a valid image URL is present. See [Gmail rolling out changes that strip CSS with background images](https://freshinbox.com/blog/gmail-rolling-out-changes-that-strip-background-image-css/) and [Gmail and background images](https://parcel.io/blog/gmail-and-background-images)."
    }
  },
  {
    "slug": "css-background-origin",
    "title": "background-origin",
    "description": "",
    "url": "https://www.caniemail.com/features/css-background-origin/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2019-02-28",
    "test_url": "https://www.caniemail.com/tests/css-background.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/oxaaoE6R3ur4T9fAPzVsQ3G2R7p1c9axDm7LLgC3cKw0F/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "a"
          }
        ],
        "android": [
          {
            "2019-02": "a"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "n"
          },
          {
            "2024-04": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n #1"
          },
          {
            "2010": "n #1"
          },
          {
            "2013": "n #1"
          },
          {
            "2016": "n #1"
          },
          {
            "2019": "n #1"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "n"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0.04.6": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5.0": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Background images origin can be used in VML with the `origin` attribute. See [VML documentation](https://docs.microsoft.com/en-us/windows/win32/vml/origin-attribute--fill--vml)."
    }
  },
  {
    "slug": "css-background-position",
    "title": "background-position",
    "description": "",
    "url": "https://www.caniemail.com/features/css-background-position/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2019-02-28",
    "test_url": "https://www.caniemail.com/tests/css-background.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/oxaaoE6R3ur4T9fAPzVsQ3G2R7p1c9axDm7LLgC3cKw0F/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "y #1"
          }
        ],
        "ios": [
          {
            "2019-02": "a"
          },
          {
            "2021-10": "y #1"
          }
        ],
        "android": [
          {
            "2019-02": "a"
          },
          {
            "2021-10": "y #1"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "y"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "y"
          },
          {
            "2024-04": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "y"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n #2"
          },
          {
            "2010": "n #2"
          },
          {
            "2013": "n #2"
          },
          {
            "2016": "n #2"
          },
          {
            "2019": "n #2"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "n"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "y #1"
          }
        ],
        "ios": [
          {
            "2019-02": "y #1"
          }
        ],
        "android": [
          {
            "2019-02": "y #1"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "y #1"
          }
        ],
        "ios": [
          {
            "2019-02": "y #1"
          }
        ],
        "android": [
          {
            "2019-02": "y #1"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0.04.6": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5.0": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "a #1"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "a #1"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. Does not support multiple values. The comma between two values is removed.",
      "2": "Background images position can be used in VML with the `position` attribute. See [VML documentation](https://docs.microsoft.com/en-us/windows/win32/vml/position-attribute--fill--vml)."
    }
  },
  {
    "slug": "css-background-repeat",
    "title": "background-repeat",
    "description": "",
    "url": "https://www.caniemail.com/features/css-background-repeat/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2019-02-28",
    "test_url": "https://www.caniemail.com/tests/css-background.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/oxaaoE6R3ur4T9fAPzVsQ3G2R7p1c9axDm7LLgC3cKw0F/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "a"
          },
          {
            "2021-10": "y"
          }
        ],
        "android": [
          {
            "2019-02": "a"
          },
          {
            "2021-10": "y"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "y"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "y"
          },
          {
            "2024-04": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "y"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n #2"
          },
          {
            "2010": "n #2"
          },
          {
            "2013": "n #2"
          },
          {
            "2016": "n #2"
          },
          {
            "2019": "n #2"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "n"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "y #1"
          }
        ],
        "ios": [
          {
            "2019-02": "y #1"
          }
        ],
        "android": [
          {
            "2019-02": "y #1"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "y #1"
          }
        ],
        "ios": [
          {
            "2019-02": "y #1"
          }
        ],
        "android": [
          {
            "2019-02": "y #1"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0.04.6": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5.0": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "a #1"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "a #1"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. Does not support multiple values. The comma between two values is removed.",
      "2": "Background images repetition can be used in VML with the `type=\"tile\"` or `type=\"frame\"` attribute. See [VML documentation](https://docs.microsoft.com/en-us/windows/win32/vml/type-attribute--fill--vml)."
    }
  },
  {
    "slug": "css-background-size",
    "title": "background-size",
    "description": "",
    "url": "https://www.caniemail.com/features/css-background-size/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2019-02-28",
    "test_url": "https://www.caniemail.com/tests/css-background.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/oxaaoE6R3ur4T9fAPzVsQ3G2R7p1c9axDm7LLgC3cKw0F/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "a #1"
          }
        ],
        "android": [
          {
            "2019-02": "a #1"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n #3"
          },
          {
            "2010": "n #3"
          },
          {
            "2013": "n #3"
          },
          {
            "2016": "n #3"
          },
          {
            "2019": "n #3"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "n"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "y #2"
          }
        ],
        "ios": [
          {
            "2019-02": "y #2"
          }
        ],
        "android": [
          {
            "2019-02": "y #2"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "y #2"
          }
        ],
        "ios": [
          {
            "2019-02": "y #2"
          }
        ],
        "android": [
          {
            "2019-02": "y #2"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0.04.6": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5.0": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. Not supported with non Google accounts. But it can be used in the `background` shorthand property instead.",
      "2": "Partial. Does not support multiple values. The comma between two values is removed.",
      "3": "Background images size can be used in VML with the `size` attribute. See [VML documentation](https://docs.microsoft.com/en-us/windows/win32/vml/size-attribute--fill--vml)."
    }
  },
  {
    "slug": "css-background",
    "title": "background",
    "description": "",
    "url": "https://www.caniemail.com/features/css-background/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2023-07-24",
    "test_url": "https://www.caniemail.com/tests/css-background.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/04SuPXr8tEGhWRlJ2Us6dA8BzgREpyxHYEmSBeyNuWyWo/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "y"
          },
          {
            "2023-07": "a #6 #7"
          },
          {
            "2023-08": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "y"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "a #6"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "a #6"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "a #6"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "a #3"
          },
          {
            "2010": "a #3"
          },
          {
            "2013": "a #3"
          },
          {
            "2016": "a #3"
          },
          {
            "2019": "a #3"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "n"
          },
          {
            "2021-10": "a #3"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "y"
          }
        ],
        "ios": [
          {
            "2019-02": "y"
          }
        ],
        "android": [
          {
            "2019-02": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "a #1 #2 #4"
          },
          {
            "2021-10": "a #1 #2"
          }
        ],
        "ios": [
          {
            "2019-02": "a #1 #2 #4"
          },
          {
            "2021-10": "a #1 #2"
          }
        ],
        "android": [
          {
            "2019-02": "a #1 #2 #4"
          },
          {
            "2021-10": "a #1 #2"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "a #1 #2 #4"
          },
          {
            "2021-10": "a #1 #2"
          }
        ],
        "ios": [
          {
            "2019-02": "a #1 #2 #4"
          },
          {
            "2021-10": "a #1 #2"
          }
        ],
        "android": [
          {
            "2019-02": "a #1 #2 #4"
          },
          {
            "2021-10": "a #1 #2"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          },
          {
            "6.0.04.6": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5.0": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y #5"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "a #1 #5 #6"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "a #1 #5 #6"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. Does not support multiple values. The comma between two values is removed.",
      "2": "Partial. Does not support the `/ value` shorthand for `background-size`. But it can be used in the `background-size` property instead.",
      "3": "Partial. Only `background-color` values are supported.",
      "4": "Partial. Images URL must be between quotes.",
      "5": "Partial. Does not support multiple values. The entire property is removed if so.",
      "6": "Partial. Does not support the `/ value` shorthand for `background-size`.",
      "7": "Partial and buggy. Removes the entire `style` attribute or `<style>` tag when a `url()` function with a valid image URL is present. See [Gmail rolling out changes that strip CSS with background images](https://freshinbox.com/blog/gmail-rolling-out-changes-that-strip-background-image-css/) and [Gmail and background images](https://parcel.io/blog/gmail-and-background-images)."
    }
  },
  {
    "slug": "css-block-inline-size",
    "title": "block-size & inline-size",
    "description": "Defines the horizontal or vertical size of an element's block, depending on its writing mode.",
    "url": "https://www.caniemail.com/features/css-block-inline-size/",
    "category": "css",
    "tags": [
      "i18n"
    ],
    "keywords": "block-size, inline-size",
    "last_test_date": "2022-07-14",
    "test_url": "https://www.caniemail.com/tests/css-block-size.html",
    "test_results_url": "https://testi.at/proj/0xeT11rcnx6IzN7f9NsVFlZ",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.13": "n"
          },
          {
            "10.15": "y"
          },
          {
            "11": "y"
          },
          {
            "12": "y"
          }
        ],
        "ios": [
          {
            "14": "y"
          },
          {
            "15": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2022-07": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "u"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          },
          {
            "2022": "n"
          }
        ],
        "windows-mail": [
          {
            "2022-07": "n"
          }
        ],
        "macos": [
          {
            "16.56": "y"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2022-07": "n"
          },
          {
            "2024-01": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "10": "y"
          },
          {
            "11": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ],
        "ios": [
          {
            "2022-07": "y"
          }
        ],
        "android": [
          {
            "2022-07": "u"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "91.11.0": "y"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ],
        "ios": [
          {
            "2022-07": "y"
          }
        ],
        "android": [
          {
            "2022-07": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-09": "n"
          }
        ],
        "ios": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-09": "n"
          }
        ],
        "ios": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": null
  },
  {
    "slug": "css-border-collapse",
    "title": "border-collapse",
    "description": "Sets whether cells inside a `<table>` have shared or separate borders.",
    "url": "https://www.caniemail.com/features/css-border-collapse/",
    "category": "css",
    "tags": [],
    "keywords": "table",
    "last_test_date": "2023-12-20",
    "test_url": "https://www.caniemail.com/tests/css-border-collapse.html",
    "test_results_url": "https://testi.at/proj/4zk4fe7tv86fn4bc6",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "2023-12": "y"
          }
        ],
        "ios": [
          {
            "2023-12": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2023-12": "y"
          }
        ],
        "ios": [
          {
            "2023-12": "y"
          }
        ],
        "android": [
          {
            "2023-12": "y"
          }
        ],
        "mobile-webmail": [
          {
            "2023-12": "y"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2023-12": "u"
          }
        ],
        "ios": [
          {
            "2023-12": "u"
          }
        ],
        "android": [
          {
            "2023-12": "u"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2023-12": "y"
          }
        ],
        "windows-mail": [
          {
            "2023-12": "y"
          }
        ],
        "macos": [
          {
            "2023-12": "y"
          }
        ],
        "outlook-com": [
          {
            "2023-12": "y"
          }
        ],
        "ios": [
          {
            "2023-12": "y"
          }
        ],
        "android": [
          {
            "2023-12": "y"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2023-12": "y"
          }
        ],
        "ios": [
          {
            "2023-12": "y"
          }
        ],
        "android": [
          {
            "2023-12": "y"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2023-12": "y"
          }
        ],
        "ios": [
          {
            "2023-12": "y"
          }
        ],
        "android": [
          {
            "2023-12": "y"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "2023-12": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2024-03": "y"
          }
        ],
        "ios": [
          {
            "2024-03": "y"
          }
        ],
        "android": [
          {
            "2024-03": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "2023-12": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2023-12": "u"
          }
        ],
        "ios": [
          {
            "2023-12": "u"
          }
        ],
        "android": [
          {
            "2023-12": "u"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2023-12": "u"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2023-12": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2023-12": "u"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2023-12": "u"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2023-12": "y"
          }
        ],
        "ios": [
          {
            "2023-12": "u"
          }
        ],
        "android": [
          {
            "2023-12": "u"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2023-12": "y"
          }
        ],
        "ios": [
          {
            "2023-12": "u"
          }
        ],
        "android": [
          {
            "2023-12": "u"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2023-12": "u"
          }
        ],
        "android": [
          {
            "2023-12": "u"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": null
  },
  {
    "slug": "css-border-image",
    "title": "border-image",
    "description": "",
    "url": "https://www.caniemail.com/features/css-border-image/",
    "category": "css",
    "tags": [],
    "keywords": null,
    "last_test_date": "2019-02-28",
    "test_url": "https://www.caniemail.com/tests/css-box-model.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/pyPQFHSYLFrhbRShalju0B2fYNwUgLuyKTLx4MLqiw5mE/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "12.4": "y"
          }
        ],
        "ios": [
          {
            "12.1": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "n"
          },
          {
            "2024-04": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2007": "n"
          },
          {
            "2010": "n"
          },
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          }
        ],
        "windows-mail": [
          {
            "2019-02": "n"
          }
        ],
        "macos": [
          {
            "2019-02": "y"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2019-02": "n"
          }
        ],
        "ios": [
          {
            "2019-02": "n"
          }
        ],
        "android": [
          {
            "2019-02": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "5.0.10.2": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.5": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": null
  },
  {
    "slug": "css-border-inline-block-individual",
    "title": "border-inline & border-block individual logical properties",
    "description": "Support for `border-inline` & `border-block` individual logical properties.",
    "url": "https://www.caniemail.com/features/css-border-inline-block-individual/",
    "category": "css",
    "tags": [
      "i18n"
    ],
    "keywords": "border-inline-color, border-block-color, border-inline-style, border-block-style, border-inline-width, border-block-width, border-inline-start, border-inline-end, border-block-start, border-block-end",
    "last_test_date": "2022-07-14",
    "test_url": "https://www.caniemail.com/tests/css-border-logical-properties.html",
    "test_results_url": "https://testi.at/proj/1yxFDAGtwrUmbf4tzMTY",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.12": "n"
          },
          {
            "10.13": "n"
          },
          {
            "10.15": "a #1"
          },
          {
            "11": "y"
          },
          {
            "12": "y"
          }
        ],
        "ios": [
          {
            "11": "n"
          },
          {
            "12": "a #1"
          },
          {
            "13": "a #1"
          },
          {
            "14": "a #1"
          },
          {
            "15": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2022-07": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ],
        "ios": [
          {
            "2022-07": "u"
          }
        ],
        "android": [
          {
            "2022-07": "u"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          },
          {
            "2021": "n"
          }
        ],
        "windows-mail": [
          {
            "2022-07": "n"
          }
        ],
        "macos": [
          {
            "2011": "a #1"
          },
          {
            "2016": "a #1"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "10": "a #1"
          },
          {
            "11": "a #1"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2024-03": "y"
          }
        ],
        "ios": [
          {
            "2024-03": "y"
          }
        ],
        "android": [
          {
            "2024-03": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.3": "u"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ],
        "ios": [
          {
            "2022-07": "y"
          }
        ],
        "android": [
          {
            "2022-07": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-09": "n"
          }
        ],
        "ios": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-09": "n"
          }
        ],
        "ios": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": {
      "1": "Partial. `border-<inline/block>-color` and `border-<inline/block>-width` does not work."
    }
  },
  {
    "slug": "css-border-inline-block-longhand",
    "title": "border-inline & border-block longhand properties",
    "description": "Support for `border-inline` & `border-block` longhand properties.",
    "url": "https://www.caniemail.com/features/css-border-inline-block-longhand/",
    "category": "css",
    "tags": [
      "i18n"
    ],
    "keywords": "border-inline-start-color, border-block-start-color, border-inline-start-style, border-block-start-style, border-inline-start-width, border-block-start-width, border-inline-end-color, border-block-end-color, border-inline-end-style, border-block-end-style, border-inline-end-width, border-block-end-width",
    "last_test_date": "2022-07-14",
    "test_url": "https://www.caniemail.com/tests/css-border-logical-properties.html",
    "test_results_url": "https://testi.at/proj/1yxFDAGtwrUmbf4tzMTY",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.12": "n"
          },
          {
            "10.13": "n"
          },
          {
            "10.15": "y"
          },
          {
            "11": "y"
          },
          {
            "12": "y"
          }
        ],
        "ios": [
          {
            "11": "n"
          },
          {
            "12": "y"
          },
          {
            "13": "y"
          },
          {
            "14": "y"
          },
          {
            "15": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2022-07": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ],
        "ios": [
          {
            "2022-07": "u"
          }
        ],
        "android": [
          {
            "2022-07": "u"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          },
          {
            "2021": "n"
          }
        ],
        "windows-mail": [
          {
            "2022-07": "n"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "10": "y"
          },
          {
            "11": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2024-03": "y"
          }
        ],
        "ios": [
          {
            "2024-03": "y"
          }
        ],
        "android": [
          {
            "2024-03": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.3": "u"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ],
        "ios": [
          {
            "2022-07": "y"
          }
        ],
        "android": [
          {
            "2022-07": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-09": "n"
          }
        ],
        "ios": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-09": "n"
          }
        ],
        "ios": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": null
  },
  {
    "slug": "css-border-inline-block",
    "title": "border-inline & border-block",
    "description": "Support for the `border-inline` and `border-block` shorthand properties.",
    "url": "https://www.caniemail.com/features/css-border-inline-block/",
    "category": "css",
    "tags": [
      "i18n"
    ],
    "keywords": "border-inline, border-block",
    "last_test_date": "2022-07-13",
    "test_url": "https://www.caniemail.com/tests/css-border-logical-properties.html",
    "test_results_url": "https://testi.at/proj/1yxFDAGtwrUmbf4tzMTY",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.15": "n"
          },
          {
            "11": "y"
          },
          {
            "12": "y"
          }
        ],
        "ios": [
          {
            "13": "n"
          },
          {
            "14": "n"
          },
          {
            "15": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2022-07": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ],
        "ios": [
          {
            "2022-07": "u"
          }
        ],
        "android": [
          {
            "2022-07": "u"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          },
          {
            "2021": "n"
          }
        ],
        "windows-mail": [
          {
            "2022-07": "n"
          }
        ],
        "macos": [
          {
            "2011": "n"
          },
          {
            "2016": "n"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "10": "n"
          },
          {
            "11": "n"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2024-03": "y"
          }
        ],
        "ios": [
          {
            "2024-03": "y"
          }
        ],
        "android": [
          {
            "2024-03": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.3": "u"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2022-07": "n"
          }
        ],
        "ios": [
          {
            "2022-07": "n"
          }
        ],
        "android": [
          {
            "2022-07": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ],
        "ios": [
          {
            "2022-07": "y"
          }
        ],
        "android": [
          {
            "2022-07": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2022-07": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2022-07": "u"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-09": "n"
          }
        ],
        "ios": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-09": "n"
          }
        ],
        "ios": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-09": "y"
          }
        ],
        "android": [
          {
            "2022-09": "y"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": null
  },
  {
    "slug": "css-border-radius-logical",
    "title": "border-radius logical properties",
    "description": "Support for border radius logical properties",
    "url": "https://www.caniemail.com/features/css-border-radius-logical/",
    "category": "css",
    "tags": [
      "i18n"
    ],
    "keywords": "border-start-start-radius, border-start-end-radius, border-end-start-radius, border-end-end-radius",
    "last_test_date": "2022-08-16",
    "test_url": "https://www.caniemail.com/tests/css-border-logical-properties.html",
    "test_results_url": "https://testi.at/proj/1yxFDAGtwrUmbf4tzMTY",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.15": "n"
          },
          {
            "11": "n"
          },
          {
            "12": "y"
          }
        ],
        "ios": [
          {
            "13": "n"
          },
          {
            "14": "n"
          },
          {
            "15": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2022-08": "n"
          }
        ],
        "ios": [
          {
            "2022-08": "n"
          }
        ],
        "android": [
          {
            "2022-08": "n"
          }
        ],
        "mobile-webmail": [
          {
            "2022-08": "n"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2022-08": "u"
          }
        ],
        "ios": [
          {
            "2022-08": "u"
          }
        ],
        "android": [
          {
            "2022-08": "u"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2013": "n"
          },
          {
            "2016": "n"
          },
          {
            "2019": "n"
          },
          {
            "2021": "n"
          }
        ],
        "windows-mail": [
          {
            "2022-08": "n"
          }
        ],
        "macos": [
          {
            "2011": "n"
          },
          {
            "2016": "n"
          },
          {
            "16.80": "n"
          }
        ],
        "outlook-com": [
          {
            "2022-08": "n"
          }
        ],
        "ios": [
          {
            "2022-08": "n"
          }
        ],
        "android": [
          {
            "2022-08": "n"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "10": "n"
          },
          {
            "11": "n"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2024-03": "y"
          }
        ],
        "ios": [
          {
            "2024-03": "y"
          }
        ],
        "android": [
          {
            "2024-03": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.3": "u"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2022-08": "n"
          }
        ],
        "ios": [
          {
            "2022-08": "n"
          }
        ],
        "android": [
          {
            "2022-08": "n"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2022-08": "n"
          }
        ],
        "ios": [
          {
            "2022-08": "n"
          }
        ],
        "android": [
          {
            "2022-08": "n"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2022-08": "y"
          }
        ],
        "ios": [
          {
            "2022-08": "y"
          }
        ],
        "android": [
          {
            "2022-08": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2022-08": "u"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2022-08": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2022-08": "u"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2022-08": "u"
          }
        ]
      }
    },
    "notes": null,
    "notes_by_num": null
  },
  {
    "slug": "css-border-radius",
    "title": "border-radius",
    "description": "The `border-radius` CSS property rounds the corners of an element's outer border edge.",
    "url": "https://www.caniemail.com/features/css-border-radius/",
    "category": "css",
    "tags": [],
    "keywords": "rounded corners",
    "last_test_date": "2021-03-09",
    "test_url": "https://www.caniemail.com/tests/css-border-radius.html",
    "test_results_url": "https://app.emailonacid.com/app/acidtest/6baogXZwm2BzrRxpjQq0z7QrcfjJQjQa2sLYKhIJSg2sh/list",
    "stats": {
      "apple-mail": {
        "macos": [
          {
            "10.3": "y"
          }
        ],
        "ios": [
          {
            "10.3": "y"
          },
          {
            "12.2": "y"
          }
        ]
      },
      "gmail": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ],
        "mobile-webmail": [
          {
            "2020-02": "y"
          }
        ]
      },
      "orange": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          },
          {
            "2021-03": "n"
          },
          {
            "2024-04": "n"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          },
          {
            "2024-04": "n"
          }
        ]
      },
      "outlook": {
        "windows": [
          {
            "2003": "n #1"
          },
          {
            "2007": "n #1"
          },
          {
            "2010": "n #1"
          },
          {
            "2013": "n #1"
          },
          {
            "2016": "n #1"
          },
          {
            "2019": "n #1"
          }
        ],
        "windows-mail": [
          {
            "2020-01": "n #1"
          }
        ],
        "macos": [
          {
            "2011": "y"
          },
          {
            "2016": "y"
          },
          {
            "16.80": "y"
          }
        ],
        "outlook-com": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "samsung-email": {
        "android": [
          {
            "6.1.31.2": "y"
          }
        ]
      },
      "sfr": {
        "desktop-webmail": [
          {
            "2019-08": "y"
          }
        ],
        "ios": [
          {
            "2019-08": "y"
          }
        ],
        "android": [
          {
            "2019-08": "y"
          }
        ]
      },
      "thunderbird": {
        "macos": [
          {
            "60.3": "y"
          }
        ]
      },
      "aol": {
        "desktop-webmail": [
          {
            "2021-02": "a #2"
          }
        ],
        "ios": [
          {
            "2021-03": "a #2"
          }
        ],
        "android": [
          {
            "2021-03": "a #2"
          }
        ]
      },
      "yahoo": {
        "desktop-webmail": [
          {
            "2021-02": "a #2"
          }
        ],
        "ios": [
          {
            "2021-03": "a #2"
          }
        ],
        "android": [
          {
            "6.18.2.1529859": "a #2"
          }
        ]
      },
      "protonmail": {
        "desktop-webmail": [
          {
            "2020-03": "y"
          }
        ],
        "ios": [
          {
            "2020-03": "y"
          }
        ],
        "android": [
          {
            "2020-03": "y"
          }
        ]
      },
      "hey": {
        "desktop-webmail": [
          {
            "2020-06": "y"
          }
        ]
      },
      "mail-ru": {
        "desktop-webmail": [
          {
            "2020-10": "y"
          }
        ]
      },
      "fastmail": {
        "desktop-webmail": [
          {
            "2021-07": "y"
          }
        ]
      },
      "laposte": {
        "desktop-webmail": [
          {
            "2021-08": "y"
          }
        ]
      },
      "gmx": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "web-de": {
        "desktop-webmail": [
          {
            "2022-06": "n"
          }
        ],
        "ios": [
          {
            "2022-06": "y"
          }
        ],
        "android": [
          {
            "2022-06": "y"
          }
        ]
      },
      "ionos-1and1": {
        "desktop-webmail": [
          {
            "2022-06": "y"
          }
```

---

## Overview

This is a JavaScript/TypeScript file. It appears to be a React component or React-related module. It contains named exports. 

---

## Detailed Analysis

### Functions

The following functions are defined in this file:

- `nicenames()`

### Dependencies

This file imports/requires:

- `./check-compatibility`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 200

- `AV1`
- `Account`
- `Additional`
- `Adds`
- `Adjacent`
- `AhzTJnsoWULAInwe2B8h7uzlsa6vGOgAkVK1VA6BbuKaW`
- `All`
- `Alpha`
- `Anchor`
- `Android`
- `Animated`
- `Animation`
- `Apple`
- `Applies`
- `Areas`
- `Asian`
- `Assets`
- `Attribute`
- `BG3iM7ZhOjpi8Qlf4E9IQxg`
- `Background`
- `Base`
- `Big`
- `Blockquote`
- `Brand`
- `Buggy`
- `Bzyzx8Z5Kvlfib1Fw9Ted8xtPE26RcjPSdUobdUywgJVm`
- `C1W5YvmzphKLen2MeUNiYUoXRfk5w8WHKlhnXU7zWqJ7H`
- `CAMb612bxbVwRWPhM4wZKNhhdcdkNxj0Rj6dtRRw6LQUO`
- `CBhafIa5yXDRKQKbV442rVFISXim84wMgXaoCqVFD8VTe`
- `CSS2`
- `Cannot`
- `Chaining`
- `Changes`
- `Child`
- `Chrome`
- `Clicking`
- `Code`
- `Comment`
- `Content`
- `Controls`
- `Converts`
- `Copy`
- `Creates`
- `Currently`
- `Cursor`
- `Custom`
- `Cw4skDHvaihUbRGS21mmXSnyxfjIQQNAMGfRwXlpf6zR7`
- `Data`
- `Defines`
- `Depends`
- `Descendant`
- `Desktop`
- `Determines`
- `DhTRmGsVH6uobU4pHD3CasJywfBL4HnEjA1LOF8f9ctso`
- `Displays`
- `DkqbHs69ek5UnK6uhZ7Uj0n5GVQNTP4Z1FvgXvnKyEoTM`
- `Doesn`
- `E45AW3a9IiIhUSBpv3dc1qPfMiMN8mLepy5BsvqtpXhhy`
- `E87UgpgtlXxt6Rsx4Ec1pcxm`
- `Each`
- `East`
- `Edge`
- `Element`
- `Elements`
- `Email`
- `Embedded`
- `Enables`
- `Equivalent`
- `Every`
- `Ew5f99Cy8NuRM0iPMVFoyYI8`
- `Explorer`
- `Fastmail`
- `Firefox`
- `Flow`
- `Fonts`
- `Free`
- `Full`
- `FvYneb1dhiR4we6rAOf4AC02oFa6ksA0sTWxbEjgmt6Mg`
- `Fykm4EjEiDat8FSTWcKYdh26kFWklJuyERBKIsasMB2VH`
- `G4YtBn8fBxEsLx6uybqcxD`
- `G4buV6sBBxUr6quykrtVA3sk`
- `General`
- `Gmail`
- `Google`
- `Gradients`
- `Grouping`
- `HTML5`
- `Hard`
- `Hotmail`
- `IExyoVbvCeJfhRfY6W30e6k4MCsSprSAk58zyNlPlms39`
- `Identification`
- `Image`
- `Images`
- `Indicates`
- `Indicators`
- `Ingjv4scPnWSgh0u0Fr7EctmGksq4DyF7Pw9PQcENfZ37`
- `Inline`
- `Interacting`
- `Internet`
- `IulqGoKCPriLhe6DbI1dWmF2AjH535vSIujVufxhenXVC`
- `JEyxyPfKHFZCPKxlgiOugpH4lyNrXX39cd9M8xaW1DojH`
- `JOOcrJZc0YcjDSZQRFP0OTlYXcw`
- `JU58WeEpop755UWcHt3uqkXW8btkk44WIkzhtL1UU3p46`
- `Kw9bvIPLsmmwVoXhbXpIu1FM31v4nV2KXMaEvPQPezSO9`
- `LAzSmlkimAnFmnrtPjPuPjpT1rO`
- `LaPoste`
- `Lai13xyIE95H6jo1BBs6ay0f3RvJdPL344S3j3M7FbeU4`
- `Lets`
- `Level`
- `Litmus`
- `Local`
- `Logical`
- `Longhand`
- `LxplTmJT9Ilq9GUyn8Aq8MVK6EO427qmx1Ic4A7jc7bOJ`
- `M1w9fKYqtXsrlJ2mlElp9b2RoSd7lDcWwftkDazPgy4hm`
- `MBJ7UfOQ1sVRvPBJNsWByvymNSwrIhi2drpCo4gTw0oM0`
- `MOk8g8TWwCTL4vLGrdMIgu3Vncqdxif6KlK4g8HfUV1mB`
- `MP4`
- `MacOS`
- `Mail`
- `Matches`
- `Message`
- `Microsoft`
- `Mixed`
- `Mobile`
- `Modern`
- `Mozilla`
- `Multiple`
- `Must`
- `Mv0IO0vs3vTgRQuJ8IzyBfD6`
- `N3bgM8CXDd1TNWZzO65F0RkiJwugaAuNYr8mvcYt1C3Da`
- `Negative`
- `Nested`
- `Nesting`
- `No78GouZXTsxEZCD6z4Hn2frAvg3tHBw1SRAP8SwPKsZ5`
- `Non`
- `O0yCP6t6l3sZ1xFrLZuEx6I5O`
- `O5rtNMDHo58i8YirVtvyUvG`
- `OAnjtSK1hEGcC3V9Q30mzIU8xKXIqwNq0M4lZywGOhQIn`
- `Office`
- `Only`
- `Opening`
- `Opens`
- `Orange`
- `Others`
- `Otherwise`
- `Outlook`
- `OyakEYuRTOxGB2hvK9C0F3lsjxpwtUJXZJPrixqyF8gEI`
- `POu1Ixvy9x2XUtzmwlFPA4Lx8DDVhRpGvraSjEmf9DnDG`
- `Partial`
- `Partially`
- `Percentage`
- `Percentages`
- `Policy`
- `Prevents`
- `Preview`
- `Properties`
- `Property`
- `ProtonMail`
- `QZ5ik13cllxUNqjfEBQf9JrI5E`
- `R6niSqR1SM`
- `RainLoop`
- `Refer`
- `Referencing`
- `Removed`
- `Removes`
- `Renders`
- `Replaced`
- `Replaces`
- `Represents`
- `Required`
- `Requires`
- `Rg26n7zpfSw6bcxjGdDU9eF0aieX8XR7QoXfSfjbOEKXt`
- `Rk9H1m9ubAYH1DwUqZu8G`
- `RlRYNGDjVNBhofxCNxloUcRbUVWGDhJ2kZ4fy6HXpEatH`
- `Roboto`
- `Roman`
- `Round`
- `RoundRect`
- `Safari`
- `Samsung`
- `Sans`
- `Screen`
- `Security`
- `See`
- `Selecting`
- `Selects`
- `Sets`
- `Setting`
- `Shorthand`
- `Show`
- `Sizes`
- `Sonoma`
- `Specifies`
- `Styles`
- `Support`
- `SupportEntry`
- `Supported`
- `Supports`
- `Targeted`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

