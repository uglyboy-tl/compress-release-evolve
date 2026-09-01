# 公众号封面制作指南

基于「压缩、释放与进化」项目的封面生成模板。本目录 `_templates/` 收纳可复用的封面模板与渲染工具，每次做新封面可复制此模板、替换文案与背景图即可。

## 目录结构

```
_templates/
├── cover-template.html   # 封面模板（3.35:1 微信公众号新版主图）
├── render-cover.py       # 渲染脚本（uv + playwright + 本机 Edge）
├── README.md             # 本文件
└── output/               # 渲染输出 PNG（脚本自动创建）
```

## 快速开始

1. 复制模板到目标事件目录（或直接改模板）：

   ```bash
   cp _templates/cover-template.html 案例/social-cards/<事件>/index.html
   ```

2. 替换模板内容：
   - 标题文字（`.title span`）：主标题两行
   - 副文案（`.sub`）：一句话简介
   - 右侧强调（`.side span`）：核心观点短句
   - 背景图（`.bg-img` 的 `background-image`：`assets/bg.jpg`）：换成你的图片路径，放入 `assets/` 目录

3. 渲染：

   ```bash
   uv run --with playwright python _templates/render-cover.py
   ```

   输出到 `output/cover.png`。

## 渲染环境说明

本机**无 node，仅 bun 与 uv**。封面截图用 `uvx` 提供的 playpelay 驱动系统已装的 **Microsoft Edge**（无需额外下载浏览器）。

- 依赖通过 `uv` 自动拉取，无需手动安装 node_modules。
- Edge 以 `channel="msedge"` 复用，脚本不需硬编码可执行路径。
- 若本机无 Edge，可改 `channel` 为 `"chromium"`（会尝试下载浏览器），或指定 `executablePath` 指向其它浏览器。

## 核心参数速查

| 参数 | 位置 | 说明 |
|------|------|------|
| 比例 | `.cover` 的 `aspect-ratio: 3.35/1` | 公众号新版主图封面比例（900px 宽→约 268px 高） |
| 背景浓度 | `.bg-img` 的 `opacity: 0.45` | 越低越淡、越接近纯蓝白渐变 |
| 蓝染 | `.bg-blend-multiply / screen` 两层的 `rgba` | 把灰黑山水染成蓝调、去掉灰雾感；不想要可整块删除 |
| 字号 | `.title` 的 `font-size: 4.2cqw` | 用 `cqw`（容器宽度百分比），整体缩放随容器自适应 |
| 字体 | `.title/.sub/.side` 的 `font-family` | 默认本地霞鹜文楷；换成 `Noto Serif SC` 等网络字体需保留 head 的字体加载 |

## 常见调整

- **尺寸更大/更小**：改 `.cover` 的 `max-width`，`cqw` 会自动等比缩放所有元素与字号。
- **去山水用纯渐变**：删掉 `.bg-img`、`.bg-blend-multiply`、`.bg-blend-screen` 三层，仅保留 `.cover` 底部的蓝白渐变即可（最干净）。
- **改文字颜色**：改 `.title/.side` 的 `color`（当前 `rgb(12,74,110)` 深蓝）。
- **忽略官方比例、只取留白**：`render-cover.py` 里改 `WIDTH` 与截图定位即可。

## 字体背景

- 模板用本地字体 **霞鹜文楷 GB Screen**，绝对路径 `/home/uglyboy/.local/share/fonts/LXGWWenKaiGBScreen.ttf`。
- 若在该机器以外的环境渲染，需改路径或删掉该 `@font-face` 改用网络字体（`Noto Sans SC` / `Noto Serif SC`）。

## 系统理论备注

封面文案遵循项目写作红线：摆事实、不评价，让矛盾自己说话。右侧强调行承载"冲突面"，标题行承载"被压缩的维度"，副题承载"熵的踪迹"。
