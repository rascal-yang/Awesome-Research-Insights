# Reinforcement Learning Methods

[Home](../../README.en.md) · [Contributing](../CONTRIBUTING.md) · [简体中文](../../insights/reinforcement-learning.md)

Rewards, exploration, credit assignment, and policy improvement.

## Multi-Reward Advantage Estimation

### Normalize Each Reward Before Aggregation

**Source**

[GDPO](https://proceedings.mlr.press/v306/liu26aa.html) (Shih-Yang Liu et al., ICML 2026) · [§3.1, Eqs. 4–6](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26aa/liu26aa.pdf#page=4) · [§4.1 and Table 1](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26aa/liu26aa.pdf#page=5) · [Paper index](../papers/reinforcement-learning.md#group-relative-policy-optimization)

**Core Idea**

For a GRPO-style update, compare rollouts on each reward separately before aggregating their advantages.

**Mechanism**

Sample a group of rollouts for the same input. Center and standardize each reward channel within that group. Sum the per-reward advantages, normalize the sum across the training batch, and use it for the policy update. The paper also studies weighting individual advantages during aggregation.

**Motivation**

Aggregating rewards before group normalization can map different combinations to the same advantage, for example when task success and format compliance offset one another. Keeping them separate preserves more distinctions in the update signal.

**Potential Applications**

- **Paper evidence** · On BFCL-v3, Qwen2.5-Instruct-1.5B improved mean tool-calling accuracy from 30.18% with GRPO to 32.81%, and format correctness from 76.33% to 80.66%, averaged over five runs (Table 1).
- **Transfer hypothesis** · For robot rollouts from a shared initial scene, consider separate success, progress, and constraint terms. Rewards need comparable rollouts and within-group variation. A constant component provides no within-group ranking signal. Physical robot performance remains to be tested.
