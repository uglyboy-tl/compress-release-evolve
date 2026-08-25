# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright"]
# ///
"""Render WeChat cover pair using Playwright via uv."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

TASK = Path(__file__).parent
HTML = TASK / "index.html"
OUT = TASK / "output"
OUT.mkdir(exist_ok=True)

TARGETS = [
    ("#wechat-21x9", "wechat-21x9.png", 2400, 900),
    ("#wechat-1x1", "wechat-1x1.png", 1080, 1080),
]

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            executable_path="/opt/microsoft/msedge/msedge",
            headless=True,
            args=["--no-sandbox", "--disable-gpu", "--font-render-hinting=none"],
        )
        page = await browser.new_page()
        await page.set_viewport_size({"width": 2400, "height": 15000})
        await page.goto(f"file://{HTML.resolve()}", wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(5000)

        for selector, name, w, h in TARGETS:
            el = page.locator(selector)
            await el.screenshot(path=str(OUT / name), type="png")
            print(f"✓ {name} ({w}×{h})")

        await browser.close()
        print(f"Done: {OUT}")

asyncio.run(main())
