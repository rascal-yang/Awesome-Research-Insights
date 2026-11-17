# ICML 2026 论文 Insight

[仓库首页](../../README.md) · [English homepage](../../README.en.md) · [PMLR 第 306 卷](https://proceedings.mlr.press/v306/) · [全量论文底册（TSV）](papers.tsv)

按 PMLR 正式论文集排序，覆盖该卷的 6,552 篇论文，包括其中的 Position Paper。每篇记录技术主题和一条 Insight。

**已整理 1,163 / 6,552 篇。** 连续整理到第 1,160 篇。下一篇从第 1,161 篇开始。底册的 `written` 表示已有 Insight，`pending` 表示待整理。

[按研究领域浏览](../../README.md#papers-by-domain) · [按技术类型浏览](../../README.md#insights-by-technical-category) · [逐篇分类清单（TSV）](classification.tsv)

## 按目录浏览

- [第 1–100 篇](0001-0100.md)
- [第 101–200 篇](0101-0200.md)
- [第 201–300 篇](0201-0300.md)
- [第 301–400 篇](0301-0400.md)
- [第 401–500 篇](0401-0500.md)
- [第 501–600 篇](0501-0600.md)
- [第 601–700 篇](0601-0700.md)
- [第 701–800 篇](0701-0800.md)
- [第 801–900 篇](0801-0900.md)
- [第 901–1000 篇](0901-1000.md)
- [第 1001–1100 篇](1001-1100.md)
- [第 1101–1160 篇](1101-1200.md)

第 1–20 篇及第 521 篇起的条目依据论文正文撰写。第 21–520 篇主要依据官方摘要。

## 此前收录

| 序号 | 论文 | 技术主题 | Insight |
| ---: | --- | --- | --- |
| 2807 | [GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](https://proceedings.mlr.press/v306/liu26aa.html) | 多奖励策略优化 | 先在同一轨迹组内分别归一化各项奖励，再合并优势，避免量级大的奖励淹没其余维度。 [专题解读](../../insights/reinforcement-learning.md#normalize-each-reward-before-aggregation) |
| 2844 | [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://proceedings.mlr.press/v306/liu26bl.html) | 动作表征监督 | 用视频前后帧提取潜动作，监督动作专家的中间层，使策略表征能利用额外的运动信号。 [专题解读](../../insights/loss-functions.md#align-action-features-with-latent-actions) |
| 4451 | [From Per-Image Low-Rank to Encoding Mismatch: Rethinking Feature Distillation in Vision Transformers](https://proceedings.mlr.press/v306/tian26k.html) | 视觉特征蒸馏 | 给小型 ViT 的特征输出接口或最后一个 Transformer 块加宽，以匹配教师模型的编码空间。 [专题解读](../../insights/modules.md#widen-the-student-distillation-interface) |
