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
- [Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models](../../papers/llm.md#cao26y-reinforcement-learning) · 中文
- [GXPO: Group Cross-Lingual Relative Policy Optimization for Code Generation](../../papers/llm.md#chai26c-reinforcement-learning) · 中文
- [Train for Truth, Keep the Skills: Binary Retrieval-Augmented Reward Mitigates Hallucinations](../../papers/llm.md#chen26a-reinforcement-learning) · 中文
- [PowerFlow: Unlocking the Dual Nature of LLMs via Principled Distribution Matching](../../papers/llm.md#chen26k-reinforcement-learning) · 中文
- [Hista and Numca: Estimate State Value Effectively for Large Language Model Reinforcement Learning](../../papers/llm.md#chen26w-reinforcement-learning) · 中文
- [Learning to Reason for Factuality](../../papers/llm.md#chen26bh-reinforcement-learning) · 中文
- [Beyond Token-level Supervision: Unlocking the Potential of Decoding-based Regression via Reinforcement Learning](../../papers/llm.md#chen26ec-reinforcement-learning) · 中文
- [Learning to Self-Verify Makes Language Models Better Reasoners](../../papers/llm.md#chen26es-reinforcement-learning) · 中文
- [OnePO: Direct One-stage Policy Optimization for SFT-free Domain Adaptation](../../papers/llm.md#chen26fi-reinforcement-learning) · 中文
- [JADE: Bridging the Strategic-Operational Gap in Dynamic Agentic RAG](../../papers/llm.md#chen26gh-reinforcement-learning) · 中文
- [DECOR: Learning to Decompose and Collaborate in Deep Search via Multi-Agent Reinforcement Learning](../../papers/llm.md#chen26gp-reinforcement-learning) · 中文
- [Beyond Trajectory-Level Attribution: Graph-Based Credit Assignment for Agentic Reinforcement Learning](../../papers/llm.md#cheng26e-reinforcement-learning) · 中文
- [Anchored Self-Play for Code Repair](../../papers/llm.md#choi26f-reinforcement-learning) · 中文
- [Less Is More: Elevating RAG via Performance-Driven Context Compression](../../papers/llm.md#cui26i-reinforcement-learning) · 中文
- [You Can Learn Tokenization End-to-End with Reinforcement Learning](../../papers/llm.md#dauncey26a-reinforcement-learning) · 中文

### Computer Vision

- [Pareto-Guided Optimal Transport for Multi-Reward Alignment](../../papers/computer-vision.md#ba26a-reinforcement-learning) · 中文
- [Test-Time Reinforcement Learning for Flow Matching](../../papers/computer-vision.md#chen26as-reinforcement-learning) · 中文
- [RELO: Reinforcement Learning to Localize for Visual Object Tracking](../../papers/computer-vision.md#chen26ea-reinforcement-learning) · 中文
- [Rethinking the Design Space of Reinforcement Learning for Diffusion Models: On the Importance of Likelihood Estimation Beyond Loss Design](../../papers/computer-vision.md#choi26o-reinforcement-learning) · 中文

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
- [Best-of-Both-Worlds for Heavy-Tailed Markov Decision Processes](../../papers/reinforcement-learning.md#chen26cc-reinforcement-learning) · 中文
- [Multi-Agent Reinforcement Learning with Submodular Reward](../../papers/reinforcement-learning.md#chen26dk-reinforcement-learning) · 中文
- [Policy-Driven World Model Adaptation for Robust Offline Model-based Reinforcement Learning](../../papers/reinforcement-learning.md#chen26fl-reinforcement-learning) · 中文
- [VIPO: Value Function Inconsistency Penalized Offline Reinforcement Learning](../../papers/reinforcement-learning.md#chen26fn-reinforcement-learning) · 中文
- [How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?](../../papers/reinforcement-learning.md#cheng26q-reinforcement-learning) · 中文
- [Hybrid Reinforcement Learning in Adversarial Markov Decision Processes](../../papers/reinforcement-learning.md#cheng26s-reinforcement-learning) · 中文
- [Bilinear Bandits with Partially Observable Features](../../papers/reinforcement-learning.md#cho26f-reinforcement-learning) · 中文
- [Chain-of-Goals Hierarchical Policy for Long-Horizon Offline Goal-Conditioned RL](../../papers/reinforcement-learning.md#choi26k-reinforcement-learning) · 中文
- [Value Aggregation with Uncertainty in Online Decentralized MARL](../../papers/reinforcement-learning.md#chu26a-reinforcement-learning) · 中文
- [Balancing Plasticity and Stability with Fast and Slow Successor Features](../../papers/reinforcement-learning.md#chua26a-reinforcement-learning) · 中文
- [Offline Reinforcement Learning with Universal Horizon Models](../../papers/reinforcement-learning.md#chung26b-reinforcement-learning) · 中文
- [Linear Bandits beyond Inner Product Spaces, the case of Bandit Optimal Transport](../../papers/reinforcement-learning.md#croissant26a-reinforcement-learning) · 中文
- [SMAC: Score-Matched Actor-Critics for Robust Offline-to-Online Transfer](../../papers/reinforcement-learning.md#de-lara26a-reinforcement-learning) · 中文
- [Multivariate Distributional Reinforcement Learning Using Sliced Divergences](../../papers/reinforcement-learning.md#debes26a-reinforcement-learning) · 中文
- [GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](../insights/reinforcement-learning.md#normalize-each-reward-before-aggregation)

### Robotics

- [Learning to Search and Searching to Learn for Generalization in Planning](../../papers/robotics.md#aichmuller26a-reinforcement-learning) · 中文
- [LAGEA: Language Guided Embodied Agents for Robotic Manipulation](../../papers/robotics.md#chowdhury26a-reinforcement-learning) · 中文

### Multimodal Learning

- [VideoTrace-R1: Long Video-based Retrieval-Augmented Generation via Reinforcement Learning](../../papers/multimodal.md#cao26m-reinforcement-learning) · 中文
- [RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning](../../papers/multimodal.md#chen26bk-reinforcement-learning) · 中文
- [OmniVideo-R1: Reinforcing Audio-visual Reasoning with Query Intention and Modality Attention](../../papers/multimodal.md#chen26ed-reinforcement-learning) · 中文
- [VideoSEG-O3: A Multi-turn Reinforcement Learning Framework for Reasoning Video Object Segmentation](../../papers/multimodal.md#dai26j-reinforcement-learning) · 中文

### Graph Learning and Recommendation

- [Efficient Online Influence Maximization under the Independent Cascade Model with Node-Level Feedback](../../papers/graph-and-recommendation.md#agarwal26a-reinforcement-learning) · 中文
- [CORAL: Uncertainty-Aware Regulation of Exposure Concentration in Recommender Systems](../../papers/graph-and-recommendation.md#bisht26a-reinforcement-learning) · 中文

### Scientific Machine Learning

- [DecAEvolve: Decompose, Adapt, and Evolve for Effective LLM-based Scientific Equation Discovery](../../papers/scientific-ml.md#behzadifar26a-reinforcement-learning) · 中文
- [Hierarchical Reinforcement Learning for Sparse-Reward Search in Commutative Algebra](../../papers/scientific-ml.md#butbaia26a-reinforcement-learning) · 中文
- [RetrOrchestrator: A Multi-Step Retrosynthesis Agent Dynamically Orchestrating Single-Step Transition Models](../../papers/scientific-ml.md#chang26g-reinforcement-learning) · 中文
- [Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning](../../papers/scientific-ml.md#chen26gv-reinforcement-learning) · 中文
<!-- classification:end -->
