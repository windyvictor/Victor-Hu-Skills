# ai-research-methodology

> **AI 辅助科研**的方法论、工具选型与提示词工程实战指南。

## 一句话定位

回答一个比「用什么提示词」更根本的问题：**AI 到底能帮科研做什么、怎么帮、边界在哪。**

核心理念：**AI 是方法与加速器，专业判断（专业 X）是主体**；所有 AI 产出必须经研究者核验。

## 何时触发

询问如何用 AI / ChatGPT / 大模型 / DeepSeek 辅助科研工作：文献检索与精读、选题与热点趋势、
数据预处理与特征工程、实验设计与创新点挖掘、实证分析与统计建模、质性编码、
文献计量与 PRISMA 系统综述、AI Code 构建与改进 Baseline、消融实验自动化、论文图表生成、
投稿与返修回复；如何选择科研 AI 工具；如何制定 AI 辅助科研工作流与学术诚信规范。

## 内容结构

```text
ai-research-methodology/
├── SKILL.md
└── references/
    ├── methodology-guides.md               # 工具选型 + 方法论白皮书精要
    ├── prompt-engineering-stem.md          # 理工科版黄金提示词模板
    └── prompt-engineering-humanities.md    # 文科版黄金提示词模板
```

## 参考资料 / 灵感来源

> 本节逐条列明参考来源、作者与借鉴内容，供追溯与致谢。
> 本技能为下列材料的**结构化整理、改写与再组织**，不含原书原文的大段复制。
> 相关权利归原作者与出版方所有；如有疏漏或异议，欢迎提 Issue 指出，我们会立即调整或删除。

### A. 方法论与工具选型（`references/methodology-guides.md`）

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| *AI for research: the ultimate guide to choosing the right tool* | Amanda Heidt，*Nature* | 按科研环节选择 AI 工具；veracity（准确性）与 citations（引用规范）原则 |
| 《AI 时代科研方法论白皮书（2026 版）》 | 马拉 AI × 灵研 AI | 七步科研工作流 + 五原则 |
| *ChatGPT in Scientific Research and Writing: A Beginner's Guide* | Jie Han、Weifeng Qiu、Eric Lichtfouse，Springer | 科研各环节中 ChatGPT 的使用方法 |
| *Three ways ChatGPT helps me in my academic writing* | Dritjon Gruda，*Nature* Career Column | 学术写作中的 AI 辅助（润色、模拟审稿、反证） |

### B. 学科提示词工程实战手册

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| 《AI 赋能科研·提示词工程实战手册（理工科版）》9 页（2026-09-22 版） | 原始出版信息未标注 | 8 环节黄金提示词（原手册 12 场景，其中框架生成/逐节撰写/润色降重已转配套技能）+ AI Code 构建 Baseline（3 场景）+ 改进 Baseline（4 策略） |
| 《AI 赋能科研·提示词工程实战手册（文科版）》10 页（2026-09-22 版） | 原始出版信息未标注 | 8 环节黄金提示词（原手册 12 场景，其中框架生成/逐节撰写/润色降重已转配套技能）+ 实证分析（问卷量表/因果推断/质性编码）+ 文献计量与 PRISMA 系统综述 |

### C. 本项目自研部分

| 内容 | 作者 | 说明 |
|---|---|---|
| 按学科与环节的 Skill 路由设计、学术诚信与合规底线章节 | 本项目作者 | 将上述材料组织为可执行的 Skill 结构 |

> ⚠️ **来源待补**：两份《提示词工程实战手册》在仓库中未记录出版方与作者，建议公开开源前核实并补充署名。

## 典型用法

> 「我是做优化算法的，怎么用 AI 帮我做消融实验的自动化？」
> 「文科研究能用 AI 做什么？给我一套可落地的提示词。」
> 「帮我设计一套 AI 辅助科研的完整工作流，并说明学术诚信红线。」
