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

<a id="paper-154295"></a>

## $\alpha$Depth: Learning Single-Pass Soft Boundary Decomposition for Stereo Conversion

[官方论文页](https://neurips.cc/virtual/2026/poster/154295) · [作者来源](https://neurips.cc/virtual/2026/poster/154295)

- **问题 / 瓶颈** · 单层深度混淆前后景
- **核心创新 / 方法** · 用局部环形透明度表示联合估计分层颜色和深度
- **Baseline** · 单层深度和抠图
- **Benchmark** · 立体转换，基准名称待核
- **关键结果 / 消融** · 作者报告减少漏色与结构畸变
- **适用条件 / 局限** · 效果取决于边界分解质量

**可复用机制** · 对含头发和散焦的样本单独比较单深度与分层深度。

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

<a id="paper-139361"></a>

## $\chi$-Bench: Can AI Agents Automate End-to-End, Long-Horizon, Policy-Rich Healthcare Workflows?

[官方论文页](https://neurips.cc/virtual/2026/poster/139361) · [作者来源](https://neurips.cc/virtual/2026/poster/139361)

- **问题 / 瓶颈** · 单轮评测不覆盖规则遵循、角色交接及多方交互
- **核心创新 / 方法** · 用模拟医疗应用检验从病例到终态和工件的完整执行
- **Baseline** · 30 种模型与执行环境组合
- **Benchmark** · 三个管理式医疗流程，20 个应用和 87 个工具，报告通过率与严格 pass³
- **关键结果 / 消融** · 最佳解决率 28%，严格 pass³ 均低于 20%，单会话表现为 3.8%
- **适用条件 / 局限** · 仿真结果，跨行业退化待验证

**可复用机制** · 为长流程 Agent 加入多角色责任交接，并对照任务隔离与共享会话。

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

<a id="paper-150269"></a>

## $\gamma$-weakly $\theta$-up-concavity: A Unified Framework for Non-Convex Optimization Beyond DR-Submodular and OSS Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/150269) · [作者来源](https://neurips.cc/virtual/2026/poster/150269)

- **问题 / 瓶颈** · 已有 DR 次模假设难覆盖初始平坦或尺度相关曲率
- **核心创新 / 方法** · 以非均匀上层线性化构造曲率和可行域相关的近似系数
- **Baseline** · DR 次模与单侧光滑方法
- **Benchmark** · 离线近似比、在线静态和动态遗憾、拟阵约束
- **关键结果 / 消融** · 恢复 DR 次模最优近似系数并改进部分单侧光滑保证
- **适用条件 / 局限** · 须核实一阶曲率假设及可行域结构

**可复用机制** · 离线有线性化保证后，可用线性优化归约推导在线界。

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

<a id="paper-155224"></a>

## $\mathbf{D^{3}S^{2}}$: Diffusion-Guided Dataset Distillation for Semantic Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/155224) · [作者来源](https://neurips.cc/virtual/2026/poster/155224)

- **问题 / 瓶颈** · 长尾与像素对齐限制分割数据蒸馏
- **核心创新 / 方法** · 优先保留稀有类别掩码，以布局条件扩散合成，联合分割一致性和类别级特征匹配引导
- **Baseline** · 随机筛选及其他蒸馏方法
- **Benchmark** · ADE20K、COCO-Stuff，Mask2Former Swin-S，mIoU
- **关键结果 / 消融** · 1% 数据预算下分别取得 24.99% 和 35.49% mIoU
- **适用条件 / 局限** · 依赖可用的布局生成器和分割特征，骨干迁移待核

**可复用机制** · 在固定压缩率下分别消融类平衡、像素一致性和特征匹配。

<a id="paper-139531"></a>

## $\mathbf{\mathtt{MAD\text{-}Bench}}$: How Do Multimodal Agents Deceive You?

[官方论文页](https://neurips.cc/virtual/2026/poster/139531) · [作者来源](https://neurips.cc/virtual/2026/poster/139531)

- **问题 / 瓶颈** · 执行失败后模型可能声称任务成功
- **核心创新 / 方法** · 在沙箱内分离任务可执行性与报告真实性，用轨迹证据检验对外声明
- **Baseline** · 10 种多模态 Agent
- **Benchmark** · 360 道沙箱题，覆盖模态、目标与工具失配
- **关键结果 / 消融** · 作者观察到多种失实报告，量化比例待核
- **适用条件 / 局限** · 不能由轨迹直接推断心理意图

**可复用机制** · 对无法执行的任务按终态及可查证据判定声明，独立测操作成功率和报告正确率。

<a id="paper-153540"></a>

## $\mathcal{P}$Torch: Narrowing the Gap Between Projection and Gradient-Based Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153540) · [作者来源](https://neurips.cc/virtual/2026/poster/153540)

- **问题 / 瓶颈** · 投影方法开销大且深层目标信号可能衰减
- **核心创新 / 方法** · 复用 PyTorch autograd 基础设施并以非线性松弛与省内存投影优化执行，证明目标衰减定理
- **Baseline** · 梯度训练和既有投影方法
- **Benchmark** · MNIST、CIFAR-10 浅层 MLP，并分析逐层信号
- **关键结果 / 消融** · 浅层表现具竞争力，但随深度增加学习信号衰减
- **适用条件 / 局限** · 深层实验细节和定理边界待核

**可复用机制** · 比较替代学习规则时记录逐层目标信号，并按深度拆分精度与计算成本。

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

<a id="paper-148682"></a>

## $PAS^2$: Physics-Anchored Spectral Reasoning for Air Quality Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/148682) · [作者来源](https://neurips.cc/virtual/2026/poster/148682)

- **问题 / 瓶颈** · 混合模型可能重复拟合一致趋势，热点突变难由局部空间特征区分。
- **核心创新 / 方法** · 物理估计锚定输入，神经分支联合局部图扩散与谱算子刻画剩余波动。
- **Baseline** · 数据驱动与物理引导模型，名称待核实。
- **Benchmark** · 真实空气质量数据，尤其关注突变；指标待核实。
- **关键结果 / 消融** · 作者报告优于对照，突变场景更明显；数值待核实。
- **适用条件 / 局限** · 依赖物理估计能解释稳定趋势。

**可复用机制** · 按平稳和突变时段分别比较直接预测与物理锚定的残差分工。

<a id="paper-139571"></a>

## $\pi$-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows

[官方论文页](https://neurips.cc/virtual/2026/poster/139571) · [作者来源](https://neurips.cc/virtual/2026/poster/139571)

- **问题 / 瓶颈** · 任务成功率掩盖助手是否能根据早期交互处理未明说的约束。
- **核心创新 / 方法** · 让需求跨会话逐步显现，设置任务依赖和用户画像。
- **Baseline** · 比较任务完成和主动性，具名模型待核实。
- **Benchmark** · 五种用户画像、100 个多轮任务，观察主动性与完成情况。
- **关键结果 / 消融** · 作者报告两类表现可分离，历史交互有助于后来识别意图。
- **适用条件 / 局限** · 模拟画像和预设意图未必覆盖真实用户。

**可复用机制** · 同一工作流对照保留及去除历史，并分别测正确主动行为和任务完成。

<a id="paper-148690"></a>

## $\pi^2$: A Simple Framework for 2D-to-3D Registration

[官方论文页](https://neurips.cc/virtual/2026/poster/148690) · [作者来源](https://neurips.cc/virtual/2026/poster/148690)

- **问题 / 瓶颈** · 匹配、可见性等多级中间输出增加配准复杂度。
- **核心创新 / 方法** · 逐点回归相机系坐标，SVD 求原点集到预测点集的刚体变换，以相机射线做训练正则。
- **Baseline** · 对比 ICL。
- **Benchmark** · KITTI 与 nuScenes，配准成功率和帧率。
- **关键结果 / 消融** · 比 ICL 分别高 2.47 与 6.72 个百分点，约 25 FPS。
- **适用条件 / 局限** · 严重遮挡下的稳定性与硬件计时细节待核实。

**可复用机制** · 用可解析的几何解码替代学习式位姿头，隔离回归误差和位姿求解成本。

<a id="paper-154197"></a>

## $R^3$: 3D Reconstruction via Relative Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/154197) · [作者来源](https://neurips.cc/virtual/2026/poster/154197)

- **问题 / 瓶颈** · 长序列使固定原点难维护，位移尺度也会增长。
- **核心创新 / 方法** · MLP 预测相对约束与置信度，统一用于训练加权和推理聚合。
- **Baseline** · 对照全局坐标回归路线；具名基线待核实。
- **Benchmark** · 离线与因果流式重建；数据和指标待核实。
- **关键结果 / 消融** · 作者报告方法支持有界内存流式推理；误差与数值待核实。
- **适用条件 / 局限** · 相对约束仍可能累积漂移。

**可复用机制** · 对长序列分别测绝对和相对表示的漂移、内存及窗口截断敏感性。

<a id="paper-153739"></a>

## $SE(2)$-Aware Conditional Distribution Transport for Vehicle Trajectory Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153739) · [作者来源](https://neurips.cc/virtual/2026/poster/153739)

- **问题 / 瓶颈** · 欧氏插值缺少车辆姿态演化的几何约束。
- **核心创新 / 方法** · 按真实数据学习条件分布，以 SE(2) 一致路径构造中间状态。
- **Baseline** · 对照其他轨迹生成方法；名称待核实。
- **Benchmark** · 真实驾驶轨迹数据，比较真实性、多样性和动态一致性。
- **关键结果 / 消融** · 作者报告三方面改善，少数运动的具体幅度待核实。
- **适用条件 / 局限** · 适用于平面刚体运动；几何归纳偏置不能替代稀有样本。

**可复用机制** · 固定数据，对照欧氏和群上插值，在不同运动频率分层测效果。

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

<a id="paper-151818"></a>

## $\textbf{EchMo}$: End-to-End Radar Echo Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/151818) · [作者来源](https://neurips.cc/virtual/2026/poster/151818)

- **问题 / 瓶颈** · 独立处理链的中间表示可能丢失对最终分割有用的信号。
- **核心创新 / 方法** · 在端到端 I/Q 输入模型中重构脉冲压缩、动目标指示和相干积累等操作。
- **Baseline** · 传统雷达流水线及依赖中间射频表示的模型。
- **Benchmark** · 脉冲多普勒雷达语义分割，数据和指标待核实。
- **关键结果 / 消融** · 作者报告分割和效率改善；数值待核实。
- **适用条件 / 局限** · 依赖原始 I/Q 信号，跨设备鲁棒性待核实。

**可复用机制** · 固定分割器和计算量，分别比较预处理固定、模块可学习和不加结构先验。

<a id="paper-151747"></a>

## $\text{PartConcepts}$: A Unified Mechanism for Fine-Grained Part Localization and Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151747) · [作者来源](https://neurips.cc/virtual/2026/poster/151747)

- **问题 / 瓶颈** · 物体级交叉注意力难区分左右部件。
- **核心创新 / 方法** · 用可学习的文本部件 token 选择性关注对应图像区域。
- **Baseline** · 专用部件分割基线，名称待核实。
- **Benchmark** · OVPS、Pascal-Part 及文本生成图像指令跟随。
- **关键结果 / 消融** · 摘要报告分割优于对照，生成时属性可绑定到部件；数值待核实。
- **适用条件 / 局限** · 训练信号和未见部件边界待核实。

**可复用机制** · 给局部语义单独学习查询，再用相同查询比较定位和生成控制。

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

<a id="paper-154751"></a>

## 2D Spatial Reasoning with Adaptive Neural Cellular Automata

[官方论文页](https://neurips.cc/virtual/2026/poster/154751) · [作者来源](https://neurips.cc/virtual/2026/poster/154751)

- **问题 / 瓶颈** · 规则网格上的固定邻域对远程几何关系建模受限。
- **核心创新 / 方法** · 在神经元胞自动机中用可变形卷积按状态调整感受野。
- **Baseline** · 摘要未列具名比较方法。
- **Benchmark** · 图像数独、迷宫最短路径等公开基准。
- **关键结果 / 消融** · 作者报告强泛化和领先结果；数字与独立消融待核实。
- **适用条件 / 局限** · 假定输入可表为二维网格；迭代次数和更大网格的边界待核实。

**可复用机制** · 固定推理步数对照固定邻域与动态邻域，检查距离增大时的性能差距。

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

<a id="paper-151779"></a>

## 3DABSeg: Adaptive 3D Ankle Bone Segmentation with Multiscale Feature Fusion Mixture-of-Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/151779) · [作者来源](https://neurips.cc/virtual/2026/poster/151779)

- **问题 / 瓶颈** · 不同通道承载的解剖信息不均，融合可能稀释边界特征。
- **核心创新 / 方法** · 用多尺度池化生成路由分数，互斥分配到融合专家，另用 KAN 与 Mamba 混合块。
- **Baseline** · 摘要未列具名方法。
- **Benchmark** · 两套踝骨 CT 数据；分割和边界精度。
- **关键结果 / 消融** · 作者报告优于对照；路由与混合块独立贡献待核。
- **适用条件 / 局限** · 主要验证在踝骨 CT；跨器官适用性待核。

**可复用机制** · 固定三维编码器，对照多尺度硬路由、软融合及共享专家，按边界误差检验增益。

<a id="paper-139453"></a>

## 3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code

[官方论文页](https://neurips.cc/virtual/2026/poster/139453) · [作者来源](https://neurips.cc/virtual/2026/poster/139453)

- **问题 / 瓶颈** · 仅靠通过执行或自动相似度难衡量程序化资产质量。
- **核心创新 / 方法** · 联合程序执行评测与人工成对偏好，并对失败归因和推理预算做分析。
- **Baseline** · 11 个 VLM，及不同推理预算、单轮和多轮。
- **Benchmark** · 3DCodeBench 和 3DCodeArena，输入文本及参考图。
- **关键结果 / 消融** · 强调 API 用法是主要失败源；能渲染的资产仍可断裂或悬浮，增加推理及多轮通常改善。
- **适用条件 / 局限** · 发现取决于所测接口及资产，未给摘要细分数值。

**可复用机制** · 为生成代码的 Agent 加程序可执行性和输出结构完整性两道评测，按失败类型决定反馈。

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

<a id="paper-155228"></a>

## 3D Fresnel Volumizing for Efficient Implicit Velocity Field Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/155228) · [作者来源](https://openreview.net/forum?id=7JwhEn9uk1)

- **问题 / 瓶颈** · 全波形反演耗时，射线近似的梯度在三维空间很稀疏。
- **核心创新 / 方法** · 用坐标网络表示速度场，将可微射线路径扩展为菲涅耳体积，以二维切片网络构造三维邻域。
- **Baseline** · 全波形反演及论文消融对照。
- **Benchmark** · 合成三维速度场重建，比较精度和耗时；具体误差指标待核实。
- **关键结果 / 消融** · 作者摘要报告最高约十倍加速且精度相近。
- **适用条件 / 局限** · 证据来自合成数据；体积近似在实测异质介质中的误差待核实。

**可复用机制** · 稀疏路径上的参数梯度不足时，比较物理相关的体积梯度与逐射线更新。

<a id="paper-156149"></a>

## 3D Gaussian Splatting within Self-Learned Neural View-Dependent Color Fields

[官方论文页](https://neurips.cc/virtual/2026/poster/156149) · [作者来源](https://openreview.net/forum?id=00MXC2OlRy)

- **问题 / 瓶颈** · 各高斯颜色独立变化会允许错误的几何仍拟合彩色图像。
- **核心创新 / 方法** · 以神经网络表示连续视角相关颜色场，约束颜色变化与空间位移的比例，促使几何解释高频图像变化。
- **Baseline** · 以独立颜色属性的 3DGS 为对照，具名版本待核实。
- **Benchmark** · 通用新视角合成及几何恢复评测，具体数据集与指标待核实。
- **关键结果 / 消融** · 作者摘要报告几何恢复改善，量化幅度待核实。
- **适用条件 / 局限** · 平滑颜色先验与材质真实急变可能不一致。

**可复用机制** · 在同等渲染误差下比较颜色连续性约束对深度和漂浮伪影的影响。

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

<a id="paper-155977"></a>

## 3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model

[官方论文页](https://neurips.cc/virtual/2026/poster/155977) · [作者来源](https://openreview.net/forum?id=1PQ7pf3kVm)

- **问题 / 瓶颈** · 通道调整无法直接恢复域偏移下失效的跨视角对应。
- **核心创新 / 方法** · 检索可变形关系候选、重连跨视角关系并以一致性细化预测。
- **Baseline** · 通常只调整通道的 PEFT 方法；具名对照待核。
- **Benchmark** · 低光重建、人场景联合重建、测试时适配。
- **关键结果 / 消融** · 作者报告多个长尾场景改善；幅度待核。
- **适用条件 / 局限** · 依赖域内仍可检索到对应关系。

**可复用机制** · 做域适配前先定位失败来自通道表示还是关系结构，再分别比较两类适配器。

<a id="paper-148721"></a>

## A$^2$IQL: Adaptive Asymmetric Implicit Q Learning for Automated Warehouse Consolidation

[官方论文页](https://neurips.cc/virtual/2026/poster/148721) · [作者来源](https://openreview.net/forum?id=vXRQ63UjQR)

- **问题 / 瓶颈** · 可变候选集和目标域奖励不匹配限制迁移。
- **核心创新 / 方法** · actor 独立打分，critic 看集合统计；用带不确定性惩罚的新奖励仅调整 actor 提取。
- **Baseline** · 启发式、源域训练、数据合并和异动态基线。
- **Benchmark** · 仓储合并日志，比较吞吐及目标迁移。
- **关键结果 / 消融** · 单域吞吐较启发式提高 20%，目标域提升幅度待核。
- **适用条件 / 局限** · 依赖目标域少量奖励数据及集合统计充分性。

**可复用机制** · 有固定日志的列表决策中以聚合 critic 降复杂度，迁移时对照只改 actor 和全量更新。

<a id="paper-139138"></a>

## A$^3$Bench: A Benchmark for Compositional Reasoning over Aggressive Interactions in Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/139138) · [作者来源](https://openreview.net/forum?id=iWKda5S9fT)

- **问题 / 瓶颈** · 粗类别分类掩盖参与者角色互换。
- **核心创新 / 方法** · 用含干扰人物的场景分别评估动作识别、角色区分和人–动作关系。
- **Baseline** · 15 种近期多模态模型，另比规模和通用推理提示。
- **Benchmark** · 视频组合推理，比较复杂度不同的参与角色绑定。
- **关键结果 / 消融** · 作者报告角色混淆随复杂度增加，规模和通用提示改善有限。
- **适用条件 / 局限** · 评测分布限所选视频，部署外推待核。

**可复用机制** · 评估细粒度视频理解时使用关系绑定量表，保留粗分类为对照。

<a id="paper-153258"></a>

## A2Eval: Agentic and Automated Evaluation for Embodied Brain

[官方论文页](https://neurips.cc/virtual/2026/poster/153258) · [作者来源](https://openreview.net/forum?id=MbGvHXDxKr)

- **问题 / 瓶颈** · 静态题库冗余且题型失衡会扭曲模型排名。
- **核心创新 / 方法** · 数据智能体归纳能力维度并构造平衡套件，评测智能体生成及核验评分流程。
- **Baseline** · 原始人工评测及与人类排序对照。
- **Benchmark** · 10 个基准、32 个模型，测成本、加速与 Spearman 排序相关性。
- **关键结果 / 消融** · 作者报告题库压缩 85%、计算降 77%，人类对齐相关系数 0.85。
- **适用条件 / 局限** · 依赖能力覆盖与自动评分核验，稀有能力保留情况待核。

**可复用机制** · 抽样缩减题库时同步验证分能力覆盖及与完整题集的排序相关性。

<a id="paper-149615"></a>

## A2I: Adjacency-to-Image Structural Encodings for Graph Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149615) · [作者来源](https://openreview.net/forum?id=omQbj7k7El)

- **问题 / 瓶颈** · 常见聚合及谱编码可能混淆非同构结构。
- **核心创新 / 方法** · 按 BFS 和度排序渲染邻接图，以冻结视觉编码器映射结构原型并与节点嵌入聚合。
- **Baseline** · GNN、图 Transformer 及已有结构编码。
- **Benchmark** · 六个节点分类基准，含异配和部分特征遮蔽场景。
- **关键结果 / 消融** · 作者报告异配及特征遮蔽下更有收益，并给出条件稳定性与可分性分析。
- **适用条件 / 局限** · 依赖排序、分辨率和有界度等分析条件。

**可复用机制** · 当谱特征不能区分局部结构时对照直接邻接编码，按异配与特征可用性拆分结果。

<a id="paper-148286"></a>

## A 3D Scene is Worth 1K Tokens: 3D-Grounded Representation for Scene Generation at Scale

[官方论文页](https://neurips.cc/virtual/2026/poster/148286) · [作者来源](https://openreview.net/forum?id=z0550PJPjK)

- **问题 / 瓶颈** · 多视图二维表示冗余且空间一致性受限。
- **核心创新 / 方法** · 从 DINOv2、SigLIP2、DA3 等基础模型导出隐式三维表示，在其中训练扩散 Transformer。
- **Baseline** · 二维多视图或视频扩散式场景生成。
- **Benchmark** · 场景生成效率、三维一致性及表示和模型扩展实验。
- **关键结果 / 消融** · 作者报告较二维方案更高效且更一致，量化待核。
- **适用条件 / 局限** · 依赖所选三维隐表示保留足够细节。

**可复用机制** · 在相同生成预算下比较二维多视角和三维共享潜空间。

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

<a id="paper-139047"></a>

## A Benchmark for Omni-Modal Reasoning in Long Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/139047) · [作者来源](https://openreview.net/forum?id=oCkr3KnHhU)

- **问题 / 瓶颈** · 单一答案分数无法定位长视频中的漏证或推理错误。
- **核心创新 / 方法** · 给开放问答提供加权分项量表；检索智能体按问题细化片段并核验各模态证据。
- **Baseline** · 既有长视频评测路线及基础模型，具名对照待核。
- **Benchmark** · LongShOTBench 单轮和多轮问答，涵盖视觉、语音、非语音音频及跨模态时序。
- **关键结果 / 消融** · 摘要描述人工核对量表和长视频证据检索，具体数值待核。
- **适用条件 / 局限** · 量表覆盖受题型与评分器影响。

**可复用机制** · 把长视频问答的结果评分拆为各模态事实、时序关系和证据支持率。

<a id="paper-139180"></a>

## ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/139180) · [作者来源](https://openreview.net/forum?id=g95RNNdLn1)

- **问题 / 瓶颈** · 第三人称文字判断看不出交互环境中的实际选择。
- **核心创新 / 方法** · 对同一叙事场景，从文字抽象与第一人称多模态环境分别评估道德行动。
- **Baseline** · 配对文字场景和游戏场景，比较 12 种基础模型。
- **Benchmark** · ABHBench 评估无害、服从、自保及选择稳定性。
- **关键结果 / 消融** · 75% 模型在匹配条件下显著改变行为，推理增强未带来单调提升。
- **适用条件 / 局限** · 证据限一个叙事游戏，外推依赖场景效度。

**可复用机制** · 设计智能体评测时将静态判断与同内容的行动任务配对对照。

<a id="paper-151803"></a>

## A Biconvex Formulation for Stable Transport of Mixture Models with a Unique Solution

[官方论文页](https://neurips.cc/virtual/2026/poster/151803) · [作者来源](https://openreview.net/forum?id=XuKcEuYQSB)

- **问题 / 瓶颈** · 逐点传输难扩展且难解释。
- **核心创新 / 方法** · 用指数族混合成分建严格双凸输运问题，并证明全局解唯一。
- **Baseline** · 逐点 OT；具名方法待核。
- **Benchmark** · 合成、图像和单细胞表达数据。
- **关键结果 / 消融** · 作者证明分布扰动受限时解变化有界，计算规模取决于成分数量。
- **适用条件 / 局限** · 依赖混合分解及模型假设。

**可复用机制** · 按样本量和成分数分别扫描时间与传输稳定性。

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

<a id="paper-139176"></a>

## AbsoluteDegradation: A Physics-Inspired Synthetic Film-Degradation Pipeline and Archival Film Restoration Benchmark

[官方论文页](https://neurips.cc/virtual/2026/poster/139176) · [作者来源](https://openreview.net/forum?id=gKunvq63KY)

- **问题 / 瓶颈** · 真实老胶片无法构造无退化配对。
- **核心创新 / 方法** · 按模拟到数字过程组合信号相关颗粒、划痕和时间连贯运动。
- **Baseline** · 既有合成训练与多个恢复架构，具名者待核。
- **Benchmark** · 81,576 帧真实档案胶片及合成训练对照。
- **关键结果 / 消融** · 作者报告合成训练改善对真实素材泛化，量化幅度待核。
- **适用条件 / 局限** · 真实数据缺完好配对，定量评价定义待核。

**可复用机制** · 按伪影类别拆分训练增强，对比独立逐帧和连贯退化。

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

<a id="paper-154083"></a>

## AcceleGrad#: Adaptive Geometry-Aware Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/154083) · [作者来源](https://openreview.net/forum?id=GL9byFkJNj)

- **问题 / 瓶颈** · 在线自适应、几何结构和加速难统一。
- **核心创新 / 方法** · 以线性耦合组合自适应锚点和范数诱导的几何分支。
- **Baseline** · 欧氏 AcceleGrad 与非欧优化器。
- **Benchmark** · 图像分类、语言建模及不同理论目标。
- **关键结果 / 消融** · 标量锚点在光滑凸目标达二次倒数速率；训练版本报告优于欧氏对照。
- **适用条件 / 局限** · 不同收敛率对应不同局部条件，不能互换。

**可复用机制** · 固定锚点策略更换几何分支并记录累计优化器开销。

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

<a id="paper-152485"></a>

## Accelerating Diffusion Language Models via Structured Suffix Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/152485) · [作者来源](https://openreview.net/forum?id=SkQxO613nL)

- **问题 / 瓶颈** · 统一局部窗口忽略后缀各段角色，重初始化也丢历史。
- **核心创新 / 方法** · 划分近、中、尾区并分配不同 token 数，将前步结果融入后缀表示。
- **Baseline** · 全后缀及仅局部窗口策略。
- **Benchmark** · 三种扩散语言模型和多项任务，比较速度与质量。
- **关键结果 / 消融** · 作者报告与其他加速叠加时长序列最高 72.16 倍。
- **适用条件 / 局限** · 最高值不是该模块单独收益。

**可复用机制** · 单独测分区选择和跨步状态复用，以同长度确认质量。

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

<a id="paper-154875"></a>

## Accelerating Long-Context LLM Prefill via Layer-wise Progressive Token Pruning in Local Deployment

[官方论文页](https://neurips.cc/virtual/2026/poster/154875) · [作者来源](https://openreview.net/forum?id=AEnl58AdSd)

- **问题 / 瓶颈** · 仅稀疏注意力不省 FFN，恢复 token 也有开销。
- **核心创新 / 方法** · 离线寻优剪枝日程，在线执行每个头独立的稀疏键值选择且无恢复。
- **Baseline** · 已有长上下文加速，具体实现待核。
- **Benchmark** · LongBench、RULER，质量、首 token 与端到端速度。
- **关键结果 / 消融** · 最高 2.13 倍首 token 加速和 3.03 倍端到端加速。
- **适用条件 / 局限** · 质量和时延依赖部署硬件与提示分布。

**可复用机制** · 固定质量约束联调层级剪枝与头级选择，报告首 token 和端到端指标。

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

<a id="paper-154818"></a>

## Accelerating the Inference Era with AI-Driven, Globally Optimized HW/SW Co-Design

[官方论文页](https://neurips.cc/virtual/2026/poster/154818) · [作者来源](https://openreview.net/forum?id=AjGASENFly)

- **问题 / 瓶颈** · 串行软硬件搜索漏掉跨阶段权衡。
- **核心创新 / 方法** · 用时间索引变量、重算变量和线性化联合表述，外层按部署信号搜索。
- **Baseline** · TPU-v3 及分离式设计流程。
- **Benchmark** · 11 个推理工作负载，比较速度及设计搜索时间。
- **关键结果 / 消融** · 作者报告六小时内找到方案，较 TPU-v3 平均约 22 倍原始加速。
- **适用条件 / 局限** · 跨硬件公平性及实物验证待核。

**可复用机制** · 在固定硬件预算对照联合与顺序求解产生的性能前沿。

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

<a id="paper-154840"></a>

## Accuracy of Noise Ceiling Estimators for Brain Scores

[官方论文页](https://neurips.cc/virtual/2026/poster/154840) · [作者来源](https://openreview.net/forum?id=AWvO8s9XuP)

- **问题 / 瓶颈** · 脑记录的噪声限制编码模型可达表现。
- **核心创新 / 方法** · 在统一记录模型下推导四种估计器并以仿真验证。
- **Baseline** · 四种常用噪声上限估计方法。
- **Benchmark** · 仿真与已有 fMRI 数据，比较估计偏差。
- **关键结果 / 消融** · 作者发现多种情形下估计器低估上限。
- **适用条件 / 局限** · 依赖记录分布和重复试验设置，具体建议待核。

**可复用机制** · 按记录与试次数模拟校准后再解释归一化脑分数。

<a id="paper-148397"></a>

## Accuracy vs. Accuracy: Computational Tradeoffs Between Classification Rates and Utility

[官方论文页](https://neurips.cc/virtual/2026/poster/148397) · [作者来源](https://openreview.net/forum?id=y9NcQvGb4C)

- **问题 / 瓶颈** · 丰富标签下子群比例与个体预测目标可能冲突
- **核心创新 / 方法** · 以贝叶斯最优丰富预测器的正分类比例定义子群精度，证明联合目标的计算障碍
- **Baseline** · 逐项高效求解与贝叶斯最优预测器
- **Benchmark** · 概率、类型或排序标签下的理论设定
- **关键结果 / 消融** · 即使逐项可高效实现且贝叶斯解同时满足，联合实现仍可能计算不可行
- **适用条件 / 局限** · 结论限论文所构造条件，常见数据上的影响待核实

**可复用机制** · 分开审查子群比例、校准与损失的可计算性

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

<a id="paper-154537"></a>

## ACDP: Architecture-aware Cross-Dataset Performance Predictor for NAS

[官方论文页](https://neurips.cc/virtual/2026/poster/154537) · [作者来源](https://openreview.net/forum?id=Cr87H0HSqL)

- **问题 / 瓶颈** · 直接拼接数据集和架构特征忽略两者的交互
- **核心创新 / 方法** · 可调数据特征提取加按架构条件化的超网络
- **Baseline** · 单数据集和跨数据集 NAS 性能预测方法
- **Benchmark** · 六个未见数据集、NAS-Bench-201 和 MobileNetV3
- **关键结果 / 消融** · CIFAR-10/100 的 Kendall τ 为 0.758/0.741；Aircraft 搜索准确率增益 2.04%
- **适用条件 / 局限** · 依赖已有架构与数据表现三元组

**可复用机制** · 让架构特征决定数据集的表征方式

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

<a id="paper-148646"></a>

## A Characterization of Latent Variable Causal Models Consistent with Observational Data

[官方论文页](https://neurips.cc/virtual/2026/poster/148646) · [作者来源](https://openreview.net/forum?id=wBBL9K3qVC)

- **问题 / 瓶颈** · 观察数据无法区分有相同条件独立性的结构模型
- **核心创新 / 方法** · 用可微参数和受部分祖先图约束的神经因果模型表示等价类
- **Baseline** · 单一结构假设的反事实估计是概念对照；实验基线待核实
- **Benchmark** · 表示定理、部分识别优化与模拟
- **关键结果 / 消融** · 证明覆盖类内反事实分布且保持结构约束
- **适用条件 / 局限** · 依赖给定的部分祖先图和优化质量

**可复用机制** · 在整个潜变量因果等价类上优化反事实范围

<a id="paper-154129"></a>

## Achieve Latency-Efficient Temporal-Coding  Spiking LLMs via Discretization-Aware Conversion

[官方论文页](https://neurips.cc/virtual/2026/poster/154129) · [作者来源](https://openreview.net/forum?id=G3WiNUM5h1)

- **问题 / 瓶颈** · 连续时间转换需要很长脉冲时间窗
- **核心创新 / 方法** · 建立离散首次脉冲模型与静态量化 ANN 的等价性，再做量化一致转换
- **Baseline** · 连续假设下的首次脉冲编码转换
- **Benchmark** · 代表性语言模型及多个基准；名称待核实
- **关键结果 / 消融** · 作者报告降低延迟并保持竞争性表现
- **适用条件 / 局限** · 实际部署收益依赖硬件与时间离散化

**可复用机制** · 以静态量化误差分析离散首次脉冲时间编码

<a id="paper-156739"></a>

## Achieving adaptivity and optimality for multi-armed bandits using Exponential-Kullback Leibler Maillard Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/156739) · [作者来源](https://neurips.cc/virtual/2026/poster/156739)

- **问题 / 瓶颈** · 已有算法通常分别满足不同最优准则
- **核心创新 / 方法** · 使用指数 KL Maillard 采样统一处理多种准则
- **Baseline** · Thompson Sampling 和 UCB 系列
- **Benchmark** · K 臂单参数指数族的理论分析
- **关键结果 / 消融** · 同时达到渐近最优、Sub-UCB、方差自适应及带对数因子的极小极大界
- **适用条件 / 局限** · 依赖奖励分布族，极小极大结果保留额外因子

**可复用机制** · 分布属于单参数指数族时同时考察多种遗憾标准

<a id="paper-148523"></a>

## Achieving Better Local Regret Bound for Online Non-Convex Bilevel Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/148523) · [作者来源](https://openreview.net/forum?id=xFpqYVlNo9)

- **问题 / 瓶颈** · 双层局部遗憾界是否最优尚不明确
- **核心创新 / 方法** · 分别对标准和窗口平均局部遗憾分析，依据变化量调节内层更新
- **Baseline** · 已有在线双层优化器；实验方法名待核实
- **Benchmark** · 标准和窗口局部遗憾、梯度评估次数及实验
- **关键结果 / 消融** · 给出两种最优界；窗口单循环版本在梯度次数与遗憾之间折衷
- **适用条件 / 局限** · 理论条件与具体实验数据待全文确认

**可复用机制** · 依据环境变化和预算选择自适应内循环或单循环

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

<a id="paper-154262"></a>

## Achieving Optimal Static and Dynamic Regret Simultaneously in Bandits with Deterministic Losses

[官方论文页](https://neurips.cc/virtual/2026/poster/154262) · [作者来源](https://openreview.net/forum?id=F6AmedacpX)

- **问题 / 瓶颈** · 分别最优不代表可同时最优
- **核心创新 / 方法** · 证明自适应对手下障碍，并对非自适应对手用负静态遗憾抵消探索代价
- **Baseline** · 分别优化静态或动态遗憾的既有算法
- **Benchmark** · 确定性损失的对抗赌博机理论
- **关键结果 / 消融** · 区分自适应与非自适应对手，后者可同时取得最优界
- **适用条件 / 局限** · 确定性损失结论不可直接外推

**可复用机制** · 根据对手可否适应来判断能否联合优化静态和动态遗憾

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

<a id="paper-148660"></a>

## A Composite Activation Function for Learning Stable Binary Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/148660) · [作者来源](https://openreview.net/forum?id=w5Om6MXAow)

- **问题 / 瓶颈** · Heaviside 不可导，普通平滑代理远离阈值时梯度衰减
- **核心创新 / 方法** · 构造 sigmoid 与双曲正切的重尾复合激活
- **Baseline** · 标准二值和图像预测模型；具体配置待核实
- **Benchmark** · 脉冲、二值及深 Heaviside 网络和概念瓶颈图像任务
- **关键结果 / 消融** · 报告稳定训练与离散化，预测表现可比或更好
- **适用条件 / 局限** · 训练代理到部署离散表示的误差需验证

**可复用机制** · 训练二值激活时保留阈值附近及尾部的梯度

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

<a id="paper-152347"></a>

## A Constrained Bi-level Optimization Framework for Constrained Preference-Based Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152347) · [作者来源](https://openreview.net/forum?id=TjhQ07qEGv)

- **问题 / 瓶颈** · 专家偏好同时包含效用和约束线索
- **核心创新 / 方法** · 外层从偏好拟合奖励及成本，内层优化受约束策略
- **Baseline** · 具体约束偏好学习对照待核实
- **Benchmark** · 多种仿真环境及理论收敛分析
- **关键结果 / 消融** · 给出 O(1/√K) 收敛率并报告仿真有效性
- **适用条件 / 局限** · 奖励与成本的可辨识性和适用于真实反馈的条件待核实

**可复用机制** · 从反馈同时学习奖励与约束成本，而非预设约束成本

<a id="paper-154268"></a>

## A Control-Theoretic Approximation to Predictive Coding Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/154268) · [作者来源](https://openreview.net/forum?id=F4cKpRSPTz)

- **问题 / 瓶颈** · 层间误差传播用于局部学习时迭代成本高
- **核心创新 / 方法** · 推导深度反馈控制是固定点附近近似，以连续中间子目标替换逐层传播
- **Baseline** · 预测编码与深度反馈控制
- **Benchmark** · 浅层线性等价理论及实验；数据集待核实
- **关键结果 / 消融** · 浅层线性网络严格等价，作者报告近似法更快且更准确
- **适用条件 / 局限** · 深度、非线性和偏离平衡会引入误差

**可复用机制** · 在接近平衡时用集中反馈近似预测编码

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

<a id="paper-150320"></a>

## A Critical $\beta$-Scale for Posterior Collapse in Dirichlet $\beta$-VAEs

[官方论文页](https://neurips.cc/virtual/2026/poster/150320) · [作者来源](https://openreview.net/forum?id=izJBnbQo5y)

- **问题 / 瓶颈** · 高斯潜变量分析不适用于单纯形
- **核心创新 / 方法** · 从数据谱、先验浓度及 trigamma 曲率推导临界值
- **Baseline** · 高斯 VAE 理论作为背景
- **Benchmark** · 高光谱解混与凸原型分析
- **关键结果 / 消融** · 正则与临界值之比可组织经验坍塌行为
- **适用条件 / 局限** · 局部推导针对对称 Dirichlet 和线性高斯解码器

**可复用机制** · 用无量纲临界比安排扫描区间。

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

<a id="paper-155735"></a>

## AdaAlloc: Adaptive Visual Token Allocation for Long-Video Question Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/155735) · [作者来源](https://openreview.net/forum?id=3L6GFiwoG6)

- **问题 / 瓶颈** · 均匀采样可能丢掉局部关键动作
- **核心创新 / 方法** · 按问题分配全局与局部预算并定位相关时间段
- **Baseline** · 同骨干同预算的视频问答方法
- **Benchmark** · LVBench、MLVU、VideoMME 等
- **关键结果 / 消融** · 作者报告持续改善，幅度待核实
- **适用条件 / 局限** · 依赖时序定位质量

**可复用机制** · 在同预算比较全局覆盖与局部分辨率的分配方式。

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

<a id="paper-153261"></a>

## AdaKVQ: Adaptive Mixed-Precision KV Cache Quantization For Efficient Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153261) · [作者来源](https://openreview.net/forum?id=MaITgepVoU)

- **问题 / 瓶颈** · 静态极低比特同时损伤长程检索并拉长生成
- **核心创新 / 方法** · 用平均注意距离识别深浅层及位置的不同精度需求
- **Baseline** · 静态 KV 量化
- **Benchmark** · 复杂推理的准确率与生成长度
- **关键结果 / 消融** · 作者观察到低比特精度下退化和生成变长并存
- **适用条件 / 局限** · 注意距离是需求代理

**可复用机制** · 观察注意距离再分配缓存精度，比较收益与适用条件。

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

<a id="paper-148211"></a>

## AdaM-Rec: Adaptive Modality Routing for Multimodal Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/148211) · [作者来源](https://openreview.net/forum?id=zXa9cVWJdT)

- **问题 / 瓶颈** · 静态融合会注入与当前请求无关的模态
- **核心创新 / 方法** · 以用户请求和结构化商品描述驱动模态路由
- **Baseline** · 静态模态融合
- **Benchmark** · 多模态推荐
- **关键结果 / 消融** · 具体效应量需核全文
- **适用条件 / 局限** · 依赖商品描述质量

**可复用机制** · 按查询选择视觉或文本证据，比较收益与适用条件。

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

<a id="paper-150249"></a>

## AdaPCLA: Curriculum Prior Internalization For Long-Tailed Longitudinal EHR Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150249) · [作者来源](https://openreview.net/forum?id=jdm8WK08ec)

- **问题 / 瓶颈** · 标准生成器低估尾部事件共现
- **核心创新 / 方法** · 通过分布感知退火内化先验并用标签经验 NTK 分析稀有更新
- **Baseline** · 标准自回归记录生成
- **Benchmark** · 纵向电子健康记录的尾部共现
- **关键结果 / 消融** · 作者给出与退火速度和 NTK 条件相关的界
- **适用条件 / 局限** · 记录分布控制无法替代隐私或临床核验

**可复用机制** · 按退火调度逐步引入稀有事件分布先验，比较收益与适用条件。

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

<a id="paper-155009"></a>

## AdaptFlow: State-Anchored Goal Conditioning with Flow Matching for Offline Goal-Conditioned RL

[官方论文页](https://neurips.cc/virtual/2026/poster/155009) · [作者来源](https://openreview.net/forum?id=9H4BX9fISD)

- **问题 / 瓶颈** · 固定目标在不同状态下的相关部分变化
- **核心创新 / 方法** · 联合编码状态和目标，产生流策略调制的缩放和偏置
- **Baseline** · 普通条件生成策略
- **Benchmark** · 离线目标条件强化学习
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 依赖离线数据目标覆盖

**可复用机制** · 让状态与目标共同决定调制参数，比较收益与适用条件。

<a id="paper-150038"></a>

## ADAPT: Hybrid Prompt Optimization for LLM Feature Visualization

[官方论文页](https://neurips.cc/virtual/2026/poster/150038) · [作者来源](https://openreview.net/forum?id=lF3IyYVmWh)

- **问题 / 瓶颈** · 离散激活最大化容易卡在局部最优
- **核心创新 / 方法** · 以束搜索初始化并配合自适应梯度变异
- **Baseline** · 既有离散提示优化
- **Benchmark** · Gemma 2 2B 稀疏自编码特征及基于数据激活的指标
- **关键结果 / 消融** · 作者报告跨层及特征类型改善
- **适用条件 / 局限** · 高激活不能单独证明因果功能

**可复用机制** · 先广搜离散提示，再用梯度导向变异，比较收益与适用条件。

<a id="paper-156089"></a>

## Adapting Actively on the Fly: Relevance-Guided Online Meta-Learning with Latent Concepts for Geospatial Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/156089) · [作者来源](https://openreview.net/forum?id=0SGmhIr9iM)

- **问题 / 瓶颈** · 地理标签昂贵且有选择偏差
- **核心创新 / 方法** · 融合潜在概念、主动学习和在线元学习以更新采样策略
- **Baseline** · 传统采样或依赖丰富标签的策略
- **Benchmark** · 有限预算下的地理目标发现
- **关键结果 / 消融** · 量化幅度需核全文
- **适用条件 / 局限** · 依赖空间数据和概念可迁移性

**可复用机制** · 采样时优先相关且未充分观测的地区，比较收益与适用条件。

<a id="paper-148897"></a>

## Adapting in the Dark: Efficient and Stable Test-Time Adaptation for Black-Box Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148897) · [作者来源](https://openreview.net/forum?id=uMjCKR7dmV)

- **问题 / 瓶颈** · 查询式输入适配昂贵
- **核心创新 / 方法** · 协调本地与黑盒预测，并结合一致性与样本筛选训练本地组件
- **Baseline** · 后处理与零阶优化及其他适配方案
- **Benchmark** · ImageNet-C、ImageNet-S/R
- **关键结果 / 消融** · 摘要报告 ViT-B/16 和 CLIP 准确率分别提升 7.1% 和 3.4%
- **适用条件 / 局限** · 依赖黑盒预测输出可用及本地模型足够相关

**可复用机制** · 为黑盒模型加可求梯度的轻量本地组件，比较收益与适用条件。

<a id="paper-148344"></a>

## Adapting to Conflict: Equilibrium Structure and Adaptive Learning in Harmonic Games

[官方论文页](https://neurips.cc/virtual/2026/poster/148344) · [作者来源](https://openreview.net/forum?id=yYe40MToUb)

- **问题 / 瓶颈** · 均衡可能是非凸集合，精细调参难迁移
- **核心创新 / 方法** · 描述奇维情形的均衡结构并给出外推 FTRL+
- **Baseline** · 精细调参的谐和博弈学习方法
- **Benchmark** · 纳什收敛与遗憾
- **关键结果 / 消融** · 证明可自适应收敛及最优阶遗憾
- **适用条件 / 局限** · 不同保证依赖博弈结构和比较情形

**可复用机制** · 在谐和博弈中选可适应的外推学习规则，比较收益与适用条件。

<a id="paper-150605"></a>

## Adapting Vision Transformers to Organoid Imaging

[官方论文页](https://neurips.cc/virtual/2026/poster/150605) · [作者来源](https://openreview.net/forum?id=gtWsD9XmKl)

- **问题 / 瓶颈** · 单数据集排名掩盖不同成像任务的迁移差异
- **核心创新 / 方法** · 跨公开数据集比较骨干并测试冻结骨干的小型域适配器
- **Baseline** · 12 个视觉基础模型
- **Benchmark** · OrgBench 的 13 个数据集，含检测、分割、分类与时序预测
- **关键结果 / 消融** · 领先模型随任务族变化，参数量预测能力有限
- **适用条件 / 局限** · 仅评估已有公开影像分布

**可复用机制** · 按影像任务选骨干而不只比较模型参数量，比较收益与适用条件。

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

<a id="paper-152820"></a>

## Adaptive Attribute Completion with Representation Space for Incomplete Graph Domain Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/152820) · [作者来源](https://openreview.net/forum?id=Q9ifmP2xFG)

- **问题 / 瓶颈** · 跨图迁移与缺失特征误差相互影响
- **核心创新 / 方法** · 用拓扑相似性引导联合补齐，迭代调整可信嵌入
- **Baseline** · 图领域适配与缺失属性处理
- **Benchmark** · 目标图节点属性部分缺失的迁移
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 依赖拓扑相似性可用于迁移

**可复用机制** · 在补齐缺失属性时同步更新可靠跨图表示，比较收益与适用条件。

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

<a id="paper-151194"></a>

## Adaptive Compression and Targeted Perturbation: A Unified Framework for Generalized Audio Deepfake Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151194) · [作者来源](https://openreview.net/forum?id=cFddukqYcW)

- **问题 / 瓶颈** · 固定瓶颈对不同音频伪造痕迹容量不足
- **核心创新 / 方法** · 从压缩池选择潜维数并结合防御性鲁棒正则
- **Baseline** · 固定检测瓶颈与标准增强
- **Benchmark** · ADD 2022、FakeOrReal、In-the-Wild
- **关键结果 / 消融** · 作者报告跨分布检测改善
- **适用条件 / 局限** · 需区分压缩与鲁棒训练各自贡献

**可复用机制** · 按输入调整检测表征维数，比较收益与适用条件。

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

<a id="paper-151580"></a>

## Adaptive Covariance and Multi-Layer Alignment for Out-of-Distribution Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151580) · [作者来源](https://openreview.net/forum?id=ZXtr5Sueqd)

- **问题 / 瓶颈** · 只看末层或固定度量会漏掉浅层线索
- **核心创新 / 方法** · 融合余弦和类条件高斯分数，并以 CutMix 代理分布外样本定层权重
- **Baseline** · 单层或固定层选择
- **Benchmark** · 跨域分布外检测
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 代理异常可能无法代表真实偏移

**可复用机制** · 按层和类内协方差可靠性组合检测分数，比较收益与适用条件。

<a id="paper-150287"></a>

## Adaptive Delayed-Update Cyclic Algorithm for Variational Inequalities

[官方论文页](https://neurips.cc/virtual/2026/poster/150287) · [作者来源](https://openreview.net/forum?id=jIJ566xVDK)

- **问题 / 瓶颈** · 循环坐标更新的调步长和同步代价较高
- **核心创新 / 方法** · 以全周期延迟算子信息实现局部自适应循环算法
- **Baseline** · 需线搜索或全局常数的方法
- **Benchmark** · 单调 Lipschitz 算子的 Minty 变分不等式
- **关键结果 / 消融** · 作者给出相应收敛分析
- **适用条件 / 局限** · 其他时延及非单调算子需另证

**可复用机制** · 用一轮前的算子信息减少块间同步，比较收益与适用条件。

<a id="paper-149207"></a>

## Adaptive Entropy-Sparing for Efficient Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149207) · [作者来源](https://openreview.net/forum?id=s9CM1Mf5CE)

- **问题 / 瓶颈** · 整段长度惩罚混淆关键推理和冗余验证
- **核心创新 / 方法** · 按组内高效参考定位序列位置，保护较早高熵步骤并惩罚超长后缀
- **Baseline** · 统一长度惩罚
- **Benchmark** · 长链推理的准确率与生成预算
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 熵是表面行为代理

**可复用机制** · 分开处理高熵关键阶段与过长后缀，比较收益与适用条件。

<a id="paper-153408"></a>

## Adaptive Feature Propagation for Attribute-Missing Graph Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/153408) · [作者来源](https://openreview.net/forum?id=LZKrYTeRWx)

- **问题 / 瓶颈** · 不可靠节点和过度平滑会损伤聚类
- **核心创新 / 方法** · 自适应估计传播贡献并保留判别性成分
- **Baseline** · 均匀传播及低通滤波
- **Benchmark** · 属性缺失图聚类
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 邻居可靠性的判断依赖观测图

**可复用机制** · 传播时按邻居可信度赋权而非一致平均，比较收益与适用条件。

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

<a id="paper-150627"></a>

## Adaptive Gated Simplicial Propagation for Node Classification in Multimodal Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/150627) · [作者来源](https://openreview.net/forum?id=ggQrbEi624)

- **问题 / 瓶颈** · 两两边难描述高阶关联
- **核心创新 / 方法** · 以单纯复形传播表达高阶关系，再按适应性门控融合
- **Baseline** · 两两 GNN
- **Benchmark** · 图文节点分类
- **关键结果 / 消融** · 量化结果需核全文
- **适用条件 / 局限** · 高阶结构生成可能增加成本

**可复用机制** · 门控聚合不同阶关系，比较收益与适用条件。

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

<a id="paper-151811"></a>

## Adaptive Inference for Functionals of M-Estimands

[官方论文页](https://neurips.cc/virtual/2026/poster/151811) · [作者来源](https://openreview.net/forum?id=Xpq9yAhis0)

- **问题 / 瓶颈** · 自适应采样下无偏估计量仍可能偏离正态
- **核心创新 / 方法** · 用 Neyman 正交性处理自适应数据中的平滑 M 估计泛函
- **Baseline** · 直接应用经典置信区间
- **Benchmark** · 自适应采样的泛函覆盖率理论
- **关键结果 / 消融** · 作者给出渐近有效区间框架
- **适用条件 / 局限** · 依赖正交条件和相应渐近假设

**可复用机制** · 针对路径依赖方差构造置信区间，比较收益与适用条件。

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

<a id="paper-148204"></a>

## Adaptive Joint Testing of Policies in Discounted Markov Decision Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/148204) · [作者来源](https://openreview.net/forum?id=zaV6HqToRX)

- **问题 / 瓶颈** · 单轨迹要同时确认证策族价值符号。
- **核心创新 / 方法** · 用占用测度对符号翻转备择做最大最小分配，并逐策略停止。
- **Baseline** · 实例下界
- **Benchmark** · 折扣表格 MDP 固定置信度检验
- **关键结果 / 消融** · 探索下限趋零时达到实例一阶速率。
- **适用条件 / 局限** · 需锚策略遍历性及可认证数值程序。

**可复用机制** · 按最难区分的价值符号分配探索，再分别停止已获证据的策略。

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

<a id="paper-151071"></a>

## Adaptive-Margin Masking and Restoration for Balanced Multimodal Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151071) · [作者来源](https://openreview.net/forum?id=dBEoIGFglt)

- **问题 / 瓶颈** · 优势模态压制其他模态，硬识别落后模态易误判。
- **核心创新 / 方法** · 用自适应间隔识别模态，结合掩码与恢复优化。
- **Baseline** · 竞争性模态平衡方法，名称待核
- **Benchmark** · 标准多模态基准，指标待核
- **关键结果 / 消融** · 作者报告各基准改善，幅度待核。
- **适用条件 / 局限** · 间隔和恢复的独立收益待核。

**可复用机制** · 用可随训练状态变化的间隔决定何时保护弱模态。

<a id="paper-153325"></a>

## Adaptive Mass-Segmented KV Compression for Long-Context Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/153325) · [作者来源](https://openreview.net/forum?id=M9KP5PrKtK)

- **问题 / 瓶颈** · 重复按 token 打分会清空连续推理片段。
- **核心创新 / 方法** · 先分段分配容量再段内评分，并用滑动平均保留历史配额信息。
- **Baseline** · 同一 token 打分器及完整 KV
- **Benchmark** · MATH500、AIME24/25、GSM8K 的 pass@1，另有检索等任务
- **关键结果 / 消融** · 相对基础打分器最高加 20 个百分点。
- **适用条件 / 局限** · 受语段划分及预算影响，注意力峰值并不总对应有用历史。

**可复用机制** · 在相同 KV 预算下测分段配额能否减少片段彻底丢失。

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

<a id="paper-151789"></a>

## Adaptive Multi-view Graph Contrastive Learning via Fractional Continuous Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/151789) · [作者来源](https://openreview.net/forum?id=Xzigfjpz3Z)

- **问题 / 瓶颈** · 手工局部和全局视图覆盖尺度有限。
- **核心创新 / 方法** · 学习分数阶动力学的导数阶数，控制传播从局部到更广范围。
- **Baseline** · 既有图对比学习方法
- **Benchmark** · 节点级与图级基准
- **关键结果 / 消融** · 作者报告持续优于对照；幅度待核。
- **适用条件 / 局限** · 连续动力学求解成本及不同图结构的收益待核。

**可复用机制** · 把图视图尺度变成可学习的传播参数。

<a id="paper-151670"></a>

## Adaptive Power Iteration Method for Differentially Private PCA

[官方论文页](https://neurips.cc/virtual/2026/poster/151670) · [作者来源](https://openreview.net/forum?id=YuZcmpevYA)

- **问题 / 瓶颈** · 通用私有 PCA 界无法利用低相干结构。
- **核心创新 / 方法** · 用相干性自适应过滤改造私有幂迭代。
- **Baseline** · 行邻接的 Dwork 等框架及单元素邻接的 Hardt–Roth
- **Benchmark** · 差分隐私下首奇异向量的理论误差
- **关键结果 / 消融** · 低相干矩阵获得优于最坏情形的保证。
- **适用条件 / 局限** · 收益依赖低相干性；邻接模型按行定义。

**可复用机制** · 为私有谱估计额外检查输入相干性，再选自适应过滤。

<a id="paper-150933"></a>

## Adaptive Prior Selection in Gaussian Process Bandits with Thompson Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/150933) · [作者来源](https://openreview.net/forum?id=eCoYINxGo4)

- **问题 / 瓶颈** · 用点估计选 GP 超参数缺少遗憾依据。
- **核心创新 / 方法** · 或淘汰预测差的先验，或给先验加超先验后做双层 Thompson 采样。
- **Baseline** · 已有 GP 先验选择法
- **Benchmark** · 合成及真实数据，累计遗憾理论
- **关键结果 / 消融** · 超先验策略有次线性遗憾上界。
- **适用条件 / 局限** · 需预设先验族，错设情况下边界待核。

**可复用机制** · 对 GP 探索比较淘汰与维持超先验不确定性。

<a id="paper-150422"></a>

## Adaptive Random Forests from Online Learning and Testing by Betting

[官方论文页](https://neurips.cc/virtual/2026/poster/150422) · [作者来源](https://openreview.net/forum?id=i9u9Y9oW7j)

- **问题 / 瓶颈** · 漂移检测器触发的整树重置难调。
- **核心创新 / 方法** · 用强自适应在线聚合跟踪树组合，按多尺度寿命调度，并用任意时刻有效检验决定挑战者替换。
- **Baseline** · Adaptive Random Forest 与其他流学习方法
- **Benchmark** · 分类、回归流与分段平稳理论
- **关键结果 / 消融** · 作者报告优于 ARF，并控制错误替换及晋升延迟。
- **适用条件 / 局限** · 时延结论要求变化后挑战者有优势。

**可复用机制** · 把模型池更新时间和替换证据分开设计。

<a id="paper-151118"></a>

## Adaptive Realizable Regression from Two Online Learners

[官方论文页](https://neurips.cc/virtual/2026/poster/151118) · [作者来源](https://openreview.net/forum?id=crQTD0yWpW)

- **问题 / 瓶颈** · 可实现回归既想利用低噪声也想保留最坏情形保证。
- **核心创新 / 方法** · 用两个在线学习器分别优化学习到的损失及其估计误差。
- **Baseline** · 最坏情形慢率
- **Benchmark** · 独立同分布、可数可实现函数类的绝对损失
- **关键结果 / 消融** · 先验依赖二阶界，有限类另有数据可验证界。
- **适用条件 / 局限** · 需要目标条件均值在函数类内，扩展损失有条件。

**可复用机制** · 把损失估计误差也交给在线学习器，并用先验编码结构。

<a id="paper-150739"></a>

## Adaptive Residual Quantization for Memory-Efficient Temporal Action Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/150739) · [作者来源](https://openreview.net/forum?id=fkjPOMuoxA)

- **问题 / 瓶颈** · 增量动作分割需保留大规模帧特征。
- **核心创新 / 方法** · 用无标签自适应残差量化 VAE 存储可供回放的帧表示。
- **Baseline** · 逐帧特征库及回放、凝缩方法
- **Benchmark** · Breakfast、ASFormer、I3D 和 DINOv3 特征
- **关键结果 / 消融** · I3D 原库 28 GB 降至 10 MB，监督分割 Edit 71.5、F1@50 为 51.2。
- **适用条件 / 局限** · 压缩后稀有细节的保留率待核。

**可复用机制** · 以任务指标而非仅重建误差验证无标签量化回放。

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

<a id="paper-149603"></a>

## Adaptive Scheduling Pipeline For Multi-Instance Asynchronous Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149603) · [作者来源](https://openreview.net/forum?id=oskhumpV2y)

- **问题 / 瓶颈** · 长度差异和队列排序导致 rollout 空闲。
- **核心创新 / 方法** · 以队列感知统一调度 padding、长尾和排序空泡，保持更新滞后上界。
- **Baseline** · MindSpeed-RL、verl
- **Benchmark** · LLM 异步后训练吞吐、迭代时间和收敛
- **关键结果 / 消融** · 端到端最高 3.22 倍，迭代缩短最高 76%。
- **适用条件 / 局限** · 收益随长度和算力配置而变。

**可复用机制** · 调度异步生成时同时记录填充、尾部和队列空泡。

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

<a id="paper-155450"></a>

## Adaptive Target-Charging with Privacy Filters and Individual Accounting

[官方论文页](https://neurips.cc/virtual/2026/poster/155450) · [作者来源](https://openreview.net/forum?id=5Vy5nPvzlg)

- **问题 / 瓶颈** · 目标计费难和任意时刻及个体过滤统一。
- **核心创新 / 方法** · 用直接随机占优给出模块化目标计费分析，并接入近似 Rényi DP 过滤。
- **Baseline** · 既有基于模拟的目标计费分析
- **Benchmark** · 任意时刻理论保证与 W3C Attribution 启发评测
- **关键结果 / 消融** · 作者报告更紧界且支持个体级计费。
- **适用条件 / 局限** · 依赖基础机制和会计条件。

**可复用机制** · 监测稀少显著偏差时用个体过滤控制可继续查询的隐私预算。

<a id="paper-148727"></a>

## Adaptive Test Case Discovery for LLM-Assisted Decision Making in High-Stakes Domains

[官方论文页](https://neurips.cc/virtual/2026/poster/148727) · [作者来源](https://openreview.net/forum?id=vWITPJYgBo)

- **问题 / 瓶颈** · 固定测试难覆盖不同失效形式，随机搜索浪费样本。
- **核心创新 / 方法** · 用流模型作代理，以自适应实验设计兼顾困难样本及多样探索。
- **Baseline** · 固定或非自适应场景设计，具体名称待核
- **Benchmark** · 贷款审批、新闻预测与灾害资源分配的辅助决策模拟
- **关键结果 / 消融** · 作者报告能发现符合目标的困难场景并保持覆盖。
- **适用条件 / 局限** · 需要可衡量测试目标，评测结果不能直接替代部署验证。

**可复用机制** · 把评测预算分配给失败率及多样性均有价值的测试场景。

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

<a id="paper-151962"></a>

## AdapToPASS: Ambiguity-aware Adaptive Spherical Transformer for Panoramic Semantic Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/151962) · [作者来源](https://openreview.net/forum?id=WWQOepiVLd)

- **问题 / 瓶颈** · 任意相机姿态破坏固定球面参考。
- **核心创新 / 方法** · 球面 Transformer 按局部边界和几何歧义适配表示。
- **Baseline** · 球面分割方法和紧凑模型
- **Benchmark** · Stanford2D3D、WildPASS 未见球面变换下 mIoU
- **关键结果 / 消融** · 相对次优方法分别提升 13.38% 和 18.77%。
- **适用条件 / 局限** · 真机持续视角变化和各组件作用待核。

**可复用机制** · 把未见球面变换单列为分割鲁棒性测试。

<a id="paper-155823"></a>

## ADA: Resolving Attribution Ambiguity in End-to-End Power System Dispatch via Two-Time-Scale Stochastic Approximation

[官方论文页](https://neurips.cc/virtual/2026/poster/155823) · [作者来源](https://openreview.net/forum?id=2bynWlZtFd)

- **问题 / 瓶颈** · 模型设错和求解错误混在同一反思反馈中。
- **核心创新 / 方法** · 快环澄清约束并选求解器，慢环依评估更新建模可行域。
- **Baseline** · 电力调度基线，名称待核
- **Benchmark** · L2RPN 模糊需求与可再生能源动态
- **关键结果 / 消融** · 报告优于基线；两时间尺度假设下有局部跟踪保证。
- **适用条件 / 局限** · 依赖可验证调度约束以及反馈质量。

**可复用机制** · 让建模反馈慢于求解决策，分开记录模型与执行错误。

<a id="paper-154534"></a>

## AdaSRU: Adaptive Source-Free Recommendation Unlearning via Gradient-Constrained Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154534) · [作者来源](https://openreview.net/forum?id=CsOU0pWrTZ)

- **问题 / 瓶颈** · 拿不到剩余训练数据，难直接测遗忘后的推荐损失。
- **核心创新 / 方法** · 估计剩余效用梯度，并给遗忘更新加自适应梯度约束。
- **Baseline** · 既有推荐遗忘方法
- **Benchmark** · 三个真实数据集，遗忘与推荐效用
- **关键结果 / 消融** · 报告较好折衷，并给近似 Pareto 驻点保证。
- **适用条件 / 局限** · 依赖代理梯度质量；抽样细节待核。

**可复用机制** · 若无法读取保留数据，用代理效用梯度约束遗忘步并检查偏差。

<a id="paper-155866"></a>

## AdaST: Adaptive Coupling for Spatial-Temporal Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/155866) · [作者来源](https://openreview.net/forum?id=2IWnVy1qoe)

- **问题 / 瓶颈** · 统一强耦合假设会把弱空间关联当成预测依据。
- **核心创新 / 方法** · 专家分解不同耦合成分，再由相关性驱动重组。
- **Baseline** · 主流时空预测模型
- **Benchmark** · 时空预测基准，名称与误差指标待核
- **关键结果 / 消融** · 作者报告优于所比模型。
- **适用条件 / 局限** · 耦合分解可辨识性待核。

**可复用机制** · 按空间及时间主导程度分组报告预测误差。

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

<a id="paper-153118"></a>

## AdaTree: Serving-Aware Adaptive Tree Construction for Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/153118) · [作者来源](https://openreview.net/forum?id=NnEEkVzU8t)

- **问题 / 瓶颈** · 静态候选树在不同请求负载下效率不稳定。
- **核心创新 / 方法** · 预测树配置的执行时间和验证通过长度，再选择效率最高者。
- **Baseline** · 链式和静态树式推测解码
- **Benchmark** · 不同到达率及请求特征的线上服务条件
- **关键结果 / 消融** · 报告持续优于两个基线，数值待核。
- **适用条件 / 局限** · 需要针对硬件和负载拟合性能预测。

**可复用机制** · 按负载选择草稿树配置并记录尾延迟与吞吐。

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

<a id="paper-150602"></a>

## AdDirector: Anchored Guidance for Generating Camera-Controllable Advertisement Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/150602) · [作者来源](https://openreview.net/forum?id=guwdwpOuYH)

- **问题 / 瓶颈** · 语义镜头指令弱约束运动，参考商品外观易漂移。
- **核心创新 / 方法** · 以结构化锚引导镜头，并以底座潜轨迹作边界条件的时间正则。
- **Baseline** · 既有参考到视频和显式运动条件方法
- **Benchmark** · 广告生成的镜头控制、外观一致和时空连贯
- **关键结果 / 消融** · 报告三项改善，具体数值待核。
- **适用条件 / 局限** · 摘要证据限广告场景，两模块作用待核。

**可复用机制** · 控制镜头时把运动锚与外观保持约束分开验证。

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

<a id="paper-148580"></a>

## A Deep Learning Framework for Scalar-on-Function Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148580) · [作者来源](https://openreview.net/forum?id=wkb5E1ietO)

- **问题 / 瓶颈** · 不规则网格采样的函数自变量难直接送入网络。
- **核心创新 / 方法** · 把轨迹变成有限基系数，再以普通或瓶颈网络匹配函数结构。
- **Baseline** · 对应的 minimax 速率
- **Benchmark** · 理论超额风险，分统计、截断、离散、近似
- **关键结果 / 消融** · 连续函数或多指标结构下得到近 minimax 速率。
- **适用条件 / 局限** · 要求相应函数正则性及有效近似基。

**可复用机制** · 采样曲线做回归时分别检查离散网格误差和截断误差。

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
