# Documentation: read-stream.spec.ts
**File Path:** `packages/render/src/node/read-stream.spec.ts`
**Language:** typescript
**Size:** 6,135 bytes
**Lines:** 192
**Generated:** 2025-11-15T20:37:31.506918Z

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

- **Path:** `packages/render/src/node/read-stream.spec.ts`
- **Name:** `read-stream.spec.ts`
- **Extension:** `.ts`
- **Language:** typescript
- **Size:** 6,135 bytes (5.99 KB)
- **Lines of Code:** 192

---

## Original Source

```typescript
import { Readable } from 'node:stream';
import { describe, expect, it } from 'vitest';
import { readStream } from './read-stream';

describe('readStream', () => {
  describe('multi-byte character handling', () => {
    it('correctly decodes Japanese characters split across chunks', async () => {
      // Create a string with Japanese text that will be split across chunks
      const japaneseText = 'これはテストです。スケジュール確認をお願いします。';
      const buffer = Buffer.from(japaneseText, 'utf-8');

      // Split the buffer at a position that would break a multi-byte character
      // "ス" in UTF-8 is E3 82 B9, let's split after E3 82
      const splitPosition = buffer.indexOf(Buffer.from('スケジュール')) + 2;

      // Create chunks that split the character
      const chunk1 = buffer.slice(0, splitPosition);
      const chunk2 = buffer.slice(splitPosition);

      // Create a mock PipeableStream that emits our chunks
      const mockStream = new Readable({
        read() {
          if (this.chunkIndex === 0) {
            this.push(chunk1);
            this.chunkIndex++;
          } else if (this.chunkIndex === 1) {
            this.push(chunk2);
            this.chunkIndex++;
          } else {
            this.push(null); // End the stream
          }
        },
      });
      mockStream.chunkIndex = 0;

      // Add pipe method to match PipeableStream interface
      const pipeableStream = {
        pipe: (writable: any) => mockStream.pipe(writable),
      };

      const result = await readStream(pipeableStream as any);

      // The result should match the original text without corruption
      expect(result).toBe(japaneseText);
      expect(result).not.toContain('\0'); // No null characters
      expect(result).toContain('スケジュール'); // Full word intact
    });

    it('handles Chinese characters split across chunks', async () => {
      const chineseText = '这是一个测试。请确认您的日程安排。';
      const buffer = Buffer.from(chineseText, 'utf-8');

      // Split in the middle of a Chinese character
      const splitPosition = buffer.indexOf(Buffer.from('日程')) + 1;

      const chunk1 = buffer.slice(0, splitPosition);
      const chunk2 = buffer.slice(splitPosition);

      const mockStream = new Readable({
        read() {
          if (this.chunkIndex === 0) {
            this.push(chunk1);
            this.chunkIndex++;
          } else if (this.chunkIndex === 1) {
            this.push(chunk2);
            this.chunkIndex++;
          } else {
            this.push(null);
          }
        },
      });
      mockStream.chunkIndex = 0;

      const pipeableStream = {
        pipe: (writable: any) => mockStream.pipe(writable),
      };

      const result = await readStream(pipeableStream as any);

      expect(result).toBe(chineseText);
      expect(result).not.toContain('\0');
      expect(result).toContain('日程');
    });

    it('handles emoji characters split across chunks', async () => {
      const emojiText = 'Hello 👋 World 🌍 Test 🚀';
      const buffer = Buffer.from(emojiText, 'utf-8');

      // Emojis are 4-byte UTF-8 sequences, split one
      const rocketEmoji = Buffer.from('🚀');
      const splitPosition = buffer.indexOf(rocketEmoji) + 2; // Split in middle of rocket emoji

      const chunk1 = buffer.slice(0, splitPosition);
      const chunk2 = buffer.slice(splitPosition);

      const mockStream = new Readable({
        read() {
          if (this.chunkIndex === 0) {
            this.push(chunk1);
            this.chunkIndex++;
          } else if (this.chunkIndex === 1) {
            this.push(chunk2);
            this.chunkIndex++;
          } else {
            this.push(null);
          }
        },
      });
      mockStream.chunkIndex = 0;

      const pipeableStream = {
        pipe: (writable: any) => mockStream.pipe(writable),
      };

      const result = await readStream(pipeableStream as any);

      expect(result).toBe(emojiText);
      expect(result).not.toContain('\0');
      expect(result).toContain('🚀');
    });

    it('handles many small chunks with multi-byte characters', async () => {
      const mixedText = 'Test テスト 测试 Тест מבחן';
      const buffer = Buffer.from(mixedText, 'utf-8');

      // Create many small chunks (3 bytes each)
      const chunks: Buffer[] = [];
      for (let i = 0; i < buffer.length; i += 3) {
        chunks.push(buffer.slice(i, Math.min(i + 3, buffer.length)));
      }

      let currentChunk = 0;
      const mockStream = new Readable({
        read() {
          if (currentChunk < chunks.length) {
            this.push(chunks[currentChunk]);
            currentChunk++;
          } else {
            this.push(null);
          }
        },
      });

      const pipeableStream = {
        pipe: (writable: any) => mockStream.pipe(writable),
      };

      const result = await readStream(pipeableStream as any);

      expect(result).toBe(mixedText);
      expect(result).not.toContain('\0');
      expect(result).toContain('テスト');
      expect(result).toContain('测试');
      expect(result).toContain('Тест');
      expect(result).toContain('מבחן');
    });
  });

  describe('ReadableStream (pipeTo) path', () => {
    it('handles multi-byte characters with ReadableStream', async () => {
      const japaneseText = 'バクラクのメールテンプレートでスケジュール確認';
      const buffer = Buffer.from(japaneseText, 'utf-8');

      // Split at a position that breaks a character
      const splitPosition = buffer.indexOf(Buffer.from('スケジュール')) + 2;
      const chunk1 = buffer.slice(0, splitPosition);
      const chunk2 = buffer.slice(splitPosition);

      // Mock a ReactDOMServerReadableStream
      const chunks = [chunk1, chunk2];

      const mockReadableStream = {
        pipeTo: async (writable: WritableStream) => {
          const writer = writable.getWriter();

          for (const chunk of chunks) {
            await writer.write(chunk);
          }

          await writer.close();
        },
      };

      const result = await readStream(mockReadableStream as any);

      expect(result).toBe(japaneseText);
      expect(result).not.toContain('\0');
      expect(result).toContain('スケジュール');
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

- `buffer()`
- `chineseText()`
- `chunk1()`
- `chunk2()`
- `chunks()`
- `currentChunk()`
- `emojiText()`
- `i()`
- `japaneseText()`
- `mixedText()`
- `mockReadableStream()`
- `mockStream()`
- `pipeableStream()`
- `result()`
- `rocketEmoji()`
- `splitPosition()`
- `writer()`

### Dependencies

This file imports/requires:

- `./read-stream`
- `node:stream`
- `vitest`

---

## Keywords & Identifiers

**Total Unique Identifiers:** 95

- `Add`
- `Buffer`
- `Chinese`
- `Create`
- `Emojis`
- `End`
- `Full`
- `Hello`
- `Japanese`
- `Math`
- `Mock`
- `PipeableStream`
- `ReactDOMServerReadableStream`
- `Readable`
- `ReadableStream`
- `Split`
- `Test`
- `World`
- `WritableStream`
- `across`
- `after`
- `any`
- `breaks`
- `buffer`
- `byte`
- `bytes`
- `character`
- `characters`
- `chineseText`
- `chunk`
- `chunk1`
- `chunk2`
- `chunkIndex`
- `chunks`
- `close`
- `correctly`
- `corruption`
- `currentChunk`
- `decodes`
- `describe`
- `each`
- `emits`
- `emoji`
- `emojiText`
- `expect`
- `getWriter`
- `handles`
- `handling`
- `indexOf`
- `intact`
- `interface`
- `japaneseText`
- `length`
- `many`
- `match`
- `method`
- `middle`
- `min`
- `mixedText`
- `mock`
- `mockReadableStream`
- `mockStream`
- `multi`
- `node`
- `one`
- `original`
- `our`
- `path`
- `pipe`
- `pipeTo`
- `pipeableStream`
- `position`
- `push`
- `read`
- `readStream`
- `result`
- `rocket`
- `rocketEmoji`
- `sequences`
- `slice`
- `small`
- `split`
- `splitPosition`
- `stream`
- `string`
- `text`
- `toBe`
- `toContain`
- `utf`
- `vitest`
- `without`
- `word`
- `writable`
- `write`
- `writer`

---

## Related Files

*Related files analysis would require cross-referencing imports and exports across the codebase.*

