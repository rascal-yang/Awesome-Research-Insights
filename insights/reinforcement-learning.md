# 强化学习方法

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/reinforcement-learning.md)

奖励、探索、信用分配与策略改进。

## 多奖励优势估计

<a id="normalize-each-reward-before-aggregation"></a>

### 多奖励先分别归一化再聚合

**来源**

[GDPO](https://proceedings.mlr.press/v306/liu26aa.html) (Shih-Yang Liu 等, ICML 2026) · [§3.1、式 4–6](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26aa/liu26aa.pdf#page=4) · [§4.1、表 1](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26aa/liu26aa.pdf#page=5) · [论文索引](../papers/reinforcement-learning.md#group-relative-policy-optimization)

**核心思路**

计算 GRPO 优势时，先比较同组轨迹在每项奖励上的得分，再聚合各项优势。

**实现机制**

同一输入采样一组 rollout，分别对每个奖励分量做组内中心化和标准差归一化。把各分量优势相加，再对整个训练批次做一次归一化，把结果用于策略更新。论文也讨论了如何在聚合时对各项优势赋权。

**设计动机**

先合并奖励再做组内归一化，不同的奖励组合可能得到相同的优势，例如成功与格式合规互相抵消时。分项处理可以保留更多有区别的更新信号。

**潜在应用**

- **论文证据** · BFCL-v3 上，Qwen2.5-Instruct-1.5B 的五次运行平均工具调用准确率由 GRPO 的 30.18% 提升到 32.81%，格式正确率由 76.33% 到 80.66%（表 1）。
- **迁移设想** · 可以在同一初始场景的多条机器人 rollout 上分别比较成功、进度和约束奖励。前提是组内奖励可比且有变化。某个奖励在整组里都相同时，归一化无法为该项创造区分信号。真机效果待验证。
