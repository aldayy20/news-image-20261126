// news-image-20261126 — entrypoint (Node 22, standard library only).
//
// The entry's image is entry.png beside this file: a 1024x1024 poster
// drawn by render.py from the real news of Thursday 26 November 2026
// (Taiwan holds its 15% US tariff rate after Trump's new salvo at 14
// trading partners, Macy's Thanksgiving Day Parade pushed to Saturday
// by storm winds, F-15EX fighters unveiled at Kadena, Flipkart's chief
// steps down, Kenya's 293,600 Saudi jobs, Gukesh–Sindarov Game 3 in
// Geneva, Champions League Wednesday-night results).
//
// This program copies that image to $MAKEFUN_OUTPUT_DIR/entry.png.
// It reads nothing else, reaches no network, and writes the same bytes
// on every run: a plain copy of a fixed file.
//
// Run it locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const MAX_BYTES = 1048576; // 1 MiB, the bounty gate
const MAX_PIXELS = 1024; // 1024 by 1024 at most

function fail(message: string): never {
  console.error(`news-image-20261126: ${message}`);
  process.exit(1);
}

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

if (!existsSync(source)) fail(`missing ${source}`);
const bytes = readFileSync(source);
if (bytes.length > MAX_BYTES) fail(`entry.png is ${bytes.length} bytes, over ${MAX_BYTES}`);
if (bytes.length < 33 || bytes[0] !== 0x89 || bytes[1] !== 0x50 || bytes[2] !== 0x4e || bytes[3] !== 0x47) {
  fail("entry.png is not a PNG (bad magic bytes)");
}
if (bytes.toString("ascii", 12, 16) !== "IHDR") fail("entry.png has no IHDR chunk");
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width > MAX_PIXELS || height > MAX_PIXELS) {
  fail(`entry.png is ${width}x${height}, over ${MAX_PIXELS}x${MAX_PIXELS}`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
if (statSync(target).size !== bytes.length) fail("copy mismatch: target size differs");
console.log(`news-image-20261126: wrote ${target} (${width}x${height}, ${bytes.length} bytes)`);
