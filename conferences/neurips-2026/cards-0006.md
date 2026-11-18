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

<a id="paper-152776"></a>

## From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/152776) · [作者来源](https://openreview.net/forum?id=QRZ8c3QtOj)

- **问题 / 瓶颈** · 模型裁判有位置偏差等系统误差。
- **核心创新 / 方法** · 校准单场胜率后拟合 Bradley–Terry，再对人机 Elo 残差做分割共形校准。
- **Baseline** · 硬标签排名与人工排名。
- **Benchmark** · LMArena 的 55 个留出模型。
- **关键结果 / 消融** · 相对人工排名误差为 17.9 Elo MAE。
- **适用条件 / 局限** · 边际覆盖依赖校准与测试样本可交换。

**可复用机制** · 分别校准对局与排名层误差。

<a id="paper-149559"></a>

## From Views to Worlds: Active Exploration over 3D Worlds for Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149559) · [作者来源](https://openreview.net/forum?id=pCouEwaa1S)

- **问题 / 瓶颈** · 额外二维视图未直接表达空间关系。
- **核心创新 / 方法** · 重建几何、相机位姿和语言关联语义，以视觉和语言接口支持多轮查询。
- **Baseline** · 原始视觉语言模型及免训练版本。
- **Benchmark** · 空间心理建模任务，具名基准待核。
- **关键结果 / 消融** · 作者报告免训练版本改善基础模型，学习探索后进一步提高。
- **适用条件 / 局限** · 受场景重建质量和查询能力限制。

**可复用机制** · 对照被动增加视图与主动几何查询。

<a id="paper-153103"></a>

## From Walls to Synergy: A Joint LLM-Evolution Framework for MILP Solvers

[官方论文页](https://neurips.cc/virtual/2026/poster/153103) · [作者来源](https://openreview.net/forum?id=NvJ3gFAFu1)

- **问题 / 瓶颈** · 单独优化预求解、切割和分支可能收益递减。
- **核心创新 / 方法** · 用协调器对齐组件生成器，以层级控制器组合多阶段策略。
- **Baseline** · 已有机器学习和语言模型方法。
- **Benchmark** · 九个 MILP 数据集。
- **关键结果 / 消融** · 作者报告各数据集表现改善，数值待核。
- **适用条件 / 局限** · 跨实例分布的迁移和计算预算待核。

**可复用机制** · 在固定预算下比较联合搜索和分别搜索后组合。

<a id="paper-152260"></a>

## From Weak Data to Strong Policy: Q-Targets Enable Provable In-Context Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152260) · [作者来源](https://openreview.net/forum?id=UNtPiyXC2w)

- **问题 / 瓶颈** · 行为预测会继承次优动作。
- **核心创新 / 方法** · 从上下文奖励和转移构造 Bellman 式 Q 目标训练 Transformer。
- **Baseline** · 匹配的行为预测 Transformer 及上下文和 TD 消融。
- **Benchmark** · 随机线性赌博机、有限时域 MDP 和 D4RL。
- **关键结果 / 消融** · 理论界分离离线数据影响和逼近误差，弱数据中收益更明显。
- **适用条件 / 局限** · 理论界仅覆盖文中假设。

**可复用机制** · 保持上下文条件相同，比较模仿与价值监督。

<a id="paper-153154"></a>

## From “Weak” Signals to Strong Models: Preference Delta Aggregation with LoRA Merging

[官方论文页](https://neurips.cc/virtual/2026/poster/153154) · [作者来源](https://openreview.net/forum?id=NTLZwZkDzg)

- **问题 / 瓶颈** · 多个弱偏好信号的更新方向可能冲突。
- **核心创新 / 方法** · 每对弱模型响应训练偏好 LoRA，再对齐子空间并聚合。
- **Baseline** · 单差分及多差分合并基线。
- **Benchmark** · 知识推理与代理搜索任务。
- **关键结果 / 消融** · 相对强模型平均加 6.8 和 7.3 分，较最强单差分高 2.1 和 4.3 分。
- **适用条件 / 局限** · 依赖弱模型能力互补和偏好顺序可靠。

**可复用机制** · 拆分偏好来源，比较直接合并和对齐合并。

<a id="paper-155549"></a>

## From Weeks to Hours: Fast and Principled SFT Curation for LLM

[官方论文页](https://neurips.cc/virtual/2026/poster/155549) · [作者来源](https://openreview.net/forum?id=4jOHUJJVCg)

- **问题 / 瓶颈** · 先大规模生成再筛选轨迹成本高。
- **核心创新 / 方法** · 短 LoRA 探测损失几何，对紧凑签名聚类，并用曲率拐点损失代理难度。
- **Baseline** · 生成后筛选及 OpenThoughts。
- **Benchmark** · 数学推理训练，并提供物理推理集。
- **关键结果 / 消融** · 作者报告用轨迹 0.1–1% 估计质量，5K 样本匹配 OpenThoughts 89K。
- **适用条件 / 局限** · 代理质量和复现开销需跨模型验证。

**可复用机制** · 在相同生成预算下评估损失探针能否提前淘汰冗余轨迹。

<a id="paper-148971"></a>

## From Zero to Hero: Training-Free Custom Concept Spawning in World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148971) · [作者来源](https://openreview.net/forum?id=tl8wcMpfSF)

- **问题 / 瓶颈** · 初始参考帧无法指定未见区域的内容。
- **核心创新 / 方法** · 短时注入外部概念潜变量替换固定首槽，再恢复原参考帧。
- **Baseline** · 原始世界模型，具名对照待核。
- **Benchmark** · 交互视频中的人物、道具与建筑插入。
- **关键结果 / 消融** · 报告光照、比例和时间一致性。
- **适用条件 / 局限** · 依赖固定首槽及后续记忆传播。

**可复用机制** · 比较持续与短窗口条件注入对身份保持的影响。

<a id="paper-152963"></a>

## Frontier Coding Agents Use Metaprogramming to Adapt to Unfamiliar Programming Languages

[官方论文页](https://neurips.cc/virtual/2026/poster/152963) · [作者来源](https://openreview.net/forum?id=P4Ev2InDix)

- **问题 / 瓶颈** · 常见语言基准可能隐藏在线适应差异。
- **核心创新 / 方法** · 在冷门语言上按文件编辑、执行和隐藏测试逐步评测，并禁用或提供生成器辅助。
- **Baseline** · 六种代理，含文本提示和生成器辅助。
- **Benchmark** · 四种冷门语言编程题。
- **关键结果 / 消融** · 禁用元编程使强代理明显退化；增加预算对弱代理作用有限。
- **适用条件 / 局限** · 结论限于所测语言和工具协议。

**可复用机制** · 区分提供更多资源与提供可运行策略的效果。

<a id="paper-139163"></a>

## Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering with Generative Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/139163) · [作者来源](https://openreview.net/forum?id=hXNx575zFR)

- **问题 / 瓶颈** · 二元通过无法表示可行设计的持续改良。
- **核心创新 / 方法** · 给定可行起点及冻结验证器，按约束下的质量评分比较迭代。
- **Baseline** · OpenEvolve 中的多模型与多框架。
- **Benchmark** · 47 个任务；此处关注库存、调度等良性案例。
- **关键结果 / 消融** · 总体上改进事件随迭代变少、增量逐次变小。
- **适用条件 / 局限** · 结果依赖验证器和搜索深度。

**可复用机制** · 以固定预算报告首次可行和后续边际改进。

<a id="paper-150144"></a>

## Frontier Language Models Struggle to Copy: Text Can Be Better Viewed in 2D

[官方论文页](https://neurips.cc/virtual/2026/poster/150144) · [作者来源](https://openreview.net/forum?id=kLtPKaSPni)

- **问题 / 瓶颈** · 一维位置编码可能促使模型匹配局部上下文。
- **核心创新 / 方法** · 将文本排成二维网格并用行列旋转位置编码。
- **Baseline** · 标准位置编码。
- **Benchmark** · 合成复制、DCLM 预训练及 NIAH。
- **关键结果 / 消融** · 浅层模型在训练长度数百倍的合成输入上仍能精确复制。
- **适用条件 / 局限** · 对其他语言建模能力的影响需核全文。

**可复用机制** · 单独评估重复上下文中的位置复制和长度外推。

<a id="paper-139096"></a>

## FrontierOR: Benchmarking LLMs' Capacity for Efficient Algorithm Design in Large-Scale Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/139096) · [作者来源](https://openreview.net/forum?id=lH8UmIzeEP)

- **问题 / 瓶颈** · 可执行求解程序不代表算法能利用问题结构。
- **核心创新 / 方法** · 从运筹研究构造标准实例并用隐藏评测比较算法设计。
- **Baseline** · Gurobi、一次生成与测试时演化。
- **Benchmark** · 110 个现实规模运筹任务。
- **关键结果 / 消融** · 最强一次生成模型仅 39% 案例在质量和运行时间均胜；选定难题演化设置为 50%。
- **适用条件 / 局限** · 两项结果的评估范围不同。

**可复用机制** · 用同预算和真实规模验证代码改进是否可扩展。

<a id="paper-151843"></a>

## FrontierSmith: Synthesizing Open-Ended Coding Problems at Scale

[官方论文页](https://neurips.cc/virtual/2026/poster/151843) · [作者来源](https://openreview.net/forum?id=XWrgnSu8qf)

- **问题 / 瓶颈** · 传统正确性任务缺少多种可行方案的训练信号。
- **核心创新 / 方法** · 变换竞赛题目标和约束，用思路分歧筛选并生成测试和验证器。
- **Baseline** · 基础模型及人类构造开放任务。
- **Benchmark** · FrontierCS 和 ALE-bench。
- **关键结果 / 消融** · Qwen3.5-9B 提高 8.82 分与 306.36 Elo 类评分单位。
- **适用条件 / 局限** · 生成验证器的正确性及训练污染需核。

**可复用机制** · 筛题时同时测可验证性和独立策略多样性。

<a id="paper-151737"></a>

## Frontier Task Synthesis Via Solution-Centric Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/151737) · [作者来源](https://openreview.net/forum?id=YT5exYsQq0)

- **问题 / 瓶颈** · 直接造题难同时控制难度与正确性。
- **核心创新 / 方法** · 结构化变换参考解，并重新生成匹配的题面与测试。
- **Baseline** · 原始任务及仅用种子题训练。
- **Benchmark** · LiveCodeBench 与 SciCode 及留出编程测试。
- **关键结果 / 消融** · gpt-oss-20b 在两个留出集提升 8.7 和 8.3 个 Pass@1 点。
- **适用条件 / 局限** · 变换覆盖度和泄漏控制需核。

**可复用机制** · 让正确参考解约束课程生成，并在留出集合检验收益。

<a id="paper-150946"></a>

## Frozen Memory Is Not Enough: Rethinking External Memory as Extraction

[官方论文页](https://neurips.cc/virtual/2026/poster/150946) · [作者来源](https://openreview.net/forum?id=e7xyZQCjBR)

- **问题 / 瓶颈** · 只携带存储表未解决目标骨干如何解释内容。
- **核心创新 / 方法** · 冻结源模型哈希记忆，仅训练目标侧轻量读取器。
- **Baseline** · 同模型配置及内容、寻址、读取器消融。
- **Benchmark** · 三乘三跨模型转移矩阵及 OpenQA。
- **关键结果 / 消融** · 所有模型对改善，最高相对困惑度下降 15.7%。
- **适用条件 / 局限** · 取决于目标侧寻址及读取器容量。

**可复用机制** · 固定存储预算，分别干预内容、寻址和读取结构。

<a id="paper-150220"></a>

## FRUC: Feedforward Dynamic Scene Reconstruction from Uncalibrated Collaborative Driving Views

[官方论文页](https://neurips.cc/virtual/2026/poster/150220) · [作者来源](https://openreview.net/forum?id=jruosxypbz)

- **问题 / 瓶颈** · 未标定协作视角可能破坏主视图已观测几何。
- **核心创新 / 方法** · 前馈几何 Transformer 学习时空遮挡场，再用零初始化残差注入补全。
- **Baseline** · 已有协作重建系统。
- **Benchmark** · V2XReal 和 UrbanIng-V2X。
- **关键结果 / 消融** · 作者报告渲染质量与效率提高，数值待核。
- **适用条件 / 局限** · 对极端视角误差和同步偏差的表现待核。

**可复用机制** · 分别计量遮挡补全收益和已知区域退化。

<a id="paper-154979"></a>

## FTerViT: Fully Ternary Vision Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/154979) · [作者来源](https://openreview.net/forum?id=9SnaFlb35c)

- **问题 / 瓶颈** · 小模型未量化组件可能成为主要内存成本。
- **核心创新 / 方法** · 三值化全部权重和归一化参数，以蒸馏和量化感知恢复训练。
- **Baseline** · FP32 DeiT-III 和此前三值 ViT。
- **Benchmark** · ImageNet-1K 与 ESP32-S3 实机。
- **关键结果 / 消融** · 384 分辨率达 82.43% 及 6.09 MB，实机配置达 79.64%。
- **适用条件 / 局限** · 激活仍为 8 位，实际延迟与硬件相关。

**可复用机制** · 报告端到端内存和实机精度，避免仅统计骨干。

<a id="paper-151309"></a>

## Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps

[官方论文页](https://neurips.cc/virtual/2026/poster/151309) · [作者来源](https://openreview.net/forum?id=bR3PWtkIml)

- **问题 / 瓶颈** · 全注意力成本高，固定稀疏预算会漏掉关键检索。
- **核心创新 / 方法** · 仅检索头保留全 KV，用低维索引和动态阈值选择稀疏注意力。
- **Baseline** · 全注意力及已有稀疏替代方法。
- **Benchmark** · 长上下文和推理，含百万 token 预填充。
- **关键结果 / 消融** · 作者报告预填充最高加速 9.36 倍，解码约 2.01 倍。
- **适用条件 / 局限** · 收益依赖架构、硬件和检索分布。

**可复用机制** · 与固定预算对照，并分别测检索召回、预填充和解码。

<a id="paper-152739"></a>

## Full-Duplex Speech-Motion Model for Dyadic Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/152739) · [作者来源](https://openreview.net/forum?id=Qisqy4uHjG)

- **问题 / 瓶颈** · 真实交互要求同时感知和生成动作与语音。
- **核心创新 / 方法** · 冻结全双工语音模型，加耦合动作通道、双人交错 token 和对齐位置编码。
- **Baseline** · 已有单人和双人交互方法，具名待核。
- **Benchmark** · Seamless Interaction 的 4000 小时数据与单双人交互基准。
- **关键结果 / 消融** · 作者报告在单双人基准中改善，数值待核。
- **适用条件 / 局限** · 依赖时序标注，实际延迟和开放交互证据待核。

**可复用机制** · 比较单人对齐与双人交错建模对响应时序的影响。

<a id="paper-148745"></a>

## Full Fine-Tuning Is Not the Problem: Why Adam Fails and SGD Succeeds in Few-Shot CLIP Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/148745) · [作者来源](https://openreview.net/forum?id=vMIIW94Dzm)

- **问题 / 瓶颈** · 少样本二阶矩低估可能放大自适应更新。
- **核心创新 / 方法** · 比较多种预条件方式，并将 Adam 首步更新预算对齐 SGD。
- **Baseline** · Adam、AdamW、SGD、Shampoo、SOAP 与 PEFT。
- **Benchmark** · 11 个数据集、3 个 CLIP 骨干、5 个样本级别。
- **关键结果 / 消融** · SGD 全量微调优于代表性 PEFT，匹配首步预算解决大部分 Adam 崩溃。
- **适用条件 / 局限** · 结论限于所测 CLIP 与少样本设置。

**可复用机制** · 把优化器和可训练参数化拆成两个独立因素。

<a id="paper-155975"></a>

## Full-Sequence Masked Diffusion for Generative Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/155975) · [作者来源](https://openreview.net/forum?id=1PgMS3zgSx)

- **问题 / 瓶颈** · 逐项生成传播误差且难整体排序
- **核心创新 / 方法** · 对历史和列表统一掩码扩散并加列表排序损失
- **Baseline** · 自回归与逐项扩散推荐
- **Benchmark** · 多个公开推荐基准的准确度及列表质量
- **关键结果 / 消融** · 作者报告两类指标均改善
- **适用条件 / 局限** · 数据集和幅度待核

**可复用机制** · 比较并行生成与逐项生成的列表一致性

<a id="paper-154377"></a>

## Fully Distributed Tâtonnement for Chores Markets

[官方论文页](https://neurips.cc/virtual/2026/poster/154377) · [作者来源](https://openreview.net/forum?id=E0qPQ0rDjg)

- **问题 / 瓶颈** · 相对调价依赖跨任务聚合
- **核心创新 / 方法** · 按当前价格及本任务的超额需求乘法更新
- **Baseline** · 相对调价及朴素瓦尔拉斯调价
- **Benchmark** · Fisher 苦差市场的均衡收敛分析
- **关键结果 / 消融** · 对连续凸一次齐次不效用证明收敛
- **适用条件 / 局限** · 结论依赖市场和不效用假设

**可复用机制** · 优先检查能否用乘法更新隐式维持全局量

<a id="paper-149567"></a>

## Fully First-Order Algorithms for Online Non-Convex Bilevel Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149567) · [作者来源](https://openreview.net/forum?id=pACG95YX0v)

- **问题 / 瓶颈** · 隐式求导需要昂贵的二阶算子
- **核心创新 / 方法** · 改写为单层在线约束问题并构造时变拉格朗日函数
- **Baseline** · 基于超梯度的在线双层方法
- **Benchmark** · 确定性和随机设定的遗憾分析及数值实验
- **关键结果 / 消融** · 自适应版本遗憾为 O(log T + V_T)
- **适用条件 / 局限** · 要求下层强凸

**可复用机制** · 在二阶算子不可用时比较约束重写与超梯度

<a id="paper-155637"></a>

## FuncFormer: Circuit Representation Learning via the Flow of Functional Propagation

[官方论文页](https://neurips.cc/virtual/2026/poster/155637) · [作者来源](https://openreview.net/forum?id=46NBp3fllK)

- **问题 / 瓶颈** · 相似拓扑可能对应不同逻辑功能
- **核心创新 / 方法** · 编码随机输入的信号传播轨迹并用双路径注意力融合
- **Baseline** · DeepGate4 等
- **Benchmark** · 电路质量预测和形式验证
- **关键结果 / 消融** · 作者报告表现提升和跨规模泛化
- **适用条件 / 局限** · 依赖逻辑仿真及输入覆盖

**可复用机制** · 用功能行为监督结构表示以区分拓扑近似实例

<a id="paper-148533"></a>

## Functional Gradient Descent with Adaptive Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/148533) · [作者来源](https://openreview.net/forum?id=xCAaTAUix7)

- **问题 / 瓶颈** · 固定近似难处理无限维梯度
- **核心创新 / 方法** · 迭代适配梯度表示并把近似纳入收敛分析
- **Baseline** · 固定近似 FGD 和神经网络
- **Benchmark** · 回归、PDE 求解和视觉
- **关键结果 / 消融** · 光滑时收敛到驻点，另在类 PL 条件下到全局最小点
- **适用条件 / 局限** · 全局保证依赖光滑及类 PL 条件

**可复用机制** · 比较梯度空间自适应近似与固定基底

<a id="paper-148539"></a>

## FunctionEvolve: Structure-Guided Symbolic Regression with LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148539) · [作者来源](https://openreview.net/forum?id=x9ZPbfgvX4)

- **问题 / 瓶颈** · 不透明候选使局部修订和拟合不稳
- **核心创新 / 方法** · 以树摘要选父式、局部编辑并按结构拟合系数
- **Baseline** · 同骨干 LLM 方法和已发表首选结果
- **Benchmark** · LLM-SRBench 合成子集 129 题
- **关键结果 / 消融** · 恢复 113 个精确式，SA@50 为 87.6%
- **适用条件 / 局限** · 合成题结果不能代表嘈杂观测

**可复用机制** · 分开验证结构搜索和系数拟合对精确恢复的影响

<a id="paper-149521"></a>

## Function graph transformers universally approximate operators between  function spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/149521) · [作者来源](https://openreview.net/forum?id=pW2Yazkjyc)

- **问题 / 瓶颈** · 有限采样难描述连续算子及网格变化
- **核心创新 / 方法** · 把函数视作图上测度并约束输出仍为单值函数
- **Baseline** · 既有 Transformer 算子学习理论
- **Benchmark** · 连续函数空间、不同输出查询域及经正则化的 Sobolev 输入
- **关键结果 / 消融** · 证明标准自注意力与点式 MLP 可近似广泛算子类
- **适用条件 / 局限** · 属于表达能力保证

**可复用机制** · 用经验图测度刻画采样细化与连续极限

<a id="paper-148186"></a>

## FuRA: Full-Rank Parameter-Efficient Fine-Tuning with Spectral Preconditioning

[官方论文页](https://neurips.cc/virtual/2026/poster/148186) · [作者来源](https://openreview.net/forum?id=zf1vYk0XnQ)

- **问题 / 瓶颈** · 低秩或无约束更新可能扰动预训练表示
- **核心创新 / 方法** · 分块张量列车分解并训练小核心和分块奇异值
- **Baseline** · 全量微调、LoRA、QLoRA
- **Benchmark** · 常识推理、数学强化学习及视觉指令微调
- **关键结果 / 消融** · LLaMA-3-8B 常识任务较全量微调高 1.37
- **适用条件 / 局限** · 跨模型和初始化成本待核

**可复用机制** · 固定参数预算比较全秩谱约束和普通低秩适配

<a id="paper-152520"></a>

## FuseAdapt: Adaptation-Space Fusion for Multi-Modal Semantic Segmentation with Missing Modalities

[官方论文页](https://neurips.cc/virtual/2026/poster/152520) · [作者来源](https://openreview.net/forum?id=SWGx6oxOoy)

- **问题 / 瓶颈** · 独立融合模块可能不耐传感器缺失
- **核心创新 / 方法** · 冻结视觉骨干，在适配路径路由模态并预测被遮蔽嵌入
- **Baseline** · 多分支或独立融合方法
- **Benchmark** · MCubeS、DELIVER 等分割基准
- **关键结果 / 消融** · 训练期预测不增加部署计算
- **适用条件 / 局限** · 教师需要完整模态

**可复用机制** · 分开测全模态和随机缺失条件下的融合效果

<a id="paper-150560"></a>

## FusionNeXt: Sequence-First 3D Multi-Modal Fusion in the Era of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/150560) · [作者来源](https://openreview.net/forum?id=hEoPVPh3pb)

- **问题 / 瓶颈** · 三维融合常依赖多种专用运算
- **核心创新 / 方法** · 统一令牌并按空间局部性序列化，以通用注意力块融合
- **Baseline** · 专用卷积、注意力及视角变换的融合路线
- **Benchmark** · nuScenes 三维检测及 Occ3D
- **关键结果 / 消融** · 作者报告任务性能和推理效率兼优
- **适用条件 / 局限** · 依赖序列化保留局部结构

**可复用机制** · 固定骨干与预算测序列化对融合效率的影响

<a id="paper-152604"></a>

## Fusion or Confusion? Multimodal Complexity Is Not All You Need

[官方论文页](https://neurips.cc/virtual/2026/poster/152604) · [作者来源](https://openreview.net/forum?id=RtOPHuqmpj)

- **问题 / 瓶颈** · 方法间实验条件差异易夸大融合优势
- **核心创新 / 方法** · 统一重实现、初始化、交叉验证和统计检验
- **Baseline** · 单模态和 SimBaMM
- **Benchmark** · 19 种方法、9 个数据集，最多 23 种模态
- **关键结果 / 消融** · 复杂方法未稳定优于简单或单模态基线
- **适用条件 / 局限** · 适用结论受数据集和实现覆盖限制

**可复用机制** · 先为每个数据集建立单模态及简单融合强基线

<a id="paper-154014"></a>

## FUTON: Fourier Tensor Network for Implicit Neural Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/154014) · [作者来源](https://openreview.net/forum?id=Gru6lQkUxo)

- **问题 / 瓶颈** · MLP 隐式表示在拟合速度和外推上存在局限
- **核心创新 / 方法** · 结合可分正交傅里叶基与低秩张量分解
- **Baseline** · 先进 MLP 隐式表示
- **Benchmark** · 图像与体数据表示
- **关键结果 / 消融** · 作者报告训练快 2–5 倍并给出通用逼近定理
- **适用条件 / 局限** · 实测线性复杂度并非所有硬件上的保证

**可复用机制** · 在平滑或周期信号上对照低秩频谱和 MLP

<a id="paper-139347"></a>

## FutureSim: Replaying World Events to Evaluate Adaptive Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139347) · [作者来源](https://openreview.net/forum?id=VBt2tCcXYT)

- **问题 / 瓶颈** · 静态数据难测长期适应与校准
- **核心创新 / 方法** · 在模拟时期逐日开放当时可用新闻并让问题随后揭晓
- **Baseline** · 固定预测器及多种前沿 Agent
- **Benchmark** · 2026 年 1–3 月现实事件预测
- **关键结果 / 消融** · 最佳准确率 25%，不少模型校准差于固定预测器
- **适用条件 / 局限** · 新闻选取和模型知识截止时间影响公平性

**可复用机制** · 时间回放中锁定信息可见时间并报告校准

<a id="paper-139181"></a>

## fxBench: Evaluating and Understanding Formula Suggestions in Spreadsheets

[官方论文页](https://neurips.cc/virtual/2026/poster/139181) · [作者来源](https://openreview.net/forum?id=g7SjbXXc9n)

- **问题 / 瓶颈** · 最终公式错误无法定位是缺信息还是推断失败
- **核心创新 / 方法** · 拆分收集、理解上下文、理解意图及书写公式
- **Baseline** · 不同规模模型及不同上下文表示
- **Benchmark** · Sheetpedia 上 503 个公式建议任务
- **关键结果 / 消融** · 提供上下文选择策略的可达上界，细项待查正文
- **适用条件 / 局限** · 证据来自现有表格任务

**可复用机制** · 用人工证据标注定位工具建议的瓶颈

<a id="paper-155624"></a>

## G$^2$TR: Generation-Guided Visual Token Reduction for Separate-Encoder Unified Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155624) · [作者来源](https://openreview.net/forum?id=4BxXFxlAW1)

- **问题 / 瓶颈** · 仅按判别相关性剪枝会损害图像编辑
- **核心创新 / 方法** · 根据与 VAE 潜表示的一致性选令牌并合并冗余
- **Baseline** · 注意力或文本图像相似度选择路线
- **Benchmark** · 图像理解和编辑，测预填充计算
- **关键结果 / 消融** · 作者报告显著减少令牌和预填充成本
- **适用条件 / 局限** · 需要分离编码器及可用生成分支

**可复用机制** · 剪枝同时审计理解和生成质量以防单目标退化

<a id="paper-149246"></a>

## G2Fusion: Geometric-to-Generative Image Fusion via Registration-Restoration Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/149246) · [作者来源](https://openreview.net/forum?id=roBp7fgTLy)

- **问题 / 瓶颈** · 形变和传感退化会互相放大
- **核心创新 / 方法** · 流估计先减小大位移，扩散融合再细修残余错位与图像质量
- **Baseline** · 分别处理配准或恢复的融合路线
- **Benchmark** · 异构传感器图像融合，具体基准待核
- **关键结果 / 消融** · 摘要描述联合处理与模块互促，量化见正文
- **适用条件 / 局限** · 初始配准偏差可能传至生成步骤

**可复用机制** · 固定退化强度扫描配准误差并比较联合训练

<a id="paper-152843"></a>

## GADMVP: Adaptive Few-Shot Graph-Level Anomaly Detection with Multi-View Structured Prompting

[官方论文页](https://neurips.cc/virtual/2026/poster/152843) · [作者来源](https://openreview.net/forum?id=PxiWypLBRI)

- **问题 / 瓶颈** · 稀有异常图难以从少量标签泛化
- **核心创新 / 方法** · 构造图的图并从少数标签提炼结构提示
- **Baseline** · 少样本图级异常检测基线
- **Benchmark** · 多个图异常检测基准
- **关键结果 / 消融** · 作者报告少标签下提升稳定性
- **适用条件 / 局限** · 依赖跨图关系在新数据上可靠

**可复用机制** · 消融图间消息与结构提示，按异常类型报告召回

<a id="paper-154242"></a>

## GAE Falls Short in Imperfect-Information Self-Play Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154242) · [作者来源](https://openreview.net/forum?id=FCbPPpvjv6)

- **问题 / 瓶颈** · 即使 critic 精确，随机策略也使 GAE 有额外方差
- **核心创新 / 方法** · 由集中动作价值 critic 做多步 Expected SARSA 备份并保留 PPO 更新
- **Baseline** · GAE 和 PPO 自博弈
- **Benchmark** · 斗地主和无限注单挑德州扑克
- **关键结果 / 消融** · 作者报告多种规模游戏表现较强
- **适用条件 / 局限** · 依赖能计算策略期望及训练集中 critic

**可复用机制** · 用同一策略和 critic 比较采样备份与期望备份

<a id="paper-155867"></a>

## Gaeta-Lie Neural SDEs: Symmetry-Regularized Learning of Stochastic Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/155867) · [作者来源](https://openreview.net/forum?id=2IFjEJUD96)

- **问题 / 瓶颈** · 灵活 SDE 的系数恢复较弱
- **核心创新 / 方法** · 先拟合代理，再从有限生成元基搜索近似李对称性，最后惩罚伊藤对称性方程残差
- **Baseline** · 多种神经 SDE 方法
- **Benchmark** · 不同维度的 SDE 与真实数据
- **关键结果 / 消融** · 作者报告系数保真改善，少数据下仍有效
- **适用条件 / 局限** · 依赖基底覆盖及初始代理质量

**可复用机制** · 从拟合模型发现对称性后再正则化，并与同预算下的原方案对照。

<a id="paper-149536"></a>

## GAIA: Geometry-Adaptive Operator Learning for Forward and Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/149536) · [作者来源](https://openreview.net/forum?id=pPxfTs1tZU)

- **问题 / 瓶颈** · 同域假设限制边值与反问题
- **核心创新 / 方法** · 以边界和内部场编码几何，交叉注意力条件化积分变换
- **Baseline** · 摊销反演方法及专用正向求解器
- **Benchmark** · 七项二维、三维任务，比较相对 L2 误差
- **关键结果 / 消融** · 翼型和阻抗断层反演的中位相对误差较次优摊销方法分别降低 64% 和 27%
- **适用条件 / 局限** · 未覆盖的几何族仍需验证

**可复用机制** · 在输入输出域不同时用几何 token 调节积分核，并与同预算下的原方案对照。

<a id="paper-150408"></a>

## GaitLingo: Self-Supervised Gait Representation Learning with Language Priors

[官方论文页](https://neurips.cc/virtual/2026/poster/150408) · [作者来源](https://openreview.net/forum?id=iGvBtSYHHN)

- **问题 / 瓶颈** · 视觉自监督难识别罕见动作属性
- **核心创新 / 方法** · 按描述的信息量和稀有度加权，用软关系蒸馏对齐视觉嵌入
- **Baseline** · GaitSSB 等自监督方法
- **Benchmark** · 六项零样本步态基准，比较 Rank-1
- **关键结果 / 消融** · 摘要报告 Gait3D 和 GREW 分别提升 12.1% 和 7.9%
- **适用条件 / 局限** · 依赖描述可靠性，模块独立收益待核

**可复用机制** · 同时利用描述给样本加权并迁移样本关系，并与同预算下的原方案对照。

<a id="paper-155397"></a>

## GAMMA: Scalable 4D Gaussian Reconstruction Model for Novel View Synthesis of Monocular Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/155397) · [作者来源](https://openreview.net/forum?id=5xaZwIPnK0)

- **问题 / 瓶颈** · 多视图输入或逐场景优化限制使用
- **核心创新 / 方法** · 从单目视频生成统一四维高斯基元
- **Baseline** · 既有动态场景重建方法，具名待核
- **Benchmark** · 动态新视图合成，测保真及效率
- **关键结果 / 消融** · 作者报告重建用时秒级且可实时渲染，详细数值待核
- **适用条件 / 局限** · 依赖训练数据覆盖，长期遮挡边界待核

**可复用机制** · 将动态场景的外观、几何和运动纳入统一前馈表示，并与同预算下的原方案对照。

<a id="paper-150837"></a>

## GAPS: Gradient-Aware Adaptation-Gap Scoring for Time-Series Anomaly Detection with Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150837) · [作者来源](https://openreview.net/forum?id=ewNIO4p75i)

- **问题 / 瓶颈** · 绝对重建误差随噪声增长，可能倒置异常排序
- **核心创新 / 方法** · 用微调损失减零样本损失，按仅用校准数据的规则选择是否纳入评分
- **Baseline** · 标准重建误差
- **Benchmark** · 合成数据、HRV、TSB-AD-U 噪声压力测试
- **关键结果 / 消融** · 理论给出条件均值中的噪声方差抵消，压力测试改善
- **适用条件 / 局限** · 理论依赖论文的噪声假设及校准分布

**可复用机制** · 比较适配前后重建误差差值以隔离噪声，并与同预算下的原方案对照。

<a id="paper-150985"></a>

## GARDO: Reinforcing Diffusion Models without Reward Hacking

[官方论文页](https://neurips.cc/virtual/2026/poster/150985) · [作者来源](https://openreview.net/forum?id=dmPzzDSb7m)

- **问题 / 瓶颈** · 代理奖励可提高而真实质量和多样性下降
- **核心创新 / 方法** · 选择性正则、周期更新参考模型，并额外奖励高质量多样样本
- **Baseline** · 普遍施加参考正则的在线强化学习
- **Benchmark** · 多代理奖励和留出图像指标
- **关键结果 / 消融** · 作者报告减少奖励投机并保持探索，幅度待核
- **适用条件 / 局限** · 依赖不确定性与多样性估计

**可复用机制** · 仅对高不确定样本加参考约束，兼顾探索，并与同预算下的原方案对照。

<a id="paper-151322"></a>

## GATE-AD: Graph Attention Network Encoding for Few-Shot Industrial Visual Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151322) · [作者来源](https://openreview.net/forum?id=bN9jwBjZqY)

- **问题 / 瓶颈** · 少量正常样本下模型容易忽略局部不一致
- **核心创新 / 方法** · 用近邻图注意力重建图块，与输入潜空间对齐并用缩放余弦误差评分
- **Baseline** · 既有少样本检测方法
- **Benchmark** · MVTec AD、VisA、MPDD，1–8 样本图像 AUROC
- **关键结果 / 消融** · 大部分配置报告领先，在线成本不随支持集大小增长
- **适用条件 / 局限** · 依赖图块表征和近邻质量

**可复用机制** · 对冻结图块做掩码邻域重建并对齐原表征，并与同预算下的原方案对照。

<a id="paper-148191"></a>

## Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/148191) · [作者来源](https://openreview.net/forum?id=zdcl2dDW9a)

- **问题 / 瓶颈** · 单一门控难同时处理旧关联和新内容
- **核心创新 / 方法** · 按通道分别门控擦除和写入，推导分块并行训练
- **Baseline** · Mamba-2、Gated DeltaNet、KDA、Mamba-3
- **Benchmark** · 1.3B 模型、100B FineWeb-Edu token，含 RULER
- **关键结果 / 消融** · 作者报告整体改善，长上下文多键检索更明显
- **适用条件 / 局限** · 更大模型和训练规模效果待核

**可复用机制** · 将压缩记忆的擦除和写入门控分离，并与同预算下的原方案对照。

<a id="paper-155117"></a>

## GauGal: Gaussian-Galerkin Electromagnetic Inverse Scattering Imaging

[官方论文页](https://neurips.cc/virtual/2026/poster/155117) · [作者来源](https://openreview.net/forum?id=8HQ2ZpGXfE)

- **问题 / 瓶颈** · 逐点电磁反演过慢，纯数据方法跨设置不稳
- **核心创新 / 方法** · 将散射方程投影到高斯基元空间，使传播及观测成为可微基元算子
- **Baseline** · 物理优化和数据驱动反演
- **Benchmark** · 合成与实测电磁反演，含未见几何和传感器
- **关键结果 / 消融** · 摘要报告较物理对照从超过 30 分钟降至不到 10 秒
- **适用条件 / 局限** · 依赖基元对物体的表示能力

**可复用机制** · 将高斯基元直接用作物理求解单元，并与同预算下的原方案对照。

<a id="paper-155744"></a>

## GAUGECAST++: A Physics-Informed Latent Forecasting System for Localized Flood Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/155744) · [作者来源](https://openreview.net/forum?id=3JmNPDqHqq)

- **问题 / 瓶颈** · 稀疏水位观测下直接预测容易错过洪峰相位
- **核心创新 / 方法** · 用测站条件坐标变换降低残余输运，并约束短期组合的幅值与相位
- **Baseline** · 神经预报基线，具名待核
- **Benchmark** · 六个英国流域，MSE、NSE、峰值时刻及量级
- **关键结果 / 消融** · 作者报告各项指标一致改善
- **适用条件 / 局限** · 跨流域及极端事件适用性待核

**可复用机制** · 同时校验长期峰值时间与短步组合一致性，并与同预算下的原方案对照。

<a id="paper-152638"></a>

## Gauge-Symmetric Dual Lagrangian Frameworks for Born-Oppenheimer Molecular Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/152638) · [作者来源](https://openreview.net/forum?id=RYM51FF2fx)

- **问题 / 瓶颈** · 逐步自洽求解开销高，残差可能导致能量漂移
- **核心创新 / 方法** · 在 Grassmann 流形传播占据子空间，用耗散残差更新约束演化
- **Baseline** · 反复求解自洽场的量子动力学
- **Benchmark** · 分子动力学仿真基准，具体系统待核
- **关键结果 / 消融** · 作者报告稳定演化并避免逐步自洽循环
- **适用条件 / 局限** · 适用物理尺度及长期能量误差待核

**可复用机制** · 演化具有物理意义的子空间而非依赖具体基底，并与同预算下的原方案对照。

<a id="paper-152745"></a>

## GauS: Differentiable Scheduling Optimization via Gaussian Reparameterization

[官方论文页](https://neurips.cc/virtual/2026/poster/152745) · [作者来源](https://openreview.net/forum?id=QfSSTcTPqe)

- **问题 / 瓶颈** · 分类式松弛忽略时间顺序且搜索空间增长快
- **核心创新 / 方法** · 以高斯随机变量做可微调度，覆盖流水线及多目标约束
- **Baseline** · 精确求解、启发式与类别松弛路线
- **Benchmark** · 多项算子调度基准，比较多目标折衷
- **关键结果 / 消融** · 作者报告获得 Pareto 最优结果，细节待核
- **适用条件 / 局限** · 离散化后的可行性与规模效应待核

**可复用机制** · 用连续有序变量松弛离散时间槽，并与同预算下的原方案对照。

<a id="paper-150496"></a>

## Gaussian Density Splatting Network

[官方论文页](https://neurips.cc/virtual/2026/poster/150496) · [作者来源](https://openreview.net/forum?id=hfCqgxJnVP)

- **问题 / 瓶颈** · 固定网格密度图对分辨率敏感
- **核心创新 / 方法** · 由局部控制点回归高斯几何及质量，经可微渲染监督
- **Baseline** · 网格密度与既有计数方法
- **Benchmark** · 四个标准人群计数基准，名称及指标待核
- **关键结果 / 消融** · 作者报告一致改善
- **适用条件 / 局限** · 拥挤、遮挡与密度分布外表现待核

**可复用机制** · 把局部密度写成可求和的连续基元质量，并与同预算下的原方案对照。

<a id="paper-149805"></a>

## Gaussian Mixture Models in Hilbert Spaces via Kernel Methods

[官方论文页](https://neurips.cc/virtual/2026/poster/149805) · [作者来源](https://openreview.net/forum?id=nE56ZJgIrl)

- **问题 / 瓶颈** · 无限维对象难以用普通密度描述
- **核心创新 / 方法** · 以核均值嵌入定义 Hilbert 空间高斯混合并优化
- **Baseline** · 摘要未给具名对照
- **Benchmark** · 函数数据及 Laplacian 空间随机图
- **关键结果 / 消融** · 证明算法良定义及模型族稠密，摘要未给量化幅度
- **适用条件 / 局限** · 依赖所选 Hilbert 几何与核

**可复用机制** · 在难定义密度的空间用核均值估计混合分布，并与同预算下的原方案对照。

<a id="paper-154521"></a>

## Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors

[官方论文页](https://neurips.cc/virtual/2026/poster/154521) · [作者来源](https://openreview.net/forum?id=CzTKz9ux3w)

- **问题 / 瓶颈** · 单一变形骨架与孤立锚点忽略非局部动态
- **核心创新 / 方法** · 插值稀疏四维锚点生成高斯，并用固定记忆槽建模熵上下文
- **Baseline** · GIFStream
- **Benchmark** · Neu3D、Panoptic Sports、MPEG MIV 的 BD-rate
- **关键结果 / 消融** · 作者报告分别降低 84.54%、76.71%、83.94%
- **适用条件 / 局限** · 不同码率及编码延时待核

**可复用机制** · 用层级时空锚点共享基元参数并编码远距相关，并与同预算下的原方案对照。

<a id="paper-151440"></a>

## GazeFlow: From Human Gaze Behavior to Generative Egocentric Gaze Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/151440) · [作者来源](https://openreview.net/forum?id=agLR3seGuO)

- **问题 / 瓶颈** · 点预测难表示多种合理视线及扫视结构
- **核心创新 / 方法** · 将全局任务线索和视频局部视觉特征作为联合流匹配条件
- **Baseline** · 既有视线预测方法，具名待核
- **Benchmark** · 标准第一视角视线数据，逐帧指标和时序行为
- **关键结果 / 消融** · 作者报告逐帧及时间动态均改善，细节待核
- **适用条件 / 局限** · 任务线索质量及跨人群泛化待核

**可复用机制** · 用分布生成视线轨迹并评估跨帧一致性，并与同预算下的原方案对照。

<a id="paper-154093"></a>

## GCD: Correcting Hidden-State Bias in Off-Policy Agentic RL

[官方论文页](https://neurips.cc/virtual/2026/poster/154093) · [作者来源](https://openreview.net/forum?id=GHjzEOgABS)

- **问题 / 瓶颈** · 新参数复用旧缓存形成混合策略，单层权重校正可能不足
- **核心创新 / 方法** · 按层界估计漂移并检测尾部事件，组合既有可信域校正
- **Baseline** · M2PO 与全量重算
- **Benchmark** · Qwen3.5-9B、GRPO、MATH-500、τ-bench
- **关键结果 / 消融** · 作者报告较重算节省 38% 采样时间，零售 pass4 较 M2PO 提高 5.7 点
- **适用条件 / 局限** · 依赖漂移界及检测器有效性

**可复用机制** · 在异步训练中将缓存隐状态漂移与 token 权重偏差分别审计，并与同预算下的原方案对照。

<a id="paper-152070"></a>

## GCD: GCM-consistent Diffusion for Zero-shot Downscaling across Heterogeneous GCMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152070) · [作者来源](https://openreview.net/forum?id=VhUKsPYt7l)

- **问题 / 瓶颈** · 无成对数据且全球模型的频谱差异干扰后验采样
- **核心创新 / 方法** · 以地理边界条件化扩散先验，联合渐进蒸馏和共轭梯度修正
- **Baseline** · 普通扩散后验采样等，具名待核
- **Benchmark** · 五个异构全球模式，含极端分位与气旋细节
- **关键结果 / 消融** · 六步采样，作者报告 99 分位精度有竞争力
- **适用条件 / 局限** · 跨地理条件和极端分布待核

**可复用机制** · 用过滤测量算子匹配外部模型与高分辨率先验频谱，并与同预算下的原方案对照。

<a id="paper-152678"></a>

## GDMD: Guiding Distribution Matching Distillation with Gradient-Based Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152678) · [作者来源](https://openreview.net/forum?id=RFJrFfNSEC)

- **问题 / 瓶颈** · 早期含噪样本的得分与蒸馏目标容易冲突
- **核心创新 / 方法** · 把分布匹配梯度视为隐式目标，评分后调节更新权重
- **Baseline** · DMD、DMDR 与多步教师
- **Benchmark** · GenEval 与人类偏好，四次函数评估
- **关键结果 / 消融** · 作者报告四步生成超过多步教师及 DMDR
- **适用条件 / 局限** · 奖励模型可靠性与更广条件待核

**可复用机制** · 按蒸馏更新方向而非早期像素样本构造奖励权重，并与同预算下的原方案对照。
