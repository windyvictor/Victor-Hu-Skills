# AI 辅助科研：方法论与工具参考指南

> 本文档由 4 份关于「AI 辅助科研」的资料提炼而成，面向大学教授与研究生，聚焦**可直接复用的工作流**与**关键提示词（prompt）模板**。文中英文术语与专有名词保留英文，原文出现的 prompt 一律以代码块原文保留。
>
> **引用说明**：正文的框架、要点与 checklist 为**提炼改写**；**代码块内的 prompt 模板为原文保留**（为保持可直接套用的功能性而未改写）。原始资料见本技能 README 的「参考资料 / 灵感来源」。prompt 模板及相关引文的著作权归原作者与出版方所有，此处仅供个人学习与研究参考，如涉侵权请联系删除。
>
> 资料来源：
> 1. *AI for research: the ultimate guide to choosing the right tool*（Nature，Amanda Heidt）
> 2. *AI 时代科研方法论白皮书（2026 版）*（马拉 AI × 灵研 AI）
> 3. *ChatGPT in Scientific Research and Writing: A Beginner's Guide*（Han, Qiu & Lichtfouse，Springer）
> 4. *Three ways ChatGPT helps me in my academic writing*（Nature Career Column，Dritjon Gruda）

**如何使用本文档**：建议先读第二章的「七步法 + 五原则」建立整体框架，再按你当前所处的科研环节（选题 / 文献 / 实验 / 写作 / 投稿）跳读对应章节。每一章的 prompt 模板可直接复制到 ChatGPT、Claude 或 Copilot 中，把方括号 `[ ]` 替换为你的具体研究信息即可复用。所有模板均原文保留，未做改写。

---

## 第一章　工具选型指南：为科研任务匹配对的 AI（Nature）

### 文档主旨
这是一篇 Nature 的「工具选型」综述，核心主张是：**不存在万能的 AI 工具，关键是根据科研环节（文献、假设、统计、写作）选择最合适的工具**。文中反复强调 veracity（准确性）与 citations（引用规范）——AI 输出必须可追溯、可核对。

### 核心方法论 / 工作流（4 大模块）
按科研流程拆分为四个可操作环节：

1. **Sharpen your literature review（锐化文献调研）**
   - 用具备 active learning 能力的学术搜索引擎（如 Semantic Scholar）主动推送相关文献；
   - 用 **Gemini Deep Research / OpenAI Deep Research** 输入查询后「离开」，模型在约 30 分钟内完成深度检索并返回报告；
   - 用 **Research Rabbit** 以一篇「种子论文」生成按主题、作者、方法互联的文献网络。

2. **Create your hypothesis（生成研究假设）**
   - 利用 AI 综合多源信息、识别 research gaps（研究空白）并连接跨领域想法；
   - ⚠️ 文中引用调查提醒：过度依赖生成式 AI 可能削弱人的 critical-thinking（批判性思维）能力，假设仍需研究者本人把关。

3. **Streamline your statistics（简化统计分析）**
   - 用 AI 代码编辑器（GitHub Copilot、Amazon Q Developer、Cursor）组织数据、搭建分析流水线、运行描述统计与可视化，已大量取代 Stack Overflow 式搜索。

4. **Polish your writing（打磨写作）**
   - 通用聊天模型在严肃学术写作上仍有短板，应使用面向科研定制的平台（见工具清单）。

> 本文为工具评测，未提供固定 prompt 模板；其方法论核心是「**按需选工具 + 强校验引用**」。

### 推荐工具清单
| 工具 | 用途 | 适用场景 |
|------|------|----------|
| Semantic Scholar | 学术搜索 + active learning 推荐 | 文献发现、追踪领域前沿 |
| Gemini / OpenAI Deep Research | 深度自动文献检索与综述 | 进入新方向前的全景调研 |
| Research Rabbit | 可视化文献关系网络 | 选题、文献地图构建 |
| GitHub Copilot / Amazon Q / Cursor | AI 代码编辑、数据分析流水线 | 统计编码、图表生成 |
| Paperpal / Thesify | 按期刊投稿规范核查稿件、提供模板 | 投稿前格式与结构自查 |
| SciSpace / Coral AI / Claude / NotebookLM / PDF.ai | 「Chat with PDF」问答 | 快速读懂单篇论文 |
| Quillbot / OpenAI Whisper | 多语言翻译与语音转写 | 非母语写作、跨语言协作 |

### 实用建议与注意事项
- **veracity 优先**：选择「更擅长给出正确引用」的模型；任何事实、数据、参考文献都必须人工核对。
- **保持批判性**：AI 可加速假设生成，但不能替代研究者对科学价值的判断；文中提醒过度依赖生成式 AI 会削弱 critical-thinking 能力，建议把 AI 输出当作「第二意见」而非定论。
- **引用可追溯**：写作类工具输出需标注来源，避免「看似合理但无出处」的内容进入稿件；优先选「更擅长给出正确引用」的模型。

---

## 第二章　AI 时代科研方法论白皮书（2026 版）

### 文档主旨
核心论断：**「AI 不会淘汰科研人员，但会淘汰不会使用 AI 的科研人员。」** 白皮书面向所有专业背景，系统给出从选题到投稿的**七步科研工作流**、**AI 辅助科研五原则**、**AI+X 选题五步路径**与**十大认知误区**，强调「AI 是方法、X（你的专业）才是主体」。

### 核心方法论 / 工作流

**一、AI 辅助科研五原则（3.3 节）**
- **验证 AI 输出**：AI 生成的代码、摘要、实验结果都需人工验证，AI 会「幻觉」给出看似正确实则不实的答案。
- **提供足够上下文**：提问时给出研究背景、数据特征、目标任务，回答质量大幅提升。
- **迭代式对话**：不要期望一次提问得完美答案，科研场景常需 5–10 轮对话。
- **AI 负责执行，你负责判断**：创新点价值、实验设计合理性须由你的专业知识判定。
- **合理使用，学术诚信**：研究思路、核心贡献、实验结果必须是真实的。

**二、AI+X 选题五步路径**
1. 识别专业问题（最耗时/最难/最依赖人工判断的任务）；
2. 确认数据可获得性（公开数据集？可收集？文献已有库？）；
3. 匹配 AI 方法（图像→CNN/ViT；时序→LSTM/Transformer；文本→BERT/LLM）；
4. 验证可行性；
5. 结合导师背景与投稿目标最终定题。

**三、科研七步法（全流程）**
- **Step01 选题**：灵研 AI 生成领域现状报告 → 交 ChatGPT 识别研究空白 → 用「问题–方法–数据」三角验证。
- **Step02 文献调研**：灵研 AI 检索高引论文 → 上传 PDF 给 Claude 提取「问题/方法/数据集/结论」→ 整理成文献矩阵 → 从「局限性」列发现 gap。
- **Step03 创新设计**：文献矩阵+gap 交 ChatGPT 头脑风暴 5–10 方向 → 用「问题–方法–效果」三段验证 → 选 1–2 个方向 → Claude 梳理技术路线。
- **Step04 Baseline 复现**：Papers with Code 找 SOTA 与开源代码 → Cursor 打开仓库请 AI 解释结构 → 报错粘给 Claude（可解 80%+）→ 记录基准指标。
- **Step05 实验设计**：ChatGPT 建议消融实验方案 → Claude 分析指标涨跌原因 → AI 辅助出图（折线/柱状/热力图）并按期刊规范排版。
- **Step06 论文写作**：AI 生成大纲 → 按「摘要五段（背景–问题–方法–结果–意义）/引言四段（重要性–现有方法–不足–贡献）」逐段写 → Claude 学术英语润色与逻辑检查。
- **Step07 投稿返修**：按主题选刊（影响因子/审稿周期/分区）→ ChatGPT 写 Cover Letter → 把 Reviewer Comments 输入 AI 按条目分类（方法质疑/实验不足/表述不清）并建议策略 → Rebuttal 按「**致谢→理解→响应→结果**」四段式回复每条意见。

### 推荐工具清单
| 工具 | 用途 | 适用场景 |
|------|------|----------|
| ChatGPT（GPT-4o） | 通用对话、论文解读、头脑风暴、润色 | 选题讨论、创新点、写作 |
| Claude（3.5/3.7） | 代码分析、长文档理解、复杂推理 | 读长论文、设计实验、英文润色 |
| Cursor | AI 代码编辑器 | GitHub 复现、环境配置、Debug |
| GitHub Copilot | 代码自动补全 | Jupyter 数据分析降门槛 |
| 灵研 AI | 科研场景专用（文献/选题/解析/写作） | AI 科研工具链核心产出 |
| Kimi / DeepSeek | 长文本/代码与数学推理 | 中文长文、数学推导 |

### 实用建议与注意事项
- **破除「门槛幻觉」**：不会编程不是障碍——ChatGPT/Claude 解释代码，Cursor 改代码配环境，Copilot 补全，你只需「理解代码在做什么」。
- **学术诚信边界**：AI 可辅助语言润色、结构梳理，但核心贡献必须是真实研究成果（误区 4）。
- **Rebuttal 草稿不可直发**：须逐条核对，确保每条回应都有真实实验或文献支撑。
- **AI 放大人的能力，不替代判断**（误区 10）。

---

## 第三章　ChatGPT 科研写作入门指南（Springer）

### 文档主旨
面向初学者的实操手册，用大量**可复现的 prompt 案例**演示 ChatGPT（GPT-3.5 / GPT-4）、GPT 赋能的 new Bing（现 Copilot）、Perplexity、ChatPDF 等工具贯穿「概念化→实验设计→发表→科普」全过程，并专章讨论 pitfalls（陷阱）与 reality check（现实核查）。

### 核心方法论 / 工作流（按科研阶段）

**A. 纠错与核查**
- **科学错误识别**：把含错的讨论文本交给模型，令其通读全文定位错误。
  ```
  Below are some discussion texts under the section "3.5 Effect of contaminant
  solution character on adsorption". I want you to read the entire article,
  understand the context, and identify the mistakes in these discussion texts.
  ```
- **公式核查**：上传模型方程，要求找出并解释错误。
  ```
  ...I want you to take a closer look at these equations. If there is any mistake
  in these equations, I want you to find it and explain it to me in detail.
  ```
- **图表解读**：让模型逐图逐表解释信息。
  ```
  Please help me analyze the figures and tables in this article, and explain
  the information in each one in detail.
  ```

**B. 同行评审（peer review）**
  ```
  You are a peer reviewer of the research article in the web browser. You need to
  be rigorous, skeptic, harsh, and constructive. List the main limitations in the
  methods, findings, and discussions of this study, and explain them in detail.
  ```

**C. 反驳审稿意见（rebuttal）** —— 把审稿人质疑 + 原文 + 参考文献全文交给模型生成反驳。
  ```
  You are an author of a review paper. In the paper, you wrote this sentence:
  "Davy et al. (2018) found large quantities of coronavirus RNAs in the intestines
  of hibernating Little brown bats (Myotis lucifugus) co-infected with the
  white-nose syndrome, which confirmed that responses of extracellular
  co-infections had led to amplified coronavirus replication and increased viral
  shedding from bats." The reviewer strongly disagrees with the sentence you wrote.
  The reviewer stated: "This is incorrect because a PCR gives the amount of RNA,
  but this doesn't always correlate with the quantity of live virus. Can't associate
  detection of RNA with live virus." The full text of the reference article
  (Davy et al. 2018) is opened in the web browser. I want you to read the entire
  article, analyze the reviewer's comments, and provide a detailed rebuttal to
  the reviewer.
  ```

**D. 实验设计（9.2 Reality Check / 9.3 Cautionary Note）**
- 用 GPT-4 列出相关参考文献的方法与仪器，作为「现实核查」基准；
- **关键操作**：在查询结尾始终要求模型给出**相关参考文献清单**，再用 Perplexity Ask 等工具交叉验证，手工比对方法学是否与该领域共识矛盾。

**E. 其他场景**：问卷设计、研究计划（mock proposal）撰写、科普文章与社交媒体改写、可视化生成（Bing Image Creator / DALL·E）。

### 推荐工具清单
| 工具 | 用途 | 适用场景 |
|------|------|----------|
| ChatGPT（GPT-4 / 3.5） | 通用对话、写作、纠错 | 全流程；GPT-4 准确性更高 |
| new Bing / Copilot | 联网检索 + 网页上下文理解 | 需读取在线文献的评审/反驳 |
| Perplexity Ask | AI 搜索 + 引用溯源 | 实验方法的现实核查 |
| ChatPDF | 上传 PDF 问答 | 单篇论文精读（注意隐私） |
| Bing Image Creator（DALL·E） | 文生图 | 科普可视化（注意手部畸变缺陷） |

**F. 移除语言壁垒（7.3 Removing Language Barriers）**
- ChatGPT 可把非母语研究者的中文思路转化为专业英文表达，降低发表门槛；但**翻译的科学准确性由作者负责**，不能因「AI 翻的」而免责。
- **模型代际差异（7.4 GPT-3.5 vs GPT-4）**：在纠错、评审、实验设计等任务上，GPT-4 的准确性与相关性显著优于 GPT-3.5，关键科研环节优先用 GPT-4。

### 实用建议与注意事项
- **hallucination（幻觉）是主要局限**：模型会提供错误/不准确信息，或把事实错误归因于不存在的来源；其生成的参考文献常含错误书目信息——**必须 fact-check**。
- **同一问题重复问会得到随机不同答案**，需用精心设计的 prompt 提升一致性。
- **合规要求**：NSF（2023）规定——用生成式 AI 写提案须披露使用程度；评审人**禁止**把提案/评审内容上传至非批准的 AI 工具（视为进入公共领域，丧失保密性）。NIH 视基金申请为「原创想法」，AI 引入的抄袭文本/伪造引用将按违规处理。建议 AI 仅用于头脑风暴与示意性 mock proposal。
- **编辑/评审提醒**：警惕被 AI 生成的长篇回复淹没，fact-checking 耗时且易漏。
- **语言壁垒**：ChatGPT 可移除语言障碍，但译者须对科学准确性负责。

---

## 第四章　用 ChatGPT 辅助学术写作的三种方式（Nature Career Column）

### 文档主旨
作者 Dritjon Gruda（期刊副主编）以「坦白」口吻分享：他几乎每天用生成式 AI **润色自己写的论文、对审稿/编辑任务获取替代性评估**。核心观点——**价值不在技术本身盲目产出文本，而在「人×工具」的对话中用自己的专业打磨产物**；AI 是 sounding board（参谋/共鸣板），不是代笔，也不替代评审。

### 核心方法论 / 工作流（3 种用法 + prompt）

**1. Polishing academic writing（润色学术写作）**
- 黄金法则：**context, context, context**（上下文为王）。先概述论文主题与核心论点，再让模型重述某段。
  ```
  I'm writing a paper on [topic] for a leading [discipline] academic journal.
  What I tried to say in the following section is [specific point]. Please rephrase
  it for clarity, coherence and conciseness, ensuring each paragraph flows into the
  next. Remove jargon. Use a professional tone.
  ```
- 这是**协作迭代**过程，首答未必完美，可继续微调：
  ```
  This isn't quite what I meant. Let's adjust this part.
  ```
  ```
  This is much clearer, but let's tweak the ending for a stronger transition to
  the next section.
  ```

**2. Elevating peer review（提升同行评审）**
- 先通读稿件、自拟要点，**不把稿件原文上传**（规避隐私），仅基于你的摘要让 AI 组织反馈。
  ```
  Assume you're an expert and seasoned scholar with 20+ years of academic experience
  in [field]. On the basis of my summary of a paper in [field], where the main focus
  is on [general topic], provide a detailed review of this paper, in the following
  order: 1) briefly discuss its core content; 2) identify its limitations; and 3)
  explain the significance of each limitation in order of importance. Maintain a
  concise and professional tone throughout.
  ```
- 模型常能提供未考虑的角度；但**最终评审责任永远在人**——须能区分事实与非事实。

**3. Optimizing editorial feedback（优化编辑反馈）**
- 作为期刊编辑，先评估论文利弊并做批注，再交 AI 起草给作者的信。
  ```
  On the basis of these notes, draft a letter to the author. Highlight the
  manuscript's key issues and clearly explain why the manuscript, despite its
  interesting topic, might not provide a substantial enough advancement to merit
  publication. Avoid jargon. Be direct. Maintain a professional and respectful
  tone throughout.
  ```

### 推荐工具清单
| 工具 | 用途 | 适用场景 |
|------|------|----------|
| ChatGPT（OpenAI） | 通用润色、评审辅助 | 日常写作与反馈草稿 |
| Gemini（Google） | 语言细微差别分析 | 需深层语义/搜索查询分析时 |
| Mixtral（开源） | 离线本地助手 | 无网络但仍需 AI 辅助时 |

### 实用建议与注意事项
- **context 是王**：没有上下文，任何模型都无法给出有意义回应。
- **隐私优先**：评审/编辑时**不要直接上传稿件原文**，用你自己的摘要代替。
- **你是责任主体**：AI 建议可能「离谱、牵强、无关或干脆错误」，审稿结论必须由你定夺。
- **AI 不取代科学本质**：好奇心、批判性思维、创新才是核心；AI 只是改善我们交流研究的方式。作者总结：生成式 AI 给科学界带来挑战，也能提升我们的写作、审稿与编辑质量——它增强的是能力，而非替代判断。

---

## 跨文档共识速记
- **幻觉（hallucination）是所有文档头号风险**：输出必须人工验证、引用必须可追溯。
- **上下文 + 迭代对话**是高质量产出的共同前提（白皮书「五原则」、Gruda「context is king」、入门指南的精心 prompt）。
- **学术诚信边界统一**：AI 可辅助语言/结构/思路，但核心贡献、数据、结论须真实；涉及提案/评审须遵守 NSF/NIH 披露与保密规定。
- **工具分层**：通用大模型（ChatGPT/Claude/Gemini）做思考与写作，代码编辑器（Cursor/Copilot）做工程，垂直工具（灵研 AI/SciSpace/Perplexity）做检索与核查。
