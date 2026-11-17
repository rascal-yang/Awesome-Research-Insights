#!/usr/bin/env python3
"""Add human- or model-written insights and refresh the ICML 2026 indexes."""

import argparse
from collections import Counter
import csv
from datetime import date
from pathlib import Path
import re

DOMAINS = {
    'L': ('llm', '大语言模型', 'Large Language Models', '语言模型、工具调用与智能体。', 'Language models, tool use, and agents.'),
    'V': ('computer-vision', '计算机视觉', 'Computer Vision', '视觉识别、表征学习与生成。', 'Recognition, visual representations, and generation.'),
    'N': ('nlp', '自然语言处理', 'Natural Language Processing', '语言、语音、检索与文本处理。', 'Language, speech, retrieval, and text processing.'),
    'R': ('reinforcement-learning', '强化学习', 'Reinforcement Learning', '交互决策、奖励、策略学习与博弈。', 'Sequential decisions, rewards, policy learning, and games.'),
    'B': ('robotics', '机器人学', 'Robotics', '机器人感知、策略学习、规划与控制。', 'Robot perception, policy learning, planning, and control.'),
    'M': ('multimodal', '多模态学习', 'Multimodal Learning', '跨视觉、文本、音频等模态的学习与推理。', 'Learning and reasoning across vision, text, audio, and other modalities.'),
    'F': ('ml-foundations', '机器学习基础与统计', 'Machine Learning Foundations and Statistics', '通用学习方法、优化、学习理论与统计推断。', 'General learning methods, optimization, learning theory, and inference.'),
    'G': ('graph-and-recommendation', '图学习与推荐', 'Graph Learning and Recommendation', '图模型、知识图谱与推荐系统。', 'Graph models, knowledge graphs, and recommender systems.'),
    'S': ('scientific-ml', '科学机器学习', 'Scientific Machine Learning', '物理、医学、生物与工程中的机器学习。', 'Machine learning for physics, medicine, biology, and engineering.'),
}
TYPES = {
    'a': ('architecture', '模型架构', 'Architectures', '整体架构与信息流。', 'Model-wide design and information flow.'),
    'm': ('modules', '模块', 'Modules', '局部组件、连接与参数化。', 'Components, connections, and parameterizations.'),
    'l': ('loss-functions', '损失函数', 'Loss Functions', '训练目标、辅助监督与正则化。', 'Objectives, auxiliary supervision, and regularization.'),
    'o': ('optimization', '优化', 'Optimization', '梯度更新、求解器与优化过程。', 'Gradient updates, solvers, and optimization dynamics.'),
    'r': ('reinforcement-learning', '强化学习方法', 'Reinforcement Learning Methods', '奖励、探索、信用分配与策略更新。', 'Rewards, exploration, credit assignment, and policy updates.'),
    't': ('training-strategies', '训练策略', 'Training Strategies', '训练日程、微调、蒸馏与迁移。', 'Schedules, fine-tuning, distillation, and transfer.'),
    'd': ('data-strategies', '数据策略', 'Data Strategies', '数据构造、筛选、标注与采样。', 'Data construction, selection, annotation, and sampling.'),
    'i': ('inference', '推理策略', 'Inference Strategies', '解码、搜索、推理时适配与高效执行。', 'Decoding, search, test-time adaptation, and efficient execution.'),
    'p': ('representation-learning', '表征学习', 'Representation Learning', '表征提取、对齐、迁移与解耦。', 'Representation extraction, alignment, transfer, and disentanglement.'),
    'e': ('evaluation', '评测与诊断', 'Evaluation and Diagnostics', '基准、评测协议、消融与失效诊断。', 'Benchmarks, evaluation protocols, ablations, and failure diagnosis.'),
    'h': ('theory-statistics', '理论与统计', 'Theory and Statistics', '学习保证、反例、估计与统计检验。', 'Learning guarantees, counterexamples, estimation, and statistical tests.'),
}

def base_text(path):
    text = path.read_text(encoding='utf-8') if path.exists() else ''
    return text.split('<!-- classification:start -->')[0].rstrip()

def apply_block(path, content):
    head = base_text(path)
    head = re.sub(r'\n\n(?:欢迎贡献首批条目。|This index is open for contributions\.)$', '', head)
    path.write_text(head + '\n\n<!-- classification:start -->\n' + content.strip() + '\n<!-- classification:end -->\n', encoding='utf-8')

def title_anchor(key, tech):
    return f'{key}-{TYPES[tech][0]}'

def new_page(path, collection, slug, label, scope, english):
    if path.exists():
        return
    home = '../../README.en.md' if english else '../README.md'
    other = f'../../{collection}/{slug}.md' if english else f'../en/{collection}/{slug}.md'
    home_label = 'Home' if english else '首页'
    other_label = '简体中文' if english else 'English'
    path.write_text(f'# {label}\n\n[{home_label}]({home}) · [{other_label}]({other})\n\n{scope}\n', encoding='utf-8')


def read_tsv(path):
    with path.open(encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file, delimiter='\t'))

def add_batch(batch_path, date):
    conference = Path('conferences/icml-2026')
    manifest = conference / 'papers.tsv'
    classifications = conference / 'classification.tsv'
    records = read_tsv(manifest)
    old_mapping = read_tsv(classifications)
    pending = {int(row['number']) for row in records if row['insight_status'] == 'pending'}
    if not pending:
        print('All proceedings entries already have insights.')
        return
    first = min(pending)
    total = len(records)
    old_count = total - len(pending)
    batch = read_tsv(batch_path)
    if not batch:
        raise ValueError('Batch is empty.')
    numbers = [int(row['number']) for row in batch]
    last = numbers[-1]
    expected = [number for number in range(first, last + 1) if number in pending]
    if last > total or numbers != expected:
        raise ValueError(f'Provide all pending papers from {first} through the end of the batch, in order.')
    by_code = {name[0]: code for code, name in DOMAINS.items()}
    technique_code = {name[0]: code for code, name in TYPES.items()}
    pmlr_order = {row['pmlr_id']: int(row['number']) for row in records}
    mapping = {
        pmlr_order[row['pmlr_id']]: by_code[row['domain']] + technique_code[row['technique']]
        for row in old_mapping
    }
    assert len(pmlr_order) == total and len(mapping) == len(old_mapping) == old_count
    assert mapping.keys() == set(range(1, total + 1)) - pending

    pages = {}
    for number, item in zip(numbers, batch):
        record = records[number - 1]
        key, domain, technique, topic, insight = (item[field] for field in ('pmlr_id', 'domain', 'technique', 'topic', 'insight'))
        if (key != record['pmlr_id'] or domain not in by_code or technique not in technique_code
                or not topic.strip() or not insight.strip() or '|' in topic or '\n' in topic or '\n' in insight):
            raise ValueError(f'Check ID, classification and text for paper {number}.')
        mapping[number] = by_code[domain] + technique_code[technique]
        record['insight_status'] = 'written'
        page_start = ((number - 1) // 100) * 100 + 1
        title = record['title'].replace('|', '\\|')
        insight = insight.replace('|', '\\|')
        row = f"| {number} | [{title}]({record['paper_url']}) | {topic} | {insight} |"
        pages.setdefault(page_start, []).append(row)

    catalog = {int(row['number']): row for row in records if row['insight_status'] == 'written'}
    existing_id = re.compile(r'^\| (\d+) \|', re.M)
    for start, new_rows in pages.items():
        end = min(start + 99, total)
        page = conference / f'{start:04d}-{end:04d}.md'
        heading = f'# ICML 2026 · 第 {start}–{min(end, last)} 篇'
        if page.exists():
            body = page.read_text(encoding='utf-8').split('\n', 1)[1]
        else:
            body = '\n[返回会议索引](README.md)\n\n| 序号 | 论文 | 技术主题 | Insight |\n| ---: | --- | --- | --- |\n'
        known = {int(n) for n in existing_id.findall(body)}
        # Rows for the three featured papers stay in the conference index.
        assert known.isdisjoint(numbers)
        page.write_text(heading + '\n' + body.rstrip() + '\n' + '\n'.join(new_rows) + '\n', encoding='utf-8')
    with manifest.open('w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(records[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(records)
    with classifications.open('w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='\t', lineterminator='\n')
        writer.writerow(['pmlr_id', 'domain', 'technique'])
        for number, (domain, technique) in sorted(mapping.items()):
            writer.writerow([catalog[number]['pmlr_id'], DOMAINS[domain][0], TYPES[technique][0]])

    index = conference / 'README.md'
    text = index.read_text(encoding='utf-8')
    outstanding = pending - set(numbers)
    continuous = min(outstanding) - 1 if outstanding else total
    progress = f'**已整理 {len(catalog):,} / {total:,} 篇。** 连续整理到第 {continuous:,} 篇。'
    if outstanding:
        progress += f'下一篇从第 {continuous + 1:,} 篇开始。'
    text, updated = re.subn(r'^\*\*已整理 .*?底册的 ', progress + '底册的 ', text, flags=re.M)
    assert updated == 1
    page_links = []
    for page in sorted(conference.glob('[0-9][0-9][0-9][0-9]-*.md')):
        first_line = page.read_text(encoding='utf-8').splitlines()[0]
        page_links.append(f"- [{first_line.removeprefix('# ICML 2026 · ')}]({page.name})")
    text, updated = re.subn(r'(## 按目录浏览\n\n)(?:- \[第 [^\n]+\n)+',
                            lambda match: match[1] + '\n'.join(page_links) + '\n', text)
    assert updated == 1
    index.write_text(text, encoding='utf-8')
    render_indexes(conference, catalog, mapping, old_count, total, first, last, date)

def render_indexes(conference, catalog, mapping, old_count, total, first, last, date):
    papers = {}
    notes = {}
    for file in sorted(conference.glob('*.md')):
        for line in file.read_text(encoding='utf-8').splitlines():
            match = re.match(r'^\| (\d+) \| .*?\((https://proceedings\.mlr\.press/v306/[\w-]+\.html)\) \| (.*?) \| (.*) \|$', line)
            if match:
                n = int(match[1])
                assert n not in notes and match[2] == catalog[n]['paper_url']
                notes[n] = match[3], match[4].split(' [专题解读]')[0]
    assert notes.keys() == catalog.keys()
    details = {
        2807: 'reinforcement-learning.md#normalize-each-reward-before-aggregation',
        2844: 'loss-functions.md#align-action-features-with-latent-actions',
        4451: 'modules.md#widen-the-student-distillation-interface',
    }
    for n, record in sorted(catalog.items()):
        key = record['pmlr_id']
        domain, technique = mapping[n]
        topic, insight = notes[n]
        papers[key] = (domain, record['title'].replace('|', r'\|'), record['paper_url'], [(technique, topic, insight, details.get(n))])
    papers['reconvla'] = ('B', 'ReconVLA', 'https://arxiv.org/abs/2508.10333', [
        ('l', '目标区域重建', '用目标物体裁剪区域的潜变量重建，给策略表征增加训练监督。', 'loss-functions.md#target-region-reconstruction-as-auxiliary-supervision'),
        ('m', '指令前缀', '把指令 token 放在图像 token 前，使视觉隐藏状态通过因果注意力读取任务信息。', 'modules.md#instruction-prefixes-for-causal-visual-grounding'),
    ])
    domain_count = Counter(domain for domain, *_ in papers.values())
    domain_tech = Counter((domain, technique) for domain, _, _, insights in papers.values() for technique, *_ in insights)
    tech_count = Counter({tech: sum(domain_tech[domain, tech] for domain in DOMAINS) for tech in TYPES})
    for english in (False, True):
        prefix = Path('en') if english else Path('.')
        language = 2 if english else 1
        scope_col = 4 if english else 3
        for domain, info in DOMAINS.items():
            slug = info[0]
            path = prefix / 'papers' / f'{slug}.md'
            new_page(path, 'papers', slug, info[language], info[scope_col], english)
            heading = 'Browse by Technique' if english else '按技术类型浏览'
            block = [f'## {heading}']
            if english:
                block += ['', 'The linked short insights are available in Chinese.']
            for technique, tinfo in TYPES.items():
                if not domain_tech[domain, technique]:
                    continue
                tech_slug, category = tinfo[0], tinfo[language]
                block += ['', f'<a id="by-{tech_slug}"></a>', '', f'### {category}', '']
                if english:
                    block += ['| Paper | Insight |', '| :--- | :--- |']
                else:
                    block += ['| 论文 | 技术主题 | Insight |', '| :--- | :--- | :--- |']
                for key, (paper_domain, title, url, insights) in papers.items():
                    if paper_domain != domain:
                        continue
                    for tech, topic, insight, detail in insights:
                        if tech != technique:
                            continue
                        anchor = title_anchor(key, tech)
                        if english:
                            destination = f'../../papers/{slug}.md#{anchor}'
                            full = f' · [Full entry](../insights/{detail})' if detail else ''
                            block.append(f'| [{title}]({url}) | [Read insight (中文)]({destination}){full} |')
                        else:
                            full = f' [详细解读](../insights/{detail})' if detail else ''
                            block.append(f'| <a id="{anchor}"></a>[{title}]({url}) | {topic} | {insight}{full} |')
            apply_block(path, '\n'.join(block))

        for technique, info in TYPES.items():
            slug = info[0]
            path = prefix / 'insights' / f'{slug}.md'
            new_page(path, 'insights', slug, info[language], info[scope_col], english)
            heading = 'Browse by Research Domain' if english else '按研究领域浏览'
            block = [f'## {heading}']
            for domain, dinfo in DOMAINS.items():
                if not domain_tech[domain, technique]:
                    continue
                domain_slug, domain_label = dinfo[0], dinfo[language]
                block += ['', f'### {domain_label}', '']
                for key, (paper_domain, title, _, insights) in papers.items():
                    if paper_domain != domain:
                        continue
                    for tech, topic, _, detail in insights:
                        if tech != technique:
                            continue
                        if english:
                            target = f'../insights/{detail}' if detail else f'../../papers/{domain_slug}.md#{title_anchor(key, tech)}'
                            note = '' if detail else ' · 中文'
                            block.append(f'- [{title}]({target}){note}')
                        else:
                            target = f'../papers/{domain_slug}.md#{title_anchor(key, tech)}'
                            block.append(f'- [{topic}]({target}) · {title}')
            apply_block(path, '\n'.join(block))

        home = Path('README.en.md' if english else 'README.md')
        text = home.read_text(encoding='utf-8')
        before = f'{old_count:,} / {total:,}'
        after = f'{len(catalog):,} / {total:,}'
        assert text.count(before) == 1
        text = text.replace(before, after)
        done = (
            f'{old_count + 1:,} papers · {old_count + 2:,} insights'
            if english else f'{old_count + 1:,} 篇论文、{old_count + 2:,} 条 Insight'
        )
        now = (
            f'{sum(domain_count.values()):,} papers · {sum(tech_count.values()):,} insights'
            if english else f'{sum(domain_count.values()):,} 篇论文、{sum(tech_count.values()):,} 条 Insight'
        )
        assert text.count(done) == 1
        text = text.replace(done, now)
        for domain, info in DOMAINS.items():
            slug, name = info[0], info[language]
            pattern = rf'^(\| \[{re.escape(name)}\]\(#[^\n]+?\) \| )\d+( \|)'
            text, inserted = re.subn(pattern, rf'\g<1>{domain_count[domain]}\g<2>', text, flags=re.M)
            assert inserted == 1, (home, slug)
            target = (prefix / 'papers' / f'{slug}.md').as_posix()
            pattern = rf'^\[(?:All papers|全部论文) \(\d+\)\]\({re.escape(target)}\)\n\n[^\n]+'
            match = re.search(pattern, text, re.M)
            assert match, (home, target)
            previous_line = match[0].splitlines()[-1]
            aliases = {
                anchor[2]: anchor[1]
                for anchor in re.finditer(r'((?:<a id="[\w-]+"></a>)+)\[[^\]\n]+\]\(([^)]+)\)', previous_line)
            }
            links = []
            for technique, tech_info in TYPES.items():
                count = domain_tech[domain, technique]
                if not count:
                    continue
                final = f'{target}#by-{tech_info[0]}'
                links.append(f'{aliases.get(final, "")}[{tech_info[language]} ({count})]({final})')
            all_label = 'All papers' if english else '全部论文'
            replacement = f'[{all_label} ({domain_count[domain]})]({target})\n\n' + ' · '.join(links)
            text = text[:match.start()] + replacement + text[match.end():]
        for technique, info in TYPES.items():
            target = (prefix / 'insights' / f'{info[0]}.md').as_posix()
            expression = rf'^(\| .*?\]\({re.escape(target)}\) \| )\d+( \|)'
            text, inserted = re.subn(expression, rf'\g<1>{tech_count[technique]}\g<2>', text, flags=re.M)
            assert inserted == 1, (home, target)
        marker = '## Recent Updates\n\n' if english else '## 最近更新\n\n'
        new_update = (
            f'- **{date}** · Added insights for ICML 2026 papers {first}–{last} and indexed them by domain and technique. [Conference index](conferences/icml-2026/README.md)'
            if english else
            f'- **{date}** · 收录并分类整理 ICML 2026 第 {first}–{last} 篇的 Insight。[会议索引](conferences/icml-2026/README.md)'
        )
        assert text.count(marker) == 1
        head, _, tail = text.partition(marker)
        footer = '## Contributing\n\n' if english else '<a id="contributing"></a>\n\n## 参与贡献\n\n'
        updates, separator, rest = tail.partition(footer)
        assert separator
        recent = [line for line in updates.splitlines() if line.startswith('- **')][:2]
        archive = 'Earlier updates' if english else '更早的更新'
        history_url = 'https://github.com/rascal-yang/Awesome-Research-Insights/commits/main/'
        history_link = f'<a id="icml-2026-first-batch"></a>\n\n[{archive}]({history_url}{home.name})'
        text = head + marker + '\n\n'.join([new_update, *recent, history_link]) + '\n\n' + footer + rest
        latest = re.compile(r'^(\*\*(?:最新收录|Latest additions) · )\d{4}-\d{2}-\d{2}', re.M)
        text, replaced = latest.subn(lambda match: match[1] + date.isoformat(), text)
        assert replaced == 1 and '| Insight |' not in text
        home.write_text(text, encoding='utf-8')

    print(f'Added {len(catalog) - old_count} insights. ICML progress: {len(catalog):,} / {total:,}.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', type=Path, help='TSV with number, pmlr_id, domain, technique, topic, and insight columns')
    parser.add_argument('--date', required=True, type=date.fromisoformat, help='Publication date (YYYY-MM-DD)')
    args = parser.parse_args()
    add_batch(args.batch, args.date)
