# 30 条英文论文写作 GPT 指令（网络流传汇编）

> **名称澄清（重要）**：本文档所据 PDF 的题名为《顶刊〈Nature〉推荐的 30 个高级 GPT 指令，一周写完一篇 SCI》。
> 经核查，该清单**并非 Nature 期刊官方发布**，而是中文自媒体（微信公众号文章，2024-12）汇编并冠以
> 《Nature》之名传播，**与 Nature 及其出版集团无任何隶属或背书关系**。此处保留原题名仅为标注素材
> 来源，不代表本仓库认同该说法。
> （补充：《Nature》确于 2024-04 刊载过 Dritjon Gruda 的专栏 *Three ways ChatGPT helps me in my
> academic writing*，但那是单篇观点文章，与本 30 条清单内容不同，二者不应混为一谈。）
>
> 源文件：`顶刊《Nature》推荐的30个高级GPT指令，一周写完一篇SCI.pdf`
> 说明：本文档共 30 条英文提示词（prompt）。**每条指令均完整保留原文英文提示词模板**（置于代码块内，未删减、未意译压缩），并附中文翻译、适用写作环节与使用要点。
> **引用说明**：提示词模板为**原文引用**（为保持可直接套用的功能性而未改写）；原始汇编**未标注作者与授权信息、版权归属不明**，本文档据实记录来源、不主张任何权利，仅供个人学习参考，如涉侵权请联系删除。
> 术语约定：原文模板中的 `[...]` 占位符一并保留，使用时替换为你的具体内容即可。

---

## 目录

- [如何使用本文档](#如何使用本文档)
- [一、前期准备与选题](#一前期准备与选题选题方向确认)
- [二、文献检索与综述](#二文献检索与综述)
- [三、研究设计与方法](#三研究设计与方法)
- [四、数据分析与结果解读](#四数据分析与结果解读)
- [五、论文正文撰写（引言/摘要/结论/标题/关键词/讨论）](#五论文正文撰写引言摘要结论标题关键词讨论)
- [六、润色、改写与翻译](#六润色改写与翻译)
- [七、投稿与回复审稿](#七投稿与回复审稿)
- [附：「一周写完一篇 SCI」工作流清单](#附一周写完一篇-sci工作流清单)

---

## 如何使用本文档

1. 按论文写作环节在上方目录中定位对应分组。
2. 将对应指令代码块内的英文提示词复制给 GPT/AI，替换 `[...]` 占位符。
3. 可结合中文翻译理解语义；「使用要点」给出实操建议。
4. 占位符对照：
   - `[你的研究领域]` / `[特定研究方向]` / `[你的研究主题]`：研究范围
   - `[你的研究想法]` / `[你的假设]` / `[你的研究问题]`：核心研究内容
   - `[列出文献链接或 DOI]` / `[粘贴你的数据]` / `[粘贴你的段落]`：具体材料
   - `[目标语言]`：翻译目标语种

---

## 一、前期准备与选题（选题/方向确认）

### 1. 头脑风暴选题指令
**适用环节**：科研选题、方向确认

**英文提示词模板：**
```text
Brainstorm potential research topics within [你的研究领域], focusing on areas with limited existing research and significant potential impact. For each topic, provide a concise explanation of its relevance, potential challenges, and anticipated outcomes. Consider interdisciplinary approaches and emerging trends within the field.
```

> 中文翻译：在[你的研究领域]内，集思广益，找出一些潜在的研究课题，重点关注现有研究有限且具有重要潜在影响的领域。对于每个课题，简要解释其相关性、潜在挑战和预期成果。考虑跨学科方法和该领域的新兴趋势。

**使用要点**：用于开题阶段发散思路；建议先写清研究领域，再让 AI 按"研究空白 + 影响力"筛选；可多轮追问以收敛到可落地的方向。

---

### 2. 分析研究方向指令
**适用环节**：选题、明确研究问题

**英文提示词模板：**
```text
Analyze the existing literature on [特定研究方向], identifying key research gaps and unresolved questions. Propose several specific, measurable, achievable, relevant, and time-bound (SMART) research questions that could address these gaps, along with a brief justification for each.
```

> 中文翻译：分析关于[特定研究方向]的现有文献，找出关键的研究空白和未解决的问题。提出几个具体的、可衡量的、可实现的、相关的、有时限的(SMART)研究问题，以解决这些差距，并对每个问题进行简要论证。

**使用要点**：把"研究空白"转化为可执行的 SMART 问题；后续可把生成的问题直接喂给指令 7/8 做方法设计。

---

### 3. 评估研究想法指令
**适用环节**：选题评估、可行性论证

**英文提示词模板：**
```text
Critically evaluate the feasibility and potential impact of the following research idea: [你的研究想法]. Consider factors such as resource availability, ethical implications, technical limitations, and potential contributions to the field. Provide a SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) to comprehensively assess the research idea.
```

> 中文翻译：批判性地评估以下研究想法的可行性和潜在影响：[你的研究想法]。考虑资源可用性、伦理意义、技术限制以及对该领域的潜在贡献等因素。提供 SWOT 分析（优势、劣势、机会、威胁），以全面评估研究想法。

**使用要点**：用 SWOT 框架做立项自评；可据此提前识别风险（伦理/技术/资源），写入研究计划（指令 25）。

---

### 24. 制定研究假设指令
**适用环节**：选题细化、假设构建

**英文提示词模板：**
```text
Formulate a research hypothesis based on the following observations: [描述你的观察].
```

> 中文翻译：根据以下观察结果制定研究假设：[描述你的观察]。

**使用要点**：先整理实验/文献观察，再让 AI 提炼为可检验假设；生成的假设可衔接指令 8（设计实验）与指令 11（结果解读）。

---

### 25. 撰写研究计划指令
**适用环节**：选题落地、基金/开题计划

**英文提示词模板：**
```text
Develop a research proposal for a study on [你的研究主题], including a detailed budget and timeline.
```

> 中文翻译：制定一项关于 [你的研究主题] 的研究计划，包括详细的预算和时间表。

**使用要点**：输出开题/基金申请初稿；预算与时间线需结合实际校正，AI 仅提供结构框架。

---

### 26. 识别伦理问题指令
**适用环节**：选题合规、伦理审查

**英文提示词模板：**
```text
Identify potential ethical considerations related to your research on [你的研究主题] and propose strategies for mitigating them.
```

> 中文翻译：识别与你关于 [你的研究主题] 的研究相关的潜在伦理考虑，并提出缓解这些问题的策略。

**使用要点**：用于 IRB/伦理审查材料准备；对涉及人/动物/敏感数据的课题尤其重要。

---

### 27. 定义关键术语指令
**适用环节**：选题表述、术语统一

**英文提示词模板：**
```text
Write a clear and concise definition of [一个与你的研究相关的关键术语].
```

> 中文翻译：对 [一个与你的研究相关的关键术语] 写一个清晰简洁的定义。

**使用要点**：统一全文术语口径；定义可用于引言、方法或术语表（glossary）。

---

## 二、文献检索与综述

### 4. 总结文献关键信息指令
**适用环节**：文献阅读、综述撰写

**英文提示词模板：**
```text
Summarize the key findings, methodologies, limitations, and contributions of the following papers: [列出文献链接或 DOI]. Organize the summary thematically, highlighting common themes and contrasting perspectives across the selected papers.
```

> 中文翻译：总结以下论文的主要发现、方法、局限性和贡献：[列出文献链接或 DOI]。按主题组织总结，突出所选论文的共同主题和对比观点。

**使用要点**：粘贴 DOI/链接或摘要文本，让 AI 做主题化对比；适合快速消化一批文献，但关键结论仍需回读原文核实。

---

### 5. 查找高影响力文献指令
**适用环节**：文献检索、奠基性文献定位

**英文提示词模板：**
```text
Identify the most influential and impactful papers published in the last 5 years on [你的研究主题]. Consider metrics such as citation count, journal impact factor, and altmetrics. Provide a brief analysis of why these papers are considered influential.
```

> 中文翻译：确定过去 5 年发表的关于[你的研究主题]的最有影响力和最有冲击力的论文。考虑诸如引用次数、期刊影响因子和替代指标等指标。简要分析为什么这些论文被认为具有影响力。

**使用要点**：用于锁定近 5 年高引/高 altmetrics 文献；结果需结合数据库（Web of Science/Google Scholar）复核，注意引用量时效偏差。

---

### 6. 创建文献综述大纲指令
**适用环节**：文献综述、引言框架

**英文提示词模板：**
```text
Create a detailed literature review outline for a paper on [你的研究主题], including key themes, subtopics, and relevant supporting literature for each. Structure the outline logically to provide a coherent narrative and demonstrate the progression of research in the field.
```

> 中文翻译：为一篇关于[你的研究主题]的论文创建一个详细的文献综述大纲，包括关键主题、子主题以及每个主题的相关支持文献。按照逻辑构建大纲，以提供连贯的叙述并展示该领域研究的进展。

**使用要点**：输出综述的逻辑骨架；可据此反向填充指令 4 的文献摘要，形成"由纲到目"的写法。

---

## 三、研究设计与方法

### 7. 建议研究方法指令
**适用环节**：方法设计、方法选型

**英文提示词模板：**
```text
Suggest appropriate research methods and experimental designs for investigating [你的研究问题], taking into account the nature of the research question, available resources, and ethical considerations. Provide a rationale for the chosen methods and discuss potential limitations.
```

> 中文翻译：建议用于调查[你的研究问题]的合适研究方法和实验设计，同时考虑到研究问题的性质、可用资源和伦理考虑。提供选择这些方法的基本原理并讨论潜在的局限性。

**使用要点**：把指令 2 的 SMART 问题作为输入；让 AI 给出方法候选 + 取舍理由，再结合领域规范定稿。

---

### 8. 设计实验指令
**适用环节**：实验设计、方法写作

**英文提示词模板：**
```text
Design a robust experiment to test the hypothesis that [你的假设]. Include detailed information on the experimental setup, materials and methods, data collection procedures, statistical analysis plan, and anticipated results. Address potential confounding variables and control measures.
```

> 中文翻译：设计一个稳健的实验来检验[你的假设]。包括实验设置、材料和方法、数据收集程序、统计分析计划和预期结果的详细信息。解决潜在的混杂变量和控制措施。

**使用要点**：覆盖"装置—材料—流程—统计—预期结果—混杂控制"六要素；输出可直接作为 Methods 初稿骨架，统计方案需与方法学家确认。

---

### 9. 评估研究方法优缺点指令
**适用环节**：方法论证、局限性讨论

**英文提示词模板：**
```text
Critically evaluate the strengths and weaknesses of using [特定研究方法] for [你的研究问题]. Compare and contrast this method with alternative approaches, considering factors such as validity, reliability, cost-effectiveness, and ethical implications.
```

> 中文翻译：批判性地评估使用[特定研究方法]解决[你的研究问题]的优势和劣势。将此方法与其他方法进行比较和对比，考虑诸如有效性、可靠性、成本效益和伦理影响等因素。

**使用要点**：用于方法部分"为何选此法"及讨论部分的局限性；建议与指令 7 联动使用。

---

### 23. 识别方法论缺陷指令
**适用环节**：方法自检、局限性（讨论）

**英文提示词模板：**
```text
Identify potential weaknesses in your research methodology and suggest ways to address them in future studies.
```

> 中文翻译：找出你研究方法中潜在的弱点，并建议在未来的研究中解决这些弱点的方法。

**使用要点**：写 Limitations 段落前做自查；输出可转化为"未来研究方向"内容。

---

## 四、数据分析与结果解读

### 10. 数据分析指令
**适用环节**：结果、数据分析

**英文提示词模板：**
```text
Analyze the following data [粘贴你的数据] and identify any statistically significant trends, patterns, or correlations. Provide visualizations (e.g., graphs, charts) to illustrate the findings and interpret their meaning in the context of the research question.
```

> 中文翻译：分析以下数据[粘贴你的数据]，并识别任何具有统计学意义的趋势、模式或相关性。提供可视化（例如，图表）来说明研究结果，并在研究问题的背景下解释其含义。

**使用要点**：粘贴结构化数据（表格/CSV）；让 AI 指出显著趋势并建议图表；**统计显著性结论须用专业软件复核**，勿直接采信 AI 判断。

---

### 11. 实验结果解读指令
**适用环节**：结果、结果解读

**英文提示词模板：**
```text
Interpret the results of the following experiment: [描述你的实验和结果]. Discuss the implications of the findings, considering both supporting and contradictory evidence from the existing literature. Address potential limitations and suggest future research directions.
```

> 中文翻译：解释以下实验的结果：[描述你的实验和结果]。讨论研究结果的含义，同时考虑现有文献中的支持和矛盾证据。解决潜在的局限性并建议未来的研究方向。

**使用要点**：对接指令 8 的预期结果；要求 AI 同时纳入"支持/矛盾"证据，避免确认偏误；输出可喂给指令 12/20 写讨论。

---

## 五、论文正文撰写（引言/摘要/结论/标题/关键词/讨论）

### 14. 撰写引言指令
**适用环节**：引言（Introduction）

**英文提示词模板：**
```text
Generate a compelling and engaging introduction for a research paper on [你的研究主题], clearly stating the research gap, research question, and the significance of the study. Provide relevant background information and establish the context for the research.
```

> 中文翻译：为一篇关于[你的研究主题]的研究论文撰写一个引人入胜且引人入胜的引言，清晰地陈述研究差距、研究问题和研究的意义。提供相关的背景信息，并为研究建立背景。

**使用要点**：引言三要素=研究空白 + 研究问题 + 意义；可结合指令 6 的综述大纲起笔。

---

### 13. 撰写摘要指令
**适用环节**：摘要（Abstract）

**英文提示词模板：**
```text
Write a concise and informative abstract for a research paper on [你的研究主题], summarizing the research question, methodology, key findings, and implications. Adhere to the word limit and formatting guidelines of the target journal.
```

> 中文翻译：为一篇关于[你的研究主题]的研究论文撰写一个简洁而翔实的摘要，总结研究问题、方法、主要发现和含义。遵守目标期刊的字数限制和格式指南。

**使用要点**：等全文成型后再写摘要；务必给定目标期刊字数/结构要求（IMRaD/结构化摘要），避免超限。

---

### 17. 建议论文标题指令
**适用环节**：标题（Title）

**英文提示词模板：**
```text
Suggest a concise and informative title for a research paper based on the following findings: [描述你的研究发现]. The title should accurately reflect the content of the paper and capture the reader's attention.
```

> 中文翻译：根据以下研究结果，建议一个简洁明了的研究论文标题：[描述你的研究发现]。标题应准确反映论文的内容并吸引读者的注意力。

**使用要点**：提供核心发现而非全文；可让 AI 给多个备选（信息型/疑问型），再人工定稿。

---

### 18. 生成关键词指令
**适用环节**：关键词（Keywords）

**英文提示词模板：**
```text
Generate a list of relevant keywords for a research paper on [你的研究主题]. These keywords should facilitate discoverability and indexing of the paper in academic databases.
```

> 中文翻译：生成与[你的研究主题]相关的关键词列表。这些关键词应有助于在学术数据库中发现和索引论文。

**使用要点**：覆盖"主题词 + 方法词 + 物种/对象词"；对照目标期刊 MeSH/投稿指南补足标准词。

---

### 12. 讨论研究意义指令
**适用环节**：讨论（意义延伸）

**英文提示词模板：**
```text
Discuss the broader implications of these findings for [你的研究领域]. Explore potential applications, theoretical contributions, and practical implications of the research. Consider the impact on policy, practice, and future research endeavors.
```

> 中文翻译：讨论这些发现对[你的研究领域]的更广泛的含义。探讨研究的潜在应用、理论贡献和实际意义。考虑对政策、实践和未来研究工作的影响。

**使用要点**：从"应用—理论—实践—政策—未来"五维展开；避免与结果部分重复，重在阐释"so what"。

---

### 20. 创建讨论部分大纲指令
**适用环节**：讨论（Discussion 结构）

**英文提示词模板：**
```text
Create a well-structured outline for the discussion section of a research paper on [你的研究主题], including key points, supporting evidence, and connections to the existing literature.
```

> 中文翻译：为一篇关于[你的研究主题]的研究论文的讨论部分创建一个结构良好的大纲，包括要点、支持证据以及与现有文献的联系。

**使用要点**：先搭大纲再成文，确保"要点—证据—文献呼应"闭环；可与指令 11/12 输出合并。

---

### 21. 论证研究意义指令
**适用环节**：讨论（创新点/贡献论证）

**英文提示词模板：**
```text
Develop a compelling argument for the significance of your research on [你的研究主题], highlighting its potential impact on the field and its contribution to knowledge.
```

> 中文翻译：对你在[你的研究主题]上的研究的重要性进行有力的论证，强调其对该领域的潜在影响及其对知识的贡献。

**使用要点**：用于突出 novelty/contribution；可提炼为 Cover Letter（指令 30）与审稿回复（亮点陈述）的素材。

---

### 19. 撰写结论指令
**适用环节**：结论（Conclusion）

**英文提示词模板：**
```text
Write a comprehensive conclusion for a research paper on [你的研究主题], summarizing the key findings, limitations, and future research directions. Restate the research question and highlight the contributions of the study.
```

> 中文翻译：为一篇关于[你的研究主题]的研究论文撰写一个全面的结论，总结主要发现、局限性和未来的研究方向。重申研究问题并强调研究的贡献。

**使用要点**：结论=发现 + 局限 + 未来 + 重申问题 + 贡献；与摘要呼应但不照抄。

---

## 六、润色、改写与翻译

### 15. 改进段落指令
**适用环节**：润色（段落级）

**英文提示词模板：**
```text
Improve the clarity, conciseness, and overall quality of the following paragraph: [粘贴你的段落]. Ensure the language is precise, the sentences are well-structured, and the flow of ideas is logical.
```

> 中文翻译：提高以下段落的清晰度、简洁性和整体质量：[粘贴你的段落]。确保语言准确，句子结构良好，思想流程合乎逻辑。

**使用要点**：逐段润色效率最高；改完对照原文确认未扭曲原意（尤其数据/因果表述）。

---

### 16. 改写句子指令
**适用环节**：改写、避免抄袭（Paraphrase）

**英文提示词模板：**
```text
Paraphrase the following sentence to avoid plagiarism while retaining the original meaning: [粘贴你的句子]. Ensure the paraphrased sentence is grammatically correct and uses appropriate academic vocabulary.
```

> 中文翻译：改写以下句子以避免剽窃，同时保留其原始含义：[粘贴你的句子]。确保改写后的句子语法正确，并使用适当的学术词汇。

**使用要点**：用于转述文献表述；改写后仍须规范引用来源，paraphrase ≠ 免引。

---

### 22. 改进论文章节指令
**适用环节**：润色（章节级连贯性）

**英文提示词模板：**
```text
Refine the following section of your research paper to enhance its logical flow and coherence: [粘贴你的部分].
```

> 中文翻译：修改你研究论文的以下部分，以增强其逻辑流程和连贯性：[粘贴你的部分]。

**使用要点**：针对整节（如 Methods/Discussion）做连贯性优化；适用于人工初稿后的整体打磨。

---

### 28. 翻译摘要指令
**适用环节**：翻译（中英互译等）

**英文提示词模板：**
```text
Translate the following abstract into [目标语言]: [粘贴你的摘要].
```

> 中文翻译：将以下摘要翻译成 [目标语言]：[粘贴你的摘要]。

**使用要点**：跨语言投稿（如中文期刊英文摘要）；译后请母语者或专业校对核校术语与语态。

---

## 七、投稿与回复审稿

### 29. 推荐投稿期刊指令
**适用环节**：选刊、投稿前

**英文提示词模板：**
```text
Generate a list of potential journals to submit your research paper on [你的研究主题], considering their scope, impact factor, and audience.
```

> 中文翻译：生成一份可以提交你关于 [你的研究主题] 的研究论文的潜在期刊列表，同时考虑其范围、影响因子和读者群。

**使用要点**：初筛候选期刊；最终结合期刊近期发文主题、开源政策、审稿周期与作者指南确认。

---

### 30. 撰写投稿信指令
**适用环节**：投稿信（Cover Letter）

**英文提示词模板：**
```text
Write a cover letter to accompany your research paper submission, highlighting the key contributions and novelty of your work.
```

> 中文翻译：写一封附在你研究论文提交材料中的投稿信，重点介绍你工作的关键贡献和新颖性。

**使用要点**：Cover Letter 突出 contribution + novelty；可复用指令 21 的论证素材，并按期刊模板补"推荐/回避审稿人"等字段。

---

## 附：「一周写完一篇 SCI」工作流清单

> 说明：源 PDF 标题为"一周写完一篇 SCI"，但正文未给出逐日日程表。以下清单**依据 30 条指令的逻辑顺序推导整理**，作为可执行的 7 天工作流参考，便于按环节检索与排期。

**Day 1 — 选题与方向确认**
- [ ] 指令 1 头脑风暴选题
- [ ] 指令 2 分析文献空白 + SMART 问题
- [ ] 指令 3 SWOT 评估研究想法
- [ ] 指令 27 统一关键术语定义

**Day 2 — 文献检索与综述**
- [ ] 指令 5 查找近 5 年高影响力文献
- [ ] 指令 4 主题化总结文献
- [ ] 指令 6 生成文献综述大纲

**Day 3 — 研究设计与方法**
- [ ] 指令 24 制定研究假设
- [ ] 指令 7 建议研究方法
- [ ] 指令 8 设计实验（含统计方案）
- [ ] 指令 9 评估方法优缺点
- [ ] 指令 26 识别并缓解伦理问题
- [ ] 指令 25 编写研究计划（预算/时间表）

**Day 4 — 数据分析与结果**
- [ ] 指令 10 数据分析与可视化
- [ ] 指令 11 结果解读（含支持/矛盾证据）

**Day 5 — 正文撰写（引言/方法/结果/讨论/摘要）**
- [ ] 指令 14 撰写引言
- [ ] 指令 20 搭建讨论大纲
- [ ] 指令 12 讨论研究意义
- [ ] 指令 21 论证研究意义
- [ ] 指令 19 撰写结论
- [ ] 指令 13 撰写摘要
- [ ] 指令 17 拟定标题 / 指令 18 生成关键词

**Day 6 — 润色与改写**
- [ ] 指令 15 改进段落
- [ ] 指令 22 改进章节连贯性
- [ ] 指令 16 改写句子（避免抄袭）
- [ ] 指令 23 识别方法论缺陷并补 Limitations
- [ ] 指令 28 如需翻译摘要

**Day 7 — 投稿**
- [ ] 指令 29 推荐/选定投稿期刊
- [ ] 指令 30 撰写投稿信（Cover Letter）
- [ ] 按期刊作者指南排版、校验格式后提交

> 提示：实际写作中可迭代反复调用（如先写雏形再润色）；"一周"为理想排期，需据数据完备度与领域难度弹性调整。审稿回复（Response to Reviewers）可复用指令 21（贡献论证）、指令 9/23（方法局限回应）的素材组织。
