#!/usr/bin/env python3
"""公众号封面渲染脚本

用 uvx 提供的 playwright 驱动本机 Edge（channel=msedge）渲染 HTML 封面并截图。

用法：
    uv run --with playwright python render-cover.py

依赖（无需手动安装，uv 自动拉取）：
    - playwright：截图浏览器自动化
    - 本机需要安装 Microsoft Edge，脚本用 channel="msedge" 直接复用；
      若没有 Edge，可改用系统 chromium（换 channel 或 executablePath）。

注意：
    - 字体：模板用本地霞鹜文楷，请确保字体文件存在（模板已硬编码绝对路径）。
    - 背景图：模板引用 bg.jpg，需与模板同目录。
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# 模板路径与输出目录（可改）
# 先找 index.html（事件目录），否则用 cover-template.html（模板目录）
HTML = Path(__file__).parent / "index.html"
if not HTML.exists():
    HTML = Path(__file__).parent / "cover-template.html"
OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

# 封面容器尺寸（对应 3.35:1）；device_scale_factor=2 输出 2x，更清晰
WIDTH = 900
SCALE = 2


def render() -> None:
    with sync_playwright() as p:
        # channel="msedge" 复用本机 Edge；headless 无头模式
        browser = p.chromium.launch(
            channel="msedge",
            headless=True,
            args=["--no-sandbox", "--disable-gpu", "--font-render-hinting=none"],
        )
        page = browser.new_page(
            viewport={"width": WIDTH, "height": int(WIDTH / 3.35) + 40},
            device_scale_factor=SCALE,
        )
        page.goto(f"file://{HTML}", wait_until="networkidle")
        # 等字体加载完成（网络字体 + 本地 @font-face）
        page.wait_for_timeout(800)

        # 只截 .cover 容器，裁掉 body padding
        cover = page.locator(".cover")
        cover.screenshot(path=str(OUT / "cover.png"), type="png")

        browser.close()
    print(f"渲染完成：{OUT / 'cover.png'}")


if __name__ == "__main__":
    try:
        render()
    except Exception as e:  # 给出可操作的错误提示
        sys.exit(f"渲染失败：{e}\n"
                 "请检查：1) 本机是否安装 Edge；2) 是否用 uv 运行（uv run --with playwright）")
