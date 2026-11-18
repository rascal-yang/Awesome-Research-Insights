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
