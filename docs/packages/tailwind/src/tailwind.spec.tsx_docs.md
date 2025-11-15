# Documentation: tailwind.spec.tsx
**File Path:** `packages/tailwind/src/tailwind.spec.tsx`
**Language:** tsx
**Size:** 17,801 bytes
**Lines:** 651
**Generated:** 2025-11-15T20:37:32.397874Z

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

- **Path:** `packages/tailwind/src/tailwind.spec.tsx`
- **Name:** `tailwind.spec.tsx`
- **Extension:** `.tsx`
- **Language:** tsx
- **Size:** 17,801 bytes (17.38 KB)
- **Lines of Code:** 651

---

## Original Source

```tsx
import { Button } from '@react-email/button';
import { Head } from '@react-email/head';
import { Heading } from '@react-email/heading';
import { Hr } from '@react-email/hr';
import { Html } from '@react-email/html';
import { Link } from '@react-email/link';
import { pretty, render } from '@react-email/render';
import { ResponsiveColumn, ResponsiveRow } from '@responsive-email/react-email';
import React from 'react';
import type { TailwindConfig } from '.';
import { Tailwind } from '.';

describe('Tailwind component', () => {
  it('allows for complex children manipulation', async () => {
    const actualOutput = await render(
      <Tailwind>
        <ResponsiveRow>
          <ResponsiveColumn>This is the first column</ResponsiveColumn>
          <ResponsiveColumn>This is the second column</ResponsiveColumn>
        </ResponsiveRow>
      </Tailwind>,
    );
    expect(actualOutput).toMatchSnapshot();
  });

  it('works with blocklist', async () => {
    const actualOutput = await render(
      <Tailwind
        config={{
          blocklist: ['bg-blue-600'],
        }}
      >
        <Head />
        <body>
          <button type="button" className="bg-blue-600 md:p-4">
            Click me
          </button>
        </body>
      </Tailwind>,
      { pretty: true },
    );

    expect(actualOutput).toMatchSnapshot();
  });

  it('works with shadows', async () => {
    expect(
      await render(
        <Tailwind>
          <div className="shadow-[#555] shadow">shadow around here</div>
        </Tailwind>,
      ).then(pretty),
    ).toMatchSnapshot();
  });

  it('works with class manipulation done on components', async () => {
    const MyComponnt = (props: {
      className?: string;
      style?: React.CSSProperties;
    }) => {
      expect(
        props.style,
        'styles should not be generated for a component',
      ).toBeUndefined();
      expect(props.className).toBe('p-4 text-blue-400');
      return (
        <div
          className={`${props.className} bg-red-500`}
          style={{ ...props.style, padding: '4px' }}
        />
      );
    };

    expect(
      await render(
        <Tailwind>
          <MyComponnt className="p-4 text-blue-400" />
        </Tailwind>,
      ),
    ).toMatchSnapshot();
  });

  it("works properly with 'no-underline'", async () => {
    const actualOutput = await render(
      <Html>
        <body>
          <Tailwind>
            <p className="text-[14px] text-black leading-[24px]">
              or copy and paste this URL into your browser:{' '}
              <Link
                className="other text-blue-600 no-underline"
                href="https://react.email"
              >
                https://react.email
              </Link>
            </p>
            <p className="text-[14px] text-black leading-[24px]">
              or copy and paste this URL into your browser:{' '}
              <Link
                className="text-blue-600 no-underline"
                href="https://react.email"
              >
                https://react.email
              </Link>
            </p>
          </Tailwind>
        </body>
      </Html>,
    );
    expect(actualOutput).toMatchSnapshot();
  });

  it('renders children with inline Tailwind styles', async () => {
    const actualOutput = await render(
      <Tailwind>
        <div className="bg-white" />
      </Tailwind>,
    );

    expect(actualOutput).toMatchSnapshot();
  });

  test('<Button className="px-3 py-2 mt-8 text-sm text-gray-200 bg-blue-600 rounded-md">', async () => {
    const actualOutput = await render(
      <Tailwind>
        <Button className="mt-8 rounded-md bg-blue-600 px-3 py-2 text-gray-200 text-sm">
          Testing button
        </Button>
        Testing
      </Tailwind>,
    );

    expect(actualOutput).toMatchSnapshot();
  });

  it('works with custom components with fragment at the root', async () => {
    const Wrapper = (props: { children: React.ReactNode }) => {
      return <Tailwind>{props.children}</Tailwind>;
    };

    const Brand = () => {
      return (
        <>
          <div className="p-[20px]">
            <p className="font-bold text-[50px]">React Email</p>
          </div>
          <div className="p-[20px]">
            <p className="font-bold text-[50px]">React Email</p>
          </div>
        </>
      );
    };

    const EmailTemplate = () => {
      return (
        <Wrapper>
          <div className="mt-[100px] text-[50px] leading-[1]">Hello world</div>
          <Brand />
        </Wrapper>
      );
    };

    const actualOutput = await render(EmailTemplate());

    expect(actualOutput).toMatchSnapshot();
  });

  it("doesn't generate styles from text", async () => {
    expect(
      await render(<Tailwind>container bg-red-500 bg-blue-300</Tailwind>),
    ).toMatchSnapshot();
  });

  it('works with components that return children', async () => {
    const Wrapper = (props: { children: React.ReactNode }) => {
      return <Tailwind>{props.children}</Tailwind>;
    };

    const Brand = () => {
      return (
        <div className="p-[20px]">
          <p className="font-bold text-[50px]">React Email</p>
        </div>
      );
    };

    const EmailTemplate = () => {
      return (
        <Wrapper>
          <div className="mt-[100px] text-[50px] leading-[1]">Hello world</div>
          <Brand />
        </Wrapper>
      );
    };

    const actualOutput = await render(EmailTemplate());

    expect(actualOutput).toMatchSnapshot();
  });

  it('works with Heading component', async () => {
    const EmailTemplate = () => {
      return (
        <Tailwind>
          Hello
          <Heading>My testing heading</Heading>
          friends
        </Tailwind>
      );
    };

    expect(await render(<EmailTemplate />)).toMatchSnapshot();
  });

  it('works with components that use React.forwardRef', async () => {
    const Wrapper = (props: { children: React.ReactNode }) => {
      return <Tailwind>{props.children}</Tailwind>;
    };

    const Brand = React.forwardRef<HTMLDivElement>((ref, props) => {
      return (
        <div
          className="p-[20px]"
          ref={ref as React.LegacyRef<HTMLDivElement>}
          {...props}
        >
          <p className="font-bold text-[50px]">React Email</p>
        </div>
      );
    });
    Brand.displayName = 'Brand';

    const EmailTemplate = () => {
      return (
        <Wrapper>
          <div className="mt-[100px] text-[50px] leading-[1]">Hello world</div>
          <Brand />
        </Wrapper>
      );
    };

    const actualOutput = await render(EmailTemplate());

    expect(actualOutput).toMatchSnapshot();
  });

  it('uses background image', async () => {
    const actualOutput = await render(
      <Tailwind>
        <div className="bg-[url(https://example.com/image.png)]" />
      </Tailwind>,
    );

    expect(actualOutput).toMatchSnapshot();
  });

  it('does not override inline styles with Tailwind styles', async () => {
    const actualOutput = await render(
      <Tailwind>
        <div
          className="bg-black text-[16px]"
          style={{ backgroundColor: 'red', fontSize: '12px' }}
        />
      </Tailwind>,
    );

    expect(actualOutput).toMatchSnapshot();
  });

  it('overrides component styles with Tailwind styles', async () => {
    const actualOutput = await render(
      <Tailwind>
        <Hr className="w-12" />
      </Tailwind>,
    );

    expect(actualOutput).toMatchSnapshot();
  });

  it('preserves mso styles', async () => {
    const actualOutput = await render(
      <Html>
        <Tailwind>
          <Head />
          <span
            dangerouslySetInnerHTML={{
              __html: `<!--[if mso]><i style="letter-spacing: 10px;mso-font-width:-100%;" hidden>&nbsp;</i><![endif]-->`,
            }}
          />
          <div className="custom-class bg-white sm:bg-red-50 sm:text-sm md:text-lg" />
        </Tailwind>
      </Html>,
    ).then(pretty);

    expect(actualOutput).toMatchSnapshot();
  });

  it('recognizes custom responsive screen', async () => {
    const actualOutput = await render(
      <Html>
        <Tailwind
          config={{
            theme: {
              screens: {
                sm: { min: '640px' },
                md: { min: '768px' },
                lg: { min: '1024px' },
                xl: { min: '1280px' },
                '2xl': { min: '1536px' },
              },
            },
          }}
        >
          <Head />
          <div className="bg-red-100 xl:bg-green-500">Test</div>
          <div className="2xl:bg-blue-500">Test</div>
        </Tailwind>
      </Html>,
    ).then(pretty);

    expect(actualOutput).toMatchSnapshot();
  });

  it('works with calc() with + sign', async () => {
    const actualOutput = await render(
      <Tailwind>
        <head />
        <div className="max-h-[calc(50px+3rem)] bg-red-100 lg:max-h-[calc(50px+5rem)]">
          <div className="h-[200px]">something tall</div>
        </div>
      </Tailwind>,
    ).then(pretty);

    expect(actualOutput).toMatchSnapshot();
  });

  describe('with non-inlinable styles', () => {
    /*
    This test is because of https://github.com/resend/react-email/issues/1112
    which was being caused because we required to, either have our <Head> component,
    or a <head> element directly inside the <Tailwind> component for media queries to be applied
    onto. The problem with this approach was that the check to see if an element was an instance of
    the <Head> component fails after minification as we did it by the function name.

    The best solution is to check for the Head element on arbitrarily deep levels of the React tree
    and apply the styles there. This also fixes the issue where it would not be allowed to use
    Tailwind classes on the <html> element as the <head> would be required directly bellow Tailwind.
  */
    it('works with arbitrarily deep (in the React tree) <head> elements', async () => {
      expect(
        await render(
          <Tailwind>
            <html lang="en">
              <head />
              <body>
                <div className="bg-red-200 sm:bg-red-300 md:bg-red-400 lg:bg-red-500" />
              </body>
            </html>
          </Tailwind>,
        ).then(pretty),
      ).toMatchSnapshot();

      const MyHead = (props: Record<string, any>) => {
        return <head {...props} />;
      };

      expect(
        await render(
          <Tailwind>
            <html lang="en">
              <MyHead />
              <body>
                <div className="bg-red-200 sm:bg-red-300 md:bg-red-400 lg:bg-red-500" />
              </body>
            </html>
          </Tailwind>,
        ),
      ).toMatchSnapshot();
    });

    it('handles non-inlinable styles in custom utilities', async () => {
      const actualOutput = await render(
        <html lang="en">
          <Tailwind
            config={{
              plugins: [
                {
                  handler: (api) => {
                    api.addUtilities({
                      '.text-body': {
                        '@apply text-[green] sm:text-[darkgreen]': {},
                      },
                    });
                  },
                },
              ],
            }}
          >
            <head />
            <body>
              <div className="text-body" />
            </body>
          </Tailwind>
        </html>,
      ).then(pretty);
      expect(actualOutput).toMatchSnapshot();
    });

    it('adds css to <head/> and keep class names', async () => {
      const actualOutput = await render(
        <html lang="en">
          <Tailwind>
            <head />
            <body>
              <div className="bg-red-200 hover:bg-red-600 focus:bg-red-700 sm:bg-red-300 sm:hover:bg-red-200 md:bg-red-400 lg:bg-red-500" />
            </body>
          </Tailwind>
        </html>,
      ).then(pretty);

      expect(actualOutput).toMatchSnapshot();
    });

    it('throws error when used without the head and with media query class names very deeply nested', async () => {
      const Component1 = (props: Record<string, any>) => {
        return (
          <div {...props} className="h-30 w-40 sm:h-10 sm:w-10">
            {props.children}
          </div>
        );
      };
      const Component2 = (props: Record<string, any>) => {
        return (
          <div {...props}>
            <Component1>{props.children}</Component1>
          </div>
        );
      };
      const Component3 = (props: Record<string, any>) => {
        return (
          <div {...props}>
            <Component2>{props.children}</Component2>
          </div>
        );
      };

      function renderComplexEmailWithoutHead() {
        return render(
          <Tailwind>
            <div className="bg-red-300">
              <Component3 className="random-classname w-full">
                <div className="w-50">Testing</div>
              </Component3>
            </div>
          </Tailwind>,
        );
      }

      await expect(
        renderComplexEmailWithoutHead,
      ).rejects.toThrowErrorMatchingSnapshot();
    });

    it('works with relatively complex media query utilities', async () => {
      const Email = () => {
        return (
          <Tailwind>
            <Head />
            <p className="text-blue-700 max-sm:text-red-600">I am some text</p>
          </Tailwind>
        );
      };

      expect(await render(<Email />).then(pretty)).toMatchSnapshot();
    });

    it('throws an error when used without a <head/>', async () => {
      function noHead() {
        return render(
          <Tailwind>
            <html lang="en">
              {/* <Head></Head> */}
              <div className="bg-red-200 sm:bg-red-500" />
            </html>
          </Tailwind>,
        ).then(pretty);
      }
      await expect(noHead).rejects.toThrowErrorMatchingSnapshot();
    });

    it('persists existing <head/> elements', async () => {
      const actualOutput = await render(
        <html lang="en">
          <Tailwind>
            <head>
              <style />
              <link />
            </head>
            <body>
              <div className="bg-red-200 sm:bg-red-500" />
            </body>
          </Tailwind>
        </html>,
      ).then(pretty);

      expect(actualOutput).toMatchSnapshot();
    });
  });

  describe('with custom theme config', () => {
    it('supports custom colors', async () => {
      const config: TailwindConfig = {
        theme: {
          extend: {
            colors: {
              custom: '#1fb6ff',
            },
          },
        },
      };

      const actualOutput = await render(
        <Tailwind config={config}>
          <div className="bg-custom text-custom" />
        </Tailwind>,
      ).then(pretty);

      expect(actualOutput).toMatchSnapshot();
    });

    it('supports custom fonts', async () => {
      const config: TailwindConfig = {
        theme: {
          extend: {
            fontFamily: {
              sans: ['Graphik', 'sans-serif'],
              serif: ['Merriweather', 'serif'],
            },
          },
        },
      };

      const actualOutput = await render(
        <Tailwind config={config}>
          <div className="font-sans" />
          <div className="font-serif" />
        </Tailwind>,
      ).then(pretty);

      expect(actualOutput).toMatchSnapshot();
    });

    it('supports custom spacing', async () => {
      const config: TailwindConfig = {
        theme: {
          extend: {
            spacing: {
              '8xl': '96rem',
            },
          },
        },
      };
      const actualOutput = await render(
        <Tailwind config={config}>
          <div className="m-8xl" />
        </Tailwind>,
      ).then(pretty);
      expect(actualOutput).toMatchSnapshot();
    });

    it('supports custom border radius', async () => {
      const config: TailwindConfig = {
        theme: {
          extend: {
            borderRadius: {
              '4xl': '2rem',
            },
          },
        },
      };
      const actualOutput = await render(
        <Tailwind config={config}>
          <div className="rounded-4xl" />
        </Tailwind>,
      ).then(pretty);
      expect(actualOutput).toMatchSnapshot();
    });

    it('supports custom text alignment', async () => {
      const config: TailwindConfig = {
        theme: {
          extend: {
            textAlign: {
              justify: 'justify',
            },
          },
        },
      };

      const actualOutput = await render(
        <Tailwind config={config}>
          <div className="text-justify" />
        </Tailwind>,
      ).then(pretty);

      expect(actualOutput).toMatchSnapshot();
    });
  });

  describe('with custom plugins config', () => {
    const config = {
      plugins: [
        {
          handler: (api) => {
            api.addUtilities({
              '.border-custom': {
                border: '2px solid',
              },
            });
          },
        },
      ],
    } satisfies TailwindConfig;

    it('supports custom plugins', async () => {
      const actualOutput = await render(
        <Tailwind config={config}>
          <div className="border-custom" />
        </Tailwind>,
      ).then(pretty);

      expect(actualOutput).toMatchSnapshot();
    });

    it('supports custom plugins with responsive styles', async () => {
      const actualOutput = await render(
        <html lang="en">
          <Tailwind config={config}>
            <head />
            <body>
              <div className="border-custom sm:border-custom" />
            </body>
          </Tailwind>
        </html>,
      ).then(pretty);

      expect(actualOutput).toMatchSnapshot();
    });
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

- `Brand()`
- `Component1()`
- `Component2()`
- `Component3()`
- `Email()`
- `EmailTemplate()`
- `MyComponnt()`
- `MyHead()`
- `Wrapper()`
- `actualOutput()`
- `config()`
- `noHead()`
- `renderComplexEmailWithoutHead()`

### Dependencies

This file imports/requires:

- `.`
- `@react-email/button`
- `@react-email/head`
- `@react-email/heading`
- `@react-email/hr`
- `@react-email/html`
- `@react-email/link`
- `@react-email/render`
- `@responsive-email/react-email`
- `react`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 200

- `Brand`
- `Button`
- `CSSProperties`
- `Click`
- `Component1`
- `Component2`
- `Component3`
- `Email`
- `EmailTemplate`
- `Graphik`
- `HTMLDivElement`
- `Head`
- `Heading`
- `Hello`
- `Html`
- `LegacyRef`
- `Link`
- `Merriweather`
- `MyComponnt`
- `MyHead`
- `React`
- `ReactNode`
- `Record`
- `ResponsiveColumn`
- `ResponsiveRow`
- `Tailwind`
- `TailwindConfig`
- `Test`
- `Testing`
- `Wrapper`
- `__html`
- `actualOutput`
- `addUtilities`
- `adds`
- `after`
- `alignment`
- `allowed`
- `allows`
- `also`
- `any`
- `api`
- `applied`
- `apply`
- `approach`
- `arbitrarily`
- `around`
- `background`
- `backgroundColor`
- `because`
- `bellow`
- `best`
- `black`
- `blocklist`
- `blue`
- `body`
- `bold`
- `border`
- `borderRadius`
- `browser`
- `button`
- `calc`
- `caused`
- `check`
- `children`
- `className`
- `classes`
- `classname`
- `colors`
- `column`
- `com`
- `complex`
- `component`
- `components`
- `config`
- `container`
- `copy`
- `css`
- `custom`
- `dangerouslySetInnerHTML`
- `darkgreen`
- `deep`
- `deeply`
- `describe`
- `directly`
- `displayName`
- `div`
- `doesn`
- `done`
- `either`
- `element`
- `elements`
- `email`
- `endif`
- `error`
- `example`
- `existing`
- `expect`
- `extend`
- `fails`
- `first`
- `fixes`
- `focus`
- `font`
- `fontFamily`
- `fontSize`
- `fonts`
- `forwardRef`
- `fragment`
- `friends`
- `full`
- `generate`
- `generated`
- `github`
- `gray`
- `green`
- `handler`
- `handles`
- `head`
- `heading`
- `here`
- `hidden`
- `hover`
- `href`
- `html`
- `https`
- `image`
- `inlinable`
- `inline`
- `inside`
- `instance`
- `into`
- `issue`
- `issues`
- `justify`
- `keep`
- `lang`
- `leading`
- `letter`
- `levels`
- `link`
- `manipulation`
- `max`
- `media`
- `min`
- `minification`
- `mso`
- `name`
- `names`
- `nbsp`
- `nested`
- `noHead`
- `non`
- `onto`
- `other`
- `our`
- `override`
- `overrides`
- `padding`
- `paste`
- `persists`
- `plugins`
- `png`
- `preserves`
- `pretty`
- `problem`
- `properly`
- `props`
- `queries`
- `query`
- `radius`
- `random`
- `react`
- `recognizes`
- `red`
- `ref`
- `rejects`
- `relatively`
- `render`
- `renderComplexEmailWithoutHead`
- `renders`
- `required`
- `resend`
- `responsive`
- `root`
- `rounded`
- `sans`
- `satisfies`
- `screen`
- `screens`
- `second`
- `see`
- `serif`
- `shadow`
- `shadows`
- `sign`
- `solid`
- `solution`
- `some`
- `something`
- `spacing`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

