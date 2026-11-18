# NeurIPS 2026

[首页](../../README.md) · [官方会议目录](https://neurips.cc/Downloads/2026)

官方目录当前列出 **9,144** 个论文海报条目，已筛选 **749** 篇，暂收录 **668** 篇。[筛选底册](papers.tsv)按官方海报 ID 记录覆盖及去留。目录可能随会议更新，候选范围核定后统一排名，收录上限为 50%。

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
| 多模态 | 诊断评测 | [A Diagnostic Benchmark for Layered Layout and Template-Variant Reasoning](cards.md#paper-139592) | 将图层与模板变体拆开评测 |
| 三维视觉 | 图监督 | [A Differentiable 3D Scene Graph Metric via Contextual Hellinger Triplet Geometry](cards.md#paper-149490) | 在训练中计量关系结构偏差 |
| 优化 | 可微求解 | [A Differentiable Interior-Point Method in Single Precision](cards.md#paper-151819) | 低精度求解时改变互补条件表示 |
| 语言模型 | 数据配比 | [ADIS-Law: Unified Scaling Laws for Annealing-Phase Domain Injection in Large Language Models](cards.md#paper-150412) | 用拟合规律联合选注入量配比与学习率 |
| 强化学习 | 公平决策 | [A Distribution Mapping Approach to Counterfactually Fair Reinforcement Learning](cards.md#paper-149942) | 策略学习前做分位数反事实校正 |
| 语言模型 | 生成控制 | [AdKnob: Ad Intensity Control and Labeling for LLM-Native Advertising](cards.md#paper-150097) | 将生成强度与输出归因分开评估 |
| 语言模型 | 缓存压缩 | [ADKV: A Low-Overhead Adaptive Delta Quantization for KV Cache in LLM Inference](cards.md#paper-150885) | 用在线元数据替代固定分组 |
| Agent | 记忆审计 | [ADMIT: Support-Gated Memory-Write Admission for Document QA Agents](cards.md#paper-155533) | 审计写入与最终回答两个界面 |
| 优化 | 分布式训练 | [A Doubly Smoothed Decentralized Stochastic Minimax Optimization Algorithm](cards.md#paper-152790) | 让原始与对偶变量共享学习率量级 |
| 计算机视觉 | 三维重建 | [AdpSplit: Error-Driven Adaptive Splitting for Faster Geometry Discovery in 3D Gaussian Splatting](cards.md#paper-152835) | 按高误差区域决定高斯增密数量 |
| 多模态 | 视频评测 | [AdShot: Benchmarking Multimodal Large Language Models for Video Advertisement Clipping](cards.md#paper-139508) | 单独约束生成时长和内容保留 |
| 计算机视觉 | 位置编码 | [A Dual-Domain Vision Transformer with Spectral Positional Bias](cards.md#paper-151216) | 用频谱位置偏置支持变分辨率 |
| 生成模型 | 训练加速 | [Advanced Routing as Regularization Allocation for Efficient Diffusion Transformer Training](cards.md#paper-152568) | 按去噪噪声级分配 token 跳层 |
| 多模态 | 偏好学习 | [Advancing Affordance-Grounded Creative Tool Use in Large Multimodal Models](cards.md#paper-153231) | 用证据约束物体部件的用途推理 |
| 强化学习 | 信用分配 | [Advancing Entropy-Level Credit Assignment in RLVR via Proximal Entropy Policy Optimization](cards.md#paper-150862) | 用局部熵而非全局熵给 token 分配优势 |
| 计算机视觉 | 视频生成 | [Advancing Narrative Long Video Generation via Training-Free Identity-Aware Memory](cards.md#paper-152023) | 长期跨提示生成时追踪显式实体身份 |
| 科学机器学习 | 神经算子 | [Advectra: Asymmetric Latent Transport for Non-Stationary Physics](cards.md#paper-148631) | 在随流坐标系中编码平流场 |
| 科学机器学习 | 鲁棒学习 | [Adversarial Attack and Defense for Machine Learning in Statistical Physics](cards.md#paper-153887) | 约束模型在物理合理局部的输出变化 |
| 强化学习 | 公平评测 | [Adversarial Group Fairness in Contextual Bandits: When Robust is Not Fair](cards.md#paper-152720) | 独立监测群体遗憾与整体指标 |
| 语言模型 | 规划评测 | [Adversarially Attacking Symbolic Vocabulary Vulnerabilities In LLM Planners](cards.md#paper-154285) | 测规划能力对等价符号改名的稳定性 |
| 优化 | 分布式训练 | [Adversary-Robust Learning from Fully Asynchronous Directional Derivative Estimates](cards.md#paper-154942) | 异步环境使用方向投影符号更新 |
| 语言模型 | 裁判防护 | [AdvJudge-Zero: Binary Decision Flips in LLM-as-a-Judge via Adversarial Control Tokens](cards.md#paper-150552) | 按不同失败形态覆盖防护训练样本 |
| 学习理论 | 循环策略 | [A dynamical systems theory of reward-modulated learning in linear recurrent networks](cards.md#paper-151421) | 按任务时域选循环规模 |
| 优化 | 多目标搜索 | [A Dynamic Decomposition Strategy for the MOEA/D With Proven Performance Guarantees](cards.md#paper-151518) | 搜索中更新目标分解 |
| 生成模型 | 推理缓存 | [AEGIS: Adaptive Efficient Generative Inference Scheduling for Structured Latent Models](cards.md#paper-155172) | 按样本难度和累计复用偏差刷新缓存 |
| 强化学习 | 离线安全 | [AEGIS: Almost Surely Safe Offline Reinforcement Learning](cards.md#paper-152975) | 让同一策略消费多种可行安全预算 |
| 生成模型 | 路径约束 | [AegisFlow: Training-free Non-myopic Path-safe Guided Flow Matching](cards.md#paper-149715) | 在全轨迹目标中加入时变屏障 |
| 联邦学习 | 隐私防护 | [Aegis: Generative Gradient Masking for Privacy-Preserving Medical Federated Learning](cards.md#paper-148730) | 在客户端更新附加合成样本贡献 |
| Agent | 信用分配 | [AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning](cards.md#paper-154854) | 按完整响应的熵信号调节优势 |
| 计算机视觉 | 动态世界模型 | [AEON: Unifying Video and 3D World Models](cards.md#paper-148481) | 让视频生成潜变量输出持久可渲染三维状态 |
| 语言模型 | 主动标注 | [AERO: Adaptive Ensemble-Disagreement Routing for Oracle Feedback in Sample-Efficient Online RLHF](cards.md#paper-153918) | 用奖励模型分歧路由人工反馈 |
| 科学机器学习 | 状态估计 | [AeroChem: Closed-loop Physics-Informed State Space Modeling for Long-term Chemically-Reactive Air Quality Forecasting](cards.md#paper-153606) | 每步校正物理状态并把后验送回模拟 |
| 科学机器学习 | 时空融合 | [AeroMosaic:Transport-Aware Multimodal Evidence Fusion for Atmospheric Pollution Risk Inference](cards.md#paper-154525) | 按风向构建每日有向依赖 |
| 多模态 | 评价学习 | [AesGI-Bench: Benchmarking and Evaluating the Aesthetic Quality of AI-Generated Images via Large Multimodal Models](cards.md#paper-138910) | 从含平局的配对偏好学多维分数 |
| 科学机器学习 | 诊断评测 | [AET-Bench: Pixel-Accurate Atomic Tomography Is Not Atom-Accurate](cards.md#paper-139587) | 以原子召回等任务指标选断层重建模型 |
| 强化学习 | 多目标优化 | [AETDICE: Unified Framework and Offline Optimization for Nonlinear Multi-Objective RL](cards.md#paper-150928) | 显式区分聚合、期望和变换的顺序 |
| 因果推断 | 图算法 | [A Faster Algorithm for the Half-Trek Criterion in Structural Causal Models](cards.md#paper-152110) | 用等价边级判据加速可识别性检查 |
| 生成模型 | 采样 | [A Favorable Regime Between ODE and SDE for Few-Step Diffusion Sampling](cards.md#paper-152991) | 少步生成选择有界且中等扩散强度的驱动 |
| 大语言模型 / Agent | 示范采样 | [A Few Teacher Steps Go a Long Way: Cost-Efficient On-Policy Data Augmentation for Agent Post-Training](cards.md#paper-150832) | 在学生到达的状态采样短教师续写。 |
| 模型可靠性 | 形式化验证 | [Affine-Image Propagation for Tight and Scalable $\ell_{2}$ Neural Network Verification](cards.md#paper-150286) | 在层间传播仿射几何，减少欧氏扰动集放松带来的损失。 |
| 优化 / 理论 | 二阶优化 | [Affine-invariant Cubic Newton with Weak Learners](cards.md#paper-150741) | 用优化路径的方向质量评价弱学习器的二阶步。 |
| 概率建模 | 数值线性代数 | [Affine Tracing: A New Paradigm for Probabilistic Linear Solvers](cards.md#paper-150970) | 将迭代求解器自动转换成可传播不确定性的仿射迭代。 |
| 自动机器学习 | 架构搜索 | [Agentic Neural Architecture Search](cards.md#paper-154949) | 让语言模型输出可替换模块槽，再由搜索算法局部优化。 |
| 多模态 / 检索 | 按需解析 | [AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generation](cards.md#paper-153107) | 检索后只解析与查询相关的视觉区域。 |
| 多模态 / Agent | 工作流评测 | [AgenticVBench: Can AI Agents Complete Real-World Video Production Tasks?](cards.md#paper-139672) | 将程序化检查与专家质评结合评估视频生产。 |
| 自动机器学习 | 代码性能评测 | [AgentKernelArena: Benchmarking Performance and Generalization of AI Coding Agents on GPU Kernels Optimization](cards.md#paper-139376) | 先验证编译和数值正确性，再测未见配置的速度。 |
| 大语言模型 / Agent | 推理缓存 | [AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems](cards.md#paper-155404) | 按结构化记忆单元校正复用的 KV 缓存。 |
| 机器人学 | 数据生成 | [AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation](cards.md#paper-139222) | 按后续动作需要的接触区域采样抓取。 |
| 优化 | 非光滑优化 | [A Frank-Wolfe Approach to Goldstein Stationarity](cards.md#paper-150421) | 需要随时停止时，输出精度单调改进的驻点序列。 |
| 大语言模型 | 剪枝重建 | [A Free Lunch in LLM Compression: Revisiting Retraining after Pruning](cards.md#paper-150765) | 重建窗口至少覆盖一个非线性子模块。 |
| 多模态学习 | 表征解释 | [A General Concept-based Decomposition for Vision–Language Embeddings](cards.md#paper-151861) | 以样本间关系监督概念分解。 |
| 计算机视觉 | 光谱重建 | [A General Filter-Enhanced Approach to Smartphone Hyperspectral Imaging](cards.md#paper-149649) | 以互补物理滤光片改善多相机的可观测性。 |
| 图学习 | 可解释传播 | [A Generalized Tikhonov Layer for Interpretable-by-design Graph Neural Networks](cards.md#paper-148963) | 用节点保真权重和拓扑滤波响应解释信息来源。 |
| 概率建模 | 核方法 | [A general kernel framework for non-CND distance measures using $&#124;\mathcal{D}&#124;$-dimensional sparse landmark embeddings](cards.md#paper-153150) | 将非 CND 距离先映射到稀疏特征。 |
| Agent | 隐私评测 | [A Generative Model of Contextual Integrity: Appropriate vs. Inappropriate Information Sharing](cards.md#paper-148966) | 同时测阻止不当披露与允许合规共享。 |
| Agent | 研发评测 | [Agent$^2$ RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?](cards.md#paper-139513) | 固定实验预算，分开测监督训练及在线强化学习。 |
| Agent | 训练反馈 | [Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback](cards.md#paper-155447) | 以交互式执行验证生成的符号世界模型。 |
| Agent | 拒绝评测 | [AgentAbstain: Do LLM Agents Know When Not to Act?](cards.md#paper-139558) | 构造同任务的应执行与应拒绝成对变体。 |
| 大语言模型 / Agent | 过程蒸馏 | [AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent](cards.md#paper-149790) | 以训练期蒸馏替换部署时的多智能体过程。 |
| Agent / 评测 | 过程诊断 | [AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation](cards.md#paper-138951) | 将测试通过率与轨迹质量分开 |
| Agent / 安全 | 防御控制 | [Agent MechSuits : Mechanistic Subspace Safety Steering for Multi-Turn CLI Agents](cards.md#paper-154113) | 把风险监测放进多轮执行过程 |
| Agent / 安全 | 故障评测 | [Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents](cards.md#paper-151325) | 把普通环境故障纳入安全回归 |
| Agent / 评测 | 持续学习 | [AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents](cards.md#paper-148896) | 把部署中学到的知识与初始能力分开测 |
| Agent / 可靠性 | 故障归因 | [AgenTracer-v2: Agentic Failure Tracer for LLM Agentic Systems](cards.md#paper-153890) | 对超长日志进行主动检索和分步归因 |
| Agent / 系统 | 并发协作 | [AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace](cards.md#paper-148882) | 共享状态上增加归属和进度广播 |
| 软件工程 | 静态分析 | [Agents as Neuro-Symbolic Reasoners: Path Feasibility Reasoning for Precise Static Bug Detection](cards.md#paper-153256) | 以局部符号推理验证静态告警 |
| Agent / 安全 | 系统隔离 | [Agent Security is a Systems Problem](cards.md#paper-140106) | 在模型外强制权限边界 |
| Agent / 评测 | 工作流考核 | [Agents' Last Exam](cards.md#paper-139517) | 用可核验结果测整段专业工作流 |
| Agent / 机器学习 | 半监督搜索 | [AgentSSL: Can MLE Agents Leverage Unlabeled Data?](cards.md#paper-154115) | 在标签不足时单测 Agent 能否利用无标签数据 |
| 推荐系统 | 长尾排序 | [AgentTailor: Dual-Gate LLM-Assisted Re-ranking for Personalized Long-Tail Recommendation](cards.md#paper-154386) | 分开测候选召回与长尾重排 |
| Agent / 安全 | 监测学习 | [Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning](cards.md#paper-152173) | 从历史监测经验训练行为监督器 |
| 多模态 / Agent | 评测构造 | [AgentVista: Evaluating Multimodal Agent in Ultra-Challenging Realistic Visual Scenarios](cards.md#paper-153463) | 要求工具决策引用细粒度视觉证据 |
| Agent / 系统 | 推理调度 | [AgentWeave: Efficient Distributed Agent Serving via Flow Decomposition](cards.md#paper-151244) | 按工作流模块区分流水气泡与请求阻塞 |
| 强化学习 | 预条件优化 | [A Geometric Perspective on Reward Function Updates in Inverse Reinforcement Learning](cards.md#paper-149606) | 用占用分布几何构造奖励更新预条件 |
| 图机器学习 | 表征诊断 | [Aggregation Dispersion: An Information-Geometric Diagnostic of Oversmoothing in Graph Neural Networks](cards.md#paper-154195) | 用传播分布的几何离散度测过平滑 |
| 强化学习 | 多智能体激励 | [AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games](cards.md#paper-154175) | 允许按状态拒绝部分转移奖励 |
| 学习理论 | 不可实现性分析 | [Agnostic Language Identification and Generation](cards.md#paper-148502) | 按数据可能不属于任何候选语言重定义目标 |
| 学习理论 | 选择性预测 | [Agnostic Online Learning with Reliable Abstention](cards.md#paper-152256) | 同时优化总误判与随机样本上的弃权 |
| 图机器学习 | 无监督迁移 | [A Graph Foundation Model for Unified Clustering](cards.md#paper-154668) | 预训练同时兼顾节点与图级信息 |
| 机器学习评测 | 选择偏差 | [Agreement without Coverage: Conditional Agreement is Non-Identifying in Variable-Support Structured Extraction](cards.md#paper-152893) | 一致率同时报告覆盖、召回与输出规模 |
| 多模态学习 | 融合校准 | [Agree to Disagree: Multimodal Autonomous Negotiation and Calibration for Entity Representation Learning](cards.md#paper-151043) | 保留模态独有残差后再按证据融合 |
| 优化 | 最优传输 | [A Grid Efficient Transport Optimization Model for the Wasserstein Barycenter Problem](cards.md#paper-153536) | 网格支持下改用精确紧凑线性规划 |
| 强化学习 | 泛化评测 | [AgriManager: A Framework and Benchmark for LLM-RL Generalization in Agricultural Management](cards.md#paper-139010) | 单独测观测、动作与奖励接口变化 |
| 多模态学习 | 尺度诊断 | [AgroOmni: A Large-Scale Multi-view Agricultural Dataset for Cross-Scale Multimodal Reasoning](cards.md#paper-139411) | 将近景、无人机和卫星样本分层测语义稳定性 |
| 认知建模 | 可塑记忆 | [A Hebbian Recurrent Neural Network Explains the Hierarchical Geometry of Sequence Memory](cards.md#paper-149363) | 用组内与组间位置分别测试分层记忆机制 |
| 科学机器学习 | 层级分词 | [A Hierarchical Tokenization Framework for Voxel-Level fMRI Representation Learning](cards.md#paper-153906) | 高压缩率时保留体素局部信息与跨脑区组织 |
| 世界模型 | 分层预测 | [A Hierarchical World Model for Driving](cards.md#paper-151694) | 用长时粗语义预测约束短时细节 |
| 机器学习 | 不确定性归因 | [A Hierarchy of Entropy-Shapley Games for Multivariate Predictive Uncertainty](cards.md#paper-153980) | 对边缘不确定性和依赖结构分别归因 |
| 生成模型 | 训练监督 | [AHPA: Adaptive Hierarchical Prior Alignment for Diffusion Transformers](cards.md#paper-149646) | 根据噪声水平切换对齐粒度 |
| Agent / 安全 | 防御评测 | [AI Agents May Always Fall for Prompt Injections](cards.md#paper-154053) | 验证模型侧过滤之外的系统权限 |
| 计算机视觉 / 数据策略 | 主动学习 | [Active Learning as Nullspace Regulation: A Spectral Representation Perspective](cards.md#paper-152553) | 选择跨轮次仍处在标注表示弱覆盖方向的样本。 |
| 可解释性 | 正则化 | [A Curvature Phase Transition Governs Coherence Penalty Efficiency Against Feature Absorption in SAEs](cards.md#paper-153574) | 根据吸收态附近的分裂曲率选 coherence 惩罚的幂指数。 |
| 大语言模型 | 稀疏推理 | [AdaCal: Adaptive Calibration for Robust Sparse Attention in Long-Context LLMs](cards.md#paper-155964) | 用轻量探针决定哪些注意力头需要补充远距离覆盖。 |
| 科学机器学习 | 等变生成 | [3D Molecule Generation from Rigid Motifs via $\mathrm{SE}(3)$ Flows](cards.md#paper-156034) | 比较刚性片段和单原子两种建模粒度。 |
| 大语言模型 | 量化 | [ACQueReLlo: Alignment-Aware Constrained Quantization via Reinforcement Learning for Large Language Models](cards.md#paper-154964) | 选择混合位宽时同时约束能力、拒答与误拒。 |
| 学习理论 | 结构约束 | [A Cross-Interaction Neural Architecture for Submodular Functions](cards.md#paper-148925) | 在保留单调次模性的同时显式建模成对交互。 |
| Agent | 错误定位 | [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](cards.md#paper-155358) | 用并行小型诊断头输出错误位置及原因以支持执行前纠偏。 |
| 具身智能 | 动作表示 | [Action Images: End-to-End Policy Learning via Multiview Video Generation](cards.md#paper-150968) | 把控制轨迹渲染为多视角动作图像，使视频骨干直接预测控制。 |
| 推荐系统 | 时序记忆 | [Action-On-Item Preference Flow: A Shared Event Schema for Predictive and Generative Personalization](cards.md#paper-148195) | 把多任务交互写成统一事件并分开维护长期、短期和情节痕迹。 |
| 具身智能 | 连续控制 | [ActionUNet: Improving Robustness of VLA Models with Efficient Multi-scale Fine-tuning](cards.md#paper-149076) | 多尺度融合后用连续动作解码约束二阶平滑。 |
| 学习理论 | 表示动力学 | [Activation Functions Shape Token Synchronization in Stochastic Transformer Dynamics](cards.md#paper-150979) | 在模型深度增长时检查激活选择是否改变 token 表示同步。 |
| 生成模型 | 安全控制 | [Activation Steering of Video Generation Models via Reduced-Order Linear Optimal Control](cards.md#paper-150198) | 按生成过程的反馈约束干预幅度，兼顾内容安全与视频质量。 |
| 图学习 | 主动采样 | [Active Corpus Selection for Training Subgraph Retrievers Using OOD Queries](cards.md#paper-153257) | 在精确匹配预算极低且正例稀少时优先获取正例标签。 |
| 计算成像 | 压缩感知 | [Active Learning for Conditional Generative Compressed Sensing](cards.md#paper-149778) | 分别选定用于测量设计和用于逆问题重建的提示。 |
| 主动学习 | 概率建模 | [Active Learning for Gaussian Process Regression Under Self-Induced Boltzmann Weights](cards.md#paper-152717) | 当评测权重依赖未知响应时，按推断的目标分布选择查询。 |
| 学习理论 | 弱监督 | [Active Learning From Positive and Unlabeled Examples](cards.md#paper-154434) | 把仅有部分正例能得到确认的查询与标准主动学习分开分析。 |
| 主动学习 | 分布预测 | [Active Learning of Conditional Generative Models via the Transport Neural Tangent Kernel](cards.md#paper-151935) | 输出为分布时按均值和形状的不确定性共同挑选输入。 |
| 计算机视觉 | 主动检索 | [Active Learning via Classifier Impact and Greedy Selection for Interactive Image Retrieval](cards.md#paper-156770) | 按候选对分类器的影响进行批内贪心标注。 |
| 时序建模 | 记忆机制 | [Active Memory Feedback Loop for Fast–Slow Dynamics in Liquid Neural Networks](cards.md#paper-148250) | 让关联记忆影响下一步 recurrent 更新，而非只扩充输出头。 |
| 具身智能 | 视频动作表征 | [ActO: Extracting Action Representations from MLLM Embeddings for Video World Models](cards.md#paper-149590) | 优先适配预训练视频语言表征，并直接评估动作与场景分离。 |
| 强化学习 | 连续控制 | [Actor-Accelerated Policy Dual Averaging for Reinforcement Learning in Continuous Action Spaces](cards.md#paper-155769) | 用学习型 actor 近似在线优化。 |
| 世界模型 | 记忆更新 | [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](cards.md#paper-154417) | 按交互事件价值保留历史。 |
| 优化 | 自适应正则 | [AdaCubic: An Adaptive Cubic Regularization Optimizer for Deep Learning](cards.md#paper-156754) | 动态调节三次牛顿正则权重。 |
| 多模态学习 | 目标对齐 | [AffectGPT-RL: Revealing Roles of Reinforcement Learning in Open-Vocabulary Emotion Recognition](cards.md#paper-149766) | 直接用不可微情绪评价构造训练奖励。 |
| Agent | 离线信用分配 | [AgentBrew: Offline Tool-Use Agent Learning from Raw Real-World Trajectories](cards.md#paper-148366) | 按动作对事后任务的贡献加权原始轨迹。 |
| 优化 | 因果贝叶斯优化 | [AgentCBO: Causal Belief Routing for Bayesian Optimization under Unknown Graphs](cards.md#paper-155417) | 优先校正会改变干预选择的图结构。 |
| Agent | 过程评测 | [AgentCollabBench: Diagnosing When Good Agents Make Bad Collaborators](cards.md#paper-139450) | 比较信息在不同协作拓扑下的保留。 |
| 多模态学习 | 强化学习 | [Agent Explorative Policy Optimization for Agentic Multimodal Reasoning](cards.md#paper-151150) | 对全错工具分支冻结思考前缀并重采样。 |
| Agent | 在线审计 | [AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems](cards.md#paper-151949) | 只用当前前缀检测最早决定性错误。 |
| Agent | 提示优化 | [AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems](cards.md#paper-153633) | 先以单代理干预定位失败来源，再按语义归类反馈。 |
| Agent | 评测诊断 | [AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Scientific Question Answering](cards.md#paper-139240) | 在同一资源预算下拆分检索和综合表现。 |
| Agent | 停止决策 | [Agentic Abstention: Do Agents Know When to Stop Instead of Act?](cards.md#paper-150912) | 把及时弃权与最终弃权分开测量。 |
| 推理 | 神经符号验证 | [Agentic Geometry Problem Solving via Human-like Parallel Bidirectional Reasoning](cards.md#paper-148892) | 把前推和目标反解复用同一套可验证定理接口。 |
| 可解释性 | 模型选择 | [Agentic-imodels: Evolving agentic interpretability tools via autoresearch](cards.md#paper-154318) | 把模型文本能否支持正确行为预测纳入选择。 |
| 强化学习 / Agent | 交互评测 | [Agentick: A Unified Benchmark for General Sequential Decision-Making Agents](cards.md#paper-138948) | 在统一任务下同时报告能力维度与观测格式差异。 |
| Agent | 偏好优化 | [Agentic Multi-Turn Reasoning: A Fairness Approach](cards.md#paper-149499) | 把多轮信用分配和罕见轨迹失衡纳入同一目标。 |
| Agent | 奖励验证 | [Agentic Reward Modeling: Verifying GUI Agent via Progressive Trajectory-Grounded Interaction](cards.md#paper-155392) | 轨迹证据不足时才让验证器探查环境状态。 |
| 视觉 / Agent | 条件规划 | [Agentic Video Editing from Underspecified Requests](cards.md#paper-149555) | 先把模糊编辑请求转成生成器可执行条件。 |
| 人机协作 | 决策建模 | [AI-Assisted Classification under Correlation Neglect and Trust](cards.md#paper-152625) | 上线前分别估计信号重叠和用户信任。 |
| 评测 | 测量本体 | [AI Construct Lexis: An Ontology of the Hidden Assumptions in AI Evaluation](cards.md#paper-139045) | 发布基准时显式记录指标与声称测量概念的关系。 |
| 可靠性 | 审计设计 | [AI Control for Sandbagging on Fuzzy Tasks](cards.md#paper-151011) | 用独立强判据检查弱评审器是否掩盖质量下跌。 |
| 评测 | 逐题分析 | [AI Evaluation Should Require Standardized Item-Level Data Releases](cards.md#paper-140079) | 保留逐题输出以验证汇总分数的含义。 |
| 科学机器学习 | 捷径诊断 | [AI for Drug Discovery Models Often Do Not Learn as Expected and How to Diagnose These Failure Modes](cards.md#paper-140017) | 验证模型是否学到目标因素时加入故意错位的对照。 |
| 多模态 / Agent | 开放评测 | [AI GAMESTORE: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games](cards.md#paper-138879) | 用开放游戏集和等经验的人类对照分开衡量能力。 |
| 可靠性 | 分布偏移 | [AI-Generated Content Should Be Evaluated by Its Substance, Not Its Source](cards.md#paper-140027) | 跨文风验收文本来源判断，并将事实验证单列。 |
| 安全治理 | 能力评测 | [AI Governance Should Prioritize Control and Knowledge Boundaries Over Limiting Intelligence](cards.md#paper-140009) | 分别审计推理能力、外部知识访问与执行权限。 |
| 多模态 / Agent | 通信路由 | [AIM: Adaptive Interaction in Multi-Agent Debate for Multimodal LLM Inference](cards.md#paper-152673) | 按实例选择文本、结构或原模态局部证据传递。 |
| 人机交互 | 群体影响评测 | [AI-Mediated Communication Can Steer Collective Opinion](cards.md#paper-155808) | 上线文本编辑器前评估细小偏差在多轮网络交流中的累积。 |
| Agent | 实验调度 | [AIRA 2: Overcoming Bottlenecks in AI Research Agents](cards.md#paper-152980) | 让搜索并发提速时同时提高候选选择评估的一致性。 |
| 架构搜索 | 多保真搜索 | [AIRA-Compose: Agentic Discovery of Neural Architectures](cards.md#paper-152477) | 用小规模候选粗排，再以固定预算扩大模型复验。 |
| 视觉 / Agent | 主动核验 | [AirIAD: Agentic Iterative Reasoning for Industrial Anomaly Detection](cards.md#paper-153593) | 诊断时按需补取局部图像与知识并相互核验。 |
| 科学机器学习 | 条件预报 | [AirMPA: A Meteorology-to-Pollution Adapter for Global Air Quality Forecasting](cards.md#paper-154614) | 将外部气象预报作为可替换的污染物预测条件。 |
| 多模态学习 | 表征对齐 | [AIR: Rethinking Image-Text Offset Alignment in Multimodal Contrastive  Representation Space](cards.md#paper-151241) | 先测概念距离导致的偏移失配，再调整文本方向。 |
| 统计学习 | 不确定性校准 | [A Kernel Nonconformity Score for Multivariate Conformal Prediction](cards.md#paper-151235) | 多维残差呈非椭圆形时，用核分数校准联合预测区间。 |
| 大语言模型 / 统计学习 | 审计校准 | [AKTD: FDR Control for LLM Training Data Detection under Approximate Exchangeability](cards.md#paper-148953) | 用独立的未入训样本估计审计统计量的不对称，再校准发现阈值。 |
| 具身智能 | 潜动作 | [ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models](cards.md#paper-152511) | 用可组合转移作为动作生成的辅助目标 |
| 安全评测 | 数据泄漏诊断 | [A Large-Scale Multi-Source Dataset Linking Hacker Community Discourse to the CVE Vulnerability Lifecycle](cards.md#paper-139194) | 以时间和事件 ID 双重隔离验证防御性情报分类 |
| 神经科学 / 强化学习 | 探索先验 | [A latent control model for realistic rodent motion](cards.md#paper-148187) | 把控制用运动先验和随机探索先验分开 |
| 大语言模型 / Agent | 可靠性 | [A Latent-Load Framework for Reliability Analysis and Intervention Design in LLM Pipelines](cards.md#paper-154404) | 按估计的错误传播收益配置有限检查点 |
| 具身智能 | 潜世界模型 | [A Latent World-Action Model with Jointly Aligned Reasoning](cards.md#paper-149267) | 用训练期未来视觉指导可部署的潜查询 |
| 科学机器学习 | 评测 | [ALETHEIA: A Multi-Frequency Eddy Current Pulsed Thermography Dataset for Neural Operator Learning in Nondestructive Testing](cards.md#paper-139797) | 按激励频率、网格和仿真到实测拆分神经算子测试 |
| 学习理论 | 代数学习 | [Algebraic Machine Learning: learning as computing subsets of the subdirect decomposition from Abstract Algebra](cards.md#paper-150997) | 用同一公理接口表示训练样本和形式约束 |
| 大语言模型 | 推理路由 | [AlgoPilot: Cross-Paradigm Reasoning in Language Models via Strategy Selection and Guidance](cards.md#paper-154391) | 将范式选择和形式化指导与执行模型分离 |
| 强化学习 | 队列调度 | [Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret](cards.md#paper-151449) | 用预设截止点停止随机探索，后段只用置信探索 |
| 对齐 / 社会选择 | 福利优化 | [Algorithmic Impact Reveals the Hidden Structure of Alignment](cards.md#paper-150980) | 将群体对齐规则比较转成后果与外部性约束的优化 |
| 优化 | 迭代诊断 | [Algorithms for Linear Equations with Min and Max Operators Under (Absolutely) Halting Condition](cards.md#paper-155929) | 按停止条件区分能安全使用的值迭代和策略迭代 |
| 计算机视觉 | 逆问题 | [Align $\&$ Invert: Solving Inverse Problems with Diffusion and Flow-based Models via Representation Alignment](cards.md#paper-148851) | 用近似目标的语义特征引导预训练生成先验 |
| 视觉 / 多模态 | 模态对齐 | [Align3D-AD: Cross-Modal Feature Alignment and Dual-Prompt Learning for Zero-shot 3D Anomaly Detection](cards.md#paper-152960) | 渲染与真实 RGB 保持独立提示并进行对齐 |
| 计算机视觉 | 评测 | [Align and Distill: Unifying and Improving Domain Adaptive Object Detection](cards.md#paper-156740) | 先统一训练协议并增强基线，再比较域适应方法 |
| 科学机器学习 | 条件生成 | [Align as You Couple: Learning Spatial Resolved Inference from H&E Images with Mollified Flow Matching](cards.md#paper-149664) | 用输入相关序列先验替代各向同性噪声作为流匹配起点 |
| 大语言模型 | 联邦学习 | [Align Before Aggregation: Basis-Consistent Federated LoRA under Heterogeneous Ranks](cards.md#paper-154308) | 下发不同秩前先对齐客户端与全局参考的前缀基 |
| 具身智能 | 轨迹规划 | [AlignDrive: Aligned Lateral-Longitudinal Planning for End-to-End Autonomous Driving](cards.md#paper-152098) | 先定横向路径，再沿路径预测纵向位移 |
| 具身智能 | 世界模型 | [Aligned Delta-Triplane Transformers as Occupancy World Models](cards.md#paper-152382) | 先补偿自运动，再预测占据变化 |
| 大语言模型 | 联邦学习 | [Aligned LoRA Updates via Intrinsic Geometry for Federated Low-Rank Adaptation](cards.md#paper-150662) | 测量客户端更新子空间冲突再选择聚合和本地约束 |
| 大语言模型 / Agent | 可靠性 | [Aligning AI Teams](cards.md#paper-154600) | 指定系统级安全负责人并记录可检查的规格 |
| 生成模型 / 强化学习 | 生成对齐 | [Aligning Few-Step Generative Model via Amortizing Sample-Based Variational Inference](cards.md#paper-155747) | 用样本粒子更新替代依赖似然的少步生成后训练。 |
| 强化学习 | 策略适配 | [Aligning Flow Map Policies with Optimal $Q$-Guidance](cards.md#paper-149374) | 在保持离线策略信赖域的同时，用评论器解析目标适配单步生成。 |
| 多模态学习 | 局部对齐 | [Aligning Forest and Trees in Images & Long Captions for Visually Grounded Understanding](cards.md#paper-155656) | 在中间层对齐文本片段和区域，在终层对齐整图和长描述。 |
| 序列建模 | 初始化 | [Aligning Inductive Bias for Data-Efficient Generalization in State Space Models](cards.md#paper-150462) | 按任务信号的功率谱初始化状态空间模型。 |
| 大语言模型 | 评测设计 | [Aligning Language Model Benchmarks with Pairwise Preferences](cards.md#paper-139753) | 用历史模型的下游成对排序重新加权静态题目。 |
| 大语言模型 | 选择性预测 | [Aligning Language Models with Selective Prediction](cards.md#paper-148722) | 将风险覆盖曲线面积作为后训练目标。 |
| 大语言模型 / Agent | 信用分配 | [Aligning LLMs Toward Multi-Turn Conversational Outcomes Using Iterative RLHF](cards.md#paper-151436) | 用对话级 Q 估计作为单轮 GRPO 的奖励。 |
| 大语言模型 | 数据重加权 | [Aligning LLMs with Biomedical Knowledge using Balanced Fine-Tuning](cards.md#paper-149582) | 区分集中出现的知识不确定性和孤立风格不确定性，再分配训练预算。 |
| 多模态学习 | 理由监督 | [Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived Semantic Dimensions](cards.md#paper-152778) | 以人的行为维度标注相似性判断理由。 |
| 大语言模型 | 部署安全评测 | [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](cards.md#paper-150322) | 把对齐回归加入 KV 缓存量化验收。 |
| 大语言模型 | 训练诊断 | [Alignment Dynamics in LLM Fine-Tuning](cards.md#paper-150384) | 在连续微调时监测对齐反转与再接触后的恢复速度。 |
| 自然语言处理 | 生成文本检测 | [Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy](cards.md#paper-151776) | 用对齐模型与基础模型的标准化似然差替代单模型似然。 |
| 可信人工智能 | 医疗评测 | [Alignment Is Not Enough for Safe Medical LLM Evaluation](cards.md#paper-140065) | 在总体专家一致性之外增加临床错误分层和提示稳定性检查。 |
| 时间序列 | 检索对齐 | [Align-RAG: Alignment Is All You Need for TSFM In-Context Learning](cards.md#paper-152416) | 给冻结预测器使用检索示例前先闭式对齐振幅和相位。 |
| 推荐系统 | 持续遗忘 | [ALIGN-Rec: Continual Recommendation under Heterogeneous Unlearning Requests](cards.md#paper-153461) | 在未来学习更新时监控已删除信号是否恢复。 |
| 机器学习理论 | 稳健优化 | [A Little Robustness Is All You Need: Leveraging Predictions for Contextual Optimization](cards.md#paper-150467) | 低预测误差仍不可直接跟随预测时，在预测邻域做稳健选策。 |
| 生成模型 | 高效推理 | [All-Addition Spiking Diffusion Models with Attention Enhancement](cards.md#paper-154963) | 把扩散网络的注意力和捷径一并改造成可加推理。 |
| 大语言模型 | 推理干预 | [Alleviating Hallucination with Training-Free Uncertainty-Guided Steering](cards.md#paper-148795) | 让现成置信度估计参与推理修正，再分别验证准确率和校准。 |
| 计算机视觉 | 图像复原 | [All-in-one Adverse Weather Removal via Prior-modulated and Velocity-constrained Rectified Flow](cards.md#paper-149069) | 用软退化估计条件化复原，并以残差流细化。 |
| 多模态 | 坐标变换 | [Allocentric Perceiver: Disentangling Allocentric Reasoning from Egocentric Visual Priors via Frame Instantiation](cards.md#paper-153797) | 把视角转换交给几何工具 |
| 多模态 | 工具推理 | [AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models](cards.md#paper-154004) | 为需要持续查询的空间推理维护外部结构 |
| Agent 安全 | 组合评测 | [Alloy Agents Can Be More Dangerous Than Either Model Alone](cards.md#paper-153761) | 在封闭评测中分别检查单步和持续多步风险 |
| 具身智能 | 探索规划 | [All Roads Lead to Rome: Flow-driven Multi-Anchor Exploration for Open-Environment Active 3D Mapping](cards.md#paper-151339) | 部分可观测时保留多个长程探索候选 |
| 强化学习 | 收敛理论 | [Almost Sure Convergence of Linear Temporal Difference Learning with Arbitrary Features](cards.md#paper-156657) | 把参数可辨识性和价值预测一致性分开 |
| 强化学习 | 随机逼近 | [Almost Sure Convergence Rates of Stochastic Approximation and Reinforcement Learning via a Poisson-Moreau Drift](cards.md#paper-151239) | 在马尔可夫噪声下比较步长衰减 |
| 表示学习 | 局部优化 | [A Local Geometric Analysis of Maximal Coding Rate Reduction via Error Bounds](cards.md#paper-155476) | 用梯度范数诊断编码率目标的局部收敛 |
| 量子机器学习 | 自然梯度 | [A Locality-Aware Surrogate for Natural-Gradient Descent in Quantum Optimization](cards.md#paper-155416) | 在有限测量预算下保留部分跨块耦合 |
| 时间序列 | 来源校验 | [A Locally Tokenized Generative Model for Robust Time-Series Watermarking](cards.md#paper-150316) | 用局部编码减少常规编辑对来源检验的影响 |
| 强化学习 | 多目标搜索 | [AlphaPareto: Formulaic Alpha Discovery with LLM-Guided Multi-Objective Reinforcement Learning](cards.md#paper-153971) | 变化的候选集合也应作为策略状态 |
| 优化 | 结构化搜索 | [AlphaPROBE: Alpha Mining via principled retriveval and on-graph biased evolution](cards.md#paper-150234) | 用候选的演化图去重并选择下一轮种子 |
| 大语言模型 | 量化 | [AlphaQ: Calibration-Free Bit Allocation for Mixture-of-Experts Quantization](cards.md#paper-150665) | 缺少校准数据时用权重谱分配专家精度 |
| 大语言模型 | 时序评测 | [ALTER: An Allen's Algebra-Based Evaluation Framework for Temporal Reasoning of LLMs](cards.md#paper-139265) | 随机改叙述顺序来排查时序捷径 |
| 持续学习 | 表示诊断 | [A Mahalanobis Margin \texorpdfstring{$\gamma_{\min}$}{gamma\_min} Bound on Task Confusion in Pretrained Class-Incremental Learning: From Infeasibility to Exponential Attenuation](cards.md#paper-151690) | 用最差任务间 Mahalanobis 间隔预测类别混淆 |
| 计算机视觉 | 数据评测 | [AmaraSpatial-10K: A Spatially and Semantically Aligned 3D Dataset for Spatial Computing and Embodied AI](cards.md#paper-139345) | 把物理可用性与语义检索分开验收资产 |
| 大语言模型 | 低秩适配 | [A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)](cards.md#paper-155103) | 沿正则强度观察旧任务和新任务分类间隔 |
| 大语言模型 | 模型合并 | [AMARIS: Merging Generalist and Specialist LLMs via Adaptive Subspace Inheritance](cards.md#paper-154547) | 按激活方向选择性继承专家更新 |
| 多模态学习 | 数据审计 | [A Matched-Budget Audit Framework for Recaptioned Image-Text Supervision Distributions](cards.md#paper-139543) | 固定描述预算，比较重写图文数据的内容覆盖与图像支持度。 |
| 学习理论 | 泛化诊断 | [A mathematical theory of balancing relational generalization and memorization](cards.md#paper-153152) | 同时用新关系组合和显式反例测试规则外推。 |
| 大语言模型 / 教育 | 人机评测 | [A Matter of Interest: Understanding Interestingness Judgments of Math Problems in Humans and Language Models](cards.md#paper-153251) | 用分群评分分布和理由对齐评估模型能否代替人评数学题。 |
| Agent | 评测生成 | [A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks](cards.md#paper-150438) | 先生成工具调用序列再写题目 |
| Agent / 安全 | 风险评测 | [AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment](cards.md#paper-139661) | 在沙箱内分别评估行为与理由 |
| 无线感知 | 自监督预训练 | [AmbientFM: A Foundation Model for Ambient Sensing](cards.md#paper-152593) | 检验单个信道表示能否替代逐任务模型 |
| 视频生成 | 推理时规划 | [AmbiguousWorld: Benchmarking and Resolving Ambiguous Instructions in Video World Models](cards.md#paper-155466) | 用多路径规划和反馈处理含糊指令 |
| 生成建模 | 分布控制 | [A Mean-Field Framework for Inference-Time Distributional Control of Diffusion Models](cards.md#paper-150099) | 群体目标用交互粒子而非逐样本独立打分 |
| 学习理论 | 结构泛化 | [A Measure-Theoretic Analysis of Reasoning: Structural Generalization and Approximation Limits](cards.md#paper-155536) | 分开扫描位置编码、深度和宽度 |
| 可解释性 | 循环模型 | [A Mechanistic Analysis of Looped Reasoning Language Models](cards.md#paper-153805) | 测每层循环轨迹是否稳定以诊断额外迭代价值 |
| 科学机器学习 | 因果诊断 | [A Mechanistic Interpretability Study of an Astronomical Foundation Model](cards.md#paper-153037) | 用消融验证探针发现的天文特征是否实际参与预测 |
| 可解释性 | 匹配反事实 | [A Mechanistic Investigation of Theory of Mind in a Large Language Model](cards.md#paper-148276) | 以非心智匹配对照检验所谓心智推理模块 |
| 控制理论 | 在线预测 | [A Memory Efficient Unified Algorithm for Online Learning of Linear Dynamical Systems](cards.md#paper-155619) | 按不稳定复杂度而非隐藏维度选择预测器容量 |
| 科学机器学习 | 守恒离散化 | [A meshfree exterior calculus for generalizable and data-efficient learning of physics from point clouds](cards.md#paper-154490) | 点云上构造守恒算子后再学习通量 |
| 大语言模型 | 量化诊断 | [A Method-Class Divide in Sub-4-Bit Quantization:\\Iterative vs.\ Single-Pass Sensitivity to Data Composition](cards.md#paper-148347) | 极低位宽下为迭代量化单独优化校准数据 |
| 优化 | 局部学习规则 | [A method to automatically discover symbolic local learning rules](cards.md#paper-150193) | 用稀疏符号损失搜索替代局部黑箱学习器 |
| 时间序列 | 专家路由 | [AME-TS: Anchored Mixture-of-Experts for Time Series Forecasting](cards.md#paper-153106) | 用可解释序列结构先验约束token路由 |
| 科学机器学习 | 约束生成 | [AMGenC: Generating Charge Balanced Amorphous Materials](cards.md#paper-154520) | 软投影维持约束趋势，再在终点离散投影 |
| 时间序列 | 结构消融 | [A Minimal Interpretable Architecture for Zero-Shot Reconstruction of Dynamical Systems](cards.md#paper-153946) | 给零样本动力学模型加入近邻后继的极简基线 |
| 大语言模型 | 集合采样 | [A Model of Diverse Sampling from Language Models](cards.md#paper-151475) | 用DPP优化整组候选的质量和互补性 |
| 贝叶斯优化 | 实验设计 | [Amortized Bayesian Experimental Design with In-Context Knowledge Conditioning](cards.md#paper-152127) | 额外知识进入上下文前按当前证据过滤 |
| 计算机视觉 | 扩散引导 | [Amortized Guidance for Image Inpainting with Pretrained Diffusion Models](cards.md#paper-152907) | 离线学习可复用修补引导，部署冻结底座 |
| 可解释性 | 核归因 | [Amortized Linear-time Exact Shapley Value for Product-Kernel Methods](cards.md#paper-149276) | 积核下利用代数结构求精确归因 |
| 优化 | 最优传输 | [Amortized Optimal Transport from Sliced Potentials](cards.md#paper-156137) | 用切片势预测完整传输势 |
| 计算机视觉 | 推理量化 | [Amortized-Precision Quantization for Early-Exit Vision Transformers](cards.md#paper-154315) | 按层实际执行概率联合选位宽与退出门槛 |
| 概率建模 | 变分推断 | [Amortized Structured Stochastic Variational Inference for Gaussian Process Latent Variable Models](cards.md#paper-152433) | 让潜变量后验依赖诱导点 |
| 统计学习 | 密度估计 | [Amortized Vine Copulas for High-Dimensional Density and Information Estimation](cards.md#paper-150646) | 复用一个二元估计器并校正边际 |
| 强化学习 | 规划蒸馏 | [Amortizing Generative Guidance for Model-Based Reinforcement Learning](cards.md#paper-152395) | 保留规划器高价值动作的多个模式 |
| 概率建模 | 超参数优化 | [Amplitude Decoupling in Gaussian Process Training: Exact Decomposition, Pole Cancellation, and Evaluation-Efficient Optimization](cards.md#paper-148358) | 先剖面化幅值再优化核形状 |
| 多模态学习 | 自适应推理 | [AMPS: Adaptive Modality Preference Steering via Functional Entropy](cards.md#paper-149128) | 按样本的模态贡献调整干预强度 |
| 强化学习 | 降方差 | [A Multi-Fidelity Control Variate Approach for Policy Gradient Estimation](cards.md#paper-156737) | 把低保真仿真作为控制变量 |
| 计算神经科学 | 信息几何 | [A multi-scale information geometry reveals the structure of mutual information in neural populations](cards.md#paper-154781) | 按刺激分辨率比较神经编码 |
| 深度学习 | 优化器 | [AMUSE: Anytime Muon with Stable Gradient Evaluation](cards.md#paper-152756) | 同时检查 Muon 低曲率进展和高曲率振荡 |
| 医学影像 | 可控生成 | [AnaDiffusion: Anatomically Compositional Latent Diffusion for Controllable 3D Brain MRI Generation](cards.md#paper-150996) | 用局部解剖生成约束全局扩散 |
| 电子设计 | 结构生成 | [AnalogToBi: Device-Level Analog Circuit Topology Generation via Bipartite Graph and Grammar Guided Decoding](cards.md#paper-150608) | 用双部图语法约束拓扑输出 |
| 生成模型 | 偏差校正 | [Analytical Correction for Subsampling Bias in Drifting Models](cards.md#paper-155602) | 用批内统计校正软最大质心估计 |
| 生成模型 | 逆问题 | [Analyzing and Guiding Zero-Shot Posterior Sampling in Diffusion Models](cards.md#paper-148817) | 在谱域确定后验采样参数 |
| 生成模型 | 训练诊断 | [Analyzing Learning-Dynamics Across Loss and Prediction Choices for Diffusion Models](cards.md#paper-155205) | 独立选择网络输出空间和损失空间 |
| 学习理论 | 算力分配 | [An Analytical Model of Compute-limited Multistage Training Pipelines](cards.md#paper-150925) | 根据预训练程度和数据质量调整各阶段预算 |
| 强化学习 | 序贯试验 | [An Anytime Algorithm for Good Arm Identification](cards.md#paper-156663) | 用可随时停止的策略识别过阈值行动 |
| 统计学习 | 软标签诊断 | [An Assessment of Human vs. Model Uncertainty in Soft-Label Learning and Calibration](cards.md#paper-139664) | 分开软标签的不确定性和标签众数变化 |
| 医学视觉 | 专家路由 | [Anatomy-Activated Mixture-of-Experts for 3D Medical Vision-Language Pre-training](cards.md#paper-151182) | 按全局器官分布而非孤立 token 分配专家。 |
| 医学视觉 | 时空建模 | [Anatomy-aware Spatio-Temporal Modeling for Echocardiography Segmentation](cards.md#paper-155842) | 将解剖关系写进注意力，并独立拟合局部周期运动。 |
| 强化学习 | 离策略梯度 | [Anatomy of Off-Policy Policy Gradient: Importance Sampling, KL Regularization, and Baselines](cards.md#paper-155331) | 复用轨迹时成对使用 KL 正则和组均值基线。 |
| 医学视觉 | 条件生成 | [Anatomy-Preserving Unpaired Medical Image Translation via Shared Latent Anchoring](cards.md#paper-154881) | 先学并冻结跨模态结构空间，再拟合目标域外观。 |
| 大语言模型 | 偏好聚合 | [An Axiomatic Analysis of DPO and NLHF as Reference-Dependent Probabilistic Voting Rules](cards.md#paper-152308) | 用单调性与阶段交换性检验后训练目标。 |
| 计算机视觉 | 三维重建 | [Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation](cards.md#paper-152132) | 以复杂度驱动的三维锚点控制高斯数量。 |
| 多模态学习 | 证据评测 | [ANCHOR: Audio-Visually Grounded Chain-of-Thought Reasoning Benchmark](cards.md#paper-139276) | 把答案正确与推理是否引用视听证据分开测。 |
| 医学视觉语言 | 结构生成 | [Anchoring LLM-based Chest X-ray Report Generation via Diffusion Language Planning](cards.md#paper-148935) | 先规划结构化检查发现，再逐字生成报告。 |
| 计算机视觉 | 持续适配 | [Anchoring Physiological Invariance, Expanding Domain Plasticity: Prior-Stabilized Dynamic Adaptation for Continual rPPG Measurement](cards.md#paper-149063) | 保护任务关键参数，只在偏移明显层扩容。 |
| 大语言模型 | 推理蒸馏 | [Anchoring Reasoning Distillation via Syntactic Constraints](cards.md#paper-154471) | 保留弱教师正确的计划，掩掉错误结果 token。 |
| 统计学习 | 降维 | [Anchor PCA](cards.md#paper-153959) | 学习跨域稳定的方差方向，而非直接池化 PCA。 |
| 大语言模型 | 安全评测 | [AnchorRep: Defending LLMs Against Cross-Model Adversarial Transfer via Representation Repulsion](cards.md#paper-149182) | 同时测防御的恶意请求失败与正常输出乱码。 |
| 具身智能 | 世界模型 | [AnchorWorld: Embodied Egocentric World Simulation with View-based Evolution Customization](cards.md#paper-150033) | 用训练时第三人称空间监督补第一视角身体遮挡。 |
| 深度学习 | 网络拓扑 | [ANCRe: Adaptive Neural Connection Reassignment for Efficient Depth Scaling](cards.md#paper-152945) | 学习跨层残差连接布局，检验深层利用率。 |
| Agent | 鲁棒评测 | [AndroidReality: How Far Are Mobile Agents from the Real World?](cards.md#paper-139580) | 按状态、转移、动作分别施加界面扰动。 |
| 学习理论 | 样本复杂度 | [A Near-optimal SQ Lower Bound for Smoothed Agnostic Learning of Boolean Halfspaces](cards.md#paper-150497) | 按坐标翻转噪声强度判断布尔半空间学习的可解难度。 |
| 优化 | 零阶估计 | [An Educated Guess: Deriving Statistically Aligned Gradient Estimates for Zeroth-Order Optimization](cards.md#paper-150140) | 用前向激活谱构造探测方向。 |
| 强化学习 | 树搜索 | [An Efficient Algorithm for Thresholding Monte Carlo Tree Search](cards.md#paper-153387) | 根节点只需判断过阈值时，直接分配序贯采样给阈值判定。 |
| 多模态学习 | 异常检测 | [An Efficient Cross-modal Feature Reconstruction Model for Multimodal Multi-class Anomaly Detection](cards.md#paper-153426) | 用跨模态重建代替同模态重建，检验是否更能区分异常。 |
| 学习理论 / 公平性 | 约束诊断 | [An Efficient Geometric Characterization of Robust Fair Learning](cards.md#paper-151262) | 用线性规划检查严格公平约束是否造成准确率对分布扰动敏感。 |
| 推荐系统 | 基准诊断 | [An Embarrassingly Simple Graph Heuristic Reveals Shortcut-Solvable Benchmarks for Sequential Recommendation](cards.md#paper-139297) | 在宣称生成式推荐学到长历史之前，先测试仅用最近一两项的图检索。 |
| 预训练 | 训练稳定性 | [An Empirical Study on Noisy Data and LLM Pretraining Loss Divergence](cards.md#paper-151029) | 区分噪声类型与规模风险 |
| 推理模型 | 过程评测 | [An Enigma of Artificial Reason: Investigating the Production-Evaluation Gap in Large Reasoning Models](cards.md#paper-149795) | 独立评测推理步骤的正确性 |
| 优化 | 等变优化器 | [An Equivariance Principle for Optimizer Design: Symmetry-Compatible Updates for Embeddings, LM Heads, and MoE Routers](cards.md#paper-154592) | 按矩阵层的对称性选择更新规则 |
| 量子学习 | 强化学习接口 | [A New Framework for Quantum Reinforcement Learning](cards.md#paper-149569) | 在量子环境保留相干回报 |
| 图学习 | 动态图建模 | [A New Perspective on Target-Conditioned Structural Dynamics for Link Prediction in Dynamic Graphs](cards.md#paper-151703) | 先更新时间结构状态，再指导邻居聚合 |
| 生成模型 | 泛化理论 | [An exact information theory of generalization phase transitions in Bayesian diffusion models](cards.md#paper-152478) | 按可见信息量诊断扩散过程记忆与泛化 |
| 模型压缩 | 低精度训练 | [Angular Networks: Low-Bit Learning from Randomized Similarity Estimators](cards.md#paper-154802) | 采用角相似估计作为低比特线性层的替代 |
| 多模态 | 视频评测 | [Animation2Code: Evaluating Temporal Visual Reasoning in Video-to-Code Generation](cards.md#paper-138932) | 分别量化动画的外观和时间对齐 |
| 教育机器学习 | 评测诊断 | [An Information-Theoretic Evaluation Framework for Benchmark and Model Diagnosis in Knowledge Tracing](cards.md#paper-149407) | 按局部可预测性分层比较知识追踪模型 |
| 公平学习 | 数据审计 | [An Information-theoretic Framework for Auditing Unfairness in Training Data](cards.md#paper-153353) | 在训练前定位对公平偏差贡献较大的特征 |
| 概率建模 | 退火 | [Annealing in variational inference mitigates mode collapse: a theoretical study on Gaussian mixtures](cards.md#paper-151971) | 共同调节退火初温与速度以减少模式塌缩 |
| 统计学习 | 在线校准 | [Announced Breaks Separate Conformal Reliability from Frequency Calibration](cards.md#paper-151358) | 已知变点时重置校准，并分开报告单步与平均覆盖 |
| 隐私学习 | PAC 样本复杂度 | [An Õptimal Differentially Private PAC Learner for Concept Classes with VC Dimension 1](cards.md#paper-149826) | 利用低 VC 类树结构减少私有学习的样本需求 |
| 科学机器学习 | 稳定状态空间 | [A Novel Schur-Decomposition-Based Weight Projection Method for Stable State-Space Neural-Network Architectures](cards.md#paper-151951) | 用 Schur 域投影约束状态矩阵稳定性 |
| 模型可靠性 | 拒答校准 | [Answering At Any Cost: Frontier LLMs Are Consequence-Insensitive](cards.md#paper-150213) | 按回答错误代价单独评测拒答 |
| 推理训练 | 自蒸馏 | [Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information](cards.md#paper-149938) | 检查含答案的教师上下文是否压低探索 token |
| 视觉生成 | 散景编辑 | [AnyBokeh: Physics-Guided Any-to-Any Bokeh Editing with Optical Fingerprint Transfer](cards.md#paper-153372) | 先拟合输入图像既有光学状态再编辑离焦 |
| 语音生成 | 分阶段编辑 | [AnyEdit: A Unified Framework for Speech and Singing Voice Editing with Real-World Environmental Consistency](cards.md#paper-152934) | 先编辑干净内容再恢复源环境声 |
| 计算机视觉 | 数据诊断 | [AnyHand: A Large-Scale Synthetic Dataset for RGB(-D) Hand Pose Estimation](cards.md#paper-139245) | 固定网络和训练流程对照合成数据的构成 |
| 多模态学习 | 传感表示 | [AnyMo: Geometry-Aware Setup-Agnostic Modeling of Human Motion in the Wild](cards.md#paper-154127) | 用同一动作的多佩戴视图学习配置不变表征 |
| 多模态学习 | 条件生成 | [AnyMo: Scaling Any-Modality Conditional Motion Generation with Masked Modeling](cards.md#paper-153279) | 以掩码建模统一可缺失的动作控制模态 |
| 多模态学习 | 结构先验 | [Anymotion: A Dataset, Benchmark, and Baseline for Controllable Human Motion Editing](cards.md#paper-151900) | 将骨架关键点与语义查询作为可检验编辑中间态 |
| 统计学习 | 风险校准 | [Anytime-Valid Conformal Risk Control](cards.md#paper-154243) | 随着标注积累反复校准时采用任意时刻有效界 |
| 大语言模型 | 推理校准 | [Anytime-Valid PAC-Bayes Certificates for Adaptive Test-Time Scaling](cards.md#paper-153451) | 为反复试预算和验证器的过程报告统一风险成本界 |
| 科学机器学习 | 神经算子 | [AOT-POT: Adaptive Operator Transformation for Large-Scale PDE Pre-training](cards.md#paper-153792) | 用输入相关多流变换处理异构 PDE，而非仅加大模型 |
| 视频生成 | 分辨率迁移 | [ApertureAttn: Native 4K Video Generation with Image-Only Supervision](cards.md#paper-154936) | 用高分辨率单帧监督训练空间高频适配 |
| 具身智能 | 规划验证 | [APIVOT: Adaptive Planning with Interleaved Vision-Language Thoughts](cards.md#paper-152333) | 空间约束强时让视觉想象验证语言计划 |
| 大语言模型 | 个性化评测 | [APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings](cards.md#paper-139154) | 用随机映射迫使模型从对话历史推断偏好 |
| 大语言模型 | 指令评测 | [AppCIF-Bench: An Application-Level Complex Instruction Following Benchmark for Large Language Models](cards.md#paper-139375) | 把执行跨度和规则嵌套深度拆开评测 |
| 视频生成 | 物理评测 | [Apple-$\pi$: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence](cards.md#paper-139053) | 分阶段测试感知、定律表达和演绎 |
| 模型适配 | 模型合并 | [Approaching Effective Merging in Model Embedding Space](cards.md#paper-149693) | 先在共享内禀子空间表达任务更新再平均 |
| 机器学习系统 | 注意力计算 | [Approaching I/O-optimality for Approximate Attention](cards.md#paper-154340) | 按快速内存大小和允许的近似选择低 I/O 注意力 |
| 概率建模 | 神经符号推断 | [Approximate Bayesian inference with exchangeable distributions for neurosymbolic AI](cards.md#paper-150027) | 利用可交换结构设计离散变分近似 |
| 算法理论 | 公平分配 | [Approximate Envy-Free Allocations  up to any k Goods](cards.md#paper-148884) | 根据可忽略物品数选可计算的公平保证 |
| 数值计算 | 核矩阵近似 | [Approximate Matrix–Vectors Under a Bounded $\ell_1$ Assumption and Applications to Kernel Matrices](cards.md#paper-150755) | 用总绝对质量决定是否以采样近似矩阵向量乘 |
| 学习理论 | 状态空间模型 | [Approximate Memory Suffices for Universal Approximation with State Space Models](cards.md#paper-148575) | 区分衰减历史任务的近似记忆和精确延迟恢复 |
| 机制设计 | 资源定价 | [Approximation Algorithms for GPU Pricing under Finite Capacity](cards.md#paper-152873) | 稀缺 GPU 容量下比较非线性菜单与按卡按小时线性定价 |
| 联邦学习 | 稳健聚合 | [Approximation Guarantees for Robust Aggregation in Federated Learning](cards.md#paper-155522) | 在稳定性和逼近干净均值之间选择聚合约束。 |
| 学习理论 | 对比学习 | [Approximation in Contrastive Representation Learning](cards.md#paper-154229) | 根据互信息核的谱尾选择对比嵌入维度。 |
| 学习理论 | 算子逼近 | [Approximation of Maximally Monotone Operators : A Graph Convergence Perspective](cards.md#paper-155734) | 对不连续或多值算子用图收敛选择逼近指标。 |
| 科学机器学习 | 网格建模 | [APPSolver: Adaptive Patch Partitioning for Point-Wise Ship Flow Prediction on Unstructured Meshes](cards.md#paper-149116) | 按流场敏感区域分配异质网格的 token 分辨率。 |
| 强化学习 | 约束优化 | [A Primal-dual Approach for Semi-Infinitely Constrained Reinforcement Learning](cards.md#paper-154351) | 用原始–对偶更新替代对连续约束族的内层求解。 |
| 多模态学习 | 视频压缩 | [A Principled Optimal Transport Framework for Frame Selection in Long Video Understanding](cards.md#paper-155583) | 按查询相关性分配帧权重，再单独约束抽帧后的时间覆盖。 |
| 计算机视觉 | 逆问题 | [A Principled Self-Referenced Early Stopping Approach for Deep Image Prior](cards.md#paper-151448) | 用伪独立观测构造早停指标，减轻无干净标签时的过拟合。 |
| 计算神经科学 | 概率建模 | [A probabilistic model of visual segmentation explains early visual cortical dynamics](cards.md#paper-154567) | 用分割推断解释视觉皮层群体活动，而非只拟合单神经元平均曲线。 |
| 大语言模型 / Agent | 过程评测 | [A Process-Level Evaluation of LLM Discovery Agents](cards.md#paper-139068) | 记录搜索行为和中间里程碑来选择发现任务的 Agent 框架。 |
| 优化 | 最优传输 | [A Provably Convergent and Practical Algorithm for Gromov–Wasserstein Optimal Transport](cards.md#paper-148839) | 用可计算可行性残差控制 Gromov–Wasserstein 投影精度。 |
| 多智能体 | 仿真降本 | [APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents](cards.md#paper-149524) | 用自适应原型复用语言模型调用，并用独立抽查校正群体估计。 |
| 科学机器学习 | 泛化评测 | [AptaBench: A Benchmark for Aptamer-Small Molecule Binding](cards.md#paper-139036) | 对成对数据按两侧实体分别做互斥划分，暴露随机切分泄漏。 |
| 科学机器学习 | 长程预测 | [AQBENCH: Benchmarking Neural Surrogates for Air Quality Forecasting](cards.md#paper-139706) | 同时测长时滚动、超阈事件和极端偏差，避免按平均误差选模型。 |
| 数字人文 / 计算机视觉 | 表征评测 | [A Quantitative Visual Taxonomy of Worldwide Writing Systems](cards.md#paper-152125) | 在字形相似度研究中分开检验视觉亲近性与谱系一致性。 |
| 大语言模型 / 优化 | 零阶微调 | [AR1-ZO: Topology-Aware Rank-1 Zeroth-Order Queries for High-Rank LoRA Fine-Tuning](cards.md#paper-155186) | 高秩 LoRA 的零阶估计改用交替秩一方向并校准缩放。 |
| 时空建模 | 条件生成 | [Arbitrarily Conditioned Hierarchical Flows for Spatiotemporal Events](cards.md#paper-154895) | 用混合掩码把预报、后验补全与部分轨迹恢复作为同一条件任务。 |
| 大语言模型 | 类比评测 | [ARCANA: A Benchmark for Abstraction and Analogical Reasoning](cards.md#paper-153989) | 单独测远类比并分析关系抽象失败，避免用近类比代表整体能力。 |
| 大语言模型 | 上下文压缩 | [ARC-Encoder: learning compressed text representations for large language models](cards.md#paper-156755) | 用共享压缩编码器为不同解码器生成较短表示。 |
| 统计学习 | 自动微分 | [Archimedean Copula Inference via Taylor-Mode AD](cards.md#paper-153718) | 用 Taylor 模式自动微分统一 Archimedean copula 的高阶密度计算。 |
| 科学机器学习 | 物理先验 | [Architecture-Embedded Physics Priors for Mitigating Spectral Bias in Physics-Informed Neural Networks](cards.md#paper-150185) | 将方程残差用于调节网络内部频谱，并和只改损失或采样对照。 |
| 大语言模型 | 来源标识 | [ArcMark: Distortion-Free Multi-Byte LLM Watermark via Optimal Transport](cards.md#paper-154160) | 评估文本水印时同时测消息恢复率与文本质量。 |
| Agent / 教育 | 能力分解评测 | [Are Agents Ready to Teach? A Multi-Stage Benchmark for Real-World Teaching Workflows](cards.md#paper-139079) | 将有界教学判断、互动辅导和真实流程执行分开验收。 |
| 视频生成 | 流式编辑 | [AR-Edit: Training-Free Streaming Video Editing without Inversion](cards.md#paper-152336) | 缓存源视频注意力值以避免反演 |
| 在线学习 | 延迟反馈 | [A Reduction from Delayed to Immediate Feedback for Online Convex Optimization with Improved Guarantees](cards.md#paper-155853) | 将即时算法封装为可处理异步反馈的版本 |
| 大语言模型 | 偏好数据 | [Are Easier or Harder Examples Better? Rethinking Data Selection for Reward Models and Preference Optimization](cards.md#paper-151585) | 先校验奖励信号质量再按难度筛样 |
| 强化学习 | 稳健策略优化 | [A Refined Sample-Complexity Analysis of Robust Policy Optimization under Decaying Actor Stepsizes](cards.md#paper-150078) | 保守 actor 更新时按 critic 条件偏差分配精度 |
| 博弈学习 | 信念搜索 | [A Regularization-Based Approach to Public Belief State Search for Adversarial Games](cards.md#paper-152665) | 用平滑正则化求解公开信念下的局部策略 |
| Agent | 安全评测 | [Are LLM Safety Judges Policy-Invariant? A Three-Principle Stress-Test](cards.md#paper-139215) | 用语义等价规则改写检验裁判稳定性 |
| 表格学习 | 漂移诊断 | [Are LLMs Good at Feature Engineering? Evidence from a Controlled Synthetic Benchmark](cards.md#paper-139570) | 使用可控漂移与已知充分特征检验特征工程 |
| 多模态学习 | 基准诊断 | [Are Multimodal Benchmarks Really Useful? Item-Level Multimodal Benchmark Diagnosis via Structure-Response Co-Calibration](cards.md#paper-139183) | 联合题目结构与遮蔽模态后的响应估计依赖 |
| 视觉生成 | 奖励设计 | [Arena-T2I Hard: Benchmarking and Improving Faithfulness with Dependency-Aware Checklist Rewards](cards.md#paper-151320) | 按依赖图评估提示约束 |
| 量子机器学习 | 评测 | [A Reproducible Evaluation Protocol for Quantum Non-Linearity in Variational Quantum Models](cards.md#paper-139813) | 对齐训练预算后分解非线性能力 |
| 可解释性 | 复现 | [A Reproduction Study of Weight-Based Mechanistic Interpretability in Bilinear MLPs](cards.md#paper-157024) | 检查权重可解释结构是否由权重衰减驱动 |
| Agent | 推理调度 | [Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents](cards.md#paper-152084) | 按交互步骤分配最低可行推理档位 |
| 推荐系统 | 评测可靠性 | [ARES: How Reliable Are LLM User Simulators for Recommender A/B Testing?](cards.md#paper-139784) | 用多用户模拟骨干复核A/B结论 |
| 大语言模型 | 水印评测 | [A Retained-Signal Interface for LLM Watermark Robustness under Paraphrase](cards.md#paper-155532) | 分报初始信号、编辑后保留与检测器性能 |
| 多模态学习 | 反事实评测 | [Are Text-to-Image Models Inductivist Turkeys? A Counterfactual Benchmark for Causal Reasoning](cards.md#paper-139397) | 把显式描述与隐式反事实推导拆开测 |
| 统计学习 | 贝叶斯推断 | [A Revisit of Hamiltonian Monte Carlo Efficiency on Bayesian Neural Networks](cards.md#paper-152689) | 选激活函数时测积分器曲率误差 |
| 多模态学习 | 分布外评测 | [Are We Making Progress in Multimodal Domain Generalization? A Comprehensive Benchmark Study](cards.md#paper-139747) | 在统一协议下比较算法与ERM |
| 生成模型 | 奖励引导 | [Are we really tilting? The mechanics of reward guidance in flow and diffusion models](cards.md#paper-148402) | 区分模态内过优化与模态选择失效 |
| 推理模型 | 机制诊断 | [Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models](cards.md#paper-154084) | 用不同初值和中间轨迹诊断错误固定点 |
| 大语言模型 | 不确定性校准 | [Argument Graph Uncertainty: Quantifying Uncertainty from the Logical Structure of Reasoning Chains](cards.md#paper-149153) | 用单条推理链的逻辑关系估置信度 |
| Agent | 不确定性评测 | [Argus: A Cross-Regime Benchmark for the Transferability of Uncertainty Quantification in Computer-Use Agents](cards.md#paper-139443) | 换模型或从开放权重切换到 API 时重新校准 |
| 计算机视觉 | 视频生成 | [ARGUS: Stacked Multi-View Identity Mosaic Injection for Subject-Preserving Video Generation](cards.md#paper-152732) | 用多视角身份条件并限制其注入阶段 |
| 多模态学习 | 检索评测 | [ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge](cards.md#paper-155756) | 分开测试领域知识与推理需求 |
| 强化学习 | 持续学习 | [ARROW: Augmented Replay for RObust World models](cards.md#paper-156771) | 将近期缓存与长期覆盖缓存分别维护 |
| 三维视觉 | 运动参数估计 | [ArtCrafter: Feed-Forward Generation of Articulated 3D Object with Analytic Joint Derivation](cards.md#paper-151536) | 从跨状态一致的部件几何解析求关节 |
| 生成模型 | 采样调度 | [ART for Diffusion Sampling: A Reinforcement Learning Approach to Timestep Scheduling](cards.md#paper-155895) | 学习扩散采样时钟并蒸馏为固定步表 |
| Agent / 三维视觉 | 可执行生成 | [Articraft: An Agentic System for Scalable Articulated 3D Asset Generation](cards.md#paper-155396) | 让生成代理编写可测试的部件程序 |
| 三维视觉 | 几何拟合 | [Articulation in Prime: Primitive-Based Articulated Object Understanding from a Single Casual Video](cards.md#paper-154376) | 用可见性感知的几何原语替代长时点轨迹 |
| 大语言模型 | 因果诊断 | [Artificial Aphasias in Lesioned Language Models](cards.md#paper-151805) | 用类别化症状而非单一准确率分析参数干预 |
| Agent | 风险评测 | [ARTIS: Agentic Risk-Aware Test-Time Scaling via Iterative Simulation](cards.md#paper-150972) | 在实际执行前用验证过的模拟器评估候选 |
| 软件工程 | 程序验证 | [ASAP: Assembly-Source Aligned Pseudocode Refinement For Binary Decompilation](cards.md#paper-148550) | 用执行等价和可重编译性验证反编译改写 |
| 计算机视觉 | 词元剪枝 | [ASAP: Attention Sink Anchored Pruning](cards.md#paper-151159) | 用跨层传播距离判断冗余而非单层注意力 |
| 可靠性 | 分布外检测 | [ASAT: Adaptive Scoring and Thresholding with Human Feedback for Robust Out-of-Distribution Detection](cards.md#paper-156772) | 随真实反馈联合更新分数和接受阈值 |
| 大语言模型 | 训练诊断 | [A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs](cards.md#paper-155425) | 沿实际更新方向近似测曲率 |
| 时间序列 | 多任务学习 | [A Scalable Multi-Task Model for Virtual Sensors](cards.md#paper-149834) | 让不同预测目标共享参数并学习输入选择 |
| 统计学习 | 连续时间建模 | [A Scalable Nonparametric Continuous-Time Survival Model through Numerical Quadrature](cards.md#paper-151002) | 用可微高阶数值积分估累计风险 |
| 科学机器学习 | 稳健性审计 | [A Scientific Claim Stability Framework for Evaluating MRI Morphometry Pipelines](cards.md#paper-139330) | 按科学结论是否保持来比较影像处理流水线 |
| 大语言模型 | 缓存调度 | [AsdaKV: Attention-Overlap Driven Semantic KV Retrieval for Long-Context LLMs](cards.md#paper-149737) | 根据高注意力区域重叠下降触发缓存刷新 |
| 在线学习 | 二阶遗憾 | [A second order regret bound for NormalHedge](cards.md#paper-153089) | 按累计专家遗憾方差选择更新规则 |
| Agent | 上下文压缩 | [A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression](cards.md#paper-153290) | 对工具日志学习可复用的精确保留规则 |
| 语言模型 | 置信校准 | [A Semantic-Sampling Framework for Evaluating Calibration in Open-Ended Question Answering](cards.md#paper-149036) | 分离回答选取与置信度估计采样 |
| 强化学习 | 多智能体分解 | [A Separation Principle for Cooperative Multi-Agent Reinforcement Learning](cards.md#paper-149847) | 以单体目标价值作为群体分配成本 |
| 时间序列 | 集合条件化 | [A Set-Sequence Model for Time Series](cards.md#paper-148413) | 用置换不变统计为各个序列提供群体上下文 |
| 具身学习 | 视频监督 | [ASH: Agents that Self-Hone via Embodied Learning](cards.md#paper-152698) | 用自身交互估计逆动力学，为无动作视频构建监督 |
| 模型安全 | 防御训练 | [A Simple Class-Agnostic Approach to Enhance Fair Adversarial Training](cards.md#paper-156125) | 在样本级区分难例与无法学习的离群样本 |
| 计算神经科学 | 空间表征 | [A simple model of co-emergence of grid and place fields](cards.md#paper-155687) | 调节感觉噪声和遮蔽，检查空间编码是否共同形成 |
| 语言模型 | 数据诊断 | [A Simple Unigram Cross-Entropy Lens on the Lexical Imprint of Pre-training Data](cards.md#paper-155069) | 用一元词交叉熵衡量训练语料与测试任务词汇对齐 |
| 强化学习 | 多目标优化 | [A Single Deep Preference-Conditioned Policy for Learning Pareto Coverage Sets](cards.md#paper-150514) | 利用偏好到回报的连续性扫过 Pareto 前沿 |
| 运筹优化 | 非平稳分配 | [A Single-Sample Polylogarithmic Regret Bound for Nonstationary Online Linear Programming](cards.md#paper-154912) | 只有少量前瞻样本时仍按新状态重解资源分配 |
| 自然语言处理 | 辅助监督 | [Ask, Answer, and Detect: Role-Playing LLMs for Personality Detection with Question-Conditioned Mixture-of-Experts](cards.md#paper-150558) | 用标准化问题的中间回答辅助抽象标签学习 |
| 语言模型 | 难度校准 | [Ask-E: An Environment for Calibrated Question Generation](cards.md#paper-139309) | 用两参考模型的求解差界定题目难度 |
| Agent | 澄清策略 | [Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents?](cards.md#paper-154769) | 按缺失信息类型而非统一时点发起澄清 |
| 语言模型 | 推理训练 | [Asking the Right Questions: Improving Reasoning with Generated Stepping Stones](cards.md#paper-149684) | 先生成可跨求解器复用的中间问题 |
| 隐私保护 | 私有推理 | [Ask in the Crowd: Differentially Private LLM Inference via Dummy-Augmented Shuffling](cards.md#paper-149860) | 用查询混合和缓存复用平衡隐私与延迟 |
| 软件工程 | 代码检索 | [Ask KG Agent: A Multi-Agent Framework for Code Localization Using Code and Knowledge Graphs](cards.md#paper-155386) | 用开发历史补充依赖图以定位维护任务 |
| 科学机器学习 | 成本敏感评测 | [ASO Atlas 2.0: Evaluating antisense oligonucleotide prediction across the preclinical pipeline](cards.md#paper-139593) | 按阶段成本加权预测价值 |
| 学习理论 | 推理深度 | [A Solvable Model of Chain-of-Thought in In-Context Learning](cards.md#paper-154777) | 按上下文与预训练覆盖验证最优推理步数 |
| 图学习 | 稀疏分解 | [A Sparse Low-Rank Biclique Decomposition for Graphs](cards.md#paper-152969) | 用有符号双团保留邻接稀疏性 |
| 统计学习 | 密度估计 | [A Spectral Framework for Closed-Form Relative Density Estimation](cards.md#paper-152831) | 用特征矩闭式拟合相对对数密度 |
| Agent安全 | 防御评测 | [ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents](cards.md#paper-139498) | 分别验收执行与澄清状态的信任策略 |
| 大语言模型 | 量化 | [ASQ: Agent-guided Semantic-aware Quantization for Large Language Models](cards.md#paper-153843) | 按语义相关位置评估通道重要性 |
| 科学机器学习 | 评测诊断 | [AssayBench: An Assay-Level Virtual Cell Benchmark for LLMs and Agents](cards.md#paper-139516) | 对异质测试组使用统一的排序评价 |
| 隐私 | 防御审计 | [Assessing Per-Sample Membership Inference Vulnerability without Retraining](cards.md#paper-155925) | 用单模型诊断样本隐私风险 |
| 生成模型 | 质量评估 | [Assessing Sample Quality in Conditional Generation under Compositional Shift](cards.md#paper-148544) | 缺少目标组合实样时分别核查真实性和属性忠实度 |
| 统计学习 | 敏感性分析 | [Assessing the robustness of heterogeneous treatment effects in survival analysis under informative censoring](cards.md#paper-149514) | 对信息性删失报告异质治疗效应界 |
| 多模态学习 | 测试时适配 | [ASSET: Acquisition-Sensitive Subspace Estimation for Test-Time Adaptation of Medical VLMs](cards.md#paper-153026) | 只在采集质量敏感子空间内更新 |
| 可解释性 | 机制分析 | [Assign and Add: A Mechanistic Study of Compositional Arithmetic](cards.md#paper-153282) | 检查同一内部模块能否跨输入表示复用 |
| 强化学习 | 人机决策 | [Assistive Dueling Bandits: No-Regret Algorithms for Assisting No-Regret Users](cards.md#paper-148914) | 用用户选择学习候选对而无需看到收益 |
| 优化 | 稳定性 | [A Stability Analysis of AdamW: Unstable Equilibria and Non-Convergence](cards.md#paper-151341) | 区分优化器固定点与动力学收敛 |
| 统计学习 | 群体协作 | [A Statistical Framework for Algorithmic Collective Action with Multiple Collectives](cards.md#paper-148932) | 将群体目标一致性纳入效果估计 |
| 模型理论 | 注意力设计 | [A Statistical Theory of Gated Attention through the Lens of Hierarchical Mixture of Experts](cards.md#paper-153011) | 比较在注意力输出与值映射处放置门控 |
| 医学影像 | 几何配准 | [A Steerable Deep Network for Model-Free Diffusion MRI Registration](cards.md#paper-156020) | 在原始空间角度域做等变配准 |
| 多模态学习 | 视频理解 | [As the Story Unfolds: Watching a Film and Identifying Characters as a Human Does](cards.md#paper-152579) | 以对话和画面逐步建立角色身份库 |
| 大语言模型 | 多任务强化学习 | [ASTOR: Multi-Task Code Reinforcement Learning via Utility-Driven Coordination](cards.md#paper-154519) | 按任务学习价值分别配训练预算和 KL 约束 |
| 优化 | 在线优化 | [ASTRA: ADMM-Accelerated Topology Reconfiguration for Dynamic Satellite Constellations](cards.md#paper-156042) | 重复约束求解用可控近似内循环 |
| 训练系统 | 数据流 | [AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs](cards.md#paper-152612) | 将 rollout 服务与训练解耦为独立组件 |
| 医学教育 | 评测设计 | [A Stratified Multi-Rater Evaluation of LLM-Based Virtual Standardized Patients with a Deployed Data-Generation Platform](cards.md#paper-139188) | 用逐话语专家参考和交叉盲评定位模拟患者偏差 |
| 图学习 | 高阶消息传递 | [A Structure-Aware Higher-Order Message Passing Framework on Walk States for Graph Classification](cards.md#paper-150813) | 用游走状态代替全量高阶元组 |
| 科学机器学习 | 分层计划 | [A Structured LLM Framework for Inorganic Material Synthesis Planning](cards.md#paper-148871) | 用离散类别连接条件选择和步骤生成 |
| Agent | 奖励塑形 | [A Subgoal-driven RL Framework for Improving Long-Horizon Web Agents](cards.md#paper-151697) | 在正常界面任务中用子目标进度补充终局评分 |
| 强化学习 | 代理目标 | [A Surrogate Perspective on Convergence of Fixed-Target DQN](cards.md#paper-155836) | 用平滑最大误差减少最坏Bellman残差 |
| 表征学习 | 向量量化 | [ASVQ: What Reparameterization Is Just Enough for Efficient Codebook Learning?](cards.md#paper-149752) | 先试自适应尺度再增加码本重参数化复杂度 |
| 推理系统 | 负载均衡 | [AsymHP: Load-Balanced Sparse Attention for Video Diffusion Transformers](cards.md#paper-151792) | 按上一扩散步的密度分配每卡注意力头 |
| 优化 | 低秩分解 | [Asymmetric Factorization for Low-Rank PSD Learning: When Is the Relaxation Exact ?](cards.md#paper-151704) | 用显式惩罚下界决定能否替换对称分解 |
| 生成模型 | 流匹配 | [Asymmetric Flow Models](cards.md#paper-156075) | 仅压缩噪声预测，保留全维数据预测 |
| 推荐系统 | 迁移诊断 | [Asymmetric Generalization in Deep CTR Models: A Block-wise Diagnosis](cards.md#paper-149702) | 分块重调后再决定哪些参数做集成 |
| 多模态学习 | 模态对齐 | [Asymmetric Hierarchical Anchoring for Robust Audio–Visual Cross-Modal Generalization](cards.md#paper-148414) | 以结构更明确的模态为共享语义锚点 |
| 隐私保护 | 可逆验证 | [Asymmetric Invertible Threat: Learning Reversible Privacy Defense for Face Recognition](cards.md#paper-152968) | 分别评估隐私遮蔽和授权恢复 |
| 音频处理 | 来源认证 | [Asymmetric Phase Coding Audio Watermarking](cards.md#paper-149813) | 将密码学签名和信道抗失真分开验证 |
| 学习理论 | 缩放规律 | [Asymmetric Scaling Laws from Sparse Features](cards.md#paper-149774) | 稀有特征覆盖不足时先增加数据 |
| 推理系统 | 流水线加速 | [AsymPipe: Accelerating Large-scale DiTs Image Editing via Asymmetry-Aware Pipeline Parallelism](cards.md#paper-148143) | 把不编辑区域的缓存收益与设备负载一起优化 |
| 生成模型 | 负向引导 | [Asymptotically Exact Negative Guidance of Diffusion Models via Positive-Unlabeled Learning](cards.md#paper-148530) | 用显式目标分布检查负向引导偏差 |
| 统计学习 | 序贯推断 | [Asymptotically Log-Optimal Bayes-Assisted Confidence Sequences for Bounded Means](cards.md#paper-153874) | 用预测模型提高选取有效鞅因子的效率 |
| 统计学习 | 差分隐私 | [Asymptotically Optimal Best Arm Identification with Fixed-Budget under Differential Privacy](cards.md#paper-150020) | 按固定预算的隐私输运指数设计采样 |
| 统计学习 | 序贯推断 | [Asymptotic Anytime-Valid Inference for U-statistics](cards.md#paper-154311) | 先区分U统计量退化性再选置信边界 |
| 分布式训练 | 异步优化 | [AsyncMesh: Fully Asynchronous Optimization for Data and Pipeline Parallelism](cards.md#paper-155437) | 按并行轴分别补偿参数陈旧 |
| 大语言模型 | 蒸馏 | [AsyncOPD: How Stale Can On-Policy Distillation Be?](cards.md#paper-156136) | 按 KL 方向选异步估计器 |
| 视觉 | 分布外检测 | [A Systematic Analysis of Out-of-Distribution Detection Under Representation and Training Paradigm Shifts](cards.md#paper-138908) | 按表征和偏移强度筛置信分数 |
| 科学机器学习 | 观测推理 | [A systematic evaluation of vision-language models for observational astronomical reasoning tasks](cards.md#paper-139292) | 一维观测先试数表，并额外验算物理理由 |
| 计算成像 | 多视角检测 | [At FullTilt: Real-Time Open-Set 3D Macromolecule Detection Directly from Tilted 2D Projections](cards.md#paper-154302) | 比较直接用原始投影和先重建体素再检测 |
| 模型安全 | 防御评测 | [A Theoretical Analysis of Backdoor Learning as Simplicity-Biased Optimization Dynamics](cards.md#paper-151187) | 用表征复测检查清洁微调是否真正消除风险 |
| 软件工程 | 代码评测 | [A Theoretical Analysis of Test-Driven Code Generation](cards.md#paper-149483) | 代码候选排序先试软功能相似度 |
| 大语言模型 | 表征机制 | [A Theoretical Analysis of Why Masked Diffusion Models Mitigate the Reversal Curse](cards.md#paper-149727) | 分别检查正反查询是否共享值侧证据 |
| 视觉 | 长尾学习 | [A Theoretical Bridge Between Long-Tailed Recognition and Continual Learning](cards.md#paper-148638) | 用持续学习方法分阶段学习头尾类别 |
| Agent | 课程学习 | [A Theoretical Framework for Self-Play Theorem Proving Algorithms](cards.md#paper-152957) | 用语义图上的多样性选择自博弈猜想 |
| 学习理论 | 在线学习 | [A Theory of Adversary-Directed Online Learning](cards.md#paper-154177) | 已知实例集但顺序可变时使用适配的复杂度量 |
| 学习理论 | 中间监督 | [A Theory of Online Learning with Autoregressive Chain-of-Thought Reasoning](cards.md#paper-154564) | 按模型类判断轨迹监督能否降低时域依赖 |
| 计算神经科学 | 动力系统 | [A Theory of Spatial Continuous Attractors in Hopfield Energy Landscapes](cards.md#paper-155828) | 分别学习吸引流形的法向恢复和切向输运 |
| 学习理论 | 生成覆盖 | [A Theory of Time-Sensitive Language Generation: Sparse Hallucination Beats Mode Collapse](cards.md#paper-154885) | 及时覆盖评测允许单独约束错误率 |
| 机器学习系统 | 训练预算 | [A Theory of Training Profit-Optimal LLMs](cards.md#paper-152898) | 先判断算力或数据瓶颈再决定新增投入 |
| 生成模型 | 理论保证 | [A Theory on Flow Matching with Neural Networks](cards.md#paper-152773) | 同时监控速度回归误差和生成分布距离 |
| 学习理论 | 推理复杂度 | [A Tight Hierarchy For Chain of Thought](cards.md#paper-152637) | 把思维链步数当独立资源量 |
| 具身智能 | 预测对齐 | [ATI-VLA: Action-Centric Predictive Vision–Language–Action Models via Actionable Alignment Then Adaptive Injection](cards.md#paper-152880) | 先对齐未来观测和动作，再用动作目标控制注入 |
| 科学机器学习 | 时序对齐 | [ATLAS: Adaptive Temporal Learning for Single-Cell Multi-Omics Alignment and Dynamics](cards.md#paper-152422) | 对稀疏配对的异步观测学习时滞，并按可靠性蒸馏 |
| 多模态 | 功能 token | [ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both](cards-0002.md#paper-155024) | 把视觉操作编码成共享的离散词元 |
| 图学习 | 跨域表示 | [AtlasULP: Domain-aware Universal Link Prediction via Relation Atlas](cards-0002.md#paper-150816) | 用关系图谱补充局部采样 |
| 视频生成 | 多尺度生成 | [AtlasVid: Efficient Ultra-High-Resolution Long Video Generation via Decoupled Global-Local Modeling](cards-0002.md#paper-150426) | 先规划低分辨率全局视频再细化 |
| 科学机器学习 | 可验证奖励 | [AtmoZero: Self-Play Post-Training for Caption-Free Weather Time-Series Captioning](cards-0002.md#paper-152217) | 用观测证据反驳不实描述 |
| 科学机器学习 | 材料模拟 | [AtomMOF: All-Atom Flow Matching for MOF-Adsorbate Structure Prediction](cards-0002.md#paper-149909) | 对比联合柔性建模与刚性宿主假设 |
| 算法 | 近似聚类 | [Atoms and Pivot Based Correlation Clustering](cards-0002.md#paper-153440) | 识别不应拆分的顶点组再执行 pivot |
| 科学机器学习 | 时序记忆 | [AtomWorld-Mem: Memory-Restored World States for Long-Horizon Atomistic Evolution](cards-0002.md#paper-155270) | 用历史恢复瞬时晶体快照遗漏的状态 |
| 图学习 | 拓扑预测 | [A Topological Encoder Decoder Framework for Temporal Graph Learning](cards-0002.md#paper-151161) | 先预测未来拓扑再生成节点及边 |
| 因果推断 | 基准诊断 | [A Topological Sorting Criterion for Random Causal Directed Acyclic Graphs](cards-0002.md#paper-154767) | 检查随机因果图能否由亲缘计数轻易排序 |
| 多模态 | 提示选择 | [A Training-Free Video Moment Retrieval Framework via Selection from Multiple Visual Prompts](cards-0002.md#paper-149512) | 分别运行提示并保留原始预测作为候选 |
| 数值优化 | 预条件 | [A Transformer-Derived Iterative Preconditioner](cards-0002.md#paper-153148) | 从模型发现迭代式预条件，再写成独立算法 |
| 概率建模 | 信赖域 | [A Trust Region Approach for Learning Schrödinger Bridges](cards-0002.md#paper-149517) | 目标仅有非归一密度时约束桥接迭代步幅 |
| 图优化 | 投影加速 | [AT-SKM-Net: An Accelerated Trainable Sampling Kaczmarz-Motzkin Framework for Linear Hard-Constraint Feasibility on Dynamic Graphs](cards-0002.md#paper-149152) | 在动态硬约束中复用低秩分解更新 |
| 视觉学习 | 特征提取 | [Attending on Attention ($A^2$): Smaller Self-Supervised ViTs Localize Better Than Larger Ones](cards-0002.md#paper-154201) | 小模型负责定位、大模型负责局部嵌入 |
| 视频生成 | 流式记忆 | [Attend Locally, Remember Linearly: Linear Attention as Cross-Frame Memory for Autoregressive Video Diffusion](cards-0002.md#paper-154730) | 在帧内保留 softmax，跨帧使用固定状态 |
| 多模态 | 人类注视对照 | [Attention Alignment Between Humans and Vision-Language Models](cards-0002.md#paper-155371) | 分开检查编码器与解码器对注意力匹配的影响 |
| 学习理论 | 经验贝叶斯 | [Attention as In-Context Empirical Bayes: A Two-Stage View via Particle Dynamics](cards-0002.md#paper-149497) | 分开调节上下文精炼深度和原始查询保留。 |
| 学习理论 | 谱估计 | [Attention-based PCA](cards-0002.md#paper-154448) | 将上下文主方向恢复用于诊断注意力表示。 |
| 因果学习 | 摊销推断 | [Attention-Based Pretraining for Unsupervised Amortized Causal Discovery](cards-0002.md#paper-153811) | 多个域共享图结构求解器。 |
| 科学机器学习 | 多模态路由 | [Attention-based Routing for Interpretable Multimodal Brain Encoding](cards-0002.md#paper-152519) | 用脑区查询替代全局静态融合。 |
| 大语言模型 | 扩散采样 | [Attention-Based Sampler for Diffusion Language Models](cards-0002.md#paper-149963) | 按注意力列和排序解掩码位置。 |
| 神经符号学习 | 软约束 | [Attention-Based Soft Answer Sets](cards-0002.md#paper-151077) | 将离散求解替换为可微不动点残差。 |
| 大语言模型 | 并行解码 | [Attention-Discounted Adaptive Sampler for Masked Diffusion Language Models](cards-0002.md#paper-150267) | 对依赖已选低置信位置的候选打软折扣。 |
| 大语言模型 | 推测解码 | [Attention Drift: What Auto-Regressive Speculative Decoding Models Learn](cards-0002.md#paper-152952) | 按草稿深度监控状态范数并加归一化。 |
| 多模态学习 | 视觉定位 | [Attention Heads are Complementary Visual Units: Mitigating Hallucinations in LVLMs via Adaptive Visual Cues Focusing](cards-0002.md#paper-149428) | 保留各注意头独有的视觉证据。 |
| 大语言模型 | 路由压缩 | [Attention Is More Than You Need: Spectral Redundancy in Multi-Head Routing](cards-0002.md#paper-155116) | 分别测共享 KV 与实际路由谱冗余。 |
| 计算机视觉 | 流式重建 | [Attention Itself Could Retrieve. RetrieveVGGT: Training-Free Long Context Streaming 3D Reconstruction via Query-Key Similarity Retrieval](cards-0002.md#paper-150300) | 用早层查询键相似度选取固定数量历史帧。 |
| 大语言模型 | 量化稳定性 | [Attention Sinks and Outliers in Attention Residuals](cards-0002.md#paper-148314) | 允许跨层路由显式表达空选择。 |
| 可解释性 | 谱诊断 | [Attention Sinks as Spectral Spikes: A Mechanism Analysis of Gated Attention](cards-0002.md#paper-153587) | 按谱和梯度两条路径检验注意力门控。 |
| 可解释性 | 梯度诊断 | [Attention Sinks Induce Gradient Sinks: Massive Activations as Gradient Regulators in Transformers](cards-0002.md#paper-151217) | 用值路径梯度干预区分汇聚和大激活。 |
| 强化学习 | 训练诊断 | [Attention Trajectories as a Diagnostic Axis for Deep Reinforcement Learning](cards-0002.md#paper-156756) | 按对象和模态追踪显著性轨迹。 |
| 计算机视觉 | 注意力蒸馏 | [Attention Transfer Is Not Universally Effective for Vision Transformers](cards-0002.md#paper-156052) | 跨教师家族前先验证学生架构兼容。 |
| 模型审计 | 来源验证 | [AttnDiff: Attention-based Differential Fingerprinting for Large Language Models](cards-0002.md#paper-151981) | 用差分行为表征交叉验证模型谱系。 |
| 学习理论 | 鲁棒学习 | [Attribute-Efficient Learning of Sparse Halfspaces with Constant Malicious Noise Rate](cards-0002.md#paper-153863) | 稀疏分类遇固定比例污染时按有效维数估算数据。 |
| 高效推理 | 早退出 | [Attribution-Guided Exit Policy for Reliable Early-Exit Inference](cards-0002.md#paper-152941) | 把跨层归因稳定性作为置信度的补充。 |
| 多模态学习 | 表征对齐 | [Attribution-Guided Shared-Private Decoupling for Noise-Reduced Audio-Visual Representation Learning](cards-0002.md#paper-150554) | 用跨模态相关片段监督共享特征。 |
| 可解释性 | 二阶归因 | [Attributions All the Way Down? The Metagame of Interpretability](cards-0002.md#paper-148384) | 分开测特征对输出和对彼此归因的影响。 |
| 联邦学习 | 张量语言 | [A typed tensor language for federated learning](cards-0002.md#paper-150243) | 先检查分布式计算能否表示成固定共享状态。 |
| 强化学习 | 多目标调度 | [Auction-Based Online Policy Adaptation for Evolving Objectives](cards-0002.md#paper-153035) | 为运行期出现或消失的目标动态插拔局部策略。 |
| 多模态学习 | 空间音频 | [Audible World Models: Spatially Aware Sound Generation for 3D Worlds](cards-0002.md#paper-154507) | 把声源附着到三维几何，再按听者位置渲染。 |
| 语音 Agent | 故障归因 | [AudioAgentBench: Evaluating Multi-Turn Voice Agents on Real-World Tasks](cards-0002.md#paper-139120) | 按回合定位第一次失误并避免重复扣分。 |
| 音频生成 | 条件路由 | [AudioCALM: Continuous Autoregressive Language Modeling for Universal Audio Generation](cards-0002.md#paper-149240) | 共享音效和音乐模型，并为语音保留独立残差。 |
| 音频学习 | 压缩表征 | [AudioGS: High-Fidelity Neural Audio Compression via Continuous Gaussian Splatting](cards-0002.md#paper-149852) | 用可渲染基元分解代替训练期码本量化。 |
| 音频学习 | 自监督表征 | [AudioSphere: Towards Self-Supervised Spatial Audio Representation Models](cards-0002.md#paper-151452) | 掩码重建时同时恢复频谱与方向线索。 |
| 多模态学习 | 时序推理 | [Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos](cards-0002.md#paper-153983) | 用时间戳连接长视频的中间音视频证据。 |
| 科学评测 | 错误诊断 | [Auditing AI peer reviewers: a dose-response and false-positive benchmark on real scientific papers](cards-0002.md#paper-152885) | 用严重度梯度和误报率联合评估自动审稿。 |
| 可靠性 | 分布外诊断 | [Auditing Attention Head Masking for Out-of-Distribution Detection: Cross-Architecture Wins, Failures, and Polarity Inversions](cards-0002.md#paper-139256) | 先检查异常分数方向再跨骨干部署。 |
| 医学影像 | 数据审计 | [Auditing Capsule Vision 2024: Within-Split Train-to-Validation Re-Exposure and a Kvasir-Channel Sensitivity Diagnostic](cards-0002.md#paper-139763) | 对视频帧基准按来源视频溯源去重。 |
| 学习理论 | 复现诊断 | [Auditing Closed-Loop Learning in Recurrent Neural Networks: Reproduction, Robustness, and Generalization](cards-0002.md#paper-157025) | 分别衡量闭环训练中的短暂损失峰、最终损失和耦合稳定性。 |
| 统计学习 | 共形校准 | [Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift](cards-0002.md#paper-138875) | 按真实量化与温度配置做覆盖验收。 |
| 医学影像 | 集成诊断 | [Auditing Correlated Failures in Frozen-Feature Pretrained-Encoder Pools for Medical Segmentation](cards-0002.md#paper-138982) | 用病例级误差相关检查骨干是否真的互补。 |
| 多语言学习 | 水印评测 | [Auditing Cross-Lingual Fairness in Language Model Watermarking](cards-0002.md#paper-138923) | 对不同语言分别校准阈值并测阈值无关区分度。 |
| 科研计量 | 证据审计 | [Auditing Evidence Framing at NeurIPS: A Decade-Scale Study of Accepted Papers](cards-0002.md#paper-139236) | 对会议证据风格的时间趋势按主题调整。 |
| 隐私评测 | 表征审计 | [Auditing Privacy Leakage in Tabular Foundation Model Embeddings](cards-0002.md#paper-149397) | 共享嵌入前评估辅助信息存在时的联合泄漏。 |
