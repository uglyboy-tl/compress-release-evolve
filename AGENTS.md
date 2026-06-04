# 项目 AGENTS.md

## 核心理论速查

本项目基于「压缩、释放与进化」系统理论。以下概念是分析的基石：

| 概念 | 一句话 |
|------|--------|
| **熵** | 随机性。系统可能处于的状态越多，熵越大。 |
| **压缩映射** | 控制 = 将复杂现象压缩为单一维度指标。关键后果：总熵不会减少，只是转移。 |
| **编码反转** | 手段变成目的，编码取代现实。如：论文从知识载体变成学术追求的目标本身。 |
| **自指闭环** | 系统内部一切反馈都被收敛到现有编码框架内解决，无法跳出框架审视自身。 |
| **维度压缩偏误** | 编码天然偏好可度量维度，不可度量维度被系统性忽视。 |
| **编码锁定** | 所有子系统围绕核心编码生长出高度耦合的依赖关系，难以自我革命。 |
| **编码进化** | 熵减（形成新编码）→ 熵增（新旧组合）→ 新熵减 → 循环往复。 |

诊断用「熵」，治疗用「编码」。找到熵转移路径是诊断，找到编码进化循环是出路。

详见 `README_zh.md` 和 `系统理论.md`。

---

## 项目近期目标

当前核心任务：**将系统理论应用于热点事件分析，产出文章和社交媒体配图。**

### 工作流

```
热点事件 → 素材收集 → 系统诊断 → 叙事写作 → 社交卡片 → 发布
```

1. **素材收集**：用 anysearch 搜索相关新闻、采访、评论，获取一手信息
2. **系统诊断**：按 `hotspot_analysis/TEMPLATE.md` 的叙事指引，诊断（用熵）→ 治疗（用编码）
3. **叙事写作**：叙事优先，概念为叙事服务。去 AI 味（参考 humanizer skill）
4. **社交卡片**：用 guizang-social-card skill 生成小红书图文 / 公众号封面

### 项目结构

```
compress-release-evolve/
├── 系统理论.md / README_zh.md / ...    # 核心理论文档
├── hotspot_analysis/                    # 热点分析
│   ├── README.md                        # 分析流程和概念框架
│   ├── TEMPLATE.md                      # 叙事指引
│   └── YYYY-MM-DD_event/               # 每个热点一个文件夹
│       ├── article.md                   # 分析文章
│       └── social-cards/               # 社交卡片
│           ├── index.html              #   HTML（一个文件含全部海报）
│           ├── render.mjs              #   渲染脚本
│           ├── assets/                 #   图片素材
│           └── output/                 #   渲染输出 PNG
└── AGENTS.md                            # 本文件
```

---

## 工具使用技巧

### Playwright 渲染社交卡片

环境：`playwright-core` 已安装，系统上 `msedge` 可用（`/opt/microsoft/msedge/msedge`）。

```js
import { chromium } from 'playwright-core';

const browser = await chromium.launch({
  executablePath: '/opt/microsoft/msedge/msedge',
  headless: true,
  args: ['--no-sandbox', '--disable-gpu', '--font-render-hinting=none'],
});
```

**关键坑位：**

1. **`networkidle` 超时**：HTML 中引用了 Google Fonts 时，`networkidle` 永远不会触发（因为离线环境无法加载）。改用 `waitUntil: 'domcontentloaded'` 并手动等待：
   ```js
   await page.goto(`file://${HTML}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
   await page.waitForTimeout(5000); // 等 WebGL canvas 和本机字体渲染
   ```

2. **viewport 设置**：需足够高以容纳所有竖向堆叠的 poster。如 10 张 1440px × 8 = 12000px，设置 `viewport: { width: 2400, height: 15000 }`。

3. **截图方式**：用 `element.screenshot()` 而非 `page.screenshot(clip)`，自动处理裁剪：
   ```js
   for (const [sel, name] of targets) {
     const el = page.locator(sel);
     await el.screenshot({ path: join(OUT, name), type: 'png' });
   }
   ```

4. **lightpanda 不可用**：本机 lightpanda 的 CDP 协议与 Playwright 不兼容，直接使用 msedge。

5. **本机字体**：优先使用本机 LXGW WenKai 替代 Google Fonts 的衬线字体，避免网络依赖：
   ```css
   --serif-zh: "LXGW WenKai GB Screen", "Noto Serif SC", serif;
   ```

### 社交卡片生成流程

1. 从 `guizang-social-card` skill 复制模板 `assets/template-editorial-card.html` 到 `index.html`
2. 选择风格：Editorial Magazine × E-ink（Indigo Porcelain 主题）或 Swiss International
3. 按 `references/layout-recipes.md` 选择每个页面的布局（M01-M16）
4. 每张卡一个 `<section class="poster xhs" id="xhs-XX">` — 所有卡写在同一个 HTML 里
5. 写入 render.mjs，运行 `node render.mjs`

### 写作原则

- **叙事优先**：先讲好故事，再用系统概念加深。不要写成分析报告。
- **概念为叙事服务**：如果概念不能帮助理解故事，不要用。
- **去掉 AI 味**：加载 humanizer skill 检查。删除填充短语、否定式排比、破折号过度使用、粗体过度使用。
- **中文引号**：始终使用中文双引号（“”），不用「」。

### 提交规范

遵循 Conventional Commits：`feat(hotspot-analysis): <描述>`。分组原则：
- 基础设施文件（README、模板）单独提交
- 文章内容单独提交
- 社交卡片工具链（HTML + render + assets）单独提交
