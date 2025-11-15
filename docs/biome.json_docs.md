# Documentation: biome.json
**File Path:** `biome.json`
**Language:** json
**Size:** 2,506 bytes
**Lines:** 101
**Generated:** 2025-11-15T20:37:31.333891Z

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

- **Path:** `biome.json`
- **Name:** `biome.json`
- **Extension:** `.json`
- **Language:** json
- **Size:** 2,506 bytes (2.45 KB)
- **Lines of Code:** 101

---

## Original Source

```json
{
  "$schema": "./node_modules/@biomejs/biome/configuration_schema.json",
  "assist": {
    "actions": {
      "source": {
        "organizeImports": "on"
      }
    }
  },
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": false
  },
  "formatter": {
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 80
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "single"
    }
  },
  "linter": {
    "enabled": true,
    "rules": {
      "style": {
        "noNonNullAssertion": "off",
        "useLiteralEnumMembers": "error",
        "useNodejsImportProtocol": "error",
        "useAsConstAssertion": "error",
        "useEnumInitializers": "error",
        "useSelfClosingElements": "error",
        "useConst": "error",
        "useSingleVarDeclarator": "error",
        "noUnusedTemplateLiteral": "error",
        "useNumberNamespace": "error",
        "noInferrableTypes": "error",
        "useExponentiationOperator": "error",
        "useTemplate": "error",
        "noParameterAssign": "error",
        "useDefaultParameterLast": "error",
        "useImportType": "error",
        "useExportType": "error",
        "noUselessElse": "error",
        "useShorthandFunctionType": "error"
      },
      "performance": {
        "noDelete": "off"
      },
      "a11y": {
        "noStaticElementInteractions": "off",
        "noSvgWithoutTitle": "off",
        "noAutofocus": "off"
      },
      "correctness": {
        "noUnusedImports": "warn",
        "useExhaustiveDependencies": "off",
        "useJsxKeyInIterable": "off",
        "noChildrenProp": "off"
      },
      "nursery": {
        "useSortedClasses": "off"
      },
      "complexity": {
        "useNumericLiterals": "error",
        "noUselessFragments": "off",
        "noForEach": "off",
        "noCommaOperator": "error",
        "noArguments": "error"
      },
      "suspicious": {
        "noArrayIndexKey": "off",
        "noExplicitAny": "off",
        "noUnknownAtRules": "off",
        "noAssignInExpressions": "off"
      },
      "security": {
        "noDangerouslySetInnerHtml": "off"
      }
    }
  },
  "files": {
    "includes": [
      "**",
      "!**/dist",
      "!**/pnpm-lock.yaml",
      "!**/.next",
      "!**/public",
      "!packages/preview-server/src/actions/email-validation/caniemail-data.ts",
      "!**/.react-email/**/*",
      "!**/node_modules/**/*",
      "!**/*.d.ts",
      "!**/out",
      "!**/.turbo",
      "!**/prism.ts"
    ]
  }
}

```

---

## Overview

This is a JSON configuration or data file. 

---

## Detailed Analysis

---

## Keywords & Identifiers

**Total Unique Identifiers:** 94

- `a11y`
- `actions`
- `assist`
- `biome`
- `biomejs`
- `caniemail`
- `clientKind`
- `complexity`
- `configuration_schema`
- `correctness`
- `data`
- `dist`
- `email`
- `enabled`
- `error`
- `files`
- `formatter`
- `git`
- `includes`
- `indentStyle`
- `indentWidth`
- `javascript`
- `json`
- `lineWidth`
- `linter`
- `lock`
- `next`
- `noArguments`
- `noArrayIndexKey`
- `noAssignInExpressions`
- `noAutofocus`
- `noChildrenProp`
- `noCommaOperator`
- `noDangerouslySetInnerHtml`
- `noDelete`
- `noExplicitAny`
- `noForEach`
- `noInferrableTypes`
- `noNonNullAssertion`
- `noParameterAssign`
- `noStaticElementInteractions`
- `noSvgWithoutTitle`
- `noUnknownAtRules`
- `noUnusedImports`
- `noUnusedTemplateLiteral`
- `noUselessElse`
- `noUselessFragments`
- `node_modules`
- `nursery`
- `off`
- `organizeImports`
- `out`
- `packages`
- `performance`
- `pnpm`
- `preview`
- `prism`
- `public`
- `quoteStyle`
- `react`
- `rules`
- `schema`
- `security`
- `server`
- `single`
- `source`
- `space`
- `src`
- `style`
- `suspicious`
- `turbo`
- `useAsConstAssertion`
- `useConst`
- `useDefaultParameterLast`
- `useEnumInitializers`
- `useExhaustiveDependencies`
- `useExponentiationOperator`
- `useExportType`
- `useIgnoreFile`
- `useImportType`
- `useJsxKeyInIterable`
- `useLiteralEnumMembers`
- `useNodejsImportProtocol`
- `useNumberNamespace`
- `useNumericLiterals`
- `useSelfClosingElements`
- `useShorthandFunctionType`
- `useSingleVarDeclarator`
- `useSortedClasses`
- `useTemplate`
- `validation`
- `vcs`
- `warn`
- `yaml`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

