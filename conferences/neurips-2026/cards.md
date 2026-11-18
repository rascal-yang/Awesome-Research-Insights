# NeurIPS 2026 论文卡

[会议索引](README.md)

<a id="paper-33u8sf3mic"></a>

## δ-Mem — Efficient Online Memory for Large Language Models

[官方论文页与作者摘要](https://neurips.cc/virtual/2026/poster/155770) · [OpenReview](https://openreview.net/forum?id=33u8SF3mIc)

- **问题 / 瓶颈** · 长期助手需要复用历史信息，延长上下文会增加计算，也无法保证模型有效利用历史。
- **核心创新 / 方法** · 给冻结的全注意力骨干加固定尺寸的关联记忆矩阵，以 delta rule 在线写入；生成时用读出的状态给注意力计算加低秩修正。
- **Baseline** · 以冻结全注意力模型为底座；对比原冻结模型和最强非 δ-Mem 记忆基线，具体名称待全文核实。
- **Benchmark** · MemoryAgentBench、LoCoMo 及通用能力对照；子任务、指标定义和比较预算待全文核实。
- **关键结果 / 消融** · 作者摘要报告使用 8×8 状态时，平均分分别达到冻结骨干和最强记忆基线的 1.10 倍与 1.15 倍；MemoryAgentBench 和 LoCoMo 分别报告 1.31 倍与 1.20 倍，分项参照及消融待核实。
- **适用条件 / 局限** · 需要访问注意力计算；固定矩阵在冲突写入、长间隔读取或新骨干上的容量边界待核实。

**可复用机制** · 对有长历史的 Agent，在固定骨干下比较延长上下文与在线写入小型状态，把历史检索表现、通用能力和推理成本分开记录。

<a id="paper-tdl6qleloi"></a>

## Fast Rates for Offline Contextual Bandits with Forward-KL Regularization under Single-Policy Concentrability

[官方论文页](https://neurips.cc/virtual/2026/poster/149055) · [作者论文 v3](https://arxiv.org/abs/2605.09214v3)

- **问题 / 瓶颈** · 反向 KL 正则已有误差倒数型快率，前向 KL 的已有分析常停留在误差平方倒数型样本复杂度。
- **核心创新 / 方法** · 用悲观估计与凸分析处理前向 KL 正则的离线上下文赌博机，统一表格设定和一般函数逼近的上界推导。
- **Baseline** · 理论比较对象为既有反向 KL 快率、前向 KL 慢率及无正则情形。
- **Benchmark** · 理论设定为单策略集中性条件下的离线上下文赌博机，以达到目标误差所需日志样本数为指标。
- **关键结果 / 消融** · 作者给出误差倒数型上界及匹配统计速率的下界；正则很弱时，样本复杂度恢复到无正则的慢率。
- **适用条件 / 局限** · 结论针对给定的日志覆盖与正则条件；向多步强化学习或其他覆盖设定延伸需要额外分析。

**可复用机制** · 为离线策略设计 KL 正则时，把覆盖条件和正则强度都写进样本效率假设。比较方法时扫描弱正则区间，检查理论快率是否仍适用。
