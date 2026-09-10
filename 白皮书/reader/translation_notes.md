# Translation Notes for "Compression, Release, and Evolution"

## 翻译说明

本文件记录了白皮书《压缩、释放与进化：基于熵的统一系统理论》中英对照版本的翻译要点和注意事项。

### 术语一致性

以下术语在全文中统一译法，评审后已固定的旧译法以括号标注。

| 英文术语 | 中文翻译 | 说明 |
|----------|----------|------|
| Entropy | 熵 | 保持热力学和信息论中的标准术语 |
| Control | 控制 | 在本理论中特指“跨维度传输随机性的过程” |
| Compression Mapping | 压缩映射 | 数学术语，保持直译 |
| Rigidity | 刚性 | 描述控制强度的术语 |
| Flexibility | 柔性 | 描述策略空间宽度的术语 |
| Antifragility | 反脆弱性 | 沿用塔勒布《反脆弱》中的中文译法 |
| Exchange Surface | 交换面 | 系统与其环境之间发生交换的界面；反脆弱性中可被设计的那部分 |
| Strategy Space | 策略空间 | 系统可用的替代路径集合 |
| Dissipation Bandwidth | 散热带宽 | 旧译“热耗散带宽”已废弃 |
| Coding | 编码 | 在本理论中具有特殊含义，指“控制规则的形式化表达” |
| Coding Reversal | 编码反转 | 旧译“编码颠倒”已废弃 |
| Dimension Compression Bias | 维度压缩偏误 | 旧译“维度压缩偏差”已废弃 |
| Self-Referential Closure | 自指闭环 | 旧译“自指闭包”已废弃 |
| Informational Isolation | 信息上的孤立化 | 闭环的热力学表述：编码不再接受来自其外部的信号的纠正 |
| Interest-Based Closure | 利益型闭环 | 自指闭环的第一种类型 |
| Epistemic Closure | 认知型闭环 | 自指闭环的第二种类型 |
| Truth-Seeking | 求知型 | 对外部事实的取向 |
| Interest-Defending | 护利型 | 对外部事实的取向 |
| Causal Hierarchy | 因果层级 | Pearl 的因果能力分层 |
| Association | 关联 | 因果层级 L1 |
| Intervention | 干预 | 因果层级 L2 |
| Counterfactual | 反事实 | 因果层级 L3 |
| Causal Capacity | 因果能力 | 系统可执行的因果推理层次 |
| Meta-Coding | 元编码 | 描述自身控制编码并有权修改它的编码 |
| Material Entropy | 物质熵 | 受生产能力约束的熵 |
| Information Entropy | 信息熵 | 受编码框架丰富性约束的熵 |
| Unified Diagram | 统一图纸 | 父系统互不重叠的路由编码 |
| Control Module | 控制模块 | 维持统一图纸的功能 |
| Control Coupling | 控制耦合 | 被内部摩擦消耗的控制力 |
| Routing | 路由 | 规定熵的移动方向与收发方 |
| Compliance | 遵循 | 子系统沿规定路径执行 |
| Compliance Channel | 遵循通道 | §2.9 的两条通道：熵供给与信息编码 |
| Redundancy | 冗余 | 保留多条相互竞争的路由 |
| Slack | 松弛 | 供给超出当前需求，留下探索余量 |
| Fluctuation | 波动 | 恢复选择压力的周期性供给变化 |
| General Equivalent | 一般等价物 | 中介熵供给的单一可测量信号，即货币 |
| Dissipative Structures | 耗散结构 | 仅在耗散流持续时存在的宏观结构 |
| Far from Equilibrium | 远离平衡 | 涨落被放大并锁定的驱动条件 |
| Fluctuation Amplification | 涨落放大 | 非线性相互作用把小扰动变成结构 |
| Persona | 人设 | 从所有可产出内容到符合人设之内容的压缩映射 |
| Code Alignment | 编码对齐 | 共享编码降低系统间的交换成本 |
| Entropy Seeker | 寻熵者 | 以熵的摄入与代谢为引擎的系统 |
| Nested Levels | 嵌套层级 | 进化自身机制在其中进化的层级 |
| Phase Transition | 相变 | 本框架中指死亡时从系统到非系统的转变 |
| Stalled Beat | 断拍 | 编码进化循环中某一拍的失败 |
| Empathy | 共情 | 两个系统之间交换的度量效率，不作道德态度解 |
| Diagnostic Protocol | 诊断协议 | 应用诊断的操作序列 |
| Boundary Diagram | 边界图 | 列出父系统、子系统与适用图纸数量的边界界定 |
| Control Distribution Map | 控制分布图 | 约束实际画在哪里、绷得多紧的盘点结果 |
| Entropy-Flow Map | 熵流向图 | 记录什么被压缩、谁在吸收成本、哪个维度先到极限 |
| Root Code | 根编码 | 驱动下一层且不受上一层直接惩罚的编码 |
| Leverage Level | 杠杆层 | 编码改变不会被更高一层惩罚的层级 |
| Code Chain | 编码链 | 嵌套系统中分隔“何处出错”与“谁能改动”的层级链条 |
| External Probe | 外部探针 | 激励不依赖编码稳定性的观察者 |
| Closure Test | 闭环检验 | 判定纠偏是否仍落在编码框架内的检验 |
| Comparison Case | 对照样本 | 机制相同、结果不同的第二系统 |

### 文化背景说明

1. **维特根斯坦的语言图像论**：
   - 维特根斯坦在《逻辑哲学论》(1922)中提出的哲学理论
   - 认为命题通过共享的逻辑形式描绘事实
   - 在本论文中作为编码描述系统的哲学先例

2. **唐代律诗 (Tang Dynasty regulated verse)**：
   - 中国古典诗歌的一种形式
   - 具有严格的音节和音调约束
   - 作为编码进化的文化例证

### 翻译原则

1. **准确性**：保持学术术语的准确性和一致性
2. **完整性**：完整传达原文的所有概念和论证
3. **流畅性**：中文译文应自然流畅，符合学术写作规范
4. **术语统一性**：同一术语在全文中保持一致译法
5. **文化背景保留**：保留必要的文化背景说明

### 标点与排版规范

1. **中文引号**：统一使用中文双引号 “”，不使用角括号 「」
2. **连字符**：统一使用 ASCII 连字符 `-`，不使用 Unicode 连字符 `‑` (U+2011)
3. **公式和符号**：保持原样，如 `f: X → Y, |Y| < |X|`
4. **引用格式**：保持作者-年份格式，如 (Prigogine & Stengers, 1984)
5. **希腊字母**：保持原符号，如 Ω, α, Σ
6. **重点术语**：按原文的加粗范围加粗，不额外增删强调

### 参考文献处理

所有参考文献条目保持英文原样，不翻译作者姓名和标题，以保持学术规范和可检索性。

## 版本信息

- **源文件**: ../white_paper.md
- **翻译日期**: 2026-09-01
- **版本**: 2.0
- **译者**: 自动生成
