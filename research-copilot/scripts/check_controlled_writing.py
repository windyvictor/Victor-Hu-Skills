#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_controlled_writing.py — 科研写作的语言质量底线体检（research-copilot 统一入口）

把两个引擎的结果合并成一份报告，并按"科研写作"对 ASD-STE100 的豁免清单做后处理：

  英文 → scripts/check_ste_compliance.py      （STE Issue 9 的可机械判定子集）
  中文 → scripts/check_plain_language.py      （中文受控写法 10 条）

为什么要后处理：STE 是航空维修文档的受控语言，直接套到论文上会误伤三类东西——
数学/形式化写作术语（assume / denote / bounds）、学术必需的模糊限制（may / should）、
以及方法与证明里的被动态与完成时。详见 references/controlled-scientific-writing.md 的豁免清单。

用法：
    python3 check_controlled_writing.py 稿件.md
    python3 check_controlled_writing.py 稿件.md --mode academic      # 默认
    python3 check_controlled_writing.py 操作手册.md --mode ste       # 不豁免，等同严格 STE
    python3 check_controlled_writing.py 稿件.md --lang zh            # 强制只跑中文
    python3 check_controlled_writing.py 摘要.md --json --strict
    cat 段落.md | python3 check_controlled_writing.py -
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
DICT_PATH = HERE.parent / "assets" / "ste-unapproved-words.tsv"
DOMAIN_PATH = HERE.parent / "assets" / "academic-domain-terms.txt"
STE_ENGINE = HERE / "check_ste_compliance.py"
CN_ENGINE = HERE / "check_plain_language.py"

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
LATIN = re.compile(r"[A-Za-z]+")

# ---------------------------------------------------------------- 学术豁免表

# kind → (academic 模式下的处置, 说明)
#   drop     直接丢弃（在学术写作里几乎总是误报）
#   info     降为 info
#   warn     降为 warn
#   keep     保留原级
ACADEMIC_EXEMPT: dict[str, tuple[str, str]] = {
    "完成时": ("warn", "学术英语在叙述既有文献的累积证据时保留现在完成时；只有描述本文单次动作才改过去时"),
    "进行时": ("keep", ""),
    "助动词被动构造": ("info", "数学写作中 “can be derived / can be solved” 是标准表达，不必强改主动"),
    "被动语态": ("warn", "方法章的 “was trained for 200 epochs” 可接受；只在主语缺失且读者需要知道执行者时才改主动"),
    "-ing 用法": ("info", "training / following / existing 等已在词典侧豁免，此处仅提示"),
    "疑似 multi-word noun 超 3 词": ("info", "术语型名词串（如 reinforcement-learning-based policy）不受此限"),
    "分号": ("warn", "学术文体允许分号分隔并列条件；只在使用者不确定时才拆句"),
    "缩略式": ("keep", "学术写作同样禁用缩写"),
    "拉丁缩写": ("drop", "et al. / e.g. / i.e. 是学术体例要求，不属违规；只要求全篇一致"),
    "英式拼写": ("warn", "学术写作只要求拼写全篇一致，不强制改成美式"),
    "短语动词（原书点名）": ("warn", "改法不是套用 DO，而是换成精确动词（run/train/solve/measure）"),
    "短语动词 [补充]": ("warn", "同上"),
    "条件位置": ("info", "学术论证中条件从句位置由论证需要决定，非硬性"),
    "must 误用": ("info", "学术写作少用祈使式，此处几乎不适用"),
    "NOTE 含祈使式": ("info", "仅当写可复现性说明/注意事项时才适用"),
    "NOTE 含限值": ("info", "同上"),
    "列表项标点": ("info", "条目用句号收尾即可，并列逗号不强制"),
    "未核准词": ("keep", "词表已预先剔除数学/形式化术语；命中即是真的模糊词"),
    "段落超长": ("warn", "方法章允许 6–8 句的长段；只有超过 8 句才必须拆"),
    "句长超限": ("relax", "科研写法上限放宽到 35 词；方法章含公式复杂度更高时允许再放宽"),
    "7.2": ("info", "仅当文档确实含 WARNING/CAUTION 时适用"),
    "7.3": ("info", "同上"),
    "安全指令起句": ("info", "同上"),
    "安全指令缺解释": ("info", "同上"),
    "安全指令缺具体危害": ("info", "同上"),
}

ACADEMIC_SENTENCE_LIMIT = 35      # 学术档句长上限（词）
ACADEMIC_PARAGRAPH_LIMIT = 8      # 学术档段落句数上限

# 中文侧同类豁免
CN_EXEMPT: dict[str, tuple[str, str]] = {
    "长句": ("relax", "允许到 40 字；摘要方法句含公式时允许再放宽"),
    "passive voice": ("warn", "同上：学术论文允许被动态"),
    "被动语态": ("warn", "同上：学术论文允许被动态"),
    "nominalisation": ("info", "数学名词（构造/映射/收敛性）本身是术语"),
    "名词化": ("info", "同上"),
    "-ing form": ("info", ""),
    "noun cluster": ("info", ""),
    "filler": ("warn", ""),
    "冗余词": ("warn", ""),
    "同义漂移": ("keep", "术语一致性是学术写作硬要求"),
    "的链过长": ("keep", ""),
}

ACADEMIC_CN_SENTENCE_LIMIT = 40

# ---------------------------------------------------------------- 套话清单（去 AI 味）
# 来源：references/academic-writing.md「减少空泛学术套话」与「英文学术表达」，
#       本机 SSD 把它数字化：原来只能靠读，现在能计数。

CN_BOILERPLATE = [
    "值得注意的是", "需要指出的是", "众所周知", "不难发现", "显而易见",
    "具有重要意义", "提供新的视角", "奠定了基础", "进一步推动", "充分体现",
    "具有广阔应用前景", "在一定程度上", "发挥着重要作用", "不容忽视",
    "综上所述", "众所周知的是", "我们可以看到", "由此可见",
]
EN_BOILERPLATE = [
    "it is worth noting that", "it should be noted that", "importantly",
    "delve into", "foster", "leverage", "in short", "the bottom line",
    "pave the way", "it is well known that", "needless to say",
    "plays an important role", "has attracted increasing attention",
]

# ---------------------------------------------------------------- 数据结构


@dataclass
class Finding:
    line: int
    engine: str          # STE / CN / SLOP
    rule: str
    kind: str
    detail: str
    text: str = ""
    severity: str = "warn"
    note: str = ""


@dataclass
class Stats:
    sentences: int = 0
    words: int = 0
    en: int = 0
    zh: int = 0
    findings: list = field(default_factory=list)

    def add(self, f: Finding) -> None:
        self.findings.append(f)


def score(st: Stats) -> int:
    if not st.sentences:
        return 100
    n = st.sentences
    hard = sum(1 for f in st.findings if f.severity == "hard")
    warn = sum(1 for f in st.findings if f.severity == "warn")
    info = sum(1 for f in st.findings if f.severity == "info")
    s = 100 - 100 * hard / n - 40 * warn / n - 12 * info / n
    return max(0, min(100, round(s)))


# ---------------------------------------------------------------- 语言分派


def classify(line: str) -> str | None:
    """判定一行的主要语言。返回 'en' / 'zh' / None（无可检内容）。"""
    s = line.strip()
    if not s or s.startswith(("#", ">", "|", "$")) or s.startswith("```"):
        return None
    cjk = len(CJK.findall(s))
    if cjk == 0:
        return "en" if LATIN.search(s) else None
    # 纯数学/表格导致 CJK 很少时按字符占比处理
    ratio = cjk / max(1, len(s))
    return "zh" if ratio > 0.12 or cjk >= 4 else ("en" if cjk <= 2 else "zh")


def mask_lines(lines: list[str], target: str) -> str:
    """保留目标语言的行，其余置空——用空行占位以保住原始行号。"""
    return "\n".join(l if classify(l) == target else "" for l in lines)


# ---------------------------------------------------------------- 引擎调用


def run_engine(engine: Path, path: Path, extra: list[str]) -> dict | None:
    cmd = [sys.executable, str(engine), str(path), "--json", *extra]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as e:
        print(f"[warn] 调用 {engine.name} 失败：{e}", file=sys.stderr)
        return None
    out = r.stdout.strip()
    if not out:
        if r.stderr.strip():
            print(f"[warn] {engine.name}: {r.stderr.strip()[:200]}", file=sys.stderr)
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        print(f"[warn] {engine.name} 输出不是合法 JSON", file=sys.stderr)
        return None


# ---------------------------------------------------------------- 后处理


def load_domain_terms(path: Path) -> set[str]:
    """读取领域术语豁免表（去掉 # 注释与空行）。"""
    terms: set[str] = set()
    if not path.exists():
        print(f"[warn] 缺少领域术语表：{path}（术语豁免已停用）", file=sys.stderr)
        return terms
    for ln in path.read_text(encoding="utf-8").splitlines():
        s = ln.split("#")[0].strip().lower()
        if s:
            terms.add(s)
    return terms


def load_base_forms():
    """复用 STE 引擎里的屈折还原函数，避免两份实现漂移。"""
    import importlib.util
    name = "_ste_engine"
    if name in sys.modules:
        return sys.modules[name].base_forms
    spec = importlib.util.spec_from_file_location(name, STE_ENGINE)
    mod = importlib.util.module_from_spec(spec)
    # 必须先注册：该模块带 `from __future__ import annotations`，dataclass 装饰器
    # 会按 sys.modules[cls.__module__] 反射类型注解，未注册会抛 AttributeError。
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod.base_forms


def matched_word(detail: str) -> str:
    """从 "word → ALT" 里取出被判定的那个词。"""
    return detail.split("→")[0].strip().strip("“”\"'").lower()


def apply_exemptions(f: Finding, table: dict, mode: str) -> Finding | None:
    """按豁免表调整严重级，返回 None 表示丢弃。"""
    if mode != "academic":
        return f
    action, note = table.get(f.kind, (None, ""))
    if action is None:
        action, note = table.get(f.rule, ("keep", ""))
    if action == "drop":
        return None
    if action == "info" and f.severity == "hard":
        f.severity = "info"
    elif action == "warn" and f.severity == "hard":
        f.severity = "warn"
    elif action == "relax":
        f.severity = relax_length(f.detail, f.severity)
    if note and action in {"warn", "info", "relax"}:
        f.note = note
    return f


def relax_length(detail: str, current: str) -> str:
    """句长/段长类：学术档按放宽后的阈值重新判定。

    两个引擎的措辞都带优化 IEC 61850 风格的「上限」字样（如 "74 字 > 上限 30 字"），
    正则必须容忍，否则 relax 静默失效、仍按 hard 报出。
    """
    lim = r"(?:上限\s*)?"      # 容掉「上限」二字
    m = re.match(rf"(\d+)\s*词\s*>\s*{lim}(\d+)\s*词", detail)
    if m:
        return "warn" if int(m.group(1)) > ACADEMIC_SENTENCE_LIMIT else "info"
    m = re.match(rf"(\d+)\s*字\s*>\s*{lim}(\d+)\s*字", detail)
    if m:
        return "warn" if int(m.group(1)) > ACADEMIC_CN_SENTENCE_LIMIT else "info"
    m = re.match(rf"(\d+)\s*words\s*>\s*{lim}\d+", detail)
    if m:
        return "warn" if int(m.group(1)) > ACADEMIC_SENTENCE_LIMIT else "info"
    m = re.match(rf"(\d+)\s*句\s*>\s*{lim}\d+\s*句", detail)
    if m:
        return "warn" if int(m.group(1)) > ACADEMIC_PARAGRAPH_LIMIT else "info"
    return current


# ---------------------------------------------------------------- 套话检查


def iter_blocks(lines: list[str]):
    """把软换行粘回逻辑段。yield (起始行号, 合并后的文本)。

    稿件常被硬折行，逐行查套话会把 "it is worth / noting that" 这类跨行短语漏掉。
    """
    buf: list[str] = []
    start = 0
    for i, raw in enumerate(lines, 1):
        s = raw.strip()
        if not s:
            if buf:
                yield start, " ".join(buf)
                buf = []
            continue
        if not buf:
            start = i
        buf.append(s)
        if s[-1] in ".。!！?？;；:：":        # 段落在此收尾
            yield start, " ".join(buf)
            buf = []
    if buf:
        yield start, " ".join(buf)


def check_boilerplate(lines: list[str], st: Stats) -> None:
    for start, text in iter_blocks(lines):
        low = text.lower()
        for term in CN_BOILERPLATE:
            if term in low:
                st.add(Finding(start, "SLOP", "去AI味", "中文套话",
                               f"“{term}” — 删掉，或换成具体事实/数据",
                               text[:60], "warn"))
        for term in EN_BOILERPLATE:
            if term in low:
                st.add(Finding(start, "SLOP", "去AI味", "英文套话",
                               f"“{term}” — 删掉，或改为直接陈述",
                               text[:60], "warn"))


# ---------------------------------------------------------------- 主流程


def process(name: str, raw: str, args: argparse.Namespace) -> tuple[Stats, list[Finding]]:
    lines = raw.splitlines()
    st = Stats()
    dropped: list[Finding] = []

    tmp_ste = tmp_cn = None
    try:
        en_lines = sum(1 for l in lines if classify(l) == "en")
        zh_lines = sum(1 for l in lines if classify(l) == "zh")
        st.en, st.zh = en_lines, zh_lines

        run_en = args.lang in {"auto", "en", "both"} and en_lines > 0
        run_zh = args.lang in {"auto", "zh", "both"} and zh_lines > 0
        if args.lang == "en":
            run_zh = False
        if args.lang == "zh":
            run_en = False

        # --- 英文 ---
        if run_en:
            fd, p = tempfile.mkstemp(suffix=".md", prefix="rc-en-")
            os.close(fd)
            tmp_ste = Path(p)
            tmp_ste.write_text(mask_lines(lines, "en"), encoding="utf-8")
            extra = ["--no-dictionary"] if args.no_dictionary else ["--dict", str(DICT_PATH)]
            data = run_engine(STE_ENGINE, tmp_ste, extra)
            if data:
                st.sentences += data["stats"].get("sentences", 0)
                st.words += data["stats"].get("words", 0)
                domain = load_domain_terms(DOMAIN_PATH)
                base_forms = load_base_forms()
                for f in data["findings"]:
                    nf = Finding(f["line"], "STE", f.get("rule", ""), f["kind"],
                                 f["detail"], f.get("text", ""), f["severity"])
                    if args.mode == "academic" and nf.kind == "未核准词":
                        # 术语豁免：数学/统计/ML/机器人的行话不该被判成冗词。
                        # 命中词可能是变位形式（remains / utilizes），要还原后再查表。
                        surface = matched_word(nf.detail)
                        if surface in domain or any(b in domain for b in base_forms(surface)):
                            dropped.append(nf)
                            continue
                        # 其余词典命中在学术散文里多为"可替换的模糊词"，属建议而非硬错
                        nf.severity = "warn"
                        nf.note = ("词表源自航空维修受控语言；术语已在 "
                                   "assets/academic-domain-terms.txt 豁免，"
                                   "剩下的多为可换成的精确动词/介词")
                        st.add(nf)
                        continue
                    kept = apply_exemptions(nf, ACADEMIC_EXEMPT, args.mode)
                    if kept is None:
                        dropped.append(nf)
                    else:
                        st.add(kept)

        # --- 中文 ---
        if run_zh:
            fd, p = tempfile.mkstemp(suffix=".md", prefix="rc-zh-")
            os.close(fd)
            tmp_cn = Path(p)
            tmp_cn.write_text(mask_lines(lines, "zh"), encoding="utf-8")
            data = run_engine(CN_ENGINE, tmp_cn, [])
            if data:
                st.sentences += data["stats"].get("cn_sentences", 0) or data["stats"].get("sentences", 0)
                for f in data["findings"]:
                    nf = Finding(f["line"], "CN", "", f["kind"], f["detail"],
                                 f.get("text", ""), f["severity"])
                    kept = apply_exemptions(nf, CN_EXEMPT, args.mode)
                    if kept is None:
                        dropped.append(nf)
                    else:
                        st.add(kept)

        # --- 套话（中英都查）---
        if not args.no_slop:
            check_boilerplate(lines, st)

    finally:
        for t in (tmp_ste, tmp_cn):
            if t and t.exists():
                try:
                    t.unlink()
                except OSError:
                    pass

    return st, dropped


def render(name: str, st: Stats, dropped: list[Finding], max_items: int, mode: str) -> str:
    order = {"hard": 0, "warn": 1, "info": 2}
    items = sorted(st.findings, key=lambda f: (order[f.severity], f.line))
    counts = {k: sum(1 for f in items if f.severity == k) for k in order}
    out = [f"== 科研写作语言底线体检 · {name} ==",
           f"   模式 {'学术档（已应用科研豁免）' if mode == 'academic' else '严格 STE 档'}", ""]

    if not items:
        out.append("  未发现可机械判定的问题。")
    else:
        out.append(f"  命中 {len(items)} 条（hard {counts['hard']} / warn {counts['warn']} / info {counts['info']}）：")
        for f in items[:max_items]:
            tag = f.engine
            out.append(f"  [{f.severity:<4}] L{f.line:<5} {tag:<4} {f.kind}：{f.detail}")
            if f.text:
                out.append(f"  {'':<26}↳ {f.text}")
            if f.note:
                out.append(f"  {'':<26}※ {f.note}")
        if len(items) > max_items:
            out.append(f"  … 还有 {len(items) - max_items} 条，加 --max-items 或 --json 查看全量")

    out += ["", "  统计：",
            f"    句 {st.sentences} · 约 {st.words} 词 · 英文行 {st.en} · 中文行 {st.zh}"]
    if mode == "academic" and dropped:
        kinds = {}
        for f in dropped:
            kinds[f.kind] = kinds.get(f.kind, 0) + 1
        out.append(f"    已按科研豁免屏蔽 {len(dropped)} 条：" + " · ".join(f"{k} {v}" for k, v in kinds.items()))
        out.append("    （严格 STE 对比用 --mode ste；被屏蔽不代表原文有问题，见 references/controlled-scientific-writing.md §3）")

    sc = score(st)
    grade = "优" if sc >= 85 else ("良" if sc >= 70 else ("及格" if sc >= 55 else "需重写"))
    out += ["", f"  评分 {sc}/100（{grade}）", "",
            "  说明：只报线索，不做终判。术语 vs 冗词、hedging 是否恰当，机器判不了。"]
    return "\n".join(out)


def render_json(name: str, st: Stats, dropped: list[Finding], mode: str) -> str:
    return json.dumps({
        "file": name, "mode": mode, "score": score(st),
        "stats": {"sentences": st.sentences, "words": st.words,
                  "en_lines": st.en, "zh_lines": st.zh},
        "findings": [{"line": f.line, "engine": f.engine, "rule": f.rule, "kind": f.kind,
                      "severity": f.severity, "detail": f.detail, "text": f.text, "note": f.note}
                     for f in sorted(st.findings, key=lambda f: f.line)],
        "suppressed_by_academic_exemption": [
            {"line": f.line, "engine": f.engine, "kind": f.kind, "detail": f.detail}
            for f in dropped],
    }, ensure_ascii=False, indent=2)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="科研写作语言底线体检（ASD-STE100 子集 + 中文受控写法 + 去 AI 味）",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help="待检查文件，或 - 表示读 stdin")
    ap.add_argument("--mode", default="academic", choices=["academic", "ste"],
                    help="academic=应用科研豁免（默认）；ste=不豁免的严格 STE")
    ap.add_argument("--lang", default="auto", choices=["auto", "en", "zh", "both"],
                    help="语言；默认 auto 按行自动判定")
    ap.add_argument("--no-dictionary", action="store_true", help="跳过未核准词检查")
    ap.add_argument("--no-slop", action="store_true", help="跳过套话（去 AI 味）检查")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="只输出评分")
    ap.add_argument("--strict", action="store_true", help="有 hard 级问题则退出码 1")
    ap.add_argument("--max-items", type=int, default=60)
    args = ap.parse_args()

    worst = 0
    for target in args.files:
        try:
            raw = sys.stdin.read() if target == "-" else Path(target).read_text(
                encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"无法读取 {target}: {e}", file=sys.stderr)
            worst = max(worst, 2)
            continue

        st, dropped = process(target, raw, args)
        hard = sum(1 for f in st.findings if f.severity == "hard")
        if hard:
            worst = max(worst, 1)

        if args.json:
            print(render_json(target, st, dropped, args.mode))
        elif args.quiet:
            print(f"{target}: {score(st)}/100")
        else:
            print(render(target, st, dropped, args.max_items, args.mode))
            print()

    if args.strict and worst == 1:
        return 1
    return worst


if __name__ == "__main__":
    sys.exit(main())
