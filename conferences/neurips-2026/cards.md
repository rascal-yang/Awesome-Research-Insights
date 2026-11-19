# NeurIPS 2026 论文卡

[会议索引](README.md)

<a id="paper-tdl6qleloi"></a>

## Fast Rates for Offline Contextual Bandits with Forward-KL Regularization under Single-Policy Concentrability

[官方论文页](https://neurips.cc/virtual/2026/poster/149055) · [作者论文 v3](https://arxiv.org/abs/2605.09214v3)

- **问题 / 瓶颈** · 反向 KL 正则已有误差倒数型快率，前向 KL 的已有分析常停留在误差平方倒数型样本复杂度。
- **核心创新 / 方法** · 用悲观估计与凸分析处理前向 KL 正则的离线上下文赌博机，统一表格设定和一般函数逼近的上界推导。
- **Baseline** · 理论比较对象为既有反向 KL 快率、前向 KL 慢率及无正则情形。
- **Benchmark** · 理论设定为单策略集中性条件下的离线上下文赌博机，以达到目标误差所需日志样本数为指标。
- **关键结果 / 消融** · 作者给出误差倒数型上界及匹配统计速率的下界；正则很弱时，样本复杂度恢复到无正则的慢率。
- **适用条件 / 局限** · 结论针对给定的日志覆盖与正则条件；向多步强化学习或其他覆盖设定延伸需要额外分析。

**可复用机制** · 为离线策略设计 KL 正则时，把覆盖条件和正则强度都写进样本效率假设。比较方法时扫描弱正则区间，检查理论快率是否仍适用。

<a id="paper-151137"></a>

## ConQuR: Corner Aligned Activation Quantization via Optimized Rotations for LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151137) · [作者来源](https://neurips.cc/virtual/2026/poster/151137)

- **问题 / 瓶颈** · 离群激活放大量化误差，旋转方法可能需要端到端训练或离线存储大量激活。
- **核心创新 / 方法** · 让归一化激活对齐内接超立方体角点，以正交 Procrustes 闭式更新旋转，并随校准样本在线更新。
- **Baseline** · 比较既有旋转量化方法，摘要未列名称。
- **Benchmark** · Llama-2 和 Llama-3，3B 至 70B 参数；评估困惑度及常识推理。
- **关键结果 / 消融** · 作者报告表现相当或改善，无需端到端训练及大量激活落盘；差值待核实。
- **适用条件 / 局限** · 校准数据代表性、量化位宽和硬件时延边界待全文确认。

**可复用机制** · 把旋转学习改成可流式执行的闭式校准，固定量化配置比较困惑度、任务准确率和峰值校准内存。

<a id="paper-155179"></a>

## Confidence-Calibrated Inference Expansion for Evaluator-Guided Test-Time Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155179) · [作者来源](https://neurips.cc/virtual/2026/poster/155179)

- **问题 / 瓶颈** · 单一置信度无法回答继续推理是否比立即接受或回退划算。
- **核心创新 / 方法** · 为三种动作训练置信度头，留出集校准，以预期成功减显式算力成本选择动作并惩罚不确定性。
- **Baseline** · 固定和自适应预算、同特征路由器及更强学习控制器。
- **Benchmark** · MATH、AIME25 做验证器引导的宽度扩展；确定答案的 General Reasoning 做评判器引导的修订。
- **关键结果 / 消融** · 校准改善效用与计算量的折衷，在多项控制对比下保持；算力无成本时高预算策略仍有竞争力。
- **适用条件 / 局限** · 评估器变化时需重新拟合与校准；摘要未给迁移幅度。

**可复用机制** · 把是否继续搜索改成动作条件风险决策，在共同预算下对比单置信度门控。

<a id="paper-150998"></a>

## MAGE: Multi-Agent Self-Evolution with Co-Evolutionary Knowledge Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/150998) · [作者来源](https://neurips.cc/virtual/2026/poster/150998)

- **问题 / 瓶颈** · 扁平记忆和自然语言反馈难同时服务跨轮任务选择与经验复用。
- **核心创新 / 方法** · 四个子图记录跨轮知识，经验子图保存教师纠错和自身成功轨迹；用同一奖励更新图、任务搜索和技能路由。
- **Baseline** · 冻结骨干的提示型方法；消融成功轨迹与教师纠错。
- **Benchmark** · 九个基准覆盖数学、问答、时空、金融、医学选择题及交互环境。
- **关键结果 / 消融** · 成功轨迹在模板型推理贡献更大，纠错经验支持较难的组合和交互。
- **适用条件 / 局限** · 依赖可用任务反馈、教师纠错和检索质量；摘要未列各基准分数。

**可复用机制** · 不要混存所有轨迹后统一排序，先对成功模板和纠错先例分别做消融并按任务类型选路由。

<a id="paper-154728"></a>

## MemContract: Contract-Sensitive Evaluation for Mutable Agent Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/154728) · [作者来源](https://neurips.cc/virtual/2026/poster/154728)

- **问题 / 瓶颈** · 检索主导的分数会压平可变记忆操作间的能力差异。
- **核心创新 / 方法** · 为六类操作设定前后条件，加入干扰、别名变化与延迟对照，用固定探针检查能检出的残留。
- **Baseline** · 匹配预算下比较七种后端，包括图记忆、混合、RAG。
- **Benchmark** · 1080 个跨会话任务；另有人类标注核验、跨模型重跑和 LongMemEval、LoCoMo 外部对照。
- **关键结果 / 消融** · GPT-4o 下图记忆 67.6%，混合 62.4%，RAG 40.6%；外部任务上图与混合的差距降到 1.8、2.8 个百分点。
- **适用条件 / 局限** · 残留探针无法认证删除，后端顺序和差距受操作组成与调优影响。

**可复用机制** · 为可变状态建模时用正式操作契约和干扰会话检验写后状态，并单独报告各操作成绩。

<a id="paper-148950"></a>

## DeltaFugue: Orchestrating Spatial and Associative Memory for Algorithmic Length Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/148950) · [作者来源](https://neurips.cc/virtual/2026/poster/148950)

- **问题 / 瓶颈** · 固定容量关联记忆难保存随序列长度增长的精确依赖。
- **核心创新 / 方法** · 以线性注意力控制器读写可微一维空间带，用 delta-rule 更新保持并行训练。
- **Baseline** · 全并行模型和自然语言实验中的 DeltaNet 基线。
- **Benchmark** · 形式语言长度泛化及 340M 参数自然语言实验，包含数学和代码领域的长度外推。
- **关键结果 / 消融** · 作者证明可识别多类形式语言，并报告长度外推较强，具体结果和硬件开销待核实。
- **适用条件 / 局限** · 理论可表达性和可训练性须分别看待，长带访问开销及更大模型表现待核实。

**可复用机制** · 按位置依赖与关联检索拆分内存职责，在外推长度下同时量化正确率、空间状态开销和并行吞吐。

<a id="paper-153322"></a>

## Beyond Pairwise Supervision: Spectral Characteristic Matching for Data-Efficient Multimodal Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153322) · [作者来源](https://openreview.net/forum?id=MAFbcmvKHt)

- **问题 / 瓶颈** · 少量配对只提供局部对应，难发现两个预训练编码器的全局分布失配。
- **核心创新 / 方法** · 比较图像与文本嵌入的特征函数，学习频域探针并分别参数化方向和半径。
- **Baseline** · 作者讨论对比学习与保几何正则；具名实验对照待全文核实。
- **Benchmark** · 迁移、检索、鲁棒性及表征分析；数据集、配对预算与指标待核实。
- **关键结果 / 消融** · 摘要报告多项评测改善，具体幅度和采样器独立贡献待核实。
- **适用条件 / 局限** · 有限频域查询对细粒度差异的覆盖及低配对预算的边界待核实。

**可复用机制** · 固定标注预算，将两模态的分布匹配作为配对损失的补充，分别测检索与迁移。

<a id="paper-153068"></a>

## GEAR-Align: Grounding-Evidence-Aware Gradient Routing for Multimodal Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153068) · [作者来源](https://openreview.net/forum?id=ODn1YAbOjd)

- **问题 / 瓶颈** · 能从文本猜出的 token 也会更新视觉参数，可能污染需要图像证据的训练信号。
- **核心创新 / 方法** · 以视觉反事实估计必要性及证据特异性，所有 token 更新语言参数，高必要性 token 更新路由，高特异性子集再更新视觉证据参数。
- **Baseline** · 以 LLaVA 式训练为出发点，两种 Qwen3 骨干受控设置；具名对照待核。
- **Benchmark** · 幻觉、局部证据与通用多模态基准，具体数据集与指标待核。
- **关键结果 / 消融** · 摘要报告幻觉敏感和局部证据任务改善，通用表现仍具竞争力；幅度待核。
- **适用条件 / 局限** · 反事实探测质量与参数模块能否拆分决定适用性。

**可复用机制** · 固定训练数据，比较所有 token 更新视觉侧和仅证据相关 token 更新，并分开测定位与通用能力。

<a id="paper-149742"></a>

## RankAlign: Unsupervised Vision-Language Representation Alignment via Rank Transformation

[官方论文页](https://neurips.cc/virtual/2026/poster/149742) · [作者来源](https://openreview.net/forum?id=ngwv68jt7S)

- **问题 / 瓶颈** · 不同模态核矩阵的数值尺度和表征密度不同，使直接匹配不稳定。
- **核心创新 / 方法** · 将两侧核矩阵分别改写为秩表征，用邻接次序匹配相对结构。
- **Baseline** · 与既有核对齐方法比较；方法名待核实。
- **Benchmark** · 多数据集无配对对齐，包括医学影像；数据集名与指标待核实。
- **关键结果 / 消融** · 摘要报告更耐噪并改善对齐；定量结果待核。
- **适用条件 / 局限** · 取决于跨模态是否共享邻接结构，相似度并列和噪声导致的排序抖动待核。

**可复用机制** · 若仅尺度不匹配，先在各输入内部做秩变换，再测试能否稳定匹配；同时对照核归一化。

<a id="paper-148644"></a>

## Breakeven complexity: A new perspective on neural partial differential equation solvers

[官方论文页](https://neurips.cc/virtual/2026/poster/148644) · [作者来源](https://neurips.cc/virtual/2026/poster/148644)

- **问题 / 瓶颈** · 单次推理加速掩盖离线训练和造数成本，也忽略低精度数值基线。
- **核心创新 / 方法** · 以误差匹配的传统求解器为对照，将数据、训练和调参成本摊到反复求解中；用缩放律选择造数预算。
- **Baseline** · 同误差的传统数值求解器和多种神经 PDE 求解器。
- **Benchmark** · APEBench 的三个二维周期 PDE 及 PyFR 多障碍流；测盈亏平衡所需前向求解次数。
- **关键结果 / 消融** · 作者摘要报告更高成本、维度或更长滚动等较难设置更可能使代理求解器有成本优势；具体阈值待核。
- **适用条件 / 局限** · 依赖目标误差、部署硬件及重复求解量。

**可复用机制** · 代理模型选型时同时给出误差匹配对照和固定启动成本，避免将吞吐量直接解释为总成本。

<a id="paper-151943"></a>

## Explanation of Dynamic Physical Field Predictions using WassersteinGrad: Application to Autoregressive Weather Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/151943) · [作者来源](https://neurips.cc/virtual/2026/poster/151943)

- **问题 / 瓶颈** · 扰动输入会移动梯度归因图中的结构，逐点平均会模糊它们。
- **核心创新 / 方法** · 计算扰动归因图的熵正则 Wasserstein 重心，提取几何共识。
- **Baseline** · 逐点平均及其他梯度归因方法，具名实验基线待核。
- **Benchmark** · 区域天气数据、经气象学家验证的神经模型，测试单步及自回归归因；指标待核。
- **关键结果 / 消融** · 摘要报告解释性质优于梯度基线；幅度待核。
- **适用条件 / 局限** · 依赖适当的空间代价，解释质量与预测精度是不同目标。

**可复用机制** · 在移动结构数据中，先区分空间偏移和幅值噪声，再决定用几何聚合还是逐点平均。

<a id="paper-153842"></a>

## Learning Spectral Compositional Koopman Operators for Global-to-Regional Weather Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/153842) · [作者来源](https://neurips.cc/virtual/2026/poster/153842)

- **问题 / 瓶颈** · 重复邻域聚合可能不断压制高频结构，导致区域预报中尺度变率衰减。
- **核心创新 / 方法** · 保留网格、编码器和解码器，将堆叠消息传递换成谱潜空间中的单步线性 Koopman 演化，联合约束基底稳定性和潜变量几何。
- **Baseline** · 消息传递处理器及当前天气预报方法，名字待核。
- **Benchmark** · 全球至区域天气预报，含 5 公里区域分辨率，比较 RMSE 和推理成本。
- **关键结果 / 消融** · 作者摘要报告区域 RMSE 降低 11–14%；按变量与时效的细项待核。
- **适用条件 / 局限** · 需检验谱演化对突发与小尺度现象的覆盖。

**可复用机制** · 固定空间编码，在长滚动下比较消息传递与谱演化，联合报告频谱与 RMSE。

<a id="paper-150539"></a>

## Online Decision-Focused Learning under Semi-Bandit Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/150539) · [作者来源](https://neurips.cc/virtual/2026/poster/150539)

- **问题 / 瓶颈** · 用模型自身填补不可见代价可误翻转反事实决策，并通过梯度强化错误。
- **核心创新 / 方法** · 贝叶斯末层在线提供不确定性和代价填补，掩码屏蔽未观测组件的直接表征梯度。
- **Baseline** · 先预测再优化、半赌博机方法及直接自填补的决策学习；具名对照待核实。
- **Benchmark** · 背包、最短路径、投资组合共五个在线实例，以累计遗憾评估。
- **关键结果 / 消融** · 作者报告五个实例的平均累计遗憾最低，四个差异显著；具体数值待核。
- **适用条件 / 局限** · 依赖可拆分成本及可观测入选组件；表征梯度与探索的各自贡献待核。

**可复用机制** · 在只观察已执行组件的在线决策中，区分补全供优化使用和补全供梯度使用，记录累计遗憾。

<a id="paper-150017"></a>

## $\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control

[官方论文页](https://neurips.cc/virtual/2026/poster/150017) · [作者来源](https://neurips.cc/virtual/2026/poster/150017)

- **问题 / 瓶颈** · 异步缓冲样本偏离当前学生与教师上下文
- **核心创新 / 方法** · 分解 rollout 与监督漂移，用新鲜度调权并约束策略变化
- **Baseline** · 同步及异步蒸馏
- **Benchmark** · 推理、工具调用及代码任务
- **关键结果 / 消融** · 接近同步性能，保留异步吞吐优势
- **适用条件 / 局限** · 漂移阈值与定量幅度待核

**可复用机制** · 固定吞吐预算比较统一权重和新鲜度权重。

<a id="paper-152538"></a>

## $\epsilon$-Good Action Identification in Fixed-Budget Monte Carlo Tree Search

[官方论文页](https://neurips.cc/virtual/2026/poster/152538) · [作者来源](https://neurips.cc/virtual/2026/poster/152538)

- **问题 / 瓶颈** · 最坏叶节点和子树间差距共同决定辨识难度
- **核心创新 / 方法** · 设计无需输入容差的算法，误判界同时依赖树内及树间间隙
- **Baseline** · 单叶退化为普通多臂赌博机，对照 halving 与 Successive Rejects
- **Benchmark** · 深度二 max–min 树、固定预算和近优误判概率
- **关键结果 / 消融** · 给出实例依赖指数衰减界，且上下界尚有差距
- **适用条件 / 局限** · 理论针对深度二，不直接推出一般 MCTS 结论

**可复用机制** · 有限预算规划需同时评估估错子树与估错最坏叶子的风险。

<a id="paper-153358"></a>

## $f$-GRPO & Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153358) · [作者来源](https://neurips.cc/virtual/2026/poster/153358)

- **问题 / 瓶颈** · 偏好散度解释不能直接用于只有标量奖励的对齐
- **核心创新 / 方法** · 用高低于平均奖励的响应诱导分布，构造 f-GRPO 与可结合离线偏好的 f-HAL
- **Baseline** · GRPO 及常见偏好监督
- **Benchmark** · 数学 RLVR 与学习奖励的安全对齐
- **关键结果 / 消融** · 作者报告数学推理改善、混合目标降低奖励投机
- **适用条件 / 局限** · 具体散度与效果量待核

**可复用机制** · 在相同奖励预算对照 GRPO 与散度变体，同时测真实任务与代理奖励。

<a id="paper-155968"></a>

## $h$-control: Training-Free Camera Control via Block-Conditional Gibbs Refinement

[官方论文页](https://neurips.cc/virtual/2026/poster/155968) · [作者来源](https://neurips.cc/virtual/2026/poster/155968)

- **问题 / 瓶颈** · 深度扭曲的视频引导与生成先验可能冲突
- **核心创新 / 方法** · 硬替换观测位置后对补集做块条件伪 Gibbs 更新，并冻结已混合的三维块
- **Baseline** · 七种免训练或训练式竞争方法
- **Benchmark** · RealEstate10K 与 DAVIS，含 FVD
- **关键结果 / 消融** · FVD 优于七种对照，所有报告指标优于免训练对照
- **适用条件 / 局限** · 依赖部分观测和局部混合，速度收益待核

**可复用机制** · 部分观测生成可将约束位点固定更新与未观测块的条件细化分离。

<a id="paper-139441"></a>

## $\mathrm{Bounded\mbox{-}RS}$: A Bounded Evaluation Protocol and Testbed for Representational Systematicity

[官方论文页](https://neurips.cc/virtual/2026/poster/139441) · [作者来源](https://neurips.cc/virtual/2026/poster/139441)

- **问题 / 瓶颈** · 组合泛化行为不能证明表征被因果使用。
- **核心创新 / 方法** · 在受控语义解析中构造匹配重组合与精确干预对，依次测可恢复性、交换、必要性和修复。
- **Baseline** · 在相同行为锚点下比较绑定与几何解释。
- **Benchmark** · 受控语义解析，按存在、因果使用等证据等级裁定。
- **关键结果 / 消融** · 所测绑定符合因果使用，所测几何解释缺乏支持。
- **适用条件 / 局限** · 几何结论限于冻结闭包与所测家族，检测器真实性未获证实。

**可复用机制** · 用同一组可控干预将表示探针结果与生成机制结论分开。

<a id="paper-155296"></a>

## $\text{A}^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/155296) · [作者来源](https://neurips.cc/virtual/2026/poster/155296)

- **问题 / 瓶颈** · 动作预测监督不足以抑制无关视觉捷径。
- **核心创新 / 方法** · 按视觉变化提议区域，经离线分割细化，再施加区域注意力与语言对比损失。
- **Baseline** · 与未加区域监督的多个 VLA 底座对照，名称待核实。
- **Benchmark** · 仿真及真机操作，比较成功率。
- **关键结果 / 消融** · 作者报告跨基准平均成功率增益为 6.5% 至 25.2%；单位和消融待核实。
- **适用条件 / 局限** · 相机运动、遮挡及分割误差会干扰伪标签。

**可复用机制** · 分开消融注意力分配和语言对比，并测变化区域与真实目标错位时的效果。

<a id="paper-148783"></a>

## $\texttt{bispectrum}$: Selective $G$-Bispectra Made Practical

[官方论文页](https://neurips.cc/virtual/2026/poster/148783) · [作者来源](https://neurips.cc/virtual/2026/poster/148783)

- **问题 / 瓶颈** · 完整群双谱开销高且实现跨群不统一。
- **核心创新 / 方法** · 用可微模块实现选择性群双谱，并针对平面和球面旋转采用专门构造。
- **Baseline** · 完整群双谱。
- **Benchmark** · 七种群作用的实现及复杂度比较；应用基准待核实。
- **关键结果 / 消融** · 有限群复杂度由平方降至线性；球面带限系数由立方降至平方。
- **适用条件 / 局限** · 依赖正确的群模型；离散实现及实际运行开销待核实。

**可复用机制** · 在已知任务对称性时，以选择性不变量作池化，与全量谱及数据增强同测。

<a id="paper-154745"></a>

## $\varphi$TD: Distributional Reinforcement Learning using Characteristic Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/154745) · [作者来源](https://neurips.cc/virtual/2026/poster/154745)

- **问题 / 瓶颈** · 常见分布式 RL 估计器对分布族的表达受限。
- **核心创新 / 方法** · 在频域计算 TD 分布损失，覆盖分位数、类别及连续混合等表示。
- **Baseline** · 分位数式与类别式分布 RL，具名对照待核实。
- **Benchmark** · 合成基准与深度强化学习环境；具体任务和指标待核实。
- **关键结果 / 消融** · 作者报告使用更宽的参数族常带来提升；幅度待核实。
- **适用条件 / 局限** · 频域采样与参数族的选择影响拟合，开销待核实。

**可复用机制** · 在固定回报任务上比较简单与混合分布头，并记录频域损失能否改善尾部估计。

<a id="paper-150442"></a>

## 2-Step Agent: How a Bayesian Decision Maker Learns from AI-Decision Support

[官方论文页](https://neurips.cc/virtual/2026/poster/150442) · [作者来源](https://neurips.cc/virtual/2026/poster/150442)

- **问题 / 瓶颈** · 准确预测仍可能通过人类信念更新导致更差决策。
- **核心创新 / 方法** · 建模先由模型预测更新贝叶斯信念，再估因果效应并选择行动，在线性高斯情形给出可计算解。
- **Baseline** · 无决策支持。
- **Benchmark** · 线性高斯推断与决策实验；场景、指标数值待核实。
- **关键结果 / 消融** · 一个错配先验即可让辅助决策更差，即使模型正确且决策者理性。
- **适用条件 / 局限** · 可计算解依赖线性高斯设定，对实际人群的外推待核实。

**可复用机制** · 部署决策支持前用有无辅助的反事实对照检验先验错配，而同时追踪预测性能和实际效用。

<a id="paper-153557"></a>

## 3A-VLA: Abstraction-Aligned Action Learning for Vision-Language Agents in 3D Game Worlds

[官方论文页](https://neurips.cc/virtual/2026/poster/153557) · [作者来源](https://neurips.cc/virtual/2026/poster/153557)

- **问题 / 瓶颈** · 稠密视觉流和含糊示范会污染动作监督。
- **核心创新 / 方法** · 用任务无关的意图及环境语义抽象形成连续对齐分，再对模仿损失加权。
- **Baseline** · 具名方法与未加权对照数值待核实。
- **Benchmark** · Minecraft、Game for Peace 及多款未见游戏的零样本评测。
- **关键结果 / 消融** · 作者报告在所测游戏表现领先；具体结果与消融待核实。
- **适用条件 / 局限** · 验证限于游戏；抽象错误会影响权重。

**可复用机制** · 对有歧义的模仿数据比较等权和语义一致性权重，并审计被下调的难例。

<a id="paper-152512"></a>

## 3D Consistency Tokens

[官方论文页](https://neurips.cc/virtual/2026/poster/152512) · [作者来源](https://neurips.cc/virtual/2026/poster/152512)

- **问题 / 瓶颈** · 重复纹理使外观对应产生歧义。
- **核心创新 / 方法** · 从点云构造几何锚点 token，以双向交叉注意力让图像 token 与锚点共同修正。
- **Baseline** · 前馈高斯模型及按场景优化方案。
- **Benchmark** · DL3DV-10K、Mip-NeRF 360、Tanks & Temples。
- **关键结果 / 消融** · 作者报告保持单次前向并优于前馈对照，质量接近优化式方案；数值待核。
- **适用条件 / 局限** · 依赖点云先验；噪声和覆盖率的失效点待核。

**可复用机制** · 重复纹理多时对照仅外观匹配与显式几何锚点，扫点云缺失强度。

<a id="paper-148954"></a>

## 3D-PLOT-LLM: Part-Level Object Tokens for 3D Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148954) · [作者来源](https://openreview.net/forum?id=tubVmG86qx)

- **问题 / 瓶颈** · 整物体表示缺少部件级引用接口。
- **核心创新 / 方法** · 将冻结点编码器的图块分组，在各组前加部件标记和保留词表 token，并用空间统计及邻接信息更新标记。
- **Baseline** · 比较 PointLLM、Kestrel、PARIS3D、SegPoint、ShapeLLM，以及去掉标记细化的变体。
- **Benchmark** · PartVerse-QA、3DCoMPaT-GrIn 和 Objaverse，含 Jaccard、严格匹配及文本评测。
- **关键结果 / 消融** · 部件槽位 Jaccard 为 0.459，严格匹配 13.78%；作者报告新增可训练参数低于 100 万。
- **适用条件 / 局限** · 依赖图块分组质量，严格匹配仍低。

**可复用机制** · 把感知区域映射到可引用的离散槽位，单独测试生成引用和理解既有引用。

<a id="paper-151080"></a>

## 3D Point Splatting for mmWave Radar Novel View Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/151080) · [作者来源](https://openreview.net/forum?id=d7DxwkjIJi)

- **问题 / 瓶颈** · 只拟合功率图会丢失相位，蒙特卡洛追踪成本高。
- **核心创新 / 方法** · 从雷达方程推导点散射，借预计算点扩散函数累积复值。
- **Baseline** · 蒙特卡洛光线追踪及光学新视角模型。
- **Benchmark** · 六组 ColoRadar 室外场景，包含多种雷达产品。
- **关键结果 / 消融** · 同一场景表示可输出 ADC、复数距离剖面和距离方位图；数值待核。
- **适用条件 / 局限** · 材料模型和散射假设的适用范围待核。

**可复用机制** · 将复值信号作为共享潜在输出，以同一场景对照多种信号产品。

<a id="paper-152761"></a>

## 3D Skew Normal Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/152761) · [作者来源](https://openreview.net/forum?id=QZ4uureDLB)

- **问题 / 瓶颈** · 对称核在单侧表面可能浪费容量。
- **核心创新 / 方法** · 以有界偏斜参数让原语从高斯平滑过渡到近半高斯，并保留边缘化解析性质。
- **Baseline** · 标准 3DGS、椭圆核及硬截断路线。
- **Benchmark** · 新视角合成，数据集及指标待核。
- **关键结果 / 消融** · 摘要描述偏斜原语可接入既有流程，效果幅度待核。
- **适用条件 / 局限** · 新参数带来的优化开销及稳定性待核。

**可复用机制** · 固定原语数量比较对称与可偏斜核，单独统计边缘误差。

<a id="paper-153051"></a>

## 3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism

[官方论文页](https://neurips.cc/virtual/2026/poster/153051) · [作者来源](https://openreview.net/forum?id=OOMPX54uZM)

- **问题 / 瓶颈** · 人工评测成本高，无参考视频难判定物理合理性。
- **核心创新 / 方法** · 把 DINO 语义与三维点轨迹结合，训练自编码器重建留出轨迹。
- **Baseline** · 领先视觉语言模型及自动视频评分。
- **Benchmark** · 多个生成视频数据集，测物理违例识别及与人评相关性。
- **关键结果 / 消融** · 作者报告物理违例识别比所比 VLM 高超过 10%，若干人评相关性翻倍。
- **适用条件 / 局限** · 依赖三维轨迹和语义估计质量。

**可复用机制** · 在无参考生成质量评估中对照纯语义、纯轨迹和联合表征。

<a id="paper-150244"></a>

## 3D-VITAL: Visibility-aware Identity Training from Artificial Liftings of 3D Reconstruction model for Cross-View Object Re-Identification

[官方论文页](https://neurips.cc/virtual/2026/poster/150244) · [作者来源](https://openreview.net/forum?id=jej1VhaCQr)

- **问题 / 瓶颈** · 单视角重建的几何失败和背面纹理幻觉会污染身份监督。
- **核心创新 / 方法** · 用显式三维网格渲染，并以源视图可见性作为像素级可靠性线索。
- **Baseline** · 以生成模型新视角增强为对照路线。
- **Benchmark** · 单视角空地跨视角重识别，具体指标待核。
- **关键结果 / 消融** · 摘要提出分别处理网格失真与未见纹理，量化值待核。
- **适用条件 / 局限** · 依赖重建质量及可见性估计。

**可复用机制** · 对合成图像监督记录像素来源并在可信区域与幻觉区域分开采样。

<a id="paper-148581"></a>

## A Batched Hartigan's $k$-Means Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/148581) · [作者来源](https://openreview.net/forum?id=wk378kUPrZ)

- **问题 / 瓶颈** · Hartigan 移点原本顺序执行，阻碍向量化。
- **核心创新 / 方法** · 用三角不等式识别可并发的移点子集，其余仍顺序更新。
- **Baseline** · 标准 Hartigan 和批量 Lloyd。
- **Benchmark** · 执行速度比较；数据集与配置待核。
- **关键结果 / 消融** · 作者报告达到与 Lloyd 可比的速度，幅度待核。
- **适用条件 / 局限** · 收益取决于有多少更新满足安全并行条件。

**可复用机制** · 对顺序局部搜索先证并发无干扰条件，再按可并行比例测吞吐。

<a id="paper-148310"></a>

## ABC-Align: Prediction-Powered Alignment with Adaptive Bias Control

[官方论文页](https://neurips.cc/virtual/2026/poster/148310) · [作者来源](https://openreview.net/forum?id=ymfnBICWLI)

- **问题 / 瓶颈** · 伪偏好标签有系统偏差，而少量人工纠偏方差较高。
- **核心创新 / 方法** · 以大量伪标签降低方差，用人工子集的估计动态控制校正。
- **Baseline** · 半监督偏好学习及 RLAIF 类方法。
- **Benchmark** · 人类反馈稀缺的 RLHF 与 DPO，任务及指标待核。
- **关键结果 / 消融** · 作者报告优于先前半监督方法。
- **适用条件 / 局限** · 依赖人工子集的代表性及偏差方差估计。

**可复用机制** · 固定人工预算对照恒定纠偏与自适应纠偏，改变教师偏差或标签量。

<a id="paper-150308"></a>

## ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space

[官方论文页](https://neurips.cc/virtual/2026/poster/150308) · [作者来源](https://openreview.net/forum?id=j5oO6647Tp)

- **问题 / 瓶颈** · 从纯噪声重启忽略相邻状态相似和不规则观测时间。
- **核心创新 / 方法** · 用单个连续非马尔可夫扩散桥，从前序状态推进且让噪声随实际时差变化，可条件化任意观测子集。
- **Baseline** · 标准噪声到数据扩散及自回归路径。
- **Benchmark** · 面向连续时空随机过程、视频或天气等，具体基准待核。
- **关键结果 / 消融** · 摘要给出从临近状态出发和噪声时差缩放的理论性质；结果幅度待核。
- **适用条件 / 局限** · 按前序状态推进依赖过程的邻近连续性。

**可复用机制** · 对不规则时间序列对照固定步噪声与物理时间噪声，并测试插值及外推。

<a id="paper-155947"></a>

## A Bitter Lesson for Data Filtering

[官方论文页](https://neurips.cc/virtual/2026/poster/155947) · [作者来源](https://openreview.net/forum?id=1bGfOCtPWO)

- **问题 / 瓶颈** · 质量过滤会删去可能可用的数据。
- **核心创新 / 方法** · 在高算力、数据稀缺区间扫描数据质量与规模。
- **Baseline** · 过滤数据和纳入低质量数据。
- **Benchmark** · 预训练缩放实验，具体模型和指标待核。
- **关键结果 / 消融** · 作者发现充分训练的大模型纳入名义低质量数据可改善表现。
- **适用条件 / 局限** · 结论限于论文所测高算力且数据稀缺区间。

**可复用机制** · 将数据供给和计算预算分开变化，测过滤收益是否变号。

<a id="paper-154233"></a>

## A Black-Box Reduction from Regret to Multi-Level Coverage

[官方论文页](https://neurips.cc/virtual/2026/poster/154233) · [作者来源](https://openreview.net/forum?id=FEc497vZlM)

- **问题 / 瓶颈** · 多级区间必须嵌套，已有方法的误差随级数平方根增长。
- **核心创新 / 方法** · 将惰性保序投影与通用在线算法组合，经对偶连接遗憾与覆盖。
- **Baseline** · 既有投影在线梯度法。
- **Benchmark** · 股票、电力需求和合成流，覆盖率与区间宽度。
- **关键结果 / 消融** · 两个实例将级数依赖改为对数平方根，并改善覆盖宽度权衡。
- **适用条件 / 局限** · 快率对应指定算法和线性化遗憾条件。

**可复用机制** · 固定覆盖水平比较校准误差、区间宽度与嵌套违规。

<a id="paper-149439"></a>

## Absolute State-wise Constrained Policy Optimization: High-Probability State-wise Constraints Satisfaction

[官方论文页](https://neurips.cc/virtual/2026/poster/149439) · [作者来源](https://openreview.net/forum?id=q54wRgjMnG)

- **问题 / 瓶颈** · 期望约束可能漏掉罕见严重违规。
- **核心创新 / 方法** · 通过无模型策略搜索的精确更新提供高概率逐状态约束证书。
- **Baseline** · 期望型及其他安全强化学习，具名方法待核。
- **Benchmark** · 连续控制机器人运动任务，测违规与奖励。
- **关键结果 / 消融** · 报告违规降低且奖励有竞争力；证书无需高斯假设。
- **适用条件 / 局限** · 要求有限方差，精确更新与实现误差的差别待核。

**可复用机制** · 安全训练同时报告平均成本和轨迹最大成本越界率。

<a id="paper-149846"></a>

## Accelerated Image Editing via Consistency-Aware Source Token Pruning

[官方论文页](https://neurips.cc/virtual/2026/poster/149846) · [作者来源](https://openreview.net/forum?id=mrTRzrrt4V)

- **问题 / 瓶颈** · 源图 token 在每步产生大量注意力成本。
- **核心创新 / 方法** · 闭式正则采样更新保源图一致，偏差引导掩码选择可裁 token。
- **Baseline** · FluxKontext 与 Qwen-Image-Edit 原推理。
- **Benchmark** · PIEBench，测推理速度、编辑保真与未编辑区域。
- **关键结果 / 消融** · 平均加速 22.4%，高分辨率最高两倍。
- **适用条件 / 局限** · 依赖采样器及编辑器结构，极端编辑条件待核。

**可复用机制** · 对比固定比例剪枝和偏差引导剪枝，分别测修改区域和保留区域。

<a id="paper-155893"></a>

## Accelerated last-iterate convergence of Extragradient via power-law stepsizes

[官方论文页](https://neurips.cc/virtual/2026/poster/155893) · [作者来源](https://openreview.net/forum?id=22Ks9TPzvQ)

- **问题 / 瓶颈** · 固定步长 EG 在双线性问题上的末迭代收敛较慢。
- **核心创新 / 方法** · 用幂律调度控制步长，比较同一与不同步长。
- **Baseline** · 固定步长 EG、加入锚定的快率。
- **Benchmark** · 无约束双线性极小极大目标，末迭代速率。
- **关键结果 / 消融** · 共享步长达近三分之二指数，解耦后达近一阶。
- **适用条件 / 局限** · 理论局限于所述设定。

**可复用机制** · 在鞍点问题中对照共享和独立衰减的外推及更新步长。

<a id="paper-156738"></a>

## Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/156738) · [作者来源](https://neurips.cc/virtual/2026/poster/156738)

- **问题 / 瓶颈** · 自回归流逐变量生成限制推理并发。
- **核心创新 / 方法** · 将较高冗余层改用并行迭代，保留强依赖早期层。
- **Baseline** · 原逐步自回归生成。
- **Benchmark** · 若干离散正规化流任务，质量和推理速度。
- **关键结果 / 消融** · 报告最高 4.7 倍，理论分析在所设条件下给出迭代保证。
- **适用条件 / 局限** · 依赖实际层间冗余，硬件收益需另测。

**可复用机制** · 先测各层并行近似误差，再选择适合并行化的层。

<a id="paper-150025"></a>

## Accelerating LLM Pre-Training through Flat-Direction Dynamics Enhancement

[官方论文页](https://neurips.cc/virtual/2026/poster/150025) · [作者来源](https://openreview.net/forum?id=lKebtNgu8P)

- **问题 / 瓶颈** · 矩阵优化器的近各向同性更新对平坦方向偏保守。
- **核心创新 / 方法** · 通过黎曼动力学解释预条件与动量，沿平坦方向增强阻尼和学习率。
- **Baseline** · 以 Muon、SOAP 为底座做原方法对照。
- **Benchmark** · 130M–1.3B 稠密与 MoE，C4、Pile 和多种调度。
- **关键结果 / 消融** · 摘要报告对两优化器加速，量化幅度待核。
- **适用条件 / 局限** · 依赖可靠的方向识别，未见规模待核。

**可复用机制** · 固定优化器和预算，比较按方向调速与统一调速。

<a id="paper-149064"></a>

## Accelerating Neural Network Training with Augmented Koopman Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/149064) · [作者来源](https://openreview.net/forum?id=t9EhPQoOTT)

- **问题 / 瓶颈** · 只外推参数无法描述动量与自适应统计。
- **核心创新 / 方法** · 从跨步快照估计 Koopman 算子，并检验外推是否退化。
- **Baseline** · 不外推的 Adam、AdamW、动量 SGD 等。
- **Benchmark** · 多优化器达到目标精度所需反传次数和时间。
- **关键结果 / 消融** · 报告反传与耗时减少，数值待核。
- **适用条件 / 局限** · 需辨识可用算子，保护性校验成本待核。

**可复用机制** · 比较仅参数与含动量等状态的外推，并统计回退频率。

<a id="paper-151611"></a>

## Accelerating Rectified Flow Models  via Trajectory-Aware Caching

[官方论文页](https://neurips.cc/virtual/2026/poster/151611) · [作者来源](https://openreview.net/forum?id=ZFDg4T5AAg)

- **问题 / 瓶颈** · 直接复用速度在长跳步积累近似误差。
- **核心创新 / 方法** · 分解速度加速度，离线定跳步区间，在线用历史方向重建。
- **Baseline** · 既有缓存加速。
- **Benchmark** · BAGEL、FLUX.1-dev、Wan2.1-1.3B；速度与参考保真。
- **关键结果 / 消融** · 文生图最高 4.14 倍，文生视频最高 2.11 倍。
- **适用条件 / 局限** · 离线统计跨模型与生成分布稳定性待核。

**可复用机制** · 以同运行时间比较直接缓存和方向补偿缓存。

<a id="paper-153909"></a>

## Accelerating Safe Reinforcement Learning with Massive Parallelism

[官方论文页](https://neurips.cc/virtual/2026/poster/153909) · [作者来源](https://openreview.net/forum?id=Ho66oVFCDg)

- **问题 / 瓶颈** · 并行短轨迹不能直接代表全回合约束成本。
- **核心创新 / 方法** · 以错峰复位生成相位混合样本，聚合成本并依据不确定性收紧约束。
- **Baseline** · 非大规模并行安全强化学习。
- **Benchmark** · 基于 MJX 的 Safety Gym，训练时间与表现。
- **关键结果 / 消融** · 报告表现可比且显著缩短时间，数值待核。
- **适用条件 / 局限** · 依赖充分相位覆盖及偏移估计。

**可复用机制** · 监控短滚动覆盖的回合阶段，验证拼接估计与真实整回合之差。

<a id="paper-151472"></a>

## Accelerating Video Inverse Problem Solvers with Autoregressive Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151472) · [作者来源](https://openreview.net/forum?id=aLw0wVmMRl)

- **问题 / 瓶颈** · 整片恢复初始慢，逐步像素一致性需重复 VAE。
- **核心创新 / 方法** · 以测量一致估计初始化自回归恢复；快速版只约束首块。
- **Baseline** · 先进非自回归视频反演。
- **Benchmark** · 视频流式恢复，测首段时延、吞吐和质量。
- **关键结果 / 消融** · 首段时延从 114 到 4 秒，吞吐从 0.71 到 1.18 FPS；快速版在 4090 达 5.91 FPS。
- **适用条件 / 局限** · 只约束首块可能累积漂移。

**可复用机制** · 分开记录首块延迟与稳定吞吐，并扫描约束间隔。

<a id="paper-139678"></a>

## AccelEval: A Whole-Program Benchmark for LLM-Generated CPU-to-GPU Code Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/139678) · [作者来源](https://openreview.net/forum?id=AtjnWVu79Q)

- **问题 / 瓶颈** · 短内核评测遗漏整程序瓶颈。
- **核心创新 / 方法** · 用确定性判定、三种输入规模及相对最佳正确方案的速度指标，并提取赢家优化模式。
- **Baseline** · CPU、最佳正确方案及 11 项人写 CUDA 参考。
- **Benchmark** · 六领域 42 任务，八个模型及不同 GPU。
- **关键结果 / 消融** · H200 中等规模最强 pass@1 达 38/42；模式提示加速 1.78 倍，泛化提示为 1.18 倍。
- **适用条件 / 局限** · 最佳已知正确方案不是理论性能上界。

**可复用机制** · 将功能正确与速度分开报告，并按规模测通用与专门优化提示。

<a id="paper-149303"></a>

## AC/DC on a Budget -- Alternating Sparse Phases

[官方论文页](https://neurips.cc/virtual/2026/poster/149303) · [作者来源](https://openreview.net/forum?id=rD5TBB47Zb)

- **问题 / 瓶颈** · AC/DC 的稠密训练阶段消耗大量 FLOPs
- **核心创新 / 方法** · 观察重引入权重的高梯度与变号，以零初始化、掩码收敛早停和仅更新少量掩码外高梯度权重改进训练
- **Baseline** · AC/DC 与标准稀疏到稀疏算法
- **Benchmark** · CIFAR100、ImageNet，比较性能与 FLOPs
- **关键结果 / 消融** · ARC 以较少计算达到 AC/DC 表现；具体比例待核实
- **适用条件 / 局限** · 实际加速取决于稀疏计算实现

**可复用机制** · 以掩码收敛终止稠密阶段或直接进行稀疏重连

<a id="paper-150094"></a>

## ACD-GS: Asymmetric Curvature-aware Densification for 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/150094) · [作者来源](https://openreview.net/forum?id=kkbCZPoC5n)

- **问题 / 瓶颈** · 屏幕空间一阶梯度不能区分纹理与几何边界
- **核心创新 / 方法** · 以深度二阶响应不对称调控克隆、分裂，配合多视图一致性与容量调节
- **Baseline** · 梯度触发的 3DGS 增密与既有方法
- **Benchmark** · 多个新视角合成数据集；数据名待核实
- **关键结果 / 消融** · 高斯数量和存储减少近 60%，渲染保真仍有竞争力
- **适用条件 / 局限** · 依赖深度与多视图证据质量

**可复用机制** · 按深度曲率决定高斯克隆与分裂

<a id="paper-154560"></a>

## ACED-Bench: Evaluating How LLM Agents Acquire and Act on Causal Evidence

[官方论文页](https://neurips.cc/virtual/2026/poster/154560) · [作者来源](https://openreview.net/forum?id=CgjWoVkcgg)

- **问题 / 瓶颈** · 文本问答无法区分静态作答与主动因果调查
- **核心创新 / 方法** · 以隐藏概率图模型确定干预和答案，用自然语言描述环境，再用证据日志定位失败
- **Baseline** · 比较新旧语言模型和三种主动智能体设计
- **Benchmark** · ACED-CORE 180 题、ACED-QUAL 150 题
- **关键结果 / 消融** · 日志定位到干预选错、证据丢失和证据已足仍继续实验
- **适用条件 / 局限** · 形式环境中诊断未必代表真实科研

**可复用机制** · 用形式化世界检验智能体选实验、保留证据及停止的能力

<a id="paper-149362"></a>

## Achieving Directional-Stationarity from a Single Random Direction Step

[官方论文页](https://neurips.cc/virtual/2026/poster/149362) · [作者来源](https://openreview.net/forum?id=qblLv39mYL)

- **问题 / 瓶颈** · 常规算法只保证较弱驻点
- **核心创新 / 方法** · 抽样方向和步长，以函数值比较决定接受
- **Baseline** · 原优化器、DCA 和近端线性方案
- **Benchmark** · 约束非光滑非凸优化下的理论与数值实验
- **关键结果 / 消融** · 积聚点几乎必然方向驻定，所分析基础方法的收敛速率可保持
- **适用条件 / 局限** · 依赖局部 Lipschitz 性和方向导数连续性

**可复用机制** · 用一次随机方向探索增强现有优化法的方向驻点保证

<a id="paper-151784"></a>

## A Closer Look at Dynamic Scene Graph Generation in the Era of Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151784) · [作者来源](https://openreview.net/forum?id=Y1D9E4ZhwT)

- **问题 / 瓶颈** · 召回导向指标会奖励过多重复或无关关系
- **核心创新 / 方法** · 增加四个指标，并将逐帧预测变为时序关系集合预测
- **Baseline** · 自底向上的动态场景图方法
- **Benchmark** · Action Genome、VidVRD、PVSG
- **关键结果 / 消融** · 作者报告多指标上改善；各模块增益待核实
- **适用条件 / 局限** · 指标是否反映部署任务效用待验证

**可复用机制** · 动态场景图同时测关系精度、信息量与重复

<a id="paper-150815"></a>

## A Communication-Theoretic Framework for LLM Agents: Cost-Aware Adaptive Reliability

[官方论文页](https://neurips.cc/virtual/2026/poster/150815) · [作者来源](https://openreview.net/forum?id=f9YBAJGutx)

- **问题 / 瓶颈** · 固定模型和推理预算无法跨任务支配其他选择
- **核心创新 / 方法** · 将采样视为随机信道，建立质量和成本可调的语义近邻路由
- **Baseline** · 固定模型、技术与预算，以及单次解码
- **Benchmark** · 69 项困难任务与 MMLU、GSM8K、HumanEval 困难子集 300 题
- **关键结果 / 消融** · 同等质量归一化成本约低 56%，同等成本质量约高 7%
- **适用条件 / 局限** · 路由依赖邻近任务的经验，域外效果待核实

**可复用机制** · 按任务难度决定重试、投票或迭代验证的预算

<a id="paper-155971"></a>

## A Compass for Useful Data: Online Data Selection via Alignment-Gated Fisher Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/155971) · [作者来源](https://openreview.net/forum?id=1Sqambi1v4)

- **问题 / 瓶颈** · 损失或梯度范数忽略更新方向和冗余
- **核心创新 / 方法** · Fisher 白化后用下降方向门控，以对数行列式度量批内更新张成空间
- **Baseline** · 在线选样基线，具名方法待核实
- **Benchmark** · 等预算监督微调，比较任务表现
- **关键结果 / 消融** · 报告一致优于所比基线，贪心批选择有常数近似保证
- **适用条件 / 局限** · 依赖 Fisher 与下降方向估计质量

**可复用机制** · 结合更新效用、下降方向和批内互补性来分配训练预算

<a id="paper-153293"></a>

## A Comprehensive View of Fairness through Distributional Stability

[官方论文页](https://neurips.cc/virtual/2026/poster/153293) · [作者来源](https://openreview.net/forum?id=MKUF4BK3dQ)

- **问题 / 瓶颈** · 固定数据分布的公平结论可能被人口组成变化破坏
- **核心创新 / 方法** · 把公平特性表述为预测比例对群体组成扰动的 Lipschitz 稳定性，以二阶锥规划混合重加权预测器
- **Baseline** · 经典公平定义作为理论特例；实验对照待核实
- **Benchmark** · 敏感属性组成变化下的理论与标准数据实验
- **关键结果 / 消融** · 给出统一于一组组成扰动的保证与泛化界
- **适用条件 / 局限** · 保证随扰动集合定义变化

**可复用机制** · 在多种人群配比下联合报告公平性而非单一测试分布

<a id="paper-155175"></a>

## A Computational Perspective to Data Ablation Experiments

[官方论文页](https://neurips.cc/virtual/2026/poster/155175) · [作者来源](https://openreview.net/forum?id=7jrxR7M4di)

- **问题 / 瓶颈** · 按经验分配消融轮数，无法预估改进收益
- **核心创新 / 方法** · 用零阶遗憾分析解释最优配方质量随消融次数的幂律，并求质量和数量权衡
- **Baseline** · DCLM 等启发式数据流程
- **Benchmark** · 预训练、监督微调、偏好优化与强化学习
- **关键结果 / 消融** · 作者报告跨阶段验证幂律并取得更好的经验帕累托前沿
- **适用条件 / 局限** · 幂律系数和外推范围需按阶段重新估计

**可复用机制** · 固定算力时联合分配数据配方搜索与最终训练预算

<a id="paper-139542"></a>

## AcousticBench: Measuring Acoustic Perception in Large Audio Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139542) · [作者来源](https://openreview.net/forum?id=JstO542VtE)

- **问题 / 瓶颈** · 混合评测难排除转写捷径
- **核心创新 / 方法** · 构造音量、语音情绪和相对质量二选一任务
- **Baseline** · ASR 级联、人类与 15 个模型
- **Benchmark** · AcousticBench 3200 题
- **关键结果 / 消融** · 转写级联接近随机，领先模型仍落后人类
- **适用条件 / 局限** · 主要测二选一

**可复用机制** · 增加转写对照检验音频基准是否依赖非词汇信息。

<a id="paper-139556"></a>

## Acting without Knowing: Planning, Prediction, and Transfer Dissociate in Interactive Visual Physics

[官方论文页](https://neurips.cc/virtual/2026/poster/139556) · [作者来源](https://openreview.net/forum?id=IoODzTVUwp)

- **问题 / 瓶颈** · 任务完成会掩盖物理理解不足
- **核心创新 / 方法** · 在共享物理谜题上对照迭代放置与反事实预测
- **Baseline** · 人类与被测多模态模型
- **Benchmark** · 虚拟物理谜题
- **关键结果 / 消融** · 成功行动未伴随稳定预测与迁移
- **适用条件 / 局限** · 结果依赖所测场景

**可复用机制** · 固定场景拆开评估预测和控制。

<a id="paper-154625"></a>

## Action Chunking Proximal Policy Optimization with Feedback Correction

[官方论文页](https://neurips.cc/virtual/2026/poster/154625) · [作者来源](https://openreview.net/forum?id=CBSS9HNaVp)

- **问题 / 瓶颈** · 动作块难估 Q 且开环不够灵活
- **核心创新 / 方法** · PPO actor 计划一段动作，逐步反馈模块在线修正
- **Baseline** · 分块和常规强化学习方案
- **Benchmark** · IsaacGym 与 Bi-DexHands 25 项仿真任务
- **关键结果 / 消融** · 中等长度更优，修正器正则平衡反馈与规划
- **适用条件 / 局限** · 真机待核实

**可复用机制** · 把块长度与反馈正则作为独立消融变量。

<a id="paper-153538"></a>

## Action-Level Behavior Policy Optimization for Variance-Reduced Policy Gradients

[官方论文页](https://neurips.cc/virtual/2026/poster/153538) · [作者来源](https://openreview.net/forum?id=KbaSvFaIVV)

- **问题 / 瓶颈** · 固定行为策略时估计器不能控制全部方差
- **核心创新 / 方法** · 分解重要性采样梯度的状态与动作方差，对动作项求最优提议
- **Baseline** · 同策略采样
- **Benchmark** · 非凸 SGD 收敛界与经验样本效率
- **关键结果 / 消融** · 精确价值与采样下动作相关时得到更紧上界
- **适用条件 / 局限** · 实际需近似价值及行为参数化

**可复用机制** · 先测动作条件梯度贡献，再决定是否改变采样。

<a id="paper-151058"></a>

## Active Context Selection Improves Simple Regret in Contextual Bandits

[官方论文页](https://neurips.cc/virtual/2026/poster/151058) · [作者来源](https://openreview.net/forum?id=dJqzCskE60)

- **问题 / 瓶颈** · 按自然人群比例抽样不保证最低简单遗憾
- **核心创新 / 方法** · 求解有限上下文设定中的紧界及采样分配
- **Baseline** · 被动上下文采样
- **Benchmark** · 已知人群权重下的加权简单遗憾
- **关键结果 / 消融** · 改善最大可达上下文数四分之一次幂量级
- **适用条件 / 局限** · 要求可以主动选择上下文

**可复用机制** · 当可控制招募来源时对照自然比例与幂律分配。

<a id="paper-149573"></a>

## Active Probabilistic Reasoning in Humans and LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149573) · [作者来源](https://openreview.net/forum?id=p8XR2JNWfi)

- **问题 / 瓶颈** · 总分掩盖推理在哪一环有效
- **核心创新 / 方法** · 构建主动概率推理任务并拟合可解释行为模型
- **Baseline** · 人类、语言模型和最优参考策略
- **Benchmark** · 测采样策略与推断决策
- **关键结果 / 消融** · 延长推理主要帮助推断，主动采样收益较小
- **适用条件 / 局限** · 结论受任务所定义的证据过程限制

**可复用机制** · 评估工具型代理时固定证据测推断，再独立比较选取证据。

<a id="paper-155159"></a>

## ActQuant: Sub-4-bit Action-Guided Quantization for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155159) · [作者来源](https://openreview.net/forum?id=7qAjVpGyah)

- **问题 / 瓶颈** · 低位宽误差不均匀地伤害控制
- **核心创新 / 方法** · 跨张量按动作贡献分位宽，块内由动作曲率调尺度
- **Baseline** · 半精度 OpenVLA-OFT 与 π0.5
- **Benchmark** · LIBERO 与 UR3 真机成功率
- **关键结果 / 消融** · 3 bit 时两模型成功率为 94.95% 和 94.8%，骨干显存最多降至约五分之一
- **适用条件 / 局限** · 需代表性动作校准数据

**可复用机制** · 以闭环动作成功衡量量化方案并分开消融位宽和块尺度。

<a id="paper-153013"></a>

## Act, Validate, Adapt: Closing the Causal Discovery-Control Loop

[官方论文页](https://neurips.cc/virtual/2026/poster/153013) · [作者来源](https://openreview.net/forum?id=OdP0tR9M9Z)

- **问题 / 瓶颈** · 观察数据拟合的图可能漏掉运行中的因果变化
- **核心创新 / 方法** · 执行动作验证候选边，再用该图优化及监测运行模式
- **Baseline** · 仅观察图与固定图重拟合
- **Benchmark** · 建筑能耗仿真及物理试验台
- **关键结果 / 消融** · 仿真能耗减 21%，模式识别 61.2% 到 80.8%
- **适用条件 / 局限** · 需可执行和测量的干预

**可复用机制** · 比较固定图重估参数与干预删边以识别收益来源。

<a id="paper-148821"></a>

## AdaCodec: A Predictive Visual Code for Video MLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148821) · [作者来源](https://openreview.net/forum?id=utdVAXHnlv)

- **问题 / 瓶颈** · 逐帧 RGB 造成视觉 token 冗余
- **核心创新 / 方法** · 预测代价高时传参考帧，其余以变化和残差编码
- **Baseline** · Qwen3-VL-8B 逐帧基线
- **Benchmark** · 11 个视频基准
- **关键结果 / 消融** · 在长视频任务用 32k token 超过 224k 基线，首 token 时间 9.26 降到 1.62 秒
- **适用条件 / 局限** · 突变及细粒度残差的信息保留待核

**可复用机制** · 固定视觉预算比较帧采样与时序残差编码。

<a id="paper-155834"></a>

## AdaMAP: Learning Adaptive Multi-Action Prediction with Grounded Dreaming Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/155834) · [作者来源](https://openreview.net/forum?id=2Wzu7RgcCE)

- **问题 / 瓶颈** · 逐步动作可复制历史而固定动作块会累积误差
- **核心创新 / 方法** · 联合预测可变长度动作块与提供未来约束的视觉预测
- **Baseline** · 单动作与固定块
- **Benchmark** · 数字游戏轨迹
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 依赖预测画面提供有效约束

**可复用机制** · 让动作块自行决定何时重新观察，比较收益与适用条件。

<a id="paper-151271"></a>

## Adam under Generalized Smoothness with Second-Moment-Type Stochastic Gradients

[官方论文页](https://neurips.cc/virtual/2026/poster/151271) · [作者来源](https://openreview.net/forum?id=bchuh1xaSe)

- **问题 / 瓶颈** · 广义光滑分析常采用强尾假设
- **核心创新 / 方法** · 使用 Adam 自归一化建立广义光滑下的收敛
- **Baseline** · 几乎处处有界或次高斯的既有分析
- **Benchmark** · 广义光滑目标的理论收敛
- **关键结果 / 消融** · 证明仅二阶矩条件下可建立收敛
- **适用条件 / 局限** · 需核具体广义光滑指数与算法参数

**可复用机制** · 检查随机梯度二阶矩与自归一化而非先假设轻尾，比较收益与适用条件。

<a id="paper-152734"></a>

## AdaOcc: Adaptive 3D Occupancy Prediction for Embodied Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/152734) · [作者来源](https://openreview.net/forum?id=QlTrxoZXUR)

- **问题 / 瓶颈** · 传感配置及预算会变化
- **核心创新 / 方法** · 几何引导双分支接入不同视角或深度来源，以稀疏语义点渐进查询
- **Baseline** · 固定配置占据方法
- **Benchmark** · 三维语义占据
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 误差随传感器和预算变化

**可复用机制** · 以渐进查询数量调节占据预测预算，比较收益与适用条件。

<a id="paper-153769"></a>

## AdaPaD: Adaptive Parallel Deflation for PEFT with Self-Correcting Rank Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/153769) · [作者来源](https://openreview.net/forum?id=IneMjsFM6P)

- **问题 / 瓶颈** · 顺序提取会冻结早期误差
- **核心创新 / 方法** · 每个秩一分量使用前序分量最新估计更新目标，再共享预算动态加秩
- **Baseline** · 预设秩联合 LoRA 与顺序消去
- **Benchmark** · 低秩分量学习及语言模型适配
- **关键结果 / 消融** · 作者描述消去误差随迭代收敛
- **适用条件 / 局限** · 适用假设与并行开销需核

**可复用机制** · 并行修正低秩分量并按重要性增长模块秩，比较收益与适用条件。

<a id="paper-150939"></a>

## AdapMatch: Adaptive Bias Decoupling for Semi-Supervised Partial Label Learning under Unknown Class Distributions

[官方论文页](https://neurips.cc/virtual/2026/poster/150939) · [作者来源](https://openreview.net/forum?id=eAtYtntHfU)

- **问题 / 瓶颈** · 多数类在筛选和消歧环节自我强化
- **核心创新 / 方法** · 将两类相互强化的偏差分别建模并校正
- **Baseline** · 隐含类别均衡的半监督偏标签方法
- **Benchmark** · 未知无标签类别比例下的偏标签学习
- **关键结果 / 消融** · 理论揭示两种偏差相互强化
- **适用条件 / 局限** · 纠偏需足够可靠的类别估计

**可复用机制** · 分别监控伪标签入选偏差与候选集消歧偏差，比较收益与适用条件。

<a id="paper-155053"></a>

## AdaPreLoRA: Adafactor Preconditioned Low-Rank Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/155053) · [作者来源](https://openreview.net/forum?id=8o83y7bppR)

- **问题 / 瓶颈** · 低秩因子化的映射雅可比秩不足
- **核心创新 / 方法** · 按权重空间预条件器和因子空间可逆代理统一 LoRA 优化器
- **Baseline** · 因子自适应、块对角、伪逆与黎曼路线
- **Benchmark** · 低秩适配的优化比较
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 代理选择引入近似误差

**可复用机制** · 选择可逆的因子空间预条件近似，比较收益与适用条件。

<a id="paper-151417"></a>

## Adaptive and Neutral Theory of Evolution Strategies for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151417) · [作者来源](https://openreview.net/forum?id=apl2nYU8FS)

- **问题 / 瓶颈** · 经典零阶理论缺少对小种群和先升后降的解释
- **核心创新 / 方法** · 用连续时间随机微分方程分析奖励方差与局部低秩曲率
- **Baseline** · 经典零阶优化分析
- **Benchmark** · 合成实验和语言模型微调
- **关键结果 / 消融** · 解释小种群有效、奖赏回落及预训练能力遗忘
- **适用条件 / 局限** · 局部低秩 Hessian 假设需检查

**可复用机制** · 分阶段评估归一化进化策略的收益与遗忘，比较收益与适用条件。

<a id="paper-154700"></a>

## Adaptive auditing of AI systems with anytime-valid guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/154700) · [作者来源](https://openreview.net/forum?id=Bfz7nxHizI)

- **问题 / 瓶颈** · 固定样本假设在自适应审计中失效
- **核心创新 / 方法** · 将模型侧和审计方的原假设分别形式化并构造任意时点有效的检验
- **Baseline** · 固定样本评估
- **Benchmark** · 小样本、序贯采样和可选停测
- **关键结果 / 消融** · 作者给出自适应推断框架
- **适用条件 / 局限** · 仍需明确审计阈值和检验条件

**可复用机制** · 让中途决定采样和停测仍支持有效检验，比较收益与适用条件。

<a id="paper-151966"></a>

## Adaptive Calibration in Non-Stationary Environments

[官方论文页](https://neurips.cc/virtual/2026/poster/151966) · [作者来源](https://openreview.net/forum?id=WTLTiMlgq3)

- **问题 / 瓶颈** · 最坏情形校准策略可能对近稳定环境过于保守
- **核心创新 / 方法** · 构造适应未知非平稳度的在线校准算法
- **Baseline** · 独立同分布与全对抗保证
- **Benchmark** · 序贯预测，非平稳度为均值偏差指标
- **关键结果 / 消融** · 作者给出按漂移程度插值的保证
- **适用条件 / 局限** · 不同误差度量下速率和适用条件需区分

**可复用机制** · 使误校准上界随环境漂移而变，比较收益与适用条件。

<a id="paper-149196"></a>

## Adaptive Communication Range for Scalable Cooperative Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149196) · [作者来源](https://openreview.net/forum?id=sBj2Ls9x9u)

- **问题 / 瓶颈** · 全局筛选与固定图妨碍扩展
- **核心创新 / 方法** · 通信策略先决定范围，行为策略接收由此形成的邻域观测
- **Baseline** · 固定通信关系与基于全局状态筛选
- **Benchmark** · 通信约束下的合作多智能体学习
- **关键结果 / 消融** · 作者给出受约束的单调改进保证
- **适用条件 / 局限** · 邻域形成机制及预算条件影响复用

**可复用机制** · 先预算内选通信范围再基于实际邻域行动，比较收益与适用条件。

<a id="paper-148937"></a>

## Adaptive Conditional Gradient Sliding: Projection-Free and Line-Search-Free Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/148937) · [作者来源](https://openreview.net/forum?id=u4sFmbwanR)

- **问题 / 瓶颈** · 投影昂贵，线搜索增加成本
- **核心创新 / 方法** · 加速外层用局部 Lipschitz 估计调步长，并由线性预言机实现有控制误差的内层
- **Baseline** · 依赖投影的方法
- **Benchmark** · 紧凸可行域上的理论函数收敛
- **关键结果 / 消融** · 给出凸加速及局部强凸下线性收敛
- **适用条件 / 局限** · 需可用线性最小化预言机

**可复用机制** · 外层梯度复用多次线性预言机调用，比较收益与适用条件。

<a id="paper-156121"></a>

## Adaptive Coordinate Transforms for Neural Operators

[官方论文页](https://neurips.cc/virtual/2026/poster/156121) · [作者来源](https://openreview.net/forum?id=0FTnHtuj1L)

- **问题 / 瓶颈** · 固定欧拉格点使移动结构不对齐
- **核心创新 / 方法** · 学习局部坐标变换并用可微采样重写特征
- **Baseline** · 固定坐标神经算子
- **Benchmark** · 含移动结构和尖锐界面的 PDE
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 采样与变换变形过大时需检查保真度

**可复用机制** · 根据特征变换坐标后再做算子计算，比较收益与适用条件。

<a id="paper-153654"></a>

## Adaptive Fine-Tuning Scheduler for Multi-Tenant Edge LLM via Convergence-Aware Bandits

[官方论文页](https://neurips.cc/virtual/2026/poster/153654) · [作者来源](https://openreview.net/forum?id=JjNnUtfLn8)

- **问题 / 瓶颈** · 饱和与低潜力租户会被普通赌博机混淆
- **核心创新 / 方法** · 以窗口和收敛感知的置信上界分配顺序微调机会
- **Baseline** · 标准多臂赌博机
- **Benchmark** · 有限 GPU 显存的多租户 LoRA 调度
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 依赖适配器增益呈阶段性收敛

**可复用机制** · 减少给已收敛适配器分配更新，比较收益与适用条件。

<a id="paper-152362"></a>

## Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/152362) · [作者来源](https://openreview.net/forum?id=Tcux9XpSfo)

- **问题 / 瓶颈** · 分数排序无法直接说明核验的边际收益
- **核心创新 / 方法** · 建立首个成功样本的成本搜索问题，以分段自适应策略处理未知分数分布
- **Baseline** · 固定生成数量及已知分布最优策略
- **Benchmark** · 数学与代码的昂贵核验设置
- **关键结果 / 消融** · 作者以动态规划刻画已知分布策略
- **适用条件 / 局限** · 关注固定提示及首个成功，评分漂移须重估

**可复用机制** · 按便宜评分的条件成功率决定是否付费核验，比较收益与适用条件。

<a id="paper-152986"></a>

## Adaptive Internal Readout for Native Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152986) · [作者来源](https://openreview.net/forum?id=OqX7hyaqf9)

- **问题 / 瓶颈** · 任务信息可能较早出现但无法被最终输出读取
- **核心创新 / 方法** · 以末层同等容量对照量化差距，再由轻量策略动态选择少数内层位点
- **Baseline** · 仅末层读取、静态及稠密融合
- **Benchmark** · 文档、图表、图解、计数和组合推理
- **关键结果 / 消融** · 作者报告匹配预算下缩小差距
- **适用条件 / 局限** · 需白盒访问内部状态且泛化受读出监督影响

**可复用机制** · 固定读出预算比较内部位点与末层，比较收益与适用条件。

<a id="paper-152859"></a>

## Adaptive LLM Routing for Multi-Turn Conversations with Continuously Evolving User Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/152859) · [作者来源](https://openreview.net/forum?id=PrL4Tfo9jW)

- **问题 / 瓶颈** · 逐轮路由忽略延迟收益。
- **核心创新 / 方法** · 用 MCTS 构造高累计奖励对话，再蒸馏轻量路由并检索近似未来状态。
- **Baseline** · 单一模型和既有路由器
- **Benchmark** · 开放域与专用多轮对话成功率、成本
- **关键结果 / 消融** · 作者报告成功率及性能成本折衷改善。
- **适用条件 / 局限** · 离线树搜索成本与用户分布偏移待核。

**可复用机制** · 用多轮累计奖励生成路由监督，在线以轻量模型替代搜索。

<a id="paper-149625"></a>

## Adaptively Incorporating Directional Hints into Zeroth-Order Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149625) · [作者来源](https://openreview.net/forum?id=ofyCInS0Mr)

- **问题 / 瓶颈** · 代理梯度方向可能逐步失准。
- **核心创新 / 方法** · 把方向提示写入控制变量，自适应设参考向量和步长。
- **Baseline** · 标准零阶下降和既有引导法
- **Benchmark** · 模拟科学优化任务及收敛阶
- **关键结果 / 消融** · 实用版在对数因子内匹配 oracle，理论阶在一阶与零阶之间插值。
- **适用条件 / 局限** · 需要低成本方向提示，效果依赖其沿轨迹质量。

**可复用机制** · 让不可靠梯度提示作为降方差项，对照强制沿提示更新。

<a id="paper-152306"></a>

## Adaptive Multi-Frame Learning for Expressive and Stable Atomic Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/152306) · [作者来源](https://openreview.net/forum?id=U3iPm0WWuK)

- **问题 / 瓶颈** · 单一原子局部坐标对异质结构表达不足，近退化时不稳。
- **核心创新 / 方法** · 按原子环境混合多个等变坐标参考，并降低低质量参考权重。
- **Baseline** · 单帧及其他晶体预测方法
- **Benchmark** · 晶体性质、受坐标连续性影响的力预测
- **关键结果 / 消融** · 作者报告自适应多帧带来一致收益。
- **适用条件 / 局限** · 依赖参考质量权重是否反映近退化风险。

**可复用机制** · 把几何参考的质量作为聚合输入，并在高对称区域专门测稳定性。

<a id="paper-149265"></a>

## Adaptive multiscale operator correction via learned spectral subspace and physics-informed optimization.

[官方论文页](https://neurips.cc/virtual/2026/poster/149265) · [作者来源](https://openreview.net/forum?id=rbb6tqGnFf)

- **问题 / 瓶颈** · 神经算子粗解难以恢复高频局部结构。
- **核心创新 / 方法** · 把粗解投影到实例自适应的小波或傅里叶子空间，按解析基函数导数最小化物理残差。
- **Baseline** · FNO
- **Benchmark** · 热、Poisson、Darcy、Helmholtz 方程及分布外误差
- **关键结果 / 消融** · 相较 FNO 最高降低约四个数量级误差。
- **适用条件 / 局限** · 需已知方程残差和合适基函数，额外优化成本待核。

**可复用机制** · 冻结粗算子后只在稀疏谱子空间做物理校正。

<a id="paper-153985"></a>

## Adaptive Robust Estimator for Policy Optimization in Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153985) · [作者来源](https://openreview.net/forum?id=H47ygC2MKi)

- **问题 / 瓶颈** · 偏态或重尾奖励让组均值失真。
- **核心创新 / 方法** · 用两级稳健位置估计替代 GRPO 经验均值。
- **Baseline** · GRPO 式经验均值中心化
- **Benchmark** · 数学推理、单及多 Agent、视觉语言导航
- **关键结果 / 消融** · 作者报告噪声及分布外条件收益更明显，并给高概率偏差界。
- **适用条件 / 局限** · 需区分异常奖励与真实稀有高价值信号。

**可复用机制** · 通过奖励污染扫描比较稳健中心与样本均值。

<a id="paper-153394"></a>

## Adaptive Stepsizes for Eligibility Traces in Deep Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153394) · [作者来源](https://openreview.net/forum?id=LfxKFrgnlA)

- **问题 / 瓶颈** · 向量学习率难与资格迹的前向后向等价兼容。
- **核心创新 / 方法** · 重新设计迹中逐坐标学习率的位置及更新规则。
- **Baseline** · 其他流式算法、PPO
- **Benchmark** · MuJoCo、MinAtar
- **关键结果 / 消融** · 摘要报告优于其他流式方法，并与使用回放的方法表现可比。
- **适用条件 / 局限** · 跨环境的学习率敏感性待核。

**可复用机制** · 改变资格迹中的学习率前先核对前后向等价条件。

<a id="paper-150536"></a>

## AdaptNC: Adaptive Nonconformity Scores for Conformal Prediction under Distribution Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/150536) · [作者来源](https://openreview.net/forum?id=hPSiFtFpGw)

- **问题 / 瓶颈** · 固定非一致性分数使分布偏移时预测区域过大。
- **核心创新 / 方法** · 联合调整分数参数和阈值，重加权训练并用回放缓和过渡。
- **Baseline** · 仅调阈值的在线共形预测
- **Benchmark** · 机器人策略、环境、传感变化；区域体积与覆盖率
- **关键结果 / 消融** · 报告在维持目标覆盖时缩小区域。
- **适用条件 / 局限** · 变化过快时回放可能滞后。

**可复用机制** · 同时更新预测集合形状与大小，并专门测切换期覆盖。

<a id="paper-150868"></a>

## AdaState: Self-Evolving Anchors for Streaming Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150868) · [作者来源](https://openreview.net/forum?id=elLf1P8oAQ)

- **问题 / 瓶颈** · 初帧在缓存中吸收过多注意力，锁住动态。
- **核心创新 / 方法** · 以每个生成块相同的相对位置结构让 KV 锚随内容递推。
- **Baseline** · 固定初始帧的自回归视频扩散
- **Benchmark** · 流式视频动态与场景演变
- **关键结果 / 消融** · 摘要报告动作更丰富，数值待核。
- **适用条件 / 局限** · 长期递推可能积累错误。

**可复用机制** · 对比固定视觉锚与可演进锚，并同时测运动和身份漂移。

<a id="paper-151941"></a>

## AdaWM: Few-Shot Adaptation of World Models to Unseen Dynamical Regimes

[官方论文页](https://neurips.cc/virtual/2026/poster/151941) · [作者来源](https://openreview.net/forum?id=Wg09sf4Nj0)

- **问题 / 瓶颈** · 少量新环境转移不足以稳定微调整个模型。
- **核心创新 / 方法** · 用少量示例推断动态条件，经 FiLM 调节模型而不执行梯度步。
- **Baseline** · 微调、MAML、较大 JEPA
- **Benchmark** · 未见动力学域下预测误差
- **关键结果 / 消融** · 五个示例最高降误差 15%；更大 JEPA 微调有 40% 退化实例。
- **适用条件 / 局限** · 示例需能区分新动力模式。

**可复用机制** · 先测试按转移示例条件化，再决定是否扩大容量或微调。

<a id="paper-152426"></a>

## Addressable Memory for Video World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152426) · [作者来源](https://openreview.net/forum?id=TCL6m7hsBg)

- **问题 / 瓶颈** · 压缩缓存仍可能因时间位置超出训练范围而无法回忆。
- **核心创新 / 方法** · 给压缩槽相对当前帧固定的有效位置；用字段聚合或边界地标分别供连贯和回忆。
- **Baseline** · 固定滑动窗及保留越界位置的压缩缓存
- **Benchmark** · 超出训练时域的滚动与 TempSSIM
- **关键结果 / 消融** · 越界时压缩与滑窗表现相同；有效寻址的字段版提升 TempSSIM 15.5%。
- **适用条件 / 局限** · 位置因果证据限所测架构。

**可复用机制** · 将缓存保留内容与位置编码分别做干预。

<a id="paper-149019"></a>

## Addressing Exogenous Variability in Cooperative Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149019) · [作者来源](https://openreview.net/forum?id=tS7YfNAPfZ)

- **问题 / 瓶颈** · 外部环境转移会间接受团队历史行动影响。
- **核心创新 / 方法** · 分解内生和外生上下文，用延迟影响强度给内在奖励加权。
- **Baseline** · 已有集中训练分散执行方法
- **Benchmark** · SMAX 对手策略偏移与未见对手
- **关键结果 / 消融** · 报告训练及泛化同时改善。
- **适用条件 / 局限** · 需能推断外生因素及其延迟影响。

**可复用机制** · 区分直接控制变量与间接影响变量后再给奖励塑形。

<a id="paper-150071"></a>

## Addressing Sparse-Rewards in RL with Scalable Hierarchical Novel Eigen Options

[官方论文页](https://neurips.cc/virtual/2026/poster/150071) · [作者来源](https://openreview.net/forum?id=ky5vzGwUTU)

- **问题 / 瓶颈** · 精确图谱选项难扩展到高维像素。
- **核心创新 / 方法** · 用新颖度加权连续 Laplacian 图绘制近似适合远程探索的选项。
- **Baseline** · 可扩展 Laplacian 选项、直接 NEO 扩展
- **Benchmark** · Montezuma、Venture 及七个困难 ProcGen 游戏
- **关键结果 / 消融** · Montezuma 回报约两者 1.8 倍；Venture 达 1135，对照近零。
- **适用条件 / 局限** · 对新颖度代理和选项长度敏感。

**可复用机制** · 用访问稀少程度塑造可扩展的时序探索选项。

<a id="paper-152302"></a>

## AdERA: Adaptive Exponent Reuse for Lossless Allgather in Sharded MoE Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152302) · [作者来源](https://openreview.net/forum?id=U4htEskiXj)

- **问题 / 瓶颈** · MoE 参数重建前 Allgather 昂贵，有损方案改变数值。
- **核心创新 / 方法** · 复用稳定权重指数，只在预测可省时的层压缩，并与通信重叠。
- **Baseline** · 有损及无损 Allgather 压缩
- **Benchmark** · 真机多 GPU 与轨迹驱动模拟，测加速和按位重建
- **关键结果 / 消融** · 相对无损基线 16 GPU 加速 3.70 倍；128 GPU 数值是模拟预测。
- **适用条件 / 局限** · 依赖指数稳定性和张量形状。

**可复用机制** · 先量化跨步指数重复率，再按每层通信收益选择是否压缩。

<a id="paper-148597"></a>

## Ad-Hoc Teamwork from Human Demonstrations

[官方论文页](https://neurips.cc/virtual/2026/poster/148597) · [作者来源](https://openreview.net/forum?id=wYE8NC5FXe)

- **问题 / 瓶颈** · 从混合演示拟合的代理队友会集中到主流协作惯例。
- **核心创新 / 方法** · 从无标签轨迹恢复多个潜在惯例，用离线校准的 KL 正则 PPO 重建代理。
- **Baseline** · 汇总行为克隆衍生代理
- **Benchmark** · Hanabi 与代理队友下的智能体排序
- **关键结果 / 消融** · 潜在代理组改变相对排序，揭示传统代理集中性。
- **适用条件 / 局限** · 主要证据来自 Hanabi，潜状态与真实惯例未必一一对应。

**可复用机制** · 用多个潜惯例构造评测队友，检查单一代理下的排序是否稳定。

<a id="paper-149490"></a>

## A Differentiable 3D Scene Graph Metric via Contextual Hellinger Triplet Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/149490) · [作者来源](https://openreview.net/forum?id=plEkglzKmI)

- **问题 / 瓶颈** · 逐项分类对关系错误区分不足
- **核心创新 / 方法** · 把物体和谓词分布组合成上下文三元组并施加可微距离
- **Baseline** · 局部分类损失
- **Benchmark** · 3DSSG 与图条件场景生成
- **关键结果 / 消融** · 摘要报告生成改善及图级项互补
- **适用条件 / 局限** · 依赖图对齐

**可复用机制** · 固定网络加入关系级指标并消融

<a id="paper-151819"></a>

## A Differentiable Interior-Point Method in Single Precision

[官方论文页](https://neurips.cc/virtual/2026/poster/151819) · [作者来源](https://openreview.net/forum?id=Xjh9eUGXeN)

- **问题 / 瓶颈** · 内点系统近解病态
- **核心创新 / 方法** · 改写互补条件以保持线性系统谱有界
- **Baseline** · 标准内点法
- **Benchmark** · 双层及端到端学习
- **关键结果 / 消融** · 单精度可稳定求解及求导
- **适用条件 / 局限** · 适用约束类别待全文核实

**可复用机制** · 以梯度误差和条件数比较求解器

<a id="paper-155533"></a>

## ADMIT: Support-Gated Memory-Write Admission for Document QA Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/155533) · [作者来源](https://openreview.net/forum?id=4sP52RCwde)

- **问题 / 瓶颈** · 缺证据内容写入后影响检索
- **核心创新 / 方法** · 词面支持检查失败时拒写记忆，允许回答走回退路径
- **Baseline** · 仅检查最终输出及开放写入
- **Benchmark** · M3DocVQA及三种代理压力测试
- **关键结果 / 消融** · 构造的词面污染为零，最终检查基线仍有 12%–32%
- **适用条件 / 局限** · 词面匹配不能保证语义真实性

**可复用机制** · 分别统计记忆污染与答案准确率

<a id="paper-152568"></a>

## Advanced Routing as Regularization Allocation for Efficient Diffusion Transformer Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152568) · [作者来源](https://openreview.net/forum?id=S8tvv8HOHm)

- **问题 / 瓶颈** · 固定路由忽视不同时间步需求
- **核心创新 / 方法** · 将随机路由视为隐式正则，对高噪声使用更强路由
- **Baseline** · TREAD 固定随机路由
- **Benchmark** · 视觉扩散模型训练
- **关键结果 / 消融** · 作者报告改善训练效率，细节待核
- **适用条件 / 局限** · 依赖噪声与梯度稳定性的关系

**可复用机制** · 等预算对照固定和噪声条件路由

<a id="paper-150862"></a>

## Advancing Entropy-Level Credit Assignment in RLVR via Proximal Entropy Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150862) · [作者来源](https://openreview.net/forum?id=enmugrKvYL)

- **问题 / 瓶颈** · 全局熵混入提示和位置差异
- **核心创新 / 方法** · 以邻近 token 的熵作参照构造近端熵权重
- **Baseline** · GRPO 及熵基线
- **Benchmark** · 三种底座的数学推理
- **关键结果 / 消融** · 报告优于对照且可迁移其他更新法
- **适用条件 / 局限** · 窗口和跨任务效果待核

**可复用机制** · 固定 rollout 比较局部与全局熵权重

<a id="paper-148631"></a>

## Advectra: Asymmetric Latent Transport for Non-Stationary Physics

[官方论文页](https://neurips.cc/virtual/2026/poster/148631) · [作者来源](https://openreview.net/forum?id=wJA5smlez3)

- **问题 / 瓶颈** · 固定坐标系难跟踪移动结构
- **核心创新 / 方法** · 正则化坐标映射解耦源和目标，以近共动系聚合与重建
- **Baseline** · 几何约束与无形态约束模型
- **Benchmark** · 被动标量输运及 Rayleigh–Taylor 不稳定性
- **关键结果 / 消融** · 作者报告优于所测对照
- **适用条件 / 局限** · 依赖可学的运动近似

**可复用机制** · 比较固定坐标和共动坐标的长期误差

<a id="paper-152720"></a>

## Adversarial Group Fairness in Contextual Bandits: When Robust is Not Fair

[官方论文页](https://neurips.cc/virtual/2026/poster/152720) · [作者来源](https://openreview.net/forum?id=QqqBvLrJr6)

- **问题 / 瓶颈** · 总体平均可掩盖少数群体失败
- **核心创新 / 方法** · 用受控漂移的策略锚、稳定聚类及群体探索做缓解
- **Baseline** · 仅总体监测
- **Benchmark** · 上下文赌博机理论
- **关键结果 / 消融** · 作者给出所设威胁模型下亚线性群体遗憾界
- **适用条件 / 局限** · 能否稳定识别群体决定适用性

**可复用机制** · 并列报告总体与最差群体遗憾

<a id="paper-151421"></a>

## A dynamical systems theory of reward-modulated learning in linear recurrent networks

[官方论文页](https://neurips.cc/virtual/2026/poster/151421) · [作者来源](https://openreview.net/forum?id=aokHxrtIxM)

- **问题 / 瓶颈** · 稀疏奖励使探索停滞
- **核心创新 / 方法** · 推导线性循环策略 REINFORCE 的低维学习动力学
- **Baseline** · 不同循环强度的理论比较
- **Benchmark** · 高维师生稀疏奖励设定
- **关键结果 / 消融** · 预测每种回合长度存在最优循环规模
- **适用条件 / 局限** · 依赖线性及对齐假设

**可复用机制** · 调整时域后重新扫描循环强度

<a id="paper-152975"></a>

## AEGIS: Almost Surely Safe Offline Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152975) · [作者来源](https://openreview.net/forum?id=Ox9slbd8dG)

- **问题 / 瓶颈** · 部署前难选定单个风险阈值
- **核心创新 / 方法** · 用最坏备份训练可行性 critic，联合奖励 critic 引导扩散
- **Baseline** · 隐式 Q 学习底座及安全离线方法
- **Benchmark** · DSRL 与人形控制
- **关键结果 / 消融** · 报告多阈值下可行性及回报兼顾
- **适用条件 / 局限** · 依赖离线支持和可行性估计

**可复用机制** · 在同一离线数据上测多个未见预算

<a id="paper-149715"></a>

## AegisFlow: Training-free Non-myopic Path-safe Guided Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/149715) · [作者来源](https://openreview.net/forum?id=nyQ14lMMIK)

- **问题 / 瓶颈** · 逐步最小修正容易贴边
- **核心创新 / 方法** · 近似 HJB 解全程受限生成控制
- **Baseline** · 近视最小范数引导
- **Benchmark** · 编辑与机器人规划
- **关键结果 / 消融** · 作者报告约束达成和目标对齐折衷改善
- **适用条件 / 局限** · 可行成本和近似误差待核

**可复用机制** · 同时衡量单步可行性和全程最小裕度

<a id="paper-148481"></a>

## AEON: Unifying Video and 3D World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148481) · [作者来源](https://openreview.net/forum?id=xUa62w8E9i)

- **问题 / 瓶颈** · 纯视频缺几何一致性
- **核心创新 / 方法** · 蒸馏适配器连接生成潜空间与 4D 高斯及相机重建解码器
- **Baseline** · 视频与三维世界模型路线
- **Benchmark** · 世界建模标准基准，名称待核
- **关键结果 / 消融** · 报告所测基准表现领先
- **适用条件 / 局限** · 依赖单目重建与适配质量

**可复用机制** · 分别评测时间真实感和跨视角一致性

<a id="paper-139587"></a>

## AET-Bench: Pixel-Accurate Atomic Tomography Is Not Atom-Accurate

[官方论文页](https://neurips.cc/virtual/2026/poster/139587) · [作者来源](https://openreview.net/forum?id=GmdQ25dIWq)

- **问题 / 瓶颈** · 体素相似度可掩盖原子错漏
- **核心创新 / 方法** · 在六级真实性阶梯上比较体素和原子层指标
- **Baseline** · 含 4D-GS 与 FISTA-TV 的 14 类方法
- **Benchmark** · AET-Bench 的 755 样本
- **关键结果 / 消融** · 单元素设置中 4D-GS 原子召回 43.9%，FISTA-TV 为 95.1%
- **适用条件 / 局限** · 结论应按真实程度分层

**可复用机制** · 分别记录体素质量和目标实体正确率

<a id="paper-150928"></a>

## AETDICE: Unified Framework and Offline Optimization for Nonlinear Multi-Objective RL

[官方论文页](https://neurips.cc/virtual/2026/poster/150928) · [作者来源](https://openreview.net/forum?id=eIYJqaER5g)

- **问题 / 瓶颈** · 非线性偏好下两类目标需要不同策略
- **核心创新 / 方法** · 用三阶段分解统一目标，在增广状态以 DICE 密度比离线求解
- **Baseline** · SER 与 ESR 两种目标框架
- **Benchmark** · 静态数据多目标策略，具名基准待核
- **关键结果 / 消融** · 作者报告可覆盖两类目标的权衡
- **适用条件 / 局限** · 增广状态成本待核

**可复用机制** · 先明确偏好与期望顺序再设计离线目标

<a id="paper-152991"></a>

## A Favorable Regime Between ODE and SDE for Few-Step Diffusion Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/152991) · [作者来源](https://openreview.net/forum?id=OnzgdNdKzx)

- **问题 / 瓶颈** · ODE 多样性不足而标准 SDE 少步不稳
- **核心创新 / 方法** · 以渐近协方差和有限步剩余项刻画噪声驱动并做结构化修正
- **Baseline** · ODE、SDE 和免训练采样器
- **Benchmark** · DiT-XL/2、EDM2 的低函数评估预算
- **关键结果 / 消融** · 作者报告改善低预算质量前沿
- **适用条件 / 局限** · 依赖驱动和模型，数值待核

**可复用机制** · 同时扫随机性强度与步数并测质量和多样性

<a id="paper-150832"></a>

## A Few Teacher Steps Go a Long Way: Cost-Efficient On-Policy Data Augmentation for Agent Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150832) · [作者来源](https://openreview.net/forum?id=exsMozVjaF)

- **问题 / 瓶颈** · 完整教师轨迹昂贵，成功过滤减少可用样本。
- **核心创新 / 方法** · 以学生诱导状态为起点，收集短、未过滤的教师续写。
- **Baseline** · 完整成功轨迹，以及仅保留学生无法独立解决的任务。
- **Benchmark** · HotpotQA、ALFWorld、Terminal-Bench-Dev。
- **关键结果 / 消融** · 作者报告短续写有利于成本效率；各任务幅度待核实。
- **适用条件 / 局限** · 需要能够复现学生到达的状态。

**可复用机制** · 将教师预算按续写长度和状态覆盖分开计量。

<a id="paper-150286"></a>

## Affine-Image Propagation for Tight and Scalable $\ell_{2}$ Neural Network Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/150286) · [作者来源](https://openreview.net/forum?id=jJKsS0Cmjn)

- **问题 / 瓶颈** · 将球变为盒或将椭球重新变成球会丢掉方向信息。
- **核心创新 / 方法** · 采用与 CROWN 兼容的仿射像传播。
- **Baseline** · α-CROWN、SDP-CROWN。
- **Benchmark** · 欧氏范数下的神经网络鲁棒性认证；具体数据集待核。
- **关键结果 / 消融** · 作者指出盒放松有维数相关损失，球化受权重条件数影响；实测数值待核。
- **适用条件 / 局限** · 非线性层仍需界估计。

**可复用机制** · 固定扰动半径比较证书紧度和计算时间。

<a id="paper-154949"></a>

## Agentic Neural Architecture Search

[官方论文页](https://neurips.cc/virtual/2026/poster/154949) · [作者来源](https://openreview.net/forum?id=9iUcWC2bXP)

- **问题 / 瓶颈** · 手写搜索空间难迁移，开放式生成又缺少受控比较。
- **核心创新 / 方法** · 先生成种子架构，再以具名槽位分解为有限搜索空间。
- **Baseline** · 人工设计搜索空间及开放式 LLM 架构生成。
- **Benchmark** · 架构搜索及组件对照；任务名待核。
- **关键结果 / 消融** · 摘要给出各组件对照方向；增益待核。
- **适用条件 / 局限** · 依赖种子与槽划分质量。

**可复用机制** · 在相同评估预算下比较自由生成、固定空间和按任务生成槽位。

<a id="paper-155404"></a>

## AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/155404) · [作者来源](https://openreview.net/forum?id=5uRXWGrFvm)

- **问题 / 瓶颈** · 每次检索都全量重编码造成预填充开销，原始文本缓存法不适配结构化记忆。
- **核心创新 / 方法** · 通过探针引导对每个记忆单元进行 KV 残差纠正。
- **Baseline** · 全量重编码和针对普通 RAG 文本的选择性重算。
- **Benchmark** · 结构化记忆的检索增强 Agent；具体基准待核。
- **关键结果 / 消融** · 摘要报告以少量纠正缓解结构化记忆缓存退化；具体幅度待核。
- **适用条件 / 局限** · 依赖记忆单元边界与探针可靠性。

**可复用机制** · 对按单元复用的缓存同时测正确率、预填充延迟和每次重算比例。

<a id="paper-139222"></a>

## AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/139222) · [作者来源](https://openreview.net/forum?id=e25kaYnRu0)

- **问题 / 瓶颈** · 仅按稳定性排序容易抓错功能部件。
- **核心创新 / 方法** · 将开放词汇三维可供性接入轨迹生成，由运动规划筛选可执行抓取。
- **Baseline** · 通用抓取与人工接触标注。
- **Benchmark** · 50 项任务、5 种本体、500 多物体及真机 FR3。
- **关键结果 / 消融** · 两类任务的轨迹采集成功率分别为人工标注的 93% 和 89%；真机平均成功率 24%。
- **适用条件 / 局限** · 依赖三维接触区域预测，轨迹采集率与真机执行率不同。

**可复用机制** · 把功能区域匹配与抓取稳定性分别纳入采样和验证。

<a id="paper-150765"></a>

## A Free Lunch in LLM Compression: Revisiting Retraining after Pruning

[官方论文页](https://neurips.cc/virtual/2026/poster/150765) · [作者来源](https://openreview.net/forum?id=fXCIZretcP)

- **问题 / 瓶颈** · 逐矩阵误差会积累成激活漂移。
- **核心创新 / 方法** · 逐局部窗口拟合稠密模型的中间激活。
- **Baseline** · 全模型剪枝后再训练、PEFT、逐矩阵重建。
- **Benchmark** · 多模型家族与规模，最高 72B，比较质量与资源。
- **关键结果 / 消融** · 局部重建匹配再训练且数据及计算少一个数量级以上，窗口达到非线性子模块后质量对粒度不敏感。
- **适用条件 / 局限** · 规律来自所测模型和剪枝设置。

**可复用机制** · 以质量、显存及校准预算共同选择激活重建窗口。

<a id="paper-151861"></a>

## A General Concept-based Decomposition for Vision–Language Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/151861) · [作者来源](https://openreview.net/forum?id=XKwu7MhFTF)

- **问题 / 瓶颈** · 逐实例分解难捕获全局语义结构。
- **核心创新 / 方法** · 在概念空间训练时保留样本间几何关系。
- **Baseline** · 实例级优化的概念分解。
- **Benchmark** · 图像和视频基准；数据集及指标待核。
- **关键结果 / 消融** · 作者报告概念分解更忠实，并保持多数原模型性能。
- **适用条件 / 局限** · 依赖概念集合及原特征结构。

**可复用机制** · 对比逐实例拟合和全局几何约束在跨域解释中的稳定性。

<a id="paper-155447"></a>

## Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/155447) · [作者来源](https://openreview.net/forum?id=5YAV5SEvXG)

- **问题 / 瓶颈** · 静态验证难发现行为级错误。
- **核心创新 / 方法** · 研究与实现后，由测试团队通过单元测试和模拟构建自适应反馈，并以多轮反馈训练。
- **Baseline** · 静态验证及同一底座训练前对照。
- **Benchmark** · 三项符号世界模型基准，含 PDDL 和可执行代码。
- **关键结果 / 消融** · 基于反馈轨迹微调后，作者报告平均相对增益 30.95%。
- **适用条件 / 局限** · 测试覆盖不足时仍可能遗漏交互错误。

**可复用机制** · 为模型生成方法分别比较静态验证、执行验证与用执行反馈训练。

<a id="paper-139558"></a>

## AgentAbstain: Do LLM Agents Know When Not to Act?

[官方论文页](https://neurips.cc/virtual/2026/poster/139558) · [作者来源](https://openreview.net/forum?id=Iee7eL6QV0)

- **问题 / 瓶颈** · 单测成功率无法检验智能体是否在不可逆动作前识别拒绝条件。
- **核心创新 / 方法** · 生成沙箱任务并控变指令、工具或状态，经确定性重放与语义评审验证。
- **Baseline** · 17 种模型与 4 套执行框架。
- **Benchmark** · 成对正确率，要求两个条件都采取正确行为。
- **关键结果 / 消融** · 最佳成对正确率为 59.5%，拒绝与一般解题能力关联较弱。
- **适用条件 / 局限** · 依赖沙箱代表性与评审准确性。

**可复用机制** · 分别记录拒绝是否正确，以及拒绝是否发生在执行之前。

<a id="paper-138951"></a>

## AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/138951) · [作者来源](https://openreview.net/forum?id=uHjkDW1QfY)

- **问题 / 瓶颈** · 最终测试无法区分可靠解决与偶然通过
- **核心创新 / 方法** · 以同题成功轨迹构造过程参考，审计回归、盲目重试和验证缺失
- **Baseline** · 仅看最终测试
- **Benchmark** · SWE-bench Verified，八种后端
- **关键结果 / 消融** · 1815 条评测轨迹中，通过轨迹有 10.7% 被归为 Lucky Pass
- **适用条件 / 局限** · 需要每题足够成功轨迹

**可复用机制** · 将测试通过率与轨迹质量分开，通过匹配基线与评测边界核验。

<a id="paper-151325"></a>

## Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/151325) · [作者来源](https://openreview.net/forum?id=bLzbzox9it)

- **问题 / 瓶颈** · 没有恶意输入也可能发生不安全续跑
- **核心创新 / 方法** · 在沙箱注入模拟良性故障并分类记录失控行为
- **Baseline** · 常规可靠性与安全基准
- **Benchmark** · 四套 GPT、Grok、Gemini 驱动系统
- **关键结果 / 消融** · 作者报告良性环境故障可诱发失控
- **适用条件 / 局限** · 模拟错误覆盖不了所有部署故障

**可复用机制** · 把普通环境故障纳入安全回归，通过匹配基线与评测边界核验。

<a id="paper-153890"></a>

## AgenTracer-v2: Agentic Failure Tracer for LLM Agentic Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/153890) · [作者来源](https://openreview.net/forum?id=HyejvL5c6c)

- **问题 / 瓶颈** · 全轨迹被动读取难定位导致失败的步骤
- **核心创新 / 方法** · 工具增强多跳诊断，利用确定性回滚构造训练样本
- **Baseline** · 被动全轨迹归因
- **Benchmark** · Tracer-Flywheel 合成约 8000 条数据；测试设置待核
- **关键结果 / 消融** · 量化细节待核
- **适用条件 / 局限** · 真实系统可能无法确定性回滚

**可复用机制** · 对超长日志进行主动检索和分步归因，通过匹配基线与评测边界核验。

<a id="paper-153256"></a>

## Agents as Neuro-Symbolic Reasoners: Path Feasibility Reasoning for Precise Static Bug Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/153256) · [作者来源](https://openreview.net/forum?id=Mbv63Mz4IY)

- **问题 / 瓶颈** · 路径不可行会造成误报，复杂代码超出单次推理上下文
- **核心创新 / 方法** · 把跨过程分析拆成局部值域推理并按需查询上下文
- **Baseline** · 静态分析和已有 LLM 告警过滤
- **Benchmark** · 静态告警验证；数据集待核
- **关键结果 / 消融** · 量化细节待核
- **适用条件 / 局限** · 路径与上下文提取质量会限制验证

**可复用机制** · 以局部符号推理验证静态告警，通过匹配基线与评测边界核验。

<a id="paper-154115"></a>

## AgentSSL: Can MLE Agents Leverage Unlabeled Data?

[官方论文页](https://neurips.cc/virtual/2026/poster/154115) · [作者来源](https://openreview.net/forum?id=G9vxuLIz7v)

- **问题 / 瓶颈** · 自动建模研究主要以完整监督为条件
- **核心创新 / 方法** · 把半监督建模视为程序搜索，分析发现和迁移策略
- **Baseline** · 纯监督的自动建模设置
- **Benchmark** · 少标签且无标签样本可用的任务；数据集待核
- **关键结果 / 消融** · 作者报告智能体可以利用无标签样本，收益条件待核
- **适用条件 / 局限** · 对领域和搜索预算敏感

**可复用机制** · 在标签不足时单测 Agent 能否利用无标签数据，通过匹配基线与评测边界核验。

<a id="paper-151244"></a>

## AgentWeave: Efficient Distributed Agent Serving via Flow Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/151244) · [作者来源](https://openreview.net/forum?id=bpk2nFIPmf)

- **问题 / 瓶颈** · 分设备有流水气泡，整工作流聚合又造成长短请求阻塞
- **核心创新 / 方法** · 按工作流分解分布式服务
- **Baseline** · 分离部署与整工作流聚合部署
- **Benchmark** · 分布式智能体服务；工作负载待核
- **关键结果 / 消融** · 定量结果待核
- **适用条件 / 局限** · 收益取决于模块耗时与请求分布

**可复用机制** · 按工作流模块区分流水气泡与请求阻塞，通过匹配基线与评测边界核验。

<a id="paper-154195"></a>

## Aggregation Dispersion: An Information-Geometric Diagnostic of Oversmoothing in Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/154195) · [作者来源](https://openreview.net/forum?id=FUpw0l0XS6)

- **问题 / 瓶颈** · 节点向量相似度不能直接描述传播分布收缩
- **核心创新 / 方法** · 将每节点的游走分布视为概率单纯形点，按 Fisher–Rao 几何测收缩
- **Baseline** · 常规节点表示相似度诊断
- **Benchmark** · 逐层消息传递图网络
- **关键结果 / 消融** · 经验结果待核
- **适用条件 / 局限** · 需要显式估计传播分布

**可复用机制** · 用传播分布的几何离散度测过平滑，通过匹配基线与评测边界核验。

<a id="paper-154175"></a>

## AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games

[官方论文页](https://neurips.cc/virtual/2026/poster/154175) · [作者来源](https://openreview.net/forum?id=Fhpafr7nn7)

- **问题 / 瓶颈** · 过度依赖赠予使智能体忽略自身收益行为
- **核心创新 / 方法** · 为既有赠予机制加适应性拒绝模块
- **Baseline** · 原赠予算法
- **Benchmark** · 混合动机博弈；任务和指标待核
- **关键结果 / 消融** · 定量结果待核
- **适用条件 / 局限** · 适用于奖励可转移的机制

**可复用机制** · 允许按状态拒绝部分转移奖励，通过匹配基线与评测边界核验。

<a id="paper-152893"></a>

## Agreement without Coverage: Conditional Agreement is Non-Identifying in Variable-Support Structured Extraction

[官方论文页](https://neurips.cc/virtual/2026/poster/152893) · [作者来源](https://openreview.net/forum?id=PcPlRvDFiC)

- **问题 / 瓶颈** · 只在可比较样本上算一致率会奖励缩小输出支持
- **核心创新 / 方法** · 对依赖预测的评估事件构建严格反例
- **Baseline** · 只用条件一致率评估
- **Benchmark** · 可变支持集结构化预测理论
- **关键结果 / 消融** · 严格反例证明更高一致率可伴随覆盖等同时变差
- **适用条件 / 局限** · 适用于支持集由预测决定的场景

**可复用机制** · 一致率同时报告覆盖、召回与输出规模，通过匹配基线与评测边界核验。

<a id="paper-151694"></a>

## A Hierarchical World Model for Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/151694) · [作者来源](https://openreview.net/forum?id=Yj5ujHJ5XD)

- **问题 / 瓶颈** · 单尺度高保真生成缺少场景结构推理
- **核心创新 / 方法** · 粗层预测长程布局，细层带条件生成细节
- **Baseline** · 单尺度预测与教师强制
- **Benchmark** · 驾驶场景；指标待核
- **关键结果 / 消融** · 摘要报告扩散强制预训练表征较丰富
- **适用条件 / 局限** · 分层误差可向细节传播

**可复用机制** · 用长时粗语义预测约束短时细节，通过匹配基线与评测边界核验。

<a id="paper-153980"></a>

## A Hierarchy of Entropy-Shapley Games for Multivariate Predictive Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/153980) · [作者来源](https://openreview.net/forum?id=H5mUgkvpmE)

- **问题 / 瓶颈** · 单值聚合和逐输出分析掩盖输出依赖
- **核心创新 / 方法** · 建立三类基于熵的 Shapley 博弈区分两类效应
- **Baseline** · 聚合标量及逐输出归因
- **Benchmark** · 多元概率预测；实证任务待核
- **关键结果 / 消融** · 主要新增量是分解式归因
- **适用条件 / 局限** · 依赖可估计联合分布或熵

**可复用机制** · 对边缘不确定性和依赖结构分别归因，通过匹配基线与评测边界核验。

<a id="paper-152553"></a>

## Active Learning as Nullspace Regulation: A Spectral Representation Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/152553) · [作者来源](https://openreview.net/forum?id=SGzlvUpAfD)

- **问题 / 瓶颈** · 不确定性或全空间多样性不足以指出当前标注集缺失哪些特征方向。
- **核心创新 / 方法** · 由有标签特征谱分解子空间，在弱覆盖方向估计未标注残差的跨轮持久性和互补性。
- **Baseline** · 对照主动学习基线，具名方法待核。
- **Benchmark** · 视觉任务上的标注效率，另比较不同骨干的样本排序。
- **关键结果 / 消融** · 作者报告标注效率可比或改善，残差收缩具有方向性，骨干变化会显著改变排序。
- **适用条件 / 局限** · 残差依赖当前特征表示；低价值噪声也可能落在弱覆盖方向。

**可复用机制** · 主动标注时同时测跨循环残差和新增覆盖，固定预算与单轮不确定性选择对照。

<a id="paper-155964"></a>

## AdaCal: Adaptive Calibration for Robust Sparse Attention in Long-Context LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155964) · [作者来源](https://openreview.net/forum?id=1VrcmRz58A)

- **问题 / 瓶颈** · 静态掩码易漏证据，统一扩大动态覆盖又增加噪声和计算。
- **核心创新 / 方法** · 根据任务类型调度，通过探针测各头熵、集中度与中间区段覆盖，只在需要时启用或扩充。
- **Baseline** · 静态与动态稀疏注意力，具名对照待核。
- **Benchmark** · 长上下文预填充，覆盖超过 32K token 的设置，测试稳健性和远距离检索。
- **关键结果 / 消融** · 作者报告对比基线稳健性提高，超过 32K 时增益更明显；幅度待核。
- **适用条件 / 局限** · 需要探针能代表真实注意力结构，额外算力与召回的权衡待核。

**可复用机制** · 用按头探针分配稀疏注意力预算，在同计算量下与固定掩码比较证据召回。

<a id="paper-154964"></a>

## ACQueReLlo: Alignment-Aware Constrained Quantization via Reinforcement Learning for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154964) · [作者来源](https://openreview.net/forum?id=9aiPOrUn3v)

- **问题 / 瓶颈** · 压缩后综合效用稳定仍会掩盖安全行为变化。
- **核心创新 / 方法** · 采用带效用和两类拒答约束的块级位宽分配，以提示子集作评估代理。
- **Baseline** · 均匀量化及其他量化方法。
- **Benchmark** · 若干语言模型，同时测压缩预算、效用和安全拒答。
- **关键结果 / 消融** · 摘要报告整体折衷更好，幅度待核。
- **适用条件 / 局限** · 代理子集对部署请求的代表性待验证。

**可复用机制** · 以相同比特预算分开记录危险请求拒答和良性请求误拒。

<a id="paper-155358"></a>

## Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique

[官方论文页](https://neurips.cc/virtual/2026/poster/155358) · [作者来源](https://openreview.net/forum?id=6CdA8QbHL5)

- **问题 / 瓶颈** · 整体不确定性分数难确定应该修改哪个工具参数。
- **核心创新 / 方法** · 在冻结语言模型生成时并行以低秩适配器读写内部表示，将不确定性转为局部自然语言诊断。
- **Baseline** · 同规模外部检测器以及内部探针。
- **Benchmark** · Qwen 和 Llama 的工具调用及闭环 ReAct，测 F1 和定位准确率。
- **关键结果 / 消融** · 摘要报告 F1 为 0.870 对 0.695，定位准确率超过 80%。
- **适用条件 / 局限** · 需访问内部状态；工具范围和误阻断率待核。

**可复用机制** · 监测 Agent 时分别评估报警准确性、错误定位及后续纠正。

<a id="paper-150968"></a>

## Action Images: End-to-End Policy Learning via Multiview Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150968) · [作者来源](https://openreview.net/forum?id=dvcWzyuusE)

- **问题 / 瓶颈** · 独立动作头难共享视频模型的像素级知识。
- **核心创新 / 方法** · 把七自由度动作映射成多视角像素轨迹，共用视频生成模型进行预测、控制和标注。
- **Baseline** · 既有视频空间世界模型及零样本策略，具名待核。
- **Benchmark** · RLBench 和真机零样本操作及联合生成。
- **关键结果 / 消融** · 作者报告成功率和联合生成质量改善，幅度待核。
- **适用条件 / 局限** · 依赖动作到像素的几何对应及解码。

**可复用机制** · 比较显式控制头与可解码的像素动作监督对换视角迁移的影响。

<a id="paper-150198"></a>

## Activation Steering of Video Generation Models via Reduced-Order Linear Optimal Control

[官方论文页](https://neurips.cc/virtual/2026/poster/150198) · [作者来源](https://openreview.net/forum?id=jzkIT7ApwP)

- **问题 / 瓶颈** · 粗粒度激活干预容易损伤原本合法的生成内容。
- **核心创新 / 方法** · 把视频生成看作动力系统，在低维表示中用反馈控制减少不必要扰动。
- **Baseline** · 既有激活干预方法，具名待核。
- **Benchmark** · 视频安全和概念控制评测，观察安全性、提示一致性及质量。
- **关键结果 / 消融** · 作者报告不安全输出下降且质量保留，数值待核。
- **适用条件 / 局限** · 低维近似在模型与场景改变后需重新验证。

**可复用机制** · 为生成模型的防护同时测安全表现、正常提示遵从和感知质量。

<a id="paper-149778"></a>

## Active Learning for Conditional Generative Compressed Sensing

[官方论文页](https://neurips.cc/virtual/2026/poster/149778) · [作者来源](https://openreview.net/forum?id=nNxxFgwPWW)

- **问题 / 瓶颈** · 提示同时改变测量分布和生成模型的重建空间，其影响容易混淆。
- **核心创新 / 方法** · 按条件生成模型设计 Christoffel 采样，分析采样与恢复提示不匹配的惩罚。
- **Baseline** · 既有近最优生成式压缩感知结果和提示匹配对照。
- **Benchmark** · 子采样傅里叶测量图像恢复，使用 Stable Diffusion。
- **关键结果 / 消融** · 得到匹配提示下的稳定恢复界，实验显示提示影响频域采样和恢复。
- **适用条件 / 局限** · 依赖条件生成器的正则性及提示兼容性。

**可复用机制** · 评测条件逆问题时交叉改变采样和重建条件，分离两者贡献。

<a id="paper-151935"></a>

## Active Learning of Conditional Generative Models via the Transport Neural Tangent Kernel

[官方论文页](https://neurips.cc/virtual/2026/poster/151935) · [作者来源](https://openreview.net/forum?id=WioQm89GJJ)

- **问题 / 瓶颈** · 均值代理看不到方差和分布形状变化。
- **核心创新 / 方法** · 将 Wasserstein 风险拆成均值与形状项，用分布敏感的传输核构造高斯过程选点。
- **Baseline** · 仅从条件均值计算的 NTK。
- **Benchmark** · 合成分布及含意图标签的文本等，比较多类条件生成模型。
- **关键结果 / 消融** · 作者报告传输核优于均值核，精确幅度待核。
- **适用条件 / 局限** · 小参数扰动的分析条件及蒙特卡洛开销需考虑。

**可复用机制** · 在概率预测任务上检查选点是否降低分布形状误差，并和仅预测均值的采样规则比较。

<a id="paper-148250"></a>

## Active Memory Feedback Loop for Fast–Slow Dynamics in Liquid Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/148250) · [作者来源](https://openreview.net/forum?id=zGqWYYr0Vc)

- **问题 / 瓶颈** · 隐状态在长时间间隔或缺测时会丢失过去信息。
- **核心创新 / 方法** · 以全局原型和新颖性门控的局部记忆形成残差，写回后续状态转移。
- **Baseline** · 底座液态网络及去掉反馈、适配或残差的消融。
- **Benchmark** · 七个时序任务，包含分类、回归、持续学习及缺测鲁棒性。
- **关键结果 / 消融** · 摘要报告七项中六项最好，消融支持循环反馈贡献。
- **适用条件 / 局限** · 记忆容量、更新代价与任务间干扰待核。

**可复用机制** · 在相同记忆容量下比较输出增强和闭环状态反馈，按观测间隔分层。

<a id="paper-149590"></a>

## ActO: Extracting Action Representations from MLLM Embeddings for Video World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149590) · [作者来源](https://openreview.net/forum?id=owi7oyTNah)

- **问题 / 瓶颈** · 从零训练动作编码器的瓶颈可能损失动作细节或泄漏背景。
- **核心创新 / 方法** · 对预训练多模态表示做对比适配，减少场景相关性并保留表达空间。
- **Baseline** · 不依赖人工标签的潜动作学习方法。
- **Benchmark** · 机器人和游戏内外域，测动作表达能力、场景不变性及动作条件生成。
- **关键结果 / 消融** · 摘要报告三方面均优于所比方法，幅度待核。
- **适用条件 / 局限** · 依赖预训练表示已经包含动作线索。

**可复用机制** · 当动作无标签时，将动作表达和场景不变性拆成独立指标。

<a id="paper-148366"></a>

## AgentBrew: Offline Tool-Use Agent Learning from Raw Real-World Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/148366) · [作者来源](https://openreview.net/forum?id=yPSKli19Mm)

- **问题 / 瓶颈** · 真实工具环境没有可扩展验证器。
- **核心创新 / 方法** · 从实际结果反推指令，以点互信息分摊动作信用。
- **Baseline** · Qwen3-32B、235B及拒绝采样。
- **Benchmark** · 三种真实 MCP 应用，测准确率和得分。
- **关键结果 / 消融** · 32B 平均增加 8.7 准确率和 9.7 得分单位。
- **适用条件 / 局限** · 依赖轨迹覆盖和可靠的事后指令。

**可复用机制** · 比较整段过滤与动作级加权能否从同一日志提取更多监督。

<a id="paper-155417"></a>

## AgentCBO: Causal Belief Routing for Bayesian Optimization under Unknown Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/155417) · [作者来源](https://openreview.net/forum?id=5qGuryamh7)

- **问题 / 瓶颈** · 完整图恢复浪费有限查询预算。
- **核心创新 / 方法** · 定义对优化器等效的图差异，仅编辑不确定边并以决策代理指标验收。
- **Baseline** · 已知图的因果贝叶斯优化。
- **Benchmark** · 十个因果优化基准，指标细项待核。
- **关键结果 / 消融** · 报告与已知图方法表现相近。
- **适用条件 / 局限** · 依赖代理指标能反映真实决策差异。

**可复用机制** · 结构学习目标可直接围绕下游决策的等价类定义。

<a id="paper-151150"></a>

## Agent Explorative Policy Optimization for Agentic Multimodal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151150) · [作者来源](https://openreview.net/forum?id=ceOxtMigKk)

- **问题 / 瓶颈** · 普通组内学习中工具失败轨迹得不到有效相对反馈。
- **核心创新 / 方法** · 按不确定性挑前缀，只重采样工具调用和后续生成。
- **Baseline** · SFT 加 GRPO。
- **Benchmark** · 九个多模态基准、三种 Qwen3-VL-Thinking 规模。
- **关键结果 / 消融** · 8B 平均 Pass@1 与 Pass@4 各提高 1.8 个百分点。
- **适用条件 / 局限** · 需要工具反馈及额外采样预算。

**可复用机制** · 在等预算下比较重采样整段推理和只重采样动作。

<a id="paper-153633"></a>

## AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/153633) · [作者来源](https://openreview.net/forum?id=JxLeRbqs0Y)

- **问题 / 瓶颈** · 从终局直接改提示容易归错因并混合失效模式。
- **核心创新 / 方法** · 逐个修改中间输出以验证责任，抽取文本梯度并聚类归纳。
- **Baseline** · 现有文本梯度优化。
- **Benchmark** · 五个多智能体基准。
- **关键结果 / 消融** · 报告表现改善，平均耗时较次快对照低 2.5 倍。
- **适用条件 / 局限** · 单代理干预可能漏掉联合失效。

**可复用机制** · 对照终局反馈与验证过的局部反馈。

<a id="paper-150912"></a>

## Agentic Abstention: Do Agents Know When to Stop Instead of Act?

[官方论文页](https://neurips.cc/virtual/2026/poster/150912) · [作者来源](https://openreview.net/forum?id=eURViGZicT)

- **问题 / 瓶颈** · 有些任务要经交互才发现不可行，最终弃权未体现浪费。
- **核心创新 / 方法** · 从交互轨迹提炼复用停止规则，不改模型参数。
- **Baseline** · 原代理与不同脚手架。
- **Benchmark** · 逾 28000 个网页购物、终端和问答任务。
- **关键结果 / 消融** · WebShop 上 70B 模型及时召回从 26.7% 到 57.4%。
- **适用条件 / 局限** · 规则跨环境适用性待核。

**可复用机制** · 量化首次可判定不可行后仍发生的动作数。

<a id="paper-154318"></a>

## Agentic-imodels: Evolving agentic interpretability tools via autoresearch

[官方论文页](https://neurips.cc/virtual/2026/poster/154318) · [作者来源](https://openreview.net/forum?id=EY6O5VNNlV)

- **问题 / 瓶颈** · 人类可解释形式不一定能被代理正确模拟。
- **核心创新 / 方法** · 按预测质量与基于文本表示的行为问答测试共同优化回归器。
- **Baseline** · 现有表格回归器及代理工具，名称待核。
- **Benchmark** · 新数据集、可解释性测试及 BLADE。
- **关键结果 / 消融** · 报告下游代理最高改善 73%。
- **适用条件 / 局限** · 依赖评审模型和测试覆盖，可能存在指标过拟合。

**可复用机制** · 按读者是否可预测反事实行为评价解释。

<a id="paper-155392"></a>

## Agentic Reward Modeling: Verifying GUI Agent via Progressive Trajectory-Grounded Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/155392) · [作者来源](https://openreview.net/forum?id=61SF5nUDyZ)

- **问题 / 瓶颈** · 被动评审漏掉隐藏状态，全面探查代价高。
- **核心创新 / 方法** · 渐进验证按从显性到潜在、低成本到高成本的顺序收集证据。
- **Baseline** · 规则判定、被动 LLM 判定和主动探查。
- **Benchmark** · OSWorld-Verified 与 AndroidWorld。
- **关键结果 / 消融** · 作者报告准确性和效率折衷改善。
- **适用条件 / 局限** · 需要可访问状态与探查权限，最优触发条件待核。

**可复用机制** · 以固定验证预算比较主动探查和按证据升级的验证。

<a id="paper-152625"></a>

## AI-Assisted Classification under Correlation Neglect and Trust

[官方论文页](https://neurips.cc/virtual/2026/poster/152625) · [作者来源](https://openreview.net/forum?id=Rhmuhzzjjr)

- **问题 / 瓶颈** · 人和模型的证据相关时，用户可能把同一证据计入两次。
- **核心创新 / 方法** · 将能力、信号重叠与信任建模，划分互补、受损与自动化区域。
- **Baseline** · 人工或 AI 独立判断及人机配合。
- **Benchmark** · ChatBench，643 名参与者，GPT-4o 与 Llama-3.1-8B。
- **关键结果 / 消融** · 辅助提高准确率 21 个百分点，估计信任低约四倍。
- **适用条件 / 局限** · 依赖二元任务与行为假设。

**可复用机制** · 评估辅助系统时控制信号重合度并测相对双方独立判断的边际贡献。

<a id="paper-152673"></a>

## AIM: Adaptive Interaction in Multi-Agent Debate for Multimodal LLM Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/152673) · [作者来源](https://openreview.net/forum?id=RGMuCsE9Er)

- **问题 / 瓶颈** · 固定文本交换在细粒度问题上丢证据且成本高。
- **核心创新 / 方法** · 从初次结构化回答提取路由特征，由轻量路由器选模态组合。
- **Baseline** · 单模态和固定组合基线。
- **Benchmark** · 八个视觉、音频、视频问答基准。
- **关键结果 / 消融** · 最高准确率提升 8.9%，相对固定组合 token 成本最多降 53.4%。
- **适用条件 / 局限** · 两个峰值对应的任务与比较口径待核。

**可复用机制** · 对照文字摘要与局部原模态传输，联测证据保真和通信成本。

<a id="paper-152980"></a>

## AIRA 2: Overcoming Bottlenecks in AI Research Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152980) · [作者来源](https://openreview.net/forum?id=OtCjJw41aB)

- **问题 / 瓶颈** · 同步执行限吞吐，评估噪声会恶化长时搜索选择。
- **核心创新 / 方法** · 并发实验池、隐藏一致评估与能交互调试的操作单元。
- **Baseline** · 既有研究 Agent 和组件消融。
- **Benchmark** · MLE-bench-30、AIRS-Bench。
- **关键结果 / 消融** · 24 小时平均百分位 81.5%，72 小时 83.1%；最佳对照 72.7%。
- **适用条件 / 局限** · 对评估过拟合的诊断限于所测任务。

**可复用机制** · 保持算力预算一致，独立控制调度并发和评分噪声以分解搜索收益。

<a id="paper-151241"></a>

## AIR: Rethinking Image-Text Offset Alignment in Multimodal Contrastive  Representation Space

[官方论文页](https://neurips.cc/virtual/2026/poster/151241) · [作者来源](https://openreview.net/forum?id=bqgwUpKHsr)

- **问题 / 瓶颈** · 跨模态嵌入中，文本变化方向与视觉方向经常不一致。
- **核心创新 / 方法** · 测量偏移对齐，使用锚点采样和概念描述学习迭代校准文本偏移。
- **Baseline** · 原文本偏移方案及既有编辑和域适配方法。
- **Benchmark** · 六数据集、八视觉语言模型；另有零样本域适配和编辑。
- **关键结果 / 消融** · 报告概念距离与失配正相关，校准改善编辑和适配。
- **适用条件 / 局限** · 不同表征空间和概念距离定义的敏感度待核。

**可复用机制** · 用成对图文变换检查方向对齐，并按语义距离分桶评估校准收益。

<a id="paper-151235"></a>

## A Kernel Nonconformity Score for Multivariate Conformal Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/151235) · [作者来源](https://openreview.net/forum?id=btzP5Ir75f)

- **问题 / 瓶颈** · 将多维残差压成标量时，等距或椭球假设可能浪费预测区域体积。
- **核心创新 / 方法** · 用多变量核分数保持残差几何，分解为各向异性 MMD，并用核协方差的有效秩刻画收敛。
- **Baseline** · 椭球型预测区域，具名实现待核。
- **Benchmark** · 多元回归，比较名义覆盖率与区域体积。
- **关键结果 / 消融** · 作者给出有限样本覆盖保证，并报告相同名义覆盖下区域更小；具体幅度待核。
- **适用条件 / 局限** · 覆盖条件和核选择须查正文；有效秩界不等于任意高维分布都易校准。

**可复用机制** · 在固定覆盖率下比较椭球和核分数，按残差结构及维度报告区域体积。

<a id="paper-148953"></a>

## AKTD: FDR Control for LLM Training Data Detection under Approximate Exchangeability

[官方论文页](https://neurips.cc/virtual/2026/poster/148953) · [作者来源](https://openreview.net/forum?id=tukhRsjkzd)

- **问题 / 瓶颈** · 文本和对照文本难以严格可交换，经典 knockoff 阈值的错误发现率可能偏高。
- **核心创新 / 方法** · 用零假设统计量的尾部不对称估计惩罚项，可用独立的纯零假设校准池。
- **Baseline** · 未经不对称校正的 knockoff+ 阈值。
- **Benchmark** · WikiMIA、MIMIR，GPT 与 Pythia，测错误发现率和检出能力。
- **关键结果 / 消融** · 作者报告估计的尾部偏差预测了错误发现率膨胀，校正恢复控制并保留检出能力；量化幅度待核。
- **适用条件 / 局限** · 校准样本须确知未入训，且要能代表被审计集合的零假设分布。

**可复用机制** · 审计模型训练数据时，先在独立已知未入训文本上检查统计对称性，再决定是否沿用默认阈值。

<a id="paper-152511"></a>

## ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152511) · [作者来源](https://openreview.net/forum?id=Saaw5yo8tX)

- **问题 / 瓶颈** · 无动作视频的重建编码不一定适合控制
- **核心创新 / 方法** · 用帧三元组约束组合与反向一致性，冻结编码器后与动作联合流匹配
- **Baseline** · 无结构潜动作
- **Benchmark** · MT50、LIBERO 与真机
- **关键结果 / 消融** · MT50 47.9%→85.0%，LIBERO 94.1%→98.1%
- **适用条件 / 局限** · 局部可加性未必跨长时或不可逆事件成立

**可复用机制** · 用可组合转移作为动作生成的辅助目标

<a id="paper-154404"></a>

## A Latent-Load Framework for Reliability Analysis and Intervention Design in LLM Pipelines

[官方论文页](https://neurips.cc/virtual/2026/poster/154404) · [作者来源](https://openreview.net/forum?id=DptlWbtTTY)

- **问题 / 瓶颈** · 单模块准确率难反映多步错误放大
- **核心创新 / 方法** · 以隐语义误差递推分解传递放大和新增错误，并用代理量估计
- **Baseline** · 固定预算下的检查点配置，具名对照待核
- **Benchmark** · 黑箱流水线下游风险与失败率
- **关键结果 / 消融** · 证明配置目标单调次模，实验报告代理风险降低
- **适用条件 / 局限** · 代理语义负载未必精确对应真实错误

**可复用机制** · 按估计的错误传播收益配置有限检查点

<a id="paper-149267"></a>

## A Latent World-Action Model with Jointly Aligned Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149267) · [作者来源](https://openreview.net/forum?id=ray5fCkxmm)

- **问题 / 瓶颈** · 像素滚动昂贵且还原大量控制无关细节
- **核心创新 / 方法** · 当前观测先验与未来帧嵌入后验双分支对齐
- **Baseline** · 直接动作和未来帧预测路线
- **Benchmark** · 多项操作基准及真机，名称待核
- **关键结果 / 消融** · 作者报告受控训练下具竞争力
- **适用条件 / 局限** · 对齐能否保留稀有接触信号待核

**可复用机制** · 用训练期未来视觉指导可部署的潜查询

<a id="paper-154391"></a>

## AlgoPilot: Cross-Paradigm Reasoning in Language Models via Strategy Selection and Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/154391) · [作者来源](https://openreview.net/forum?id=DvbKbQMohf)

- **问题 / 瓶颈** · 固定提示难应对不同求解范式
- **核心创新 / 方法** · 训练路由模块选号，再由专家生成结构化指导供执行模型使用
- **Baseline** · Qwen3-8B 原模型及 GLM-5 提示等
- **Benchmark** · 5 类问题、13 基准、66 个领域
- **关键结果 / 消融** · 同底座平均准确率 38.4%→72.9%
- **适用条件 / 局限** · 跨执行模型迁移范围待核

**可复用机制** · 将范式选择和形式化指导与执行模型分离

<a id="paper-148851"></a>

## Align $\&$ Invert: Solving Inverse Problems with Diffusion and Flow-based Models via Representation Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/148851) · [作者来源](https://openreview.net/forum?id=uh5JsNmPig)

- **问题 / 瓶颈** · 观测退化时缺少干净目标用于对齐
- **核心创新 / 方法** · 推理时在 DINOv2 特征空间施加表征对齐正则
- **Baseline** · 不加对齐的扩散或流求解器
- **Benchmark** · 超分、修补、高斯与运动去模糊
- **关键结果 / 消融** · 作者报告质量一致改善并减少达到同等效果的离散步数
- **适用条件 / 局限** · 近似目标有偏时可能引入错误语义

**可复用机制** · 用近似目标的语义特征引导预训练生成先验

<a id="paper-156740"></a>

## Align and Distill: Unifying and Improving Domain Adaptive Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/156740) · [作者来源](https://openreview.net/forum?id=ssXSrZ94sR)

- **问题 / 瓶颈** · 不同实现与弱对照会高估收益
- **核心创新 / 方法** · 统一实现、现代骨干和多域评测，通过 ALDI++ 验证协议
- **Baseline** · 公平重训的域适应检测基线
- **Benchmark** · Cityscapes→Foggy、Sim10k→Cityscapes、CFC-DAOD
- **关键结果 / 消融** · 分别较先前最佳提高 3.5、5.7 和 0.6 AP50
- **适用条件 / 局限** · 结论限所测检测器和域迁移

**可复用机制** · 先统一训练协议并增强基线，再比较域适应方法

<a id="paper-152098"></a>

## AlignDrive: Aligned Lateral-Longitudinal Planning for End-to-End Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/152098) · [作者来源](https://openreview.net/forum?id=VXtoyI6yEY)

- **问题 / 瓶颈** · 并行预测横纵轨迹容易失配
- **核心创新 / 方法** · 将纵向规划写成以横向路径为条件的一维位移回归
- **Baseline** · 横纵并行规划
- **Benchmark** · Bench2Drive、Fail2Drive
- **关键结果 / 消融** · 驾驶分 89.07、成功率 73.18%
- **适用条件 / 局限** · 错误横向候选会限制后段修正

**可复用机制** · 先定横向路径，再沿路径预测纵向位移

<a id="paper-152382"></a>

## Aligned Delta-Triplane Transformers as Occupancy World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152382) · [作者来源](https://openreview.net/forum?id=TVtLbFPjtb)

- **问题 / 瓶颈** · 完整重预测浪费静态区域的建模预算
- **核心创新 / 方法** · 对齐三平面历史，按自运动及外部查询预测残差
- **Baseline** · 完整状态占据预测
- **Benchmark** · Occ3D-nus，预测质量和速度
- **关键结果 / 消融** · 作者报告更少参数、更高帧率和预测改善
- **适用条件 / 局限** · 补偿误差可能被误认为真实场景变化

**可复用机制** · 先补偿自运动，再预测占据变化

<a id="paper-155747"></a>

## Aligning Few-Step Generative Model via Amortizing Sample-Based Variational Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/155747) · [作者来源](https://openreview.net/forum?id=3Hk7OwZj3Y)

- **问题 / 瓶颈** · 少步生成器常无易求似然，现有方法也受求解器限制。
- **核心创新 / 方法** · 将问题写成参考分布上的奖励倾斜，以 Stein 变分梯度更新粒子，再用不动点回归摊销进生成器。
- **Baseline** · 与现有策略提取方法比较，具名细节待核实。
- **Benchmark** · 56 项离线和 30 项离线到在线操作任务；图像实验覆盖 ImageNet-256 至 1024 分辨率文生图。
- **关键结果 / 消融** · 作者报告操作任务优于对照，并验证 GAN、漂移、Consistency 与 flow map 骨干可用；幅度待核。
- **适用条件 / 局限** · 需能取参考样本与评估奖励，粒子成本待核。

**可复用机制** · 当不同生成头无法共享似然训练时，把同一粒子目标摊销到各自参数。

<a id="paper-149374"></a>

## Aligning Flow Map Policies with Optimal $Q$-Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/149374) · [作者来源](https://openreview.net/forum?id=qXke3MFbyG)

- **问题 / 瓶颈** · 多次求解生成动力学增加闭环延迟。
- **核心创新 / 方法** · 用流映射支持可变步幅，以评论器推导信赖域内的适配目标，并用重加噪束搜索提供迭代选项。
- **Baseline** · 比较单步策略 MVP。
- **Benchmark** · OGBench、RoboMimic 的 12 个操作和移动任务，测成功率。
- **关键结果 / 消融** · 相对 MVP 的平均成功率提高 21.3%；束搜索开销待核。
- **适用条件 / 局限** · 信赖域和效果依赖 Q 值质量。

**可复用机制** · 分别测单跳适配与多轮束搜索，以固定时延预算选择生成步数。

<a id="paper-155656"></a>

## Aligning Forest and Trees in Images & Long Captions for Visually Grounded Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/155656) · [作者来源](https://openreview.net/forum?id=3zxG6gSB4n)

- **问题 / 瓶颈** · 全局对比学习容易依赖显著场景线索，忽略描述细节。
- **核心创新 / 方法** · 细到粗图像编码器与部件到整体文本编码器共同学习局部语义再聚合。
- **Baseline** · 与 CLIP 类全局对齐路线比较，具名实验设置待核。
- **Benchmark** · 3000 万图文对训练，六个长文本检索基准与无区域监督定位。
- **关键结果 / 消融** · 作者报告六个检索基准领先并观察到区域定位。
- **适用条件 / 局限** · 依赖长描述包含与可见部件互相对应的描述；等数据量对照待核。

**可复用机制** · 固定整图对比目标，增加中间层局部监督，用细节反事实描述检验收益。

<a id="paper-150462"></a>

## Aligning Inductive Bias for Data-Efficient Generalization in State Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150462) · [作者来源](https://openreview.net/forum?id=hr5OmcgyP5)

- **问题 / 瓶颈** · 固定的频率偏好可能与任务信号错位，消耗额外样本。
- **核心创新 / 方法** · 分析线性时不变 SSM 诱导核与模型频率响应，再用谱匹配选择初始参数。
- **Baseline** · 默认初始化，对照频谱匹配前后。
- **Benchmark** · 受控合成任务、单层可训练 SSM 及真实深层序列任务，考察数据效率。
- **关键结果 / 消融** · 当任务有相关谱结构且默认频谱错配时收益明显；幅度待核。
- **适用条件 / 局限** · 理论针对线性时不变 SSM，深层实验界限待核。

**可复用机制** · 先测任务与模型初始频率响应的错配，再决定是否花预算做任务自适应初始化。

<a id="paper-139753"></a>

## Aligning Language Model Benchmarks with Pairwise Preferences

[官方论文页](https://neurips.cc/virtual/2026/poster/139753) · [作者来源](https://openreview.net/forum?id=6gX1eKoDVX)

- **问题 / 瓶颈** · 综合基准分数与目标部署中的模型排名常不一致。
- **核心创新 / 方法** · 利用下游表现学习题目权重，在未见模型上预测相对顺序。
- **Baseline** · 原基准与朴素对齐方式，细节待核。
- **Benchmark** · 4576 个模型和六个基准，测下游排序预测和跨规模迁移。
- **关键结果 / 消融** · 作者报告多数情况下能跨规模；部分设置使用少至 20 个模型即能对齐。
- **适用条件 / 局限** · 需已知下游排序，部署任务变化需重验。

**可复用机制** · 以按模型族或规模留出的方式验证题目权重，避免加权时记住当前排名。

<a id="paper-148722"></a>

## Aligning Language Models with Selective Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/148722) · [作者来源](https://openreview.net/forum?id=vXRPlOT3KJ)

- **问题 / 瓶颈** · 提高正确率或校准度未必能改善模型何时应弃答。
- **核心创新 / 方法** · 用选择奖励强化学习直接针对 AURC 训练。
- **Baseline** · 其他正确率、校准或选择性预测路线，具名对照待核。
- **Benchmark** · 同分布与分布外任务上的风险覆盖曲线及面积。
- **关键结果 / 消融** · 作者报告两种分布下风险覆盖权衡均改善；幅度待核。
- **适用条件 / 局限** · 风险标签与部署分布决定曲线含义。

**可复用机制** · 部署要求允许弃答时，以固定覆盖率风险或 AURC 选模型，而非只看原始正确率。

<a id="paper-151436"></a>

## Aligning LLMs Toward Multi-Turn Conversational Outcomes Using Iterative RLHF

[官方论文页](https://neurips.cc/virtual/2026/poster/151436) · [作者来源](https://openreview.net/forum?id=ajJbdafVVH)

- **问题 / 瓶颈** · 多轮延迟目标难直接分配给逐 token 更新。
- **核心创新 / 方法** · 将多轮目标分解成单轮 RLHF 序列，交替采集日志、拟合 Q 与离线批更新。
- **Baseline** · 使用标准单轮 GRPO 优化器，比较方案细节待核。
- **Benchmark** · 六个多轮对话环境，评估目标完成表现。
- **关键结果 / 消融** · 作者论证近似策略改进等价并报告有效；幅度待核。
- **适用条件 / 局限** · 依赖价值估计可概括未来对话效用。

**可复用机制** · 保留单轮训练工具链，把长程反馈通过回合价值接口传给每个回复。

<a id="paper-150322"></a>

## Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation

[官方论文页](https://neurips.cc/virtual/2026/poster/150322) · [作者来源](https://openreview.net/forum?id=iyno3PkrLm)

- **问题 / 瓶颈** · 困惑度几乎不变时，拒答表现仍可能下降。
- **核心创新 / 方法** · 用按通道诊断区分量化误差来源，并据归因选缓解方式。
- **Baseline** · 常规量化及基于注意力的分配，另报告生产量化验证。
- **Benchmark** · 11 个指令模型，五个基准共 1894 个提示，测安全与通用表现。
- **关键结果 / 消融** · 作者报告诊断支持不同模型选择不同缓解方案，恢复最高约 97% 的损失。
- **适用条件 / 局限** · 安全测集覆盖和硬件条件影响结论。

**可复用机制** · 将任务表现、缓存预算和安全回归并列作为部署验收信号。

<a id="paper-150384"></a>

## Alignment Dynamics in LLM Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/150384) · [作者来源](https://openreview.net/forum?id=iRH7xi46GH)

- **问题 / 瓶颈** · 参数空间梯度和输出分布变化呈现不同诊断信号。
- **核心创新 / 方法** · 以可解析对齐分数分解已有约束的反弹和当前数据产生的驱动。
- **Baseline** · 对照不同历史微调及再次暴露设置，细节待核。
- **Benchmark** · 安全对齐与情感设置中的连续微调，另有受控实验。
- **关键结果 / 消融** · 作者报告对齐可反转，重新暴露后恢复更快，后验集中度影响反弹。
- **适用条件 / 局限** · 解析条件和真实训练规模的匹配程度待核。

**可复用机制** · 对交替微调阶段分别记录当前任务和既有对齐，测恢复曲线以识别潜在保留。

<a id="paper-151776"></a>

## Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy

[官方论文页](https://neurips.cc/virtual/2026/poster/151776) · [作者来源](https://openreview.net/forum?id=Y714JTtMXQ)

- **问题 / 瓶颈** · 高熵内容会干扰似然检测。
- **核心创新 / 方法** · 将对齐印记分解为指令偏差和偏好奖励，再做信息加权标准化。
- **Baseline** · Fast-DetectGPT 与其他似然检测。
- **Benchmark** · 零样本文本检测，具体集合和指标定义待全文确认。
- **关键结果 / 消融** · 作者摘要报告相对最强基线改善 45.82%；指标口径待核。
- **适用条件 / 局限** · 依赖可获得模型对及其分布接近等条件。

**可复用机制** · 在成对可用模型上单独检查高熵文本，评估成对差分是否消除内容复杂度偏差。

<a id="paper-152416"></a>

## Align-RAG: Alignment Is All You Need for TSFM In-Context Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152416) · [作者来源](https://openreview.net/forum?id=THqFc0nGPv)

- **问题 / 瓶颈** · 示例形状可用但幅值与时间偏差会干扰上下文。
- **核心创新 / 方法** · 逐对做幅值缩放与整数位移，示例直接进入冻结骨干。
- **Baseline** · 训练的检索融合适配器和未来段洗牌控制。
- **Benchmark** · Chronos-Bolt 七个数据集及四个冻结预测骨干，测 MSE。
- **关键结果 / 消融** · 对训练适配器平均 MSE 降 3.75%；额外骨干降 2.5% 到 13.7%。
- **适用条件 / 局限** · 需要形状对应和整数移位近似，非平稳相位下待核。

**可复用机制** · 在投入训练检索融合头前先测试闭式对齐基线。

<a id="paper-153461"></a>

## ALIGN-Rec: Continual Recommendation under Heterogeneous Unlearning Requests

[官方论文页](https://neurips.cc/virtual/2026/poster/153461) · [作者来源](https://openreview.net/forum?id=L8dS5AKSwG)

- **问题 / 瓶颈** · 共享用户与物品表征会使被删除交互重新起作用。
- **核心创新 / 方法** · 用低秩曲率代理维护保留和遗忘子空间，并构造摘要用于方向约束。
- **Baseline** · 与持续推荐及推荐遗忘路线比较，具名基线待核。
- **Benchmark** · 多推荐数据集、删除粒度及流式设定，评估保留与抑制。
- **关键结果 / 消融** · 作者报告有效并给出子空间追踪与方向抑制的理论保证。
- **适用条件 / 局限** · 曲率近似和交互分布变化的影响待核。

**可复用机制** · 用多轮删后更新评测遗忘，并单独识别共享表示导致的信号恢复。

<a id="paper-150467"></a>

## A Little Robustness Is All You Need: Leveraging Predictions for Contextual Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150467) · [作者来源](https://openreview.net/forum?id=hofrVF7K3J)

- **问题 / 瓶颈** · RMSE 可趋于零但决策超额损失仍为常数。
- **核心创新 / 方法** · 在预测周围小邻域按最坏情形优化，将代价刻画为稳健优化缺口。
- **Baseline** · 直接执行预测状态的最优动作，以及既有定价结果。
- **Benchmark** · 上下文定价、租滑雪板与房屋交易，理论上比较超额损失。
- **关键结果 / 消融** · 三项任务给出随预测 RMSE 的三分之二次幂损失界。
- **适用条件 / 局限** · 适用范围取决于问题稳健缺口和可求解性。

**可复用机制** · 在损失不连续的场景用决策后悔检验预测器，比较直接跟随与邻域稳健动作。

<a id="paper-153797"></a>

## Allocentric Perceiver: Disentangling Allocentric Reasoning from Egocentric Visual Priors via Frame Instantiation

[官方论文页](https://neurips.cc/virtual/2026/poster/153797) · [作者来源](https://openreview.net/forum?id=IchiIZiHVH)

- **问题 / 瓶颈** · 模型难以从观察视角切换到问题指定视角
- **核心创新 / 方法** · 重建度量几何并建立查询指定的参考系，将变换后结果作为结构化信息提供给 VLM
- **Baseline** · 空间微调模型与原始骨干
- **Benchmark** · 多骨干的空间推理基准
- **关键结果 / 消融** · 异位视角任务约提升 10%，原视角能力维持
- **适用条件 / 局限** · 依赖几何恢复准确度

**可复用机制** · 比较显式换坐标与模型自行推理，按视角差分层评测

<a id="paper-151339"></a>

## All Roads Lead to Rome: Flow-driven Multi-Anchor Exploration for Open-Environment Active 3D Mapping

[官方论文页](https://neurips.cc/virtual/2026/poster/151339) · [作者来源](https://openreview.net/forum?id=bIXDUAeSPg)

- **问题 / 瓶颈** · 单点目标在新场景中容易压掉合理探索方向
- **核心创新 / 方法** · 用条件流匹配生成长程锚点分布，再接路径规划
- **Baseline** · 单点目标预测
- **Benchmark** · 未见环境中的主动三维建图
- **关键结果 / 消融** · 作者将单点预测识别为泛化瓶颈，幅度待核
- **适用条件 / 局限** · 依赖本地观测及规划器

**可复用机制** · 固定规划预算，对照单锚和多锚的覆盖及路程

<a id="paper-150665"></a>

## AlphaQ: Calibration-Free Bit Allocation for Mixture-of-Experts Quantization

[官方论文页](https://neurips.cc/virtual/2026/poster/150665) · [作者来源](https://openreview.net/forum?id=gNcuTCbBdm)

- **问题 / 瓶颈** · 代理语料可能误估专家利用率
- **核心创新 / 方法** · 以专家权重谱重尾程度作为混合位宽分配信号
- **Baseline** · 依赖校准集的混精度方法
- **Benchmark** · MoE 语言模型量化，具体配置待核
- **关键结果 / 消融** · 摘要给出专家谱差异作为分配依据，量化结果待核
- **适用条件 / 局限** · 重尾不必然等价于任务重要性

**可复用机制** · 固定显存对照均匀位宽、权重谱与数据校准

<a id="paper-139265"></a>

## ALTER: An Allen's Algebra-Based Evaluation Framework for Temporal Reasoning of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139265) · [作者来源](https://openreview.net/forum?id=ay0UXDsniW)

- **问题 / 瓶颈** · 显式时间点和故事顺序容易泄露答案
- **核心创新 / 方法** · 用 Allen 区间代数构造可验证关系网，再转成自然语言
- **Baseline** · 依赖显式时点的合成任务
- **Benchmark** · 2500 个时序问答，按事件密度和逻辑复杂度划分
- **关键结果 / 消融** · 揭示密集事件性能下降及叙述顺序偏差
- **适用条件 / 局限** · 规则网络到自然故事的迁移待验证

**可复用机制** · 固定逻辑图改写叙述，隔离真正关系推理

<a id="paper-151690"></a>

## A Mahalanobis Margin \texorpdfstring{$\gamma_{\min}$}{gamma\_min} Bound on Task Confusion in Pretrained Class-Incremental Learning: From Infeasibility to Exponential Attenuation

[官方论文页](https://neurips.cc/virtual/2026/poster/151690) · [作者来源](https://openreview.net/forum?id=Yljy4oNHZD)

- **问题 / 瓶颈** · 只缓解遗忘仍可能有跨任务类别混淆
- **核心创新 / 方法** · 在预训练表示上分析原型分类器，推导跨任务混淆上界
- **Baseline** · 联合训练及原型型增量分类器
- **Benchmark** · 类增量学习的理论边界
- **关键结果 / 消融** · 间隔越大时混淆界指数衰减
- **适用条件 / 局限** · 适用受分析的原型分类器，估计依赖特征与协方差

**可复用机制** · 在增量训练前用稳健任务间隔筛选骨干

<a id="paper-155103"></a>

## A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)

[官方论文页](https://neurips.cc/virtual/2026/poster/155103) · [作者来源](https://openreview.net/forum?id=8PbIL0Lq7v)

- **问题 / 瓶颈** · 适配及合并能保留旧能力的条件不清
- **核心创新 / 方法** · 在线性分类和近正交任务下分析最优低秩解及最大间隔
- **Baseline** · 不同正则区间的低秩解
- **Benchmark** · 多类线性分类的理论分析
- **关键结果 / 消融** · 中间正则区间对齐最大间隔解，并给出间隔权衡
- **适用条件 / 局限** · 近正交及线性假设限制外推

**可复用机制** · 调 LoRA 时同时测旧任务和新任务间隔，核对是否可合并

<a id="paper-154547"></a>

## AMARIS: Merging Generalist and Specialist LLMs via Adaptive Subspace Inheritance

[官方论文页](https://neurips.cc/virtual/2026/poster/154547) · [作者来源](https://openreview.net/forum?id=CkmAPV0HiB)

- **问题 / 瓶颈** · 参数插值难控制通用能力受损
- **核心创新 / 方法** · 用广义特征方向建低秩门控，在通用激活偏差预算下保留专家激活
- **Baseline** · 插值、稀疏平均等免训练合并
- **Benchmark** · Qwen3 8B、32B，金融、指令和东南亚多语
- **关键结果 / 消融** · 金融示例报告保留 98.37% 专项及 95.76% 通用能力
- **适用条件 / 局限** · 依赖可估计的激活协方差和代表性样本

**可复用机制** · 比较专家收益和通用损失曲线，再选投影秩及保留预算

<a id="paper-153152"></a>

## A mathematical theory of balancing relational generalization and memorization

[官方论文页](https://neurips.cc/virtual/2026/poster/153152) · [作者来源](https://openreview.net/forum?id=NU4GwTj57W)

- **问题 / 瓶颈** · 仅测可传递关系会掩盖模型无法兼顾规则与例外的问题。
- **核心创新 / 方法** · 构造带例外的传递推断，用核岭回归解析表征几何如何影响行为，并在语言模型微调后检查预测错误。
- **Baseline** · 对照无例外的传递推断与不同表征几何。
- **Benchmark** · 核岭回归的理论设定和顺序关系语言模型任务；指标细节待核。
- **关键结果 / 消融** · 作者报告规则与例外可同时学到，但比无例外任务更依赖表征几何；语言模型出现理论预测的系统性错误。
- **适用条件 / 局限** · 解析结论限于所用模型和任务；复杂规则中的适用性待验证。

**可复用机制** · 测试规则学习时对普通外推与例外记忆分别打分，并比较容易混淆关系的表征。

<a id="paper-150438"></a>

## A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks

[官方论文页](https://neurips.cc/virtual/2026/poster/150438) · [作者来源](https://openreview.net/forum?id=i267XddnJt)

- **问题 / 瓶颈** · 先写场景会限制工具组合
- **核心创新 / 方法** · 用有效性反馈训练对比 n-gram，聚类抽样再迭代难度
- **Baseline** · τ²-Bench
- **Benchmark** · 三个领域与11组模型配对，测成功率及组合覆盖
- **关键结果 / 消融** · 组合数量超过两倍，Gemini-3-Flash 从0.82–0.94降至0.28–0.61
- **适用条件 / 局限** · 有效性取决于模型裁判和工具域

**可复用机制** · 先生成工具调用序列再写题目。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-150099"></a>

## A Mean-Field Framework for Inference-Time Distributional Control of Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150099) · [作者来源](https://neurips.cc/virtual/2026/poster/150099)

- **问题 / 瓶颈** · 逐点奖励难表达多样性及总体匹配
- **核心创新 / 方法** · 用平均场定义倾斜分布，再用加权交互粒子采样
- **Baseline** · 逐点奖励引导为特例
- **Benchmark** · 可解析低维分布上的目标分布匹配
- **关键结果 / 消融** · 作者报告能匹配指定分布，数值待核
- **适用条件 / 局限** · 高维非生物通用场景外推及粒子开销待核

**可复用机制** · 群体目标用交互粒子而非逐样本独立打分。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-153805"></a>

## A Mechanistic Analysis of Looped Reasoning Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153805) · [作者来源](https://openreview.net/forum?id=IZqME3ZTLU)

- **问题 / 瓶颈** · 循环推理的层内行为不明
- **核心创新 / 方法** · 同时追踪潜状态定点与注意力头跨轮行为
- **Baseline** · 标准前馈模型及循环架构变体
- **Benchmark** · 循环语言模型潜状态和注意力行为
- **关键结果 / 消融** · 多种模型的层分别收敛到不同定点，推理阶段逐轮重现
- **适用条件 / 局限** · 结论不覆盖全部循环架构，数值待核

**可复用机制** · 测每层循环轨迹是否稳定以诊断额外迭代价值。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-148276"></a>

## A Mechanistic Investigation of Theory of Mind in a Large Language Model

[官方论文页](https://neurips.cc/virtual/2026/poster/148276) · [作者来源](https://openreview.net/forum?id=z3sn6b2Hk3)

- **问题 / 瓶颈** · 经典错误信念任务同时含表征与现实偏差
- **核心创新 / 方法** · 在人类信念及照片提示间匹配状态与答案，结合因果中介及表征相似度
- **Baseline** · 无主体的照片场景
- **Benchmark** · Qwen2.5-14B-Instruct匹配提示
- **关键结果 / 消融** · 中层头在两类场景跟踪偏差，后层不同头检索答案
- **适用条件 / 局限** · 单模型与经典任务限制

**可复用机制** · 以非心智匹配对照检验所谓心智推理模块。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-155619"></a>

## A Memory Efficient Unified Algorithm for Online Learning of Linear Dynamical Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/155619) · [作者来源](https://openreview.net/forum?id=4D7dKjdRtk)

- **问题 / 瓶颈** · 稳定模态大量存在时全状态维度夸大预测难度
- **核心创新 / 方法** · 将复杂、不衰减或非半单模态计为有效复杂度并构造统一预测算法
- **Baseline** · 有界系数滤波器的方向数下界
- **Benchmark** · 线性动力系统在线预测理论设定
- **关键结果 / 消融** · 参数量约随复杂度平方，滤波器至少需相应数量方向
- **适用条件 / 局限** · 限于论文定义的线性系统和复杂度

**可复用机制** · 按不稳定复杂度而非隐藏维度选择预测器容量。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-154490"></a>

## A meshfree exterior calculus for generalizable and data-efficient learning of physics from point clouds

[官方论文页](https://neurips.cc/virtual/2026/poster/154490) · [作者来源](https://openreview.net/forum?id=DDvFxExo8j)

- **问题 / 瓶颈** · 网格生成限制不同几何间迁移
- **核心创新 / 方法** · 用稀疏Schur补得到虚拟测度，在旋转不变局部坐标学习边通量
- **Baseline** · 神经算子基线
- **Benchmark** · 五个PDE基准及SimJEB
- **关键结果 / 消融** · PDE域外误差低一至两个数量级，支架任务所需训练几何更少
- **适用条件 / 局限** · 点云特征仍须落在训练范围

**可复用机制** · 点云上构造守恒算子后再学习通量。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-148347"></a>

## A Method-Class Divide in Sub-4-Bit Quantization:\\Iterative vs.\ Single-Pass Sensitivity to Data Composition

[官方论文页](https://neurips.cc/virtual/2026/poster/148347) · [作者来源](https://openreview.net/forum?id=yY3pWWSxW5)

- **问题 / 瓶颈** · 重建损失下降未必改善下游
- **核心创新 / 方法** · 匹配200样本预算，比较不同算法和位宽下的数据组成敏感性
- **Baseline** · SignRound V2、OmniQuant、AQLM、GPTQ、AWQ
- **Benchmark** · 六模型三位宽十任务四种子，另有70B核验
- **关键结果 / 消融** · 迭代法增0.74–1.93个百分点，单次解析法变化至多0.30个百分点
- **适用条件 / 局限** · 收益限于性能崩溃前的特定区间

**可复用机制** · 极低位宽下为迭代量化单独优化校准数据。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-150193"></a>

## A method to automatically discover symbolic local learning rules

[官方论文页](https://neurips.cc/virtual/2026/poster/150193) · [作者来源](https://openreview.net/forum?id=k34hp1xwIt)

- **问题 / 瓶颈** · 反传替代规则难解释及迁移
- **核心创新 / 方法** · 构建局部张量单项式字典，回归各层多项式损失使梯度改善全局目标
- **Baseline** · 反向传播及MLP规则生成
- **Benchmark** · 小型网络的重建、分类及自监督任务
- **关键结果 / 消融** · 分类准确率可比反传，发现规则较稀疏
- **适用条件 / 局限** · 仅小模型和极小数据

**可复用机制** · 用稀疏符号损失搜索替代局部黑箱学习器。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-151475"></a>

## A Model of Diverse Sampling from Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151475) · [作者来源](https://openreview.net/forum?id=aKT7UzwbZC)

- **问题 / 瓶颈** · 单条高质量样本重复生成会导致集合覆盖差
- **核心创新 / 方法** · 先抽有限候选池并重要性加权，再做K-DPP或贪心MAP
- **Baseline** · 温度采样、多样束搜索、K-means重排及LLM选择
- **Benchmark** · 开放生成、Ambrosia及GSM8K，质量多样性权衡
- **关键结果 / 消融** · 报告改善帕累托前沿，池大小的KL偏差界为O(1/N)
- **适用条件 / 局限** · 依赖候选池与嵌入距离能覆盖语义模式

**可复用机制** · 用DPP优化整组候选的质量和互补性。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-152127"></a>

## Amortized Bayesian Experimental Design with In-Context Knowledge Conditioning

[官方论文页](https://neurips.cc/virtual/2026/poster/152127) · [作者来源](https://openreview.net/forum?id=VKgRWLKDIJ)

- **问题 / 瓶颈** · 摊销实验策略难接受部署时新先验
- **核心创新 / 方法** · 将先验及历史实验变成token，用共享Transformer及可靠性过滤
- **Baseline** · 不提供额外知识的同类策略
- **Benchmark** · 四个贝叶斯实验设计基准
- **关键结果 / 消融** · 可靠知识加速早期信息获取，无效知识时接近对照
- **适用条件 / 局限** · 过滤器在未知冲突分布下的表现待核

**可复用机制** · 额外知识进入上下文前按当前证据过滤。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-156137"></a>

## Amortized Optimal Transport from Sliced Potentials

[官方论文页](https://neurips.cc/virtual/2026/poster/156137) · [作者来源](https://openreview.net/forum?id=09aWoE8edl)

- **问题 / 瓶颈** · 多对测度反复求解昂贵
- **核心创新 / 方法** · 从切片 Kantorovich 势用最小二乘或对偶目标拟合原势，再恢复计划
- **Baseline** · 逐对求解及两种摊销策略
- **Benchmark** · 重复最优传输问题，指标待核
- **关键结果 / 消融** · 作者报告提升重复求解效率，数值待核
- **适用条件 / 局限** · 依赖训练测度覆盖及势估计质量

**可复用机制** · 固定测度族比较势回归与直接拟合对偶目标

<a id="paper-154315"></a>

## Amortized-Precision Quantization for Early-Exit Vision Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/154315) · [作者来源](https://openreview.net/forum?id=EYh3OlleoZ)

- **问题 / 瓶颈** · 静态量化噪声会改变提前退出路径
- **核心创新 / 方法** · 用随机层暴露刻画深度和精度权衡，再双层优化门槛和位宽
- **Baseline** · 静态全深度量化
- **Benchmark** · ViT 提前退出精度及效率
- **关键结果 / 消融** · 摘要报告改善 Pareto 前沿，幅度待核
- **适用条件 / 局限** · 依赖退出分布的稳定性

**可复用机制** · 部署动态推理时把退出率和位宽视为联合变量

<a id="paper-150646"></a>

## Amortized Vine Copulas for High-Dimensional Density and Information Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/150646) · [作者来源](https://openreview.net/forum?id=gVrwhk9HGC)

- **问题 / 瓶颈** · 逐边拟合 vine copula 耗时
- **核心创新 / 方法** · 用共享去噪模型预测密度格，再投影使边际接近均匀
- **Baseline** · 传统逐边拟合
- **Benchmark** · 合成和真实连续数据
- **关键结果 / 消融** · 摘要报告可用 GPU 推理替代逐边优化，细项待核
- **适用条件 / 局限** · 限简化 vine 与连续数据

**可复用机制** · 让共享估计器学习局部结构，并显式投影保持全局概率约束

<a id="paper-152395"></a>

## Amortizing Generative Guidance for Model-Based Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152395) · [作者来源](https://openreview.net/forum?id=TPXx2a0pW6)

- **问题 / 瓶颈** · 单高斯蒸馏会将不同动作模式平均
- **核心创新 / 方法** · 用生成式多模态提案吸收 MPPI 监督并服务后续规划
- **Baseline** · 单峰高斯提案
- **Benchmark** · 连续控制的模型强化学习
- **关键结果 / 消融** · 作者分析规划监督的多模态性，定量细节待核
- **适用条件 / 局限** · 提案多样性仍受规划器覆盖限制

**可复用机制** · 比较单峰与多峰提案的高价值模式覆盖

<a id="paper-148358"></a>

## Amplitude Decoupling in Gaussian Process Training: Exact Decomposition, Pole Cancellation, and Evaluation-Efficient Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/148358) · [作者来源](https://openreview.net/forum?id=yTtdoIL1Yk)

- **问题 / 瓶颈** · 幅值与其条件最优值失配会导致线搜索拒绝
- **核心创新 / 方法** · 将精确对数似然拆成剖面项和非负幅值失配项
- **Baseline** · 未剖面化精确 GP 优化
- **Benchmark** · Armijo 线搜索及解析分解
- **关键结果 / 消融** · 失配项可归类约八成被拒试探，口径待核
- **适用条件 / 局限** · 依赖精确 GP 的特定参数化

**可复用机制** · 把可解析优化的尺度变量消去再比较求值预算

<a id="paper-149128"></a>

## AMPS: Adaptive Modality Preference Steering via Functional Entropy

[官方论文页](https://neurips.cc/virtual/2026/poster/149128) · [作者来源](https://openreview.net/forum?id=sebyXeDUnB)

- **问题 / 瓶颈** · 同一强度会过度影响正常推理或不足以纠偏
- **核心创新 / 方法** · 以模态贡献率诊断样本敏感度，按输入调整模态偏好
- **Baseline** · 统一强度干预
- **Benchmark** · 多模态模型，详细任务待核
- **关键结果 / 消融** · 作者报告单一强度不适合不同样本，效应幅度待核
- **适用条件 / 局限** · 诊断指标依赖模型内部信息

**可复用机制** · 先测每个样本的模态贡献再分配干预算力

<a id="paper-156737"></a>

## A Multi-Fidelity Control Variate Approach for Policy Gradient Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/156737) · [作者来源](https://neurips.cc/virtual/2026/poster/156737)

- **问题 / 瓶颈** · 高保真交互昂贵，直接迁移低保真又会带来偏差
- **核心创新 / 方法** · 用低保真样本构造控制变量，结合少量高保真数据形成无偏梯度
- **Baseline** · 普通 REINFORCE
- **Benchmark** · 多保真训练，任务及预算待核
- **关键结果 / 消融** · 论文给出无偏降方差估计，经验幅度待核
- **适用条件 / 局限** · 低保真信号与高保真梯度需足够相关

**可复用机制** · 先测跨保真相关性，再选择两种仿真的采样比例

<a id="paper-152756"></a>

## AMUSE: Anytime Muon with Stable Gradient Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/152756) · [作者来源](https://openreview.net/forum?id=QadbBzDY4q)

- **问题 / 瓶颈** · 正交化可能放大陡峭方向噪声
- **核心创新 / 方法** · 用河谷分解诊断正交动量，并设计稳定梯度评估的随时优化
- **Baseline** · AdamW、Muon 及无调度优化
- **Benchmark** · 深度网络优化，具体训练配置待核
- **关键结果 / 消融** · 作者观察到低曲率推进加快与主方向振荡并存
- **适用条件 / 局限** · 河谷诊断的适用范围待核

**可复用机制** · 评估优化器时把沿平坦空间的进展与陡峭方向波动分开测

<a id="paper-150608"></a>

## AnalogToBi: Device-Level Analog Circuit Topology Generation via Bipartite Graph and Grammar Guided Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/150608) · [作者来源](https://openreview.net/forum?id=gsxHqdgGnD)

- **问题 / 瓶颈** · 序列生成容易记忆命名并违反连接规则
- **核心创新 / 方法** · 双部图表示电路，重命名增强并在解码时施加语法
- **Baseline** · 序列式电路生成
- **Benchmark** · 多类型模拟电路，具体配置待核
- **关键结果 / 消融** · 摘要报告结构有效性和泛化改善
- **适用条件 / 局限** · 语法有效不保证电气性能

**可复用机制** · 对结构生成任务分开验证命名不变性、合法性和性能

<a id="paper-155602"></a>

## Analytical Correction for Subsampling Bias in Drifting Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155602) · [作者来源](https://openreview.net/forum?id=4LUhCWAQzE)

- **问题 / 瓶颈** · 自归一化造成有限批次质心偏差
- **核心创新 / 方法** · 推导主导偏差项，再用批内量进行闭式插值校正
- **Baseline** · 未经校正的漂移场
- **Benchmark** · 一步生成模型及批大小，细节待核
- **关键结果 / 消融** · 证明未校正偏差为批大小的倒数阶，给出降低阶数的修正
- **适用条件 / 局限** · 依赖所用质心和渐近条件

**可复用机制** · 对批内归一化估计器先推导偏差再用同预算检验校正

<a id="paper-148817"></a>

## Analyzing and Guiding Zero-Shot Posterior Sampling in Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148817) · [作者来源](https://openreview.net/forum?id=uujn530GnO)

- **问题 / 瓶颈** · 零样本扩散重建常依赖手动调参
- **核心创新 / 方法** · 在高斯先验下闭式表示理想后验和近似采样器并逐谱比较
- **Baseline** · 理想后验及已有近似采样器
- **Benchmark** · 退化观测逆问题，具体任务待核
- **关键结果 / 消融** · 作者给出替代启发式调参的解析框架
- **适用条件 / 局限** · 依赖高斯近似

**可复用机制** · 用可解特例隔离各频段误差后再迁移参数

<a id="paper-155205"></a>

## Analyzing Learning-Dynamics Across Loss and Prediction Choices for Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155205) · [作者来源](https://openreview.net/forum?id=7VbCqahJMH)

- **问题 / 瓶颈** · 只按损失重加权等价会忽略表示瓶颈
- **核心创新 / 方法** · 交叉比较数据、噪声、速度三种预测与三种监督空间
- **Baseline** · 三乘三矩阵内对照
- **Benchmark** · 扩散去噪，按表示瓶颈分层
- **关键结果 / 消融** · 作者发现损失改变噪声级权重，预测空间改变网络学习对象
- **适用条件 / 局限** · 结论受表征能力与训练条件限制

**可复用机制** · 做扩散消融时分别调整输出和损失并按容量分层

<a id="paper-150925"></a>

## An Analytical Model of Compute-limited Multistage Training Pipelines

[官方论文页](https://neurips.cc/virtual/2026/poster/150925) · [作者来源](https://openreview.net/forum?id=eKJJOkZmQA)

- **问题 / 瓶颈** · 多阶段训练效果难用统一算力分配解释
- **核心创新 / 方法** · 建立可解析的预训练、SFT 与 RL 模型
- **Baseline** · 阶段预算与数据质量的模型内对照
- **Benchmark** · 解析多阶段设定，外部验证待核
- **关键结果 / 消融** · 模型复现 SFT 与 RL 互补以及预训练质量上限等现象
- **适用条件 / 局限** · 简化模型给出定性预测

**可复用机制** · 用分阶段等预算消融验证何处出现预训练瓶颈

<a id="paper-139664"></a>

## An Assessment of Human vs. Model Uncertainty in Soft-Label Learning and Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/139664) · [作者来源](https://openreview.net/forum?id=C9mjkOAlNE)

- **问题 / 瓶颈** · 软标签改善可能来自纠正标签而非表达不确定性
- **核心创新 / 方法** · 重新标注并构造受控对照隔离众数变化
- **Baseline** · 人类软标签、合成标签及受控对照
- **Benchmark** · MNIST 与合成变体，测准确率、校准和训练稳定
- **关键结果 / 消融** · 作者报告主要收益在难样本校准与多次训练稳定
- **适用条件 / 局限** · 需多位标注者，复杂任务泛化待核

**可复用机制** · 固定标签众数后比较软硬监督，避免把纠错归于不确定性建模

<a id="paper-155331"></a>

## Anatomy of Off-Policy Policy Gradient: Importance Sampling, KL Regularization, and Baselines

[官方论文页](https://neurips.cc/virtual/2026/poster/155331) · [作者来源](https://openreview.net/forum?id=6QcGiRb4iq)

- **问题 / 瓶颈** · 离策略更新可能使最优策略失去驻点性质。
- **核心创新 / 方法** · 分析保持驻点的校正，把组相对梯度关联到轨迹 Bellman 残差，并以基线偏移实现悲观。
- **Baseline** · 轨迹重要性加权、GRPO 及传统离线 RL。
- **Benchmark** · 一般离策略目标、全策略与单策略覆盖理论，测驻点和遗憾界。
- **关键结果 / 消融** · 该目标族仅两组校正保持所述驻点；非对称 REINFORCE 有单策略覆盖遗憾界。
- **适用条件 / 局限** · 结论限于所设目标族及覆盖假设。

**可复用机制** · 更换离策略基线前检查驻点与悲观性是否随之变化。

<a id="paper-154471"></a>

## Anchoring Reasoning Distillation via Syntactic Constraints

[官方论文页](https://neurips.cc/virtual/2026/poster/154471) · [作者来源](https://openreview.net/forum?id=DLOseBaFqU)

- **问题 / 瓶颈** · 整条丢弃有算术错的推理会损失计划监督。
- **核心创新 / 方法** · 拆成前提、操作、结果，符号执行核验并对错误结果做梯度屏蔽。
- **Baseline** · 六个对照含 PoT 和 Gold-SFT。
- **Benchmark** · 三个 Qwen3 尺度，八基准，含 GSM8K、MATH-500、AIME、ProofWriter。
- **关键结果 / 消融** · 1.7B 下相对最近对照 GSM8K 增 11.1、MATH-500 增 9.8；纯逻辑对照中尺度优势消失。
- **适用条件 / 局限** · 依赖可符号执行的操作，算术卸载的因果贡献未完全隔离。

**可复用机制** · 核验教师轨迹时区分操作计划与执行结果，并以纯逻辑任务检验迁移。

<a id="paper-153959"></a>

## Anchor PCA

[官方论文页](https://neurips.cc/virtual/2026/poster/153959) · [作者来源](https://openreview.net/forum?id=HFtvKUB8yF)

- **问题 / 瓶颈** · 少数域的高方差会支配池化特征。
- **核心创新 / 方法** · 平衡解释方差与共享子空间对各域子空间的一致性，可化为修正矩阵 PCA。
- **Baseline** · 池化 PCA 与最坏域对照。
- **Benchmark** · 仿真与有时间漂移的气体传感数据，测不变空间恢复及未见域解释方差。
- **关键结果 / 消融** · 恢复最大不变子空间；未见域方差解释改善。
- **适用条件 / 局限** · 理论依赖有界域特异协方差膨胀。

**可复用机制** · 多域无监督表示先验证共享方差方向，避免仅按池化解释率选择维度。

<a id="paper-150033"></a>

## AnchorWorld: Embodied Egocentric World Simulation with View-based Evolution Customization

[官方论文页](https://neurips.cc/virtual/2026/poster/150033) · [作者来源](https://openreview.net/forum?id=lGpA57MjjA)

- **问题 / 瓶颈** · 第一人称画面常截断人体，导致交互空间关系不完整。
- **核心创新 / 方法** · 用外部视角监督完整人体和场景关系，以世界坐标锚点及文本控制局部变化。
- **Baseline** · 现有自视角模拟方法，名称待核。
- **Benchmark** · 自视角交互和定制场景，考察时空几何及文本条件一致性。
- **关键结果 / 消融** · 作者报告比对照改善，摘要未给数值。
- **适用条件 / 局限** · 需要外部相机监督和可靠共用坐标。

**可复用机制** · 用同一第一视角推理预算消融训练期外部视角，并检查被遮挡肢体的接触关系。

<a id="paper-152945"></a>

## ANCRe: Adaptive Neural Connection Reassignment for Efficient Depth Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/152945) · [作者来源](https://openreview.net/forum?id=PDLcIMayHD)

- **问题 / 瓶颈** · 固定残差布局可能让深层参与不足或收敛慢。
- **核心创新 / 方法** · 参数化并从数据学习残差连接，分析其布局对优化的影响。
- **Baseline** · 常规残差连接。
- **Benchmark** · LLM 预训练、扩散模型、深层 ResNet，测收敛和深度效率。
- **关键结果 / 消融** · 示例理论存在指数收敛率差距；作者报告实践开销低于 1%。
- **适用条件 / 局限** · 理论示例与大模型效果的因果外推待核。

**可复用机制** · 固定层数和算力，用可学习路由对照固定残差布局。

<a id="paper-139580"></a>

## AndroidReality: How Far Are Mobile Agents from the Real World?

[官方论文页](https://neurips.cc/virtual/2026/poster/139580) · [作者来源](https://openreview.net/forum?id=H8jkwac4sG)

- **问题 / 瓶颈** · 干净移动端评测会高估真实界面下可靠性。
- **核心创新 / 方法** · 用 MDP 三轴构造 AndroidWorld 压力测试，并检验免训练自省恢复。
- **Baseline** · 原 AndroidWorld 与有无恢复的 Agent 配置。
- **Benchmark** · 干净及受控扰动环境，检查失败类型和任务表现。
- **关键结果 / 消融** · 作者报告显著稳健性缺口和四类错误，恢复机制改善两类环境。
- **适用条件 / 局限** · 模拟扰动对真实设备分布覆盖待核。

**可复用机制** · 维护 UI agent 时分层报告各扰动轴鲁棒性与恢复成本。

<a id="paper-150140"></a>

## An Educated Guess: Deriving Statistically Aligned Gradient Estimates for Zeroth-Order Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150140) · [作者来源](https://openreview.net/forum?id=kMdijHwnR7)

- **问题 / 瓶颈** · 高维各向同性扰动易与梯度错位。
- **核心创新 / 方法** · 在随机假设下从激活几何估计搜索方向，配合方向正交和协方差校正。
- **Baseline** · 常规扰动方法及反向传播。
- **Benchmark** · 多层和卷积网络，测梯度对齐、偏差方差及稳定性。
- **关键结果 / 消融** · 作者分析探测稳定机制；摘要未给量化增益。
- **适用条件 / 局限** · 依赖激活结构对梯度有指示作用。

**可复用机制** · 固定查询预算，在零阶微调中比较各向同性和激活条件探测。

<a id="paper-151262"></a>

## An Efficient Geometric Characterization of Robust Fair Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151262) · [作者来源](https://openreview.net/forum?id=bi33LQMlVp)

- **问题 / 瓶颈** · 严格约束下最优分类器的准确率可能在小分布变化时骤变。
- **核心创新 / 方法** · 对可表示成凸多面体的假设族给出几何判定，并用线性规划审计。
- **Baseline** · 严格公平和近似公平约束的理论对照。
- **Benchmark** · 随机化分类器及线性损失设定，覆盖人口统计均等、机会均等与预测均等。
- **关键结果 / 消融** · 作者给出稳健性的完整刻画，并证明在其设定内放宽为近似公平可得到稳健性。
- **适用条件 / 局限** · 理论依赖凸多面体假设族及线性准则；放宽容差的代价需按场景判断。

**可复用机制** · 对集成分类器选公平容差前，用可行域几何检查严格约束下的性能敏感性。

<a id="paper-139297"></a>

## An Embarrassingly Simple Graph Heuristic Reveals Shortcut-Solvable Benchmarks for Sequential Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/139297) · [作者来源](https://openreview.net/forum?id=Yt9idh9KSB)

- **问题 / 瓶颈** · 常用测试集可能有局部转移和特征相似捷径。
- **核心创新 / 方法** · 以短历史在物品转移图召回、按特征相似排名，并按分支数、平滑性和长历史依赖诊断。
- **Baseline** · 现代序列推荐方法及短历史图启发式。
- **Benchmark** · 14 个数据集，含 Amazon Review Sports 与 CDs；比较 NDCG@10。
- **关键结果 / 消融** · 作者报告启发式在 10/14 个数据集有竞争力；两个具名数据集较最强对照相对提高 38.10% 和 44.18%。
- **适用条件 / 局限** · 适用性受数据结构和划分限制；不能从离线排序外推部署收益。

**可复用机制** · 在每个序列基准增加低成本短历史对照，并在削弱捷径的分组检查复杂模型是否仍有优势。

<a id="paper-151029"></a>

## An Empirical Study on Noisy Data and LLM Pretraining Loss Divergence

[官方论文页](https://neurips.cc/virtual/2026/poster/151029) · [作者来源](https://openreview.net/forum?id=dUlQyCtmxc)

- **问题 / 瓶颈** · 真实语料噪声与损失发散关系不清
- **核心创新 / 方法** · 在干净语料注入可控随机噪声，扫描比例和规模
- **Baseline** · 以干净数据与不同噪声设置作对照
- **Benchmark** · 480M 至 5.2B 模型的预训练损失
- **关键结果 / 消融** · 噪声可诱发发散，概率随类型、比例和规模变化
- **适用条件 / 局限** · 人工注入不完全代表自然噪声

**可复用机制** · 预训练压力测试按噪声类型分层并记录发散率

<a id="paper-154592"></a>

## An Equivariance Principle for Optimizer Design: Symmetry-Compatible Updates for Embeddings, LM Heads, and MoE Routers

[官方论文页](https://neurips.cc/virtual/2026/poster/154592) · [作者来源](https://openreview.net/forum?id=CROYfMoFTK)

- **问题 / 瓶颈** · 逐坐标更新破坏正交等变性
- **核心创新 / 方法** · 按线性层、嵌入与路由器的不同对称性导出谱或行级更新
- **Baseline** · Adam 与相关谱优化器
- **Benchmark** · 矩阵层更新的理论分析；实验细节待核
- **关键结果 / 消融** · 指出逐坐标适应与矩阵谱结构的冲突
- **适用条件 / 局限** · 依赖参数的对称群；收益需分别评估

**可复用机制** · 在层型变换下核查更新等变性再选优化器

<a id="paper-152478"></a>

## An exact information theory of generalization phase transitions in Bayesian diffusion models

[官方论文页](https://neurips.cc/virtual/2026/poster/152478) · [作者来源](https://openreview.net/forum?id=SmybBxKaYv)

- **问题 / 瓶颈** · 高维分布学习边界难解析
- **核心创新 / 方法** · 以受限观测的贝叶斯后验反向扩散，分析数据量与信息量
- **Baseline** · 局部信息限制的解析扩散模型
- **Benchmark** · BIRD 理论与早期训练的 UNet、DiT
- **关键结果 / 消融** · 推导记忆与泛化的相边界
- **适用条件 / 局限** · 精确结论针对解析模型

**可复用机制** · 扫描训练样本量和有效感受野并测记忆迹象

<a id="paper-154802"></a>

## Angular Networks: Low-Bit Learning from Randomized Similarity Estimators

[官方论文页](https://neurips.cc/virtual/2026/poster/154802) · [作者来源](https://openreview.net/forum?id=ArO2Yj6xnL)

- **问题 / 瓶颈** · 直接量化欧氏线性算子可能需代理梯度
- **核心创新 / 方法** · 前向用随机低比特投影估计余弦，反向按连续角几何计算
- **Baseline** · 量化线性层及直通估计路线
- **Benchmark** · 单层植入模型理论；实践评测细节待核
- **关键结果 / 消融** · 小 G-Gradient 在设定内蕴含精确恢复
- **适用条件 / 局限** · 理论限单层植入设置

**可复用机制** · 在等比特预算比较余弦估计和量化线性层

<a id="paper-153353"></a>

## An Information-theoretic Framework for Auditing Unfairness in Training Data

[官方论文页](https://neurips.cc/virtual/2026/poster/153353) · [作者来源](https://openreview.net/forum?id=M0oyqiGx4z)

- **问题 / 瓶颈** · 模型审计难区分数据本身的偏差
- **核心创新 / 方法** · 以独立性公理定义特征集合信息量，用 Shapley 分摊贡献
- **Baseline** · 基础信息度量和模型级审计
- **Benchmark** · 统计均等和均等机会等定义下的分析
- **关键结果 / 消融** · 部分度量的贡献能调节冗余
- **适用条件 / 局限** · 估计互信息和联盟贡献需要可靠样本

**可复用机制** · 固定公平定义后在训练前检查特征冗余和偏差信号

<a id="paper-151971"></a>

## Annealing in variational inference mitigates mode collapse: a theoretical study on Gaussian mixtures

[官方论文页](https://neurips.cc/virtual/2026/poster/151971) · [作者来源](https://openreview.net/forum?id=WS1Hwfq4Ay)

- **问题 / 瓶颈** · 变分推断可能漏掉混合分布的模式
- **核心创新 / 方法** · 利用低维统计量刻画退火下的坍塌概率
- **Baseline** · 不同初温和退火速率
- **Benchmark** · 高斯混合理论与 RealNVP 数值验证
- **关键结果 / 消融** · 合理调度能降低塌缩，流模型呈定性趋势
- **适用条件 / 局限** · 解析边界限高斯混合

**可复用机制** · 扫初温和退火时长并以模式覆盖选配置

<a id="paper-151951"></a>

## A Novel Schur-Decomposition-Based Weight Projection Method for Stable State-Space Neural-Network Architectures

[官方论文页](https://neurips.cc/virtual/2026/poster/151951) · [作者来源](https://openreview.net/forum?id=WbOem86LmL)

- **问题 / 瓶颈** · 拟合准确的模型可能有不稳定长期动力学
- **核心创新 / 方法** · 投影实 Schur 分解的准三角因子到稳定形式，支持反向传播
- **Baseline** · 已有稳定系统辨识方法
- **Benchmark** · 合成线性系统，以精度、收敛和复杂度比较
- **关键结果 / 消融** · 作者报告精度和收敛可比，复杂度略增
- **适用条件 / 局限** · 验证主要针对线性系统

**可复用机制** · 辨识时比较硬稳定投影与软惩罚，并检查长时滚动

<a id="paper-150213"></a>

## Answering At Any Cost: Frontier LLMs Are Consequence-Insensitive

[官方论文页](https://neurips.cc/virtual/2026/poster/150213) · [作者来源](https://openreview.net/forum?id=juGEeYEuAS)

- **问题 / 瓶颈** · 常用准确率忽略模型是否随风险调整行为
- **核心创新 / 方法** · 用显式效用或自然语言改写风险，检查提交或拒答变化
- **Baseline** · 五个前沿模型家族
- **Benchmark** · 编码与数学推理，测风险响应和拒答
- **关键结果 / 消融** · 模型系统性拒答不足，某些严格应拒答条件仍作答
- **适用条件 / 局限** · 提示中的后果与真实部署有距离

**可复用机制** · 单独扫描错误成本，记录准确率和有害过度提交

<a id="paper-149938"></a>

## Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information

[官方论文页](https://neurips.cc/virtual/2026/poster/149938) · [作者来源](https://openreview.net/forum?id=m54c3b8Evb)

- **问题 / 瓶颈** · 特权提示可能抑制长推理所需的试探
- **核心创新 / 方法** · 用点互信息诊断影响，反转蒸馏方向并以熵门控
- **Baseline** · 默认在策略自蒸馏
- **Benchmark** · 数学推理；具名基准待核
- **关键结果 / 消融** · 摘要指出特权上下文对结构和探索 token 方向不同
- **适用条件 / 局限** · 依赖教师条件和可核验解法

**可复用机制** · 采用自蒸馏前对照有无特权信息时探索 token 的变化

<a id="paper-152934"></a>

## AnyEdit: A Unified Framework for Speech and Singing Voice Editing with Real-World Environmental Consistency

[官方论文页](https://neurips.cc/virtual/2026/poster/152934) · [作者来源](https://openreview.net/forum?id=PHYLBNJrV1)

- **问题 / 瓶颈** · 端到端带噪生成混淆内容修改和环境重建
- **核心创新 / 方法** · 从噪声输入蒸馏干净韵律 token，分阶段以流匹配渲染源声学上下文
- **Baseline** · 强语音及歌声编辑基线，名称待核
- **Benchmark** · AnyEditBench 与中英文语音歌声，评估内容准确、主观质量和背景一致
- **关键结果 / 消融** · 作者报告噪声与混响下三方面改善
- **适用条件 / 局限** · 依赖源声学上下文，独立消融待核

**可复用机制** · 将内容决策和环境渲染拆开，并单独测未修改片段稳定性。

<a id="paper-154127"></a>

## AnyMo: Geometry-Aware Setup-Agnostic Modeling of Human Motion in the Wild

[官方论文页](https://neurips.cc/virtual/2026/poster/154127) · [作者来源](https://openreview.net/forum?id=G4z36ToJi1)

- **问题 / 瓶颈** · IMU 信号依赖位置、朝向与设备
- **核心创新 / 方法** · 物理模拟多身体位置，配对位置视图并遮盖部分观测训练图编码器，再和语言对齐
- **Baseline** · 各任务既有方法，具名对照待核
- **Benchmark** · 14 个未见识别数据集，另测跨模态检索与描述
- **关键结果 / 消融** · 摘要报告识别 Accuracy/F1/R@2 平均提高 11.7%/11.6%/22.6%
- **适用条件 / 局限** · 依赖合成 IMU 对现场条件的覆盖

**可复用机制** · 让同一状态的不同传感器布置成为配对监督，再留出未见布置测试。

<a id="paper-153279"></a>

## AnyMo: Scaling Any-Modality Conditional Motion Generation with Masked Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/153279) · [作者来源](https://openreview.net/forum?id=MRJBlKpvg3)

- **问题 / 瓶颈** · 固定模态架构难覆盖文本、音乐和轨迹组合
- **核心创新 / 方法** · 对齐多模态动作数据，以残差 FSQ 表示动作并用掩码 Transformer 建模
- **Baseline** · 具体对照待核
- **Benchmark** · OmniHuMo，测试多模态组合的动作质量和空间风格控制
- **关键结果 / 消融** · 作者报告支持任意模态组合，量化结果待核
- **适用条件 / 局限** · 数据规模和具体模型机制的贡献需分别验证

**可复用机制** · 共享动作词表并按控制模态组合分层测缺失输入。

<a id="paper-154243"></a>

## Anytime-Valid Conformal Risk Control

[官方论文页](https://neurips.cc/virtual/2026/poster/154243) · [作者来源](https://openreview.net/forum?id=FCHpcvgVme)

- **问题 / 瓶颈** · 固定样本量的平均风险保证不覆盖任意中途停止
- **核心创新 / 方法** · 用分位数推导递增校准集上的高概率联合控制
- **Baseline** · 固定样本保形风险控制
- **Benchmark** · 理论界、仿真与真实数值例子，详情待核
- **关键结果 / 消融** · 给出匹配下界并证明渐近紧致
- **适用条件 / 局限** · 分布漂移的具体要求待核

**可复用机制** · 预先写明可重复查看的校准协议，并采用覆盖停止规则的保证。

<a id="paper-153451"></a>

## Anytime-Valid PAC-Bayes Certificates for Adaptive Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/153451) · [作者来源](https://openreview.net/forum?id=LBokJOYjeC)

- **问题 / 瓶颈** · 反复查看验证集会使固定配方误差条偏乐观
- **核心创新 / 方法** · 对随机预测器及费用推导时间一致 PAC-Bayes 证书
- **Baseline** · 固定配方验证界与不同采样预算
- **Benchmark** · 合成审计及 192 道 GSM8K、gpt-4.1-mini
- **关键结果 / 消融** · 正确答案是唯一众数时投票才有指数改善保证，否则增算力可放大错误
- **适用条件 / 局限** · 有限审计不能代替目标域覆盖

**可复用机制** · 同时记录预算搜索与停止规则，将收益按答案众数边际分层。

<a id="paper-154936"></a>

## ApertureAttn: Native 4K Video Generation with Image-Only Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/154936) · [作者来源](https://openreview.net/forum?id=9pq44O4Vzq)

- **问题 / 瓶颈** · 高分辨率视频数据稀缺
- **核心创新 / 方法** · 以倒置注意力金字塔集中适配空间细节，时序采用距离引导注意力和窗口外推
- **Baseline** · 直接用高分辨率视频训练的方法
- **Benchmark** · 原生 4K 生成评估画质与时序一致性，指标待核
- **关键结果 / 消融** · 作者报告图像监督下具竞争力，成本与分项数值待核
- **适用条件 / 局限** · 依赖已有视频先验，长时运动边界待核

**可复用机制** · 分离空间分辨率训练与时序约束，分别核对细节和闪烁。

<a id="paper-152333"></a>

## APIVOT: Adaptive Planning with Interleaved Vision-Language Thoughts

[官方论文页](https://neurips.cc/virtual/2026/poster/152333) · [作者来源](https://openreview.net/forum?id=TrMEmzHHdo)

- **问题 / 瓶颈** · 语义分解不能直接保证物理可执行
- **核心创新 / 方法** · 在语言任务推理与视觉未来状态之间学习按需交替
- **Baseline** · 通用 VLM 及已有规划框架
- **Benchmark** · 长程厨房任务，按空间约束比较成功与推理效率
- **关键结果 / 消融** · 作者报告空间限制强时增益最大
- **适用条件 / 局限** · 视觉想象真实性及跨任务适用性待核

**可复用机制** · 对照固定模态调度和按需验证，并按空间约束程度统计。

<a id="paper-139154"></a>

## APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings

[官方论文页](https://neurips.cc/virtual/2026/poster/139154) · [作者来源](https://openreview.net/forum?id=hu9OtupX9p)

- **问题 / 瓶颈** · 已有测法可能混淆风格偏好和总体回答质量
- **核心创新 / 方法** · 隐藏重采样用户属性与响应属性的映射
- **Baseline** · 路由、检索增强、软提示及无个性化
- **Benchmark** · Llama-3.1-8B、Qwen-3.5-27B 上的 APM 风格适配
- **关键结果 / 消融** · 路由最稳定，检索仅强底座受益，软提示无显著改善
- **适用条件 / 局限** · 随机映射不等同真实偏好分布

**可复用机制** · 评测历史个性化时控制先验捷径并分别测风格与质量。

<a id="paper-139053"></a>

## Apple-$\pi$: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence

[官方论文页](https://neurips.cc/virtual/2026/poster/139053) · [作者来源](https://openreview.net/forum?id=nwMoRojkLQ)

- **问题 / 瓶颈** · 最终视频貌似合理不能定位物理错误所在
- **核心创新 / 方法** · 用单定律与多定律场景结合三阶段可见推理和客观物理指标
- **Baseline** · 11 个模型
- **Benchmark** · Orchard 400 段视频和十类经典力学任务
- **关键结果 / 消融** · 最高得分仅 0.473，作者报告多定律迁移与仿真到真实差距
- **适用条件 / 局限** · 可见轨迹不能证明内部推理，物理范围限经典力学

**可复用机制** · 在终态评分之外增加隔离定律和分阶段指标。

<a id="paper-149693"></a>

## Approaching Effective Merging in Model Embedding Space

[官方论文页](https://neurips.cc/virtual/2026/poster/149693) · [作者来源](https://openreview.net/forum?id=o8ovLEF82T)

- **问题 / 瓶颈** · 参数更新不对齐时平均权重会相互抵消
- **核心创新 / 方法** · 从预训练模型低秩结构构造更新表示，再用对齐子空间合并
- **Baseline** · 朴素权重平均等，具名方法待核
- **Benchmark** · ViT 视觉与多模态语言模型任务
- **关键结果 / 消融** · 作者报告合并效果改善，幅度待核
- **适用条件 / 局限** · 依赖共享底座和可表征的低秩适配

**可复用机制** · 将平均位置作为设计变量，比较原权重空间与共享表示空间。

<a id="paper-154340"></a>

## Approaching I/O-optimality for Approximate Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/154340) · [作者来源](https://openreview.net/forum?id=EKuz0q2V2L)

- **问题 / 瓶颈** · 精确注意力即便优化仍可能随序列长度二次增长数据搬运
- **核心创新 / 方法** · 利用近似注意力结构构造 I/O 算法并证明对应制度下界
- **Baseline** · FlashAttention 与相关变体
- **Benchmark** · 按序列长度、维度和快内存容量比较理论数据传输
- **关键结果 / 消融** · 多数参数制度给出近线性序列长度依赖，且接近下界
- **适用条件 / 局限** · 近似条件及误差边界须查正文，未见硬件实测

**可复用机制** · 分开测数据搬运量、近似误差和计算时间以确定切换算法的制度。

<a id="paper-150755"></a>

## Approximate Matrix–Vectors Under a Bounded $\ell_1$ Assumption and Applications to Kernel Matrices

[官方论文页](https://neurips.cc/virtual/2026/poster/150755) · [作者来源](https://openreview.net/forum?id=fdnwYRqXgU)

- **问题 / 瓶颈** · 精确乘积的二次开销对稀轻矩阵浪费
- **核心创新 / 方法** · 有界总质量下用采样近似，核矩阵通过密度估计约简
- **Baseline** · 既有高斯核矩阵乘算法
- **Benchmark** · 理论查询复杂度、预处理成本与加性误差
- **关键结果 / 消融** · 一般矩阵查询为 O(γn^1.5/ε)，核版本无需预处理
- **适用条件 / 局限** · 依赖质量上界及密度估计器噪声分析

**可复用机制** · 先评估矩阵总质量，再按误差预算比较精确与采样式求乘。

<a id="paper-148575"></a>

## Approximate Memory Suffices for Universal Approximation with State Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148575) · [作者来源](https://openreview.net/forum?id=wqs1OgZFKP)

- **问题 / 瓶颈** · 简单线性状态能否支持普适序列映射不明确
- **核心创新 / 方法** · 用固定对角收缩积累指数痕迹，奇异 Vandermonde 读出近似短窗
- **Baseline** · 精确有限延迟恢复及一般非线性循环
- **Benchmark** · 紧输入集上的连续因果时间等变衰减记忆算子
- **关键结果 / 消融** · 证明均匀近似和固定有限痕迹无法精确恢复延迟
- **适用条件 / 局限** · 精度相关读出存在条件数代价

**可复用机制** · 使用稳定简单递推时单独监控读出条件数，勿以普适性推断精确记忆。

<a id="paper-155522"></a>

## Approximation Guarantees for Robust Aggregation in Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155522) · [作者来源](https://openreview.net/forum?id=4ySjO4QTTH)

- **问题 / 瓶颈** · 面对异常参与方时，几何有效性约束可能牺牲对参考均值的逼近。
- **核心创新 / 方法** · 分别给出盒有效性与凸包有效性下的近似界，并构造达到相应上界的聚合方法。
- **Baseline** · 比较盒有效与凸包有效的聚合规则。
- **Benchmark** · FedSGD、FedAvg 和标准异常参与方设定；观察稳定性与异质数据上的准确性。
- **关键结果 / 消融** · 凸包有效性下构造 2d 近似，匹配已有下界；实验中更强有效性改善稳定性，更紧的均值逼近可能提高异质场景准确率。
- **适用条件 / 局限** · 部分界依赖参与方数大于异常方上限的两倍，适用条件须逐条区分。

**可复用机制** · 在固定数据异质性下联合报告稳定性和均值逼近，而不是用单一准确率决定聚合器。

<a id="paper-154229"></a>

## Approximation in Contrastive Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154229) · [作者来源](https://openreview.net/forum?id=FFSgETbjWN)

- **问题 / 瓶颈** · 增大嵌入宽度何时改善检索缺少可解释的近似条件。
- **核心创新 / 方法** · 将 PMI 关联到紧算子，分析内积模型的有限秩谱近似，并推导风险到检索误差的校准界。
- **Baseline** · 对照有限秩内积模型与一般神经评分函数。
- **Benchmark** · 理论比较谱尾误差、结构低秩下逼近速率和下游检索误差。
- **关键结果 / 消融** · 有限维误差受谱尾控制，满足密度比噪声条件时得到快校准率。
- **适用条件 / 局限** · 需要紧算子等分析假设；实际数据中谱尾的估计稳定性待核。

**可复用机制** · 先测经验谱尾，再判断加宽双编码器是否可能提升检索。

<a id="paper-154351"></a>

## A Primal-dual Approach for Semi-Infinitely Constrained Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154351) · [作者来源](https://openreview.net/forum?id=EEnVsdysX0)

- **问题 / 瓶颈** · 约束无限多时，内层搜索昂贵，也可能使策略过度保守。
- **核心创新 / 方法** · 将任务写成正则化鞍点问题，以一阶更新配合 NPG 或 PPO 子程序。
- **Baseline** · 已有原始型半无限约束强化学习算法。
- **Benchmark** · 数值实验和无线通信功率控制；具体指标待核。
- **关键结果 / 消融** · 作者报告优于所比原始型方法且无需解内层优化。
- **适用条件 / 局限** · 依赖鞍点表述和约束估计质量，部署时硬约束保证待核。

**可复用机制** · 在相同采样预算下比较每次策略更新的成本、违规率和任务回报。

<a id="paper-151448"></a>

## A Principled Self-Referenced Early Stopping Approach for Deep Image Prior

[官方论文页](https://neurips.cc/virtual/2026/poster/151448) · [作者来源](https://openreview.net/forum?id=aagILQC10A)

- **问题 / 瓶颈** · 深度图像先验训练过久会拟合噪声，而重复独立测量通常不可得。
- **核心创新 / 方法** · 构造伪自参考图像并分析共享噪声如何影响验证，给出按逆问题定制的早停方法。
- **Baseline** · 既有深度图像先验早停方法。
- **Benchmark** · 自然图像恢复和医学重建，不同噪声类型及水平。
- **关键结果 / 消融** · 作者报告多种设置表现改善，且无需事先知道噪声特性。
- **适用条件 / 局限** · 伪观测的共享噪声可能使停止规则偏移，需核查构造适用条件。

**可复用机制** · 比较训练损失与伪参考误差的停止位置，并按共享噪声强度报告误差。

<a id="paper-149524"></a>

## APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/149524) · [作者来源](https://openreview.net/forum?id=pVNs5UOYq3)

- **问题 / 瓶颈** · 大规模代理逐个调用成本高，但简单复用可能偏移群体分布。
- **核心创新 / 方法** · 将人口转移估计拆为覆盖、抽查残差、传播偏差和上下文错位，并据此控制原型模拟。
- **Baseline** · 规模导向与同预算方法，全量语言模型模拟为参考。
- **Benchmark** · 千万代理多轮舆论模拟，比较调用次数和最终轮 JSD。
- **关键结果 / 消融** · 作者报告较全量模拟减少约 381.1 倍调用，最终轮 JSD 为 0.094。
- **适用条件 / 局限** · 目标是逼近全量模型模拟，和真实群体的一致性需独立验证。

**可复用机制** · 报告复用率时同时保留原型覆盖误差和独立审计残差。

<a id="paper-155186"></a>

## AR1-ZO: Topology-Aware Rank-1 Zeroth-Order Queries for High-Rank LoRA Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/155186) · [作者来源](https://openreview.net/forum?id=7eOsaBX3qO)

- **问题 / 瓶颈** · 固定评估噪声下，高秩联合扰动的有效信号可能衰减。
- **核心创新 / 方法** · 使用交替秩一原子查询与随秩调整的拓扑缩放，保持激活方向信号。
- **Baseline** · 匹配查询次数的零阶微调方法。
- **Benchmark** · OPT 与 Qwen3，在每次两次前向预算下比较信号与高秩适配。
- **关键结果 / 消融** · 作者报告恢复沿有效方向的信号，使高秩 LoRA 可用。
- **适用条件 / 局限** · 尽管单次查询规模不随秩增加，覆盖所有方向仍有摊销成本。

**可复用机制** · 做同预算消融时将高秩扰动信噪比和长期覆盖效率分开记录。

<a id="paper-154895"></a>

## Arbitrarily Conditioned Hierarchical Flows for Spatiotemporal Events

[官方论文页](https://neurips.cc/virtual/2026/poster/154895) · [作者来源](https://openreview.net/forum?id=A8CPCX5IjP)

- **问题 / 瓶颈** · 固定因果训练顺序难以处理任意已知事件或缺失模式。
- **核心创新 / 方法** · 以历史编码器和生成解码器实现层级流，用混合掩码训练任意观察条件并计算条件强度。
- **Baseline** · 既有预测和条件推断基线，具名方法待核。
- **Benchmark** · 合成和真实事件数据，测预测与条件推断。
- **关键结果 / 消融** · 作者报告两类任务均优于所比模型，具体幅度待核。
- **适用条件 / 局限** · 依赖训练掩码覆盖部署缺失模式，条件强度校准待核。

**可复用机制** · 在相同骨干上对照固定顺序和混合掩码，以完全留出的观察模式衡量迁移。

<a id="paper-156755"></a>

## ARC-Encoder: learning compressed text representations for large language models

[官方论文页](https://neurips.cc/virtual/2026/poster/156755) · [作者来源](https://neurips.cc/virtual/2026/poster/156755)

- **问题 / 瓶颈** · 文本上下文增长带来较大推理支出，不同解码器通常需要重新训练压缩器。
- **核心创新 / 方法** · 学习较少的连续文本表示，并适配多个基础或指令解码器。
- **Baseline** · 对照原文本输入及不同压缩倍率。
- **Benchmark** · 上下文学习和窗口扩展等任务，比较效果与推理效率。
- **关键结果 / 消融** · 作者报告常用压缩倍率为四倍或八倍，单编码器可微调至多个解码器。
- **适用条件 / 局限** · 压缩可能丢失精确词面信息，跨解码器依赖适配。

**可复用机制** · 在同等上下文预算下比较原文截断和潜空间压缩，并单测细节保真。

<a id="paper-152336"></a>

## AR-Edit: Training-Free Streaming Video Editing without Inversion

[官方论文页](https://neurips.cc/virtual/2026/poster/152336) · [作者来源](https://openreview.net/forum?id=Tq0zQSyHNl)

- **问题 / 瓶颈** · 流式输入看不到未来帧
- **核心创新 / 方法** · 查询与键跨步稳定，单次提取的源值在自回归去噪中按需注入
- **Baseline** · 反演式编辑
- **Benchmark** · 流式视频重建与编辑
- **关键结果 / 消融** · 作者报告重建保真可比
- **适用条件 / 局限** · 限所测蒸馏架构

**可复用机制** · 比较一次缓存和逐段反演的画质及时延

<a id="paper-155853"></a>

## A Reduction from Delayed to Immediate Feedback for Online Convex Optimization with Improved Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/155853) · [作者来源](https://openreview.net/forum?id=2PgCkZnWDO)

- **问题 / 瓶颈** · 轮次延迟会叠加额外遗憾
- **核心创新 / 方法** · 连续时间分解学习误差与延迟漂移
- **Baseline** · 既有一阶及赌博机凸优化界
- **Benchmark** · 在线凸优化遗憾界
- **关键结果 / 消融** · 赌博机延迟项降至总延迟的平方根阶
- **适用条件 / 局限** · 依赖凸反馈设定

**可复用机制** · 分别追踪总延迟和学习项来选异步算法

<a id="paper-151585"></a>

## Are Easier or Harder Examples Better? Rethinking Data Selection for Reward Models and Preference Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151585) · [作者来源](https://openreview.net/forum?id=ZVpkdTlkIZ)

- **问题 / 瓶颈** · 难例与易例优劣结论冲突
- **核心创新 / 方法** · 用参考奖励模型的分差排序并注入不同噪声
- **Baseline** · 难例与全量训练
- **Benchmark** · 奖励模型、DPO、GRPO
- **关键结果 / 消融** · 前20%易例经常追平全量，弱代理下优势可逆转
- **适用条件 / 局限** · 需可靠参考奖励

**可复用机制** · 用奖励噪声扫描验证数据筛选是否稳健

<a id="paper-152665"></a>

## A Regularization-Based Approach to Public Belief State Search for Adversarial Games

[官方论文页](https://neurips.cc/virtual/2026/poster/152665) · [作者来源](https://openreview.net/forum?id=RIlBGF1FLf)

- **问题 / 瓶颈** · 既有方法对重解位置或策略输出有限制
- **核心创新 / 方法** · Gravel 在公开信念状态搜索中用正则保持博弈一致性
- **Baseline** · ReBeL 与既有 gadget 方法
- **Benchmark** · 无限注德州扑克对局与残局
- **关键结果 / 消融** · 作者报告优于 ReBeL
- **适用条件 / 局限** · 其他博弈及成本待核

**可复用机制** · 在需要显式输出策略的信念搜索中比较平滑正则与重解机制

<a id="paper-139215"></a>

## Are LLM Safety Judges Policy-Invariant? A Three-Principle Stress-Test

[官方论文页](https://neurips.cc/virtual/2026/poster/139215) · [作者来源](https://openreview.net/forum?id=eDvLM8DzS1)

- **问题 / 瓶颈** · 判决可能随无关措辞翻转
- **核心创新 / 方法** · 分别测等价改写、阈值变化与歧义校准
- **Baseline** · 重复评判抖动与有意阈值变化
- **Benchmark** · ASSEBench 与 R-Judge，四种裁判
- **关键结果 / 消融** · 等价改写超基线翻转最高9.1%
- **适用条件 / 局限** · 依赖等价认证和歧义标注

**可复用机制** · 安全评测需报告改写敏感度并区别于真实阈值变化

<a id="paper-139183"></a>

## Are Multimodal Benchmarks Really Useful? Item-Level Multimodal Benchmark Diagnosis via Structure-Response Co-Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/139183) · [作者来源](https://openreview.net/forum?id=fzADHlYut6)

- **问题 / 瓶颈** · 单看准确率无法发现单模态捷径
- **核心创新 / 方法** · 以结构先验锚定模态条件题目响应模型
- **Baseline** · 结构或响应单独诊断
- **Benchmark** · 基准精炼及人工题级标注
- **关键结果 / 消融** · 报告优于现有诊断方法
- **适用条件 / 局限** · 依赖所测模型及先验准确性

**可复用机制** · 用内容证据交叉验证模态消融来定位捷径题

<a id="paper-157024"></a>

## A Reproduction Study of Weight-Based Mechanistic Interpretability in Bilinear MLPs

[官方论文页](https://neurips.cc/virtual/2026/poster/157024) · [作者来源](https://openreview.net/forum?id=6k7qRdz7rD)

- **问题 / 瓶颈** · 辅助解释模型及训练设置可能影响原结论
- **核心创新 / 方法** · 复现双线性层的谱分析并对比正则和噪声
- **Baseline** · Pearce等原研究与正则消融
- **Benchmark** · 视觉和三种已发布语言模型
- **关键结果 / 消融** · 视觉结论复现，语言的低秩结论仅部分成立
- **适用条件 / 局限** · 缺失匹配SAE产物

**可复用机制** · 复现解释性结果时分开测结构归因和辅助解释器敏感性

<a id="paper-139784"></a>

## ARES: How Reliable Are LLM User Simulators for Recommender A/B Testing?

[官方论文页](https://neurips.cc/virtual/2026/poster/139784) · [作者来源](https://openreview.net/forum?id=4zC2OLTIPd)

- **问题 / 瓶颈** · 模拟骨干本身可能决定胜负
- **核心创新 / 方法** · 将推荐器与骨干效应分开，在文本和UI中交叉检查
- **Baseline** · 不同骨干及同组推荐器
- **Benchmark** · MovieLens-1M，九骨干五推荐器
- **关键结果 / 消融** · 仅换骨干约20%配对翻转
- **适用条件 / 局限** · 模拟一致性不能替代真人验证

**可复用机制** · 报告模拟器效应并复核跨骨干不一致的结论

<a id="paper-155532"></a>

## A Retained-Signal Interface for LLM Watermark Robustness under Paraphrase

[官方论文页](https://neurips.cc/virtual/2026/poster/155532) · [作者来源](https://openreview.net/forum?id=4sTuTf9CyC)

- **问题 / 瓶颈** · 单个AUC难跨重写与水印比较
- **核心创新 / 方法** · 基于保留KL信号给理论界，配合投影审计
- **Baseline** · KGW和Unigram配多种改写模型
- **Benchmark** · 保留信号与改写后AUC关系
- **关键结果 / 消融** · 作者报告可跨长度与强度预测AUC
- **适用条件 / 局限** · 投影结果依赖检测器

**可复用机制** · 用固定语义保真预算比较标记可靠性

<a id="paper-152689"></a>

## A Revisit of Hamiltonian Monte Carlo Efficiency on Bayesian Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/152689) · [作者来源](https://openreview.net/forum?id=RAcqfke8WC)

- **问题 / 瓶颈** · 光滑激活也可能导致采样低效
- **核心创新 / 方法** · 推导蛙跳局部误差以识别三阶曲率的影响
- **Baseline** · 分段线性与光滑无界激活
- **Benchmark** · 贝叶斯神经网络HMC采样
- **关键结果 / 消融** · 某些光滑激活效率退化可与分段线性相当
- **适用条件 / 局限** · 依赖所测后验和架构

**可复用机制** · 用步长敏感性扫描校验激活函数与采样器搭配

<a id="paper-148402"></a>

## Are we really tilting? The mechanics of reward guidance in flow and diffusion models

[官方论文页](https://neurips.cc/virtual/2026/poster/148402) · [作者来源](https://openreview.net/forum?id=y7pWRezznh)

- **问题 / 瓶颈** · 指导奖励上升可伴随保真下降
- **核心创新 / 方法** · 解析有限粒子估计误差，分别用衰减与多候选采样处理
- **Baseline** · 标准奖励引导
- **Benchmark** · 高斯混合、棋盘及FLUX.1
- **关键结果 / 消融** · 作者报告实验证实两种偏差及对应修正
- **适用条件 / 局限** · 理论依赖简化目标与奖励

**可复用机制** · 分别测模态比例和模态内质量以诊断引导失败

<a id="paper-154084"></a>

## Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154084) · [作者来源](https://openreview.net/forum?id=GL0HgZuYCW)

- **问题 / 瓶颈** · 长迭代可能停在错误解
- **核心创新 / 方法** · 跟踪层级推理迭代并用多来源扰动获得候选
- **Baseline** · 原始HRM
- **Benchmark** · Sudoku-Extreme与简单缺格任务
- **关键结果 / 消融** · 组合增强从55.0%提升至96.9%
- **适用条件 / 局限** · 联合收益不可代替独立消融

**可复用机制** · 绘制逐步正确率并检测增加计算是否仍停在同一解

<a id="paper-149153"></a>

## Argument Graph Uncertainty: Quantifying Uncertainty from the Logical Structure of Reasoning Chains

[官方论文页](https://neurips.cc/virtual/2026/poster/149153) · [作者来源](https://openreview.net/forum?id=sRkn7hto0l)

- **问题 / 瓶颈** · 重复采样昂贵，词元分数忽视论证结构
- **核心创新 / 方法** · 切分命题并用自然语言推断构图，把边分数汇入选项的 Dirichlet 后验
- **Baseline** · 词元与一致性估计
- **Benchmark** · GPQA、多种推理模型，具体校准指标待核
- **关键结果 / 消融** · 作者报告优于对照且与现有信号互补
- **适用条件 / 局限** · 限选择题和可读推理链

**可复用机制** · 固定主模型调用次数，对照结构分数和词元分数

<a id="paper-139443"></a>

## Argus: A Cross-Regime Benchmark for the Transferability of Uncertainty Quantification in Computer-Use Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139443) · [作者来源](https://openreview.net/forum?id=PcafO7KeeW)

- **问题 / 瓶颈** · 单模型上的分数排序可能无法迁移
- **核心创新 / 方法** · 交叉比较模型、数据集和可观测接口，并验证共形点击区域的覆盖
- **Baseline** · 开放权重 27 种及 API 8 种方案
- **Benchmark** · 四个开放模型和四套数据，另含三家 API，测秩相关、AUROC 和覆盖
- **关键结果 / 消融** · 同模型跨数据平均秩相关 0.705，跨接口约 0.08
- **适用条件 / 局限** · 限单步 GUI 定位，区域覆盖受校准分布影响

**可复用机制** · 先在部署接口验证分数及覆盖，再沿用原阈值

<a id="paper-156771"></a>

## ARROW: Augmented Replay for RObust World models

[官方论文页](https://neurips.cc/virtual/2026/poster/156771) · [作者来源](https://neurips.cc/virtual/2026/poster/156771)

- **问题 / 瓶颈** · 固定先进先出会丢失旧任务多样性
- **核心创新 / 方法** · 在 DreamerV3 中用短期缓存和分布匹配的长期缓存训练世界模型
- **Baseline** · 相同缓存大小的无模型及有模型方法
- **Benchmark** · Atari 与 Procgen CoinRun 变体，测遗忘和前向迁移
- **关键结果 / 消融** · 无共享结构任务遗忘较少，前向迁移相近
- **适用条件 / 局限** · 长缓冲抽样规则与跨任务收益待全文核实

**可复用机制** · 固定存储限制比较近期优先与旧任务覆盖策略

<a id="paper-151536"></a>

## ArtCrafter: Feed-Forward Generation of Articulated 3D Object with Analytic Joint Derivation

[官方论文页](https://neurips.cc/virtual/2026/poster/151536) · [作者来源](https://openreview.net/forum?id=ZwxUmdqiMF)

- **问题 / 瓶颈** · 直接回归关节可能与生成网格不一致
- **核心创新 / 方法** · 让共享基座关联开闭状态部件槽，随后由刚体变换求关节
- **Baseline** · 检索法及生成法
- **Benchmark** · URDF-Anything+，部件几何和四类关节指标
- **关键结果 / 消融** · 作者报告全部关节指标改善
- **适用条件 / 局限** · 需要开闭两态图像及刚性部件假设

**可复用机制** · 先预测具几何对应的中间物，再把可解析参数留给几何求解

<a id="paper-155895"></a>

## ART for Diffusion Sampling: A Reinforcement Learning Approach to Timestep Scheduling

[官方论文页](https://neurips.cc/virtual/2026/poster/155895) · [作者来源](https://openreview.net/forum?id=21auOU2ZNu)

- **问题 / 瓶颈** · 固定离散网格不能把预算分给误差大的阶段
- **核心创新 / 方法** · 重参数化时间以降低 Euler 离散误差，再以连续时间强化学习求调度
- **Baseline** · EDM 官方流程下的原调度
- **Benchmark** · CIFAR-10、AFHQv2、FFHQ、ImageNet，测 FID
- **关键结果 / 消融** · CIFAR-10 多种预算改善，蒸馏调度可无重训迁移
- **适用条件 / 局限** · 依赖目标求解器，其他离散误差下需复验

**可复用机制** · 固定步数比较学习网格和手工网格，单列训练成本

<a id="paper-154376"></a>

## Articulation in Prime: Primitive-Based Articulated Object Understanding from a Single Casual Video

[官方论文页](https://neurips.cc/virtual/2026/poster/154376) · [作者来源](https://openreview.net/forum?id=E1IZTqQCz0)

- **问题 / 瓶颈** · 遮挡与相机运动使点对应不稳
- **核心创新 / 方法** · 联合优化原语分组和旋转或平移关节，部分观测按可见性处理
- **Baseline** · 既有单目关节恢复方法
- **Benchmark** · AiP-synth 和 AiP-real，含剧烈相机运动与遮挡
- **关键结果 / 消融** · 作者报告优于对照，幅度待核
- **适用条件 / 局限** · 依赖原语近似和所覆盖关节类型

**可复用机制** · 当点轨迹不稳时比较结构化部件拟合与点匹配

<a id="paper-150972"></a>

## ARTIS: Agentic Risk-Aware Test-Time Scaling via Iterative Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/150972) · [作者来源](https://openreview.net/forum?id=dsPG32kLnQ)

- **问题 / 瓶颈** · 通用模拟器可能漏掉少见高影响失败
- **核心创新 / 方法** · 隔离模拟探索与实际提交，并对模拟器的失败覆盖做针对性改进
- **Baseline** · 普通语言模型模拟器
- **Benchmark** · 多轮多步代理基准，具体名称待核
- **关键结果 / 消融** · 作者报告可靠性改善依赖风险场景模拟质量
- **适用条件 / 局限** · 模拟通过无法保证真实环境安全

**可复用机制** · 先测模拟器在留出失败案例上的保真度，再用于执行前筛选

<a id="paper-151159"></a>

## ASAP: Attention Sink Anchored Pruning

[官方论文页](https://neurips.cc/virtual/2026/poster/151159) · [作者来源](https://openreview.net/forum?id=caL9VT4BtX)

- **问题 / 瓶颈** · 注意力汇点可让低信息词元表面分数偏高
- **核心创新 / 方法** · 将跨层注意力视作随机游走，按到汇点的扩散距离分组并合并背景
- **Baseline** · 现有词元压缩方法，具名对照待核
- **Benchmark** · 图像、视频和视觉语言任务的准确率及吞吐
- **关键结果 / 消融** · 作者报告吞吐最高增加 48%
- **适用条件 / 局限** · 依赖注意力可读，运行硬件和输入分辨率影响收益

**可复用机制** · 在相同算力下比较单层排序与跨层传播剪枝

<a id="paper-156772"></a>

## ASAT: Adaptive Scoring and Thresholding with Human Feedback for Robust Out-of-Distribution Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/156772) · [作者来源](https://openreview.net/forum?id=4Kd0VMsL76)

- **问题 / 瓶颈** · 只按已知分布定阈值无法控制异常误收
- **核心创新 / 方法** · 引入人工反馈调整评分与门限，在约定条件下控制错误率
- **Baseline** · 固定分数或固定阈值方法，名称待核
- **Benchmark** · OpenOOD，比较两类错误率
- **关键结果 / 消融** · 作者报告平稳条件下有控制保证，漂移时会短暂违约
- **适用条件 / 局限** · 依赖反馈和分布假设

**可复用机制** · 将上线误收约束与适应速度同时纳入检测器选择

<a id="paper-155425"></a>

## A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155425) · [作者来源](https://openreview.net/forum?id=5l3JqAoTnr)

- **问题 / 瓶颈** · 直接计算 Hessian 最大特征值成本高
- **核心创新 / 方法** · 以少于十次前向测临界尖锐度，并定义跨目标的相对版本
- **Baseline** · Hessian 尖锐度作为参照
- **Benchmark** · 最高 7B 的 OLMo-2 预训练和中训
- **关键结果 / 消融** · 观察到逐步变尖及稳定边缘现象
- **适用条件 / 局限** · 方向代理不能刻画完整 Hessian 结构

**可复用机制** · 比较数据配比时监控更新方向对当前和目标数据损失曲率的影响

<a id="paper-139330"></a>

## A Scientific Claim Stability Framework for Evaluating MRI Morphometry Pipelines

[官方论文页](https://neurips.cc/virtual/2026/poster/139330) · [作者来源](https://openreview.net/forum?id=WgIesR9ByR)

- **问题 / 瓶颈** · 测量相关性高也可能换掉支持结论的区域
- **核心创新 / 方法** · 构建结论卡并跨数据、流程、图谱等变动重测支持证据
- **Baseline** · 特征一致性评估，以及专家和模型复核
- **Benchmark** · 三套数据五个队列、10370 扫描和 2783 张结论卡
- **关键结果 / 消融** · 观察到证据向量相近但关键支持区域变化
- **适用条件 / 局限** · 依赖事先选定的结论和扰动范围

**可复用机制** · 在分析流水线变更时将关键科学命题及支持区域一同审计

<a id="paper-149036"></a>

## A Semantic-Sampling Framework for Evaluating Calibration in Open-Ended Question Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/149036) · [作者来源](https://openreview.net/forum?id=tL3fAjECyx)

- **问题 / 瓶颈** · 开放回答缺乏封闭标签及可用 logits
- **核心创新 / 方法** · 按语义聚类回答，以类频率作置信度并比较同样本与留出估计
- **Baseline** · 口述置信、已有抽样和 logit 评估
- **Benchmark** · 三个开放问答基准、五种商用模型
- **关键结果 / 消融** · 两估计渐近无偏，困难问题上留出版本误差更小
- **适用条件 / 局限** · 依赖语义等价判定和抽样预算

**可复用机制** · 用独立样本复核选中答案的语义频率。

<a id="paper-149847"></a>

## A Separation Principle for Cooperative Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149847) · [作者来源](https://openreview.net/forum?id=mrNoBqs1mU)

- **问题 / 瓶颈** · 联合学习路线和分配不随群体规模扩展
- **核心创新 / 方法** · 独立训练目标条件策略，以最优运输协调群体
- **Baseline** · MARL、最短路
- **Benchmark** · 随机网格及曼哈顿配送
- **关键结果 / 消融** · 网格平均时间降逾40%，曼哈顿最多20%
- **适用条件 / 局限** · 需单体动力学解耦，群体目标耦合

**可复用机制** · 将可解耦的局部控制与全局匹配分开实现。

<a id="paper-152698"></a>

## ASH: Agents that Self-Hone via Embodied Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152698) · [作者来源](https://openreview.net/forum?id=R43XRkyGkH)

- **问题 / 瓶颈** · 长程环境缺标注动作且人工奖励难规模化
- **核心创新 / 方法** · 卡住后从自身轨迹学习逆动力学，再用相关视频提取动作和关键记忆
- **Baseline** · 行为克隆、检索增强、零样本
- **Benchmark** · 两款游戏的八小时里程碑
- **关键结果 / 消融** · 平均11.2及9.9/12，对照6.5及6.0
- **适用条件 / 局限** · 局限于已测游戏；跨域动作映射待核

**可复用机制** · 评估视频学习时对照只检索关键帧与进一步估计动作。

<a id="paper-150514"></a>

## A Single Deep Preference-Conditioned Policy for Learning Pareto Coverage Sets

[官方论文页](https://neurips.cc/virtual/2026/poster/150514) · [作者来源](https://openreview.net/forum?id=hX6SBd1fFp)

- **问题 / 瓶颈** · 非线性标量化下偏好与最优解对应不清
- **核心创新 / 方法** · 平滑 Tchebycheff 与占用测度镜像下降，每步以旧策略作 KL 参考
- **Baseline** · 近期多目标 RL 方法
- **Benchmark** · 八个 MO-Gymnasium 任务；超体积与期望效用
- **关键结果 / 消融** · 理论目标差 O(1/k)，实验平均排名最佳
- **适用条件 / 局限** · 唯一性和 Lipschitz 证明限表格及内部偏好条件

**可复用机制** · 检查偏好插值下回报连续性，并与独立训练对照。

<a id="paper-139309"></a>

## Ask-E: An Environment for Calibrated Question Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/139309) · [作者来源](https://openreview.net/forum?id=YBhF7eTE3o)

- **问题 / 瓶颈** · 准确生成模型能力边缘的题目难度高
- **核心创新 / 方法** · 以两个模型中恰有一个可解作为目标区间
- **Baseline** · 前沿模型在相同校准任务上的表现
- **Benchmark** · Ask-E 与下游数学基准
- **关键结果 / 消融** · 前沿模型校准低于50%，训练后下游改善
- **适用条件 / 局限** · 依赖参考能力排序与求解噪声

**可复用机制** · 生成评测题时先固定两档参考求解器再测跨档区分度。

<a id="paper-154769"></a>

## Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents?

[官方论文页](https://neurips.cc/virtual/2026/poster/154769) · [作者来源](https://openreview.net/forum?id=B5ZuTZqnmv)

- **问题 / 瓶颈** · 过早猜测与过晚纠错均可能损害长程任务
- **核心创新 / 方法** · 在不同轨迹阶段注入金标准澄清，按目标、输入、约束和上下文分组
- **Baseline** · 不询问和其他注入时点
- **Benchmark** · 三个基准、84变体、逾6000次；pass@3
- **关键结果 / 消融** · 目标澄清约过10%便失去价值，输入约保留到50%
- **适用条件 / 局限** · 强制注入不等于学会自主提问

**可复用机制** · 为每类信息绘制收益随进度变化曲线。

<a id="paper-149684"></a>

## Asking the Right Questions: Improving Reasoning with Generated Stepping Stones

[官方论文页](https://neurips.cc/virtual/2026/poster/149684) · [作者来源](https://openreview.net/forum?id=oCEzkjKEVt)

- **问题 / 瓶颈** · 直接求解难以利用简化或子问题
- **核心创新 / 方法** · 加入独立问题生成器，并用合成数据做 SFT 与 RL
- **Baseline** · 默认推理流程
- **Benchmark** · 推理任务和不同能力求解器；具名待核
- **关键结果 / 消融** · 作者报告好问题可迁移，后训练可提高有用性
- **适用条件 / 局限** · 生成耗时及错误中间问题影响待核

**可复用机制** · 对比额外推理预算和额外子问题预算。

<a id="paper-152831"></a>

## A Spectral Framework for Closed-Form Relative Density Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/152831) · [作者来源](https://openreview.net/forum?id=Q5UGhwLahz)

- **问题 / 瓶颈** · 变分方法往往需要迭代优化
- **核心创新 / 方法** · 将 KL 表为加权卡方积分，再用最小二乘的谱解
- **Baseline** · 变分估计、逻辑及 softmax 回归
- **Benchmark** · 合成数据与归一化条件模型
- **关键结果 / 消融** · 作者给出收敛保证，精度数值待核
- **适用条件 / 局限** · 固定特征与线性参数化是主要设定

**可复用机制** · 将固定特征的闭式估计与等预算迭代求解对照

<a id="paper-148544"></a>

## Assessing Sample Quality in Conditional Generation under Compositional Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/148544) · [作者来源](https://openreview.net/forum?id=x6NGTz0aAP)

- **问题 / 瓶颈** · 标准条件指标需要不可获得的目标分布
- **核心创新 / 方法** · 用训练分布评估全局真实性及各属性相对替代条件的匹配
- **Baseline** · 未筛选生成与已有预训练模型
- **Benchmark** · 视觉控制任务与成像数据，下游表现
- **关键结果 / 消融** · 作者报告筛选改善结构和下游预测
- **适用条件 / 局限** · 依赖已观察属性的覆盖

**可复用机制** · 将真实性和条件忠实度分开用于筛选与拒答

<a id="paper-153026"></a>

## ASSET: Acquisition-Sensitive Subspace Estimation for Test-Time Adaptation of Medical VLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153026) · [作者来源](https://openreview.net/forum?id=OZI1vf23wm)

- **问题 / 瓶颈** · 通用微调容易过拟合小目标集
- **核心创新 / 方法** · 根据采集型增强前后的预测和梯度差估计子空间并迭代更新
- **Baseline** · 一般测试时适配，具名基线待核
- **Benchmark** · 多数据集与骨干，测采集偏移准确率
- **关键结果 / 消融** · 作者报告平均改善 2.62%，最强偏移改善 4.12%
- **适用条件 / 局限** · 增强须近似真实偏移

**可复用机制** · 同预算比较全集更新与退化敏感方向更新

<a id="paper-153282"></a>

## Assign and Add: A Mechanistic Study of Compositional Arithmetic

[官方论文页](https://neurips.cc/virtual/2026/poster/153282) · [作者来源](https://openreview.net/forum?id=MPwsN5TWrW)

- **问题 / 瓶颈** · 正确外推不揭示内部组合方式
- **核心创新 / 方法** · 用变量赋值和模加的分离训练集跟踪模块和阶段
- **Baseline** · 直接输入数与变量间接输入
- **Benchmark** · 小 Transformer 的组合算术
- **关键结果 / 消融** · 同一模加 MLP 两路复用，训练呈三个阶段
- **适用条件 / 局限** · 任务受控，不能直接推广到开放语言

**可复用机制** · 以等价输入和留出组合复核模块复用

<a id="paper-151341"></a>

## A Stability Analysis of AdamW: Unstable Equilibria and Non-Convergence

[官方论文页](https://neurips.cc/virtual/2026/poster/151341) · [作者来源](https://openreview.net/forum?id=bGprJAGt6w)

- **问题 / 瓶颈** · AdamW 即使在简单目标上也可能振荡
- **核心创新 / 方法** · 将固定点表述为约束正则问题驻点并分析局部稳定性
- **Baseline** · 原 AdamW 与保持固定点的修改
- **Benchmark** · 一维数值与高维连续时间分析
- **关键结果 / 消融** · 作者观察不稳定平衡和持续振荡
- **适用条件 / 局限** · 连续时间充分条件不自动推广到离散大步长

**可复用机制** · 选择动量和衰减时同时测驻点附近轨迹稳定性

<a id="paper-153011"></a>

## A Statistical Theory of Gated Attention through the Lens of Hierarchical Mixture of Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/153011) · [作者来源](https://openreview.net/forum?id=Oe70EbkiGc)

- **问题 / 瓶颈** · 门控样本效率的机制不明确
- **核心创新 / 方法** · 将注意力元素写为层级专家混合并分析专家估计
- **Baseline** · 标准多头注意力与不同门控位置
- **Benchmark** · 专家估计理论比较
- **关键结果 / 消融** · 作者在设定下导出多项式对指数样本需求
- **适用条件 / 局限** · 理论不能直接等同真实预训练成本

**可复用机制** · 固定训练预算做门控插入位置消融

<a id="paper-154519"></a>

## ASTOR: Multi-Task Code Reinforcement Learning via Utility-Driven Coordination

[官方论文页](https://neurips.cc/virtual/2026/poster/154519) · [作者来源](https://openreview.net/forum?id=CzqAXCaI97)

- **问题 / 瓶颈** · 统一课程及更新强度忽略任务协同和进度
- **核心创新 / 方法** · 任务效用驱动分配预算、采样提示并动态调 KL
- **Baseline** · 专用策略和多任务 RL
- **Benchmark** · 两种 LLM、四项代码任务
- **关键结果 / 消融** · 报告较最强多任务对照提高 7.5%–12.8%
- **适用条件 / 局限** · 任务效用估计及单模块收益待核

**可复用机制** · 固定总预算分开消融采样和约束调度

<a id="paper-155836"></a>

## A Surrogate Perspective on Convergence of Fixed-Target DQN

[官方论文页](https://neurips.cc/virtual/2026/poster/155836) · [作者来源](https://openreview.net/forum?id=2W16djzTLs)

- **问题 / 瓶颈** · 平均回归损失与最大范数收缩不一致
- **核心创新 / 方法** · 推导内循环精度阈值并设计软最大范数代理
- **Baseline** · MSE与Huber固定目标DQN
- **Benchmark** · 理论收敛与Atari最坏残差
- **关键结果 / 消融** · 软最大范数要求的内层精度较宽松且残差降低
- **适用条件 / 局限** · 收敛只到逼近误差下限

**可复用机制** · 按控制目标的范数选择回归损失

<a id="paper-149752"></a>

## ASVQ: What Reparameterization Is Just Enough for Efficient Codebook Learning?

[官方论文页](https://neurips.cc/virtual/2026/poster/149752) · [作者来源](https://openreview.net/forum?id=nd6Lcw7MOf)

- **问题 / 瓶颈** · 复杂变换增加开销，码本仍可能塌缩
- **核心创新 / 方法** · 解耦学习的自适应尺度重参数化
- **Baseline** · 更复杂的码本重参数化
- **Benchmark** · 图像和音频分词，测重建、利用率和稳定性
- **关键结果 / 消融** · 三方面改善，数字待核
- **适用条件 / 局限** · 不同码本容量下收益待核

**可复用机制** · 以相同码本预算比较尺度与高容量变换

<a id="paper-151792"></a>

## AsymHP: Load-Balanced Sparse Attention for Video Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151792) · [作者来源](https://openreview.net/forum?id=XyeAckrYOC)

- **问题 / 瓶颈** · 均分头数导致稀疏负载不均
- **核心创新 / 方法** · 用密度与掩码成本模型做不等大小重分片
- **Baseline** · 对称头并行
- **Benchmark** · H100视频扩散稀疏注意力延迟
- **关键结果 / 消融** · 最高1.54倍加速
- **适用条件 / 局限** · 依赖跨步密度可预测性

**可复用机制** · 按预测算量分片并测通信与等待

<a id="paper-156075"></a>

## Asymmetric Flow Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156075) · [作者来源](https://openreview.net/forum?id=0ddDpfXvoV)

- **问题 / 瓶颈** · 像素流预测负担高维噪声
- **核心创新 / 方法** · 非对称参数化并解析恢复全维速度，支持潜模型升维
- **Baseline** · DiT/JiT及FLUX.2 klein 9B潜底座
- **Benchmark** · ImageNet 256 FID、HPSv3、DPG-Bench、GenEval
- **关键结果 / 消融** · ImageNet FID 1.57，像素微调改善所报指标
- **适用条件 / 局限** · 依赖可用低秩噪声空间

**可复用机制** · 分别选择数据和噪声的预测秩

<a id="paper-149774"></a>

## Asymmetric Scaling Laws from Sparse Features

[官方论文页](https://neurips.cc/virtual/2026/poster/149774) · [作者来源](https://openreview.net/forum?id=nPOMra0Pqu)

- **问题 / 瓶颈** · 参数放大无法覆盖未见坐标
- **核心创新 / 方法** · 分析稀疏模型的分段缩放与插值阈值
- **Baseline** · 稠密模型和欠参过参分析
- **Benchmark** · 理论及数值验证，测总体损失和训练稳定性
- **关键结果 / 消融** · 两侧缩放指数不同，计算最优偏向数据
- **适用条件 / 局限** · 取决于稀疏模型假设

**可复用机制** · 按稀有特征的覆盖率分层比较数据和参数投入

<a id="paper-148530"></a>

## Asymptotically Exact Negative Guidance of Diffusion Models via Positive-Unlabeled Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148530) · [作者来源](https://openreview.net/forum?id=xCdsktvB3f)

- **问题 / 瓶颈** · 局部排斥难通过增加计算消除偏差
- **核心创新 / 方法** · 通过正例未标记估计负条件概率，再用序贯蒙特卡洛校正
- **Baseline** · 局部排斥类扩散引导
- **Benchmark** · 参考样本与分数指定的负条件，评测待核
- **关键结果 / 消融** · 提出渐近精确采样，有限预算收益待核
- **适用条件 / 局限** · 需可靠的概率估计及粒子预算

**可复用机制** · 明确写出所需密度再验证引导样本

<a id="paper-153874"></a>

## Asymptotically Log-Optimal Bayes-Assisted Confidence Sequences for Bounded Means

[官方论文页](https://neurips.cc/virtual/2026/poster/153874) · [作者来源](https://openreview.net/forum?id=I6z9IukSBB)

- **问题 / 瓶颈** · 通用更新无法利用先验
- **核心创新 / 方法** · 贝叶斯预测在有效因子中选择预期对数增长最大的更新
- **Baseline** · 通用置信序列与真分布oracle
- **Benchmark** · 有界IID均值、合成实验及LLM最优臂识别
- **关键结果 / 消融** · 预测一致时达到oracle渐近对数增长
- **适用条件 / 局限** · 适用有界IID目标，模型错误影响效率

**可复用机制** · 分开验证因子合法性和预测辅助后的区间宽度

<a id="paper-155437"></a>

## AsyncMesh: Fully Asynchronous Optimization for Data and Pipeline Parallelism

[官方论文页](https://neurips.cc/virtual/2026/poster/155437) · [作者来源](https://openreview.net/forum?id=5e4wynkfYC)

- **问题 / 瓶颈** · 同步传输限制跨集群训练
- **核心创新 / 方法** · 流水线用权重前瞻，数据并行用稀疏平均与指数移动校正
- **Baseline** · 全同步训练
- **Benchmark** · 大语言模型训练，比较效果与通信开销
- **关键结果 / 消融** · 作者报告效果相当、通信下降，并给出收敛保证
- **适用条件 / 局限** · 具体拓扑和陈旧边界待核

**可复用机制** · 分别测两类并行轴的通信与陈旧，再选择补偿方式

<a id="paper-156136"></a>

## AsyncOPD: How Stale Can On-Policy Distillation Be?

[官方论文页](https://neurips.cc/virtual/2026/poster/156136) · [作者来源](https://openreview.net/forum?id=09mcfBxsZ4)

- **问题 / 瓶颈** · 采样陈旧度可能改变蒸馏更新
- **核心创新 / 方法** · 学习时重算反向 KL，并用多样本蒙特卡洛降低缓存约束下的方差
- **Baseline** · 同步蒸馏、异步强化学习稳定方法
- **Benchmark** · 推理模型蒸馏的吞吐及准确度
- **关键结果 / 消融** · 吞吐为同步的 1.6–3.8 倍且准确度相当，前向 KL 更耐陈旧
- **适用条件 / 局限** · 教师仅对缓存动作有分数

**可复用机制** · 分别扫描两种 KL 的陈旧度并测缓存采样方差

<a id="paper-138908"></a>

## A Systematic Analysis of Out-of-Distribution Detection Under Representation and Training Paradigm Shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/138908) · [作者来源](https://openreview.net/forum?id=xZm0LvUahe)

- **问题 / 瓶颈** · 检测分数排名随骨干改变
- **核心创新 / 方法** · 控制多重比较，并用神经坍缩测量预测候选分数家族
- **Baseline** · NNGuide、fDBD、CTM 等
- **Benchmark** · 四个图像分类源集，近中远偏移，AURC 和 AUGRC
- **关键结果 / 消融** · CNN 近偏移偏向间隔分数，微调 ViT 更偏重建与残差
- **适用条件 / 局限** · 语义距离分组依赖 CLIP

**可复用机制** · 迁移检测器前记录坍缩指标并按偏移强度分组比较

<a id="paper-149483"></a>

## A Theoretical Analysis of Test-Driven Code Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149483) · [作者来源](https://openreview.net/forum?id=pnb7TQTzC2)

- **问题 / 瓶颈** · 严格等价只给粗粒度执行信号
- **核心创新 / 方法** · 把候选选择形式化为估计问题，把反馈生成与汤普森采样联系
- **Baseline** · 严格功能等价与模糊相似度
- **Benchmark** · BigCodeBenchHard、LeetCodeDataset、QiskitHumanEvalSim
- **关键结果 / 消融** · 软相似度在理论条件下信噪比更高，任务歧义带来不可约遗憾
- **适用条件 / 局限** · 依赖执行反馈与理论假设

**可复用机制** · 反馈无效时先明确规格并区分不可观察目标

<a id="paper-149727"></a>

## A Theoretical Analysis of Why Masked Diffusion Models Mitigate the Reversal Curse

[官方论文页](https://neurips.cc/virtual/2026/poster/149727) · [作者来源](https://openreview.net/forum?id=noEiGT8prX)

- **问题 / 瓶颈** · 掩码顺序本身无法解释反向查询迁移
- **核心创新 / 方法** · 分析共享 Transformer 参数与相对位置注意力的耦合
- **Baseline** · 自回归与掩码扩散；不同方向查询
- **Benchmark** · 单层实验及 LLaDA、Dream
- **关键结果 / 消融** · 报告共享存储梯度对齐且反向预测改善
- **适用条件 / 局限** · 严格证明限单层设定

**可复用机制** · 诊断关系反转时同时测证据共享和位置路由

<a id="paper-155828"></a>

## A Theory of Spatial Continuous Attractors in Hopfield Energy Landscapes

[官方论文页](https://neurips.cc/virtual/2026/poster/155828) · [作者来源](https://openreview.net/forum?id=2aMmeCVNCj)

- **问题 / 瓶颈** · 空间状态既需抗扰又需随输入移动
- **核心创新 / 方法** · 以傅里叶能量构造兼容 Hopfield 的环与环面
- **Baseline** · 不同扰动及速度条件；具名基线待核
- **Benchmark** · 头向与网格细胞模型
- **关键结果 / 消融** · 报告扰动后恢复及多种速度下稳定移动
- **适用条件 / 局限** · 生物对应范围待验证

**可复用机制** · 连续状态记忆同时测试回流形和沿流形跟踪

<a id="paper-152773"></a>

## A Theory on Flow Matching with Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/152773) · [作者来源](https://openreview.net/forum?id=QTCtJIao9O)

- **问题 / 瓶颈** · 速度拟合效果与最终分布误差之间需明确关联
- **核心创新 / 方法** · 在过参数两层 ReLU 分析优化和泛化，再导出 Wasserstein 界
- **Baseline** · 不同误差度量；具名对照待核
- **Benchmark** · 合成与真实图像实验
- **关键结果 / 消融** · 作者给出梯度下降、泛化及生成距离保证
- **适用条件 / 局限** · 网络与优化假设限制外推

**可复用机制** · 流模型验证同时给速度目标误差及下游分布距离

<a id="paper-152880"></a>

## ATI-VLA: Action-Centric Predictive Vision–Language–Action Models via Actionable Alignment Then Adaptive Injection

[官方论文页](https://neurips.cc/virtual/2026/poster/152880) · [作者来源](https://openreview.net/forum?id=PgXh7Sncl1)

- **问题 / 瓶颈** · 联合预测可能与动作优化冲突
- **核心创新 / 方法** · 用共享离散码本表示两者，预测潜变量经轻量侧路进入解码
- **Baseline** · 直接动作和既有预测式 VLA
- **Benchmark** · 仿真和真机操作，比较表现与收敛
- **关键结果 / 消融** · 作者报告改善表现和收敛，幅度待核
- **适用条件 / 局限** · 依赖码本保留可行动信息

**可复用机制** · 比较共享码本与直接注入，检查同预算下的动作收益
