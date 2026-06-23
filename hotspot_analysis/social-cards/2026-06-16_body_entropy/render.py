from playwright.sync_api import sync_playwright
import os, subprocess, sys

html_path = os.path.join(os.getcwd(), 'index.html')
out_dir = os.path.join(os.getcwd(), 'output')

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path='/opt/microsoft/msedge/msedge',
        headless=True,
        args=['--no-sandbox', '--disable-gpu', '--font-render-hinting=none']
    )
    page = browser.new_page()
    page.set_viewport_size({'width': 2400, 'height': 15000})
    page.goto(f'file://{html_path}', wait_until='domcontentloaded', timeout=60000)
    page.wait_for_timeout(5000)
    page.locator('#wechat-21x9').screenshot(path=os.path.join(out_dir, 'wechat-21x9-cover.png'))
    page.locator('#wechat-1x1').screenshot(path=os.path.join(out_dir, 'wechat-1x1-cover.png'))
    browser.close()

subprocess.run([sys.executable, os.path.join(os.getcwd(), 'stitch.py')], check=True)
print('渲染完成，输出保存在:', out_dir)
