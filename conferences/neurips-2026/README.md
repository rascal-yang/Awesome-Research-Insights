# NeurIPS 2026

[首页](../../README.md) · [官方会议目录](https://neurips.cc/Downloads/2026)

官方目录当前列出 **9,144** 个论文海报条目，已筛选 **2189** 篇，暂收录 **2029** 篇。[筛选底册](papers.tsv)按官方海报 ID 记录覆盖及去留。目录可能随会议更新，候选范围核定后统一排名，收录上限为 50%。

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
| 科研可靠性 | 防御审计 | [Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases](cards-0002.md#paper-139641) | 在科研复现中分别验收检测和修复。 |
| 表征学习 | 部署评测 | [Auditing Single-Query Recoverability in Self-Supervised Representations](cards-0002.md#paper-152886) | 单输入系统按单输入验收。 |
| 大语言模型 | 评审校准 | [Auditing the Judge: Human-Grounded Bias Discovery, Quantification, and Mitigation in LLM Judges](cards-0002.md#paper-153728) | 用人机分歧发现偏差，再用受控改写测量偏差。 |
| 大语言模型 | 身份核验 | [Auditor-Assisted Summary-Channel Verification for Hosted LLM Identity Substitution](cards-0002.md#paper-154384) | 以公开推理摘要作为托管模型身份的审计信号。 |
| 计算机视觉 | 输入增强 | [AuGhostmentation: The Eyes Never Stand Still—$\textit{Why Should CNNs?}$](cards-0002.md#paper-152194) | 将弱位移副本叠到原图增强扰动鲁棒性。 |
| 医学影像 | 几何等变 | [Augmented Equivariant Mesh Networks for Anatomical Segmentation](cards-0002.md#paper-153175) | 分别评估网格在标准位姿和旋转扰动下的分割。 |
| 强化学习 | 约束优化 | [Augmented Lagrangian Method for Last-Iterate Convergence for Constrained MDPs](cards-0002.md#paper-155499) | 单策略部署时检验最终迭代收敛。 |
| 优化 | 局部学习 | [Augmented Lagrangian Predictive Coding](cards-0002.md#paper-154623) | 用逐层对偶变量累积预测约束误差。 |
| 统计学习 | 最优传输 | [A Unified Approach for Computing Wasserstein Barycenters of Discrete and Continuous Measures](cards-0002.md#paper-154277) | 混合点云和密度输入时使用统一的重心求解。 |
| 多模态学习 | 音频标记化 | [A Unified Audio Language Model with Text-Aligned Factorized Audio Tokenization](cards-0002.md#paper-154205) | 将语言可表达信息与波形保真信息分开编码。 |
| 隐私 | 风险界 | [A Unified Framework for Adversary-Aware Differential Privacy Bounds](cards-0002.md#paper-153636) | 评估差分隐私时将无输出时的先验成功率纳入比较。 |
| 计算机视觉 | 条件生成 | [A Unified Framework for Image-to-3D Part Generation via Variable Granularity](cards-0002.md#paper-150141) | 在单模型内比较点、框和掩码三种控制。 |
| 机制设计 | 资源分配 | [A Unified Framework for Uniform-Price Resource Allocation Mechanisms](cards-0002.md#paper-154380) | 采用比例式分配时比较统一价格规则。 |
| 图学习 | 跨域对齐 | [A Unified Graph Language Model for Multi-Domain Multi-Task Graph Alignment Instruction Tuning](cards-0002.md#paper-148900) | 按图数据和指令的对齐难度组织训练。 |
| 多模态学习 | 时空编码 | [A Unified Image and Video Encoder for Multimodal LLMs](cards-0002.md#paper-154993) | 把低层时序建模前移到视觉编码器。 |
| 优化 | 学习率迁移 | [A Unified Merge Calculus for Learning-Rate Scaling on Neural Computation Graphs](cards-0002.md#paper-152315) | 按计算图合并方式而非只按深度迁移学习率。 |
| 统计学习 | 结构约束 | [A Unified Neural Architecture for Variable-Wise Shape Constraints](cards-0002.md#paper-149870) | 用结构保证逐变量单调性或曲率。 |
| 图学习 | 域适应 | [A unified pairwise distribution matching framework for graph domain adaptation under structure shift](cards-0002.md#paper-154823) | 边结构变化时对齐连接节点对的分布。 |
| 评测 | 稳健性审计 | [A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation](cards-0002.md#paper-148880) | 给成对偏好排行榜同时报告名次集合、全序和置信区间稳定性。 |
| 优化 | 稀疏求解 | [A Unified Semismooth Newton Approach to Multitask and Multivariate Square-Root Lasso Problems](cards-0002.md#paper-151762) | 多响应平方根 Lasso 用降维半光滑牛顿法。 |
| 多模态 | 目标函数 | [A Unified Spectral Theory of Multimodal Losses](cards-0002.md#paper-155760) | 单侧噪声重时优先检验定向生成 |
| 学习理论 | 上下文学习 | [A Unified Theoretical Framework for Task Recognition and Task Learning in In-Context Learning](cards-0002.md#paper-149830) | 按任务频率分组测提示长度收益 |
| 图学习 | 不确定性 | [A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion](cards-0002.md#paper-151405) | 共享随机嵌入并为校准与 OOD 分设读出 |
| 可解释性 | 组合表示 | [A Unifying Perspective on Language Model Interpretability](cards-0002.md#paper-148396) | 用共同的张量积假设交叉检验探针与干预 |
| 优化 | 算子正则 | [A Unifying View of Anchoring via Operator-Side Tikhonov Regularization](cards-0002.md#paper-153667) | 在算子查询端加入消失的正则以复用原更新 |
| 视觉 / Agent | 闭环工具 | [AURA: An Autonomous Retouching Agent with Photographic Visual Thinking](cards-0002.md#paper-148451) | 长程编辑每步回读图像再决定局部工具操作 |
| 视频生成 | 结构化控制 | [Auteur: Language-Driven Cinematographic Framing for Human-Centric Video Generation](cards-0002.md#paper-155137) | 用相对演员的镜头语言生成关键帧 |
| 大语言模型 | 数据管线评测 | [AutoDataBench: How Far Are LLM Agents from Autonomously Engineering Post-Training Data Pipelines?](cards-0002.md#paper-139001) | 固定学生模型，以训练后的效果检验数据管线 |
| Agent | 离线记忆 | [Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents](cards-0002.md#paper-152534) | 把即时记忆采集和跨会话压缩拆成两个阶段 |
| 计算机视觉 | 标注迁移 | [AutoExpert: Automating 3D LiDAR Annotation from Expert-Crafted Guidelines](cards-0002.md#paper-139399) | 把专家标注规范作为少样本跨模态评测输入 |
| 信息检索 | 多跳推理 | [Autofocus Retrieval: An Effective Pipeline for Multi-Hop Question Answering With Semi-Structured Knowledge](cards-0002.md#paper-156757) | 先提取关系约束，再逐步扩大候选范围 |
| AI 安全 | 防御评测 | [AutoHoney: Automating, Deploying, and Evaluating Scheming Honeypots Across Production Codebases](cards-0002.md#paper-139153) | 分开测任务范围和评测知情状态对审计结果的影响 |
| 可视分析 | 算法选型 | [AutoManifold: Agentic Design of Data Visualisation Algorithms via Manifold Embedding](cards-0002.md#paper-154589) | 按用户的结构保留目标评测嵌入算法 |
| Agent | 故障检测 | [Automata from Agent Traces: Failure and Next-Step Prediction](cards-0002.md#paper-148996) | 跨轨迹建有限状态机并监控各状态失败信号 |
| 因果推断 | 方法搜索 | [Automated Causal Effect Estimation through Self-Evolving AI](cards-0002.md#paper-150563) | 有代理回报时分别评估代理和真实效应误差 |
| 数据质量 | 标注诊断 | [Automated Hypothesis Discovery for Characterizing Annotation Disagreement](cards-0002.md#paper-139723) | 留出验证用于筛选生成的分歧假设 |
| 优化 | 核设计 | [Automated Kernel Discovery Towards Understanding High-dimensional Bayesian Optimization](cards-0002.md#paper-149210) | 用留一概率评分选核并分离数学提案和实现 |
| 优化 / Agent | 经验记忆 | [Automated Reformulation of Robust Optimization via Memory-Augmented Large Language Models](cards-0002.md#paper-148230) | 把失败推导整理成可跨底座移植的重写经验 |
| 软件工程 | 规则优化 | [Automatically Refining Coding Rules for AI Coding Agents](cards-0002.md#paper-153609) | 用留出功能测试筛选自动变异的编程规则 |
| 强化学习 | 约束优化 | [Automatic Constraint Policy Optimization based on Continuous Constraint Interpolation Framework for Offline Reinforcement Learning](cards-0002.md#paper-151401) | 用验证反馈自调离线策略约束类型。 |
| Agent / 科学机器学习 | 研究评测 | [Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?](cards-0002.md#paper-139352) | 区分智能体的工程调参与领域创新。 |
| Agent | 记忆学习 | [AUTOMEM: Automated Learning of Memory as a Cognitive Skill](cards-0002.md#paper-150660) | 把文件记忆决策与任务动作分开优化。 |
| 多模态 | 状态评测 | [Automotive-ENV: Benchmarking Multimodal Models in Automotive Cockpit Environments](cards-0002.md#paper-139849) | 用环境状态验收 GUI 行为。 |
| Agent | 持续适配 | [Autonomous Continual Learning for Environment Adaptation of Computer-Use Agents](cards-0002.md#paper-154225) | 用上一轮反馈生成贴近当前能力的课程。 |
| 科学机器学习 | 假设检验 | [Autonomous Scientific Discovery via Iterative Meta-Reflection](cards-0002.md#paper-149249) | 将已验证的发现作为下一轮假设生成输入。 |
| 计算机视觉 | 动态表征 | [Autoregressive Appearance Prediction for 3D Gaussian Avatars](cards-0002.md#paper-154526) | 用历史外观隐状态解释同姿态不同外观。 |
| Agent | 离线评估 | [Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents](cards-0002.md#paper-153481) | 让目标策略在每个模拟转移后重新行动。 |
| 学习理论 | 自回归估计 | [Autoregressive Learning in Joint KL: Sharp Oracle Bounds and Lower Bounds](cards-0002.md#paper-154406) | 用联合 KL 区分错设近似与序列估计误差。 |
| 多模态 | 奖励分解 | [Auto-Rubric as Reward: From Implicit Preference to Explicit Generative Criteria](cards-0002.md#paper-151565) | 比较输出前先生成任务特定的质量细则。 |
| Agent | 执行迭代 | [AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](cards-0002.md#paper-151256) | 用留出任务检验从失败轨迹提出的配置修订。 |
| Agent | 协作管理 | [AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation](cards-0002.md#paper-151734) | 在固定预算下比较共享实验状态和固定中央分工。 |
| 数学推理 | 数据合成 | [AuxGeoAgent: Synthesizing Challenging Geometry Proving Data via Planning and Symbolic Deduction](cards-0002.md#paper-139298) | 按是否需要辅助构造定向生成练习。 |
| 多模态 | 强化学习 | [Auxiliary Clues Aware’s Geometry Problem Solving](cards-0002.md#paper-149037) | 按图形线索对证明推理的贡献加权。 |
| 多模态 | 编辑评测 | [AVENUE: Audio-Video Editing Understanding and Evaluation](cards-0002.md#paper-138887) | 逐样本记录目标改动及应保留模态。 |
| 脑科学 | 混杂控制 | [AVID: A 5T fMRI Dataset for Benchmarking Auditory-induced Visual Mental Imagery Decoding](cards-0002.md#paper-139564) | 用听觉诱发想象控制视觉刺激混杂。 |
| 多模态 | 传感融合 | [AVI-HT: Adaptive Vision-IMU Fusion for 3D Hand Tracking](cards-0002.md#paper-154518) | 遮挡条件下按传感器动态调节可信度。 |
| 多模态 | 推理预算 | [AVIS: Adaptive Test-Time Scaling for Vision–Language Models](cards-0002.md#paper-150182) | 联合分配视觉 token 和推理采样次数。 |
| Agent / 系统 | 进化搜索 | [AVO: Agentic Variation Operators for Autonomous Evolutionary Search](cards-0002.md#paper-153311) | 让变异算子访问谱系和执行反馈。 |
| 多模态学习 | 令牌压缩 | [AVOC: Enhancing Hour-Level Audio-Video Understanding in Omni-Modal LLMs via Retrieval-Inspired Token Compression](cards-0002.md#paper-154191) | 按相关性、重要性和多样性选择长视频令牌。 |
| 图学习 | 拓扑学习 | [Avoiding Feature Collapse in Graph ODEs via Hysteretic Topology Evolution](cards-0002.md#paper-150833) | 需要长期保留差异时改变有效边支持。 |
| AI 对齐 | 监督协议 | [Avoiding Obfuscation with Prover-Estimator Debate](cards-0002.md#paper-148404) | 审查递归辩论双方的计算负担。 |
| 大语言模型 | 自蒸馏 | [AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals](cards-0002.md#paper-150780) | 用跨教师视图共识确定更新方向。 |
| 医学影像 | 表征预训练 | [A World Model of Radiologist Reading for Medical Image Representation Learning](cards-0002.md#paper-154476) | 把专家扫视顺序作为训练监督。 |
| 计算机视觉 | 推理剪枝 | [AWP: Activation-based Window Pruning for Gigapixel Object Detection](cards-0002.md#paper-151192) | 先测 FFN 激活均值能否无训练地选窗。 |
| 强化学习 | 多智能体分解 | [Axiomatic Reinforcement Learning for Open Multi-Agent Systems from Shapley Axioms](cards-0002.md#paper-148243) | 以合作博弈公理约束开放队伍的个体值。 |
| 大语言模型 / 科学推理 | 奖励设计 | [Axiomatic World Modeling for Physics Reasoning](cards-0002.md#paper-150823) | 给物理前提建模和求解过程分别评分。 |
| 优化 / 系统 | 并行求解 | [B$^3$-PWL: GPU-Batched Branch-and-Bound for Piecewise-Linear Optimization with SOS2 Constraints](cards-0002.md#paper-150051) | 批量求解分支定界中的松弛子问题。 |
| 优化 | 梯度估计 | [B2P-Corr: Batch-to-Population Gradient Estimators for Non-Decomposable Correlation Losses](cards-0002.md#paper-154786) | 对相关系数损失维护跨批矩统计量。 |
| Agent / 世界模型 | 在线模型修订 | [Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models](cards-0002.md#paper-150860) | 把更新后丢失的旧转移用作反例。 |
| 学习理论 / 评测 | 观察式归纳 | [BabyTheorist: A Benchmark for Learning to Theorize the World from Observation Alone](cards-0002.md#paper-139168) | 测试从未标组的持续观测里归纳可复用规则。 |
| 科学机器学习 | 动态图估计 | [BACE: Behavior-Adaptive Connectivity Estimation from Multi-Region Neural Recordings](cards-0002.md#paper-151970) | 用行为条件图预测神经活动并检查边稳定性。 |
| 生成模型 / 评测 | 异常检测 | [Backbone-Equated Diffusion OOD via Sparse Internal Snapshots](cards-0002.md#paper-154161) | 在匹配骨干和测试成本后检查单次内部快照。 |
| 模型安全 | 防御评测 | [Backdoor Attacks Rerouted: BatchNorm as a Sink for Adversarial Signals](cards-0002.md#paper-155957) | 单独检验可疑模型的归一化统计及防御效果。 |
| 模型安全 | 适配器净化 | [Backdoor Purification for LoRA-Tuned LLMs via Null-Space Projection](cards-0002.md#paper-153189) | 在隔离验证环境检查可疑适配器的净化与技能保留。 |
| 大语言模型 | 多目标偏好 | [Back to Blackwell: Closing the Loop on Intransitivity in Multi-Objective Preference Fine-Tuning](cards-0002.md#paper-148405) | 当偏好循环时保留多目标判据。 |
| 语言模型 | 推理搜索 | [Backtracking with Linear-in-Depth Search-Space Growth: Width-Limited Tree Search for Large Language Models](cards-0002.md#paper-155253) | 同预算比较有无回溯及宽度约束 |
| 优化 | 多任务学习 | [Balanced Multi-Task Learning from an Optimality-Gap Perspective](cards-0002.md#paper-153699) | 比较损失尺度与局部改进上限两种归一化 |
| 生成模型 | 频谱损失 | [Balancing Frequencies and Pixels in Flow Matching](cards-0002.md#paper-151310) | 分别消融频谱监督和阶段切换 |
| 生成模型 | 分层编码 | [Balancing Image Compression and Generation with Bootstrapped Tokenization](cards-0002.md#paper-155939) | 固定 token 预算对照分层与混合编码 |
| 视觉 | 自监督表征 | [BAL: Bidirectional Autoregression in Latent Space for Learning Human Movement Representations](cards-0002.md#paper-152565) | 分别消融双向训练与局部目标 |
| 多模态 | 奖励设计 | [BalCapRL : A Balanced Framework for RL-Based MLLM Image Captioning](cards-0002.md#paper-149366) | 分别测长度、忠实性和表达后再调组合奖励 |
| Agent | 模型路由 | [Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery](cards-0002.md#paper-154569) | 同预算对照均值路由与谱系信用 |
| 语言模型 | 信用分配 | [BALTO: Balanced Token-Level Policy Optimization for Hallucination Mitigation](cards-0002.md#paper-150212) | 在混合正误回答中对照局部和整段奖励 |
| 强化学习 | 在线表示 | [Bandits via Additive Quantized Representations](cards-0002.md#paper-155168) | 固定内存比较原特征及分级量化表示 |
| Agent | 评测 | [BankerToolBench: Evaluating AI Agents in End-to-End Investment Banking Workflows](cards-0002.md#paper-139094) | 分别统计单产物错误与跨文档矛盾 |
| 视觉 | 少样本分割 | [BAPM: Boundary-Aware Prompt Mining for Training-Free Few-Shot Medical Image Segmentation](cards-0002.md#paper-155064) | 同预算比较随机负提示和可信边界负提示 |
| 语言模型 | 安全控制 | [BarrierSteer: LLM Safety via Learning Barrier Steering](cards-0002.md#paper-148333) | 联合测量漏判、误拒与任务质量 |
| 视觉 | 连续控制 | [Barycentric Guidance: Turning Foundation Image Editors into Continuous Affective Controllers](cards-0002.md#paper-153096) | 用控制平面全域误差替代少量端点测试 |
| 推荐 / 语言模型 | 持续适配 | [Base Items Overfit, New Items Underfit: Hidden Cost of Joint Training in Incremental Adaptation](cards-0002.md#paper-156066) | 绘制旧新质量随训练时长变化的独立曲线 |
| 视觉 | 长尾学习 | [BasicLT: Basic-Level Abstraction and Selective Differentiation for Long-Tailed Recognition](cards-0002.md#paper-150159) | 按类频率和粗类置信分组测细化收益 |
| 科学机器学习 | 摊销推断 | [BASIL-DCM: Biophysical Amortized Scalable Inference for Latent Dynamic Causal Modeling](cards-0002.md#paper-152400) | 用前向谱一致性验证摊销生成参数 |
| 深度学习 | 注意力参数化 | [Basis-Mediated Bilinear Attention: A New Method for Greatly Reducing Query--Key Pathway Parameters](cards-0002.md#paper-154941) | 同预算比较共享基、完全共享和独立低秩 |
| 语言模型 | 推理解码 | [BASTION: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting](cards-0002.md#paper-151263) | 相同草稿下比较固定及自适应预算 |
| 视觉 | 流式重建 | [BAT3R: Robust Online 3D Reconstruction with Bayesian Adaptive State Updates](cards-0002.md#paper-153286) | 分开测历史区域保护及新场景更新 |
| 视觉 | 几何细化 | [BA-T: An Iterative Transformer for Two-View Bundle Adjustment](cards-0002.md#paper-148295) | 同延迟比较重复几何层和加深解码器 |
| 多模态 | 测试时适配 | [Batch-Conditioned Semantic Anchors for Robust Transductive Adaptation of Vision--Language Models](cards-0002.md#paper-154091) | 按批次可靠性移动语义锚点 |
| 学习理论 | 受限通信 | [Batched Stochastic Linear Bandits with 1-Bit Communication Constraints](cards-0002.md#paper-150229) | 将批反馈位预算单列为遗憾项 |
| 多模态 | 联合生成 | [Baton: Explicit Semantic Blueprints for Joint Video-Audio Generation](cards-0002.md#paper-153708) | 去噪前对齐关键帧级音视频计划 |
| 鲁棒学习 | 蒸馏 | [BayesAT: Bayes-Guided Progressive Distillation for Semi-Supervised Adversarial Training](cards-0002.md#paper-150593) | 按学习阶段提高教师标签温度 |
| 统计学习 | 分布回归 | [Bayesian Additive Distribution Regression](cards-0002.md#paper-152064) | 用浅树先验表达分布值输入的低维边际 |
| 统计学习 | 不确定性估计 | [Bayesian Backprop as Belief Propagation: Single-Pass Predictive Uncertainty](cards-0002.md#paper-154383) | 用单次矩传播代替重复采样推理 |
| 因果推断 | 实验设计 | [Bayesian Causal Experimental Design for CATE Estimation under Noncompliance](cards-0002.md#paper-154028) | 以处理效应的信息增益挑选鼓励实验 |
| 因果推断 | 敏感性分析 | [Bayesian Causal Stress Testing: Posterior Fragility of Treatment-Effect Conclusions](cards-0002.md#paper-155177) | 分别报告后验区间和推翻主张的最小扰动 |
| 决策理论 | 专家反馈 | [Bayesian Decision Making around Experts](cards-0002.md#paper-149882) | 用单位更新预算的信息价值选择专家或自身数据 |
| 优化 | 函数空间搜索 | [Bayesian Optimization on Function Spaces via Sparse RKHS Manifolds](cards-0002.md#paper-150567) | 在稀疏核表示中直接优化函数 |
| 优化 | 信赖域 | [Bayesian Optimization with Fisher Information Geometry: Gradient Bounds and Trust-Region Methods](cards-0002.md#paper-156134) | 用代理后验局部敏感度设置搜索尺度 |
| 大语言模型 | 奖励适配 | [Bayesian Preference Learning for Test-Time Steerable Reward Models](cards-0002.md#paper-150486) | 通过示例更新潜在偏好以调节奖励模型 |
| 大语言模型 | 测试时搜索 | [Bayesian Test-Time Inference of Task-Aligned Similarity from Weak Interactive Feedback](cards-0002.md#paper-152715) | 根据少量反馈动态推断当前任务的相似性轴 |
| 评测 | 评判校准 | [BayesJudge: Uncertainty-Aware Bayesian Meta-Evaluation of Human and LLM Judgments](cards-0002.md#paper-138918) | 保留平局并交换候选次序以测位置偏差 |
| 统计学习 | 评测上限 | [Bayes-Optimal BER and AUC: Estimation and Evaluation of Estimators](cards-0002.md#paper-152377) | 类别失衡时估计最优 BER 或 AUC 而非准确率上限 |
| 联邦学习 | 持续学习 | [Bayes-pFCL:Bayesian Personalized Federated Continual Learning](cards-0002.md#paper-149379) | 分别量化任务更新和聚合造成的知识漂移 |
| 多模态 | 检索增强 | [BayesRAG: Probabilistic Mutual Evidence Corroboration for Multimodal Retrieval-Augmented Generation](cards-0002.md#paper-154974) | 用语义与版面互证重排图文组合 |
| Agent | 协作诊断 | [Bayes-Sufficient Compression Is Not Enough: How Communication Helps in Multi-Agent Systems?](cards-0002.md#paper-155601) | 比较压缩消息、原始上下文和不通信 |
| Agent / 优化 | 基准诊断 | [BBOWP-Bench: Evaluating LLMs on Black-Box Optimization Word Problems](cards-0002.md#paper-139160) | 分别验收黑箱优化的搜索空间构造和算法选择 |
| 统计学习 | 因果推断 | [B-CALM: Bias-Limited Bayesian Borrowing for RCT-Anchored Treatment Effects under Covariate Mismatch](cards-0002.md#paper-155646) | 用偏差先验限制外部数据借用。 |
| 大语言模型 | 模型融合 | [BDC-Merge: Cross-Architecture Model Merging via Dependency Alignment](cards-0002.md#paper-151593) | 用非线性依赖对齐异构模型。 |
| 具身智能 | 域适应 | [BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation](cards-0002.md#paper-151303) | 按样本差异学习源示范权重。 |
| Agent / 教育 | 行为模拟 | [BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation](cards-0002.md#paper-155338) | 把策略决策与执行生成分开，保留模拟学习者错误。 |
| 多模态学习 | 分层评测 | [BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories](cards-0002.md#paper-139293) | 分别评估识别状态与判断动作可执行性。 |
| 图学习 | 子图搜索 | [BeamWitness: Rooted Subgraph Beam Search for Selective Graph Representation Learning](cards-0002.md#paper-149610) | 预测前显式搜索有限数量的连通证据子图。 |
| 科学机器学习 | 三维表征 | [BEAST3D: animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting](cards-0002.md#paper-149762) | 已知标定时用留出视角渲染预训练行为表征。 |
| Agent / 数据库 | 运行合规评测 | [Be CARE-ful with Text-to-SQL Benchmarks](cards-0002.md#paper-139633) | 将查询正确性与并发、权限、完整性和效率分开验收。 |
| 生成模型 | 流匹配 | [Beckmann Transport Models: From Autonomous Flows to One-Step Maps](cards-0002.md#paper-154577) | 在低维目标分布条件下比较自治流与直接一步映射。 |
| 强化学习 | 部分可观测控制 | [BECON: Belief-Conditioned Constrained Multi-Objective Reinforcement Learning under Drifting Preferences and Budgets](cards-0002.md#paper-153172) | 按不确定性融合推断的任务偏好与外部信号。 |
| 多模态学习 | 表征诊断 | [Before It Fades: Reinforcing Temporal Representations at Inference Time in VideoLLMs](cards-0002.md#paper-155460) | 用反转帧序定位时间信号衰减并在推理期补回。 |
| 多模态学习 | 分层评测 | [Before Words, Beyond Speech: Evaluating Nonverbal Social Reasoning in Early Childhood](cards-0002.md#paper-139741) | 把社会推理拆成情景、行为和人际关系层级。 |
| 大语言模型 | 后训练诊断 | [Behaving Better, Thinking Worse: Sycophancy Across Post-Training Stages](cards-0002.md#paper-153819) | 联合比较生成翻转率与同样本预测概率。 |
| 强化学习 | 行为搜索 | [Behavioral Foundation Models for Quality Diversity](cards-0002.md#paper-148386) | 在预训练行为潜空间内做质量多样性搜索。 |
| 计算机视觉 | 表征对齐 | [Behavioral Geometric Supervision Aligns Video Foundation Models with Human Social Perception](cards-0002.md#paper-149277) | 用人类视频相似性判断监督局部和全局嵌入几何。 |
| Agent | 信息流诊断 | [Behavioral Probes for Information Flow in LLM Swarms](cards-0002.md#paper-149644) | 用外部依赖与参数知识依赖辅助智能体结构选择。 |
| 个性化建模 | 离线评测 | [BehaviorBench: Modeling Real-World User Decisions from Behavioral Traces](cards-0002.md#paper-138919) | 将用户信念推断与下一步动作预测分别测量。 |
| 模仿学习 | 蒸馏理论 | [Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback](cards-0002.md#paper-150673) | 有噪教师下优先验证学生访问状态上的在线蒸馏。 |
| 强化学习 | 奖励鲁棒性 | [Behavior-Discriminative Reward Shaping for Reward-Robust Reinforcement Learning](cards-0002.md#paper-155941) | 按策略排序等价类定义奖励不确定集。 |
| 多模态学习 | 强化后训练 | [Behavior Pack Optimization for Video MLLM Post-Training](cards-0002.md#paper-150981) | 把同一视频问题的反事实视图作为联合奖励单位。 |
| 表情分析 | 多任务优化 | [Behaviour4All: A Dependency-Aware Toolkit for in-the-wild Facial Behaviour Analysis](cards-0002.md#paper-150818) | 用任务依赖约束部分标注联合训练 |
| Agent | 状态更新 | [Belief Engine: Configurable Stance Dynamics for Multi-Agent LLM Deliberation](cards-0002.md#paper-151258) | 让立场变化受显式证据吸收与先验锚定控制 |
| 强化学习 | 收缩性分析 | [Bellman Contraction under MMD: A Unified Framework](cards-0002.md#paper-150640) | 用差分核条件检验分布式 Bellman 更新的收缩 |
| 大语言模型 | 防御评测 | [BELLS-O: Evaluating the Operational Trade-offs of LLM Supervision Systems](cards-0002.md#paper-139421) | 采购监督模型时联测检出、误报、成本和延迟 |
| Agent | 评估偏差 | [Below the Reliability Floor: Recovering True Success from Judge-Gated Loops](cards-0002.md#paper-156773) | 重试门控后独立抽取金标准验证真实成功率 |
| 大语言模型 | 表示诊断 | [Benchmark for Assessing Olfactory Perception of Large Language Models](cards-0002.md#paper-139778) | 对同一问题比较名称输入和结构输入 |
| 大语言模型 | 基准审计 | [Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs](cards-0002.md#paper-138960) | 区分基准的辨别力、饱和余量和实际采用 |
| 大语言模型 | 防御监测 | [Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs](cards-0002.md#paper-139423) | 将安全分类与分布外报警独立融合 |
| 多模态学习 | 结构生成 | [Benchmarking and Optimizing Multimodal Structured Generation: The OracleGraph Dataset and PRISM Framework](cards-0002.md#paper-149901) | 用图级诊断向自蒸馏教师提供结构错误信息 |
| 表格学习 | 算子选型 | [Benchmarking Attention for Tabular Foundation Models](cards-0002.md#paper-139839) | 按行列注意力形状分别选择计算后端 |
| 科学机器学习 | 泛化评估 | [Benchmarking Compositional Generalisation for Machine Learning Interatomic Potentials](cards-0002.md#paper-139491) | 以组合留出代替只做随机样本划分 |
| 具身多模态 | 评测分解 | [Benchmarking Fine-Grained Spatio-Temporal Awareness in Embodied Brain Models](cards-0002.md#paper-139463) | 单独评估语义理解与时空定位 |
| 图学习 | 基准复核 | [Benchmarking Graph Self-Supervised Learning for Node-Level Tasks: Insights and Strong Baseline](cards-0002.md#paper-138872) | 公平调参后再决定采用生成式或对比式预训练 |
| 大语言模型 | 隐私审计 | [Benchmarking Membership Privacy Risks in Preference-Based LLM Post-Training](cards-0002.md#paper-139392) | 按完整偏好记录衡量隐私风险 |
| 多模态学习 | 视觉推理评测 | [Benchmarking Multimodal Mathematical Reasoning with Explicit Visual Dependency](cards-0002.md#paper-139044) | 用多图显式依赖检查何时真的需要视觉 |
| Agent | 协作评测 | [Benchmarking Open-Ended Multi-Agent Coordination in Language Agents](cards-0002.md#paper-139589) | 用可控协作难度区分个人生存和团队协调 |
| 大语言模型 | 行为评估 | [Benchmarking Risk Attitudes of LLMs](cards-0002.md#paper-139608) | 在相同感知风险下比较模型采取的动作 |
| 时序预测 | 故障评测 | [Benchmarking Sensor-Fault Robustness in Forecasting](cards-0002.md#paper-138912) | 单独比较干净精度与故障最坏误差。 |
| 科学机器学习 | 基准诊断 | [Benchmarking sequence-to-ensemble predictors on UNICORNEdb, a UniProt-grouped database of PDB-derived conformational ensembles](cards-0002.md#paper-138904) | 按同一实体配对观测，避免相似样本差异混入状态变化。 |
| 大语言模型 | 领域评测 | [Benchmarking Vietnamese Legal Knowledge of Large Language Models](cards-0002.md#paper-139241) | 按法条层级和认知难度分层构造评测。 |
| Agent | 部署审计 | [Benchmark Recovery Does Not Certify a Frozen Tool-Trigger Contract After Quantization](cards-0002.md#paper-155241) | 量化验收时固定工具权限与参考标签，再单独检查触发。 |
| 大语言模型 | 基准诊断 | [Benchmarks Are Not Atomic: Composition-Aware LLM Evaluation using BenchHub](cards-0002.md#paper-139267) | 用属性分布匹配应用后再比较模型。 |
| 统计学习 | 测量可靠性 | [Benchmarks as Measurement Instruments: Quantifying Signal and Noise for More Efficient AI Evaluations Under Distribution Shift](cards-0002.md#paper-139555) | 按目标模型群体估计题目对排名的测量价值。 |
| 大语言模型 | 数据消融 | [Benchmark Shadows: How Data Regimes Shape Parameter Footprints and Generalization](cards-0002.md#paper-154989) | 把重复和频率集中分开，对照后续多样数据能否修复。 |
| 多智能体学习 | 实验设计 | [Bench-MFG: A Benchmark Suite for Learning in Stationary Mean Field Games](cards-0002.md#paper-139725) | 按耦合类型分层生成随机博弈实例。 |
| 科学机器学习 | 诊断评测 | [BenchRep-T: A Systematic Evaluation of T-Cell Repertoire-Based Disease Diagnostics](cards-0002.md#paper-139621) | 在诊断模型选型中同时控制测序深度和人口统计混杂。 |
| 大语言模型 | 防御验收 | [Benign Reinforcement Learning Can Amplify Latent Backdoors](cards-0002.md#paper-149677) | 在强化学习后重新进行安全回归测试。 |
| 统计学习 | 序贯推断 | [Bentkus-type asymptotic e-values](cards-0002.md#paper-155963) | 需要较紧的事后区间时对照 Bentkus 型 e 值。 |
| 多模态学习 | 生成架构 | [Bernini: Latent Semantic Planning for Video Diffusion](cards-0002.md#paper-154106) | 用视觉语义潜变量作为规划器和视频渲染器的接口。 |
| 生成模型 | 快速采样 | [Bernoulli Flow Models: Self-Consistent Generative Modeling for Binary Data](cards-0002.md#paper-155986) | 二值扩散跳步时使用与间隔一致的后验。 |
| 科学机器学习 | 表征诊断 | [BESS-Bench: Benchmarking Spectral Representations for Be-Star Variability](cards-0002.md#paper-139851) | 分别用形态探测和下一观测预测选时序模型。 |
| 强化学习 | 纯探索 | [Best Arm Identification for Bandits with Shifting Means](cards-0002.md#paper-153746) | 奖励存在共同漂移时用重要性加权取代固定均值停止检验。 |
| 强化学习 | 主动查询 | [Best Arm Identification in Generalized Linear Bandits via Hybrid Feedback](cards-0002.md#paper-151037) | 把单臂绝对观测和成对比较纳入同一查询设计。 |
| 生成模型 | 推理引导 | [Best-of-$N$ Guidance for Test-time Diffusion Alignment](cards-0002.md#paper-154666) | 并行去噪过程中用当前优选粒子引导其余样本。 |
| 统计学习 | 序贯检验 | [Bet Imaginatively, not Historically in Independent-Data Sequential Testing](cards-0002.md#paper-155229) | 独立同分布假设成立时，用重排历史估计下注收益。 |
| 大语言模型 | 架构诊断 | [Better Language Models Require Better Domain-Specific Inductive Biases](cards-0002.md#paper-140098) | 激活函数搜索后加跨领域移植对照。 |
| 生成模型 | 流匹配 | [Better Source, Better Flow: Learning Condition-Dependent Source Distribution for Flow Matching](cards-0002.md#paper-148679) | 学习条件源分布 |
| 科学机器学习 | 高分辨率表示 | [Beyond 3 Million Tokens: A Multi-Modal Foundation Model for Full-Resolution Heliophysics](cards-0002.md#paper-152539) | 保留掩码区域的压缩频率视图 |
| Agent | 诊断评测 | [Beyond Accuracy: A Diagnostic Benchmark for Hypothesis-Driven Experiment Planning in LLM Agents](cards-0002.md#paper-139344) | 拆分实验规划各环节评测 |
| 大语言模型 | 压缩 | [Beyond Adjacent Layers: Graph-Guided Layer Fusion for Compressing Large Language Models](cards-0002.md#paper-152044) | 按全层相似性选保留层 |
| 具身智能 | 行为校准 | [Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models](cards-0002.md#paper-150087) | 分别测任务保持和任务改变后的动作 |
| 多模态学习 | 数据审计 | [Beyond a Single Score: An Audit of Aesthetic Evaluation in Text-to-Image Pipelines Across Subcultural Visual Languages](cards-0002.md#paper-139303) | 按风格报告审美过滤保留率 |
| 学习理论 | 专家路由 | [Beyond Augmented-Action Surrogates for Multi-Expert Learning-to-Defer](cards-0002.md#paper-148942) | 解耦类别与各专家的训练头 |
| 优化 | 域泛化 | [Beyond Average Flatness: Domain-wise Flatness for Domain Generalization](cards-0002.md#paper-150477) | 按域测尖锐度并约束域间不平衡 |
| 多模态学习 | 组合评测 | [Beyond Bag-of-Words: Diagnosing Compositional Binding Failures in Vision-Language Models](cards-0002.md#paper-139620) | 配对最小场景和真实上下文 |
| 计算机视觉 | 来源标识 | [Beyond Bit Matching: Orthogonal Watermarks for Collusion-Resistant Image Fingerprinting](cards-0002.md#paper-148565) | 按检测误报约束设计图像指纹 |
| 优化 | 随机优化 | [Beyond Bounded Variance: Variance-Reduced Normalized Methods for Nonconvex Optimization under Blum-Gladyshev Noise](cards-0002.md#paper-150036) | 根据噪声增长和光滑性选择归一化更新 |
| 具身智能 | 地图评测 | [Beyond Chamfer Distance: Granular Order-aware Evaluation Metric For Online Mapping](cards-0002.md#paper-139462) | 区分折线排序、定位和检出 |
| 强化学习 | 策略优化 | [Beyond Clipping: Signed Logarithmic Smoothing for Policy Optimization](cards-0002.md#paper-153088) | 平滑整个重要性加权优势而非只截断比率 |
| 大语言模型 | 置信校准 | [Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs](cards-0002.md#paper-149177) | 按任务类型选择自评维度 |
| 可视化 | 降维 | [Beyond Contraction: Geometry-Faithful Supervised Dimensionality Reduction for Data Visualization](cards-0002.md#paper-155065) | 优先正则读出平滑并约束邻域扭曲 |
| 图学习 | 结构编码 | [Beyond Coordinates: Encoding Graph Structure via Contextual Distribution and Relational Similarity](cards-0002.md#paper-148246) | 使用上下文分布和相似核表示局部结构 |
| 视频生成 | 诊断评测 | [Beyond Copy-Paste: How Well Do Subject-Driven Video Models Understand Their Subjects?](cards-0002.md#paper-152728) | 用未见同主体目标检验身份保持 |
| 大语言模型 | 后训练 | [Beyond Correctness: Robustness-Driven Evolutionary Self-Training for Large Language Models](cards-0002.md#paper-151953) | 按推理轨迹的扰动稳健性筛选正确答案 |
| 具身智能 | 表征预训练 | [Beyond Data Scaling: Representation-Centric Pre-training for Vision-Language-Action Models](cards-0002.md#paper-155956) | 共享跨本体动作监督并允许下游换头 |
| 大语言模型 / 多模态 | 参数高效适配 | [Beyond Decoupled PEFT: Geometry-Aware Low-Rank Adaptation via Riemannian Reparameterization](cards-0002.md#paper-153695) | 把低秩方向预算限定在权重方向的切空间 |
| 强化学习 | 课程学习 | [Beyond difficulties: Insights for provably efficient design of autocurriculum in RLVR](cards-0002.md#paper-149187) | 按训练收益而非当前成功率选题 |
| 视觉生成 | 蒸馏 | [Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation](cards-0002.md#paper-154363) | 在输出分布匹配外加入内部预测监督 |
| 智能体 | 技能迁移 | [Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns](cards-0002.md#paper-152827) | 按页面布局结构复用正常交互技能 |
| 三维视觉 | 控制诊断 | [Beyond Downstream Scores: Controlled Diagnostics for Point-Cloud Self-Supervised Learning Evaluation](cards-0002.md#paper-139098) | 将预训练信号、可见几何和读出分别消融 |
| 科学机器学习 | 评测设计 | [Beyond Drug Discovery: The Nanotechnology Molecular Optimization (NMO) Benchmark](cards-0002.md#paper-139426) | 采用物理模拟检验代理分数能否代表科学效用 |
| 动力系统 | 相似性 | [Beyond DSA: Conjugacy-based Comparison of Dynamical Systems](cards-0002.md#paper-152248) | 将对齐约束为状态双射诱导的变换 |
| 表征学习 | 谱分析 | [Beyond Eigenfunctions: Divergence Principal Functions for Representation Learning](cards-0002.md#paper-153338) | 按训练散度选择低秩表示几何 |
| 可靠性 | 分布外评测 | [Beyond Empirical Support: Structured Outlier Generation via Sinkhorn Optimal Transport](cards-0002.md#paper-151741) | 在弱支持边界构造受语义约束的压力样本 |
| 多模态学习 | 组件消融 | [Beyond Encoder Accumulation: Measuring Encoder Roles in Multi-Encoder VLMs](cards-0002.md#paper-152266) | 重新训练编码器组合而非仅在固定权重上遮蔽 |
| 持续学习 | 记忆预算 | [Beyond Exemplar Selection: Value-Aware Memory Allocation in Replay-Based Continual Learning](cards-0002.md#paper-155700) | 在固定缓存中按类别效用调整配额 |
| 强化学习 | 风险规划 | [Beyond Expected Values: Risk-Sensitive Planning with Distributional Monte-Carlo Tree Search](cards-0002.md#paper-149403) | 在树边维护回报分布以评估嵌套尾部风险 |
| 三维视觉 | 结构先验 | [Beyond Family Labels: A Taxonomic Ornstein-Uhlenbeck Prior for Avian 3D Shape Recovery](cards-0002.md#paper-151996) | 用连续分类树距离替代同科二元标签 |
| 大语言模型 | 能力校准 | [Beyond Fixed Benchmarks and Worst-Case Attacks: Dynamic Boundary Evaluation for Language Models](cards-0002.md#paper-139552) | 用靠近模型能力边界的题估计可比较分数 |
| 多模态学习 | 长视频 | [Beyond Flat Frames: Hierarchical Graph Reasoning for Long Video Understanding](cards-0002.md#paper-152948) | 用事件图粗检索后再找关键帧 |
| 分布式学习 | 通信 | [Beyond Flat Gossip: Tiered Gossip Learning for Scalable Collaborative AI](cards-0002.md#paper-154579) | 将数据持有节点与高容量混合节点分层 |
| 图学习 | 层次生成 | [Beyond Flat Walks: Compositional Abstraction for Autoregressive Graph Generation](cards-0002.md#paper-152657) | 在复杂图上对照社区分解与平坦线性化 |
| 高效推理 | 静态部署 | [Beyond FLOPs: Train-Full, Deploy-Partial Multi-Exit Inference via Selective Lightweight IC Ensemble](cards-0002.md#paper-152802) | 使用校准后的静态截断替代逐样本动态退出 |
| 视觉表征 | 生成蒸馏 | [Beyond Generation: Unlocking Discriminative Representations from Diffusion Models](cards-0002.md#paper-150350) | 以生成的类 token 作为判别学习教师 |
| 多模态学习 | 组合对齐 | [Beyond Global Alignment: Structured Compositional Reasoning for Vision-Language Models](cards-0002.md#paper-155609) | 分开监督关系方向与属性的对象归属 |
| 大语言模型 | 评测诊断 | [Beyond Ground Truth: Evaluating Non-Verifiable Reasoning in LLMs through Moral Robustness](cards-0002.md#paper-154911) | 用多轮一致性评估价值判断。 |
| 多模态学习 | 区域对齐 | [Beyond Hard Negatives: Grounded Positive Supervision for Compositional CLIP](cards-0002.md#paper-150916) | 用结构化正例改善属性绑定。 |
| 大语言模型 | 模拟诊断 | [Beyond High and Low: Evaluating Graded Cognitive Diversity in LLM Persona Simulations](cards-0002.md#paper-138966) | 使用反思错误分布检验模拟人群。 |
| 学习理论 | 可识别性 | [Beyond ICA: Identifiability by Symmetry Breaking](cards-0002.md#paper-150471) | 用对称性条件判断潜表示能否恢复。 |
| 表格学习 | 基准诊断 | [Beyond IID: How General Are Tabular Foundation Models, Really?](cards-0002.md#paper-139490) | 选表格模型时分别检查时间、分组与 IID 划分。 |
| 统计学习 | 保形校准 | [Beyond Imputation: Mask-Adaptive Conformal Prediction via Tree Embeddings on General Missing Data Mechanisms](cards-0002.md#paper-154427) | 在缺失掩码层面检查覆盖率。 |
| 可解释性 | 组合搜索 | [Beyond Incremental Beam Search for Compositional Explanations of Neurons](cards-0002.md#paper-152763) | 避免按单个概念增量扩展时过早丢掉解释候选。 |
| 多模态学习 | 表征干预 | [Beyond Interpretability: When, Why, and How Sparse Autoencoders Enable Label-Free Visual Steering](cards-0002.md#paper-148658) | 用逐样本重建误差决定是否采用稀疏特征修正。 |
| 推荐系统 | 离线评测 | [Beyond IPS: Reliable Counterfactual Evaluation in Multi-Stage Ad Systems without Logged Propensities](cards-0002.md#paper-151796) | 无记录倾向时对直接奖励估计做目标分布校正。 |
| 时序学习 | 训练数据剪枝 | [Beyond Isolation: Neighbor-Consistent Data Pruning for Multivariate Time Series Forecasting](cards-0002.md#paper-154771) | 用重叠窗口的损失轨迹一致性诊断异常样本。 |
| 自监督学习 | 表征几何 | [Beyond Isotropy in JEPAs: Hamiltonian Geometry and Symplectic Prediction](cards-0002.md#paper-149858) | 通过跨视图预测耦合注入结构先验。 |
| 统计学习 | 排序聚合 | [Beyond Kemeny Medians: Consensus Ranking Distributions. Definition, Properties and Statistical Learning](cards-0002.md#paper-149736) | 用多个局部共识代表有分群的排序分布。 |
| 概率建模 | 采样 | [Beyond Langevin: Sampling Multimodal Densities using the Witten Laplacian on 1-forms](cards-0002.md#paper-155804) | 区分跨模态路径探索和盆地内采样。 |
| 大语言模型 | 表征控制 | [Beyond Linear Activation Steering: Invertible Latent Transformations for Controlling LLM Behavior](cards-0002.md#paper-148807) | 对照固定方向和随输入变化的潜空间干预。 |
| 时序学习 | 专家路由 | [Beyond Linear Decoders: Dynamic Expert-Coupled Optimal Decoding for Time Series Forecasting](cards-0002.md#paper-153816) | 依据变量动态选择预测解码专家。 |
| Agent | 故障归因 | [Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution](cards-0002.md#paper-149719) | 用轻量轨迹图替代长文本故障归因。 |
| 图学习 | 分数阶扩散 | [Beyond Local Neighborhoods: Fractional Diffusion with Levy Flights on Simplicial Complexes for Link Prediction](cards-0002.md#paper-148623) | 需要跨远距离高阶关系时测试单纯形上的非局部扩散。 |
| 大语言模型 | 微调路由 | [Beyond LoRA vs. Full Fine-Tuning: Gradient-Guided Optimizer Routing for LLM Adaptation](cards-0002.md#paper-154880) | 在优化器层动态分配低秩和全量更新。 |
| 神经形态计算 | 频率选择 | [Beyond Low-Pass Dynamics: Frequency-Selective Spiking Reservoirs with Resonant Neurons](cards-0002.md#paper-148662) | 用异构共振单元辨别不同时标。 |
| 统计学习 | 局部校准 | [Beyond Marginal Coverage: Efficient Localized Conformal Prediction via Residual Rank Calibration](cards-0002.md#paper-153265) | 用标准化残差的局部秩代替逐查询的加权分位数。 |
| 系统效率 | 稀疏算子 | [Beyond Masked Sparsity: SNACK Enables Truly Sparse Neural Networks on GPU](cards-0002.md#paper-150469) | 高稀疏度时改用真正稀疏的前后向 |
| 统计学习 | 参数估计 | [Beyond Maximum Likelihood: Variational Inequality Estimation for Generalized Linear Models](cards-0002.md#paper-152448) | 对非标准链接用变分不等式估计 |
| 视觉 | 逆问题 | [Beyond MMSE: Enhancing PnP Restoration with ProxiMAP](cards-0002.md#paper-151995) | 使残余噪声匹配去噪器训练噪声 |
| 量子学习 | 表征诊断 | [Beyond MNIST: Limitations of Amplitude Encoding on Quantum Classification](cards-0002.md#paper-150197) | 诊断编码集中后再投入训练 |
| 多模态 | 模型融合 | [Beyond Modality Fusion: Deep Ensembles for Multimodal Classification](cards-0002.md#paper-155113) | 等参数比较单模态集成和特征融合 |
| 信号处理 | 结构保真 | [Beyond MSE: Differentiable Complexity Priors for Structure-Preserving Neural Denoising](cards-0002.md#paper-153782) | 用复杂度一致性监督去噪 |
| 图学习 | 离散扩散 | [Beyond Node Sequences: Relational Diffusion for Unified Graph Learning](cards-0002.md#paper-148255) | 以边为基本生成单位 |
| 视觉 | 异常检测 | [Beyond Normal References: Discriminative Few-Shot Anomaly Detection](cards-0002.md#paper-153262) | 将异常参考用于学习偏离正常的方向 |
| 强化学习 | 先验诊断 | [Beyond One-Size-Fits-All: Diagnosis-Driven Online Reinforcement Learning with Offline Priors](cards-0002.md#paper-140053) | 用在线证据决定何时削弱离线先验 |
| Agent | 过程奖励 | [Beyond Outcome Rewards: Process-Aware Optimization for Search Agents](cards-0002.md#paper-148305) | 按结果和当前证据调整搜索奖励 |
| Agent | 自蒸馏 | [Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents](cards-0002.md#paper-154780) | 只在失败轨迹上按步骤调整优势幅度 |
| 大语言模型 | 提示优化 | [Beyond Outcome: Trajectory-Driven Prompt Optimization via Multi-Dimensional Rewards](cards-0002.md#paper-150285) | 监督反思过程的一致性 |
| 图学习 | 传播诊断 | [Beyond Oversquashing: Understanding Signal Propagation in GNNs Via Observables](cards-0002.md#paper-154868) | 测特定源到目标区域的信号输运 |
| 大语言模型 | 偏好优化 | [Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph](cards-0002.md#paper-150929) | 按偏好图聚合多样本，平局不给梯度 |
| 联邦学习 | 行为蒸馏 | [Beyond Parameter Aggregation: Semantic Consensus for Federated Fine-Tuning of LLMs](cards-0002.md#paper-155550) | 异构客户端共享行为语义而非参数 |
| 大语言模型 | 模型合并 | [Beyond Parameter Arithmetic: Sparse Complementary Fusion for Distribution-Aware Model Merging](cards-0002.md#paper-149097) | 合并时跟踪终止和重复异常 |
| 强化学习 | 离线博弈 | [Beyond Pessimism: Offline Learning in KL-regularized Games](cards-0002.md#paper-153617) | 在 KL 正则下检验是否需要悲观估计 |
| 视觉 | 扩散采样 | [Beyond Pixel Space: Frequency-Domain Uncertainty Estimation for Structure-Aware Diffusion Guidance](cards-0002.md#paper-152220) | 在频域估计不确定性并引导去噪 |
| 视觉 | 边界监督 | [Beyond Pixel-wise Supervision: Local Structure Regularization for Semantic Segmentation](cards-0002.md#paper-154585) | 监督语义概率的局部结构强度与方向 |
| Agent | 世界模型 | [Beyond Prediction: Steering VLM Agents with Retrospective World Modeling](cards-0002.md#paper-155042) | 用逆向解释一致性作为过渡奖励 |
| 可解释性 | 人机评测 | [Beyond Proxy Metrics: MLLM-Based Human Surrogate Evaluation for Explainable AI](cards-0002.md#paper-152905) | 按解释用途选择指标并校验模型代评 |
| Agent | 记忆检索 | [Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation](cards-0002.md#paper-150607) | 先拆出区分性事实再聚合 |
| 大语言模型 | 联邦检索 | [Beyond Raw Context Transfer: Representation-based Federated Retrieval-Augmented Generation](cards-0002.md#paper-150023) | 比较跨站点表征与原文交换 |
| 自动驾驶 | 记忆表征 | [Beyond Raw Observations: Distilling and Storing Invariant Driving Memories for Generalizable Autonomous Driving](cards-0002.md#paper-152198) | 检索决策相关不变量 |
| 计算机视觉 | 图像取证 | [Beyond Real or Fake: A Dual-Channel Authenticity and Reasoning Protocol for Photographic Assessment](cards-0002.md#paper-154533) | 分别审计相机指纹和内容一致性 |
| 大语言模型 | 社会推理评测 | [Beyond Right and Wrong: Evaluating Second-order Social Reasoning in Large Language Models](cards-0002.md#paper-139315) | 将规范识别与观察者反应分开测试 |
| 多模态学习 | 安全数据 | [Beyond Risky Activities: Bridging the Supervision Gap for Situational Risk Reasoning](cards-0002.md#paper-139234) | 构造同一行为在不同场景的风险对照 |
| 计算机视觉 | 立体校正 | [Beyond Row Alignment: Virtual-Camera-Aware Online Stereo Rectification](cards-0002.md#paper-151291) | 用深度可用性评价在线校正 |
| 多模态学习 | 属性监督 | [Beyond Scalar Distances: Semantic Attribute Gradients from Frozen MLLMs for Visual Embeddings](cards-0002.md#paper-153671) | 从成对图像的属性判断学习检索表征 |
| 计算机视觉 | 视频分割 | [Beyond [SEG] Tokens: Training-Free Video Reasoning Segmentation via Counterfactual Inference  and Contrastive Concept](cards-0002.md#paper-154601) | 先离散选择实例再跟踪 |
| 多模态学习 | 视觉压缩 | [Beyond Selection: Token Parameterization for Extreme Visual Token Compression](cards-0002.md#paper-151663) | 将基底截断与坐标组织独立设计 |
| 自动驾驶 | 基准诊断 | [Beyond Self-Play and Scale: A Behavior Benchmark for Generalization in Autonomous Driving](cards-0002.md#paper-139295) | 将训练模拟器表现与标准规划基准分开验证 |
| 统计学习 | 概率融合 | [Beyond Semantic Alignment: Geometric Incomparability in Multi-Oracle Soft Fusion](cards-0002.md#paper-149809) | 先校准概率几何再做软融合 |
| Agent | 检索 | [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](cards-0002.md#paper-155649) | 允许检索策略根据中间证据调整查询操作 |
| 学习理论 | 推理诊断 | [Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens](cards-0002.md#paper-156774) | 单独区分中间计算支架与可读语义的贡献 |
| 多模态学习 | 后训练 | [Beyond SFT-to-RL: Pre-alignment via Black-box On-policy Distillation for Multimodal RL](cards-0002.md#paper-153111) | 在监督微调和强化学习间加入分布对齐 |
| 多模态学习 | 空间先验 | [Beyond Single Expert: Harmonizing Diverse Visual Priors in MLLMs for Spatial Understanding](cards-0002.md#paper-150326) | 按任务融合互补视觉先验 |
| 计算机视觉 | 扩散推理 | [Beyond Single-Shot Conditioning: Test-Time Condition Refinement for Diffusion-Based Image Restoration](cards-0002.md#paper-153799) | 在推理期间更新视觉条件 |
| 科学机器学习 | 动力学建模 | [Beyond Single-Step Likelihood: Gibbs Variational Last Layers for Long-Horizon Dynamics Learning](cards-0002.md#paper-152213) | 用多步损失训练贝叶斯末层 |
| 医学影像 / 多模态 | 弱监督对齐 | [Beyond Sparse Captions: Aligning Slide-Level Text and Patch-Level Vision in Pathology](cards-0002.md#paper-149751) | 用切片级报告查询局部图像特征 |
| 计算机视觉 | 密集匹配 | [Beyond Spatial and Temporal Priors: A Generalizable Approach for Dense Correspondence Matching](cards-0002.md#paper-149352) | 以身份一致性学习非物理连续的对应关系 |
| 多模态学习 | 表征约束 | [Beyond Spatial-Domain Supervision: A Relation Constrained Space for Multi-Modal Image Fusion](cards-0002.md#paper-150788) | 在关系空间监督融合 |
| 医学影像 | 半监督学习 | [Beyond Stabilization: Dual-EMA Teachers for Global–Local Semantic Learning in Semi-Supervised Medical Image Segmentation](cards-0002.md#paper-153534) | 用两种 EMA 时间尺度分别监督整体和局部 |
| 大语言模型 | 推理干预 | [Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention](cards-0002.md#paper-155564) | 比较激活上的固定向量与概念条件动态变换 |
| 大语言模型 | 参数高效微调 | [Beyond Structural Agnosticism: Stable-Rank-Guided LoRA for Structure-Aware Fine-Tuning](cards-0002.md#paper-151865) | 按层谱结构与任务梯度分配低秩容量 |
| 强化学习 | 评测诊断 | [Beyond Success Rates: Trainability and Extractability in Offline GCRL](cards-0002.md#paper-139429) | 以超参数景观比较策略提取的鲁棒性 |
| Agent | 在线监控 | [Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents](cards-0002.md#paper-152482) | 检查长程前缀是否仍符合授权任务 |
| Agent | 能力诊断 | [Beyond Task Success: Probing Cognitive Primitives in Web Agents](cards-0002.md#paper-139465) | 用配对任务隔离规划和探索能力 |
| 生成模型 | 强化微调 | [Beyond the Dirac Delta: Mitigating Diversity Collapse in Reinforcement Fine-Tuning for Image Generation](cards-0002.md#paper-155487) | 在固定对齐要求下显式评估多样性 |
| 推荐系统 | 稳健性评测 | [Beyond the Full Slate: Evaluating MNL Algorithms on All Slates](cards-0002.md#paper-149458) | 按实际小候选集而非全库误差选模型 |
| 图学习 | 双向蒸馏 | [Beyond the Golden Teacher: Enhancing Graph Learning through LLM-GNN Co-teaching](cards-0002.md#paper-150344) | 让文本和图模型互教并追踪何时由冲突转为一致 |
| 信号处理 | 连续稀疏分解 | [Beyond the Grid: Continuous Dictionary Pursuit for Interpretable Signal Decomposition](cards-0002.md#paper-151808) | 在连续参数空间拟合可解释信号原子 |
| 在线优化 | 公平分配 | [Beyond the Half Approximation: Fair and Efficient Online Class Matching](cards-0002.md#paper-153402) | 按阈值在类别公平和匹配效率之间切换 |
| 多模态学习 | 表征诊断 | [Beyond the Linear Separability Ceiling: Aligning Representations in VLMs](cards-0002.md#paper-156758) | 用线性探针区分视觉表示不足和读出失败 |
| 机器学习系统 | 并行策略 | [Beyond the Node Barrier: Zero-Shot Strategy Planning for LLM Training on Super-Nodes](cards-0002.md#paper-149841) | 在高速互连平台重新评估跨节点张量和专家并行 |
| 大语言模型 | 防护检测 | [Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs](cards-0002.md#paper-151177) | 用扩散解码前的响应表征补充输入风险检测 |
| 时间序列 | 表示学习 | [Beyond the Readout: Reservoir State Statistics for Model-Space Learning under Sparse Observations](cards-0002.md#paper-152483) | 用动态轨迹统计补充稀疏通道的拟合参数 |
| 统计学习 | 偏移风险估计 | [Beyond the Training Distribution: Evaluating Predictions Under Distribution Shift and Selection Bias](cards-0002.md#paper-149001) | 同时校正目标协变量偏移和选择性标签 |
| 机器学习系统 | 分布式训练调参 | [Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training](cards-0002.md#paper-150603) | 先用小规模测量和全局推演筛训练配置 |
| 具身智能 | 空间先验 | [Beyond Thinking: Imagining in 360$^\circ$ for Humanoid Visual Search](cards-0002.md#paper-149744) | 用多假设空间布局引导主动搜索。 |
| 多模态 | 时空定位 | [Beyond Token Representations: Explicit Visual Object Grounding for Video Reasoning Segmentation](cards-0002.md#paper-155293) | 将分割目标明确为框和点，并跨查询校准。 |
| 生成模型 | 蒸馏 | [Beyond Trajectory Matching: Reflow with Marginal Distribution Alignment](cards-0002.md#paper-155442) | 沿每段蒸馏轨迹同时约束终点边际。 |
| 大语言模型 | 行为评测 | [Beyond Truthfulness: Evaluating Honesty in Large Language Models](cards-0002.md#paper-139425) | 将模型知道正确答案和是否如实表达分开计分。 |
| 计算机视觉 | 可控恢复 | [Beyond Unidirectional: Unsupervised Trajectory Learning for Omnidirectional Controllable Underwater Image Enhancement](cards-0002.md#paper-151882) | 训练任意源目标强度间的相对变换。 |
| 大语言模型 | 检索校验 | [Beyond Uniform Detection: Adaptive Hallucination Detection for RAG Across Response Regimes](cards-0002.md#paper-155755) | 按回答类型切换幻觉检测信号。 |
| 科学机器学习 | 守恒动力学 | [Beyond Unit-Circle Eigenvalues: Invariant Bases for Stable State Space Dynamics](cards-0002.md#paper-149242) | 同时约束特征值和守恒量对应的模态基底。 |
| 多模态 | 视频检索 | [Beyond Visual Boundaries: Rethinking Scene Segmentation for Movie RAG](cards-0002.md#paper-139396) | 按叙事事件切分电影检索单元。 |
| 医学影像 | 密集表征 | [Beyond ViT Tokens: Masked-Diffusion Pretrained Convolutional Pathology Foundation Model for Cell-Level Dense Prediction](cards-0002.md#paper-148943) | 需要像素级连续性时比较卷积掩蔽扩散与 patch 预训练。 |
| 学习理论 | 推理预算 | [Beyond What Seems Necessary: Hidden Gains from Scaling Training-Time Reasoning Length under Outcome Supervision](cards-0002.md#paper-151533) | 用分布外验证决定训练推理长度。 |
| 具身智能 | 动作表征 | [Beyond World-Frame Action Heads: Motion-Centric Action Frames for Vision-Language-Action Models](cards-0002.md#paper-155672) | 先在学习的运动局部坐标中组装动作。 |
| 优化 | 数据压缩 | [Beyond Worst-Case Coreset Bounds for $k$-Clustering via Determinantal Sampling](cards-0002.md#paper-148163) | 自然分布假设成立时比较行列式采样构造聚类核心集。 |
| 生理信号 | 连续表征 | [B[FM]$^2$: Brain Foundation Model via Flow Matching with SplitUNet](cards-0002.md#paper-148190) | 按时间和电极轴分别卷积，只沿时间下采样。 |
| 大语言模型 | 强化学习 | [BFS-PO: Best-First Search for Large Reasoning Models](cards-0002.md#paper-153193) | 训练时将最短正确分支作为优先探索对象。 |
| Agent | 运维编排 | [Bian Que: An Agentic Framework with Flexible Skill Arrangement for Online System Operations](cards-0002.md#paper-148501) | 将事件相关数据和知识选择封装为可修订技能。 |
| 计算机视觉 | 检测审计 | [BIAS-ID: A Framework for Analyzing Transformation Biases in AI-Generated Image Detectors](cards-0002.md#paper-139597) | 分开评估变换偏差与一般鲁棒性。 |
| 图学习 | 误差诊断 | [Bias, Measurement Error, and Double-Dipping: When Can GNN Convolutions Help Brain Connectome Prediction?](cards-0002.md#paper-153204) | 用独立估计图与同样本图对照检查重复使用测量噪声。 |
| 大语言模型 | 偏好优化 | [Bias-Variance Optimized Preference Optimization for Large Reasoning Models](cards-0002.md#paper-152470) | 把普通推理梯度与空推理分支梯度混合降方差。 |
| 优化 | 层级代理 | [Bidirectional Information Flow (BIF) - A Sample Efficient Hierarchical Gaussian Process for Bayesian Optimization](cards-0002.md#paper-149175) | 用父子双向反馈拟合组合目标 |
| 生成模型 | 稀疏注意力 | [Bidirectional Sparse Attention for Faster Video Diffusion Training](cards-0002.md#paper-154292) | 同时筛查询和键值 |
| 科学机器学习 | 多解建模 | [Bifurcation Models: Learning Set-Valued Solution Maps with Weight-Tied Dynamics](cards-0002.md#paper-149009) | 用吸引子集合表示多个正确解 |
| 计算机视觉 | 大图生成 | [BigCell: Generating Gigapixel Whole-Slide Images](cards-0002.md#paper-152972) | 按区域重要性调度滑窗生成 |
| 生成模型 | 记忆诊断 | [Bigger Isn't Always Memorizing: Early Stopping Overparameterized Diffusion Models](cards-0002.md#paper-156775) | 数据规模变化后重新校准早停点 |
| 计算机视觉 | 稀疏检测 | [BiHashFormer: Hash-Driven Dual-Branch Transformer for Efficient Object Detection in HRW Shots](cards-0002.md#paper-152107) | 用快速补偿支路覆盖主检测器遗漏 |
| 大语言模型 | 数据加权 | [Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning](cards-0002.md#paper-155173) | 用真实验证任务学习合成轨迹权重 |
| 机器人学 | 定位 | [BiLi: Bridging the Last Mile in LiDAR Localization](cards-0002.md#paper-153081) | 将地图流形约束与时序蒸馏结合 |
| 学习理论 | 在线匹配 | [Bilinear Matching Bandits](cards-0002.md#paper-149557) | 利用双线性结构设计分行探索 |
| 大语言模型 | 低比特推理 | [BiLoCo: Binary Low-Rank Corrections for LLM FP4 Decode](cards-0002.md#paper-149418) | 用符号低秩残差和主矩阵乘并行 |
| 多模态学习 | 离散扩散 | [BiMoGen: Bidirectional Motion-Text Generation via Unified Masked Discrete Diffusion](cards-0002.md#paper-152019) | 训练时暴露自身预测并在早期纠错 |
| 统计学习 | 结构表示 | [Binary Regression:  Universal Ising Model, Binary Expansion and Beyond](cards-0002.md#paper-155424) | 以辅助二值变量表示高阶依赖 |
| 多模态学习 | 表征对齐 | [Binding Multiple Modalities via Multimodal Wasserstein Barycenter](cards-0002.md#paper-149098) | 用跨模态重心作为对齐中心 |
| 多模态学习 | 视觉推理 | [Binding Visual Features Point by Point](cards-0002.md#paper-148298) | 让模型先指向对象再判断其属性 |
| 科学机器学习 | 结构正则化 | [Biological Graph Priors Enable Representation Learning for Cellular Microscopy](cards-0002.md#paper-150999) | 用已知关系约束显微图像表征 |
| 多模态学习 | 域适应 | [Biomedical Acquisition-induced Style Shifts as Mixture Shifts: Style-aware Mixture-of-Experts Multimodal Prompt Learning](cards-0002.md#paper-152391) | 将设备风格偏移当成潜在成分比例变化 |
| 科学机器学习 | 图像质量验证 | [BioMicroAgents: A Co-evolutionary Multi-Agent Framework for High-Fidelity Biomicroscopy Imaging](cards-0002.md#paper-155868) | 用独立验证阶段检查增强是否保留结构 |
| 安全评测 | 级联验证 | [BioSafetyBench: Agentic Cascade Evaluation for the Bio-AI Ecosystem](cards-0002.md#paper-138924) | 用独立评估器核对中间产物与下游风险 |
| Agent | 能力评测 | [BioXArena: Benchmarking LLM Agents on Multi-Modal Biomedical Machine Learning Tasks](cards-0002.md#paper-138952) | 固定骨干和资源再比较代理框架 |
| Agent | 强化学习 | [BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments](cards-0002.md#paper-152242) | 复用数据库副本时保证轨迹状态隔离 |
| 视觉 | 三维重建 | [Birth-Death Structural Learning for 3D Gaussian Splatting](cards-0002.md#paper-155061) | 用重建损失的一阶变化选增删原语 |
| 安全 | 防护验证 | [BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition](cards-0002.md#paper-152920) | 对可信执行环境的参数隔离做独立验证 |
| 视觉 | 生成建模 | [BitDance: Scaling Autoregressive Generative Models with Binary Tokens](cards-0002.md#paper-153956) | 用扩散预测高容量二值视觉码而非枚举类别 |
| 语言模型 | 推理加速 | [BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models](cards-0002.md#paper-154757) | 将接受前缀同时对齐缓存与执行图复用 |
| Agent | 学习理论 | [Bits Beat Tokens: A Regret Rate Distortion Theory for Large Language Model Agents](cards-0002.md#paper-150556) | 用决策相关信息量衡量上下文而非长度 |
| 模型架构 | 脉冲网络 | [BitShift-RoPE: Zero-FLOP Relative Positional Encoding for Spiking Neural Network Transformers](cards-0002.md#paper-150476) | 用整数循环移位实现相对位置编码 |
| 优化 | 零阶估计 | [Black-Box Followers, White-Box Leaders: Partial Zeroth-Order Methods for MPECs](cards-0002.md#paper-155774) | 仅对不可微的未知响应做零阶估计 |
| 统计学习 | 模型审计 | [Black-box model classification under the discriminative factorization](cards-0002.md#paper-154419) | 先估计查询集合的判别能力再分配审计预算 |
| 语言模型 | 不确定性量化 | [Black-Box Uncertainty Quantification for Large Language Models via Ensemble-of-Ensembles](cards-0002.md#paper-151082) | 比较同提示采样和语义等价改写的变异 |
| 语言模型 | 数据选择 | [BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training](cards-0002.md#paper-152234) | 动态更新用于超额损失选择的参考模型 |
| 模型训练 | 局部学习 | [BLANP: Memory-Efficient Backpropagation-Free Local Training via Antithetic Node Perturbation](cards-0002.md#paper-155644) | 内存紧张时比较局部反向梯度与对偶扰动更新 |
| 视觉 | 三维动画 | [BLARM: Animating 3D Objects from Video via Blending LAtent Rigid Motion Primitives](cards-0002.md#paper-155225) | 将网格变形表示为共享刚体运动的混合 |
| 多模态 | 联邦学习 | [BLEND: Balancing Personalization vs. Generalization in Federated Vision–Language Models](cards-0002.md#paper-154470) | 将共享跨模态调节与客户端投影分开 |
| 科学机器学习 | 集合预报 | [BlendCast: Teaching Vision-Language Model to Anticipate Member Skill in Weather Ensembles](cards-0002.md#paper-149073) | 按变量和大气状态预估成员权重 |
| 多模态 | 可验证智能体 | [BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](cards-0002.md#paper-151100) | 按场景状态差异为3D编辑生成可验证奖励 |
| 科学机器学习 | 预报评测 | [Blind-Window Forecasting: Real-Time Benchmarking and Multimodal Reconstruction for Tropical Cyclones](cards-0002.md#paper-150222) | 按推理时真实可获得的时间戳构造预报测试 |
| 优化 | 块重采样 | [Blocked Gibbs meets Diffusion Transformers: Unsupervised Learning for Constraint Optimization](cards-0002.md#paper-148271) | 用退火块大小实现离散约束的局部大步修正 |
| 科学机器学习 | 逆问题 | [BlockFormer: Transformer-based inference from interaction maps](cards-0002.md#paper-153580) | 让交互图逆推模型兼容实体数量和大小变化 |
| 大语言模型 | 剪枝 | [Block-OBS-GS: Exact Per-Block Joint Brain Surgery with Gauss–Seidel Refinement for LLM Pruning](cards-0002.md#paper-152355) | 固定剪枝掩码后精确求块内权重并做跨块校正 |
| 强化学习 | 遗憾分析 | [Block Optimism for Nonstationary Bandits with Latent Linear Dynamics](cards-0002.md#paper-151108) | 潜状态受动作影响时按有限记忆块做乐观探索 |
| 大语言模型 | 强化学习后训练 | [Block-R1: Rethinking the Role of Block Size in Multi-domain Reinforcement Learning for Diffusion Large Language Models](cards-0002.md#paper-139480) | 训练扩散语言模型时按样本选 rollout 块大小 |
| 大语言模型 | 稀疏注意力 | [Block Sparse Flash Attention](cards-0002.md#paper-155122) | 在计算精确查询键分数后按块阈值省去低价值计算 |
| 高效机器学习 | 向量量化 | [Block Sphere Vector Quantization](cards-0002.md#paper-152314) | 根据重建或检索目标选择量化准则 |
| 高效机器学习 | 注意力求导 | [Block-Wise Differentiable Sinkhorn Attention: Tail-Refinement Gradients with a Gap-Aware Dustbin Bridge](cards-0002.md#paper-155973) | 只对迭代求解器的短精修尾部求导，以降低存储 |
| 计算机视觉 | 三维重建 | [Blur Issue Matters for Thermal Novel View Synthesis: A Floating Gaussian Suppression Approach](cards-0002.md#paper-148566) | 识别单通道成像中亮度和透明度相互补偿 |
| 大语言模型 | 注意力量化 | [BMAttn: Block-Aligned Mixed-Precision Attention Quantization for LLM Inference](cards-0002.md#paper-152092) | 分块分配精度以兼顾重要性和 GPU 规则访存 |
| 大语言模型 | 推理评测 | [BoardGameArena: A Multi-Dimensional Benchmark for Strategic Reasoning of LLMs in Board Games](cards-0002.md#paper-139541) | 分别测试合法走子和实际策略选择 |
| 优化 | 基准审计 | [BO-Arena: An Evolving Benchmark for High-Dimensional Bayesian Optimisation](cards-0002.md#paper-138938) | 用公共实现和简单 GP 对照检验高维优化新方法 |
| 可信机器学习 | 防御评测 | [BodyBench: Evaluating Adversarial Image Defenses Against AI Nudification Inpainting](cards-0002.md#paper-139845) | 以实际危害指标验证隐私防护 |
| 优化 | 稀疏决策 | [BONSAI: Bayesian Optimization with Natural Simplicity and Interpretability](cards-0002.md#paper-155059) | 在限制采集效用损失时尽量保留默认配置 |
| 神经科学 / 多模态 | 数据增强 | [Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation](cards-0002.md#paper-154738) | 按数据来源调节合成与真实观测的训练配比 |
| 图学习 | 对比表征 | [Boosting Graph Contrastive Learning via Manifold-Guided Representation Disentanglement](cards-0002.md#paper-151362) | 对增强视图只在共享子空间约束一致性 |
| 大语言模型 | 递归推理 | [Boosting Inference with Guided Reasoning: Stochastic Exploration for Recursive Models](cards-0002.md#paper-149759) | 仅在停止头能区分好轨迹时用随机推理搜索 |
| 大语言模型 | 奖励塑形 | [Boosting LLM Reasoning via Human-Inspired Reward Shaping](cards-0002.md#paper-153592) | 错误阶段鼓励探索，成功后再惩罚冗长 |
| 强化学习 | 经验回放 | [Boosting Multiagent Reinforcement Learning at High Replay Ratios with Ensemble Reset](cards-0002.md#paper-149143) | 高回放比下监控休眠神经元并周期重置价值集成 |
| 强化学习 | 经验回放 | [Boosting Off-Policy RLVR with Data-Centric Replay](cards-0002.md#paper-154959) | 控制轨迹陈旧度 |
| 视觉生成 | 推理筛选 | [Boosting Text-to-Image Diffusion Models via Core Token Attention-Based Seed Selection](cards-0002.md#paper-152409) | 按早期注意力挑种子 |
| 统计学习 | 多重检验 | [BOOST: Power-Optimal Strong-FWER Testing for Block-Structured Multiplicity](cards-0002.md#paper-152078) | 按块分配检验预算 |
| 强化学习 | 课程设计 | [Boost Reasoning Evolution via Responsive Rollout Difficulty Manipulation](cards-0002.md#paper-154872) | 按单题成功率调整提示长度 |
| Agent | 开发环境 | [BootstrapAgent: Turning Repository Setup into Reusable Agent Knowledge](cards-0002.md#paper-151994) | 把安装与诊断记录为可冷启动复验的契约 |
| 强化学习 | 生成策略 | [Bootstrapped Bipartite Actor-Critic for Diffusion RL](cards-0002.md#paper-155139) | 用动作Q差为成对偏好加权 |
| 学习理论 | 偏好决策 | [Borda-Based Fair Multi-User Dueling Bandit in Tabular and Generalized Linear Settings](cards-0002.md#paper-155261) | 按用户Borda效用构建纳什福利 |
| 表征学习 | 压缩评测 | [Bottleneck Benchmark: Sequence Compression Under Controlled Difficulty and Fixed Latent Size](cards-0002.md#paper-139737) | 固定潜变量尺寸再扫任务难度 |
| 大语言模型 | 推理诊断 | [Boule or Baguette? A Study on Task Topology, Length Generalization, and the Benefit of Reasoning Trace](cards-0002.md#paper-151781) | 分开测证明深度和任务广度 |
| Agent | 工具链诊断 | [Boundary-Induced Forgetting in Large Language Model Tool Chains: Measuring Field-Routing Failures](cards-0002.md#paper-155598) | 按字段依赖测跨工具传播 |
| 表征学习 | 数据效率 | [Boundary Mass in Feature Space as a Label-Budget Diagnostic for Representations](cards-0002.md#paper-149689) | 测边界附近的特征质量判断标注需求 |
| 计算机视觉 | 渐进压缩 | [Bound-Conditioned Latent Inference for Progressive Image Compression](cards-0002.md#paper-149342) | 用已解码符号约束连续潜变量 |
| 计算成像 | 误差估计 | [Bounding Global and Local Compression Error of Signal Parameterizations](cards-0002.md#paper-148822) | 用不同压缩级预测之差估计误差 |
| 科学机器学习 | 外推诊断 | [Bounds on Extrapolation across Phase Transitions with Generalized Regression](cards-0002.md#paper-153578) | 用广义特征值问题估计跨相外推风险 |
| 多模态学习 | 视觉提示 | [BoxTuning: Object-Aware Visual Prompting for  Multimodal Model Fine-Tuning](cards-0002.md#paper-149433) | 在视频帧中直接绘制物体空间状态 |
| 大语言模型 | 量化微调 | [BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning](cards-0002.md#paper-149729) | 用二值适配器替代半精度适配器 |
| 多模态学习 | 缺失模态 | [BRACE: Bipolar Reference-Aware Calibration and Estimation for Incomplete Multimodal Learning](cards-0002.md#paper-150021) | 利用上下参考群判断修正方向 |
| 神经科学 | 语音解码 | [Brain2voice 2.0: High-performance voice synthesis brain-computer interface](cards-0002.md#paper-148803) | 联合监督连续声学、离散声学和音素 |
| 神经科学 | 证据监督 | [BrainCoT: A Multi-Task Zero-Shot Brain Signal Foundation Model with Neurometric-Anchored Chain-of-Thought Reasoning](cards-0002.md#paper-155614) | 将神经指标作为可核对的预测依据 |
| 神经科学 | 图注意力 | [Brain Economy-Aligned Graph Transformers](cards-0002.md#paper-153903) | 把结构成本注入连接而非节点 |
| 科学机器学习 | 评测 | [BrainEM: A Large-Scale and Diverse Benchmark for EM Neuron Segmentation in Connectomics](cards-0002.md#paper-139121) | 分开测目标域少量标注与纯跨源复用。 |
| 多模态学习 | 时频预训练 | [Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG](cards-0002.md#paper-155505) | 共享专家与模态专属专家分工。 |
| 多模态学习 | 证据评测 | [BrainTRACE: Tracing Longitudinal, Multimodal, and Volumetric Evidence in Brain MRI Clinical Reasoning](cards-0002.md#paper-139162) | 把纵向综合结论拆为可核查的证据链。 |
| 科学机器学习 | 时序预测 | [BrainVista: Modeling Naturalistic Brain Dynamics as Multimodal Next-Token Prediction](cards-0002.md#paper-153166) | 把刺激输入对齐到预测查询，并切断未来信息。 |
| 多模态学习 | 迁移适配 | [BrainWhisperer: Leveraging Whisper for Speech Decoding in Neuroprosthetics](cards-0002.md#paper-155029) | 将会话漂移交给分层低秩投影。 |
| 科学机器学习 | 条件生成 | [BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics](cards-0002.md#paper-155412) | 用受试者的静态结构条件约束动态生成。 |
| 大语言模型 | 形式化评测 | [BraveATA: Benchmarking Broad and Verifiable End-to-End Automated Theoretical Analysis of Large Language Models](cards-0002.md#paper-139549) | 拆测理论发现、建模和证明。 |
| 计算机视觉 | 生成 | [BRAVO: Bridge Matching for Autoregressive Video Generation](cards-0002.md#paper-148431) | 从上一帧出发学习相邻帧运输。 |
| 强化学习 | 信用分配 | [Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning](cards-0002.md#paper-150356) | 按对有效解集合的边际贡献分奖励。 |
| 语音识别 | 鲁棒微调 | [Breaking Adversarial Transferability in Fine-Tuned Speech Recognition](cards-0002.md#paper-153915) | 部署前验证公开底座的风险是否残留在微调模型。 |
| 联邦学习 | 鲁棒聚合 | [Breaking BAD: Heterogeneous Byzantine-Robust Federated Learning via Gather and Scatter Scores](cards-0002.md#paper-148208) | 同时检查更新的局部聚集与整体离散。 |
| 统计学习 | 信息估计 | [Breaking Curse of Dimensionality for Mutual Information Estimation with Vine Copulas](cards-0002.md#paper-154130) | 依赖复杂时比较藤 copula 与神经互信息估计。 |
| 时序学习 | 自监督 | [Breaking feature collapse in self-supervised time series encoder](cards-0002.md#paper-155178) | 以表示空间约束补充掩码重建。 |
| 深度学习 | 稀疏微调 | [Breaking Information Islands in Sparse Tuning via Small-World Connectivity](cards-0002.md#paper-155451) | 相同参数预算下改善跨块连接。 |
| 多模态学习 | 量化 | [Breaking Modality Heterogeneity in Low-Bit Quantization for Large Vision-Language Models](cards-0002.md#paper-153382) | 将模态特有的离群通道分开校准。 |
| 科学机器学习 | 数据增强 | [Breaking Noise Shortcuts in Self-Supervised Learning via Noise-Aligned View Generation](cards-0002.md#paper-153415) | 对同图的两个自监督视图重采样独立噪声。 |
| 统计学习 | 联邦采样 | [Breaking the $\sqrt{d}$ Communication Barrier in Federated Sampling with Adaptive Hamiltonian Monte Carlo](cards-0002.md#paper-152679) | 按客户端偏移调整同步频率。 |
| 强化学习 | 梯度估计 | [Breaking the Bias Barrier in Concave Multi-Objective Reinforcement Learning](cards-0002.md#paper-154531) | 检查效用平滑性后决定是否用多层蒙特卡洛。 |
| 推理系统 | 稀疏注意力 | [Breaking the Exactness Barrier: Interleaved DeepSeek Sparse Attention for Efficient Long Context Reasoning](cards-0002.md#paper-154778) | 按设备交错切分上下文并用放宽的局部排名替代精确全局排名。 |
| 强化学习 | 动作搜索 | [Breaking the Grid: Distance-Guided Reinforcement Learning in Large Discrete Action Spaces](cards-0002.md#paper-151813) | 按动作距离抽样邻域而非遍历整个动作空间。 |
| 生成模型 | 多体生成 | [Breaking the Group Size Barrier: Parameter-Efficient Group Dance Generation with Chain-of-Dancers](cards-0002.md#paper-151566) | 冻结单体生成器，按个体顺序生成并聚合已生成同伴。 |
| 统计学习 | 隐私评测 | [Breaking the Quality–Privacy Tradeoff in Tabular Data Generation via In-Context Learning](cards-0002.md#paper-152928) | 小样本表格合成优先比较上下文适配和逐表训练。 |
| 多模态学习 | 时序信用分配 | [Breaking the Second Barrier: Sub-Second Timestamped Omni-Modal Captioning](cards-0002.md#paper-151142) | 分别给字幕结构片段分配语义与时间奖励。 |
| 生成模型 | 条件调度 | [Breaking the Static: Dynamic Text Conditioning for Diverse Image Generation](cards-0002.md#paper-152353) | 初段只保留低频语义，后段逐步恢复完整提示。 |
| 生成模型 | 专家路由 | [Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE](cards-0002.md#paper-152515) | 视频 MoE 给语义专家与通用专家分工，避免强制全局均匀路由。 |
| 训练系统 | 优化器量化 | [BReD: Block Replay Dithering for Stable Low-Bit EMA Optimizer States](cards-0002.md#paper-150618) | 为反复量化的 EMA 状态控制舍入偏差与方差。 |
| 优化 | 分布稳健训练 | [Brenier Meets Adversarial Training: Optimal Transport Geometry for Robust Learning](cards-0002.md#paper-152709) | 用运输映射的循环单调性检查分布鲁棒目标。 |
| 生成模型 | 结构化解码 | [BrickAnything: Geometry-Conditioned Buildable Brick Generation with Structure-Aware Tokenization](cards-0002.md#paper-154364) | 用局部连接树替代仅按空间坐标排列的生成序列。 |
| 计算机视觉 | 成像恢复 | [Bricker to BRACE: A Bracket Exposure RAW Dataset and Restoration Model for Flicker-Banding](cards-0002.md#paper-149112) | 用包围曝光捕获条纹随曝光变化的特征。 |
| 计算机视觉 | 约束引导 | [BrickFlow: Connectivity-Guided Brick Reconstruction](cards-0002.md#paper-151991) | 推理时加解析连接场修正生成的部件位姿。 |
| 多模态学习 | 时序对齐 | [BRIDGE: Brain-Vision Representation Integration through Depth and Granularity Encoding](cards-0002.md#paper-155233) | 让视觉教师提供跨层表示，并分阶段池化脑信号。 |
| 生成模型 | 训练前诊断 | [Bridge Graphical Models: Coupling, Projection, and Current-Preserving Dynamics for Generative Modeling](cards-0002.md#paper-148153) | 先用桥速度的条件方差筛选耦合，再投入长时间训练。 |
| 计算机视觉 | 深度融合 | [BridgeMVS: Bridging Multi-View Stereo and Monodepth via Bidirectional Dynamic Fusion](cards-0002.md#paper-151655) | 让单目先验和多视角几何双向校准并跨尺度传递。 |
| 生成模型 | 条件采样 | [BridgeTwist: Twisting Schrödinger Bridges for Training-Free Conditional Sampling](cards-0002.md#paper-151085) | 冻结桥生成器，以端点估计和退火重要性权重做条件采样。 |
| 多模态学习 | 三维建模 | [Bridging 1D, 2D, and 3D with Any-to-Any Multimodal Modeling](cards-0002.md#paper-156144) | 用离散 token 和共同掩码任务联训不同三维表示。 |
| 图学习 | 可扩展评测 | [Bridging Academia and Industry: A Comprehensive Benchmark for Attributed Graph Clustering](cards-0002.md#paper-139018) | 按规模、同配性和标签可得性验证图聚类。 |
| 多模态学习 | 测试时适配 | [Bridging CLIP with DINO: Cross-Modal Information Maximization for Online Test-Time Adaptation](cards-0002.md#paper-152887) | 将文本原型投影到冻结自监督视觉空间，并过滤不可靠样本梯度。 |
| 语言模型 | 缩放律 | [Bridging Compute- and Data-Optimal Pretraining](cards-0002.md#paper-155350) | 按新鲜数据约束分配训练预算 |
| 时间序列 | 生成架构 | [Bridging Diffusion and Autoregression for Flexible Time Series Synthesis](cards-0002.md#paper-155931) | 跨块自回归、块内联合去噪 |
| 图学习 | 距离近似 | [Bridging Graph Worlds: Neural Approximation of Gromov-Wasserstein Distances](cards-0002.md#paper-151656) | 用学习代理批量比较图结构 |
| 计算机视觉 | 交替优化 | [Bridging Image Restoration and Recognition via Causal Mediated Unrolling](cards-0002.md#paper-153651) | 把识别信号和自然图像先验分步施加 |
| 多模态 Agent | 结构化记忆 | [Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning](cards-0002.md#paper-156072) | 长视频同时索引局部证据与跨时段叙事 |
| 强化学习 | 课程采样 | [Bridging Risk Approximation Gaps in Model Predictive Task Sampling via In-Context Modeling](cards-0002.md#paper-150549) | 按下一次策略更新后的难度选任务 |
| 强化学习 | 约束学习 | [Bridging Safety and Performance in Autonomous Systems using Offline Reinforcement Learning](cards-0002.md#paper-150431) | 将安全约束写入状态可行域而非仅作软惩罚 |
| 自动驾驶 | 表征迁移 | [Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](cards-0002.md#paper-151833) | 将生成阶段学到的运动编码器与视觉编码器一同迁移 |
| 通用机器学习 | 域适配 | [Bridging Sequence and Structure with Unified Domain Adaptation for Drug-Target Interaction Prediction](cards-0002.md#paper-156127) | 推迟使用目标域伪标签，先校准预测 |
| 自动驾驶 | 域对齐 | [Bridging Simulation and Reality: Geometry and Decision Alignment for Autonomous Driving](cards-0002.md#paper-151850) | 同时检查几何对齐与策略行为对齐 |
| 多模态学习 | 可追溯监督 | [Bridging Structure and Language: Graph-Based Visual Reasoning for Autonomous Road Understanding](cards-0002.md#paper-151879) | 用可执行图查询生成有可验证落点的问答 |
| 推荐系统 | 表示对齐 | [Bridging Textual Profiles and Latent User Embeddings for Personalization](cards-0002.md#paper-152825) | 按检索效用训练可读用户画像 |
| 语言模型 | 安全对齐 | [Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment](cards-0002.md#paper-149662) | 分开测风险判断与最终拒答 |
| 语言模型 | 缓存复用 | [Bridging the Gap: Position-Independent Cache Reuse for Hybrid SSM-Attention Architectures](cards-0002.md#paper-152513) | 统一混合注意力和状态空间层的跨位置缓存粒度 |
| 医学影像 | 跨模态蒸馏 | [Bridging the Modality Bottleneck in Pathology MIL through Virtual Molecular Staining](cards-0002.md#paper-150709) | 训练时以配对观测改造投影层，部署只用图像 |
| 科学机器学习 | 分布校准 | [Bridging the Simulation-to-Experiment Gap with Adversarial Distribution Alignment](cards-0002.md#paper-151598) | 用真实部分观测校准完整仿真的生成模型 |
| 语言模型 | 稳健评测 | [Brittlebench: Quantifying LLM robustness via prompt sensitivity](cards-0002.md#paper-139284) | 以语义等价改写测试排行榜稳定性 |
| 优化 | 双层优化 | [BROS: Bias-Corrected Randomized Subspaces for Memory-Efficient Single-Loop Bilevel Optimization](cards-0002.md#paper-149705) | 用随机子空间估计 Hessian 作用节省内存 |
| 语言模型 | 安全优化 | [BSO: Safety Alignment Is Density Ratio Matching](cards-0002.md#paper-156078) | 把安全偏好优化定义成比率匹配 |
| 表格生成 | 分块扩散 | [BSTabDiff: Block-Subunit Diffusion Priors for High-Dimensional Tabular Data Generation](cards-0002.md#paper-151140) | 用块级潜变量替代高维联合密度建模。 |
| 时间序列 | 计算分配 | [BucpTSF: Breaking the Uniform Computation Paradigm in Time-Series Forecasting](cards-0002.md#paper-148238) | 按信息密度、频带和预测跨度分配计算。 |
| 联邦学习 | 隐私训练 | [Budget-Conditioned Clipping Policies for Differentially Private Federated Learning](cards-0002.md#paper-150613) | 在公开代理上学习预算与轮次到裁剪阈值的映射后冻结。 |
| 强化学习 | 离策略估计 | [Budgeted Multi-Source Counterfactual Annotation for Off-Policy Evaluation](cards-0002.md#paper-155643) | 按成本与误差分配有限的反事实标注。 |
| 决策理论 | 预算分配 | [Budgeting Discretion: Theory and Evidence on Street-Level Decision-Making](cards-0002.md#paper-153217) | 依据收益分布尾部形态决定保留多少人工覆盖额度。 |
| 计算机视觉 | 三维高斯剪枝 | [BudSplat: Feed-forward 3D Gaussian Splatting under a Rendering Budget](cards-0002.md#paper-148823) | 按细节重要性和渲染贡献共同分配高斯。 |
| 深度学习 | 训练动力学 | [Bug or Feature$^2$: Weight Drift, Activation Sparsity, and Spikes](cards-0002.md#paper-149709) | 修改激活函数时同时监控稀疏度与异常尖峰。 |
| 智能体 | 代码工件评测 | [Build-and-Find: An Effort-Aware Protocol for Evaluating Agent-Managed Codebases](cards-0002.md#paper-138900) | 只有意图可可靠找回时才比较代码库检索开销。 |
| 几何深度学习 | 流形层 | [Building Transformation Layers for Riemannian Neural Networks](cards-0002.md#paper-151412) | 在相同层构造框架下比较不同流形。 |
| 量子机器学习 | 后验生成 | [BuresTomFlow: Bures-Geometric Flow Matching for Posterior Quantum Tomography](cards-0002.md#paper-148329) | 在保真度几何中学习量子态后验而非仅估点。 |
| 图学习 | 双曲注意力 | [Busemannformer: Horospherical Self-Attention for Hyperbolic Graph Transformers](cards-0002.md#paper-151890) | 按任务对称性和标签的层级属性选几何打分。 |
| 多模态学习 | 视频取证 | [BusterX: MLLM-Powered AI-Generated Video Forgery Detection and Explanation](cards-0002.md#paper-151123) | 把检测泛化和解释质量分开评估。 |
| 图学习 | 解释评测 | [B-XAIC Dataset: Benchmarking Explainable AI for Graph Neural Networks Using Chemical Data](cards-0002.md#paper-139598) | 用已知理由验证图解释而不仅依赖数据代理分数。 |
| 可解释性 | 特征复现 | [Bypassing PC1 Makes SAEs More Reproducible](cards-0002.md#paper-156083) | 训练稀疏自编码器时旁路主成分再在推理加回。 |
| 语言模型 | 蒸馏 | [ByteDistill: Cross-Tokenizer Distillation via Chunk-wise Byte-Level Distribution Alignment](cards-0002.md#paper-149633) | 跨分词器时对齐下一个可观测字节的分布。 |
| 多模态学习 | 细粒度微调 | [C2FT: Enhancing Fine-Grained Perception in MLLMs via Confuse-then-Contrast Fine-Tuning](cards-0002.md#paper-151433) | 按目标模型的具体混淆组织多图对照监督。 |
| 强化学习 | 分层控制评测 | [C2G-BENCH: A Cyber-Physical Evaluation Benchmark for Hierarchical Reinforcement Learning in Grid-Interactive Hyperscale Data Centers](cards-0002.md#paper-139076) | 用耦合的双时间尺度测试上层计划与下层控制。 |
| 智能体 | 角色记忆 | [C3: Long-Horizon Character Consistency via Causal-Continuous State Dynamics and Memory Rewriting](cards-0002.md#paper-151786) | 用连续状态和滞回更新角色，并按当前关系重释事件。 |
| 医学影像 | 压力测试 | [C3VD-DEFCOL: A Deformable Colonoscopy Dataset with Time-Resolved 3D Ground Truth and Realistic Appearance](cards-0002.md#paper-139182) | 按已知形变强度分层评估位姿估计。 |
| 生成模型 | 数值采样 | [CAB: Accelerating Flow and Diffusion Sampling via Rectification and Corrected Adams-Bashforth](cards-0002.md#paper-150465) | 低步数采样时比较带历史速度校正的多步积分。 |
| 计算机视觉 | 奖励建模 | [CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](cards-0002.md#paper-153622) | 为视频奖励模型监督异常所在时间和空间。 |
| Agent | 缓存通信 | [CacheMAS: Cache Communication for Single-Pass, Jointly-Optimized Multi-Agent Systems](cards-0002.md#paper-154215) | 让多个角色通过预填充缓存共享状态，最终角色一次生成。 |
| 生成模型 | 推理缓存 | [Cache the Future: Training-Free Self-Revision for Diffusion Transformer Acceleration](cards-0002.md#paper-149314) | 用稀疏计算的后续状态修订此前跳过的时间步。 |
| 生成模型 | 覆盖诊断 | [CADMA: Capacity-Aware Recall Decomposition for Generative Model Assessment](cards-0002.md#paper-139801) | 用一对一局部分配评估生成分布的有效覆盖。 |
| 表格学习 | 特征构造 | [CAFE: Causally-Guided Automated Feature Engineering with Multi-Agent Reinforcement Learning](cards-0002.md#paper-151842) | 用软因果结构先验约束特征搜索，而非硬删除候选。 |
| 多模态学习 | 拓扑注意力 | [CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal Models](cards-0002.md#paper-151831) | 给多房间场景按物体和房间两层建立信息路径。 |
| 视频理解 | 比较式评估 | [CA-Judge: Teach Large Models to Judge Anomalies via Comparison for Video Anomaly Detection](cards-0002.md#paper-153516) | 用少数有信息量的参考比较代替绝对异常打分。 |
| 统计学习 | 校准评测 | [CalArena: A Large Scale Post-Hoc Calibration Benchmark](cards-0002.md#paper-139709) | 用恰当评分规则的改善度同时监测校准收益和预测质量。 |
| 统计学习 | 半监督估计 | [Calibeating Prediction-Powered Inference](cards-0002.md#paper-150100) | 先用小标注集校准预测分数，再用全量协变量估计均值。 |
| 强化学习 | 安全策略改进 | [Calibrated Safe Policy Improvement for Continuous Offline Reinforcement Learning](cards-0002.md#paper-148367) | 用校准的一步模型误差证书限制连续域搜索。 |
| 优化 | 曲率估计 | [Calibrated Target Noise Recovers Curvature from the Gradients](cards-0002.md#paper-154444) | 只有批梯度时用校准目标扰动估计曲率。 |
| 医学人工智能 | 概率校准 | [Calibrating Agentic LLMs for Clinical Prediction](cards-0002.md#paper-149149) | 临床预测 Agent 的验证同时检查风险概率校准和区分能力。 |
| 大语言模型 | 语义校准 | [Calibrating LLMs with Semantic-level Reward](cards-0002.md#paper-154784) | 通过答案语义一致性训练校准，减少置信度措辞影响。 |
| 科学机器学习 | 不确定性估计 | [Calibrating Scientific Foundation Models with Inference-Time Stochastic Attention](cards-0002.md#paper-153839) | 固定模型，通过随机注意力生成集合预测。 |
| Agent | 干预决策 | [Calibration Is Not Control: Intervention Advantage for LLM-Agent Oversight](cards-0002.md#paper-149357) | 从同一轨迹前缀比较继续和采取干预的预期效用。 |
| 统计学习 | 无标签校准 | [Calibration without Ground Truth](cards-0002.md#paper-152525) | 检查主模型和参考模型是否相互可校准，再决定是否转移校准信息。 |
| 统计学习 | 统计校准 | [Calibration without labels in multiple testing](cards-0002.md#paper-150447) | 校准局部错误率时用伪标签代替真实标签 |
| Agent | 隔离防御 | [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](cards-0002.md#paper-155134) | 将可信规划与界面感知隔离 |
| 多模态 | 记忆机制 | [CAM: Question Answering on Entity-Centric Videos with Continuous Extraction and Adaptive Querying](cards-0002.md#paper-150537) | 将实体级长期摘要和按问题回查原始视频结合 |
| 视觉 | 记忆评测 | [Can 4D Foundation Models Remember?](cards-0002.md#paper-139573) | 用全景参考评估物体离开视野后的记忆 |
| Agent | 流程评测 | [Can Agents Price a Reaction? Evaluating LLMs on Chemical Cost Reasoning](cards-0002.md#paper-139478) | 用冻结价格快照和阶段分数评估工具代理 |
| Agent | 证据评测 | [Can AI Agents Synthesize Scientific Conclusions?](cards-0002.md#paper-139077) | 科学结论评估隔离答案泄漏并测事实级覆盖 |
| 法律AI | 证据归因 | [Can an LLM Reason Like a Lawyer? Benchmarking the ability of LLMs to map the facts of a case to the elements of the applicable legal rule](cards-0002.md#paper-139058) | 对法律模型测试事实到规则要件的显式归因 |
| 隐私 | 编码 | [Can Bits Seal Language?](cards-0002.md#paper-153783) | 把输入离散编码的隐私与效用一起比较 |
| 学习理论 | 鲁棒评测 | [Can Circuit Alignment Predict OOD Generalization?](cards-0002.md#paper-155822) | 用计算路径对齐而非仅激活相似度估计跨域性能 |
| 推荐 | 图表示 | [Can Complementary Signals Bridge Similarity Islands?  Manifold-Augmented Graph Embedding for Multimodal Recommendation](cards-0002.md#paper-155124) | 显式区分互补关系与相似替代关系 |
| Agent | 约束设计 | [CANDO: Cooperative Agentic Network for Layout Design Optimization](cards-0002.md#paper-153174) | 以场地约束验证器指导布局迭代 |
| 优化 | 梯度估计 | [Can Entry-Wise Clipping Give Spectral Control of Stochastic Gradients?](cards-0002.md#paper-154679) | 梯度噪声重尾时试验逐元素平滑收缩 |
| 系统 | 并行规划 | [Can Hybrid-Parallel Planning Support Alternating Model–Strategy Design? Dependency-Keyed Per-Layer Primitives for Re-Planning](cards-0002.md#paper-149399) | 并行策略重算时仅复用依赖签名一致的层级原语 |
| 公平性 | 排序诊断 | [Can Ideologues Agree on Quality? From Non-identifiable Latent Factors to Collective Outcomes](cards-0002.md#paper-154284) | 众包评分模型中明示何谓中立评价者 |
| 强化学习 | 探索奖励 | [Can In-Context Learning Support Intrinsic Curiosity?](cards-0002.md#paper-151481) | 按任务是否有时间依赖决定用上下文预测误差近似学习进展 |
| 大语言模型 | 长上下文 | [Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale](cards-0002.md#paper-153028) | 百万 token 检索单独诊断注意力归一化稀释 |
| Agent | 风险评测 | [Can Large Language Models Develop Gambling Addiction?](cards-0002.md#paper-149163) | 分别测试下注自主权和目标自主权的风险 |
| 多模态 | 表征适配 | [Can Linguistic Reasoning Vectors Enhance Multimodal Reasoning Ability?](cards-0002.md#paper-155152) | 从基础语言模型抽取推理方向辅助视觉语言模型 |
| Agent | 工具评测 | [Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations](cards-0002.md#paper-139774) | 将地理工具代理的工具选择和参数定位分开评估 |
| 可解释性 | 行为诊断 | [Can LLMs explain themselves truthfully with code?](cards-0002.md#paper-150242) | 用留出输入上的行为一致性验证自解释。 |
| 大语言模型 | 数学评测 | [Can LLMs Reliably Grade Olympiad Proofs? A Controlled Study of Mathematical Verification with LLMs](cards-0002.md#paper-153381) | 将证明评分视为离散评分选择并报告序数一致性。 |
| 大语言模型 | 检索校准 | [Can LLMs Take Retrieved Information with a Grain of Salt?](cards-0002.md#paper-148640) | 衡量模型在来源不确定时是否调整回答置信。 |
| 统计学习 | 多源校准 | [Can Metadata Fix the Gauge? Calibration Turns Sparse Multi-Source Learning from Sparse PCA into Sparse Mean Recovery](cards-0002.md#paper-152833) | 优先采集可验证的相对坐标信息，再合并来源。 |
| 机器学习系统 | 分布式训练 | [Can Model Merging Improve Aggregation in DiLoCo?](cards-0002.md#paper-154543) | 局部训练间隔较长时对比合并式聚合和伪梯度平均。 |
| 深度学习 | 稀疏训练 | [Cannistraci-Hebb Channel-wise Dynamic Sparse Training of Convolutional Neural Networks with Contextual Modulation](cards-0002.md#paper-149797) | 按卷积通道构建拓扑并更新稀疏连接。 |
| 学习理论 | 条件预测 | [Canonical Predictive Quotients: A Theory of Prediction under Hidden Predictive State Uncertainty with ICL Implications](cards-0002.md#paper-154631) | 只恢复会改变当前最优预测的隐状态区别。 |
| 机器学习系统 | 推理调度 | [Canopy: Tree-Aware Rollout Scheduling for Agent Reinforcement Learning](cards-0002.md#paper-154204) | 把 rollout 树结构传给调度与 KV 缓存管理。 |
| 计算机视觉 | 来源验证 | [Can Pixels Alone Reveal Image Origin? Minimax Limits and Learnable Interfaces for Passive Provenance](cards-0002.md#paper-154460) | 分别验证来源统计可分性与接口暴露带来的风险。 |
| 多模态学习 | 反事实评测 | [Can the Parts Fool the Test? Counterfactual Pairing Cycles for Relational OOD](cards-0002.md#paper-149781) | 保持图和文字成分不变，仅更换配对测试关系绑定。 |
| 视频生成 | 采样调度 | [CanvasMAR: Improving Masked Autoregressive Video Prediction With Canvas](cards-0002.md#paper-148170) | 先提供全局未来帧粗预测，再逐区补细节。 |
| 计算机视觉 | 主动感知 | [CanViT: Toward Active-Vision Foundation Models](cards-0002.md#paper-151128) | 将局部感知骨干与可持续更新的场景记忆分离。 |
| 具身智能 | 安全评测 | [Can VLMs Reason When to Stop for Human Safety?](cards-0002.md#paper-139187) | 对同一任务构造应停止和可继续的配对场景。 |
| 计算机视觉 | 伪影定位 | [Can We Model the Artifacts Explicitly? Disentangle Artifacts via Pairwise Edit Relations for Image Manipulation Localization](cards-0002.md#paper-155638) | 用同源编辑之间的关系监督潜在伪影表征。 |
| 统计学习 | 评测诊断 | [Can We Trust Item Response Theory for AI Evaluation?](cards-0002.md#paper-139287) | 使用 IRT 前按模型数量和能力分布做仿真校准。 |
| 大语言模型 | 知识编辑 | [Capacity Allocation at the Source: Sparse Target Optimization for LLM Knowledge Editing](cards-0002.md#paper-148802) | 在求目标隐态时约束稀疏度，减少多次编辑干扰。 |
| 优化 | 延迟反馈 | [Capacity-Constrained Online Convex Optimization with Delayed Feedback](cards-0002.md#paper-151561) | 用随机调度和重要性权重管理有限反馈追踪预算。 |
| 自然语言处理 | 过程监督 | [CAPER: Clause-Aligned Process Supervision for Text-to-SQL](cards-0002.md#paper-149623) | 将 SQL 语义子句作为奖励和故障定位单元。 |
| Agent | 约束优化 | [CAPO: A Primal-Dual Framework for Constraint-Aware Prompt Optimization](cards-0002.md#paper-149769) | 为工具使用和输出要求设显式阈值后优化系统提示。 |
| 机器学习系统 | 隐私推理 | [Capricorn: Highly Efficient and Secure Mixture of Experts Inference Framework](cards-0002.md#paper-152572) | 分别优化安全 MoE 路由与激活的通信开销。 |
| 大语言模型 | 遗忘评测 | [CapTrack: Multifaceted Evaluation of Forgetting in LLM Post-Training](cards-0002.md#paper-138881) | 按能力拆分后训练漂移 |
| 大语言模型 | 上下文蒸馏 | [Capturing In-Context Learning Dynamics with Task Operators](cards-0002.md#paper-149094) | 用输入相关算子代替固定任务向量 |
| 大语言模型 | 能力评测 | [Capturing LLM Capabilities via Evidence-Calibrated Query Clustering](cards-0002.md#paper-148906) | 按模型表现校准语义聚类 |
| 科学机器学习 | 算子学习 | [Capturing Membrane Dynamics and Spike Timing of Human Neurons at Scale using Neural Operators](cards-0002.md#paper-149091) | 同类神经元共享条件算子 |
| 推荐系统 | 多关系损失 | [Cardinality-Decomposed Loss for Heterogeneous GNNs](cards-0002.md#paper-150315) | 按关系基数配置训练损失 |
| Agent | 强化学习 | [CARD: Internalizing Expert Critique into Reinforcement Learning for Deep Search](cards-0002.md#paper-152838) | 对被反馈真正改写的步骤提高权重 |
| 医疗多模态 | 评测诊断 | [CardioLens: Revealing the Clinical Reality Gap of MLLMs via Multi-Sequence Cardiac MRI Evaluations](cards-0002.md#paper-139679) | 按完整影像流程分层验收 |
| 大语言模型 | 过程评测 | [CAREBench: Evaluating LLMs' Emotion Understanding by Assessing Cognitive Appraisal Reasoning](cards-0002.md#paper-139329) | 把情绪推断过程与终局标签分开测 |
| 计算机视觉 | 反事实评测 | [CARVE: Counterfactual Video Editing for Auditing and Hardening Video Detectors](cards-0002.md#paper-151526) | 正交干预环境和事件来诊断检测捷径 |
| 优化 | 泛化正则 | [CASAM: Consistency-Anchored Sharpness-Aware Minimization for Improved Model Generalization](cards-0002.md#paper-152013) | 用样本与批梯度的一致性分配训练权重 |
| 多模态学习 | 解释性 | [Cascaded Sparse Autoencoders LearnMulti-Level Visual Concepts in Multimodal LLMs](cards-0002.md#paper-151133) | 用特征字典训练上层稀疏编码器 |
| 大语言模型 | 自博弈 | [CasePlay: Self-Play Reinforcement Learning from Case Reports for Medical Reasoning](cards-0002.md#paper-153097) | 用信息点覆盖和题目质量分别约束自博弈 |
| 生成模型 | 可解释性 | [CASL: Concept-Aligned Sparse Latents for Interpreting Diffusion Models](cards-0002.md#paper-149923) | 先训练稀疏字典再以少量概念标签建立映射 |
| 统计学习 | 结构化潜变量 | [CASL-VAE: Learning Structured Latent Variables from Unpaired Data for Semi-supervised Clustering and Paired Sample Generation](cards-0002.md#paper-150313) | 把共享变化和目标群体内部变化分解 |
| 神经符号学习 | 约束投影 | [Casper: A Projection-Based Neurosymbolic Layer for Scalable & Guaranteed Constraint Satisfaction](cards-0002.md#paper-149782) | 把可行性作为可微输出层 |
| Agent | 防御监测 | [CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring](cards-0002.md#paper-150932) | 合并多渠道信号识别异常传播 |
| 推荐系统 | 离散表征 | [CASQRec: Collaborative-Adaptive Semantic Quantization for Multimodal Recommendation](cards-0002.md#paper-155565) | 让协同行为监督语义码分配 |
| 时间序列 | 分布预测 | [CAST: Causal Anchored Simplex Transport for Distribution-Valued Time Series](cards-0002.md#paper-155150) | 用上下文区分同状态下的不同转移规律 |
| 强化学习 | 稳健迁移 | [CAST: Certifiable Aggregation of Smoothed Teachers for Robust Policy Adaptation](cards-0002.md#paper-151249) | 聚合带证书的源策略并复查目标侧保证 |
| 多模态学习 | 能力诊断 | [Castle-in-the-Air: Probing the Foundational Visual Deficits of MLLMs via Bottom-Up Cognitive Factors](cards-0002.md#paper-139489) | 在高层问答之外测可控难度的基础视觉 |
| 按授权模型评估数据重编码 | 数据授权 | [Catch-Only-One: Non-Transferable Examples for Model-Specific Authorization](cards-0002.md#paper-151014) | 检验授权与未知模型的效用差距 |
| 语言模型 | 自适应计算 | [Catch Your Breath: Adaptive Computation for Self-Paced Sequence Production](cards-0002.md#paper-152630) | 让模型学习何时暂停和继续 |
| 语言模型安全 | 偏好优化 | [Cat-DPO: Category-Adaptive Safety Alignment](cards-0002.md#paper-151048) | 按风险类别分别调节训练边际 |
| 认知建模 | 状态估计 | [Categorical Bayes filtering for computational phenotyping in adaptive learning](cards-0002.md#paper-153212) | 用可微分网格替代随机外层粒子 |
| 图学习 | 归纳偏置 | [Caterpillar GNN: Replacing Message Passing with Graph-Level Aggregation](cards-0002.md#paper-148837) | 按任务需求限制图网络表达力 |
| 多模态学习 | 推理加速 | [CATS: Acceptance-Oriented Critical Token Adaptive Selection for Multimodal Speculative Decoding](cards-0002.md#paper-154883) | 优先对齐视觉依赖或高拒绝率 token |
| 科学机器学习 | 消融设计 | [Cauchy Scientific Networks: Loss–Architecture Alignment and Its Limit](cards-0002.md#paper-148993) | 交叉消融损失与激活函数 |
| 因果学习 | 理论 | [Causal Abstractions, Categorically Unified](cards-0002.md#paper-153629) | 分开验证图兼容与变量聚合 |
| 计算机视觉 | 结构监督 | [CausalAffect: Causally Guided Learning of Psychology-Aligned Facial Affect Relations](cards-0002.md#paper-148159) | 将全局关系与样本关系分开拟合 |
| 计算机视觉 | 可解释性 | [Causal Attribution via Activation Patching](cards-0002.md#paper-155095) | 在中间层直接检验图块表征贡献 |
| 公平性 | 因果分解 | [Causal Bias Detection in Generative Artifical Intelligence](cards-0002.md#paper-149915) | 审计生成模型时区分路径效应和机制替换效应 |
| 计算机视觉 | 记忆路由 | [CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives](cards-0002.md#paper-154338) | 跨镜头视频按内容相关性选缓存 |
| 因果学习 | 鲁棒评测 | [CausalCompass: Evaluating the Robustness of  Time-Series Causal Discovery in Misspecified Scenarios](cards-0002.md#paper-139526) | 把标准化与假设违背分别做对照 |
| 可解释性 | 概念监督 | [Causal Concept Explanations for Deep Neural Models](cards-0003.md#paper-149967) | 用必要性、充分性和独立性约束概念嵌入 |
| 多模态学习 | 诊断基准 | [CausalConflictBench: Can Multimodal Models Follow Local Mechanisms That Conflict with Commonsense?](cards-0003.md#paper-139553) | 用违背常识的局部规则测试规则遵循 |
| 因果学习 | 图发现 | [Causal Discovery from Unseen Environments](cards-0003.md#paper-151347) | 无环境标签时先以合并数据测试 ICA-LiNGAM |
| 因果学习 | 图发现 | [Causal Discovery over Clusters of Variables in Non-Markovian Systems](cards-0003.md#paper-152473) | 聚簇变量存在潜混杂时采用容纳隐变量的等价类 |
| 因果学习 | 截断分布 | [Causal Discovery Under Hard Selection Bias: A New Robust Score-Matching Approach](cards-0003.md#paper-153240) | 用分数及其雅可比恢复硬筛选数据中的因果结构 |
| 因果学习 | 时间序列 | [Causal Discovery under Time-Varying Delays](cards-0003.md#paper-152445) | 显式允许因果时延随时间改变 |
| 因果学习 | 方向辨识 | [Causal Discovery via Transformed Low-Rank Quantile Surfaces](cards-0003.md#paper-149402) | 用变换后条件分位曲面的秩比较双变量因果方向 |
| 因果学习 | 错误发现控制 | [Causal Discovery with False Positive Error Control](cards-0003.md#paper-151569) | 保留方向不确定标记并同时约束假边与错方向 |
| 具身智能 | 反事实评测 | [CausalDriveBench: Evaluating Causal Reasoning in Vision-Language-Action Models for Autonomous Driving](cards-0003.md#paper-139161) | 分开评估因果解释与动作轨迹是否响应同一反事实 |
| 大语言模型 | 编辑表示 | [Causal Edit Serialization](cards-0003.md#paper-153668) | 区分生成位置与源内容地址来学习显式编辑 |
| 因果学习 | 潜在混杂 | [Causal Effect Identification with a Single Agnostic Proxy](cards-0003.md#paper-149771) | 以候选集加独立性检验替代单代理闭式估计 |
| 因果学习 / Agent | 网络干预 | [Causal Effects with Unobserved Unit Types in Interacting Human–AI Systems](cards-0003.md#paper-149288) | 以预期人类占比和干预暴露差异恢复人群平均效应 |
| 隐私与可靠性 | 防御评测 | [Causal Evaluation of Membership Inference Attacks](cards-0003.md#paper-154373) | 把训练数据隐私审计中的训练干扰和评测分布差异分开记录 |
| 具身智能 / Agent | 几何规划 | [Causal-Geo: Neuro-Symbolic Spatial Grounding for Situated Agent Planning](cards-0003.md#paper-155379) | 让语义偏好调整路径代价，几何层单独约束可行性 |
| 计算机视觉 | 捷径抑制 | [Causal Gradient Steering: Exposing Shortcut Gradients by Destroying Causal Signal](cards-0003.md#paper-148981) | 用移除语义证据后的配对样本估计捷径梯度 |
| 因果学习 | 缺失时间序列 | [Causal heteroscedastic structure learning from incomplete temporal data](cards-0003.md#paper-151770) | 联合校正插补和估计因果图 |
| 因果学习 | 面板干预 | [Causal Inference for Sequential Settings under Interference and Latent Confounding](cards-0003.md#paper-149757) | 在序列干预估计中同时建模邻接依赖和低秩隐混杂 |
| 因果学习 | 环境不变性 | [Causal learning with the invariance principle](cards-0003.md#paper-148923) | 依据多个环境中保持不变的因果机制识别图 |
| 大语言模型 | 训练数据配比 | [CausalMix: Data Mixture as Causal Inference for Language Model Training](cards-0003.md#paper-154762) | 让配比随数据池状态变化，用小模型试验估计条件收益 |
| 因果学习 | 迁移设计 | [Causal Multi-Task Demand Learning](cards-0003.md#paper-153237) | 用价格序列处理跨任务混杂，同时保留局部外生监督 |
| 神经网络理论 | 训练诊断 | [Causal pieces: analysing and improving spiking neural networks piece by piece](cards-0003.md#paper-148689) | 用单脉冲网络激活子网的分区数诊断初始化 |
| 推荐系统 | 分布偏移 | [Causal Representation Learning for Generalisable Recommendation](cards-0003.md#paper-148867) | 用因果解耦训练项提升从旧日志向上线候选分布迁移 |
| 多模态学习 | 反事实评测 | [CausalSpatial: A Benchmark for Object-Centric Causal Spatial Reasoning](cards-0003.md#paper-138913) | 用显式模拟画面辅助反事实空间判断 |
| 因果推断 | 代理调整 | [Causal Survival Forests with Negative Controls](cards-0003.md#paper-153856) | 在生存森林中引入负对照和正交损失 |
| 因果推断 | 合成预训练 | [CausalTab: Pretraining Across Causal Environments for Tabular Causal Discovery](cards-0003.md#paper-150884) | 把图结构、机制和干预制度作为独立采样因素 |
| 计算机视觉 | 视频理解 | [Causal-VLM: Dense Causal Captioning in Videos](cards-0003.md#paper-139209) | 联合训练时间定位、事件描述和因果边预测 |
| 多模态学习 | 过程奖励 | [CAVE: A Structured Credit Assignment Approach for Fragmented Visual Evidence Reasoning](cards-0003.md#paper-153157) | 分别给有效找证据、更新判断和调整焦点赋予奖励 |
| 计算机视觉 | 数据审计 | [CCDiff: Inverse Canonical Correlation Analysis for Discovering Visual Differences in Natural Language](cards-0003.md#paper-148652) | 用统计关联分析发现图像集合的语义差异 |
| 计算机视觉 | 低显存训练 | [CC-GS: Low-Memory 3D Gaussian Splatting Training via CPU-GPU Block-Wise Context Compositing](cards-0003.md#paper-154162) | 按块优化并缓存其余块的像素合成上下文 |
| 统计学习 | 生存建模 | [CCTimeBoost: Learning Time-Varying Relative Risk with Case-Control Boosted Trees](cards-0003.md#paper-148611) | 用含时间特征的分组 softmax 训练提升树 |
| 医学影像 | 连续视图生成 | [CD-RCM: Generalizable Continuous-Depth Novel View Synthesis for Reflectance Confocal Microscopy](cards-0003.md#paper-156085) | 在轴向插值中显式建模浅层遮挡 |
| 大语言模型 | 端侧推理 | [CECAR: Cache & Expert Co-Aware Routing Accelerates On-Device Inference of MoE LLMs](cards-0003.md#paper-152287) | 让专家路由使用预计复用距离 |
| 统计学习 | 序贯评测 | [CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes](cards-0003.md#paper-148283) | 用任意时点有效的区间决定何时停止评测 |
| 科学机器学习 | 上下文表示 | [CellMSA: Context Modeling for Single-Cell Representation Learning](cards-0003.md#paper-151414) | 将不同批次的相似观测用于上下文表示学习 |
| 可靠性 | 证据评测 | [CellularS2-Bench: A Staged, Evidence-Grounded Benchmark for Cellular Network Security Reasoning](cards-0003.md#paper-138931) | 分阶段验证模型能否引用和串联规范证据 |
| 可解释性 | 时频归因 | [CENDRe: Concept Extraction with Natural Domain Representations](cards-0003.md#paper-150459) | 在时间和频率域定位同一概念 |
| Agent | 长程评测 | [CEO-Bench: Can Agents Play the Long Game?](cards-0003.md#paper-139585) | 单独记录长程经营的累计结果与适应表现 |
| 科学机器学习 | 样本效率 | [Cephalonauts One: A deep fMRI dataset for decoding naturalistic speech in the human brain](cards-0003.md#paper-139123) | 按同一参与者数据量绘制神经解码学习曲线 |
| 优化 | 几何估计 | [Certifiably Optimal Robust Angular Synchronization](cards-0003.md#paper-153331) | 用节点约束界收紧鲁棒旋转同步搜索 |
| 学习理论 | 形式化验证 | [Certification-Enhanced Generalization Bounds](cards-0003.md#paper-150658) | 用样本级稳定性验证辅助分布泛化界 |
| 学习理论 | 认证下界 | [Certification from Examples is Hard for Circuits and Transformers under Minimal Overparametrization](cards-0003.md#paper-150529) | 评估算法任务时区分平均准确率与精确一致性认证 |
| 模型验证 | 隐私证明 | [Certified but Private: Scalable Zero-Knowledge Proofs for the Formal Verification of Neural Networks](cards-0003.md#paper-151824) | 用零知识证明交付局部鲁棒证书而保留权重私密 |
| 强化学习 | 因果决策 | [Certified Policy Optimisation for Nested Causal Bandits via PAC-Bayes Risk](cards-0003.md#paper-148390) | 对跨层策略按机制建模并独立认证。 |
| 可解释性 | 稳健认证 | [Certified Robust Interpretability via Concept-Space Stability under Interventional Proxies](cards-0003.md#paper-148991) | 同时认证标签稳定和概念稳定。 |
| 优化 | 稳健认证 | [Certified Single-Level Reformulation for Tri-Level Cyber-Physical Grid Security](cards-0003.md#paper-152235) | 以保守上界验证既定防御资源分配。 |
| 科学机器学习 | 部署评测 | [CFC26: Building Evaluations for Deployment in Sonar-Based Fish Counting](cards-0003.md#paper-139843) | 用跨地点切分及累计计数误差验证生态监测模型。 |
| 大语言模型 | 预算校准 | [C-GRPO: Conformal Group Relative Policy Optimization](cards-0003.md#paper-152332) | 用共形停止阈值自适应分配 rollout。 |
| 大语言模型 | 不确定性估计 | [CHAIN: Complementary Signed Graph Propagation for Uncertainty Quantification in Large Language Models](cards-0003.md#paper-154069) | 用回应间支持与矛盾结构估计置信度。 |
| 多智能体学习 | 持续学习 | [CHAIN: Continual Heterogeneous Cooperation with Information Bottleneck for Multi-Agent Reinforcement Learning](cards-0003.md#paper-155574) | 对共享状态表征压缩并鼓励各智能体形成不同专长。 |
| 计算机视觉 | 轨迹生成 | [ChainFlow-VLA: Causal Flow Planning with Vision-Language Models](cards-0003.md#paper-149929) | 先生成因果轨迹模式，再生成模式内残差。 |
| 图学习 | 组合优化 | [Chaining 2-FWL GNNs for Combinatorial Graph Alignment](cards-0003.md#paper-151502) | 将离散匹配反馈接回下一阶段图网络。 |
| 具身智能 | 策略纠错 | [Chain-of-Correction: Progress-Aware Policy Steering via Anchor-Grounded Predictive Reasoning](cards-0003.md#paper-154354) | 借助三维关系同时复查过去和预测整体任务进度。 |
| 学习理论 | 注意力结构 | [Chain of Dual Structures in Transformer Attention](cards-0003.md#paper-149520) | 用凸势统一选择注意力的打分与聚合。 |
| 大语言模型 | 模型路由 | [Chain-of-Route: State-Aware LLM Routing for Multi-Turn Conversations](cards-0003.md#paper-154597) | 多轮路由同时追踪上下文质量与缓存成本。 |
| 大语言模型 | 可解释性评测 | [Chain-of-Thought Oversight Should Not Treat Faithfulness as Monitorability](cards-0003.md#paper-140099) | 分别验收推理可见性、忠实性、可监测性和可定位性。 |
| 多模态学习 | 空间推理评测 | [ChainSpace: A Chained-Reasoning Paradigm for Spatial Intelligence](cards-0003.md#paper-150110) | 用跨轮约束链检验是否维持空间状态。 |
| 生成模型 | 约束采样 | [Chance-constrained Flow Matching for High-Fidelity Constraint-aware Generation](cards-0003.md#paper-150205) | 在通用物理生成中用概率约束避免直接投影带噪状态。 |
| 具身智能 | 长期定位 | [Change-Robust Online Topological Memory for Long-Term Relocalization and Semantic Navigation](cards-0003.md#paper-149306) | 持续验证多个连续位姿假设后再提交闭环。 |
| 计算机视觉 | 多通道表示 | [Channel Mixer: A Pretrainable Tokenizer for Scalable Multi-Channel Vision Transformers](cards-0003.md#paper-151923) | 在空间图块内先融合通道，让注意力长度与通道数解耦。 |
| 视觉 | 量化 | [Channel-wise Vector Quantization](cards-0003.md#paper-152137) | 把图像 token 粒度改成通道 |
| 视觉 | 通道表示 | [ChanSFormer: A Channel Agnostic Vision Transformer for Multi-Channel Cell Painting Images](cards-0003.md#paper-149597) | 用通道 CLS 保留身份并交换信息 |
| 学习理论 | 训练诊断 | [Characterizing Learning in Deep Neural Networks using a Tractable Algorithmic Complexity Estimator](cards-0003.md#paper-148219) | 跟踪多值权重块复杂度辅助压缩 |
| 大语言模型 | 隐私评测 | [Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects](cards-0003.md#paper-154072) | 扩散生成也需独立做隐私验收 |
| 视觉 | 可解释评估 | [Characterizing the Aesthetic Defaults of Generative Image Models](cards-0003.md#paper-139666) | 控制内容后比较生成器的默认风格 |
| 优化 | 训练稳定性 | [Characterizing the Edge of Stability in Variational Training Without Priors](cards-0003.md#paper-153245) | 联合选择学习率和蒙特卡罗样本数 |
| 学习理论 | 增强分析 | [Characterizing the Generalization Error of Random Feature Regression with Arbitrary Data-Augmentation](cards-0003.md#paper-153550) | 按增强后的前两阶统计量预测测试误差 |
| 量子机器学习 | 核设计 | [Characterizing Trainability of Instantaneous Quantum Polynomial Circuit Born Machine](cards-0003.md#paper-154648) | 按线路生成元和核谱选择可训练设定 |
| 因果推断 | 外推诊断 | [Characterizing Underrepresentation in Generalizing Causal Survival Estimates](cards-0003.md#paper-153000) | 把基线覆盖不足与随访删失分别诊断 |
| 视觉 | 表示诊断 | [Characterizing Universal Object Representations Across Vision Models](cards-0003.md#paper-156019) | 以维度的跨模型复现率度量通用性 |
| 视觉 | 组合泛化 | [Character Mixing for Video Generation](cards-0003.md#paper-148244) | 测试角色和伙伴、场景的交叉留出 |
| 系统 | 分布式推理训练 | [CHARM+: Cross-Hardware Attention with Re-Merge Multistream Mechanism](cards-0003.md#paper-154071) | 异构链路的通信分别调度 |
| 多模态 | 评测 | [ChartArena: A Unified Benchmark with Atomic-Primitive Reasoning for Chart Parsing](cards-0003.md#paper-148773) | 用统一语义表示比较不同图表输出格式 |
| 图学习 | 动态图 | [Chasing Label Shifters: A Change-Aware Framework for Dynamic Graph Node Classification](cards-0003.md#paper-150479) | 单独报告发生标签转移节点的错误 |
| 视觉 | 谱混合 | [CHASM: Cross-frequency Harmonized Axis-Separable Mixing for Spectral Token Operators](cards-0003.md#paper-148306) | 跨频共享通道基底，频率增益分开学习 |
| 统计学习 | 回归诊断 | [Cheap Per-Component Testing for PLS, Stable Under Rotation](cards-0003.md#paper-148469) | 对留出数据重新拟合监督子空间 |
| Agent | 行为评测 | [Cheap Talk, Real Stakes: Commitment and Exploitation in Human-LLM Strategic Interaction](cards-0003.md#paper-148921) | 把行动前沟通和最终执行联合审计 |
| 视觉 | 形状建模 | [Chebyshev Differential Flows for Shape Matching and Interpolation with Endpoint Guidance](cards-0003.md#paper-150678) | 用连续雅可比轨迹建模非刚性变形 |
| 世界模型 | 状态追踪评测 | [Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences](cards-0003.md#paper-139263) | 用均匀合法轨迹检验模型是否学到转移规则。 |
| 计算机视觉 | 时序姿态估计 | [ChildPose: Foundation for Children Pose Modeling](cards-0003.md#paper-150424) | 用邻帧记忆与发育属性监督适配儿童姿态。 |
| 机器学习系统 | 空间序列建模 | [ChiP-STAR: Spatial-Topological Attention for Pre-trained Generative Chip Routing](cards-0003.md#paper-150942) | 序列化几何树时同时编码遍历顺序与物理位置。 |
| Agent | 工具决策 | [Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](cards-0003.md#paper-152373) | 在执行之前对同一上下文中的备选调用估计长程价值。 |
| 机器学习系统 | 推理调度 | [CHoRD: Coordinating Scheduling and Data Placement for Efficient Deep Neural Network Inference on Chiplet-Based GPUs](cards-0003.md#paper-153059) | 跨芯粒联合决定核函数调度与权重和激活驻留。 |
| 大语言模型 | 跨模型检测 | [CHORD: Cross-Model Hallucination Detection via Relational Graph Discrimination](cards-0003.md#paper-153626) | 幻觉检测在未见模型上比较关系特征与原始隐状态。 |
| 科学机器学习 | 传感器布设 | [Christoffel-DPS: Optimal sensor placement in diffusion posterior sampling for arbitrary distributions](cards-0003.md#paper-148240) | 低预算非高斯恢复时按信号分布选择传感位置。 |
| 大语言模型 | 时间评测 | [ChronosAlign: A Large-Scale, Updatable Benchmark for Decomposing Temporal Alignment in LLMs](cards-0003.md#paper-139317) | 同一事实用显式年份、当前时间和无时间对照提问。 |
| 大语言模型 | 显存优化 | [ChunkFT: Byte-Streamed Optimization for Memory-Efficient Full Fine-Tuning](cards-0003.md#paper-155153) | 以动态子张量工作集更新全模型，避免同时持有密集梯度。 |
| Agent | 工具接口 | [CI4A: Semantic Component Interfaces for Agents Empowering Web Automation](cards-0003.md#paper-155855) | 用页面语义组件提供受控工具，而非只暴露低层点击。 |
| 强化学习 | 探索奖励 | [CIG: Exploration via Conditional Information Gain](cards-0003.md#paper-149190) | 按回放历史和本回合前缀共同计算探索奖励。 |
| 多模态学习 | 视频评测 | [CineMME: Benchmarking Fine-Grained Perception and Plot Reasoning in Multimodal Large Language Models](cards-0003.md#paper-139332) | 同时检查对白时间、内容、说话人及剧情答案。 |
| 计算机视觉 | 视频生成 | [CineOrchestra: Unified Entity-Centric Conditioning for Cinematic Video Generation](cards-0003.md#paper-149533) | 把人物、动作、相机和剪辑统一成实体与时间区间。 |
| 安全机器学习 | 隐私推理编译 | [CipherFlow: Hardware-Aware Compiler Framework for Low-Latency Hybrid Secure Inference](cards-0003.md#paper-155825) | 按目标设备及网络条件联合选安全算子与转换。 |
| 多模态学习 | 组合推理评测 | [CIPHERGRID Benchmark: From Multimodal Rule Inference to Sequential Action](cards-0003.md#paper-139313) | 分开验证符号解码、规则推断和路径规划，再考查组合。 |
| 大语言模型 | 蒸馏 | [Circuit-Level Knowledge Distillation for Large Language Models](cards-0003.md#paper-153589) | 蒸馏时对齐计算路径，并与只匹配输出比较。 |
| 大语言模型 | 训练数据选择 | [CircuitSeer: Mining High-Quality Data by Probing Mathematical Reasoning Circuits in LLMs](cards-0003.md#paper-152316) | 以推理回路响应作为数学数据筛选信号。 |
| 统计学习 | 推理预算 | [CITE: Anytime Valid Statistical Inference in LLM Self-Consistency](cards-0003.md#paper-150250) | 自适应停止采样时用可随时有效的众数认证。 |
| 大语言模型 | 证据检索 | [Cite What You Explore: Budget-Aware LLM Reasoning over Medical KGs with Verifiable Evidence](cards-0003.md#paper-153952) | 在固定图检索预算下区分证据支持度和引用正确性。 |
| 计算机视觉 | 空间条件生成 | [City-RAG: Stepping Into a City via Spatially-Grounded Video Generation](cards-0003.md#paper-154638) | 用地理配准资料约束生成场景的静态结构。 |
| 三维视觉 | 结构推理 | [CitySTAR: Agent-Driven Structured and Topology-Aware Reasoning for Open-Vocabulary Urban 3D Grounding](cards-0003.md#paper-151477) | 使用拓扑约束验证城市三维定位候选。 |
| Agent | 流程评测 | [CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in Civilization VI](cards-0003.md#paper-139660) | 分别测主动检查和承诺落实。 |
| 三维视觉 | 约束建模 | [CLAMP: A Sim-to-Real Benchmark for Closed-Loop Kinematic Pose Estimation and Assembly Reasoning](cards-0003.md#paper-139311) | 混合完好与缺件条件检验机构位姿估计。 |
| 分布式训练 | 通信压缩 | [Clapping: Removing Per-sample Storage for Pipeline Parallel Learning with Communication Compression](cards-0003.md#paper-148239) | 以懒惰采样降低流水线压缩的逐样本状态开销。 |
| 多模态 | 交互监督 | [Clarification as Supervision: Reinforcement Learning for Vision-Language Interfaces](cards-0003.md#paper-152087) | 把澄清请求转为首轮视觉描述的训练信号。 |
| 统计学习 | 共形预测 | [Class Adaptive Conformal Training](cards-0003.md#paper-152303) | 按类别调节预测集，同时守住全局覆盖。 |
| 计算机视觉 | 域泛化 | [Class–Domain Discriminability Guided Representation Enhancement for Domain Generalization](cards-0003.md#paper-152601) | 按通道的类别与域敏感性分别施加约束。 |
| 持续学习 | 原型维护 | [Class-Domain Incremental Learning with Extensible Multi-Center Modeling](cards-0003.md#paper-153465) | 类别和领域同步扩展时维护可增长的多中心树。 |
| 优化理论 | 训练动力学 | [Classification at the Edge of Stability: Unifying Self-Stabilization and Convergence Rates](cards-0003.md#paper-152056) | 大步长分类时同时跟踪尖锐度与方向残差。 |
| 表示学习 | 层次聚类 | [Classification Fields: Arbitrarily Fine Recursive Hierarchical Clustering From Few Examples](cards-0003.md#paper-151054) | 用共享局部细分规则外推超出已观察层级的结构。 |
| 统计学习 | 高维判别 | [Classification of high-dimensional data with spiked covariance matrix structure](cards-0003.md#paper-156776) | 在白化空间筛选均值差最大的坐标。 |
| 持续学习 | 参数高效适配 | [Class-Incremental Learning via LoRA-based Elastic Ensemble of Experts](cards-0003.md#paper-155401) | 据表示饱和度决定扩充 LoRA 专家。 |
| 持续学习 | 反捷径增强 | [Class-Mixed Diffusion Augmentation for Shortcut-Breaking in Continual Learning](cards-0003.md#paper-154098) | 生成能打断任务识别捷径的辅助类别。 |
| Agent | 可靠性评测 | [ClawBenchPro: Benchmarking How Well Agent Harnesses Work](cards-0003.md#paper-139365) | 用零缺陷执行率与成本共同选运行框架。 |
| 生成模型 | 水印 | [CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation](cards-0003.md#paper-149791) | 在后段去噪注入水印并按解码置信度调强度。 |
| Agent | 轨迹评测 | [Claw-Eval: Towards Trustworthy Evaluation of Autonomous Agents](cards-0003.md#paper-139588) | 用执行轨迹、审计日志与环境快照共同评分。 |
| 计算机视觉 | 风格迁移 | [CLeaR: A Unified Framework for Resolving the Leakage–Degradation Dilemma in Style Transfer](cards-0003.md#paper-151839) | 以多编码器共享像素锚点约束风格 |
| 图学习 | 伪标签校准 | [CLEAR: Complementary Tripartite Play with Bayesian Calibration for Semi-Supervised Edge Classification](cards-0003.md#paper-153511) | 用互补图视角筛选伪标签，再用邻域先验校准 |
| 多模态学习 | 偏好对齐 | [Clearer Sight, Fewer Lies: Oriented Pickup Preference Optimization for Multimodal Hallucination Mitigation](cards-0003.md#paper-155535) | 固定正确回答，按视觉证据强弱构造排序监督 |
| 临床机器学习 | 跨模态预训练 | [CLEF: EEG Foundation Models for Learning Clinical Semantics](cards-0003.md#paper-148625) | 先保留整段 EEG，再以报告及结构化病历对齐表示 |
| 计算机视觉 | 交互重建 | [Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks](cards-0003.md#paper-148962) | 让前馈重建接收稀疏跨图对应以纠错 |
| Agent | 轨迹验证 | [CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling](cards-0003.md#paper-150357) | 把训练期校准的验证问题复用于测试时重试筛选 |
| 临床机器学习 | 交互评测 | [ClinMAS: A Knowledge-Grounded Multi-Agent Simulation Framework for Evaluating Clinical Reasoning in LLMs](cards-0003.md#paper-139102) | 将诊断准确率和多轮信息收集质量分开测量 |
| 科学机器学习 | 时序稳健性 | [ClinStab: Stability-Oriented Learning for Medical Time Series via Dual-Stream Alignment](cards-0003.md#paper-149545) | 按通道能量分流并保留低能量残差信息 |
| 计算机视觉 | 持续适配 | [C-LoRA: Continual Low-Rank Adaptation for Pre-trained Visual Models](cards-0003.md#paper-149746) | 用共享低秩子空间的路由控制遗忘和新任务更新 |
| 科学机器学习 | 隐式表征 | [Closed-Form Implicit Neural Representations](cards-0003.md#paper-148458) | 按局部频谱复杂度分配闭式拟合容量 |
| 优化 | 闭式求解 | [Closed-Form Last Layer Optimization](cards-0003.md#paper-155421) | 平方损失下交替更新骨干和闭式线性头 |
| 计算机视觉 | 数据蒸馏 | [Closed-Form Linear-Probe Dataset Distillation for Pre-trained Vision Models](cards-0003.md#paper-153458) | 闭式内层配判别式外层目标压缩线性探针数据 |
| 大语言模型 | 闭环对齐 | [Closed-Loop Alignment: Socially Coupled In-Context Learning and Relational Posterior Collapse](cards-0003.md#paper-154248) | 用闭环增益诊断多轮互动中的反馈放大 |
| 自动驾驶 | 数据混合 | [Closed Loop Dynamic Driving Data Mixture for Real-Synthetic Co-Training](cards-0003.md#paper-149779) | 按闭环表现更新合成驾驶场景的采样配比 |
| 计算机视觉 | 流式建图 | [CLoSeR: Closing the Loop for Long-Context Streaming Reconstruction](cards-0003.md#paper-148375) | 先验证尺度一致性，再选择较简单的刚体位姿图 |
| 科学机器学习 | 随机动力学 | [Closing the Approximation Gap in Simulation-free Latent SDEs](cards-0003.md#paper-150349) | 在给定边缘分布下优化路径律，减少免模拟推断偏差 |
| 强化学习 | 纯探索理论 | [Closing the Gap on the Sample Complexity of 1-Identification](cards-0003.md#paper-148361) | 以实例级样本复杂度比较阈值臂搜索算法 |
| 多模态学习 | 生成式检索 | [Closing the Indexing-Decoding Gap in Multimodal Generative Retrieval via Prefix Retention Optimization](cards-0003.md#paper-150601) | 直接优化目标标识符前缀的束搜索存活率 |
| 时间序列 | 生成训练 | [Closing the Loop: Co-Evolving EM for Irregular Time Series Generation in Lifted Representations](cards-0003.md#paper-155475) | 用当前生成器反复补全缺失值 |
| 深度学习 | 注意力架构 | [Closing the Loop with Fixed-Point Self-Attention](cards-0003.md#paper-153850) | 只循环注意力直到表示稳定 |
| Agent | 奖励设计 | [Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL](cards-0003.md#paper-149208) | 用真实执行结果校准反思奖励 |
| 科学机器学习 | 物理模拟 | [ClothTransformer: Unified Latent-Space Transformers for Scalable Cloth Simulation](cards-0003.md#paper-151474) | 把不同分辨率的布料网格压到同样大小的潜状态 |
| 科学机器学习 | 评测 | [CLR-voyance : Reinforcing Open-Ended Reasoning for Inpatient Clinical Decision Support with Outcome-Aware Rubrics](cards-0003.md#paper-150688) | 把决策时可见上下文与评分用的未来证据隔离 |
| 大语言模型 | 持续训练 | [CLUE: Closing the Loop on Conflict and Collapse in LLM Unlearning](cards-0003.md#paper-152428) | 根据遗忘与保留梯度冲突决定何时切换或停止 |
| 统计学习 | 不确定性估计 | [CLUE: Correlated Latent Uncertainty for Single-Pass Deep Uncertainty Estimation](cards-0003.md#paper-151334) | 用相关潜变量支持单次推理时的不确定性收缩 |
| 大语言模型 | 量化 | [ClusQuant: Mitigating Outliers with Clustering-Based Representations for Low-Precision LRMs](cards-0003.md#paper-150265) | 以思考早期解码样本校准量化并按层分配码本 |
| 统计学习 | 稳健预测 | [Clustered Randomized Smoothing for Stochastic Prediction Functions](cards-0003.md#paper-153010) | 对多峰预测逐簇平滑后保留混合分布 |
| 语音处理 | 防御检测 | [Clustering-Free End-to-End Spoof Diarization with Encoder-Decoder Attractors](cards-0003.md#paper-150333) | 通过可变基数集合预测联合定位伪造片段与来源类别 |
| 学习理论 | 聚类 | [Clustering with Weak Distance Oracles](cards-0003.md#paper-155449) | 当成对距离多数可信时选弱预言机算法 |
| 计算机视觉 | 三维定位 | [ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting](cards-0003.md#paper-152567) | 先形成场景自适应候选簇，再按语言排序 |
| 信息检索 | 向量索引 | [Cluster with Auctions for Vector Search](cards-0003.md#paper-153334) | 查询和库分布不同时分开学习分桶与探测 |
| Agent | 强化学习 | [CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use](cards-0003.md#paper-152001) | 把开放式工具行为拆成有证据的二元奖励准则 |
| 科学机器学习 | 工具评测 | [CME–SpectrumBench: Can LLMs Analyze Condensed Matter Spectral Data?](cards-0003.md#paper-139485) | 将科学数组理解分成直接读数、程序计算与人工程序三档 |
| 计算机视觉 | 数据策略 | [CM-EVS: Sparse Panoramic RGB-D-Pose Data for Complete Scene Coverage](cards-0003.md#paper-139081) | 按增量覆盖和深度冲突选择稀疏全景视点 |
| 多模态学习 | 特征对齐 | [CMI-Trans: Cross Modal Inconsistency-aware Transport for HSI-LiDAR Classification](cards-0003.md#paper-155422) | 用局部模态可靠性决定融合对齐权重 |
| 大语言模型 | 量化 | [CMPQ: Compensatory Quantization via Input-Aware Hessian Damping](cards-0003.md#paper-153383) | 避开已被上游量化噪声污染的输入方向 |
| 计算机视觉 | 视频表征 | [CoANeRV: Coordinate-Aware Token-Space Neural Video Representation](cards-0003.md#paper-152151) | 共享坐标解码器，把实例差异留给视频 token |
| 因果学习 | 因果抽象 | [Coarsening Linear Non-Gaussian Causal Models with Cycles](cards-0003.md#paper-152930) | 聚合线性非高斯系统时允许底层存在反馈环 |
| 科学机器学习 | 神经算子 | [Coarse-to-Fine 3D MRI Reconstruction via Resolution-Agnostic Neural Operators](cards-0003.md#paper-151950) | 低分辨率训练后直接迁移到更细体素网格 |
| 生成模型 | 推理采样 | [Coarse-to-Fine Compositional Diffusion for Long-Horizon Planning](cards-0003.md#paper-148485) | 先生成全局骨架，再用原局部模型补细节 |
| 计算机视觉 | 视频生成 | [Coarse-to-Real: Generative Rendering for Populated Dynamic Scenes](cards-0003.md#paper-150766) | 先学真实视频外观，再用少量合成配对数据引入控制 |
| 具身智能 | 轨迹精修 | [Coarse-to-Refine: Trajectory Self-Refinement in Single Autoregressive Pass for Driving VLA](cards-0003.md#paper-154559) | 在同一次自回归序列内生成草案和修订轨迹 |
| 计算机视觉 | 分层评测 | [COCOTree: A Dataset and Benchmark for Open Tree-Structured Visual Decomposition](cards-0003.md#paper-139427) | 用同一指标评估掩码、标签与树结构 |
| 科学机器学习 | 群体建模 | [CODA: Cohort- and Drift-aware Foundation Model for Multimodal Clinical Reasoning](cards-0003.md#paper-149608) | 将群体原型与个体偏离分开表示 |
| 机器学习系统 | 算子融合 | [CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs](cards-0003.md#paper-153802) | 尽量在矩阵乘法输出块仍驻片上时执行后处理 |
| Agent | 界面预测 | [Code2World: A GUI World Model via Renderable Code Generation](cards-0003.md#paper-151489) | 将可渲染界面作为动作后状态的中间表示 |
| 多模态学习 | 蒸馏 | [Codebook-Guided Cross-Modal Knowledge Distillation for Structurally Heterogeneous Features](cards-0003.md#paper-155243) | 缺少逐位置对齐时改用概念级码本 |
| 计算机视觉 | 表示压缩 | [CodecSplat: Ultra-Compact Latent Coding for Feed-Forward 3D Gaussian Splatting](cards-0003.md#paper-151528) | 编码规整的二维生成中间特征而非最终高斯集合 |
| 软件工程 | 评测设计 | [Code Review Bench: An Automated Benchmark for Evaluating the Software Factory](cards-0003.md#paper-139002) | 用开发者实际处理建议的行为补充静态审查基准 |
| 多模态学习 | 特征路由 | [CoDeRNet: Selective Cross-Task Routing under Heterogeneous Supervision for Change Detection and Captioning](cards-0003.md#paper-149333) | 同时看接收任务的需求和发出任务的置信度 |
| 大语言模型 | 奖励建模 | [CodeScaler: Scaling Code LLM Training and Test-Time Inference via Reward Models](cards-0003.md#paper-149471) | 测试稀缺时用验证数据训练奖励模型并用于候选排序 |
| 软件工程 | 人机监督 | [Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?](cards-0003.md#paper-155551) | 用提交前人工确认率检验代理安全告警是否有效 |
| 生成模型 | 蒸馏损失 | [CoDMD: Copula-aware Distribution Matching Distillation for Fast Video Generation](cards-0003.md#paper-154796) | 少步蒸馏中保持样本间及帧间关系 |
| Agent | 策略图 | [CoE-Agent: Co-Evolving Patient-Doctor Agents via Interactive Policy Graph Optimization for Clinical Decision Making](cards-0003.md#paper-155085) | 用显式策略图连接信息收集、工具与决策 |
| 大语言模型 | 群体微调 | [Co-evolution: A "One-to-many" LLM Fine-Tuning Paradigm](cards-0003.md#paper-149378) | 以边际覆盖奖励降低多个微调后代的冗余 |
| 生成模型 | 流匹配 | [Co-Evolving Interpolants and Flows via Path-Flow Alignment](cards-0003.md#paper-153495) | 联合学习插值路径时监测中间分布熵 |
| 大语言模型 | 蒸馏 | [Co-Evolving Policy Distillation](cards-0003.md#paper-152206) | 把专家互蒸馏插入各自强化学习过程 |
| 具身智能 | 反事实监督 | [CofactVLA: Deconfounding Vision-Language-Action Models via Counterfactual Intervention](cards-0003.md#paper-153110) | 用语言遮蔽分支诊断视觉捷径 |
| Agent | 长程评测 | [CoffeeBench: A Benchmark for Long-Horizon Strategic Decision-Making in Multi-Agent Economies](cards-0003.md#paper-138891) | 将持续谈判与利润纳入多智能体评测 |
| 多模态学习 | 行为评测 | [CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments](cards-0003.md#paper-139836) | 用原始交互界面和响应时限测行为特征 |
| 大语言模型 | 评测诊断 | [CogBench: Evaluating Cognitive-Level Control in LLM Question Generation](cards-0003.md#paper-139467) | 用异级动词限制检验问题的真实认知层级 |
| 认知科学 | 机制建模 | [Cognitive constraints and thalamocortical architecture explain systematic biases and neural signatures in human hierarchical decision-making](cards-0003.md#paper-155926) | 为层级选择和情境切换分别引入约束 |
| 大语言模型 | 泛化诊断 | [Cognitive Firewalls: A Synthetic Account of Cross-Lingual Reasoning Collapse](cards-0003.md#paper-153873) | 区分总体能力和条件策略切换 |
| 计算机视觉 | 生成训练 | [Co-GRPO: Co-Optimized Group Relative Policy Optimization for Masked Image Generation](cards-0003.md#paper-148331) | 将解码调度和模型纳入同一个轨迹奖励 |
| 计算机视觉 | 代理指标审计 | [COHE: Auditing Non-Transitivity in Sample Difficulty Proxies for Vision Models](cards-0003.md#paper-139659) | 在用难度代理筛数据前验证决策收益 |
| 机器人学 | 语义规划 | [Coherence-Aware Transition-Intent Fusion for LTL Planning under Uncertain Semantic Maps](cards-0003.md#paper-152340) | 把多个可行自动机转移保留到动作选择 |
| 学习理论 | 一致性投影 | [Coherence Mechanisms for Provable Self-Improvement](cards-0003.md#paper-150732) | 用任务保持变换构造模型自修正约束 |
| 医学影像 | 分层委托 | [Coherent Hierarchical Multi-Label  Learning to Defer for Medical Imaging](cards-0003.md#paper-149553) | 在整棵标签树上解码交接决定 |
| 统计学习 | 树结构 | [Coherent Routing in Decision Trees: Phase-Interference Learning for Interpretable Tabular Prediction](cards-0003.md#paper-155857) | 用可解释的分支相位检查软树的路径交互 |
| 科学机器学习 | 约束评测 | [CoilStellaration: A Dataset and Benchmark for Engineering-Aware Stellarator Coilset Generation](cards-0003.md#paper-139216) | 工程几何可行性与目标场保真分别验收 |
| 计算机视觉 | 三维表征 | [CoLa3D: Composable Latent 3D Decomposition](cards-0003.md#paper-156142) | 直接从场景共享潜变量分解物体 |
| 时间序列 | 可解释性 | [CoLaX: Context-Aware Local Explanations for Time Series Classification](cards-0003.md#paper-155599) | 让局部解释受全序列上下文调节 |
| 医学机器学习 | 证据审计 | [ColdDDI: Evaluating Knowledge Utilization in Cold-Start Drug-Drug Interaction Prediction](cards-0003.md#paper-138874) | 用输入遮蔽区分知识可用性和实际使用 |
| 大语言模型 | 推理蒸馏 | [Collaborative Reasoning Distillation via Cross-Feedback and Coherent Curation](cards-0003.md#paper-152076) | 在教师答案拼接之前验证过程正确性 |
| 多模态学习 | 闭环推理 | [CollabVR: Collaborative Video Reasoning with Vision-Language and Video Generation Models](cards-0003.md#paper-149957) | 按局部失败类型分配视频重试预算 |
| 推荐系统 | 表征学习 | [Collapse Hunter: Tackling the Dimensional Degeneration in Generative Ranking](cards-0003.md#paper-154459) | 先定位交互通道再加非线性 |
| 计算机视觉 | 条件生成 | [COLLAR: Cascaded Object-Level Latent Refinement for High-Fidelity Conditional Generation](cards-0003.md#paper-149747) | 先扩局部视野再融合全图 |
| 多模态学习 | 基准诊断 | [ColorConceptBench: A Benchmark for Probabilistic Color-Concept Understanding in Text-to-Image Models](cards-0003.md#paper-139721) | 用颜色分布评估隐式语义 |
| 计算机视觉 | 扩散采样 | [Colored Noise Diffusion Sampling](cards-0003.md#paper-148997) | 按时间和频带分配随机噪声 |
| Agent | 防御评测 | [Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems](cards-0003.md#paper-138980) | 分别审计讨论与实际行为 |
| 科学机器学习 | 稀疏自动微分 | [Colour me shocked: Exact Molecular Hessians from MLIPs in O(N) time using sparse differentiation!](cards-0003.md#paper-151062) | 用已知稀疏图压缩二阶求导 |
| 多模态学习 | 潜变量推理 | [CoLVR: Enhancing Exploratory Latent Visual Reasoning via Contrastive Optimization](cards-0003.md#paper-154180) | 对中间表征施加对比约束而非硬匹配 |
| 图学习 | 异常检测 | [Combating Camouflage and Forgetting: Spatio-Temporal Dual Denoising for Money Laundering Detection](cards-0003.md#paper-152926) | 分开处理邻域噪声和时间漂移 |
| 大语言模型 | 持续学习 | [Combating Catastrophic Forgetting in Continual Domain Adaptation via Knowledge Recasting](cards-0003.md#paper-148553) | 将新域例子转写成已有技能可复用的程序 |
| 大语言模型 | 防御审计 | [Combating Data Laundering in LLM Training](cards-0003.md#paper-155652) | 测试版权审计是否对训练文本形式差异敏感 |
| 时间序列 | 异常检测 | [COMET: Codebook-based Online-adaptive Multi-scale Embedding for Time-series Anomaly Detection](cards-0003.md#paper-150690) | 仅用可靠正常样本在线刷新原型 |
| 多模态学习 | 不确定性 | [CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation](cards-0003.md#paper-151624) | 将语境歧义和可接受答案数量分开估计 |
| 多模态学习 | 持续学习 | [COMET: Decoupled Distillation, Routing, and Capacity Control for Task-Agnostic Continual Vision--Language Learning](cards-0003.md#paper-152607) | 把保持特征关系、专家路由和容量增减拆开 |
| 医疗人工智能 | 多智能体评测 | [CoMMa: Contribution-Aware Medical Multi-Agents for Decentralized Oncology Decision Support](cards-0003.md#paper-153350) | 将分区代理贡献显式量化以便追查 |
| 大语言模型 | 推理诊断 | [Commit Then Explore: Reasoning Models Diversify, Not Converge](cards-0003.md#paper-151110) | 先测答案在推理前段是否已可读出，再决定延长预算 |
| 医疗人工智能 | 联邦统计 | [Communication-Efficient Federated Learning of Latent Patient Representations from Multi-Institutional EHRs](cards-0003.md#paper-151353) | 先判断低秩边缘统计能否替代多轮共享 |
| 机器学习系统 | 通信压缩 | [Communication-Efficient LLM Adaptation over Decentralized GPU Meshes](cards-0003.md#paper-153942) | 将快速压缩更新和低频高保真锚点分开 |
| 联邦学习 | 模型合并 | [Communication-Efficient Personalized Adaptation via Federated-Local Model Merging](cards-0003.md#paper-150059) | 用任务损失上界选择全局与本地模型的混合权重 |
| 大语言模型 | KV 检索 | [CommunityKV: Efficient Long-Context Decoding via Graph Partitioning](cards-0003.md#paper-154739) | 用预填充注意力图静态分组，再局部更新。 |
| 大语言模型 | 归因诊断 | [Commutator Memory: Sparse, Path-Local Reading and Steering in Language Models](cards-0003.md#paper-156037) | 按 token 追踪后训练换序影响。 |
| 多模态学习 | 压缩 | [Comp$^2$VLM: A Hybrid Framework Combining Quantization and Lossless Compression for Efficient Vision-Language Models](cards-0003.md#paper-153373) | 联合选择量化尺度和便于并行解码的编码。 |
| 大语言模型 | 稀疏注意力 | [CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection](cards-0003.md#paper-153990) | 把稀疏掩码转为分页 KV 块表。 |
| 推荐系统 | 策略压缩 | [Compact Representations of Impact-Based Fair-Ranking Policies](cards-0003.md#paper-152227) | 以物品索引对偶向量替代每用户排序混合。 |
| 科学机器学习 | 结构剪枝 | [Compact SO(3) Equivariant Atomistic Foundation Models via Structural Pruning](cards-0003.md#paper-154865) | 按完整不可约表示块剪枝。 |
| 计算机视觉 | 三维重建 | [CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](cards-0003.md#paper-155667) | 根据纹理和区域复杂度分配高斯。 |
| 学习理论 | 架构诊断 | [Comparing Linear Regions in ReLU-Type Networks: Theory and Monte Carlo Methods](cards-0003.md#paper-153164) | 用线性模式 Monte Carlo 比较层宽配置。 |
| 大语言模型 | 架构诊断 | [Comparing Transformers and Hybrid Models at the Token Level](cards-0003.md#paper-154270) | 按 token 类型测混合架构相对纯注意力的收益。 |
| Agent / 优化 | 模板检索 | [COMPASS: Composable Policy-Amortized Structured Search for LLM-Based Optimization Modeling](cards-0003.md#paper-150292) | 让求解反馈训练模板图的遍历策略。 |
| 生成模型 | 流匹配 | [Compatible Likelihoods for Flow Matching on Manifolds](cards-0003.md#paper-150283) | 先验证总体最优速度是否复现边缘速度。 |
| 时序建模 | 事件预测 | [Competing Event Models: Next Event Prediction Under Interventions](cards-0003.md#paper-150873) | 分别建模各事件的潜在等待时间。 |
| 大语言模型 | KV 压缩 | [CompilerKV: Risk-Adaptive KV Cache Compression via Offline Experience Compilation](cards-0003.md#paper-153264) | 离线估计注意力头可靠性后用于运行时压缩。 |
| 多模态学习 | 评测校准 | [CompJudge: Fine-Grained Comparative Evaluation using Multimodal LLM for Subject-Driven Generation](cards-0003.md#paper-148734) | 用配对比较重新校准生成图像身份保持打分。 |
| 多模态学习 | 测试时适配 | [Complementary Cache Guidance with Gradient Disentanglement for Continuous Test-Time Adaptation](cards-0003.md#paper-151298) | 分开短期与长期缓存，并隔离梯度方向。 |
| 计算机视觉 | 部件发现 | [Complementing DINO Features with Image Structure for Part Discovery](cards-0003.md#paper-151156) | 先按边界分区再池化冻结特征。 |
| 学习理论 | 可辨识性 | [Complete or Sparse: A Tale of Two Identifiabilities](cards-0003.md#paper-155305) | 按表征维数及因果方向选择潜变量恢复约束。 |
| 科学机器学习 | 数据评测 | [CompleteRXN: Toward Completing Open Chemical Reaction Databases](cards-0003.md#paper-138965) | 用未策展数据验证缺失补全能否迁移。 |
| 计算机视觉 | 多细节渲染 | [Complexity Aware Continuous Level of Details for Gaussian Splatting](cards-0003.md#paper-155902) | 按场景复杂度训练及保留原语，并测不同预算。 |
| 多模态学习 | 联邦适配 | [Complexity-Aware LoRA Aggregation for Modality-Heterogeneous Federated Person Re-identification](cards-0003.md#paper-151019) | 按任务复杂度聚合低秩更新 |
| 计算机视觉 | 几何正则 | [Complexity-guided Regularization for Generalizable Human Gaussian Splatting](cards-0003.md#paper-148201) | 给复杂区域增配高斯及监督 |
| 图学习 | 复杂度分析 | [Complexity of Classical Acceleration for $\ell_1$-Regularized PageRank](cards-0003.md#paper-153053) | 按节点活跃边界判断是否启用加速 |
| 统计学习 | 差分隐私 | [Complexity of Differentially Private Selection via Federated APIs](cards-0003.md#paper-153126) | 需要私有选优时比较聚合与稀疏向量接口 |
| Agent | 信用分配 | [Complex Optimization Modeling via Multiagent Fine-Tuning and Skill-Augmented Reasoning](cards-0003.md#paper-155127) | 给建模流程的中间角色分配反事实反馈 |
| 生成模型 | 扩散桥 | [Complex Schrödinger Bridges](cards-0003.md#paper-153202) | 给分布转换显式引入几何先验 |
| Agent | 互补奖励 | [COMPLLLM: Fine-tuning LLMs to Discover Complementary Signals for Decision-making](cards-0003.md#paper-155547) | 按对下游决策的新增信息训练助手 |
| 计算机视觉 | 分布外检测 | [Component-Based Out-of-Distribution Detection](cards-0003.md#paper-148274) | 分别测组件外观漂移和组合不一致 |
| 因果学习 | 仿真评测 | [Composable Causality: A Toolkit for Systematic Time-Series Causal Discovery and Treatment-Effect Benchmarking](cards-0003.md#paper-139605) | 固定其他生成因素单独扫描缺失机制 |
| 大语言模型 | 条件生成 | [COMPOSE: Composing Future Theorems from Citations and Formal Structure](cards-0003.md#paper-151315) | 生成数学研究假说时同时检索引用与形式依赖 |
| 计算机视觉 | 多视角关联 | [COMPOSE: Hypergraph Cover Optimization for Multi-view 3D Human Pose Estimation](cards-0003.md#paper-150956) | 用高阶关联代替逐视角匹配 |
| 具身智能 | 位姿跟踪 | [ComPose: When to Trust Hands for Object Pose Tracking](cards-0003.md#paper-151739) | 物体被手遮挡时引入选择性的手部运动证据 |
| 强化学习 | 多源行为引导 | [Compose Your Oracles: Off Policy Improvement with Aggregated Guidance](cards-0003.md#paper-149600) | 按来源估值筛选互补专家的候选动作 |
| 科学机器学习 | 约束采样 | [Composing Diffusion Priors with Explicit Physical Context via Generative Gibbs Sampling](cards-0003.md#paper-152144) | 将冻结先验同显式物理约束用交替推断组合 |
| 学习理论 | 组合泛化 | [Compositional Generalization Certificates via the Van Kampen Theorem](cards-0003.md#paper-152239) | 检查模块交叠处是否处于正确表示分支 |
| 具身智能 | 技能组合 | [Compositional Policy Optimization with Language Models](cards-0003.md#paper-149110) | 根据后续子任务表现确定前一技能的参数 |
| 大语言模型 | 组合训练 | [Compositional Reasoning in Language Models under Reinforcement Learning Post-Training](cards-0003.md#paper-155613) | 训练完整组合任务与仅训练组件作双向迁移对照 |
| 具身智能 | 轨迹规划 | [Compositional Training-Free Diffusion Planning for Long-Horizon Multiple Reach-Avoid Tasks](cards-0003.md#paper-151682) | 拼接任务无关短程先验并逐段校验约束 |
| 大语言模型 | 课程设计 | [Composition-RL: Compose Your Verifiable Prompts for Reinforcement Learning of Large Language Models](cards-0003.md#paper-148886) | 把已饱和的可验提示组合成更难的新题 |
| 大语言模型 | 模型压缩 | [COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression](cards-0003.md#paper-150918) | 用正交字典和分层预算替代所有层共享的低秩假设 |
| 表征学习 | 功能压缩 | [Compressible Representations: Functional Spines in Deep Neural Networks](cards-0003.md#paper-154300) | 按下游敏感性选投影方向 |
| 机器学习 | 等价化简 | [Compressing Collections of Trees with Decision Equivalence](cards-0003.md#paper-150720) | 按决策边界去重树集合 |
| 多模态学习 | 量化诊断 | [Computational Depth Predicts Quantization Sensitivity in Multimodal Models](cards-0003.md#paper-150194) | 用浅探针预测深任务量化退化 |
| 学习理论 | 机制设计 | [Computational Dynamic Mechanism Design](cards-0003.md#paper-153891) | 把动态激励相容检验放入双层优化 |
| 学习理论 | 可复现学习 | [Computationally Efficient Replicable Learning of Parities and Applications](cards-0003.md#paper-150028) | 区分统计可学与计算可学 |
| 统计学习 | 参数辨识 | [Computationally sufficient statistics for Ising models](cards-0003.md#paper-155651) | 按可观测统计阶数分析 Ising 辨识 |
| 大语言模型 | 训练目标 | [Compute Aligned Training: Optimizing for Test Time Inference](cards-0003.md#paper-153933) | 按部署时聚合规则定义后训练损失 |
| 机器学习系统 | 算力分配 | [Compute Allocation Under Model-Provider Competition](cards-0003.md#paper-152439) | 将延迟和需求拥塞纳入分配模型 |
| 优化 | 动量分析 | [Compute Efficiency and Serial Runtime Tradeoffs for Stochastic Momentum Methods](cards-0003.md#paper-148716) | 同时比较迭代数与总梯度开销 |
| 科学机器学习 | 数据预算 | [Compute-optimal data scaling for neural surrogates via multi-fidelity training](cards-0003.md#paper-151246) | 联合选择样本量和数值保真度 |
| 学习理论 | 训练预算 | [Compute-Optimal Pretrain--Fine-tune in Ridge Gradient Flow](cards-0003.md#paper-152040) | 按下游几何选预训练切换点 |
| 可靠性 | 实验审计 | [Computer Science Conferences Should Require Nonrepudiable Experimental Results](cards-0003.md#paper-140060) | 让报告数值绑定到可核验的执行 |
| Agent | 评测诊断 | [Computer Use at the Edge of the Statistical Precipice](cards-0003.md#paper-151946) | 在静态电脑使用基准加入不看屏幕的对照 |
| 优化 | 最优传输 | [Computing All Optimal Partial $p$-Wasserstein Matchings on the Line](cards-0003.md#paper-155133) | 在一维部分传输中复用平衡区间计算 |
| 学习理论 | 组合算法 | [Computing Thiele Rules on Interval Elections and their Generalizations](cards-0003.md#paper-150647) | 按候选者区间和选民区间分别设计算法 |
| 多模态学习 | 持续学习 | [Concentrated Gradients Amplify Forgetting: Dominant-direction Projection for Continual Multimodal Learning](cards-0003.md#paper-154350) | 约束梯度主方向而非只保护共享参数 |
| 医学影像 | 多模态路由 | [Concept-Aware Wasserstein Routing with Vision-Language Guidance for Few-Shot WSI Classification](cards-0003.md#paper-149192) | 在弱监督切片分类中让图块匹配多个语义概念 |
| 可解释性 | 表征诊断 | [Concept frustration: Aligning human concepts and machine representations](cards-0003.md#paper-149108) | 以任务相关几何检查模型概念关系是否超出人类本体 |
| 表征学习 | 概念解耦 | [Concept-Localized Generative Representations](cards-0003.md#paper-150809) | 显式区分概念与残差潜变量 |
| 学习理论 | 可识别性 | [Concept Modulation Models: A Unified Framework for Identifiability and Extrapolation](cards-0003.md#paper-153542) | 分开验证观测域识别与未见属性外推 |
| 计算机视觉 | 概念瓶颈 | [Concepts in Motion: Temporal Concept Bottleneck Model for Interpretable Video Classification](cards-0003.md#paper-151556) | 让每个概念分别建模出现时间 |
| 多模态学习 | 弱监督 | [Concepts Worth Having: Refining VLM-Guided Concept Bottleneck Models with Minimal Annotations](cards-0003.md#paper-151925) | 以少量密集人工概念标注修正视觉语言伪标签 |
| 统计学习 | 共形预测 | [Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models](cards-0003.md#paper-152103) | 联合校准概念和类标签并修正逻辑冲突 |
| 大语言模型 | 约束优化 | [Concise Reasoning Through the Lens of Lagrangian Optimization](cards-0003.md#paper-151507) | 用准确率下限约束推理长度 |
| 可解释性 | 电路诊断 | [Conclusions from Circuit Extraction Depend on the Level of Description: A Controlled Comparison](cards-0003.md#paper-155212) | 按注意力头和精确边分别检验电路稳定性 |
| 图学习 | 几何表示 | [Concorde: Geometry-Aware Link Prediction via Decoupled Energy Minimization](cards-0003.md#paper-150148) | 把稳定拓扑锚点与学习的几何残差分离 |
| 机器人学 | 三维建图 | [Concord-SLAM: Cross-Render Concordance for Boundary-Native Semantic Gaussian SLAM](cards-0003.md#paper-154365) | 用同一地图的语义、深度和法线分歧指导边界更新 |
| 生成模型 | 采样诊断 | [Concurrence of Symmetry Breaking and Nonlocality Phase Transitions in Diffusion Models](cards-0003.md#paper-153436) | 联合寻找全局去噪需求与语义分支出现的时间窗 |
| 多模态学习 | 联合采样 | [Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Process](cards-0003.md#paper-154281) | 让图文同一步内交换置信度并允许撤回决定 |
| 具身智能 | 时序表示 | [CondenseVLA: Learnable History Condensation for Efficient Multi-Frame VLA](cards-0003.md#paper-149245) | 将多帧历史压入固定数量的可学习槽 |
| 因果学习 | 分布估计 | [Conditional Counterfactual Mean Embeddings: Doubly Robust Estimation and Learning Rates](cards-0003.md#paper-152006) | 异质效应分析中估计完整的反事实分布 |
| 大语言模型 | 评测校准 | [Conditional Evaluation of Language Models with Cheap Auxiliary Signals](cards-0003.md#paper-153992) | 用目标区域内中心化的廉价信号降低人评成本 |
| 统计学习 | 图模型 | [Conditional independence and graphical models for rankings](cards-0003.md#paper-153084) | 在相对顺序表示上表达排名的条件独立 |
| 大语言模型 | 安全评测 | [Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](cards-0003.md#paper-151278) | 用多样部署语境复核后训练安全干预效果 |
| 多模态学习 | 视频评测 | [Conditional Multi-Event Temporal Grounding in Long-Form Video](cards-0003.md#paper-139151) | 联合测全部满足条件的事件定位、计数和拒答 |
| 大语言模型 | 测试时引导 | [Conditional Optimal Bridge for Riemannian Activation Steering](cards-0003.md#paper-153803) | 按当前激活选择内容质量引导方向 |
| 概率建模 | 条件采样 | [Conditioning Gaussian Processes on Almost Anything](cards-0003.md#paper-155789) | 用同一高斯过程推断框架接入非共轭观测 |
| 多模态学习 | 置信度校准 | [ConfDet: Learning Reliable Confidence for MLLM-based Detection](cards-0003.md#paper-151261) | 把检测置信度作为显式输出训练和校准 |
| 语言模型 | 并行解码 | [Confidence-Based Decoding is Provably Efficient for Diffusion Language Models](cards-0003.md#paper-151802) | 按累计熵决定解掩码数量 |
| 大语言模型 | 模型路由 | [Confidence Estimation via Decoupled Smoothing for Dynamic LLM Routing and Aggregation](cards-0003.md#paper-148424) | 按查询选择路由或集成 |
| 大语言模型 | 模型保护 | [Conflict-Aware Logit Adapters for Utility-Preserving Anti-Distillation](cards-0003.md#paper-152508) | 比较训练时保护与解码时干预 |
| 大语言模型 | 检索增强 | [Conflict-Suppressed RAG: A Simple Decoding-Time Framework for Faithful Retrieval-Augmented Generation](cards-0003.md#paper-148415) | 检索与参数知识冲突时测试解码干预 |
| Agent | 故障归因 | [Conformal Agent Error Attribution](cards-0003.md#paper-150722) | 预测可回滚的连续故障窗口 |
| 生成模型 | 缓存校准 | [Conformal Cache: Reliable Proxy-Discrepancy Caching for Fast Generative Inference](cards-0003.md#paper-150311) | 对缓存误差代理做单侧校准 |
| 大语言模型 | 共形生成 | [Conformal Language Modeling via Posterior Sampling](cards-0003.md#paper-150795) | 把置信控制放入条件生成 |
| 统计学习 | 分布回归 | [Conformal Prediction for Distribution-to-Distribution Regression](cards-0003.md#paper-155524) | 在正交基上构造可抽样的预测集合 |
| 科学机器学习 | 时序校准 | [Conformal Prediction for Time-Dependent PDEs](cards-0003.md#paper-150920) | 按网格精度和时间跨度检查覆盖 |
| 大语言模型 | 不确定性校准 | [Conformal Prediction with Paraphrase-Aware Scoring for LLM Uncertainty Quantification](cards-0003.md#paper-152533) | 用等义改写集合代替单提示计分 |
| 大语言模型 | 选择性决策 | [Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs](cards-0003.md#paper-148731) | 为自适应部署使用逐轮有效的选择风险控制 |
| 联邦学习 | 客户端选择 | [Confounding-Aware Client Selection in Federated Learning via Causal Mediation Analysis](cards-0003.md#paper-149343) | 区分报价驱动的选择与数据贡献 |
| 科学机器学习 | 校准诊断 | [ConnectomeBench2: A Unified Benchmark for Automated Connectomic Proofreading](cards-0003.md#paper-139242) | 用分布距离筛查神经影像校对的失准 |
| 生成模型 | 似然理论 | [Conservation Laws for Diffusion Models](cards-0003.md#paper-152592) | 有限容量下按局部后验难度比较噪声路径 |
| 强化学习 | 约束策略 | [Conservatism Controllable Compositional Guidance for Offline Safe Reinforcement Learning](cards-0003.md#paper-149132) | 部署时分开调节奖励与安全引导 |
| 统计学习 | 稳健控制 | [Conservative Continuous-Time Treatment Optimization](cards-0003.md#paper-150543) | 对离线连续控制惩罚预测轨迹超出观测支持 |
| 统计学习 | 后验校准 | [Conservative neural posterior estimation via distributionally robust training](cards-0003.md#paper-155960) | 低仿真预算下用分布鲁棒损失训练后验 |
| 优化 | 多目标决策 | [Conservative Pareto Set Amortization for Offline Multi-Objective Optimization](cards-0003.md#paper-152985) | 按偏好直接查询单个设计 |
| 大语言模型 | 推理筛选 | [Consilience for Verifier-Free Test-Time Scaling](cards-0003.md#paper-153648) | 按置信度轨迹选解 |
| Agent | 可靠性评测 | [Consistency as a Testable Property: Statistical Methods to Evaluate AI Agent Reliability](cards-0003.md#paper-155880) | 测语义等价扰动下的过程稳定性 |
| 计算机视觉 | 概念移除 | [Consistency-Preserving Concept Erasure via Unsafe–Safe Pairing and Directional Fisher-weighted Adaptation](cards-0003.md#paper-151483) | 用配对替代监督保留周边语义 |
| 科学机器学习 | 逆问题 | [Consistency Regularised Gradient Flows for Inverse Problems](cards-0003.md#paper-154153) | 在潜空间联合采样与调提示 |
| 图学习 | 防御聚合 | [Consistency-Verified Backdoor Defense for Federated Graph Learning via Cross-Layer Drift](cards-0003.md#paper-152211) | 服务器核对风险与提交更新后再加权 |
| 计算机视觉 | 三维重建 | [Consistent 3D Surface Flow Model with Global State](cards-0003.md#paper-148758) | 分离全局表示容量和点云输出分辨率 |
| 统计学习 | 空间聚类 | [Consistent Bayesian Spatial Domain Partitioning Using Predictive Spanning Tree Methods](cards-0003.md#paper-156639) | 用生成树切分构造可预测的连续区域 |
| 图学习 | 几何表示 | [Consistent Geometric Deep Learning via Hilbert Bundles and Cellular Sheaves](cards-0003.md#paper-153249) | 对流形上的函数型信号保留纤维间连接 |
| 统计学习 | 弱监督损失 | [Consistent One-vs-All Losses Robust to Misspecification of the Weak Label Transition Model](cards-0003.md#paper-150290) | 转移模型不稳时优先保证分类排序 |
| 大语言模型 | 测试时学习 | [Consolidating Reasoning with Test-Time Learning](cards-0003.md#paper-150965) | 用可更新参数合成多条轨迹 |
| 大语言模型 | 无梯度后训练 | [Consolidating Rewarded Perturbations for LLM Post-Training](cards-0003.md#paper-153456) | 把奖励加权专家折叠为单次推理模型 |
| 联邦学习 | 聚合优化 | [Constant Term Shrinkage for Federated Learning](cards-0003.md#paper-152366) | 只收缩受异质性影响的更新分量 |
| 优化 | 受约束采样 | [Constrained Bombieri Point Processes](cards-0003.md#paper-154134) | 样本规模固定时考虑精确组合采样 |
| 大语言模型 | 约束推理 | [Constrained Code Generation with Discrete Diffusion](cards-0003.md#paper-148166) | 在去噪中加入程序正确性检查 |
| 大语言模型 | 约束解码 | [Constrained Decoding for Diffusion Language Models via Efficient Inference over Finite Automata](cards-0003.md#paper-149103) | 把格式约束编成有限自动机再并行采样 |
| 模型压缩 | 低秩剪枝 | [Constrained Factorization with Diagonal Scaling: Rank-Revealing Training and Pruning](cards-0003.md#paper-152576) | 显式对角尺度用于训练中识别冗余 |
| 图学习 | 受约束生成 | [Constrained Goal-directed Planar Graph Generation with Grammar-based Reinforcement Learning](cards-0003.md#paper-154981) | 将语法动作投影到随状态变化的可行集 |
| 图学习 | 谱聚类 | [Constrained Graph Clustering: A Spectral Algorithm with Generalized Eigenvectors](cards-0003.md#paper-151463) | 用必须同组和禁同组两图构造广义谱嵌入 |
| 计算机视觉 | 生成引导 | [Constrained Look-ahead Guidance for Interference-Aware Flow Editing](cards-0003.md#paper-151736) | 更新前先预测编辑与保真是否冲突 |
| 强化学习 | 安全约束 | [Constrained MDPs with Trajectory Constraints](cards-0003.md#paper-154144) | 高风险约束按历史条件化而非从起点平均 |
| 神经网络 | 架构 | [Constrained Modulatory Reservoirs for Context-Dependent Computation](cards-0003.md#paper-152484) | 隔离循环调制的贡献 |
| 优化 | 随机近端方法 | [Constrained Stochastic Spectral Preconditioning Converges for Nonconvex Objectives](cards-0003.md#paper-149304) | 用近端扩展处理谱优化约束 |
| 图学习 | 约束条件化 | [CONSTRAINER: Promptable Graph-Structured Optimization via Constraint Conditioning](cards-0003.md#paper-154276) | 显式编码约束以复用求解骨干 |
| 数据归因 | 约束敏感性 | [Constraint-Aware Influence Estimation in Deep Constrained Learning](cards-0003.md#paper-155081) | 样本移除时同时考虑可行域变化 |
| 语言模型 | 合规评测 | [Constraint Retrieval Is Not Constraint Enforcement in Large Language Models](cards-0003.md#paper-155108) | 分开评估规则召回和执行 |
| 组合优化 | 多专家蒸馏 | [Constructive Neural Policies for the Quadratic Assignment Problem via Multi-Expert Imitation](cards-0003.md#paper-152789) | 单趟构造分配时保留专家序列多样性 |
| 经济学 | 市场反馈 | [Consumer Search and Social Learning in Agentic Markets](cards-0003.md#paper-154159) | 设计搜索系统时验证搜索信号是否进入公共反馈 |
| 生成模型 | 非平衡最优传输 | [Contact Geometry for Generative Models: An Unbalanced Optimal Transport Formulation](cards-0003.md#paper-154366) | 对未配对图像分布分开建模迁移与质量变化 |
| 语言模型 | 流式记忆 | [Context as Low-Rank Weights: Bounded Parametric Dynamic Memory for Unbounded Context](cards-0003.md#paper-149750) | 以固定秩权重更新替代部分历史缓存 |
| 计算机视觉 | 生成顺序 | [Context-Aware Autoregressive Image Generation for Emerging Reasoning Properties](cards-0003.md#paper-151846) | 动态选择下一个空间生成位置 |
| 多模态 | 缺失模态 | [Context-Aware Generative Imputation for Robust Multimodal Learning in Missing Modality Scenarios](cards-0003.md#paper-151257) | 从已见模态补全任务潜变量 |
| 密码学 | 上下文隔离 | [Context Binding and Reusable Leakage in Threshold Decryption](cards-0003.md#paper-153871) | 评估泄漏后果时检查历史授权是否影响未来 |
| 计算机视觉 | 评测诊断 | [ContextShift: A Controlled Benchmark for Context Dependence in Object Detection](cards-0003.md#paper-139652) | 固定物体外观后单独改变背景 |
| 生成模型 | 推理预算 | [Contextual Flow Matching: Adaptive Step Selection in Flow Models for Efficient Visual Generation](cards-0003.md#paper-148315) | 根据输入分配流模型积分步数 |
| 生成模型 | 训练损失 | [Contextual Flow Matching for High-quality Visual Content Generation](cards-0003.md#paper-156013) | 训练速度场时约束局部空间关系 |
| 多模态 | 互动评测 | [Contextualized Evaluation of Vision Language Models through Dynamic Interviews](cards-0003.md#paper-138894) | 用任务状态图驱动多轮追问 |
| 强化学习 | 上下文价值 | [Context Value Informed In-Context Reinforcement Learning](cards-0003.md#paper-149025) | 在有限测试轨迹中用价值预测辅助上下文适应 |
| Agent | 持续学习评测 | [Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments](cards-0003.md#paper-139270) | 把经验带来的增益与底座能力分开 |
| 生成模型 | 回放选择 | [Continual Learning in Modern Hopfield Networks with an Application to Diffusion Models](cards-0003.md#paper-152180) | 优先回放能量较高且易遗忘的样本 |
| 具身智能 | 持续学习 | [Continually Evolving Skill Knowledge in Vision Language Action Model](cards-0003.md#paper-155372) | 共享固定容量网络并按技能知识路由 |
| 机器人学 | 持续技能学习 | [Continual Robot Learning via Language-Guided Skill Acquisition](cards-0003.md#paper-156741) | 按语义相关性挑已有技能热启动新技能。 |
| 机器学习基础 | 时序诊断 | [Continuity Laws for Sequential Models](cards-0003.md#paper-149660) | 用时间细化试验验证序列模型是否连续，再选择降采样频率。 |
| 计算机视觉 | 连续位姿估计 | [ContinuLoc: Continuous Pose Inference over Neural Fields for UAV Geo-Localization](cards-0003.md#paper-149317) | 用可查询连续语义地图取代固定候选位姿库。 |
| 多模态学习 | 声学蒸馏 | [Continuous Audio Thinking for Large Audio Language Models](cards-0003.md#paper-148651) | 把声学证据保存在预填充的连续潜空间中。 |
| 统计学习 | 连续深度 | [Continuous-depth Deep Gaussian Processes](cards-0003.md#paper-150043) | 深层高斯过程优化恶化时，对照残差化与连续深度先验。 |
| 大语言模型 | 扩散训练 | [Continuous Diffusion Scales Competitively with Discrete Diffusion for Language](cards-0003.md#paper-152067) | 比较连续与离散扩散时，匹配架构与计算，并单测似然训练的嵌入收益。 |
| 计算机视觉 | 动态参数化 | [Continuous Expert Assembly: Instance-Conditioned Low-Rank Residuals for All-in-One Image Restoration](cards-0003.md#paper-149532) | 对空间位置分别生成低秩残差以处理局部退化。 |
| 大语言模型 | 潜扩散 | [Continuous Latent Diffusion Language Model](cards-0003.md#paper-154716) | 把全局语义生成和局部 token 实现分开建模。 |
| 统计学习 | 缺失值补全 | [Continuously-Augmented Hybrid Masked Diffusion Model for Data Imputation](cards-0003.md#paper-148351) | 将观测硬约束嵌入采样过程。 |
| 强化学习 | 技能发现 | [Continuous Open-ended Discovery and Evolution of Skills as Hierarchical Reward Programs](cards-0003.md#paper-149488) | 以可执行成功判定及依赖链组织仿真技能课程。 |
| 优化 | 非欧几何优化 | [Continuous p-adic Optimization](cards-0003.md#paper-149111) | 离散赋值使梯度消失时，将优化提升到保几何的连通空间。 |
| 生成模型 | 条件扩散 | [Continuous Personalized Diffusion Model via Spinor-Component Forward Geometry](cards-0003.md#paper-153749) | 把连续控制信号注入前向扩散几何。 |
| 生成模型 | 扩散蒸馏 | [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](cards-0003.md#paper-150079) | 将固定时间锚点改成连续随机日程，并对学生轨迹外预测做匹配。 |
| 统计学习 | 后验采样 | [Contour Monte Carlo: Sampling via Energy Level Sets](cards-0003.md#paper-155748) | 把困难后验采样拆分为能量边缘和层集内条件采样。 |
| Agent | 工具合规评测 | [ContractBench: Can LLM Agents Preserve Observation Contracts?](cards-0003.md#paper-139770) | 分别验收中间工件的时效与字节完整性。 |
| 图学习 | 稳定传播 | [Contractive Monoids: The Algebra Behind Stable Residual Propagation in Deep Graph Neural Networks](cards-0003.md#paper-150369) | 深层消息传递用含恒等元且对组合闭合的收缩约束。 |
| 大语言模型 | 推理蒸馏 | [Contractive Restoring Flows: Robust Reasoning Distillation via Orbital Stability](cards-0003.md#paper-152740) | 蒸馏时收缩离开教师轨迹的误差，保留沿轨迹的变化。 |
| 表示学习 | 对比采样 | [Contrast encodes inductive bias: separating slow noise from dynamics in predictive representation learning](cards-0003.md#paper-149353) | 使用同轨迹负样本以移除轨迹特有慢噪声捷径。 |
| 图学习 | 防御检测 | [Contrastive Adversarial Training for Robust Graph Neural Networks under Label Poisoning](cards-0003.md#paper-150131) | 使用标签与局部图结构的一致性识别异常监督。 |
| 科学机器学习 | 证据比较 | [Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](cards-0003.md#paper-154298) | 对同一个问题比较互斥解释，用证据更新排序。 |
| 计算机视觉 | 域适应 | [Contrastive Hypergraph Source-free Domain Adaptive Object Detection in Adverse Weathers](cards-0003.md#paper-152434) | 恶劣天气下用超边传播候选间语义。 |
| 学习理论 | 对比监督 | [Contrastive Identification and Generation in the Limit](cards-0003.md#paper-150695) | 先判定无方向的成对监督是否足以识别或生成。 |
| 机器学习 | 主动采集 | [Contrastive Nonmyopic Objective Cost-Tradeoff Acquisition for Longitudinal Data](cards-0003.md#paper-148964) | 按长期预测收益缓存测量计划。 |
| 强化学习 | 表征学习 | [Contrastive Pretraining Scales Agentic Exploration](cards-0003.md#paper-149777) | 预训练时保留候选动作间的可区分性。 |
| 大语言模型 | 遗忘正则 | [Contrastive Representation Shaping for LLM Unlearning](cards-0003.md#paper-151743) | 把遗忘与保留表示干扰作为辅助目标。 |
| 信息检索 | 重排序 | [Contrastive Retrieval Heads for Improved Attention-Based Reranking](cards-0003.md#paper-150870) | 按相关与干扰文档区分能力选注意力头。 |
| 大语言模型 | 解码 | [Contrastive Thinking Decoding: Steering Answer Generation in Reasoning Models](cards-0003.md#paper-153432) | 用退化推理轨迹作为答案解码的对照。 |
| 机器学习 | 模型合并 | [Contribution-Aware Structured Sparsity for Model Merging](cards-0003.md#paper-154890) | 按任务贡献筛结构组件再合并权重。 |
| 科学机器学习 | 数据同化 | [Control-Augmented Autoregressive Diffusion for Data Assimilation](cards-0003.md#paper-152028) | 离线学习观测校正以降低滚动同化成本。 |
| 多智能体 | 稳健监测 | [Control Charts for Multi-Agent Systems](cards-0003.md#paper-156073) | 监测自适应群体时保留固定参考对照。 |
| 强化学习 | 表征训练 | [Control First, Robustness Next: Decoupled Representation Learning for Visual RL Generalization](cards-0003.md#paper-155463) | 先学控制表征，再离线对齐强增强输入。 |
| 三维视觉 | 特权蒸馏 | [ControlFlow3D: Distilling Multi-View Knowledge into Latent Flow Matching for Point Cloud Upsampling](cards-0003.md#paper-151092) | 训练用多视图，部署仅输入点云。 |
| 大语言模型 | 轨迹正则 | [ControlJEPA: Principled Trajectory Regularization via Lyapunov Tube Loss](cards-0003.md#paper-149461) | 用可解释容差控制隐藏状态横向偏离。 |
| 推荐系统 | 可控表示 | [Controllable and Content Based Recommendations](cards-0003.md#paper-152374) | 用可编辑文本用户画像作为推荐接口。 |
| 三维视觉 | 条件生成 | [Controllable Dynamic 3D Shape Generation via 3D Trajectories and Text](cards-0003.md#paper-154139) | 将空间轨迹作为文字之外的运动控制输入。 |
| 因果学习 | 仿真评测 | [Controllable Generative Sandbox for Causal Inference](cards-0003.md#paper-155513) | 校准混合类型模拟数据，同时独立扫描因果难点。 |
| 多模态学习 | 奖励设计 | [Controllable Multi-label Video Safety Detection via Adaptive Tversky Policy Optimization](cards-0003.md#paper-155376) | 按部署需求选择多标签审核的查准和查全权衡。 |
| 计算机视觉 | 结构生成 | [Controllable Road Marking Generation](cards-0003.md#paper-155875) | 对细线布局使用由软到硬的结构约束。 |
| Agent | 模拟评测 | [Controllable User Simulation](cards-0003.md#paper-148816) | 在轨迹生成前设定控制条件 |
| 统计学习 | 混杂校正 | [Controlling for Omitted Variable Bias in Deep Neural Networks](cards-0003.md#paper-153604) | 固定预训练骨干后估计协变量效应 |
| 计算机视觉 | 测试时适配 | [Controlling Temporal Pseudo-Label Marginals for Stable Online Test-Time Adaptation](cards-0003.md#paper-151349) | 监测跨时间的伪标签类别收缩 |
| 科学机器学习 | 稳定性正则 | [Controlling Transient Amplification Improves Long-horizon Rollouts](cards-0003.md#paper-149068) | 训练时监控沿轨迹的雅可比非正规性与不对易性 |
| 可解释性 | 干预诊断 | [Control Reinforcement Learning: Token-Level Mechanistic Analysis via Learned SAE Feature Steering](cards-0003.md#paper-151630) | 分别检查任务内贡献与跨任务迁移 |
| 计算机视觉 | 条件生成 | [ControlSVG: Exploring Controllable SVG Generation with Autoregressive Models](cards-0003.md#paper-151441) | 将中间矢量输出回馈后续生成 |
| 控制理论 | 状态估计 | [Control Under the Wrong Model Is Better Than Under the Correct One](cards-0003.md#paper-149917) | 存在内部噪声时联合选择估计和控制模型 |
| 学习理论 | 二阶优化 | [Convergence Analysis of Newton's Method for Neural Networks in the Overparameterized Limit](cards-0003.md#paper-149087) | 按宽度调整 Newton 正则并检查频谱 |
| 强化学习 | 联邦训练 | [Convergence Guarantees for Federated SARSA with Local Training and Heterogeneous Agents](cards-0003.md#paper-155534) | 按客户端差异权衡本地 SARSA 更新和同步 |
| 学习理论 | 初始化 | [Convergence of Near-Linear Width ReLU Networks with Unbalanced Initialization](cards-0003.md#paper-149591) | 在主动训练隐藏层时检验输出主导初始化 |
| 学习理论 | 组合推理 | [Convex Compositional Reasoning Models](cards-0003.md#paper-152956) | 保留因子可加性并约束每个因子的输入凸性 |
| 机器学习 | 损失函数 | [Conveyance: A Versatile Framework for Learning in Structured Class Spaces](cards-0003.md#paper-155590) | 用类别关系决定需保护的分类间隔 |
| 科学机器学习 | 主动搜索 | [Cool Graphs: Active Property Search Towards Quantum Nano-Refrigerators](cards-0003.md#paper-152915) | 把昂贵仿真预算集中在性质符号未确定的候选 |
| Agent | 协作诊断 | [COOP$^2$: Defining, Observing, and Repairing Cooperation in LLM Multi-Agent Systems](cards-0003.md#paper-139333) | 只在群体计划预测会违反约束时触发修复 |
| 强化学习 | 探索策略 | [Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration](cards-0003.md#paper-153701) | 在保证已有回报的前提下优化探索奖励 |
| 统计学习 | 共形预测 | [Co-optimization for Adaptive Conformal Prediction](cards-0003.md#paper-150402) | 分别拟合预测区间中心和半径 |
| 强化学习 | 推理搜索 | [Coordinating Hundreds of RL Agents through Scalable Inference-Time Search](cards-0003.md#paper-149906) | 在共享团队目标下为每个智能体搜索独立潜变量 |
| 强化学习 | 协作诊断 | [Coordination Connectivity: Shared Initialization Shapes the Joint-Policy Landscape in MARL](cards-0003.md#paper-154512) | 用联合策略权重插值检测团队版本兼容 |
| 多模态学习 | 高效视频推理 | [CoPE-VideoLM: Leveraging Codec Primitives For Efficient Video Language Modelling](cards-0003.md#paper-152600) | 用编码器运动向量和残差补足稀疏关键帧 |
| 科学机器学习 | 逆向设计 | [Co-PiLOT: Constrained Physics-Informed Latent Optimization for Target-Driven Inverse Design](cards-0003.md#paper-150787) | 在材料模拟预算有限时比较潜空间约束搜索 |
| 多模态学习 | 测试时适配 | [COPRA: Conditional Parameter Adaptation with Reinforcement Learning for Video Anomaly Detection](cards-0003.md#paper-151176) | 按视频片段生成权重增量。 |
| 大语言模型 | 量化 | [CoQuant: Covariance-Aware Rotation for 2-bit KV Cache Quantization](cards-0003.md#paper-154658) | 按注意力实际使用的协方差选择 KV 旋转。 |
| 科学机器学习 | 拓扑评测 | [CORAL: A Benchmark for Structure-aware and Brain-wide Neuron Reconstruction in Light Microscopy](cards-0003.md#paper-139515) | 把拓扑正确性与局部几何接近度分别测量。 |
| 大语言模型 | 低秩适配 | [CORA: Per-Slice Coherent Orthogonal Rotation for SVD-based Low-Rank Adaptation](cards-0003.md#paper-152402) | 用同一旋转联合改写左右奇异基。 |
| 多模态学习 | 缓存压缩 | [CoRDS: Coreset-Based Representative and Diverse Selection for Streaming Video Understanding](cards-0003.md#paper-153844) | 联合考虑键值覆盖和子集互补性。 |
| 大语言模型 | 量化 | [CoreQ: Learning-Free Mismatch Correction and Successive Rounding for Quantization](cards-0003.md#paper-155856) | 分层调节量化失配校正幅度。 |
| 大语言模型 | 检索 | [CoRE-RL: Co-evolving Reasoning Trajectories and Evidence Subgraphs with Learned Evidence Projection](cards-0003.md#paper-151276) | 用中间推理中缺证据的主张继续定向检索。 |
| 生成模型 | 流匹配 | [Coreset-Induced Conditional Velocity Flow Matching](cards-0003.md#paper-154272) | 给内部速度流提供数据构成的近似源。 |
| 学习理论 | 聚类 | [Coresets for Clustering Using Noisy Comparisons and Few Distance Queries](cards-0003.md#paper-149987) | 直接距离昂贵时用比较查询构造核心集。 |
| 大语言模型 | 蒸馏诊断 | [Cornerstones or Stumbling Blocks? Deciphering the Rock Tokens in On-Policy Distillation](cards-0003.md#paper-152055) | 重新评估长期高损失 token 的训练权重。 |
| 计算机视觉 | 模型剪枝 | [CORP: Closed-Form One-shot Representation-Preserving Structured Pruning for Transformers](cards-0003.md#paper-150895) | 用保留结构线性补偿剪除部分的表示。 |
| Agent | 信用分配 | [Correctable Fork Tokens: Verifier-Anchored Selective Credit Assignment for Tool-Integrated RLVR](cards-0003.md#paper-153790) | 用答案条件下的不确定性下降定位工具调用关键 token。 |
| 大语言模型 | 推理诊断 | [Correct but Unselectable: The Hidden Interface Tax in Multi-Candidate Reasoning](cards-0003.md#paper-152214) | 区分生成到正确答案和选择器能读取正确答案。 |
| 统计学习 | 贝叶斯推断 | [Corrected Integrated Laplace Approximation for Bayesian Inference in Latent Gaussian Models](cards-0003.md#paper-154255) | 用重要性采样修正拉普拉斯边缘化误差。 |
| 多模态学习 | 推理校正 | [Correction Space Steering for Hallucination Mitigation in Large Vision-Language Models](cards-0003.md#paper-150994) | 将输入相关的激活修正限制在低秩空间。 |
| 大语言模型 | 扩散后训练 | [Corrective Diffusion Language Models](cards-0003.md#paper-154007) | 显式监督可见错误 token，学习原位修订。 |
| 大语言模型 | 偏好优化 | [Correct, Route, Calibrate: Efficient Preference Optimization from Noisy, Heterogeneous Human Feedback](cards-0003.md#paper-152258) | 把标注噪声、任务分配和标注员评分联合考虑。 |
| 机器学习基础与统计 | 隐私训练 | [Correlating Cross-Iteration Noise for DP-SGD using Model Curvature](cards-0003.md#paper-151628) | 按损失曲率设计跨迭代隐私噪声相关性。 |
| 强化学习 | 模型路由 | [Correlation-Aware Contextual Bandits with Surrogate Rewards for LLM Routing](cards-0003.md#paper-149327) | 代理反馈可能偏差时分开训练真实奖励与代理估计器。 |
| 计算机视觉 | 注意力监督 | [Correpondence Alignment For Improved Virtual Try-On](cards-0003.md#paper-151032) | 在虚拟试衣中直接监督衣物与人体的 QK 对应。 |
| 计算机视觉 | 匹配过滤 | [Correspondence Pruning by Iterative Structural Rectification](cards-0003.md#paper-155477) | 逐层重估匹配结构，并以冻结结构作为消融。 |
| 强化学习 | 多智能体协调 | [CorridorLight: Cooperation as Task Negotiation with Causal Gating for Traffic Signal Control](cards-0003.md#paper-155914) | 用少量走廊级子任务协调快速本地控制。 |
| Agent / 安全 | 防御评测 | [Corrupted Plans, Clean Traces: What Planning-Execution Decoupling Reveals About CoT Monitoring](cards-0003.md#paper-152688) | 独立评估过程监察的漏报与推理预算。 |
| 学习理论 | 鲁棒学习 | [Corruptions of Supervised Learning Problems: Typology and Mitigations](cards-0003.md#paper-156659) | 先区分标签扰动与属性扰动，再决定是否只修正损失。 |
| 科学机器学习 | 跨模态迁移 | [CORTEG: Foundation Models Enable Cross-Modality Representation Transfer from Scalp to Intracranial Brain Recordings](cards-0003.md#paper-154557) | 以空间适配和双频词元接入已预训练的另一种传感器模型。 |
| 科学机器学习 | 时序表征 | [Cortically-Resolved Recurrent Architecture for fMRI](cards-0003.md#paper-152414) | 为每个空间区域学习独立时间整合窗口。 |
| Agent | 上下文管理 | [CORVUS: Context Optimization and Reduction Via Underlying Synchronization for LLM Coding Agents](cards-0003.md#paper-149092) | 将文件读取动作和可更新文件内容分离。 |
| 强化学习 | 信用分配 | [COSAC: Counterfactual Credit Assignment in Sequential Cooperative Teams](cards-0003.md#paper-150611) | 用共享奖励回归与假想后续替代逐智能体环境重放。 |
| 计算机视觉 | 序列化 | [CoScan: Multi-Scale Content-Adaptive Space-Filling Scans for Causal State-Space Image Restoration](cards-0003.md#paper-151869) | 对视觉状态空间模型按图像内容生成扫描路径。 |
| 计算机视觉 | 评测诊断 | [Cosine is Human: The Reproducibility Ceiling of Perceptual Similarity](cards-0003.md#paper-139285) | 按人类投票一致性分层并估计重测上限。 |
| 科学机器学习 | 缺失模态 | [COSMIO: A Benchmark for Cross-Survey Modality Imputation](cards-0003.md#paper-139351) | 同时验证罕见事件补全和下游检出。 |
| 统计学习 | 成本敏感评估 | [Cost-Aware Best-LLM Identification using Dueling Feedback](cards-0003.md#paper-151916) | 按成对判断的证据价值和费用选下一组待比较模型。 |
| 优化 | 采样策略 | [Cost-Aware Learning](cards-0003.md#paper-151093) | 按梯度贡献及样本代价选择有限和优化的采样分布。 |
| 统计学习 | 公平审计 | [Cost Efficient Fairness Audit Under Partial Feedback](cards-0003.md#paper-153329) | 在仅观察正向分配结果时按标注成本选择补采。 |
| Agent / 安全 | 防御监察 | [CoT-Guard: Small Models for Strong Monitoring](cards-0003.md#paper-149885) | 蒸馏小型监察模型，并对分布外异常单独评估。 |
| 大语言模型 | 蒸馏 | [CoTrek: Toward Scalable On-Policy Distillation for Long Chain-of-Thought Reasoning](cards-0003.md#paper-154397) | 在推理偏离后蒸馏短修复段，并随恢复能力增加深度。 |
| 大语言模型 | 推理分析 | [CoTs as Probabilistic Programs: A Programmatic View of Thinking Step-by-Step in Language Models](cards-0003.md#paper-151761) | 用可执行概率程序区分轨迹似然和答案证据。 |
| 具身智能 / 世界模型 | 失效归因 | [Counterfactual Debugging the World Model Transfer Gap](cards-0003.md#paper-155458) | 优先修正对策略得分有反事实影响的状态或奖励偏差。 |
| Agent | 经验蒸馏 | [Counterfactual Distillation: Internalizing Reflective Experience into LLM Agent](cards-0003.md#paper-154297) | 将反馈驱动的修正动作蒸馏回原始决策状态。 |
| 因果学习 | 分布校正 | [Counterfactual Estimation under Composite Treatments via Progressive Distribution Alignment](cards-0003.md#paper-151311) | 按已知因果图逐分量对齐干预分布。 |
| 时间序列 | 反事实生成 | [Counterfactual Explanations for Time-Series Classification via Constrained Flow Matching](cards-0003.md#paper-155627) | 用硬标签约束通用生成器。 |
| 具身智能 | 对比监督 | [Counterfactual Instruction Grounding for Vision-Language-Action Models](cards-0003.md#paper-152584) | 让动作轨迹能辨认原指令。 |
| 可解释性 | 近邻查询 | [Counterfactual Maps: What They Are and How to Find Them](cards-0003.md#paper-153015) | 将树集成反事实转成最近区域搜索。 |
| 统计学习 | 在线校准 | [Counterfactual Online Conformal Prediction Under Adaptive Logging](cards-0003.md#paper-150109) | 对行动选择造成的记录偏差做倾向加权。 |
| 学习理论 | 状态压缩 | [Counterfactual Predictive State Representations: The Intrinsic Dimension of Partial-Information Games](cards-0003.md#paper-148259) | 用反事实预测查询的秩选择状态维数。 |
| Agent | 信用分配 | [Counterfactual Rollout Replay: Forkable Environments as Free Process Rewards for Software Engineering Agents](cards-0003.md#paper-151386) | 在可复原的软件任务状态比较备选操作的回报。 |
| 可解释性 | 约束生成 | [CounterFlowNet: From Minimal Changes to Meaningful Counterfactual Explanations](cards-0003.md#paper-148627) | 在反事实解码时屏蔽不可行动作。 |
| 世界模型 | 多视角评测 | [CounterStrike-1K: A Multi-Perspective Dataset of Professional Gameplay for World Modeling](cards-0003.md#paper-139606) | 用同步参与者视图验证共享状态一致性。 |
| 计算机视觉 | 抗噪监督 | [Counting without Scale: Scale-Consistent Error Correction for Crowd Counting](cards-0003.md#paper-150435) | 并用尺度一致和标注误差校正损失。 |
| 科学机器学习 | 耦合算子 | [CoupledFlow: One-Step Neural Operators for Coupled Multi-Physics PDEs](cards-0003.md#paper-155294) | 用全系统状态条件化各物理过程的传输速度。 |
| 生成模型 | 推理引导 | [Coupled Guidance for Flow Matching](cards-0003.md#paper-153836) | 对流匹配按训练耦合推导引导。 |
| 科学机器学习 | 积分约束 | [Coupled Integral PINN for Discontinuity](cards-0003.md#paper-153205) | 激波附近用积分守恒监督。 |
| 强化学习 | 图协同 | [Coupling-Aware Reinforcement Learning for Co-Evolving Graph Games](cards-0003.md#paper-154400) | 只读取结构耦合节点并限制策略漂移。 |
| 生成模型 | 一步解码 | [Coupling Models for One-Step Discrete Generation](cards-0003.md#paper-154013) | 学习数据与噪声的耦合再一次解码。 |
| 因果学习 | 面板反事实 | [Covariate-Adjusted Deep Causal Learning for Heterogeneous Panel Data Models](cards-0003.md#paper-153186) | 分离非线性协变量和时序潜因子。 |
| 计算机视觉 | 持续适配 | [COVD: Continual Open-Vocabulary Object Detection with Novel Concept Injection](cards-0003.md#paper-155540) | 冻结视觉编码，仅调整少量文本参数引入概念。 |
| 大语言模型 | 量化校准 | [Coverage-Based Calibration for Post-Training Quantization via Weighted Maximum Coverage over Outlier Channels](cards-0003.md#paper-154675) | 用带权覆盖挑选校准文本。 |
| 大语言模型 | 稀疏解码 | [Coverage-Verified Sparse Attention: Closed-Loop Quality Control for Long-Context LLM Decoding](cards-0003.md#paper-155083) | 只恢复覆盖不足的注意力头。 |
| 多模态学习 | 图像融合 | [CoVisIT: Cross-modal Prior Guided Diffusion Model for Visible-to-Infrared Image Translation](cards-0003.md#paper-152458) | 将结构与热测量分别交给各自可靠的输入。 |
| 具身智能 | 世界模型 | [CoWorld-VLA: Thinking in a Multi-Expert World Model for Autonomous Driving](cards-0003.md#paper-156015) | 以分工世界表征直接条件化轨迹生成 |
| 大语言模型 | 低精度训练 | [CPA: Efficient and Stable FP4 RL Training via Cross-Precision Alignment](cards-0003.md#paper-150296) | 对齐真实低精度采样和高精度训练的概率 |
| 学习理论 | 模型架构 | [CP-MLPs: A Tensor-Rank Theory of Tied and Untied MLP Blocks](cards-0003.md#paper-151658) | 按目标交互对称性选择门控共享 |
| 计算机视觉 | 失效诊断 | [Cracks in the Foundation: A Civil Infrastructure Dataset to Challenge Vision Foundation Models](cards-0003.md#paper-139052) | 在低纹理结构表面独立验证缺陷分割 |
| 多模态学习 | 因果诊断 | [CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models](cards-0003.md#paper-149960) | 分别验证冲突证据裁决和证据不足时的拒答 |
| 联邦学习 | 优化 | [CRAFT: Conflict-Resolved Aggregation for Federated Training](cards-0003.md#paper-152651) | 约束全局更新不反向冲突参与客户端 |
| 强化学习 | 策略优化 | [CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies](cards-0003.md#paper-150208) | 用稠密代理配合真实闭环残差做后训练 |
| 具身智能 | 技能组合 | [CrafterDojo: A Suite of Foundation Models for Building Open-Ended Embodied Agents in Crafter](cards-0003.md#paper-139437) | 在轻量沙箱验证层级技能是否改善长程任务 |
| Agent | 研究复现 | [Crafter: Towards Automated Reproducible Machine Learning via Agentic Code Generation](cards-0003.md#paper-151168) | 先核对证据规格再生成、执行和修复实现 |
| Agent | 权重合并 | [CRANE: Constrained Reasoning Injection for Code Agents via Nullspace Editing](cards-0003.md#paper-155462) | 在授权代码维护中分别验证推理增量与工具协议 |
| 强化学习 | 信用分配 | [Credit Assignment with Resets in Language Model Reasoning](cards-0003.md#paper-151001) | 从中间状态重采样后缀定位推理错误 |
| 时间序列 | 评测诊断 | [CREF: Forecasting Benchmarks for the Age of Agents](cards-0003.md#paper-139433) | 冻结预测后等未来数据发布再评分 |
| 计算机视觉 | 位置编码 | [CRePE: Curved Ray Expectation Positional Encoding for Unified-Camera-Controlled Video Generation](cards-0003.md#paper-149844) | 在广角视频中将深度分布写入射线编码 |
| 自然语言处理 | 流式推理 | [CRESiST: Self-Enhancing Exploritive Policy Learning for Simultaneous Speech Translation](cards-0003.md#paper-149613) | 交织输入和输出以保留缓存并学习何时读写 |
| 多模态学习 | 诊断评测 | [CRISP: Compositional Reasoning over Images via Stackable Programs for VLMs](cards-0003.md#paper-139787) | 同时评分视觉推理步骤和最终答案 |
| 计算机视觉 | 解码器 | [CRISP: Fixing Flying Pixels in Latent LiDAR Generation via Diffusion Decoding](cards-0003.md#paper-153441) | 冻结潜变量模型，只更换解码器验证深度边缘错误 |
| 数据策略 | 元数据验证 | [Croissant Baker: Metadata Generation for Discoverable, Governable, and Reusable ML Datasets](cards-0003.md#paper-139027) | 通过本地格式处理器产生可验证元数据 |
| Agent | 结构化评测 | [CroissantMiner: Automated Extraction and Validation of Croissant Metadata for ML Datasets](cards-0003.md#paper-139073) | 对跨章节字段比较单次全局抽取与多 Agent 分解 |
| 机器学习 | 迁移诊断 | [Cross-Architecture Transferability is Width-Confounded:Diagnosis and Subspace Correction](cards-0003.md#paper-151354) | 跨架构选模型时先校正宽度 |
| 多模态学习 | 不确定性 | [Cross-Attentive Bayesian Low-Rank Adaptation for Multimodal Uncertainty Estimation](cards-0003.md#paper-149084) | 用局部语音线索调节适配器置信度 |
| 科学机器学习 | 基准诊断 | [Cross-Cell-Line Perturbation Prediction Needs Controls](cards-0003.md#paper-139089) | 用无效应与平均差值对照检验泛化指标 |
| 多模态学习 | 推理校验 | [Cross-Channel Agreement Beats Consensus: Compositional Verification for Geometry Reasoning](cards-0003.md#paper-151708) | 让不同错误来源的路径相互印证 |
| 可解释性 | 时序特征 | [Crosscoding Through Time: Sparse Feature Discovery Across Sequence Positions](cards-0003.md#paper-151653) | 跨序列位置学习稀疏特征 |
| 机器学习系统 | 约束解码 | [Cross-Dialect Generalization Without Retraining: Benchmarks and Evaluation of Schema-Derived Constrained Decoding for MLIR](cards-0003.md#paper-138884) | 从编译器规范生成解码约束 |
| 科学机器学习 | 分布外泛化 | [Cross-Distribution Generalization in Longitudinal Behavioral Data Through Frozen Coherence Constraints](cards-0003.md#paper-150347) | 冻结语义参照约束行为表征 |
| 持续学习 | 提示适配 | [Cross-Domain Knowledge Separation and Positive Transmission for Noisy Domain Incremental Learning](cards-0003.md#paper-152725) | 隔离领域知识后只迁移可靠部分 |
| 可解释性 | 跨模型探针 | [Cross-Family Universality of Behavioral Axes via Anchor-Projected Representations](cards-0003.md#paper-153625) | 用共享样本比对行为方向 |
| 统计学习 | 后验估计 | [Cross-Fitting for Neural Posterior Estimation](cards-0003.md#paper-153646) | 用折外残差学习条件不确定性 |
| 生成模型 | 流匹配 | [Cross Flow: One-Step Generation Across Latent and Pixel Spaces](cards-0003.md#paper-151273) | 让低维噪声直接映射到像素 |
| 计算机视觉 | 测试时适配 | [Cross-Foundation Complementary Learning Systems for Continual Test-Time Adaptation in Open-Vocabulary Semantic Segmentation](cards-0003.md#paper-148739) | 分离视觉快更新和语义稳定约束 |
| 计算机视觉 | 监督设计 | [CrossID: Cross-Supervised Spatio-Temporal Gated Fusion for Personalized Portrait Generation](cards-0003.md#paper-150764) | 用交叉监督检验参考身份与描述的解耦 |
| 统计学习 | 评测方差 | [Crossing the Validation crisis: Cross-validation reduces benchmarking variance surprisingly well](cards-0003.md#paper-139193) | 以样本增益判断是否继续增加交叉验证折数 |
| 多模态学习 | 幻觉定位 | [Cross-Layer Evolution Graph Learning for Fine-grained VLM Hallucination Detection](cards-0003.md#paper-150184) | 用跨层轨迹与句级标签定位token异常 |
| 机器人学 | 跨模态蒸馏 | [Cross-Modal Prior-Guided Training with Visual Foundation Models for Unsupervised LiDAR Point Cloud Registration](cards-0003.md#paper-155262) | 训练时借视觉先验指导纯LiDAR配准 |
| 可解释性 | 电路比较 | [Cross-Model Circuit Discovery](cards-0003.md#paper-148536) | 在模型与层的联合字典中找共享电路 |
| 大语言模型 | 缓存复用 | [Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse](cards-0003.md#paper-153772) | 在同族模型切换前验证KV映射误差 |
| 图学习 | 图匹配 | [Cross-order Consensus Graph Matching](cards-0003.md#paper-153663) | 同时建模节点与边对应，并约束两者一致 |
| 大语言模型 | 选择性预测 | [Cross-Question Reliable Reinforcement Learning](cards-0003.md#paper-155202) | 按跨题相对置信度训练拒答 |
| 多模态学习 | 防御校准 | [CrossSteer:Cross-Modal Safety Steering for Audio-Language Models](cards-0003.md#paper-148830) | 比较文本与语音来源的安全表征 |
| Agent | 权限隔离 | [Cross-User Poisoning: User-Task Boundary Failures in Multi-User Collaborative Language Agents](cards-0003.md#paper-148398) | 显式记录用户和任务授权范围 |
| 多模态学习 | 跨模态检索 | [CrossWeave: Emergent Cross-Modal Scene and Instance Retrieval from Sparse 2D-3D Alignment](cards-0003.md#paper-152755) | 用稀疏局部对应监督代替全局标签 |
| 大语言模型 | 适配器合并 | [Crowded in B-Space: Calibrating Shared Directions for LoRA Merging](cards-0003.md#paper-152853) | 合并 LoRA 前校准输出侧共享方向 |
| 表格学习 | 推理检索 | [CRUMB: Efficient Prior Fitted Network Inference via Distributionally Matched Context Batching](cards-0003.md#paper-148277) | 为每组测试样本选择分布匹配的训练上下文 |
| Agent | 提问评测 | [CruxBench: A Benchmark of Information Discovery](cards-0003.md#paper-139175) | 按子问题改变目标判断的程度评分 |
| 科学机器学习 | 结构评测 | [CryoAtlas: A Large Curated Dataset and Unified Benchmark for Cryo-EM Atomic Model Building](cards-0003.md#paper-139015) | 联合检查结构误差、观测一致性与物理有效性 |
| 科学机器学习 | 几何等变 | [CryoGeo: Latent Pose Equivariance for Amortized Ab Initio Cryo-EM Reconstruction](cards-0003.md#paper-149543) | 直接约束模型输出对已知坐标变换的响应 |
| 科学机器学习 | 教师选择 | [CrystalREPA: Transferring Physical Priors from Universal MLIPs to Crystal Generative Models](cards-0003.md#paper-154603) | 用原子表征可分性选择晶体生成教师 |
| Agent | 软件工程评测 | [CSBench: A Comprehensive Benchmark for Evaluating Project-Level System Construction in Computer Science](cards-0003.md#paper-139195) | 将项目构建和算法题通过率分别验收 |
| 图学习 | 图卷积 | [CSCN: The Crossed Subtree Convolutional Network](cards-0003.md#paper-149718) | 用对齐后的子树序列降低对深层消息传递的依赖 |
| 强化学习 | 占用正则 | [CS-DICE: Offline Reinforcement Learning with Coherent Occupancy Regularization](cards-0003.md#paper-153299) | 将正则参考限制为部署策略可表达的经验切片 |
| 生成模型 | 去噪调度 | [CSFlow: Aligning Flow Matching with Human Contrast Sensitivity](cards-0003.md#paper-154473) | 按每一步形成的频带和人类敏感性分配去噪权重 |
| 多模态学习 | 传感对齐 | [CSI-TextBench: A Dataset and Benchmark for Language-Grounded Ambient Sensing Perception](cards-0003.md#paper-139630) | 以分层描述训练非视觉传感输入的开放查询 |
| 生成模型 | 注意力加速 | [CSLA: Sparse-Linear Attention with Learnable Routing and Quantization-aware Training](cards-0003.md#paper-149892) | 以可训练路由代替按权重大小分配注意力分支 |
| 模型安全 | 防御检测 | [CSO-LLM: Class Subspace Orthogonalization for Post-Training Backdoor Detection and Trigger Inversion in LLMs](cards-0003.md#paper-153774) | 区分正常类别特征与可疑模型行为 |
| 机器人学 | 技能强化学习 | [CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization](cards-0003.md#paper-153130) | 先校正技能先验，再按技能裁剪策略更新 |
| 大语言模型 | 反事实评测 | [CTE-Bench: Audited Counterfactual Trace Evaluation for Stateful Software Simulators](cards-0003.md#paper-139020) | 分开报告有真实历史辅助和独立滚动的预测。 |
| 科学机器学习 | 标注策略 | [CT-Lesion: A Multi-Region CT Dataset for Co-existing Lesion Segmentation and Detection](cards-0003.md#paper-139728) | 跨解剖区补充稀有病灶监督。 |
| 多模态学习 | 专家协作 | [CTM-AI: A Blueprint for General AI Inspired by a Model of Consciousness](cards-0003.md#paper-148258) | 跨模态任务中检验动态信息选择是否优于固定专家组合。 |
| 大语言模型 | 持续适配 | [CTRL: Continual Test-Time Reinforcement Learning for Large Language Models](cards-0003.md#paper-153321) | 在持续测试时更新中同时控制伪监督错误和历史梯度干扰。 |
| 生成模型 | 推理缓存 | [CuBic: Curvature-Driven Dynamic Inference Caching for Fast, High-Fidelity Flow Matching](cards-0003.md#paper-149614) | 按流轨迹弯曲程度选择更新频率和空间粒度。 |
| 机器学习系统 | 调试评测 | [CUDABeaver: Benchmarking LLM-Based Automated CUDA Debugging](cards-0003.md#paper-139244) | 验收 GPU 修复时同时检查正确性和性能保留。 |
| 机器学习系统 | 生成评测 | [CUDABench: Benchmarking LLMs for Text-to-CUDA Generation](cards-0003.md#paper-148268) | 把编译、运行语义和硬件效率分层验收。 |
| 大语言模型 | 安全评测 | [CultureRed: Benchmarking Culture-Specific AI Safety Based on Global Statutes](cards-0003.md#paper-139752) | 同时测地区规则下的漏拒与误拒。 |
| 强化学习 | 遗忘策略 | [CURe: Conservative Unlearning with Soft-Gating Regularization for Offline Reinforcement Learning](cards-0003.md#paper-155375) | 保留和删除数据共享支持时按干扰程度调节遗忘。 |
| 大语言模型 | 推理安全 | [CURE: Counterfactual Unsafe-token Re-masking for Diffusion Large Language Model Test-time Alignment](cards-0003.md#paper-151876) | 对扩散解码优先修正局部风险状态。 |
| 推荐系统 | 跨域训练 | [CURE: Coupled User-Grouped Reinforcement Learning for Cross-Domain Recommendation with Non-Overlapping Users](cards-0003.md#paper-151750) | 以同用户的可靠域内信号校准跨域伪标签更新。 |
| 多模态学习 | 半监督适配 | [CURE: Visual Reprogramming of Vision-Language Models under Limited Supervision](cards-0003.md#paper-155870) | 按校准后置信边际使用无标签样本。 |
| 大语言模型 | 安全训练 | [Curriculum Learning for Safety Alignment](cards-0003.md#paper-154369) | 偏好优化时按难度逐步采样并更新参考模型。 |
| 科学机器学习 | 训练策略 | [Curriculum Multiple Shooting for Robust Training of Neural and Universal Differential Equations](cards-0003.md#paper-153849) | 神经微分方程训练合用课程与分段射击。 |
| 大语言模型 | 形式验证 | [Curriculum proof repair with learned counterexamples](cards-0003.md#paper-156100) | 按不变量依赖顺序训练证明失败诊断。 |
| 优化 | 近似理论 | [Curvature Beyond Positivity: Greedy Guarantees for Arbitrary Submodular Functions](cards-0003.md#paper-150081) | 判断含负值的次模目标能否使用贪心。 |
| 优化 | 复杂度下界 | [Curvature-Dependent Lower Bounds for Frank-Wolfe](cards-0003.md#paper-154986) | 区分可行域曲率带来的加速与所用步长规则的极限。 |
| 优化 | 在线学习下界 | [Curvature-Dependent Lower Bounds for Riemannian Online Convex Optimization](cards-0003.md#paper-153902) | 在负曲率空间区分梯度反馈和完整损失反馈。 |
| 优化 | 初始化 | [Curvature-Guided Parameter Initialization for Multi-Task Learning](cards-0003.md#paper-152159) | 对多任务训练先检查初始化敏感性，再比较梯度改造方法。 |
| 多模态 | 拓扑评测 | [CurveBench: A Benchmark for Exact Topological Reasoning over Nested Jordan Curves](cards-0003.md#paper-138987) | 用完整包含树验收视觉推理 |
| 强化学习 | 样本权重 | [CurveRL: Principled Distribution-Aware Context Reweighting for LLM Reasoning](cards-0003.md#paper-149893) | 按通过率分布而非绝对值调整提示权重 |
| 大语言模型 | 推理加速 | [CutAttn: Discovering Cognitive Transition Layers for Efficient Long-Context Prefilling](cards-0003.md#paper-148257) | 在注意力转为集中的层裁剪隐藏状态 |
| 优化 | 资源分配 | [CUVET: A Partitioning Approach for Continuous Treatment Assignment At Scale](cards-0003.md#paper-148338) | 分群后按边际投入产出分配连续预算 |
| 时间序列 | 连续时间预测 | [CVTA: Cross-Variable Temporal Attention for Multivariate Irregular Time Series Prediction](cards-0003.md#paper-152025) | 用紧凑跨变量状态预测异步序列 |
| 图学习 | 检索增强 | [CWAGraph: Retrieving What Was Never Explicitly Identified in Graph-Based RAG](cards-0003.md#paper-149212) | 检索有界规则时显式表示适用范围与例外 |
| 安全评测 | 防御效用 | [CyberDualEval: Measuring Dual-Use Cyber Risks in Frontier Language Models](cards-0003.md#paper-138885) | 分别验证防御回答质量和拒绝校准 |
| 计算机视觉 | 循环监督 | [CyCLeGen: Cycle-Consistent Layout Prediction and Image Generation](cards-0003.md#paper-153270) | 用布局到图像再到布局的一致性作训练信号 |
| 医学影像 | 周期表示 | [CycleSpectra: Cyclic Motion Spectra for Phase-Queryable 4D Cardiac Reconstruction](cards-0003.md#paper-152695) | 用固定周期合成层查询任意相位 |
| 计算机视觉 | 离散扩散 | [Cyclic Discrete Diffusion: A Novel Multi-Class Segmentation Refinement Technique](cards-0003.md#paper-155503) | 在统一多类别标签空间精修分割 |
| 时间序列 | 几何流匹配 | [Cylindrical Geodesic Flow Matching for Quasiperiodic Physiological Signal Transformation](cards-0003.md#paper-155983) | 为周期信号选择尊重相位环绕的插值 |
| 大语言模型 | 权重量化 | [D$^2$Quant: Accurate Low-bit Post-Training Weight Quantization for LLMs](cards-0003.md#paper-151535) | 分别处理降维投影保真和激活均值漂移 |
| 生成模型 | 可微评价 | [D2D: Detector-to-Differentiable Critic for Improved Numeracy in Text-to-Image Generation](cards-0003.md#paper-153310) | 将检测器的计数信号改造为可微指导 |
| 强化学习 | 信用分配 | [DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in Diffusion Language Models](cards-0003.md#paper-148695) | 按去噪进展分配 token 权重并改进似然估计 |
| 安全 | 防御回放 | [DACE: Diversity-Driven Adversarial Co-Evolution for Robust LLM Safety Alignment](cards-0003.md#paper-154329) | 用带不确定度的历史防御反馈降低遗忘 |
| 强化学习 | 离线数据 | [DaCe-DT: Data-Centric Offline Multi-Task Reinforcement Learning via Adaptive Prompts and Trajectory Correction for Heterogeneous Tasks](cards-0003.md#paper-156146) | 按任务复杂度和轨迹质量调整提示和回报 |
| 强化学习 | 算力调度 | [DACE RL for Compute Efficient Reinforcement Learning in Small Model Reasoning](cards-0003.md#paper-151411) | 以训练诊断动态调整 rollout 预算 |
| 视觉学习 | 参数高效适配 | [DAGA: Dynamic Attention-Guided Adaptation for Self-Supervised Vision Transformers](cards-0003.md#paper-153686) | 以注意力质量决定是否开启实例门控。 |
| 科学机器学习 | 图结构正则 | [DAG-Biased Graph Learning for Multimodal Survival on EHR](cards-0003.md#paper-155436) | 用软无环先验约束多模态关系，并保留注意传播。 |
| Agent | 增量规划 | [DAGent: Evaluate-then-Grow Planning for Deep Research Agents](cards-0003.md#paper-150664) | 依据上一轮节点的证据置信度扩展任务图。 |
| 机器学习系统 | 硬件感知搜索 | [Dancing in Fetters: Pareto-Optimal On-Device LLMs under Hardware Constraints](cards-0003.md#paper-151308) | 先以代理损失和目标设备时延筛选架构。 |
| 科学机器学习 | 球面算子 | [Dandelions: A Spherical Flower for Neural Simulation of Planetary Dynamics](cards-0003.md#paper-155531) | 用大圆上的特征运输代替经纬网卷积。 |
| 大语言模型 | 依赖检索 | [DAPS: Dependency-Aware Premise Selection for LLM Theorem Proving](cards-0003.md#paper-148819) | 对形式化证明候选建依赖邻域，并按组学习排序。 |
| 计算机视觉 | 域适配 | [DARE: Dual-Level Adversarial Learning with Domain-Aware Regularization for Whole Slide Image Classification](cards-0003.md#paper-154306) | 分别对齐局部块与全局样本嵌入。 |
| 多模态学习 | 几何融合 | [DarkVGGT: Seeing Through Darkness Using Thermal Geometry without Daylight Tax](cards-0003.md#paper-148595) | 可见光弱时选择性注入热红外几何，保留正常光照表现。 |
| 强化学习 | 变化检测 | [DARLING: Detection Augmented Reinforcement Learning with Non-Stationary Guarantees](cards-0003.md#paper-151097) | 以可检测变化点决定何时重新适配在线策略。 |
| 强化学习 | 残差适配 | [DARPAN: Controllability-Aware Residual Filtering for Pretrained Physical Control](cards-0003.md#paper-152813) | 用动作可影响的残差信号决定在线适配。 |
| 计算机视觉 | 异常表征 | [DART: Domain-Agnostic Residual Transfer for Generalist Anomaly Detection](cards-0003.md#paper-152532) | 把异常参考残差拆成异常与域特异两部分。 |
| 统计学习 | 实验设计 | [DARTS: Targeting Prognostic Covariates in Budget-Constrained Sequential Experiments](cards-0003.md#paper-151821) | 用前批反馈选择后批应购买的协变量。 |
| 大语言模型 | 模型路由 | [DART: Zero-Shot Dual-Side Alignment Routing for LLM Performance-Cost Tradeoffs](cards-0003.md#paper-155299) | 把查询难度和模型能力投影到共同空间以接入新模型。 |
| 大语言模型 | 稀疏注意力 | [DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention](cards-0003.md#paper-151399) | 按查询自适应选择 KV 块，并允许细层梯度返回粗选择。 |
| 图学习 | 序列决策 | [DASM: Dynamic Autoregressive Subgraph Mining via Two-Stage Policy Alignment](cards-0003.md#paper-155623) | 用整轨迹质量监督子图停止边界。 |
| 科学机器学习 | 符号搜索 | [DASS: A Solver-Agnostic Dynamic Auxiliary Search Strategy for Symbolic Regression](cards-0003.md#paper-149310) | 给不同求解器共享一个动态更新的高潜力子空间。 |
| 深度学习 | 注意力度量 | [Data-Adaptive Mahalanobis Metric Learning for Cross-Head Attention in Transformers](cards-0003.md#paper-151478) | 用输入相关的跨头度量替代各头独立相似度。 |
| 统计学习 | 机制设计 | [Data Auctions for Retrieval Augmented Generation](cards-0003.md#paper-154287) | 在专属分配的 RAG 数据拍卖中兼顾近似效率与激励相容。 |
| 多模态学习 | 数据配比 | [DataComp-VLM: Improved open datasets for Vision-Language Models](cards-0003.md#paper-138991) | 固定预算对照混合与过滤，并随模型规模扫描。 |
| 大语言模型 | 训练正则 | [Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws](cards-0003.md#paper-149999) | 有限语料下独立比较掩码辅助监督与单纯增强权重衰减。 |
| 计算机视觉 | 数据配比 | [Data Density Scaling Laws for Image Self-Distillation](cards-0003.md#paper-150410) | 固定训练步数扫描唯一图像和重复次数，按域拟合响应。 |
| 学习理论 | 机制诊断 | [Data Diversity Drives the Emergence of Symbolic Mechanisms Supporting Abstract Reasoning](cards-0003.md#paper-155264) | 验证新推理机制时控制训练多样性再比较架构。 |
| 因果推断 | 协变量选择 | [Data-Driven Covariate Selection for Nonparametric and Cycle-Agnostic Causal Effect Estimation](cards-0003.md#paper-155410) | 存在反馈时，先验证局部调整条件再决定是否需要估计全图。 |
| 科学机器学习 | 软标注 | [Data-Driven Soft Labeling Scales DNA Read Classification to Whole-Body Cell-Type Deconvolution](cards-0003.md#paper-150257) | 多类弱监督中比较软标签与硬标签对校准和聚合误差的影响。 |
| 机器学习基础 | 约束推理 | [Data-Efficient Learning for Constraint Satisfaction Problems via  Relational Biases and Hard Axiom Clamping](cards-0003.md#paper-150335) | 将不可改变量从自由预测中分离，并检验每轮钳制的收益。 |
| 大语言模型 | 数据评测 | [DataFlex: A Unified Benchmark and Evaluation Platform for Data-Centric Training of Large Language Models](cards-0003.md#paper-139364) | 评测数据算法时统一训练协议并按模型尺寸及资源域分别报告。 |
| 可解释性 | 指标诊断 | [Data-Free Metrics Are Not Invariant Under Functionality-Preserving Reparametrisations](cards-0003.md#paper-152919) | 用函数等价模型做指标不变性测试，再将指标用于压缩选层。 |
| 持续学习 | 在线分类 | [Data-Free Reservoir Features for Efficient Long-Horizon Cold-Start Continual Learning](cards-0003.md#paper-154499) | 在极少初始数据时加入随机固定特征加在线头作为低成本对照。 |
| 医学影像 | 数据审计 | [Dataset Collections: Challenges of Large-Scale Data Aggregation in 3D Medical Image Datasets](cards-0003.md#paper-139023) | 合并公共数据时保留来源图，并按原始来源核查训练测试交叉。 |
| 计算机视觉 | 数据蒸馏 | [Dataset Distillation via Drifting](cards-0003.md#paper-155633) | 用冻结骨干的训练贡献筛小数据，并检查换骨干后的收益。 |
| 强化学习 | 采样优化 | [Dataset Mismatch Matters in Group Relative Policy Optimization for Reinforcement Learning from Verifiable Rewards](cards-0003.md#paper-151119) | 目标数据不可共享时，可用汇总验证信号更新源任务分配。 |
| 大语言模型 | 解码调度 | [DAWN: Dependency-Aware Fast Inference for Diffusion LLMs](cards-0003.md#paper-153138) | 在同质量预算下对照按置信度和按依赖结构批量解码。 |
| 科学机器学习 | 概率传输 | [DBPS: Doob-Bridge Posterior Sampler with Balanced Endpoint-Population Control for Unpaired Neurodegenerative Pathology Transport](cards-0003.md#paper-154080) | 无配对传输中扫描个体与总体引导权重并保留两个边界基线。 |
| 计算机视觉 | 动态计算 | [DC-DiT: Adaptive Compute and Elastic Inference for Visual Generation via Dynamic Chunking](cards-0003.md#paper-148857) | 比较按内容及时间步压缩与固定 token 预算的质量计算曲线。 |
| 科学机器学习 | 时空压缩 | [DC-Ocean: Deep Latent Compression for Global High-Resolution Ocean Forecasting](cards-0003.md#paper-152997) | 分别报告近边界和远场误差，并测压缩对滚动预报的影响。 |
| 生成模型 | 图像压缩 | [DC-SAE: Deep Compression Semantic Autoencoder for Faster Diffusion Convergence](cards-0003.md#paper-152595) | 在固定潜空间大小下对照单语义编码与保留像素支路。 |
| 软件安全 | 防御审计 | [DCVD: Dual-Channel Cross-Modal Fusion for Joint Vulnerability Detection and Localization](cards-0003.md#paper-152806) | 为授权代码审计分别测全局检出与定位质量，保留人工确认。 |
| 计算机视觉 | 通道建模 | [DC-ViT: Modulating Spatial and Channel Interactions for Multi-Channel Images](cards-0003.md#paper-150507) | 对照共享注意力和解耦交互，按通道组合报告稳健性。 |
| 多智能体学习 | 通信调度 | [DDACOM: Dual-Decoupled Adaptive Communication for Multi-Agent Reinforcement Learning under Dynamic Networks](cards-0003.md#paper-154024) | 在波动带宽下分别评估消息价值和发送策略，以同字节预算比较。 |
| Agent/评测 | 配对诊断 | [DDBench: A Benchmark for Agentic Debugging on Distributed Systems](cards-0003.md#paper-138907) | 对同一分布式故障配对提供运行证据 |
| 视觉/可解释性 | 最小充分集 | [DD-CAM: Minimal Sufficient Explanations for Vision Models Using Delta Debugging](cards-0003.md#paper-151520) | 用最小充分激活集合生成热图 |
| 视觉 | 流形度量 | [DDGE: Disentangled Dirichlet Geodesic Evaluation for Robust Few-Shot Learning](cards-0003.md#paper-151036) | 噪声少样本中比较密度感知测地线与平直距离 |
| 视觉 | 跨视角蒸馏 | [DDMS: Discriminative Distillation of Multi-view Foundational Features into Single-view Models](cards-0003.md#paper-148341) | 让单视角学生学习多视角几何，同时保留局部判别性 |
| 视觉/数据 | 蒸馏审计 | [DD-Ranking: Rethinking the Evaluation of Dataset Distillation](cards-0003.md#paper-139355) | 锁定评估阶段软标签与增强来比较蒸馏图像 |
| 多模态/医疗 | 轨迹评测 | [DDx-TRACE: A Benchmark for Medical Diagnostic Trajectories in VLMs](cards-0003.md#paper-139550) | 隐藏证据并逐步检验系统何时索取、更新和停止 |
| 强化学习/系统 | 约束调度 | [Deadline-Constrained Dynamic Workflow Scheduling Can be Cast as a Representation Learning Problem](cards-0003.md#paper-151183) | 先筛选截止风险再优化资源成本 |
| Agent | 行为评测 | [DEBATE: A Large-Scale Benchmark for Evaluating Opinion Dynamics in Role-Playing LLM Agents](cards-0003.md#paper-139011) | 将群体信念变化和下一消息质量分别衡量 |
| 因果学习 | 反事实生成 | [Debiased Counterfactual Generation via Flow Matching from Observations](cards-0003.md#paper-149078) | 从观察分布学习去混杂变换 |
| 生成模型 | 偏好去偏 | [Debiased DPO for Diffusion Models](cards-0003.md#paper-149883) | 合成人类偏好代理标签应先校正再融入DPO |
| 统计学习 | 随机投影 | [Debiasing Random Oblique Projections for Subsampled OLS and Fast CUR in High Dimensions](cards-0003.md#paper-149261) | 对子采样伪逆导致的偏差做独立校正 |
| 统计学习 | 草图去偏 | [Debiasing Sketched Ridge Regression: A Functional Estimation Perspective](cards-0003.md#paper-149463) | 使用多草图线性聚合消除岭估计低阶偏差 |
| 优化 | 分布式训练 | [Decentralized $\mu^2$-SGD: Narrowing the Parallelism Gap to Centralized Learning](cards-0003.md#paper-149890) | 根据通信图选择并行度和分布式优化器 |
| 大语言模型 | 概率集成 | [Decentralized Aggregation of LLM Predictions via Wagering Mechanisms](cards-0004.md#paper-150523) | 用相对于留一集成的预期得分优势加权 |
| 学习理论 | 耦合动力学 | [Decentralized Coupled Representation Learning](cards-0004.md#paper-151009) | 设计局部表征学习时检查快慢尺度与谱隙 |
| 强化学习/规划 | 多智能体路径 | [Decentralized Multi-Goal Multi-Agent Pathfinding with Spatial Prior and Neighbor Intent Prediction](cards-0004.md#paper-151866) | 联合安排目标次序以降低局部避碰压力 |
| 强化学习 | 分散式探索 | [Decentralized Q-Learning in Markov Potential Games](cards-0004.md#paper-155245) | 根据折扣访问频率调节平滑最优响应 |
| 分布式学习 | 排序聚合 | [Decentralized Ranking Aggregation via Gossip: Convergence and Robustness](cards-0004.md#paper-151288) | 在节点间传递排序信息求共识 |
| 检索增强 | 归因诊断 | [Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation](cards-0004.md#paper-152927) | 独立检查证据与被查询实体是否一致 |
| 神经信号分析 | 主动采集 | [Decide Before You Record: Heterogeneity-Guided Pre-Acquisition Stimulus Selection for Cross-Day Neuroprostheses](cards-0004.md#paper-149170) | 采集校准信号前按跨日异质性选择刺激 |
| 因果学习 | 目标加权 | [Decision-Aware Proximal Bridge Learning for Optimal Treatment Selection](cards-0004.md#paper-155924) | 按决策相关动作区域分配因果拟合权重 |
| 强化学习 | 可微规划 | [Decision-Focused Learning in MDPs: An Occupancy Measure Approach](cards-0004.md#paper-149225) | 在预测动力学时通过占用测度规划反传 |
| 优化 | 情景生成 | [Decision Focused Scenario Learning for Contextual Stochastic Programming](cards-0004.md#paper-151045) | 按决策质量而非仅按分布拟合选择情景 |
| 可解释性 | 因果路径 | [Decision Path Tracing for Causal Analysis in Transformers](cards-0004.md#paper-153801) | 用干预后自修复差异检查路径是否承载决策 |
| 大语言模型 | 推理诊断 | [Decoding the Critique Mechanism in Large Reasoning Models](cards-0004.md#paper-154405) | 同时测错误中间步骤与最终恢复 |
| 生成模型 | 分阶段优化 | [DecompDreamer: A Composition-Aware Curriculum for Structured 3D Asset Generation](cards-0004.md#paper-156777) | 先定对象关系再细化部件 |
| 多模态学习 | 验证器 | [Decomposed Graded Verifier for Generative World Modeling](cards-0004.md#paper-152463) | 把复杂目标拆成可评分子项 |
| 多模态学习 | 分解表征 | [Decomposed Representations Mitigate the Alignment–Specificity Trade-off in Multi-Omics](cards-0004.md#paper-149003) | 独立保留共享、私有及融合信息 |
| 生成模型 | 推理蒸馏 | [Decompose the Distillation: Interpretable Single-Pass Guidance for Diffusion Models](cards-0004.md#paper-152875) | 单次前向保留可独立调节的引导方向 |
| 大语言模型 | 扩展律诊断 | [Decomposing and Reshaping Scaling Laws through Token Learning Times](cards-0004.md#paper-152417) | 追踪单 token 学习时间解释总体损失变化 |
| 统计学习 | 归因校准 | [Decomposing Conformal Uncertainty: Calibration- and Instance-Driven Feature Attribution](cards-0004.md#paper-149998) | 分别归因校准样本与测试实例的区间宽度 |
| 科学机器学习 | 空间解释 | [Decomposing Earth Embeddings with Sparse Autoencoders](cards-0004.md#paper-150168) | 用地理一致性和标签恢复评估地球表示分解 |
| 因果学习 | 架构选择 | [Decomposing Effects in Neural Causal Models](cards-0004.md#paper-151693) | 把因果图固定后比较子机制的参数共享 |
| 可解释性 | 表示几何 | [Decomposing how prompting steers behavior](cards-0004.md#paper-153074) | 比较哪种低复杂度映射解释提示变化 |
| 学习理论 | 训练动力学 | [Decomposing SGD Dynamics in Neural Networks: Teacher-Induced Spikes and Variance Inflation](cards-0004.md#paper-149560) | 检查无关子空间方差再决定是否冻结 |
| 机器学习系统 | 概率预测 | [Decomposing Temporal and Job-Induced Dynamics for Probabilistic Computing Workload Forecasting via Graph-Conditioned Dual-Branch Diffusion](cards-0004.md#paper-152921) | 引入随调度变化的机器依赖预测负载 |
| 神经科学 | 低秩建模 | [Decomposing the modulation of interactions between neuronal populations](cards-0004.md#paper-152282) | 用三方低秩交互分析条件变化 |
| 机器学习 | 主动学习 | [Deconstructing Multi-Task Active Learning: The Paradox of Gradient Conflict and Orthogonal Decomposition](cards-0004.md#paper-153116) | 采集冲突样本，更新时再消解冲突 |
| 计算机视觉 | 奖励设计 | [DeCoRL: Decomposed Consistency Reinforcement Learning for Multi-Image Composition](cards-0004.md#paper-148478) | 把多图一致性奖励拆成对象级信号 |
| 具身智能 | 主动感知 | [Decoupled Complementary Fields on 3D Gaussian Maps for Embodied Navigation and Reasoning](cards-0004.md#paper-149572) | 区分待验证证据与可执行导航条件 |
| 优化 | 训练诊断 | [Decoupled Descent: Exact Test Error Tracking Via Approximate Message Passing](cards-0004.md#paper-152459) | 比较数据复用偏差修正与普通梯度下降 |
| 多模态学习 | 提示学习 | [Decoupled Mode Connectivity for Base-to-Novel Generalization in Vision-Language Models](cards-0004.md#paper-150180) | 分开学习基础类专门化与未见类保持提示 |
| 半监督学习 | 训练策略 | [Decoupled Optimization for Teacher-Student Semi-Supervised Learning via a Pioneer Student](cards-0004.md#paper-149914) | 用独立学生支路减少参数和梯度耦合 |
| 多模态学习 | 检索表征 | [Decoupled Prototype Contrastive Alignment Hashing for Cross-Modal Retrieval](cards-0004.md#paper-151599) | 分别约束语义和哈希空间，再单独对齐原型 |
| 生成模型 | 安全防护 | [Decoupled Safety Control: A Safety-Control Algorithm for Training-Free Safety Guidance](cards-0004.md#paper-151316) | 把当前生成状态与安全目标分开用于防护 |
| 计算机视觉 | 视频生成 | [Decoupling Action from Egocentric Observation for World Simulation](cards-0004.md#paper-152818) | 按去噪阶段分别维持结构和修正局部对应 |
| 语音 / Agent | 强化学习 | [Decoupling Conversational Dynamics in Full-Duplex Spoken Models through Reinforcement Learning](cards-0004.md#paper-151800) | 将何时讲话单独作为强化学习目标 |
| 计算机视觉 | 图像恢复 | [Decoupling Direction and Magnitude: Language-Steered Flow Matching for Super-Resolution in the Dark](cards-0004.md#paper-149168) | 为不同图像位置选不同恢复步长 |
| 强化学习 | 探索 | [Decoupling Exploration and Policy Optimization: Uncertainty Guided Tree Search for Hard Exploration](cards-0004.md#paper-154428) | 先独立探索，再蒸馏可部署策略 |
| 强化学习 | 价值估计 | [Decoupling is the Key: Scaling Deep Value Networks in Reinforcement Leanring](cards-0004.md#paper-149216) | 加深价值网络前检查目标耦合 |
| 机器学习 | 联邦学习 | [Decoupling Label Shift and Surrogate Gradient Errors for Robust Federated Spiking Neural Networks](cards-0004.md#paper-154393) | 先修正客户端发放阈值再对齐统计量 |
| 强化学习 | 风险建模 | [Decoupling Time and Risk: Risk-Sensitive Reinforcement Learning with General Discounting](cards-0004.md#paper-150052) | 独立定义时间偏好与回报风险偏好 |
| 计算机视觉 | 表征学习 | [DecQ: Detail-Condensing Queries for Enhanced Reconstruction and Generation in Representation Autoencoders](cards-0004.md#paper-152326) | 冻结视觉骨干，用少量查询侧路传递细节 |
| 计算机视觉 | 防御评测 | [DEDCA: Test-Time Adaptation for Generalized AI-Generated Image Detection](cards-0004.md#paper-151979) | 用检测证据间的分歧引导无标签适配 |
| 多模态学习 / 医学 | 证据路由 | [DeepArrhythmia: Segment-Contextualized ECG Arrhythmia Classification via Selective Evidence Acquisition](cards-0004.md#paper-150425) | 按段级置信度决定是否增加诊断证据 |
| 统计学习 | 最优传输 | [Deep Barycentric Regression for Optimal Transport Map Estimation and its Statistical Optimality](cards-0004.md#paper-151777) | 用离线传输规划生成回归目标 |
| 强化学习 | 价值估计 | [Deep Double Q-learning](cards-0004.md#paper-153820) | 对照双估计器训练 |
| 统计学习 | 不确定性分解 | [Deep Ensembles for Epistemic Uncertainty: A Frequentist Perspective](cards-0004.md#paper-155011) | 拆开数据变化与训练随机性 |
| 计算机视觉 | 防御评测 | [DeepfakeGenome: Toward Next-Generation Deepfake Attribution](cards-0004.md#paper-139410) | 用检索评估未知来源归因 |
| 概率建模 | 图结构推断 | [Deep Gaussian Processes on Directed Acyclic Graphs](cards-0004.md#paper-155757) | 保留各层观测及拓扑依赖 |
| 统计学习 | 结构化后验 | [Deep Generative Models for Phylogenetic Inference with Complex Evolutionary Processes](cards-0004.md#paper-151547) | 对比不同构造顺序的离散树生成 |
| 统计学习 | 方差估计 | [Deep Heteroskedastic Regression: Post-Hoc Variance Estimation from Latent Representations](cards-0004.md#paper-151494) | 冻结均值预测器后单独拟合方差 |
| 科学机器学习 | 动力学辨识 | [Deep-Koopman-KANDy: Dictionary Discovery for Deep-Koopman Operators with Kolmogorov-Arnold Networks for Dynamics](cards-0004.md#paper-152578) | 训练完再选择符号读出字典 |
| 学习理论 | 特征学习 | [Deep Learning as Neural Low-Degree Filtering: A Spectral Theory of Hierarchical Feature Learning](cards-0004.md#paper-151589) | 用逐层低阶相关解释早期特征形成 |
| 科学机器学习 | 湍流闭合 | [Deep Learning-based Algebraic Reynolds Stress Closures for RANS simulations of Turbulent Flows](cards-0004.md#paper-151498) | 在求解器内训练物理结构化闭合 |
| 可解释性 | 表征探针 | [Deep Minds and Shallow Probes](cards-0004.md#paper-152977) | 按坐标变换不变性选择探针 |
| 计算机视觉 | 软监督 | [Deep Probabilistic Supervision for Image Classification](cards-0004.md#paper-148229) | 从模型预测估计样本级目标分布 |
| Agent | 推理组织 | [Deep Reasoning in General Purpose Agents via Structured Meta-Cognition](cards-0004.md#paper-153616) | 按任务动态构造可执行推理结构 |
| 大语言模型 | 奖励设计 | [Deep Research as Rubric](cards-0004.md#paper-153645) | 由外部证据构造可验证评分项 |
| 机器学习基础 | 约束学习 | [DeepVoting: Learning and Improving Voting Rules with Fine-Tuning](cards-0004.md#paper-155301) | 用公理损失微调既有投票规则 |
| 强化学习 | 表征适配 | [Default Feature Representations of the Cognitive Map](cards-0004.md#paper-154918) | 固定状态特征，仅更新环境算子 |
| Agent | 运行时防护 | [Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents](cards-0004.md#paper-152017) | 对敏感动作做任务边界检查 |
| 可靠性 | 运行范围建模 | [Defining Operational Conditions for Safety-Critical AI-Based Systems from Data](cards-0004.md#paper-151160) | 从数据估计运行域，再对照采样覆盖 |
| 生成模型 | 密集奖励 | [DeFlowCritic: Dense Latent Reward Alignment for Text-to-Image Flow Matching Models](cards-0004.md#paper-154436) | 在中间潜变量提供评价而非只评价最终图像 |
| 强化学习 | 离线策略提取 | [DeFlow: Decoupling Behavior-Prior Modeling and Value Maximization for Offline Policy Extraction](cards-0004.md#paper-155920) | 保留生成先验并用残差改进动作 |
| 计算机视觉 | 几何重建 | [Deformable 2D Gaussian Splatting](cards-0004.md#paper-153737) | 让表面基元适应尖边 |
| 具身智能 | 示范增强 | [DeformGen: Dynamics-Based Topology Augmentation for Deformable Manipulation Policy Learning](cards-0004.md#paper-149334) | 按真实形变扩充状态及配套动作 |
| 科学机器学习 | 世界模型 | [DeformMaster: An Interactive Physics-Neural World Model for Deformable Objects from Videos](cards-0004.md#paper-152675) | 将物理滚动与神经残差结合 |
| 科学机器学习 | 表征解耦 | [DEFT: Disentanglement-Enhanced Fine-Tuning for EEG Foundation Models](cards-0004.md#paper-149268) | 分类只使用任务相关分支 |
| 计算机视觉 | 深度重建 | [DegBins: Degradation-Driven Binning for Depth Super-Resolution](cards-0004.md#paper-150704) | 用随退化变化的离散区间预测深度残差 |
| 计算机视觉 | 自监督 | [DeGlare: Self-Supervised Specular Removal for Industrial Metallic Surfaces via Multi-Illumination Priors](cards-0004.md#paper-153930) | 利用同位置多光照代替像素真值 |
| 计算机视觉 | 迭代架构 | [Déjà View: Looping Transformers for Multi-View 3D Reconstruction](cards-0004.md#paper-154303) | 用共享迭代块替代独立解码层 |
| 强化学习 | 状态抽象 | [Delayed homomorphic reinforcement learning for environments with delayed feedback](cards-0004.md#paper-155078) | 折叠延迟反馈造成的控制冗余状态 |
| 科学机器学习 | 时序检测 | [Delay-Embedded Representations for Robust Saccade Classification in Noisy Oculographic Signals](cards-0004.md#paper-150466) | 先用延迟窗口聚类召回候选，再做约束拟合 |
| 强化学习 | 策略梯度 | [Delightful Distributed Policy Gradient](cards-0004.md#paper-155678) | 过滤离策略样本时联合考虑优势和惊讶度 |
| 计算机视觉 | 图像编辑 | [Delta-Adapter: Scalable Exemplar-Based Image Editing with Single-Pair Supervision](cards-0004.md#paper-153315) | 以语义变分代替双配对编辑监督 |
| 优化 | 动量 | [DeltaMomentum: A Key-Value based Anisotropic Momentum Update via Delta Rule](cards-0004.md#paper-151284) | 用输入相关遗忘代替统一衰减 |
| 多模态学习 | 蒸馏数据 | [DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation](cards-0004.md#paper-153494) | 按教师学生答案分布差筛蒸馏题 |
| 生成模型 | 弱监督 | [DELTA: Robustly Training Label-Conditional Diffusion Models with Weak Annotations](cards-0004.md#paper-155940) | 将真实类别作为潜变量联合恢复 |
| 自然语言处理 | 语音推理 | [DELTA-TTS: Adapting Autoregressive Model into a Diffusion Language Model for Text-to-Speech](cards-0004.md#paper-151215) | 冻结语音自回归骨干并转并行扩散 |
| 多模态学习 | 时空监督 | [DELTAVID: Enhancing Fine-Grained Spatiotemporal Perception with Cross-Video Differences](cards-0004.md#paper-152418) | 用双视频局部差异构造可验监督 |
| 优化 | 多任务学习 | [Delve into the Applicability of Advanced Optimizers for Multi-Task Learning](cards-0004.md#paper-149197) | 在实际含动量的更新上测梯度去冲突 |
| Agent | 课程学习 | [Democratizing Tool Learning with Environments Fully Simulated by a Free 8B Language Model](cards-0004.md#paper-153684) | 评估本地小模型模拟环境能否支持工具学习 |
| 统计学习 | 公平性 | [Demographic parity in regression and classification within the unawareness framework](cards-0004.md#paper-156660) | 检查分类决策集嵌套性再复用公平回归 |
| 视觉生成 | 推理引导 | [Demystifying Classifier-Free Guidance for Auto-Regressive Image Generation](cards-0004.md#paper-152530) | 以条件差分削弱重复并复用注意力。 |
| 语言模型 | 数值稳定 | [Demystifying Numerical Errors in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL](cards-0004.md#paper-155629) | 针对内核边界误差提高精度。 |
| 优化 | 频谱诊断 | [Denoise First, Orthogonalize Later: Understanding Momentum in Muon via Spectral Filtering](cards-0004.md#paper-155576) | 在 Muon 正交化前做动量滤波。 |
| 学习理论 | 距离去噪 | [Denoising Distances in Metric Measure Spaces](cards-0004.md#paper-151878) | 按精度需求选择高效或高成本距离估计。 |
| 统计学习 | 变分推断 | [Denoising Implicit Variational Inference](cards-0004.md#paper-154041) | 直接学边缘分数来替代内层采样。 |
| 具身智能 | 动作去噪 | [Denoising-Time Heterogeneity in VLA Action Generation: A Controlled Study via Step-Wise Expert](cards-0004.md#paper-151512) | 用正反日程检验专家何时有用。 |
| 语言模型 | 扩散采样 | [Denoising Time Matters: Diverse Generation in Diffusion Language Models](cards-0004.md#paper-154837) | 早期增加语义分支，后期退火扰动。 |
| 语言模型 | 蒸馏 | [Dense Cross-Tokenizer Distillation via Semantic Optimal Local Alignment](cards-0004.md#paper-153427) | 用局部语义传输对齐不同词表的密集分布。 |
| 计算机视觉 | 光流匹配 | [Dense Flow from Adaptive Correspondence](cards-0004.md#paper-153814) | 让匹配单元随图像内容改变。 |
| 模型压缩 | 结构剪枝 | [Dense Structural Compression of Transformers via Gauge-Correct Channel Removal](cards-0004.md#paper-149337) | 剪除相乘因子通道前校正重参数化偏差。 |
| 统计学习 | 决策委派 | [Density-Ratio Losses for Post-Hoc Learning to Defer](cards-0004.md#paper-154375) | 用模型与专家的理想分布密度比设委派阈值。 |
| 语言模型 | 并行解码 | [Dependency-Guided Parallel Decoding in Discrete Diffusion Language Models](cards-0004.md#paper-151486) | 按位置依赖选并行解掩码集合。 |
| 语言模型 | 记忆评测 | [Deployment-Memory LLM Test-Time Training Should Require Behavioral Evidence Beyond Perplexity](cards-0004.md#paper-140012) | 用移除支持上下文后的行为验证记忆。 |
| 机器人学 | 在线模仿 | [Deployment-Time Online Imitation Learning from Corrective Demonstrations](cards-0004.md#paper-154654) | 用无历史存储的增量回归吸收专家纠正。 |
| 计算机视觉 | 深度评测 | [Depth2Pose: A Pose-Based Benchmark for Monocular Depth Estimation without Ground-Truth Depth](cards-0004.md#paper-139479) | 用相机相对位姿检测深度对几何任务的效用。 |
| 语言模型 | 无损解码 | [Depth Exploration for LLM Decoding](cards-0004.md#paper-152407) | 并行探索多个深度并由全深度模型验证。 |
| 语言模型 | 缓存共享 | [DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction](cards-0004.md#paper-152636) | 用浅中层配对重建深层 KV，改变梯度路径。 |
| 计算机视觉 | 几何监督 | [DepthMaster: Unified Monocular Depth Estimation for Perspective and Panoramic Images](cards-0004.md#paper-149698) | 以重叠透视块和对应一致性统一全景深度。 |
| 语言模型 | 深度循环 | [Depth-Recurrent Attention Mixtures: Giving Latent Reasoning the Attention it Deserves](cards-0004.md#paper-150663) | 用序列、深度和专家注意力共用单层循环。 |
| 语音识别 | 参数共享 | [Depth through Recurrence: Towards Ultra-Efficient On-Device ASR](cards-0004.md#paper-149074) | 依据层表示相似度选择可复用的循环块。 |
| 科学机器学习 | 导数监督 | [Derivative-Informed Training of Neural Operators On-the-Fly via Sketched Tangent Consistency](cards-0004.md#paper-152655) | 用在线切线残差代替离线导数标签 |
| 科学机器学习 | 状态表示 | [Derived Fields Preserve Fine-Scale Detail in Budgeted Neural Simulators](cards-0004.md#paper-152570) | 固定存储预算时优先选携带的物理状态 |
| 优化 | 超参缩放 | [Deriving Hyperparameter Scaling Laws via Modern Optimization Theory](cards-0004.md#paper-154887) | 据预算联调批量、动量和学习率 |
| 强化学习 | 监督设计 | [Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL](cards-0004.md#paper-153178) | 独立验收训练监控器的实际风险抑制效果 |
| 多模态学习 | 数据归因 | [Designing Kernel Surrogate Models for Multimodal Attribution](cards-0004.md#paper-154581) | 用非加性代理衡量样本间的模态互补 |
| 生成模型 | 扩散强化学习 | [Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space View](cards-0004.md#paper-155438) | 把前向匹配与反向轨迹更新放在同一方差对照中 |
| 多模态学习 | 空间编码 | [Despa: Resolving Spatial Collapse in VLMs via Depth-Grounded Geometry](cards-0004.md#paper-155220) | 将深度几何写入视觉位置编码 |
| 计算机视觉 | 蒸馏 | [DetailAnywhere: Fashion Detail Generation via Cross-Modal Feature Alignment Distillation](cards-0004.md#paper-151134) | 在局部细节生成中蒸馏参考和目标双分支 |
| 计算机视觉 | 信用分配 | [Detect Anything in Graphic Design: Element-Level Rewards for Autoregressive Detection](cards-0004.md#paper-150451) | 按图层顺序解码并按元素给奖励 |
| 时间序列 | 诊断评测 | [Detect, Explain, Interpret: An End-to-End Benchmark for Time Series Anomaly Detection, Explainability and Interpretability.](cards-0004.md#paper-139119) | 分开度量告警正确、维度归因与语义解释 |
| 机器学习系统 | 防御评测 | [Detecting Hidden ML Training With Zero-Overhead Telemetry](cards-0004.md#paper-155937) | 分开报告常规与未知 GPU 工作负载的监测准确率 |
| 大语言模型 | 污染诊断 | [Detecting RLVR Training Data via Structural Convergence of Reasoning](cards-0004.md#paper-155181) | 在已知训练集划分上检查推理输出多样性是否收缩 |
| 统计学习 | 风险校准 | [Detection and Classification in Latent Spaces: High-Dimensional Analysis and Validation](cards-0004.md#paper-150861) | 按潜维度和样本比率校准误报和漏检 |
| 计算机视觉 | 防御检测 | [DetectViT: Test-time Backdoor Detection for Vision Transformers via Inter-Head Attention Discrepancy](cards-0004.md#paper-151934) | 用头间注意模式做外部视觉权重的运行时审计 |
| 多模态学习 | 空间指代 | [Detect What You Need: Chain-of-Causal Reasoning for 3D Intent Grounding](cards-0004.md#paper-153726) | 先把抽象意图拆成功能要求再选三维物体 |
| 科学机器学习 | 噪声建模 | [DETS: An Interval-Censored Evidential Sampling Framework for Cross-Domain Scientific Discovery](cards-0004.md#paper-148978) | 对有容差的观测拟合区间质量 |
| 多模态学习 | 训练课程 | [Developmental Visual Experience Scaffolds Grounded Concept Acquisition in Vision-Language Models](cards-0004.md#paper-148931) | 先呈现低频和弱色彩信号再恢复清晰图像 |
| 具身智能 | 仿真迁移 | [DexMirror: Real-to-Sim Scene Mirroring for Sim-to-Real Dexterous Manipulation](cards-0004.md#paper-153302) | 把机器人与重建场景的对齐误差作为独立验收量 |
| 具身智能 | 位姿估计 | [DexOPE: 6D Object Pose Estimation in Dexterous Manipulation](cards-0004.md#paper-151955) | 遮挡时保留多峰位姿并用接触约束筛选 |
| 具身智能 | 无监督技能 | [Dexterous Skill Discovery via Topology-Aware Wasserstein Dependency](cards-0004.md#paper-154902) | 按物体位姿变化而非机械手自身运动衡量技能多样性 |
| 计算机视觉 | 数据增强 | [D-GAP: Improving Out-of-Domain Robustness via Dataset-Agnostic and Gradient-Guided Augmentation in Amplitude and Pixel Spaces](cards-0004.md#paper-153375) | 根据任务梯度选择扰动频段和像素 |
| 强化学习 | 风险控制 | [DGRAF: Observation-Quality-Aware Reinforcement Learning for Dynamic Reconfigurable Batteries](cards-0004.md#paper-155974) | 让决策保守度随缺失观测的重建质量变化 |
| 计算机视觉 | 视频适配 | [DiA: Directional Adapter](cards-0004.md#paper-148763) | 分别建模动作发生前和发生后的线索 |
| Agent / 软件工程 | 评测诊断 | [DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents](cards-0004.md#paper-151898) | 软件交互失败后，根据历史定位可区分评测器失误和功能缺陷的检查 |
| 科学机器学习 | 球面神经算子 | [DIAGNO: Diagonal Spherical Neural Operators for Heterogeneous Earth Dynamics Modeling](cards-0004.md#paper-154008) | 容许球面频域模态交换以表示地球空间异质性 |
| 多模态学习 | 证据诊断 | [Diagnosing and Correcting Bias in MLLM for Long Video Understanding](cards-0004.md#paper-154288) | 把完整视频、仅问题和局部显著片段作为证据对照 |
| 多模态学习 | 鲁棒评测 | [Diagnosing and Mitigating Modality Interference in Multimodal Large Language Models](cards-0004.md#paper-153711) | 只改变与任务无关的模态来测模态干扰 |
| 多模态学习 | 视觉依赖诊断 | [Diagnosing and Repairing Visual Collapse in Compact Medical Multimodal LLMs](cards-0004.md#paper-149438) | 用视觉与文本残差的独立消融判断模型是否真的使用图像 |
| 大语言模型 | 规则诊断 | [DiagnosticIQ: A Benchmark for LLM-Based Industrial Maintenance Action Recommendation from Symbolic Rules](cards-0004.md#paper-139853) | 用配对改写检测模型是否稳定依据符号规则作判断 |
| 学习理论 | 优化动力学 | [Diagonalizing the Softmax: Hadamard Initialization for Tractable Cross-Entropy Dynamics](cards-0004.md#paper-152327) | 用结构化初始化剥离交叉熵训练中特有的耦合 |
| 大语言模型 | 结构化奖励 | [DiagSQL: A Diagnostic Validator for Text-to-SQL with Reward Allocation and Co-occurrence Shaping](cards-0004.md#paper-155455) | 对结构化验证输出按组成部分分配信用 |
| Agent | 推理预算 | [DialBandit: Adaptive Sequential Search with Tunable Evaluation Fidelity](cards-0004.md#paper-149867) | 在级联中联合选择查询模型、评估精度和停止时机 |
| 语音 | 低资源增强 | [Dialect ASR based on Multi-View Pseudo-Parallel Augmentation and Noise-Robust Contrastive Learning](cards-0004.md#paper-155164) | 用伪平行多视图和分层对比学习区分共享语义与方言 |
| 自然语言处理 | 方言数据 | [DialectLLM: A Dialect-Aware Dialog[ue] Generation Framework Beyond Standard American English](cards-0004.md#paper-153135) | 对用户话语和助手回答分别选择方言特征 |
| Agent / 安全 | 防御评测 | [DIBench: Benchmarking Decision Integrity of GUI-based Mobile Agents Under Deceptive Injections](cards-0004.md#paper-139390) | 单独核验移动代理的选择是否满足指令约束 |
| Agent / 教育 | 反事实评测 | [DICE: Decoupling Capability from Intervention Necessity in LLM Tutoring](cards-0004.md#paper-151451) | 根据干预相对不干预的收益决定是否回应 |
| 大语言模型 | 量化 | [DICEQuant: Distortion-Compensated Rounding with Dual-Ended Shrinkage for LLM Quantization](cards-0004.md#paper-148173) | 按下游敏感度补偿舍入误差 |
| 大语言模型 | 模型压缩 | [DictLLM: Post-training Compression of Large Language Model with Dictionary Kernels](cards-0004.md#paper-151096) | 为成组层共享字典 |
| 计算机视觉 | 三维生成 | [DiDE: Direct Injection with Color-Texture DEcoupling for 3D Stylization](cards-0004.md#paper-152453) | 用独立参考控制颜色和纹理 |
| 计算机视觉 | 三维重建 | [Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty Aware Differentiable Optimization](cards-0004.md#paper-155720) | 训练专为测试时求解设计的初始化 |
| 多模态学习 | 生成引导 | [Diff-Aid: Inference-time Adaptive Interaction Denoising for Rectified Text-to-Image Generation](cards-0004.md#paper-149887) | 按层和步调节逐 token 图文交互 |
| 科学机器学习 | 张量表示 | [DiffATS: Diffusion in Aligned Tensor Space](cards-0004.md#paper-150268) | 先消除低秩分解坐标歧义再学分布 |
| 多模态学习 | 奖励设计 | [DiffCap-RL: Differential QA Rewards for Dense Image and Video Captioning](cards-0004.md#paper-152243) | 对当前采样分歧动态出题 |
| 计算机视觉 | 因子分解 | [Diff-CA: Separating Common and Salient Factors with Diffusion Models](cards-0004.md#paper-152753) | 分别编辑共享属性与组间特异属性 |
| 科学机器学习 | 约束生成 | [DiffCool: Label-Free Synthesis of Chip-Tailored Heat Sinks via Thermal-Aware Diffusion](cards-0004.md#paper-152390) | 将制造约束写进采样状态转移 |
| 计算机视觉 | 监督采样 | [Diffeomoprhism-Informed 3D Gaussian Splattings via Screen-Space Optimal Transport (OT)](cards-0004.md#paper-151447) | 降采样前把监督预算移向细节区域 |
| 机器人学 | 多智能体控制 | [DiffeoMorph: Learning to Morph 3D Shapes Using Differentiable Agent-Based Simulations](cards-0004.md#paper-155314) | 以连续形状分布监督模拟机器人群 |
| 优化 | 分布优化 | [Difference of Convex Programming in the Wasserstein Space with Applications to MMD Optimization](cards-0004.md#paper-148506) | 对非凸分布目标测试凸差更新 |
| 时间序列 | 扩散预测 | [Differencing the Diffusion Trajectory toward Uncertain Components for Time Series Forecasting](cards-0004.md#paper-154330) | 沿去噪时钟调整差分结构 |
| 多智能体强化学习 | 信念建模 | [Differentiable Belief-based Opponent Shaping](cards-0004.md#paper-154944) | 在封闭博弈中用估计信念研究策略协作 |
| 大语言模型 | 模型压缩 | [Differentiable Bit-Widths: Co-optimizing Pruning and Quantization via SVD for Ultra-Efficient LLM Compression](cards-0004.md#paper-148406) | 允许统一训练学出零位宽从而剪除成分 |
| 图学习 | 时序聚类 | [Differentiable Cluster Discovery in Temporal Graphs](cards-0004.md#paper-156759) | 联合更新时序表示与离散分组 |
| 学习理论 | 算法学习 | [Differentiable Exact Learning of Algorithms](cards-0004.md#paper-148538) | 用外部执行轨迹监督控制器而无需专家内部状态 |
| 优化 | 可微组合选择 | [Differentiable Knapsack and Top-k Operators via Dynamic Programming](cards-0004.md#paper-153641) | 直接平滑动态规划递推 |
| 规划 | 符号学习 | [Differentiable Learning of Lifted Action Schemas for Classical Planning](cards-0004.md#paper-153043) | 把动作参数识别和模式归纳一起学习 |
| 控制 | 隐式微分 | [Differentiable Nonlinear Model Predictive Control](cards-0004.md#paper-153003) | 从求解器最优性条件提取灵敏度 |
| 计算几何 | 可微正则 | [Differentiable Range-Partition Entropy for Entropy-Sensitive Geometric Algorithms](cards-0004.md#paper-149856) | 用软分区熵训练几何预处理 |
| 统计学习 | 序列推断 | [Differentiable Systematic Resampling for Variational Sequential Monte Carlo](cards-0004.md#paper-156105) | 用连续系统重采样训练粒子滤波 |
| 大语言模型 | 评测诊断 | [Differential Item Functioning as an Item-Level Diagnostic for LLM Benchmarks](cards-0004.md#paper-139203) | 同总分模型仍按题目检查跨家族偏差 |
| 隐私机器学习 | 模型合并 | [Differentially Private Model Merging](cards-0004.md#paper-149241) | 按部署隐私预算合并已训练模型 |
| 隐私机器学习 | 奖励估计 | [Differentially Private Sparse Reward Estimation with Preference Feedback](cards-0004.md#paper-148832) | 在稀疏偏好模型中按有效特征维度核算样本量 |
| 计算机视觉 | 概念抑制 | [Differential Vector Erasure: Unified Training-Free Concept Erasure for Flow Matching Models](cards-0004.md#paper-155037) | 在流匹配推理时直接抑制目标概念分量 |
| 组合优化 | 可微网络设计 | [Differentiating Network Design Objectives for Balancing Cost and Distance](cards-0004.md#paper-151671) | 将路由局部动作作为可训练决策 |
| 生成模型 | 奖励对齐 | [Diff-Instruct with Diffused Reward: Towards Principled One-step Generator RL](cards-0004.md#paper-153078) | 对整个去噪轨迹对齐奖励 |
| 时间序列 | 状态估计 | [Diff-Kalman: Difference-Driven Learning for Structure-Preserving Kalman Filtering](cards-0004.md#paper-150096) | 分别修正 Kalman 预测与更新 |
| 时间序列 | 概率预测 | [DiffPTS: Rethinking Diffusion ELBO for Probabilistic Time Series Forecasting](cards-0004.md#paper-148542) | 统一噪声估计与扩散训练目标 |
| 可解释性 | 机制追踪 | [DifFRACT: Diffusion Feature Reconstruction and Attribution for Circuit Tracing](cards-0004.md#paper-150450) | 按去噪时刻拟合 MLP 的输入输出以追踪生成机制 |
| 生成模型 | 一步生成 | [DiffRatio: Training One-Step Diffusion Models Without Teacher Supervision](cards-0004.md#paper-155104) | 以密度比训练一步扩散并对并行候选评分 |
| 科学机器学习 | 缺失数据 | [DiffRisk: Diffusion Representation Learning with Informative Missingness for Health Risk Prediction](cards-0004.md#paper-151677) | 把缺失结构纳入条件表示 |
| 自然语言处理 | 文本评测 | [DiffScore: Text Evaluation Beyond Autoregressive Likelihood](cards-0004.md#paper-149202) | 用多掩码率重建比较流畅性和整体一致性 |
| 多模态学习 | 奖励设计 | [Diffusion-DRF: Free, Rich, and Differentiable Reward for Video Diffusion Fine-Tuning](cards-0004.md#paper-150318) | 以分解问题代替视频对齐单标量 |
| 组合优化 | 生成搜索 | [Diffusion-Enhanced GFlowNet for Solving Vehicle Routing Problems](cards-0004.md#paper-155420) | 用去噪扰动扩大车辆路径解空间探索 |
| 多模态学习 | 空间定位 | [Diffusion Fine-Tuning: Iterative Refinement for Advanced Grounding with Diffusion Large Language Models](cards-0004.md#paper-154060) | 联合迭代多边形坐标而非逐顶点提交 |
| 生成模型 | 蒸馏对齐 | [Diffusion fine-tuning with Rewarded Moment Matching Distillation](cards-0004.md#paper-150176) | 同时蒸馏并优化可校准预测指标 |
| 强化学习 | 扩散策略 | [Diffusion Guidance Is a Controllable Policy Improvement Operator](cards-0004.md#paper-151465) | 调节生成引导强度改善离线策略 |
| 语言模型 | 长度推断 | [Diffusion Language Models Can Approximate Optimal Infilling Lengths Implicitly](cards-0004.md#paper-154873) | 先校准首步置信度再选补全长度。 |
| 计算机视觉 | 自监督学习 | [Diffusion Masked Pretraining for Dynamic Point Cloud](cards-0004.md#paper-148526) | 分别去掉遮挡位置泄漏并保留运动多解。 |
| 多模态学习 | 参数高效适配 | [Diffusion Meta-Prompting and Steering for Generalizable Foundation Model Adaptation](cards-0004.md#paper-154312) | 用已有提示参数库合成新任务提示。 |
| 学习理论 | 扩散几何 | [Diffusion Model's Generalization Can Be Characterized by Inductive Biases toward a Data-Dependent Ridge Manifold](cards-0004.md#paper-150031) | 用法向和切向误差分别解释生成样本偏离与覆盖。 |
| 学习理论 | 误差诊断 | [Diffusion Models Observe Only Gradients: A Geometric Perspective on Score Matching Errors](cards-0004.md#paper-151563) | 用可见于边缘分布的梯度误差评估分数模型。 |
| 生成模型 | 引导训练 | [Diffusion Models without Classifier-free Guidance](cards-0004.md#paper-150145) | 将推理阶段的条件引导纳入训练目标。 |
| 概率建模 | 序贯采样 | [Diffusion Path Samplers via Sequential Monte Carlo](cards-0004.md#paper-152139) | 用 SMC 给未归一化目标的中间扩散分布估计分数。 |
| 语言模型 / 强化学习 | 信用分配 | [Diffusion-State Policy Optimization for Masked Diffusion Language Models](cards-0004.md#paper-153673) | 在现有掩码滚动状态分支，只更新新增填充 token。 |
| 强化学习 | 层级规划 | [Diffusion Subgoal Planning for Long-Horizon Offline Goal-Conditioned Reinforcement Learning](cards-0004.md#paper-150829) | 用目标条件扩散生成子目标代替高层价值引导。 |
| 多模态学习 | 并行解码 | [Diffusion Thinking for Fast Long-Form Spatial Reasoning in Vision--Language Models](cards-0004.md#paper-150048) | 在推理块内并行，再把节省时间用在少量纠错轮次。 |
| 可解释性 | 时序表征 | [Diffusion-Time Concept Manifolds: Sparse Autoencoder Groups for Interpreting Denoising Language Models](cards-0004.md#paper-154152) | 用稀疏特征组跟踪去噪过程中概念信息的变化。 |
| 生成模型 | 模型架构 | [Diffusion Transformers with Residual Adaptive Layer Normalization](cards-0004.md#paper-151083) | 把浅层残差送进深层的 adaLN 调制接口。 |
| 科学机器学习 | 推理时搜索 | [Diffusion Tree Search for Inference Time Adaptation of Material Foundation Models](cards-0004.md#paper-151930) | 将已有属性条件模型作为搜索提案，兼顾多目标晶体生成。 |
| 科学机器学习 | 采样热启动 | [Diffusion-warm sampling of the XY model enables fast thermalization at scale](cards-0004.md#paper-155666) | 用小格点扩散模型为大系统 MCMC 提供初态。 |
| 计算机视觉 | 三维分割 | [DIGS: Distribution-Informed Gaussian Splatting for Training-Free Open-Vocabulary 3D Segmentation](cards-0004.md#paper-155419) | 保留边界原语的多峰标签后验，到渲染阶段再做硬决策。 |
| 语言模型 | 潜变量蒸馏 | [DiLaDiff: Distilled Latent-augmented Diffusion for Language Modeling](cards-0004.md#paper-150062) | 给并行离散解码提供共享语义潜变量。 |
| 多模态学习 | 模型合并 | [DiM$^3$: Bridging Multilingual and Multimodal Models via Direction- and Magnitude-Aware Merging](cards-0004.md#paper-154617) | 按参数更新方向和幅值筛选语言与视觉语言残差。 |
| 学习理论 | 状态维数 | [Dimension Bounds for Contractive Reservoir Computing from Input Entropy](cards-0004.md#paper-155874) | 用输入熵与收缩率共同选择储备池的稳定性。 |
| 概率建模 | 数值积分 | [Dimension-Uniform Discretization Analysis of Preconditioned Annealed Langevin Dynamics for Multimodal Gaussian Mixtures](cards-0004.md#paper-153363) | 高维退火 Langevin 中精确积分刚性线性项。 |
| 三维视觉 | 语义蒸馏 | [DinoComplete: 3D Shape Completion with Distilled Semantic Priors and State Space Models](cards-0004.md#paper-155664) | 从残缺点云预测体素对齐的语义先验 |
| 计算机视觉 | 自监督学习 | [DINOv3](cards-0004.md#paper-156661) | 用 Gram 锚定保持长期训练的密集特征 |
| 图学习 | 规模外推 | [DiPhon: Diffusion on Graphons for Scalable Graph Generation](cards-0004.md#paper-148916) | 以规模无关的连续极限设计图扩散 |
| 统计学习 | 独立性检验 | [DiPMInd: Distance profile based mutual independence testing for random objects](cards-0004.md#paper-156633) | 跨度量空间用联合距离剖面检验独立性 |
| 强化学习 | 奖励分配 | [DiPO: Disentangled Perplexity Policy Optimization for Fine-grained Exploration-Exploitation Trade-Off](cards-0004.md#paper-148861) | 用困惑度区分探索样本与利用样本 |
| 强化学习 | 奖励学习 | [DiReCL: Learning Differentiable Reward Code with Inverse Reinforcement Learning](cards-0004.md#paper-148348) | 保留可读奖励代码并用示范校准参数 |
| 优化 | 随机求根 | [Direct Acceleration of Stochastic Root-Finding Without Variance Reduction and Regularization](cards-0004.md#paper-153100) | 固定批量时比较双锚点与加大批量的加速方案 |
| 计算机视觉 | 渲染加速 | [Direct Conditional Parameterization for N-Dimensional Splatting](cards-0004.md#paper-155500) | 直接参数化查询条件下的图元属性 |
| 多模态学习 | 连续条件化 | [Direct Conditioning of Audio Diffusion Transformers on fMRI Reveals Cortical Contributions to Sound Reconstruction](cards-0004.md#paper-152995) | 将连续输入通过适配器直接接入音频扩散 |
| 统计学习 | 漂移估计 | [Direct Estimation of Schrödinger Bridge Time-Series Drifts: Finite-Sample, Asymptotic, and Adaptive Guarantees](cards-0004.md#paper-155581) | 直接在漂移层估计以隔离统计误差 |
| 计算机视觉 | 归纳偏置诊断 | [Directional Confusions Reveal Divergent Inductive Biases Through Rate-Distortion Geometry in Human and Machine Vision](cards-0004.md#paper-152629) | 在准确率匹配时比较错误方向与率失真曲线 |
| 生成模型 | 条件编码 | [Directional Noise Conditioning for Diffusion Models](cards-0004.md#paper-150199) | 将视觉属性编码进初始噪声方向 |
| 强化学习 | 离线到在线迁移 | [Direction-Aware Offline-to-Online Learning in Linear Contextual Bandits](cards-0004.md#paper-148256) | 只在低偏差且历史覆盖充分的方向复用日志 |
| 多模态学习 | 几何对齐 | [Direct Product Flow Matching: Decoupling Radial and Angular Dynamics for Few-Shot Adaptation](cards-0004.md#paper-149331) | 分别适配特征半径和角度 |
| 具身智能 | 约束规划 | [DiRecT: Safe Diffusion-Based Planning via Receding-Horizon Denoising](cards-0004.md#paper-155798) | 只对干净轨迹施加终端可行性约束 |
| 计算机视觉 | 表面位置编码 | [DirectUV: Image-Conditioned UV Texture Generation with Surface-Aware Positional Encoding](cards-0004.md#paper-153147) | 用三维表面距离设计 UV 注意力 |
| 时间序列 | 多模态预测 | [Dirichlet-Guided Group Forecasting for Alleviating Over-smoothing in Time Series Forecasting](cards-0004.md#paper-154424) | 预测多个动力学模式并校准模式权重 |
| 生成模型 | 低比特量化 | [DiRotQ: Rotation-Aware Quantization for 4-bit Diffusion Transformers](cards-0004.md#paper-155781) | 保留高方差激活子空间的较高精度 |
| 计算机视觉 | 三维定位 | [Disambiguating 2D-3D Correspondences in Gaussian Splatting-based Feature Fields for Visual Localization](cards-0004.md#paper-152518) | 将渲染图元细分成更明确的匹配单位 |
| 软件工程 | 测试评测 | [DIS-Bench: Evaluating LLMs on System Testing via Directed Input Synthesis](cards-0004.md#paper-138947) | 用可达分支的系统输入任务单独评价测试能力 |
