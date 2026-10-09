# 英文论文专用提示词

英文科研论文在中文规则之外追加以下限制。使用时整段复制，把 `【Paste text here】` 替换为目标文本。
若处理的是完整章节，可先套用 `prompts-sections.md` 中对应章节的中文逻辑，再用本提示词做英文层面的清洗。

```text
Revise the following academic text for clarity, precision, and natural scholarly prose.

Preserve all scientific claims, data, citations, terminology, equations, and qualifications.

Avoid stock AI-generated transitions and filler expressions when they add no information, including phrases such as:

"it is worth noting"
"importantly"
"it should be noted that"
"delve into"
"foster"
"leverage"
"in short"
"the bottom line"
"this is not X but Y"

Do not mechanically replace these expressions with synonyms. Rewrite the sentence so that the underlying fact, relationship, evidence, consequence, or implication is stated directly.

Prefer concrete nouns and precise verbs over abstract nominalizations.

Do not exaggerate novelty, significance, causality, or generalizability.

Use technical terminology when it is standard and necessary in the field, but avoid unnecessary jargon.

Do not turn prose into bullet points unless the information is genuinely parallel or procedural.

Avoid repetitive paragraph structures and mechanical concluding sentences.

Maintain logical continuity between sentences. Each sentence should either add evidence, explanation, qualification, comparison, or a necessary transition to the argument.

Where the text discusses a key technical step, method, mechanism, or innovation, give it appropriate explanatory weight rather than spending disproportionate space on generic background.

Output only the revised text.

Text:

【Paste text here】
```
