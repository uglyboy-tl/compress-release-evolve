import { chromium } from 'playwright-core';
import { join } from 'path';

const HTML = join(process.cwd(), 'index-xhs.html');
const OUT = join(process.cwd(), 'output');

(async () => {
  const browser = await chromium.launch({
    executablePath: '/opt/microsoft/msedge/msedge',
    headless: true,
    args: ['--no-sandbox', '--disable-gpu', '--font-render-hinting=none'],
  });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1080, height: 15000 });
  await page.goto(`file://${HTML}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000); // 等待 WebGL canvas 和字体渲染

  // 渲染8张小红书卡片
  for (let i = 1; i <= 8; i++) {
    const id = `xhs-${String(i).padStart(2, '0')}`;
    const element = page.locator(`#${id}`);
    await element.screenshot({ path: join(OUT, `xhs-${String(i).padStart(2, '0')}.png`), type: 'png' });
  }

  await browser.close();
  console.log('小红书卡片渲染完成，输出保存在:', OUT);
})();