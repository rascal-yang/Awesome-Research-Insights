# 图学习与推荐

[首页](../README.md) · [English](../en/papers/graph-and-recommendation.md)

图模型、知识图谱与推荐系统。

<!-- classification:start -->
## 按技术类型浏览

[模型架构](#by-architecture) · [模块](#by-modules) · [损失函数](#by-loss-functions) · [优化](#by-optimization) · [强化学习方法](#by-reinforcement-learning) · [训练策略](#by-training-strategies) · [数据策略](#by-data-strategies) · [推理策略](#by-inference) · [表征学习](#by-representation-learning) · [评测与诊断](#by-evaluation) · [理论与统计](#by-theory-statistics)

<a id="by-architecture"></a>

### 模型架构

- <a id="bandyopadhyay26a-architecture"></a>[RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation](../conferences/icml-2026/cards/0201-0300.md#paper-bandyopadhyay26a)
- <a id="chen26al-architecture"></a>[OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search](../conferences/icml-2026/cards/0501-0600.md#paper-chen26al)
- <a id="de-castelli26a-architecture"></a>[Adaptive Memory Retention in Dynamic Graphs](../conferences/icml-2026/cards/0801-0900.md#paper-de-castelli26a)
- <a id="eliasof26a-architecture"></a>[Graph Neural Dynamics via Learned Energy and Tangential Flows](../conferences/icml-2026/cards/1001-1100.md#paper-eliasof26a)
- <a id="fang26g-architecture"></a>[MC-HNN: Learning Latent Structural Semantics and High-Rank Representations for Hypergraph Neural Networks](../conferences/icml-2026/cards/1001-1100.md#paper-fang26g)
- <a id="fernandez26a-architecture"></a>[L2G-NET: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations](../conferences/icml-2026/cards/1101-1200.md#paper-fernandez26a)
- <a id="gailhard26a-architecture"></a>[Feature-Aware (Hyper)graph Generation via Next-Scale Prediction](../conferences/icml-2026/cards/1101-1200.md#paper-gailhard26a)
- <a id="gantes26a-architecture"></a>[SuperHype: Hypergraph Generation via Graph-Superposition Decomposition](../conferences/icml-2026/cards/1201-1300.md#paper-gantes26a)
- <a id="hossen26a-architecture"></a>[Hierarchical Multi Scale Graph Neural Networks: Scalable Heterophilous Learning with Oversmoothing and Oversquashing Mitigation](../conferences/icml-2026/cards/1601-1700.md#paper-hossen26a)
- <a id="huang26ax-architecture"></a>[Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning](../conferences/icml-2026/cards/1701-1800.md#paper-huang26ax)
- <a id="huang26cj-architecture"></a>[GeoFlow: Geo-Aware Modeling of Inter-Area Relationships in Origin-Destination Flow Prediction and Generation](../conferences/icml-2026/cards/1701-1800.md#paper-huang26cj)
- <a id="johnson26a-architecture"></a>[VDW-GNNs: Vector diffusion wavelets for geometric graph neural networks](../conferences/icml-2026/cards/1901-2000.md#paper-johnson26a)
- <a id="liu26x-architecture"></a>[Learning Graph Foundation Models on Riemannian Graph-of-Graphs](../conferences/icml-2026/cards/2801-2900.md#paper-liu26x)
- <a id="liu26ep-architecture"></a>[Ramba: Selective State-Space Models for Relational Deep Learning](../conferences/icml-2026/cards/2901-3000.md#paper-liu26ep)
- <a id="marcoccia26a-architecture"></a>[NetDiff: Graph Diffusion with Improved Global Capabilities to Generate and Update Mobile Network Topologies](../conferences/icml-2026/cards/3201-3300.md#paper-marcoccia26a)
- <a id="miao26e-architecture"></a>[LLM-MatLogic: Executable Exchange Contracts for Knowledge-Graph Query Answering with Scoped Negation](../conferences/icml-2026/cards/3201-3300.md#paper-miao26e)
- <a id="mo26a-architecture"></a>[Entangled No More: Multi-Domain Decoupling for Robust Dynamic Graph Neural Networks](../conferences/icml-2026/cards/3301-3400.md#paper-mo26a)
- <a id="nikolentzos26a-architecture"></a>[InvGNN: Learning Invertible Node Representations on Graphs](../conferences/icml-2026/cards/3401-3500.md#paper-nikolentzos26a)
- <a id="peng26e-architecture"></a>[Sheaf Neural Networks on SPD Manifolds: Second-Order Geometric Representation Learning](../conferences/icml-2026/cards/3601-3700.md#paper-peng26e)
- <a id="qi26j-architecture"></a>[Lightweight and Interpretable Transformer via Mixed Graph Algorithm Unrolling for Traffic Forecast](../conferences/icml-2026/cards/3701-3800.md#paper-qi26j)
- <a id="qian26e-architecture"></a>[On the Expressive Power of GNNs to Solve Linear SDPs](../conferences/icml-2026/cards/3701-3800.md#paper-qian26e)
- <a id="raghuvanshi26a-architecture"></a>[Learning Long Range Spatio-Temporal Representations over Continuous Time Dynamic Graphs with State Space Models](../conferences/icml-2026/cards/3701-3800.md#paper-raghuvanshi26a)
- <a id="seely26a-architecture"></a>[Learning Multi-Agent Coordination via Sheaf-ADMM](../conferences/icml-2026/cards/3901-4000.md#paper-seely26a)
- <a id="shi26t-architecture"></a>[S$^3$GNN: Efficient Global Mixing and Local Message Passing for Long-Range Graph Learning](../conferences/icml-2026/cards/4101-4200.md#paper-shi26t)
- <a id="sun26e-architecture"></a>[Adaptive Recurrent Message Passing for Test Time Computing on Graphs](../conferences/icml-2026/cards/4201-4300.md#paper-sun26e)
- <a id="wang26m-architecture"></a>[Full-Spectrum Graph Neural Networks: Expressive and Scalable](../conferences/icml-2026/cards/4501-4600.md#paper-wang26m)
- <a id="wang26kj-architecture"></a>[Expressive Graph Neural Networks via Equivariant Use of Noise](../conferences/icml-2026/cards/4801-4900.md#paper-wang26kj)
- <a id="xiao26j-architecture"></a>[Capacity-Agnostic Parameter Isolation for Continual Graph Learning](../conferences/icml-2026/cards/5101-5200.md#paper-xiao26j)

<a id="by-modules"></a>

### 模块

- <a id="bai26i-modules"></a>[GI-GCN: Global Interacted Graph Convolutional Networks via Dominant Sets for Graph Classification](../conferences/icml-2026/cards/0101-0200.md#paper-bai26i)
- <a id="barcelo26a-modules"></a>[Message Passing on the Edge: Towards Scalable and Expressive GNNs](../conferences/icml-2026/cards/0201-0300.md#paper-barcelo26a)
- <a id="chen26gm-modules"></a>[Weaving Graph over Tokens: Contextualizing Structured Sequences for LLMs](../conferences/icml-2026/cards/0601-0700.md#paper-chen26gm)
- <a id="choi26d-modules"></a>[Gauge-Equivariant Graph Networks via Self-Interference Cancellation](../conferences/icml-2026/cards/0701-0800.md#paper-choi26d)
- <a id="fesser26b-modules"></a>[Unitary Convolutions for Message-passing and Positional Encodings on Directed Graphs](../conferences/icml-2026/cards/1101-1200.md#paper-fesser26b)
- <a id="krahn26a-modules"></a>[Collapsed Effective Operators for Higher-order Structures](../conferences/icml-2026/cards/2201-2300.md#paper-krahn26a)
- <a id="liu26gb-modules"></a>[Modeling Spectral Energy Shifts in Spatio-Temporal Graph Anomaly Detection](../conferences/icml-2026/cards/2901-3000.md#paper-liu26gb)
- <a id="reid26a-modules"></a>[Rotary Position Encodings for Graphs](../conferences/icml-2026/cards/3801-3900.md#paper-reid26a)
- <a id="sim26b-modules"></a>[Learning Multi-Scale Hypergraph for High-Order Brain Connectivity Analysis](../conferences/icml-2026/cards/4101-4200.md#paper-sim26b)
- <a id="sun26f-modules"></a>[Enhancing LLMs for Graph Tasks via Graph-aware LoRA Generation](../conferences/icml-2026/cards/4201-4300.md#paper-sun26f)
- <a id="yan26i-modules"></a>[MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning](../conferences/icml-2026/cards/5301-5400.md#paper-yan26i)
- <a id="yang26cg-modules"></a>[Fast Mixture of Curvature-Aware Experts for Diverse and Dynamic Graph Topologies](../conferences/icml-2026/cards/5401-5500.md#paper-yang26cg)

<a id="by-loss-functions"></a>

### 损失函数

- <a id="chen26ez-loss-functions"></a>[Mitigating Reward Hacking in LLM-based Recommendation: A Preference Optimization Approach](../conferences/icml-2026/cards/0601-0700.md#paper-chen26ez)
- <a id="chen26gx-loss-functions"></a>[ST-TGExplainer: Disentangling Stability and Transition Patterns for Temporal GNN Interpretability](../conferences/icml-2026/cards/0601-0700.md#paper-chen26gx)
- <a id="deng26u-loss-functions"></a>[Discriminative Mixture-of-Experts on Graphs with Reliable Expert Fusion](../conferences/icml-2026/cards/0801-0900.md#paper-deng26u)
- <a id="ding26v-loss-functions"></a>[Discriminative Attribute Graph Clustering Through Topology-Guided Contrastive Learning](../conferences/icml-2026/cards/0901-1000.md#paper-ding26v)
- <a id="downer26a-loss-functions"></a>[Watermarking Graph Neural Networks via Explanations for Ownership Protection](../conferences/icml-2026/cards/0901-1000.md#paper-downer26a)
- <a id="lee26w-loss-functions"></a>[Rethinking Contrastive Learning for Graph Collaborative Filtering: Limitations and a Simple Remedy](../conferences/icml-2026/cards/2301-2400.md#paper-lee26w)
- <a id="ran26c-loss-functions"></a>[Differentially Private Cross-Silo Recommendation from Implicit Feedback](../conferences/icml-2026/cards/3801-3900.md#paper-ran26c)
- <a id="siampou26a-loss-functions"></a>[Mobility-Embedded POIs: Learning What A Place Is and How It Is Used from Human Movement](../conferences/icml-2026/cards/4101-4200.md#paper-siampou26a)
- <a id="tian26h-loss-functions"></a>[Learning Discriminative and Generalizable Anomaly Detector for Dynamic Graph with Limited Supervision](../conferences/icml-2026/cards/4401-4500.md#paper-tian26h)
- <a id="wang26hb-loss-functions"></a>[Learnable Kernel Density Estimation for Graphs and Its Application to Graph-Level Anomaly Detection](../conferences/icml-2026/cards/4701-4800.md#paper-wang26hb)
- <a id="wu26j-loss-functions"></a>[Multi-scale Explainer for Graph Neural Networks](../conferences/icml-2026/cards/5001-5100.md#paper-wu26j)
- <a id="xu26a-loss-functions"></a>[SFCLTA: Spectral Fusion Contrastive Learning with Topology-Adaptive Graph Augmentation](../conferences/icml-2026/cards/5201-5300.md#paper-xu26a)
- <a id="yu26am-loss-functions"></a>[Improving LLM-Based Recommenders with Conservative Generative Flow Networks](../conferences/icml-2026/cards/5601-5700.md#paper-yu26am)
- <a id="zhang26ds-loss-functions"></a>[SAOT: Self-Supervised Continual Graph Learning with Structure-Aware Optimal Transport](../conferences/icml-2026/cards/5801-5900.md#paper-zhang26ds)

<a id="by-optimization"></a>

### 优化

- <a id="bai26g-optimization"></a>[Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle](../conferences/icml-2026/cards/0101-0200.md#paper-bai26g)
- <a id="chakraborty26b-optimization"></a>[Fairness in Aggregation: Optimal Top-$k$ and Improved Full Ranking](../conferences/icml-2026/cards/0401-0500.md#paper-chakraborty26b)
- <a id="chen26b-optimization"></a>[Differentially Private Range Subgraph Counting](../conferences/icml-2026/cards/0401-0500.md#paper-chen26b)
- <a id="cheng26j-optimization"></a>[What Makes a Desired Graph for Relational Deep Learning?](../conferences/icml-2026/cards/0601-0700.md#paper-cheng26j)
- <a id="gupta26b-optimization"></a>[Adapting to Evolving Graphs: A Scalable Framework for Dynamic Coarsening](../conferences/icml-2026/cards/1401-1500.md#paper-gupta26b)
- <a id="hosseini26b-optimization"></a>[Neural Dispersion on Graphs](../conferences/icml-2026/cards/1601-1700.md#paper-hosseini26b)
- <a id="huang26k-optimization"></a>[Homophily-Heterogeneity Gradient Surgery for Federated Graph Learning](../conferences/icml-2026/cards/1601-1700.md#paper-huang26k)
- <a id="huang26az-optimization"></a>[Attributed Network Alignment: Statistical Limits and Efficient Algorithm](../conferences/icml-2026/cards/1701-1800.md#paper-huang26az)
- <a id="huang26bi-optimization"></a>[Towards Generative Graph Matching for Graph Edit Distance Computation](../conferences/icml-2026/cards/1701-1800.md#paper-huang26bi)
- <a id="huang26bz-optimization"></a>[Optimal Transport–Guided Stochastic Control for Graph Combinatorial Optimization](../conferences/icml-2026/cards/1701-1800.md#paper-huang26bz)
- <a id="jaziri26a-optimization"></a>[Generative Large Neighborhood Search: Scalable Set Cover Optimization via Discrete Diffusion](../conferences/icml-2026/cards/1801-1900.md#paper-jaziri26a)
- <a id="john26a-optimization"></a>[An Approximation Algorithm for Graph Label Selection](../conferences/icml-2026/cards/1901-2000.md#paper-john26a)
- <a id="jourdan26a-optimization"></a>[Fully Dynamic Coreset Spectral Clustering](../conferences/icml-2026/cards/2001-2100.md#paper-jourdan26a)
- <a id="kataria26a-optimization"></a>[GraphFLEx: Unsupervised Structure Learning $\underline\textF$ramework for $\underline\textL$arge $\underline\textEx$panding $\underline\textGraph$s](../conferences/icml-2026/cards/2001-2100.md#paper-kataria26a)
- <a id="li26kb-optimization"></a>[COPF: An Online Framework for Deployment-Stable Counterfactual Fairness in Evolving Graphs](../conferences/icml-2026/cards/2601-2700.md#paper-li26kb)
- <a id="qian26d-optimization"></a>[Learning to Approximate Uniform Facility Location via Graph Neural Networks](../conferences/icml-2026/cards/3701-3800.md#paper-qian26d)
- <a id="wang26eh-optimization"></a>[Beyond Model Base Retrieval: Weaving Knowledge to Master Fine-grained Neural Network Design](../conferences/icml-2026/cards/4701-4800.md#paper-wang26eh)
- <a id="zhao26q-optimization"></a>[DiP-G: Discrete Prompting for Graph Neural Networks](../conferences/icml-2026/cards/6001-6100.md#paper-zhao26q)

<a id="by-reinforcement-learning"></a>

### 强化学习方法

- <a id="agarwal26a-reinforcement-learning"></a>[Efficient Online Influence Maximization under the Independent Cascade Model with Node-Level Feedback](../conferences/icml-2026/cards/0001-0100.md#paper-agarwal26a)
- <a id="bisht26a-reinforcement-learning"></a>[CORAL: Uncertainty-Aware Regulation of Exposure Concentration in Recommender Systems](../conferences/icml-2026/cards/0201-0300.md#paper-bisht26a)
- <a id="hou26g-reinforcement-learning"></a>[ProRL: Effective Reinforcement Learning for Proactive Recommendation via Rectified Policy Gradient Estimation](../conferences/icml-2026/cards/1601-1700.md#paper-hou26g)
- <a id="kiyohara26a-reinforcement-learning"></a>[Credit-assigned Policy Gradient for Early Stage Retrieval in Two-stage Ranking](../conferences/icml-2026/cards/2101-2200.md#paper-kiyohara26a)
- <a id="li26w-reinforcement-learning"></a>[Incentivized Exploration with Stochastic Covariates: A Two-Stage Mechanism Design for Recommender System](../conferences/icml-2026/cards/2401-2500.md#paper-li26w)

<a id="by-training-strategies"></a>

### 训练策略

- <a id="arafat26a-training-strategies"></a>[Adversarial Attacks and Robust Training for Hypergraph Neural Networks](../conferences/icml-2026/cards/0101-0200.md#paper-arafat26a)
- <a id="canturk26a-training-strategies"></a>[Can Computational Reducibility Lead to Transferable Models for Graph Combinatorial Optimization?](../conferences/icml-2026/cards/0301-0400.md#paper-canturk26a)
- <a id="chen26cz-training-strategies"></a>[Message Tuning Outshines Graph Prompt Tuning: A Prismatic Space Perspective](../conferences/icml-2026/cards/0501-0600.md#paper-chen26cz)
- <a id="gosch26a-training-strategies"></a>[Certifying Graph Neural Networks Against Label and Structure Poisoning](../conferences/icml-2026/cards/1301-1400.md#paper-gosch26a)
- <a id="grover26a-training-strategies"></a>[Feedback Control for Multi-Objective Graph Self-Supervision](../conferences/icml-2026/cards/1301-1400.md#paper-grover26a)
- <a id="li26fv-training-strategies"></a>[FedRGL: Robust Federated Graph Learning under Label Noise](../conferences/icml-2026/cards/2501-2600.md#paper-li26fv)
- <a id="li26ih-training-strategies"></a>[Being More Lightweight and Practical: Mini-sized Contrastive Learning Pre-trained Models for Fine-grained Traffic Task](../conferences/icml-2026/cards/2601-2700.md#paper-li26ih)
- <a id="liu26b-training-strategies"></a>[FlatLand: Personalized Graph Federated Learning via Tailored Lorentz Space](../conferences/icml-2026/cards/2701-2800.md#paper-liu26b)
- <a id="navarro26a-training-strategies"></a>[Adaptive Node Feature Selection for Graph Neural Networks](../conferences/icml-2026/cards/3401-3500.md#paper-navarro26a)
- <a id="pan26h-training-strategies"></a>[Problem Distributions as Tasks: Repurposing Meta Learning for Generative Combinatorial Optimization towards Multi-task Pretraining and Adaptation](../conferences/icml-2026/cards/3501-3600.md#paper-pan26h)
- <a id="prakash26c-training-strategies"></a>[Obliviate: Efficient Unlearning in Recommender Systems](../conferences/icml-2026/cards/3601-3700.md#paper-prakash26c)
- <a id="saber26a-training-strategies"></a>[RADE: Random Add-Drop Edge as a Regularizer](../conferences/icml-2026/cards/3901-4000.md#paper-saber26a)
- <a id="yue26c-training-strategies"></a>[Revisiting Pre-Propagation GNNs: Robust Diffusion Operators and Hidden-State Re-Propagation](../conferences/icml-2026/cards/5601-5700.md#paper-yue26c)

<a id="by-data-strategies"></a>

### 数据策略

- <a id="azizpour26a-data-strategies"></a>[From Moments to Models: Graphon-Mixture Learning for Mixup and Contrastive Learning](../conferences/icml-2026/cards/0101-0200.md#paper-azizpour26a)
- <a id="chen26cr-data-strategies"></a>[DANCE: Dynamic, Available, Neighbor-gated Condensation for Federated Text-Attributed Graphs](../conferences/icml-2026/cards/0501-0600.md#paper-chen26cr)
- <a id="eremeev26a-data-strategies"></a>[GraphPFN: A Prior-Data Fitted Graph Foundation Model](../conferences/icml-2026/cards/1001-1100.md#paper-eremeev26a)
- <a id="hou26c-data-strategies"></a>[HIAL: Towards Semantics-Aware Hypergraph Active Learning via Dual-Perspective Information Maximization](../conferences/icml-2026/cards/1601-1700.md#paper-hou26c)
- <a id="ju26c-data-strategies"></a>[Identifying and Correcting Label Noise for Robust GNNs via Influence Contradiction](../conferences/icml-2026/cards/2001-2100.md#paper-ju26c)
- <a id="kothapalli26a-data-strategies"></a>[PluRel: Synthetic Data unlocks Scaling Laws for Relational Foundation Models](../conferences/icml-2026/cards/2201-2300.md#paper-kothapalli26a)
- <a id="li26gi-data-strategies"></a>[Anchor-guided Hypergraph Condensation with Dual-level Discrimination](../conferences/icml-2026/cards/2501-2600.md#paper-li26gi)
- <a id="li26hb-data-strategies"></a>[GOCM: Single-Step Graph Outlier Synthesis via Origin Consistency Model](../conferences/icml-2026/cards/2601-2700.md#paper-li26hb)
- <a id="tang26l-data-strategies"></a>[Reconstruction Outcomes Look Similar but Processes Differ: Improving Context Consistency and Coverage in Graph Masked Auto-Encoder](../conferences/icml-2026/cards/4301-4400.md#paper-tang26l)
- <a id="wang26db-data-strategies"></a>[Negative Sampling From the Ground Up: A Redesign for Recommendations](../conferences/icml-2026/cards/4601-4700.md#paper-wang26db)
- <a id="wang26jz-data-strategies"></a>[Relational In-Context Learning via Synthetic Pre-training with Structural Prior](../conferences/icml-2026/cards/4801-4900.md#paper-wang26jz)
- <a id="wen26j-data-strategies"></a>[Progressive Graph Structure Adjustment for Homophily Shift Adaptation](../conferences/icml-2026/cards/4901-5000.md#paper-wen26j)
- <a id="wu26ac-data-strategies"></a>[Scalable Topology-Preserving Graph Coarsening: Concepts and Algorithms](../conferences/icml-2026/cards/5001-5100.md#paper-wu26ac)
- <a id="yao26e-data-strategies"></a>[H$^2$CL: Heterogeneity-Aware Hypergraph Contrastive Learning for Robust Representation Learning](../conferences/icml-2026/cards/5401-5500.md#paper-yao26e)
- <a id="yin26d-data-strategies"></a>[Rel-MOSS: Towards Imbalanced Relational Deep Learning on Relational Databases](../conferences/icml-2026/cards/5501-5600.md#paper-yin26d)
- <a id="zhang26gf-data-strategies"></a>[Can Recommender Systems Teach Themselves? A Recursive Self-Improving Framework with Fidelity Control](../conferences/icml-2026/cards/5901-6000.md#paper-zhang26gf)

<a id="by-inference"></a>

### 推理策略

- <a id="ai26c-inference"></a>[PromptDyG: Test-Time Prompt Adaptation on Dynamic Graphs](../conferences/icml-2026/cards/0001-0100.md#paper-ai26c)
- <a id="bisht26b-inference"></a>[CARE: Adaptive Calibration for Reliable Recommendations](../conferences/icml-2026/cards/0201-0300.md#paper-bisht26b)
- <a id="fomina26a-inference"></a>[On Efficient Scaling of GNNs via IO-Aware Layers Implementations](../conferences/icml-2026/cards/1101-1200.md#paper-fomina26a)
- <a id="gao26t-inference"></a>[Beyond Explicit Edges: Robust Reasoning over Noisy and Sparse Knowledge Graphs](../conferences/icml-2026/cards/1201-1300.md#paper-gao26t)
- <a id="guo26t-inference"></a>[GRASP: Graph Reasoning via Agentic Solving and Probing of LLMs](../conferences/icml-2026/cards/1301-1400.md#paper-guo26t)
- <a id="guo26ac-inference"></a>[X-EviProbe: Post-hoc Parameter-Free Evidential Uncertainty Quantification for Frozen Graph Neural Networks](../conferences/icml-2026/cards/1301-1400.md#paper-guo26ac)
- <a id="jiang26al-inference"></a>[GFMate: Empowering Graph Foundation Models with Test-time Prompt Tuning](../conferences/icml-2026/cards/1901-2000.md#paper-jiang26al)
- <a id="li26gz-inference"></a>[LoRe: Adaptive Interaction-Evaluation Routing with Per-step Interaction Budgets for Iterative Graph Solvers](../conferences/icml-2026/cards/2501-2600.md#paper-li26gz)
- <a id="lu26s-inference"></a>[Information-Geometric Adaptive Sampling for Graph Diffusion](../conferences/icml-2026/cards/3001-3100.md#paper-lu26s)
- <a id="luo26s-inference"></a>[SimGFM: Simplifying Discrete Flow Matching for Graph Generation](../conferences/icml-2026/cards/3001-3100.md#paper-luo26s)
- <a id="olausson26a-inference"></a>[Amortizing Maximum Inner Product Search with Learned Support Functions](../conferences/icml-2026/cards/3501-3600.md#paper-olausson26a)
- <a id="xiong26a-inference"></a>[Variational Bayesian Flow Network for Graph Generation](../conferences/icml-2026/cards/5101-5200.md#paper-xiong26a)
- <a id="zhang26fh-inference"></a>[Hard-Constrained Graph Generation with Discrete-Projection Diffusion](../conferences/icml-2026/cards/5801-5900.md#paper-zhang26fh)

<a id="by-representation-learning"></a>

### 表征学习

- <a id="behmanesh26a-representation-learning"></a>[Graph Alignment via Dual-Pass Spectral Encoding and Latent Space Communication](../conferences/icml-2026/cards/0201-0300.md#paper-behmanesh26a)
- <a id="cai26f-representation-learning"></a>[CONTEXTOR: Contextualized High-order Contrastive Learning](../conferences/icml-2026/cards/0301-0400.md#paper-cai26f)
- <a id="chen26ak-representation-learning"></a>[SynGR: Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation](../conferences/icml-2026/cards/0501-0600.md#paper-chen26ak)
- <a id="chen26fu-representation-learning"></a>[Boundary Embedding Shaping with Adaptive Contrastive Learning for Graph Structural Disentanglement](../conferences/icml-2026/cards/0601-0700.md#paper-chen26fu)
- <a id="choromanski26a-representation-learning"></a>[Computationally-efficient Graph Modeling with Refined Graph Random Features](../conferences/icml-2026/cards/0701-0800.md#paper-choromanski26a)
- <a id="debaussart-joniec26a-representation-learning"></a>[Parametrized Power-Iteration Clustering for Directed Graphs](../conferences/icml-2026/cards/0801-0900.md#paper-debaussart-joniec26a)
- <a id="du26o-representation-learning"></a>[From Distribution to Geometry: Stable Graph Generalization via Invariant Barycenters](../conferences/icml-2026/cards/0901-1000.md#paper-du26o)
- <a id="ezoe26a-representation-learning"></a>[Unfolded Laplacian Spectral Embedding: A Theoretically Grounded Approach to Dynamic Network Representation](../conferences/icml-2026/cards/1001-1100.md#paper-ezoe26a)
- <a id="guo26p-representation-learning"></a>[CCLRec: Consensus-driven Contrastive Learning for LLM-enhanced Graph Recommendation](../conferences/icml-2026/cards/1301-1400.md#paper-guo26p)
- <a id="he26l-representation-learning"></a>[Structure-Centric Graph Foundation Model via Geometric Bases](../conferences/icml-2026/cards/1501-1600.md#paper-he26l)
- <a id="he26af-representation-learning"></a>[GP2F: Cross-Domain Graph Prompting with Adaptive Fusion of Pre-trained Graph Neural Networks](../conferences/icml-2026/cards/1501-1600.md#paper-he26af)
- <a id="he26at-representation-learning"></a>[A Graph Foundation Model with Cross-Modal Alignment and Modality-Aware Expert Fusion for Multi-Modal Graphs](../conferences/icml-2026/cards/1501-1600.md#paper-he26at)
- <a id="hu26x-representation-learning"></a>[Hierarchical Anchor Graph Learning for Multi-View Clustering](../conferences/icml-2026/cards/1601-1700.md#paper-hu26x)
- <a id="hu26ag-representation-learning"></a>[A Consensus Anchor-guided Hypergraph Framework for Incomplete Multi-view Clustering](../conferences/icml-2026/cards/1601-1700.md#paper-hu26ag)
- <a id="huang26bs-representation-learning"></a>[Exploring Motif-based Heterogeneous Graph Learning for ReDoS Detection](../conferences/icml-2026/cards/1701-1800.md#paper-huang26bs)
- <a id="jiang26b-representation-learning"></a>[Efficient Synthetic Network Generation via Latent Embedding Reconstruction](../conferences/icml-2026/cards/1901-2000.md#paper-jiang26b)
- <a id="lee26ad-representation-learning"></a>[Generative Representation Learning on Hyper-relational Knowledge Graphs via Masked Discrete Diffusion](../conferences/icml-2026/cards/2301-2400.md#paper-lee26ad)
- <a id="lee26ah-representation-learning"></a>[View Space: Learning Representation across Arbitrary Graphs](../conferences/icml-2026/cards/2301-2400.md#paper-lee26ah)
- <a id="li26gu-representation-learning"></a>[CELL: A Causal Perspective for Fairness-aware Graph Adaptation](../conferences/icml-2026/cards/2501-2600.md#paper-li26gu)
- <a id="li26hm-representation-learning"></a>[Graph is a Substrate Across Data Modalities](../conferences/icml-2026/cards/2601-2700.md#paper-li26hm)
- <a id="liang26y-representation-learning"></a>[CL-GCL: Comprehensive and Lightweight Graph Contrastive Learning](../conferences/icml-2026/cards/2701-2800.md#paper-liang26y)
- <a id="liu26by-representation-learning"></a>[Toward Effective Multimodal Graph Foundation Model: A Divide-and-Conquer Based Approach](../conferences/icml-2026/cards/2801-2900.md#paper-liu26by)
- <a id="liu26cp-representation-learning"></a>[Rethinking Feature Alignment in Generalist Graph Anomaly Detection: A Relational Fingerprint-based Approach](../conferences/icml-2026/cards/2801-2900.md#paper-liu26cp)
- <a id="liu26eg-representation-learning"></a>[HVAE: Hyperbolic Variational Autoencoder For Flexible Knowledge Transfer Across Multiple Domains](../conferences/icml-2026/cards/2901-3000.md#paper-liu26eg)
- <a id="ma26aj-representation-learning"></a>[Seeking Commonality, Preserving Specificity: A Spectral-Aware Hierarchical Framework for Cross-City Road Representation Learning](../conferences/icml-2026/cards/3101-3200.md#paper-ma26aj)
- <a id="manenti26b-representation-learning"></a>[SWING: Unlocking Implicit Graph Representations for Graph Random Features](../conferences/icml-2026/cards/3201-3300.md#paper-manenti26b)
- <a id="mishra26c-representation-learning"></a>[Polaris: Coupled Orbital Polar Embeddings for Hierarchical Concept Learning](../conferences/icml-2026/cards/3301-3400.md#paper-mishra26c)
- <a id="nakis26a-representation-learning"></a>[Aitchison Embeddings for Learning Compositional Graph Representations](../conferences/icml-2026/cards/3401-3500.md#paper-nakis26a)
- <a id="rubio-madrigal26a-representation-learning"></a>[Fixed Aggregation Features Can Rival GNNs](../conferences/icml-2026/cards/3901-4000.md#paper-rubio-madrigal26a)
- <a id="shan26b-representation-learning"></a>[Revisiting Positive Samples in Graph Contrastive Learning: From the Perspective of Message Passing](../conferences/icml-2026/cards/4001-4100.md#paper-shan26b)
- <a id="shevkunov26a-representation-learning"></a>[Relevance-Based Embeddings: Lightweight Candidate Retrieval via Heavy-Ranker Calls](../conferences/icml-2026/cards/4001-4100.md#paper-shevkunov26a)
- <a id="sun26ab-representation-learning"></a>[Unsat Core Prediction through Polarity-Aware Representation Learning over Clause-Literal Hypergraphs](../conferences/icml-2026/cards/4301-4400.md#paper-sun26ab)
- <a id="truong26a-representation-learning"></a>[Plain Transformers are Surprisingly Powerful Link Predictors](../conferences/icml-2026/cards/4401-4500.md#paper-truong26a)
- <a id="wang26gl-representation-learning"></a>[What Information Matters? Graph Out-of-Distribution Detection via Tri-Component Information Decomposition](../conferences/icml-2026/cards/4701-4800.md#paper-wang26gl)
- <a id="xu26ce-representation-learning"></a>[No Need to Train Your RDB Foundation Model](../conferences/icml-2026/cards/5201-5300.md#paper-xu26ce)

<a id="by-evaluation"></a>

### 评测与诊断

- <a id="agbaje26a-evaluation"></a>[Revisiting Asymmetries in Black-box Link Stealing against Graph Neural Networks](../conferences/icml-2026/cards/0001-0100.md#paper-agbaje26a)
- <a id="akula26a-evaluation"></a>[Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors](../conferences/icml-2026/cards/0001-0100.md#paper-akula26a)
- <a id="ferrini26a-evaluation"></a>[Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution](../conferences/icml-2026/cards/1101-1200.md#paper-ferrini26a)
- <a id="forbat26a-evaluation"></a>[Is Graph Mixup Beneficial? Investigating Interpolation And Empirical Performance of Graph Mixup Methods](../conferences/icml-2026/cards/1101-1200.md#paper-forbat26a)
- <a id="guan26b-evaluation"></a>[VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion in Multimodal LLM Recommender Systems](../conferences/icml-2026/cards/1301-1400.md#paper-guan26b)
- <a id="heidari26a-evaluation"></a>[TN-SHAP-G: Graph-Structured Tensor Network Surrogates for Shapley Values and Interactions](../conferences/icml-2026/cards/1501-1600.md#paper-heidari26a)
- <a id="lagesse26a-evaluation"></a>[Graph Alignment for Benchmarking Graph Neural Networks and Learning Positional Encodings](../conferences/icml-2026/cards/2201-2300.md#paper-lagesse26a)
- <a id="liu26gd-evaluation"></a>[Towards the Explainability of Temporal Graph Networks via Memory Backtracking and Topological Attribution](../conferences/icml-2026/cards/2901-3000.md#paper-liu26gd)
- <a id="mukherjee26a-evaluation"></a>[BOCLOAK: Optimal Transport-Guided Adversarial Attacks on Graph Neural Network-Based Bot Detection](../conferences/icml-2026/cards/3301-3400.md#paper-mukherjee26a)
- <a id="selvam26a-evaluation"></a>[Gaming Consensus: Coordinated Manipulation in Crowdsourced Fact-Checking](../conferences/icml-2026/cards/3901-4000.md#paper-selvam26a)
- <a id="zhang26ih-evaluation"></a>[Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation](../conferences/icml-2026/cards/5901-6000.md#paper-zhang26ih)

<a id="by-theory-statistics"></a>

### 理论与统计

- <a id="amran26a-theory-statistics"></a>[A Graphop Analysis of Graph Neural Networks on Sparse Graphs: Generalization and Universal Approximation](../conferences/icml-2026/cards/0001-0100.md#paper-amran26a)
- <a id="badreddine26a-theory-statistics"></a>[On the Theoretical Limitations of Embedding-based Link Prediction](../conferences/icml-2026/cards/0101-0200.md#paper-badreddine26a)
- <a id="charpenay26a-theory-statistics"></a>[Faithful Relational Reasoning with Region-based Embeddings: Expressivity of Convex Coordinate-wise Models](../conferences/icml-2026/cards/0401-0500.md#paper-charpenay26a)
- <a id="colini-baldeschi26a-theory-statistics"></a>[Multicalibration Yields Better Matchings](../conferences/icml-2026/cards/0701-0800.md#paper-colini-baldeschi26a)
- <a id="fan26c-theory-statistics"></a>[Graph-Preference Learning: Debiasing Network-Sampled Human Feedback for Target Welfare Estimation](../conferences/icml-2026/cards/1001-1100.md#paper-fan26c)
- <a id="fetrat-qharabagh26a-theory-statistics"></a>[Learning to Execute Graph Algorithms Exactly with Graph Neural Networks](../conferences/icml-2026/cards/1101-1200.md#paper-fetrat-qharabagh26a)
- <a id="flora26a-theory-statistics"></a>[Understanding Truncated Positional Encodings for Graph Neural Networks](../conferences/icml-2026/cards/1101-1200.md#paper-flora26a)
- <a id="guo26d-theory-statistics"></a>[Delving into Non-Exchangeability for Conformal Prediction in Graph-Structured Multivariate Time Series](../conferences/icml-2026/cards/1301-1400.md#paper-guo26d)
- <a id="harker26a-theory-statistics"></a>[On the Optimization Trajectory of DeepWalk Embeddings](../conferences/icml-2026/cards/1401-1500.md#paper-harker26a)
- <a id="jiang26aj-theory-statistics"></a>[Quantum Algorithms for Triangle Cut Sparsification](../conferences/icml-2026/cards/1901-2000.md#paper-jiang26aj)
- <a id="keriven26a-theory-statistics"></a>[Backward Oversmoothing: why is it hard to train deep Graph Neural Networks?](../conferences/icml-2026/cards/2001-2100.md#paper-keriven26a)
- <a id="koke26a-theory-statistics"></a>[Graph Neural Networks Are Not Continuous Across Graph Resolutions](../conferences/icml-2026/cards/2101-2200.md#paper-koke26a)
- <a id="kummer26a-theory-statistics"></a>[A Unifying Relational Perspective on Expressive Lottery Tickets](../conferences/icml-2026/cards/2201-2300.md#paper-kummer26a)
- <a id="lin26as-theory-statistics"></a>[Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration](../conferences/icml-2026/cards/2701-2800.md#paper-lin26as)
- <a id="liu26ed-theory-statistics"></a>[Estimating Correlation Clustering Cost in Node-Arrival Stream](../conferences/icml-2026/cards/2901-3000.md#paper-liu26ed)
- <a id="maruyama26a-theory-statistics"></a>[Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks](../conferences/icml-2026/cards/3201-3300.md#paper-maruyama26a)
- <a id="migali26a-theory-statistics"></a>[Learning to Rank from Incomplete Rankings](../conferences/icml-2026/cards/3201-3300.md#paper-migali26a)
- <a id="park26x-theory-statistics"></a>[Quantile-Free Uncertainty Quantification in Graph Neural Networks](../conferences/icml-2026/cards/3601-3700.md#paper-park26x)
- <a id="rancati26a-theory-statistics"></a>[Learning Discrete Diffusion on Graphs via Free-Energy Gradient Flows](../conferences/icml-2026/cards/3801-3900.md#paper-rancati26a)
- <a id="shu26a-theory-statistics"></a>[Size Transferability of Graph Convolutional Networks across Sparsity: A Generalized Graphon Perspective](../conferences/icml-2026/cards/4101-4200.md#paper-shu26a)
- <a id="taing26a-theory-statistics"></a>[On the Effect of Misspecifying the Embedding Dimension in Low-rank Network Models](../conferences/icml-2026/cards/4301-4400.md#paper-taing26a)
- <a id="turan26a-theory-statistics"></a>[Beyond ReLU: Bifurcation, Oversmoothing, and Topological Priors](../conferences/icml-2026/cards/4501-4600.md#paper-turan26a)
- <a id="wittig26a-theory-statistics"></a>[Which Algorithms Can Graph Neural Networks Learn?](../conferences/icml-2026/cards/4901-5000.md#paper-wittig26a)
<!-- classification:end -->
