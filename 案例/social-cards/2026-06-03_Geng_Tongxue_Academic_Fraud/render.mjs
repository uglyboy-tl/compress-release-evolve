import { chromium } from 'playwright-core';
import { join } from 'path';
import { mkdirSync } from 'fs';

const HTML = join(import.meta.dirname, 'index.html');
const OUT = join(import.meta.dirname, 'output');
mkdirSync(OUT, { recursive: true });

const EDGE = '/opt/microsoft/msedge/msedge';

const targets = [
  ['#xhs-01', 'xhs-p01-cover.png'],
  ['#xhs-02', 'xhs-p02-code-reverse.png'],
  ['#xhs-03', 'xhs-p03-entropy-transfer.png'],
  ['#xhs-04', 'xhs-p04-self-ref.png'],
  ['#xhs-05', 'xhs-p05-evolution.png'],
  ['#xhs-06', 'xhs-p06-good-academics-a.png'],
  ['#xhs-06b', 'xhs-p06-good-academics-b.png'],
  ['#xhs-07', 'xhs-p07-conclusion.png'],
  ['#wechat-21x9', 'wechat-21x9-cover.png'],
  ['#wechat-1x1', 'wechat-1x1-cover.png'],
];

async function main() {
  const browser = await chromium.launch({
    executablePath: EDGE,
    headless: true,
    args: ['--no-sandbox', '--disable-gpu', '--font-render-hinting=none'],
  });
  const page = await browser.newPage({ viewport: { width: 2400, height: 15000 } });
  await page.goto(`file://${HTML}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);

  for (const [sel, name] of targets) {
    const el = page.locator(sel);
    const box = await el.boundingBox();
    if (!box) { console.log(`SKIP ${sel}`); continue; }
    await el.screenshot({ path: join(OUT, name), type: 'png' });
    console.log(`OK ${name}  ${Math.round(box.width)}x${Math.round(box.height)}`);
  }

  await browser.close();
  console.log('Done');
}

main().catch(e => { console.error(e); process.exit(1); });
