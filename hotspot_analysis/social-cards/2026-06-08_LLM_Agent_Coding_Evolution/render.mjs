import { chromium } from 'playwright-core';
import { join, dirname } from 'path';
import { mkdirSync } from 'fs';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const HTML = join(__dirname, 'index.html');
const OUT = join(__dirname, 'output');
mkdirSync(OUT, { recursive: true });

const targets = [
  ['#wechat-21x9',   'wechat-21x9-cover.png'],
  ['#wechat-1x1',    'wechat-1x1-cover.png'],
  ['#wechat-pair-preview', 'wechat-cover-pair-preview.png'],
];

const browser = await chromium.launch({
  executablePath: '/opt/microsoft/msedge/msedge',
  headless: true,
  args: ['--no-sandbox', '--disable-gpu', '--font-render-hinting=none'],
});

const page = await browser.newPage({ viewport: { width: 3800, height: 2000 } });
await page.goto(`file://${HTML}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(5000);

for (const [sel, name] of targets) {
  const el = page.locator(sel);
  await el.screenshot({ path: join(OUT, name), type: 'png' });
  console.log(`✓ ${name}`);
}

await browser.close();
console.log('Done — all images in output/');
