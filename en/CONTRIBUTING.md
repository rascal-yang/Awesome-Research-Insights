# Contributing

[Home](../README.en.md) · [简体中文](../CONTRIBUTING.md)

Propose an insight or a correction in a pull request. You can use a GitHub issue to suggest a paper or discuss where a technique belongs.

## Inclusion Criteria

A paper qualifies if it offers one independently explainable insight that readers can verify in the original. This can be a working technique, a condition under which a result holds, a counterexample, or an evidenced failure mode. State the evidence and its scope. Transfer scenarios are optional.

## Add an Insight

1. Find the original paper and locate the relevant section, figure, equation, or code.
2. Add the insight to its primary technical category using the [insight template](templates/insight-template.md). Use one H3 per insight; use an existing H2 when it fits or add a focused method family.
3. Add or update the paper's primary domain entry using the [paper template](templates/paper-template.md). Link directly to each associated insight. Use cross-links when a paper or insight fits additional categories.
4. For an addition, update the latest-additions date on both the [Chinese](../README.md) and [English](../README.en.md) homepages and add one line under **Recent Updates** when preparing the batch for merge.

### Review Checklist

- The source is easy to locate and supports the mechanism described.
- The insight explains what changes, what inputs or supervision it needs, and why the authors introduced it.
- State what the paper’s evidence supports. Label any transfer hypothesis separately.
- Relative links resolve, including links into individual insight headings.

## Keep the Index Current

For ICML 2026 entries, record the primary domain and technique in the [classification list](../conferences/icml-2026/classification.tsv). Update the matching section on the domain page and the cross-domain technique index, then check both homepage counts. English indexes may link to short Chinese insights.

For batch updates, run `python conferences/icml-2026/append_batch.py <batch.tsv> --date YYYY-MM-DD` from the repository root. Use the columns `number`, `pmlr_id`, `domain`, `technique`, `topic`, and `insight` in that order, with existing classification values. The script checks numbering and refreshes the indexes. Write each insight from the paper.

Count papers in their primary domain indexes. Each paper counts once regardless of its insight count or cross-links. Update the domain counts on both homepages when adding, removing, or moving a paper.

- **On merge.** Use the merge date for the latest additions on both homepages. Keep the three most recent batches in **Recent Updates**. Earlier changes remain in the pull request history.
- **As needed.** Correct claims and replace stale links in the canonical entry. Mention substantive corrections in **Recent Updates**. When moving or renaming an entry, update inbound links in the same pull request.
- **Monthly.** Review the month's additions and any flagged entries for source accuracy, resource links, duplicates, and taxonomy. Update **Last reviewed** with the date and scope after the check.

Maintain one canonical paper row and one canonical insight body. Keep the homepage headings stable so existing links remain easy to find.

Keep translated entries aligned with their canonical Chinese entries. Use the same insight anchors in both languages.
