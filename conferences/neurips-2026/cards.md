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

<a id="paper-139592"></a>

## A Diagnostic Benchmark for Layered Layout and Template-Variant Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139592) · [作者来源](https://openreview.net/forum?id=GVMikNSGQx)

- **问题 / 瓶颈** · 扁平布局遗漏结构
- **核心创新 / 方法** · 使用真实层级和模板族设计理解与生成任务
- **Baseline** · 前沿视觉语言模型及字体 Jaccard
- **Benchmark** · GDB 的 1,148 个模板
- **关键结果 / 消融** · 层序能力与其他空间能力分离，字体基线在模板匹配可持平
- **适用条件 / 局限** · 模板覆盖边界待核

**可复用机制** · 按图层关系及模板变体分别测泛化

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

<a id="paper-150412"></a>

## ADIS-Law: Unified Scaling Laws for Annealing-Phase Domain Injection in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150412) · [作者来源](https://openreview.net/forum?id=iEWLc5YXWC)

- **问题 / 瓶颈** · 独立扫描难预测晚期领域注入
- **核心创新 / 方法** · 分开建模通用域遗忘恢复与目标域幂律适应
- **Baseline** · 未具名既有缩放规律
- **Benchmark** · 预算及参数规模外推
- **关键结果 / 消融** · 轨迹相关 0.947，尾部损失相对误差低于 5%
- **适用条件 / 局限** · 依赖拟合分布

**可复用机制** · 小规模联合扫描后验证规模外推

<a id="paper-149942"></a>

## A Distribution Mapping Approach to Counterfactually Fair Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149942) · [作者来源](https://openreview.net/forum?id=m2ZnEPnMy0)

- **问题 / 瓶颈** · 序列决策可累积群体差异
- **核心创新 / 方法** · 逐步映射状态与奖励的反事实分布
- **Baseline** · 常见加性反事实假设
- **Benchmark** · 数值实验及数字健康干预数据
- **关键结果 / 消融** · 给出逐步不公平和长期次优上界
- **适用条件 / 局限** · 要求因果及正规性假设

**可复用机制** · 分开测反事实校正与策略训练的影响

<a id="paper-150097"></a>

## AdKnob: Ad Intensity Control and Labeling for LLM-Native Advertising

[官方论文页](https://neurips.cc/virtual/2026/poster/150097) · [作者来源](https://openreview.net/forum?id=kilXcw3jhS)

- **问题 / 瓶颈** · 强度无法细调且难识别受控片段
- **核心创新 / 方法** · 以无预训练关联的控制 token 配合 DPO，并用注意力归因识别段落
- **Baseline** · 现有强度与标注方法
- **Benchmark** · MI-KnobSet、六个模型及人工评估
- **关键结果 / 消融** · 报告强度更均匀且人工偏好最高 89.6%
- **适用条件 / 局限** · 归因忠实性待核

**可复用机制** · 对控制等级测试单调性及输出归因

<a id="paper-150885"></a>

## ADKV: A Low-Overhead Adaptive Delta Quantization for KV Cache in LLM Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/150885) · [作者来源](https://openreview.net/forum?id=eg0RKFy1ZG)

- **问题 / 瓶颈** · RoPE 后的离群通道随时间漂移
- **核心创新 / 方法** · 逐通道 EMA 跟踪零点与尺度并增量编码
- **Baseline** · 静态分组量化
- **Benchmark** · 生成与长上下文
- **关键结果 / 消融** · 元数据减少约 12.8 倍且精度相当
- **适用条件 / 局限** · 算子收益依赖硬件

**可复用机制** · 分开测元数据、注意力误差和解码速度

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

<a id="paper-152790"></a>

## A Doubly Smoothed Decentralized Stochastic Minimax Optimization Algorithm

[官方论文页](https://neurips.cc/virtual/2026/poster/152790) · [作者来源](https://openreview.net/forum?id=QJwveeEv8G)

- **问题 / 瓶颈** · 异尺度步长难调
- **核心创新 / 方法** · 两边用平滑梯度并管理辅助变量通信
- **Baseline** · 异尺度随机极小极大方法
- **Benchmark** · 非凸 PL 分析及实验
- **关键结果 / 消融** · 条件数项达到 κ 的 3/2 次方
- **适用条件 / 局限** · 理论依赖 PL 条件

**可复用机制** · 固定通信预算比较双平滑与单平滑

<a id="paper-152835"></a>

## AdpSplit: Error-Driven Adaptive Splitting for Faster Geometry Discovery in 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/152835) · [作者来源](https://openreview.net/forum?id=Q3uOxL1oc9)

- **问题 / 瓶颈** · 固定二分限制少轮次训练
- **核心创新 / 方法** · 用像素 L1 误差统计选子高斯数及初始化
- **Baseline** · 标准二分及 FastGS
- **Benchmark** · MipNeRF360、Deep-Blending、Tanks & Temples
- **关键结果 / 消融** · 训练节约 9.2%–22.3%
- **适用条件 / 局限** · 取决于误差定位

**可复用机制** · 同等画质下测增密轮次和总时长

<a id="paper-139508"></a>

## AdShot: Benchmarking Multimodal Large Language Models for Video Advertisement Clipping

[官方论文页](https://neurips.cc/virtual/2026/poster/139508) · [作者来源](https://openreview.net/forum?id=LdyT9DvTWB)

- **问题 / 瓶颈** · 镜头匹配不能反映剪辑预算
- **核心创新 / 方法** · 以专业长短广告对比镜头选择及内容偏差
- **Baseline** · 13 个视频和 2 个音视频模型
- **Benchmark** · 823 对广告的精确率、召回及长度误差
- **关键结果 / 消融** · 平均长度绝对误差 5.39 秒，常过长
- **适用条件 / 局限** · 广告领域证据

**可复用机制** · 将预算违约与内容遗漏分开统计

<a id="paper-151216"></a>

## A Dual-Domain Vision Transformer with Spectral Positional Bias

[官方论文页](https://neurips.cc/virtual/2026/poster/151216) · [作者来源](https://openreview.net/forum?id=c4AamFDDmb)

- **问题 / 瓶颈** · 空间位置表插值改变结构
- **核心创新 / 方法** · 以频域参数表示平移等变偏置
- **Baseline** · Swin 相对位置表与无偏置
- **Benchmark** · ImageNet-1K
- **关键结果 / 消融** · 较 Swin 偏置提升 1.98 个百分点
- **适用条件 / 局限** · 适用网格与预算待核

**可复用机制** · 固定骨干测换网格后的精度与参数量

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

<a id="paper-153231"></a>

## Advancing Affordance-Grounded Creative Tool Use in Large Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153231) · [作者来源](https://openreview.net/forum?id=Mo5RsO1diV)

- **问题 / 瓶颈** · 模型会漏检关键部件并编造属性
- **核心创新 / 方法** · 以可供性知识库构造偏好对并用 DPO 对齐
- **Baseline** · 未对齐模型
- **Benchmark** · MM-CreativityBench
- **关键结果 / 消融** · 作者报告实体、部件选择改善与幻觉减少
- **适用条件 / 局限** · 依赖知识库覆盖

**可复用机制** · 分别测实体检索、部件定位与用途推理

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

<a id="paper-152023"></a>

## Advancing Narrative Long Video Generation via Training-Free Identity-Aware Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/152023) · [作者来源](https://openreview.net/forum?id=W66Ni14uAk)

- **问题 / 瓶颈** · 仅相似度检索可造成身份漂移
- **核心创新 / 方法** · 以显式实体跟踪接入免训练记忆及异步验证
- **Baseline** · 既有长视频生成
- **Benchmark** · NarraStream-Bench 的 324 个脚本
- **关键结果 / 消融** · 较最强对照高 2.56 分，60 秒设置快 1.39 倍
- **适用条件 / 局限** · 依赖身份检索

**可复用机制** · 按实体重新出现的间隔分层评估

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

<a id="paper-153887"></a>

## Adversarial Attack and Defense for Machine Learning in Statistical Physics

[官方论文页](https://neurips.cc/virtual/2026/poster/153887) · [作者来源](https://openreview.net/forum?id=I0iY7DbMc6)

- **问题 / 瓶颈** · 科学敏感性会放大输入误差
- **核心创新 / 方法** · 对局部函数变差施加正则
- **Baseline** · 常规学习及摘要未具名对照
- **Benchmark** · 统计物理模型理论与实验
- **关键结果 / 消融** · 作者报告降低误差影响
- **适用条件 / 局限** · 依赖局部物理邻域定义

**可复用机制** · 同时记录稳健性与正常科学误差

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

<a id="paper-154285"></a>

## Adversarially Attacking Symbolic Vocabulary Vulnerabilities In LLM Planners

[官方论文页](https://neurips.cc/virtual/2026/poster/154285) · [作者来源](https://openreview.net/forum?id=Exn9wjDvOI)

- **问题 / 瓶颈** · 熟悉的名称可能充当表面捷径
- **核心创新 / 方法** · 在等价任务语义下用不同命名测试规划并区分理解与求解
- **Baseline** · 基础规划模型及既有鲁棒框架
- **Benchmark** · 符号规划任务及成功率
- **关键结果 / 消融** · 作者报告部分设置表现大幅降低
- **适用条件 / 局限** · 改名应保持语义等价

**可复用机制** · 把符号不变性加入独立回归评测

<a id="paper-154942"></a>

## Adversary-Robust Learning from Fully Asynchronous Directional Derivative Estimates

[官方论文页](https://neurips.cc/virtual/2026/poster/154942) · [作者来源](https://openreview.net/forum?id=9lsYgXnywJ)

- **问题 / 瓶颈** · 同步聚合阻碍异步学习
- **核心创新 / 方法** · 采用符号投影及双时间尺度去偏
- **Baseline** · 鲁棒聚合方法
- **Benchmark** · 非凸收敛分析及 MNIST
- **关键结果 / 消融** · 报告精度及墙钟耗时优于比较方法
- **适用条件 / 局限** · 网络与参与方假设待核

**可复用机制** · 固定训练预算同时测墙钟与收敛

<a id="paper-150552"></a>

## AdvJudge-Zero: Binary Decision Flips in LLM-as-a-Judge via Adversarial Control Tokens

[官方论文页](https://neurips.cc/virtual/2026/poster/150552) · [作者来源](https://openreview.net/forum?id=hIXruOAir7)

- **问题 / 瓶颈** · 单一采样策略难以泛化到不同裁判
- **核心创新 / 方法** · 用分层样本构建防护微调并评估跨模型检验
- **Baseline** · 未防护与朴素抽样微调
- **Benchmark** · MATH、GSM8K 及模型族迁移
- **关键结果 / 消融** · 摘要报告分层覆盖比池大小更关键，且减少训练中裁判失稳
- **适用条件 / 局限** · 受分类体系和任务范围限制

**可复用机制** · 固定训练量对照随机与失败类型分层抽样

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

<a id="paper-151518"></a>

## A Dynamic Decomposition Strategy for the MOEA/D With Proven Performance Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/151518) · [作者来源](https://openreview.net/forum?id=a3xSiMutbk)

- **问题 / 瓶颈** · 固定分解难覆盖 Pareto 前沿
- **核心创新 / 方法** · 以自调整分解处理离散双目标
- **Baseline** · 经典固定分解 MOEA/D
- **Benchmark** · 单调扭曲 LOTZ
- **关键结果 / 消融** · 期望 O(n^4) 次评估覆盖所设问题
- **适用条件 / 局限** · 仅证明特定问题族

**可复用机制** · 报告覆盖均匀性及达到全前沿的预算

<a id="paper-155172"></a>

## AEGIS: Adaptive Efficient Generative Inference Scheduling for Structured Latent Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155172) · [作者来源](https://openreview.net/forum?id=7kUytwtf6g)

- **问题 / 瓶颈** · 固定刷新不能适应轨迹差异
- **核心创新 / 方法** · 在线跟踪难度及修正欠量并分配跳过和刷新配额
- **Baseline** · 固定开环缓存计划
- **Benchmark** · 结构潜变量生成
- **关键结果 / 消融** · 作者报告速度质量折衷改善并给复用漂移上界
- **适用条件 / 局限** · 具体模型和阈值待核

**可复用机制** · 固定质量要求下对照自适应与固定计划

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

<a id="paper-148730"></a>

## Aegis: Generative Gradient Masking for Privacy-Preserving Medical Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148730) · [作者来源](https://openreview.net/forum?id=vUlQnQztWO)

- **问题 / 瓶颈** · 常见梯度扰动会损伤任务精度
- **核心创新 / 方法** · 让共享更新包含来自本地任务相关合成数据的掩蔽梯度
- **Baseline** · 梯度扰动及不掩蔽对照
- **Benchmark** · 医疗联邦训练的隐私与任务效用
- **关键结果 / 消融** · 作者报告支持防护效果并给收敛分析
- **适用条件 / 局限** · 需审计模拟威胁覆盖与合成偏差

**可复用机制** · 固定任务精度时比较防护成功与成本

<a id="paper-154854"></a>

## AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154854) · [作者来源](https://openreview.net/forum?id=AOIuq1ld4R)

- **问题 / 瓶颈** · token 级熵难对应环境动作
- **核心创新 / 方法** · 以响应级不确定性重缩放优势
- **Baseline** · 稀疏结果奖励策略与额外监督方案
- **Benchmark** · ALFWorld、WebShop 等
- **关键结果 / 消融** · 具体幅度待全文核实
- **适用条件 / 局限** · 结果取决于响应作为有效动作的设定

**可复用机制** · 同任务比较 token 与响应级优势调节

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

<a id="paper-153918"></a>

## AERO: Adaptive Ensemble-Disagreement Routing for Oracle Feedback in Sample-Efficient Online RLHF

[官方论文页](https://neurips.cc/virtual/2026/poster/153918) · [作者来源](https://openreview.net/forum?id=HexbOT3aCq)

- **问题 / 瓶颈** · 均匀查询浪费可靠样本的标注
- **核心创新 / 方法** · 按集成投票熵和自适应阈值决定人工或合成偏好
- **Baseline** · 在线 DPO 与主动探索基线
- **Benchmark** · 多模型族的在线 RLHF
- **关键结果 / 消融** · 报告减少人工查询同时保持竞争表现
- **适用条件 / 局限** · 依赖分歧校准

**可复用机制** · 固定标注预算对照均匀与分歧路由

<a id="paper-153606"></a>

## AeroChem: Closed-loop Physics-Informed State Space Modeling for Long-term Chemically-Reactive Air Quality Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/153606) · [作者来源](https://openreview.net/forum?id=K8qavlGl1B)

- **问题 / 瓶颈** · 只融合最终输出难抑制长时漂移
- **核心创新 / 方法** · 物理过程与虚拟观测通过神经 Kalman 融合反复修正
- **Baseline** · 纯数据及开放环物理模型
- **Benchmark** · HanoiAir 与一项公开基准
- **关键结果 / 消融** · 作者报告长时稳定性及突变预测改善
- **适用条件 / 局限** · 需可信过程先验与观测误差模型

**可复用机制** · 固定模块对照输出融合和状态闭环

<a id="paper-154525"></a>

## AeroMosaic:Transport-Aware Multimodal Evidence Fusion for Atmospheric Pollution Risk Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/154525) · [作者来源](https://openreview.net/forum?id=Cwisp6UwX8)

- **问题 / 瓶颈** · 静态图难涵盖跨城输运
- **核心创新 / 方法** · 分角色保留数值和降水上下文，并在汇聚后沿风向图传播
- **Baseline** · 通用时序和图方法
- **Benchmark** · 六项 PM2.5 风险评测，按年份划分
- **关键结果 / 消融** · 协议内支持有向结构有用
- **适用条件 / 局限** · 无先知输入的设置尚待评估

**可复用机制** · 用时间切分对照风向动态图和静态邻接

<a id="paper-138910"></a>

## AesGI-Bench: Benchmarking and Evaluating the Aesthetic Quality of AI-Generated Images via Large Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/138910) · [作者来源](https://openreview.net/forum?id=xWaaWv8NtK)

- **问题 / 瓶颈** · 单一审美排名无法区分质量维度
- **核心创新 / 方法** · 以平局感知损失训练三个分数头
- **Baseline** · Qwen3.5 底座和常规指标
- **Benchmark** · AesGI-Bench 含 19,485 张图和 117K 对比较
- **关键结果 / 消融** · 作者报告多模态评价与人工偏好比常规指标更一致
- **适用条件 / 局限** · 受评价者组成和生成器覆盖限制

**可复用机制** · 以平局和维度标签训练后验证单样本校准

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

<a id="paper-152110"></a>

## A Faster Algorithm for the Half-Trek Criterion in Structural Causal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152110) · [作者来源](https://openreview.net/forum?id=VSTKL0A1Fz)

- **问题 / 瓶颈** · 现有半径迹判据计算随节点数快速增长
- **核心创新 / 方法** · 导出等价判据并设计随机算法
- **Baseline** · 原 HTC 算法及 SEMID
- **Benchmark** · 线性结构因果模型与稀疏图
- **关键结果 / 消融** · 一般复杂度 O(n^4)，稀疏 O(n^3)，原方法 O(n^5)
- **适用条件 / 局限** · 针对所述泛型识别判据

**可复用机制** · 按图稀疏度评估结构搜索内的判据开销

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

<a id="paper-150741"></a>

## Affine-invariant Cubic Newton with Weak Learners

[官方论文页](https://neurips.cc/virtual/2026/poster/150741) · [作者来源](https://openreview.net/forum?id=fjyjg3gCmx)

- **问题 / 瓶颈** · 既有全局分析对最坏弱边过于敏感。
- **核心创新 / 方法** · 将仿射不变三次 Newton 扩展至弱学习器，以 Hessian 范数中的方向改进确定阻尼。
- **Baseline** · 梯度正则化 Newton boosting。
- **Benchmark** · 凸优化中的收敛速率分析。
- **关键结果 / 消融** · 作者将更新化为显式步长的阻尼弱 Newton 步；定理细节待核。
- **适用条件 / 局限** · 依赖凸性及 Hessian 几何假设。

**可复用机制** · 比较基于最坏弱边的步长设计与路径平均方向质量。

<a id="paper-150970"></a>

## Affine Tracing: A New Paradigm for Probabilistic Linear Solvers

[官方论文页](https://neurips.cc/virtual/2026/poster/150970) · [作者来源](https://openreview.net/forum?id=duOAO1yJKQ)

- **问题 / 瓶颈** · 概率迭代法的人工推导拖慢应用。
- **核心创新 / 方法** · 用仿射追踪提取迭代更新并传播不确定性。
- **Baseline** · 贝叶斯概率线性求解器与概率迭代法。
- **Benchmark** · 线性系统有限步求解的不确定性及校准分析。
- **关键结果 / 消融** · 作者证明贝叶斯求解器可纳入非平稳仿射概率迭代，并给出校准结果。
- **适用条件 / 局限** · 结论适用于所定仿射迭代条件。

**可复用机制** · 为现有确定性迭代器提供概率输出时，优先检查能否追踪仿射更新。

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

<a id="paper-153107"></a>

## AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153107) · [作者来源](https://openreview.net/forum?id=NtBkgEhEww)

- **问题 / 瓶颈** · 给生成器整页图像会增加 token 并稀释证据。
- **核心创新 / 方法** · 用轻量版面分析驱动查询条件下的局部 OCR。
- **Baseline** · 整页检索、静态全文 OCR。
- **Benchmark** · 复杂视觉文档问答与检索增强生成。
- **关键结果 / 消融** · 准确率和 token 节省的具体幅度待核。
- **适用条件 / 局限** · 版面定位漏召回会抹去证据。

**可复用机制** · 对照整页及局部解析，同时记录证据召回和视觉 token。

<a id="paper-139672"></a>

## AgenticVBench: Can AI Agents Complete Real-World Video Production Tasks?

[官方论文页](https://neurips.cc/virtual/2026/poster/139672) · [作者来源](https://openreview.net/forum?id=BZpjhtRxCt)

- **问题 / 瓶颈** · 静态问答无法覆盖长程工具调用与产物质量。
- **核心创新 / 方法** · 以行业专家工作为素材构建任务，联合程序检查与专家量表。
- **Baseline** · 比较前沿 VLM 的原生和开源执行框架。
- **Benchmark** · 100 项任务、四类工作流，使用产物评分。
- **关键结果 / 消融** · 最佳所测模型得分低于 30%。
- **适用条件 / 局限** · 聚合评分受任务和工具覆盖影响。

**可复用机制** · 对复合应用将可验证产物属性与主观质量拆成两个评价通道。

<a id="paper-139376"></a>

## AgentKernelArena: Benchmarking Performance and Generalization of AI Coding Agents on GPU Kernels Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/139376) · [作者来源](https://openreview.net/forum?id=Twe3Jz6Q0V)

- **问题 / 瓶颈** · 单轮代码生成无法代表编译、剖析和迭代优化。
- **核心创新 / 方法** · 在隔离环境中执行完整优化流程，对正确性和性能设顺序门槛。
- **Baseline** · 单轮内核生成和不同代码智能体。
- **Benchmark** · 196 项 HIP 与 Triton 优化或转换任务，含未见配置。
- **关键结果 / 消融** · 摘要强调配置外推和完整流程；具体排名待核。
- **适用条件 / 局限** · 速度取决于硬件及测量配置。

**可复用机制** · 只在正确实现里比较速度，并用未见配置识别针对评测点的过拟合。

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

<a id="paper-150421"></a>

## A Frank-Wolfe Approach to Goldstein Stationarity

[官方论文页](https://neurips.cc/virtual/2026/poster/150421) · [作者来源](https://openreview.net/forum?id=iAYv33Isy5)

- **问题 / 瓶颈** · 已有非渐近方法需要预先知道问题参数。
- **核心创新 / 方法** · 修改既有算法，将其置于 Frank-Wolfe 框架。
- **Baseline** · 已有 Goldstein 驻点算法。
- **Benchmark** · 非光滑非凸 Lipschitz 函数，考察驻点复杂度。
- **关键结果 / 消融** · 作者证明序列的驻点精度单调改善，极限为 Clarke 驻点。
- **适用条件 / 局限** · 最优复杂度结论针对非随机情形。

**可复用机制** · 未知目标精度下比较固定预算算法与可随时中止的驻点序列。

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

<a id="paper-149649"></a>

## A General Filter-Enhanced Approach to Smartphone Hyperspectral Imaging

[官方论文页](https://neurips.cc/virtual/2026/poster/149649) · [作者来源](https://openreview.net/forum?id=oV35NKGER4)

- **问题 / 瓶颈** · 单幅 RGB 光谱信息有限。
- **核心创新 / 方法** · 用选定滤光片调节相机响应，将各相机 RGB 信息融合重建。
- **Baseline** · 传统单图重建。
- **Benchmark** · Doomer 的错位多 RGB 图像及高光谱真值；跨手机校准。
- **关键结果 / 消融** · 摘要报告精度和跨设备迁移改善，数值待核。
- **适用条件 / 局限** · 需要附加滤光片与设备校准。

**可复用机制** · 在逆问题中先改变传感响应，再测试融合带来的增益。

<a id="paper-148963"></a>

## A Generalized Tikhonov Layer for Interpretable-by-design Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/148963) · [作者来源](https://openreview.net/forum?id=tr3vYV6oRS)

- **问题 / 瓶颈** · 黑盒 GNN 难辨认模型依赖节点自身还是邻域。
- **核心创新 / 方法** · 以广义 Tikhonov 问题的精确解定义传播，学习节点权重和图滤波多项式。
- **Baseline** · 不透明 GNN 基线。
- **Benchmark** · 标准图分类并评估解释；数据集待核。
- **关键结果 / 消融** · 作者证明不同解释对应不同传播算子，报告分类与基线相当或更好。
- **适用条件 / 局限** · 全局感受野结论依赖支撑连通性。

**可复用机制** · 将解释变量绑定到传播算子，并检验不同解释是否真会改变输出。

<a id="paper-153150"></a>

## A general kernel framework for non-CND distance measures using $|\mathcal{D}|$-dimensional sparse landmark embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/153150) · [作者来源](https://openreview.net/forum?id=NUy4Iw41lK)

- **问题 / 瓶颈** · 直接由任意距离构核无法保证正半定。
- **核心创新 / 方法** · 用围绕训练点的紧支撑函数构造地标嵌入，再应用标准正半定核。
- **Baseline** · 特定领域距离核。
- **Benchmark** · 测地距离与 Wasserstein 距离，考察预测和不确定性。
- **关键结果 / 消融** · 作者证明构建结果正半定，并报告预测和不确定性相当或更好。
- **适用条件 / 局限** · 实际稀疏度受支撑半径和局部点密度影响。

**可复用机制** · 分开验证距离的语义表示能力与核矩阵的合法性。

<a id="paper-148966"></a>

## A Generative Model of Contextual Integrity: Appropriate vs. Inappropriate Information Sharing

[官方论文页](https://neurips.cc/virtual/2026/poster/148966) · [作者来源](https://openreview.net/forum?id=tnB9Xtbfa6)

- **问题 / 瓶颈** · 单向披露率可能惩罚正常的信息流。
- **核心创新 / 方法** · 按情境完整性构造多角色模拟和双向指标。
- **Baseline** · 不同决策逻辑、认知配置和模型。
- **Benchmark** · 情境化信息共享模拟，衡量保护和效用。
- **关键结果 / 消融** · 三个维度的受测干预均未同时弥合两侧差距。
- **适用条件 / 局限** · 依赖模拟规范覆盖，结论限所测变体。

**可复用机制** · 评估隐私控制时同时报告错误放行与错误拒绝。

<a id="paper-139513"></a>

## Agent$^2$ RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?

[官方论文页](https://neurips.cc/virtual/2026/poster/139513) · [作者来源](https://openreview.net/forum?id=LJihH43YTU)

- **问题 / 瓶颈** · 单一结果难区分工程成功和可重复学习能力。
- **核心创新 / 方法** · 在隔离工作区内提供底座、数据及评分接口，要求智能体提交训练产物。
- **Baseline** · 五类 Agent 系统和六种驱动模型。
- **Benchmark** · 三级六任务，从静态规则训练到闭环在线 RL。
- **关键结果 / 消融** · 多数成功路线依赖监督训练，互动设置跨栈波动明显。
- **适用条件 / 局限** · 单次成功不能说明稳定性，受预算与执行框架影响。

**可复用机制** · 比较研发智能体时记录训练轨迹、预算消耗与多次运行波动。

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

<a id="paper-149790"></a>

## AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent

[官方论文页](https://neurips.cc/virtual/2026/poster/149790) · [作者来源](https://openreview.net/forum?id=nIWXTEWPSb)

- **问题 / 瓶颈** · 多轮辩论提高部署成本并可能传递错误。
- **核心创新 / 方法** · 对照推理增强微调、轨迹增强及过程感知蒸馏。
- **Baseline** · 单模型与多智能体推理。
- **Benchmark** · 多模型与任务的推理和自我纠正评估；具体基准待核。
- **关键结果 / 消融** · 作者报告学生保留部分多智能体推理效果及单体推理效率，幅度待核。
- **适用条件 / 局限** · 依赖教师轨迹质量，训练代价需要单独核算。

**可复用机制** · 按同等推理预算比较在线辩论、只蒸馏结果与过程蒸馏。

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

<a id="paper-154113"></a>

## Agent MechSuits : Mechanistic Subspace Safety Steering for Multi-Turn CLI Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154113) · [作者来源](https://openreview.net/forum?id=GAW18QTdGu)

- **问题 / 瓶颈** · 外部护栏对连续行为的控制较粗
- **核心创新 / 方法** · 白盒防御在模型内部用安全子空间实施运行时干预
- **Baseline** · 外部护栏和单轮白盒安全评估
- **Benchmark** · 多轮 CLI 智能体；设置待核实
- **关键结果 / 消融** · 量化结果待查全文
- **适用条件 / 局限** · 要求白盒与在线干预权限

**可复用机制** · 把风险监测放进多轮执行过程，通过匹配基线与评测边界核验。

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

<a id="paper-148896"></a>

## AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/148896) · [作者来源](https://openreview.net/forum?id=uNezciDNHb)

- **问题 / 瓶颈** · 单轮静态评测看不到长期经验积累
- **核心创新 / 方法** · 程序化生成开放文本游戏，交错学习和推理，再诊断知识与技能
- **Baseline** · 固定任务和静态能力评测
- **Benchmark** · 长程文本游戏及诊断测试
- **关键结果 / 消融** · 摘要重点为评测协议，具体模型结果待核实
- **适用条件 / 局限** · 文本游戏向真实场景的外推需验证

**可复用机制** · 把部署中学到的知识与初始能力分开测，通过匹配基线与评测边界核验。

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

<a id="paper-148882"></a>

## AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace

[官方论文页](https://neurips.cc/virtual/2026/poster/148882) · [作者来源](https://openreview.net/forum?id=uTjkLPcoGn)

- **问题 / 瓶颈** · 串行交接与独立采样难协调多文件工作
- **核心创新 / 方法** · 在 CRDT 合并的文件系统上提供文件认领、状态、广播
- **Baseline** · 串行交接、独立采样与单智能体
- **Benchmark** · 多后端并行编码；任务与指标待核
- **关键结果 / 消融** · 摘要报告硬任务单智能体常提前退出，具体对照待核
- **适用条件 / 局限** · 需要可合并文件和协作约定

**可复用机制** · 共享状态上增加归属和进度广播，通过匹配基线与评测边界核验。

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

<a id="paper-140106"></a>

## Agent Security is a Systems Problem

[官方论文页](https://neurips.cc/virtual/2026/poster/140106) · [作者来源](https://openreview.net/forum?id=8gDb2bnWWf)

- **问题 / 瓶颈** · 模型本身可能偏离安全约束
- **核心创新 / 方法** · 将智能体模型当作不可信组件，在系统层执行不变量
- **Baseline** · 以模型鲁棒性为主的路线
- **Benchmark** · 十一例真实事件的回顾分析
- **关键结果 / 消融** · 作者以案例论证系统设计原则；无新防御量化对照
- **适用条件 / 局限** · 位置论文，充分性取决于具体系统实现

**可复用机制** · 在模型外强制权限边界，通过匹配基线与评测边界核验。

<a id="paper-139517"></a>

## Agents' Last Exam

[官方论文页](https://neurips.cc/virtual/2026/poster/139517) · [作者来源](https://openreview.net/forum?id=L1pAwhCE4k)

- **问题 / 瓶颈** · 短独立题无法衡量持续执行能力
- **核心创新 / 方法** · 按职业分类采集真实工作实例与验收任务
- **Baseline** · 短程通用基准
- **Benchmark** · 13 个行业集群、55 子领域、1490 项
- **关键结果 / 消融** · 具体模型结果待核实
- **适用条件 / 局限** · 行业覆盖和任务抽样会影响外推

**可复用机制** · 用可核验结果测整段专业工作流，通过匹配基线与评测边界核验。

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

<a id="paper-154386"></a>

## AgentTailor: Dual-Gate LLM-Assisted Re-ranking for Personalized Long-Tail Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/154386) · [作者来源](https://openreview.net/forum?id=DyNI87FtpG)

- **问题 / 瓶颈** · 相关尾项未被召回时，重排无从弥补
- **核心创新 / 方法** · 语义召回后按条件启用证据驱动的双门控长尾重排
- **Baseline** · 全局重加权和不透明排序
- **Benchmark** · 个性化长尾推荐；数据集待核
- **关键结果 / 消融** · 量化比较待核
- **适用条件 / 局限** · 依赖召回质量和证据可信度

**可复用机制** · 分开测候选召回与长尾重排，通过匹配基线与评测边界核验。

<a id="paper-152173"></a>

## Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152173) · [作者来源](https://openreview.net/forum?id=V0AFOUpwqi)

- **问题 / 瓶颈** · 独立审查每条轨迹难辨长期意图偏离
- **核心创新 / 方法** · 学习监控器，显式分析信念和目标一致性
- **Baseline** · 脚手架和集成监控
- **Benchmark** · 长程监督轨迹，数据集待核
- **关键结果 / 消融** · 量化结果待核
- **适用条件 / 局限** · 监测推断需要可核验行为证据

**可复用机制** · 从历史监测经验训练行为监督器，通过匹配基线与评测边界核验。

<a id="paper-153463"></a>

## AgentVista: Evaluating Multimodal Agent in Ultra-Challenging Realistic Visual Scenarios

[官方论文页](https://neurips.cc/virtual/2026/poster/153463) · [作者来源](https://openreview.net/forum?id=L7xyzwUody)

- **问题 / 瓶颈** · 单轮视觉推理无法评估跨模态长程工具使用
- **核心创新 / 方法** · 构造现实视觉场景与自然混合工具流程
- **Baseline** · 单轮视觉任务与单工具评测
- **Benchmark** · 七类 25 个子领域；指标待核
- **关键结果 / 消融** · 具体模型结果待核
- **适用条件 / 局限** · 真实流程覆盖及工具版本变动需考虑

**可复用机制** · 要求工具决策引用细粒度视觉证据，通过匹配基线与评测边界核验。

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

<a id="paper-149606"></a>

## A Geometric Perspective on Reward Function Updates in Inverse Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149606) · [作者来源](https://openreview.net/forum?id=oqLzCT1cus)

- **问题 / 瓶颈** · 普通奖励梯度忽视占用空间的几何
- **核心创新 / 方法** · 利用通往最优占用分布的直线路径推导奖励梯度变化
- **Baseline** · 拉格朗日原始对偶梯度法
- **Benchmark** · 逆强化学习理论；实验设置待核
- **关键结果 / 消融** · 量化结果待核
- **适用条件 / 局限** · 依赖占用空间结构和目标可利用性

**可复用机制** · 用占用分布几何构造奖励更新预条件，通过匹配基线与评测边界核验。

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

<a id="paper-148502"></a>

## Agnostic Language Identification and Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148502) · [作者来源](https://openreview.net/forum?id=xLgXRcC5Wp)

- **问题 / 瓶颈** · 已有速率建立在语言可实现性上
- **核心创新 / 方法** · 用不限制输入分布的不可知目标分别刻画识别和生成
- **Baseline** · 可实现情形已有速率
- **Benchmark** · 语言识别与生成理论
- **关键结果 / 消融** · 作者报告近紧速率
- **适用条件 / 局限** · 结论受所定义目标约束

**可复用机制** · 按数据可能不属于任何候选语言重定义目标，通过匹配基线与评测边界核验。

<a id="paper-152256"></a>

## Agnostic Online Learning with Reliable Abstention

[官方论文页](https://neurips.cc/virtual/2026/poster/152256) · [作者来源](https://openreview.net/forum?id=UPw8Xoj7Wo)

- **问题 / 瓶颈** · 输入混有随机样本和未知对抗注入
- **核心创新 / 方法** · 在允许任意标签的在线模型推导可靠弃权算法
- **Baseline** · 可实现情形及经典在线学习
- **Benchmark** · 固定与自适应对手下的理论误判和弃权
- **关键结果 / 消融** · 证明两类超额误差次线性
- **适用条件 / 局限** · 依赖注入模型与评价规则

**可复用机制** · 同时优化总误判与随机样本上的弃权，通过匹配基线与评测边界核验。

<a id="paper-154668"></a>

## A Graph Foundation Model for Unified Clustering

[官方论文页](https://neurips.cc/virtual/2026/poster/154668) · [作者来源](https://openreview.net/forum?id=BuafzhL3jU)

- **问题 / 瓶颈** · 传统聚类难跨数据图泛化
- **核心创新 / 方法** · 预训练图基础模型再进行无标签目标域适配
- **Baseline** · 逐数据集重新训练
- **Benchmark** · 跨域图聚类；数据集待核
- **关键结果 / 消融** · 量化结果待核
- **适用条件 / 局限** · 目标域仍需微调

**可复用机制** · 预训练同时兼顾节点与图级信息，通过匹配基线与评测边界核验。

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

<a id="paper-151043"></a>

## Agree to Disagree: Multimodal Autonomous Negotiation and Calibration for Entity Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151043) · [作者来源](https://openreview.net/forum?id=dPWL521xDs)

- **问题 / 瓶颈** · 刚性对齐受主导模态偏置
- **核心创新 / 方法** · 先收缩质心周围不稳定变化，再用协商注意力保留互补证据
- **Baseline** · 刚性跨模态对齐
- **Benchmark** · 多模态知识图谱补全；指标待核
- **关键结果 / 消融** · 量化结果待核
- **适用条件 / 局限** · 需能区分模态噪声与有用残差

**可复用机制** · 保留模态独有残差后再按证据融合，通过匹配基线与评测边界核验。

<a id="paper-153536"></a>

## A Grid Efficient Transport Optimization Model for the Wasserstein Barycenter Problem

[官方论文页](https://neurips.cc/virtual/2026/poster/153536) · [作者来源](https://openreview.net/forum?id=KcRsOQnPQQ)

- **问题 / 瓶颈** · 标准重心线性规划变量数为二次规模
- **核心创新 / 方法** · 固定支持网格上的紧凑 LP 同时恢复重心与运输计划
- **Baseline** · 经典 LP 与熵正则求解器
- **Benchmark** · 合成及真实数据，比较效果和求解开销
- **关键结果 / 消融** · 变量为 O(dMN^(1+1/d))，标准为 O(MN²)
- **适用条件 / 局限** · 依赖固定网格支持

**可复用机制** · 网格支持下改用精确紧凑线性规划，通过匹配基线与评测边界核验。

<a id="paper-139010"></a>

## AgriManager: A Framework and Benchmark for LLM-RL Generalization in Agricultural Management

[官方论文页](https://neurips.cc/virtual/2026/poster/139010) · [作者来源](https://openreview.net/forum?id=qpBXkIWHNU)

- **问题 / 瓶颈** · 同一接口的分布外测试遗漏结构变化
- **核心创新 / 方法** · 把接口变化定义成 schema shift，与固定接口偏移分开评估
- **Baseline** · 固定接口策略与提示条件策略
- **Benchmark** · 农业管理模拟；任务待核
- **关键结果 / 消融** · 具体结果待核
- **适用条件 / 局限** · 接口迁移结论受任务设计约束

**可复用机制** · 单独测观测、动作与奖励接口变化，通过匹配基线与评测边界核验。

<a id="paper-139411"></a>

## AgroOmni: A Large-Scale Multi-view Agricultural Dataset for Cross-Scale Multimodal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139411) · [作者来源](https://openreview.net/forum?id=SGObw0CXzN)

- **问题 / 瓶颈** · 尺度混淆可导致跨视角语义崩溃
- **核心创新 / 方法** · 对多视角农业数据按尺度与任务构建问答对照
- **Baseline** · 现有多模态模型
- **Benchmark** · AgroOmni，28.8 万问答、56 任务类别
- **关键结果 / 消融** · 报告地面尺度偏置；细分成绩待核
- **适用条件 / 局限** · 领域语义能否推广待验证

**可复用机制** · 将近景、无人机和卫星样本分层测语义稳定性，通过匹配基线与评测边界核验。

<a id="paper-149363"></a>

## A Hebbian Recurrent Neural Network Explains the Hierarchical Geometry of Sequence Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/149363) · [作者来源](https://openreview.net/forum?id=qb2jbK0rwi)

- **问题 / 瓶颈** · 单一时序指标无法区分全局与局部秩
- **核心创新 / 方法** · 用快速 Hebbian 可塑循环网络学习回忆并分析几何折叠
- **Baseline** · 对照循环模型
- **Benchmark** · 秩回忆、新绑定及分层序列泛化
- **关键结果 / 消融** · 作者报告较对照泛化改善
- **适用条件 / 局限** · 建模结果不能单独证明生物机制

**可复用机制** · 用组内与组间位置分别测试分层记忆机制，通过匹配基线与评测边界核验。

<a id="paper-153906"></a>

## A Hierarchical Tokenization Framework for Voxel-Level fMRI Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153906) · [作者来源](https://openreview.net/forum?id=Hpd9Zg6RQs)

- **问题 / 瓶颈** · 粗粒度分区会丢失细尺度信号
- **核心创新 / 方法** · 按体素组、区域和功能网络做层级 token 化
- **Baseline** · 分区和单尺度 token 化
- **Benchmark** · 静息态 fMRI 重建和下游建模
- **关键结果 / 消融** · 约 415 倍压缩，报告重建改善
- **适用条件 / 局限** · 固定图谱跨人群适用性待核

**可复用机制** · 高压缩率时保留体素局部信息与跨脑区组织，通过匹配基线与评测边界核验。

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

<a id="paper-149646"></a>

## AHPA: Adaptive Hierarchical Prior Alignment for Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/149646) · [作者来源](https://openreview.net/forum?id=oVv65Pv6Fq)

- **问题 / 瓶颈** · 固定监督粒度未反映去噪阶段差异
- **核心创新 / 方法** · 高噪对齐语义布局，低噪对齐细节结构
- **Baseline** · 固定目标或固定粒度的特征对齐
- **Benchmark** · 扩散 Transformer 训练；数据集待核
- **关键结果 / 消融** · 量化结果待核
- **适用条件 / 局限** · 分段边界需随噪声调度验证

**可复用机制** · 根据噪声水平切换对齐粒度，通过匹配基线与评测边界核验。

<a id="paper-154053"></a>

## AI Agents May Always Fall for Prompt Injections

[官方论文页](https://neurips.cc/virtual/2026/poster/154053) · [作者来源](https://openreview.net/forum?id=GYhFkdxedz)

- **问题 / 瓶颈** · 数据与指令区分不能覆盖上下文相关的违规
- **核心创新 / 方法** · 用情境完整性描述合法信息流，检验防御边界
- **Baseline** · 数据与指令分离
- **Benchmark** · 安全与普通场景对照；指标待核
- **关键结果 / 消融** · 作者论证现有防御可遗漏违规并伤害正常行为
- **适用条件 / 局限** · 论证依赖设定，部署需独立权限控制

**可复用机制** · 验证模型侧过滤之外的系统权限，通过匹配基线与评测边界核验。

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

<a id="paper-153574"></a>

## A Curvature Phase Transition Governs Coherence Penalty Efficiency Against Feature Absorption in SAEs

[官方论文页](https://neurips.cc/virtual/2026/poster/153574) · [作者来源](https://openreview.net/forum?id=KOLzZ1TkRg)

- **问题 / 瓶颈** · 稀疏自编码器原子可能吸收多个概念，而只看惩罚值无法判断能否推动特征分裂。
- **核心创新 / 方法** · 计算吸收态沿分裂方向的黎曼 Hessian，识别二次幂处的相变，并给出相关特征下的阈值。
- **Baseline** · 同族不同幂指数的相干惩罚。
- **Benchmark** · Pythia-160M 与 Gemma-2-2B 上的竞争激活 SAE，考察正则权重效率和特征吸收。
- **关键结果 / 消融** · 摘要报告实验支持理论排序，并核查吸收减少来自特征改善；细项待核。
- **适用条件 / 局限** · 结论依赖分析的吸收构型及相关性设定。

**可复用机制** · 选择表示正则项时，先检查失败态附近沿期望修复方向的曲率，再用特征级指标检验修复。

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

<a id="paper-156034"></a>

## 3D Molecule Generation from Rigid Motifs via $\mathrm{SE}(3)$ Flows

[官方论文页](https://neurips.cc/virtual/2026/poster/156034) · [作者来源](https://openreview.net/forum?id=10JJ9uxd6J)

- **问题 / 瓶颈** · 逐原子生成需要处理大量自由度。
- **核心创新 / 方法** · 把小分子表示为刚性片段，在刚体变换空间学习等变生成。
- **Baseline** · 逐原子生成方法。
- **Benchmark** · GEOM-Drugs 等，考察原子稳定性、表示大小与生成步数。
- **关键结果 / 消融** · 摘要报告生成步数减为原来的二分之一至十分之一，表示压缩 3.5 倍。
- **适用条件 / 局限** · 片段划分会影响对柔性构象的表达。

**可复用机制** · 对具有刚性局部结构的几何对象，按结构单元生成并量化表达代价。

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

<a id="paper-148925"></a>

## A Cross-Interaction Neural Architecture for Submodular Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/148925) · [作者来源](https://openreview.net/forum?id=uBVOypPlGr)

- **问题 / 瓶颈** · 成对交互项随集合规模增长，容易表现为超模。
- **核心创新 / 方法** · 用导数衰减受控的凹变换把给定单调超模函数转成次模函数，并设计多层结构。
- **Baseline** · 既有结构化次模网络，名称待核。
- **Benchmark** · 表达能力分析和实验对照，数据集待核。
- **关键结果 / 消融** · 作者给出变换条件及近似次模扩展，实验报告改善。
- **适用条件 / 局限** · 只有满足导数和交互条件时才有结构保证。

**可复用机制** · 需要成对交互又需要贪心优化时，在组合网络前检查单调次模约束。

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

<a id="paper-148195"></a>

## Action-On-Item Preference Flow: A Shared Event Schema for Predictive and Generative Personalization

[官方论文页](https://neurips.cc/virtual/2026/poster/148195) · [作者来源](https://openreview.net/forum?id=zcUo1wZa1X)

- **问题 / 瓶颈** · 不同平台动作语义不同，单一历史向量易混淆兴趣尺度。
- **核心创新 / 方法** · 用动作与对象组成正负及指令型证据，写入多时间尺度状态，再按命令读取。
- **Baseline** · 不分时序痕迹的最强方法和双示例语言模型。
- **Benchmark** · MovieLens、MIND、PENS、OpenAI-Reddit，测 MRR、nDCG 和个性化生成。
- **关键结果 / 消融** · MIND 的 MRR 与 nDCG 分别提升 10.05 和 9.01，去掉动作条件时 MRR 降 6.52。
- **适用条件 / 局限** · 需要可映射的反馈语义，跨域标签解释需校准。

**可复用机制** · 比较共享事件模式与专用编码器，并按稳定兴趣与短时意图分别评测。

<a id="paper-149076"></a>

## ActionUNet: Improving Robustness of VLA Models with Efficient Multi-scale Fine-tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/149076) · [作者来源](https://openreview.net/forum?id=t3p8yqEZl7)

- **问题 / 瓶颈** · 由粗到细的动作融合可能引入短时震荡。
- **核心创新 / 方法** · 在动作特征空间以时序 U-Net 适配，接条件 SIREN 解码并约束二阶变化。
- **Baseline** · 以 π0.5 为起点，另验证 OpenVLA-OFT。
- **Benchmark** · RoboTwin 2.0、LIBERO-Plus、真机困难任务。
- **关键结果 / 消融** · 三个设置成功率分别绝对提高 9.8、6.1、11.4 个百分点。
- **适用条件 / 局限** · 跨控制器与采样频率的稳定性待核。

**可复用机制** · 在同一骨干上同时测动作急动度和任务成功，拆分时序融合及平滑约束。

<a id="paper-150979"></a>

## Activation Functions Shape Token Synchronization in Stochastic Transformer Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/150979) · [作者来源](https://openreview.net/forum?id=do7lcGzKAH)

- **问题 / 瓶颈** · 共享噪声可能把 token 推向一致，减少表示差异。
- **核心创新 / 方法** · 在球面交互粒子近似中，使用激活对应的 NNGP 核刻画共同噪声。
- **Baseline** · 比较 ReLU 及其幂、GELU、SiLU、tanh。
- **Benchmark** · 随机 Transformer 动力系统，考察维度、离散程度和完全同步。
- **关键结果 / 消融** · 作者给出若干同步边界，并在注意力强度条件下证明 ReLU² 阻止完全塌缩。
- **适用条件 / 局限** · 属于指定的随机动力近似，真实训练模型需另验。

**可复用机制** · 比较激活时除损失外监控表示离散度，检查注意力强度是否改变结论。

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

<a id="paper-153257"></a>

## Active Corpus Selection for Training Subgraph Retrievers Using OOD Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/153257) · [作者来源](https://openreview.net/forum?id=MbIpE61lGH)

- **问题 / 瓶颈** · 查询分布变化时为候选子图反复求解代价高。
- **核心创新 / 方法** · 按查询选小规模语料候选，用一次构建的索引跨分布复用。
- **Baseline** · 六个子图检索对照，名称待核。
- **Benchmark** · 四个分子图数据集，测分布偏移后的检索准确度。
- **关键结果 / 消融** · 摘要报告一致优于对照，并给出极端类别不均衡下优先分配正例预算的理论条件。
- **适用条件 / 局限** · 类别比例和可检索到的正例覆盖限制结论。

**可复用机制** · 按标签计算代价和类别比例确定标注预算，验证可复用索引是否降低每域开销。

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

<a id="paper-152717"></a>

## Active Learning for Gaussian Process Regression Under Self-Induced Boltzmann Weights

[官方论文页](https://neurips.cc/virtual/2026/poster/152717) · [作者来源](https://openreview.net/forum?id=Qt4h1OOhOo)

- **问题 / 瓶颈** · 目标分布由待学习函数决定，归一化常数不可直接求。
- **核心创新 / 方法** · 用高斯过程代理形成自诱导加权采集函数，并比较蒙特卡洛变体。
- **Baseline** · 既有主动学习方法和 Thompson 采样变体。
- **Benchmark** · 合成与真实建模任务，考察加权预测误差。
- **关键结果 / 消融** · 提供高概率终点误差收敛与更紧的平均情形保证，摘要报告实验改善。
- **适用条件 / 局限** · 依赖高斯过程及理论条件，强错设的后果待核。

**可复用机制** · 当评价重点落在未知函数决定的区域时，统一更新响应与查询目标。

<a id="paper-154434"></a>

## Active Learning From Positive and Unlabeled Examples

[官方论文页](https://neurips.cc/virtual/2026/poster/154434) · [作者来源](https://openreview.net/forum?id=DaOrmOgOYi)

- **问题 / 瓶颈** · 查询后无反馈可能是负例，也可能是未揭示的正例。
- **核心创新 / 方法** · 建立正例经独立随机门控才揭示标签的主动学习模型。
- **Baseline** · 标准主动学习与被动正例—未标注学习为问题背景。
- **Benchmark** · 以理论标签复杂度衡量，摘要未列经验基准。
- **关键结果 / 消融** · 作者给出该反馈设定的首项理论分析，定量界待查正文。
- **适用条件 / 局限** · 依赖独立揭示假设。

**可复用机制** · 若收集系统只返回部分正反馈，建模其揭示概率，并将无反馈单独编码。

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

<a id="paper-156770"></a>

## Active Learning via Classifier Impact and Greedy Selection for Interactive Image Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/156770) · [作者来源](https://neurips.cc/virtual/2026/poster/156770)

- **问题 / 瓶颈** · 开放集小样本检索的类别不平衡使分类式选点不稳定。
- **核心创新 / 方法** · 定义分类器影响采集函数，并根据已选候选更新同一批次的选择。
- **Baseline** · 交互图像检索的现有主动学习方法。
- **Benchmark** · 以 SVM、MLP 和高斯过程做交互图像检索。
- **关键结果 / 消融** · 作者报告优于常用对照，并对高斯过程给出贪心近似保证。
- **适用条件 / 局限** · 理论保证不直接覆盖其他分类器。

**可复用机制** · 在标注预算固定时比较分类器影响贪心选择和独立批量打分。

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

<a id="paper-155769"></a>

## Actor-Accelerated Policy Dual Averaging for Reinforcement Learning in Continuous Action Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/155769) · [作者来源](https://openreview.net/forum?id=34NGCK5xuh)

- **问题 / 瓶颈** · 连续动作下每步求解 PDA 子问题昂贵。
- **核心创新 / 方法** · 用策略网络近似子问题解，并分析误差如何进入收敛界。
- **Baseline** · PPO；其余待核。
- **Benchmark** · 机器人、控制和运筹任务；名单待核。
- **关键结果 / 消融** · 报告优于 PPO，数值待核。
- **适用条件 / 局限** · 收敛依赖近似误差条件。

**可复用机制** · 把在线求解器蒸馏为 actor，再按近似误差比较时延与性能。

<a id="paper-154417"></a>

## ActWorld: From Explorable to Interactive World Model via Action-Aware Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/154417) · [作者来源](https://openreview.net/forum?id=DisAMFjByQ)

- **问题 / 瓶颈** · 只保留最近帧会丢失改变物体状态的关键画面。
- **核心创新 / 方法** · 用动作感知压缩与持久记忆保存事件更新和物体身份。
- **Baseline** · 仅导航的世界模型。
- **Benchmark** · 滚动生成中的视点控制和交互保真。
- **关键结果 / 消融** · 报告交互改善且视点控制保持，数值待核。
- **适用条件 / 局限** · 依赖交互数据标注与事件识别。

**可复用机制** · 在固定记忆容量下对照事件驱动保留与按时间淘汰。

<a id="paper-156754"></a>

## AdaCubic: An Adaptive Cubic Regularization Optimizer for Deep Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/156754) · [作者来源](https://openreview.net/forum?id=pZBQ7J37lk)

- **问题 / 瓶颈** · 固定权重难兼顾曲率和步长。
- **核心创新 / 方法** · 以带三次约束的辅助问题更新权重，并用 Hutchinson 近似曲率。
- **Baseline** · 常用深度优化器，名称待核。
- **Benchmark** · 视觉、语言和信号处理任务。
- **关键结果 / 消融** · 固定超参下报告优于或接近对照，数值待核。
- **适用条件 / 局限** · 保证是局部的，曲率估计开销待核。

**可复用机制** · 在固定调参预算下对照自适应三次正则与固定权重。

<a id="paper-149766"></a>

## AffectGPT-RL: Revealing Roles of Reinforcement Learning in Open-Vocabulary Emotion Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/149766) · [作者来源](https://openreview.net/forum?id=nUblZoo4wF)

- **问题 / 瓶颈** · 词元损失与开放词表情绪指标不一致。
- **核心创新 / 方法** · 通过 RL 优化任务奖励，并对照推理和奖励选择。
- **Baseline** · 词元损失训练及不同奖励，具名方法待核。
- **Benchmark** · 开放词表多模态情绪识别及 MER-UniBench。
- **关键结果 / 消融** · 报告开放词表和基础情绪识别改善，数值待核。
- **适用条件 / 局限** · 依赖情绪轮定义，跨数据集稳定性待核。

**可复用机制** · 评价指标不可微时，对照策略奖励和词元损失，隔离推理和奖励贡献。

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

<a id="paper-139450"></a>

## AgentCollabBench: Diagnosing When Good Agents Make Bad Collaborators

[官方论文页](https://neurips.cc/virtual/2026/poster/139450) · [作者来源](https://openreview.net/forum?id=P9qqypDzuC)

- **问题 / 瓶颈** · 终局正确可能掩盖中间约束丢失。
- **核心创新 / 方法** · 构造隔离约束衰减、错误信念、任务串扰及追踪信息的诊断任务。
- **Baseline** · 四种语言模型与不同通信拓扑。
- **Benchmark** · 900 个经人工核验的软件与数据任务。
- **关键结果 / 消融** · 拓扑解释 7%–40% 的多跳信息留存变异。
- **适用条件 / 局限** · 结果依赖所测拓扑和任务，不能直接外推。

**可复用机制** · 单独测合流节点是否保留少数分支的约束。

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

<a id="paper-151949"></a>

## AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/151949) · [作者来源](https://openreview.net/forum?id=Wdc59fvT3R)

- **问题 / 瓶颈** · 事后归因无法阻止错误传播。
- **核心创新 / 方法** · 用相邻安全和失败前缀学习风险边界，再训练错误内容、位置和责任者定位。
- **Baseline** · GPT-4.1 和 DeepSeek-V4-Pro 等审计对照。
- **Benchmark** · AFTraj-2K 和 Who&When。
- **关键结果 / 消融** · 报告最高 19.9% 性能提升及约三倍定位误差改善。
- **适用条件 / 局限** · 前缀标注依赖评审一致性。

**可复用机制** · 对审计器同时记录定位误差和触发时机。

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

<a id="paper-139240"></a>

## AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Scientific Question Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/139240) · [作者来源](https://openreview.net/forum?id=cqWV4VfaEw)

- **问题 / 瓶颈** · 总准确率掩盖工具和预算管理差异。
- **核心创新 / 方法** · 在固定七工具沙箱拆解检索、综合、工具调用和资源管理。
- **Baseline** · 19 个模型。
- **Benchmark** · 1011 道科学多跳选择题。
- **关键结果 / 消融** · 两个 Claude 版本总分差不足一点但检索与综合优势相反。
- **适用条件 / 局限** · 结论依赖选择题、工具和预算设定。

**可复用机制** · 部署前用分项诊断选模型，避免按总分替代组件评估。

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

<a id="paper-148892"></a>

## Agentic Geometry Problem Solving via Human-like Parallel Bidirectional Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148892) · [作者来源](https://openreview.net/forum?id=uPyHEd0byJ)

- **问题 / 瓶颈** · 仅单向搜索的形式几何求解空间大。
- **核心创新 / 方法** · 语言模型规划并反思，符号求解器验证前向应用和反向分解。
- **Baseline** · 已有形式几何方法，名称待核。
- **Benchmark** · FormalGeo7K 求解准确率。
- **关键结果 / 消融** · 报告准确率 95.8%。
- **适用条件 / 局限** · 依赖可形式化的定理与符号环境。

**可复用机制** · 当任务有可逆规则，分别测正向构造、反向拆解及组合搜索。

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

<a id="paper-138948"></a>

## Agentick: A Unified Benchmark for General Sequential Decision-Making Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/138948) · [作者来源](https://openreview.net/forum?id=uQfa6HnJkS)

- **问题 / 瓶颈** · 不同代理范式缺少直接可比环境。
- **核心创新 / 方法** · 统一 Gymnasium 接口，以 oracle 策略进行归一化评价。
- **Baseline** · RL、LLM、VLM、混合及人类配置。
- **Benchmark** · 37 任务、27 配置及逾 90000 回合。
- **关键结果 / 消融** · PPO 擅长规划和多代理，ASCII 在所测条件优于自然语言。
- **适用条件 / 局限** · 观测格式的结论依赖程序化任务。

**可复用机制** · 固定任务和动作空间，只切换观察格式测代理差异。

<a id="paper-149499"></a>

## Agentic Multi-Turn Reasoning: A Fairness Approach

[官方论文页](https://neurips.cc/virtual/2026/poster/149499) · [作者来源](https://openreview.net/forum?id=pgIzfBqw2D)

- **问题 / 瓶颈** · 末端监督稀疏且常见模式支配学习。
- **核心创新 / 方法** · 公平多级偏好目标在多个层级优化并处理数据失衡。
- **Baseline** · 多级偏好框架及现有推理方法，名称待核。
- **Benchmark** · 多轮代理推理基准，名称待核。
- **关键结果 / 消融** · 报告理论分析与领先实证，独立消融待核。
- **适用条件 / 局限** · 摘要没有描述具体层级和权重算法。

**可复用机制** · 报告数据频次分组指标并消融多级和均衡目标。

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

<a id="paper-149555"></a>

## Agentic Video Editing from Underspecified Requests

[官方论文页](https://neurips.cc/virtual/2026/poster/149555) · [作者来源](https://openreview.net/forum?id=pGPKhPBqR0)

- **问题 / 瓶颈** · 真实请求常缺参考和空间目标。
- **核心创新 / 方法** · 工具增强 VLM 生成结构化编辑计划，并学习参考选择及工具偏好。
- **Baseline** · 纯文本基线及兼容冻结编辑器。
- **Benchmark** · EditVerse-Bench、OpenVE-Bench、AgentEdit-Bench。
- **关键结果 / 消融** · 摘要报告优于纯文本且可迁移到冻结编辑器。
- **适用条件 / 局限** · 依赖编辑器暴露相应条件，细项待核。

**可复用机制** · 固定编辑器比较直接文本与结构化条件补全。

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

<a id="paper-139045"></a>

## AI Construct Lexis: An Ontology of the Hidden Assumptions in AI Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139045) · [作者来源](https://openreview.net/forum?id=oEjiodkMgU)

- **问题 / 瓶颈** · 模型分数与能力概念的映射常缺证据。
- **核心创新 / 方法** · 从文献抽取概念、行为、工具与映射并建成版本化本体。
- **Baseline** · 专家标注对照；摘要未列其他流水线。
- **Benchmark** · 超过 8337 篇论文及专家抽样核对。
- **关键结果 / 消融** · 抽取 977 个概念、1694 个工具、830 个行为指标和 5900 个关系。
- **适用条件 / 局限** · 关系是文献主张，需独立效度验证。

**可复用机制** · 把能力主张对应到可观察行为和测量工具，再逐条验证映射。

<a id="paper-151011"></a>

## AI Control for Sandbagging on Fuzzy Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/151011) · [作者来源](https://openreview.net/forum?id=dbpdUpHxHF)

- **问题 / 瓶颈** · 开放式任务的弱评分可能无法反映真实质量。
- **核心创新 / 方法** · 在实验提案任务对照弱评分与可访问原论文的代理评审，并复核改进评分指令。
- **Baseline** · 原弱评分指令与改进版本。
- **Benchmark** · 近期机器学习论文衍生的实验提案。
- **关键结果 / 消融** · 观察到弱分高而代理质量低；改进评分在所测条件下更稳健。
- **适用条件 / 局限** · 代理评分不是直接真实结果，泛化待核。

**可复用机制** · 将任务评分与评分器审计分开，测高分样本中的真低质量率。

<a id="paper-140079"></a>

## AI Evaluation Should Require Standardized Item-Level Data Releases

[官方论文页](https://neurips.cc/virtual/2026/poster/140079) · [作者来源](https://openreview.net/forum?id=MTjR4BxEXy)

- **问题 / 瓶颈** · 汇总分无法定位坏题或概念错配。
- **核心创新 / 方法** · 统一逐题响应格式，构建 OpenEval 并展示题目诊断。
- **Baseline** · 以聚合分为主的评测惯例。
- **Benchmark** · 约 155k 题、10M 响应的评测档案。
- **关键结果 / 消融** · 逐题分析识别低质量条目和内部结构问题；摘要未给比例。
- **适用条件 / 局限** · 需要一致标识与可发布响应，污染仍需检查。

**可复用机制** · 在发布分数时附逐题结果以支持复核与误差分解。

<a id="paper-140017"></a>

## AI for Drug Discovery Models Often Do Not Learn as Expected and How to Diagnose These Failure Modes

[官方论文页](https://neurips.cc/virtual/2026/poster/140017) · [作者来源](https://openreview.net/forum?id=pwdkgwxCZU)

- **问题 / 瓶颈** · 标签捷径可让模型高分而丧失泛化。
- **核心创新 / 方法** · 设置只接触简化或无关信号的对照，检查其相对原模型表现。
- **Baseline** · 使用原输入的任务模型与故意错位基线。
- **Benchmark** · 多个药物发现评测案例；具名数据待核。
- **关键结果 / 消融** · 案例显示错位基线可暴露数据偏差。
- **适用条件 / 局限** · 高分是警讯，不能唯一定位原因。

**可复用机制** · 对任何表征学习任务构造不具备目标信息的对照，测试它是否仍达同等表现。

<a id="paper-138879"></a>

## AI GAMESTORE: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games

[官方论文页](https://neurips.cc/virtual/2026/poster/138879) · [作者来源](https://openreview.net/forum?id=zFv5xwDcsy)

- **问题 / 瓶颈** · 固定窄基准易饱和。
- **核心创新 / 方法** · 从平台游戏构建容器化环境并由人审核。
- **Baseline** · 七个 VLM 与人类平均表现。
- **Benchmark** · 100 个游戏的短时试玩。
- **关键结果 / 消融** · 最佳模型在多数游戏不到人类平均得分一成。
- **适用条件 / 局限** · 短时表现不能代表长期学习，抽样依赖榜单。

**可复用机制** · 持续更换环境任务并匹配体验预算，避免把重复练习当泛化。

<a id="paper-140027"></a>

## AI-Generated Content Should Be Evaluated by Its Substance, Not Its Source

[官方论文页](https://neurips.cc/virtual/2026/poster/140027) · [作者来源](https://openreview.net/forum?id=jXobTKM5f0)

- **问题 / 瓶颈** · 来源标签不能证明可靠性，文风变化也会破坏检测。
- **核心创新 / 方法** · 通过小规模复现和文献分析比较偏移前后检测表现。
- **Baseline** · 同一检测器的原始与偏移条件。
- **Benchmark** · 文本来源检测，指标 AUROC。
- **关键结果 / 消融** · 文中示例从 0.999 降至 0.56。
- **适用条件 / 局限** · 示例范围有限，未验证通用事实检测器。

**可复用机制** · 对来源分类器做文风留出评估，并独立测错误事实的检出率。

<a id="paper-140009"></a>

## AI Governance Should Prioritize Control and Knowledge Boundaries Over Limiting Intelligence

[官方论文页](https://neurips.cc/virtual/2026/poster/140009) · [作者来源](https://openreview.net/forum?id=tJJOzoeeQH)

- **问题 / 瓶颈** · 以单一智能指标预测实际影响会遗漏权限及信息约束。
- **核心创新 / 方法** · 拆分能力路径，并以理论界和随机仿真检查瓶颈。
- **Baseline** · 跨不同搜索能力与授权条件对照。
- **Benchmark** · 六组 NK 景观模拟。
- **关键结果 / 消融** · 分析与仿真显示知识或授权等待会限制能力增益转化。
- **适用条件 / 局限** · 简化仿真不能直接预测真实部署。

**可复用机制** · 做权限敏感性分析，区分生成计划、取得信息及真正执行三个阶段。

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

<a id="paper-155808"></a>

## AI-Mediated Communication Can Steer Collective Opinion

[官方论文页](https://neurips.cc/virtual/2026/poster/155808) · [作者来源](https://openreview.net/forum?id=2jvTv6EcKS)

- **问题 / 瓶颈** · 个人样本上的小偏差可能经网络放大。
- **核心创新 / 方法** · 结合文本编辑审计、意见动力学平衡分析和真实网络数据仿真。
- **Baseline** · 有人机中介与不同中介设置的比较。
- **Benchmark** · 多模型文本编辑与网络仿真，另有 X 功能审计。
- **关键结果 / 消融** · 作者报告方向性偏差可改变集体意见平衡。
- **适用条件 / 局限** · 意见动力学采用简化假设，不能推出实际人群因果效应。

**可复用机制** · 把单步偏差审计和群体反馈模拟结合，测试中介工具的长期外部性。

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

<a id="paper-152477"></a>

## AIRA-Compose: Agentic Discovery of Neural Architectures

[官方论文页](https://neurips.cc/virtual/2026/poster/152477) · [作者来源](https://openreview.net/forum?id=SnDDQz5O4F)

- **问题 / 瓶颈** · 小模型表现不一定等价于大模型的效率前沿。
- **核心创新 / 方法** · 以注意力、MLP 与状态空间模块为组合原语，先搜索百万参数候选再预训十亿参数入选模型。
- **Baseline** · Llama 3.2、Composer 搜索替代和改版 Nemotron-2。
- **Benchmark** · 固定 token 预算的 1B 预训练与下游任务。
- **关键结果 / 消融** · 两款入选结构较 Llama 3.2 分别提高 2.4% 与 3.8%。
- **适用条件 / 局限** · 跨规模排序稳定性及搜索总成本待核。

**可复用机制** · 将小规模搜索成本和大规模重跑成本一起核算，保留固定预算对照。

<a id="paper-153593"></a>

## AirIAD: Agentic Iterative Reasoning for Industrial Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/153593) · [作者来源](https://openreview.net/forum?id=KGsOIl5BNC)

- **问题 / 瓶颈** · 单次预测会累积局部缺陷与领域描述的错配。
- **核心创新 / 方法** · 将放大和检索构成迭代证据获取，并用监督及分步策略训练强化核验。
- **Baseline** · 底座 Qwen3-VL-Instruct-4B；具名实验对照待核。
- **Benchmark** · MMAD 异常检测和细粒度诊断。
- **关键结果 / 消融** · 作者报告所测基准性能领先，量化幅度待核。
- **适用条件 / 局限** · 依赖检索知识质量与小缺陷的可观测性。

**可复用机制** · 对照只放大、只检索及交叉核验，记录错误类型和工具调用开销。

<a id="paper-154614"></a>

## AirMPA: A Meteorology-to-Pollution Adapter for Global Air Quality Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154614) · [作者来源](https://openreview.net/forum?id=CHMrEIBEZR)

- **问题 / 瓶颈** · 统一预测会把天气与污染动力学耦合。
- **核心创新 / 方法** · 以天气场、排放先验及历史污染物驱动双分支自回归污染物模型。
- **Baseline** · Aurora 与 CAMS。
- **Benchmark** · 13 种污染物、0.4° 分辨率、12 小时步长、五日预报。
- **关键结果 / 消融** · 约九成污染物和提前量组合优于 CAMS，48 小时外所有变量优于 CAMS。
- **适用条件 / 局限** · 训练气象再分析与部署预报有输入偏移。

**可复用机制** · 保持污染物模型固定，替换气象预报模块并按提前量分层比较误差。

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

<a id="paper-139194"></a>

## A Large-Scale Multi-Source Dataset Linking Hacker Community Discourse to the CVE Vulnerability Lifecycle

[官方论文页](https://neurips.cc/virtual/2026/poster/139194) · [作者来源](https://neurips.cc/virtual/2026/poster/139194)

- **问题 / 瓶颈** · 随机切分可能泄漏事件身份
- **核心创新 / 方法** · 用时间顺序与事件互斥切分区分前瞻泛化和重复识别
- **Baseline** · 摘要未给比较方法
- **Benchmark** · 跨来源实体识别和前瞻分割
- **关键结果 / 消融** · 作者提供来源捷径与泄漏诊断，定量结果待核
- **适用条件 / 局限** · 证据限所覆盖来源与时间段

**可复用机制** · 以时间和事件 ID 双重隔离验证防御性情报分类

<a id="paper-148187"></a>

## A latent control model for realistic rodent motion

[官方论文页](https://neurips.cc/virtual/2026/poster/148187) · [作者来源](https://openreview.net/forum?id=zebI1xXFB1)

- **问题 / 瓶颈** · 模仿出的虚拟动物随机探索时可能动作失真
- **核心创新 / 方法** · 变分架构分别学习控制和探索先验
- **Baseline** · 既有模仿动物控制方法，具名对照待核
- **Benchmark** · 虚拟大鼠目标行为与稀疏奖励
- **关键结果 / 消融** · 作者报告自然探索和稀疏奖励学习可兼得
- **适用条件 / 局限** · 仿真表现不能直接代表真实动物

**可复用机制** · 把控制用运动先验和随机探索先验分开

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

<a id="paper-139797"></a>

## ALETHEIA: A Multi-Frequency Eddy Current Pulsed Thermography Dataset for Neural Operator Learning in Nondestructive Testing

[官方论文页](https://neurips.cc/virtual/2026/poster/139797) · [作者来源](https://openreview.net/forum?id=3x55aqNQ9m)

- **问题 / 瓶颈** · 边界观测稀疏且有噪声，纯仿真结果外推有限
- **核心创新 / 方法** · 用同一热传播过程定义正演与表面测量反演，并加入实测校准
- **Baseline** · 多种神经算子，名称待核
- **Benchmark** · 4700 余样本、10 种频率、规则与非规则网格
- **关键结果 / 消融** · 摘要给出三项统一任务，差异结果待核
- **适用条件 / 局限** · 实测为带裂纹钢轨，材料泛化待核

**可复用机制** · 按激励频率、网格和仿真到实测拆分神经算子测试

<a id="paper-150997"></a>

## Algebraic Machine Learning: learning as computing subsets of the subdirect decomposition from Abstract Algebra

[官方论文页](https://neurips.cc/virtual/2026/poster/150997) · [作者来源](https://openreview.net/forum?id=dhg9MiFY8n)

- **问题 / 瓶颈** · 数值学习与形式约束常用不同求解流程
- **核心创新 / 方法** · 将任务编码为代数公理，以次直分解的分量子集构造模型
- **Baseline** · 验证选参的通用 MLP
- **Benchmark** · 24 个分类集及形式约束示例
- **关键结果 / 消融** · 分类准确率统计上相近，加逻辑读出后作者报告提升
- **适用条件 / 局限** · 分解的计算规模与公理编码成本待核

**可复用机制** · 用同一公理接口表示训练样本和形式约束

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

<a id="paper-151449"></a>

## Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret

[官方论文页](https://neurips.cc/virtual/2026/poster/151449) · [作者来源](https://openreview.net/forum?id=aaW5WlCQsj)

- **问题 / 瓶颈** · 持续随机调度会增加队列长度遗憾
- **核心创新 / 方法** · 先随机估计，再混合随机与 UCB，截止后转为纯 UCB
- **Baseline** · 已有随机上下文队列赌博机算法
- **Benchmark** · 固定时域终点的期望队长差
- **关键结果 / 消融** · 速率由 T^-1/4 改善至 T^-1/2，忽略对数项，并有下界
- **适用条件 / 局限** · 依赖随机上下文和队列负漂移条件

**可复用机制** · 用预设截止点停止随机探索，后段只用置信探索

<a id="paper-150980"></a>

## Algorithmic Impact Reveals the Hidden Structure of Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/150980) · [作者来源](https://openreview.net/forum?id=dnysHFYeGx)

- **问题 / 瓶颈** · 偏好聚合可能忽略参与者间的福利影响
- **核心创新 / 方法** · 以凸影响空间表示机制，用线性优化比较福利和个体约束
- **Baseline** · 不同福利机制及随机独裁
- **Benchmark** · 捐赠分配、食品分配、语言回答等真实偏好示例
- **关键结果 / 消融** · 作者展示可建模策略操纵与参与外部性
- **适用条件 / 局限** · 取决于福利和后果的可观测建模

**可复用机制** · 将群体对齐规则比较转成后果与外部性约束的优化

<a id="paper-155929"></a>

## Algorithms for Linear Equations with Min and Max Operators Under (Absolutely) Halting Condition

[官方论文页](https://neurips.cc/virtual/2026/poster/155929) · [作者来源](https://openreview.net/forum?id=1jUqq6Mfzi)

- **问题 / 瓶颈** · 经典迭代在更一般的 min/max 方程可能不收敛
- **核心创新 / 方法** · 用对角缩放证明绝对停止类值迭代收敛，并为一般类改造策略迭代
- **Baseline** · 经典值迭代与策略迭代
- **Benchmark** · 三类停止方程的理论比较
- **关键结果 / 消融** · 绝对停止时策略迭代可发散，一般停止两者均可失效
- **适用条件 / 局限** · 须核实方程所满足的停止类别

**可复用机制** · 按停止条件区分能安全使用的值迭代和策略迭代

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

<a id="paper-152960"></a>

## Align3D-AD: Cross-Modal Feature Alignment and Dual-Prompt Learning for Zero-shot 3D Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/152960) · [作者来源](https://openreview.net/forum?id=P5rO538Rjx)

- **问题 / 瓶颈** · RGB 骨干直接处理三维渲染会遇域偏移
- **核心创新 / 方法** · 用辅助类别 RGB 引导渲染表征，按语义一致性重加权并对比对齐双提示
- **Baseline** · 既有零样本三维异常方法
- **Benchmark** · MVTec3D-AD、Eyecandies、Real3D-AD
- **关键结果 / 消融** · 作者报告一对其余及跨数据集均改善
- **适用条件 / 局限** · 依赖辅助类别的 RGB 及跨域相关性

**可复用机制** · 渲染与真实 RGB 保持独立提示并进行对齐

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

<a id="paper-149664"></a>

## Align as You Couple: Learning Spatial Resolved Inference from H&E Images with Mollified Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/149664) · [作者来源](https://openreview.net/forum?id=oLyNGLsplV)

- **问题 / 瓶颈** · 组织图像与表达分布间存在耦合与覆盖差异
- **核心创新 / 方法** · 从输入图像构造条件先验，并平滑耦合边界以稳定速度场
- **Baseline** · 摘要未列具名方法
- **Benchmark** · 切片图像到空间表达推断，指标待核
- **关键结果 / 消融** · 作者报告预测表现改善，具体消融待核
- **适用条件 / 局限** · 需要同类组织与可靠跨模态监督

**可复用机制** · 用输入相关序列先验替代各向同性噪声作为流匹配起点

<a id="paper-154308"></a>

## Align Before Aggregation: Basis-Consistent Federated LoRA under Heterogeneous Ranks

[官方论文页](https://neurips.cc/virtual/2026/poster/154308) · [作者来源](https://openreview.net/forum?id=EfUHrLQ6uH)

- **问题 / 瓶颈** · 反复重分解会使低秩客户端收到的基前缀不稳定
- **核心创新 / 方法** · 将局部基对齐后重构更新，再重分解并固定基规约
- **Baseline** · 代表性联邦 LoRA 聚合方法
- **Benchmark** · 不同客户端秩异质程度
- **关键结果 / 消融** · 作者报告最强秩异质设置收益更大
- **适用条件 / 局限** · 区别于数据异质导致的方向冲突，需比较基稳定性

**可复用机制** · 下发不同秩前先对齐客户端与全局参考的前缀基

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

<a id="paper-150662"></a>

## Aligned LoRA Updates via Intrinsic Geometry for Federated Low-Rank Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/150662) · [作者来源](https://openreview.net/forum?id=gOYBV7SBxP)

- **问题 / 瓶颈** · 异质数据导致低秩更新相互抵消
- **核心创新 / 方法** · 用子空间度量诊断方向冲突，并在聚合对齐与本地更新中抑制冲突
- **Baseline** · 既有联邦低秩适配方法
- **Benchmark** · 数据异质设置下的下游任务
- **关键结果 / 消融** · 报告冲突随数据异质增强且集中在列空间
- **适用条件 / 局限** · 与秩异质导致的前缀不稳需分别检查

**可复用机制** · 测量客户端更新子空间冲突再选择聚合和本地约束

<a id="paper-154600"></a>

## Aligning AI Teams

[官方论文页](https://neurips.cc/virtual/2026/poster/154600) · [作者来源](https://openreview.net/forum?id=COJLsgVYoq)

- **问题 / 瓶颈** · 个体对齐未必继承到团队，职责分散导致漏查
- **核心创新 / 方法** · 对照相互批评和群聊，测试显式安全负责人及规格文档
- **Baseline** · 单智能体、普通团队、群聊和互评
- **Benchmark** · 两项软件任务和十项咨询提案任务
- **关键结果 / 消融** · 作者报告指定安全责任或发布规格可恢复部分对齐
- **适用条件 / 局限** · 不同任务与模型上的效应大小待核

**可复用机制** · 指定系统级安全负责人并记录可检查的规格

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

<a id="paper-149582"></a>

## Aligning LLMs with Biomedical Knowledge using Balanced Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/149582) · [作者来源](https://openreview.net/forum?id=p2HWge7bRt)

- **问题 / 瓶颈** · 领域语料的低置信 token 并非同一类噪声。
- **核心创新 / 方法** · 同时以组归一化调整 token 权重，并对知识密集序列重新分配样本权重。
- **Baseline** · 同训练设置下的 SFT 与 DFT。
- **Benchmark** · 医学评测与后续稀疏奖励训练，具体数据集及指标待核。
- **关键结果 / 消融** · 作者报告较两种微调方式增益稳定，后续稀疏奖励训练表现改善。
- **适用条件 / 局限** · 不同领域低置信密集区未必代表知识缺口。

**可复用机制** · 通用专业语料微调时单独检验难点的局部集中度，并比较 token 与序列级重加权。

<a id="paper-152778"></a>

## Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived Semantic Dimensions

[官方论文页](https://neurips.cc/virtual/2026/poster/152778) · [作者来源](https://openreview.net/forum?id=QPV6HxIK35)

- **问题 / 瓶颈** · 答对相似性问题仍可能依赖与人不同的特征。
- **核心创新 / 方法** · 从三选一行为得到的 66 维语义空间中选择显著维度，转成理由监督。
- **Baseline** · 与普通多模态评测及未对齐模型比较，具名基线待核。
- **Benchmark** · 以 470 万人类判断构建的空间；标准多模态任务与独立 NSD 的 fMRI 表征相似分析。
- **关键结果 / 消融** · 作者报告行为一致性及神经表征对齐提高；幅度待核。
- **适用条件 / 局限** · 理由来源于推断的人类维度，不能直接代表个体判断。

**可复用机制** · 在答案之外以独立行为证据监督理由，并分别测人类一致性和任务正确率。

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

<a id="paper-140065"></a>

## Alignment Is Not Enough for Safe Medical LLM Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/140065) · [作者来源](https://openreview.net/forum?id=Tju86JH3mo)

- **问题 / 瓶颈** · 单总体分数隐藏危险误判与临床意见不确定。
- **核心创新 / 方法** · 重查已有评测并提出任务规则手册、专家验证集及错误分析协议。
- **Baseline** · 比较以评审一致性作为主要证据的做法。
- **Benchmark** · 重查医疗评审设置，检查等价诊断、答案遗漏及支持治疗计划。
- **关键结果 / 消融** · 作者发现实用评审器仍可能拒绝等价诊断及认可不安全答案。
- **适用条件 / 局限** · 属于立场及案例复核，未证明协议普适。

**可复用机制** · 使用自动评审作高影响筛选前，以专家标记的关键错误集验证其稳定性。

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

<a id="paper-154963"></a>

## All-Addition Spiking Diffusion Models with Attention Enhancement

[官方论文页](https://neurips.cc/virtual/2026/poster/154963) · [作者来源](https://openreview.net/forum?id=9bpunbjC2G)

- **问题 / 瓶颈** · 脉冲骨干省乘法，但非脉冲模块仍可能抵消优势。
- **核心创新 / 方法** · 用非负三值脉冲、膜电位注意力和可加捷径，经重参数化实现推理只加。
- **Baseline** · 对照其他脉冲生成器。
- **Benchmark** · 生成质量与脉冲时间步，具体数据集指标待核。
- **关键结果 / 消融** · 作者报告更少时间步下改善质量。
- **适用条件 / 局限** · 算子计数与实测能耗不同，硬件结果待确认。

**可复用机制** · 压缩算子时同时审计残差链路和注意力，以真实设备测能耗。

<a id="paper-148795"></a>

## Alleviating Hallucination with Training-Free Uncertainty-Guided Steering

[官方论文页](https://neurips.cc/virtual/2026/poster/148795) · [作者来源](https://openreview.net/forum?id=v2TDfSvdkb)

- **问题 / 瓶颈** · 置信估计通常只用于后验拒答。
- **核心创新 / 方法** · 沿置信度对逐层激活的梯度修改推理状态，无参数更新。
- **Baseline** · 与不做激活干预的生成比较，具名方法待核。
- **Benchmark** · 多个任务的幻觉率，具体集和指标待核。
- **关键结果 / 消融** · 作者报告多任务幻觉减少。
- **适用条件 / 局限** · 低不确定性未必等于正确，依赖可信置信代理及梯度访问。

**可复用机制** · 比较同一置信分数用于弃答、重排和激活修正时的效用。

<a id="paper-149069"></a>

## All-in-one Adverse Weather Removal via Prior-modulated and Velocity-constrained Rectified Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/149069) · [作者来源](https://openreview.net/forum?id=t5syQ7vPjU)

- **问题 / 瓶颈** · 未见与混合天气导致统一像素复原过平滑。
- **核心创新 / 方法** · 冻结视觉语言模型预测天气概率及属性，条件归一化和适配器产生锚点，再用终点一致的残差整流流匹配细化。
- **Baseline** · 对照现有天气复原方法，具体名称待核。
- **Benchmark** · 跨集单一和混合天气图像复原，比较保真度和感知质量。
- **关键结果 / 消融** · 作者报告两类指标及跨集泛化改善。
- **适用条件 / 局限** · 依赖天气感知及初估质量，独立收益待核。

**可复用机制** · 比较硬退化类别与软属性作为恢复条件，再分离残差细化的作用。

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

<a id="paper-154004"></a>

## AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154004) · [作者来源](https://openreview.net/forum?id=Gu9oMaNyKv)

- **问题 / 瓶颈** · 单帧观察难支持拓扑和路线推理
- **核心创新 / 方法** · 把观察转换为空间树及路线图，以工具调度和证据仲裁使用地图
- **Baseline** · 原始专有模型
- **Benchmark** · VSI-Bench、MindCube
- **关键结果 / 消融** · 免训练设置报告提升 5% 至 18%
- **适用条件 / 局限** · 地图重建错误可传到规划

**可复用机制** · 对照一次性几何变换与持久地图查询，分别测单跳和多步任务

<a id="paper-153761"></a>

## Alloy Agents Can Be More Dangerous Than Either Model Alone

[官方论文页](https://neurips.cc/virtual/2026/poster/153761) · [作者来源](https://openreview.net/forum?id=Is7kzM3Dxo)

- **问题 / 瓶颈** · 独立模型的结果无法代表组合后的长期行为
- **核心创新 / 方法** · 按风险是否需要持续多轮划分评测，比较组合系统和各组件
- **Baseline** · 相同模型分别单独运行
- **Benchmark** · 单步及持续多步安全评测
- **关键结果 / 消融** · 作者观察到组合表现的方向随任务结构改变
- **适用条件 / 局限** · 结论只覆盖受测模型和协议

**可复用机制** · 上线前独立审计组合系统的跨轮状态和多步风险

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

<a id="paper-156657"></a>

## Almost Sure Convergence of Linear Temporal Difference Learning with Arbitrary Features

[官方论文页](https://neurips.cc/virtual/2026/poster/156657) · [作者来源](https://neurips.cc/virtual/2026/poster/156657)

- **问题 / 瓶颈** · 特征线性相关破坏常用的参数唯一性条件
- **核心创新 / 方法** · 刻画线性 TD 平均 ODE 的有界不变集
- **Baseline** · 假定特征独立的线性 TD 分析
- **Benchmark** · 线性价值预测的几乎必然收敛证明
- **关键结果 / 消融** · 权重到有界集合，集合内价值估计几乎处处相同
- **适用条件 / 局限** · 针对线性 TD 及论文条件

**可复用机制** · 分析冗余特征时单独检查预测一致性

<a id="paper-151239"></a>

## Almost Sure Convergence Rates of Stochastic Approximation and Reinforcement Learning via a Poisson-Moreau Drift

[官方论文页](https://neurips.cc/virtual/2026/poster/151239) · [作者来源](https://openreview.net/forum?id=brmKAqSWd0)

- **问题 / 瓶颈** · 依赖噪声使几乎必然速率难证明
- **核心创新 / 方法** · 以 Poisson 方程校正 Moreau 平滑得到的 Lyapunov 漂移
- **Baseline** · 独立噪声情形的速率参照
- **Benchmark** · 期望更新为收缩映射的随机逼近
- **关键结果 / 消融** · 调和步长得到接近误差阶 n 的负一次方的速率
- **适用条件 / 局限** · 需要收缩更新和论文规定噪声条件

**可复用机制** · 校验算法满足何种漂移条件后再迁移步长结论

<a id="paper-155476"></a>

## A Local Geometric Analysis of Maximal Coding Rate Reduction via Error Bounds

[官方论文页](https://neurips.cc/virtual/2026/poster/155476) · [作者来源](https://openreview.net/forum?id=5JGz4ivDSM)

- **问题 / 瓶颈** · 难解释一阶法靠近局部极值时收敛快
- **核心创新 / 方法** · 证明局部梯度误差界，进而推出 PL 型条件及二次增长
- **Baseline** · 一阶优化迭代；其他对照待核
- **Benchmark** · 理论分析及数值收敛实验
- **关键结果 / 消融** · 局部线性收敛，实验支持预测趋势
- **适用条件 / 局限** · 仅在极值邻域及论文条件下

**可复用机制** · 对编码率损失监测梯度和局部距解趋势，区分热启动和全局优化

<a id="paper-155416"></a>

## A Locality-Aware Surrogate for Natural-Gradient Descent in Quantum Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155416) · [作者来源](https://openreview.net/forum?id=5qbHr87u5d)

- **问题 / 瓶颈** · 完整量子 Fisher 昂贵，块对角会丢耦合
- **核心创新 / 方法** · 按 Pauli 权重截断并基于支撑重叠保留项，复用测量数据
- **Baseline** · 块对角 QNG、随机自然梯度
- **Benchmark** · 有限测量次数的变分量子优化
- **关键结果 / 消融** · 方法给出截断的偏差方差权衡，数值待核
- **适用条件 / 局限** · 依赖生成元的局部结构

**可复用机制** · 扫描截断级别并在同等测量预算下比较

<a id="paper-150316"></a>

## A Locally Tokenized Generative Model for Robust Time-Series Watermarking

[官方论文页](https://neurips.cc/virtual/2026/poster/150316) · [作者来源](https://openreview.net/forum?id=j0GmuP3V69)

- **问题 / 瓶颈** · 整体重编码会让普通局部变化波及整个检测统计量
- **核心创新 / 方法** · 以有界时间窗口形成离散标记，限制重编码的传播范围
- **Baseline** · 全局耦合重编码
- **Benchmark** · 金融、能源、神经影像四项基准
- **关键结果 / 消融** · 作者报告检测能力和误报更稳定，生成质量保持
- **适用条件 / 局限** · 局部化可能限制长程表示

**可复用机制** · 在真实数据变换下同时评测误报和检出，验证局部表示的稳定性

<a id="paper-153971"></a>

## AlphaPareto: Formulaic Alpha Discovery with LLM-Guided Multi-Objective Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153971) · [作者来源](https://openreview.net/forum?id=H8C7jHFbSI)

- **问题 / 瓶颈** · 候选池变化使同一搜索动作的收益发生变化
- **核心创新 / 方法** · 编码当前候选及整个候选池，并用 Pareto 正则处理多个目标
- **Baseline** · 固定池表征及单目标强化学习
- **Benchmark** · 公式化金融因子搜索，指标细节待核
- **关键结果 / 消融** · 摘要给出非平稳建模及向量目标贡献，收益细项待核
- **适用条件 / 局限** · 池编码可能遗漏因子依赖，市场外推待核

**可复用机制** · 在动态候选池上区分局部方案质量与集合层收益

<a id="paper-150234"></a>

## AlphaPROBE: Alpha Mining via principled retriveval and on-graph biased evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/150234) · [作者来源](https://openreview.net/forum?id=jnNAuSXHv2)

- **问题 / 瓶颈** · 独立生成和单谱系迭代可能重复搜索
- **核心创新 / 方法** · 以 DAG 记录祖先关系，结合贝叶斯检索与祖先条件生成
- **Baseline** · 独立生成和局部父子演化
- **Benchmark** · 金融因子发现，具名设置待核
- **关键结果 / 消融** · 摘要未核实量化幅度
- **适用条件 / 局限** · 谱系记录质量影响复用

**可复用机制** · 固定探索预算，比较平面候选池与谱系索引的重复率

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

<a id="paper-139345"></a>

## AmaraSpatial-10K: A Spatially and Semantically Aligned 3D Dataset for Spatial Computing and Embodied AI

[官方论文页](https://neurips.cc/virtual/2026/poster/139345) · [作者来源](https://openreview.net/forum?id=VXIAvMmHzI)

- **问题 / 瓶颈** · 资产尺度、锚点和碰撞几何错误影响部署
- **核心创新 / 方法** · 联合评估尺度合理性、锚点误差、跨模态一致性及物理稳定性
- **Baseline** · Objaverse、HSSD、ABO、GSO
- **Benchmark** · 三维资产库、Habitat-Sim 和 Holodeck
- **关键结果 / 消融** · 相对 Objaverse Recall@5 为 0.612 对 0.181，物理稳定率报告 99.1%
- **适用条件 / 局限** · 合成资产与仿真指标未必代表真实应用

**可复用机制** · 给资产库加尺度、锚点及落地稳定性三类检查

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

<a id="paper-139543"></a>

## A Matched-Budget Audit Framework for Recaptioned Image-Text Supervision Distributions

[官方论文页](https://neurips.cc/virtual/2026/poster/139543) · [作者来源](https://openreview.net/forum?id=JobgYHJvPo)

- **问题 / 瓶颈** · 描述长度容易混入语义质量比较，训练后评分又受训练配置干扰。
- **核心创新 / 方法** · 用固定 64 词汇单元窗口，按共享的可控基本单元口径审计覆盖、图像支持和文本表面质量。
- **Baseline** · 比较原始和重写描述的配对数据，以及不同评判模型。
- **Benchmark** · 五个公开语料上的七组配对；含 CC12M；用 Qwen 和 Gemma 评判。
- **关键结果 / 消融** · 四组跨语料配对每条描述多出 3.40–6.35 个受图像支持的基本单元；CC12M 中更长和更密并不等价。
- **适用条件 / 局限** · 评判模型可能共享偏差，词汇预算与单元切分会影响结果。

**可复用机制** · 比较图文标注策略时先匹配描述预算，再分开报告内容覆盖和图像支持。

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

<a id="paper-153251"></a>

## A Matter of Interest: Understanding Interestingness Judgments of Math Problems in Humans and Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153251) · [作者来源](https://openreview.net/forum?id=MdhVFMmtwx)

- **问题 / 瓶颈** · 平均分相近可能掩盖模型和人对趣味性的分歧。
- **核心创新 / 方法** · 比较模型与两类人的评分和理由，再对生成题目先验有效性过滤后评趣味。
- **Baseline** · 有大学数学经验的众包参与者、国际数学奥赛选手与多种语言模型。
- **Benchmark** · 数学题趣味性评分、评分分布、理由相关性和过滤后的模型生成题。
- **关键结果 / 消融** · 作者报告整体趋势可相似，但多数模型未复现人的评分分布，理由相关性较低。
- **适用条件 / 局限** · 趣味性受人群及题库影响；摘要未说明评判协议与数值。

**可复用机制** · 采用模型代理人评前同时比较分布、理由和群体差异，单独记录生成问题的有效率。

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

<a id="paper-139661"></a>

## AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment

[官方论文页](https://neurips.cc/virtual/2026/poster/139661) · [作者来源](https://neurips.cc/virtual/2026/poster/139661)

- **问题 / 瓶颈** · 显式有害指令测试难覆盖隐式目标冲突
- **核心创新 / 方法** · 按威胁感知、机会和推理建立防御评测维度
- **Baseline** · 显式有害指令评测为概念对照
- **Benchmark** · 七行业35场景，十个模型
- **关键结果 / 消融** · 跨场景差距62个百分点，显式解释缺失仍可出现违规
- **适用条件 / 局限** · 仅限所测场景，自述不可替代行为监测

**可复用机制** · 在沙箱内分别评估行为与理由。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-152593"></a>

## AmbientFM: A Foundation Model for Ambient Sensing

[官方论文页](https://neurips.cc/virtual/2026/poster/152593) · [作者来源](https://openreview.net/forum?id=RxX10wg674)

- **问题 / 瓶颈** · WiFi感知训练流程碎片化
- **核心创新 / 方法** · 结合对比、掩码重建和无线物理约束预训练CSI
- **Baseline** · 任务专用方案，具名对照待核
- **Benchmark** · 20类设备数据及9项下游任务，含AUROC和空间重建
- **关键结果 / 消融** · 分类基准AUROC均超过0.90
- **适用条件 / 局限** · 设备外泛化与目标函数独立贡献待核

**可复用机制** · 检验单个信道表示能否替代逐任务模型。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-155466"></a>

## AmbiguousWorld: Benchmarking and Resolving Ambiguous Instructions in Video World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155466) · [作者来源](https://openreview.net/forum?id=5ORWSQZFqy)

- **问题 / 瓶颈** · 单一路径容易误解指令及破坏物理一致性
- **核心创新 / 方法** · VLM拆子目标并以物理和功能维度剪枝
- **Baseline** · 现有视频生成方案，名称待核
- **Benchmark** · DROID标注评测，对照人工评价
- **关键结果 / 消融** · 成功率最多提高29个百分点，加权一致性提高24.2分
- **适用条件 / 局限** · 依赖视频模型与裁判，实体执行待核

**可复用机制** · 用多路径规划和反馈处理含糊指令。以卡片中的对照与评测核对该选择的适用范围。

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

<a id="paper-155536"></a>

## A Measure-Theoretic Analysis of Reasoning: Structural Generalization and Approximation Limits

[官方论文页](https://neurips.cc/virtual/2026/poster/155536) · [作者来源](https://openreview.net/forum?id=4s7rR55ePz)

- **问题 / 瓶颈** · 规模规律难解释组合搜索的域外风险
- **核心创新 / 方法** · 以Wasserstein距离描述轨迹偏移，再用对偶性和深度下界分解
- **Baseline** · 绝对位置与旋转编码，深宽变化
- **Benchmark** · 54种Transformer配置的组合搜索
- **关键结果 / 消融** · 报告风险随域偏移增大，深度限制不能单靠加宽补偿
- **适用条件 / 局限** · 下界依赖Dyck语言映射和理论架构

**可复用机制** · 分开扫描位置编码、深度和宽度。以卡片中的对照与评测核对该选择的适用范围。

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

<a id="paper-153037"></a>

## A Mechanistic Interpretability Study of an Astronomical Foundation Model

[官方论文页](https://neurips.cc/virtual/2026/poster/153037) · [作者来源](https://openreview.net/forum?id=OUspS8vKSM)

- **问题 / 瓶颈** · 可解码特征未必具有因果作用
- **核心创新 / 方法** · 按星系条件分层，结合逐层探针、消融和激活替换
- **Baseline** · AION-1仅测光与测光加影像
- **Benchmark** · 星系红移预测，含尘埃衰减和延展星系
- **关键结果 / 消融** · 一个可探测的头消融无可测影响，另一头消融消除尘埃组多模态优势
- **适用条件 / 局限** · 单模型与特定探针集合

**可复用机制** · 用消融验证探针发现的天文特征是否实际参与预测。以卡片中的对照与评测核对该选择的适用范围。

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

<a id="paper-153106"></a>

## AME-TS: Anchored Mixture-of-Experts for Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/153106) · [作者来源](https://openreview.net/forum?id=NtOUejNcpe)

- **问题 / 瓶颈** · 标准MoE专家在微调中分工不稳定
- **核心创新 / 方法** · 以可预测性、季节、趋势和稀疏性预测专家先验
- **Baseline** · 标准MoE及时间序列基础模型
- **Benchmark** · GIFT-Eval准确率效率，M5微调路由稳定性
- **关键结果 / 消融** · 小规模优势较明显，规模大时保持竞争力且激活参数更少
- **适用条件 / 局限** · 先验描述符可能不覆盖域外结构

**可复用机制** · 用可解释序列结构先验约束token路由。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-154520"></a>

## AMGenC: Generating Charge Balanced Amorphous Materials

[官方论文页](https://neurips.cc/virtual/2026/poster/154520) · [作者来源](https://openreview.net/forum?id=CzhhqLpjCl)

- **问题 / 瓶颈** · 无约束采样易产生电荷不守恒材料
- **核心创新 / 方法** · 约束中心化元素噪声、逐步软投影及最终离散投影
- **Baseline** · 无约束生成，具名对照待核
- **Benchmark** · 两个非晶材料数据集，测守恒和逆设计精度
- **关键结果 / 消融** · 报告实现精确电荷平衡且未损失逆设计精度
- **适用条件 / 局限** · 同时满足其他材料约束仍待核

**可复用机制** · 软投影维持约束趋势，再在终点离散投影。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-153946"></a>

## A Minimal Interpretable Architecture for Zero-Shot Reconstruction of Dynamical Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/153946) · [作者来源](https://openreview.net/forum?id=HNtohc9Bxl)

- **问题 / 瓶颈** · 完整架构掩盖预测所需的最小机制
- **核心创新 / 方法** · 将DynaMix归约为当前状态、上下文最近邻及其后继的线性组合
- **Baseline** · DynaMix及上下文复读
- **Benchmark** · 混沌和周期系统，单步误差与动力学重建
- **关键结果 / 消融** · 两参数模型重建有竞争力，短期误差与重建目标可能分离
- **适用条件 / 局限** · 限于所测系统和上下文范围

**可复用机制** · 给零样本动力学模型加入近邻后继的极简基线。以卡片中的对照与评测核对该选择的适用范围。

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

<a id="paper-152907"></a>

## Amortized Guidance for Image Inpainting with Pretrained Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152907) · [作者来源](https://openreview.net/forum?id=PVo9A82GnZ)

- **问题 / 瓶颈** · 任务专训或逐例优化成本高
- **核心创新 / 方法** · 将确定性引导转为辅助高斯问题，并学习连续时间actor–critic引导
- **Baseline** · 冻结底座修补与摊销方法
- **Benchmark** · AFHQv2、FFHQ及ImageNet，多种掩码
- **关键结果 / 消融** · 新增训练参数不到1%，质量速度权衡改善
- **适用条件 / 局限** · 新掩码分布及不同骨干的迁移待核

**可复用机制** · 离线学习可复用修补引导，部署冻结底座。以卡片中的对照与评测核对该选择的适用范围。

<a id="paper-149276"></a>

## Amortized Linear-time Exact Shapley Value for Product-Kernel Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/149276) · [作者来源](https://openreview.net/forum?id=rWupQhgBV4)

- **问题 / 瓶颈** · 常规Shapley近似引入估计误差
- **核心创新 / 方法** · 用乘法单位元替代移除的特征核因子，再共享递推求所有归因
- **Baseline** · 近似SHAP及RKHS-SHAP为背景
- **Benchmark** · 积核模型与核差异的理论设定
- **关键结果 / 消融** · 全部特征二次时间，摊销每特征线性
- **适用条件 / 局限** · 归因语义依赖积核及论文定义的移除操作

**可复用机制** · 积核下利用代数结构求精确归因。以卡片中的对照与评测核对该选择的适用范围。

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

<a id="paper-152433"></a>

## Amortized Structured Stochastic Variational Inference for Gaussian Process Latent Variable Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152433) · [作者来源](https://openreview.net/forum?id=TAYlbKu0tU)

- **问题 / 瓶颈** · 均值场切断两者依赖，弱化流形不确定性
- **核心创新 / 方法** · 摊销条件潜变量后验，保留与 GP 诱导点的依赖
- **Baseline** · 均值场 GP-LVM
- **Benchmark** · 潜流形不确定性，数据集待核
- **关键结果 / 消融** · 摘要报告结构化后验改善估计，细项待核
- **适用条件 / 局限** · 增加条件推断成本

**可复用机制** · 对比结构化与独立后验的校准和计算开销

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

<a id="paper-154781"></a>

## A multi-scale information geometry reveals the structure of mutual information in neural populations

[官方论文页](https://neurips.cc/virtual/2026/poster/154781) · [作者来源](https://openreview.net/forum?id=B1fQuBGYFx)

- **问题 / 瓶颈** · 不同表征距离会导向不同编码解释
- **核心创新 / 方法** · 由粗粒化收缩公理导出多尺度 Fisher 几何并联系互信息
- **Baseline** · 其他表征距离构造
- **Benchmark** · 刺激分辨率变化下的神经反应，细节待核
- **关键结果 / 消融** · 作者给出几何和互信息的理论联系
- **适用条件 / 局限** · 依赖所定义的粗粒化及概率模型

**可复用机制** · 对同一神经编码分别分析细粒度与粗粒度，而非择一距离

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

<a id="paper-150996"></a>

## AnaDiffusion: Anatomically Compositional Latent Diffusion for Controllable 3D Brain MRI Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150996) · [作者来源](https://openreview.net/forum?id=diicBKjM0w)

- **问题 / 瓶颈** · 整体生成难以精确控制指定区域
- **核心创新 / 方法** · 先训练区域扩散，拼接局部后注入全脑潜变量继续去噪
- **Baseline** · 整体式三维生成
- **Benchmark** · 脑 MRI 局部控制与整体验证，细节待核
- **关键结果 / 消融** · 摘要报告可保留指定结构并恢复全局上下文
- **适用条件 / 局限** · 依赖解剖区域划分，临床有效性待核

**可复用机制** · 比较整体采样与部件注入，分别测局部一致和全局连贯

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

<a id="paper-156663"></a>

## An Anytime Algorithm for Good Arm Identification

[官方论文页](https://neurips.cc/virtual/2026/poster/156663) · [作者来源](https://neurips.cc/virtual/2026/poster/156663)

- **问题 / 瓶颈** · 收集预算和调用时刻可能事先未知
- **核心创新 / 方法** · 设计无调参的 APGAI 采样规则和相应停止法
- **Baseline** · 均匀采样
- **Benchmark** · 随机赌博机的固定置信和固定预算设定
- **关键结果 / 消融** · 作者给出任意时刻错误界及加入停止规则后的样本复杂度界
- **适用条件 / 局限** · 依赖随机赌博机假设

**可复用机制** · 将寻找合格候选与证明没有合格候选分别计量

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

<a id="paper-151182"></a>

## Anatomy-Activated Mixture-of-Experts for 3D Medical Vision-Language Pre-training

[官方论文页](https://neurips.cc/virtual/2026/poster/151182) · [作者来源](https://openreview.net/forum?id=cOJs7gDYiz)

- **问题 / 瓶颈** · 局部视觉特征缺少切片整体器官信息。
- **核心创新 / 方法** · 以器官存在直方图和全局上下文路由图块，并用多尺度器官查询投影。
- **Baseline** · 现有医学预训练方法，名称待核。
- **Benchmark** · 六万余 CT 预训练，下游分割、分类、检测及 MRI 和超声迁移。
- **关键结果 / 消融** · 作者报告多项任务领先及跨模态泛化；幅度待核。
- **适用条件 / 局限** · 依赖器官预测的准确性。

**可复用机制** · 比较图块级全局条件与 token 路由的专家专门化和计算成本。

<a id="paper-155842"></a>

## Anatomy-aware Spatio-Temporal Modeling for Echocardiography Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/155842) · [作者来源](https://openreview.net/forum?id=2TtThaZ1Ks)

- **问题 / 瓶颈** · 低质超声及域偏移使心脏边界难辨。
- **核心创新 / 方法** · 以解剖空间关系正则注意力，经可变形空间聚合后做时序状态空间建模。
- **Baseline** · 现有超声分割，名称待核。
- **Benchmark** · CAMUS、EA 及分布外床旁超声，测分割。
- **关键结果 / 消融** · 作者报告分割精度和跨域表现改善；数值待核。
- **适用条件 / 局限** · 解剖先验对异常结构的适用边界待查。

**可复用机制** · 分别消融结构正则和运动建模，检验域偏移下各自收益。

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

<a id="paper-154881"></a>

## Anatomy-Preserving Unpaired Medical Image Translation via Shared Latent Anchoring

[官方论文页](https://neurips.cc/virtual/2026/poster/154881) · [作者来源](https://openreview.net/forum?id=AC5Xd25rUC)

- **问题 / 瓶颈** · 非配对转换可能改动解剖结构。
- **核心创新 / 方法** · 用掩码重建锚定结构潜变量，以目标域原型补源域弱监督，再训练条件流。
- **Baseline** · 配对与非配对方法，名称待核。
- **Benchmark** · OCT 至 OCTA 和脑 MR 至 CT，含 PSNR 和 SSIM。
- **关键结果 / 消融** · OCT 至 OCTA 的 PSNR 和 SSIM 最多改善 11.2% 和 26.4%。
- **适用条件 / 局限** · 需要可用结构监督，罕见结构保真待核。

**可复用机制** · 对非配对生成分别固定结构和外观路径，并对照联合训练。

<a id="paper-152308"></a>

## An Axiomatic Analysis of DPO and NLHF as Reference-Dependent Probabilistic Voting Rules

[官方论文页](https://neurips.cc/virtual/2026/poster/152308) · [作者来源](https://openreview.net/forum?id=U33O5GzkG8)

- **问题 / 瓶颈** · 异质偏好聚合可能依赖参考模型或训练顺序。
- **核心创新 / 方法** · 将 DPO 和 NLHF 写成依赖参考的概率投票规则并比较公理。
- **Baseline** · DPO、NLHF 和概率 Borda。
- **Benchmark** · CoVal 与真实底座，统计公理违反频率及幅度。
- **关键结果 / 消融** · NLHF 在 KL 强度低于界时违反单调性；DPO 恒满足单调性，但违反两项人口公理。
- **适用条件 / 局限** · 结论依赖建模和公理定义。

**可复用机制** · 多轮偏好训练交换阶段顺序，检查最终分布及群体偏好响应。

<a id="paper-152132"></a>

## Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation

[官方论文页](https://neurips.cc/virtual/2026/poster/152132) · [作者来源](https://openreview.net/forum?id=VHM6LwnWRO)

- **问题 / 瓶颈** · 每像素一个高斯会在平坦区域浪费原语。
- **核心创新 / 方法** · 按熵布置锚点并聚合遮挡感知的多视角信息，再解码局部高斯。
- **Baseline** · 逐像素前馈 3DGS。
- **Benchmark** · 多个新视角合成数据集，测渲染和高斯用量。
- **关键结果 / 消融** · 作者报告近一个数量级的原语减少和更高渲染质量。
- **适用条件 / 局限** · 熵可能混淆视觉纹理与几何复杂度。

**可复用机制** · 固定原语数比较像素对齐与自适应锚点的外推质量。

<a id="paper-139276"></a>

## ANCHOR: Audio-Visually Grounded Chain-of-Thought Reasoning Benchmark

[官方论文页](https://neurips.cc/virtual/2026/poster/139276) · [作者来源](https://openreview.net/forum?id=a4PqqhFMnJ)

- **问题 / 瓶颈** · 高答题率可掩盖解释缺少感知依据。
- **核心创新 / 方法** · 人工校验帧、框及声音线索，联合评价回答和理由定位。
- **Baseline** · 九个 MLLM 及去掉提示线索的设置。
- **Benchmark** · 224 个核验视频、975 个 QA，测答案和证据对齐。
- **关键结果 / 消融** · 移除框准确率降 7.7 个百分点；全线索 57.7%，仅声音 16.1%。
- **适用条件 / 局限** · 评判一致性及线索提示对策略的影响待核。

**可复用机制** · 以匹配输入区分答对、理由正确和证据定位，再分别做模态消融。

<a id="paper-148935"></a>

## Anchoring LLM-based Chest X-ray Report Generation via Diffusion Language Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/148935) · [作者来源](https://openreview.net/forum?id=u78842hqLu)

- **问题 / 瓶颈** · 自回归解码需同时承担全局规划与语言实现。
- **核心创新 / 方法** · 用扩散语言模型预测结构化提纲，以提纲约束自回归报告。
- **Baseline** · 既有报告生成和规划消融；名称待核。
- **Benchmark** · MIMIC-CXR，评估临床忠实性。
- **关键结果 / 消融** · 作者报告忠实性改善且两组件互补，数值待核。
- **适用条件 / 局限** · 仅摘要证据，提纲错误可传播。

**可复用机制** · 在图像到长文本任务比较自由生成与结构化提纲，分别测事实与表达。

<a id="paper-149063"></a>

## Anchoring Physiological Invariance, Expanding Domain Plasticity: Prior-Stabilized Dynamic Adaptation for Continual rPPG Measurement

[官方论文页](https://neurips.cc/virtual/2026/poster/149063) · [作者来源](https://openreview.net/forum?id=t9PpANJFJe)

- **问题 / 瓶颈** · 视频域切换引发遗忘并使适配不稳。
- **核心创新 / 方法** · 用 Fisher 识别并保留关键参数，按层检测偏移、扩展分支并继承参数。
- **Baseline** · 持续学习对照，名称待核。
- **Benchmark** · 五个公共远程脉搏测量数据集。
- **关键结果 / 消融** · 作者报告抗遗忘和域适配改善。
- **适用条件 / 局限** · 扩容开销与变化检测误差待核。

**可复用机制** · 比较全面扩容和分层扩容，分别报告过去域误差和新增参数。

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

<a id="paper-149182"></a>

## AnchorRep: Defending LLMs Against Cross-Model Adversarial Transfer via Representation Repulsion

[官方论文页](https://neurips.cc/virtual/2026/poster/149182) · [作者来源](https://neurips.cc/virtual/2026/poster/149182)

- **问题 / 瓶颈** · 只测拒绝率会漏掉正常文本退化。
- **核心创新 / 方法** · 以表征分离训练防御，并引入正常输出乱码率。
- **Baseline** · 既有跨模型防御方法，名称待核。
- **Benchmark** · 五个模型、四类架构，比较跨模型安全性和正常输出。
- **关键结果 / 消融** · 作者报告不安全成功率不超过 1.1%；部分已有防御的正常乱码率可达 77%。
- **适用条件 / 局限** · 乱码指标与模型家族覆盖待核。

**可复用机制** · 部署安全适配前分开测正常拒绝与文本质量，避免单一拒绝指标掩盖退化。

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

<a id="paper-150497"></a>

## A Near-optimal SQ Lower Bound for Smoothed Agnostic Learning of Boolean Halfspaces

[官方论文页](https://neurips.cc/virtual/2026/poster/150497) · [作者来源](https://openreview.net/forum?id=hf4WNJ6sRf)

- **问题 / 瓶颈** · 连续平滑模型结果不能直接套用于布尔空间。
- **核心创新 / 方法** · 分析 L1 多项式回归上界与统计查询下界。
- **Baseline** · 连续高斯设定的已知结果。
- **Benchmark** · 均匀布尔输入、每坐标独立翻转，比较运行、样本及 SQ 复杂度。
- **关键结果 / 消融** · 给出近匹配的上界和 SQ 下界，随精度与平滑强度变化。
- **适用条件 / 局限** · 下界限于 SQ，且需均匀边缘。

**可复用机制** · 在离散噪声下单独扫描平滑强度和目标误差，避免将低噪声区当作同等易学。

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

<a id="paper-153387"></a>

## An Efficient Algorithm for Thresholding Monte Carlo Tree Search

[官方论文页](https://neurips.cc/virtual/2026/poster/153387) · [作者来源](https://openreview.net/forum?id=LlqiVTIyml)

- **问题 / 瓶颈** · 求最优动作或估精确根值可能浪费预算。
- **核心创新 / 方法** · 为已知极大极小树的叶奖励使用 Track-and-Stop，改造 D-Tracking 为比率式。
- **Baseline** · 标准 D-Tracking。
- **Benchmark** · 阈值树搜索，测误差保证、样本数与单轮计算。
- **关键结果 / 消融** · 渐近样本最优，单轮开销从臂数线性降为对数。
- **适用条件 / 局限** · 依赖已知树及可抽样叶奖励。

**可复用机制** · 验收问题用二元置信停止规则，与完整求值对照预算。

<a id="paper-153426"></a>

## An Efficient Cross-modal Feature Reconstruction Model for Multimodal Multi-class Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/153426) · [作者来源](https://openreview.net/forum?id=LQQHB5gOGa)

- **问题 / 瓶颈** · 统一模型容量增加时也可能准确重建异常，从而压低异常分数。
- **核心创新 / 方法** · 用自适应交互和混合注意力卷积重建跨模态特征，利用模态对应难度约束重建。
- **Baseline** · 比较多模态异常检测方法；具名对照待全文核实。
- **Benchmark** · MVTec 3D-AD 和 Eyecandies 的多类异常检测，另比较计算量。
- **关键结果 / 消融** · 作者报告待测基准表现改善，约 44.63M 参数、15.77 GFLOPs。
- **适用条件 / 局限** · 需要多传感器输入；模态错位导致的误报需单独测量。

**可复用机制** · 用同等模型容量对照同模态与跨模态重建，在正常和异常样本上分别测误差。

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

<a id="paper-149795"></a>

## An Enigma of Artificial Reason: Investigating the Production-Evaluation Gap in Large Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149795) · [作者来源](https://openreview.net/forum?id=nHVT3A8K70)

- **问题 / 瓶颈** · 正确终值掩盖链路错误
- **核心创新 / 方法** · VAIR 用正确答案配有错误步骤的解法隔离评判能力
- **Baseline** · 人类解题与评分、模型解题与评分
- **Benchmark** · VAIR 数学题
- **关键结果 / 消融** · 前沿模型评判可低至48%，解题仍接近满分
- **适用条件 / 局限** · 数学题结论跨域待核

**可复用机制** · 给判题模型构造正确终值但无效证明的对照

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

<a id="paper-149569"></a>

## A New Framework for Quantum Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149569) · [作者来源](https://openreview.net/forum?id=p9Lz3Nd5c2)

- **问题 / 瓶颈** · 中间测量可能扰动轨迹
- **核心创新 / 方法** · 以条件量子通道表示策略和环境，保留状态、行动与回报寄存器
- **Baseline** · 采用经典编码或途中测量的量子强化学习框架
- **Benchmark** · 全量子强化学习的形式化设置
- **关键结果 / 消融** · 给出无需中间测量的接口
- **适用条件 / 局限** · 依赖相干寄存器与通道实现

**可复用机制** · 设计量子策略时单列何处需测量并比较轨迹扰动

<a id="paper-151703"></a>

## A New Perspective on Target-Conditioned Structural Dynamics for Link Prediction in Dynamic Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/151703) · [作者来源](https://openreview.net/forum?id=YfsyoH7YFs)

- **问题 / 瓶颈** · 稀疏硬指标在与高维特征拼接后可能被稀释
- **核心创新 / 方法** · 构造目标条件的混合结构状态，按近期历史演化后调节聚合
- **Baseline** · 以结构编码作静态输入的目标条件模型
- **Benchmark** · 动态链接预测，具名数据集待核
- **关键结果 / 消融** · 方法保留目标结构的时间演化，数值待核
- **适用条件 / 局限** · 依赖近期历史和结构证据可得

**可复用机制** · 将重要但稀疏的结构信号从输入特征改为显式更新状态

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

<a id="paper-138932"></a>

## Animation2Code: Evaluating Temporal Visual Reasoning in Video-to-Code Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/138932) · [作者来源](https://openreview.net/forum?id=veADXfstkO)

- **问题 / 瓶颈** · 静态相似不能证明理解运动
- **核心创新 / 方法** · 从动画视频生成可执行代码，渲染后拆分外观和时序指标
- **Baseline** · 现有视觉语言模型
- **Benchmark** · 1069 个网页动画及对应实现
- **关键结果 / 消融** · 作者报告外观相似时仍可时序不一致
- **适用条件 / 局限** · 证据限网页动画

**可复用机制** · 视频重建评测将轨迹或相位误差独立记录

<a id="paper-149407"></a>

## An Information-Theoretic Evaluation Framework for Benchmark and Model Diagnosis in Knowledge Tracing

[官方论文页](https://neurips.cc/virtual/2026/poster/149407) · [作者来源](https://openreview.net/forum?id=qISxwVTG3L)

- **问题 / 瓶颈** · 总体 AUC 掩盖不同难度的改进
- **核心创新 / 方法** · 以 CTW 估计交互局部不可约不确定性，按熵分箱
- **Baseline** · 总体 AUC 和准确度比较
- **Benchmark** · NIPS Task 3/4、Algebra 2005
- **关键结果 / 消融** · 改进随不确定性显著变化
- **适用条件 / 局限** · CTW 是操作代理，不能视为真实理论上限

**可复用机制** · 在相同数据上比较高低可预测区间的模型增益

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

<a id="paper-151358"></a>

## Announced Breaks Separate Conformal Reliability from Frequency Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/151358) · [作者来源](https://openreview.net/forum?id=b9d9BqKBKg)

- **问题 / 瓶颈** · 等待覆盖错误才调节会增加检测延迟
- **核心创新 / 方法** · 分段 split-CP 重置分位数，比较宣布变点的 ACI 更新
- **Baseline** · 反应式自适应共形方法
- **Benchmark** · 变点后覆盖理论与合成实验
- **关键结果 / 消融** · 单步概率差率为平方根倒数，纯 ACI 平均频率差可为倒数
- **适用条件 / 局限** · 实际 ACI 带投影与预热需修正

**可复用机制** · 分别审计每步覆盖概率和累计经验覆盖

<a id="paper-149826"></a>

## An Õptimal Differentially Private PAC Learner for Concept Classes with VC Dimension 1

[官方论文页](https://neurips.cc/virtual/2026/poster/149826) · [作者来源](https://openreview.net/forum?id=n1036lYSI7)

- **问题 / 瓶颈** · 一般类上界对 Littlestone 维度依赖较高
- **核心创新 / 方法** · 用私有中位数先找树深再定位节点，按需返回适当叶节点
- **Baseline** · 先前一般 VC 类上界与迭代对数下界
- **Benchmark** · VC维度1的差分隐私PAC理论
- **关键结果 / 消融** · 样本复杂度对维度近迭代对数
- **适用条件 / 局限** · 不直接推广到高VC维类

**可复用机制** · 设计私有学习器时检查是否可用概念结构降低定位成本

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

<a id="paper-153372"></a>

## AnyBokeh: Physics-Guided Any-to-Any Bokeh Editing with Optical Fingerprint Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/153372) · [作者来源](https://openreview.net/forum?id=LrBZHLRicR)

- **问题 / 瓶颈** · 把已有模糊一并去除易丢失输入线索
- **核心创新 / 方法** · 估计带符号的弥散圈和视差，拟合两者关系转移光学特性
- **Baseline** · 假设全清晰输入的散景编辑路线
- **Benchmark** · 任意焦点与光圈条件的单图编辑，具名评测待核
- **关键结果 / 消融** · 摘要提出利用原有模糊线索避免重建伪影
- **适用条件 / 局限** · 依赖视差与模糊估计

**可复用机制** · 对非理想输入先估计观测过程再改变生成条件

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

<a id="paper-139245"></a>

## AnyHand: A Large-Scale Synthetic Dataset for RGB(-D) Hand Pose Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/139245) · [作者来源](https://openreview.net/forum?id=cUZmslkWyQ)

- **问题 / 瓶颈** · 只扩大样本数难判断遮挡、深度与场景覆盖各自价值
- **核心创新 / 方法** · 构建含对齐深度与几何标注的合成图像并做规模和组成消融
- **Baseline** · 相同 RGB 架构和训练配方，另比既有 RGB-D 方法
- **Benchmark** · FreiHAND、HO-3D，手姿估计
- **关键结果 / 消融** · 摘要报告固定网络时添加合成数据有效，轻量深度融合亦优于对照
- **适用条件 / 局限** · 依赖合成覆盖和真实场景差距

**可复用机制** · 通过固定训练配方的组成消融评估增补数据质量。

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

<a id="paper-151900"></a>

## Anymotion: A Dataset, Benchmark, and Baseline for Controllable Human Motion Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/151900) · [作者来源](https://openreview.net/forum?id=X6fainOrUU)

- **问题 / 瓶颈** · 直接生成编辑动作难兼顾语义要求和身体结构
- **核心创新 / 方法** · 多模态模型先推导关键点及 MetaQueries，再条件化扩散生成
- **Baseline** · 具体动作编辑对照待核
- **Benchmark** · HME-1M 与 Human Motion-Bench，覆盖六大类编辑
- **关键结果 / 消融** · 作者报告多类场景效果改善，模块消融待核
- **适用条件 / 局限** · 依赖关键点规划质量与分类覆盖

**可复用机制** · 用显式骨架和语义先验引导生成，并对照移除各类中间态。

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

<a id="paper-153792"></a>

## AOT-POT: Adaptive Operator Transformation for Large-Scale PDE Pre-training

[官方论文页](https://neurips.cc/virtual/2026/poster/153792) · [作者来源](https://openreview.net/forum?id=IdluSNs3f6)

- **问题 / 瓶颈** · 不同 PDE 的解算子结构难共同逼近
- **核心创新 / 方法** · 在子层前后以输入权重聚散平行流，并用 Sinkhorn 投影混合
- **Baseline** · 既有多 PDE 预训练，名称待核
- **Benchmark** · 12 个 PDE 基准，相对 L2 误差及域内外微调
- **关键结果 / 消融** · 增加约 3% 参数，平均相对 L2 误差降低 40.9%
- **适用条件 / 局限** · 多流与算子简化之间的独立贡献待核

**可复用机制** · 等参数对照统一加宽与输入相关流变换，按 PDE 分组评估。

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

<a id="paper-139375"></a>

## AppCIF-Bench: An Application-Level Complex Instruction Following Benchmark for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139375) · [作者来源](https://openreview.net/forum?id=TxXrHtF43g)

- **问题 / 瓶颈** · 短指令评测难区分记忆干扰与规则推演失败
- **核心创新 / 方法** · 用长系统提示及可执行模拟器构造场景和两个难度轴
- **Baseline** · 十二种代表性语言模型
- **Benchmark** · 五场景 466 个条目，测严格满足率
- **关键结果 / 消融** · 严格满足率范围 1.1% 到 45.9%
- **适用条件 / 局限** · 局限于模拟器规则与所测场景

**可复用机制** · 用正交难度设计定位复杂指令失败来自跨度还是规则深度。

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

<a id="paper-150027"></a>

## Approximate Bayesian inference with exchangeable distributions for neurosymbolic AI

[官方论文页](https://neurips.cc/virtual/2026/poster/150027) · [作者来源](https://openreview.net/forum?id=lK0AUkECXy)

- **问题 / 瓶颈** · 通用变分方法难处理复杂离散符号域
- **核心创新 / 方法** · 将问题化为后验推断，结合可交换分布与符号结构约束变分族
- **Baseline** · 通用变分推断和序贯 Monte Carlo
- **Benchmark** · 神经符号的结构与统计保证设定，实证待核
- **关键结果 / 消融** · 作者报告可保留测试时统计保证，具体形式待核
- **适用条件 / 局限** · 可交换假设及可推断规模须核查

**可复用机制** · 选择变分族时先识别符号对称性，同时验证近似误差与保证。

<a id="paper-148884"></a>

## Approximate Envy-Free Allocations  up to any k Goods

[官方论文页](https://neurips.cc/virtual/2026/poster/148884) · [作者来源](https://openreview.net/forum?id=uTA7e7Me8B)

- **问题 / 瓶颈** · 严格无嫉妒近似保证在较多代理时受限
- **核心创新 / 方法** · 推广 3PA 算法并分析图定向可行性
- **Baseline** · 既有 3PA 与少人数近似 EFX
- **Benchmark** · 加性估值下的存在性和多项式可计算性
- **关键结果 / 消融** · 作者给出任意人数的 3/4-EF2X，以及八人的 2/3-EFX
- **适用条件 / 局限** · 依赖加性估值，图定向另有难度

**可复用机制** · 当分配方案失效时，明确区分公平容差和可忽略物品数。

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

<a id="paper-152873"></a>

## Approximation Algorithms for GPU Pricing under Finite Capacity

[官方论文页](https://neurips.cc/virtual/2026/poster/152873) · [作者来源](https://openreview.net/forum?id=PjMPnWAPNr)

- **问题 / 瓶颈** · 需求和占用时间异质时线性价格收益可能很差
- **核心创新 / 方法** · 用容量松弛凸规划求全局菜单，租赁时耦合时段并随机节流
- **Baseline** · 线性价格和最优匿名静态菜单
- **Benchmark** · 销售和租赁的理论近似保证及模拟
- **关键结果 / 消融** · 小需求条件下销售达到 (1−ε)/2 近似，租赁为 (1−ε)/4
- **适用条件 / 局限** · 依赖模型设定和需求相对容量的上界

**可复用机制** · 制定固定资源菜单时，将容量和持有时间纳入定价对照。

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

<a id="paper-155734"></a>

## Approximation of Maximally Monotone Operators : A Graph Convergence Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/155734) · [作者来源](https://openreview.net/forum?id=3LWdbECcwo)

- **问题 / 瓶颈** · 逐点或积分误差难表达多值算子在跳变处的关系。
- **核心创新 / 方法** · 采用局部 Painlevé–Kuratowski 图收敛，并通过预解式参数化保持极大单调性。
- **Baseline** · 理论对照一致逼近及 Lp 逼近。
- **Benchmark** · 极大单调算子的局部图收敛与结构保持。
- **关键结果 / 消融** · 证明可用连续编码器–解码器做局部图逼近，并可保持极大单调性。
- **适用条件 / 局限** · 证明限于所设算子类，实际有限模型规模和收敛速度待核。

**可复用机制** · 当目标是关系图而非单值函数时，跟踪图距离和结构约束，避免仅用点预测误差。

<a id="paper-149116"></a>

## APPSolver: Adaptive Patch Partitioning for Point-Wise Ship Flow Prediction on Unstructured Meshes

[官方论文页](https://neurips.cc/virtual/2026/poster/149116) · [作者来源](https://openreview.net/forum?id=slRT3ex527)

- **问题 / 瓶颈** · 全局均匀图块对高变化区域过粗，对远场过细。
- **核心创新 / 方法** · 靠近船体及尾流细分、远场合并，将自适应图块送入 Transformer 预测一步速度与压力。
- **Baseline** · 对照其他 ShipBench 模型及图块压缩消融。
- **Benchmark** · ShipBench 一步时序推进，用 MAE、MSE，另测留出船体。
- **关键结果 / 消融** · 作者报告 MAE、MSE 最低，条件 token 在部分未知船体上有收益。
- **适用条件 / 局限** · 证据集中在船体流动与一步预测，长时滚动稳定性待核。

**可复用机制** · 固定 token 预算，对比按物理变化分区与均匀划分，并分别测近场和远场误差。

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

<a id="paper-155583"></a>

## A Principled Optimal Transport Framework for Frame Selection in Long Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/155583) · [作者来源](https://openreview.net/forum?id=4XADBFGyMq)

- **问题 / 瓶颈** · 逐帧得分可能集中于少数片段而丢掉视频上下文。
- **核心创新 / 方法** · 用非平衡熵正则最优传输做软匹配，再以动态规划选覆盖合理的帧子集。
- **Baseline** · 三类长视频任务中的免训练选帧方法；理论联系 Q-Frame。
- **Benchmark** · 三项长视频理解基准，比较固定预算下的理解质量。
- **关键结果 / 消融** · 作者报告三项均改善，并证明单源时导出 Gibbs 型权重。
- **适用条件 / 局限** · 依赖帧和查询表示，时间预算及运行开销具体数值待核。

**可复用机制** · 在固定帧数下分开消融相关性评分和覆盖优化。

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

<a id="paper-154567"></a>

## A probabilistic model of visual segmentation explains early visual cortical dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/154567) · [作者来源](https://openreview.net/forum?id=CdtOCPVGrR)

- **问题 / 瓶颈** · 自然场景中的皮层动态有异质性，统一增益或变异衰减曲线可能掩盖其组织方式。
- **核心创新 / 方法** · 建立自然图像分割概率模型，将推断出的分割结构关联到增益和变异衰减。
- **Baseline** · 对照经典单神经元实验规律。
- **Benchmark** · 自然图像推断及视觉皮层动态，具体数据和指标待核。
- **关键结果 / 消融** · 作者报告再现经典效应，并预测群体层异质性与分割结构相关。
- **适用条件 / 局限** · 群体级预测的跨模态实证仍需核查。

**可复用机制** · 检验层级视觉模型时并行比较单元平均与按推断对象分组后的动态。

<a id="paper-139068"></a>

## A Process-Level Evaluation of LLM Discovery Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139068) · [作者来源](https://openreview.net/forum?id=nATPxisXJo)

- **问题 / 瓶颈** · 最终分数相同可能掩盖模型在搜索过程中的不同策略。
- **核心创新 / 方法** · 在不同模型与框架的全交叉实验中采集轨迹并构建过程评分。
- **Baseline** · 六种语言模型与四类框架。
- **Benchmark** · 24 项发现任务和 1,728 条轨迹，对比里程碑和最终分数。
- **关键结果 / 消融** · 框架收益强依赖任务，同分模型也呈现不同搜索行为。
- **适用条件 / 局限** · 任务筛选与轨迹编码规则影响结论，跨任务族证据待核实。

**可复用机制** · 框架选型时对同任务记录探索行为和阶段完成度，检查终局分数能否解释过程差异。

<a id="paper-148839"></a>

## A Provably Convergent and Practical Algorithm for Gromov–Wasserstein Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/148839) · [作者来源](https://openreview.net/forum?id=umKsf7P52m)

- **问题 / 瓶颈** · 不精确投影的传统停止条件可能依赖不可得的准确投影。
- **核心创新 / 方法** · 在投影梯度中使用可验证残差，再随迭代衰减投影容差。
- **Baseline** · 比较需要不可得精确投影或缺少收敛保证的投影方案。
- **Benchmark** · 理论考察驻点收敛及全序列收敛，实测设置待核。
- **关键结果 / 消融** · 证明子序列收敛，附加容差衰减条件时得到全序列收敛。
- **适用条件 / 局限** · 只保证驻点；容差与单步投影开销仍需权衡。

**可复用机制** · 用可观测残差替代需精确解的内部终止条件，并校验其容差衰减。

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

<a id="paper-139036"></a>

## AptaBench: A Benchmark for Aptamer-Small Molecule Binding

[官方论文页](https://neurips.cc/virtual/2026/poster/139036) · [作者来源](https://openreview.net/forum?id=oki2P3XNXN)

- **问题 / 瓶颈** · 随机划分可能让测试实体与训练集重合，夸大泛化效果。
- **核心创新 / 方法** · 用实体不重叠的拆分比较配对任务的泛化表现。
- **Baseline** · 随机切分与实体不重叠切分。
- **Benchmark** · 分类和连续回归，比较切分方式变化后的表现。
- **关键结果 / 消融** · 作者报告连续回归的拟合优度在互斥设定下从 0.65 降至约 0.30。
- **适用条件 / 局限** · 结果受标签质量及样本覆盖影响。

**可复用机制** · 对配对任务分别测左侧、右侧和双侧新实体场景，并报告相对随机拆分的差距。

<a id="paper-139706"></a>

## AQBENCH: Benchmarking Neural Surrogates for Air Quality Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/139706) · [作者来源](https://openreview.net/forum?id=9VdHenNk02)

- **问题 / 瓶颈** · 通用 PDE 榜单排名不能反映真实空气质量长期预报与超标识别。
- **核心创新 / 方法** · 将多时域误差、超标、极端事件与物理残差放入同一评测，并比较联合与独立训练。
- **Baseline** · 比较谱神经算子、Transolver 等，并对照多污染物和单污染物。
- **Benchmark** · AQBENCH，168 小时 RMSE、超标检测、极端偏差及平流扩散残差。
- **关键结果 / 消融** · 谱算子在 168 小时 RMSE 落后；联合训练让 Transolver 的 168 小时表现改善 21%。
- **适用条件 / 局限** · 证据限于所用空气质量数据与任务，不自动外推其他 PDE。

**可复用机制** · 部署选择按预警指标和时域分别排行，核查联合训练是否改善尾部错误。

<a id="paper-152125"></a>

## A Quantitative Visual Taxonomy of Worldwide Writing Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/152125) · [作者来源](https://openreview.net/forum?id=VLPMAYjWxj)

- **问题 / 瓶颈** · 脚本视觉近似可能来自外形收敛，而非共同历史。
- **核心创新 / 方法** · 构造全球书写系统视觉分类并用受控扰动及外部时空元数据检验。
- **Baseline** · 传统谱系与独立地理、时间元数据。
- **Benchmark** · 全球文字字形，测结构扰动稳定性与外部相关性。
- **关键结果 / 消融** · 作者报告结构对扰动稳定，与时空元数据呈中等相关，并发现跨谱系视觉关联。
- **适用条件 / 局限** · 视觉证据不能单独证明历史传播或谱系联系。

**可复用机制** · 把历史解释建立在外部元数据佐证上，同时记录无谱系联系的视觉近邻。

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

<a id="paper-153989"></a>

## ARCANA: A Benchmark for Abstraction and Analogical Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/153989) · [作者来源](https://openreview.net/forum?id=H30SaXZgYu)

- **问题 / 瓶颈** · 熟悉或表面相似任务难暴露模型在远类比中的错误。
- **核心创新 / 方法** · 用 ARCANA 对照不同抽象距离，并通过概念转换、内省和反思框架做干预。
- **Baseline** · 基础语言模型、人类和带 ConceptSIR 的模型。
- **Benchmark** · ARCANA 抽象类比题和人类对照。
- **关键结果 / 消融** · 作者观察到模型与人类仍有差距，而框架能解开部分原本失败的题。
- **适用条件 / 局限** · 评测任务分布及反思带来的额外计算需独立比较。

**可复用机制** · 比较提示策略时按类比距离分桶并匹配推理预算。

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

<a id="paper-153718"></a>

## Archimedean Copula Inference via Taylor-Mode AD

[官方论文页](https://neurips.cc/virtual/2026/poster/153718) · [作者来源](https://openreview.net/forum?id=JHPRlItZ0c)

- **问题 / 瓶颈** · 手写高阶导数使新生成函数和删失数据的似然实现成本高。
- **核心创新 / 方法** · 将生成函数的多阶导数整合到可微计算，以同一接口支持用户定义生成函数与删失机制。
- **Baseline** · 对照已有专用密度计算及多种传统 copula 家族。
- **Benchmark** · 模拟、MIMIC-IV、标普行业收益和视网膜病变数据；测拟合和单密度耗时。
- **关键结果 / 消融** · 作者报告 35 维约 650 倍单密度加速，并展示最高 8,000 维计算。
- **适用条件 / 局限** · 速度受维度、家族、实现与硬件影响；生成函数合法性仍需验证。

**可复用机制** · 将高阶似然导数集中到自动微分接口，对照数值精度与维度扩展曲线。

<a id="paper-150185"></a>

## Architecture-Embedded Physics Priors for Mitigating Spectral Bias in Physics-Informed Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/150185) · [作者来源](https://openreview.net/forum?id=k4m1F3R3m4)

- **问题 / 瓶颈** · PINN 容易欠拟合偏微分方程解的高频分量。
- **核心创新 / 方法** · 联合学习有界坐标变形、残差驱动的傅里叶注意力和低频调节高频的门控。
- **Baseline** · 七种 PINN 对照，具体名称和训练预算待核。
- **Benchmark** · Helmholtz、波动、Klein–Gordon 和 Burgers 正问题，另有 Burgers 反演与地震重建。
- **关键结果 / 消融** · 作者报告精度改善、伪影减少，摘要未给幅度及独立消融。
- **适用条件 / 局限** · 需要可求的方程残差；不同模块能否独立迁移仍需核实。

**可复用机制** · 若方程已知但网络漏掉高频结构，可对照用残差信号选内部频带和只在输出端加残差损失。

<a id="paper-154160"></a>

## ArcMark: Distortion-Free Multi-Byte LLM Watermark via Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/154160) · [作者来源](https://openreview.net/forum?id=FoM8DBv8MZ)

- **问题 / 瓶颈** · 多比特水印沿用逐 token 编码，短文本的载荷与恢复可靠性受限。
- **核心创新 / 方法** · 将保持下一 token 分布的水印建模为信道编码问题，用容量界指导多字节编码与传输。
- **Baseline** · 多比特无失真水印和无水印模型输出。
- **Benchmark** · 短文本消息恢复、局部文本修改后的恢复，以及困惑度和下游任务质量。
- **关键结果 / 消融** · 作者报告数百 token 可嵌入多字节，恢复更准且质量可比；数值与模型待全文核对。
- **适用条件 / 局限** · 保持边缘分布不保证所有编辑后可恢复；容量依赖模型生成分布。

**可复用机制** · 设计来源标识时在固定文本长度和质量预算下扫描载荷，并分开报告原文与编辑后恢复率。

<a id="paper-139079"></a>

## Are Agents Ready to Teach? A Multi-Stage Benchmark for Real-World Teaching Workflows

[官方论文页](https://neurips.cc/virtual/2026/poster/139079) · [作者来源](https://openreview.net/forum?id=mTPfMFHAm7)

- **问题 / 瓶颈** · 答题或工具准确率无法覆盖识别学习状态、连续调整辅导和执行干预。
- **核心创新 / 方法** · 按教学理论构造任务，用多种验证信号与人工审核评估三类能力。
- **Baseline** · 多种前沿语言模型；摘要未列名。
- **Benchmark** · EduAgentBench 的 150 项任务，覆盖多轮辅导、教学判断和类似 Canvas 的流程。
- **关键结果 / 消融** · 作者观察到有界判断较可行，真实情境辅导和自主流程执行仍未达专业标准。
- **适用条件 / 局限** · 专业标准、人审一致性及其他教学系统上的迁移需复核。

**可复用机制** · 评测专业 agent 时把判断与执行拆开，同时在多轮任务中测观察和干预的闭环质量。

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

<a id="paper-150078"></a>

## A Refined Sample-Complexity Analysis of Robust Policy Optimization under Decaying Actor Stepsizes

[官方论文页](https://neurips.cc/virtual/2026/poster/150078) · [作者来源](https://openreview.net/forum?id=ktgqkymXsp)

- **问题 / 瓶颈** · 每次高精度稳健评估代价高
- **核心创新 / 方法** · 局部分析显示条件偏差随估计误差二次缩小
- **Baseline** · 控制完整一阶 critic 误差的分析
- **Benchmark** · KL 稳健策略的样本复杂度
- **关键结果 / 消融** · 目标误差 ε 对应 critic 均方误差同阶要求
- **适用条件 / 局限** · 局部且依赖步长条件

**可复用机制** · 按最终更新实际依赖的偏差而非原始误差设精度

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

<a id="paper-139570"></a>

## Are LLMs Good at Feature Engineering? Evidence from a Controlled Synthetic Benchmark

[官方论文页](https://neurips.cc/virtual/2026/poster/139570) · [作者来源](https://openreview.net/forum?id=HuY0OF2zX6)

- **问题 / 瓶颈** · 独立同分布划分掩盖时间伪相关
- **核心创新 / 方法** · 同步生成可观测数据和 Oracle 充分特征
- **Baseline** · 不做特征工程及不同 LLM 流程
- **Benchmark** · TabGen 合成时序表格
- **关键结果 / 消融** · 漂移下许多方法低于无特征工程基线
- **适用条件 / 局限** · 合成机制的外部效度待验

**可复用机制** · 保留已知上界并按时间划分检验加工特征的迁移

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

<a id="paper-151320"></a>

## Arena-T2I Hard: Benchmarking and Improving Faithfulness with Dependency-Aware Checklist Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/151320) · [作者来源](https://openreview.net/forum?id=bNK3Svyy8O)

- **问题 / 瓶颈** · 整体偏好常掩盖细粒度不忠实
- **核心创新 / 方法** · 将约束拆成有向无环图，父约束失败时置零子项
- **Baseline** · 整体 Bradley–Terry 偏好
- **Benchmark** · 310条提示、11个系统
- **关键结果 / 消融** · 最强系统0.855，系统差距33个百分点
- **适用条件 / 局限** · 依赖分解及视觉评判可靠性

**可复用机制** · 将父子条件纳入生成奖励并分开看审美与忠实性

<a id="paper-139813"></a>

## A Reproducible Evaluation Protocol for Quantum Non-Linearity in Variational Quantum Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139813) · [作者来源](https://openreview.net/forum?id=37XAXg90Dc)

- **问题 / 瓶颈** · 单一表现数值掩盖表达和训练的差别
- **核心创新 / 方法** · 分别测频率、梯度方差、训练效率和噪声稳定
- **Baseline** · 六种变分结构及经典和混合模型
- **Benchmark** · 含混沌动力任务及退极化噪声
- **关键结果 / 消融** · 作者报告单指标掩盖的能力差异
- **适用条件 / 局限** · 综合排名受权重与噪声设置影响

**可复用机制** · 选择电路时把非线性表达与训练稳定分开评估

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

<a id="paper-152084"></a>

## Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152084) · [作者来源](https://openreview.net/forum?id=VbY7iyZuyN)

- **问题 / 瓶颈** · 固定高档成本大，固定低档易失效
- **核心创新 / 方法** · 基于历史用轻量路由预测步骤所需档位
- **Baseline** · 固定高低档及随机选择
- **Benchmark** · TAU-Bench、BrowseComp-Plus、WebArena
- **关键结果 / 消融** · 推理token最多降低52.7%
- **适用条件 / 局限** · 依赖可调档模型与成功标注

**可复用机制** · 通过逐步成功对照为路由构造最小算力标签

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

<a id="paper-139397"></a>

## Are Text-to-Image Models Inductivist Turkeys? A Counterfactual Benchmark for Causal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139397) · [作者来源](https://openreview.net/forum?id=TD8M73M2nz)

- **问题 / 瓶颈** · 看似合理的图像可能只复现常见相关性
- **核心创新 / 方法** · 按事实、显式反事实与隐式反事实组织任务
- **Baseline** · 多种开源及闭源模型
- **Benchmark** · CF-World，先验抵抗及推理保留率
- **关键结果 / 消融** · 作者报告反事实设置普遍退化
- **适用条件 / 局限** · 依赖视觉评判质量

**可复用机制** · 通过移除显式视觉提示估计模型遵循新规则的能力

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

<a id="paper-139747"></a>

## Are We Making Progress in Multimodal Domain Generalization? A Comprehensive Benchmark Study

[官方论文页](https://neurips.cc/virtual/2026/poster/139747) · [作者来源](https://openreview.net/forum?id=6tWrq9LvUT)

- **问题 / 瓶颈** · 数据与模态设置不统一使排行难比较
- **核心创新 / 方法** · 固定划分及模态组合，增加缺失与损坏诊断
- **Baseline** · ERM及九种代表方法
- **Benchmark** · 六数据集、95个跨域任务
- **关键结果 / 消融** · 作者报告专用方法较ERM改善边际，且无方法普遍占优
- **适用条件 / 局限** · 覆盖限三类任务

**可复用机制** · 先对齐评测协议，再分开比较缺失、损坏与分布外检测

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

<a id="paper-152732"></a>

## ARGUS: Stacked Multi-View Identity Mosaic Injection for Subject-Preserving Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152732) · [作者来源](https://openreview.net/forum?id=Qlic1VUQ6h)

- **问题 / 瓶颈** · 单帧参考在转身和遮挡时易漂移
- **核心创新 / 方法** · 将九个局部视图拼成前缀条件，在结构形成期注入身份并自适应调节引导
- **Baseline** · Wan 2.1 底座，比较 Hailuo、VACE-14B 等
- **Benchmark** · OpenS2V-Eval、HardID-Celeb 及 47 人盲评
- **关键结果 / 消融** · 作者报告七项指标中五项领先
- **适用条件 / 局限** · 需多视角且对齐参考，视图数量的独立贡献待核

**可复用机制** · 对比多视角和单帧条件，并分别测遮挡、转身及参考复制

<a id="paper-155756"></a>

## ARK: A Dual-Axis Multimodal Retrieval Benchmark along Reasoning and Knowledge

[官方论文页](https://neurips.cc/virtual/2026/poster/155756) · [作者来源](https://openreview.net/forum?id=3BQmlx6S58)

- **问题 / 瓶颈** · 总体检索分数会掩盖视觉空间推理失败
- **核心创新 / 方法** · 按知识领域和推理技能交叉分层，并构造针对性难负例
- **Baseline** · 26 种文本及多模态检索器，另测重排序与改写
- **Benchmark** · ARK，覆盖 16 种视觉数据类型
- **关键结果 / 消融** · 细粒度视觉与空间推理仍弱，检索增强有收益
- **适用条件 / 局限** · 结论依赖难负例质量，具体分数待核

**可复用机制** · 在固定语料上按推理类型报告召回，防止语义捷径虚增表现

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

<a id="paper-155396"></a>

## Articraft: An Agentic System for Scalable Articulated 3D Asset Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155396) · [作者来源](https://openreview.net/forum?id=5ygNle8IdK)

- **问题 / 瓶颈** · 直接生成资产缺少关节约束和反馈
- **核心创新 / 方法** · 用专用接口描述几何与关节，在受限工作区验收并回传结构化错误
- **Baseline** · 通用代码代理与关节资产生成器
- **Benchmark** · Articraft-10K、245 类及下游模拟应用
- **关键结果 / 消融** · 作者报告资产质量高于对照
- **适用条件 / 局限** · 类别和验证规则的覆盖限制产出

**可复用机制** · 先将生成任务压缩到类型化接口，再对照有无执行反馈

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

<a id="paper-151805"></a>

## Artificial Aphasias in Lesioned Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151805) · [作者来源](https://openreview.net/forum?id=Xt1WIN9XQN)

- **问题 / 瓶颈** · 总体性能下降无法说明哪些语言功能受损
- **核心创新 / 方法** · 屏蔽指定参数后用文本失语量表比较症状分布
- **Baseline** · 层深、注意力和前馈投影及人类症状分布
- **Benchmark** · 五个十亿级模型、112426 条输出
- **关键结果 / 消融** · 不同模块和深度出现不同症状，且总体分布与人类不同
- **适用条件 / 局限** · 人工损伤不等于临床病理

**可复用机制** · 逐模块干预后报告错误谱，检查相同平均下降是否来自不同机制

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

<a id="paper-148550"></a>

## ASAP: Assembly-Source Aligned Pseudocode Refinement For Binary Decompilation

[官方论文页](https://neurips.cc/virtual/2026/poster/148550) · [作者来源](https://openreview.net/forum?id=x36xk9UY3Z)

- **问题 / 瓶颈** · 伪代码文本可读并不代表忠实于二进制语义
- **核心创新 / 方法** · 以原始低层表示为补充证据并测试改写输出的功能保真
- **Baseline** · 最强反编译改写对照，名称待核
- **Benchmark** · 两个反编译基准及多种编译优化级别
- **关键结果 / 消融** · 重执行率 64.7% 到 71.9%，重编译率 91.6% 到 96.6%
- **适用条件 / 局限** · 依赖测试覆盖，重编译成功并不证明功能等价

**可复用机制** · 代码恢复评估同时测编译、重执行及未覆盖路径

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

<a id="paper-149834"></a>

## A Scalable Multi-Task Model for Virtual Sensors

[官方论文页](https://neurips.cc/virtual/2026/poster/149834) · [作者来源](https://openreview.net/forum?id=mxCxGqU9Yz)

- **问题 / 瓶颈** · 独立虚拟传感器需手选输入且无法共享任务信息
- **核心创新 / 方法** · 联合预测多个目标并学习各目标相关的输入信号
- **Baseline** · 独立单任务及统一模型
- **Benchmark** · 三个基准和超过 180 亿样本的应用数据
- **关键结果 / 消融** · 作者报告相对统一对照最高节省 415 倍计算时间和 951 倍内存
- **适用条件 / 局限** · 极值依赖硬件和基线，配置待核

**可复用机制** · 对多目标传感估计比较共享与独立结构，并测任务数增长成本

<a id="paper-151002"></a>

## A Scalable Nonparametric Continuous-Time Survival Model through Numerical Quadrature

[官方论文页](https://neurips.cc/virtual/2026/poster/151002) · [作者来源](https://openreview.net/forum?id=dfT2nmqW27)

- **问题 / 瓶颈** · 连续生存似然的积分限制灵活建模
- **核心创新 / 方法** · 用 Gauss–Legendre 求积处理累计风险，并按时间做低秩权重调节
- **Baseline** · 生存建模对照，具名方法待核
- **Benchmark** · 合成、真实表格和医学图像任务
- **关键结果 / 消融** · 作者给出积分误差界并报告瞬时风险估计优势
- **适用条件 / 局限** · 求积点数和风险函数光滑性影响误差

**可复用机制** · 让积分误差和预测误差分别进入连续时间模型验收

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

<a id="paper-149737"></a>

## AsdaKV: Attention-Overlap Driven Semantic KV Retrieval for Long-Context LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149737) · [作者来源](https://openreview.net/forum?id=njapeOwRUM)

- **问题 / 瓶颈** · 固定页与模型实际历史依赖边界不一致
- **核心创新 / 方法** · 用相邻解码的注意力重叠检测漂移，组织可变窗口并保留 GPU 定额缓存
- **Baseline** · 已有 KV 检索办法，名称待核
- **Benchmark** · 多任务、多模型长输入与长输出比较
- **关键结果 / 消融** · 作者报告同缓存预算下准确率提高，长输入速度可比
- **适用条件 / 局限** · 依赖 CPU 带宽、注意力探针与阈值

**可复用机制** · 按注意力漂移刷新并与固定刷新周期比较命中与吞吐

<a id="paper-153089"></a>

## A second order regret bound for NormalHedge

[官方论文页](https://neurips.cc/virtual/2026/poster/153089) · [作者来源](https://openreview.net/forum?id=O42j6ibmbL)

- **问题 / 瓶颈** · 易序列上的最坏情形界过松
- **核心创新 / 方法** · 以随机连续时间极限启发 NormalHedge 变体
- **Baseline** · 原 NormalHedge 家族
- **Benchmark** · 专家建议；ε分位遗憾
- **关键结果 / 消融** · 当 V_T 超过 log N 时，界为 O(√(V_T log(V_T/ε)))
- **适用条件 / 局限** · 依赖算法加权二阶矩及阈值

**可复用机制** · 遇到易序列时用可观测方差界评估在线专家混合。

<a id="paper-153290"></a>

## A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/153290) · [作者来源](https://openreview.net/forum?id=MMhankfnpV)

- **问题 / 瓶颈** · 低信息密度输出冲淡错误与路径
- **核心创新 / 方法** · 跨任务存储由轨迹提炼的规则并按任务调整
- **Baseline** · 静态规则及摘要压缩
- **Benchmark** · TerminalBench 两版、SWE-Bench Lite 等六基准
- **关键结果 / 消融** · 常规成功率增 1–4 点，下游 token 省 12–27%
- **适用条件 / 局限** · 依赖关键证据未被删；对照细项待核

**可复用机制** · 压缩日志时区分必须逐字保留的字段与可过滤噪声。

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

<a id="paper-148413"></a>

## A Set-Sequence Model for Time Series

[官方论文页](https://neurips.cc/virtual/2026/poster/148413) · [作者来源](https://openreview.net/forum?id=y1ZoyGsVuL)

- **问题 / 瓶颈** · 固定跨单元通道无法应对成员数量变化
- **核心创新 / 方法** · 集合编码群体后，将摘要条件化到单元各自序列模型
- **Baseline** · 独立时序骨干与领域对照
- **Benchmark** · 传染模拟、股票组合及贷款风险；Sharpe、AUC
- **关键结果 / 消融** · 作者报告两实证指标改善
- **适用条件 / 局限** · 共享摘要可能忽略细粒度交互

**可复用机制** · 对动态成员场景同时测排列不变性和换规模表现。

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

<a id="paper-156125"></a>

## A Simple Class-Agnostic Approach to Enhance Fair Adversarial Training

[官方论文页](https://neurips.cc/virtual/2026/poster/156125) · [作者来源](https://openreview.net/forum?id=0Cyh5Wvx03)

- **问题 / 瓶颈** · 大类别集逐类估权样本不足
- **核心创新 / 方法** · 可靠性门控抑制离群、优先边界难例、降权已稳健样本
- **Baseline** · 按类别调权的对抗训练
- **Benchmark** · 最坏类稳健性及干净准确率；具名基准待核
- **关键结果 / 消融** · 作者报告最坏类改善并保持干净准确率
- **适用条件 / 局限** · 难例分组可靠性与数值待核

**可复用机制** · 用于防御时报告最坏组指标及高难度区间的训练收益。

<a id="paper-155687"></a>

## A simple model of co-emergence of grid and place fields

[官方论文页](https://neurips.cc/virtual/2026/poster/155687) · [作者来源](https://openreview.net/forum?id=3gP67zjrHg)

- **问题 / 瓶颈** · 分开建模难解释两类空间细胞共同形成
- **核心创新 / 方法** · 用满足兴奋抑制约束的递归网络预测下一感觉观测
- **Baseline** · 以某一空间细胞为先验或单独涌现的模型
- **Benchmark** · 1000 种训练配置和多类空间场景
- **关键结果 / 消融** · 两类代码共现，比例随噪声与遮蔽变化，并定性复现多个观察
- **适用条件 / 局限** · 属于模型证据，神经因果待验证

**可复用机制** · 同时检查缺失观测重构与动态预测对空间表示的影响。

<a id="paper-155069"></a>

## A Simple Unigram Cross-Entropy Lens on the Lexical Imprint of Pre-training Data

[官方论文页](https://neurips.cc/virtual/2026/poster/155069) · [作者来源](https://openreview.net/forum?id=8hN2Bcw0x2)

- **问题 / 瓶颈** · 语料效果难和训练配方分离
- **核心创新 / 方法** · 固定配方预训练，扫描语料对齐并用于文档选择与推测解码路由
- **Baseline** · 随机同规模取样、重要性重采样、通用草稿模型
- **Benchmark** · 11 个基准、4 种语料、3 种规模
- **关键结果 / 消融** · 对齐跟踪所有基准准确率，并改善筛选及路由
- **适用条件 / 局限** · 只量词汇分布，不能代替语义或污染检查

**可复用机制** · 在固定训练预算下将词汇对齐作为低成本对照。

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

<a id="paper-154912"></a>

## A Single-Sample Polylogarithmic Regret Bound for Nonstationary Online Linear Programming

[官方论文页](https://neurips.cc/virtual/2026/poster/154912) · [作者来源](https://openreview.net/forum?id=A03IL03XrS)

- **问题 / 瓶颈** · 需求随时间变化且接受决策不可撤销
- **核心创新 / 方法** · 结合动态规划与对偶方法的重解
- **Baseline** · 平稳在线线性规划分析
- **Benchmark** · 独立非同分布请求，每个未来分布一独立样本；遗憾
- **关键结果 / 消融** · 资源线性增长时遗憾 O(log² n)
- **适用条件 / 局限** · 要求大资源与独立性，常数细节待核

**可复用机制** · 在日志有限的入场控制中显式检查预算规模和工作负载变化。

<a id="paper-150558"></a>

## Ask, Answer, and Detect: Role-Playing LLMs for Personality Detection with Question-Conditioned Mixture-of-Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/150558) · [作者来源](https://openreview.net/forum?id=hFHitNXO1g)

- **问题 / 瓶颈** · 稀疏标签不足以把自由文本对齐到抽象构念
- **核心创新 / 方法** · 生成问卷式辅助目标，以问题条件专家和多任务训练融合表示
- **Baseline** · 直接编码文本分类及具名模型待核
- **Benchmark** · Kaggle、Pandora 人格标签
- **关键结果 / 消融** · 相对提升13.60%与19.72%
- **适用条件 / 局限** · 生成回答并非真实自评；隐私、公平和效度须单测

**可复用机制** · 抽象标签任务可对照问题级辅助监督，独立验证其真实性。

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

<a id="paper-149860"></a>

## Ask in the Crowd: Differentially Private LLM Inference via Dummy-Augmented Shuffling

[官方论文页](https://neurips.cc/virtual/2026/poster/149860) · [作者来源](https://openreview.net/forum?id=mitOdW71vU)

- **问题 / 瓶颈** · 输入嵌入加噪会降低效用
- **核心创新 / 方法** · 客户端混洗真实与掩护查询，复用共享前缀缓存
- **Baseline** · 明文推理及嵌入加噪方法
- **Benchmark** · 分类、生成及查询隐私评测
- **关键结果 / 消融** · 作者报告效用接近明文且延迟可用
- **适用条件 / 局限** · 保证依赖威胁模型和掩护分布

**可复用机制** · 在固定隐私预算下同时测效用、延迟和服务端可观察信息。

<a id="paper-155386"></a>

## Ask KG Agent: A Multi-Agent Framework for Code Localization Using Code and Knowledge Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/155386) · [作者来源](https://openreview.net/forum?id=62XPovBV57)

- **问题 / 瓶颈** · 代码结构不表达历史设计缘由
- **核心创新 / 方法** · 结合依赖与设计历史知识图进行缺陷位置检索
- **Baseline** · 12 种代码定位方法
- **Benchmark** · 软件问题到代码位置的检索
- **关键结果 / 消融** · 作者报告优于所有对照，幅度待核
- **适用条件 / 局限** · 历史稀少或过时时信号受限

**可复用机制** · 比较仅当前代码与加入历史检索后的维护定位命中率。

<a id="paper-139593"></a>

## ASO Atlas 2.0: Evaluating antisense oligonucleotide prediction across the preclinical pipeline

[官方论文页](https://neurips.cc/virtual/2026/poster/139593) · [作者来源](https://openreview.net/forum?id=GVCHxvTflc)

- **问题 / 瓶颈** · 平均准确率会掩盖昂贵阶段的小幅改善
- **核心创新 / 方法** · 将分阶段筛选表现转化成模拟流程成本
- **Baseline** · 仅按准确率排序
- **Benchmark** · 代表性多阶段工作流模拟
- **关键结果 / 消融** · 作者报告成本排序和预测准确率排序反转
- **适用条件 / 局限** · 节省是模型投影，依赖单位成本及流程假设

**可复用机制** · 多阶段实验先做成本敏感性分析，再决定优先改进哪个阶段。

<a id="paper-154777"></a>

## A Solvable Model of Chain-of-Thought in In-Context Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154777) · [作者来源](https://openreview.net/forum?id=B3HqjP2biY)

- **问题 / 瓶颈** · 加深推理可能放大估计误差
- **核心创新 / 方法** · 在线性回归中将推理建模为参数迭代，解析深度、训练量和上下文关系
- **Baseline** · 不同推理深度和信息预算
- **Benchmark** · 线性回归理论、线性及 softmax 注意力实验
- **关键结果 / 消融** · 刻画快速改善、慢改善、饱和与过度推理的相变
- **适用条件 / 局限** · 理论依赖高维线性设定

**可复用机制** · 评测推理预算时同时扫描信息量和步数。
