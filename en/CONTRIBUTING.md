# Contributing

[Home](../README.en.md) · [简体中文](../CONTRIBUTING.md)

Use a pull request to add a paper or correct an entry. Use the [six-field card template (中文)](../templates/paper-card-template.md) to capture the comparisons, scope, and source evidence.

## Inclusion criteria

Use the same criteria across fields and venues. Include only reusable technical insights supported by the paper. Paper quality, venue prestige, benchmark scores, and state-of-the-art status do not determine inclusion.

Four kinds of insight qualify, including **new mechanisms, new approaches, new findings, and failure lessons**. A simple auxiliary loss, reward design, or training technique can qualify when its reuse value is clear.

Apply three checks before considering a paper for inclusion.

| Question | Required evidence |
| --- | --- |
| **What can someone take away?** | An independently usable procedure, a supported finding, or a failure worth avoiding. |
| **What does it add?** | A design, approach, or boundary of applicability beyond the closest method that informs a technical choice. |
| **Does it need its own card?** | A distinct lesson. Keep the representative that explains a shared mechanism and its conditions most clearly. |

Prioritize removing the following five kinds of entries. Check any separate contribution against the three questions before excluding a paper.

- **Applications alone.** Existing methods moved to another task or dataset.
- **Integration alone.** Existing modules or tools combined without an independently reusable mechanism.
- **Scale alone.** More parameters, data, or compute supply the main contribution.
- **Scores alone.** Gains or isolated failures without a supported method or finding that informs a choice.
- **Redundant variants.** Existing cards already cover the transferable design.

Describe the operations and assumptions of a method. State the evidence and conditions for a finding or failure lesson. Exclude work whose value is confined to its setting with no specific way to transfer or adapt it. A curator's hypothetical transfer alone is insufficient. Leave uncertain evidence pending.

Starting from 4,105 existing ICML 2026 cards, this cleanup will remove at least half and retain at most 2,052. Among qualifying papers, prioritize clear operations, explicit conditions, and contributions with few substitutes. Record each exclusion reason in the manifest. Name the representative for redundant mechanisms and identify capacity-based exclusions explicitly.

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
