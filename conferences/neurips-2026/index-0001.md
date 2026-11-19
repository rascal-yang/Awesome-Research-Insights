# NeurIPS 2026 论文索引 · 第 1 卷

[会议首页](README.md)

| 领域 | 技术类型 | 论文卡 | 能改变的技术选择 |
| --- | --- | --- | --- |
| 强化学习 / 学习理论 | 离线决策 | [Fast Rates for Offline Contextual Bandits with Forward-KL Regularization under Single-Policy Concentrability](cards.md#paper-tdl6qleloi) | 在日志覆盖有限时，根据正则强度判断前向 KL 的样本复杂度是否进入快率区间。 |
| 大语言模型 | 激活量化 | [ConQuR: Corner Aligned Activation Quantization via Optimized Rotations for LLMs](cards.md#paper-151137) | 按激活方向校准正交旋转，降低低比特误差和校准成本。 |
| 大语言模型 / 推理 | 推理预算 | [Confidence-Calibrated Inference Expansion for Evaluator-Guided Test-Time Reasoning](cards.md#paper-155179) | 分别校准接受、回退和扩展后的成功概率，再按净收益分配算力。 |
| Agent | 经验记忆 | [MAGE: Multi-Agent Self-Evolution with Co-Evolutionary Knowledge Graphs](cards.md#paper-150998) | 分别检索成功推理和失败纠正，使冻结执行模型随经验增长改进。 |
| Agent | 记忆评测 | [MemContract: Contract-Sensitive Evaluation for Mutable Agent Memory](cards.md#paper-154728) | 比较记忆后端时单测修订、弃用、擦除和来源追踪。 |
| 大语言模型 / 学习架构 | 空间记忆 | [DeltaFugue: Orchestrating Spatial and Associative Memory for Algorithmic Length Generalization](cards.md#paper-148950) | 将位置敏感的长程结构交给可寻址空间带，而非继续压缩进固定关联状态。 |
| 多模态学习 | 分布对齐 | [Beyond Pairwise Supervision: Spectral Characteristic Matching for Data-Efficient Multimodal Alignment](cards.md#paper-153322) | 配对很少时同时优化点对点目标与跨模态分布差异。 |
| 多模态学习 | 梯度路由 | [GEAR-Align: Grounding-Evidence-Aware Gradient Routing for Multimodal Alignment](cards.md#paper-153068) | 按答案 token 对视觉的依赖程度分配梯度。 |
| 多模态学习 | 无监督对齐 | [RankAlign: Unsupervised Vision-Language Representation Alignment via Rank Transformation](cards.md#paper-149742) | 无配对对齐时比较绝对相似度和模态内部邻居排序。 |
| 科学机器学习 | 成本评测 | [Breakeven complexity: A new perspective on neural partial differential equation solvers](cards.md#paper-148644) | 按同误差的数值解算器计算盈亏平衡求解次数。 |
| 科学机器学习 | 归因诊断 | [Explanation of Dynamic Physical Field Predictions using WassersteinGrad: Application to Autoregressive Weather Forecasting](cards.md#paper-151943) | 归因误差主要是空间错位时使用几何重心。 |
| 科学机器学习 | 时序算子 | [Learning Spectral Compositional Koopman Operators for Global-to-Regional Weather Forecasting](cards.md#paper-153842) | 长程预报先诊断消息传递引起的频谱平滑。 |
| 强化学习 / 优化 | 部分反馈学习 | [Online Decision-Focused Learning under Semi-Bandit Feedback](cards.md#paper-150539) | 用未观测代价补全候选决策，但只用实测组件更新表征。 |
| 大语言模型 | 异步蒸馏 | [$\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control](cards.md#paper-150017) | 按样本新鲜度调节异步蒸馏 |
| 强化学习 / 理论 | 树搜索 | [$\epsilon$-Good Action Identification in Fixed-Budget Monte Carlo Tree Search](cards.md#paper-152538) | 固定预算下以近优识别率衡量采样 |
| 大语言模型 | 奖励对齐 | [$f$-GRPO & Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment](cards.md#paper-153358) | 以组内相对奖励划分对齐样本并选择散度 |
| 计算机视觉 | 条件生成 | [$h$-control: Training-Free Camera Control via Block-Conditional Gibbs Refinement](cards.md#paper-155968) | 按同噪声级细化未观测区域 |
| 学习理论 / 可解释性 | 因果评测 | [$\mathrm{Bounded\mbox{-}RS}$: A Bounded Evaluation Protocol and Testbed for Representational Systematicity](cards.md#paper-139441) | 把可解码性与生成过程实际使用分开检验。 |
| 具身智能 / 多模态 | 感知监督 | [$\text{A}^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation](cards.md#paper-155296) | 从操作引起的画面变化离线构造目标区域监督。 |
| 学习理论 / 视觉 | 不变表征 | [$\texttt{bispectrum}$: Selective $G$-Bispectra Made Practical](cards.md#paper-148783) | 在已知对称群的任务中测试选择性双谱池化。 |
| 强化学习 | 回报分布 | [$\varphi$TD: Distributional Reinforcement Learning using Characteristic Functions](cards.md#paper-154745) | 需要连续多峰回报时用特征函数损失。 |
| 因果学习 | 决策支持 | [2-Step Agent: How a Bayesian Decision Maker Learns from AI-Decision Support](cards.md#paper-150442) | 评估模型辅助时扫描用户先验与真实参数的错配。 |
| 多模态 / Agent | 模仿重加权 | [3A-VLA: Abstraction-Aligned Action Learning for Vision-Language Agents in 3D Game Worlds](cards.md#paper-153557) | 用意图和环境可供性一致程度调节示范损失。 |
| 计算机视觉 | 多视图对齐 | [3D Consistency Tokens](cards.md#paper-152512) | 将跨视图匹配建立在共享三维位置上。 |
| 多模态学习 | 部件表征 | [3D-PLOT-LLM: Part-Level Object Tokens for 3D Large Language Models](cards.md#paper-148954) | 用可引用词表槽位把部件作为语言模型输入和输出中的实体。 |
| 计算机视觉 / 雷达 | 物理渲染 | [3D Point Splatting for mmWave Radar Novel View Synthesis](cards.md#paper-151080) | 保留复相位再派生雷达产品 |
| 计算机视觉 | 三维表示 | [3D Skew Normal Splatting](cards.md#paper-152761) | 在非对称边界用可学习偏斜原语 |
| 计算机视觉 | 视频评测 | [3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](cards.md#paper-153051) | 用含语义的三维轨迹重建评估视频物理一致性 |
| 计算机视觉 | 数据增强 | [3D-VITAL: Visibility-aware Identity Training from Artificial Liftings of 3D Reconstruction model for Cross-View Object Re-Identification](cards.md#paper-150244) | 将合成新视角的真实可见部分与幻觉纹理区分 |
| 优化 | 聚类算法 | [A Batched Hartigan's $k$-Means Clustering](cards.md#paper-148581) | 以安全独立性筛选可并行坐标更新 |
| 大语言模型 | 偏好学习 | [ABC-Align: Prediction-Powered Alignment with Adaptive Bias Control](cards.md#paper-148310) | 按偏差与方差动态调节人工纠偏强度 |
| 生成建模 | 时空建模 | [ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](cards.md#paper-150308) | 把扩散推进时间与物理时间对齐 |
| 大语言模型 | 数据策略 | [A Bitter Lesson for Data Filtering](cards.md#paper-155947) | 在高算力且数据稀缺时，把不过滤作为等预算预训练对照。 |
| 统计学习 | 在线校准 | [A Black-Box Reduction from Regret to Multi-Level Coverage](cards.md#paper-154233) | 用在线算法的线性化遗憾控制多级覆盖。 |
| 强化学习 | 约束优化 | [Absolute State-wise Constrained Policy Optimization: High-Probability State-wise Constraints Satisfaction](cards.md#paper-149439) | 监控整条轨迹的瞬时成本最大值。 |
| 计算机视觉 | 推理剪枝 | [Accelerated Image Editing via Consistency-Aware Source Token Pruning](cards.md#paper-149846) | 用显式采样修正替代部分源图注意力。 |
| 优化 | 极小极大优化 | [Accelerated last-iterate convergence of Extragradient via power-law stepsizes](cards.md#paper-155893) | 将外推与更新步长解耦。 |
| 生成模型 | 并行解码 | [Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding](cards.md#paper-156738) | 按层依赖冗余选择 Jacobi 解码。 |
| 优化 | 预训练优化 | [Accelerating LLM Pre-Training through Flat-Direction Dynamics Enhancement](cards.md#paper-150025) | 对曲率较平的方向分配更激进更新。 |
| 优化 | 训练动力学 | [Accelerating Neural Network Training with Augmented Koopman Dynamics](cards.md#paper-149064) | 同时外推参数和优化器内部状态。 |
| 生成模型 | 推理缓存 | [Accelerating Rectified Flow Models  via Trajectory-Aware Caching](cards.md#paper-151611) | 分别追踪流速度的大小偏差和方向偏差。 |
| 强化学习 | 并行约束学习 | [Accelerating Safe Reinforcement Learning with Massive Parallelism](cards.md#paper-153909) | 按回合相位重建成本而非直接平均短滚动。 |
| 计算机视觉 | 视频反演 | [Accelerating Video Inverse Problem Solvers with Autoregressive Diffusion Models](cards.md#paper-151472) | 用测量一致初值启动流式逆扩散。 |
| 机器学习系统 | 评测与诊断 | [AccelEval: A Whole-Program Benchmark for LLM-Generated CPU-to-GPU Code Acceleration](cards.md#paper-139678) | 用端到端正确性和同任务性能上限评估 GPU 代码生成。 |
| 高效训练 | 稀疏重连 | [AC/DC on a Budget -- Alternating Sparse Phases](cards.md#paper-149303) | 以掩码收敛终止稠密阶段或直接进行稀疏重连 |
| 计算机视觉 | 三维重建 | [ACD-GS: Asymmetric Curvature-aware Densification for 3D Gaussian Splatting](cards.md#paper-150094) | 按深度曲率决定高斯克隆与分裂 |
| Agent | 因果评测 | [ACED-Bench: Evaluating How LLM Agents Acquire and Act on Causal Evidence](cards.md#paper-154560) | 用形式化世界检验智能体选实验、保留证据及停止的能力 |
| 优化 | 非光滑优化 | [Achieving Directional-Stationarity from a Single Random Direction Step](cards.md#paper-149362) | 用一次随机方向探索增强现有优化法的方向驻点保证 |
| 多模态学习 | 时序结构评测 | [A Closer Look at Dynamic Scene Graph Generation in the Era of Multimodal Large Language Models](cards.md#paper-151784) | 动态场景图同时测关系精度、信息量与重复 |
| Agent | 预算路由 | [A Communication-Theoretic Framework for LLM Agents: Cost-Aware Adaptive Reliability](cards.md#paper-150815) | 按任务难度决定重试、投票或迭代验证的预算 |
| 训练数据 | 在线选样 | [A Compass for Useful Data: Online Data Selection via Alignment-Gated Fisher Geometry](cards.md#paper-155971) | 结合更新效用、下降方向和批内互补性来分配训练预算 |
| 学习理论 | 稳健公平性 | [A Comprehensive View of Fairness through Distributional Stability](cards.md#paper-153293) | 在多种人群配比下联合报告公平性而非单一测试分布 |
| 训练数据 | 消融预算 | [A Computational Perspective to Data Ablation Experiments](cards.md#paper-155175) | 固定算力时联合分配数据配方搜索与最终训练预算 |
| 多模态 | 评测 | [AcousticBench: Measuring Acoustic Perception in Large Audio Language Models](cards.md#paper-139542) | 用无词汇声学对照隔离听觉能力 |
| 多模态 | 评测 | [Acting without Knowing: Planning, Prediction, and Transfer Dissociate in Interactive Visual Physics](cards.md#paper-139556) | 同一场景分别测行动、预测和迁移 |
| 强化学习 | 动作分块 | [Action Chunking Proximal Policy Optimization with Feedback Correction](cards.md#paper-154625) | 用标准状态价值并在块内闭环纠偏 |
| 强化学习 | 方差控制 | [Action-Level Behavior Policy Optimization for Variance-Reduced Policy Gradients](cards.md#paper-153538) | 固定状态分布后改行动提议分布 |
| 学习理论 | 抽样设计 | [Active Context Selection Improves Simple Regret in Contextual Bandits](cards.md#paper-151058) | 主动抽样按目标人群权重的三分之二次幂分配 |
| Agent | 行为评测 | [Active Probabilistic Reasoning in Humans and LLMs](cards.md#paper-149573) | 分别测证据收集与证据整合 |
| 具身智能 | 量化 | [ActQuant: Sub-4-bit Action-Guided Quantization for Vision-Language-Action Models](cards.md#paper-155159) | 按动作敏感度分配位宽和张量内尺度 |
| 因果学习 | 闭环辨识 | [Act, Validate, Adapt: Closing the Causal Discovery-Control Loop](cards.md#paper-153013) | 用干预验证图结构而非只重新拟合系数 |
| 多模态 | 视频编码 | [AdaCodec: A Predictive Visual Code for Video MLLMs](cards.md#paper-148821) | 用关键帧和预测残差取代重复编码邻帧 |
| Agent | 策略学习 | [AdaMAP: Learning Adaptive Multi-Action Prediction with Grounded Dreaming Guidance](cards.md#paper-155834) | 让动作块自行决定何时重新观察 |
| 优化 | 收敛分析 | [Adam under Generalized Smoothness with Second-Moment-Type Stochastic Gradients](cards.md#paper-151271) | 检查随机梯度二阶矩与自归一化而非先假设轻尾 |
| 具身智能 | 三维感知 | [AdaOcc: Adaptive 3D Occupancy Prediction for Embodied Tasks](cards.md#paper-152734) | 以渐进查询数量调节占据预测预算 |
| 语言模型 | 低秩适配 | [AdaPaD: Adaptive Parallel Deflation for PEFT with Self-Correcting Rank Discovery](cards.md#paper-153769) | 并行修正低秩分量并按重要性增长模块秩 |
| 机器学习 | 半监督学习 | [AdapMatch: Adaptive Bias Decoupling for Semi-Supervised Partial Label Learning under Unknown Class Distributions](cards.md#paper-150939) | 分别监控伪标签入选偏差与候选集消歧偏差 |
| 优化 | 低秩适配 | [AdaPreLoRA: Adafactor Preconditioned Low-Rank Adaptation](cards.md#paper-155053) | 选择可逆的因子空间预条件近似 |
| 优化 | 进化策略 | [Adaptive and Neutral Theory of Evolution Strategies for Large Language Models](cards.md#paper-151417) | 分阶段评估归一化进化策略的收益与遗忘 |
| 机器学习 | 统计审计 | [Adaptive auditing of AI systems with anytime-valid guarantees](cards.md#paper-154700) | 让中途决定采样和停测仍支持有效检验 |
| 学习理论 | 校准 | [Adaptive Calibration in Non-Stationary Environments](cards.md#paper-151966) | 使误校准上界随环境漂移而变 |
| 强化学习 | 多智能体通信 | [Adaptive Communication Range for Scalable Cooperative Multi-Agent Reinforcement Learning](cards.md#paper-149196) | 先预算内选通信范围再基于实际邻域行动 |
| 优化 | 投影无关优化 | [Adaptive Conditional Gradient Sliding: Projection-Free and Line-Search-Free Acceleration](cards.md#paper-148937) | 外层梯度复用多次线性预言机调用 |
| 科学机器学习 | 神经算子 | [Adaptive Coordinate Transforms for Neural Operators](cards.md#paper-156121) | 根据特征变换坐标后再做算子计算 |
| 系统 | 资源调度 | [Adaptive Fine-Tuning Scheduler for Multi-Tenant Edge LLM via Convergence-Aware Bandits](cards.md#paper-153654) | 减少给已收敛适配器分配更新 |
| 语言模型 | 推理搜索 | [Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification](cards.md#paper-152362) | 按便宜评分的条件成功率决定是否付费核验 |
| 多模态 | 动态读出 | [Adaptive Internal Readout for Native Multimodal Models](cards.md#paper-152986) | 固定读出预算比较内部位点与末层 |
| Agent | 模型路由 | [Adaptive LLM Routing for Multi-Turn Conversations with Continuously Evolving User Queries](cards.md#paper-152859) | 用多轮累计奖励生成路由监督，在线以轻量模型替代搜索。 |
| 优化 | 零阶优化 | [Adaptively Incorporating Directional Hints into Zeroth-Order Optimization](cards.md#paper-149625) | 让不可靠梯度提示作为降方差项，对照强制沿提示更新。 |
| 科学机器学习 | 几何表征 | [Adaptive Multi-Frame Learning for Expressive and Stable Atomic Representations](cards.md#paper-152306) | 把几何参考的质量作为聚合输入，并在高对称区域专门测稳定性。 |
| 科学机器学习 | 神经算子 | [Adaptive multiscale operator correction via learned spectral subspace and physics-informed optimization.](cards.md#paper-149265) | 冻结粗算子后只在稀疏谱子空间做物理校正。 |
| 大语言模型 | 奖励鲁棒化 | [Adaptive Robust Estimator for Policy Optimization in Reinforcement Learning](cards.md#paper-153985) | 通过奖励污染扫描比较稳健中心与样本均值。 |
| 强化学习 | 资格迹 | [Adaptive Stepsizes for Eligibility Traces in Deep Reinforcement Learning](cards.md#paper-153394) | 改变资格迹中的学习率前先核对前后向等价条件。 |
| 统计学习 | 不确定性校准 | [AdaptNC: Adaptive Nonconformity Scores for Conformal Prediction under Distribution Shift](cards.md#paper-150536) | 同时更新预测集合形状与大小，并专门测切换期覆盖。 |
| 生成模型 | 流式视频 | [AdaState: Self-Evolving Anchors for Streaming Video Generation](cards.md#paper-150868) | 对比固定视觉锚与可演进锚，并同时测运动和身份漂移。 |
| 世界模型 | 少样本适配 | [AdaWM: Few-Shot Adaptation of World Models to Unseen Dynamical Regimes](cards.md#paper-151941) | 先测试按转移示例条件化，再决定是否扩大容量或微调。 |
| 世界模型 | 记忆寻址 | [Addressable Memory for Video World Models](cards.md#paper-152426) | 将缓存保留内容与位置编码分别做干预。 |
| 多智能体学习 | 奖励塑形 | [Addressing Exogenous Variability in Cooperative Multi-Agent Reinforcement Learning](cards.md#paper-149019) | 区分直接控制变量与间接影响变量后再给奖励塑形。 |
| 强化学习 | 探索技能 | [Addressing Sparse-Rewards in RL with Scalable Hierarchical Novel Eigen Options](cards.md#paper-150071) | 用访问稀少程度塑造可扩展的时序探索选项。 |
| 机器学习系统 | 无损通信 | [AdERA: Adaptive Exponent Reuse for Lossless Allgather in Sharded MoE Training](cards.md#paper-152302) | 先量化跨步指数重复率，再按每层通信收益选择是否压缩。 |
| 多智能体学习 | 协作评测 | [Ad-Hoc Teamwork from Human Demonstrations](cards.md#paper-148597) | 用多个潜惯例构造评测队友，检查单一代理下的排序是否稳定。 |
| 三维视觉 | 图监督 | [A Differentiable 3D Scene Graph Metric via Contextual Hellinger Triplet Geometry](cards.md#paper-149490) | 在训练中计量关系结构偏差 |
| 优化 | 可微求解 | [A Differentiable Interior-Point Method in Single Precision](cards.md#paper-151819) | 低精度求解时改变互补条件表示 |
| Agent | 记忆审计 | [ADMIT: Support-Gated Memory-Write Admission for Document QA Agents](cards.md#paper-155533) | 审计写入与最终回答两个界面 |
| 生成模型 | 训练加速 | [Advanced Routing as Regularization Allocation for Efficient Diffusion Transformer Training](cards.md#paper-152568) | 按去噪噪声级分配 token 跳层 |
| 强化学习 | 信用分配 | [Advancing Entropy-Level Credit Assignment in RLVR via Proximal Entropy Policy Optimization](cards.md#paper-150862) | 用局部熵而非全局熵给 token 分配优势 |
| 科学机器学习 | 神经算子 | [Advectra: Asymmetric Latent Transport for Non-Stationary Physics](cards.md#paper-148631) | 在随流坐标系中编码平流场 |
| 强化学习 | 公平评测 | [Adversarial Group Fairness in Contextual Bandits: When Robust is Not Fair](cards.md#paper-152720) | 独立监测群体遗憾与整体指标 |
| 学习理论 | 循环策略 | [A dynamical systems theory of reward-modulated learning in linear recurrent networks](cards.md#paper-151421) | 按任务时域选循环规模 |
| 强化学习 | 离线安全 | [AEGIS: Almost Surely Safe Offline Reinforcement Learning](cards.md#paper-152975) | 让同一策略消费多种可行安全预算 |
| 生成模型 | 路径约束 | [AegisFlow: Training-free Non-myopic Path-safe Guided Flow Matching](cards.md#paper-149715) | 在全轨迹目标中加入时变屏障 |
| 计算机视觉 | 动态世界模型 | [AEON: Unifying Video and 3D World Models](cards.md#paper-148481) | 让视频生成潜变量输出持久可渲染三维状态 |
| 科学机器学习 | 诊断评测 | [AET-Bench: Pixel-Accurate Atomic Tomography Is Not Atom-Accurate](cards.md#paper-139587) | 以原子召回等任务指标选断层重建模型 |
| 强化学习 | 多目标优化 | [AETDICE: Unified Framework and Offline Optimization for Nonlinear Multi-Objective RL](cards.md#paper-150928) | 显式区分聚合、期望和变换的顺序 |
| 生成模型 | 采样 | [A Favorable Regime Between ODE and SDE for Few-Step Diffusion Sampling](cards.md#paper-152991) | 少步生成选择有界且中等扩散强度的驱动 |
| 大语言模型 / Agent | 示范采样 | [A Few Teacher Steps Go a Long Way: Cost-Efficient On-Policy Data Augmentation for Agent Post-Training](cards.md#paper-150832) | 在学生到达的状态采样短教师续写。 |
| 模型可靠性 | 形式化验证 | [Affine-Image Propagation for Tight and Scalable $\ell_{2}$ Neural Network Verification](cards.md#paper-150286) | 在层间传播仿射几何，减少欧氏扰动集放松带来的损失。 |
| 自动机器学习 | 架构搜索 | [Agentic Neural Architecture Search](cards.md#paper-154949) | 让语言模型输出可替换模块槽，再由搜索算法局部优化。 |
| 大语言模型 / Agent | 推理缓存 | [AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems](cards.md#paper-155404) | 按结构化记忆单元校正复用的 KV 缓存。 |
| 机器人学 | 数据生成 | [AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation](cards.md#paper-139222) | 按后续动作需要的接触区域采样抓取。 |
| 大语言模型 | 剪枝重建 | [A Free Lunch in LLM Compression: Revisiting Retraining after Pruning](cards.md#paper-150765) | 重建窗口至少覆盖一个非线性子模块。 |
| 多模态学习 | 表征解释 | [A General Concept-based Decomposition for Vision–Language Embeddings](cards.md#paper-151861) | 以样本间关系监督概念分解。 |
| Agent | 训练反馈 | [Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback](cards.md#paper-155447) | 以交互式执行验证生成的符号世界模型。 |
| Agent | 拒绝评测 | [AgentAbstain: Do LLM Agents Know When Not to Act?](cards.md#paper-139558) | 构造同任务的应执行与应拒绝成对变体。 |
| Agent / 评测 | 过程诊断 | [AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation](cards.md#paper-138951) | 将测试通过率与轨迹质量分开 |
| Agent / 安全 | 故障评测 | [Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents](cards.md#paper-151325) | 把普通环境故障纳入安全回归 |
| Agent / 可靠性 | 故障归因 | [AgenTracer-v2: Agentic Failure Tracer for LLM Agentic Systems](cards.md#paper-153890) | 对超长日志进行主动检索和分步归因 |
| 软件工程 | 静态分析 | [Agents as Neuro-Symbolic Reasoners: Path Feasibility Reasoning for Precise Static Bug Detection](cards.md#paper-153256) | 以局部符号推理验证静态告警 |
| Agent / 机器学习 | 半监督搜索 | [AgentSSL: Can MLE Agents Leverage Unlabeled Data?](cards.md#paper-154115) | 在标签不足时单测 Agent 能否利用无标签数据 |
| Agent / 系统 | 推理调度 | [AgentWeave: Efficient Distributed Agent Serving via Flow Decomposition](cards.md#paper-151244) | 按工作流模块区分流水气泡与请求阻塞 |
| 图机器学习 | 表征诊断 | [Aggregation Dispersion: An Information-Geometric Diagnostic of Oversmoothing in Graph Neural Networks](cards.md#paper-154195) | 用传播分布的几何离散度测过平滑 |
| 强化学习 | 多智能体激励 | [AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games](cards.md#paper-154175) | 允许按状态拒绝部分转移奖励 |
| 机器学习评测 | 选择偏差 | [Agreement without Coverage: Conditional Agreement is Non-Identifying in Variable-Support Structured Extraction](cards.md#paper-152893) | 一致率同时报告覆盖、召回与输出规模 |
| 世界模型 | 分层预测 | [A Hierarchical World Model for Driving](cards.md#paper-151694) | 用长时粗语义预测约束短时细节 |
| 机器学习 | 不确定性归因 | [A Hierarchy of Entropy-Shapley Games for Multivariate Predictive Uncertainty](cards.md#paper-153980) | 对边缘不确定性和依赖结构分别归因 |
| 计算机视觉 / 数据策略 | 主动学习 | [Active Learning as Nullspace Regulation: A Spectral Representation Perspective](cards.md#paper-152553) | 选择跨轮次仍处在标注表示弱覆盖方向的样本。 |
| 大语言模型 | 稀疏推理 | [AdaCal: Adaptive Calibration for Robust Sparse Attention in Long-Context LLMs](cards.md#paper-155964) | 用轻量探针决定哪些注意力头需要补充远距离覆盖。 |
| 大语言模型 | 量化 | [ACQueReLlo: Alignment-Aware Constrained Quantization via Reinforcement Learning for Large Language Models](cards.md#paper-154964) | 选择混合位宽时同时约束能力、拒答与误拒。 |
| Agent | 错误定位 | [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](cards.md#paper-155358) | 用并行小型诊断头输出错误位置及原因以支持执行前纠偏。 |
| 具身智能 | 动作表示 | [Action Images: End-to-End Policy Learning via Multiview Video Generation](cards.md#paper-150968) | 把控制轨迹渲染为多视角动作图像，使视频骨干直接预测控制。 |
| 生成模型 | 安全控制 | [Activation Steering of Video Generation Models via Reduced-Order Linear Optimal Control](cards.md#paper-150198) | 按生成过程的反馈约束干预幅度，兼顾内容安全与视频质量。 |
| 计算成像 | 压缩感知 | [Active Learning for Conditional Generative Compressed Sensing](cards.md#paper-149778) | 分别选定用于测量设计和用于逆问题重建的提示。 |
| 主动学习 | 分布预测 | [Active Learning of Conditional Generative Models via the Transport Neural Tangent Kernel](cards.md#paper-151935) | 输出为分布时按均值和形状的不确定性共同挑选输入。 |
| 时序建模 | 记忆机制 | [Active Memory Feedback Loop for Fast–Slow Dynamics in Liquid Neural Networks](cards.md#paper-148250) | 让关联记忆影响下一步 recurrent 更新，而非只扩充输出头。 |
| 具身智能 | 视频动作表征 | [ActO: Extracting Action Representations from MLLM Embeddings for Video World Models](cards.md#paper-149590) | 优先适配预训练视频语言表征，并直接评估动作与场景分离。 |
| Agent | 离线信用分配 | [AgentBrew: Offline Tool-Use Agent Learning from Raw Real-World Trajectories](cards.md#paper-148366) | 按动作对事后任务的贡献加权原始轨迹。 |
| 优化 | 因果贝叶斯优化 | [AgentCBO: Causal Belief Routing for Bayesian Optimization under Unknown Graphs](cards.md#paper-155417) | 优先校正会改变干预选择的图结构。 |
| 多模态学习 | 强化学习 | [Agent Explorative Policy Optimization for Agentic Multimodal Reasoning](cards.md#paper-151150) | 对全错工具分支冻结思考前缀并重采样。 |
| Agent | 提示优化 | [AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems](cards.md#paper-153633) | 先以单代理干预定位失败来源，再按语义归类反馈。 |
| Agent | 停止决策 | [Agentic Abstention: Do Agents Know When to Stop Instead of Act?](cards.md#paper-150912) | 把及时弃权与最终弃权分开测量。 |
| 可解释性 | 模型选择 | [Agentic-imodels: Evolving agentic interpretability tools via autoresearch](cards.md#paper-154318) | 把模型文本能否支持正确行为预测纳入选择。 |
| Agent | 奖励验证 | [Agentic Reward Modeling: Verifying GUI Agent via Progressive Trajectory-Grounded Interaction](cards.md#paper-155392) | 轨迹证据不足时才让验证器探查环境状态。 |
| 人机协作 | 决策建模 | [AI-Assisted Classification under Correlation Neglect and Trust](cards.md#paper-152625) | 上线前分别估计信号重叠和用户信任。 |
| 多模态 / Agent | 通信路由 | [AIM: Adaptive Interaction in Multi-Agent Debate for Multimodal LLM Inference](cards.md#paper-152673) | 按实例选择文本、结构或原模态局部证据传递。 |
| Agent | 实验调度 | [AIRA 2: Overcoming Bottlenecks in AI Research Agents](cards.md#paper-152980) | 让搜索并发提速时同时提高候选选择评估的一致性。 |
| 多模态学习 | 表征对齐 | [AIR: Rethinking Image-Text Offset Alignment in Multimodal Contrastive  Representation Space](cards.md#paper-151241) | 先测概念距离导致的偏移失配，再调整文本方向。 |
| 统计学习 | 不确定性校准 | [A Kernel Nonconformity Score for Multivariate Conformal Prediction](cards.md#paper-151235) | 多维残差呈非椭圆形时，用核分数校准联合预测区间。 |
| 大语言模型 / 统计学习 | 审计校准 | [AKTD: FDR Control for LLM Training Data Detection under Approximate Exchangeability](cards.md#paper-148953) | 用独立的未入训样本估计审计统计量的不对称，再校准发现阈值。 |
| 具身智能 | 潜动作 | [ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models](cards.md#paper-152511) | 用可组合转移作为动作生成的辅助目标 |
| 大语言模型 / Agent | 可靠性 | [A Latent-Load Framework for Reliability Analysis and Intervention Design in LLM Pipelines](cards.md#paper-154404) | 按估计的错误传播收益配置有限检查点 |
| 具身智能 | 潜世界模型 | [A Latent World-Action Model with Jointly Aligned Reasoning](cards.md#paper-149267) | 用训练期未来视觉指导可部署的潜查询 |
| 大语言模型 | 推理路由 | [AlgoPilot: Cross-Paradigm Reasoning in Language Models via Strategy Selection and Guidance](cards.md#paper-154391) | 将范式选择和形式化指导与执行模型分离 |
| 计算机视觉 | 逆问题 | [Align $\&$ Invert: Solving Inverse Problems with Diffusion and Flow-based Models via Representation Alignment](cards.md#paper-148851) | 用近似目标的语义特征引导预训练生成先验 |
| 计算机视觉 | 评测 | [Align and Distill: Unifying and Improving Domain Adaptive Object Detection](cards.md#paper-156740) | 先统一训练协议并增强基线，再比较域适应方法 |
| 具身智能 | 轨迹规划 | [AlignDrive: Aligned Lateral-Longitudinal Planning for End-to-End Autonomous Driving](cards.md#paper-152098) | 先定横向路径，再沿路径预测纵向位移 |
| 具身智能 | 世界模型 | [Aligned Delta-Triplane Transformers as Occupancy World Models](cards.md#paper-152382) | 先补偿自运动，再预测占据变化 |
| 生成模型 / 强化学习 | 生成对齐 | [Aligning Few-Step Generative Model via Amortizing Sample-Based Variational Inference](cards.md#paper-155747) | 用样本粒子更新替代依赖似然的少步生成后训练。 |
| 强化学习 | 策略适配 | [Aligning Flow Map Policies with Optimal $Q$-Guidance](cards.md#paper-149374) | 在保持离线策略信赖域的同时，用评论器解析目标适配单步生成。 |
| 多模态学习 | 局部对齐 | [Aligning Forest and Trees in Images & Long Captions for Visually Grounded Understanding](cards.md#paper-155656) | 在中间层对齐文本片段和区域，在终层对齐整图和长描述。 |
| 序列建模 | 初始化 | [Aligning Inductive Bias for Data-Efficient Generalization in State Space Models](cards.md#paper-150462) | 按任务信号的功率谱初始化状态空间模型。 |
| 大语言模型 | 评测设计 | [Aligning Language Model Benchmarks with Pairwise Preferences](cards.md#paper-139753) | 用历史模型的下游成对排序重新加权静态题目。 |
| 大语言模型 | 选择性预测 | [Aligning Language Models with Selective Prediction](cards.md#paper-148722) | 将风险覆盖曲线面积作为后训练目标。 |
| 大语言模型 / Agent | 信用分配 | [Aligning LLMs Toward Multi-Turn Conversational Outcomes Using Iterative RLHF](cards.md#paper-151436) | 用对话级 Q 估计作为单轮 GRPO 的奖励。 |
| 大语言模型 | 部署安全评测 | [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](cards.md#paper-150322) | 把对齐回归加入 KV 缓存量化验收。 |
| 大语言模型 | 训练诊断 | [Alignment Dynamics in LLM Fine-Tuning](cards.md#paper-150384) | 在连续微调时监测对齐反转与再接触后的恢复速度。 |
| 自然语言处理 | 生成文本检测 | [Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy](cards.md#paper-151776) | 用对齐模型与基础模型的标准化似然差替代单模型似然。 |
| 时间序列 | 检索对齐 | [Align-RAG: Alignment Is All You Need for TSFM In-Context Learning](cards.md#paper-152416) | 给冻结预测器使用检索示例前先闭式对齐振幅和相位。 |
| 推荐系统 | 持续遗忘 | [ALIGN-Rec: Continual Recommendation under Heterogeneous Unlearning Requests](cards.md#paper-153461) | 在未来学习更新时监控已删除信号是否恢复。 |
| 机器学习理论 | 稳健优化 | [A Little Robustness Is All You Need: Leveraging Predictions for Contextual Optimization](cards.md#paper-150467) | 低预测误差仍不可直接跟随预测时，在预测邻域做稳健选策。 |
| 多模态 | 坐标变换 | [Allocentric Perceiver: Disentangling Allocentric Reasoning from Egocentric Visual Priors via Frame Instantiation](cards.md#paper-153797) | 把视角转换交给几何工具 |
| 具身智能 | 探索规划 | [All Roads Lead to Rome: Flow-driven Multi-Anchor Exploration for Open-Environment Active 3D Mapping](cards.md#paper-151339) | 部分可观测时保留多个长程探索候选 |
| 大语言模型 | 量化 | [AlphaQ: Calibration-Free Bit Allocation for Mixture-of-Experts Quantization](cards.md#paper-150665) | 缺少校准数据时用权重谱分配专家精度 |
| 大语言模型 | 时序评测 | [ALTER: An Allen's Algebra-Based Evaluation Framework for Temporal Reasoning of LLMs](cards.md#paper-139265) | 随机改叙述顺序来排查时序捷径 |
| 持续学习 | 表示诊断 | [A Mahalanobis Margin \texorpdfstring{$\gamma_{\min}$}{gamma\_min} Bound on Task Confusion in Pretrained Class-Incremental Learning: From Infeasibility to Exponential Attenuation](cards.md#paper-151690) | 用最差任务间 Mahalanobis 间隔预测类别混淆 |
| 大语言模型 | 低秩适配 | [A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)](cards.md#paper-155103) | 沿正则强度观察旧任务和新任务分类间隔 |
| 大语言模型 | 模型合并 | [AMARIS: Merging Generalist and Specialist LLMs via Adaptive Subspace Inheritance](cards.md#paper-154547) | 按激活方向选择性继承专家更新 |
| 学习理论 | 泛化诊断 | [A mathematical theory of balancing relational generalization and memorization](cards.md#paper-153152) | 同时用新关系组合和显式反例测试规则外推。 |
| Agent | 评测生成 | [A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks](cards.md#paper-150438) | 先生成工具调用序列再写题目 |
| 生成建模 | 分布控制 | [A Mean-Field Framework for Inference-Time Distributional Control of Diffusion Models](cards.md#paper-150099) | 群体目标用交互粒子而非逐样本独立打分 |
| 可解释性 | 循环模型 | [A Mechanistic Analysis of Looped Reasoning Language Models](cards.md#paper-153805) | 测每层循环轨迹是否稳定以诊断额外迭代价值 |
| 可解释性 | 匹配反事实 | [A Mechanistic Investigation of Theory of Mind in a Large Language Model](cards.md#paper-148276) | 以非心智匹配对照检验所谓心智推理模块 |
| 控制理论 | 在线预测 | [A Memory Efficient Unified Algorithm for Online Learning of Linear Dynamical Systems](cards.md#paper-155619) | 按不稳定复杂度而非隐藏维度选择预测器容量 |
| 科学机器学习 | 守恒离散化 | [A meshfree exterior calculus for generalizable and data-efficient learning of physics from point clouds](cards.md#paper-154490) | 点云上构造守恒算子后再学习通量 |
| 大语言模型 | 量化诊断 | [A Method-Class Divide in Sub-4-Bit Quantization:\\Iterative vs.\ Single-Pass Sensitivity to Data Composition](cards.md#paper-148347) | 极低位宽下为迭代量化单独优化校准数据 |
| 优化 | 局部学习规则 | [A method to automatically discover symbolic local learning rules](cards.md#paper-150193) | 用稀疏符号损失搜索替代局部黑箱学习器 |
| 大语言模型 | 集合采样 | [A Model of Diverse Sampling from Language Models](cards.md#paper-151475) | 用DPP优化整组候选的质量和互补性 |
| 贝叶斯优化 | 实验设计 | [Amortized Bayesian Experimental Design with In-Context Knowledge Conditioning](cards.md#paper-152127) | 额外知识进入上下文前按当前证据过滤 |
| 优化 | 最优传输 | [Amortized Optimal Transport from Sliced Potentials](cards.md#paper-156137) | 用切片势预测完整传输势 |
| 计算机视觉 | 推理量化 | [Amortized-Precision Quantization for Early-Exit Vision Transformers](cards.md#paper-154315) | 按层实际执行概率联合选位宽与退出门槛 |
| 统计学习 | 密度估计 | [Amortized Vine Copulas for High-Dimensional Density and Information Estimation](cards.md#paper-150646) | 复用一个二元估计器并校正边际 |
| 强化学习 | 规划蒸馏 | [Amortizing Generative Guidance for Model-Based Reinforcement Learning](cards.md#paper-152395) | 保留规划器高价值动作的多个模式 |
| 概率建模 | 超参数优化 | [Amplitude Decoupling in Gaussian Process Training: Exact Decomposition, Pole Cancellation, and Evaluation-Efficient Optimization](cards.md#paper-148358) | 先剖面化幅值再优化核形状 |
| 多模态学习 | 自适应推理 | [AMPS: Adaptive Modality Preference Steering via Functional Entropy](cards.md#paper-149128) | 按样本的模态贡献调整干预强度 |
| 强化学习 | 降方差 | [A Multi-Fidelity Control Variate Approach for Policy Gradient Estimation](cards.md#paper-156737) | 把低保真仿真作为控制变量 |
| 深度学习 | 优化器 | [AMUSE: Anytime Muon with Stable Gradient Evaluation](cards.md#paper-152756) | 同时检查 Muon 低曲率进展和高曲率振荡 |
| 电子设计 | 结构生成 | [AnalogToBi: Device-Level Analog Circuit Topology Generation via Bipartite Graph and Grammar Guided Decoding](cards.md#paper-150608) | 用双部图语法约束拓扑输出 |
| 生成模型 | 偏差校正 | [Analytical Correction for Subsampling Bias in Drifting Models](cards.md#paper-155602) | 用批内统计校正软最大质心估计 |
| 生成模型 | 逆问题 | [Analyzing and Guiding Zero-Shot Posterior Sampling in Diffusion Models](cards.md#paper-148817) | 在谱域确定后验采样参数 |
| 生成模型 | 训练诊断 | [Analyzing Learning-Dynamics Across Loss and Prediction Choices for Diffusion Models](cards.md#paper-155205) | 独立选择网络输出空间和损失空间 |
| 学习理论 | 算力分配 | [An Analytical Model of Compute-limited Multistage Training Pipelines](cards.md#paper-150925) | 根据预训练程度和数据质量调整各阶段预算 |
| 统计学习 | 软标签诊断 | [An Assessment of Human vs. Model Uncertainty in Soft-Label Learning and Calibration](cards.md#paper-139664) | 分开软标签的不确定性和标签众数变化 |
| 强化学习 | 离策略梯度 | [Anatomy of Off-Policy Policy Gradient: Importance Sampling, KL Regularization, and Baselines](cards.md#paper-155331) | 复用轨迹时成对使用 KL 正则和组均值基线。 |
| 大语言模型 | 推理蒸馏 | [Anchoring Reasoning Distillation via Syntactic Constraints](cards.md#paper-154471) | 保留弱教师正确的计划，掩掉错误结果 token。 |
| 统计学习 | 降维 | [Anchor PCA](cards.md#paper-153959) | 学习跨域稳定的方差方向，而非直接池化 PCA。 |
| 具身智能 | 世界模型 | [AnchorWorld: Embodied Egocentric World Simulation with View-based Evolution Customization](cards.md#paper-150033) | 用训练时第三人称空间监督补第一视角身体遮挡。 |
| 深度学习 | 网络拓扑 | [ANCRe: Adaptive Neural Connection Reassignment for Efficient Depth Scaling](cards.md#paper-152945) | 学习跨层残差连接布局，检验深层利用率。 |
| Agent | 鲁棒评测 | [AndroidReality: How Far Are Mobile Agents from the Real World?](cards.md#paper-139580) | 按状态、转移、动作分别施加界面扰动。 |
| 优化 | 零阶估计 | [An Educated Guess: Deriving Statistically Aligned Gradient Estimates for Zeroth-Order Optimization](cards.md#paper-150140) | 用前向激活谱构造探测方向。 |
| 学习理论 / 公平性 | 约束诊断 | [An Efficient Geometric Characterization of Robust Fair Learning](cards.md#paper-151262) | 用线性规划检查严格公平约束是否造成准确率对分布扰动敏感。 |
| 推荐系统 | 基准诊断 | [An Embarrassingly Simple Graph Heuristic Reveals Shortcut-Solvable Benchmarks for Sequential Recommendation](cards.md#paper-139297) | 在宣称生成式推荐学到长历史之前，先测试仅用最近一两项的图检索。 |
| 预训练 | 训练稳定性 | [An Empirical Study on Noisy Data and LLM Pretraining Loss Divergence](cards.md#paper-151029) | 区分噪声类型与规模风险 |
| 优化 | 等变优化器 | [An Equivariance Principle for Optimizer Design: Symmetry-Compatible Updates for Embeddings, LM Heads, and MoE Routers](cards.md#paper-154592) | 按矩阵层的对称性选择更新规则 |
| 生成模型 | 泛化理论 | [An exact information theory of generalization phase transitions in Bayesian diffusion models](cards.md#paper-152478) | 按可见信息量诊断扩散过程记忆与泛化 |
| 模型压缩 | 低精度训练 | [Angular Networks: Low-Bit Learning from Randomized Similarity Estimators](cards.md#paper-154802) | 采用角相似估计作为低比特线性层的替代 |
| 公平学习 | 数据审计 | [An Information-theoretic Framework for Auditing Unfairness in Training Data](cards.md#paper-153353) | 在训练前定位对公平偏差贡献较大的特征 |
| 概率建模 | 退火 | [Annealing in variational inference mitigates mode collapse: a theoretical study on Gaussian mixtures](cards.md#paper-151971) | 共同调节退火初温与速度以减少模式塌缩 |
| 科学机器学习 | 稳定状态空间 | [A Novel Schur-Decomposition-Based Weight Projection Method for Stable State-Space Neural-Network Architectures](cards.md#paper-151951) | 用 Schur 域投影约束状态矩阵稳定性 |
| 模型可靠性 | 拒答校准 | [Answering At Any Cost: Frontier LLMs Are Consequence-Insensitive](cards.md#paper-150213) | 按回答错误代价单独评测拒答 |
| 推理训练 | 自蒸馏 | [Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information](cards.md#paper-149938) | 检查含答案的教师上下文是否压低探索 token |
| 语音生成 | 分阶段编辑 | [AnyEdit: A Unified Framework for Speech and Singing Voice Editing with Real-World Environmental Consistency](cards.md#paper-152934) | 先编辑干净内容再恢复源环境声 |
| 多模态学习 | 传感表示 | [AnyMo: Geometry-Aware Setup-Agnostic Modeling of Human Motion in the Wild](cards.md#paper-154127) | 用同一动作的多佩戴视图学习配置不变表征 |
| 多模态学习 | 条件生成 | [AnyMo: Scaling Any-Modality Conditional Motion Generation with Masked Modeling](cards.md#paper-153279) | 以掩码建模统一可缺失的动作控制模态 |
| 统计学习 | 风险校准 | [Anytime-Valid Conformal Risk Control](cards.md#paper-154243) | 随着标注积累反复校准时采用任意时刻有效界 |
| 大语言模型 | 推理校准 | [Anytime-Valid PAC-Bayes Certificates for Adaptive Test-Time Scaling](cards.md#paper-153451) | 为反复试预算和验证器的过程报告统一风险成本界 |
| 视频生成 | 分辨率迁移 | [ApertureAttn: Native 4K Video Generation with Image-Only Supervision](cards.md#paper-154936) | 用高分辨率单帧监督训练空间高频适配 |
| 具身智能 | 规划验证 | [APIVOT: Adaptive Planning with Interleaved Vision-Language Thoughts](cards.md#paper-152333) | 空间约束强时让视觉想象验证语言计划 |
| 大语言模型 | 个性化评测 | [APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings](cards.md#paper-139154) | 用随机映射迫使模型从对话历史推断偏好 |
| 视频生成 | 物理评测 | [Apple-$\pi$: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence](cards.md#paper-139053) | 分阶段测试感知、定律表达和演绎 |
| 模型适配 | 模型合并 | [Approaching Effective Merging in Model Embedding Space](cards.md#paper-149693) | 先在共享内禀子空间表达任务更新再平均 |
| 机器学习系统 | 注意力计算 | [Approaching I/O-optimality for Approximate Attention](cards.md#paper-154340) | 按快速内存大小和允许的近似选择低 I/O 注意力 |
| 数值计算 | 核矩阵近似 | [Approximate Matrix–Vectors Under a Bounded $\ell_1$ Assumption and Applications to Kernel Matrices](cards.md#paper-150755) | 用总绝对质量决定是否以采样近似矩阵向量乘 |
| 学习理论 | 状态空间模型 | [Approximate Memory Suffices for Universal Approximation with State Space Models](cards.md#paper-148575) | 区分衰减历史任务的近似记忆和精确延迟恢复 |
| 联邦学习 | 稳健聚合 | [Approximation Guarantees for Robust Aggregation in Federated Learning](cards.md#paper-155522) | 在稳定性和逼近干净均值之间选择聚合约束。 |
| 学习理论 | 对比学习 | [Approximation in Contrastive Representation Learning](cards.md#paper-154229) | 根据互信息核的谱尾选择对比嵌入维度。 |
| 强化学习 | 约束优化 | [A Primal-dual Approach for Semi-Infinitely Constrained Reinforcement Learning](cards.md#paper-154351) | 用原始–对偶更新替代对连续约束族的内层求解。 |
| 计算机视觉 | 逆问题 | [A Principled Self-Referenced Early Stopping Approach for Deep Image Prior](cards.md#paper-151448) | 用伪独立观测构造早停指标，减轻无干净标签时的过拟合。 |
| 多智能体 | 仿真降本 | [APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents](cards.md#paper-149524) | 用自适应原型复用语言模型调用，并用独立抽查校正群体估计。 |
| 大语言模型 / 优化 | 零阶微调 | [AR1-ZO: Topology-Aware Rank-1 Zeroth-Order Queries for High-Rank LoRA Fine-Tuning](cards.md#paper-155186) | 高秩 LoRA 的零阶估计改用交替秩一方向并校准缩放。 |
| 时空建模 | 条件生成 | [Arbitrarily Conditioned Hierarchical Flows for Spatiotemporal Events](cards.md#paper-154895) | 用混合掩码把预报、后验补全与部分轨迹恢复作为同一条件任务。 |
| 大语言模型 | 上下文压缩 | [ARC-Encoder: learning compressed text representations for large language models](cards.md#paper-156755) | 用共享压缩编码器为不同解码器生成较短表示。 |
| 视频生成 | 流式编辑 | [AR-Edit: Training-Free Streaming Video Editing without Inversion](cards.md#paper-152336) | 缓存源视频注意力值以避免反演 |
| 在线学习 | 延迟反馈 | [A Reduction from Delayed to Immediate Feedback for Online Convex Optimization with Improved Guarantees](cards.md#paper-155853) | 将即时算法封装为可处理异步反馈的版本 |
| 大语言模型 | 偏好数据 | [Are Easier or Harder Examples Better? Rethinking Data Selection for Reward Models and Preference Optimization](cards.md#paper-151585) | 先校验奖励信号质量再按难度筛样 |
| 博弈学习 | 信念搜索 | [A Regularization-Based Approach to Public Belief State Search for Adversarial Games](cards.md#paper-152665) | 用平滑正则化求解公开信念下的局部策略 |
| Agent | 安全评测 | [Are LLM Safety Judges Policy-Invariant? A Three-Principle Stress-Test](cards.md#paper-139215) | 用语义等价规则改写检验裁判稳定性 |
| 多模态学习 | 基准诊断 | [Are Multimodal Benchmarks Really Useful? Item-Level Multimodal Benchmark Diagnosis via Structure-Response Co-Calibration](cards.md#paper-139183) | 联合题目结构与遮蔽模态后的响应估计依赖 |
| 可解释性 | 复现 | [A Reproduction Study of Weight-Based Mechanistic Interpretability in Bilinear MLPs](cards.md#paper-157024) | 检查权重可解释结构是否由权重衰减驱动 |
| 推荐系统 | 评测可靠性 | [ARES: How Reliable Are LLM User Simulators for Recommender A/B Testing?](cards.md#paper-139784) | 用多用户模拟骨干复核A/B结论 |
| 大语言模型 | 水印评测 | [A Retained-Signal Interface for LLM Watermark Robustness under Paraphrase](cards.md#paper-155532) | 分报初始信号、编辑后保留与检测器性能 |
| 统计学习 | 贝叶斯推断 | [A Revisit of Hamiltonian Monte Carlo Efficiency on Bayesian Neural Networks](cards.md#paper-152689) | 选激活函数时测积分器曲率误差 |
| 生成模型 | 奖励引导 | [Are we really tilting? The mechanics of reward guidance in flow and diffusion models](cards.md#paper-148402) | 区分模态内过优化与模态选择失效 |
| 推理模型 | 机制诊断 | [Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models](cards.md#paper-154084) | 用不同初值和中间轨迹诊断错误固定点 |
| 大语言模型 | 不确定性校准 | [Argument Graph Uncertainty: Quantifying Uncertainty from the Logical Structure of Reasoning Chains](cards.md#paper-149153) | 用单条推理链的逻辑关系估置信度 |
| Agent | 不确定性评测 | [Argus: A Cross-Regime Benchmark for the Transferability of Uncertainty Quantification in Computer-Use Agents](cards.md#paper-139443) | 换模型或从开放权重切换到 API 时重新校准 |
| 强化学习 | 持续学习 | [ARROW: Augmented Replay for RObust World models](cards.md#paper-156771) | 将近期缓存与长期覆盖缓存分别维护 |
| 三维视觉 | 运动参数估计 | [ArtCrafter: Feed-Forward Generation of Articulated 3D Object with Analytic Joint Derivation](cards.md#paper-151536) | 从跨状态一致的部件几何解析求关节 |
| 生成模型 | 采样调度 | [ART for Diffusion Sampling: A Reinforcement Learning Approach to Timestep Scheduling](cards.md#paper-155895) | 学习扩散采样时钟并蒸馏为固定步表 |
| 三维视觉 | 几何拟合 | [Articulation in Prime: Primitive-Based Articulated Object Understanding from a Single Casual Video](cards.md#paper-154376) | 用可见性感知的几何原语替代长时点轨迹 |
| Agent | 风险评测 | [ARTIS: Agentic Risk-Aware Test-Time Scaling via Iterative Simulation](cards.md#paper-150972) | 在实际执行前用验证过的模拟器评估候选 |
| 计算机视觉 | 词元剪枝 | [ASAP: Attention Sink Anchored Pruning](cards.md#paper-151159) | 用跨层传播距离判断冗余而非单层注意力 |
| 可靠性 | 分布外检测 | [ASAT: Adaptive Scoring and Thresholding with Human Feedback for Robust Out-of-Distribution Detection](cards.md#paper-156772) | 随真实反馈联合更新分数和接受阈值 |
| 大语言模型 | 训练诊断 | [A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs](cards.md#paper-155425) | 沿实际更新方向近似测曲率 |
| 科学机器学习 | 稳健性审计 | [A Scientific Claim Stability Framework for Evaluating MRI Morphometry Pipelines](cards.md#paper-139330) | 按科学结论是否保持来比较影像处理流水线 |
| 语言模型 | 置信校准 | [A Semantic-Sampling Framework for Evaluating Calibration in Open-Ended Question Answering](cards.md#paper-149036) | 分离回答选取与置信度估计采样 |
| 强化学习 | 多智能体分解 | [A Separation Principle for Cooperative Multi-Agent Reinforcement Learning](cards.md#paper-149847) | 以单体目标价值作为群体分配成本 |
| 具身学习 | 视频监督 | [ASH: Agents that Self-Hone via Embodied Learning](cards.md#paper-152698) | 用自身交互估计逆动力学，为无动作视频构建监督 |
| 强化学习 | 多目标优化 | [A Single Deep Preference-Conditioned Policy for Learning Pareto Coverage Sets](cards.md#paper-150514) | 利用偏好到回报的连续性扫过 Pareto 前沿 |
| 语言模型 | 难度校准 | [Ask-E: An Environment for Calibrated Question Generation](cards.md#paper-139309) | 用两参考模型的求解差界定题目难度 |
| Agent | 澄清策略 | [Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents?](cards.md#paper-154769) | 按缺失信息类型而非统一时点发起澄清 |
| 语言模型 | 推理训练 | [Asking the Right Questions: Improving Reasoning with Generated Stepping Stones](cards.md#paper-149684) | 先生成可跨求解器复用的中间问题 |
| 统计学习 | 密度估计 | [A Spectral Framework for Closed-Form Relative Density Estimation](cards.md#paper-152831) | 用特征矩闭式拟合相对对数密度 |
| 生成模型 | 质量评估 | [Assessing Sample Quality in Conditional Generation under Compositional Shift](cards.md#paper-148544) | 缺少目标组合实样时分别核查真实性和属性忠实度 |
| 多模态学习 | 测试时适配 | [ASSET: Acquisition-Sensitive Subspace Estimation for Test-Time Adaptation of Medical VLMs](cards.md#paper-153026) | 只在采集质量敏感子空间内更新 |
| 可解释性 | 机制分析 | [Assign and Add: A Mechanistic Study of Compositional Arithmetic](cards.md#paper-153282) | 检查同一内部模块能否跨输入表示复用 |
| 优化 | 稳定性 | [A Stability Analysis of AdamW: Unstable Equilibria and Non-Convergence](cards.md#paper-151341) | 区分优化器固定点与动力学收敛 |
| 模型理论 | 注意力设计 | [A Statistical Theory of Gated Attention through the Lens of Hierarchical Mixture of Experts](cards.md#paper-153011) | 比较在注意力输出与值映射处放置门控 |
| 大语言模型 | 多任务强化学习 | [ASTOR: Multi-Task Code Reinforcement Learning via Utility-Driven Coordination](cards.md#paper-154519) | 按任务学习价值分别配训练预算和 KL 约束 |
| 强化学习 | 代理目标 | [A Surrogate Perspective on Convergence of Fixed-Target DQN](cards.md#paper-155836) | 用平滑最大误差减少最坏Bellman残差 |
| 表征学习 | 向量量化 | [ASVQ: What Reparameterization Is Just Enough for Efficient Codebook Learning?](cards.md#paper-149752) | 先试自适应尺度再增加码本重参数化复杂度 |
| 推理系统 | 负载均衡 | [AsymHP: Load-Balanced Sparse Attention for Video Diffusion Transformers](cards.md#paper-151792) | 按上一扩散步的密度分配每卡注意力头 |
| 生成模型 | 流匹配 | [Asymmetric Flow Models](cards.md#paper-156075) | 仅压缩噪声预测，保留全维数据预测 |
| 学习理论 | 缩放规律 | [Asymmetric Scaling Laws from Sparse Features](cards.md#paper-149774) | 稀有特征覆盖不足时先增加数据 |
| 生成模型 | 负向引导 | [Asymptotically Exact Negative Guidance of Diffusion Models via Positive-Unlabeled Learning](cards.md#paper-148530) | 用显式目标分布检查负向引导偏差 |
| 统计学习 | 序贯推断 | [Asymptotically Log-Optimal Bayes-Assisted Confidence Sequences for Bounded Means](cards.md#paper-153874) | 用预测模型提高选取有效鞅因子的效率 |
| 分布式训练 | 异步优化 | [AsyncMesh: Fully Asynchronous Optimization for Data and Pipeline Parallelism](cards.md#paper-155437) | 按并行轴分别补偿参数陈旧 |
| 大语言模型 | 蒸馏 | [AsyncOPD: How Stale Can On-Policy Distillation Be?](cards.md#paper-156136) | 按 KL 方向选异步估计器 |
| 视觉 | 分布外检测 | [A Systematic Analysis of Out-of-Distribution Detection Under Representation and Training Paradigm Shifts](cards.md#paper-138908) | 按表征和偏移强度筛置信分数 |
| 软件工程 | 代码评测 | [A Theoretical Analysis of Test-Driven Code Generation](cards.md#paper-149483) | 代码候选排序先试软功能相似度 |
| 大语言模型 | 表征机制 | [A Theoretical Analysis of Why Masked Diffusion Models Mitigate the Reversal Curse](cards.md#paper-149727) | 分别检查正反查询是否共享值侧证据 |
| 计算神经科学 | 动力系统 | [A Theory of Spatial Continuous Attractors in Hopfield Energy Landscapes](cards.md#paper-155828) | 分别学习吸引流形的法向恢复和切向输运 |
| 生成模型 | 理论保证 | [A Theory on Flow Matching with Neural Networks](cards.md#paper-152773) | 同时监控速度回归误差和生成分布距离 |
| 具身智能 | 预测对齐 | [ATI-VLA: Action-Centric Predictive Vision–Language–Action Models via Actionable Alignment Then Adaptive Injection](cards.md#paper-152880) | 先对齐未来观测和动作，再用动作目标控制注入 |
