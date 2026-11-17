# Contributing

[Home](../README.en.md) · [简体中文](../CONTRIBUTING.md)

Use a pull request to add a paper or correct an entry. Include at least one mechanism, condition, counterexample, or failure mode supported by the paper. Use the [six-field card template (中文)](../templates/paper-card-template.md) to capture the comparisons, scope, and source evidence.

## Add or revise a card

1. Search by paper title and identifier. When a preprint and proceedings paper describe the same work, update the sources in its existing card.
2. Fill the six fields from the paper. Put detailed mechanism notes inside the card. Mark missing information as unreported and label any transfer hypothesis.
3. Link the card once in its primary domain. Link to its mechanism from each relevant technique index. Both language indexes use the same card.

Review ICML 2026 papers in proceedings order. To add a batch, run the following from the repository root.

```text
python conferences/icml-2026/append_batch.py <batch.tsv> --date YYYY-MM-DD --paper-cards <cards.tsv>
```

Use the columns `number`, `pmlr_id`, `domain`, `technique`, `topic`, and `insight` in the batch TSV. Use the existing [classification values](../conferences/icml-2026/classification.tsv) and supply the same paper IDs in both TSVs. The updater writes the cards, refreshes the indexes, and synchronizes the homepage counts.

To revise the six fields, run `python conferences/icml-2026/paper_cards.py <cards.tsv>`. To edit a mechanism, update it in the card and keep its anchor.

Before merging, check the cited evidence, evaluation settings, paper IDs, taxonomy, links, and both homepage counts. Count each paper once and count each mechanism under its technique.
