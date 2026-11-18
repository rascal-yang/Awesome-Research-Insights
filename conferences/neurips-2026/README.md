# NeurIPS 2026

[首页](../../README.md) · [官方会议目录](https://neurips.cc/Downloads/2026)

官方目录当前列出 **9,144** 个论文海报条目，已筛选 **218** 篇，暂收录 **178** 篇。[筛选底册](papers.tsv)按官方海报 ID 记录覆盖及去留。目录可能随会议更新，候选范围核定后统一排名，收录上限为 50%。

目录统计：下载目录的海报条目与三地论文页的 9,128 个海报 ID 已对照。下载目录另有 16 个条目，其中包含复现赛道。已发现同名多场次展示，论文级去重仍在进行。

| 领域 | 技术类型 | 论文卡 | 能改变的技术选择 |
| --- | --- | --- | --- |
| 大语言模型 / Agent | 在线记忆 | [δ-Mem](cards.md#paper-33u8sf3mic) | 在冻结骨干上用小型可写状态修正注意力，比较延长上下文与更新记忆的效果。 |
| 强化学习 / 学习理论 | 离线决策 | [Fast Rates for Offline Contextual Bandits with Forward-KL Regularization under Single-Policy Concentrability](cards.md#paper-tdl6qleloi) | 在日志覆盖有限时，根据正则强度判断前向 KL 的样本复杂度是否进入快率区间。 |
| 大语言模型 | 激活量化 | [ConQuR: Corner Aligned Activation Quantization via Optimized Rotations for LLMs](cards.md#paper-151137) | 按激活方向校准正交旋转，降低低比特误差和校准成本。 |
| 大语言模型 / 推理 | 推理预算 | [Confidence-Calibrated Inference Expansion for Evaluator-Guided Test-Time Reasoning](cards.md#paper-155179) | 分别校准接受、回退和扩展后的成功概率，再按净收益分配算力。 |
| Agent | 经验记忆 | [MAGE: Multi-Agent Self-Evolution with Co-Evolutionary Knowledge Graphs](cards.md#paper-150998) | 分别检索成功推理和失败纠正，使冻结执行模型随经验增长改进。 |
| Agent | 记忆评测 | [MemContract: Contract-Sensitive Evaluation for Mutable Agent Memory](cards.md#paper-154728) | 比较记忆后端时单测修订、弃用、擦除和来源追踪。 |
| 大语言模型 / 学习架构 | 空间记忆 | [DeltaFugue: Orchestrating Spatial and Associative Memory for Algorithmic Length Generalization](cards.md#paper-148950) | 将位置敏感的长程结构交给可寻址空间带，而非继续压缩进固定关联状态。 |
| 多模态学习 | 分布对齐 | [Beyond Pairwise Supervision: Spectral Characteristic Matching for Data-Efficient Multimodal Alignment](cards.md#paper-153322) | 配对很少时同时优化点对点目标与跨模态分布差异。 |
| 计算机视觉 | 多通道表征 | [Disentangling Channel Semantics in Vision Transformers via Token Decorrelation and Composition-Aware Modulation](cards.md#paper-152861) | 按输入样本的通道组合调制特征，并让各上下文 token 提供互补信号。 |
| 多模态学习 | 推理加速 | [Fewer Tokens, Fewer Layers: Efficient Vision Token Pruning and On-Policy Distillation to Accelerate VLMs](cards.md#paper-152441) | 同时减少视觉预填充与长文本解码开销。 |
| 多模态学习 | 梯度路由 | [GEAR-Align: Grounding-Evidence-Aware Gradient Routing for Multimodal Alignment](cards.md#paper-153068) | 按答案 token 对视觉的依赖程度分配梯度。 |
| 多模态学习 | 无监督对齐 | [RankAlign: Unsupervised Vision-Language Representation Alignment via Rank Transformation](cards.md#paper-149742) | 无配对对齐时比较绝对相似度和模态内部邻居排序。 |
| 科学机器学习 | 成本评测 | [Breakeven complexity: A new perspective on neural partial differential equation solvers](cards.md#paper-148644) | 按同误差的数值解算器计算盈亏平衡求解次数。 |
| 科学机器学习 | 归因诊断 | [Explanation of Dynamic Physical Field Predictions using WassersteinGrad: Application to Autoregressive Weather Forecasting](cards.md#paper-151943) | 归因误差主要是空间错位时使用几何重心。 |
| 科学机器学习 | 时序算子 | [Learning Spectral Compositional Koopman Operators for Global-to-Regional Weather Forecasting](cards.md#paper-153842) | 长程预报先诊断消息传递引起的频谱平滑。 |
| 科学机器学习 | 神经算子 | [Theory Guided and Interpretable Neural Operator Design for Partial Differential Equation Learning](cards.md#paper-151006) | 用自适应傅里叶分解指导复杂流形上的算子结构。 |
| 科学机器学习 | 概率预报 | [Tyche: One Step Flow for Efficient Probabilistic Weather Forecasting](cards.md#paper-153693) | 压缩生成步数后继续用滚动校准目标训练。 |
| 优化 / 概率建模 | 稳健决策 | [Deferred Aggregation in Hierarchical Bayesian Optimization](cards.md#paper-149951) | 各模型先选候选点，再用中心样本聚合决策。 |
| 强化学习 / 优化 | 部分反馈学习 | [Online Decision-Focused Learning under Semi-Bandit Feedback](cards.md#paper-150539) | 用未观测代价补全候选决策，但只用实测组件更新表征。 |
| 计算机视觉 | 分层表征 | [$\alpha$Depth: Learning Single-Pass Soft Boundary Decomposition for Stereo Conversion](cards.md#paper-154295) | 将混合边界拆为颜色和深度层 |
| 大语言模型 | 异步蒸馏 | [$\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control](cards.md#paper-150017) | 按样本新鲜度调节异步蒸馏 |
| Agent | 工作流评测 | [$\chi$-Bench: Can AI Agents Automate End-to-End, Long-Horizon, Policy-Rich Healthcare Workflows?](cards.md#paper-139361) | 分别测独立回合和共享会话 |
| 强化学习 / 理论 | 树搜索 | [$\epsilon$-Good Action Identification in Fixed-Budget Monte Carlo Tree Search](cards.md#paper-152538) | 固定预算下以近优识别率衡量采样 |
| 大语言模型 | 奖励对齐 | [$f$-GRPO & Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment](cards.md#paper-153358) | 以组内相对奖励划分对齐样本并选择散度 |
| 优化 / 理论 | 曲率建模 | [$\gamma$-weakly $\theta$-up-concavity: A Unified Framework for Non-Convex Optimization Beyond DR-Submodular and OSS Functions](cards.md#paper-150269) | 根据曲率条件选用线性代理 |
| 计算机视觉 | 条件生成 | [$h$-control: Training-Free Camera Control via Block-Conditional Gibbs Refinement](cards.md#paper-155968) | 按同噪声级细化未观测区域 |
| 计算机视觉 | 数据蒸馏 | [$\mathbf{D^{3}S^{2}}$: Diffusion-Guided Dataset Distillation for Semantic Segmentation](cards.md#paper-155224) | 先按类别筛掩码，再用像素和特征约束合成 |
| 多模态 / Agent | 可靠性评测 | [$\mathbf{\mathtt{MAD\text{-}Bench}}$: How Do Multimodal Agents Deceive You?](cards.md#paper-139531) | 把任务声明与可查执行证据独立对比 |
| 优化 / 理论 | 训练诊断 | [$\mathcal{P}$Torch: Narrowing the Gap Between Projection and Gradient-Based Learning](cards.md#paper-153540) | 在比较投影与梯度训练时扫描深度 |
| 学习理论 / 可解释性 | 因果评测 | [$\mathrm{Bounded\mbox{-}RS}$: A Bounded Evaluation Protocol and Testbed for Representational Systematicity](cards.md#paper-139441) | 把可解码性与生成过程实际使用分开检验。 |
| 科学机器学习 | 物理引导预测 | [$PAS^2$: Physics-Anchored Spectral Reasoning for Air Quality Forecasting](cards.md#paper-148682) | 先估确定性趋势，再让神经分支学习波动。 |
| Agent | 主动性评测 | [$\pi$-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows](cards.md#paper-139571) | 独立统计任务完成与提前发现隐含需求。 |
| 计算机视觉 | 几何配准 | [$\pi^2$: A Simple Framework for 2D-to-3D Registration](cards.md#paper-148690) | 预测点云在相机坐标系的位置，再解析求刚体位姿。 |
| 计算机视觉 | 流式重建 | [$R^3$: 3D Reconstruction via Relative Regression](cards.md#paper-154197) | 用加权相对位姿约束替代单一全局锚点。 |
| 生成建模 | 几何条件生成 | [$SE(2)$-Aware Conditional Distribution Transport for Vehicle Trajectory Generation](cards.md#paper-153739) | 在平面刚体位姿空间定义轨迹生成的中间输运状态。 |
| 具身智能 / 多模态 | 感知监督 | [$\text{A}^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation](cards.md#paper-155296) | 从操作引起的画面变化离线构造目标区域监督。 |
| 科学机器学习 / 视觉 | 传感信号建模 | [$\textbf{EchMo}$: End-to-End Radar Echo Segmentation](cards.md#paper-151818) | 把雷达处理阶段参数化成可微模块，联合优化分割。 |
| 计算机视觉 | 部件定位 | [$\text{PartConcepts}$: A Unified Mechanism for Fine-Grained Part Localization and Generation](cards.md#paper-151747) | 训练部件专用 token 提高细粒度属性绑定。 |
| 学习理论 / 视觉 | 不变表征 | [$\texttt{bispectrum}$: Selective $G$-Bispectra Made Practical](cards.md#paper-148783) | 在已知对称群的任务中测试选择性双谱池化。 |
| 强化学习 | 回报分布 | [$\varphi$TD: Distributional Reinforcement Learning using Characteristic Functions](cards.md#paper-154745) | 需要连续多峰回报时用特征函数损失。 |
| 计算机视觉 | 空间推理 | [2D Spatial Reasoning with Adaptive Neural Cellular Automata](cards.md#paper-154751) | 把固定局部传播改成可动态改变感受野的迭代推理。 |
| 因果学习 | 决策支持 | [2-Step Agent: How a Bayesian Decision Maker Learns from AI-Decision Support](cards.md#paper-150442) | 评估模型辅助时扫描用户先验与真实参数的错配。 |
| 多模态 / Agent | 模仿重加权 | [3A-VLA: Abstraction-Aligned Action Learning for Vision-Language Agents in 3D Game Worlds](cards.md#paper-153557) | 用意图和环境可供性一致程度调节示范损失。 |
| 医学影像 | 特征路由 | [3DABSeg: Adaptive 3D Ankle Bone Segmentation with Multiscale Feature Fusion Mixture-of-Experts](cards.md#paper-151779) | 按多尺度空间统计将通道硬分给不同专家。 |
| 多模态 / Agent | 失败诊断 | [3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code](cards.md#paper-139453) | 分开统计程序运行失败与渲染成功后的几何缺陷。 |
| 计算机视觉 | 多视图对齐 | [3D Consistency Tokens](cards.md#paper-152512) | 将跨视图匹配建立在共享三维位置上。 |
| 科学机器学习 | 逆问题 | [3D Fresnel Volumizing for Efficient Implicit Velocity Field Reconstruction](cards.md#paper-155228) | 把沿射线的稀疏梯度扩展到物理相关的邻域。 |
| 计算机视觉 | 三维重建 | [3D Gaussian Splatting within Self-Learned Neural View-Dependent Color Fields](cards.md#paper-156149) | 对高斯颜色施加连续场约束，减轻颜色对几何错误的补偿。 |
| 多模态学习 | 部件表征 | [3D-PLOT-LLM: Part-Level Object Tokens for 3D Large Language Models](cards.md#paper-148954) | 用可引用词表槽位把部件作为语言模型输入和输出中的实体。 |
| 计算机视觉 / 雷达 | 物理渲染 | [3D Point Splatting for mmWave Radar Novel View Synthesis](cards.md#paper-151080) | 保留复相位再派生雷达产品 |
| 计算机视觉 | 三维表示 | [3D Skew Normal Splatting](cards.md#paper-152761) | 在非对称边界用可学习偏斜原语 |
| 计算机视觉 | 视频评测 | [3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](cards.md#paper-153051) | 用含语义的三维轨迹重建评估视频物理一致性 |
| 计算机视觉 | 数据增强 | [3D-VITAL: Visibility-aware Identity Training from Artificial Liftings of 3D Reconstruction model for Cross-View Object Re-Identification](cards.md#paper-150244) | 将合成新视角的真实可见部分与幻觉纹理区分 |
| 计算机视觉 | 参数高效适配 | [3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model](cards.md#paper-155977) | 显式修复跨视角关系以适配三维模型 |
| 强化学习 | 离线策略提取 | [A$^2$IQL: Adaptive Asymmetric Implicit Q Learning for Automated Warehouse Consolidation](cards.md#paper-148721) | 动作集合很大时分离逐候选打分和集合价值估计 |
| 多模态学习 | 关系评测 | [A$^3$Bench: A Benchmark for Compositional Reasoning over Aggressive Interactions in Videos](cards.md#paper-139138) | 显式测试人物与动作的绑定 |
| 具身智能 / 多模态 | 评测压缩 | [A2Eval: Agentic and Automated Evaluation for Embodied Brain](cards.md#paper-153258) | 按能力覆盖压缩评测并测排序保持 |
| 图学习 | 结构编码 | [A2I: Adjacency-to-Image Structural Encodings for Graph Learning](cards.md#paper-149615) | 用局部邻接布局给节点编码补图结构 |
| 计算机视觉 | 三维生成 | [A 3D Scene is Worth 1K Tokens: 3D-Grounded Representation for Scene Generation at Scale](cards.md#paper-148286) | 在显式反映三维结构的隐空间做去噪 |
| 优化 | 聚类算法 | [A Batched Hartigan's $k$-Means Clustering](cards.md#paper-148581) | 以安全独立性筛选可并行坐标更新 |
| 大语言模型 | 偏好学习 | [ABC-Align: Prediction-Powered Alignment with Adaptive Bias Control](cards.md#paper-148310) | 按偏差与方差动态调节人工纠偏强度 |
| 生成建模 | 时空建模 | [ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](cards.md#paper-150308) | 把扩散推进时间与物理时间对齐 |
| 多模态学习 | 长视频评测 | [A Benchmark for Omni-Modal Reasoning in Long Videos](cards.md#paper-139047) | 用分项证据量表区分视觉、语音和环境声失败 |
| 多模态学习 / Agent | 行为评测 | [ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective](cards.md#paper-139180) | 用匹配场景检验旁观判断能否预测作为行动者的选择 |
| 统计学习 | 最优传输 | [A Biconvex Formulation for Stable Transport of Mixture Models with a Unique Solution](cards.md#paper-151803) | 将传输基本单位换成子群而非样本。 |
| 大语言模型 | 数据策略 | [A Bitter Lesson for Data Filtering](cards.md#paper-155947) | 在高算力且数据稀缺时，把不过滤作为等预算预训练对照。 |
| 统计学习 | 在线校准 | [A Black-Box Reduction from Regret to Multi-Level Coverage](cards.md#paper-154233) | 用在线算法的线性化遗憾控制多级覆盖。 |
| 计算机视觉 | 退化模拟 | [AbsoluteDegradation: A Physics-Inspired Synthetic Film-Degradation Pipeline and Archival Film Restoration Benchmark](cards.md#paper-139176) | 分解并控制模拟伪影的来源和时间相关性。 |
| 强化学习 | 约束优化 | [Absolute State-wise Constrained Policy Optimization: High-Probability State-wise Constraints Satisfaction](cards.md#paper-149439) | 监控整条轨迹的瞬时成本最大值。 |
| 优化 | 加速方法 | [AcceleGrad#: Adaptive Geometry-Aware Acceleration](cards.md#paper-154083) | 将自适应锚点和任务选定的非欧几何分开选。 |
| 计算机视觉 | 推理剪枝 | [Accelerated Image Editing via Consistency-Aware Source Token Pruning](cards.md#paper-149846) | 用显式采样修正替代部分源图注意力。 |
| 优化 | 极小极大优化 | [Accelerated last-iterate convergence of Extragradient via power-law stepsizes](cards.md#paper-155893) | 将外推与更新步长解耦。 |
| 大语言模型 | 扩散推理 | [Accelerating Diffusion Language Models via Structured Suffix Modeling](cards.md#paper-152485) | 分段保留后缀位点，复用前一去噪步信息。 |
| 生成模型 | 并行解码 | [Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding](cards.md#paper-156738) | 按层依赖冗余选择 Jacobi 解码。 |
| 优化 | 预训练优化 | [Accelerating LLM Pre-Training through Flat-Direction Dynamics Enhancement](cards.md#paper-150025) | 对曲率较平的方向分配更激进更新。 |
| 大语言模型 | 预填充加速 | [Accelerating Long-Context LLM Prefill via Layer-wise Progressive Token Pruning in Local Deployment](cards.md#paper-154875) | 离线按时延预算确定逐层剪枝策略。 |
| 优化 | 训练动力学 | [Accelerating Neural Network Training with Augmented Koopman Dynamics](cards.md#paper-149064) | 同时外推参数和优化器内部状态。 |
| 生成模型 | 推理缓存 | [Accelerating Rectified Flow Models  via Trajectory-Aware Caching](cards.md#paper-151611) | 分别追踪流速度的大小偏差和方向偏差。 |
| 强化学习 | 并行约束学习 | [Accelerating Safe Reinforcement Learning with Massive Parallelism](cards.md#paper-153909) | 按回合相位重建成本而非直接平均短滚动。 |
| 机器学习系统 | 软硬件协同 | [Accelerating the Inference Era with AI-Driven, Globally Optimized HW/SW Co-Design](cards.md#paper-154818) | 联合优化切分融合、内存驻留和重算。 |
| 计算机视觉 | 视频反演 | [Accelerating Video Inverse Problem Solvers with Autoregressive Diffusion Models](cards.md#paper-151472) | 用测量一致初值启动流式逆扩散。 |
| 机器学习系统 | 评测与诊断 | [AccelEval: A Whole-Program Benchmark for LLM-Generated CPU-to-GPU Code Acceleration](cards.md#paper-139678) | 用端到端正确性和同任务性能上限评估 GPU 代码生成。 |
| 神经科学 / 统计学习 | 评测校准 | [Accuracy of Noise Ceiling Estimators for Brain Scores](cards.md#paper-154840) | 先检查噪声上限估计器偏差再比较脑对齐分数。 |
| 学习理论 | 公平性 | [Accuracy vs. Accuracy: Computational Tradeoffs Between Classification Rates and Utility](cards.md#paper-148397) | 分开审查子群比例、校准与损失的可计算性 |
| 高效训练 | 稀疏重连 | [AC/DC on a Budget -- Alternating Sparse Phases](cards.md#paper-149303) | 以掩码收敛终止稠密阶段或直接进行稀疏重连 |
| 计算机视觉 | 三维重建 | [ACD-GS: Asymmetric Curvature-aware Densification for 3D Gaussian Splatting](cards.md#paper-150094) | 按深度曲率决定高斯克隆与分裂 |
| 自动机器学习 | 架构搜索 | [ACDP: Architecture-aware Cross-Dataset Performance Predictor for NAS](cards.md#paper-154537) | 让架构特征决定数据集的表征方式 |
| Agent | 因果评测 | [ACED-Bench: Evaluating How LLM Agents Acquire and Act on Causal Evidence](cards.md#paper-154560) | 用形式化世界检验智能体选实验、保留证据及停止的能力 |
| 因果推断 | 部分识别 | [A Characterization of Latent Variable Causal Models Consistent with Observational Data](cards.md#paper-148646) | 在整个潜变量因果等价类上优化反事实范围 |
| 高效训练与推理 | 脉冲模型转换 | [Achieve Latency-Efficient Temporal-Coding  Spiking LLMs via Discretization-Aware Conversion](cards.md#paper-154129) | 以静态量化误差分析离散首次脉冲时间编码 |
| 强化学习 | 赌博机 | [Achieving adaptivity and optimality for multi-armed bandits using Exponential-Kullback Leibler Maillard Sampling](cards.md#paper-156739) | 分布属于单参数指数族时同时考察多种遗憾标准 |
| 优化 | 在线双层优化 | [Achieving Better Local Regret Bound for Online Non-Convex Bilevel Optimization](cards.md#paper-148523) | 依据环境变化和预算选择自适应内循环或单循环 |
| 优化 | 非光滑优化 | [Achieving Directional-Stationarity from a Single Random Direction Step](cards.md#paper-149362) | 用一次随机方向探索增强现有优化法的方向驻点保证 |
| 强化学习 | 遗憾分析 | [Achieving Optimal Static and Dynamic Regret Simultaneously in Bandits with Deterministic Losses](cards.md#paper-154262) | 根据对手可否适应来判断能否联合优化静态和动态遗憾 |
| 多模态学习 | 时序结构评测 | [A Closer Look at Dynamic Scene Graph Generation in the Era of Multimodal Large Language Models](cards.md#paper-151784) | 动态场景图同时测关系精度、信息量与重复 |
| Agent | 预算路由 | [A Communication-Theoretic Framework for LLM Agents: Cost-Aware Adaptive Reliability](cards.md#paper-150815) | 按任务难度决定重试、投票或迭代验证的预算 |
| 训练数据 | 在线选样 | [A Compass for Useful Data: Online Data Selection via Alignment-Gated Fisher Geometry](cards.md#paper-155971) | 结合更新效用、下降方向和批内互补性来分配训练预算 |
| 表征学习 | 离散表征 | [A Composite Activation Function for Learning Stable Binary Representations](cards.md#paper-148660) | 训练二值激活时保留阈值附近及尾部的梯度 |
| 学习理论 | 稳健公平性 | [A Comprehensive View of Fairness through Distributional Stability](cards.md#paper-153293) | 在多种人群配比下联合报告公平性而非单一测试分布 |
| 训练数据 | 消融预算 | [A Computational Perspective to Data Ablation Experiments](cards.md#paper-155175) | 固定算力时联合分配数据配方搜索与最终训练预算 |
| 强化学习 | 偏好约束 | [A Constrained Bi-level Optimization Framework for Constrained Preference-Based Reinforcement Learning](cards.md#paper-152347) | 从反馈同时学习奖励与约束成本，而非预设约束成本 |
| 深度学习 | 局部学习 | [A Control-Theoretic Approximation to Predictive Coding Dynamics](cards.md#paper-154268) | 在接近平衡时用集中反馈近似预测编码 |
| 多模态 | 评测 | [AcousticBench: Measuring Acoustic Perception in Large Audio Language Models](cards.md#paper-139542) | 用无词汇声学对照隔离听觉能力 |
| 学习理论 | 超参诊断 | [A Critical $\beta$-Scale for Posterior Collapse in Dirichlet $\beta$-VAEs](cards.md#paper-150320) | 先估计坍塌阈值再搜索正则 |
| 多模态 | 评测 | [Acting without Knowing: Planning, Prediction, and Transfer Dissociate in Interactive Visual Physics](cards.md#paper-139556) | 同一场景分别测行动、预测和迁移 |
| 强化学习 | 动作分块 | [Action Chunking Proximal Policy Optimization with Feedback Correction](cards.md#paper-154625) | 用标准状态价值并在块内闭环纠偏 |
| 强化学习 | 方差控制 | [Action-Level Behavior Policy Optimization for Variance-Reduced Policy Gradients](cards.md#paper-153538) | 固定状态分布后改行动提议分布 |
| 学习理论 | 抽样设计 | [Active Context Selection Improves Simple Regret in Contextual Bandits](cards.md#paper-151058) | 主动抽样按目标人群权重的三分之二次幂分配 |
| Agent | 行为评测 | [Active Probabilistic Reasoning in Humans and LLMs](cards.md#paper-149573) | 分别测证据收集与证据整合 |
| 具身智能 | 量化 | [ActQuant: Sub-4-bit Action-Guided Quantization for Vision-Language-Action Models](cards.md#paper-155159) | 按动作敏感度分配位宽和张量内尺度 |
| 因果学习 | 闭环辨识 | [Act, Validate, Adapt: Closing the Causal Discovery-Control Loop](cards.md#paper-153013) | 用干预验证图结构而非只重新拟合系数 |
| 多模态 | 推理预算 | [AdaAlloc: Adaptive Visual Token Allocation for Long-Video Question Answering](cards.md#paper-155735) | 在同一 token 预算内动态分配全局和局部证据 |
| 多模态 | 视频编码 | [AdaCodec: A Predictive Visual Code for Video MLLMs](cards.md#paper-148821) | 用关键帧和预测残差取代重复编码邻帧 |
| 语言模型 | 量化 | [AdaKVQ: Adaptive Mixed-Precision KV Cache Quantization For Efficient Reasoning Models](cards.md#paper-153261) | 观察注意距离再分配缓存精度 |
| Agent | 策略学习 | [AdaMAP: Learning Adaptive Multi-Action Prediction with Grounded Dreaming Guidance](cards.md#paper-155834) | 让动作块自行决定何时重新观察 |
| 多模态 | 推荐 | [AdaM-Rec: Adaptive Modality Routing for Multimodal Recommendation](cards.md#paper-148211) | 按查询选择视觉或文本证据 |
| 优化 | 收敛分析 | [Adam under Generalized Smoothness with Second-Moment-Type Stochastic Gradients](cards.md#paper-151271) | 检查随机梯度二阶矩与自归一化而非先假设轻尾 |
| 具身智能 | 三维感知 | [AdaOcc: Adaptive 3D Occupancy Prediction for Embodied Tasks](cards.md#paper-152734) | 以渐进查询数量调节占据预测预算 |
| 语言模型 | 低秩适配 | [AdaPaD: Adaptive Parallel Deflation for PEFT with Self-Correcting Rank Discovery](cards.md#paper-153769) | 并行修正低秩分量并按重要性增长模块秩 |
| 科学机器学习 | 长尾生成 | [AdaPCLA: Curriculum Prior Internalization For Long-Tailed Longitudinal EHR Generation](cards.md#paper-150249) | 按退火调度逐步引入稀有事件分布先验 |
| 机器学习 | 半监督学习 | [AdapMatch: Adaptive Bias Decoupling for Semi-Supervised Partial Label Learning under Unknown Class Distributions](cards.md#paper-150939) | 分别监控伪标签入选偏差与候选集消歧偏差 |
| 优化 | 低秩适配 | [AdaPreLoRA: Adafactor Preconditioned Low-Rank Adaptation](cards.md#paper-155053) | 选择可逆的因子空间预条件近似 |
| 强化学习 | 目标条件策略 | [AdaptFlow: State-Anchored Goal Conditioning with Flow Matching for Offline Goal-Conditioned RL](cards.md#paper-155009) | 让状态与目标共同决定调制参数 |
| 语言模型 | 可解释性 | [ADAPT: Hybrid Prompt Optimization for LLM Feature Visualization](cards.md#paper-150038) | 先广搜离散提示，再用梯度导向变异 |
| 科学机器学习 | 主动采样 | [Adapting Actively on the Fly: Relevance-Guided Online Meta-Learning with Latent Concepts for Geospatial Discovery](cards.md#paper-156089) | 采样时优先相关且未充分观测的地区 |
| 机器学习 | 测试时适配 | [Adapting in the Dark: Efficient and Stable Test-Time Adaptation for Black-Box Models](cards.md#paper-148897) | 为黑盒模型加可求梯度的轻量本地组件 |
| 学习理论 | 博弈 | [Adapting to Conflict: Equilibrium Structure and Adaptive Learning in Harmonic Games](cards.md#paper-148344) | 在谐和博弈中选可适应的外推学习规则 |
| 科学机器学习 | 视觉评测 | [Adapting Vision Transformers to Organoid Imaging](cards.md#paper-150605) | 按影像任务选骨干而不只比较模型参数量 |
| 优化 | 进化策略 | [Adaptive and Neutral Theory of Evolution Strategies for Large Language Models](cards.md#paper-151417) | 分阶段评估归一化进化策略的收益与遗忘 |
| 图学习 | 领域适配 | [Adaptive Attribute Completion with Representation Space for Incomplete Graph Domain Adaptation](cards.md#paper-152820) | 在补齐缺失属性时同步更新可靠跨图表示 |
| 机器学习 | 统计审计 | [Adaptive auditing of AI systems with anytime-valid guarantees](cards.md#paper-154700) | 让中途决定采样和停测仍支持有效检验 |
| 学习理论 | 校准 | [Adaptive Calibration in Non-Stationary Environments](cards.md#paper-151966) | 使误校准上界随环境漂移而变 |
| 强化学习 | 多智能体通信 | [Adaptive Communication Range for Scalable Cooperative Multi-Agent Reinforcement Learning](cards.md#paper-149196) | 先预算内选通信范围再基于实际邻域行动 |
| 音频学习 | 防御检测 | [Adaptive Compression and Targeted Perturbation: A Unified Framework for Generalized Audio Deepfake Detection](cards.md#paper-151194) | 按输入调整检测表征维数 |
| 优化 | 投影无关优化 | [Adaptive Conditional Gradient Sliding: Projection-Free and Line-Search-Free Acceleration](cards.md#paper-148937) | 外层梯度复用多次线性预言机调用 |
| 科学机器学习 | 神经算子 | [Adaptive Coordinate Transforms for Neural Operators](cards.md#paper-156121) | 根据特征变换坐标后再做算子计算 |
| 机器学习 | 分布外检测 | [Adaptive Covariance and Multi-Layer Alignment for Out-of-Distribution Detection](cards.md#paper-151580) | 按层和类内协方差可靠性组合检测分数 |
| 优化 | 变分不等式 | [Adaptive Delayed-Update Cyclic Algorithm for Variational Inequalities](cards.md#paper-150287) | 用一轮前的算子信息减少块间同步 |
| 语言模型 | 推理效率 | [Adaptive Entropy-Sparing for Efficient Reasoning](cards.md#paper-149207) | 分开处理高熵关键阶段与过长后缀 |
| 图学习 | 缺失特征 | [Adaptive Feature Propagation for Attribute-Missing Graph Clustering](cards.md#paper-153408) | 传播时按邻居可信度赋权而非一致平均 |
| 系统 | 资源调度 | [Adaptive Fine-Tuning Scheduler for Multi-Tenant Edge LLM via Convergence-Aware Bandits](cards.md#paper-153654) | 减少给已收敛适配器分配更新 |
| 图学习 | 多模态融合 | [Adaptive Gated Simplicial Propagation for Node Classification in Multimodal Graphs](cards.md#paper-150627) | 门控聚合不同阶关系 |
| 语言模型 | 推理搜索 | [Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification](cards.md#paper-152362) | 按便宜评分的条件成功率决定是否付费核验 |
| 统计学习 | 自适应推断 | [Adaptive Inference for Functionals of M-Estimands](cards.md#paper-151811) | 针对路径依赖方差构造置信区间 |
| 多模态 | 动态读出 | [Adaptive Internal Readout for Native Multimodal Models](cards.md#paper-152986) | 固定读出预算比较内部位点与末层 |
| 强化学习 | 策略检验 | [Adaptive Joint Testing of Policies in Discounted Markov Decision Processes](cards.md#paper-148204) | 按最难区分的价值符号分配探索，再分别停止已获证据的策略。 |
| Agent | 模型路由 | [Adaptive LLM Routing for Multi-Turn Conversations with Continuously Evolving User Queries](cards.md#paper-152859) | 用多轮累计奖励生成路由监督，在线以轻量模型替代搜索。 |
| 优化 | 零阶优化 | [Adaptively Incorporating Directional Hints into Zeroth-Order Optimization](cards.md#paper-149625) | 让不可靠梯度提示作为降方差项，对照强制沿提示更新。 |
| 多模态学习 | 模态平衡 | [Adaptive-Margin Masking and Restoration for Balanced Multimodal Learning](cards.md#paper-151071) | 用可随训练状态变化的间隔决定何时保护弱模态。 |
| 大语言模型 | 缓存压缩 | [Adaptive Mass-Segmented KV Compression for Long-Context Reasoning](cards.md#paper-153325) | 在相同 KV 预算下测分段配额能否减少片段彻底丢失。 |
| 科学机器学习 | 几何表征 | [Adaptive Multi-Frame Learning for Expressive and Stable Atomic Representations](cards.md#paper-152306) | 把几何参考的质量作为聚合输入，并在高对称区域专门测稳定性。 |
| 科学机器学习 | 神经算子 | [Adaptive multiscale operator correction via learned spectral subspace and physics-informed optimization.](cards.md#paper-149265) | 冻结粗算子后只在稀疏谱子空间做物理校正。 |
| 图学习 | 对比学习 | [Adaptive Multi-view Graph Contrastive Learning via Fractional Continuous Dynamics](cards.md#paper-151789) | 把图视图尺度变成可学习的传播参数。 |
| 统计学习 | 差分隐私 | [Adaptive Power Iteration Method for Differentially Private PCA](cards.md#paper-151670) | 为私有谱估计额外检查输入相干性，再选自适应过滤。 |
| 强化学习 | 贝叶斯探索 | [Adaptive Prior Selection in Gaussian Process Bandits with Thompson Sampling](cards.md#paper-150933) | 对 GP 探索比较淘汰与维持超先验不确定性。 |
| 在线学习 | 漂移适应 | [Adaptive Random Forests from Online Learning and Testing by Betting](cards.md#paper-150422) | 把模型池更新时间和替换证据分开设计。 |
| 统计学习 | 回归理论 | [Adaptive Realizable Regression from Two Online Learners](cards.md#paper-151118) | 把损失估计误差也交给在线学习器，并用先验编码结构。 |
| 计算机视觉 | 视频记忆 | [Adaptive Residual Quantization for Memory-Efficient Temporal Action Segmentation](cards.md#paper-150739) | 以任务指标而非仅重建误差验证无标签量化回放。 |
| 大语言模型 | 奖励鲁棒化 | [Adaptive Robust Estimator for Policy Optimization in Reinforcement Learning](cards.md#paper-153985) | 通过奖励污染扫描比较稳健中心与样本均值。 |
| 机器学习系统 | 异步训练 | [Adaptive Scheduling Pipeline For Multi-Instance Asynchronous Reinforcement Learning](cards.md#paper-149603) | 调度异步生成时同时记录填充、尾部和队列空泡。 |
| 强化学习 | 资格迹 | [Adaptive Stepsizes for Eligibility Traces in Deep Reinforcement Learning](cards.md#paper-153394) | 改变资格迹中的学习率前先核对前后向等价条件。 |
| 隐私学习 | 隐私会计 | [Adaptive Target-Charging with Privacy Filters and Individual Accounting](cards.md#paper-155450) | 监测稀少显著偏差时用个体过滤控制可继续查询的隐私预算。 |
| Agent | 可靠性评测 | [Adaptive Test Case Discovery for LLM-Assisted Decision Making in High-Stakes Domains](cards.md#paper-148727) | 把评测预算分配给失败率及多样性均有价值的测试场景。 |
| 统计学习 | 不确定性校准 | [AdaptNC: Adaptive Nonconformity Scores for Conformal Prediction under Distribution Shift](cards.md#paper-150536) | 同时更新预测集合形状与大小，并专门测切换期覆盖。 |
| 计算机视觉 | 全景分割 | [AdapToPASS: Ambiguity-aware Adaptive Spherical Transformer for Panoramic Semantic Segmentation](cards.md#paper-151962) | 把未见球面变换单列为分割鲁棒性测试。 |
| Agent | 求解反馈 | [ADA: Resolving Attribution Ambiguity in End-to-End Power System Dispatch via Two-Time-Scale Stochastic Approximation](cards.md#paper-155823) | 让建模反馈慢于求解决策，分开记录模型与执行错误。 |
| 推荐系统 | 机器遗忘 | [AdaSRU: Adaptive Source-Free Recommendation Unlearning via Gradient-Constrained Optimization](cards.md#paper-154534) | 若无法读取保留数据，用代理效用梯度约束遗忘步并检查偏差。 |
| 时序预测 | 自适应建模 | [AdaST: Adaptive Coupling for Spatial-Temporal Forecasting](cards.md#paper-155866) | 按空间及时间主导程度分组报告预测误差。 |
| 生成模型 | 流式视频 | [AdaState: Self-Evolving Anchors for Streaming Video Generation](cards.md#paper-150868) | 对比固定视觉锚与可演进锚，并同时测运动和身份漂移。 |
| 机器学习系统 | 推测解码 | [AdaTree: Serving-Aware Adaptive Tree Construction for Speculative Decoding](cards.md#paper-153118) | 按负载选择草稿树配置并记录尾延迟与吞吐。 |
| 世界模型 | 少样本适配 | [AdaWM: Few-Shot Adaptation of World Models to Unseen Dynamical Regimes](cards.md#paper-151941) | 先测试按转移示例条件化，再决定是否扩大容量或微调。 |
| 生成模型 | 视频控制 | [AdDirector: Anchored Guidance for Generating Camera-Controllable Advertisement Videos](cards.md#paper-150602) | 控制镜头时把运动锚与外观保持约束分开验证。 |
| 世界模型 | 记忆寻址 | [Addressable Memory for Video World Models](cards.md#paper-152426) | 将缓存保留内容与位置编码分别做干预。 |
| 多智能体学习 | 奖励塑形 | [Addressing Exogenous Variability in Cooperative Multi-Agent Reinforcement Learning](cards.md#paper-149019) | 区分直接控制变量与间接影响变量后再给奖励塑形。 |
| 强化学习 | 探索技能 | [Addressing Sparse-Rewards in RL with Scalable Hierarchical Novel Eigen Options](cards.md#paper-150071) | 用访问稀少程度塑造可扩展的时序探索选项。 |
| 统计学习 | 函数回归 | [A Deep Learning Framework for Scalar-on-Function Models](cards.md#paper-148580) | 采样曲线做回归时分别检查离散网格误差和截断误差。 |
| 机器学习系统 | 无损通信 | [AdERA: Adaptive Exponent Reuse for Lossless Allgather in Sharded MoE Training](cards.md#paper-152302) | 先量化跨步指数重复率，再按每层通信收益选择是否压缩。 |
| 多智能体学习 | 协作评测 | [Ad-Hoc Teamwork from Human Demonstrations](cards.md#paper-148597) | 用多个潜惯例构造评测队友，检查单一代理下的排序是否稳定。 |
