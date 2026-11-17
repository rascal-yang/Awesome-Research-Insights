#!/usr/bin/env python3
"""Add evidence-backed paper cards and link them from the existing indexes."""

import argparse
from collections import defaultdict
import csv
from pathlib import Path
import posixpath
import re

CONFERENCE = Path('conferences/icml-2026')
CARD_DIR = CONFERENCE / 'cards'
RECONVLA = {
    'pmlr_id': 'reconvla',
    'title': 'ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver',
    'paper_url': 'https://arxiv.org/abs/2508.10333',
}
RECONVLA_PAGE = Path('papers/reconvla.md')
FIELDS = {
    'problem': '问题 / 瓶颈',
    'method': '核心创新 / 方法',
    'baseline': 'Baseline',
    'benchmark': 'Benchmark',
    'results': '关键结果 / 消融',
    'limits': '适用条件 / 局限',
}
COLUMNS = ['pmlr_id', *FIELDS, 'evidence']
CARD_ANCHOR = re.compile(r'^<a id="paper-([\w-]+)"></a>$', re.M)
SOURCE_LINK = re.compile(r'\[[^\]\n]+\]\(https://[^\s()]+\)')
CARD_LINK = re.compile(r' · \[(?:论文卡|Paper card \(中文\))\]\([^\n)]+\)')


def read_tsv(path):
    with path.open(encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file, delimiter='\t'))


def catalog():
    return {
        row['pmlr_id']: row
        for row in read_tsv(CONFERENCE / 'papers.tsv')
        if row['insight_status'] == 'written'
    } | {'reconvla': RECONVLA}


def card_page(paper):
    if paper['pmlr_id'] == 'reconvla':
        return RECONVLA_PAGE
    start = (int(paper['number']) - 1) // 100 * 100 + 1
    end = min(start + 99, 6552)
    return CARD_DIR / f'{start:04d}-{end:04d}.md'


def card_locations(papers):
    locations = {}
    for path in [*sorted(CARD_DIR.glob('[0-9]*.md')), RECONVLA_PAGE]:
        if not path.is_file():
            continue
        for match in CARD_ANCHOR.finditer(path.read_text(encoding='utf-8')):
            key = match[1]
            if key in locations or key not in papers or card_page(papers[key]) != path:
                raise ValueError(f'Unexpected or duplicate paper card {key} in {path}.')
            locations[key] = path
    return locations


def load_card_rows(path):
    with path.open(encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        if reader.fieldnames != COLUMNS:
            raise ValueError(f'Expected these card columns: {", ".join(COLUMNS)}.')
        rows = list(reader)
    if not rows:
        raise ValueError('Paper card batch is empty.')
    keys = set()
    for row in rows:
        key = row['pmlr_id']
        if (None in row or not all(value and value.strip() and not re.search(r'[\r\n\t]', value)
                                   for value in row.values())):
            raise ValueError(f'Paper card {key} requires six fields and evidence on single lines.')
        if not re.fullmatch(r'[\w-]+', key) or key in keys:
            raise ValueError(f'Invalid or duplicate paper ID: {key}.')
        if not SOURCE_LINK.search(row['evidence']):
            raise ValueError(f'Paper card {key} requires an HTTPS evidence link.')
        keys.add(key)
    return rows


def relative_link(source, target):
    # Markdown destinations always use forward slashes.
    return posixpath.relpath(target.as_posix(), source.parent.as_posix())


def render_card(path, paper, row, classification):
    key = paper['pmlr_id']
    if key == 'reconvla':
        mechanisms = (
            '[用目标区域重建做辅助监督](../insights/loss-functions.md#target-region-reconstruction-as-auxiliary-supervision)'
            ' · [用指令前缀让视觉表征感知任务](../insights/modules.md#instruction-prefixes-for-causal-visual-grounding)'
        )
        title = paper['title']
    else:
        domain, technique = classification[key]
        index = relative_link(path, Path('papers') / f'{domain}.md')
        mechanisms = f'[关联 Insight]({index}#{key}-{technique})'
        title = f"{paper['number']} · {paper['title']}"
    labels = [f'- **{label}** · {row[field]}' for field, label in FIELDS.items()]
    return '\n'.join([
        f'<a id="paper-{key}"></a>',
        '',
        f'## {title}',
        '',
        f"[原文]({paper['paper_url']}) · {mechanisms}",
        '',
        *labels,
        '',
        f"**原文定位** · {row['evidence']}",
    ])


def write_if_changed(path, content):
    if not path.is_file() or path.read_text(encoding='utf-8') != content:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')


def write_cards(rows):
    papers = catalog()
    classification = {
        row['pmlr_id']: (row['domain'], row['technique'])
        for row in read_tsv(CONFERENCE / 'classification.tsv')
    }
    locations = card_locations(papers)
    updates = defaultdict(dict)
    for row in rows:
        key = row['pmlr_id']
        if key not in papers:
            raise ValueError(f'Paper {key} does not have an Insight in the catalog.')
        path = card_page(papers[key])
        updates[path][key] = render_card(path, papers[key], row, classification)
    for path, new_cards in updates.items():
        body = path.read_text(encoding='utf-8') if path in locations.values() else ''
        matches = list(CARD_ANCHOR.finditer(body))
        cards = {
            match[1]: body[match.start():next_match].strip()
            for match, next_match in zip(matches, [*(m.start() for m in matches[1:]), len(body)])
        } | new_cards
        if path == RECONVLA_PAGE:
            heading = '# ReconVLA 论文卡\n\n[机器人学索引](robotics.md)'
        else:
            start, end = map(int, path.stem.split('-'))
            heading = f'# ICML 2026 · 第 {start}–{end} 篇论文卡\n\n[论文卡索引](README.md) · [会议索引](../README.md)'
        keys = sorted(cards, key=lambda key: int(papers[key].get('number', 0)))
        write_if_changed(path, heading + '\n\n' + '\n\n'.join(cards[key] for key in keys) + '\n')


def refresh_card_links():
    papers = catalog()
    locations = card_locations(papers)
    if not locations:
        return
    urls = {papers[key]['paper_url']: (key, path) for key, path in locations.items()}
    paper_link = re.compile(r'\]\((https://(?:proceedings\.mlr\.press/v306/[\w-]+\.html|arxiv\.org/abs/2508\.10333(?:v1)?))\)')
    paths = [
        *CONFERENCE.glob('*.md'),
        *Path('papers').glob('*.md'),
        *Path('en/papers').glob('*.md'),
        *Path('insights').glob('*.md'),
        *Path('en/insights').glob('*.md'),
    ]
    for path in paths:
        if path == RECONVLA_PAGE:
            continue
        original = path.read_text(encoding='utf-8')
        label = 'Paper card (中文)' if path.parts[0] == 'en' else '论文卡'
        is_insight = path.parent.name == 'insights'
        lines = original.splitlines(keepends=True)
        for index, line in enumerate(lines):
            line = CARD_LINK.sub('', line)
            match = paper_link.search(line)
            if is_insight and line.startswith(('ReconVLA（Song ', 'ReconVLA (Song ')):
                url = RECONVLA['paper_url']
            elif line.startswith(('| ', '[') if is_insight else '| ') and match:
                url = match[1].removesuffix('v1')
            else:
                continue
            if url in urls:
                key, target = urls[url]
                relative = relative_link(path, target)
                link = f' · [{label}]({relative}#paper-{key})'
                # Leave the full citation intact on detail pages.
                insert = len(line.rstrip('\r\n')) if is_insight else match.end()
                lines[index] = line[:insert] + link + line[insert:]
        write_if_changed(path, ''.join(lines))
    pages = defaultdict(int)
    for path in locations.values():
        if path != RECONVLA_PAGE:
            pages[path] += 1
    index = [
        '# ICML 2026 论文卡', '',
        '[会议索引](../README.md) · [仓库首页](../../../README.md)', '',
        f'**已补充 {sum(pages.values()):,} / {len(papers) - 1:,} 篇已收录的 ICML 2026 论文。**',
        '',
        '每张论文卡汇集研究问题、方法、对照、评测、结果和适用边界，并链接原文与 Insight。',
        '',
    ]
    for path, count in sorted(pages.items()):
        start, end = map(int, path.stem.split('-'))
        index.append(f'- [第 {start}–{end} 篇]({path.name}) · {count} 张')
    write_if_changed(CARD_DIR / 'README.md', '\n'.join(index) + '\n')


def add_cards(path):
    rows = load_card_rows(path)
    write_cards(rows)
    refresh_card_links()
    print(f'Updated {len(rows)} paper cards.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cards', type=Path, help='TSV containing six editorial fields and evidence per paper')
    args = parser.parse_args()
    add_cards(args.cards)
