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

<!-- classification:start -->
## 按研究领域浏览

### 大语言模型

- [奖励优化](../papers/llm.md#ackermann26a-reinforcement-learning) · Gradient Regularization Mitigates Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards
- [Agent 后训练](../papers/llm.md#agarwal26e-reinforcement-learning) · Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use
- [多目标偏好优化](../papers/llm.md#agnihotri26a-reinforcement-learning) · Multi-Objective Preference Optimization: Improving Human Alignment of Generative Models
- [LLM 强化学习](../papers/llm.md#arnal26a-reinforcement-learning) · Efficient RL Training for LLMs with Experience Replay
- [测试时推理](../papers/llm.md#baek26a-reinforcement-learning) · D-FUSEr: Diverse Failure, Unified Success via Error-Distribution Shaping in LLM Reasoning
- [异步强化学习](../papers/llm.md#bai26k-reinforcement-learning) · D-ARL: A Distribution-Matched Asynchronous Reinforcement Learning Framework for Language Reasoning
- [生成安全对齐](../papers/llm.md#ball26b-reinforcement-learning) · Don’t Walk the Line: Boundary Guidance for Filtered Generation
- [GRPO 探索](../papers/llm.md#bamba26b-reinforcement-learning) · XRPO: Pushing the Limits of GRPO with Targeted Exploration and Exploitation
- [可验证奖励强化学习](../papers/llm.md#bi26a-reinforcement-learning) · EchoRL: Reinforcement Learning via Rollout Echoing
- [多领域推理强化学习](../papers/llm.md#bi26c-reinforcement-learning) · Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning
- [Agent 测试时记忆](../papers/llm.md#cai26b-reinforcement-learning) · From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory
- [策略更新几何](../papers/llm.md#cai26c-reinforcement-learning) · Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian Isometric Policy Optimization
- [示范驱动的逆强化学习](../papers/llm.md#cai26k-reinforcement-learning) · Escaping the Verifier: Learning to Reason via Demonstrations
- [形式逻辑过程奖励](../papers/llm.md#cao26y-reinforcement-learning) · Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models
- [跨语言代码强化学习](../papers/llm.md#chai26c-reinforcement-learning) · GXPO: Group Cross-Lingual Relative Policy Optimization for Code Generation
- [事实性二元奖励](../papers/llm.md#chen26a-reinforcement-learning) · Train for Truth, Keep the Skills: Binary Retrieval-Augmented Reward Mitigates Hallucinations
- [无监督强化学习分布匹配](../papers/llm.md#chen26k-reinforcement-learning) · PowerFlow: Unlocking the Dual Nature of LLMs via Principled Distribution Matching
- [语言模型状态价值估计](../papers/llm.md#chen26w-reinforcement-learning) · Hista and Numca: Estimate State Value Effectively for Large Language Model Reinforcement Learning

### 计算机视觉

- [多奖励生成优化](../papers/computer-vision.md#ba26a-reinforcement-learning) · Pareto-Guided Optimal Transport for Multi-Reward Alignment
- [流匹配测试时优化](../papers/computer-vision.md#chen26as-reinforcement-learning) · Test-Time Reinforcement Learning for Flow Matching

### 自然语言处理

- [多跳事实核查](../papers/nlp.md#bu26e-reinforcement-learning) · Grounding Multi-Hop Reasoning in Structural Causal Models via Group Relative Policy Optimization

### 强化学习

- [价值函数学习](../papers/reinforcement-learning.md#agrawalla26a-reinforcement-learning) · What Does Flow-Matching Bring to TD-Learning?
- [分布强化学习](../papers/reinforcement-learning.md#akgul26a-reinforcement-learning) · Distributional Active Inference
- [多来源在线学习](../papers/reinforcement-learning.md#anand26a-reinforcement-learning) · Data-Source Adaptive Online Learning under Heteroscedastic Noise
- [离策略学习](../papers/reinforcement-learning.md#aouali26a-reinforcement-learning) · Off-Policy Learning in Large Action Spaces: Optimization Matters More Than Estimation
- [零样本离策略学习](../papers/reinforcement-learning.md#asadulaev26b-reinforcement-learning) · Zero-Shot Off-Policy Learning
- [长任务信用分配](../papers/reinforcement-learning.md#auzina26a-reinforcement-learning) · Intrinsic Credit Assignment for Long Horizon Interaction
- [神经逻辑老虎机](../papers/reinforcement-learning.md#bae26a-reinforcement-learning) · Neural Logistic Bandits
- [多智能体通信](../papers/reinforcement-learning.md#bae26c-reinforcement-learning) · LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning
- [目标条件测试时 RL](../papers/reinforcement-learning.md#bagatella26a-reinforcement-learning) · Test-time Offline Reinforcement Learning on Goal-related Experience
- [部署反馈下的强化学习](../papers/reinforcement-learning.md#basu26a-reinforcement-learning) · Performative Policy Gradient: Optimality in Performative Reinforcement Learning
- [多反馈奖励学习](../papers/reinforcement-learning.md#baur26a-reinforcement-learning) · MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference
- [安全策略优化](../papers/reinforcement-learning.md#belouadah26a-reinforcement-learning) · CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning
- [低数据模仿学习](../papers/reinforcement-learning.md#blonde26a-reinforcement-learning) · Noise-Guided Transport: Imitation Learning from Random Priors
- [因果元强化学习](../papers/reinforcement-learning.md#bo26c-reinforcement-learning) · Counterfactual Bootstrap for Robust Meta-Reinforcement Learning
- [离线到在线强化学习](../papers/reinforcement-learning.md#bui26a-reinforcement-learning) · Efficient and Uncertainty-Aware Diffusion Framework for Offline-to-Online Reinforcement Learning
- [流匹配策略优化](../papers/reinforcement-learning.md#cao26f-reinforcement-learning) · Direct Flow Q-Learning
- [多奖励策略优化](../papers/reinforcement-learning.md#liu26aa-reinforcement-learning) · GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization

### 机器人学

- [规划与强化学习](../papers/robotics.md#aichmuller26a-reinforcement-learning) · Learning to Search and Searching to Learn for Generalization in Planning

### 多模态学习

- [长视频推理奖励](../papers/multimodal.md#cao26m-reinforcement-learning) · VideoTrace-R1: Long Video-based Retrieval-Augmented Generation via Reinforcement Learning

### 图学习与推荐

- [在线影响力最大化](../papers/graph-and-recommendation.md#agarwal26a-reinforcement-learning) · Efficient Online Influence Maximization under the Independent Cascade Model with Node-Level Feedback
- [推荐曝光控制](../papers/graph-and-recommendation.md#bisht26a-reinforcement-learning) · CORAL: Uncertainty-Aware Regulation of Exposure Concentration in Recommender Systems

### 科学机器学习

- [科学方程发现](../papers/scientific-ml.md#behzadifar26a-reinforcement-learning) · DecAEvolve: Decompose, Adapt, and Evolve for Effective LLM-based Scientific Equation Discovery
- [数学反例搜索](../papers/scientific-ml.md#butbaia26a-reinforcement-learning) · Hierarchical Reinforcement Learning for Sparse-Reward Search in Commutative Algebra
- [逆合成搜索工具选择](../papers/scientific-ml.md#chang26g-reinforcement-learning) · RetrOrchestrator: A Multi-Step Retrosynthesis Agent Dynamically Orchestrating Single-Step Transition Models
<!-- classification:end -->
