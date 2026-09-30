# 项目长期记忆 — Skills 仓库（My Skills）

## 仓库定位

胡老师把 `My Skills/`（坚果云内）下的全部 skill 开源到 GitHub 共享。
面向中英文双语受众，以学术科研类 skill 为主体。

## 文档约定（2026-09-30 确立，胡老师确认「全部保留」）

### 两层 README 结构

| 层级 | 文件 | 读者 | 职责 |
|---|---|---|---|
| 第一层 | 仓库根 `README.md`（**英文，默认**） | 人 | GitHub 首页渲染的门面：总览、四分类索引表、场景对照表、安装、组合用法、版权声明 |
| 第一层 | 仓库根 `README.cn.md`（中文） | 人 | 同上，中文版；两文件顶部**第 3 行**各有语言切换行 |
| 第二层 | 各 skill 目录下 `README.md` | 人 | 详情页：一句话定位 / 解决什么问题 / 何时触发 / 内容结构树 / **参考资料·灵感来源** / 典型用法 |

### 参考资料清单约定（2026-09-30 胡老师要求，用于规避版权纠纷）

- **13 个 skill 的 README 全部设有 `## 参考资料 / 灵感来源` 小节**，位置在「内容结构」之后、
  「典型用法」之前。
- 固定格式：标题 → 声明引用块（结构化整理、无大段原文复制、侵权即删）→
  三列表格 `| 来源 | 作者 / 出处 | 借鉴内容 |`。来源多时按 A/B/C 主题分组。
- **原则：只写文件里实际记录的来源，绝不臆造作者。** 提取方法：
  `head -6 "$f" | grep -E "^>"` 批量抓 `> 来源：` 标注。
- 无外部来源的 skill（research-copilot、academic-deai-writing）**据实写「原创」**，
  并留一句「如后续引入外部方法论请增补署名」。
- 来源不明时**显式标注风险**（academic-paper-prompts 的两份网络流传 PDF、
  ai-research-methodology 的实战手册、human-3-skill 的初始中文 Prompt）。
- 各 skill 的权威来源清单位置（新增/更新来源时先看这里）：
  - `graduate-research-career/references/12-source-map.md`（20 部文档完整索引，最详尽）
  - `research-paper-writing/README.md`（7 组 38 行，最庞大）
  - `ai-gongwen-writing/SKILL.md` 尾部来源说明（明确区分手册内容 / 国标 / 自研补全）

### 命名约定（2026-09-30 胡老师指定）

- **英文版文件名固定为 `README.md`**（英文升为默认，英文为国际开源主语言）。
- **中文版文件名固定为 `README.cn.md`**（胡老师明确选用 `.cn`，**不是** 更常见的 `.zh-CN`；
  如需改为社区惯例 `README.zh-CN.md` 需先征求同意）。
- **GitHub 只自动渲染 `README.md`，且无内置多语言切换**（已查证）。
  因此根目录**必须保留一个 `README.md`**，中英文切换只能靠文件顶部的链接行实现。
- 语言切换行位置：紧跟 H1 标题之后的第 3 行，两文件保持一致。
  格式：`**English | [中文](./README.cn.md)**` / `**中文 | [English](./README.md)**`。

### 关键原则

- **`SKILL.md` 是唯一必需文件**，平台只读它；`README.md` 不会被 Agent 读取，纯人类文档。
- **`SKILL.md` 会被加载进模型上下文（占 token、参与触发）**，因此
  「给人看的啰嗦说明」一律放 `README.md`，**不要塞进 SKILL.md**。
- **每个 skill 目录都要有 `README.md`**（胡老师选择全量保留，一致优先于精简）。
  新增 skill 时按同一模板补一份。
- 已知同步负担仅两处：README 的「内容结构树」（随文件增减更新）与「何时触发」
  （与 SKILL.md 的 `description` 字段重叠）。改动 SKILL.md 时需回看这两处。

## 目录内 skill 分组（4 组 13 个）

- **A 科研写作与产出**：research-paper-writing、academic-deai-writing、
  academic-paper-prompts、grant-proposal-ai、ai-research-methodology
- **B 文献阅读与知识管理**：critical-paper-reading、socratic-reading、zettelkasten-notes
- **C 科研协作与生涯**：research-copilot、graduate-research-career
- **D 职场写作与通用思维**：ai-gongwen-writing、modern-thinking-toolkit、human-3-skill

## 已确定：许可证与署名（2026-09-30 胡老师决定）

- **整仓采用 MIT License**，`LICENSE` 已创建于仓库根目录。
- **版权署名**：`Copyright (c) 2026 Jin Hu`。
  来源：本机 `git config --global user.name` = "Jin Hu"、`user.email` = "jhu@cqjtu.edu.cn"、
  macOS 账户全名 = "胡进"。**如需改用中文名或其他形式，须先征求同意。**
- 两个根 README 的 License 章节已统一为 MIT，并加了「MIT 只覆盖作者本人贡献，
  **不改变**第三方原始素材的权利归属」的说明；结构树中 `LICENSE` 注释同步更新。
- ⚠️ 原「代码 MIT + 文档 CC BY-NC-SA 4.0」的分层建议**已废弃**，不要重提。
- ⚠️ 已向胡老师提示：MIT 允许商业使用与闭源再分发，与「部分内容提炼自商业出版物」
  存在张力（他知情后仍选 MIT）。

## 已确定：引用规范（2026-09-30，四轮执行）

开源前对全库实施引用规范化：**① 直接引用原文必须加引号并注明出处；② 能自己写的就自己写；
③ 提示词类不改写（改写即失值），改为「原文引用 + 标注来源」；④ 引文卡片须「引号 + 出处页码
+ 自己的注解」，禁无出处大段摘抄。**

已落实：modern-thinking-toolkit **147 处金句补注讲次**；academic-paper-prompts、
ai-research-methodology、research-paper-writing、zettelkasten-notes 等加引用声明/版权提示；
根 README（中英）版权声明改为「三类内容分治表」（提炼改写 / 原文引用已标注 / 版权受限第三方）。

⚠️ **开源前必查三项**：① **本地绝对路径泄露**（`/Volumes/…`，已清 2 处）；
② **第三方名称误标**（"Nature 推荐"实为自媒体汇编，已更正 6 处）；③ **第三方授权条款**
（不可假设为 CC 系列——Phrasebank 实为「个人使用、禁电子分发」）。

⚠️ **工具坑**：macOS 的 BSD grep **不支持 `\|` 交替**，`grep "a\|b"` 静默返回空、
会误判「无残留」。**务必用 `grep -E` 或 Grep 工具（ripgrep）**。

⚠️ **本轮已向胡老师说明的重要判断**：第 ② 条（只留方法骨架）**不适用于 prompt 类 skill**
——`academic-paper-prompts` 的核心价值就是可直接复制的提示词，全部改写即使其失效；
该处应适用第 ③ 条（原文引用 + 标注），**功能性优先**。

## 已决定：版权风险采「保留现状 + 事后响应」策略（2026-09-30 胡老师拍板）

**胡老师决定：全部保留不变，不预先削减任何内容；出问题再解决。** 原四个待决项
（Phrasebank 432 条句式、academic-paper-prompts 来源不明、human-3-skill 授权、
README 英译）**暂不处理，不再追问**。除非胡老师主动提起，不要重复提醒这些风险。

→ 这意味着：**接受「先发布、遇投诉再响应」的风险模型**。已在两个根 README 写入
「侵权即删」承诺，作为响应机制的公开依据。

### 应急预案：若收到权利人通知，快速处置路径（备忘，勿主动展示）

| 风险等级 | 文件 | 处置动作 |
|---|---|---|
| 高 | `research-paper-writing/references/academic-english-phrases.md`、`phrasebank-extended.md` | 432 条 Phrasebank 句式，整体移除或削减至每类 3–5 条示例 |
| 高 | `modern-thinking-toolkit/references/gaoyan-*.md`、`laoyu-*.md` 等 | 147 处金句引用（已标注讲次），删除引用行或改为纯要点概括 |
| 中 | `academic-paper-prompts/references/prompt-schemes-*.md`、`nature-30-prompts.md` | 提示词原文，替换为自写等价提示词 |
| 中 | `ai-gongwen-writing/`、`grant-proposal-ai/`、`zettelkasten-notes/` | 按通知范围缩减相应章节 |

处置通用动作：① 该文件加删除或替换；② 根 README 与对应 skill README 的来源清单同步更新；
③ 提交信息写清原因，保留可追溯性。**处置前先备份到 `/tmp/`。**

## 待决事项（未完成）

1. **各 skill 的 README 未做英译**（仍为中文）。— 唯一遗留项，胡老师未要求推进。
