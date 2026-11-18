#!/usr/bin/env python3
"""Add a batch of paper cards and refresh the ICML 2026 indexes."""

import argparse
from collections import Counter, defaultdict
import csv
from datetime import date
from pathlib import Path
import re

from paper_cards import (
    CARD_ANCHOR, CONFERENCE, MECHANISM, RECONVLA, card_href, card_locations, card_page,
    catalog as card_catalog, load_card_rows, read_tsv, refresh_card_index, write_cards,
    write_if_changed,
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


def read_screening(path, records, review_existing):
    rows = read_tsv(path)
    if not rows:
        raise ValueError('Screening batch is empty.')
    decisions = {}
    for row in rows:
        if row.keys() != {'number', 'pmlr_id', 'decision', 'reason'}:
            raise ValueError('Expected screening columns: number, pmlr_id, decision, reason.')
        number = int(row['number'])
        decision, reason = row['decision'], row['reason'].strip()
        if (not 1 <= number <= len(records) or number in decisions
                or decision not in {'keep', 'exclude'} or not reason or re.search(r'[\r\n\t]', reason)):
            raise ValueError(f'Invalid or duplicate screening decision for paper {number}.')
        record = records[number - 1]
        status = 'written' if review_existing else 'pending'
        completed = bool(record['screening_reason'])
        revising_exclusion = review_existing and decision == 'exclude'
        if (record['pmlr_id'] != row['pmlr_id'] or record['insight_status'] != status
                or (completed and not revising_exclusion)):
            raise ValueError(f'Paper {number} is not awaiting this screening decision.')
        decisions[number] = decision, reason
    return decisions


def review_cards(reviews, locations):
    updates = defaultdict(dict)
    for key, review in reviews.items():
        updates[locations[key]][key] = review
    for path, decisions in updates.items():
        body = path.read_text(encoding='utf-8')
        matches = list(CARD_ANCHOR.finditer(body))
        sections = [body[:matches[0].start()]]
        for index, match in enumerate(matches):
            decision, reason = decisions.get(match[1], (None, ''))
            if decision == 'exclude':
                continue
            end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
            section = body[match.start():end]
            if decision == 'keep' and '**可复用机制** · ' not in section:
                section = section.rstrip() + f'\n\n**可复用机制** · {reason}\n\n'
            sections.append(section)
        if len(sections) == 1:
            path.unlink()
        else:
            write_if_changed(path, ''.join(sections).rstrip() + '\n')


def add_batch(batch_path, date, paper_cards, screening, review_existing=False):
    conference = CONFERENCE
    manifest = conference / 'papers.tsv'
    classifications = conference / 'classification.tsv'
    records = read_tsv(manifest)
    if any(row["insight_status"] == "ranked-out" for row in records):
        raise ValueError("Restore the candidate set before applying a screening batch to this ranked collection.")
    old_mapping = read_tsv(classifications)
    for record in records:
        record.setdefault('screening_reason', '')
    total = len(records)
    written = {int(row['number']) for row in records if row['insight_status'] == 'written'}
    decisions = read_screening(screening, records, review_existing)
    first, last = min(decisions), max(decisions)
    retained = sorted(n for n, (decision, _) in decisions.items() if decision == 'keep')
    batch = read_tsv(batch_path) if batch_path else []
    cards = load_card_rows(paper_cards) if paper_cards else []
    numbers = [int(row['number']) for row in batch]
    if review_existing:
        if batch_path or paper_cards:
            raise ValueError('Reviewing existing cards requires only screening decisions.')
    else:
        if any(not records[n - 1]['screening_reason'] for n in written):
            raise ValueError('Finish screening existing cards before adding new papers.')
        pending = [int(row['number']) for row in records if row['insight_status'] == 'pending']
        expected = [n for n in pending if n <= last]
        if list(decisions) != expected:
            raise ValueError(f'Screen all pending papers from {pending[0]} through {last}, in order.')
        if (numbers != retained or [row['pmlr_id'] for row in cards] != [row['pmlr_id'] for row in batch]):
            raise ValueError('Provide an Insight and card, in order, for each retained paper.')
    by_code = {name[0]: code for code, name in DOMAINS.items()}
    technique_code = {name[0]: code for code, name in TYPES.items()}
    pmlr_order = {row['pmlr_id']: int(row['number']) for row in records}
    mapping = {
        pmlr_order[row['pmlr_id']]: by_code[row['domain']] + technique_code[row['technique']]
        for row in old_mapping
    }
    assert len(pmlr_order) == total and len(mapping) == len(old_mapping) == len(written)
    assert mapping.keys() == written

    mechanisms = {}
    for number, item in zip(numbers, batch):
        record = records[number - 1]
        key, domain, technique, topic, insight = (item[field] for field in ('pmlr_id', 'domain', 'technique', 'topic', 'insight'))
        if (key != record['pmlr_id'] or domain not in by_code or technique not in technique_code
                or not topic.strip() or not insight.strip() or re.search(r'[\r\n|]', topic)
                or re.search(r'[\r\n]', insight)):
            raise ValueError(f'Check ID, classification and text for paper {number}.')
        mapping[number] = by_code[domain] + technique_code[technique]
        mechanisms[key] = technique, topic.strip(), insight.strip()

    indexed = card_catalog()
    locations = card_locations(indexed)
    if locations.keys() != indexed.keys():
        raise ValueError('Existing papers must have cards before appending a new batch.')

    for n, (decision, reason) in decisions.items():
        record = records[n - 1]
        record['screening_reason'] = reason
        record['insight_status'] = 'written' if decision == 'keep' else 'excluded'
        if review_existing and decision == 'exclude':
            del mapping[n]

    catalog = {int(row['number']): row for row in records if row['insight_status'] == 'written'}
    with manifest.open('w', encoding='utf-8', newline='') as file:
        columns = ['number', 'pmlr_id', 'title', 'paper_url', 'screening_reason', 'insight_status']
        writer = csv.DictWriter(file, fieldnames=columns, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(records)
    with classifications.open('w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='\t', lineterminator='\n')
        writer.writerow(['pmlr_id', 'domain', 'technique'])
        for number, (domain, technique) in sorted(mapping.items()):
            writer.writerow([catalog[number]['pmlr_id'], DOMAINS[domain][0], TYPES[technique][0]])

    if review_existing:
        review_cards({records[n - 1]['pmlr_id']: review for n, review in decisions.items()}, locations)
    if cards:
        write_cards(cards, mechanisms)
    screened = sum(bool(row['screening_reason']) for row in records)
    unreviewed = [n for n, row in catalog.items() if not row['screening_reason']]
    next_pending = next((int(row['number']) for row in records if row['insight_status'] == 'pending'), None)
    render_conference_index(catalog, screened, total, unreviewed, next_pending)
    range_label = str(first) if first == last else f'{first}–{last}'
    if last - first + 1 == len(decisions):
        update = (f'筛选 ICML 2026 编号 {range_label}，同步更新收录索引。',
                  f'Screened ICML 2026 papers {range_label} and updated the indexes.')
    else:
        update = (f'复核 {len(decisions)} 张 ICML 2026 论文卡，移除 {len(decisions) - len(retained)} 张。',
                  f'Reviewed {len(decisions)} ICML 2026 cards and removed {len(decisions) - len(retained)}.')
    render_indexes(catalog, mapping, screened, total, date, update)
    refresh_card_index()
    from paper_scores import SCORE_FILE, merge_scores
    if SCORE_FILE.exists():
        merge_scores([], False, None)
    print(f'Screened {len(decisions)} papers in this batch, retained {len(retained)}, '
          f'excluded {len(decisions) - len(retained)}. Total: {screened:,} / {total:,} screened, '
          f'{len(catalog):,} cards, including {len(unreviewed):,} awaiting review.')


def render_conference_index(catalog, screened, total, unreviewed, next_pending):
    index = CONFERENCE / 'README.md'
    text = index.read_text(encoding='utf-8')
    progress = f'**已筛选 {screened:,} / {total:,} 篇，当前收录 {len(catalog):,} 篇。**'
    if unreviewed:
        progress += f' 其中 {len(unreviewed):,} 张旧卡待复核，下一张从第 {unreviewed[0]:,} 篇开始。'
    elif next_pending is not None:
        progress += f' 下一篇从第 {next_pending:,} 篇开始筛选。'
    progress += (' 底册的 `written` 表示有论文卡，`excluded` 表示筛选后未收录，`pending` 表示待筛选。'
                 ' `screening_reason` 记录已完成的筛选判断。')
    text, updated = re.subn(r'^\*\*已(?:整理|筛选) .+$', lambda _: progress, text, flags=re.M)
    assert updated == 1
    groups = defaultdict(list)
    for number, paper in catalog.items():
        groups[card_page(paper).name].append(number)
    page_links = [f'- [编号 {numbers[0]}–{numbers[-1]}](cards/{name})' if len(numbers) > 1 else
                  f'- [编号 {numbers[0]}](cards/{name})' for name, numbers in groups.items()]
    contents = '\n'.join(page_links) + '\n\n<a id="此前收录"></a>'
    text, updated = re.subn(r'(## 按论文编号浏览\n\n).*?(?=\n\n\[逐篇分类清单)',
                            lambda match: match[1] + contents, text, flags=re.S)
    assert updated == 1
    index.write_text(text, encoding='utf-8')

def render_indexes(catalog, mapping, screened, total, date, update):
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

        home = Path('README.en.md' if english else 'README.md')
        text = home.read_text(encoding='utf-8')
        progress = (f'{screened:,} / {total:,} screened · {len(catalog):,} included' if english else
                    f'{screened:,} / {total:,} 篇已筛选 · 收录 {len(catalog):,} 篇')
        text, replaced = re.subn(r'(\[ICML 2026 · )[^\]]+(\]\(conferences/icml-2026/README\.md\))',
                                 lambda match: match[1] + progress + match[2], text)
        assert replaced == 1
        now = (
            f'{sum(domain_count.values()):,} papers · {sum(tech_count.values()):,} mechanisms'
            if english else f'{sum(domain_count.values()):,} 篇论文、{sum(tech_count.values()):,} 个技术机制'
        )
        totals = r'[\d,]+ papers · [\d,]+ mechanisms' if english else r'[\d,]+ 篇论文、[\d,]+ 个技术机制'
        text, replaced = re.subn(totals, now, text)
        assert replaced == 1
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
        new_update = f'- **{date}** · {update[english]}'
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
        latest = re.compile(r'^\*\*(?:最新收录|最新筛选|Latest additions|Latest screening) · \d{4}-\d{2}-\d{2}\*\*', re.M)
        label = 'Latest screening' if english else '最新筛选'
        text, replaced = latest.subn(f'**{label} · {date.isoformat()}**', text)
        assert replaced == 1 and '| Insight |' not in text
        home.write_text(text, encoding='utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', type=Path, nargs='?', help='TSV of Insights from newly retained papers')
    parser.add_argument('--date', required=True, type=date.fromisoformat, help='Publication date (YYYY-MM-DD)')
    parser.add_argument('--paper-cards', type=Path, help='Matching TSV of six-field paper cards')
    parser.add_argument('--screening', type=Path, required=True, help='TSV with number, pmlr_id, decision, and reason columns')
    parser.add_argument('--review-existing', action='store_true', help='Apply decisions to previously published cards')
    args = parser.parse_args()
    add_batch(args.batch, args.date, args.paper_cards, args.screening, args.review_existing)
