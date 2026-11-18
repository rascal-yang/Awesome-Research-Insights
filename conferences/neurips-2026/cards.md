# NeurIPS 2026 论文卡

[会议索引](README.md)

<a id="paper-33u8sf3mic"></a>

## δ-Mem — Efficient Online Memory for Large Language Models

[官方论文页与作者摘要](https://neurips.cc/virtual/2026/poster/155770) · [OpenReview](https://openreview.net/forum?id=33u8SF3mIc)

- **问题 / 瓶颈** · 长期助手需要复用历史信息，延长上下文会增加计算，也无法保证模型有效利用历史。
- **核心创新 / 方法** · 给冻结的全注意力骨干加固定尺寸的关联记忆矩阵，以 delta rule 在线写入；生成时用读出的状态给注意力计算加低秩修正。
- **Baseline** · 以冻结全注意力模型为底座；对比原冻结模型和最强非 δ-Mem 记忆基线，具体名称待全文核实。
- **Benchmark** · MemoryAgentBench、LoCoMo 及通用能力对照；子任务、指标定义和比较预算待全文核实。
- **关键结果 / 消融** · 作者摘要报告使用 8×8 状态时，平均分分别达到冻结骨干和最强记忆基线的 1.10 倍与 1.15 倍；MemoryAgentBench 和 LoCoMo 分别报告 1.31 倍与 1.20 倍，分项参照及消融待核实。
- **适用条件 / 局限** · 需要访问注意力计算；固定矩阵在冲突写入、长间隔读取或新骨干上的容量边界待核实。

**可复用机制** · 对有长历史的 Agent，在固定骨干下比较延长上下文与在线写入小型状态，把历史检索表现、通用能力和推理成本分开记录。

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

<a id="paper-152861"></a>

## Disentangling Channel Semantics in Vision Transformers via Token Decorrelation and Composition-Aware Modulation

[官方论文页](https://neurips.cc/virtual/2026/poster/152861) · [作者来源](https://openreview.net/forum?id=PqIEMrqSdB)

- **问题 / 瓶颈** · 通道高度冗余时，多通道 ViT 的上下文 token 容易集中到少数通道。
- **核心创新 / 方法** · 对上下文 token 去相关，让 CLS 保留共享语义、记忆 token 捕获互补通道信息，再以 CLS 生成样本级调制。
- **Baseline** · 与已有多通道 ViT 比较；具体名称待核实。
- **Benchmark** · JUMP-CP、CHAMMI、So2Sat；摘要未列指标定义。
- **关键结果 / 消融** · 三个基准均改善，提升幅度随数据集的通道冗余而变化，摘要给出的相关系数范围为 0.19–0.77。
- **适用条件 / 局限** · 跨数据集关联不等同于因果，去相关强度及缺失通道的影响待核实。

**可复用机制** · 按通道冗余分层测共享摘要和记忆 token 的重叠，联合对照静态通道嵌入与动态调制。

<a id="paper-152441"></a>

## Fewer Tokens, Fewer Layers: Efficient Vision Token Pruning and On-Policy Distillation to Accelerate VLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152441) · [作者来源](https://openreview.net/forum?id=T7WbWqjpqm)

- **问题 / 瓶颈** · 只裁视觉 token 主要减少预填充，且依赖显式注意力图的裁剪难兼容高效注意力。
- **核心创新 / 方法** · 用 FlashPruner 无注意力图选 token，把裁剪器与语言模型前几层组为草稿模型，以 on-policy 蒸馏做自投机解码。
- **Baseline** · 比较原模型和视觉裁剪路线；具名基线待核实。
- **Benchmark** · MVBench，测首 token 延迟、解码速度和相对准确率。
- **关键结果 / 消融** · 仅保留 10% 视觉 token 时，摘要报告首 token 提速 1.5 倍、解码提速 2 倍并保留 96.8% 相对准确率。
- **适用条件 / 局限** · 收益取决于输出长度、投机接受率和推理硬件；摘要未给分项边界。

**可复用机制** · 为长输出任务分别记录预填充和解码成本，用部署策略自产样本训练轻量草稿。

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

<a id="paper-151006"></a>

## Theory Guided and Interpretable Neural Operator Design for Partial Differential Equation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151006) · [作者来源](https://neurips.cc/virtual/2026/poster/151006)

- **问题 / 瓶颈** · 尖锐梯度与非欧几里得定义域会给一般神经算子带来逼近困难。
- **核心创新 / 方法** · AFDONet 将自适应傅里叶分解与神经算子嵌入定制变分自编码器，面向光滑流形上的非线性 PDE。
- **Baseline** · 既有神经 PDE 求解器，具体基线待核。
- **Benchmark** · 黎曼流形和尖锐梯度的 PDE 基准，比较解精度和计算效率；具名任务和指标待核。
- **关键结果 / 消融** · 摘要报告在上述两类设置表现更佳，具体幅度及消融待核。
- **适用条件 / 局限** · 适用于论文所定义的光滑流形与 PDE 类；定理前提待核。

**可复用机制** · 评估算子离散化时，分开标记几何复杂性和解的梯度尖锐程度，与通用算子做对照。

<a id="paper-153693"></a>

## Tyche: One Step Flow for Efficient Probabilistic Weather Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/153693) · [作者来源](https://neurips.cc/virtual/2026/poster/153693)

- **问题 / 瓶颈** · 逐步去噪推理随预报长度、集合大小和去噪步数增长。
- **核心创新 / 方法** · 以目的时刻条件化的平均速度进行单步条件流采样；用 JVP 正则维持时序自洽，并以滚动课程 CRPS 微调。
- **Baseline** · 多步生成模型及 ECMWF IFS 运行集合。
- **Benchmark** · ERA5，1.5 度、6 小时分辨率；预测表现与集合校准，含 CRPS 监督。
- **关键结果 / 消融** · 摘要报告单次函数评估与多步基线及 IFS 表现相当或更优；变量级结果待核。
- **适用条件 / 局限** · 相同结论能否用于更高分辨率及极端尾部事件待核。

**可复用机制** · 减少生成函数评估次数时，在相同集合规模下同时比较质量、计算量和长滚动校准。

<a id="paper-149951"></a>

## Deferred Aggregation in Hierarchical Bayesian Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149951) · [作者来源](https://neurips.cc/virtual/2026/poster/149951)

- **问题 / 瓶颈** · 先平均高斯过程或采集函数容易让少数错设模型拖累整体。
- **核心创新 / 方法** · 让每个超参数模型独立提议查询点，再选与其他建议总体距离最小的候选。
- **Baseline** · 平均模型或采集函数的早期聚合及标准贝叶斯优化。
- **Benchmark** · 错设高斯过程的遗憾上界、玩具示例和合成及真实优化任务。
- **关键结果 / 消融** · 在所设错设模型中，早聚合的误差项依赖全部模型平均，迟聚合取决于低错设多数；作者报告多数实验优于基线。
- **适用条件 / 局限** · 理论前提是低错设模型占多数，候选距离的定义也会影响聚合。

**可复用机制** · 当模型集成用于选下一步实验，可对照聚合预测和聚合决策，并扫描异常模型比例。

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
