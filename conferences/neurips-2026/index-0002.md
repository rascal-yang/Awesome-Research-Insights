# NeurIPS 2026 论文索引 · 第 2 卷

[会议首页](README.md)

| 领域 | 技术类型 | 论文卡 | 能改变的技术选择 |
| --- | --- | --- | --- |
| 多模态 | 功能 token | [ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both](cards-0002.md#paper-155024) | 把视觉操作编码成共享的离散词元 |
| 视频生成 | 多尺度生成 | [AtlasVid: Efficient Ultra-High-Resolution Long Video Generation via Decoupled Global-Local Modeling](cards-0002.md#paper-150426) | 先规划低分辨率全局视频再细化 |
| 图学习 | 拓扑预测 | [A Topological Encoder Decoder Framework for Temporal Graph Learning](cards-0002.md#paper-151161) | 先预测未来拓扑再生成节点及边 |
| 因果推断 | 基准诊断 | [A Topological Sorting Criterion for Random Causal Directed Acyclic Graphs](cards-0002.md#paper-154767) | 检查随机因果图能否由亲缘计数轻易排序 |
| 数值优化 | 预条件 | [A Transformer-Derived Iterative Preconditioner](cards-0002.md#paper-153148) | 从模型发现迭代式预条件，再写成独立算法 |
| 概率建模 | 信赖域 | [A Trust Region Approach for Learning Schrödinger Bridges](cards-0002.md#paper-149517) | 目标仅有非归一密度时约束桥接迭代步幅 |
| 视觉学习 | 特征提取 | [Attending on Attention ($A^2$): Smaller Self-Supervised ViTs Localize Better Than Larger Ones](cards-0002.md#paper-154201) | 小模型负责定位、大模型负责局部嵌入 |
| 视频生成 | 流式记忆 | [Attend Locally, Remember Linearly: Linear Attention as Cross-Frame Memory for Autoregressive Video Diffusion](cards-0002.md#paper-154730) | 在帧内保留 softmax，跨帧使用固定状态 |
| 学习理论 | 经验贝叶斯 | [Attention as In-Context Empirical Bayes: A Two-Stage View via Particle Dynamics](cards-0002.md#paper-149497) | 分开调节上下文精炼深度和原始查询保留。 |
| 因果学习 | 摊销推断 | [Attention-Based Pretraining for Unsupervised Amortized Causal Discovery](cards-0002.md#paper-153811) | 多个域共享图结构求解器。 |
| 大语言模型 | 扩散采样 | [Attention-Based Sampler for Diffusion Language Models](cards-0002.md#paper-149963) | 按注意力列和排序解掩码位置。 |
| 神经符号学习 | 软约束 | [Attention-Based Soft Answer Sets](cards-0002.md#paper-151077) | 将离散求解替换为可微不动点残差。 |
| 大语言模型 | 并行解码 | [Attention-Discounted Adaptive Sampler for Masked Diffusion Language Models](cards-0002.md#paper-150267) | 对依赖已选低置信位置的候选打软折扣。 |
| 大语言模型 | 推测解码 | [Attention Drift: What Auto-Regressive Speculative Decoding Models Learn](cards-0002.md#paper-152952) | 按草稿深度监控状态范数并加归一化。 |
| 多模态学习 | 视觉定位 | [Attention Heads are Complementary Visual Units: Mitigating Hallucinations in LVLMs via Adaptive Visual Cues Focusing](cards-0002.md#paper-149428) | 保留各注意头独有的视觉证据。 |
| 大语言模型 | 路由压缩 | [Attention Is More Than You Need: Spectral Redundancy in Multi-Head Routing](cards-0002.md#paper-155116) | 分别测共享 KV 与实际路由谱冗余。 |
| 计算机视觉 | 流式重建 | [Attention Itself Could Retrieve. RetrieveVGGT: Training-Free Long Context Streaming 3D Reconstruction via Query-Key Similarity Retrieval](cards-0002.md#paper-150300) | 用早层查询键相似度选取固定数量历史帧。 |
| 计算机视觉 | 注意力蒸馏 | [Attention Transfer Is Not Universally Effective for Vision Transformers](cards-0002.md#paper-156052) | 跨教师家族前先验证学生架构兼容。 |
| 模型审计 | 来源验证 | [AttnDiff: Attention-based Differential Fingerprinting for Large Language Models](cards-0002.md#paper-151981) | 用差分行为表征交叉验证模型谱系。 |
| 高效推理 | 早退出 | [Attribution-Guided Exit Policy for Reliable Early-Exit Inference](cards-0002.md#paper-152941) | 把跨层归因稳定性作为置信度的补充。 |
| 可解释性 | 二阶归因 | [Attributions All the Way Down? The Metagame of Interpretability](cards-0002.md#paper-148384) | 分开测特征对输出和对彼此归因的影响。 |
| 强化学习 | 多目标调度 | [Auction-Based Online Policy Adaptation for Evolving Objectives](cards-0002.md#paper-153035) | 为运行期出现或消失的目标动态插拔局部策略。 |
| 多模态学习 | 空间音频 | [Audible World Models: Spatially Aware Sound Generation for 3D Worlds](cards-0002.md#paper-154507) | 把声源附着到三维几何，再按听者位置渲染。 |
| 语音 Agent | 故障归因 | [AudioAgentBench: Evaluating Multi-Turn Voice Agents on Real-World Tasks](cards-0002.md#paper-139120) | 按回合定位第一次失误并避免重复扣分。 |
| 音频学习 | 压缩表征 | [AudioGS: High-Fidelity Neural Audio Compression via Continuous Gaussian Splatting](cards-0002.md#paper-149852) | 用可渲染基元分解代替训练期码本量化。 |
| 音频学习 | 自监督表征 | [AudioSphere: Towards Self-Supervised Spatial Audio Representation Models](cards-0002.md#paper-151452) | 掩码重建时同时恢复频谱与方向线索。 |
| 多模态学习 | 时序推理 | [Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos](cards-0002.md#paper-153983) | 用时间戳连接长视频的中间音视频证据。 |
| 科学评测 | 错误诊断 | [Auditing AI peer reviewers: a dose-response and false-positive benchmark on real scientific papers](cards-0002.md#paper-152885) | 用严重度梯度和误报率联合评估自动审稿。 |
| 可靠性 | 分布外诊断 | [Auditing Attention Head Masking for Out-of-Distribution Detection: Cross-Architecture Wins, Failures, and Polarity Inversions](cards-0002.md#paper-139256) | 先检查异常分数方向再跨骨干部署。 |
| 学习理论 | 复现诊断 | [Auditing Closed-Loop Learning in Recurrent Neural Networks: Reproduction, Robustness, and Generalization](cards-0002.md#paper-157025) | 分别衡量闭环训练中的短暂损失峰、最终损失和耦合稳定性。 |
| 统计学习 | 共形校准 | [Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift](cards-0002.md#paper-138875) | 按真实量化与温度配置做覆盖验收。 |
| 表征学习 | 部署评测 | [Auditing Single-Query Recoverability in Self-Supervised Representations](cards-0002.md#paper-152886) | 单输入系统按单输入验收。 |
| 大语言模型 | 评审校准 | [Auditing the Judge: Human-Grounded Bias Discovery, Quantification, and Mitigation in LLM Judges](cards-0002.md#paper-153728) | 用人机分歧发现偏差，再用受控改写测量偏差。 |
| 强化学习 | 约束优化 | [Augmented Lagrangian Method for Last-Iterate Convergence for Constrained MDPs](cards-0002.md#paper-155499) | 单策略部署时检验最终迭代收敛。 |
| 多模态学习 | 音频标记化 | [A Unified Audio Language Model with Text-Aligned Factorized Audio Tokenization](cards-0002.md#paper-154205) | 将语言可表达信息与波形保真信息分开编码。 |
| 隐私 | 风险界 | [A Unified Framework for Adversary-Aware Differential Privacy Bounds](cards-0002.md#paper-153636) | 评估差分隐私时将无输出时的先验成功率纳入比较。 |
| 多模态学习 | 时空编码 | [A Unified Image and Video Encoder for Multimodal LLMs](cards-0002.md#paper-154993) | 把低层时序建模前移到视觉编码器。 |
| 优化 | 学习率迁移 | [A Unified Merge Calculus for Learning-Rate Scaling on Neural Computation Graphs](cards-0002.md#paper-152315) | 按计算图合并方式而非只按深度迁移学习率。 |
| 统计学习 | 结构约束 | [A Unified Neural Architecture for Variable-Wise Shape Constraints](cards-0002.md#paper-149870) | 用结构保证逐变量单调性或曲率。 |
| 多模态 | 目标函数 | [A Unified Spectral Theory of Multimodal Losses](cards-0002.md#paper-155760) | 单侧噪声重时优先检验定向生成 |
| 学习理论 | 上下文学习 | [A Unified Theoretical Framework for Task Recognition and Task Learning in In-Context Learning](cards-0002.md#paper-149830) | 按任务频率分组测提示长度收益 |
| 优化 | 算子正则 | [A Unifying View of Anchoring via Operator-Side Tikhonov Regularization](cards-0002.md#paper-153667) | 在算子查询端加入消失的正则以复用原更新 |
| 视频生成 | 结构化控制 | [Auteur: Language-Driven Cinematographic Framing for Human-Centric Video Generation](cards-0002.md#paper-155137) | 用相对演员的镜头语言生成关键帧 |
| 大语言模型 | 数据管线评测 | [AutoDataBench: How Far Are LLM Agents from Autonomously Engineering Post-Training Data Pipelines?](cards-0002.md#paper-139001) | 固定学生模型，以训练后的效果检验数据管线 |
| Agent | 离线记忆 | [Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents](cards-0002.md#paper-152534) | 把即时记忆采集和跨会话压缩拆成两个阶段 |
| AI 安全 | 防御评测 | [AutoHoney: Automating, Deploying, and Evaluating Scheming Honeypots Across Production Codebases](cards-0002.md#paper-139153) | 分开测任务范围和评测知情状态对审计结果的影响 |
| Agent | 故障检测 | [Automata from Agent Traces: Failure and Next-Step Prediction](cards-0002.md#paper-148996) | 跨轨迹建有限状态机并监控各状态失败信号 |
| 数据质量 | 标注诊断 | [Automated Hypothesis Discovery for Characterizing Annotation Disagreement](cards-0002.md#paper-139723) | 留出验证用于筛选生成的分歧假设 |
| 优化 | 核设计 | [Automated Kernel Discovery Towards Understanding High-dimensional Bayesian Optimization](cards-0002.md#paper-149210) | 用留一概率评分选核并分离数学提案和实现 |
| 强化学习 | 约束优化 | [Automatic Constraint Policy Optimization based on Continuous Constraint Interpolation Framework for Offline Reinforcement Learning](cards-0002.md#paper-151401) | 用验证反馈自调离线策略约束类型。 |
| Agent / 科学机器学习 | 研究评测 | [Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?](cards-0002.md#paper-139352) | 区分智能体的工程调参与领域创新。 |
| Agent | 记忆学习 | [AUTOMEM: Automated Learning of Memory as a Cognitive Skill](cards-0002.md#paper-150660) | 把文件记忆决策与任务动作分开优化。 |
| Agent | 持续适配 | [Autonomous Continual Learning for Environment Adaptation of Computer-Use Agents](cards-0002.md#paper-154225) | 用上一轮反馈生成贴近当前能力的课程。 |
| 科学机器学习 | 假设检验 | [Autonomous Scientific Discovery via Iterative Meta-Reflection](cards-0002.md#paper-149249) | 将已验证的发现作为下一轮假设生成输入。 |
| Agent | 离线评估 | [Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents](cards-0002.md#paper-153481) | 让目标策略在每个模拟转移后重新行动。 |
| 多模态 | 奖励分解 | [Auto-Rubric as Reward: From Implicit Preference to Explicit Generative Criteria](cards-0002.md#paper-151565) | 比较输出前先生成任务特定的质量细则。 |
| Agent | 执行迭代 | [AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](cards-0002.md#paper-151256) | 用留出任务检验从失败轨迹提出的配置修订。 |
| 多模态 | 编辑评测 | [AVENUE: Audio-Video Editing Understanding and Evaluation](cards-0002.md#paper-138887) | 逐样本记录目标改动及应保留模态。 |
| 多模态 | 传感融合 | [AVI-HT: Adaptive Vision-IMU Fusion for 3D Hand Tracking](cards-0002.md#paper-154518) | 遮挡条件下按传感器动态调节可信度。 |
| 多模态 | 推理预算 | [AVIS: Adaptive Test-Time Scaling for Vision–Language Models](cards-0002.md#paper-150182) | 联合分配视觉 token 和推理采样次数。 |
| 大语言模型 | 自蒸馏 | [AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals](cards-0002.md#paper-150780) | 用跨教师视图共识确定更新方向。 |
| 强化学习 | 多智能体分解 | [Axiomatic Reinforcement Learning for Open Multi-Agent Systems from Shapley Axioms](cards-0002.md#paper-148243) | 以合作博弈公理约束开放队伍的个体值。 |
| 大语言模型 / 科学推理 | 奖励设计 | [Axiomatic World Modeling for Physics Reasoning](cards-0002.md#paper-150823) | 给物理前提建模和求解过程分别评分。 |
| 优化 | 梯度估计 | [B2P-Corr: Batch-to-Population Gradient Estimators for Non-Decomposable Correlation Losses](cards-0002.md#paper-154786) | 对相关系数损失维护跨批矩统计量。 |
| Agent / 世界模型 | 在线模型修订 | [Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models](cards-0002.md#paper-150860) | 把更新后丢失的旧转移用作反例。 |
| 生成模型 / 评测 | 异常检测 | [Backbone-Equated Diffusion OOD via Sparse Internal Snapshots](cards-0002.md#paper-154161) | 在匹配骨干和测试成本后检查单次内部快照。 |
| 大语言模型 | 多目标偏好 | [Back to Blackwell: Closing the Loop on Intransitivity in Multi-Objective Preference Fine-Tuning](cards-0002.md#paper-148405) | 当偏好循环时保留多目标判据。 |
| 语言模型 | 推理搜索 | [Backtracking with Linear-in-Depth Search-Space Growth: Width-Limited Tree Search for Large Language Models](cards-0002.md#paper-155253) | 同预算比较有无回溯及宽度约束 |
| 优化 | 多任务学习 | [Balanced Multi-Task Learning from an Optimality-Gap Perspective](cards-0002.md#paper-153699) | 比较损失尺度与局部改进上限两种归一化 |
| 生成模型 | 频谱损失 | [Balancing Frequencies and Pixels in Flow Matching](cards-0002.md#paper-151310) | 分别消融频谱监督和阶段切换 |
| Agent | 模型路由 | [Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery](cards-0002.md#paper-154569) | 同预算对照均值路由与谱系信用 |
| 语言模型 | 信用分配 | [BALTO: Balanced Token-Level Policy Optimization for Hallucination Mitigation](cards-0002.md#paper-150212) | 在混合正误回答中对照局部和整段奖励 |
| 推荐 / 语言模型 | 持续适配 | [Base Items Overfit, New Items Underfit: Hidden Cost of Joint Training in Incremental Adaptation](cards-0002.md#paper-156066) | 绘制旧新质量随训练时长变化的独立曲线 |
| 深度学习 | 注意力参数化 | [Basis-Mediated Bilinear Attention: A New Method for Greatly Reducing Query--Key Pathway Parameters](cards-0002.md#paper-154941) | 同预算比较共享基、完全共享和独立低秩 |
| 语言模型 | 推理解码 | [BASTION: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting](cards-0002.md#paper-151263) | 相同草稿下比较固定及自适应预算 |
| 视觉 | 流式重建 | [BAT3R: Robust Online 3D Reconstruction with Bayesian Adaptive State Updates](cards-0002.md#paper-153286) | 分开测历史区域保护及新场景更新 |
| 视觉 | 几何细化 | [BA-T: An Iterative Transformer for Two-View Bundle Adjustment](cards-0002.md#paper-148295) | 同延迟比较重复几何层和加深解码器 |
| 多模态 | 测试时适配 | [Batch-Conditioned Semantic Anchors for Robust Transductive Adaptation of Vision--Language Models](cards-0002.md#paper-154091) | 按批次可靠性移动语义锚点 |
| 学习理论 | 受限通信 | [Batched Stochastic Linear Bandits with 1-Bit Communication Constraints](cards-0002.md#paper-150229) | 将批反馈位预算单列为遗憾项 |
| 多模态 | 联合生成 | [Baton: Explicit Semantic Blueprints for Joint Video-Audio Generation](cards-0002.md#paper-153708) | 去噪前对齐关键帧级音视频计划 |
| 统计学习 | 不确定性估计 | [Bayesian Backprop as Belief Propagation: Single-Pass Predictive Uncertainty](cards-0002.md#paper-154383) | 用单次矩传播代替重复采样推理 |
| 因果推断 | 敏感性分析 | [Bayesian Causal Stress Testing: Posterior Fragility of Treatment-Effect Conclusions](cards-0002.md#paper-155177) | 分别报告后验区间和推翻主张的最小扰动 |
| 决策理论 | 专家反馈 | [Bayesian Decision Making around Experts](cards-0002.md#paper-149882) | 用单位更新预算的信息价值选择专家或自身数据 |
| 优化 | 信赖域 | [Bayesian Optimization with Fisher Information Geometry: Gradient Bounds and Trust-Region Methods](cards-0002.md#paper-156134) | 用代理后验局部敏感度设置搜索尺度 |
| 大语言模型 | 奖励适配 | [Bayesian Preference Learning for Test-Time Steerable Reward Models](cards-0002.md#paper-150486) | 通过示例更新潜在偏好以调节奖励模型 |
| 大语言模型 | 测试时搜索 | [Bayesian Test-Time Inference of Task-Aligned Similarity from Weak Interactive Feedback](cards-0002.md#paper-152715) | 根据少量反馈动态推断当前任务的相似性轴 |
| 评测 | 评判校准 | [BayesJudge: Uncertainty-Aware Bayesian Meta-Evaluation of Human and LLM Judgments](cards-0002.md#paper-138918) | 保留平局并交换候选次序以测位置偏差 |
| 统计学习 | 评测上限 | [Bayes-Optimal BER and AUC: Estimation and Evaluation of Estimators](cards-0002.md#paper-152377) | 类别失衡时估计最优 BER 或 AUC 而非准确率上限 |
| Agent | 协作诊断 | [Bayes-Sufficient Compression Is Not Enough: How Communication Helps in Multi-Agent Systems?](cards-0002.md#paper-155601) | 比较压缩消息、原始上下文和不通信 |
| 大语言模型 | 模型融合 | [BDC-Merge: Cross-Architecture Model Merging via Dependency Alignment](cards-0002.md#paper-151593) | 用非线性依赖对齐异构模型。 |
| 具身智能 | 域适应 | [BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation](cards-0002.md#paper-151303) | 按样本差异学习源示范权重。 |
| 强化学习 | 部分可观测控制 | [BECON: Belief-Conditioned Constrained Multi-Objective Reinforcement Learning under Drifting Preferences and Budgets](cards-0002.md#paper-153172) | 按不确定性融合推断的任务偏好与外部信号。 |
| 多模态学习 | 表征诊断 | [Before It Fades: Reinforcing Temporal Representations at Inference Time in VideoLLMs](cards-0002.md#paper-155460) | 用反转帧序定位时间信号衰减并在推理期补回。 |
| 大语言模型 | 后训练诊断 | [Behaving Better, Thinking Worse: Sycophancy Across Post-Training Stages](cards-0002.md#paper-153819) | 联合比较生成翻转率与同样本预测概率。 |
| 强化学习 | 行为搜索 | [Behavioral Foundation Models for Quality Diversity](cards-0002.md#paper-148386) | 在预训练行为潜空间内做质量多样性搜索。 |
| 计算机视觉 | 表征对齐 | [Behavioral Geometric Supervision Aligns Video Foundation Models with Human Social Perception](cards-0002.md#paper-149277) | 用人类视频相似性判断监督局部和全局嵌入几何。 |
| 模仿学习 | 蒸馏理论 | [Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback](cards-0002.md#paper-150673) | 有噪教师下优先验证学生访问状态上的在线蒸馏。 |
| 强化学习 | 奖励鲁棒性 | [Behavior-Discriminative Reward Shaping for Reward-Robust Reinforcement Learning](cards-0002.md#paper-155941) | 按策略排序等价类定义奖励不确定集。 |
| 多模态学习 | 强化后训练 | [Behavior Pack Optimization for Video MLLM Post-Training](cards-0002.md#paper-150981) | 把同一视频问题的反事实视图作为联合奖励单位。 |
| Agent | 状态更新 | [Belief Engine: Configurable Stance Dynamics for Multi-Agent LLM Deliberation](cards-0002.md#paper-151258) | 让立场变化受显式证据吸收与先验锚定控制 |
| 强化学习 | 收缩性分析 | [Bellman Contraction under MMD: A Unified Framework](cards-0002.md#paper-150640) | 用差分核条件检验分布式 Bellman 更新的收缩 |
| Agent | 评估偏差 | [Below the Reliability Floor: Recovering True Success from Judge-Gated Loops](cards-0002.md#paper-156773) | 重试门控后独立抽取金标准验证真实成功率 |
| 大语言模型 | 防御监测 | [Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs](cards-0002.md#paper-139423) | 将安全分类与分布外报警独立融合 |
| 时序预测 | 故障评测 | [Benchmarking Sensor-Fault Robustness in Forecasting](cards-0002.md#paper-138912) | 单独比较干净精度与故障最坏误差。 |
| Agent | 部署审计 | [Benchmark Recovery Does Not Certify a Frozen Tool-Trigger Contract After Quantization](cards-0002.md#paper-155241) | 量化验收时固定工具权限与参考标签，再单独检查触发。 |
| 大语言模型 | 基准诊断 | [Benchmarks Are Not Atomic: Composition-Aware LLM Evaluation using BenchHub](cards-0002.md#paper-139267) | 用属性分布匹配应用后再比较模型。 |
| 统计学习 | 测量可靠性 | [Benchmarks as Measurement Instruments: Quantifying Signal and Noise for More Efficient AI Evaluations Under Distribution Shift](cards-0002.md#paper-139555) | 按目标模型群体估计题目对排名的测量价值。 |
| 大语言模型 | 数据消融 | [Benchmark Shadows: How Data Regimes Shape Parameter Footprints and Generalization](cards-0002.md#paper-154989) | 把重复和频率集中分开，对照后续多样数据能否修复。 |
| 大语言模型 | 防御验收 | [Benign Reinforcement Learning Can Amplify Latent Backdoors](cards-0002.md#paper-149677) | 在强化学习后重新进行安全回归测试。 |
| 多模态学习 | 生成架构 | [Bernini: Latent Semantic Planning for Video Diffusion](cards-0002.md#paper-154106) | 用视觉语义潜变量作为规划器和视频渲染器的接口。 |
| 生成模型 | 快速采样 | [Bernoulli Flow Models: Self-Consistent Generative Modeling for Binary Data](cards-0002.md#paper-155986) | 二值扩散跳步时使用与间隔一致的后验。 |
| 强化学习 | 纯探索 | [Best Arm Identification for Bandits with Shifting Means](cards-0002.md#paper-153746) | 奖励存在共同漂移时用重要性加权取代固定均值停止检验。 |
| 强化学习 | 主动查询 | [Best Arm Identification in Generalized Linear Bandits via Hybrid Feedback](cards-0002.md#paper-151037) | 把单臂绝对观测和成对比较纳入同一查询设计。 |
| 生成模型 | 推理引导 | [Best-of-$N$ Guidance for Test-time Diffusion Alignment](cards-0002.md#paper-154666) | 并行去噪过程中用当前优选粒子引导其余样本。 |
| 统计学习 | 序贯检验 | [Bet Imaginatively, not Historically in Independent-Data Sequential Testing](cards-0002.md#paper-155229) | 独立同分布假设成立时，用重排历史估计下注收益。 |
| 生成模型 | 流匹配 | [Better Source, Better Flow: Learning Condition-Dependent Source Distribution for Flow Matching](cards-0002.md#paper-148679) | 学习条件源分布 |
| 大语言模型 | 压缩 | [Beyond Adjacent Layers: Graph-Guided Layer Fusion for Compressing Large Language Models](cards-0002.md#paper-152044) | 按全层相似性选保留层 |
| 具身智能 | 行为校准 | [Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models](cards-0002.md#paper-150087) | 分别测任务保持和任务改变后的动作 |
| 学习理论 | 专家路由 | [Beyond Augmented-Action Surrogates for Multi-Expert Learning-to-Defer](cards-0002.md#paper-148942) | 解耦类别与各专家的训练头 |
| 优化 | 域泛化 | [Beyond Average Flatness: Domain-wise Flatness for Domain Generalization](cards-0002.md#paper-150477) | 按域测尖锐度并约束域间不平衡 |
| 多模态学习 | 组合评测 | [Beyond Bag-of-Words: Diagnosing Compositional Binding Failures in Vision-Language Models](cards-0002.md#paper-139620) | 配对最小场景和真实上下文 |
| 具身智能 | 地图评测 | [Beyond Chamfer Distance: Granular Order-aware Evaluation Metric For Online Mapping](cards-0002.md#paper-139462) | 区分折线排序、定位和检出 |
| 强化学习 | 策略优化 | [Beyond Clipping: Signed Logarithmic Smoothing for Policy Optimization](cards-0002.md#paper-153088) | 平滑整个重要性加权优势而非只截断比率 |
| 视频生成 | 诊断评测 | [Beyond Copy-Paste: How Well Do Subject-Driven Video Models Understand Their Subjects?](cards-0002.md#paper-152728) | 用未见同主体目标检验身份保持 |
| 大语言模型 | 后训练 | [Beyond Correctness: Robustness-Driven Evolutionary Self-Training for Large Language Models](cards-0002.md#paper-151953) | 按推理轨迹的扰动稳健性筛选正确答案 |
| 具身智能 | 表征预训练 | [Beyond Data Scaling: Representation-Centric Pre-training for Vision-Language-Action Models](cards-0002.md#paper-155956) | 共享跨本体动作监督并允许下游换头 |
| 大语言模型 / 多模态 | 参数高效适配 | [Beyond Decoupled PEFT: Geometry-Aware Low-Rank Adaptation via Riemannian Reparameterization](cards-0002.md#paper-153695) | 把低秩方向预算限定在权重方向的切空间 |
| 强化学习 | 课程学习 | [Beyond difficulties: Insights for provably efficient design of autocurriculum in RLVR](cards-0002.md#paper-149187) | 按训练收益而非当前成功率选题 |
| 视觉生成 | 蒸馏 | [Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation](cards-0002.md#paper-154363) | 在输出分布匹配外加入内部预测监督 |
| 三维视觉 | 控制诊断 | [Beyond Downstream Scores: Controlled Diagnostics for Point-Cloud Self-Supervised Learning Evaluation](cards-0002.md#paper-139098) | 将预训练信号、可见几何和读出分别消融 |
| 动力系统 | 相似性 | [Beyond DSA: Conjugacy-based Comparison of Dynamical Systems](cards-0002.md#paper-152248) | 将对齐约束为状态双射诱导的变换 |
| 表征学习 | 谱分析 | [Beyond Eigenfunctions: Divergence Principal Functions for Representation Learning](cards-0002.md#paper-153338) | 按训练散度选择低秩表示几何 |
| 多模态学习 | 组件消融 | [Beyond Encoder Accumulation: Measuring Encoder Roles in Multi-Encoder VLMs](cards-0002.md#paper-152266) | 重新训练编码器组合而非仅在固定权重上遮蔽 |
| 持续学习 | 记忆预算 | [Beyond Exemplar Selection: Value-Aware Memory Allocation in Replay-Based Continual Learning](cards-0002.md#paper-155700) | 在固定缓存中按类别效用调整配额 |
| 强化学习 | 风险规划 | [Beyond Expected Values: Risk-Sensitive Planning with Distributional Monte-Carlo Tree Search](cards-0002.md#paper-149403) | 在树边维护回报分布以评估嵌套尾部风险 |
| 高效推理 | 静态部署 | [Beyond FLOPs: Train-Full, Deploy-Partial Multi-Exit Inference via Selective Lightweight IC Ensemble](cards-0002.md#paper-152802) | 使用校准后的静态截断替代逐样本动态退出 |
| 多模态学习 | 组合对齐 | [Beyond Global Alignment: Structured Compositional Reasoning for Vision-Language Models](cards-0002.md#paper-155609) | 分开监督关系方向与属性的对象归属 |
| 多模态学习 | 区域对齐 | [Beyond Hard Negatives: Grounded Positive Supervision for Compositional CLIP](cards-0002.md#paper-150916) | 用结构化正例改善属性绑定。 |
| 表格学习 | 基准诊断 | [Beyond IID: How General Are Tabular Foundation Models, Really?](cards-0002.md#paper-139490) | 选表格模型时分别检查时间、分组与 IID 划分。 |
| 统计学习 | 保形校准 | [Beyond Imputation: Mask-Adaptive Conformal Prediction via Tree Embeddings on General Missing Data Mechanisms](cards-0002.md#paper-154427) | 在缺失掩码层面检查覆盖率。 |
| 可解释性 | 组合搜索 | [Beyond Incremental Beam Search for Compositional Explanations of Neurons](cards-0002.md#paper-152763) | 避免按单个概念增量扩展时过早丢掉解释候选。 |
| 多模态学习 | 表征干预 | [Beyond Interpretability: When, Why, and How Sparse Autoencoders Enable Label-Free Visual Steering](cards-0002.md#paper-148658) | 用逐样本重建误差决定是否采用稀疏特征修正。 |
| 时序学习 | 训练数据剪枝 | [Beyond Isolation: Neighbor-Consistent Data Pruning for Multivariate Time Series Forecasting](cards-0002.md#paper-154771) | 用重叠窗口的损失轨迹一致性诊断异常样本。 |
| 自监督学习 | 表征几何 | [Beyond Isotropy in JEPAs: Hamiltonian Geometry and Symplectic Prediction](cards-0002.md#paper-149858) | 通过跨视图预测耦合注入结构先验。 |
| 大语言模型 | 表征控制 | [Beyond Linear Activation Steering: Invertible Latent Transformations for Controlling LLM Behavior](cards-0002.md#paper-148807) | 对照固定方向和随输入变化的潜空间干预。 |
| Agent | 故障归因 | [Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution](cards-0002.md#paper-149719) | 用轻量轨迹图替代长文本故障归因。 |
| 大语言模型 | 微调路由 | [Beyond LoRA vs. Full Fine-Tuning: Gradient-Guided Optimizer Routing for LLM Adaptation](cards-0002.md#paper-154880) | 在优化器层动态分配低秩和全量更新。 |
| 神经形态计算 | 频率选择 | [Beyond Low-Pass Dynamics: Frequency-Selective Spiking Reservoirs with Resonant Neurons](cards-0002.md#paper-148662) | 用异构共振单元辨别不同时标。 |
| 统计学习 | 局部校准 | [Beyond Marginal Coverage: Efficient Localized Conformal Prediction via Residual Rank Calibration](cards-0002.md#paper-153265) | 用标准化残差的局部秩代替逐查询的加权分位数。 |
| 系统效率 | 稀疏算子 | [Beyond Masked Sparsity: SNACK Enables Truly Sparse Neural Networks on GPU](cards-0002.md#paper-150469) | 高稀疏度时改用真正稀疏的前后向 |
| 视觉 | 逆问题 | [Beyond MMSE: Enhancing PnP Restoration with ProxiMAP](cards-0002.md#paper-151995) | 使残余噪声匹配去噪器训练噪声 |
| 多模态 | 模型融合 | [Beyond Modality Fusion: Deep Ensembles for Multimodal Classification](cards-0002.md#paper-155113) | 等参数比较单模态集成和特征融合 |
| Agent | 自蒸馏 | [Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents](cards-0002.md#paper-154780) | 只在失败轨迹上按步骤调整优势幅度 |
| 图学习 | 传播诊断 | [Beyond Oversquashing: Understanding Signal Propagation in GNNs Via Observables](cards-0002.md#paper-154868) | 测特定源到目标区域的信号输运 |
| 大语言模型 | 偏好优化 | [Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph](cards-0002.md#paper-150929) | 按偏好图聚合多样本，平局不给梯度 |
| 联邦学习 | 行为蒸馏 | [Beyond Parameter Aggregation: Semantic Consensus for Federated Fine-Tuning of LLMs](cards-0002.md#paper-155550) | 异构客户端共享行为语义而非参数 |
| 大语言模型 | 模型合并 | [Beyond Parameter Arithmetic: Sparse Complementary Fusion for Distribution-Aware Model Merging](cards-0002.md#paper-149097) | 合并时跟踪终止和重复异常 |
| 视觉 | 扩散采样 | [Beyond Pixel Space: Frequency-Domain Uncertainty Estimation for Structure-Aware Diffusion Guidance](cards-0002.md#paper-152220) | 在频域估计不确定性并引导去噪 |
| Agent | 世界模型 | [Beyond Prediction: Steering VLM Agents with Retrospective World Modeling](cards-0002.md#paper-155042) | 用逆向解释一致性作为过渡奖励 |
| Agent | 记忆检索 | [Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation](cards-0002.md#paper-150607) | 先拆出区分性事实再聚合 |
| 计算机视觉 | 立体校正 | [Beyond Row Alignment: Virtual-Camera-Aware Online Stereo Rectification](cards-0002.md#paper-151291) | 用深度可用性评价在线校正 |
| 多模态学习 | 属性监督 | [Beyond Scalar Distances: Semantic Attribute Gradients from Frozen MLLMs for Visual Embeddings](cards-0002.md#paper-153671) | 从成对图像的属性判断学习检索表征 |
| 多模态学习 | 视觉压缩 | [Beyond Selection: Token Parameterization for Extreme Visual Token Compression](cards-0002.md#paper-151663) | 将基底截断与坐标组织独立设计 |
| 统计学习 | 概率融合 | [Beyond Semantic Alignment: Geometric Incomparability in Multi-Oracle Soft Fusion](cards-0002.md#paper-149809) | 先校准概率几何再做软融合 |
| 学习理论 | 推理诊断 | [Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens](cards-0002.md#paper-156774) | 单独区分中间计算支架与可读语义的贡献 |
| 科学机器学习 | 动力学建模 | [Beyond Single-Step Likelihood: Gibbs Variational Last Layers for Long-Horizon Dynamics Learning](cards-0002.md#paper-152213) | 用多步损失训练贝叶斯末层 |
| 计算机视觉 | 密集匹配 | [Beyond Spatial and Temporal Priors: A Generalizable Approach for Dense Correspondence Matching](cards-0002.md#paper-149352) | 以身份一致性学习非物理连续的对应关系 |
| 多模态学习 | 表征约束 | [Beyond Spatial-Domain Supervision: A Relation Constrained Space for Multi-Modal Image Fusion](cards-0002.md#paper-150788) | 在关系空间监督融合 |
| 大语言模型 | 推理干预 | [Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention](cards-0002.md#paper-155564) | 比较激活上的固定向量与概念条件动态变换 |
| 大语言模型 | 参数高效微调 | [Beyond Structural Agnosticism: Stable-Rank-Guided LoRA for Structure-Aware Fine-Tuning](cards-0002.md#paper-151865) | 按层谱结构与任务梯度分配低秩容量 |
| 强化学习 | 评测诊断 | [Beyond Success Rates: Trainability and Extractability in Offline GCRL](cards-0002.md#paper-139429) | 以超参数景观比较策略提取的鲁棒性 |
| Agent | 在线监控 | [Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents](cards-0002.md#paper-152482) | 检查长程前缀是否仍符合授权任务 |
| Agent | 能力诊断 | [Beyond Task Success: Probing Cognitive Primitives in Web Agents](cards-0002.md#paper-139465) | 用配对任务隔离规划和探索能力 |
| 生成模型 | 强化微调 | [Beyond the Dirac Delta: Mitigating Diversity Collapse in Reinforcement Fine-Tuning for Image Generation](cards-0002.md#paper-155487) | 在固定对齐要求下显式评估多样性 |
| 推荐系统 | 稳健性评测 | [Beyond the Full Slate: Evaluating MNL Algorithms on All Slates](cards-0002.md#paper-149458) | 按实际小候选集而非全库误差选模型 |
| 图学习 | 双向蒸馏 | [Beyond the Golden Teacher: Enhancing Graph Learning through LLM-GNN Co-teaching](cards-0002.md#paper-150344) | 让文本和图模型互教并追踪何时由冲突转为一致 |
| 信号处理 | 连续稀疏分解 | [Beyond the Grid: Continuous Dictionary Pursuit for Interpretable Signal Decomposition](cards-0002.md#paper-151808) | 在连续参数空间拟合可解释信号原子 |
| 多模态学习 | 表征诊断 | [Beyond the Linear Separability Ceiling: Aligning Representations in VLMs](cards-0002.md#paper-156758) | 用线性探针区分视觉表示不足和读出失败 |
| 机器学习系统 | 并行策略 | [Beyond the Node Barrier: Zero-Shot Strategy Planning for LLM Training on Super-Nodes](cards-0002.md#paper-149841) | 在高速互连平台重新评估跨节点张量和专家并行 |
| 大语言模型 | 防护检测 | [Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs](cards-0002.md#paper-151177) | 用扩散解码前的响应表征补充输入风险检测 |
| 时间序列 | 表示学习 | [Beyond the Readout: Reservoir State Statistics for Model-Space Learning under Sparse Observations](cards-0002.md#paper-152483) | 用动态轨迹统计补充稀疏通道的拟合参数 |
| 统计学习 | 偏移风险估计 | [Beyond the Training Distribution: Evaluating Predictions Under Distribution Shift and Selection Bias](cards-0002.md#paper-149001) | 同时校正目标协变量偏移和选择性标签 |
| 机器学习系统 | 分布式训练调参 | [Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training](cards-0002.md#paper-150603) | 先用小规模测量和全局推演筛训练配置 |
| 具身智能 | 空间先验 | [Beyond Thinking: Imagining in 360$^\circ$ for Humanoid Visual Search](cards-0002.md#paper-149744) | 用多假设空间布局引导主动搜索。 |
| 多模态 | 时空定位 | [Beyond Token Representations: Explicit Visual Object Grounding for Video Reasoning Segmentation](cards-0002.md#paper-155293) | 将分割目标明确为框和点，并跨查询校准。 |
| 生成模型 | 蒸馏 | [Beyond Trajectory Matching: Reflow with Marginal Distribution Alignment](cards-0002.md#paper-155442) | 沿每段蒸馏轨迹同时约束终点边际。 |
| 大语言模型 | 检索校验 | [Beyond Uniform Detection: Adaptive Hallucination Detection for RAG Across Response Regimes](cards-0002.md#paper-155755) | 按回答类型切换幻觉检测信号。 |
| 科学机器学习 | 守恒动力学 | [Beyond Unit-Circle Eigenvalues: Invariant Bases for Stable State Space Dynamics](cards-0002.md#paper-149242) | 同时约束特征值和守恒量对应的模态基底。 |
| 多模态 | 视频检索 | [Beyond Visual Boundaries: Rethinking Scene Segmentation for Movie RAG](cards-0002.md#paper-139396) | 按叙事事件切分电影检索单元。 |
| 学习理论 | 推理预算 | [Beyond What Seems Necessary: Hidden Gains from Scaling Training-Time Reasoning Length under Outcome Supervision](cards-0002.md#paper-151533) | 用分布外验证决定训练推理长度。 |
| 具身智能 | 动作表征 | [Beyond World-Frame Action Heads: Motion-Centric Action Frames for Vision-Language-Action Models](cards-0002.md#paper-155672) | 先在学习的运动局部坐标中组装动作。 |
| 图学习 | 误差诊断 | [Bias, Measurement Error, and Double-Dipping: When Can GNN Convolutions Help Brain Connectome Prediction?](cards-0002.md#paper-153204) | 用独立估计图与同样本图对照检查重复使用测量噪声。 |
| 大语言模型 | 偏好优化 | [Bias-Variance Optimized Preference Optimization for Large Reasoning Models](cards-0002.md#paper-152470) | 把普通推理梯度与空推理分支梯度混合降方差。 |
| 生成模型 | 稀疏注意力 | [Bidirectional Sparse Attention for Faster Video Diffusion Training](cards-0002.md#paper-154292) | 同时筛查询和键值 |
| 科学机器学习 | 多解建模 | [Bifurcation Models: Learning Set-Valued Solution Maps with Weight-Tied Dynamics](cards-0002.md#paper-149009) | 用吸引子集合表示多个正确解 |
| 生成模型 | 记忆诊断 | [Bigger Isn't Always Memorizing: Early Stopping Overparameterized Diffusion Models](cards-0002.md#paper-156775) | 数据规模变化后重新校准早停点 |
| 大语言模型 | 数据加权 | [Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning](cards-0002.md#paper-155173) | 用真实验证任务学习合成轨迹权重 |
| 学习理论 | 在线匹配 | [Bilinear Matching Bandits](cards-0002.md#paper-149557) | 利用双线性结构设计分行探索 |
| 大语言模型 | 低比特推理 | [BiLoCo: Binary Low-Rank Corrections for LLM FP4 Decode](cards-0002.md#paper-149418) | 用符号低秩残差和主矩阵乘并行 |
| 多模态学习 | 表征对齐 | [Binding Multiple Modalities via Multimodal Wasserstein Barycenter](cards-0002.md#paper-149098) | 用跨模态重心作为对齐中心 |
| 多模态学习 | 视觉推理 | [Binding Visual Features Point by Point](cards-0002.md#paper-148298) | 让模型先指向对象再判断其属性 |
| Agent | 强化学习 | [BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments](cards-0002.md#paper-152242) | 复用数据库副本时保证轨迹状态隔离 |
| 视觉 | 生成建模 | [BitDance: Scaling Autoregressive Generative Models with Binary Tokens](cards-0002.md#paper-153956) | 用扩散预测高容量二值视觉码而非枚举类别 |
| 语言模型 | 推理加速 | [BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models](cards-0002.md#paper-154757) | 将接受前缀同时对齐缓存与执行图复用 |
| Agent | 学习理论 | [Bits Beat Tokens: A Regret Rate Distortion Theory for Large Language Model Agents](cards-0002.md#paper-150556) | 用决策相关信息量衡量上下文而非长度 |
| 模型架构 | 脉冲网络 | [BitShift-RoPE: Zero-FLOP Relative Positional Encoding for Spiking Neural Network Transformers](cards-0002.md#paper-150476) | 用整数循环移位实现相对位置编码 |
| 优化 | 零阶估计 | [Black-Box Followers, White-Box Leaders: Partial Zeroth-Order Methods for MPECs](cards-0002.md#paper-155774) | 仅对不可微的未知响应做零阶估计 |
| 语言模型 | 不确定性量化 | [Black-Box Uncertainty Quantification for Large Language Models via Ensemble-of-Ensembles](cards-0002.md#paper-151082) | 比较同提示采样和语义等价改写的变异 |
| 语言模型 | 数据选择 | [BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training](cards-0002.md#paper-152234) | 动态更新用于超额损失选择的参考模型 |
| 模型训练 | 局部学习 | [BLANP: Memory-Efficient Backpropagation-Free Local Training via Antithetic Node Perturbation](cards-0002.md#paper-155644) | 内存紧张时比较局部反向梯度与对偶扰动更新 |
| 视觉 | 三维动画 | [BLARM: Animating 3D Objects from Video via Blending LAtent Rigid Motion Primitives](cards-0002.md#paper-155225) | 将网格变形表示为共享刚体运动的混合 |
| 多模态 | 可验证智能体 | [BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](cards-0002.md#paper-151100) | 按场景状态差异为3D编辑生成可验证奖励 |
| 科学机器学习 | 预报评测 | [Blind-Window Forecasting: Real-Time Benchmarking and Multimodal Reconstruction for Tropical Cyclones](cards-0002.md#paper-150222) | 按推理时真实可获得的时间戳构造预报测试 |
| 优化 | 块重采样 | [Blocked Gibbs meets Diffusion Transformers: Unsupervised Learning for Constraint Optimization](cards-0002.md#paper-148271) | 用退火块大小实现离散约束的局部大步修正 |
| 大语言模型 | 剪枝 | [Block-OBS-GS: Exact Per-Block Joint Brain Surgery with Gauss–Seidel Refinement for LLM Pruning](cards-0002.md#paper-152355) | 固定剪枝掩码后精确求块内权重并做跨块校正 |
| 大语言模型 | 强化学习后训练 | [Block-R1: Rethinking the Role of Block Size in Multi-domain Reinforcement Learning for Diffusion Large Language Models](cards-0002.md#paper-139480) | 训练扩散语言模型时按样本选 rollout 块大小 |
| 大语言模型 | 稀疏注意力 | [Block Sparse Flash Attention](cards-0002.md#paper-155122) | 在计算精确查询键分数后按块阈值省去低价值计算 |
| 高效机器学习 | 向量量化 | [Block Sphere Vector Quantization](cards-0002.md#paper-152314) | 根据重建或检索目标选择量化准则 |
| 大语言模型 | 注意力量化 | [BMAttn: Block-Aligned Mixed-Precision Attention Quantization for LLM Inference](cards-0002.md#paper-152092) | 分块分配精度以兼顾重要性和 GPU 规则访存 |
| 优化 | 基准审计 | [BO-Arena: An Evolving Benchmark for High-Dimensional Bayesian Optimisation](cards-0002.md#paper-138938) | 用公共实现和简单 GP 对照检验高维优化新方法 |
| 优化 | 稀疏决策 | [BONSAI: Bayesian Optimization with Natural Simplicity and Interpretability](cards-0002.md#paper-155059) | 在限制采集效用损失时尽量保留默认配置 |
| 大语言模型 | 递归推理 | [Boosting Inference with Guided Reasoning: Stochastic Exploration for Recursive Models](cards-0002.md#paper-149759) | 仅在停止头能区分好轨迹时用随机推理搜索 |
| 强化学习 | 经验回放 | [Boosting Multiagent Reinforcement Learning at High Replay Ratios with Ensemble Reset](cards-0002.md#paper-149143) | 高回放比下监控休眠神经元并周期重置价值集成 |
| 强化学习 | 经验回放 | [Boosting Off-Policy RLVR with Data-Centric Replay](cards-0002.md#paper-154959) | 控制轨迹陈旧度 |
| 强化学习 | 课程设计 | [Boost Reasoning Evolution via Responsive Rollout Difficulty Manipulation](cards-0002.md#paper-154872) | 按单题成功率调整提示长度 |
| Agent | 开发环境 | [BootstrapAgent: Turning Repository Setup into Reusable Agent Knowledge](cards-0002.md#paper-151994) | 把安装与诊断记录为可冷启动复验的契约 |
| 强化学习 | 生成策略 | [Bootstrapped Bipartite Actor-Critic for Diffusion RL](cards-0002.md#paper-155139) | 用动作Q差为成对偏好加权 |
| 表征学习 | 压缩评测 | [Bottleneck Benchmark: Sequence Compression Under Controlled Difficulty and Fixed Latent Size](cards-0002.md#paper-139737) | 固定潜变量尺寸再扫任务难度 |
| Agent | 工具链诊断 | [Boundary-Induced Forgetting in Large Language Model Tool Chains: Measuring Field-Routing Failures](cards-0002.md#paper-155598) | 按字段依赖测跨工具传播 |
| 表征学习 | 数据效率 | [Boundary Mass in Feature Space as a Label-Budget Diagnostic for Representations](cards-0002.md#paper-149689) | 测边界附近的特征质量判断标注需求 |
| 计算机视觉 | 渐进压缩 | [Bound-Conditioned Latent Inference for Progressive Image Compression](cards-0002.md#paper-149342) | 用已解码符号约束连续潜变量 |
| 计算成像 | 误差估计 | [Bounding Global and Local Compression Error of Signal Parameterizations](cards-0002.md#paper-148822) | 用不同压缩级预测之差估计误差 |
| 科学机器学习 | 外推诊断 | [Bounds on Extrapolation across Phase Transitions with Generalized Regression](cards-0002.md#paper-153578) | 用广义特征值问题估计跨相外推风险 |
| 大语言模型 | 量化微调 | [BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning](cards-0002.md#paper-149729) | 用二值适配器替代半精度适配器 |
| 多模态学习 | 缺失模态 | [BRACE: Bipolar Reference-Aware Calibration and Estimation for Incomplete Multimodal Learning](cards-0002.md#paper-150021) | 利用上下参考群判断修正方向 |
| 计算机视觉 | 生成 | [BRAVO: Bridge Matching for Autoregressive Video Generation](cards-0002.md#paper-148431) | 从上一帧出发学习相邻帧运输。 |
| 强化学习 | 信用分配 | [Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning](cards-0002.md#paper-150356) | 按对有效解集合的边际贡献分奖励。 |
| 语音识别 | 鲁棒微调 | [Breaking Adversarial Transferability in Fine-Tuned Speech Recognition](cards-0002.md#paper-153915) | 部署前验证公开底座的风险是否残留在微调模型。 |
| 联邦学习 | 鲁棒聚合 | [Breaking BAD: Heterogeneous Byzantine-Robust Federated Learning via Gather and Scatter Scores](cards-0002.md#paper-148208) | 同时检查更新的局部聚集与整体离散。 |
| 统计学习 | 信息估计 | [Breaking Curse of Dimensionality for Mutual Information Estimation with Vine Copulas](cards-0002.md#paper-154130) | 依赖复杂时比较藤 copula 与神经互信息估计。 |
| 深度学习 | 稀疏微调 | [Breaking Information Islands in Sparse Tuning via Small-World Connectivity](cards-0002.md#paper-155451) | 相同参数预算下改善跨块连接。 |
| 多模态学习 | 量化 | [Breaking Modality Heterogeneity in Low-Bit Quantization for Large Vision-Language Models](cards-0002.md#paper-153382) | 将模态特有的离群通道分开校准。 |
| 科学机器学习 | 数据增强 | [Breaking Noise Shortcuts in Self-Supervised Learning via Noise-Aligned View Generation](cards-0002.md#paper-153415) | 对同图的两个自监督视图重采样独立噪声。 |
| 强化学习 | 梯度估计 | [Breaking the Bias Barrier in Concave Multi-Objective Reinforcement Learning](cards-0002.md#paper-154531) | 检查效用平滑性后决定是否用多层蒙特卡洛。 |
| 推理系统 | 稀疏注意力 | [Breaking the Exactness Barrier: Interleaved DeepSeek Sparse Attention for Efficient Long Context Reasoning](cards-0002.md#paper-154778) | 按设备交错切分上下文并用放宽的局部排名替代精确全局排名。 |
| 强化学习 | 动作搜索 | [Breaking the Grid: Distance-Guided Reinforcement Learning in Large Discrete Action Spaces](cards-0002.md#paper-151813) | 按动作距离抽样邻域而非遍历整个动作空间。 |
| 多模态学习 | 时序信用分配 | [Breaking the Second Barrier: Sub-Second Timestamped Omni-Modal Captioning](cards-0002.md#paper-151142) | 分别给字幕结构片段分配语义与时间奖励。 |
| 生成模型 | 条件调度 | [Breaking the Static: Dynamic Text Conditioning for Diverse Image Generation](cards-0002.md#paper-152353) | 初段只保留低频语义，后段逐步恢复完整提示。 |
| 生成模型 | 专家路由 | [Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE](cards-0002.md#paper-152515) | 视频 MoE 给语义专家与通用专家分工，避免强制全局均匀路由。 |
| 训练系统 | 优化器量化 | [BReD: Block Replay Dithering for Stable Low-Bit EMA Optimizer States](cards-0002.md#paper-150618) | 为反复量化的 EMA 状态控制舍入偏差与方差。 |
| 优化 | 分布稳健训练 | [Brenier Meets Adversarial Training: Optimal Transport Geometry for Robust Learning](cards-0002.md#paper-152709) | 用运输映射的循环单调性检查分布鲁棒目标。 |
| 生成模型 | 结构化解码 | [BrickAnything: Geometry-Conditioned Buildable Brick Generation with Structure-Aware Tokenization](cards-0002.md#paper-154364) | 用局部连接树替代仅按空间坐标排列的生成序列。 |
| 计算机视觉 | 约束引导 | [BrickFlow: Connectivity-Guided Brick Reconstruction](cards-0002.md#paper-151991) | 推理时加解析连接场修正生成的部件位姿。 |
| 生成模型 | 训练前诊断 | [Bridge Graphical Models: Coupling, Projection, and Current-Preserving Dynamics for Generative Modeling](cards-0002.md#paper-148153) | 先用桥速度的条件方差筛选耦合，再投入长时间训练。 |
| 计算机视觉 | 深度融合 | [BridgeMVS: Bridging Multi-View Stereo and Monodepth via Bidirectional Dynamic Fusion](cards-0002.md#paper-151655) | 让单目先验和多视角几何双向校准并跨尺度传递。 |
| 生成模型 | 条件采样 | [BridgeTwist: Twisting Schrödinger Bridges for Training-Free Conditional Sampling](cards-0002.md#paper-151085) | 冻结桥生成器，以端点估计和退火重要性权重做条件采样。 |
| 多模态学习 | 测试时适配 | [Bridging CLIP with DINO: Cross-Modal Information Maximization for Online Test-Time Adaptation](cards-0002.md#paper-152887) | 将文本原型投影到冻结自监督视觉空间，并过滤不可靠样本梯度。 |
| 语言模型 | 缩放律 | [Bridging Compute- and Data-Optimal Pretraining](cards-0002.md#paper-155350) | 按新鲜数据约束分配训练预算 |
| 时间序列 | 生成架构 | [Bridging Diffusion and Autoregression for Flexible Time Series Synthesis](cards-0002.md#paper-155931) | 跨块自回归、块内联合去噪 |
| 计算机视觉 | 交替优化 | [Bridging Image Restoration and Recognition via Causal Mediated Unrolling](cards-0002.md#paper-153651) | 把识别信号和自然图像先验分步施加 |
| 多模态 Agent | 结构化记忆 | [Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning](cards-0002.md#paper-156072) | 长视频同时索引局部证据与跨时段叙事 |
| 强化学习 | 课程采样 | [Bridging Risk Approximation Gaps in Model Predictive Task Sampling via In-Context Modeling](cards-0002.md#paper-150549) | 按下一次策略更新后的难度选任务 |
| 自动驾驶 | 表征迁移 | [Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](cards-0002.md#paper-151833) | 将生成阶段学到的运动编码器与视觉编码器一同迁移 |
| 自动驾驶 | 域对齐 | [Bridging Simulation and Reality: Geometry and Decision Alignment for Autonomous Driving](cards-0002.md#paper-151850) | 同时检查几何对齐与策略行为对齐 |
| 多模态学习 | 可追溯监督 | [Bridging Structure and Language: Graph-Based Visual Reasoning for Autonomous Road Understanding](cards-0002.md#paper-151879) | 用可执行图查询生成有可验证落点的问答 |
| 语言模型 | 安全对齐 | [Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment](cards-0002.md#paper-149662) | 分开测风险判断与最终拒答 |
| 语言模型 | 缓存复用 | [Bridging the Gap: Position-Independent Cache Reuse for Hybrid SSM-Attention Architectures](cards-0002.md#paper-152513) | 统一混合注意力和状态空间层的跨位置缓存粒度 |
| 科学机器学习 | 分布校准 | [Bridging the Simulation-to-Experiment Gap with Adversarial Distribution Alignment](cards-0002.md#paper-151598) | 用真实部分观测校准完整仿真的生成模型 |
| 语言模型 | 稳健评测 | [Brittlebench: Quantifying LLM robustness via prompt sensitivity](cards-0002.md#paper-139284) | 以语义等价改写测试排行榜稳定性 |
| 优化 | 双层优化 | [BROS: Bias-Corrected Randomized Subspaces for Memory-Efficient Single-Loop Bilevel Optimization](cards-0002.md#paper-149705) | 用随机子空间估计 Hessian 作用节省内存 |
| 语言模型 | 安全优化 | [BSO: Safety Alignment Is Density Ratio Matching](cards-0002.md#paper-156078) | 把安全偏好优化定义成比率匹配 |
| 表格生成 | 分块扩散 | [BSTabDiff: Block-Subunit Diffusion Priors for High-Dimensional Tabular Data Generation](cards-0002.md#paper-151140) | 用块级潜变量替代高维联合密度建模。 |
| 联邦学习 | 隐私训练 | [Budget-Conditioned Clipping Policies for Differentially Private Federated Learning](cards-0002.md#paper-150613) | 在公开代理上学习预算与轮次到裁剪阈值的映射后冻结。 |
| 强化学习 | 离策略估计 | [Budgeted Multi-Source Counterfactual Annotation for Off-Policy Evaluation](cards-0002.md#paper-155643) | 按成本与误差分配有限的反事实标注。 |
| 深度学习 | 训练动力学 | [Bug or Feature$^2$: Weight Drift, Activation Sparsity, and Spikes](cards-0002.md#paper-149709) | 修改激活函数时同时监控稀疏度与异常尖峰。 |
| 图学习 | 双曲注意力 | [Busemannformer: Horospherical Self-Attention for Hyperbolic Graph Transformers](cards-0002.md#paper-151890) | 按任务对称性和标签的层级属性选几何打分。 |
| 可解释性 | 特征复现 | [Bypassing PC1 Makes SAEs More Reproducible](cards-0002.md#paper-156083) | 训练稀疏自编码器时旁路主成分再在推理加回。 |
| 语言模型 | 蒸馏 | [ByteDistill: Cross-Tokenizer Distillation via Chunk-wise Byte-Level Distribution Alignment](cards-0002.md#paper-149633) | 跨分词器时对齐下一个可观测字节的分布。 |
| 多模态学习 | 细粒度微调 | [C2FT: Enhancing Fine-Grained Perception in MLLMs via Confuse-then-Contrast Fine-Tuning](cards-0002.md#paper-151433) | 按目标模型的具体混淆组织多图对照监督。 |
| 智能体 | 角色记忆 | [C3: Long-Horizon Character Consistency via Causal-Continuous State Dynamics and Memory Rewriting](cards-0002.md#paper-151786) | 用连续状态和滞回更新角色，并按当前关系重释事件。 |
| 生成模型 | 数值采样 | [CAB: Accelerating Flow and Diffusion Sampling via Rectification and Corrected Adams-Bashforth](cards-0002.md#paper-150465) | 低步数采样时比较带历史速度校正的多步积分。 |
| 计算机视觉 | 奖励建模 | [CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](cards-0002.md#paper-153622) | 为视频奖励模型监督异常所在时间和空间。 |
| Agent | 缓存通信 | [CacheMAS: Cache Communication for Single-Pass, Jointly-Optimized Multi-Agent Systems](cards-0002.md#paper-154215) | 让多个角色通过预填充缓存共享状态，最终角色一次生成。 |
| 生成模型 | 推理缓存 | [Cache the Future: Training-Free Self-Revision for Diffusion Transformer Acceleration](cards-0002.md#paper-149314) | 用稀疏计算的后续状态修订此前跳过的时间步。 |
| 生成模型 | 覆盖诊断 | [CADMA: Capacity-Aware Recall Decomposition for Generative Model Assessment](cards-0002.md#paper-139801) | 用一对一局部分配评估生成分布的有效覆盖。 |
| 表格学习 | 特征构造 | [CAFE: Causally-Guided Automated Feature Engineering with Multi-Agent Reinforcement Learning](cards-0002.md#paper-151842) | 用软因果结构先验约束特征搜索，而非硬删除候选。 |
| 多模态学习 | 拓扑注意力 | [CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal Models](cards-0002.md#paper-151831) | 给多房间场景按物体和房间两层建立信息路径。 |
| 统计学习 | 校准评测 | [CalArena: A Large Scale Post-Hoc Calibration Benchmark](cards-0002.md#paper-139709) | 用恰当评分规则的改善度同时监测校准收益和预测质量。 |
| 统计学习 | 半监督估计 | [Calibeating Prediction-Powered Inference](cards-0002.md#paper-150100) | 先用小标注集校准预测分数，再用全量协变量估计均值。 |
| 强化学习 | 安全策略改进 | [Calibrated Safe Policy Improvement for Continuous Offline Reinforcement Learning](cards-0002.md#paper-148367) | 用校准的一步模型误差证书限制连续域搜索。 |
| 优化 | 曲率估计 | [Calibrated Target Noise Recovers Curvature from the Gradients](cards-0002.md#paper-154444) | 只有批梯度时用校准目标扰动估计曲率。 |
| 大语言模型 | 语义校准 | [Calibrating LLMs with Semantic-level Reward](cards-0002.md#paper-154784) | 通过答案语义一致性训练校准，减少置信度措辞影响。 |
| Agent | 干预决策 | [Calibration Is Not Control: Intervention Advantage for LLM-Agent Oversight](cards-0002.md#paper-149357) | 从同一轨迹前缀比较继续和采取干预的预期效用。 |
| 统计学习 | 无标签校准 | [Calibration without Ground Truth](cards-0002.md#paper-152525) | 检查主模型和参考模型是否相互可校准，再决定是否转移校准信息。 |
| 多模态 | 记忆机制 | [CAM: Question Answering on Entity-Centric Videos with Continuous Extraction and Adaptive Querying](cards-0002.md#paper-150537) | 将实体级长期摘要和按问题回查原始视频结合 |
| 视觉 | 记忆评测 | [Can 4D Foundation Models Remember?](cards-0002.md#paper-139573) | 用全景参考评估物体离开视野后的记忆 |
| 学习理论 | 鲁棒评测 | [Can Circuit Alignment Predict OOD Generalization?](cards-0002.md#paper-155822) | 用计算路径对齐而非仅激活相似度估计跨域性能 |
| 优化 | 梯度估计 | [Can Entry-Wise Clipping Give Spectral Control of Stochastic Gradients?](cards-0002.md#paper-154679) | 梯度噪声重尾时试验逐元素平滑收缩 |
| 系统 | 并行规划 | [Can Hybrid-Parallel Planning Support Alternating Model–Strategy Design? Dependency-Keyed Per-Layer Primitives for Re-Planning](cards-0002.md#paper-149399) | 并行策略重算时仅复用依赖签名一致的层级原语 |
| 强化学习 | 探索奖励 | [Can In-Context Learning Support Intrinsic Curiosity?](cards-0002.md#paper-151481) | 按任务是否有时间依赖决定用上下文预测误差近似学习进展 |
| 大语言模型 | 长上下文 | [Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale](cards-0002.md#paper-153028) | 百万 token 检索单独诊断注意力归一化稀释 |
| 可解释性 | 行为诊断 | [Can LLMs explain themselves truthfully with code?](cards-0002.md#paper-150242) | 用留出输入上的行为一致性验证自解释。 |
| 统计学习 | 多源校准 | [Can Metadata Fix the Gauge? Calibration Turns Sparse Multi-Source Learning from Sparse PCA into Sparse Mean Recovery](cards-0002.md#paper-152833) | 优先采集可验证的相对坐标信息，再合并来源。 |
| 学习理论 | 条件预测 | [Canonical Predictive Quotients: A Theory of Prediction under Hidden Predictive State Uncertainty with ICL Implications](cards-0002.md#paper-154631) | 只恢复会改变当前最优预测的隐状态区别。 |
| 机器学习系统 | 推理调度 | [Canopy: Tree-Aware Rollout Scheduling for Agent Reinforcement Learning](cards-0002.md#paper-154204) | 把 rollout 树结构传给调度与 KV 缓存管理。 |
| 多模态学习 | 反事实评测 | [Can the Parts Fool the Test? Counterfactual Pairing Cycles for Relational OOD](cards-0002.md#paper-149781) | 保持图和文字成分不变，仅更换配对测试关系绑定。 |
| 视频生成 | 采样调度 | [CanvasMAR: Improving Masked Autoregressive Video Prediction With Canvas](cards-0002.md#paper-148170) | 先提供全局未来帧粗预测，再逐区补细节。 |
| 计算机视觉 | 主动感知 | [CanViT: Toward Active-Vision Foundation Models](cards-0002.md#paper-151128) | 将局部感知骨干与可持续更新的场景记忆分离。 |
| 具身智能 | 安全评测 | [Can VLMs Reason When to Stop for Human Safety?](cards-0002.md#paper-139187) | 对同一任务构造应停止和可继续的配对场景。 |
| 统计学习 | 评测诊断 | [Can We Trust Item Response Theory for AI Evaluation?](cards-0002.md#paper-139287) | 使用 IRT 前按模型数量和能力分布做仿真校准。 |
| 大语言模型 | 知识编辑 | [Capacity Allocation at the Source: Sparse Target Optimization for LLM Knowledge Editing](cards-0002.md#paper-148802) | 在求目标隐态时约束稀疏度，减少多次编辑干扰。 |
| 优化 | 延迟反馈 | [Capacity-Constrained Online Convex Optimization with Delayed Feedback](cards-0002.md#paper-151561) | 用随机调度和重要性权重管理有限反馈追踪预算。 |
| 自然语言处理 | 过程监督 | [CAPER: Clause-Aligned Process Supervision for Text-to-SQL](cards-0002.md#paper-149623) | 将 SQL 语义子句作为奖励和故障定位单元。 |
| Agent | 约束优化 | [CAPO: A Primal-Dual Framework for Constraint-Aware Prompt Optimization](cards-0002.md#paper-149769) | 为工具使用和输出要求设显式阈值后优化系统提示。 |
| 大语言模型 | 遗忘评测 | [CapTrack: Multifaceted Evaluation of Forgetting in LLM Post-Training](cards-0002.md#paper-138881) | 按能力拆分后训练漂移 |
| 大语言模型 | 上下文蒸馏 | [Capturing In-Context Learning Dynamics with Task Operators](cards-0002.md#paper-149094) | 用输入相关算子代替固定任务向量 |
| 大语言模型 | 能力评测 | [Capturing LLM Capabilities via Evidence-Calibrated Query Clustering](cards-0002.md#paper-148906) | 按模型表现校准语义聚类 |
| 推荐系统 | 多关系损失 | [Cardinality-Decomposed Loss for Heterogeneous GNNs](cards-0002.md#paper-150315) | 按关系基数配置训练损失 |
| Agent | 强化学习 | [CARD: Internalizing Expert Critique into Reinforcement Learning for Deep Search](cards-0002.md#paper-152838) | 对被反馈真正改写的步骤提高权重 |
| 计算机视觉 | 反事实评测 | [CARVE: Counterfactual Video Editing for Auditing and Hardening Video Detectors](cards-0002.md#paper-151526) | 正交干预环境和事件来诊断检测捷径 |
| 优化 | 泛化正则 | [CASAM: Consistency-Anchored Sharpness-Aware Minimization for Improved Model Generalization](cards-0002.md#paper-152013) | 用样本与批梯度的一致性分配训练权重 |
| 多模态学习 | 解释性 | [Cascaded Sparse Autoencoders LearnMulti-Level Visual Concepts in Multimodal LLMs](cards-0002.md#paper-151133) | 用特征字典训练上层稀疏编码器 |
| 神经符号学习 | 约束投影 | [Casper: A Projection-Based Neurosymbolic Layer for Scalable & Guaranteed Constraint Satisfaction](cards-0002.md#paper-149782) | 把可行性作为可微输出层 |
| Agent | 防御监测 | [CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring](cards-0002.md#paper-150932) | 合并多渠道信号识别异常传播 |
| 时间序列 | 分布预测 | [CAST: Causal Anchored Simplex Transport for Distribution-Valued Time Series](cards-0002.md#paper-155150) | 用上下文区分同状态下的不同转移规律 |
| 强化学习 | 稳健迁移 | [CAST: Certifiable Aggregation of Smoothed Teachers for Robust Policy Adaptation](cards-0002.md#paper-151249) | 聚合带证书的源策略并复查目标侧保证 |
| 多模态学习 | 能力诊断 | [Castle-in-the-Air: Probing the Foundational Visual Deficits of MLLMs via Bottom-Up Cognitive Factors](cards-0002.md#paper-139489) | 在高层问答之外测可控难度的基础视觉 |
| 语言模型 | 自适应计算 | [Catch Your Breath: Adaptive Computation for Self-Paced Sequence Production](cards-0002.md#paper-152630) | 让模型学习何时暂停和继续 |
| 多模态学习 | 推理加速 | [CATS: Acceptance-Oriented Critical Token Adaptive Selection for Multimodal Speculative Decoding](cards-0002.md#paper-154883) | 优先对齐视觉依赖或高拒绝率 token |
| 计算机视觉 | 可解释性 | [Causal Attribution via Activation Patching](cards-0002.md#paper-155095) | 在中间层直接检验图块表征贡献 |
| 计算机视觉 | 记忆路由 | [CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives](cards-0002.md#paper-154338) | 跨镜头视频按内容相关性选缓存 |
| 因果学习 | 鲁棒评测 | [CausalCompass: Evaluating the Robustness of  Time-Series Causal Discovery in Misspecified Scenarios](cards-0002.md#paper-139526) | 把标准化与假设违背分别做对照 |
