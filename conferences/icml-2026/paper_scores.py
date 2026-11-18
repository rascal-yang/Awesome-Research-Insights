#!/usr/bin/env python3
"""Merge source-based editorial scores and rank a fully scored proceedings."""

import argparse
from collections import Counter
import csv
from pathlib import Path
import re

from paper_cards import CONFERENCE, read_tsv, write_if_changed

WEIGHTS = {'novelty': 7, 'reuse': 6, 'usability': 4, 'distinctness': 3}
INPUT_COLUMNS = ['number', 'pmlr_id', *WEIGHTS, 'reason']
OUTPUT_COLUMNS = ['number', 'pmlr_id', *WEIGHTS, 'total', 'rank', 'reason', 'status']
SCORE_FILE = CONFERENCE / 'scores.tsv'


def load_scores(path, manifest):
    with path.open(encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        if reader.fieldnames != INPUT_COLUMNS:
            raise ValueError(f'Unexpected score columns in {path}.')
        rows = list(reader)
    seen = set()
    for row in rows:
        number = int(row['number'])
        if (number not in manifest or number in seen or None in row
                or row['pmlr_id'] != manifest[number]['pmlr_id']):
            raise ValueError(f'Invalid or duplicate paper ID in {path}: {number}.')
        if any(not re.fullmatch(r'[0-5]', row[field]) for field in WEIGHTS):
            raise ValueError(f'Paper {number} requires four integer scores from 0 to 5.')
        if not row['reason'].strip() or re.search(r'[\r\n\t]', row['reason']):
            raise ValueError(f'Paper {number} requires a specific single-line rationale.')
        row['total'] = str(sum(int(row[field]) * weight for field, weight in WEIGHTS.items()))
        row['rank'] = ''
        row['status'] = 'scored'
        seen.add(number)
    return rows


def score_key(row):
    return tuple(int(row[field]) for field in ('total', *WEIGHTS))


def rank_scores(rows, quota, tie_order):
    ordered = sorted(rows, key=lambda row: (*(-value for value in score_key(row)), int(row['number'])))
    if 0 < quota < len(ordered) and score_key(ordered[quota - 1]) == score_key(ordered[quota]):
        boundary_key = score_key(ordered[quota])
        tied = [row for row in ordered if score_key(row) == boundary_key]
        numbers = {int(row['number']) for row in tied}
        if set(tie_order) != numbers:
            raise ValueError('Reassess the cutoff tie and supply all tied IDs with --tie-order. '
                             f'Tied papers: {", ".join(map(str, sorted(numbers)))}.')
        if {position for position, _ in tie_order.values()} != set(range(1, len(tied) + 1)):
            raise ValueError('Cutoff tie positions must run from 1 through the tied group size.')
        tied.sort(key=lambda row: tie_order[int(row['number'])][0])
        start = next(index for index, row in enumerate(ordered) if score_key(row) == boundary_key)
        ordered[start:start + len(tied)] = tied
        for row in tied:
            row['reason'] += ' 截止同分复核。' + tie_order[int(row['number'])][1]
    for rank, row in enumerate(ordered, 1):
        row['rank'] = str(rank)
        row['status'] = 'selected' if rank <= quota else 'ranked-out'
    return ordered


def merge_scores(shards, rank, tie_path):
    manifest_rows = read_tsv(CONFERENCE / 'papers.tsv')
    if any(row['insight_status'] == 'ranked-out' for row in manifest_rows):
        raise ValueError('Restore the candidate set before changing scores in this ranked collection.')
    manifest = {int(row['number']): row for row in manifest_rows}
    if len(manifest) != 6552 or set(manifest) != set(range(1, 6553)):
        raise ValueError('Expected the complete, uniquely numbered ICML 2026 manifest.')
    existing = read_tsv(SCORE_FILE) if SCORE_FILE.exists() else []
    scored = {}
    for row in existing:
        number = int(row['number'])
        if number in scored or row['pmlr_id'] != manifest[number]['pmlr_id']:
            raise ValueError(f'Invalid existing score record {number}.')
        if (row['status'] not in {'pending', 'rule-excluded'}
                and manifest[number]['insight_status'] != 'excluded'):
            scored[number] = {field: row[field] for field in INPUT_COLUMNS}
    batch_numbers = set()
    for path in shards:
        for row in load_scores(path, manifest):
            number = int(row['number'])
            if number in batch_numbers:
                raise ValueError(f'Paper {number} occurs in multiple input shards.')
            if manifest[number]['insight_status'] == 'excluded':
                raise ValueError(f'Paper {number} was excluded by the inclusion rules.')
            scored[number] = row
            batch_numbers.add(number)
    # Recompute derived fields on every run, including scores loaded from disk.
    for number, row in scored.items():
        if any(not re.fullmatch(r'[0-5]', row[field]) for field in WEIGHTS):
            raise ValueError(f'Invalid score for {number}.')
        row.update(total=str(sum(int(row[field]) * weight for field, weight in WEIGHTS.items())),
                   rank='', status='scored')
    excluded = {number for number, row in manifest.items() if row['insight_status'] == 'excluded'}
    if excluded & scored.keys():
        raise ValueError('An excluded paper still has a score. Review the conflicting records.')
    if rank:
        missing = manifest.keys() - excluded - scored.keys()
        if missing:
            raise ValueError(f'Score all eligible papers before ranking. Missing {len(missing):,}, '
                             f'beginning with {min(missing)}.')
        tie_order = {}
        if tie_path:
            for row in read_tsv(tie_path):
                number = int(row['number'])
                if number in tie_order or not row['reason'].strip():
                    raise ValueError('Cutoff review requires unique IDs and specific reasons.')
                tie_order[number] = int(row['position']), row['reason']
        rank_scores(list(scored.values()), len(manifest) // 2, tie_order)
    output = []
    for number, paper in manifest.items():
        if number in scored:
            output.append(scored[number])
        else:
            row = dict.fromkeys(OUTPUT_COLUMNS, '')
            row.update(number=str(number), pmlr_id=paper['pmlr_id'])
            row['status'] = 'rule-excluded' if number in excluded else 'pending'
            row['reason'] = paper['screening_reason'] if number in excluded else '待原文复核评分'
            output.append(row)
    with SCORE_FILE.open('w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=OUTPUT_COLUMNS, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(output)
    index = CONFERENCE / 'README.md'
    body = index.read_text(encoding='utf-8')
    progress = (f'**技术复用评分 · {len(scored):,} / 6,552 篇已评分。** '
                f'另有 {len(excluded):,} 篇按收录规则排除。全部完成后统一排名，最多保留 3,276 篇。'
                ' [评分与排名（TSV）](scores.tsv)')
    if '**技术复用评分 · ' in body:
        body = re.sub(r'^\*\*技术复用评分 · .+$', lambda _: progress, body, flags=re.M)
    else:
        body = body.replace('\n<a id="按目录浏览"></a>', '\n' + progress + '\n\n<a id="按目录浏览"></a>', 1)
    write_if_changed(index, body)
    counts = Counter(row['status'] for row in output)
    print(f'{len(scored):,} scored, {len(excluded):,} excluded by rules. Status counts: {dict(counts)}.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('shards', type=Path, nargs='*', help='TSVs containing four scores and a source-based reason')
    parser.add_argument('--rank', action='store_true', help='Rank only after every eligible paper has been scored')
    parser.add_argument('--tie-order', type=Path, help='Cutoff review TSV with number, position, and reason')
    args = parser.parse_args()
    merge_scores(args.shards, args.rank, args.tie_order)
