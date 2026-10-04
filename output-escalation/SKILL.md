---
name: output-escalation
description: Choose the highest-leverage output medium for a message, and escalate beyond plain text when reading is the bottleneck. Use this skill when explaining, teaching, clarifying, illustrating, or presenting anything — especially when the content involves structure, process, dynamics, comparison, or spatial and temporal reasoning. It supplies a five-rung escalation ladder (controlled plain-language writing, diagrams and tables, single-file interactive HTML explainer, narrated explainer video, discardable software artifact) with ready templates and scripts for every rung, and a full implementation of ASD-STE100 Simplified Technical English (Issue 9, all 53 writing rules plus the controlled dictionary) for writing that must be unambiguous, checkable, and translatable. Triggers: "explain X", "讲清楚", "讲解一下", "给我看看", "画个图", "做个可视化", "做个讲解网页", "做个讲解视频", "make this clearer", "show me", "visualize this", "explainer", "teach me", "ASD-STE100", "Simplified Technical English", "受控英语", "受控语言", "技术文档写作规范", "检查这段英文有没有违规", "简化这段英文", "写操作手册/维修手册/SOP".
agent_created: true
---

# Output Escalation — 输出升维阶梯

## 这个技能解决什么问题

大多数回复的默认介质是文字。但文字不是最省力的介质。读者的成本在"把线性符号在脑内重建
成结构"这一步。当这一步变贵时，就换介质。

**第一原则：先判断读者的力气该花在哪里，再选介质。**

- 力气该花在**记住一个结论** → 一句话，或用受控语言写成极短的段落。
- 该花在**看清结构、关系、流程、对比** → 图。
- 该花在**自己动手试、看参数变化** → 可交互网页。
- 该花在**跟着一条时间线走完一段叙事** → 图解视频。
- 该花在**反复做同一件事** → 一个用完即弃的小工具。

推论（Karpathy 的核心判断）：模型能力与代码都在变得充裕，所以可以索要"大型、定制、
用完即弃"的软件件——网页、视频、模拟器。这类东西以前只有专门立项才值得做，现在不值
得多想一秒。**默认思维要从"我能说出什么"改成"什么东西能让对方最快看懂"。**

## 触发后的第一步：选级，不选内容

选级发生在写正文之前。不要先写一大段文字再想"要不要配图"。

### 五级阶梯

| 级 | 介质 | 读者的动作 | 什么时候停在这里 |
|---|---|---|---|
| **R0** | 直接答 | 读一行 | 结论唯一、无结构、无争议。**默认从这里起，够用就不要升。** |
| **R1** | 受控文字 | 逐句读，不用重读 | 需要精确复述/执行（SOP、讲义、说明书、给对方的正式回复）。用 **ASD-STE100** 受控语言约束：`references/rung-1-controlled-writing.md`（分档与中文等价）→ `references/ste-writing-rules.md`（53 条规则）→ `references/ste-dictionary.md`（受控词典） |
| **R2** | 表格 / 图 | 扫一眼，看拓扑 | 内容主体是**结构、关系、先后、阶段、对比、空间布局**。见 `references/rung-2-diagrams.md` |
| **R3** | 单文件交互网页 | 拖、点、悬停、看动画 | 需要**参数化试探**（改一个量看结果变化）、需要**时间演化**、需要分享出去一份自解释的东西。见 `references/rung-3-html-explainer.md` |
| **R4** | 图解视频 | 看，不用想 | **线性叙事 + 时间演化**，且值得被反复观看/转发/当仪式感内容。见 `references/rung-4-explainer-video.md` |
| **R5** | 可丢弃软件件 | 当作工具用 | 同一件事会被反复做，或需要成为一个可操作的物件（计算器、模拟器、播放器）。见 `references/rung-5-discardable-artifacts.md` |

### 升维判据（命中就考虑升一级）

- **重读信号**：读者要回看上一段才能理解这一段。
- **结构信号**：说明里出现"三个部分""相互""先后""取决于"。
- **空间信号**：讲的是布局、位置、方向、距离。
- **时间信号**：讲的是状态迁移、演化、收敛、衰减。
- **试探信号**：对方会问"如果 X 变大会怎样"。
- **重复信号**：这是这周第三次讲同一件事。

### 降级判据（命中就必须停在低级）

- 结论一句话能说清，却做了个视频 → 这是噪音，不是表达。
- 产出时间远超问题本身的重量（一句话的问题配 3 分钟视频）。
- 对方在手机上看、在会议上抢时间、只需要一个数字。
- 你要解释的东西本身没有结构，只是常识。

**升维有成本：产出时间、对方的学习成本、以及"看起来在认真"的表演风险。** 升维的正当理由
永远是"阅读是瓶颈"，不是"这样显得完整"。

## 各级的质量底线

每级都有硬约束。**细节在对应 reference 里，这里只放不可违背的几条。**

- **R1**：一句一事；主动语态；只用一个词表达一个意思；多步骤用竖排列表而不是长句。
  **六个数字记牢**（都是含上限）：程序句 20 词 · 描述句 25 词 · NOTE 25 词 · 每段 6 句 · multi-word noun 3 词 · 分号禁用。
- **R2**：一图一主张；图题写结论而不是写"XX 示意图"；颜色语义固定（中国场景：涨红跌绿）。
- **R3**：单文件自包含；深浅两套主题都要能读（浅底深字 / 深底浅字，绝不深底深字）；
  首屏 3 秒内可读；动效 ≤ 400ms 且尊重 `prefers-reduced-motion`。
- **R4**：旁白先写、画面后配（画面为旁白服务）；每段停留 = 旁白时长 + 0.3s；1920×1080 / 30fps。
- **R5**：一个工具只解决一个动作；能离线跑；有明确的输入输出；用完可以删。

## 组合使用

阶梯不是互斥的，是**叠放**的。高阶介质里的文字仍然要过 R1 这一关：

- 网页的文案、图注、按钮文字 → 用受控写法。
- 视频的旁白、字幕 → 用受控写法（这是决定视频好不好懂的最大变量）。
- 图里的标签 → 用受控写法，且更短。

一个好组合：**R3 网页里嵌 R2 图 + R4 视频短片 + R1 受控文字**。网页是外壳，其余是内容。

## R1 的底座：ASD-STE100 的完整实现

R1 不是"文风建议"，是一门**受控自然语言**（ASD-STE100 *Simplified Technical English*, Issue 9, 2025）。
它由两部分组成：**Part 1 写作规则**（9 节 53 条）与 **Part 2 受控词典**（875 个核准词 + 1274 个未核准词）。
两者都在本技能里落成了可直接用的文件——规则逐条带判据与例外，词典带 244 条高频替换表，另有一个把
53 条里可机械判定的部分全做进去的检查脚本。

**什么时候真的需要用完整 STE**：写安全规程、维修/操作手册、SOP、需要翻译成多语言的技术文档、
或任何"读者会照着做、做错会出事"的文本。**日常回复用 80% 版就够**——分档标准见
`references/rung-1-controlled-writing.md` 第 1 节。

三个最容易被忽略但一直在起作用的约束：
1. **一个词只准一个含义**（Rule 1.3 + 9.2）——`see` 只表示"用眼看到"，想表达"弄清"必须写 `make sure`。
2. **时态只有 6 种**（Rule 3.2）——没有完成时、没有进行时。时间关系靠词汇而非屈折变化。
3. **词数是可算的**（Rule 8.4–8.7）——数字、缩写、连字符词、括号内容各算一个词，所以句长上限是可被机器检查的。

## 资源索引

| 文件 | 用途 |
|---|---|
| `references/rung-1-controlled-writing.md` | **R1 入口**：三档强度（完整 STE / 80% 版 / 中文受控写法）、软化清单、中文 10 条等价约束、提示词模板 |
| `references/ste-writing-rules.md` | **ASD-STE100 Issue 9 全 53 条规则**（§1 用词 → §9 写作实践）+ GR-1~GR-8 + 阈值速查 + 可机械判定清单 |
| `references/ste-dictionary.md` | 受控词典机制：条目解剖、词性限制、未核准词 4 条出路、**244 条高频"未核准词 → 核准替代词"对照表** |
| `references/rung-2-diagrams.md` | 何时图优于文、图型选择表、绘图铁律、常见错误 |
| `references/rung-3-html-explainer.md` | 单文件交互网页的工程硬约束、页面叙事骨架、交互模式库、交付方式 |
| `references/rung-4-explainer-video.md` | 3b1b 风格要素、四步流水线、TTS 三种方案（本地免费 / edge-tts / ElevenLabs）、ffmpeg 命令配方、常见坑 |
| `references/rung-5-discardable-artifacts.md` | 可丢弃软件件的判断法、最小实现约定、边界 |
| `assets/ste-checklist.md` | **单页自查清单**：写作 / 改稿时最常用的入口（⚙ 标记项可交给脚本查） |
| `assets/html-explainer-template.html` | 可直接改的单文件网页骨架（主题自适应 + 三种交互模式） |
| `assets/video-scenes.example.json` | 视频场景清单示例（喂给下面那个脚本） |
| `assets/ste-unapproved-words.tsv` | 244 条未核准词 → 核准替代词（供检查脚本调用） |
| `scripts/check_ste_compliance.py` | **英文严格 STE 自检**：分号/缩略式/句长 20·25·25/段落 6 句/完成时/进行时/助动词被动/被动/-ing/短语动词/拉丁缩写/英式拼写/未核准词/列表结构/安全指令三段式，按 Rule 8.4–8.7 计词 |
| `scripts/check_plain_language.py` | 中文 + 通用可读性自检：长句/被动/名词化/-ing/名词簇/"的"链/冗余词/同义漂移 |
| `scripts/build_explainer_video.py` | **R4 一键成片**：`say`/edge-tts 配音 + 场景图 → mp4（支持 `--drawtext` / `--music` / `--srt` / `--dry-run`） |

## 工作流

1. **判级**：用上面的升维/降级判据定级，并用一句话说明理由。
2. **写底盘**：无论哪级，先把文字写成受控风格。英文跑 `scripts/check_ste_compliance.py <草稿.md>`，
   中文跑 `scripts/check_plain_language.py <草稿.md>`。要写严格 STE 文档时，先读
   `references/rung-1-controlled-writing.md` 定档，再按 `references/ste-writing-rules.md` 逐节执行。
3. **造介质**：按对应 reference 的硬约束产出。R3 从 `assets/html-explainer-template.html` 起手；R4 从 `assets/video-scenes.example.json` 起手。
4. **自检**：对照该级的质量底线逐条过。
5. **交付**：落盘到工作目录，用 `present_files` 打开预览（HTML 会进预览面板）。
6. **回话**：最终回复里说明"选了这一级、为什么、以及有没有更省力的替代级"。
