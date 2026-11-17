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

<!-- classification:start -->
## Browse by Research Domain

### Large Language Models

- [Gradient Regularization Mitigates Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards](../../papers/llm.md#ackermann26a-reinforcement-learning) · 中文
- [Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use](../../papers/llm.md#agarwal26e-reinforcement-learning) · 中文
- [Multi-Objective Preference Optimization: Improving Human Alignment of Generative Models](../../papers/llm.md#agnihotri26a-reinforcement-learning) · 中文
- [Efficient RL Training for LLMs with Experience Replay](../../papers/llm.md#arnal26a-reinforcement-learning) · 中文
- [D-FUSEr: Diverse Failure, Unified Success via Error-Distribution Shaping in LLM Reasoning](../../papers/llm.md#baek26a-reinforcement-learning) · 中文
- [D-ARL: A Distribution-Matched Asynchronous Reinforcement Learning Framework for Language Reasoning](../../papers/llm.md#bai26k-reinforcement-learning) · 中文
- [Don’t Walk the Line: Boundary Guidance for Filtered Generation](../../papers/llm.md#ball26b-reinforcement-learning) · 中文
- [XRPO: Pushing the Limits of GRPO with Targeted Exploration and Exploitation](../../papers/llm.md#bamba26b-reinforcement-learning) · 中文
- [EchoRL: Reinforcement Learning via Rollout Echoing](../../papers/llm.md#bi26a-reinforcement-learning) · 中文
- [Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning](../../papers/llm.md#bi26c-reinforcement-learning) · 中文
- [From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory](../../papers/llm.md#cai26b-reinforcement-learning) · 中文
- [Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian Isometric Policy Optimization](../../papers/llm.md#cai26c-reinforcement-learning) · 中文
- [Escaping the Verifier: Learning to Reason via Demonstrations](../../papers/llm.md#cai26k-reinforcement-learning) · 中文

### Computer Vision

- [Pareto-Guided Optimal Transport for Multi-Reward Alignment](../../papers/computer-vision.md#ba26a-reinforcement-learning) · 中文

### Natural Language Processing

- [Grounding Multi-Hop Reasoning in Structural Causal Models via Group Relative Policy Optimization](../../papers/nlp.md#bu26e-reinforcement-learning) · 中文

### Reinforcement Learning

- [What Does Flow-Matching Bring to TD-Learning?](../../papers/reinforcement-learning.md#agrawalla26a-reinforcement-learning) · 中文
- [Distributional Active Inference](../../papers/reinforcement-learning.md#akgul26a-reinforcement-learning) · 中文
- [Data-Source Adaptive Online Learning under Heteroscedastic Noise](../../papers/reinforcement-learning.md#anand26a-reinforcement-learning) · 中文
- [Off-Policy Learning in Large Action Spaces: Optimization Matters More Than Estimation](../../papers/reinforcement-learning.md#aouali26a-reinforcement-learning) · 中文
- [Zero-Shot Off-Policy Learning](../../papers/reinforcement-learning.md#asadulaev26b-reinforcement-learning) · 中文
- [Intrinsic Credit Assignment for Long Horizon Interaction](../../papers/reinforcement-learning.md#auzina26a-reinforcement-learning) · 中文
- [Neural Logistic Bandits](../../papers/reinforcement-learning.md#bae26a-reinforcement-learning) · 中文
- [LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning](../../papers/reinforcement-learning.md#bae26c-reinforcement-learning) · 中文
- [Test-time Offline Reinforcement Learning on Goal-related Experience](../../papers/reinforcement-learning.md#bagatella26a-reinforcement-learning) · 中文
- [Performative Policy Gradient: Optimality in Performative Reinforcement Learning](../../papers/reinforcement-learning.md#basu26a-reinforcement-learning) · 中文
- [MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference](../../papers/reinforcement-learning.md#baur26a-reinforcement-learning) · 中文
- [CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning](../../papers/reinforcement-learning.md#belouadah26a-reinforcement-learning) · 中文
- [Noise-Guided Transport: Imitation Learning from Random Priors](../../papers/reinforcement-learning.md#blonde26a-reinforcement-learning) · 中文
- [Counterfactual Bootstrap for Robust Meta-Reinforcement Learning](../../papers/reinforcement-learning.md#bo26c-reinforcement-learning) · 中文
- [Efficient and Uncertainty-Aware Diffusion Framework for Offline-to-Online Reinforcement Learning](../../papers/reinforcement-learning.md#bui26a-reinforcement-learning) · 中文
- [Direct Flow Q-Learning](../../papers/reinforcement-learning.md#cao26f-reinforcement-learning) · 中文
- [GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](../insights/reinforcement-learning.md#normalize-each-reward-before-aggregation)

### Robotics

- [Learning to Search and Searching to Learn for Generalization in Planning](../../papers/robotics.md#aichmuller26a-reinforcement-learning) · 中文

### Multimodal Learning

- [VideoTrace-R1: Long Video-based Retrieval-Augmented Generation via Reinforcement Learning](../../papers/multimodal.md#cao26m-reinforcement-learning) · 中文

### Graph Learning and Recommendation

- [Efficient Online Influence Maximization under the Independent Cascade Model with Node-Level Feedback](../../papers/graph-and-recommendation.md#agarwal26a-reinforcement-learning) · 中文
- [CORAL: Uncertainty-Aware Regulation of Exposure Concentration in Recommender Systems](../../papers/graph-and-recommendation.md#bisht26a-reinforcement-learning) · 中文

### Scientific Machine Learning

- [DecAEvolve: Decompose, Adapt, and Evolve for Effective LLM-based Scientific Equation Discovery](../../papers/scientific-ml.md#behzadifar26a-reinforcement-learning) · 中文
- [Hierarchical Reinforcement Learning for Sparse-Reward Search in Commutative Algebra](../../papers/scientific-ml.md#butbaia26a-reinforcement-learning) · 中文
<!-- classification:end -->
