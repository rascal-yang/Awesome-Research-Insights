# 参与贡献

[首页](README.md) · [English](en/CONTRIBUTING.md)

欢迎通过 Pull Request 补充论文或修正已有条目。论文应有至少一种可从原文核实的机制、成立条件、反例或失败经验。用[六字段论文卡模板](templates/paper-card-template.md)记录比较、适用范围和证据。

## 新增或修订论文卡

1. 按题名和论文编号查重。预印本与会议版属于同一工作时，更新同一张卡的来源。
2. 依据原文填六字段。专门的机制解读可作为卡内小节，并注明验证范围。缺项标为「未报告」，迁移设想明确标注。
3. 在主领域索引放一个论文卡入口，技术索引链接到卡内对应机制。中英文索引使用同一张卡。

ICML 2026 按官方论文集顺序整理。从仓库根目录运行以下命令新增一批论文卡。

```text
python conferences/icml-2026/append_batch.py <批次.tsv> --date YYYY-MM-DD --paper-cards <论文卡.tsv>
```

批次表头依次为 `number`、`pmlr_id`、`domain`、`technique`、`topic`、`insight`。沿用[分类清单](conferences/icml-2026/classification.tsv)中的分类，两张 TSV 的论文 ID 必须一致。脚本写入论文卡、更新索引并同步首页计数。

修订六字段时，运行 `python conferences/icml-2026/paper_cards.py <论文卡.tsv>`。更正卡内机制时，编辑对应小节并保留链接锚点。

合并前检查原文定位、评测条件、论文 ID、分类、链接和中英文首页计数。每篇论文计一次，卡内各机制按技术分类分别计数。
