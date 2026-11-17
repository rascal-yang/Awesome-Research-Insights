# Contributing

[Home](../README.en.md) · [简体中文](../CONTRIBUTING.md)

Use a pull request to add a paper or correct an entry. Use the [six-field card template (中文)](../templates/paper-card-template.md) to capture the comparisons, scope, and source evidence.

## Inclusion criteria

Use the same criteria across fields and venues. Include only reusable technical insights supported by the paper. Paper quality, venue prestige, benchmark scores, and state-of-the-art status do not determine inclusion.

- **New mechanism.** A reusable module, algorithm, loss, reward function, or optimization strategy.
- **New approach.** A design that can transfer to other tasks or fields.
- **New finding.** An experimentally or theoretically supported training or optimization pattern, including counterintuitive results.
- **Failure lesson.** A broadly informative failure cause, limitation, or negative result.

Ask three questions in order. Include the paper only if all three answers are yes. Simple auxiliary losses, reward designs, and training techniques can qualify.

1. Does the paper contain a technical mechanism, approach, finding, or failure lesson worth extracting?
2. Can someone understand and use the insight independently of the paper?
3. Can you name a specific way to transfer it, adapt it, or use it to inform a design decision?

When the main contribution is applying existing methods to a new task or dataset, scaling models, data, or compute, integrating existing components, improving performance, or designing for a narrow setting, check the paper for a separate insight that passes all three questions. Leave uncertain cases pending until the evidence can be checked.

## Add or revise a card

1. Search by paper title and identifier. When a preprint and proceedings paper describe the same work, update the sources in its existing card.
2. Fill the six fields from the paper. Put detailed mechanism notes inside the card. Mark missing information as unreported and label any transfer hypothesis.
3. Link the card once in its primary domain. Link to its mechanism from each relevant technique index. Both language indexes use the same card.

Review ICML 2026 papers in proceedings order. To add a batch, run the following from the repository root.

```text
python conferences/icml-2026/append_batch.py <batch.tsv> --date YYYY-MM-DD --paper-cards <cards.tsv> --screening <screening.tsv>
```

Use `number`, `pmlr_id`, `decision`, and `reason` in the screening TSV. Record `keep` or `exclude` for each screened paper in proceedings order. Explain the transfer value for inclusion. For exclusions, explain which criterion the paper did not meet and cite the section or PDF page checked.

Use `number`, `pmlr_id`, `domain`, `technique`, `topic`, and `insight` in the batch TSV. Follow the existing [classification values](../conferences/icml-2026/classification.tsv). Supply Insights and cards only for `keep` decisions. A batch without retained papers needs only `--date` and `--screening`. To review published cards, add `--review-existing` and supply the date and screening TSV. The updater synchronizes the cards, indexes, and counts of screened and included papers.

To revise the six fields, run `python conferences/icml-2026/paper_cards.py <cards.tsv>`. To edit a mechanism, update it in the card and keep its anchor.

Before merging, check the cited evidence, evaluation settings, paper IDs, taxonomy, links, and both homepage counts. Count each paper once and count each mechanism under its technique.
