#!/usr/bin/env python3
"""Maintain the six fields and attached mechanisms of each paper card."""

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
EVIDENCE_PAGE_LINK = re.compile(r'\[([^\]\n]+)\]\((https://[^\s()]+#page=(\d+))\)')
MECHANISM = re.compile(r'^<a id="([\w-]+)"></a>\n\n(?:### |\*\*技术主题\*\* · )([^\n]+)$', re.M)
TOPIC = re.compile(r'^<a id="[\w-]+"></a>\n\n\*\*技术主题\*\* · [^\n]+\n\n', re.M)


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


def label_evidence_pages(evidence):
    def label(match):
        title, url, page = match.groups()
        suffix = f'（PDF 第 {page} 页）'
        if title.endswith(suffix):
            return match[0]
        return f'[{title}{suffix}]({url})'

    return EVIDENCE_PAGE_LINK.sub(label, evidence)


def render_card(paper, row, topic=''):
    key = paper['pmlr_id']
    if key == 'reconvla':
        title = paper['title']
    else:
        title = f"{paper['number']} · {paper['title']}"
    labels = [f'- **{label}** · {row[field]}' for field, label in FIELDS.items()]
    return '\n'.join([
        f'<a id="paper-{key}"></a>',
        '',
        f'## {title}',
        '',
        f"[原文]({paper['paper_url']})",
        '',
        topic + '\n'.join(labels),
        '',
        f"**原文定位** · {label_evidence_pages(row['evidence'])}",
    ])


def write_if_changed(path, content):
    if not path.is_file() or path.read_text(encoding='utf-8') != content:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')


def write_cards(rows, mechanisms=None):
    papers = catalog()
    locations = card_locations(papers)
    updates = defaultdict(dict)
    for row in rows:
        key = row['pmlr_id']
        if key not in papers:
            raise ValueError(f'Paper {key} does not have an Insight in the catalog.')
        path = card_page(papers[key])
        updates[path][key] = row
    for path, new_cards in updates.items():
        body = path.read_text(encoding='utf-8') if path in locations.values() else ''
        matches = list(CARD_ANCHOR.finditer(body))
        cards = {
            match[1]: body[match.start():next_match].strip()
            for match, next_match in zip(matches, [*(m.start() for m in matches[1:]), len(body)])
        }
        for key, row in new_cards.items():
            topic = ''
            suffix = ''
            if key in cards:
                match = TOPIC.search(cards[key])
                topic = match[0] if match else ''
                evidence = re.search(r'^\*\*原文定位\*\* · .+$', cards[key], re.M)
                if evidence is None:
                    raise ValueError(f'Paper card {key} has no evidence line.')
                suffix = cards[key][evidence.end():]
            if mechanisms and key in mechanisms:
                technique, title, insight = mechanisms[key]
                topic = render_topic(key, technique, title)
                suffix = f'\n\n**可复用机制** · {insight}'
            cards[key] = render_card(papers[key], row, topic) + suffix
        if path == RECONVLA_PAGE:
            heading = '# ReconVLA 论文卡\n\n[机器人学索引](robotics.md)'
        else:
            start, end = map(int, path.stem.split('-'))
            heading = f'# ICML 2026 · 第 {start}–{end} 篇论文卡\n\n[会议索引](../README.md)'
        keys = sorted(cards, key=lambda key: int(papers[key].get('number', 0)))
        write_if_changed(path, heading + '\n\n' + '\n\n'.join(cards[key] for key in keys) + '\n')


def render_topic(key, technique, topic):
    return f'<a id="{key}-{technique}"></a>\n\n**技术主题** · {topic}\n\n'


def card_href(index, paper, anchor):
    return f'{relative_link(index, card_page(paper))}#{anchor}'


def refresh_card_index():
    papers = catalog()
    locations = card_locations(papers)
    if not locations:
        return
    count = len(locations) - int(RECONVLA['pmlr_id'] in locations)
    index = [
        '# ICML 2026 论文卡', '',
        f'已补充 {count:,} / {len(papers) - 1:,} 篇已收录论文的六字段卡。', '',
        '[按论文编号浏览](../README.md#按论文编号浏览)',
    ]
    write_if_changed(CARD_DIR / 'README.md', '\n'.join(index) + '\n')


def add_cards(path):
    rows = load_card_rows(path)
    write_cards(rows)
    refresh_card_index()
    print(f'Updated {len(rows)} paper cards.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cards', type=Path, help='TSV containing six editorial fields and evidence per paper')
    args = parser.parse_args()
    add_cards(args.cards)
