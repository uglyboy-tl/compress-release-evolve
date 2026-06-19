import { chromium } from 'playwright-core';
import { join } from 'path';

const HTML = join(process.cwd(), 'index.html');
const OUT = join(process.cwd(), 'output');

(async () => {
  const browser = await chromium.launch({
    executablePath: '/opt/microsoft/msedge/msedge',
    headless: true,
    args: ['--no-sandbox', '--disable-gpu', '--font-render-hinting=none'],
  });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 2400, height: 15000 });
  await page.goto(`file://${HTML}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000); // 等待 WebGL canvas 和字体渲染

  // 截图 21:9 封面
  const wide = page.locator('#wechat-21x9');
  await wide.screenshot({ path: join(OUT, 'wechat-21x9-cover.png'), type: 'png' });

  // 截图 1:1 封面
  const square = page.locator('#wechat-1x1');
  await square.screenshot({ path: join(OUT, 'wechat-1x1-cover.png'), type: 'png' });

  // 截图配对预览
  const preview = page.locator('.pair-preview');
  await preview.screenshot({ path: join(OUT, 'wechat-cover-pair-preview.png'), type: 'png' });

  await browser.close();
  console.log('渲染完成，输出保存在:', OUT);
})();