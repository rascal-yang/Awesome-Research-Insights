# 强化学习

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/papers/reinforcement-learning.md)

从交互、反馈和离线经验中学习。

<!-- classification:start -->
## 按技术类型浏览

[模型架构](#by-architecture) · [损失函数](#by-loss-functions) · [优化](#by-optimization) · [强化学习方法](#by-reinforcement-learning) · [训练策略](#by-training-strategies) · [数据策略](#by-data-strategies) · [推理策略](#by-inference) · [表征学习](#by-representation-learning) · [评测与诊断](#by-evaluation) · [理论与统计](#by-theory-statistics)

<a id="by-architecture"></a>

### 模型架构

- <a id="bian26a-architecture"></a>[RN-D: Discretized Categorical Actors for On-Policy Reinforcement Learning](../conferences/icml-2026/cards/0201-0300.md#paper-bian26a)
- <a id="huang26ba-architecture"></a>[VJEPA: Variational Joint Embedding Predictive Architectures as Probabilistic World Models](../conferences/icml-2026/cards/1701-1800.md#paper-huang26ba)
- <a id="koeppe26a-architecture"></a>[Mitigating Plasticity Loss through Architectural Design in Continual Learning](../conferences/icml-2026/cards/2101-2200.md#paper-koeppe26a)
- <a id="kresse26a-architecture"></a>[Differentiable Weightless Controllers: Learning Logic Circuits for Continuous Control](../conferences/icml-2026/cards/2201-2300.md#paper-kresse26a)
- <a id="lei26g-architecture"></a>[QHyer: Q-conditioned Hybrid Attention-mamba Transformer for Offline Goal-conditioned RL](../conferences/icml-2026/cards/2301-2400.md#paper-lei26g)

<a id="by-loss-functions"></a>

### 损失函数

- <a id="chen26ep-loss-functions"></a>[Continuity-Regularized Flow Matching for Offline Reinforcement Learning](../conferences/icml-2026/cards/0601-0700.md#paper-chen26ep)
- <a id="hassen26a-loss-functions"></a>[Spectral Flow Matching: Stabilizing Stochastic GFlowNets via Frequency-Domain Regularization](../conferences/icml-2026/cards/1401-1500.md#paper-hassen26a)
- <a id="jiang26ai-loss-functions"></a>[Boosting World Models Learning via Latent-Space Value Alignment](../conferences/icml-2026/cards/1901-2000.md#paper-jiang26ai)
- <a id="kharyal26a-loss-functions"></a>[Reward Learning through Ranking Mean Squared Error](../conferences/icml-2026/cards/2001-2100.md#paper-kharyal26a)
- <a id="lee26aj-loss-functions"></a>[Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods](../conferences/icml-2026/cards/2301-2400.md#paper-lee26aj)

<a id="by-optimization"></a>

### 优化

- <a id="corso26a-optimization"></a>[Fast Mixing Steady-State Control in Markov Decision Processes](../conferences/icml-2026/cards/0701-0800.md#paper-corso26a)
- <a id="dam26a-optimization"></a>[Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing](../conferences/icml-2026/cards/0801-0900.md#paper-dam26a)
- <a id="ko26a-optimization"></a>[Beyond the Bellman Recursion: A Pontryagin-Guided Framework for Non-Exponential Discounting](../conferences/icml-2026/cards/2101-2200.md#paper-ko26a)

<a id="by-reinforcement-learning"></a><a id="group-relative-policy-optimization"></a>

### 强化学习方法

- <a id="agrawalla26a-reinforcement-learning"></a>[What Does Flow-Matching Bring to TD-Learning?](../conferences/icml-2026/cards/0001-0100.md#paper-agrawalla26a)
- <a id="akgul26a-reinforcement-learning"></a>[Distributional Active Inference](../conferences/icml-2026/cards/0001-0100.md#paper-akgul26a)
- <a id="anand26a-reinforcement-learning"></a>[Data-Source Adaptive Online Learning under Heteroscedastic Noise](../conferences/icml-2026/cards/0001-0100.md#paper-anand26a)
- <a id="aouali26a-reinforcement-learning"></a>[Off-Policy Learning in Large Action Spaces: Optimization Matters More Than Estimation](../conferences/icml-2026/cards/0101-0200.md#paper-aouali26a)
- <a id="asadulaev26b-reinforcement-learning"></a>[Zero-Shot Off-Policy Learning](../conferences/icml-2026/cards/0101-0200.md#paper-asadulaev26b)
- <a id="auzina26a-reinforcement-learning"></a>[Intrinsic Credit Assignment for Long Horizon Interaction](../conferences/icml-2026/cards/0101-0200.md#paper-auzina26a)
- <a id="bae26a-reinforcement-learning"></a>[Neural Logistic Bandits](../conferences/icml-2026/cards/0101-0200.md#paper-bae26a)
- <a id="bae26c-reinforcement-learning"></a>[LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning](../conferences/icml-2026/cards/0101-0200.md#paper-bae26c)
- <a id="bagatella26a-reinforcement-learning"></a>[Test-time Offline Reinforcement Learning on Goal-related Experience](../conferences/icml-2026/cards/0101-0200.md#paper-bagatella26a)
- <a id="basu26a-reinforcement-learning"></a>[Performative Policy Gradient: Optimality in Performative Reinforcement Learning](../conferences/icml-2026/cards/0201-0300.md#paper-basu26a)
- <a id="baur26a-reinforcement-learning"></a>[MAVRL: Learning Reward Functions from Multiple Feedback Types with Amortized Variational Inference](../conferences/icml-2026/cards/0201-0300.md#paper-baur26a)
- <a id="belouadah26a-reinforcement-learning"></a>[CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning](../conferences/icml-2026/cards/0201-0300.md#paper-belouadah26a)
- <a id="blonde26a-reinforcement-learning"></a>[Noise-Guided Transport: Imitation Learning from Random Priors](../conferences/icml-2026/cards/0201-0300.md#paper-blonde26a)
- <a id="bo26c-reinforcement-learning"></a>[Counterfactual Bootstrap for Robust Meta-Reinforcement Learning](../conferences/icml-2026/cards/0301-0400.md#paper-bo26c)
- <a id="bui26a-reinforcement-learning"></a>[Efficient and Uncertainty-Aware Diffusion Framework for Offline-to-Online Reinforcement Learning](../conferences/icml-2026/cards/0301-0400.md#paper-bui26a)
- <a id="cao26f-reinforcement-learning"></a>[Direct Flow Q-Learning](../conferences/icml-2026/cards/0301-0400.md#paper-cao26f)
- <a id="chen26cc-reinforcement-learning"></a>[Best-of-Both-Worlds for Heavy-Tailed Markov Decision Processes](../conferences/icml-2026/cards/0501-0600.md#paper-chen26cc)
- <a id="chen26dk-reinforcement-learning"></a>[Multi-Agent Reinforcement Learning with Submodular Reward](../conferences/icml-2026/cards/0501-0600.md#paper-chen26dk)
- <a id="chen26fl-reinforcement-learning"></a>[Policy-Driven World Model Adaptation for Robust Offline Model-based Reinforcement Learning](../conferences/icml-2026/cards/0601-0700.md#paper-chen26fl)
- <a id="chen26fn-reinforcement-learning"></a>[VIPO: Value Function Inconsistency Penalized Offline Reinforcement Learning](../conferences/icml-2026/cards/0601-0700.md#paper-chen26fn)
- <a id="cheng26q-reinforcement-learning"></a>[How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?](../conferences/icml-2026/cards/0601-0700.md#paper-cheng26q)
- <a id="cheng26s-reinforcement-learning"></a>[Hybrid Reinforcement Learning in Adversarial Markov Decision Processes](../conferences/icml-2026/cards/0601-0700.md#paper-cheng26s)
- <a id="cho26f-reinforcement-learning"></a>[Bilinear Bandits with Partially Observable Features](../conferences/icml-2026/cards/0701-0800.md#paper-cho26f)
- <a id="choi26k-reinforcement-learning"></a>[Chain-of-Goals Hierarchical Policy for Long-Horizon Offline Goal-Conditioned RL](../conferences/icml-2026/cards/0701-0800.md#paper-choi26k)
- <a id="chu26a-reinforcement-learning"></a>[Value Aggregation with Uncertainty in Online Decentralized MARL](../conferences/icml-2026/cards/0701-0800.md#paper-chu26a)
- <a id="chua26a-reinforcement-learning"></a>[Balancing Plasticity and Stability with Fast and Slow Successor Features](../conferences/icml-2026/cards/0701-0800.md#paper-chua26a)
- <a id="chung26b-reinforcement-learning"></a>[Offline Reinforcement Learning with Universal Horizon Models](../conferences/icml-2026/cards/0701-0800.md#paper-chung26b)
- <a id="croissant26a-reinforcement-learning"></a>[Linear Bandits beyond Inner Product Spaces, the case of Bandit Optimal Transport](../conferences/icml-2026/cards/0701-0800.md#paper-croissant26a)
- <a id="de-lara26a-reinforcement-learning"></a>[SMAC: Score-Matched Actor-Critics for Robust Offline-to-Online Transfer](../conferences/icml-2026/cards/0801-0900.md#paper-de-lara26a)
- <a id="debes26a-reinforcement-learning"></a>[Multivariate Distributional Reinforcement Learning Using Sliced Divergences](../conferences/icml-2026/cards/0801-0900.md#paper-debes26a)
- <a id="deng26b-reinforcement-learning"></a>[BFTS: Thompson Sampling with Bayesian Additive Regression Trees](../conferences/icml-2026/cards/0801-0900.md#paper-deng26b)
- <a id="deng26n-reinforcement-learning"></a>[Sparse Topology-Aware Pairwise Scoring for Large-Scale Multi-Agent Reinforcement Learning](../conferences/icml-2026/cards/0801-0900.md#paper-deng26n)
- <a id="ding26z-reinforcement-learning"></a>[Sample-Efficient Diffusion-based Reinforcement Learning with Critic Guidance](../conferences/icml-2026/cards/0901-1000.md#paper-ding26z)
- <a id="diwan26a-reinforcement-learning"></a>[Trust Region Inverse Reinforcement Learning: Explicit Dual Ascent using Local Policy Updates](../conferences/icml-2026/cards/0901-1000.md#paper-diwan26a)
- <a id="dong26d-reinforcement-learning"></a>[TQL: Scaling Q-Functions with Transformers by Preventing Attention Collapse](../conferences/icml-2026/cards/0901-1000.md#paper-dong26d)
- <a id="dong26m-reinforcement-learning"></a>[Mean Flow Policy Optimization](../conferences/icml-2026/cards/0901-1000.md#paper-dong26m)
- <a id="doo26a-reinforcement-learning"></a>[Q-Flow: Stable and Expressive Reinforcement Learning with Flow-based Policy](../conferences/icml-2026/cards/0901-1000.md#paper-doo26a)
- <a id="du26b-reinforcement-learning"></a>[Stabilizing PPO via Latent-Space Regularization and KDE-Driven Exploration](../conferences/icml-2026/cards/0901-1000.md#paper-du26b)
- <a id="du26p-reinforcement-learning"></a>[IEC: When Information-Driven Exploration Meets Spectral Consensus via Primal–Dual Reward Regularization in Decentralized MARL](../conferences/icml-2026/cards/0901-1000.md#paper-du26p)
- <a id="eberhard26b-reinforcement-learning"></a>[Commit to the Bit: Reactive Reinforcement Learning Done Right](../conferences/icml-2026/cards/1001-1100.md#paper-eberhard26b)
- <a id="edgar26a-reinforcement-learning"></a>[Moment Matching Q-Learning](../conferences/icml-2026/cards/1001-1100.md#paper-edgar26a)
- <a id="ezer26a-reinforcement-learning"></a>[Stochastic Linear Bandits with Parameter Noise](../conferences/icml-2026/cards/1001-1100.md#paper-ezer26a)
- <a id="farebrother26a-reinforcement-learning"></a>[Compositional Planning with Jumpy World Models](../conferences/icml-2026/cards/1001-1100.md#paper-farebrother26a)
- <a id="fei26a-reinforcement-learning"></a>[Learning Interpretable Options by Identifying Reward Diffusion Bottlenecks in Reinforcement Learning](../conferences/icml-2026/cards/1001-1100.md#paper-fei26a)
- <a id="feng26q-reinforcement-learning"></a>[Offline Reinforcement Learning with Generative Trajectory Policies](../conferences/icml-2026/cards/1101-1200.md#paper-feng26q)
- <a id="fu26b-reinforcement-learning"></a>[FlowMAP: Flow Matching for Generalizable Agent Planning](../conferences/icml-2026/cards/1101-1200.md#paper-fu26b)
- <a id="fu26k-reinforcement-learning"></a>[HPS: Hyperspherical Parameter Sharing for Efficient Multi-Agent Reinforcement Learning](../conferences/icml-2026/cards/1101-1200.md#paper-fu26k)
- <a id="fukazawa26a-reinforcement-learning"></a>[RAMAC: Multimodal Risk-Aware Offline Reinforcement Learning and the Role of Behavior Regularization](../conferences/icml-2026/cards/1101-1200.md#paper-fukazawa26a)
- <a id="gao26ak-reinforcement-learning"></a>[Decentralized Bandits without Global Clock for Dynamic Matching Market](../conferences/icml-2026/cards/1201-1300.md#paper-gao26ak)
- <a id="genalti26a-reinforcement-learning"></a>[Online Packet Scheduling with Deadlines and Learning](../conferences/icml-2026/cards/1201-1300.md#paper-genalti26a)
- <a id="gerogiannis26a-reinforcement-learning"></a>[DAL: A Practical Prior-Free Black-Box Framework for Piecewise Stationary Bandits](../conferences/icml-2026/cards/1201-1300.md#paper-gerogiannis26a)
- <a id="ghosh26a-reinforcement-learning"></a>[Online Robust Reinforcement Learning with General Function Approximation](../conferences/icml-2026/cards/1201-1300.md#paper-ghosh26a)
- <a id="goyal26a-reinforcement-learning"></a>[Contextual Slate GLM Bandits with Limited Adaptivity](../conferences/icml-2026/cards/1301-1400.md#paper-goyal26a)
- <a id="han26i-reinforcement-learning"></a>[Transferable Reinforcement Learning via Probabilistic Latent Embeddings and Dynamic Policy Adaptation for Sim-to-Real Deployment](../conferences/icml-2026/cards/1401-1500.md#paper-han26i)
- <a id="harvey26a-reinforcement-learning"></a>[Unsupervised Hierarchical Skill Discovery](../conferences/icml-2026/cards/1401-1500.md#paper-harvey26a)
- <a id="he26u-reinforcement-learning"></a>[Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games](../conferences/icml-2026/cards/1501-1600.md#paper-he26u)
- <a id="he26v-reinforcement-learning"></a>[HyMTRL: A Hybrid Multi-Task Reinforcement Learning Framework via Phased Policy Evolution](../conferences/icml-2026/cards/1501-1600.md#paper-he26v)
- <a id="he26aa-reinforcement-learning"></a>[Doubly Regularized Markov Decision Processes for Robust Reinforcement Learning](../conferences/icml-2026/cards/1501-1600.md#paper-he26aa)
- <a id="henaff26a-reinforcement-learning"></a>[Scalable Option Learning in High-Throughput Environments](../conferences/icml-2026/cards/1501-1600.md#paper-henaff26a)
- <a id="hoang26c-reinforcement-learning"></a>[DualCOIL: Offline Imitation Learning from Contrasting Demonstrations](../conferences/icml-2026/cards/1501-1600.md#paper-hoang26c)
- <a id="hu26am-reinforcement-learning"></a>[Human-in-the-Loop Policy Optimization for Preference-Based Multi-Objective Reinforcement Learning](../conferences/icml-2026/cards/1601-1700.md#paper-hu26am)
- <a id="hu26bd-reinforcement-learning"></a>[Time-Consistent Robust Multi-Objective Reinforcement Learning via a Bellman–Isaacs Weight-Adversary Recursion](../conferences/icml-2026/cards/1601-1700.md#paper-hu26bd)
- <a id="iwaki26a-reinforcement-learning"></a>[Mirror Descent Actor Critic via Bounded Advantage Learning](../conferences/icml-2026/cards/1801-1900.md#paper-iwaki26a)
- <a id="jiang26u-reinforcement-learning"></a>[Secure Multi-agent Reinforcement Learning for Service Systems with Affinity and Byzantine Nodes: Stability Analysis and Protection Design](../conferences/icml-2026/cards/1901-2000.md#paper-jiang26u)
- <a id="jiang26ba-reinforcement-learning"></a>[Budget-Efficient Attacks and Robustness Training for Cooperative MARL](../conferences/icml-2026/cards/1901-2000.md#paper-jiang26ba)
- <a id="kim26ai-reinforcement-learning"></a>[Frictional Q-Learning](../conferences/icml-2026/cards/2101-2200.md#paper-kim26ai)
- <a id="kobanda26a-reinforcement-learning"></a>[Adaptive Quasimetric Mapping : Principled Topological Abstraction for Robust Offline Goal-Conditioned Navigation](../conferences/icml-2026/cards/2101-2200.md#paper-kobanda26a)
- <a id="kong26e-reinforcement-learning"></a>[Latent Spherical Flow Policy for Reinforcement Learning with Combinatorial Actions](../conferences/icml-2026/cards/2101-2200.md#paper-kong26e)
- <a id="kwon26c-reinforcement-learning"></a>[Safety Generalization Under Distribution Shift in Safe Reinforcement Learning: A Diabetes Testbed](../conferences/icml-2026/cards/2201-2300.md#paper-kwon26c)
- <a id="le26a-reinforcement-learning"></a>[Trust-Region Diffusion Policies for Massively Parallel On-Policy RL](../conferences/icml-2026/cards/2201-2300.md#paper-le26a)
- <a id="lee26s-reinforcement-learning"></a>[Interaction-Breaking Adversarial Learning Framework for Robust Multi-Agent Reinforcement Learning](../conferences/icml-2026/cards/2301-2400.md#paper-lee26s)
- <a id="lee26t-reinforcement-learning"></a>[Towards Efficient and Expressive Offline RL via Flow-Anchored Noise-conditioned Q-Learning](../conferences/icml-2026/cards/2301-2400.md#paper-lee26t)
- <a id="lee26ae-reinforcement-learning"></a>[Quantum Robust Inner Minimization for Reinforcement Learning with Quadratic Speed-Up in Query Complexity](../conferences/icml-2026/cards/2301-2400.md#paper-lee26ae)
- <a id="li26b-reinforcement-learning"></a>[Scaling Multi-Agent Environment Co-Design with Diffusion Models](../conferences/icml-2026/cards/2301-2400.md#paper-li26b)
- <a id="li26bj-reinforcement-learning"></a>[What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity](../conferences/icml-2026/cards/2401-2500.md#paper-li26bj)
- <a id="li26ee-reinforcement-learning"></a>[Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning](../conferences/icml-2026/cards/2501-2600.md#paper-li26ee)
- <a id="liu26aa-reinforcement-learning"></a>[GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](../conferences/icml-2026/cards/2801-2900.md#paper-liu26aa)

<a id="by-training-strategies"></a>

### 训练策略

- <a id="lee26ai-training-strategies"></a>[CompleteP for RL: Maintaining Feature Learning When Scaling Deep Reinforcement Learning](../conferences/icml-2026/cards/2301-2400.md#paper-lee26ai)

<a id="by-data-strategies"></a>

### 数据策略

- <a id="bendib26a-data-strategies"></a>[Improving Zero-Shot Offline RL via Behavioral Task Sampling](../conferences/icml-2026/cards/0201-0300.md#paper-bendib26a)
- <a id="chen26gd-data-strategies"></a>[Transport or Discard: Robust Unbalanced Optimal Transport for Cross-Domain Policy Adaptation](../conferences/icml-2026/cards/0601-0700.md#paper-chen26gd)
- <a id="fagan26a-data-strategies"></a>[The Two-Hump Problem: Bridging the Difficulty Gap in Mathematical Reinforcement Learning](../conferences/icml-2026/cards/1001-1100.md#paper-fagan26a)
- <a id="feng26aa-data-strategies"></a>[Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling](../conferences/icml-2026/cards/1101-1200.md#paper-feng26aa)

<a id="by-inference"></a>

### 推理策略

- <a id="brosseit26a-inference"></a>[Mind the Budget: Accelerating Deep Reinforcement Learning using Constrained Early Exit Neural Networks](../conferences/icml-2026/cards/0301-0400.md#paper-brosseit26a)
- <a id="chang26a-inference"></a>[The Surprising Difficulty of Search in Model-Based Reinforcement Learning](../conferences/icml-2026/cards/0401-0500.md#paper-chang26a)
- <a id="cui26h-inference"></a>[DRIVE: Distributional and Retrieval-Augmented Bidding with Value Evaluation](../conferences/icml-2026/cards/0701-0800.md#paper-cui26h)
- <a id="gu26a-inference"></a>[SARL: Structure-Aligned Reinforcement Learning for Bridging the Perception-Action Gap in Airspace](../conferences/icml-2026/cards/1301-1400.md#paper-gu26a)
- <a id="guo26r-inference"></a>[RAD: Retrieval High-quality Demonstrations to Enhance Decision-making](../conferences/icml-2026/cards/1301-1400.md#paper-guo26r)
- <a id="howard26a-inference"></a>[Recursive Monte-Carlo Tree Search](../conferences/icml-2026/cards/1601-1700.md#paper-howard26a)
- <a id="kim26bq-inference"></a>[Identifiable Token Correspondence for World Models](../conferences/icml-2026/cards/2101-2200.md#paper-kim26bq)

<a id="by-representation-learning"></a>

### 表征学习

- <a id="bastankhah26a-representation-learning"></a>[Learning to Perceive the World Through Control: Empowerment-Based Representation Learning](../conferences/icml-2026/cards/0201-0300.md#paper-bastankhah26a)
- <a id="huber26a-representation-learning"></a>[Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-Dimensional Control Tasks](../conferences/icml-2026/cards/1701-1800.md#paper-huber26a)
- <a id="hyeon26a-representation-learning"></a>[Action-Sufficient Goal Representations](../conferences/icml-2026/cards/1801-1900.md#paper-hyeon26a)
- <a id="je-gal26a-representation-learning"></a>[Factorized Scheduling Principle: Learning Interpretable and Transferable Policies via Structured Additive Functions](../conferences/icml-2026/cards/1801-1900.md#paper-je-gal26a)
- <a id="kang26f-representation-learning"></a>[Latent Representation Alignment for Offline Goal-Conditioned Reinforcement Learning](../conferences/icml-2026/cards/2001-2100.md#paper-kang26f)
- <a id="kim26x-representation-learning"></a>[Compositional Transduction with Latent Analogies for Offline Goal-Conditioned Reinforcement Learning](../conferences/icml-2026/cards/2101-2200.md#paper-kim26x)

<a id="by-evaluation"></a>

### 评测与诊断

- <a id="bates26a-evaluation"></a>[Beyond Rewards in RL for Cyber Defence](../conferences/icml-2026/cards/0201-0300.md#paper-bates26a)
- <a id="cherepanov26a-evaluation"></a>[KAGE-Bench: Fast Known-Axis Visual Generalization Evaluation for Reinforcement Learning](../conferences/icml-2026/cards/0701-0800.md#paper-cherepanov26a)
- <a id="guo26f-evaluation"></a>[PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent](../conferences/icml-2026/cards/1301-1400.md#paper-guo26f)
- <a id="jing26d-evaluation"></a>[Benchmarking the Limits of In-Context Reinforcement Learning for Ad-Hoc Teamwork](../conferences/icml-2026/cards/1901-2000.md#paper-jing26d)
- <a id="lazri26a-evaluation"></a>[MAFE: Enabling Equitable Algorithm Design in Multi-Agent Multi-Stage Decision-Making Systems](../conferences/icml-2026/cards/2201-2300.md#paper-lazri26a)
- <a id="lee26az-evaluation"></a>[TABX: A High-Throughput Sandbox Battle Simulator for Multi-Agent Reinforcement Learning](../conferences/icml-2026/cards/2301-2400.md#paper-lee26az)

<a id="by-theory-statistics"></a>

### 理论与统计

- <a id="abbadi26a-theory-statistics"></a>[What Preferences Can—and Cannot—Predict in Multi-Agent Online Learning](../conferences/icml-2026/cards/0001-0100.md#paper-abbadi26a)
- <a id="anagnostides26b-theory-statistics"></a>[(Doubly) Exponential Lower Bounds for Follow the Regularized Leader in Potential Games](../conferences/icml-2026/cards/0001-0100.md#paper-anagnostides26b)
- <a id="anderson26a-theory-statistics"></a>[The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes](../conferences/icml-2026/cards/0001-0100.md#paper-anderson26a)
- <a id="ann26a-theory-statistics"></a>[Generalized Linear Bandits with Memory](../conferences/icml-2026/cards/0001-0100.md#paper-ann26a)
- <a id="arora26b-theory-statistics"></a>[Minimax-Optimal Policy Regret in Partially Observable Markov Games](../conferences/icml-2026/cards/0101-0200.md#paper-arora26b)
- <a id="balagopalan26a-theory-statistics"></a>[Fixed Budget is No Harder Than Fixed Confidence in Best-Arm Identification up to Logarithmic Factors](../conferences/icml-2026/cards/0101-0200.md#paper-balagopalan26a)
- <a id="balcan26a-theory-statistics"></a>[Learning in Structured Stackelberg Games](../conferences/icml-2026/cards/0101-0200.md#paper-balcan26a)
- <a id="banihashem26a-theory-statistics"></a>[Bandit Social Learning with Exploration Episodes](../conferences/icml-2026/cards/0201-0300.md#paper-banihashem26a)
- <a id="barbara26a-theory-statistics"></a>[Optimal Rates for Feasible Payoff Set Estimation in Games](../conferences/icml-2026/cards/0201-0300.md#paper-barbara26a)
- <a id="benyamine26a-theory-statistics"></a>[Dynamic Programming for Epistemic Uncertainty in Markov Decision Processes](../conferences/icml-2026/cards/0201-0300.md#paper-benyamine26a)
- <a id="bollini26a-theory-statistics"></a>[Learning in Bayesian Stackelberg Games With Unknown Follower’s Types](../conferences/icml-2026/cards/0301-0400.md#paper-bollini26a)
- <a id="braverman26a-theory-statistics"></a>[Online Learning with Recency: Algorithms for Sliding-window Streaming Multi-armed Bandits](../conferences/icml-2026/cards/0301-0400.md#paper-braverman26a)
- <a id="cao26x-theory-statistics"></a>[Understanding Behavior Cloning with Action Quantization](../conferences/icml-2026/cards/0401-0500.md#paper-cao26x)
- <a id="carr26a-theory-statistics"></a>[Reinforcement Learning with Pairwise Preferences in Long-Term Decision Problems](../conferences/icml-2026/cards/0401-0500.md#paper-carr26a)
- <a id="chen26dy-theory-statistics"></a>[Noise as a Natural Regularizer in Markov Decision Processes: Connecting Environmental Stochasticity and Policy Simplicity](../conferences/icml-2026/cards/0501-0600.md#paper-chen26dy)
- <a id="chen26ef-theory-statistics"></a>[A Causal Decomposition Approach for Fair Contextual Multi-Armed Bandits](../conferences/icml-2026/cards/0601-0700.md#paper-chen26ef)
- <a id="chen26gk-theory-statistics"></a>[Offline Two-Player Zero-Sum Markov Games with KL Regularization](../conferences/icml-2026/cards/0601-0700.md#paper-chen26gk)
- <a id="drago26a-theory-statistics"></a>[Online Compatible Reward Identification from Preference Feedback](../conferences/icml-2026/cards/0901-1000.md#paper-drago26a)
- <a id="ebi26a-theory-statistics"></a>[Informed Asymmetric Actor-Critic: Leveraging Privileged Signals Beyond Full-State Access](../conferences/icml-2026/cards/1001-1100.md#paper-ebi26a)
- <a id="escamilla26a-theory-statistics"></a>[When Can You Poison Rewards? A Tight Characterization of Reward Poisoning in Linear MDPs](../conferences/icml-2026/cards/1001-1100.md#paper-escamilla26a)
- <a id="faizal26a-theory-statistics"></a>[Local Policies for Graph-Structured Markov Decision Processes](../conferences/icml-2026/cards/1001-1100.md#paper-faizal26a)
- <a id="flynn26b-theory-statistics"></a>[Posterior Sampling Reinforcement Learning with Gaussian Processes for Continuous Control: Sublinear Regret Bounds for Unbounded State Spaces](../conferences/icml-2026/cards/1101-1200.md#paper-flynn26b)
- <a id="gauthier26a-theory-statistics"></a>[Anytime Detection of Strategic Deviations in Multi-Agent Systems](../conferences/icml-2026/cards/1201-1300.md#paper-gauthier26a)
- <a id="ghugare26a-theory-statistics"></a>[On the Role of Computation in Reinforcement Learning](../conferences/icml-2026/cards/1201-1300.md#paper-ghugare26a)
- <a id="giorgi26a-theory-statistics"></a>[Impact of Connectivity on Laplacian Representations in Reinforcement Learning](../conferences/icml-2026/cards/1201-1300.md#paper-giorgi26a)
- <a id="gong26i-theory-statistics"></a>[The Cost of Information: Phase Transitions in Contextual Bandits with Paid Observations](../conferences/icml-2026/cards/1301-1400.md#paper-gong26i)
- <a id="han26z-theory-statistics"></a>[Non-Uniform Noise-to-Signal Ratio in the REINFORCE Policy-Gradient Estimator](../conferences/icml-2026/cards/1401-1500.md#paper-han26z)
- <a id="hopkins26b-theory-statistics"></a>[From Generative to Episodic: Sample-Efficient Replicable Reinforcement Learning](../conferences/icml-2026/cards/1501-1600.md#paper-hopkins26b)
- <a id="hu26f-theory-statistics"></a>[Finite-time Convergence Analysis of Actor-Critic with Evolving Reward](../conferences/icml-2026/cards/1601-1700.md#paper-hu26f)
- <a id="hu26bc-theory-statistics"></a>[Near-Minimax Multi-Objective RL under Predictable Adversarial Preferences and Preference-Free Exploration in Linear MDPs](../conferences/icml-2026/cards/1601-1700.md#paper-hu26bc)
- <a id="huang26x-theory-statistics"></a>[Breaking the Computational Barrier: Provably Efficient Actor–Critic for Low-Rank MDPs](../conferences/icml-2026/cards/1701-1800.md#paper-huang26x)
- <a id="hudson26a-theory-statistics"></a>[Corrigibility Transformation: Constructing Goals That Accept Updates](../conferences/icml-2026/cards/1701-1800.md#paper-hudson26a)
- <a id="hwang26c-theory-statistics"></a>[Box Thirding: Anytime Best Arm Identification under Insufficient Sampling](../conferences/icml-2026/cards/1701-1800.md#paper-hwang26c)
- <a id="ipsen26a-theory-statistics"></a>[Revenue Guarantees of No-Swap-Regret Dynamics in First Price Auctions](../conferences/icml-2026/cards/1801-1900.md#paper-ipsen26a)
- <a id="ji26n-theory-statistics"></a>[Near-Optimal Regret for KL-Regularized Multi-Armed Bandits](../conferences/icml-2026/cards/1801-1900.md#paper-ji26n)
- <a id="kim26ar-theory-statistics"></a>[Follow-the-Perturbed-Leader for Decoupled Bandits: Best-of-Both-Worlds and Practicality](../conferences/icml-2026/cards/2101-2200.md#paper-kim26ar)
- <a id="kock26a-theory-statistics"></a>[Deep Reinforcement Learning Finds Bayes-Nash Equilibrium in Competitive Newsvendor Problems](../conferences/icml-2026/cards/2101-2200.md#paper-kock26a)
- <a id="labbi26a-theory-statistics"></a>[Refined Analysis of Entropy-Regularized Actor-Critic](../conferences/icml-2026/cards/2201-2300.md#paper-labbi26a)
- <a id="lambrecht26a-theory-statistics"></a>[Population-Aware Imitation Learning in Mean-field Games with Common Noise](../conferences/icml-2026/cards/2201-2300.md#paper-lambrecht26a)
- <a id="lederer26a-theory-statistics"></a>[Policy Search via Bayesian Optimization with Temporal Difference Gaussian Processes](../conferences/icml-2026/cards/2301-2400.md#paper-lederer26a)
- <a id="lee26o-theory-statistics"></a>[Minimax Optimal Strategy for Delayed Observations in Online Reinforcement Learning](../conferences/icml-2026/cards/2301-2400.md#paper-lee26o)
- <a id="lee26bf-theory-statistics"></a>[Emergent Communication Under Misinformation](../conferences/icml-2026/cards/2301-2400.md#paper-lee26bf)
- <a id="lefebvre26a-theory-statistics"></a>[The Cost of Commitment in Option-Based Hierarchical RL](../conferences/icml-2026/cards/2301-2400.md#paper-lefebvre26a)
- <a id="levy26a-theory-statistics"></a>[Optimal Regret for Policy Optimization in Contextual Bandits](../conferences/icml-2026/cards/2301-2400.md#paper-levy26a)
- <a id="levy26b-theory-statistics"></a>[Near-Optimal Regret for Policy Optimization in Contextual MDPs with General Offline Function Approximation](../conferences/icml-2026/cards/2301-2400.md#paper-levy26b)
<!-- classification:end -->
