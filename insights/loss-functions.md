# 损失函数

[首页](../README.md) · [参与贡献](../CONTRIBUTING.md) · [English](../en/insights/loss-functions.md)

训练目标、辅助监督与正则化。

<!-- classification:start -->
## 按研究领域浏览

[大语言模型](#by-llm) · [计算机视觉](#by-computer-vision) · [自然语言处理](#by-nlp) · [强化学习](#by-reinforcement-learning) · [机器人学](#by-robotics) · [多模态学习](#by-multimodal) · [机器学习基础与统计](#by-ml-foundations) · [图学习与推荐](#by-graph-and-recommendation) · [科学机器学习](#by-scientific-ml)

<a id="by-llm"></a>

### 大语言模型

- [偏好学习](../conferences/icml-2026/cards/0001-0100.md#abas26a-loss-functions) · TUR-DPO: Topology- and Uncertainty-Aware Direct Preference Optimization
- [异质偏好学习](../conferences/icml-2026/cards/0101-0200.md#aouad26a-loss-functions) · The Sign Estimator: Preference Modeling for LLM Alignment under Heterogeneity
- [潜在思维链的重建监督](../conferences/icml-2026/cards/0501-0600.md#chen26bi-loss-functions) · What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis
- [MoE 软路由负载均衡](../conferences/icml-2026/cards/0501-0600.md#chen26br-loss-functions) · $φ$-Balancing for Mixture-of-Experts Training
- [离散扩散的奖励倾斜匹配](../conferences/icml-2026/cards/0601-0700.md#chen26el-loss-functions) · Discrete Tilt Matching
- [自博弈偏好语义校准](../conferences/icml-2026/cards/0601-0700.md#chen26hc-loss-functions) · $\textitS$-SPPO: Semantic-Calibrated Self-Play Preference Optimization
- [语言模型蒸馏的尾部 KL](../conferences/icml-2026/cards/0801-0900.md#dasgupta26a-loss-functions) · Don’t Ignore the Tail: Decoupled Distillation Produces Top Maths Students on an Academic Budget
- [按目标词元概率调节微调梯度](../conferences/icml-2026/cards/1001-1100.md#fan26j-loss-functions) · Navigating the Pareto Frontier of Alignment: Spectrum-Adaptive Fine-Tuning for LLMs
- [推理链去偏的后缀优化](../conferences/icml-2026/cards/1101-1200.md#feng26z-loss-functions) · Self-correcting for Debiasing Large Language Models
- [注意力汇的门控与负载均衡](../conferences/icml-2026/cards/1101-1200.md#fu26v-loss-functions) · Attention Sink Forges Native MoE in Attention Layers: Sink-Aware Training to Address Head Collapse
- [拆分语言模型的双端泄漏防护](../conferences/icml-2026/cards/1301-1400.md#gu26o-loss-functions) · From Prompts to Responses: Dual-Sided Data Leakage and Defense in Split Large Language Models
- [分别约束同层分工与跨层专家路径](../conferences/icml-2026/cards/1601-1700.md#hu26d-loss-functions) · Synergistic Intra- and Cross-Layer Regularization Losses for MoE Expert Specialization
- [以局部方向一致性约束隐状态轨迹](../conferences/icml-2026/cards/1701-1800.md#huang26s-loss-functions) · Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA
- [偏好对的总概率约束](../conferences/icml-2026/cards/1801-1900.md#im26a-loss-functions) · Normalized Rewards for Preference Optimization

<a id="by-computer-vision"></a>

### 计算机视觉

- [视觉生成偏好对齐](../conferences/icml-2026/cards/0101-0200.md#bai26c-loss-functions) · Threshold-Guided Optimization for Visual Generative Models
- [密集小目标计数](../conferences/icml-2026/cards/0301-0400.md#bo26a-loss-functions) · Benchmarking Dense and Indiscernible Object Counting with Blueberries
- [单步超分辨率的全路径对齐](../conferences/icml-2026/cards/0801-0900.md#deng26e-loss-functions) · Joint Geometric and Trajectory Consistency Learning for One-Step Real-World Super-Resolution
- [全参考画质的锚定对抗训练](../conferences/icml-2026/cards/1401-1500.md#gushchin26a-loss-functions) · BiRQA: Bidirectional Robust Quality Assessment for Images
- [类别遗忘的邻域保护与表征分散](../conferences/icml-2026/cards/1401-1500.md#ha26b-loss-functions) · Unlearning’s Blind Spots: Over-Unlearning and Prototypical Relearning Attack
- [在商空间中去掉物体重组的整体刚体自由度](../conferences/icml-2026/cards/1501-1600.md#heck26a-loss-functions) · SE(n)-Invariant Flow Matching: A General Framework with Application to Object Reassembly
- [用方向导数保持蒸馏的输入可控性](../conferences/icml-2026/cards/1701-1800.md#huang26bj-loss-functions) · Restoring Initial Noise Sensitivity in Text-to-Image Distillation via Geometric Alignment
- [以逆向重建约束长视频滚动](../conferences/icml-2026/cards/1701-1800.md#huang26bt-loss-functions) · LIVE: Long-horizon Interactive Video World Modeling
- [训练对重缩放敏感的模型更新](../conferences/icml-2026/cards/1801-1900.md#jang26e-loss-functions) · Making Models Unmergeable via Scaling-Sensitive Loss Landscape

<a id="by-nlp"></a>

### 自然语言处理

- [检索器生成正则](../conferences/icml-2026/cards/0301-0400.md#cai26d-loss-functions) · ElicitR: Unlocking Latent Reasoning in Dense Retrievers via Generative Regularization
- [按真假标签约束语音内容与高频残差的一致程度](../conferences/icml-2026/cards/1501-1600.md#hidekel26a-loss-functions) · SONAR: Spectral-Contrastive Audio Residuals for Generalizable Deepfake Detection

<a id="by-reinforcement-learning"></a>

### 强化学习

- [离线强化学习流策略正则](../conferences/icml-2026/cards/0601-0700.md#chen26ep-loss-functions) · Continuity-Regularized Flow Matching for Offline Reinforcement Learning
- [用频域平滑正则降低随机流训练方差](../conferences/icml-2026/cards/1401-1500.md#hassen26a-loss-functions) · Spectral Flow Matching: Stabilizing Stochastic GFlowNets via Frequency-Domain Regularization

<a id="by-robotics"></a>

### 机器人学

- [面向决策的数字孪生](../conferences/icml-2026/cards/0001-0100.md#amad26a-loss-functions) · DT²: Decision-Targeted Digital Twins
- [单步操作策略的速度方向监督](../conferences/icml-2026/cards/1001-1100.md#fang26h-loss-functions) · OMP: One-step Meanflow Policy with Directional Alignment
- <a id="align-action-features-with-latent-actions"></a><a id="latent-action-alignment"></a>[用潜动作监督动作专家的中间层](../conferences/icml-2026/cards/2801-2900.md#liu26bl-loss-functions) · LARA: Latent Action Representation Alignment for Vision-Language-Action Models
- <a id="target-region-reconstruction-as-auxiliary-supervision"></a><a id="auxiliary-visual-supervision"></a>[用目标区域重建做辅助监督](../papers/reconvla.md#reconvla-loss-functions) · ReconVLA

<a id="by-multimodal"></a>

### 多模态学习

- [自监督流匹配](../conferences/icml-2026/cards/0401-0500.md#chefer26a-loss-functions) · Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis
- [多模态提示泛化](../conferences/icml-2026/cards/0501-0600.md#chen26au-loss-functions) · Do-Prompt: Causal Interventions Meet Variational Prompt Bottlenecks
- [视觉指令微调的语言偏差正则](../conferences/icml-2026/cards/0501-0600.md#chen26bn-loss-functions) · Language Bias in LVLMs: From In-Depth Analysis to Simple and Effective Mitigation
- [多轮音频编辑的独立加噪](../conferences/icml-2026/cards/0501-0600.md#chen26dq-loss-functions) · AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing
- [可变长多模态样本的公平自监督](../conferences/icml-2026/cards/0601-0700.md#cheong26a-loss-functions) · FairSSL: Fair Multimodal Self-Supervised Learning
- [长视频配音的掩码与快捷去噪监督](../conferences/icml-2026/cards/0801-0900.md#dellali26a-loss-functions) · SALSA-V: Shortcut-Augmented Long-form Synchronized Audio from Videos
- [共享视觉上下文的对比偏好优化](../conferences/icml-2026/cards/0801-0900.md#deng26z-loss-functions) · Learning from Fine-Grained Visual Discrepancies: Mitigating Multimodal Hallucinations via In-Context Visual Contrastive Optimization
- [图像实例约束的雷达场景流](../conferences/icml-2026/cards/1101-1200.md#fu26r-loss-functions) · Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation
- [统一视觉 token 的分量焦点损失](../conferences/icml-2026/cards/1301-1400.md#gong26b-loss-functions) · Twins: Learn to Predict Unified Representations with Focal Loss
- [整流流中的对比速度擦除](../conferences/icml-2026/cards/1301-1400.md#grebe26a-loss-functions) · GEM: Geometric Erasure by Contrastive Velocity Matching in Rectified Flows
- [CAD 参数词元的三维点监督](../conferences/icml-2026/cards/1301-1400.md#guan26g-loss-functions) · Bridging Tokens and Geometry: Token-wise 3D Supervision for CAD Generation
- [让新增可信表格字段在训练中带来收益](../conferences/icml-2026/cards/1401-1500.md#hasny26a-loss-functions) · No Data? No Problem: Robust Vision-Tabular Learning with Missing Values
- [以径向蕴涵与球面角距分工表示分类树](../conferences/icml-2026/cards/1501-1600.md#he26ai-loss-functions) · Learning Taxonomic Trees with Hierarchical Representation Regularization for Large Multimodal Models
- [跨模型对齐多视图特征分布](../conferences/icml-2026/cards/1601-1700.md#hu26aw-loss-functions) · DART: Distribution-Aware Adaptive Relational Transfer for Adversarial Attacks against Closed-Source MLLMs

<a id="by-ml-foundations"></a>

### 机器学习基础与统计

- [分布偏移鲁棒性](../conferences/icml-2026/cards/0001-0100.md#agirman26a-loss-functions) · Iterative Robust Satisficing: Minimizing Performance Degradation Under Distribution Shift
- [聚合标签学习](../conferences/icml-2026/cards/0101-0200.md#applebaum26a-loss-functions) · Optimal Learning from Label Proportions with General Loss Functions
- [近似等变正则](../conferences/icml-2026/cards/0201-0300.md#berndt26a-loss-functions) · Approximate Equivariance via Projection-Based Regularisation
- [不平衡域泛化](../conferences/icml-2026/cards/0301-0400.md#cao26k-loss-functions) · Negatives-Dominant Contrastive Learning for Generalization in Imbalanced Domains
- [单步条件采样](../conferences/icml-2026/cards/0401-0500.md#chatterjee26a-loss-functions) · One-shot Conditional Sampling: MMD meets Nearest Neighbors
- [密度加权的分位数回归](../conferences/icml-2026/cards/0501-0600.md#chen26bm-loss-functions) · Colorful Pinball: Density-Weighted Quantile Regression for Conditional Guarantee of Conformal Prediction
- [专家失衡下的代价敏感路由](../conferences/icml-2026/cards/0701-0800.md#cortes26b-loss-functions) · Optimized Deferral for Imbalanced Settings
- [极少正标签下的 PU 风险正则](../conferences/icml-2026/cards/0801-0900.md#dai26f-loss-functions) · Positive-Unlabeled Learning with Extreme Scarcity of Labeled Positives
- [协变量偏移下的期望一致性校准](../conferences/icml-2026/cards/0901-1000.md#dong26e-loss-functions) · Expectation Consistency Loss: Rethink Confidence Calibration under Covariate Shift
- [InfoNCE 的端点尾部修正](../conferences/icml-2026/cards/1001-1100.md#erol26a-loss-functions) · When Softmax Fails at the Top: Extreme-Value Corrections for InfoNCE
- [时序预测的信息几何损失](../conferences/icml-2026/cards/1001-1100.md#fang26m-loss-functions) · Information Geometry Loss for Time Series Forecasting
- [未归一化目标的批次广义偏差损失](../conferences/icml-2026/cards/1001-1100.md#fawkes26a-loss-functions) · $f$-Trajectory Balance: A Loss Family for Tuning GFlowNets, Generative Models, and LLMs with Off- and On-Policy Data
- [多视图聚类的截断张量低秩惩罚](../conferences/icml-2026/cards/1101-1200.md#fu26g-loss-functions) · Nonconvex Low-Rank Tensor Representation with Deep Priors for Multiview Subspace Clustering
- [用拓扑一致性约束特征激活](../conferences/icml-2026/cards/1201-1300.md#gaukstad26a-loss-functions) · Learning Coherent Representations: A Topological Approach to Interpretability
- [用能量构造去噪漂移监督并复用探索轨迹](../conferences/icml-2026/cards/1401-1500.md#havens26a-loss-functions) · Flow Sampling : Learning to Sample from Unnormalized Densities via Denoising Conditional Processes
- [用任务对称性约束加速迟发泛化](../conferences/icml-2026/cards/1701-1800.md#hwang26d-loss-functions) · Intrinsic Task Symmetry Drives Generalization in Algorithmic Tasks

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [推荐排序的伪负例偏好优化](../conferences/icml-2026/cards/0601-0700.md#chen26ez-loss-functions) · Mitigating Reward Hacking in LLM-based Recommendation: A Preference Optimization Approach
- [联邦图学习的 Fisher 参数对齐](../conferences/icml-2026/cards/0601-0700.md#chen26gu-loss-functions) · GraphP-FL: Personalized Federated Graph Learning via Dynamic Structure Awareness and Fisher Information Elastic Alignment
- [时序图解释的稳定与转变证据](../conferences/icml-2026/cards/0601-0700.md#chen26gx-loss-functions) · ST-TGExplainer: Disentangling Stability and Transition Patterns for Temporal GNN Interpretability
- [图混合专家的分组对比路由](../conferences/icml-2026/cards/0801-0900.md#deng26u-loss-functions) · Discriminative Mixture-of-Experts on Graphs with Reliable Expert Fusion
- [属性图聚类的双视图去冗余](../conferences/icml-2026/cards/0901-1000.md#ding26v-loss-functions) · Discriminative Attribute Graph Clustering Through Topology-Guided Contrastive Learning
- [基于子图解释的模型水印](../conferences/icml-2026/cards/0901-1000.md#downer26a-loss-functions) · Watermarking Graph Neural Networks via Explanations for Ownership Protection

<a id="by-scientific-ml"></a>

### 科学机器学习

- [鲁棒损失](../conferences/icml-2026/cards/0001-0100.md#abijuru26b-loss-functions) · Heavy-tailed Physics-Informed Neural Networks
- [网格算子学习](../conferences/icml-2026/cards/0101-0200.md#anwer26a-loss-functions) · Certificates for Complex-Compatible Learned Cochain Laplacians
- [空间转录组预测](../conferences/icml-2026/cards/0301-0400.md#byeon26a-loss-functions) · HEXST: Hexagonal Shifted-Window Transformer for Spatial Transcriptomics Gene Expression Prediction
- [生物声学辅助监督](../conferences/icml-2026/cards/0401-0500.md#chasmai26a-loss-functions) · MetaPerch: Learning from metadata for bioacoustics foundation models
- [心电与报告对齐](../conferences/icml-2026/cards/0401-0500.md#chen26y-loss-functions) · SGERA: Stein-Guided ECG-Report Alignment for ECG Representation Learning
- [共病多标签表征](../conferences/icml-2026/cards/0501-0600.md#chen26at-loss-functions) · FACT: Fuzzy Alignment with Comorbidity Topology for Reliable Multi-Label Medical Image Diagnosis
- [生理时序的跨窗重建监督](../conferences/icml-2026/cards/0601-0700.md#chen26fk-loss-functions) · Self-Supervised Dynamical System Representations for Physiological Time-Series
- [医学分割的形态自适应损失](../conferences/icml-2026/cards/0701-0800.md#chowdhury26b-loss-functions) · S2M-Net: Spectral-Spatial Mixing with Morphology-Aware Adaptive Loss for Medical Image Segmentation
- [固定边界等离子体平衡监督](../conferences/icml-2026/cards/0901-1000.md#ding26w-loss-functions) · Physics-informed Neural Operator Learning for Nonlinear Grad-Shafranov Equation
- [交换关联泛函的导数监督](../conferences/icml-2026/cards/1001-1100.md#eberhard26a-loss-functions) · Derivative Informed Learning of Exchange-Correlation Functionals
- [保留配体受体关系的细胞传输](../conferences/icml-2026/cards/1001-1100.md#estevez26b-loss-functions) · CellBRIDGE: Learning Cellular Trajectories via Interaction-Aware Alignment
- [自一致控制训练扩散桥](../conferences/icml-2026/cards/1601-1700.md#howard26b-loss-functions) · Control Consistency Losses for Diffusion Bridges
- [用对抗正交隔开坐标变化与动力学修正](../conferences/icml-2026/cards/1701-1800.md#huh26a-loss-functions) · Identifiable Smooth Conjugacy Learning via Adversarial Orthogonality
- [将路径结构和尾部风险直接接进配置策略](../conferences/icml-2026/cards/1701-1800.md#hwang26j-loss-functions) · Signature-Informed Transformer for Asset Allocation
<!-- classification:end -->
