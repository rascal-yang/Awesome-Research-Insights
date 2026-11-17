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
- [让教师词元熵决定何时补正向 KL](../conferences/icml-2026/cards/1901-2000.md#jin26e-loss-functions) · Entropy-Aware On-Policy Distillation of Language Models
- [按解码方向筛选跨样本冗余激活](../conferences/icml-2026/cards/1901-2000.md#jin26j-loss-functions) · C$^2$R: Cross-sample Consistency Regularization Mitigates Feature Splitting and Absorption in Sparse Autoencoders
- [剪枝语言模型的循环起点纠偏](../conferences/icml-2026/cards/2301-2400.md#lee26bb-loss-functions) · FOCUS & RePAIR: Mitigating Text Degeneration via Token-Level Guidance For Pruned Large Language Models
- [按基座已有能力调节微调损失的低概率权重](../conferences/icml-2026/cards/2501-2600.md#li26ew-loss-functions) · Beyond Log Likelihood: Probability-Based Objectives for Supervised Fine-Tuning across the Model Capability Continuum
- [用任务条件学习困惑度偏好标签的置信度](../conferences/icml-2026/cards/2601-2700.md#li26jp-loss-functions) · Task-Aware Preference Calibration for Direct Preference Optimization
- [惩罚微调中升高的有害注意力汇点差异](../conferences/icml-2026/cards/2801-2900.md#liu26cf-loss-functions) · Surgery: Mitigating Harmful Fine-Tuning for Large Language Models via Attention Sink
- [对同一正确推理内的冗余段做掩码偏好](../conferences/icml-2026/cards/2801-2900.md#liu26dp-loss-functions) · ThoughtFold: Folding Reasoning Chains via Introspective Preference Learning
- [中续训练用分散损失解除小模型嵌入锥化](../conferences/icml-2026/cards/2901-3000.md#liu26dy-loss-functions) · Dispersion Loss Counteracts Embedding Condensation and Improves Generalization in Small Language Models
- [在反嵌入前锚定有害查询表征](../conferences/icml-2026/cards/3001-3100.md#lu26ac-loss-functions) · Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks
- [偏好优化的对比互信息](../conferences/icml-2026/cards/3101-3200.md#lv26a-loss-functions) · The Hidden Link between RLHF and Contrastive Learning
- [把比较器的平局纳入偏好学习](../conferences/icml-2026/cards/3101-3200.md#lv26l-loss-functions) · When Labelers Stay Silent: The Power of Ties in Cost-Effective Preference Learning
- [语义自适应偏好间隔](../conferences/icml-2026/cards/3301-3400.md#mohri26e-loss-functions) · Mind the Gap: Structure-Aware Consistency in Preference Learning
- [为每个前缀匹配偏好密度比](../conferences/icml-2026/cards/3401-3500.md#nguyen26l-loss-functions) · TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching
- [自回归前缀偏好](../conferences/icml-2026/cards/3401-3500.md#oi26b-loss-functions) · Autoregressive Direct Preference Optimization
- [偏好部分最优传输](../conferences/icml-2026/cards/3501-3600.md#pan26o-loss-functions) · Optimal Transport for LLM Reward Modeling from Noisy Feedback

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
- [让一致性训练更新指向数据流形](../conferences/icml-2026/cards/2001-2100.md#kim26e-loss-functions) · Align Your Trajectory Tangent: Training Better Consistency Models via Manifold-Aligned Tangents
- [把类原型的几何留在分类输出层](../conferences/icml-2026/cards/2201-2300.md#koromilas26b-loss-functions) · Neural Collapse by Design: Learning Class Prototypes on the Hypersphere
- [匹配带零点质量的最大熵表征目标](../conferences/icml-2026/cards/2201-2300.md#kuang26b-loss-functions) · Rectified LpJEPA: Joint-Embedding Predictive Architectures with Sparse and Maximum-Entropy Representations
- [用正负条件分数校正扩散软提示](../conferences/icml-2026/cards/2301-2400.md#lee26k-loss-functions) · Alignment-Guided Score Matching for Text-to-Image Alignment in Diffusion Models
- [用幅度等变把去噪监督迁移至低噪区](../conferences/icml-2026/cards/2301-2400.md#levac26a-loss-functions) · Normalization-equivariant Diffusion Models: Learning Posterior Samplers From Noisy And Partial Measurements
- [让高斯基元的颜色歧义反过来指导表面修复](../conferences/icml-2026/cards/2601-2700.md#li26iz-loss-functions) · Revisiting Photometric Ambiguity for Accurate Gaussian-Splatting Surface Reconstruction
- [用运输代价固定对抗生成的映射](../conferences/icml-2026/cards/2701-2800.md#lin26ao-loss-functions) · Adversarial Flow Models
- [分别约束类条件子空间方向和谱容量](../conferences/icml-2026/cards/2801-2900.md#liu26cc-loss-functions) · Geometric Rate–Distortion Invariance for Domain Generalization
- [带噪潜空间偏好建模](../conferences/icml-2026/cards/2901-3000.md#liu26fh-loss-functions) · Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling
- [单步像素平均流参数化](../conferences/icml-2026/cards/3001-3100.md#lu26t-loss-functions) · One-step Latent-free Image Generation with Pixel Mean Flows
- [给地理半正样本分配软负标签](../conferences/icml-2026/cards/3501-3600.md#ouyang26g-loss-functions) · Must All Negatives Be Pushed Away Equally? Uncertainty-Aware Cross-View Geo-Localization via Normal Inverse Gamma Distribution

<a id="by-nlp"></a>

### 自然语言处理

- [检索器生成正则](../conferences/icml-2026/cards/0301-0400.md#cai26d-loss-functions) · ElicitR: Unlocking Latent Reasoning in Dense Retrievers via Generative Regularization
- [按真假标签约束语音内容与高频残差的一致程度](../conferences/icml-2026/cards/1501-1600.md#hidekel26a-loss-functions) · SONAR: Spectral-Contrastive Audio Residuals for Generalizable Deepfake Detection

<a id="by-reinforcement-learning"></a>

### 强化学习

- [离线强化学习流策略正则](../conferences/icml-2026/cards/0601-0700.md#chen26ep-loss-functions) · Continuity-Regularized Flow Matching for Offline Reinforcement Learning
- [用频域平滑正则降低随机流训练方差](../conferences/icml-2026/cards/1401-1500.md#hassen26a-loss-functions) · Spectral Flow Matching: Stabilizing Stochastic GFlowNets via Frequency-Domain Regularization
- [对齐潜状态与任务价值而保留预测损失](../conferences/icml-2026/cards/1901-2000.md#jiang26ai-loss-functions) · Boosting World Models Learning via Latent-Space Value Alignment
- [按轨迹回报软排序学习序数评级](../conferences/icml-2026/cards/2001-2100.md#kharyal26a-loss-functions) · Reward Learning through Ranking Mean Squared Error
- [约束 critic 的动作梯度来平滑策略](../conferences/icml-2026/cards/2301-2400.md#lee26aj-loss-functions) · Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods
- [在视觉强化学习中从部分帧预测回合回报](../conferences/icml-2026/cards/3001-3100.md#lu26al-loss-functions) · Return-Critic: Bridging Goal Discrepancy for Efficient Visual Reinforcement Learning
- [用对数重要性比的高斯权重复用旧轨迹](../conferences/icml-2026/cards/3001-3100.md#lu26at-loss-functions) · GIPO: Gaussian Importance Sampling Policy Optimization
- [混合专家谱可塑性](../conferences/icml-2026/cards/3001-3100.md#luo26ah-loss-functions) · SPHERE: Mitigating the Loss of Spectral Plasticity in Mixture-of-Experts for Deep Reinforcement Learning

<a id="by-robotics"></a>

### 机器人学

- [面向决策的数字孪生](../conferences/icml-2026/cards/0001-0100.md#amad26a-loss-functions) · DT²: Decision-Targeted Digital Twins
- [单步操作策略的速度方向监督](../conferences/icml-2026/cards/1001-1100.md#fang26h-loss-functions) · OMP: One-step Meanflow Policy with Directional Alignment
- [用本体状态距离给视觉摘要提供软监督](../conferences/icml-2026/cards/2101-2200.md#kim26ao-loss-functions) · Contrastive Representation Regularization for Vision-Language-Action Models
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
- [用循环一致性约束未配对扩散桥](../conferences/icml-2026/cards/2201-2300.md#kosman26a-loss-functions) · Structured Diffusion Bridges: Inductive Bias for Denoising Diffusion Bridges
- [用双重归一化限制错标梯度](../conferences/icml-2026/cards/2501-2600.md#li26er-loss-functions) · Intrinsic Gradient Suppression for Label-Noise Prompt Tuning in Vision–Language Models
- [用相关负类监督视觉词元做密集预测](../conferences/icml-2026/cards/2501-2600.md#li26fg-loss-functions) · DenseMLLM: Standard Multimodal LLMs for Dense Prediction
- [未量化潜变量对语音解码器的自指导](../conferences/icml-2026/cards/2601-2700.md#li26jy-loss-functions) · Self-Guidance: Enhancing Neural Codecs via Decoder Manifold Alignment
- [对可能翻转偏好的市场条件单独监督敏感性](../conferences/icml-2026/cards/2701-2800.md#liu26e-loss-functions) · GeoReward: Mitigating Contextual Variable Overestimation in Vision-Language Models for Cross-Market Preference Prediction
- [用梯度式通道正则压缩连续音频](../conferences/icml-2026/cards/2901-3000.md#liu26ei-loss-functions) · STAR-VAE: Structured Topology-Aware Regularization for Audio Reconstruction and Generation
- [在对抗训练中对齐类别分布和证据总量](../conferences/icml-2026/cards/3001-3100.md#lu26af-loss-functions) · Calibrating Uncertainty for Zero-Shot Adversarial CLIP
- [以类别锚点约束视觉提示范数](../conferences/icml-2026/cards/3101-3200.md#ma26ai-loss-functions) · AlignedNorm: Prompting Vision–Language Models via Coupled Prompt Field
- [专家路由的 Dirichlet 先验](../conferences/icml-2026/cards/3301-3400.md#mirvakhabova26a-loss-functions) · Dirichlet-Prior Shaping: Guiding Expert Specialization in Upcycled MoEs
- [扩散概念擦除散度](../conferences/icml-2026/cards/3401-3500.md#novello26a-loss-functions) · A Unified Framework for Diffusion Model Unlearning with f-Divergence
- [时序耦合流匹配](../conferences/icml-2026/cards/3501-3600.md#pan26m-loss-functions) · Temporal-aware Flow Matching for Video Generation with Temporally Coherent Motion

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
- [在目标条件下惩罚预测与偏差的依赖](../conferences/icml-2026/cards/2001-2100.md#kavak26a-loss-functions) · DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation
- [无标签局部预测一致性](../conferences/icml-2026/cards/2101-2200.md#kim26ab-loss-functions) · Inconsistency-Aware Minimization: Improving Generalization with Unlabeled Data
- [把带噪等级变成可比较的概率序](../conferences/icml-2026/cards/2301-2400.md#lee26aq-loss-functions) · Stochastic Order Learning: An Approach to Rank Estimation Using Noisy Data
- [连续秩差的对比学习](../conferences/icml-2026/cards/2301-2400.md#lee26bd-loss-functions) · Contrastive Order Learning: A General Framework for Ordinal Regression
- [用半群导出的线性代理监督流映射](../conferences/icml-2026/cards/2501-2600.md#li26fn-loss-functions) · Trajectory Consistency for One-Step Generation on Euler Mean Flows
- [用逐样本正确性约束候选专家的训练竞争](../conferences/icml-2026/cards/2701-2800.md#liu26g-loss-functions) · When More Experts Hurt: Underfitting in Multi-Expert Learning to Defer
- [以成对监督保存语义相反标签的分歧度](../conferences/icml-2026/cards/3001-3100.md#lu26an-loss-functions) · Divisiveness-Consistent Label Distribution Learning
- [线性内核一致损失](../conferences/icml-2026/cards/3301-3400.md#mohri26d-loss-functions) · Linear-Core Surrogates: Smooth Loss Functions with Linear Rates for Classification and Structured Prediction
- [用可能性上确界估计认知不确定性](../conferences/icml-2026/cards/3401-3500.md#ni26b-loss-functions) · Possibilistic Predictive Uncertainty for Deep Learning
- [用噪声层级分类识别能量分布的模态权重](../conferences/icml-2026/cards/3501-3600.md#ouyang26b-loss-functions) · A Diffusive Classification Loss for Learning Energy-based Generative Models

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [推荐排序的伪负例偏好优化](../conferences/icml-2026/cards/0601-0700.md#chen26ez-loss-functions) · Mitigating Reward Hacking in LLM-based Recommendation: A Preference Optimization Approach
- [联邦图学习的 Fisher 参数对齐](../conferences/icml-2026/cards/0601-0700.md#chen26gu-loss-functions) · GraphP-FL: Personalized Federated Graph Learning via Dynamic Structure Awareness and Fisher Information Elastic Alignment
- [时序图解释的稳定与转变证据](../conferences/icml-2026/cards/0601-0700.md#chen26gx-loss-functions) · ST-TGExplainer: Disentangling Stability and Transition Patterns for Temporal GNN Interpretability
- [图混合专家的分组对比路由](../conferences/icml-2026/cards/0801-0900.md#deng26u-loss-functions) · Discriminative Mixture-of-Experts on Graphs with Reliable Expert Fusion
- [属性图聚类的双视图去冗余](../conferences/icml-2026/cards/0901-1000.md#ding26v-loss-functions) · Discriminative Attribute Graph Clustering Through Topology-Guided Contrastive Learning
- [基于子图解释的模型水印](../conferences/icml-2026/cards/0901-1000.md#downer26a-loss-functions) · Watermarking Graph Neural Networks via Explanations for Ownership Protection
- [按邻居类型重写图推荐的负样本分数](../conferences/icml-2026/cards/2301-2400.md#lee26w-loss-functions) · Rethinking Contrastive Learning for Graph Collaborative Filtering: Limitations and a Simple Remedy

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
- [把物理残差监督送到扩散中间层](../conferences/icml-2026/cards/1801-1900.md#jia26j-loss-functions) · Learning to Think in Physics: Breaking Shortcut Learning in Scientific Diffusion via Representation Alignment
- [用有序峰集合替代昂贵的原子指派](../conferences/icml-2026/cards/1901-2000.md#jin26k-loss-functions) · From Human Labels to Literature: Semi-Supervised Learning of NMR Chemical Shifts at Scale
- [随机抽 Hessian 列监督势能曲率](../conferences/icml-2026/cards/2101-2200.md#koker26a-loss-functions) · PFT: Phonon Fine-tuning for Machine Learned Interatomic Potentials
- [只对预测均值施加 PDE 残差并重抽配点](../conferences/icml-2026/cards/2501-2600.md#li26dg-loss-functions) · Bias-Spectrum Neural Processes for Parametric PDEs: Architecture Priors Meet PDE Constraints
- [迭代神经算子逐步加权高频残差](../conferences/icml-2026/cards/2801-2900.md#liu26dm-loss-functions) · Iterative Refinement Neural Operators are Learned Fixed-Point Solvers: A Principled Approach to Spectral Bias Mitigation
- [PINN 边界与残差对齐](../conferences/icml-2026/cards/3001-3100.md#luo26am-loss-functions) · Mitigating Gradient Pathology in PINNs through Aligned Constraint
- [单细胞扰动稀疏信号加权](../conferences/icml-2026/cards/3201-3300.md#mejia26a-loss-functions) · Needles in the Haystack: Addressing Signal Dilution Improves scRNA-seq Perturbation Response Modeling and Evaluation
- [混沌系统模拟](../conferences/icml-2026/cards/3201-3300.md#melo26a-loss-functions) · Learning to Emulate Chaos: Adversarial Optimal Transport Regularization
- [让细胞扰动原型只受正样本吸引](../conferences/icml-2026/cards/3401-3500.md#nightingale26a-loss-functions) · Asymmetric Contrastive Objectives for Efficient Phenotypic Screening
<!-- classification:end -->
