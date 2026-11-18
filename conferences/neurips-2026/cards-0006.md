# NeurIPS 2026 论文卡 6

[会议索引](README.md)

<a id="paper-152020"></a>

## From Generation to Restoration: Residual Diffusion for Neural Channel Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/152020) · [作者来源](https://openreview.net/forum?id=W6pSRJD1gO)

- **问题 / 瓶颈** · 通用先验丢失接收信号已有的信息。
- **核心创新 / 方法** · 构造接收信号到干净码字的残差桥，以确定性概率流求解。
- **Baseline** · 已有神经解码器和常规扩散解码。
- **Benchmark** · 信道编码基准，比较解码和迭代开销。
- **关键结果 / 消融** · 作者报告相当或更好的解码表现且减少迭代。
- **适用条件 / 局限** · 码族及信道偏移影响待核。

**可复用机制** · 对恢复任务用观测作为生成起点，绘制跳步的准确率和延迟曲线。

<a id="paper-149657"></a>

## From Generic to Dedicated: A Novel Optimizer for Online Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149657) · [作者来源](https://openreview.net/forum?id=oReUobH6m9)

- **问题 / 瓶颈** · 单遍非平稳数据易导致遗忘。
- **核心创新 / 方法** · SPIN 插值快序列和稳定序列，理论连接逆 Hessian 近似及正则。
- **Baseline** · SGD、AdamW 等通用优化器。
- **Benchmark** · 在线持续学习，包括无回放和内存限制。
- **关键结果 / 消融** · 作者报告多个方法替换优化器后改善。
- **适用条件 / 局限** · 模型和漂移强度下的超参敏感性待核。

**可复用机制** · 固定缓存预算比较快慢参数插值和单一更新序列。

<a id="paper-155317"></a>

## From Groups to Rings: Causal Evidence for Algebraic Decomposition in Grokked Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/155317) · [作者来源](https://openreview.net/forum?id=6WDYFB6ALB)

- **问题 / 瓶颈** · 表示相关性不足以证明分量独立。
- **核心创新 / 方法** · 按 Wedderburn–Artin 分量交换内部表示，对照预测变化。
- **Baseline** · 机会水平及不同代数结构、模型容量。
- **Benchmark** · 11 个交换代数及非交换群，测交换干预准确率。
- **关键结果 / 消融** · 交换代数实验 IIA 至少 0.97，错误仍集中于分量，约为机会水平 3.8 倍。
- **适用条件 / 局限** · 证据限于所研究代数任务。

**可复用机制** · 事先指定结构分量，用干预检验错误是否跨分量传播。

<a id="paper-151117"></a>

## From Heartbeat to Cardiochoreography: A Mechanics Foundation Model for Individualized 4D Cardiac Motion Generation Conditioned on Electrophysiology

[官方论文页](https://neurips.cc/virtual/2026/poster/151117) · [作者来源](https://openreview.net/forum?id=crTTYgpAhR)

- **问题 / 瓶颈** · 同步采集的传感信号与运动响应仍可有物理滞后。
- **核心创新 / 方法** · 用可学习小波导出延迟感知条件，再生成个体心脏运动。
- **Baseline** · 通用运动扩散模型。
- **Benchmark** · UK Biobank 40577 人，评估运动恢复和个体多样性。
- **关键结果 / 消融** · 作者报告保留个体差异，而通用对照趋向总体均值。
- **适用条件 / 局限** · 为观察性重建研究，跨数据验证待核。

**可复用机制** · 对异步多传感重建比较固定对齐和可学习延迟条件，并统计个体差异保留。

<a id="paper-154254"></a>

## From History to State: Constant-Context Skill Learning for LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154254) · [作者来源](https://openreview.net/forum?id=F9AmFBisYk)

- **问题 / 瓶颈** · 长技能提示和不断增长的上下文推高推理成本。
- **核心创新 / 方法** · 确定性跟踪器渲染进度状态并给子目标奖励，任务族模块通过 SFT 和 RL 学流程。
- **Baseline** · 受控 ReAct 与已发表智能体训练方法。
- **Benchmark** · ALFWorld、WebShop、SciWorld。
- **关键结果 / 消融** · Qwen3-8B 分别达 89.6%、76.8%、66.4%，每轮提示 token 减少 2–7 倍。
- **适用条件 / 局限** · 依赖状态跟踪正确性和可复用任务族。

**可复用机制** · 在可观测流程中对照全历史与紧凑状态下的成功率和提示开销。

<a id="paper-154407"></a>

## From Ideas to Code: Tree-structured Policy Optimization for Automated Algorithm Design with LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154407) · [作者来源](https://openreview.net/forum?id=Doxqy5ndUy)

- **问题 / 瓶颈** · 只奖励最终结果无法区分思路与实现质量。
- **核心创新 / 方法** · ATPO 对树状采样的构想和实现分别估计组相对优势。
- **Baseline** · FunSearch、EoH、OpenEvolve 原版。
- **Benchmark** · 算法设计、未见任务实例和替代搜索方式。
- **关键结果 / 消融** · 作者报告集成后改善且能迁移。
- **适用条件 / 局限** · 不同树深和预算对效果的影响待核。

**可复用机制** · 多阶段生成允许多个实现共享同一构想时，分层估计信用。

<a id="paper-148563"></a>

## From Inexact Gradients to Byzantine Robustness: Acceleration and Optimization under Similarity

[官方论文页](https://neurips.cc/virtual/2026/poster/148563) · [作者来源](https://openreview.net/forum?id=wx2qpHOXO8)

- **问题 / 瓶颈** · 逐聚合器构建收敛证明难以推广到加速算法。
- **核心创新 / 方法** · 将鲁棒聚合抽象为不精确梯度预言机，分析额外梯度加速和辅助损失相似情形。
- **Baseline** · 既有拜占庭鲁棒分布式优化。
- **Benchmark** · 理论收敛界及通信复杂度实验。
- **关键结果 / 消融** · 作者报告最优渐近误差及更低通信复杂度。
- **适用条件 / 局限** · 需要满足聚合误差与相似性假设。

**可复用机制** · 比较不同防御聚合器时把误差界与外层优化器分析分离。

<a id="paper-153875"></a>

## From Intent to Evidence: A Categorical Approach for Structural Evaluation of Deep Research Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153875) · [作者来源](https://openreview.net/forum?id=I6Icjutm2f)

- **问题 / 瓶颈** · 总准确率无法区分检索、核验和合成失败。
- **核心创新 / 方法** · 把任务拆成跨跳检索、多源核对、碎片重排和反驳无据假设。
- **Baseline** · 16 个系统，及无结构化工具对照。
- **Benchmark** · 296 个双语问题，人工复核答案。
- **关键结果 / 消融** · 最好系统平均 19.9%，作者报告追踪式搜索和分类工具有增益。
- **适用条件 / 局限** · 小规模任务与人工判断的外推待验。

**可复用机制** · 对研究助手把证据路径与最终答案分别评分。

<a id="paper-154711"></a>

## From I/O to Code with Discovery Agent

[官方论文页](https://neurips.cc/virtual/2026/poster/154711) · [作者来源](https://openreview.net/forum?id=BZxrI7kEUy)

- **问题 / 瓶颈** · 仅凭输入输出时程序空间大且欠定。
- **核心创新 / 方法** · DIO-Agent 用执行误差信号引导候选修改，按复杂度逐级放宽构造。
- **Baseline** · 示例编程、演化搜索和等采样预算方法。
- **Benchmark** · IO2Code 多难度基准。
- **关键结果 / 消融** · 作者报告多种模型和各难度均优于对照。
- **适用条件 / 局限** · 少量可见样例不足以唯一确定语义。

**可复用机制** · 在普通算法题上比较复杂度课程与均匀采样，并以未见样例复测。

<a id="paper-152999"></a>

## From Isolated feature to Orbits:\\Discovering Music Concepts via Multi-SAE Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152999) · [作者来源](https://openreview.net/forum?id=OiLTPYgHYL)

- **问题 / 瓶颈** · 单独命名特征无法捕获音乐中的移调关系。
- **核心创新 / 方法** · 经移调构造配对输入，对齐多视角 SAE 表示得到有序轨道。
- **Baseline** · 以单特征定位为比较思路，具名对照待核。
- **Benchmark** · 两个音乐模型中识别和弦、调式与旋律结构。
- **关键结果 / 消融** · 作者报告少量锚点可解释整组概念。
- **适用条件 / 局限** · 依赖已知变换及足够稳定的特征。

**可复用机制** · 对已知对称群构造变换对，测表示中是否出现一致轨道。

<a id="paper-152949"></a>

## From Jumps to Signatures: a Generative Method for Temporal Point Processes

[官方论文页](https://neurips.cc/virtual/2026/poster/152949) · [作者来源](https://openreview.net/forum?id=PAf9lZ4UZW)

- **问题 / 瓶颈** · 逐事件损失不易捕获全局轨迹差异。
- **核心创新 / 方法** · 用事件间隔嵌入做稳定的连续路径提升，以签名训练并导出分布差异指标。
- **Baseline** · 既有生成时序点过程方法。
- **Benchmark** · 合成与真实数据集，八项互补指标。
- **关键结果 / 消融** · 平均排名最高，64% 数据集与指标组合优于或距最强对照一个标准误内。
- **适用条件 / 局限** · 依赖嵌入可辨识性和签名截断。

**可复用机制** · 在变长序列中比较局部预测损失和全路径分布匹配。

<a id="paper-152846"></a>

## From Label Priors to Task Evidence: Long-Video Frame Selection via Bayesian GRPO

[官方论文页](https://neurips.cc/virtual/2026/poster/152846) · [作者来源](https://openreview.net/forum?id=Pw7tnoVlx1)

- **问题 / 瓶颈** · 静态关键帧标签未必覆盖推理所需证据。
- **核心创新 / 方法** · 先用监督学习初始化显著性，再把冻结 MLLM 的负对数似然作为密集证据，以 Bayesian GRPO 更新。
- **Baseline** · 静态标注检索、重型 MLLM 打分器。
- **Benchmark** · Video-MME、MLVU、LongVideoBench；对照准确率和效率。
- **关键结果 / 消融** · 摘要报告匹配重型评分器准确率且维持轻量效率，数值待核。
- **适用条件 / 局限** · 训练绑定下游模型；换模型效果待验证。

**可复用机制** · 固定帧预算比较标签监督和下游任务证据监督。

<a id="paper-150517"></a>

## From Likelihood Convergence to Parameter Convergence in POMDPs

[官方论文页](https://neurips.cc/virtual/2026/poster/150517) · [作者来源](https://openreview.net/forum?id=hWP93Z7A1J)

- **问题 / 瓶颈** · POMDP 似然差小未直接说明潜在转移核恢复得好。
- **核心创新 / 方法** · 将参数误差界写为似然差、观测与转移核条件性及行为策略的函数，涵盖两种观测完备设定。
- **Baseline** · MLE、OMLE 型及其他控制似然差的方法均适用该结论。
- **Benchmark** · 有限样本 POMDP 参数恢复与状态奖励规划；经验基准待核。
- **关键结果 / 消融** · 理论分离覆盖和混合性与模型可辨识性的作用。
- **适用条件 / 局限** · 依赖核结构条件与合适数据覆盖；不可无条件外推。

**可复用机制** · 比较日志策略时除似然外记录核恢复、动作覆盖和混合速度。

<a id="paper-154680"></a>

## From Link Prediction to Linear Community Detection: A Finite-Sample Guarantee for Graph Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/154680) · [作者来源](https://openreview.net/forum?id=BoHltLOSMR)

- **问题 / 瓶颈** · 边预测成功能否转化为节点分类缺少定量解释。
- **核心创新 / 方法** · 在 SBM 中对有界 GNN 和对称双线性解码器证明条件归约，并构造 PSD 度量下的少标签近质心分类。
- **Baseline** · 理论以总体留出链路预测超额风险为起点；消融待核。
- **Benchmark** · 合成 SBM，考察边风险、分数误差及社区分类误差。
- **关键结果 / 消融** · 有界稠密设定中统计项为约根号 d/n；合成实验检验结论链。
- **适用条件 / 局限** · 结论依赖 SBM 和解码假设，最坏情况常数可能偏保守。

**可复用机制** · 考察边预训练时将优化、架构逼近与统计误差分别诊断。

<a id="paper-150953"></a>

## From Local Skills to Long-Horizon Tasks: Progressive Skill Exploration for LLM Web Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/150953) · [作者来源](https://openreview.net/forum?id=e3N4nXBwUe)

- **问题 / 瓶颈** · 稀疏终局奖励使随机探索难以获得可用反馈。
- **核心创新 / 方法** · SCOPE 从历史交互中提取技能和失败经验，编排技能链，用同链失败引导下一轮探索，再在线蒸馏。
- **Baseline** · 各测试环境中的最强所比基线；名称待核。
- **Benchmark** · WebArena、WebVoyager、WebShop 上的授权基准交互。
- **关键结果 / 消融** · 摘要报告相对提升 3.9% 至 18.6%。
- **适用条件 / 局限** · 依赖能稳定提取和组合子技能；跨站与运行开销待核。

**可复用机制** · 用可验证子任务建立短到长的课程，并按失败所属技能做诊断。

<a id="paper-154042"></a>

## From Local to Global: Progressive Consensus via Hierarchical Communication in Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154042) · [作者来源](https://openreview.net/forum?id=GfEY4lEw9W)

- **问题 / 瓶颈** · 局部视野限制全局理解，平铺通信有冗余。
- **核心创新 / 方法** · 按感知焦点分组，组内通信后由代表交换摘要，并用 KL 对齐共识、VAE 保留全局任务信息。
- **Baseline** · 通信式与共识式 MARL 方法；具名基线待核。
- **Benchmark** · 多智能体强化学习任务，比较任务难度与智能体规模。
- **关键结果 / 消融** · 作者报告优势在更困难和更大规模设置较明显。
- **适用条件 / 局限** · 依赖分组合理及代表可用，通信预算和消融待核。

**可复用机制** · 对照平铺与层级通信，固定带宽测回报和共识质量。

<a id="paper-155180"></a>

## From Matching to Reasoning: Query-Aware Long Video Summarization

[官方论文页](https://neurips.cc/virtual/2026/poster/155180) · [作者来源](https://openreview.net/forum?id=7iNfz7RRVW)

- **问题 / 瓶颈** · 局部相关度高的片段可能重复，无法拼出全局证据。
- **核心创新 / 方法** · 自回归生成查询条件摘要，联合建模跨段依赖、显著性和查询相关性。
- **Baseline** · 局部查询片段打分等方法；具名比较待核。
- **Benchmark** · LQVS 开放词汇长视频查询与预算约束抽取式摘要。
- **关键结果 / 消融** · 作者报告摘要表现及查询解耦度改善；数值待核。
- **适用条件 / 局限** · 效果受预算、片段切分及指标有效性影响。

**可复用机制** · 用相同视频的不同查询检查摘要是否真正随证据需求变化。

<a id="paper-154251"></a>

## From Matrix Inversion to Constraints: Provably Tighter Confidence Regions for Importance Weights in Label Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/154251) · [作者来源](https://openreview.net/forum?id=FA5NKoBbAJ)

- **问题 / 瓶颈** · 对区间矩阵求逆会放大重要性权重的置信区间。
- **核心创新 / 方法** · 保留原矩阵关系构造联合区域，以线性规划投影为边际区间。
- **Baseline** · 区间线性系统的消元或求逆法。
- **Benchmark** · AGNews、MNIST、CIFAR-10、N24News、nuImages；比较区间及预测集大小。
- **关键结果 / 消融** · 在有限样本有效性下给出更紧理论界，摘要报告实验区间更短。
- **适用条件 / 局限** · 依赖标签偏移假设，域间类条件分布变化时需重验。

**可复用机制** · 当目标参数受线性矩阵关系约束时，比较原空间联合约束与逐元素求逆。

<a id="paper-152123"></a>

## From Next-Token to Next-Block: A Principled Adaptation Path for Diffusion LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152123) · [作者来源](https://openreview.net/forum?id=VLjkAcK9fS)

- **问题 / 瓶颈** · 直接微调或随机调整掩码可能损伤预训练知识。
- **核心创新 / 方法** · 保持已提交上下文因果，块内允许双向交互，使用一次并行训练与 AR 辅助指导并逐步加块。
- **Baseline** · 随机掩码退火、直接块扩散微调及其他扩散语言模型。
- **Benchmark** · 通识、数学和代码，覆盖多种初始化与模型尺度。
- **关键结果 / 消融** · 作者报告改进平均适配表现，NBDIFF-7B 支持 32K 上下文。
- **适用条件 / 局限** · 适用于块扩散；推理吞吐与跨块大小稳定性待核。

**可复用机制** · 先固定已有上下文因果结构，只渐增需要并行的局部范围。

<a id="paper-148590"></a>

## From Nodes to Pixels: Topological and Structural Two-View Graph Imaging

[官方论文页](https://neurips.cc/virtual/2026/poster/148590) · [作者来源](https://openreview.net/forum?id=wd6T1tqNIh)

- **问题 / 瓶颈** · 节点排列和图规模变化阻碍共享输入接口。
- **核心创新 / 方法** · 以持久性表面网格编码拓扑，通过内在节点评分分组统计边密度形成结构视图，再做跨视图对比。
- **Baseline** · 单视图、标准融合与其他图方法。
- **Benchmark** · 图分类基准；具体任务及数值待核。
- **关键结果 / 消融** · 摘要报告双视图优于单视图与标准融合，且有分辨率控制的稳定性结果。
- **适用条件 / 局限** · 固定分辨率可能丢失局部结构，依赖内在评分。

**可复用机制** · 选择图输入接口时在相同张量尺寸下对照单拓扑、单结构及融合。

<a id="paper-155787"></a>

## From Noise to Diversity: Random Embedding Injection in LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155787) · [作者来源](https://openreview.net/forum?id=2tl55s2775)

- **问题 / 瓶颈** · 优化软提示的收益可能来自注入位置本身而非学到的内容。
- **核心创新 / 方法** · 按预训练嵌入的均值、方差拟合各向同性高斯，重新采样软提示并分析早期分支。
- **Baseline** · 优化软提示、温度采样与 DAPO 设置。
- **Benchmark** · 数学推理，比较早期 token 多样性、准确率和 Pass@N。
- **关键结果 / 消融** · 摘要报告若干设置下准确率与优化软提示可比，结合温度采样可扩大 Pass@N。
- **适用条件 / 局限** · 收益与模型、嵌入尺度和采样预算相关，数值待核。

**可复用机制** · 软提示实验可用同长度随机嵌入分离学习内容和输入结构效应。

<a id="paper-150800"></a>

## From Non-Convex to Strongly Convex: Curvature-Adaptive FTPL for Online Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150800) · [作者来源](https://openreview.net/forum?id=fIWVuCJFiG)

- **问题 / 瓶颈** · 固定扰动只能体现最坏情况遗憾，不利用曲率累积。
- **核心创新 / 方法** · 用只依赖过去损失的跟随领导者规则选择时变扰动，使表现接近事后最优规模。
- **Baseline** · 固定扰动 FTPL、事后最优规模及理论下界。
- **Benchmark** · 在线非凸 Lipschitz 损失及累积曲率序列。
- **关键结果 / 消融** · 最坏情况为根号 T 级遗憾；曲率线性累积且预言机足够准时为对数级。
- **适用条件 / 局限** · 依赖近似离线优化预言机及其精度。

**可复用机制** · 若问题可访问离线求解器，记录曲率累积并与固定扰动策略比较。

<a id="paper-148296"></a>

## From Outcome to Representation: Tracing Reasoning Mechanisms through Integrated Policy Gradient

[官方论文页](https://neurips.cc/virtual/2026/poster/148296) · [作者来源](https://openreview.net/forum?id=yutHGESj05)

- **问题 / 瓶颈** · 局部解释无法追踪组件对多步推理结果的影响。
- **核心创新 / 方法** · 用积分策略梯度沿整条推理轨迹对不可微结果做路径归因，给出因果中介分析的线性近似。
- **Baseline** · 局部效应和文本模式归因为背景对照；具名方法待核。
- **Benchmark** · 语言模型多步推理，考察组件定位和结果关联。
- **关键结果 / 消融** · 作者报告可定位集中且稀疏的组件，量化结果待核。
- **适用条件 / 局限** · 线性近似不构成完整因果证明。

**可复用机制** · 联合测输出行为及跨步归因，使用受控组件复核归因稳定性。

<a id="paper-150388"></a>

## From Patches to Trajectories: Privileged Process Supervision for Software-Engineering Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/150388) · [作者来源](https://openreview.net/forum?id=iQIFIFP5W7)

- **问题 / 瓶颈** · 结局过滤保留了冗余、无依据的修复步骤。
- **核心创新 / 方法** · 将常规维护补丁转换成事实和里程碑图，盲化教师并校验各短段是否基于可见证据。
- **Baseline** · 终局过滤 SFT 及工具错误掩码版本。
- **Benchmark** · SWE-Gym、SWE-bench Verified 与 Lite，测 Pass@1 和推理成本。
- **关键结果 / 消融** · 使用 1,800 条样本，Verified 最多增加 10.8 个点，单例推理成本低 15%。
- **适用条件 / 局限** · 需要训练期可信补丁，并防止泄漏到学生输入。

**可复用机制** · 用参考修复验证中间调查步骤，而非仅以测试最终通过作数据门槛。

<a id="paper-153962"></a>

## From Perception to Punchline: Empowering VLM with the Art of In-the-wild Memes

[官方论文页](https://neurips.cc/virtual/2026/poster/153962) · [作者来源](https://openreview.net/forum?id=HDw4usJpF9)

- **问题 / 瓶颈** · 直接图到标题监督忽视语境，跨模板评分噪声大。
- **核心创新 / 方法** · 从真实标题反推多路径推理监督，在同模板组内训练成对奖励并用于优化。
- **Baseline** · 直接生成与其他推理或偏好对照，具体名称待核。
- **Benchmark** · 野外表情包生成，测推理多样性、偏好对齐与质量。
- **关键结果 / 消融** · 作者报告三项改善，并给出信赖域内的理论条件。
- **适用条件 / 局限** · 理论依赖优质路径质量及组内可比性。

**可复用机制** · 在开放生成中先按可比条件分组，再检验组内偏好能否预测人工选择。

<a id="paper-153632"></a>

## From Persistence to Survival: Hypothesis Testing, Effect Sizes and Vectorisation for Topological Features

[官方论文页](https://neurips.cc/virtual/2026/poster/153632) · [作者来源](https://openreview.net/forum?id=JxamHvfzlr)

- **问题 / 瓶颈** · 持久图缺少统一的统计比较和向量接口。
- **核心创新 / 方法** · 把每个拓扑特征的寿命作为完整观测时间，基于经验生存函数做两样本检验及稳定表示。
- **Baseline** · 对照其他拓扑特征向量化，具名基线待核。
- **Benchmark** · 可控拓扑的合成流形，另有 14 个图和点云基准。
- **关键结果 / 消融** · 作者报告检验第一类错误校准及较高检验力，并给出 Wasserstein 稳定性。
- **适用条件 / 局限** · 特征对比侧重寿命分布，出生位置影响需另测。

**可复用机制** · 需同时判断拓扑差异并训练分类器时，用同一寿命表示保持解释一致。

<a id="paper-139321"></a>

## From Pixels to Concepts: Do Segmentation Models Understand What They Segment?

[官方论文页](https://neurips.cc/virtual/2026/poster/139321) · [作者来源](https://openreview.net/forum?id=XP1FvR8d8X)

- **问题 / 瓶颈** · 准确定位可能来自视觉显著性而忽略提示语义。
- **核心创新 / 方法** · 构造正提示和误导负提示配对，保持真值区域并改变外观、上下文或本体线索。
- **Baseline** · 比较不同提示分割模型及规模，含 SAM3 所代表的概念分割路线。
- **Benchmark** · CAFE 2,146 对样本，覆盖三种反事实类别。
- **关键结果 / 消融** · 作者观察到误导提示下仍经常得到准确掩码，说明概念判别与定位分离。
- **适用条件 / 局限** · 依赖反事实编辑有效且未引入伪影，跨类别强度待核。

**可复用机制** · 并列报告正提示定位和错误语义的拒答，避免只看掩码重合。

<a id="paper-151710"></a>

## From POMDP Theory to Deep RL with Particle Filters

[官方论文页](https://neurips.cc/virtual/2026/poster/151710) · [作者来源](https://openreview.net/forum?id=YcveAbhXYA)

- **问题 / 瓶颈** · 理论模型和实用深度 POMDP 算法的近似误差难对照。
- **核心创新 / 方法** · 用序贯蒙特卡洛过滤，在线更新动力学，短时滚动后以状态价值引导。
- **Baseline** · QMDP 类型近似及深度 MPC 实例；具名对照待核。
- **Benchmark** · POMDP 在线决策的理论遗憾与多环境深度强化学习实验。
- **关键结果 / 消融** · 遗憾拆分为模型、粒子、滚动与 QMDP 结构偏差。
- **适用条件 / 局限** · 误差界依赖建模和估计条件，增加深度有计算代价。

**可复用机制** · 用四项误差拆解指导将计算分给状态估计还是规划。

<a id="paper-154078"></a>

## From Post-Hoc to Ante-Hoc: Consistently Explainable Semi-Supervised Time Series Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/154078) · [作者来源](https://openreview.net/forum?id=GMZeOQcKOW)

- **问题 / 瓶颈** · 事后解释不能保证模型实际使用所标特征。
- **核心创新 / 方法** · 预测式辅助训练教师，从归因提取充分子集，监督门控并蒸馏只看所选输入的学生。
- **Baseline** · 近期半监督时间序列分类及无门控教师。
- **Benchmark** · 八个数据集、四种标签比例、五种子；MIT-BIH 有显著性注释。
- **关键结果 / 消融** · 保留 20% 至 45% 特征仍具竞争准确率；MIT-BIH 还测试 10% 至 20%。
- **适用条件 / 局限** · 充分子集可能不唯一，医疗部署需另验。

**可复用机制** · 同时测门控学生保真度、输入保留率及可用时的真值区域一致性。

<a id="paper-148699"></a>

## From Preference Data to Personalization: Tracing Sycophancy in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148699) · [作者来源](https://openreview.net/forum?id=viJknQbGQA)

- **问题 / 瓶颈** · 直接将一致回答计为迎合，会混淆正确认同和不当附和。
- **核心创新 / 方法** · 用有效性评分器和控制用户开放度、利害程度的探针比较偏好数据、评分规则与个性化。
- **Baseline** · 人工偏好数据、自动评审、上下文头像配置与常规模型对照。
- **Benchmark** · SycoDrift 的 3,298 个探针，覆盖 14 个模型及三种偏好数据。
- **关键结果 / 消融** · 作者报告人工数据的认同偏好较弱，自动评分规则和个性化更易扩大不当认同。
- **适用条件 / 局限** · 依赖有效性标注和人物设定的代表性。

**可复用机制** · 评估个性化时，固定主张有效性和人设匹配程度分别测纠错与认同。

<a id="paper-154046"></a>

## From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills

[官方论文页](https://neurips.cc/virtual/2026/poster/154046) · [作者来源](https://openreview.net/forum?id=GciYMFDFBW)

- **问题 / 瓶颈** · 平均技能收益掩盖了跨模型和任务的负迁移。
- **核心创新 / 方法** · 在经验生成、提取、使用各阶段做系统对照，提炼按效用引导提取的元技能。
- **Baseline** · 比较不同提取器、使用者和经验组合。
- **Benchmark** · 五个代理任务域，测实际效用和负迁移。
- **关键结果 / 消融** · 提取能力与消费能力可能分离，元技能减少负迁移；幅度待核。
- **适用条件 / 局限** · 依赖各任务域及技能接口，跨域性仍需复核。

**可复用机制** · 为技能库建提取器—消费者迁移矩阵，按效用验证再共享。

<a id="paper-152795"></a>

## From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152795) · [作者来源](https://openreview.net/forum?id=QIDIchi6N0)

- **问题 / 瓶颈** · 只验最终答案使困难题反馈稀疏
- **核心创新 / 方法** · 从参考解抽取可验子题；各位置组内归一化后把优势赋给对应答案段
- **Baseline** · GRPO 与课程学习
- **Benchmark** · 七个数学基准，含 AIME24/25、IMO-Bench
- **关键结果 / 消融** · 两种 Qwen3 基座平均提高 4.1 和 1.9 分
- **适用条件 / 局限** · 需要参考解及可验证子题

**可复用机制** · 用分段验收与端到端奖励的同预算对照，检查探索收益

<a id="paper-148253"></a>

## From Representational Complementarity to Dual Systems: Synergizing VLM and Vision-Only Backbones for End-to-End Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/148253) · [作者来源](https://openreview.net/forum?id=zGQGEEXiVl)

- **问题 / 瓶颈** · 不同视觉骨干对几何和交互的优势未知
- **核心创新 / 方法** · 固定扩散规划器比较骨干，训练轨迹评分器选择跨模型候选
- **Baseline** · InternVL3、Qwen3VL、ResNet、ViT、EVA-CLIP
- **Benchmark** · NAVSIM，PDMS 和延迟
- **关键结果 / 消融** · 混合选择由 90.80 到 92.10；快慢系统调用 VLM 约 15%
- **适用条件 / 局限** · 场景与延迟收益需跨基准验证

**可复用机制** · 固定下游，把骨干互补性转成条件路由

<a id="paper-148303"></a>

## From Retrieval to Recognition: Knowledge-Enhanced Foundation Models for Time Series Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/148303) · [作者来源](https://openreview.net/forum?id=yqUEv3yP3e)

- **问题 / 瓶颈** · 微调难精确调用相关知识
- **核心创新 / 方法** · 以独立查询编码器检索数值实例，再和基础模型嵌入融合
- **Baseline** · 仅参数微调的时间序列基础模型
- **Benchmark** · 158 个数据集的分类
- **关键结果 / 消融** · 作者报告一致改善，幅度待核
- **适用条件 / 局限** · 检索库质量与切分防泄漏需核查

**可复用机制** · 固定骨干比较有无实例检索，并记录检索得分和分类收益

<a id="paper-150964"></a>

## From Sample to Subset Construction: Coverage-Aware Curation of Robot Demonstrations

[官方论文页](https://neurips.cc/virtual/2026/poster/150964) · [作者来源](https://openreview.net/forum?id=dwYhsDanf7)

- **问题 / 瓶颈** · 冗余轨迹稀释学习，稀有片段可能关键
- **核心创新 / 方法** · 统一考虑闭环价值影响、运动学可靠性和相对已选集合的覆盖
- **Baseline** · CUPID、SCIZOR、Demo-SCORE
- **Benchmark** · 三项 Robomimic 仿真与三项 Franka 实机任务
- **关键结果 / 消融** · 作者报告平均闭环收益为仿真 15%、实机 35%，覆盖项贡献主要
- **适用条件 / 局限** · 受覆盖度量与固定预算影响

**可复用机制** · 等预算比较独立排序与逐次更新覆盖的子集选择

<a id="paper-150171"></a>

## From Seeing to Foreseeing: Unleashing LVLM Thinking in Dynamic Latent Space

[官方论文页](https://neurips.cc/virtual/2026/poster/150171) · [作者来源](https://openreview.net/forum?id=k9WRKd8CYo)

- **问题 / 瓶颈** · 静态视觉潜变量无法明确表达动态
- **核心创新 / 方法** · 按新颖度抽取动态潜变量，两阶段监督后用对比目标区分真实与反事实轨迹
- **Baseline** · 文本、工具和静态潜变量推理；具名待核
- **Benchmark** · BabyVision 和 HRBench4K
- **关键结果 / 消融** · 作者分别报告 10.82% 与 10.50% 改善
- **适用条件 / 局限** · 静态图像只能推断可能动态

**可复用机制** · 固定图像上下文，消融真实和反事实动态监督

<a id="paper-153955"></a>

## From Senses to Decisions: The Information Flow of Auditory and Visual Perception in Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153955) · [作者来源](https://openreview.net/forum?id=HISWDrw0Ol)

- **问题 / 瓶颈** · 声音与图像路由随输入排列变化
- **核心创新 / 方法** · 对照视频与多项交错输入，追踪顺序和并行情形的信息流
- **Baseline** · 不同 token 保留和输入配置
- **Benchmark** · Qwen2.5-Omni、Video-SALMONN2 Plus，3B 和 7B
- **关键结果 / 消融** · 信息转移后删除部分 token 影响很小，部分任务反而改善
- **适用条件 / 局限** · 剪枝位置依赖输入结构

**可复用机制** · 用层级干预确定各模态 token 何时可安全删减

<a id="paper-155707"></a>

## From sequences to schemas: low-rank recurrent dynamics underlie abstract relational representations

[官方论文页](https://neurips.cc/virtual/2026/poster/155707) · [作者来源](https://openreview.net/forum?id=3XO2JXx10F)

- **问题 / 瓶颈** · 模式泛化的记忆机制难辨识
- **核心创新 / 方法** · 训练 RNN 识别代数模式，消融领先循环分量以检查早期关系记忆
- **Baseline** · 下一 token 预测与关系分类
- **Benchmark** · AAB、ABA 等符号序列
- **关键结果 / 消融** · 领先分量消融损害早期关系记忆，单步敏感性保留
- **适用条件 / 局限** · 合成序列不代表自然认知

**可复用机制** · 比较目标函数对关系抽象的影响，并用低秩消融作因果检验

<a id="paper-148891"></a>

## From SGD to Muon: Adaptive Optimization via Schatten-p Norms

[官方论文页](https://neurips.cc/virtual/2026/poster/148891) · [作者来源](https://openreview.net/forum?id=uQkr5twCZH)

- **问题 / 瓶颈** · 固定更新范数可能不匹配层几何
- **核心创新 / 方法** · 由单步随机特征回归代理推导选择规则，在 SGD 与 Muon 之间插值
- **Baseline** · Muon、AdamW；含参数预条件变体
- **Benchmark** · 三种训练场景与运行开销
- **关键结果 / 消融** · 匹配或超过两基线中较优者，额外开销约 3%
- **适用条件 / 局限** · 代理最优未必等于长程最优

**可复用机制** · 按层诊断几何选择收益，并控制运行预算

<a id="paper-152509"></a>

## From Small to Large: Cross-Scale Graph Domain Adaptation via Local-Global Structural Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/152509) · [作者来源](https://openreview.net/forum?id=Sb0yr9VOw6)

- **问题 / 瓶颈** · 采样源图同时缺局部邻域和全局覆盖
- **核心创新 / 方法** · 补偿邻域、匹配全局结构，并经自适应 GCN-MLP 融合
- **Baseline** · 常规图域适配；具名对照待核
- **Benchmark** · 多个图迁移基准与采样比例
- **关键结果 / 消融** · 源图不完整时作者报告持续改善
- **适用条件 / 局限** · 补偿有效性取决于采样偏差

**可复用机制** · 按采样比例分别消融局部和全局对齐

<a id="paper-148685"></a>

## From Solver Trajectories to Teaching Trajectories: Cognition-Aligned Reasoning Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/148685) · [作者来源](https://openreview.net/forum?id=vozYLGC2YA)

- **问题 / 瓶颈** · 强求解轨迹未必适合弱学生模仿
- **核心创新 / 方法** · 用学生分布对齐与逻辑一致性双奖励优化轨迹改写
- **Baseline** · 原始教师轨迹
- **Benchmark** · 多个学生模型与分布内外任务
- **关键结果 / 消融** · 作者报告分布内改善及分布外收益
- **适用条件 / 局限** · 双奖励的成本与错误边界待核

**可复用机制** · 固定教师轨迹数量，对照原轨迹与学生适配轨迹

<a id="paper-154431"></a>

## From Squeezing to Grounding: Visual Guided DPO for Multimodal Hallucination Mitigation

[官方论文页](https://neurips.cc/virtual/2026/poster/154431) · [作者来源](https://openreview.net/forum?id=DdP4SoPK7L)

- **问题 / 瓶颈** · 偏好优化可能把概率质量推向语言捷径
- **核心创新 / 方法** · 用 token 视觉依赖和短语幻觉定位计算风险，重加权拒绝梯度与视觉对比项
- **Baseline** · DPO、已有挤压感知和锚定方法
- **Benchmark** · 四个幻觉基准、三种骨干
- **关键结果 / 消融** · 作者报告幻觉减少且回答仍有信息
- **适用条件 / 局限** · 视觉依赖估计误差待测

**可复用机制** · 同步追踪两类回答概率及图像扰动敏感性

<a id="paper-155740"></a>

## From Static Geometry to Dynamical Singularity: Detecting Memorization in Diffusion Models via Score Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/155740) · [作者来源](https://openreview.net/forum?id=3KVTmKRBPc)

- **问题 / 瓶颈** · 曲率审计成本高
- **核心创新 / 方法** · 用条件与无条件的沿轨迹分数演化差异作为检测量
- **Baseline** · 显式曲率方法
- **Benchmark** · Stable Diffusion 记忆检测
- **关键结果 / 消融** · 作者报告早期反向步骤即可识别且无需新增反传
- **适用条件 / 局限** · 效果受模型及引导设置影响

**可复用机制** · 在相同误报预算下比较轨迹代理与曲率审计

<a id="paper-154418"></a>

## From Structural Feedback to Prompt Policies: Learning Faithful Text-to-Image Prompt Editors

[官方论文页](https://neurips.cc/virtual/2026/poster/154418) · [作者来源](https://openreview.net/forum?id=DikML74WUt)

- **问题 / 瓶颈** · 自由改写可能牺牲用户语义
- **核心创新 / 方法** · 在校准场景图约束下做保守编辑，并用平滑关系反馈学习
- **Baseline** · 自由改写与美学优化
- **Benchmark** · 多提示数据集、图像骨干、人评与 Gemini-VQA
- **关键结果 / 消融** · 作者报告关系保真更稳定，并改善保真和美学权衡
- **适用条件 / 局限** · 依赖场景图与验证器质量

**可复用机制** · 分开评价关系保留与观感，避免用训练奖励自证

<a id="paper-153945"></a>

## From Table to Cell: Attention for Better Reasoning with TABALIGN

[官方论文页](https://neurips.cc/virtual/2026/poster/153945) · [作者来源](https://openreview.net/forum?id=HOEBdl2bk0)

- **问题 / 瓶颈** · 行顺序改变及依据错位影响表格推理
- **核心创新 / 方法** · 扩散规划器生成单元格二值掩码，验证器按注意力重叠验收步骤
- **Baseline** · 同骨干自回归规划及同规模开源方法
- **Benchmark** · 八项表格问答与事实验证
- **关键结果 / 消融** · 平均准确率提高 15.76 个百分点，同骨干消融为 2.87 个百分点
- **适用条件 / 局限** · 依赖单元格可定位及人审监督

**可复用机制** · 以行重排和依据追踪分别检验计划稳定性与执行正确率

<a id="paper-154681"></a>

## From Talking Words to Sharing Thoughts: Scalable Multi-LLM Aggregation via Structured Message Passing

[官方论文页](https://neurips.cc/virtual/2026/poster/154681) · [作者来源](https://openreview.net/forum?id=BmE5XhMLO5)

- **问题 / 瓶颈** · 迭代重问开销大且多数弱模型可覆盖强模型
- **核心创新 / 方法** · 在二部因子图上传播概率消息，按可靠度限制对锚点的覆盖
- **Baseline** · 迭代多智能体集成
- **Benchmark** · MMLU、MMLU-Pro、GPQA、MedMCQA
- **关键结果 / 消融** · 作者报告 token 用量减 97%，调用最多减少六倍
- **适用条件 / 局限** · 需要可靠的输出分布和专家校准

**可复用机制** · 固定调用预算，消融可靠锚点以辨别集成增益

<a id="paper-155821"></a>

## From Topology to Retrieval: Decoding Embedding Spaces with Unified Signatures

[官方论文页](https://neurips.cc/virtual/2026/poster/155821) · [作者来源](https://openreview.net/forum?id=2cbJBFU7At)

- **问题 / 瓶颈** · 单个拓扑指标难反映嵌入空间整体结构
- **核心创新 / 方法** · 统一多种拓扑与几何信号，评估与检索和模型属性的联系
- **Baseline** · 单一几何或拓扑指标
- **Benchmark** · 多个文本嵌入模型与检索数据集
- **关键结果 / 消融** · 作者报告联合签名更能预测表现
- **适用条件 / 局限** · 相关性不代表因果，跨数据切分待核

**可复用机制** · 在留出模型上验证联合几何指标是否优于单项指标
