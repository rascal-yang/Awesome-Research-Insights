#!/usr/bin/env python3
"""Add a batch of paper cards and refresh the ICML 2026 indexes."""

import argparse
from collections import Counter
import csv
from datetime import date
from pathlib import Path
import re

from paper_cards import (
    CONFERENCE, MECHANISM, RECONVLA, card_href, card_locations, card_page, catalog as card_catalog,
    load_card_rows, read_tsv, refresh_card_index, write_cards,
)

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
LEGACY_MECHANISM_ANCHORS = {
    'reconvla-loss-functions': ('target-region-reconstruction-as-auxiliary-supervision', 'auxiliary-visual-supervision'),
    'reconvla-modules': ('instruction-prefixes-for-causal-visual-grounding', 'multimodal-token-layout'),
    'liu26aa-reinforcement-learning': ('normalize-each-reward-before-aggregation', 'multi-reward-advantage-estimation'),
    'liu26bl-loss-functions': ('align-action-features-with-latent-actions', 'latent-action-alignment'),
    'tian26k-modules': ('widen-the-student-distillation-interface', 'distillation-interface-design'),
}

def base_text(path):
    text = path.read_text(encoding='utf-8') if path.exists() else ''
    return text.split('<!-- classification:start -->')[0].rstrip()

def apply_block(path, content):
    head = base_text(path)
    head = re.sub(r'\n\n(?:欢迎贡献首批条目。|This index is open for contributions\.)$', '', head)
    path.write_text(head + '\n\n<!-- classification:start -->\n' + content.strip() + '\n<!-- classification:end -->\n',
                    encoding='utf-8')

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


def add_batch(batch_path, date, paper_cards):
    conference = CONFERENCE
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
    cards = load_card_rows(paper_cards)
    if {row['pmlr_id'] for row in cards} != {row['pmlr_id'] for row in batch}:
        raise ValueError('Provide one paper card for each paper in this Insight batch.')
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

    mechanisms = {}
    for number, item in zip(numbers, batch):
        record = records[number - 1]
        key, domain, technique, topic, insight = (item[field] for field in ('pmlr_id', 'domain', 'technique', 'topic', 'insight'))
        if (key != record['pmlr_id'] or domain not in by_code or technique not in technique_code
                or not topic.strip() or not insight.strip() or re.search(r'[\r\n|]', topic)
                or re.search(r'[\r\n]', insight)):
            raise ValueError(f'Check ID, classification and text for paper {number}.')
        mapping[number] = by_code[domain] + technique_code[technique]
        record['insight_status'] = 'written'
        mechanisms[key] = technique, topic.strip(), insight.strip()

    indexed = card_catalog()
    if card_locations(indexed).keys() != indexed.keys():
        raise ValueError('Existing papers must have cards before appending a new batch.')

    catalog = {int(row['number']): row for row in records if row['insight_status'] == 'written'}
    with manifest.open('w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(records[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(records)
    with classifications.open('w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='\t', lineterminator='\n')
        writer.writerow(['pmlr_id', 'domain', 'technique'])
        for number, (domain, technique) in sorted(mapping.items()):
            writer.writerow([catalog[number]['pmlr_id'], DOMAINS[domain][0], TYPES[technique][0]])

    outstanding = pending - set(numbers)
    continuous = min(outstanding) - 1 if outstanding else total
    write_cards(cards, mechanisms)
    render_conference_index(catalog, continuous, total)
    render_indexes(catalog, mapping, old_count, total, first, last, date)
    refresh_card_index()


def render_conference_index(catalog, continuous, total):
    index = CONFERENCE / 'README.md'
    text = index.read_text(encoding='utf-8')
    progress = f'**已整理 {len(catalog):,} / {total:,} 篇。** 连续整理到第 {continuous:,} 篇。'
    if continuous < total:
        progress += f'下一篇从第 {continuous + 1:,} 篇开始。'
    text, updated = re.subn(r'^\*\*已整理 .*?底册的 ', progress + '底册的 ', text, flags=re.M)
    assert updated == 1
    page_links = []
    for start in range(1, continuous + 1, 100):
        end = min(start + 99, continuous)
        name = card_page(catalog[start]).name
        page_links.append(f'- [第 {start}–{end} 篇](cards/{name})')
    other = sorted(n for n in catalog if n > continuous)
    extra = ['<a id="此前收录"></a>']
    if other:
        extra += ['', '## 已收录的其他编号', '']
        for number in other:
            paper = catalog[number]
            target = card_href(index, paper, f"paper-{paper['pmlr_id']}")
            extra.append(f"- [{number} · {paper['title']}]({target})")
    contents = '\n\n'.join(['\n'.join(page_links), '\n'.join(extra)])
    text, updated = re.subn(r'(## 按论文编号浏览\n\n).*?(?=\n\n\[逐篇分类清单)',
                            lambda match: match[1] + contents, text, flags=re.S)
    assert updated == 1
    index.write_text(text, encoding='utf-8')

def render_indexes(catalog, mapping, old_count, total, first=None, last=None, date=None):
    papers = {}
    titles = {}
    for path in set(card_locations(card_catalog()).values()):
        for anchor, title in MECHANISM.findall(path.read_text(encoding='utf-8')):
            if anchor in titles:
                raise ValueError(f'Duplicate mechanism: {anchor}')
            titles[anchor] = title
    for n, record in sorted(catalog.items()):
        key = record['pmlr_id']
        domain, technique = mapping[n]
        papers[key] = domain, record['title'], record, [technique]
    papers['reconvla'] = 'B', 'ReconVLA', RECONVLA, ['l', 'm']
    domain_count = Counter(domain for domain, *_ in papers.values())
    primary_techniques = {(domain, techniques[0]) for domain, _, _, techniques in papers.values()}
    domain_tech = Counter((domain, technique) for domain, _, _, techniques in papers.values() for technique in techniques)
    tech_count = Counter(technique for _, _, _, techniques in papers.values() for technique in techniques)
    domain_aliases = {
        ('V', 'm'): ('vision-model-distillation',),
        ('R', 'r'): ('group-relative-policy-optimization',),
        ('B', 'l'): ('vision-language-action-models',),
    }
    for english in (False, True):
        prefix = Path('en') if english else Path('.')
        language = 2 if english else 1
        scope_col = 4 if english else 3
        for domain, info in DOMAINS.items():
            slug = info[0]
            path = prefix / 'papers' / f'{slug}.md'
            new_page(path, 'papers', slug, info[language], info[scope_col], english)
            heading = 'Browse by Technique' if english else '按技术类型浏览'
            available = [
                (technique, tinfo) for technique, tinfo in TYPES.items()
                if (domain, technique) in primary_techniques
            ]
            contents = ' · '.join(f'[{info[language]}](#by-{info[0]})' for _, info in available)
            block = [f'## {heading}', '', contents]
            for technique, tinfo in available:
                tech_slug, category = tinfo[0], tinfo[language]
                anchors = (f'by-{tech_slug}', *domain_aliases.get((domain, technique), ()))
                block += ['', ''.join(f'<a id="{anchor}"></a>' for anchor in anchors), '', f'### {category}', '']
                for key, (paper_domain, title, paper, techniques) in papers.items():
                    if paper_domain == domain and technique == techniques[0]:
                        anchors = ''.join(f'<a id="{title_anchor(key, tech)}"></a>' for tech in techniques)
                        target = card_href(path, paper, f'paper-{key}')
                        block.append(f'- {anchors}[{title}]({target})')
            apply_block(path, '\n'.join(block))

        for technique, info in TYPES.items():
            slug = info[0]
            path = prefix / 'insights' / f'{slug}.md'
            new_page(path, 'insights', slug, info[language], info[scope_col], english)
            heading = 'Browse by Research Domain' if english else '按研究领域浏览'
            contents = ' · '.join(
                f'[{dinfo[language]}](#by-{dinfo[0]})'
                for domain, dinfo in DOMAINS.items() if domain_tech[domain, technique]
            )
            block = [f'## {heading}', '', contents]
            for domain, dinfo in DOMAINS.items():
                if not domain_tech[domain, technique]:
                    continue
                domain_slug, domain_label = dinfo[0], dinfo[language]
                block += ['', f'<a id="by-{domain_slug}"></a>', '', f'### {domain_label}', '']
                for key, (paper_domain, title, paper, techniques) in papers.items():
                    if paper_domain == domain and technique in techniques:
                        anchor = title_anchor(key, technique)
                        target = card_href(path, paper, anchor)
                        aliases = ''.join(f'<a id="{old}"></a>' for old in LEGACY_MECHANISM_ANCHORS.get(anchor, ()))
                        if english:
                            block.append(f'- {aliases}[{title}]({target}) · 中文')
                        else:
                            block.append(f'- {aliases}[{titles[anchor]}]({target}) · {title}')
            apply_block(path, '\n'.join(block))

        if date is None:
            continue
        home = Path('README.en.md' if english else 'README.md')
        text = home.read_text(encoding='utf-8')
        before = f'{old_count:,} / {total:,}'
        after = f'{len(catalog):,} / {total:,}'
        assert text.count(before) == 1
        text = text.replace(before, after)
        done = (
            f'{old_count + 1:,} papers · {old_count + 2:,} mechanisms'
            if english else f'{old_count + 1:,} 篇论文、{old_count + 2:,} 个技术机制'
        )
        now = (
            f'{sum(domain_count.values()):,} papers · {sum(tech_count.values()):,} mechanisms'
            if english else f'{sum(domain_count.values()):,} 篇论文、{sum(tech_count.values()):,} 个技术机制'
        )
        assert text.count(done) == 1
        text = text.replace(done, now)
        for domain, info in DOMAINS.items():
            slug = info[0]
            target = (prefix / 'papers' / f'{slug}.md').as_posix()
            pattern = rf'^(\| .*?\]\({re.escape(target)}\) \| )\d+( \|)'
            text, inserted = re.subn(pattern, rf'\g<1>{domain_count[domain]}\g<2>', text, flags=re.M)
            assert inserted == 1, (home, slug)
        for technique, info in TYPES.items():
            target = (prefix / 'insights' / f'{info[0]}.md').as_posix()
            expression = rf'^(\| .*?\]\({re.escape(target)}\) \| )\d+( \|)'
            text, inserted = re.subn(expression, rf'\g<1>{tech_count[technique]}\g<2>', text, flags=re.M)
            assert inserted == 1, (home, target)
        marker = '## Recent Updates\n\n' if english else '## 最近更新\n\n'
        new_update = (
            f'- **{date}** · Added and classified ICML 2026 paper cards {first}–{last}.'
            if english else
            f'- **{date}** · 收录并分类整理 ICML 2026 第 {first}–{last} 篇的论文卡。'
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

    if date is not None:
        print(f'Added {len(catalog) - old_count} cards. ICML progress: {len(catalog):,} / {total:,}.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', type=Path, help='TSV with number, pmlr_id, domain, technique, topic, and insight columns')
    parser.add_argument('--date', required=True, type=date.fromisoformat, help='Publication date (YYYY-MM-DD)')
    parser.add_argument('--paper-cards', type=Path, required=True, help='Matching TSV of six-field paper cards')
    args = parser.parse_args()
    add_batch(args.batch, args.date, args.paper_cards)
