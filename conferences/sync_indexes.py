"""Refresh both homepages and shared indexes from conference card links."""

from collections import defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
VENUES = {"corl-2026": "CoRL 2026", "neurips-2026": "NeurIPS 2026", "cvpr-2026": "CVPR 2026"}
START = "<!-- conference-classification:start -->"
END = "<!-- conference-classification:end -->"
CARD = re.compile(r"(cards(?:-\d{4})?\.md)#(paper-[\w-]+)")

# Earlier conference indexes use free-form labels. Preserve these labels in
# the conference pages and map recognizable labels to the shared taxonomy.
DOMAINS = {
    "robotics": r"具身|机器人|VLA|^操作|自动驾驶|导航|^控制",
    "multimodal": r"多模态|视觉语言|跨模态|音视频",
    "llm": r"语言模型|大模型|LLM|Agent|智能体|代码|软件工程",
    "computer-vision": r"视觉|图像|视频|三维|点云",
    "nlp": r"自然语言|语音|文本|翻译|语言学",
    "reinforcement-learning": r"强化学习|模仿学习|博弈|马尔可夫|决策",
    "scientific-ml": r"科学|物理|医学|生物|化学|分子|气象|材料|药物|基因|蛋白|地球|能源|PDE",
    "graph-and-recommendation": r"图学习|图神经|推荐|知识图谱|图表示|图算法",
    "ml-foundations": r"统计|优化|理论|机器学习|深度学习|生成|时间序列|联邦|因果|可解释|表征|扩散|安全|系统|隐私|持续学习",
}
TECHNIQUES = {
    "evaluation": r"评测|评估|诊断|基准|消融|测量|检测|审计|解释|度量|失效|验证",
    "loss-functions": r"损失|正则|辅助监督|目标函数|对比目标|力监督",
    "reinforcement-learning": r"强化学习|奖励|信用分配|探索|策略梯度|策略优化|价值学习|价值估计|演员|Actor.Critic|偏好优化",
    "data-strategies": r"数据|采集|标注|筛选|课程生成|重采样|增强|样本选择",
    "training-strategies": r"训练|蒸馏|微调|迁移|持续学习|模型合并|行为克隆|监督",
    "inference": r"推理|解码|搜索|部署|规划|测试时|调度|缓存|量化|剪枝|采样|执行|生成",
    "optimization": r"优化|求解|梯度|近端|最优传输|变分|参数更新",
    "theory-statistics": r"理论|统计|界|收敛|校准|贝叶斯|保证|可辨识|因果|估计|不确定性",
    "representation-learning": r"表征|表示|编码|对齐|嵌入|特征|潜空间|几何",
    "architecture": r"架构|世界模型|神经算子|网络|动力学|专家模型|状态空间",
    "modules": r"模块|注意力|门控|路由|记忆|组件|融合|接口|连接",
}


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, content):
    if not path.exists() or read(path) != content:
        path.write_text(content, encoding="utf-8", newline="\n")


def category(label, taxonomy):
    for part in label.split(" / "):
        for key, pattern in taxonomy.items():
            if re.search(pattern, part, re.IGNORECASE):
                return key
    return "pending-classification"


def conference_links():
    domains, techniques = defaultdict(list), defaultdict(list)
    for venue in VENUES:
        directory = ROOT / "conferences" / venue
        rows = {}
        for path in [directory / "README.md", *sorted(directory.glob("index-*.md"))]:
            for line in read(path).splitlines():
                if not line.startswith("| ") or not CARD.search(line):
                    continue
                domain, technique, link, _ = line[2:].split(" | ", 3)
                file, anchor = CARD.search(link).groups()
                assert anchor not in rows, (venue, anchor)
                rows[anchor] = file
                title = link[:link.rindex("](")] + "]"
                for groups, key in ((domains, category(domain, DOMAINS)),
                                    (techniques, category(technique, TECHNIQUES))):
                    groups[key].append((venue, file, anchor, title))
        anchors = [(anchor, path.name) for path in directory.glob("cards*.md")
                   for anchor in re.findall(r'id="(paper-[\w-]+)"', read(path))]
        assert len(anchors) == len(rows) and dict(anchors) == rows, venue
    return domains, techniques


def update_index(path, entries, english, index_type, neurips_provisional):
    pending = path.stem == "pending-classification"
    if pending:
        heading = "Pending classification" if english else "待归类"
        back = "../../README.en.md" if english else "../README.md"
        body = f"# {heading}\n\n[{'Home' if english else '首页'}]({back})\n"
    else:
        body = read(path).split(START, 1)[0].rstrip() + "\n"
    # Count the card links shown to readers. The domain view counts each
    # paper once even when it contributes multiple technical mechanisms.
    existing = re.findall(r"^- .*?\]\(([^\n)]+\.md#[\w-]+)\)", body, re.M)
    if index_type == "papers":
        existing = {item.split("#", 1)[-1] for item in existing}
    if entries:
        prefix = "../../" if english else "../"
        lines = [START]
        for venue in VENUES:
            links = [f"- {title}({prefix}conferences/{venue}/{file}#{anchor})"
                     for v, file, anchor, title in entries if v == venue]
            if links:
                name = VENUES[venue]
                if venue == "cvpr-2026" or (venue == "neurips-2026" and neurips_provisional):
                    name += " (provisional)" if english else "（暂收录）"
                lines.extend([f"## {name}", "", *links, ""])
        body += "\n" + "\n".join([*lines, END, ""])
    write(path, body)
    return len(existing) + len(entries)


def sync():
    domains, techniques = conference_links()
    neurips_provisional = not (ROOT / "conferences/neurips-2026/final-selection.tsv").exists()
    previous_totals = None
    for english, home_name in ((False, "README.md"), (True, "README.en.md")):
        home = ROOT / home_name
        content = read(home)
        content = re.sub(
            r"^\| \[(?:CoRL|NeurIPS) 2026\]\(conferences/[^)]+\) \| .*\n",
            "", content, flags=re.M,
        )
        totals = []
        for folder, groups in (("papers", domains), ("insights", techniques)):
            prefix = ("en/" if english else "") + folder
            pending = f"{prefix}/pending-classification.md"
            content = re.sub(rf"^\| .*\]\({pending}\) \| .*\n", "", content, flags=re.M)
            pattern = rf"^(\| .*?\]\(({prefix}/([^)/]+)\.md)\) \| )([\d,]+)( \|.*)$"
            matches = list(re.finditer(pattern, content, re.M))
            assert len(matches) == (9 if folder == "papers" else 11)
            keys = {m[3] for m in matches}
            assert set(groups) <= keys | {"pending-classification"}
            counts = {m[3]: update_index(ROOT / m[2], groups[m[3]], english, folder, neurips_provisional)
                      for m in matches}
            fallback = update_index(ROOT / pending, groups["pending-classification"],
                                    english, folder, neurips_provisional)
            count = sum(counts.values()) + fallback
            totals.append(count)
            offset = matches[-1].end()
            if fallback:
                counts["pending-classification"] = fallback
                label = "Pending classification" if english else "待归类"
                detail = ("Conference labels awaiting taxonomy mapping" if english
                          else "会议原标签待映射到统一分类。")
                content = content[:offset] + f"\n| [{label}]({pending}) | {fallback:,} | {detail} |" + content[offset:]
            content = re.sub(pattern, lambda m: f"{m[1]}{counts[m[3]]:,}{m[5]}", content, flags=re.M)
        papers, mechanisms = totals
        if previous_totals is not None:
            assert totals == previous_totals, (home_name, totals, previous_totals)
        previous_totals = totals
        units = ("papers", "mechanisms") if english else ("篇论文", "个技术机制")
        prefix = "" if english else "共 "
        suffix = "." if english else "。"
        for count, unit in zip(totals, units):
            pattern = rf"^\*\*{prefix}[\d,]+ {unit}{re.escape(suffix)}\*\*"
            summary = f"**{prefix}{count:,} {unit}{suffix}**"
            content, changes = re.subn(pattern, summary, content, flags=re.M)
            assert changes == 1, (home_name, unit)
        write(home, content)
        print(home_name, f'{papers:,} papers, {mechanisms:,} mechanisms')


if __name__ == "__main__":
    sync()
