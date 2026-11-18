# NeurIPS 2026

[首页](../../README.md) · [官方会议目录](https://neurips.cc/Downloads/2026)

官方目录当前列出 **9,144** 个论文海报条目，已筛选 **51** 篇，暂收录 **49** 篇。[筛选底册](papers.tsv)按官方海报 ID 记录覆盖及去留。目录可能随会议更新，候选范围核定后统一排名，收录上限为 50%。

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
