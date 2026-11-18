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
- [遗忘后上下文保留](../conferences/icml-2026/cards/3601-3700.md#peng26a-loss-functions) · Forget to Know, Remember to Use: Context-Aware Unlearning for Large Language Models
- [对齐不同掩码长度下的答案分布](../conferences/icml-2026/cards/3601-3700.md#piskorz26a-loss-functions) · Masks Can Be Distracting: On Context Comprehension in Diffusion Language Models
- [让投机解码的草稿损失直接优化接受长度](../conferences/icml-2026/cards/3901-4000.md#samarin26a-loss-functions) · LK Losses: Direct Acceptance Rate Optimization for Speculative Decoding
- [用序列成对对数比消掉温度配分函数](../conferences/icml-2026/cards/3901-4000.md#scheufele26a-loss-functions) · Temperature Scaling in Discrete Sequence (Language) Models
- [用跨语言安全间隔调节逐样本偏好训练](../conferences/icml-2026/cards/4101-4200.md#shi26e-loss-functions) · Multilingual Safety Alignment via Representation-Space Separability
- [在惩罚两类失败的同时排序失败严重程度](../conferences/icml-2026/cards/4101-4200.md#simko26a-loss-functions) · Training with Honeypots: Reshaping How LLMs Fail Under Adversarial Attacks
- [属性熵减少的澄清提问奖励](../conferences/icml-2026/cards/4201-4300.md#sun26i-loss-functions) · Closing the Expression Gap in LLM Instructions via Socratic Questioning
- [按成败分组的熵重分配](../conferences/icml-2026/cards/4301-4400.md#tan26e-loss-functions) · GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy
- [reference-regularized-self-play](../conferences/icml-2026/cards/4301-4400.md#tang26ab-loss-functions) · RSPO: Regularized Self-Play Alignment of Large Language Models
- [base-anchored-latent-blocking](../conferences/icml-2026/cards/4501-4600.md#ustaomeroglu26a-loss-functions) · BLOCK-EM: Preventing Emergent Misalignment via Latent Blocking
- [带截断的f散度自博弈](../conferences/icml-2026/cards/4501-4600.md#vuong26b-loss-functions) · $f$-Divergence Self-Play for Tabular Anomaly Detection via Large Language Models
- [含噪偏好的有界梯度目标](../conferences/icml-2026/cards/4701-4800.md#wang26fa-loss-functions) · Unbiased Alignment for Large Language Models with Noisy Preferences
- [根锚定前缀信用分配](../conferences/icml-2026/cards/4701-4800.md#wang26fi-loss-functions) · Rooted Absorbed Prefix Trajectory Balance with Submodular Replay for GFlowNet Training
- [蒸馏的高阶交互稀疏惩罚](../conferences/icml-2026/cards/4701-4800.md#wang26gj-loss-functions) · A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions
- [替换与吸收独立调度的离散纠错](../conferences/icml-2026/cards/4801-4900.md#wang26ho-loss-functions) · Generalized Discrete Diffusion with Self-Correction
- [可靠锚点非对称正则](../conferences/icml-2026/cards/4801-4900.md#wang26ju-loss-functions) · Towards Context-Invariant Safety Alignment for Large Language Models
- [循环中间分布的优势加权监督](../conferences/icml-2026/cards/4901-5000.md#williams26b-loss-functions) · Prioritize the Process, Not Just the Outcome: Rewarding Latent Thought Trajectories Improves Reasoning in Looped Language Models
- [PRM学习的轨迹重要性与长度控制](../conferences/icml-2026/cards/5001-5100.md#wu26cl-loss-functions) · rePIRL: Learn PRM with Inverse RL for LLM Reasoning
- [按表征差距归一的偏好损失](../conferences/icml-2026/cards/5101-5200.md#xie26a-loss-functions) · When Distance Distracts: Representation Distance Bias in BT-Loss for Reward Models
- [以Jacobian正则区分稳定与有效吸引子](../conferences/icml-2026/cards/5301-5400.md#yang26t-loss-functions) · Stabilizing Recurrent Dynamics for Test-Time Scalable Latent Reasoning in Looped Language Models

<a id="by-computer-vision"></a>

### 计算机视觉

- [视觉生成偏好对齐](../conferences/icml-2026/cards/0101-0200.md#bai26c-loss-functions) · Threshold-Guided Optimization for Visual Generative Models
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
- [同时拟合目标域和限制实例改动](../conferences/icml-2026/cards/3801-3900.md#rakitin26a-loss-functions) · One-step Optimal Transport via Regularized Distribution Matching Distillation
- [用 Rényi 散度调整扩散训练的覆盖和保真](../conferences/icml-2026/cards/4001-4100.md#shen26g-loss-functions) · Rényi Diffusion Models
- [沿视频轨迹对齐参考相似度的排序](../conferences/icml-2026/cards/4101-4200.md#simion26a-loss-functions) · 3DPoV: Improving 3D understanding via Patch Ordering on Videos
- [真值与扩张框语义对比奖励](../conferences/icml-2026/cards/4201-4300.md#su26b-loss-functions) · PMSPO: Progressive Matching and Semantic-Aware Policy Optimization for Camouflaged Object Detection
- [persistent-connectivity-regularization](../conferences/icml-2026/cards/4301-4400.md#sun26ai-loss-functions) · Topology-Aware Contrastive Learning: Regulating Representation Connectivity via Persistent Homology
- [clean-forward-noisy-backward-edit-cycle](../conferences/icml-2026/cards/4401-4500.md#tewel26a-loss-functions) · Unpaired Visual Editing with Self-Consistent Flow Matching
- [trajectory-consistent-koopman](../conferences/icml-2026/cards/4501-4600.md#turan26c-loss-functions) · Unfolding Generative Flows with Koopman Operators: Trajectory-Preserving Linearization
- [head-proxy-cam-distillation](../conferences/icml-2026/cards/4501-4600.md#wan26o-loss-functions) · Shortcut-Resistant CAM Distillation for Long-Tailed Recognition
- [弱监督指定待移除子空间](../conferences/icml-2026/cards/4601-4700.md#wang26ao-loss-functions) · Privacy-Aware Video Anomaly Detection through Orthogonal Subspace Projection
- [难度与不确定性联合长度预算](../conferences/icml-2026/cards/4601-4700.md#wang26ba-loss-functions) · Don’t Overthink with Pixels: Efficient Reasoning for Segmentation
- [正交重构的风格蒸馏](../conferences/icml-2026/cards/4601-4700.md#wang26bi-loss-functions) · StyleDistillation: A New Insight of Image Style Enables Personalized Aesthetic Manipulation
- [频谱加权偏好对齐](../conferences/icml-2026/cards/4601-4700.md#wang26ch-loss-functions) · Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
- [shared-query-field-supervision](../conferences/icml-2026/cards/4601-4700.md#wang26dh-loss-functions) · NoiseSDF2NoiseSDF: Learning Clean Neural Fields from Noisy Supervision
- [prototype-loss-rejection](../conferences/icml-2026/cards/4601-4700.md#wang26dl-loss-functions) · One Coin Has Two Sides: Single Positive Multi Label Learning from Salient Annotations
- [动态语义锚遗忘奖励](../conferences/icml-2026/cards/4701-4800.md#wang26ef-loss-functions) · Preference-Calibrated Optimization with Score-Level Distribution Alignment for Text-to-Image Diffusion Model Unlearning
- [少样本避让路由校正](../conferences/icml-2026/cards/4701-4800.md#wang26eo-loss-functions) · Fleet: Few Shots Lead Effective AI-generated Image Detection
- [光流监督的增量视频特征差](../conferences/icml-2026/cards/4701-4800.md#wang26eu-loss-functions) · EmWorld: Emotion World Model with Latent State Evolution for Scenario-Incremental Dynamic Facial Expression Recognition
- [扩散噪声核的双视图谱对齐](../conferences/icml-2026/cards/4801-4900.md#wang26hu-loss-functions) · Revisiting Spectral Representations in Generative Diffusion Models
- [随深度变尖的监督目标](../conferences/icml-2026/cards/4801-4900.md#wang26ib-loss-functions) · Deep Trajectory Supervision: Deep Supervision Strikes Back
- [表达与属性的双粒度检测对齐](../conferences/icml-2026/cards/4901-5000.md#wei26af-loss-functions) · Open-Text Aerial Detection: A Unified Framework For Aerial Visual Grounding And Detection
- [假分数残差的反向目标](../conferences/icml-2026/cards/5001-5100.md#wu26q-loss-functions) · SGMD: Score Gradient Matching Distillation for Few-Step Video Diffusion Distillation
- [分频局部Wasserstein失真](../conferences/icml-2026/cards/5001-5100.md#wu26ae-loss-functions) · Frequency-Aware Perceptual Optimization for Low-Complexity Implicit Image Compression
- [首步监督与后续分布蒸馏](../conferences/icml-2026/cards/5001-5100.md#wu26ag-loss-functions) · Diversity-Preserved Distribution Matching Distillation for Fast Visual Synthesis
- [负样本反射目标的偏好训练](../conferences/icml-2026/cards/5001-5100.md#wu26ay-loss-functions) · PortraitRL: Reinforcement Learning for Portrait Pose Transfer with Multi-Objective Reward
- [按回报分支施加区域约束](../conferences/icml-2026/cards/5001-5100.md#wu26bm-loss-functions) · CoCoEdit: Content-Consistent Image Editing via Region Regularized Reinforcement Learning
- [对语义配对真假样本限制过分分离](../conferences/icml-2026/cards/5201-5300.md#xu26s-loss-functions) · BPL: Generalizable Deepfake Detection via Bias-only Pair-aware Learning
- [有符号优势加权的匹配后训练](../conferences/icml-2026/cards/5301-5400.md#xue26c-loss-functions) · Advantage Weighted Matching: Aligning RL with Pretraining in Diffusion Models
- [SIM2频谱运动残差正则](../conferences/icml-2026/cards/5301-5400.md#xue26d-loss-functions) · Physics-Guided Motion Loss for Video Generation Model

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
- [高UTD非中心冗余正则](../conferences/icml-2026/cards/4201-4300.md#song26j-loss-functions) · R2R2: Robust Representation for Intensive Experience Reuse via Redundancy Reduction in Self-Predictive Learning
- [chunk价值引导单步critic](../conferences/icml-2026/cards/4201-4300.md#song26t-loss-functions) · Chunk-Guided Q-Learning
- [finite-compute-maxrl](../conferences/icml-2026/cards/4301-4400.md#tajwar26a-loss-functions) · Maximum Likelihood Reinforcement Learning
- [cost-consistent-graph-transport](../conferences/icml-2026/cards/4401-4500.md#theodoropoulos26a-loss-functions) · Generalized Schrödinger Bridge on Graphs
- [删失轨迹的生存价值学习](../conferences/icml-2026/cards/4401-4500.md#tiofack26a-loss-functions) · SVL: Goal-Conditioned Reinforcement Learning as Survival Learning
- [distributional-error-weighting](../conferences/icml-2026/cards/4701-4800.md#wang26dp-loss-functions) · Reflect-then-Correct: Rebalancing Task Optimization for Generalizable Meta-Reinforcement Learning via Distributional Value Error Reduction
- [持续时间排序的多尺度潜空间](../conferences/icml-2026/cards/4801-4900.md#wang26if-loss-functions) · Learning Multi-Timescale Abstractions for Hierarchical Combinatorial Planning
- [结果与过程一致性的评价器奖励](../conferences/icml-2026/cards/4801-4900.md#wang26jf-loss-functions) · RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
- [裁剪密度比的即时奖励塑形](../conferences/icml-2026/cards/4801-4900.md#wang26ko-loss-functions) · Target-Driven Policy Optimization for Sequential Counterfactual Outcome Control
- [随机占优约束的分布式逆强化学习](../conferences/icml-2026/cards/5001-5100.md#wu26ch-loss-functions) · Distributional Inverse Reinforcement Learning
- [状态密度控制的技能复用优势](../conferences/icml-2026/cards/5101-5200.md#xiao26v-loss-functions) · Offline Multi-agent Continual Cooperation via Skill Partition and Reuse
- [把Bellman可行性施加到在线状态](../conferences/icml-2026/cards/5201-5300.md#xu26bk-loss-functions) · Non-Adversarial Imitation Learning Provably Free of Compounding Errors: The Value Flow Mechanism
- [保持源边界的Bellman路径耦合](../conferences/icml-2026/cards/5301-5400.md#xu26ct-loss-functions) · Path-Coupled Bellman Flows for Distributional Reinforcement Learning
- [组共享自动机的过程奖励](../conferences/icml-2026/cards/5301-5400.md#yan26k-loss-functions) · GLARE: Scalable Neuro-Symbolic Reward Shaping for LLM Agents via Group-Level Automata

<a id="by-robotics"></a>

### 机器人学

- [面向决策的数字孪生](../conferences/icml-2026/cards/0001-0100.md#amad26a-loss-functions) · DT²: Decision-Targeted Digital Twins
- [单步操作策略的速度方向监督](../conferences/icml-2026/cards/1001-1100.md#fang26h-loss-functions) · OMP: One-step Meanflow Policy with Directional Alignment
- [用本体状态距离给视觉摘要提供软监督](../conferences/icml-2026/cards/2101-2200.md#kim26ao-loss-functions) · Contrastive Representation Regularization for Vision-Language-Action Models
- <a id="align-action-features-with-latent-actions"></a><a id="latent-action-alignment"></a>[用潜动作监督动作专家的中间层](../conferences/icml-2026/cards/2801-2900.md#liu26bl-loss-functions) · LARA: Latent Action Representation Alignment for Vision-Language-Action Models
- [回报校验的残差正则门控](../conferences/icml-2026/cards/4301-4400.md#sun26al-loss-functions) · From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning
- [multiview-latent-actions](../conferences/icml-2026/cards/4501-4600.md#wan26f-loss-functions) · Multi-view Consistent Latent Action Learning for World Modeling and Control
- [Temporal Straightening for Latent Planning](../conferences/icml-2026/cards/4501-4600.md#wang26n-loss-functions) · Temporal Straightening for Latent Planning
- [morphology-routing-diversity](../conferences/icml-2026/cards/4601-4700.md#wang26dk-loss-functions) · ECo-MoE: Embodiment-Conditioned Mixture of Experts Increases the Evolvability of Robots
- [counterfactual-affordance-cones](../conferences/icml-2026/cards/4701-4800.md#wang26dy-loss-functions) · Learning Attribute–Affordance Hierarchies in Hyperbolic Space for Open-Vocabulary 3D Object Affordance Grounding
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
- [以类条件最优传输对齐互补模态证据](../conferences/icml-2026/cards/3601-3700.md#pellicer26a-loss-functions) · CAMP: Coherent Alignment of Multimodal Prototypes for Explainable Complementary Learning
- [保留模态间隙的关系对齐](../conferences/icml-2026/cards/4101-4200.md#shi26ag-loss-functions) · Structured Multi-modal Graph Disentanglement for Psychiatric Diagnosis
- [bidirectional-reconstruction-consistency](../conferences/icml-2026/cards/4201-4300.md#sun26u-loss-functions) · Scalable Medical Multimodal Fusion via Symmetric Consistency Modeling
- [admissibility-weighted-noisy-hashing](../conferences/icml-2026/cards/4301-4400.md#sun26ah-loss-functions) · Learning with Admissibility: Robust Fuzzy Hashing for Cross-Modal Retrieval with Noisy Labels
- [不确定性感知相似度](../conferences/icml-2026/cards/4301-4400.md#sun26aj-loss-functions) · Robust Self-reflective Hashing for Cross-modal Retrieval with Noisy Label
- [集合几何奖励与边际信用](../conferences/icml-2026/cards/4301-4400.md#tang26f-loss-functions) · Escaping the Likelihood Trap: Geometric Diversity Optimization for Long-Form Image Captioning
- [中间对象证据奖励](../conferences/icml-2026/cards/4301-4400.md#tang26u-loss-functions) · Artemis: Structured Visual Reasoning for Perception Policy Learning
- [各模态自身的信息瓶颈对齐](../conferences/icml-2026/cards/4601-4700.md#wang26at-loss-functions) · IBMA: Information Bottleneck-Based Multimodal Alignment
- [低熵视图单向指导高熵视图](../conferences/icml-2026/cards/4601-4700.md#wang26de-loss-functions) · Asymmetric Multi-View Clustering with Hyperbolic Uncertainty Modeling
- [wasserstein-group-variance](../conferences/icml-2026/cards/4601-4700.md#wang26di-loss-functions) · Test-Time Debiasing with Probabilistic Prompts via Wasserstein Distance in Vision-Language Models
- [因果学生的逐帧流速度蒸馏](../conferences/icml-2026/cards/4801-4900.md#wang26iv-loss-functions) · REST: Diffusion-based Real-time End-to-end Streaming Talking Head Generation via ID-Context Caching and Asynchronous Streaming Distillation
- [生成跨模态锚点约束遗忘边界](../conferences/icml-2026/cards/4801-4900.md#wang26ja-loss-functions) · Beyond Sample-Level Forgetting: Improving Reliability in Multimodal Unlearning
- [安全偏好样本的对比梯度修正](../conferences/icml-2026/cards/5001-5100.md#wu26w-loss-functions) · Towards Seed-Robust Safety Alignment in Text-to-Image Models
- [共享模型文本引导视觉推理](../conferences/icml-2026/cards/5001-5100.md#xi26c-loss-functions) · Awakening Visual Reasoning: Mitigating Post-Training Failure in Vision-Text Compression
- [最终正确性门控的检索奖励](../conferences/icml-2026/cards/5101-5200.md#xie26e-loss-functions) · Video-MTR: Reinforced Multi-Turn Reasoning for Long Video Understanding
- [在文本侧排斥近邻描述](../conferences/icml-2026/cards/5101-5200.md#xie26y-loss-functions) · FG-CLIP 2: A Bilingual Fine-grained Vision-Language Alignment Model
- [按轮熵连续重加权GRPO优势](../conferences/icml-2026/cards/5101-5200.md#xing26g-loss-functions) · Native Active Perception as Reasoning for Omni-Modal Understanding
- [同区域多问题的潜表示一致奖励](../conferences/icml-2026/cards/5201-5300.md#xu26aw-loss-functions) · Semantic-Enriched Latent Visual Reasoning
- [多事件定位同时奖励覆盖和计数](../conferences/icml-2026/cards/5201-5300.md#xu26cc-loss-functions) · Towards One-to-Many Temporal Grounding

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
- [稀少配对监督与边缘样本分工](../conferences/icml-2026/cards/3601-3700.md#persiianov26a-loss-functions) · Inverse Entropic Optimal Transport Solves Semi-supervised Learning via Data Likelihood Maximization
- [把 IPW 下游风险曲率写进倾向得分损失](../conferences/icml-2026/cards/3601-3700.md#plaud26a-loss-functions) · Tailoring Strictly Proper Scoring Rules for Downstream Tasks: An Application to Causal Inference
- [反向扩散高斯矩联合匹配](../conferences/icml-2026/cards/3701-3800.md#qian26h-loss-functions) · Likelihood Matching for Diffusion Models
- [用类先验扰动稳住长尾伪标签训练](../conferences/icml-2026/cards/3701-3800.md#qiao26b-loss-functions) · Class-Prior Perturbation-Robust Regularization for Imbalanced Unreliable Partial Label Learning
- [以两组预测差代替逐对对齐](../conferences/icml-2026/cards/3801-3900.md#reichart26a-loss-functions) · Scaling Unsupervised Multi-Source Federated Domain Adaptation through Group-Wise Discrepancy Minimization
- [无标签环境识别预测应忽略的变化方向](../conferences/icml-2026/cards/3901-4000.md#saengkyongam26a-loss-functions) · Anti-causal domain generalization: Leveraging unlabeled data
- [异常检测的白噪声残差与自适应滤波](../conferences/icml-2026/cards/4001-4100.md#shang26e-loss-functions) · COGNOS: Universal Enhancement for Time Series Anomaly Detection via Constrained Gaussian-Noise Optimization and Smoothing
- [把判别梯度与置信校准分开](../conferences/icml-2026/cards/4001-4100.md#sheng26a-loss-functions) · From Individual Calibration to Reliable Classifiers: ALD Parameterization with mPAIC Guarantees
- [把可靠性先验写入不确定性下界](../conferences/icml-2026/cards/4101-4200.md#shihab26b-loss-functions) · CalPro: Prior-Aware Evidential Conformal Prediction with Structure-Aware Sensitivity Bounds for Protein Structures
- [稀疏雅可比与少量锚点配准](../conferences/icml-2026/cards/4101-4200.md#shrestha26a-loss-functions) · Domain Transfer Becomes Identifiable via a Single Alignment
- [分布约束校准与无偏矩损失](../conferences/icml-2026/cards/4101-4200.md#smith26a-loss-functions) · Calibrating Generative Models to Distributional Constraints
- [全序事件下界训练](../conferences/icml-2026/cards/4301-4400.md#tang26x-loss-functions) · Learning to Rank by Directly Optimizing Full-Order Probabilities
- [value-repulsion-grokking](../conferences/icml-2026/cards/4401-4500.md#tao26f-loss-functions) · The Geometric Origin of Grokking: Accelerating Generalization via Active Structural Reorganization
- [多尺度几何集合生成损失](../conferences/icml-2026/cards/4401-4500.md#torkamani26a-loss-functions) · Magnitude Distance: A Geometric Measure of Dataset Similarity
- [amortized-attribution](../conferences/icml-2026/cards/4401-4500.md#tran26h-loss-functions) · Unified Time Series Explanations via Amortized Optimization and Instance-level Multi-Expert Knowledge Distillation
- [solver-free-decision-loss](../conferences/icml-2026/cards/4501-4600.md#wan26i-loss-functions) · A Solver-Free Training Method for Predict-then-Optimize
- [数据分布距离与约束可信度](../conferences/icml-2026/cards/4701-4800.md#wang26gd-loss-functions) · BASIL: Scalable Bayesian Semi-supervised Clustering with Feature Selection and Adaptive Constraint Weighting
- [频率组稀疏与组内谱稀疏](../conferences/icml-2026/cards/4701-4800.md#wang26gk-loss-functions) · Refining Dual Spectral Sparsity in Transformed Tensor Singular Values
- [实例条件的任务标签关系监督](../conferences/icml-2026/cards/4901-5000.md#wang26li-loss-functions) · ReCoG: Relational and Compact Context Graph Learning for Few-shot Molecular Property Prediction
- [校准应检查路由后的聚合](../conferences/icml-2026/cards/4901-5000.md#wong26a-loss-functions) · Toward Calibrated Mixture-of-Experts Under Distribution Shift
- [流形流映射的停止目标回归](../conferences/icml-2026/cards/4901-5000.md#woo26a-loss-functions) · Riemannian MeanFlow
- [对密度比梯度的Sobolev正则](../conferences/icml-2026/cards/5101-5200.md#xie26b-loss-functions) · Sobolev Regularized Score Difference Estimation in Diffusion Models
- [按主方向与方差匹配合成数据](../conferences/icml-2026/cards/5101-5200.md#xie26l-loss-functions) · FedUSD: Unbiased Synthetic Data for Federated Learning
- [用分箱密度头精炼回归伪标签](../conferences/icml-2026/cards/5201-5300.md#xu26i-loss-functions) · Discretized Density-Guided Source-Free Domain Adaptation for Regression
- [按teacher不确定性选择反向交叉熵](../conferences/icml-2026/cards/5201-5300.md#xu26by-loss-functions) · Weak-to-Strong Generalization via Bregman Bias–Variance Decomposition
- [源目标差校正的冻结预测蒸馏](../conferences/icml-2026/cards/5301-5400.md#yan26l-loss-functions) · Invariant Representation Learning for Source-Free Time Series Forecasting with LLM-Centric Proxy Denoising

<a id="by-graph-and-recommendation"></a>

### 图学习与推荐

- [推荐排序的伪负例偏好优化](../conferences/icml-2026/cards/0601-0700.md#chen26ez-loss-functions) · Mitigating Reward Hacking in LLM-based Recommendation: A Preference Optimization Approach
- [时序图解释的稳定与转变证据](../conferences/icml-2026/cards/0601-0700.md#chen26gx-loss-functions) · ST-TGExplainer: Disentangling Stability and Transition Patterns for Temporal GNN Interpretability
- [图混合专家的分组对比路由](../conferences/icml-2026/cards/0801-0900.md#deng26u-loss-functions) · Discriminative Mixture-of-Experts on Graphs with Reliable Expert Fusion
- [属性图聚类的双视图去冗余](../conferences/icml-2026/cards/0901-1000.md#ding26v-loss-functions) · Discriminative Attribute Graph Clustering Through Topology-Guided Contrastive Learning
- [基于子图解释的模型水印](../conferences/icml-2026/cards/0901-1000.md#downer26a-loss-functions) · Watermarking Graph Neural Networks via Explanations for Ownership Protection
- [按邻居类型重写图推荐的负样本分数](../conferences/icml-2026/cards/2301-2400.md#lee26w-loss-functions) · Rethinking Contrastive Learning for Graph Collaborative Filtering: Limitations and a Simple Remedy
- [隐式推荐的互补损失与私有分解](../conferences/icml-2026/cards/3801-3900.md#ran26c-loss-functions) · Differentially Private Cross-Silo Recommendation from Implicit Feedback
- [以多空间尺度的分布教师辅助长尾实体表征](../conferences/icml-2026/cards/4101-4200.md#siampou26a-loss-functions) · Mobility-Embedded POIs: Learning What A Place Is and How It Is Used from Human Movement
- [event-residual-shell-restriction](../conferences/icml-2026/cards/4401-4500.md#tian26h-loss-functions) · Learning Discriminative and Generalizable Anomaly Detector for Dynamic Graph with Limited Supervision
- [图相对核密度异常目标](../conferences/icml-2026/cards/4701-4800.md#wang26hb-loss-functions) · Learnable Kernel Density Estimation for Graphs and Its Application to Graph-Level Anomaly Detection
- [跨稀疏率监督解释边](../conferences/icml-2026/cards/5001-5100.md#wu26j-loss-functions) · Multi-scale Explainer for Graph Neural Networks
- [改变同配性但约束拓扑扰动的图增强](../conferences/icml-2026/cards/5201-5300.md#xu26a-loss-functions) · SFCLTA: Spectral Fusion Contrastive Learning with Topology-Adaptive Graph Augmentation

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
- [不平衡光谱识别的对称信息瓶颈](../conferences/icml-2026/cards/3701-3800.md#qin26b-loss-functions) · SymSpectra: Symmetric Information Bottleneck Framework for Molecular Structure Recognition under Imbalanced Settings
- [用离策略能量标签校正密度形状](../conferences/icml-2026/cards/3901-4000.md#schopmans26a-loss-functions) · Efficient Training of Boltzmann Generators Using Off-Policy Log-Dispersion Regularization
- [用独立残差乘积消除 BSDE 损失偏差](../conferences/icml-2026/cards/4001-4100.md#seo26c-loss-functions) · Unbiased and Second-Order-Free Training for High-Dimensional PDEs
- [按保真度拆分可用监督](../conferences/icml-2026/cards/4601-4700.md#wang26av-loss-functions) · Credible Information Subset Decomposition: An End-to-End Multi-fidelity Learning Model by Modeling Label Information
<!-- classification:end -->
