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

<a id="paper-151913"></a>

## GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151913) · [作者来源](https://openreview.net/forum?id=WxO85pTOHz)

- **问题 / 瓶颈** · 扩散策略似然难以计算，随机掩码 ELBO 代理带来训练与推理不匹配。
- **核心创新 / 方法** · 从反向 KL 正则 RL 的闭式解构造优势引导教师，用免归一化目标匹配去噪 logits。
- **Baseline** · 先前 ELBO 类 RL 方法，具名版本待核实。
- **Benchmark** · LLaDA-8B 与 Dream-7B，规划、数学与编程任务，测试准确率及训练奖励走势。
- **关键结果 / 消融** · 摘要报告测试准确率最高提高 19.6%，训练奖励更稳定。
- **适用条件 / 局限** · 具体任务、代价和消融待核实。

**可复用机制** · 扩散策略似然难直接估计时，比较优势引导的 logits 匹配与 ELBO 策略优化。

<a id="paper-155708"></a>

## GEAR: A GPU-Accelerated Global Solver for Nonlinear Programs via Linear Bound Propagation

[官方论文页](https://neurips.cc/virtual/2026/poster/155708) · [作者来源](https://openreview.net/forum?id=3WdBmyLLLC)

- **问题 / 瓶颈** · 网络验证的线性传播面对一般非线性约束和全局目标时无法直接套用。
- **核心创新 / 方法** · 将传播的线性界同时用于对偶界、不可行检测和原始解搜索，收紧双线性松弛并耦合投影增广拉格朗日。
- **Baseline** · SCIP、BARON、LindoGlobal。
- **Benchmark** · GAMS 和 MINLPLib 的 505 个有界连续 NLP，180 秒内求解数。
- **关键结果 / 消融** · 解出 399 个，其中 104 个 SCIP 未解出。
- **适用条件 / 局限** · 证据限有界连续问题，轨迹规划表现和 GPU 成本待核实。

**可复用机制** · 把传播得到的约束松弛同时复用于全局界和原始可行解搜索。

<a id="paper-152259"></a>

## GEAR: Bridging the Planner-Actor Gap via Gradient-Aligned Policy Extraction

[官方论文页](https://neurips.cc/virtual/2026/poster/152259) · [作者来源](https://openreview.net/forum?id=UOmajXNPS7)

- **问题 / 瓶颈** · 规划与 actor 分治产生分布错位，前向 KL 覆盖多个相冲突的动作模式。
- **核心创新 / 方法** · 从连续时间 HJB 推导局部价值方向上的一阶对齐量，以其调制样本内策略提取权重。
- **Baseline** · 前向和反向 KL 类提取方法，具体实验基线待核实。
- **Benchmark** · HumanoidBench 连续控制，比较样本效率和最终性能。
- **关键结果 / 消融** · 作者报告样本效率和最终表现提升，数值待核实。
- **适用条件 / 局限** · 基准以外效果及对价值梯度估计误差的敏感性待核实。

**可复用机制** · 提取规划策略时测试按价值梯度加权，弱化方向有冲突的模仿样本。

<a id="paper-155668"></a>

## GEAR: Generator-Adaptive State Space Models for Associative Recall

[官方论文页](https://neurips.cc/virtual/2026/poster/155668) · [作者来源](https://openreview.net/forum?id=3skXDWaobd)

- **问题 / 瓶颈** · 固定容量循环状态限制上下文键值关联记忆。
- **核心创新 / 方法** · 慢速超网络产生 LoRA 系数，调整 token 到递归参数的生成器，保留 Mamba-3 线性扫描。
- **Baseline** · 等规模 Mamba-3 及同尺度消融。
- **Benchmark** · 180M 参数、2B FineWeb-Edu tokens，MQAR 候选限制 NLL。
- **关键结果 / 消融** · 紧凑 MQAR 在 32、64、128 个绑定处 NLL 分别降低 0.70、0.69、0.48。
- **适用条件 / 局限** · 主要证据为低规模训练和受控关联回忆，强干扰和更大模型的收益待核实。

**可复用机制** · 通过上下文适配参数生成器增强状态空间模型的关联检索。

<a id="paper-150448"></a>

## GeLVR: Geometry-Consistent Latent Visual Reasoning in Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/150448) · [作者来源](https://openreview.net/forum?id=hxfHcylGsr)

- **问题 / 瓶颈** · 逐槽监督忽略潜变量之间的几何关系，导致视觉潜空间碎裂。
- **核心创新 / 方法** · SFT 对齐关系结构，RL 用球面 von Mises–Fisher 策略和几何保持正则处理混合动作。
- **Baseline** · 既有视觉推理方法及组件消融，名称待核实。
- **Benchmark** · 多个视觉推理基准，含高分辨率和细粒度感知，数据集和指标待核实。
- **关键结果 / 消融** · 作者报告胜过现有方法并在消融中观察到组件贡献，数值待核实。
- **适用条件 / 局限** · 依赖球面策略与解码器几何相符，迁移范围待核实。

**可复用机制** · 视觉潜变量做奖励优化时同步保留 SFT 阶段学习到的关系结构。

<a id="paper-148804"></a>

## GEM: Interpretable Language Models via Geometric Embedding Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/148804) · [作者来源](https://openreview.net/forum?id=v0zubhBiC2)

- **问题 / 瓶颈** · 隐层状态与词表嵌入几何脱节，使逐层解读依赖额外探针。
- **核心创新 / 方法** · 预训练自监督约束最终隐状态接近预测概率加权的 token 向量组合。
- **Baseline** · 标准预训练。
- **Benchmark** · 135M、360M、760M 模型，比较困惑度、各向异性和逐层可解码性，语料与基准名称待核实。
- **关键结果 / 消融** · 作者报告困惑度最多下降 53%，并改善原生语言头的逐层解码和因果忠实度。
- **适用条件 / 局限** · 规模限 760M 及以下，具体指标和消融待核实。

**可复用机制** · 用模型自己的概率分布在词表空间生成目标向量，给隐表征提供可直接解码的几何约束。

<a id="paper-138976"></a>

## GenAI Evaluation Results are Largely Artifacts of Evaluation Design Choices: Evidence from Audit Studies of Resume Screening

[官方论文页](https://neurips.cc/virtual/2026/poster/138976) · [作者来源](https://openreview.net/forum?id=sy5IWI4jWC)

- **问题 / 瓶颈** · 围绕同一偏差问题的生成式 AI 审计结论受实验选择影响。
- **核心创新 / 方法** · 分解实验设计轴，并对姓名、岗位与简历配对及模型作组合反事实替换。
- **Baseline** · 三个复现实验框架。
- **Benchmark** · 36 篇简历筛选审计论文、1,134 次反事实实验，跟踪结论翻转率和留出预测 R²。
- **关键结果 / 消融** · 结论约 22% 的时候反转，部分设置的留出预测平均 R² 为 0.807。
- **适用条件 / 局限** · 观察来源为偏见审计；其他任务的翻转率需自行测量。

**可复用机制** · 在报告模型排序或偏差前，对关键评测模块做因子化扰动并统计结论稳定性。

<a id="paper-152591"></a>

## GenCOPE: Syn2Real Generalized Category-Level Object Pose Estimation for Robotic Picking

[官方论文页](https://neurips.cc/virtual/2026/poster/152591) · [作者来源](https://openreview.net/forum?id=RxgmX9P4VV)

- **问题 / 瓶颈** · 类级位姿估计依赖为新类采集大量真实数据，合成与真实纹理不同。
- **核心创新 / 方法** · 在 2D 和 3D 编码中施加类内语义一致性，以密集跨模态融合约束位姿回归，部署使用全局特征。
- **Baseline** · 既有类级位姿估计方法，具名对照待核实。
- **Benchmark** · REAL275、Wild6D 与机器人操纵实景，精度和效率指标待核实。
- **关键结果 / 消融** · 作者报告合成到真实泛化优于对照，提升幅度待核实。
- **适用条件 / 局限** · 适用范围受合成资产、类内形状变化和真实传感器域差影响，具体边界待核实。

**可复用机制** · 把识别共享形状与解除纹理捷径分开处理，在两种表征空间分别约束一致性。

<a id="paper-152039"></a>

## GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators

[官方论文页](https://neurips.cc/virtual/2026/poster/152039) · [作者来源](https://openreview.net/forum?id=W0Cx9tJ1x9)

- **问题 / 瓶颈** · 实际交互昂贵，静态训练集难随智能体能力变化。
- **核心创新 / 方法** · 让生成式模拟器与智能体共同进化，以课程奖励鼓励生成当前能力附近的任务。
- **Baseline** · 7B 对照、较大模型及 Gemini 2.5 Pro 离线增广。
- **Benchmark** · API-Bank、ALFWorld、BFCL、Bamboogle、TravelPlanner。
- **关键结果 / 消融** · 作者报告相对 7B 基线指标改善最高 40.3%，且比离线增广用更少数据。
- **适用条件 / 局限** · 实际训练预算、指标定义和模拟器失真影响待核实。

**可复用机制** · 将环境生成器当作可训练的课程策略，用当前能力反馈代替静态任务分布。

<a id="paper-139415"></a>

## General Agent Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139415) · [作者来源](https://openreview.net/forum?id=S7RB40ZMCQ)

- **问题 / 瓶颈** · 跨基准的协议胶水容易把架构和底座效应混在一起。
- **核心创新 / 方法** · 用统一协议和评测框架对 5 种架构、5 个底座和 6 个基准做全因子实验。
- **Baseline** · 工具调用、MCP、代码生成、CLI 等架构与领域定制 Agent。
- **Benchmark** · 软件工程、客服、深度研究和个人助理等六项评测，具名任务和指标待核实。
- **关键结果 / 消融** · 固定底座时架构差最高 12 个百分点；4/6 任务中领先通用 Agent 与领域定制对照无法区分。
- **适用条件 / 局限** · 覆盖的开源权重模型只有两个，协议排序不宜推广到其他底座。

**可复用机制** · 把协议选择与底座选择交叉评测，并报告特定组合的系统性失败。

<a id="paper-149308"></a>

## Generalised Linear Models in Deep Bayesian RL with Learnable Basis Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/149308) · [作者来源](https://openreview.net/forum?id=r9MG6uLaeW)

- **问题 / 瓶颈** · 任务参数与状态直接进入深层网络会依赖变分推断，任务表征容易混在一起。
- **核心创新 / 方法** · 在学习的基函数上构建广义线性转移和奖励模型，精确推断任务参数与噪声并计算边际似然。
- **Baseline** · 具代表性的既有 Meta-RL 方法，名称待核实。
- **Benchmark** · MuJoCo 与 MetaWorld，指标及任务划分待核实。
- **关键结果 / 消融** · 摘要报告性能最高达对照 1.8 倍，并给出任务表征距离和样本核对应的关系。
- **适用条件 / 局限** · 任务参数化受基函数模型约束，跨具身平台迁移待核实。

**可复用机制** · 试用可学习特征加可解析后验，隔离任务适应的推断复杂度与表示学习。

<a id="paper-153653"></a>

## Generalizable Physics Simulation through Compositional Energy Minimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153653) · [作者来源](https://openreview.net/forum?id=JjtvTbTp56)

- **问题 / 瓶颈** · 直接拟合总状态转移的 GNN 对新构形和实体数量泛化有限。
- **核心创新 / 方法** · 分别学习力对应的势能，推理时把势能相加并求全局最小值。
- **Baseline** · 既有 GNN 仿真方案，具名基线待核实。
- **Benchmark** · 2D、3D 和粒子仿真，含规模和构形外推，指标待核实。
- **关键结果 / 消融** · 作者报告优于 GNN 方案，幅度和求解代价待核实。
- **适用条件 / 局限** · 依赖目标动力学能以势能分解表达，非保守相互作用适用性待核实。

**可复用机制** · 用可复用的局部势能表达相互作用，再以组合和求解获得新系统动力学。

<a id="paper-154976"></a>

## Generalization at the Edge of Stability

[官方论文页](https://neurips.cc/virtual/2026/poster/154976) · [作者来源](https://openreview.net/forum?id=9UYTAT1rtr)

- **问题 / 瓶颈** · 稳定性边缘具有混沌振荡，仅用单值锐度指标难以反映吸引集结构。
- **核心创新 / 方法** · 把随机优化器表示为随机动力系统，借 Lyapunov 维数引入基于 Hessian 谱和部分行列式的泛化界。
- **Baseline** · 基于 Hessian 迹或谱范数的既有复杂度量。
- **Benchmark** · MLP、Transformer 和 grokking 实验，具体规模与指标待核实。
- **关键结果 / 消融** · 摘要报告实验与理论一致，未报告量化幅度。
- **适用条件 / 局限** · 完整谱计算代价和真实大模型上的可操作性待核实。

**可复用机制** · 诊断大步长泛化时对比谱形状或部分行列式与单一锐度指标的解释力。

<a id="paper-148559"></a>

## Generalization Dynamics of Linear Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148559) · [作者来源](https://openreview.net/forum?id=wzMJ3pDLv1)

- **问题 / 瓶颈** · 有限数据可能漏掉变异方向，训练损失无法反映这些方向的测试误差。
- **核心创新 / 方法** · 在高斯数据和线性去噪器下分区间分析样本量、协方差谱和正则的影响。
- **Baseline** · 理论对比不同样本维数比、谱衰减和正则设置。
- **Benchmark** · 高斯线性理论设置，以训练—测试损失差和采样分布 KL 衡量。
- **关键结果 / 消融** · 小样本区间中谱衰减、正则和早停可缓解过拟合；高样本区间 KL 以 d/N 量级收敛。
- **适用条件 / 局限** · 非线性扩散和真实数据尚需验证。

**可复用机制** · 用数据谱与样本量共同选择扩散训练的诊断维度，避免低训练误差掩盖未观测方向。

<a id="paper-152148"></a>

## Generalization Error Bounds for Picard-Type Operator Learning in Nonlinear Parabolic PDEs

[官方论文页](https://neurips.cc/virtual/2026/poster/152148) · [作者来源](https://openreview.net/forum?id=VB04LSNGnh)

- **问题 / 瓶颈** · 有限分辨率训练需保留非线性抛物 PDE 结构并降低离散化依赖。
- **核心创新 / 方法** · 将 Duhamel–Picard 迭代抽象为状态转移，误差界区分实现与估计，可跨时间块复用局部算子。
- **Baseline** · 理论分析 Picard 截断、实现和估计误差，具名实证对照待核实。
- **Benchmark** · 以环面非线性热方程和 Picard 型 FNO 说明，数据规模与指标待核实。
- **关键结果 / 消融** · 在理论条件下加深 Picard 迭代减少截断误差，而熵估计项不无界增长。
- **适用条件 / 局限** · 理论限非线性抛物 PDE 假设，超出该范围的动力学外推需验证。

**可复用机制** · 当动力学存在自然逐步校正形式时，先评估共享局部算子迭代深度再扩大模型。

<a id="paper-152152"></a>

## Generalization in Neural Networks Through the Lens of Magnitude Potential

[官方论文页](https://neurips.cc/virtual/2026/poster/152152) · [作者来源](https://openreview.net/forum?id=V9A3lPMU5E)

- **问题 / 瓶颈** · 常用全局几何指标难解释单点表征
- **核心创新 / 方法** · 以度量 magnitude potential 比较类内和全体样本对单点的表征
- **Baseline** · Feldman 记忆分数及神经坍缩
- **Benchmark** · 训练点记忆相关性与模运算 grokking
- **关键结果 / 消融** · 势比在抑制坍缩时仍有信息，并能检测决策边界变化
- **适用条件 / 局限** · 相关性不等同因果，跨任务效度待核

**可复用机制** · 将逐点势比和聚合边界信号分开报告

<a id="paper-140049"></a>

## Generalization Measures for Deep Learning Should Be Audited for Fragility

[官方论文页](https://neurips.cc/virtual/2026/poster/140049) · [作者来源](https://openreview.net/forum?id=ZbkyZd1PpG)

- **问题 / 瓶颈** · 训练后指标可能在预测质量几乎不变时反转
- **核心创新 / 方法** · 比较超参、时间、数据复杂度、匹配误差与不变性
- **Baseline** · 路径范数、参数空间 PAC-Bayes、函数空间边际似然
- **Benchmark** · 训练曲线和样本复杂度变化
- **关键结果 / 消融** · SGD 和 Adam 切换可反转路径范数趋势；校准基线也有局限
- **适用条件 / 局限** · 报告是审计证据，不能证明所有指标失效

**可复用机制** · 先验证对常规无关改变的稳定性，再解释指标与泛化的关系

<a id="paper-149408"></a>

## Generalization Without Compression Penalty: A Stability Analysis of Error Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/149408) · [作者来源](https://openreview.net/forum?id=qHC1EJ6gni)

- **问题 / 瓶颈** · 误差反馈的优化收敛不直接说明泛化
- **核心创新 / 方法** · 平均模型稳定性分析联合跟踪参数和误差缓冲
- **Baseline** · Top-k、Random-k、量化
- **Benchmark** · 凸损失及单节点和 DiLoCo-EF
- **关键结果 / 消融** · 凸设定的压缩稳定性项衰减，匹配收缩因子时实验轨迹接近
- **适用条件 / 局限** · 理论依赖凸设定，深网外推待验证

**可复用机制** · 压缩选型时比较同收缩率和同训练进度，而非只比较通信量

<a id="paper-152221"></a>

## Generalized Adaptive Boosting and the Geometry of Mistakes

[官方论文页](https://neurips.cc/virtual/2026/poster/152221) · [作者来源](https://openreview.net/forum?id=Uf1pIHYHQJ)

- **问题 / 瓶颈** · 单个聚合错误率无法表达代价不对称
- **核心创新 / 方法** · 用可达错误对集合定义 Z 学习器，几何刻画可提升性并自适应提升
- **Baseline** · 经典 boosting 和既有多目标扩展
- **Benchmark** · 误报和漏报对集合的理论分析
- **关键结果 / 消融** · 给出完整刻画及置信度放大结果
- **适用条件 / 局限** · 定理条件和算法成本待核全文

**可复用机制** · 先刻画联合误差保证再选提升方案

<a id="paper-151689"></a>

## Generalized Bayes for Causal Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/151689) · [作者来源](https://openreview.net/forum?id=Ym1qwTHLhL)

- **问题 / 瓶颈** · 完整生成似然要求难以指定的高维干扰项
- **核心创新 / 方法** · 直接对 ATE 或 CATE 设先验，用识别损失而非全数据似然更新
- **Baseline** · 标准贝叶斯及已有效果估计流程
- **Benchmark** · 多种因果估计设定，考察区间校准
- **关键结果 / 消融** · 正交损失下后验趋近 oracle，校准后可获频率有效性
- **适用条件 / 局限** · 依赖识别与正交条件，且后验需校准

**可复用机制** · 保留正交估计流水线，单独验证后验覆盖率

<a id="paper-149236"></a>

## Generalized Influence Functions for Better Model Change Estimates

[官方论文页](https://neurips.cc/virtual/2026/poster/149236) · [作者来源](https://openreview.net/forum?id=ruWxVzBmD7)

- **问题 / 瓶颈** · 全参数影响近似会扰动无关权重，阻尼有偏
- **核心创新 / 方法** · GIF 选限制子空间，p-LiSSA 求解限制的逆 Hessian 乘积
- **Baseline** · 普通影响函数和带阻尼求解
- **Benchmark** · 五项图像及文本遗忘基准
- **关键结果 / 消融** · 更新 10% 参数，准确率保持最高多 2.12 个百分点；求解残差缩小 9.6 倍
- **适用条件 / 局限** · 依赖梯度对齐和曲率，有限更新近似需复核

**可复用机制** · 将变化估计的子空间误差和逆问题残差分别检验

<a id="paper-151588"></a>

## Generalized Intention Modeling in Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151588) · [作者来源](https://openreview.net/forum?id=ZSayYS6nBW)

- **问题 / 瓶颈** · 固定下一动作或未来状态不一定代表各任务意图
- **核心创新 / 方法** · 学习多种表征的表现导向混合，增加与自身未来回报互信息的表征
- **Baseline** · 固定目标的对手建模
- **Benchmark** · 多智能体任务，比较策略表现
- **关键结果 / 消融** · 作者报告匹配或超过对照
- **适用条件 / 局限** · 仅适用于所测交互设定，分布变化需另测

**可复用机制** · 固定策略容量比较任务自适应的意图混合与预设目标

<a id="paper-154052"></a>

## Generalized Laplacian in Spectral Seriation on Manifold Data

[官方论文页](https://neurips.cc/virtual/2026/poster/154052) · [作者来源](https://openreview.net/forum?id=GZLpAjTrJj)

- **问题 / 瓶颈** · 标准谱序列化在节点度不均时可能敏感
- **核心创新 / 方法** · 比较移位、图差分与额外归一化的广义拉普拉斯
- **Baseline** · 标准归一化及其他广义变体
- **Benchmark** · 带噪闭曲线及图像拍摄角度
- **关键结果 / 消融** · 额外归一化对指数最稳健，理论用特征子空间扰动控误差
- **适用条件 / 局限** · 恢复至旋转和反射，限制于闭曲线设定

**可复用机制** · 用噪声和取样密度扫描选择归一化

<a id="paper-152117"></a>

## Generalized Priority-Aware Shapley Value

[官方论文页](https://neurips.cc/virtual/2026/poster/152117) · [作者来源](https://openreview.net/forum?id=VPwZ5z3kGM)

- **问题 / 瓶颈** · 传统优先 Shapley 通常要求二值无环优先图
- **核心创新 / 方法** · 按任意加权有向图惩罚随机排序中的违例
- **Baseline** · 经典 Shapley 及优先扩展
- **Benchmark** · Chatbot Arena 循环偏好图上的集成估值
- **关键结果 / 消融** · 不同个体和成对优先权平衡产生不同估值
- **适用条件 / 局限** · 依赖优先信号与权重定义

**可复用机制** · 报告优先权扫描下的估值稳定性

<a id="paper-156634"></a>

## Generalized Robust Adaptive-Bandwidth Multi-View Manifold Learning in High Dimensions with Noise

[官方论文页](https://neurips.cc/virtual/2026/poster/156634) · [作者来源](https://neurips.cc/virtual/2026/poster/156634)

- **问题 / 瓶颈** · 高维异质噪声使共享带宽损害嵌入
- **核心创新 / 方法** · 构建视图依赖带宽的联合扩散算子
- **Baseline** · 固定带宽和各视图等带宽
- **Benchmark** · 多视图数值实验，测抗噪和嵌入质量
- **关键结果 / 消融** · 共同流形下有渐近收敛，数值质量较对照改善
- **适用条件 / 局限** · 依赖共同潜流形模型，有限样本条件待核

**可复用机制** · 固定视图数据单独扫描带宽与噪声强度

<a id="paper-156744"></a>

## Generalized Smooth Stochastic Variational Inequalities: Almost Sure Convergence and Convergence Rates

[官方论文页](https://neurips.cc/virtual/2026/poster/156744) · [作者来源](https://openreview.net/forum?id=EjqSpbUBWU)

- **问题 / 瓶颈** · 全局平滑和随机样本有界假设可能不成立
- **核心创新 / 方法** · 分析裁剪投影与裁剪 Korpelevich 更新
- **Baseline** · 两类裁剪方法的理论分析
- **Benchmark** · 结构化非单调算子与 p-准锐性
- **关键结果 / 消融** · 给出几乎处处收敛，部分光滑指数下给出期望收敛率
- **适用条件 / 局限** · 依赖准锐性和广义光滑条件

**可复用机制** · 部署前用问题结构核对裁剪收敛定理可用性

<a id="paper-152114"></a>

## Generalized Wasserstein Flow Matching: Transport Plans, Everywhere, All at Once

[官方论文页](https://neurips.cc/virtual/2026/poster/152114) · [作者来源](https://openreview.net/forum?id=VRSgjWCWsh)

- **问题 / 瓶颈** · 逐点流难表达集合之间的嵌套几何
- **核心创新 / 方法** · 以内外两层传输计划导出速度，并用切片或线性 Wasserstein 近似
- **Baseline** · 既有点云及集合生成；具名待核
- **Benchmark** · 点云及集合生成，关注轨迹和计算可行性
- **关键结果 / 消融** · 作者报告更稳定的近直轨迹，数值待核
- **适用条件 / 局限** · 依赖嵌套距离近似，近似误差待查

**可复用机制** · 比较集合级与点级流对结构保留的差异

<a id="paper-154367"></a>

## Generalizing Action-Conditioned Latent World Models with Video Model Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/154367) · [作者来源](https://openreview.net/forum?id=E6rncT8Glg)

- **问题 / 瓶颈** · 生成画面把动力学与源域错配和伪影纠缠
- **核心创新 / 方法** · 用同动作环境随机化构造离线库，只加监督给冻结编码器的时间差分
- **Baseline** · 只用真实数据及直接蒸馏生成潜变量
- **Benchmark** · EgoDex、BAIR、Physion 的动作恢复、未来预测与接触读出
- **关键结果 / 消融** · 作者报告跨三类任务优于两种对照
- **适用条件 / 局限** · 依赖同动作生成质量，差分仍可能有伪影

**可复用机制** · 分开建模内容延续与动作变化，保持在线预测走潜空间

<a id="paper-149398"></a>

## Generalizing Test-time Compute-optimal Scaling as an Optimizable Graph

[官方论文页](https://neurips.cc/virtual/2026/poster/149398) · [作者来源](https://openreview.net/forum?id=qLpliLv4oh)

- **问题 / 瓶颈** · 固定协作拓扑与单模型可能无法适配任务
- **核心创新 / 方法** · 将多模型协作表示成概率图，以文本反馈迭代更新候选
- **Baseline** · 传统搜索和语言模型搜索对照
- **Benchmark** · 推理准确率、延迟和图搜索样本效率
- **关键结果 / 消融** · 作者报告联合目标及搜索效率改善
- **适用条件 / 局限** · 反馈开销与图迁移边界待查

**可复用机制** · 记录搜索成本和部署成本，比较固定拓扑与按任务搜索

<a id="paper-153719"></a>

## Generalizing the Geometry of Model Merging Through Fréchet Averages

[官方论文页](https://neurips.cc/virtual/2026/poster/153719) · [作者来源](https://openreview.net/forum?id=JHO7pEMdma)

- **问题 / 瓶颈** · 直接平均参数受模型对称性影响
- **核心创新 / 方法** · 将合并定义为测地距离最小化，低秩适配器使用商流形
- **Baseline** · Fisher merging 和现有 LoRA 合并方法
- **Benchmark** · LoRA 合并比较，具体任务与指标待核
- **关键结果 / 消融** · 部分简化设定覆盖 Fisher 合并，作者展示商空间实现
- **适用条件 / 局限** · 取决于度量与距离近似，非所有架构通用

**可复用机制** · 随机重参数化同一适配器，检验合并预测是否改变

<a id="paper-150849"></a>

## Generate in Reconstruction Space, Match in Semantic Space: Transport Geometry for One-Step Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150849) · [作者来源](https://openreview.net/forum?id=etwEuQt1jd)

- **问题 / 瓶颈** · 像素细节使估计分布对齐困难，优化评估特征会误导
- **核心创新 / 方法** · 用冻结 SSL 表征计算 Sinkhorn 散度，比较表示压缩和匹配稳定性
- **Baseline** · 其他表征与 Inception 匹配
- **Benchmark** · ImageNet 单步生成，考察 FID 和匹配稳定性
- **关键结果 / 消融** · 作者报告相应对照 FID 降至约 1/39，并观察到评估特征可能改善 FID 而损伤样本
- **适用条件 / 局限** · 倍率的具体参照及特征选择须查正文

**可复用机制** · 训练与评估可用不同特征，补充稳定性和样本质量检查

<a id="paper-149033"></a>

## Generating Financial Time Series by Matching Random Convolutional Features

[官方论文页](https://neurips.cc/virtual/2026/poster/149033) · [作者来源](https://openreview.net/forum?id=tLVW1Y9hBz)

- **问题 / 瓶颈** · 单条历史路径训练判别器易过拟合，路径签名截断受限
- **核心创新 / 方法** · 将 Rocket 类竞争统计软化为可微随机特征，匹配真实与生成序列
- **Baseline** · 签名特征和扩散方法
- **Benchmark** · 小样本金融序列生成、双样本检验与分类
- **关键结果 / 消融** · 作者报告生成对照改善，检验与分类也具竞争力
- **适用条件 / 局限** · 非平稳结构及对随机卷积种子的敏感性待核

**可复用机制** · 固定特征抽取器并比较特征匹配和学习判别器

<a id="paper-150409"></a>

## Generating from Discrete Distributions Using Diffusions: Insights from Random Constraint Satisfaction Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/150409) · [作者来源](https://openreview.net/forum?id=iGHKaEN77P)

- **问题 / 瓶颈** · 单一约束难度可能掩盖离散生成的机制差异
- **核心创新 / 方法** · 用随机 k-SAT 和 k-XORSAT 理论对照均匀解采样
- **Baseline** · 连续扩散、掩码离散扩散、理论理想精度
- **Benchmark** · 随机约束满足问题，测解生成精度
- **关键结果 / 消融** · 连续扩散在所测场景表现更好，变量排序可改善结果
- **适用条件 / 局限** · 只记录合成非生物证据，真实任务可迁移性待核

**可复用机制** · 跨约束密度与顺序开展同预算比较

<a id="paper-151636"></a>

## Generating in the Limit with Infinitely Many Hallucinations

[官方论文页](https://neurips.cc/virtual/2026/poster/151636) · [作者来源](https://openreview.net/forum?id=Z78RzgzukZ)

- **问题 / 瓶颈** · 覆盖广度与有效性可能冲突
- **核心创新 / 方法** · 用渐近精度、召回和固定比例新颖性分析极限生成
- **Baseline** · 要求最终始终有效的学习者
- **Benchmark** · 对手揭示目标语言的理论模型
- **关键结果 / 消融** · 允许无穷但零频率错误，在部分目标被永久隐去时可严格提高召回
- **适用条件 / 局限** · 抽象枚举假设不能直接推出现代语言模型的实测结果

**可复用机制** · 评测同时跟踪覆盖、无效率和重复率，区分计数与频率

<a id="paper-152322"></a>

## Generating the Wild: Individual-Consistent Image-to-Video Generation for Wildlife

[官方论文页](https://neurips.cc/virtual/2026/poster/152322) · [作者来源](https://openreview.net/forum?id=Twfrs5sTBH)

- **问题 / 瓶颈** · 图生视频会弱化区分个体的皮毛纹理、条纹和斑点。
- **核心创新 / 方法** · 冻结图生视频主干，从参考图像提取高频特征并结合前景信息，将身份 token 注入交叉注意力。
- **Baseline** · 现有图生视频方法，具名对照未报告。
- **Benchmark** · WildlifeVid 上评估图生视频与动物重识别，具体指标未报告。
- **关键结果 / 消融** · 摘要报告个体一致性更强，合成视频改善下游重识别。
- **适用条件 / 局限** · 证据集中于野生动物，其他对象和遮挡条件待验证。

**可复用机制** · 合成对象追踪训练数据时，用独立身份分支保护细粒度外观，并用下游重识别验证其价值。

<a id="paper-152197"></a>

## Generation-Drift-Guided Block Pruning for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152197) · [作者来源](https://openreview.net/forum?id=UqSplWfSWJ)

- **问题 / 瓶颈** · 局部差异和教师强制困惑度会低估某些模块对生成式推理的贡献。
- **核心创新 / 方法** · 自生成少量探测轨迹，按尾部位置的生成漂移估计模块重要性，再自适应搜索要移除的模块。
- **Baseline** · Block Influence、困惑度及其他结构化剪枝基线。
- **Benchmark** · 分类与生成式推理，具体数据集和指标未报告。
- **关键结果 / 消融** · 摘要报告生成式推理保留得更好。
- **适用条件 / 局限** · 探测场景覆盖与长轨迹稳定性的关系待验证。

**可复用机制** · 给生成式智能体裁剪模型时，用实际解码后的行为变化筛模块，并单独核对长程推理。

<a id="paper-149460"></a>

## Generation-for-Understanding with Structured Action Scripts for Embodied Multimodal Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149460) · [作者来源](https://openreview.net/forum?id=pwF9hVdYIp)

- **问题 / 瓶颈** · 事后视频描述偏粗，VLM 容易遗漏中间动作和结果状态。
- **核心创新 / 方法** · 将交互拆为原子事件和状态差分，用真实起止帧与脚本合成视频，按语义、端点、物理合理性和时序筛片，再组合为多粒度字幕与问答。
- **Baseline** · 事后标注式视频语言监督，具体对照未报告。
- **Benchmark** · 公开具身视频、干扰项幻觉测试、仿真 VLA 与实机任务，具体指标未报告。
- **关键结果 / 消融** · 摘要报告细粒度动作和结果识别、时序及下游控制获益。
- **适用条件 / 局限** · 依赖可得端点图像和能识别物理错误的验证器。

**可复用机制** · 缺少操作过程标签时，先指定状态变化和真实端点，再把可验证的生成片段用于 VLM 适配。

<a id="paper-153938"></a>

## Generation Navigator: A State-Aware Agentic Framework for Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153938) · [作者来源](https://openreview.net/forum?id=HS7Cbd4eu1)

- **问题 / 瓶颈** · 单个状态的奖励忽略中间改进、退化和空耗轮次。
- **核心创新 / 方法** · 把图像生成视为依赖当前状态的动作决策，用 PRE-GRPO 对轨迹的质量峰值、后续保持和效率赋奖。
- **Baseline** · 提示改写和手工规则闭环智能体，具名对照未报告。
- **Benchmark** · WISE 和 T2I-ReasonBench，指标为 WISE 得分和推理准确率。
- **关键结果 / 消融** · 摘要报告 WISE 为 0.90，T2I-ReasonBench 推理准确率为 79.06%。
- **适用条件 / 局限** · 依赖可评估的中间输出，其他工具链上的增益待验证。

**可复用机制** · 训练反复编辑输出的智能体时，分别评估最好中间结果、之后的退化和额外调用成本。

<a id="paper-149816"></a>

## Generative Active Learning via Bayesian Acquisition for Improving the Efficiency of Synthetic Data

[官方论文页](https://neurips.cc/virtual/2026/poster/149816) · [作者来源](https://openreview.net/forum?id=n94j33Dy4F)

- **问题 / 瓶颈** · 合成样本多并不保证能给目标模型提供新训练信号。
- **核心创新 / 方法** · 对目标模型末层做拉普拉斯近似估计 BALD，再用 Feynman–Kac 引导扩散生成以维持结构多样性。
- **Baseline** · 现有合成数据方案，具名对照未报告。
- **Benchmark** · Imagenette、ImageNet-100 分类和 MS-COCO 检测，评估下游精度及分布外泛化。
- **关键结果 / 消融** · 摘要报告下游精度与分布外泛化改善。
- **适用条件 / 局限** · 末层近似可能遗漏表征层不确定性，生成器能力仍限制数据覆盖。

**可复用机制** · 给感知系统补合成数据时，用下游模型的互信息选择生成方向，再核对多样性与任务效果。

<a id="paper-155388"></a>

## Generative Actor-Critic with Soft Bridge Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/155388) · [作者来源](https://openreview.net/forum?id=62FfbuBmjc)

- **问题 / 瓶颈** · 生成策略难计算动作边缘密度，多次共享网络调用增加控制时延和训练成本。
- **核心创新 / 方法** · 在 tanh 之前连接固定基潜变量与终端动作潜变量，把最大熵目标提升到对高熵参考桥的路径相对熵，有限步时化为采样转移控制能量。
- **Baseline** · 扩散和流匹配策略及轻量单遍 actor。
- **Benchmark** · 连续控制，比较回报、推理时延和计算开销，具名任务未报告。
- **关键结果 / 消融** · 摘要报告回报优于或接近强基线，推理维持低时延。
- **适用条件 / 局限** · 路径熵正则依赖所设参考过程和桥参数化。

**可复用机制** · 当控制需要多模态动作但时延紧，用小型分步桥对采样路径正则，并实测回报和时延。

<a id="paper-149988"></a>

## Generative Conformal Prediction with Optimized Coverage Allocation

[官方论文页](https://neurips.cc/virtual/2026/poster/149988) · [作者来源](https://openreview.net/forum?id=lgTafhvFUa)

- **问题 / 瓶颈** · 多模态或异质输出容易让共形集合过大。
- **核心创新 / 方法** · 用生成模型拟合条件分布，再优化不同排序位置的覆盖分配，给出混合整数线性规划与渐近密度水平集结果。
- **Baseline** · 现有共形预测方法，具名对照未报告。
- **Benchmark** · 合成、半合成和真实数据，比较覆盖有效性及集合效率。
- **关键结果 / 消融** · 摘要报告覆盖有效且集合更紧凑。
- **适用条件 / 局限** · 整数规划开销以及控制场景下覆盖保证的适用范围待核实。

**可复用机制** · 为多模态轨迹模型构造预测集合时，单独优化各分支覆盖分配，再测有限样本覆盖和集合大小。

<a id="paper-149041"></a>

## Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control

[官方论文页](https://neurips.cc/virtual/2026/poster/149041) · [作者来源](https://openreview.net/forum?id=tIN1NuFf6l)

- **问题 / 瓶颈** · 固定积分步数无法适应闭环动作规划的难度差异。
- **核心创新 / 方法** · 学习时间无条件的动作序列速度场，将动作生成改为迭代细化；以速度场范数作停止和不收敛信号。
- **Baseline** · 固定时间调度的扩散 Transformer 与流匹配 VLA。
- **Benchmark** · 仿真和实机任务比较控制表现与收敛式推理，具体任务未报告。
- **关键结果 / 消融** · 摘要报告任务表现持平或改善，允许不同决策使用不同细化步数。
- **适用条件 / 局限** · 范数是生成收敛信号，实际执行成功率仍需验证。

**可复用机制** · 给机器人动作生成分配推理步数时，比较固定调度和残差停止，并检查分布偏移下的误报。

<a id="paper-154926"></a>

## Generative Cross-Entropy: A Strictly Proper Loss for Data-Efficient Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/154926) · [作者来源](https://openreview.net/forum?id=9vWmNwDMJB)

- **问题 / 瓶颈** · 标签稀缺时标准交叉熵样本效率受限。
- **核心创新 / 方法** · 从类条件似然推导 GenCE，在批内对样本的 softmax 得分重新归一化，耦合同类例子的梯度；在完备性条件下证明严格适当性。
- **Baseline** · 标准交叉熵和其他常用损失。
- **Benchmark** · 三个数据集、两种架构，覆盖平衡少样本与类别不平衡，比较分类、校准及分布外检测。
- **关键结果 / 消融** · 摘要报告三类评测均获益。
- **适用条件 / 局限** · 依赖批内频率构成与完备性条件，极稀少类别表现待验证。

**可复用机制** · 低标签感知任务可实验性地更换交叉熵，联报准确率、校准和批大小敏感性。

<a id="paper-152354"></a>

## Generative Modeling by Value-Driven Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/152354) · [作者来源](https://openreview.net/forum?id=ThBmruiLEV)

- **问题 / 瓶颈** · 生成分布的随机输运若反复模拟，训练与采样计算负担较重。
- **核心创新 / 方法** · 将离散时间随机输运写作线性规划，以不需要模拟的原始对偶算法拟合价值函数并导出输运策略。
- **Baseline** · 流、扩散和薛定谔桥方法。
- **Benchmark** · 含条件生成和不配对图像翻译，数据与指标未报告。
- **关键结果 / 消融** · 摘要报告训练良好的策略产生较直路径并可快速模拟。
- **适用条件 / 局限** · 依赖价值函数拟合质量，具体计算优势待核实。

**可复用机制** · 训练条件生成器时，可把近似价值函数作为输运接口，并对比路径弯曲度、样本质量与耗时。

<a id="paper-154240"></a>

## Generative Modeling via Drifting

[官方论文页](https://neurips.cc/virtual/2026/poster/154240) · [作者来源](https://openreview.net/forum?id=FCkkBolf4o)

- **问题 / 瓶颈** · 扩散和流方法通常把分布迁移留给推理阶段的多步迭代。
- **核心创新 / 方法** · 引入在生成分布与数据分布匹配时达到平衡的漂移场，以此构造训练目标让参数更新迁移生成分布。
- **Baseline** · 迭代式流和扩散模型，具名方法未报告。
- **Benchmark** · ImageNet 256×256，评估潜空间和像素空间单步生成的 FID。
- **关键结果 / 消融** · 摘要报告潜空间 FID 1.54、像素空间 FID 1.61。
- **适用条件 / 局限** · 单步图像证据不涵盖时序生成或动作模型。

**可复用机制** · 低延迟生成可尝试训练期分布校正，并在等计算预算下比较单步输出质量。

<a id="paper-153794"></a>

## Generative Object Detection with Co-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/153794) · [作者来源](https://openreview.net/forum?id=IdUJaSN2pj)

- **问题 / 瓶颈** · 坐标 token 的间接监督使生成式检测缺少精细定位信号。
- **核心创新 / 方法** · 在视觉编码器接入 DETR 式目标查询，将查询投影到 token 空间，联合训练查询重建、定位和自回归生成，借交错掩码逐步撤去候选辅助。
- **Baseline** · 判别式与生成式检测器，具名对照未报告。
- **Benchmark** · 标准目标检测和指代表达理解任务，具体数据集和指标未报告。
- **关键结果 / 消融** · 摘要报告直接坐标生成改善，并保持定位和语言指代能力。
- **适用条件 / 局限** · 依赖对象级监督及分阶段训练，密集或未知类别下效果待验证。

**可复用机制** · 训练机器人语言定位时，可用检测器查询监督生成式模型，再撤掉外部候选验证是否真正获得定位能力。

<a id="paper-155741"></a>

## Generative OOD-regularized Model-based Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155741) · [作者来源](https://openreview.net/forum?id=3KDoYUU2CU)

- **问题 / 瓶颈** · 稀疏离线数据易引导策略选择分布外动作，检测更准也未必使策略更好。
- **核心创新 / 方法** · 将状态动作生成密度估计接入基于模型的离线强化学习，把策略更新限制到数据高密度区，并比较多个密度估计器。
- **Baseline** · 原始基于模型的离线 RL 与不同密度估计器。
- **Benchmark** · 真实医疗数据和稀疏离线 RL 数据，比较分布外检测与策略表现。
- **关键结果 / 消融** · 摘要报告医疗数据上优于当时基线 17%；稳定动力学中检测质量一般与策略收益正相关，动力学不确定时保守惩罚可能更合适。
- **适用条件 / 局限** · 存在理论条件，17% 对应具体指标和尺度未报告。

**可复用机制** · 选择机器人离线 RL 的惩罚时，按动力学误差分组比较策略收益，避免只按 OOD 检测精度选密度模型。

<a id="paper-155620"></a>

## Generative Scenario Rollouts for End-to-End Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/155620) · [作者来源](https://openreview.net/forum?id=4CvrLyVNLO)

- **问题 / 瓶颈** · 稀疏轨迹标注限制 VLA 对其他主体和长时域未来的推理。
- **核心创新 / 方法** · 用规划、运动和语言监督学习自车及其他主体潜变量，联合自回归预测未来潜变量和文本，以真实标签或伪标签作滚动一致性约束。
- **Baseline** · 主要以模仿学习训练的 VLA，具名对照未报告。
- **Benchmark** · Bench2Drive，开放及闭环设置，比较驾驶分数和成功率。
- **关键结果 / 消融** · 摘要报告驾驶分数和成功率分别增加 15.7 和 26.2。
- **适用条件 / 局限** · 证据来自自动驾驶，跨机器人平台以及伪标签误差传播待验证。

**可复用机制** · 长程具身规划可显式滚动预测其他主体和环境变化，并对不同预测长度测漂移。

<a id="paper-152786"></a>

## Generative Structure from Motion with Native 3D Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152786) · [作者来源](https://openreview.net/forum?id=QL96jpgsPY)

- **问题 / 瓶颈** · 先估位姿再生成几何会级联误差，单独三维生成又可能偏离输入。
- **核心创新 / 方法** · 用共享注意力联合去噪形状和各视角位姿潜变量，以紧凑 UV 体积表示限制序列长度，最后按恢复位姿取图像特征细化。
- **Baseline** · 运动恢复结构、串接重建与生成及三维生成基线。
- **Benchmark** · Toys4k 和 GSO 的四个未标定视角，使用新视角 PSNR、中位 Chamfer 距离和 Acc@5°。
- **关键结果 / 消融** · 相对最强三维生成基线，PSNR 增加 3.2–4.5 dB，Chamfer 距离降低 2.8–3.8 倍，位姿 Acc@5° 超过 96%。
- **适用条件 / 局限** · 对象级评测，未观测区域取决于生成先验。

**可复用机制** · 对视角稀疏的机器人观测，比较位姿几何联合建模与顺序建模，并独立测几何和位姿。

<a id="paper-155907"></a>

## GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/155907) · [作者来源](https://openreview.net/forum?id=1wiUEkM8XE)

- **问题 / 瓶颈** · 最终图像标量奖励难以归因到检索、参考选择和提示组合。
- **核心创新 / 方法** · 比较同请求的多次工具轨迹，提取强弱差异作为特权教师上下文，再以在策略自蒸馏施加 token 级监督。
- **Baseline** · 只使用图像级奖励的生成智能体和其他图像生成框架。
- **Benchmark** · 公共基准与 GenEvolve-Bench，具体指标未报告。
- **关键结果 / 消融** · 摘要报告相对强基线提升。
- **适用条件 / 局限** · 需要可比较的同目标轨迹及可靠质量排序。

**可复用机制** · 为多工具智能体做归因时，比较同任务轨迹，为教师提供可定位到动作级的差异。

<a id="paper-149818"></a>

## GenRec: Knowing Where to Reconstruct and Where to Generate

[官方论文页](https://neurips.cc/virtual/2026/poster/149818) · [作者来源](https://openreview.net/forum?id=n68heFQnNa)

- **问题 / 瓶颈** · 稀疏视图下可见像素有观测约束，遮挡像素有多个合理解。
- **核心创新 / 方法** · 以相机和单目深度生成观测掩码，联合去噪 RGB 与场景坐标；由掩码门控监督，只细化可见区的高频像素。
- **Baseline** · 比较纯生成新视角方法；具名模型未报告。
- **Benchmark** · RealEstate10K、DL3DV-10K、Mip-NeRF 360；单视图外推和双视图插值，分别度量观测区保真与未观测区感知质量。
- **关键结果 / 消融** · 作者摘要报告观测区保真最好，未观测区感知质量也优于纯生成基线；幅度未报告。
- **适用条件 / 局限** · 依赖单目深度和相机信息，摘要未报告错误掩码下的退化。

**可复用机制** · 对有观测和无观测区域分别配置损失，并分别测复原误差与生成质量。

<a id="paper-151044"></a>

## GenRM-Flow: Generators are Process-aware Reward Models in Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/151044) · [作者来源](https://openreview.net/forum?id=dPSEe9I3nw)

- **问题 / 瓶颈** · 外部视频打分器只看最终像素或冻结特征，生成器过程信息未被用来打分。
- **核心创新 / 方法** · 从 KL 约束的最优策略析出奖励，以流匹配似然代理将其表达为连续时间相对速度预测误差，再将奖励用于 Flow-GRPO。
- **Baseline** · 外部视觉语言打分器；讨论 DPO、IPO 与 RWR 作为偏好微调路径。
- **Benchmark** · 视频生成偏好对齐与下游生成质量；数据集与指标未报告。
- **关键结果 / 消融** · 作者摘要报告生成器内生奖励可替换外部评分并改善下游生成；幅度未报告。
- **适用条件 / 局限** · 证据针对流匹配视频生成，其他生成目标上的等价性未报告。

**可复用机制** · 有似然代理的生成器可先验证误差差分是否足以提供过程奖励，再决定训练外部打分器。

<a id="paper-153355"></a>

## Gen-Searcher: Reinforcing Agentic Search for Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153355) · [作者来源](https://openreview.net/forum?id=M0ZcmOLHIp)

- **问题 / 瓶颈** · 冻结生成器难以处理需要新知识或跨源证据的提示。
- **核心创新 / 方法** · 先监督微调多跳搜索代理，再用文本和图像两类反馈进行 GRPO，使代理收集陈述与参考图像。
- **Baseline** · 基于 Qwen-Image；比较其改进前表现。
- **Benchmark** · KnowGen 与 WISE，知识密集型图像生成；摘要以分数差报告结果。
- **关键结果 / 消融** · 作者摘要报告 KnowGen 约加 16 分，WISE 约加 15 分。
- **适用条件 / 局限** · 双奖励的独立贡献、搜索成本和噪声敏感性未报告。

**可复用机制** · 训练接入外部工具的生成代理时，将事实检索和视觉参考质量分别反馈，并用单奖励消融检查贡献。

<a id="paper-151515"></a>

## GenZ: Hybrid statistical–foundational models for knowledge discovery from real-valued multidimensional targets

[官方论文页](https://neurips.cc/virtual/2026/poster/151515) · [作者来源](https://openreview.net/forum?id=a4poCCC5UA)

- **问题 / 瓶颈** · 直接对样本总结容易只发现输入的常见属性，难以解释指定的连续目标。
- **核心创新 / 方法** · 按当前潜变量后验划分样本，请基础模型归纳组间语义差别，再以问答作为噪声特征解释多维目标。
- **Baseline** · 房价回归比较零样本基础模型与使用相同样本 LLM 嵌入的 TabPFN。
- **Benchmark** · 房价、Netflix 冷启动、亚利桑那物种生态、视觉皮层 fMRI；评估预测与发现的特征。
- **关键结果 / 消融** · 作者报告房价预测胜过两类基线；固定输入改变目标会得到不同语义特征；幅度未报告。
- **适用条件 / 局限** · 依赖基础模型能描述样本，共现特征的因果解释未验证。

**可复用机制** · 先用目标相关的后验组织样本，再让模型命名区别，并用固定输入、更换监督目标的实验确认特征随目标变化。

<a id="paper-138937"></a>

## GeoBiaset: A Counterfactual Benchmark for Demographic Bias in World-Level Geolocalization

[官方论文页](https://neurips.cc/virtual/2026/poster/138937) · [作者来源](https://openreview.net/forum?id=vKDpJIzx4W)

- **问题 / 瓶颈** · 总体地理定位准确率难以识别模型是否利用人物外观作地区捷径。
- **核心创新 / 方法** · 以带坐标背景构造外观变化的反事实前景，使用 POPI 统计预测是否偏向人物组关联地区，按地标可用性拆分。
- **Baseline** · 与未受该扰动的图像对照；具名模型未报告。
- **Benchmark** · GeoBiaset 的 9541 张图像与七组外观编辑；洲级表现、POPI 及地标分组。
- **关键结果 / 消融** · 作者摘要报告错配插入使洲级表现下降 16%–47%，无地标时注意更多落在面部。
- **适用条件 / 局限** · 编辑真实性及不同编辑来源的鲁棒性未报告。

**可复用机制** · 评估视觉定位捷径时改变可疑线索、保持标签不变，并测预测偏移的具体方向。

<a id="paper-154164"></a>

## GeoCurv-TTT: Geometry-Aware Deformation Restoration for 3D Test-Time Training

[官方论文页](https://neurips.cc/virtual/2026/poster/154164) · [作者来源](https://openreview.net/forum?id=FnOlkLApNW)

- **问题 / 瓶颈** · 点云分类遇到分布偏移时，随机掩码可能破坏关键几何。
- **核心创新 / 方法** · 低曲率平面定向形变，高曲率结构保持；单样本以恢复目标做自监督更新，流式以更新批归一化统计适应。
- **Baseline** · 比较几何无关遮挡和骨架式预任务；具名基线未报告。
- **Benchmark** · ModelNet40-C、ShapeNet-C、ScanObjectNN-C；准确率、效率及适应耗时。
- **关键结果 / 消融** · 作者摘要报告三套评测上的准确率和适应效率改善；具体数值未报告。
- **适用条件 / 局限** · 证据来自分类扰动基准，真实机器人流中的收益未报告。

**可复用机制** · 在设计三维自监督扰动时先保留任务所需的稳定结构，再测试较弱区域的扰动能否帮助适应。

<a id="paper-139820"></a>

## GeoG2U-Bench: When Does Generation Help Understanding in Ultra-High-Resolution Remote Sensing?

[官方论文页](https://neurips.cc/virtual/2026/poster/139820) · [作者来源](https://openreview.net/forum?id=2k7W2ijRCW)

- **问题 / 瓶颈** · 超高分辨率图像下，生成中间图像可能帮助观察，也可能引入伪证。
- **核心创新 / 方法** · 比较直接问答与生成后问答，要求输出可审计的局部裁剪、标注、区域图或时间回溯图。
- **Baseline** · 同任务的 Direct 与 Generate-then-Answer，覆盖若干模型族。
- **Benchmark** · GeoG2U-Bench 覆盖 300 城市、20 个子任务、约 3000 个样本，场景达 20000×20000 像素；比较问答表现。
- **关键结果 / 消融** · 作者摘要报告任务相关且可靠的中间图帮助跨尺度定位等任务，错误中间图可拖累答题。
- **适用条件 / 局限** · 来自遥感场景；摘要未给可靠性阈值或迁移评测。

**可复用机制** · 给多模态代理增加生成步骤前，先检查生成证据是否忠于输入，再按任务比较它对答案的净收益。

<a id="paper-148154"></a>

## GeoMamba: Geometry-Aware State Space Modeling for Image Restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/148154) · [作者来源](https://openreview.net/forum?id=ztrNOMAstc)

- **问题 / 瓶颈** · 相似性重排可让二维远邻在序列相邻，使固定离散步长错误沿用历史状态。
- **核心创新 / 方法** · 按相邻标记的欧氏距离设置离散时间步，衰减跨空间跳跃的影响；另以特征和梯度预测连续调制参数。
- **Baseline** · 与 Transformer、Mamba 的图像复原模型比较；具名版本未报告。
- **Benchmark** · 轻量及经典超分辨率、去噪与 JPEG 伪影去除；具名数据与指标未报告。
- **关键结果 / 消融** · 摘要报告超分辨率一致改善，其他两类任务表现更好或相当。
- **适用条件 / 局限** · 长跳跃也可能含相关上下文；极端扫描策略下的影响未报告。

**可复用机制** · 将空间数据重排成状态空间序列时，保留原坐标距离，比较固定步长和距离条件步长。

<a id="paper-155498"></a>

## GeoMemory: Geometry-Indexed Memory for Long-Horizon Interactive Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155498) · [作者来源](https://openreview.net/forum?id=57vx3F2jgX)

- **问题 / 瓶颈** · 有限窗口下仅依赖时间上下文会忘记旧位置，过度依赖空间记忆也会损伤新场景。
- **核心创新 / 方法** · 混合探索和重访样本，用连续前向训练扩大位姿差，以 VGGT 产出的增量三维缓存进行点到帧检索。
- **Baseline** · 仅时间上下文与空间记忆方法是摘要讨论的对照；具名模型未报告。
- **Benchmark** · Minecraft 交互生成；长程空间一致性、新场景视觉质量和实时性。
- **关键结果 / 消融** · 摘要报告长程一致性和新场景质量改善并支持实时交互；数值未报告。
- **适用条件 / 局限** · 依赖几何缓存质量，摘要未验证真实环境和大规模缓存。

**可复用机制** · 对可重访世界同时训练写入、查询与忽略空间记忆，并按探索或重访分别评估。

<a id="paper-153576"></a>

## Geometric Alignment without Functional Equivalence: A Layer-wise Analysis of the Speech-Text Modality Gap

[官方论文页](https://neurips.cc/virtual/2026/poster/153576) · [作者来源](https://openreview.net/forum?id=KNuSWirJEG)

- **问题 / 瓶颈** · 语音与文本表征可以在中层相似，但语音问答仍较差。
- **核心创新 / 方法** · 对齐语音和文本 token，逐层测 CKA、匹配样本的答案间隔与决策位置注意，干预语音时序。
- **Baseline** · ASR 接语言模型、原速语音和仅按数量合并 KV。
- **Benchmark** · 四个开放权重语音语言模型，SpeechMMLU、VoiceBench BBH；CKA、答案间隔及准确率。
- **关键结果 / 消融** · BBH 从 59.9% 提升到 1.2 倍语速的 62.1% 或去静音的 61.9%；两种干预分别修复 34.3%、38.2% 的文本答对语音答错样本。
- **适用条件 / 局限** · 只验证特定语音模型和任务；视觉长序列迁移未验证。

**可复用机制** · 遇到跨模态准确率差距时，用同内容配对测末层答案间隔，再决定是否优化时序聚合。

<a id="paper-150566"></a>

## Geometrically Disentangling Concept Learning from the Language Modeling Loss

[官方论文页](https://neurips.cc/virtual/2026/poster/150566) · [作者来源](https://openreview.net/forum?id=hCPiDLv4VS)

- **问题 / 瓶颈** · 下一词预测是单一损失，探针表现难以揭示损失何时对特定概念施加优化压力。
- **核心创新 / 方法** · 逐层逐检查点比较概念探针子空间与下一词损失平均梯度外积的对齐，即优化参与度。
- **Baseline** · 与概念探针表现及行为变化的时间轨迹对照。
- **Benchmark** · Pythia-1B 与 410M 的 19 个检查点；12 项词汇、句法和语义任务。
- **关键结果 / 消融** · 作者摘要报告优化参与峰值常早于最大行为变化，也观察到持续高值与多峰。
- **适用条件 / 局限** · 受探针定义影响，时间先后不确立因果，已有反例。

**可复用机制** · 定位能力突然出现前的变化时，把行为曲线与损失更新在目标概念方向上的投影并排分析。

<a id="paper-148252"></a>

## Geometric Analysis of Neural Regression Collapse via Intrinsic Dimension

[官方论文页](https://neurips.cc/virtual/2026/poster/148252) · [作者来源](https://openreview.net/forum?id=zGe5UWouYJ)

- **问题 / 瓶颈** · 分类中的表征塌缩经验未必适用于多变量回归。
- **核心创新 / 方法** · 对照末层特征和目标的内在维数，考察表征压缩在不同数据量与噪声条件下的影响。
- **Baseline** · 比较塌缩和未塌缩模型、变动特征维数的对照；具名模式未报告。
- **Benchmark** · 控制任务及合成回归；对照泛化表现与估计内在维数。
- **关键结果 / 消融** · 作者摘要报告回归塌缩降低表现，未塌缩条件下维数的效果依赖数据量与噪声。
- **适用条件 / 局限** · 摘要中维数关系不等式显示不完整，不能据此设通用阈值。

**可复用机制** · 调整连续控制表征瓶颈时，联合扫描维数、数据量和噪声，检查是否因过压缩丢失目标变化。

<a id="paper-155768"></a>

## Geometric Factual Recall in Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/155768) · [作者来源](https://openreview.net/forum?id=34a614De3N)

- **问题 / 瓶颈** · 关联矩阵记忆观点难解释嵌入中可承载的关系结构。
- **核心创新 / 方法** · 理论构造以属性向量的线性叠加编码主体，再由 ReLU 门控 MLP 按关系选出属性；测试单跳与多跳。
- **Baseline** · 与权重矩阵式关联存储的容量观点比较；多跳对照使用与省略思维链的构造。
- **Benchmark** · 随机双射的关系查询，单层单跳及关系链，比较嵌入容量和迁移。
- **关键结果 / 消融** · 作者证明受控单跳设定下对数嵌入维度已足够；重置主体嵌入后训练所得 MLP 可零样本适配新双射。
- **适用条件 / 局限** · 证据基于受控随机关系，开放文本、噪声和真实知识结构未验证。

**可复用机制** · 设计可更新的结构化记忆时，分别测试能否只替换记录向量而复用查询选择器。

<a id="paper-151572"></a>

## Geometric Gain Graph: Zero-Token Graph Construction for Multi-Hop RAG

[官方论文页](https://neurips.cc/virtual/2026/poster/151572) · [作者来源](https://openreview.net/forum?id=ZbE8MH6DMy)

- **问题 / 瓶颈** · 纯相似检索易集中于重复证据，生成式抽取构图则增加成本且可能偏题。
- **核心创新 / 方法** · 在文档嵌入中用 cosθ×sinθ 构边衡量相关和差异，并以拓扑惩罚压低常见枢纽，引导扩散接触外围证据。
- **Baseline** · 比较依赖语言模型构图的 Graph RAG；具名系统未报告。
- **Benchmark** · 复杂多跳问答，比较答案表现和构图时语言模型 token 使用；具名数据未报告。
- **关键结果 / 消融** · 作者报告多跳表现优于 Graph RAG 基线且构图不调用语言模型；向量计算仍需要资源。
- **适用条件 / 局限** · 结果依赖嵌入能表达互补证据；域迁移、建立邻接的计算规模未报告。

**可复用机制** · 多跳 RAG 可先对比纯相似、相关性乘差异与枢纽惩罚，分别监测召回重复与遗漏长尾证据。

<a id="paper-154169"></a>

## Geometric Instability of Hidden-State Trajectories Predicts Reasoning Failures in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154169) · [作者来源](https://openreview.net/forum?id=FlBf0YQuYc)

- **问题 / 瓶颈** · 流畅的错误推理可能同时具有高输出置信度。
- **核心创新 / 方法** · VANE 从单次前向的逐层隐藏状态提取速度、加速度或急动、曲率、测地偏离和 token 连贯性。
- **Baseline** · 比较 token 对数概率，并用基础模型作指令微调对照。
- **Benchmark** · 六个 1.5B–72B 模型及五个数学、代码和语言推理基准，指标为 AUROC、覆盖率和选择性准确率。
- **关键结果 / 消融** · AUROC 为 70.7–96.6，30 组平均高于对数概率 25 个百分点；70B 量级量化模型在 50% 覆盖率下达到 96.1% 准确率。
- **适用条件 / 局限** · 依赖逐层隐藏状态；具体基准名称待核实。

**可复用机制** · 比较按轨迹不稳定性与输出对数概率筛选推理答案时的覆盖率–准确率曲线。

<a id="paper-155324"></a>

## Geometric Latent Reasoning Induces Shorter Generations in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155324) · [作者来源](https://openreview.net/forum?id=6TX25lR2SG)

- **问题 / 瓶颈** · 显式推理受离散词表和生成长度约束。
- **核心创新 / 方法** · GLR 在预训练词嵌入空间训练轻量转移头，以文本思维链为锚点预测方向更新，容许连续轨迹偏离实际 token。
- **Baseline** · 显式思维链；具名对照待核实。
- **Benchmark** · Qwen3 数学推理，比较生成步数与解题表现；数据集待核实。
- **关键结果 / 消融** · 作者摘要报告没有长度损失也会缩短生成，幅度待核实。
- **适用条件 / 局限** · 证据限于 Qwen3 数学任务，连续步成本和准确率的关系仍需分开测量。

**可复用机制** · 固定总计算预算，对比部分连续思考和全离散生成，并同时报告正确率及两类步数。

<a id="paper-150955"></a>

## Geometric Prompt-Trajectory Planning for Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/150955) · [作者来源](https://openreview.net/forum?id=e22Krci8Dn)

- **问题 / 瓶颈** · 并行抽样成本随调用数上升，而且错误可能高度相关。
- **核心创新 / 方法** · Maze 缓存冻结编码器的示例向量，以轻量路径评分器排序少样本示例序列，只用排名靠前的序列调用目标模型。
- **Baseline** · 单次调用提示优化、宽度优先抽样和 best-of-N。
- **Benchmark** · 多项推理评测，比较推理表现、调用数及延迟；具名基准待核实。
- **关键结果 / 消融** · 作者报告 Maze 单次调用优于单次调用对照，MultiMaze 用更低调用数和延迟获得较大部分并行采样收益。
- **适用条件 / 局限** · 依赖候选池覆盖优质示例序列且评分能辨别好序列。

**可复用机制** · 比较增加候选提示排序深度与增加模型采样次数在同一延迟下的收益。

<a id="paper-150508"></a>

## Geometry-Adaptive Explainer for Faithful Dictionary-Based Interpretability under Distribution Shift

[官方论文页](https://neurips.cc/virtual/2026/poster/150508) · [作者来源](https://openreview.net/forum?id=hZQ6hH0lDD)

- **问题 / 瓶颈** · 域偏移可能旋转活跃表征子空间，降低在原域训练的解释字典的因果忠实度。
- **核心创新 / 方法** · GAE 用新域活跃子空间对齐稀疏字典，同时保留原有特征结构，无需梯度更新。
- **Baseline** · 稀疏自编码器和 transcoder 是适用字典；比较未适配字典及基于训练的适配对照。
- **Benchmark** · 多模型和多个分布偏移设置，比较因果忠实度；具名任务待核实。
- **关键结果 / 消融** · 作者证明相对未适配字典改善，超额损失受二阶矩偏移的二次界控制；实验中达到或超过训练式对照。
- **适用条件 / 局限** · 需要访问无标签目标域激活；具名模型和指标待核实。

**可复用机制** · 先测新域的活跃子空间偏移，再用干预测试几何对齐是否恢复原字典的因果解释。

<a id="paper-148380"></a>

## Geometry-Aware Flow Matching for Sparse-View 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/148380) · [作者来源](https://openreview.net/forum?id=yKjmobiqnX)

- **问题 / 瓶颈** · 稀疏视图高斯重建直接预测终点，布局和细节的生成路径缺乏监督。
- **核心创新 / 方法** · GRiF 用视图条件流匹配推进层级化高斯状态，以旋转感知路径更新方向变量。
- **Baseline** · 比较直接预测最终场景的前馈高斯重建方法；具名对照待核实。
- **Benchmark** · RealEstate10K、ACID 域内重建，ScanNet、DL3DV、DTU 零样本迁移；具名指标待核实。
- **关键结果 / 消融** · 作者报告域内重建及跨域迁移均改善。
- **适用条件 / 局限** · 依赖受控的源场景和层级状态设计；生成耗时待核实。

**可复用机制** · 对含旋转、位置和外观的状态，比较共享端点回归与按属性几何构造的条件生成路径。

<a id="paper-150070"></a>

## Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice

[官方论文页](https://neurips.cc/virtual/2026/poster/150070) · [作者来源](https://openreview.net/forum?id=kyUowLfsTH)

- **问题 / 瓶颈** · 只按运行时间排序会忽略解码时 KV 缓存随序列增长而变化。
- **核心创新 / 方法** · SVF 最小体积优先，其 1-bit 变体用一位提示减少长度信息依赖，并集成到 vLLM。
- **Baseline** · 比较时间优先调度如最短作业优先，并与既有 SVF 理论界比较。
- **Benchmark** · vLLM 上的 Llama-3.1，比较平均延迟、尾延迟、吞吐及理论竞争比。
- **关键结果 / 消融** · 已知输出长度时竞争比上界从 48 收紧到 5；摘要报告平均和尾延迟改善。
- **适用条件 / 局限** · 理论界 5 依赖已知输出长度，1-bit 设置需单独评估。

**可复用机制** · 多模态交互推理若受 KV 显存限制，分别用执行时间和显存×时间为同一请求序列排序。

<a id="paper-153365"></a>

## Geometry-Aware Representation Denoising for Multi-view Image Restoration and 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/153365) · [作者来源](https://openreview.net/forum?id=LvYWFrtR8k)

- **问题 / 瓶颈** · 前馈多视角重建器在退化图像上容易失准。
- **核心创新 / 方法** · GARD 在重建器几何感知特征空间执行扩散复原，并用额外解码器从净化表征恢复 RGB。
- **Baseline** · 基于前馈重建器改进；具名比较方法待核实。
- **Benchmark** · DA3 多视角图像复原与三维重建；退化类型和具名指标待核实。
- **关键结果 / 消融** · 作者报告几何和图像均改善，幅度待核实。
- **适用条件 / 局限** · 依赖重建底座的表征含有足够的几何信息。

**可复用机制** · 对比像素预处理与特征去噪，同时测量几何质量和成像质量，防止图像观感掩盖几何错误。

<a id="paper-155279"></a>

## Geometry-Aware Zeroth-Order Optimization for Fine-Tuning Quantized LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/155279) · [作者来源](https://openreview.net/forum?id=6r0PI7Q3I7)

- **问题 / 瓶颈** · 对严格正的量化尺度采用欧氏扰动会越过可行边界。
- **核心创新 / 方法** · HoZO 建立测地完备的黎曼度量和闭式指数映射，使零阶扰动保持尺度为正。
- **Baseline** · 比较既有零阶优化及一阶微调；具名零阶方法待核实。
- **Benchmark** · 六项下游任务与三种模型规模，比较任务表现及显存；含 4-bit Llama-2-70B。
- **关键结果 / 消融** · 作者报告比一阶微调少用 34 倍显存，单张 48 GB GPU 完成上述量化模型微调。
- **适用条件 / 局限** · 具名任务及相同显存预算下的性能差异待核实。

**可复用机制** · 对正值参数先选择可行域内的双侧扰动，再比较欧氏扰动加裁剪是否引入估计偏差。

<a id="paper-148649"></a>

## Geometry-Calibrated Conformal Abstention for Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148649) · [作者来源](https://openreview.net/forum?id=wAjaheyp6R)

- **问题 / 瓶颈** · 开放式答案难以直接给出共形预测所需的不一致分数，重训拒答行为可能过度保守。
- **核心创新 / 方法** · CA 以后处理方式结合表征几何校准与共形阈值，为参与率和回答正确率给出有限样本保证。
- **Baseline** · 从共形预测改造；具名经验对照待核实。
- **Benchmark** · 开放式语言模型选择性回答，以参与率和条件正确率评价；具名数据集待核实。
- **关键结果 / 消融** · 作者摘要报告选择性回答改善，条件正确率为 75%。
- **适用条件 / 局限** · 依赖可访问内表征；校准集与部署分布变化时的保证待核实。

**可复用机制** · 设计 agent 的拒答或请求外部工具阈值时，同时约束参与率和条件正确率。

<a id="paper-149549"></a>

## Geometry-Centered 3D Latent World Models for Growing Surfaces

[官方论文页](https://neurips.cc/virtual/2026/poster/149549) · [作者来源](https://openreview.net/forum?id=pJ1GLwHzZ6)

- **问题 / 瓶颈** · 固定支撑域或像素预测的世界模型难以表示物质增加时几何范围的变化。
- **核心创新 / 方法** · FOLIAGE 将成熟区域压缩为骨架，为活跃生长前沿保留高分辨率，并将可部署多模态观测、动作条件和仅训练时使用的物理能量分开。
- **Baseline** · 摘要报告比较强基线，具名方法待核实。
- **Benchmark** · SURF-GARDEN、SURF-BENCH，比较材料逆推、五步网格预测 Chamfer 误差以及跨模态 mAP@100，并评估传感器丢失和对应扰动。
- **关键结果 / 消融** · 相对对照三项结果约为误差降低 40%、误差降低 20%、检索提升 25%；另有真实植物与动态三维迁移。
- **适用条件 / 局限** · 主证据来自生长表面基准；训练依赖特权物理信号。

**可复用机制** · 将高分辨率潜状态放在控制或结构改变的边界，固定预算下与均匀空间表征比较。

<a id="paper-155126"></a>

## Geometry Conflict: Explaining and Controlling Forgetting in LLM Continual Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/155126) · [作者来源](https://openreview.net/forum?id=8EOfA3Wh07)

- **问题 / 瓶颈** · 连续后训练中任务更新可能相互干扰
- **核心创新 / 方法** · 以参数更新的协方差表示任务几何，用高斯 Wasserstein 重心构造共享度量，以冲突门控合并校正
- **Baseline** · 无数据合并方法，具名对照未报告
- **Benchmark** · Qwen3 0.6B 至 14B，持续学习领域和能力两类设置，评估保留能力与最终表现
- **关键结果 / 消融** · 摘要报告两类表现均优于无数据对照，幅度未报告
- **适用条件 / 局限** · 摘要未给出其他模型家族结果

**可复用机制** · 比较固定任务相似度与随当前权重变化的冲突度对遗忘的预测能力

<a id="paper-153809"></a>

## Geometry-Constrained Kolmogorov–Arnold Networks: Learning Edge Geometry via Banach Duality

[官方论文页](https://neurips.cc/virtual/2026/poster/153809) · [作者来源](https://openreview.net/forum?id=IYu64aV0LR)

- **问题 / 瓶颈** · 固定基函数预设边函数响应
- **核心创新 / 方法** · 从 Banach 对偶映射构建边激活，每条边学习一个指数，调整阈值响应和原点附近敏感性
- **Baseline** · 固定基 KAN，包括交叉验证样条
- **Benchmark** · 50 道 Feynman 符号回归方程，含少样本和噪声条件
- **关键结果 / 消融** · 相对样条赢下 85/90 个少样本设置，报告噪声退化 3.7 倍对 21.6 倍
- **适用条件 / 局限** · 证据聚焦符号回归

**可复用机制** · 对重视抗扰的边函数同时比较拟合误差和扰动放大

<a id="paper-150174"></a>

## Geometry-Guided Semantic Reconstruction for 3D Instance Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/150174) · [作者来源](https://openreview.net/forum?id=k8lnRfJDKH)

- **问题 / 瓶颈** · 直接拼接无法确保语义和三维结构对齐
- **核心创新 / 方法** · 遮挡部分背景上的提升二维先验，让三维编码器重建，并在稀疏编码前用几何调制先验
- **Baseline** · 两个实例分割基架，具名版本未报告
- **Benchmark** · ScanNetV2 和 ScanNet200，全数据及少样本三维实例分割，指标未报告
- **关键结果 / 消融** · 结果更好或相当，幅度未报告
- **适用条件 / 局限** · 依赖可提升到三维坐标的二维先验

**可复用机制** · 将跨表征融合改成受目标几何约束的遮挡恢复任务

<a id="paper-149198"></a>

## Geometry is an Operator: Lie-Algebraic Space Routing for View-Robust 3D MLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149198) · [作者来源](https://openreview.net/forum?id=sBOq6IiZpM)

- **问题 / 瓶颈** · 几何加性注入难以校正跨视角语义漂移
- **核心创新 / 方法** · 从三维 token 预测旋转状态和路由系数，按三元组施加 Lie 群作用，融合原始、三维上下文与变换路径
- **Baseline** · 加性几何融合方法
- **Benchmark** · 三维场景理解和空间推理，含大姿态变化分组，具名数据与指标未报告
- **关键结果 / 消融** · 报告跨视角稳健性提高，严重姿态变化下收益尤明显
- **适用条件 / 局限** · 依赖可用三维几何 token

**可复用机制** · 跨视角表征可比较显式群作用与添加几何特征

<a id="paper-149667"></a>

## Geometry Matters in Packed 3D Attention

[官方论文页](https://neurips.cc/virtual/2026/poster/149667) · [作者来源](https://openreview.net/forum?id=oLN3S4iIZn)

- **问题 / 瓶颈** · 压紧三维 token 后序列距离随布局改变
- **核心创新 / 方法** · 局部注意力保持精确，远场用三维连续块摘要，压缩前以真实网格坐标施加轴向 RoPE
- **Baseline** · 匹配的可学习位置局部全局注意力、TokenGrid 3D U-Net、稠密 SDPA
- **Benchmark** · 合成重打包，Allen WTC–11 hiPSC 显微图像，测 macro Dice 和延迟
- **关键结果 / 消融** · 262k token 下最终 macro Dice 高 0.1248，65k token 实现在摘要设置下比稠密 SDPA 快 6.49 倍
- **适用条件 / 局限** · 主要实证来自显微三维网格

**可复用机制** · 改变打包顺序做不变性检查，可发现模型学到了布局

<a id="paper-150238"></a>

## Geometry Meets Physics: Data-Efficient Pre-Training for Unstructured Neural PDE Solvers

[官方论文页](https://neurips.cc/virtual/2026/poster/150238) · [作者来源](https://openreview.net/forum?id=jidnQA2TIz)

- **问题 / 瓶颈** · 非结构化三维 PDE 求解标注数据昂贵
- **核心创新 / 方法** · 稳态用内蕴形状描述符学习域表征，瞬态以在线合成 PDE 数据预训练
- **Baseline** · 摘要未点名对照
- **Benchmark** · 稳态与瞬态 PDE 下游少数据微调，摘要未给具名数据集和误差定义
- **关键结果 / 消融** · 报告最高 3 倍收敛速度、2 倍数据效率及最高 25% 精度提升
- **适用条件 / 局限** · 依赖形状描述符或合成物理与下游任务共享结构

**可复用机制** · 数据昂贵的物理代理模型可先检验廉价物理预训练能否改善微调

<a id="paper-150707"></a>

## Geometry over Density: Few-Shot Cross-Domain OOD Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/150707) · [作者来源](https://openreview.net/forum?id=g7cJBv2nOf)

- **问题 / 瓶颈** · 新域往往只有少量域内样本
- **核心创新 / 方法** · 由扩散模型分数构造幅值积分和动态平滑度两个量，刻画轨迹交互
- **Baseline** · 需用 5 万至 16.3 万样本训练的对照，名称未报告
- **Benchmark** · 12 组跨域 OOD 测试，每组约 100 个无标注域内样本，指标 AUROC
- **关键结果 / 消融** · 平均 AUROC 93.7%，与高样本量对照有竞争力
- **适用条件 / 局限** · 仍需每组的少量域内参考样本

**可复用机制** · 感知系统切换环境时可比较轨迹统计和静态密度特征

<a id="paper-151891"></a>

## Geometry-Regularized Collapse Resistance via Consensus Enhancement for Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151891) · [作者来源](https://openreview.net/forum?id=XADFq5Hg3V)

- **问题 / 瓶颈** · 客户端数据异质使蒸馏共识携带局部偏差
- **核心创新 / 方法** · 约束主子空间的能量分布，避免少数分量集中，并按全局类别原型图对齐客户端关系
- **Baseline** · 八种对照，摘要未点名
- **Benchmark** · 两个任务的八个数据集，关注客户端共识与全局泛化，指标未报告
- **关键结果 / 消融** · 报告两方面改善并超过八种对照，幅度未报告
- **适用条件 / 局限** · 依赖预训练特征及可建立全局类别原型

**可复用机制** · 跨设备适应可分别诊断谱塌缩和关系漂移

<a id="paper-153923"></a>

## GeoMIND: A Benchmark for Spatial Understanding in Robotic Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153923) · [作者来源](https://openreview.net/forum?id=HdIY4lSNir)

- **问题 / 瓶颈** · 显著视觉提示和静态测试可绕开空间推理
- **核心创新 / 方法** · 用校验目标及可执行交互构造桌面任务，分别评测空间推理和空间记忆
- **Baseline** · 多类具身智能体，名称未报告
- **Benchmark** · GeoMIND 的 27 个设计和 54 个任务变体，具体指标未报告
- **关键结果 / 消融** · 摘要指出身份跟踪和把关系约束转为动作是共同失败点
- **适用条件 / 局限** · 已报告证据来自桌面操作

**可复用机制** · 设计干预前后成对场景，测量成功是否依赖持续跟踪目标身份

<a id="paper-151461"></a>

## GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/151461) · [作者来源](https://openreview.net/forum?id=aT3fx6NjSJ)

- **问题 / 瓶颈** · 逐层独立优化遗漏冗余，相邻层未必兼容
- **核心创新 / 方法** · 顺序优化跨层权重配对和共享字典分解，并结合结构稀疏保留各层校准几何
- **Baseline** · 独立结构化分解及启发式分组的配对分解
- **Benchmark** · 多个 Transformer 架构、规模和模态，具名数据和指标未报告
- **关键结果 / 消融** · 摘要报告优于独立或启发式分组方案
- **适用条件 / 局限** · 依赖校准激活，具体校准规模未报告

**可复用机制** · 为边缘模型选择共享基时，按校准数据估计跨层兼容度

<a id="paper-151984"></a>

## GeoPano: Towards Geometrically Accurate Panoramic 3D Reconstruction from a Single Panorama

[官方论文页](https://neurips.cc/virtual/2026/poster/151984) · [作者来源](https://openreview.net/forum?id=WMfFfSSyY6)

- **问题 / 瓶颈** · 全景切分为透视图之后跨视图结构不一致
- **核心创新 / 方法** · 用全局全景几何引导跨视图注意力，同时优化透视局部点云和全景均匀全局点云损失
- **Baseline** · 既有单图全景重建方法，名称未报告
- **Benchmark** · 单全景图三维重建，评估重建、几何一致性和视觉保真度
- **关键结果 / 消融** · 摘要报告各方面优于对照，幅度未报告
- **适用条件 / 局限** · 依赖完整全景和可统一坐标的投影

**可复用机制** · 把宽视野输入切块处理时，可用同一坐标系的整体损失检验拼接质量

<a id="paper-153630"></a>

## GEOPHYS: The Geometry of Physical Plausibility

[官方论文页](https://neurips.cc/virtual/2026/poster/153630) · [作者来源](https://openreview.net/forum?id=JxqjhovyBZ)

- **问题 / 瓶颈** · 视频物理评审可能依赖昂贵世界模型或专项训练
- **核心创新 / 方法** · 从逐帧特征提取曲率、速度变化、加速度与预测残差，用于异常识别或 best-of-N 候选排序
- **Baseline** · V-JEPA 2、GPT-4o、Gemini 等，生成奖励对照 V-JEPA 2
- **Benchmark** · LikePhys、IntPhys2 准确率及 MAGI-1 4.5B 的 PhysicsIQ
- **关键结果 / 消融** · 两个识别准确率分别 97.7% 和 93.3%，生成分数从 53.8% 到 64.7%
- **适用条件 / 局限** · 证据限定已评估物理违例及生成器

**可复用机制** · 世界模型候选排序可先测冻结表征动态是否能担任轻量奖励代理

<a id="paper-152380"></a>

## GeoPMR: Preserving Relational and Hierarchical Geometry in Multimodal Molecular Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152380) · [作者来源](https://openreview.net/forum?id=TWQ5xdccxN)

- **问题 / 瓶颈** · 逐点对比对齐可能扭曲各模态关系，欧氏空间也难表达分支层级
- **核心创新 / 方法** · 学习模态独有度量，用 Gromov–Wasserstein 对齐距离矩阵，并在双曲表征中约束父子与同层关系
- **Baseline** · InfoNCE、VICReg 属于文中比较的范式，具体实验对照未报告
- **Benchmark** · 七个性质预测基准，分类 AUC 和回归 MAE
- **关键结果 / 消融** · 摘要报告分类 AUC 改善 1.4%、回归 MAE 改善 1.7%
- **适用条件 / 局限** · 需要知道层级关系，跨领域验证未报告

**可复用机制** · 分层标注的异质感知信号可比较关系级与实例级对齐

<a id="paper-152938"></a>

## GeoRad-3D: Factorized Geometry Transport and Residual Radiometry for 3D Radar Nowcasting

[官方论文页](https://neurips.cc/virtual/2026/poster/152938) · [作者来源](https://openreview.net/forum?id=PGN6GYPOlq)

- **问题 / 瓶颈** · 统一确定性回归混合运动规律和局部强度波动
- **核心创新 / 方法** · 用共享运动场和局部补正推进几何，确定性预测基础强度，再用条件流匹配建模其残差，在渲染空间汇总分位数
- **Baseline** · 基于时空一致高斯地块方法，与最强已公开基线比较
- **Benchmark** · NEXRAD 协议，20/30/40 dBZ 的 Pool4 CSI 及 LPIPS-Radar
- **关键结果 / 消融** · 各门槛 CSI 约增 45%、82%、124%，LPIPS-Radar 降 31.0%
- **适用条件 / 局限** · 已报告证据限于该雷达协议

**可复用机制** · 对动态场景预测先对齐几何，再采样难以预测的局部观测残差

<a id="paper-152062"></a>

## GeoReason: Bridging Logical Reasoning and Spatial Fidelity in Remote Sensing Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/152062) · [作者来源](https://openreview.net/forum?id=Vmz7n0aAW8)

- **问题 / 瓶颈** · 在长推理末端生成分割 token 会失去细粒度视觉证据
- **核心创新 / 方法** · 开头注入分割 token，先框后掩码定位，并加图块到 token 的显式对齐损失
- **Baseline** · 已有推理分割方案，摘要未点名
- **Benchmark** · Earthreason 和 RRSIS-D 遥感分割评测，指标未报告
- **关键结果 / 消融** · 摘要报告优于既有方案，幅度未报告
- **适用条件 / 局限** · 验证来自遥感小目标，跨域结果未报告

**可复用机制** · 长指令的分割或抓取定位可测试提前植入空间锚点能否减少漂移

<a id="paper-155697"></a>

## GeoRouter: Dynamic Paradigm Routing for Worldwide Image Geolocalization

[官方论文页](https://neurips.cc/virtual/2026/poster/155697) · [作者来源](https://openreview.net/forum?id=3cSHwt2dIW)

- **问题 / 瓶颈** · 检索和生成擅长处理不同类型的查询
- **核心创新 / 方法** · 让视觉语言模型路由查询，用两条路线的地理误差差距构造成对偏好监督
- **Baseline** · 独立检索和生成路线及其他方法，具名对照未报告
- **Benchmark** · IM2GPS3K 和 YFCC4K 世界图像定位，具体指标未报告
- **关键结果 / 消融** · 摘要报告优于现有对照，幅度未报告
- **适用条件 / 局限** · 训练需要两路预测及真实标签，其他任务未报告

**可复用机制** · Agent 在检索和生成间选择工具时，可比较连续收益差值和二元胜负标签

<a id="paper-149350"></a>

## GeoSPRINT: Geometric Redundancy-Aware Step Pruning for Inference in Diffusion Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/149350) · [作者来源](https://openreview.net/forum?id=qj6phkQ9Bx)

- **问题 / 瓶颈** · 均匀去噪时刻在轨迹平直区域浪费计算
- **核心创新 / 方法** · 使用 QR 分解检测潜空间近共面轨迹，把更多更新分配给高曲率区间，从而构造非均匀日程
- **Baseline** · 均匀 DDIM、DPM-Solver++
- **Benchmark** · CIFAR-10、LSUN Church、Stable Diffusion v1.5，在匹配网络调用数下评估 FID
- **关键结果 / 消融** · CIFAR-10 改善 0.7 至 1.1 FID，LSUN Church 在 52 步从 1.48 降至 1.26
- **适用条件 / 局限** · 跨日程或域复用的效果未报告

**可复用机制** · 扩散动作策略可先测轨迹复杂度是否能解释逐段步数需求

<a id="paper-139481"></a>

## GeoSym127K: Scalable Symbolically-verifiable Synthesis for Multimodal Geometric Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139481) · [作者来源](https://openreview.net/forum?id=NO4INpEpCi)

- **问题 / 瓶颈** · 图形推理训练数据缺乏精确的可验证标签
- **核心创新 / 方法** · 按类型语法造题，解析求解器生成符号真值，同源渲染图形并构造监督，再比较从结构化 SFT 初始化的可验证奖励学习
- **Baseline** · 零样本强化学习和闭源模型，包括 Doubao-1.8
- **Benchmark** · GeoSym-Bench 511 个样本及 MathVerse Vision-Only、WeMath
- **关键结果 / 消融** · Qwen3-VL-8B 在前者提升 22.21 个百分点，WeMath 达 61.52%，报告提升 6.19 个百分点
- **适用条件 / 局限** · 依赖可形式化题型及精确可判定答案

**可复用机制** · 对可形式化视觉任务，可用同一场景程序生成输入、监督和强化学习校验

<a id="paper-152562"></a>

## GeoTransolver: Learning Physics on Irregular Domains using Multi-scale Geometry Aware Physics Attention Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/152562) · [作者来源](https://openreview.net/forum?id=SDYGxHUdHE)

- **问题 / 瓶颈** · 不规则域的状态表征难以持续利用几何与工况。
- **核心创新 / 方法** · 在学习的状态切片上做物理自注意力，并在每层交叉读取多尺度球查询生成的共享几何上下文。
- **Baseline** · Transolver、Domino、文献 AB-UPT。
- **Benchmark** · DrivAerML、SHIFT-SUV、SHIFT-Wing 的阻力/升力 R² 和场变量相对 L1；碰撞任务评估相对 L2 轨迹误差和运动学 MSE。
- **关键结果 / 消融** · 摘要报告精度、分布偏移鲁棒性与数据效率提升；具体幅度未报告。
- **适用条件 / 局限** · 证据限于所测不规则域工程问题。

**可复用机制** · 先建多尺度几何记忆，再让各层状态切片反复查询，避免几何信号只在输入层出现。

<a id="paper-149346"></a>

## GeoWind2Plan: Mission-Time 3D Urban Wind Prediction for Energy-Efficient UAV Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/149346) · [作者来源](https://openreview.net/forum?id=qmFNLvxGRp)

- **问题 / 瓶颈** · 逐工况模拟城市三维风场耗时，规划窗口短。
- **核心创新 / 方法** · 以背景风为坐标基准，只预测候选走廊相关的局部风场，用其优化路径与速度，再用高保真风场评价。
- **Baseline** · 风无关规划、高保真 CFD 参考规划。
- **Benchmark** · 留出的城市、风速和任务风角；以 CFD 下能耗和推理耗时评估。
- **关键结果 / 消融** · 约 3 秒推理；顺风、逆风、侧风较风无关规划节能 6.9%、12.7%、4.5%。
- **适用条件 / 局限** · 评测采用 CFD；实飞结果未报告。

**可复用机制** · 规划只依赖局部场时，按决策走廊分配预测计算，并用高保真环境中的最终代价衡量近似是否足够。

<a id="paper-148633"></a>

## GeoWorld: A Geometry-First World Model for Reconstruction and Imagination

[官方论文页](https://neurips.cc/virtual/2026/poster/148633) · [作者来源](https://openreview.net/forum?id=wI49OV3byB)

- **问题 / 瓶颈** · RGB 视频生成难保证可测量的几何，几何模型的长轨迹或稀疏外推又受限。
- **核心创新 / 方法** · 用相机射线和相对位姿调节分层注意力；把冻结的视频扩散模型隐状态映射为几何潜空间的条件。
- **Baseline** · 已有几何空间世界模型；具体名称未报告。
- **Benchmark** · 长相机轨迹与稀疏观测外推，比较几何一致性；数据集和指标未报告。
- **关键结果 / 消融** · 摘要报告可扩展至长轨迹，先验辅助外推改善几何一致性。
- **适用条件 / 局限** · 依赖相机几何与冻结相机条件视频模型。

**可复用机制** · 要同时保留可测几何和通用视觉先验，可把后者置于条件通道，由几何潜空间承担生成。

<a id="paper-154006"></a>

## GeoX: Mastering Geospatial Reasoning Through Self-Play and Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/154006) · [作者来源](https://openreview.net/forum?id=Gtiv2ckiib)

- **问题 / 瓶颈** · 空间推理问题组合多，逐条人工标注成本高。
- **核心创新 / 方法** · 同一视觉语言策略交替生成问题与可执行程序，并在溯因、演绎、归纳任务上用执行反馈联合强化学习。
- **Baseline** · 基础 VLM 与使用数百万精选样本训练的常规基线。
- **Benchmark** · 地理空间推理任务和自博弈生成评测集；摘要未报告指标细节。
- **关键结果 / 消融** · 基础模型平均最多提高 5.5 分，达到或超过常规基线。
- **适用条件 / 局限** · 需要可执行的场景谓词及分割工具；其他图像域未报告。

**可复用机制** · 给视觉关系题配可执行判据，让出题器和解题器共享可验证反馈，可减少组合题人工标注。

<a id="paper-139012"></a>

## Get a GRIP, this will be a long TRIP: A Quantifiable Long-Range Framework for Verifying Over-squashing

[官方论文页](https://neurips.cc/virtual/2026/poster/139012) · [作者来源](https://openreview.net/forum?id=qTEOyobP0r)

- **问题 / 瓶颈** · 图上标称长程任务可被局部模型解决，混淆信息传播距离与其他瓶颈。
- **核心创新 / 方法** · 用四项公理定义长程任务，借稳定分布在任意图上生成可证明的 k 跳任务，并构造分距离极大似然误差下界。
- **Baseline** · 四个常用长程基准与可解释的分距离最优估计器。
- **Benchmark** · 四个评测审计和 TRIP 图拓扑实验；比较公理合规性和曲率与 GNN 表现的关联。
- **关键结果 / 消融** · 发现既有基准的失败模式；一类曲率指标在 TRIP 中与模型表现无关。
- **适用条件 / 局限** · 结论受合成任务和所测曲率定义约束。

**可复用机制** · 遇到长上下文能力声明，先构造可证明必须访问指定距离的信息的对照，再检测模型能力。

<a id="paper-151444"></a>

## GGQR: Gaussian-Grounded Query Refinement for Feed-Forward 4D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/151444) · [作者来源](https://openreview.net/forum?id=aeBYEqSDxP)

- **问题 / 瓶颈** · 逐帧高斯冗余，单步由 2D 到 4D 回归歧义大。
- **核心创新 / 方法** · 带平台形时间核的高斯查询跨帧持续，在共享三维空间中按当前高斯状态读观测并残差更新。
- **Baseline** · 现有前馈 4D Gaussian Splatting 方法；名称未报告。
- **Benchmark** · 单目动态重建的新视角与新时刻渲染和运动建模；数据集与指标未报告。
- **关键结果 / 消融** · 摘要报告在前馈方法中达到新最优并改善下游运动建模。
- **适用条件 / 局限** · 依赖基础模型把二维观测提升到共享三维空间。

**可复用机制** · 动态场景中，给原语显式存续窗口并按中间几何状态迭代取证，可缓解逐帧冗余与单次回归歧义。

<a id="paper-148812"></a>

## gHAWK: Structural Encoding for Scalable Training of Graph Neural Networks on Knowledge Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/148812) · [作者来源](https://openreview.net/forum?id=uw0STVeH8D)

- **问题 / 瓶颈** · 小批量图消息传递可见邻域不完整，学习结构低效。
- **核心创新 / 方法** · 用 Bloom filter 压缩局部邻域，以 TransE 嵌入表示全局位置，和文本等节点特征一起送入 GNN。
- **Baseline** · 简单 GNN 与复杂关系感知 GNN。
- **Benchmark** · Open Graph Benchmark 大图上的节点属性预测和链接预测；具体指标未报告。
- **关键结果 / 消融** · 摘要报告提升准确率、内存表现和收敛，简单 GNN 可超过复杂关系感知模型。
- **适用条件 / 局限** · 依赖可预处理图结构；动态图下的更新代价未报告。

**可复用机制** · 采样割裂全图结构时，可把廉价的全局位置和局部邻域摘要预存为节点特征。

<a id="paper-152747"></a>

## Ghosted Layers: Unconstrained Activation Alignment for Recovering Layer-Pruned LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152747) · [作者来源](https://openreview.net/forum?id=QdursVtog1)

- **问题 / 瓶颈** · 删除解码块改变下一层输入分布。
- **核心创新 / 方法** · 从小校准集闭式求解无约束线性边界对齐算子，以重建裁层引入的激活差异。
- **Baseline** · 已有免训练恢复方法，通常限制对齐算子子空间。
- **Benchmark** · 多个 LLM 骨干及裁层策略，比较准确率和困惑度；模型与任务名未报告。
- **关键结果 / 消融** · 摘要报告优于先前免训练基线并保持裁层效率。
- **适用条件 / 局限** · 依赖校准样本；在分布偏移或极高裁剪率下的表现未报告。

**可复用机制** · 移除模块后可显式最小化剩余模块的输入偏差，先比较闭式线性修复和重新训练的成本。

<a id="paper-149354"></a>

## GHOST: Geometry-Hierarchical Online Streaming Token Eviction for Efficient 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/149354) · [作者来源](https://openreview.net/forum?id=qhHNkQs6l0)

- **问题 / 瓶颈** · 单目流重建的 KV 随时间增长，固定锚帧与注意力启发式难保留有效几何。
- **核心创新 / 方法** · 以模型自身三维输出分两级评分，保护特殊 token，依据余弦相似性分配各层缓存。
- **Baseline** · 固定锚帧与注意力启发式；具体对比名称未报告。
- **Benchmark** · 多项三维重建基准，比较质量、缓存占用及推理速度；名称未报告。
- **关键结果 / 消融** · 摘要报告缓存约减半，推理加速 1.75 倍并保持重建质量。
- **适用条件 / 局限** · 几何重要性依赖在线预测质量，误差传播影响未报告。

**可复用机制** · 对流式感知按下游表征效用保留缓存，而非只保留固定帧或注意力最高 token。

<a id="paper-153445"></a>

## Gibbs Gradient Descent: A Langevin Approach to Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153445) · [作者来源](https://openreview.net/forum?id=LFrMGs6Z6P)

- **问题 / 瓶颈** · 分布优化的嵌套采样昂贵，单循环 Gibbs 梯度下降仍有有限粒子噪声。
- **核心创新 / 方法** · 分析有限与无限粒子 Gibbs 梯度下降，并为有限可观测量结构提出控制变量。
- **Baseline** · Marion 等的 Gibbs 梯度下降和理想无限粒子系统。
- **Benchmark** · 理想与有限粒子系统的理论比较；实证任务未报告。
- **关键结果 / 消融** · 给出持续 O(1/n) 方差项，控制变量降低可观测量层面的粒子误差。
- **适用条件 / 局限** · 控制变量结果依赖有限可观测量结构。

**可复用机制** · 单循环联合采样与优化时，把预算用于关键可观测量的降方差，减少盲目增加粒子数的需求。

<a id="paper-154879"></a>

## GIFT: Representation Geometry Matters for Single-Domain Generalized Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/154879) · [作者来源](https://openreview.net/forum?id=AD11zTIipA)

- **问题 / 瓶颈** · 无约束微调可能破坏与域不变语义有关的表征结构。
- **核心创新 / 方法** · 在预训练权重上施加可学习 Householder 反射，并用轻量逐通道缩放补充任务适配。
- **Baseline** · 既有 S-DGOD 最优方法；名称未报告。
- **Benchmark** · Cityscapes-C 和 Diverse Weather Dataset 的单域泛化检测，指标 mPC。
- **关键结果 / 消融** · 增加低于 1% 主干可训练参数；两数据集 mPC 分别提高 7.9% 和 2.9%。
- **适用条件 / 局限** · 证据来自单域目标检测；其他任务未报告。

**可复用机制** · 小参数迁移可把保持表示几何的更新和通道幅度适配拆开，检验前者是否提高分布外鲁棒性。

<a id="paper-139591"></a>

## GISA: A Benchmark for General Information-Seeking Assistant

[官方论文页](https://neurips.cc/virtual/2026/poster/139591) · [作者来源](https://openreview.net/forum?id=GcIxVsG6Yv)

- **问题 / 瓶颈** · 从已知答案倒推问题会偏离用户需求，静态答案容易被记忆。
- **核心创新 / 方法** · 收集人写查询及完整人类搜索路径，采用四种结构化答案并定期更新子集答案。
- **Baseline** · 主流 LLM 与商用搜索产品；名称未报告。
- **Benchmark** · 373 道信息检索问题；用 exact match 测试单项、集合、列表、表格答案。
- **关键结果 / 消融** · 最优也仅 19.30% 精确匹配；复杂规划和全面收集任务尤其困难。
- **适用条件 / 局限** · 精确匹配依赖结构化输出和答案规范；未报告实时子集规模。

**可复用机制** · 从真实需求出发构造搜索任务，配套时效标注和完整人类轨迹，区分规划失败、搜索覆盖不足与记忆捷径。

<a id="paper-152787"></a>

## GIST: Gauge-Invariant Spectral Transformers for Scalable Graph Neural Operators

[官方论文页](https://neurips.cc/virtual/2026/poster/152787) · [作者来源](https://openreview.net/forum?id=QL5IahmmDj)

- **问题 / 瓶颈** · 谱位置编码有求解开销且可能破坏规范不变性，换网格会失效。
- **核心创新 / 方法** · 注意力只使用高效近似谱嵌入的两两内积，估计规范不变核并给出离散失配误差界。
- **Baseline** · 谱编码与高效近似方法；具体模型名未报告。
- **Benchmark** · AirfRANS、ShapeNet-Car、DrivAerNet、DrivAerNet++ 和 PPI；最大 75 万节点，PPI 指标 micro-F1。
- **关键结果 / 消融** · 摘要报告端到端 O(N) 与网格任务达到最优；PPI micro-F1 为 99.50%。
- **适用条件 / 局限** · 误差界假设和复杂度适用设置需查正文。

**可复用机制** · 同一对象有多种网格或谱基表示时，限制模型使用不变的关系量以改善跨离散化迁移。

<a id="paper-152398"></a>

## Git Context Controller: Manage the Context of Agents by Agentic Git

[官方论文页](https://neurips.cc/virtual/2026/poster/152398) · [作者来源](https://openreview.net/forum?id=TOI57aH7Gz)

- **问题 / 瓶颈** · 交互历史无界增长，跨会话复用和多轨迹协作困难。
- **核心创新 / 方法** · 使用版本化文件状态记录里程碑，支持独立分支、合并与分层历史检索。
- **Baseline** · 强长上下文基线及 26 个开源或商用系统。
- **Benchmark** · SWE-Bench Verified 的任务解决率及 BrowseComp；后者具体指标未报告。
- **关键结果 / 消融** · SWE-Bench Verified 成功率超 80%，较强长上下文基线相对提高逾 13%。
- **适用条件 / 局限** · 分支合并冲突与版本存储开销数据未报告。

**可复用机制** · 长任务设结构化版本检查点，让并行假设拥有独立可回溯状态，再以明确操作合并。

<a id="paper-138882"></a>

## GitInject: Real-World Prompt Injection Attacks in AI-Powered CI/CD Pipelines

[官方论文页](https://neurips.cc/virtual/2026/poster/138882) · [作者来源](https://openreview.net/forum?id=yuUk1yfRpn)

- **问题 / 瓶颈** · 自动化代码助手同时读外部贡献并拥有内部权限，存在信任边界失守风险。
- **核心创新 / 方法** · 以隔离环境检验多款工作流在权限及沙盒边界下的防护表现。
- **Baseline** · 四家提供方的五个工作流及工作流级防护配置。
- **Benchmark** · 工作流安全性、对策覆盖范围及可用性代价；具体量化指标未报告。
- **关键结果 / 消融** · 测试配置下各提供方均存在高严重度风险。
- **适用条件 / 局限** · 结论受工作流配置和权限模型影响。

**可复用机制** · 审计 Agent 时以输入来源和授权作为授信依据，并测试低权输入无法改变高权限策略。

<a id="paper-152891"></a>

## GIVLA: Deep Geometry Internalization for A Lightweight VLA via Geometry Instruction and Gradient-Informed Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152891) · [作者来源](https://openreview.net/forum?id=PdCwcQz2FA)

- **问题 / 瓶颈** · 通用 VLA 缺显式空间意识，感知和动作任务之间存在梯度干扰。
- **核心创新 / 方法** · 在 VLA 主干内深度耦合几何先验，并用梯度信息安排两阶段训练。
- **Baseline** · 已有 VLA；具体模型名未报告。
- **Benchmark** · LIBERO 和实体机器人平台，比较准确性、鲁棒性和参数效率；具体指标未报告。
- **关键结果 / 消融** · 摘要报告精度和鲁棒性更优且参数效率高。
- **适用条件 / 局限** · 依赖几何先验，训练阶段及实体条件细节未报告。

**可复用机制** · 给策略加入空间辅助目标时，先测它与动作梯度的干扰，再据此规划联合训练时机。

<a id="paper-152133"></a>

## GLACIER: Rethinking Mass Spectrum Prediction as an Object Detection Problem

[官方论文页](https://neurips.cc/virtual/2026/poster/152133) · [作者来源](https://openreview.net/forum?id=VGzoNiwKMJ)

- **问题 / 瓶颈** · 质谱预测先枚举分子片段再评分，推理慢且候选彼此独立。
- **核心创新 / 方法** · 借用目标检测思路，用单阶段图 Transformer 直接预测片段子图及谱贡献。
- **Baseline** · 候选枚举后评分的双阶段模型及既有最佳方法。
- **Benchmark** · MassSpecGym 和 NIST’20 的 MS/MS Top-1 检索准确率与推理速度。
- **关键结果 / 消融** · 有/无对比微调时两数据集分别为 62.4%/62.1% 与 55.2%/38.2%；双阶段模型相比约有三倍加速。
- **适用条件 / 局限** · 直预测对长尾片段及分布外结构的表现未报告。

**可复用机制** · 在开销主要来自组合候选枚举时，可试固定预算的集合预测来生成结构与其效应。

<a id="paper-149584"></a>

## Glance Before You Tell: Anomaly-Guided 3D Radiology Report Generation with Heat-Conduction Slice Encoders

[官方论文页](https://neurips.cc/virtual/2026/poster/149584) · [作者来源](https://openreview.net/forum?id=p124P8VSQH)

- **问题 / 瓶颈** · 体数据冗余可能诱发报告幻觉；外部分割器的错误会传入生成端。
- **核心创新 / 方法** · 有符号热传导编码分离平滑结构和异常样残差，将可疑切片按粗器官上下文整理成视觉前缀。
- **Baseline** · 外部分割或医学短语队列式证据路由方法；具体基线未报告。
- **Benchmark** · 三项 3D 放射学报告任务，临床保真度及幻觉指标；基准名与数值未报告。
- **关键结果 / 消融** · 摘要报告临床保真与幻觉评测一致改善。
- **适用条件 / 局限** · 依赖粗器官上下文，非医疗体数据的迁移未验证。

**可复用机制** · 长视觉观测中，可先用异常残差信号做证据路由，并保持部位结构后再生成。

<a id="paper-150150"></a>

## GLARE: Generating Listening Heads with Appropriate REactions

[官方论文页](https://neurips.cc/virtual/2026/poster/150150) · [作者来源](https://openreview.net/forum?id=kJcRgMLqWX)

- **问题 / 瓶颈** · 画面逼真度很难衡量交流中的反应是否恰当及及时。
- **核心创新 / 方法** · 对流匹配 Transformer 增加语调条件和逐帧反应损失，分别评估反应发生、时间区间、非对称偏差和局部画质。
- **Baseline** · 已有聆听头生成方法与仅衡量画质的生成指标。
- **Benchmark** · RealTalk 和 Seamless Interaction 派生的 147 小时、64,557 个六类事件；R-F1、R-tIoU、R-ATD、R-FID。
- **关键结果 / 消融** · 摘要报告视觉保真度及反应指标均改善。
- **适用条件 / 局限** · 依赖事件标注，行为词表限于六类头部或面部反应。

**可复用机制** · 为响应型数字人或交互策略分开测是否响应、响应时序和表现质量，避免画质掩盖行为错误。

<a id="paper-154081"></a>

## GLINT: Sparsely Gated Vision-Language Alignment for Fine-Grained Radiology Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/154081) · [作者来源](https://openreview.net/forum?id=GLHgQkefOp)

- **问题 / 瓶颈** · 报告级文本配对无法指出具体发现所在区域，密集权重会稀释局部对应。
- **核心创新 / 方法** · 在独立嵌入空间用 sigmoid 门控筛选文本相关图块，并将可训练编码器中间特征约束到冻结自监督教师。
- **Baseline** · 比较自监督编码器与医学视觉语言模型；具名对照未报告。
- **Benchmark** · 二维胸片与三维胸部 CT 的零样本分类、定位和分割，另评估下游分类及报告生成；指标未报告。
- **关键结果 / 消融** · 作者报告定位与分割收益最显著，并展示无掩码监督的三维 CT 零样本分割。
- **适用条件 / 局限** · 摘要仅提供放射影像场景的验证。

**可复用机制** · 在区域只占画面小部分的弱监督任务中，分开比较稀疏门控和冻结教师约束对定位的贡献。

<a id="paper-151745"></a>

## Glob3R: Global Structure-from-Motion with 3D Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151745) · [作者来源](https://openreview.net/forum?id=YQG92O0dwh)

- **问题 / 瓶颈** · 前馈几何模型分块处理长序列时容易积累漂移和尺度不一致。
- **核心创新 / 方法** · 在冻结 Pi3X 上加稠密匹配头，将局部形变转成多视角轨迹；关键帧滑窗传播约束，最后做运动平均和束调整。
- **Baseline** · 以 Pi3X 为骨干，比较前馈几何模型、可扩展重建方法与经典 SfM。
- **Benchmark** · 室内、室外、驾驶及无序 SfM，并评估下游神经渲染；具名数据集与指标未报告。
- **关键结果 / 消融** · 作者报告重建兼具精度和鲁棒性，优化位姿改善渲染。
- **适用条件 / 局限** · 仍依赖跨视图匹配以及重叠窗口内的轨迹关联。

**可复用机制** · 用学习到的局部对应初始化可累积的全局几何约束，分别量化漂移与匹配质量。

<a id="paper-153438"></a>

## Global Context Guidance for Diffusion Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153438) · [作者来源](https://openreview.net/forum?id=LIdk3v52Wt)

- **问题 / 瓶颈** · 去噪过度依赖近邻上下文，弱模型引导每步另需一次前向。
- **核心创新 / 方法** · GCG 在特征空间增强全局上下文利用，省去独立弱模型。
- **Baseline** · 比较现有弱模型引导方法；具体方法名未报告。
- **Benchmark** · 在 LLaDA-8B、Dream-7B、LLaDA-1.5 上测试多个任务及推断开销；具名任务和指标未报告。
- **关键结果 / 消融** · 作者报告跨模型优于既有引导且开销更低；量化幅度未报告。
- **适用条件 / 局限** · 摘要未交代特征构造细节和逐任务结果。

**可复用机制** · 先测去噪步骤对局部与全局上下文的依赖，再决定是否以特征修改替代每步双模型推断。

<a id="paper-153209"></a>

## Global Importance Estimation for KV Cache Eviction

[官方论文页](https://neurips.cc/virtual/2026/poster/153209) · [作者来源](https://openreview.net/forum?id=N1gDvQ8d8n)

- **问题 / 瓶颈** · 低容量 KV 缓存可能删除当前关注度低、后续间接引用重要的 token。
- **核心创新 / 方法** · PRKV 将注意力转换为转移图，通过个性化 PageRank 传播 token 重要性，无需再训练。
- **Baseline** · 比较已有 KV 淘汰方法；具名基线未报告。
- **Benchmark** · 多个语言模型家族的长上下文理解、稀疏检索和思维链，比较任务表现、峰值内存及端到端开销。
- **关键结果 / 消融** · 作者报告最高 90% 压缩时仍具竞争力并降低峰值内存；具体数值未报告。
- **适用条件 / 局限** · 摘要未交代图传播成本随上下文长度扩展的曲线。

**可复用机制** · 在缓存极紧的任务中，专门检查多跳评分能否保护支撑后续推理的早期信息。

<a id="paper-152447"></a>

## Global Optimality for Constrained Exploration via Penalty Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/152447) · [作者来源](https://openreview.net/forum?id=T2vHX7E0dN)

- **问题 / 瓶颈** · 约束占用熵不可加，策略参数化后优化非凸，已有弱遗憾保证不直接给出最终策略。
- **核心创新 / 方法** · PGP 对凸占用约束施加二次惩罚，将惩罚目标的梯度写成伪奖励，形成单循环更新。
- **Baseline** · 理论比较 Ying 等（2025）的无模型策略梯度；实验具名方法未报告。
- **Benchmark** · 网格世界消融及两个连续控制任务，考察约束探索；实验指标与任务名未报告。
- **关键结果 / 消融** · 理论保证末次策略的熵次优性和约束违反均可界于 ε；作者报告连续控制验证。
- **适用条件 / 局限** · 理论依赖占用约束凸性；摘要未给出有限样本下的实证约束代价。

**可复用机制** · 遇到不可加的状态—动作分布目标，先检查其梯度能否表示为可供现有学习器使用的伪奖励。

<a id="paper-139393"></a>

## Global PIQA: Evaluating Commonsense Reasoning Across 100+ Languages and Cultures

[官方论文页](https://neurips.cc/virtual/2026/poster/139393) · [作者来源](https://openreview.net/forum?id=TGSeFxFoPi)

- **问题 / 瓶颈** · 翻译集易忽略本土知识，而各地原创集难比较语言差距。
- **核心创新 / 方法** · Global PIQA 同时收集当地常识题和文化中性题的平行翻译，由母语者验证。
- **Baseline** · 比较先进语言模型；具名对照未报告。
- **Benchmark** · 141 种语言变体的常识推理；平行分组覆盖 131 种语言变体，以准确率比较跨语言差距。
- **关键结果 / 消融** · 非平行分组过半含本地文化元素，平行组语言间准确率差距最高报告为 68%。
- **适用条件 / 局限** · 平行题只代表筛选后的文化中性常识，摘要未报告与本土组的逐语言对应。

**可复用机制** · 给多语言智能体评测设计两条互补证据链，用平行题识别语言差距，用本土题识别知识缺口。

<a id="paper-154884"></a>

## GLOVE: Global Verifier for LLM Memory-Environment Realignment

[官方论文页](https://neurips.cc/virtual/2026/poster/154884) · [作者来源](https://openreview.net/forum?id=AAW7ljVgUz)

- **问题 / 瓶颈** · 动态环境会使旧记忆失效，任务奖励和模型自省提供的验证信号都有局限。
- **核心创新 / 方法** · GLOVE 主动探测环境并比较新观测与检索记忆，以相对一致性触发验证和更新。
- **Baseline** · 比较多种语言模型记忆设计及显隐环境漂移；具名对照未报告。
- **Benchmark** · 网页导航、离散规划、连续及具身控制，含仿真与实体机器人，以任务成功率评估适应。
- **关键结果 / 消融** · 作者报告多个任务和记忆设计下适应改善，部分情形从接近失败恢复到较高成功率；具体幅度未报告。
- **适用条件 / 局限** · 依赖可获得且有判别力的新观测；探测成本未报告。

**可复用机制** · 把主动核验加入记忆读取路径，并单独衡量探测成本和成员条目的更新准确性。

<a id="paper-152961"></a>

## Gluing Local Contexts into Global Meaning: A Sheaf-Theoretic Decomposition of Transformer Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/152961) · [作者来源](https://openreview.net/forum?id=P5J2YE6sLF)

- **问题 / 瓶颈** · 改写对的单层协方差无法区分语义等价关系在跨层变换中何时失配。
- **核心创新 / 方法** · 从改写图构造层论上边界与拉普拉斯算子，叠加层间边，用环上的谐波量检查跨层变换与改写关系是否交换。
- **Baseline** · 比较方差匹配、探针、LEACE 和随机干预方向。
- **Benchmark** · 九种模型架构的因果干预、八种架构的留出 CounterFact、Llama-2-7B 风格迁移事实保留及编码器秩。
- **关键结果 / 消融** · 作者报告谱补空间因果影响为方差匹配对照的 5.6–26.5 倍，CounterFact 平均改善 17.9 个百分点。
- **适用条件 / 局限** · 依赖语义等价改写与跨层对齐；风格迁移事实保留只报告一个模型。

**可复用机制** · 用同义输入的跨层一致性测量选择干预子空间，并以等方差方向控制幅度效应。

<a id="paper-151218"></a>

## GlyphAnchor: Enhancing Visual Text Rendering via Position-Anchored Glyph Priors

[官方论文页](https://neurips.cc/virtual/2026/poster/151218) · [作者来源](https://openreview.net/forum?id=c3aMyawBN4)

- **问题 / 瓶颈** · 长文本、密排文字和罕见字的准确渲染仍不稳定。
- **核心创新 / 方法** · 以位置锚定的字形图块作为生成与编辑 DiT 的轻量条件，分阶段监督微调并做文本感知后训练。
- **Baseline** · 对照包括无显式字形先验的原生渲染与专门的字形条件方案；具名基线未报告。
- **Benchmark** · InfoTextBench 及其他未具名基准的生成与编辑，覆盖长文本、复杂密排和罕见字，检查文字保真与图像质量。
- **关键结果 / 消融** · 作者报告多个骨干和基准中文字保真提高、总体图像质量维持；数值未报告。
- **适用条件 / 局限** · 依赖可用的字形和对应空间位置。

**可复用机制** · 需要可读性与布局同时受控时，把预期视觉符号绑定到目标坐标，而非仅输入文字串。

<a id="paper-152097"></a>

## GMO-E²DIT: Grounded Multi-Operation Editing for E-Commerce Images

[官方论文页](https://neurips.cc/virtual/2026/poster/152097) · [作者来源](https://openreview.net/forum?id=VXvQ42upd6)

- **问题 / 瓶颈** · 一步式编辑混合意图解析、定位和生成，容易遗漏多项操作或破坏其他区域。
- **核心创新 / 方法** · 视觉语言模型先生成有区域定位的编辑清单，再通过操作相关掩码与引用逐项执行并检查中间结果。
- **Baseline** · 比较一步式编辑和强闭源模型；具名基线未报告。
- **Benchmark** · EComEditBench 指令驱动编辑，评估指令准确性与编辑保真；具体指标未报告。
- **关键结果 / 消融** · 作者报告优于已有基线，并与强闭源模型表现接近。
- **适用条件 / 局限** · 依赖能定位和复核的区域操作，摘要未报告循环带来的延迟。

**可复用机制** · 对一组可部分成功的生成操作，保存已完成状态，只重试未通过核验的子操作。

<a id="paper-152436"></a>

## GNES: Neural-Guided Evolutionary Program Search for Interpretable Multi-Agent Control

[官方论文页](https://neurips.cc/virtual/2026/poster/152436) · [作者来源](https://neurips.cc/virtual/2026/poster/152436)

- **问题 / 瓶颈** · 离散控制程序仅能从稀疏且昂贵的长时模拟获得反馈。
- **核心创新 / 方法** · 将控制器树作为状态、合法遗传编辑作为动作，用图策略及价值模型为树搜索提供引导，最终交由模拟器验证。
- **Baseline** · 比较进化和多智能体强化学习基线，具体名称未报告。
- **Benchmark** · 三套 AirSim 去中心化集群控制任务，考察搜索效率和控制器质量。
- **关键结果 / 消融** · 作者报告搜索效率和最终质量改善，图策略价值模型及树搜索均有贡献。
- **适用条件 / 局限** · 依赖预定义程序语法与模拟器，真实机器人验证未报告。

**可复用机制** · 把可解释控制器的搜索预算分给可验证的局部程序编辑，单独对照直接遗传搜索。

<a id="paper-151409"></a>

## GNNs Meet Sequence Models Along the Shortest-Path: an Expressive Method for Link Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/151409) · [作者来源](https://neurips.cc/virtual/2026/poster/151409)

- **问题 / 瓶颈** · 节点消息传递可能遗漏特定候选边的多跳结构。
- **核心创新 / 方法** · 用 GNN 生成节点向量，再以序列模型处理候选两端最短路径上的向量序列。
- **Baseline** · 比较标准消息传递 GNN 与若干结构特征方法，具名实验基线未报告。
- **Benchmark** · 通用链接预测基准，摘要未报告具体数据集和指标。
- **关键结果 / 消融** · 理论上比所比较的结构方法更有表达力，作者报告多个基准取得领先结果。
- **适用条件 / 局限** · 摘要未报告多条并列最短路径及不连通节点对的处理。

**可复用机制** · 为知识图谱关系预测加一条连接路径的序列输入，并用纯端点评分做等容量对照。

<a id="paper-153765"></a>

## Goal-Conditioned Supervised Learning for Multi-Objective Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/153765) · [作者来源](https://neurips.cc/virtual/2026/poster/153765)

- **问题 / 瓶颈** · 固定损失权重难兼顾冲突目标，离线轨迹也包含大量低收益动作。
- **核心创新 / 方法** · 扩展 GCSL，将未来回报表示为多维目标向量，推理时选择可达到且满足偏好的目标。
- **Baseline** · 基于标准 GCSL，具名比较基线未报告。
- **Benchmark** · 商业级推荐中的离线下一动作预测，数据与指标未报告。
- **关键结果 / 消融** · 作者报告可扩展且能减弱噪声数据的影响，幅度未报告。
- **适用条件 / 局限** · 证据来自推荐场景，依赖离线轨迹覆盖可行目标。

**可复用机制** · 当历史日志覆盖若干可行权衡时，用回报向量训练一个条件策略，再单测目标选择器。

<a id="paper-154845"></a>

## GOAT-AL: Pseudo Neural Collapse Guides Adaptive Coverage for All-Budget Active Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154845) · [作者来源](https://neurips.cc/virtual/2026/poster/154845)

- **问题 / 瓶颈** · 小预算偏重覆盖，大预算偏重不确定性，固定过渡时点不适应表示学习进度。
- **核心创新 / 方法** · 用伪类内离散度 pCDNV 的峰值检测表示成熟度，保持覆盖目标并将底层特征从自监督表示改为任务对齐表示。
- **Baseline** · 与主动学习代表方法比较，具名基线未报告。
- **Benchmark** · CIFAR-10、CIFAR-100 与 TinyImageNet，覆盖低、中、高标注预算。
- **关键结果 / 消融** · 作者报告各预算下与领先方法相当或更优，数值未报告。
- **适用条件 / 局限** · 峰值在多标签、开放集和分布变化下的稳定性未报告。

**可复用机制** · 用无标签几何统计量控制何时把候选采样空间从通用特征转到任务特征。

<a id="paper-148735"></a>

## Going Down Memory Lane: Scaling Tokens for Video Stream Understanding with Dynamic KV-Cache Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/148735) · [作者来源](https://neurips.cc/virtual/2026/poster/148735)

- **问题 / 瓶颈** · 每帧缓存过小丢失细节，直接扩大每帧 token 数又可能降低相似度检索质量。
- **核心创新 / 方法** · 适应性选择保留局部时空信息，并以外部模型组成免训练检索集成。
- **Baseline** · 与 ReKV 比较，使用 Qwen2.5-VL-7B。
- **Benchmark** · CG-Bench、LVBench、VideoMME 长视频子集，衡量问答表现。
- **关键结果 / 消融** · 对 ReKV 的摘要报告提升分别为 8.0%、8.5% 和 2.4%。
- **适用条件 / 局限** · 依赖缓存表示及外部检索模型，额外时延未报告。

**可复用机制** · 为流式智能体做同预算消融，分别测试帧内去冗余和检索重排对证据召回的影响。

<a id="paper-152922"></a>

## Golden Layers and Where to Find Them: Improved Knowledge Editing for Large Language Models Via Layer Gradient Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/152922) · [作者来源](https://neurips.cc/virtual/2026/poster/152922)

- **问题 / 瓶颈** · 在全层上逐次执行知识编辑以确定位置，成本高且不同请求的最优层可能不同。
- **核心创新 / 方法** · 用梯度归因估计接近逐样本最优的固定编辑层，并检验代理数据选层的迁移。
- **Baseline** · 对照逐样本最优编辑层及多种知识编辑方法，具名方法未报告。
- **Benchmark** · 多种 LLM 和多个知识编辑数据集，具名基准和指标未报告。
- **关键结果 / 消融** · 作者报告固定层接近逐样本最优，且代理集选择可跨数据集迁移。
- **适用条件 / 局限** · 对其他模型行为的副作用及连续编辑中的稳定性需单独验证。

**可复用机制** · 模型编辑前离线做梯度层归因，并保留少量穷举编辑作层选择质量对照。

<a id="paper-155209"></a>

## GOLD PANNING: Strategic Context Shuffling for Needle-in-Haystack Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155209) · [作者来源](https://neurips.cc/virtual/2026/poster/155209)

- **问题 / 瓶颈** · 黑盒 LLM 长上下文检索受证据位置影响，无法直接修改注意力。
- **核心创新 / 方法** · 贝叶斯循环依据模型答复更新相关性信念，并优先将高信念文档放到响应更具诊断性的位置。
- **Baseline** · 对比 Permutation Self-Consistency。
- **Benchmark** · 开放权重及闭源模型的多文档问答，指标为 F1 与查询数。
- **关键结果 / 消融** · 摘要报告以少 30%–65% 的查询达到相近 F1，理论结果在其假设下为对数级轮次。
- **适用条件 / 局限** · 依赖可测的位置特征及可控顺序，复杂多证据任务的覆盖未报告。

**可复用机制** · 缓存模型的位置诊断曲线，在固定调用预算下与随机重排比较证据定位。

<a id="paper-149416"></a>

## Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/149416) · [作者来源](https://neurips.cc/virtual/2026/poster/149416)

- **问题 / 瓶颈** · 多视图重建的全局注意力随输入长度二次增长。
- **核心创新 / 方法** · 先按视图多样性挑候选帧，再按注意力熵选择层相关的帧内 KV 稀疏度。
- **Baseline** · 比较原始视觉几何 Transformer 和其他稀疏方案，具名基线未报告。
- **Benchmark** · 多视图三维重建，含 500 张图像场景，比较运行速度和重建表现。
- **关键结果 / 消融** · 摘要报告 500 图像场景加速超过 85%，表现持平或改善。
- **适用条件 / 局限** · 对低重叠视图及动态场景的影响未报告。

**可复用机制** · 把场景覆盖需求与同一帧的细节需求拆开做 token 预算消融。

<a id="paper-150838"></a>

## GoT: A Game-Theoretic Approach to the Game of Twenty Questions

[官方论文页](https://neurips.cc/virtual/2026/poster/150838) · [作者来源](https://neurips.cc/virtual/2026/poster/150838)

- **问题 / 瓶颈** · 自然语言二十问的启发式策略可能在不利隐藏目标上失效。
- **核心创新 / 方法** · 将对抗性问答建模为扩展式零和博弈，对受限变体近似求纳什均衡策略。
- **Baseline** · 直接提示与启发式引导搜索。
- **Benchmark** · 多设定的 Strategic Language Search，比较最坏情况表现。
- **关键结果 / 消融** · 摘要报告所有测试设定的最坏情况均改善，提升幅度未报告。
- **适用条件 / 局限** · 求解面向受限变体，真实交互中答复噪声和候选规模的影响未报告。

**可复用机制** · 对连续提问智能体同时记录先验平均表现和最差对象表现，再决定是否引入博弈搜索。

<a id="paper-152654"></a>

## GPA: General Principled Framework for Linearizing Softmax Attention via KV Cache Approximation

[官方论文页](https://neurips.cc/virtual/2026/poster/152654) · [作者来源](https://neurips.cc/virtual/2026/poster/152654)

- **问题 / 瓶颈** · 线性注意力缺少与 Softmax 之间的函数误差定位和系统改进路径。
- **核心创新 / 方法** · 分解冗余消除、位置拆分的 token 量化、位置压缩、跨层相似和多状态分解，给出误差界并构造可继承预训练权重的 GPA。
- **Baseline** · 比较 MVA 和 GSA 等线性注意力方法。
- **Benchmark** · 多项基准并比较微调资源，具名数据集及指标未报告。
- **关键结果 / 消融** · 摘要报告 GPA 优于上述基线并需要更少微调资源，未报告幅度。
- **适用条件 / 局限** · 跨上下文长度和不同缓存预算的误差细节未报告。

**可复用机制** · 替换预训练注意力前，为内容压缩、位置压缩和跨层共享各自记录精度与内存变化。

<a id="paper-139632"></a>

## GPT-Image-Edit-1M: An Auditable Million-Scale Dataset for Instruction-Guided Image Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/139632) · [作者来源](https://neurips.cc/virtual/2026/poster/139632)

- **问题 / 瓶颈** · 图像编辑数据中有弱编辑、指令错配和不可追踪的过滤。
- **核心创新 / 方法** · 以带理由的保留、重标注或删除决策审核样本，重标注匹配实测修改，再用独立评审复跑协议。
- **Baseline** · 与 FLUX.1-Kontext-dev 及等规模随机再生成子集比较。
- **Benchmark** · 评估 GEdit-EN、ImgEdit、KRISBench 等及共享样本质量量表。
- **关键结果 / 消融** · 质量评分 6.90→7.67。等规模对照显示再生成贡献最大，审核带来较小但稳定的收益。
- **适用条件 / 局限** · 依赖生成器与评审器，独立人工审计及跨域复现未报告。

**可复用机制** · 给多模态轨迹数据保留决策理由，并用等规模对照确认改进来自重标还是生成升级。

<a id="paper-149931"></a>

## GPU Hierarchy Meets Structured Matrices: Fast Algorithms for State-Space Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149931) · [作者来源](https://neurips.cc/virtual/2026/poster/149931)

- **问题 / 瓶颈** · 常用序列长度下 SSM 内核受边界状态和衰减掩码瓶颈限制。
- **核心创新 / 方法** · 切分长度独立于矩阵乘 tile，按 1-半可分结构将块内衰减与秩一块间项分开计算。
- **Baseline** · 官方 Triton Mamba-2、FlashAttention-4 及稳定 direct segsum。
- **Benchmark** · H100 上不同序列长度的预填充时间、带宽及稳定掩码性能。
- **关键结果 / 消融** · 预填充较 Triton Mamba-2 快 4.1 倍，1–2k 开始快于 FlashAttention-4，较朴素稳定掩码快 1.35–1.40 倍。
- **适用条件 / 局限** · 实测基于 H100，其他硬件的分界长度未报告。

**可复用机制** · 将序列混合层比较放在目标训练长度上，同时测放大误差、带宽和端到端预填充。

<a id="paper-148527"></a>

## GraDE: A Graph Diffusion Estimator for Frequent Subgraph Discovery in Neural Architectures

[官方论文页](https://neurips.cc/virtual/2026/poster/148527) · [作者来源](https://neurips.cc/virtual/2026/poster/148527)

- **问题 / 瓶颈** · 枚举大子图成本高，直接采样难找到高频模式。
- **核心创新 / 方法** · 学习图扩散分布并用典型性估计对子图候选排序，以此引导搜索。
- **Baseline** · 与采样基线比较，具名实现未报告。
- **Benchmark** · 神经架构图上的子图排序准确性及发现模式的中位频率。
- **关键结果 / 消融** · 作者报告排序准确度最高相对改善 114%，中位频率最高提高 30 倍。
- **适用条件 / 局限** · 典型性为频率代理，跨架构族泛化和训练成本细节未报告。

**可复用机制** · 将扩散分数作为架构子图枚举优先级，再对高优先候选用真实频率回测。

<a id="paper-153272"></a>

## Gradient Boosted Trees for Retrieval-Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153272) · [作者来源](https://neurips.cc/virtual/2026/poster/153272)

- **问题 / 瓶颈** · 迭代 RAG 容易重问热门方面，固定树难补回首轮漏掉的方面。
- **核心创新 / 方法** · 在检索嵌入空间给叶节点估计残差，仅对欠覆盖叶生成改写并以单调改进门控接纳。
- **Baseline** · 比较迭代和结构化 RAG 基线，具名方法未报告。
- **Benchmark** · 标准 RAG 基准与长尾问答设定，具名数据集和指标未报告。
- **关键结果 / 消融** · 摘要报告一致改善，长尾问题增益最大，幅度未报告。
- **适用条件 / 局限** · 语义嵌入残差必须能够识别实际证据缺口，查询预算细节未报告。

**可复用机制** · 用同轮次预算比较全树重写和缺口定向扩展，同时记录子问题证据覆盖。

<a id="paper-156635"></a>

## Gradient descent inference in empirical risk minimization

[官方论文页](https://neurips.cc/virtual/2026/poster/156635) · [作者来源](https://neurips.cc/virtual/2026/poster/156635)

- **问题 / 瓶颈** · 高维经验风险最小化中，迭代共享同一批数据，相关性使逐步推断困难。
- **核心创新 / 方法** · 用两张 Onsager 修正矩阵描述联合状态演化，以可观测的历史损失导数方向线性组合去偏，系数由数据估计。
- **Baseline** · 平方损失线性回归中与去偏凸正则估计量对照。
- **Benchmark** · 单指标回归、广义逻辑回归与线性回归分析，关注近似正态性和泛化误差。
- **关键结果 / 消融** · 去偏后逐步近似正态，无须等到优化收敛；在线性模型中末期有分布意义的对应。
- **适用条件 / 局限** · 样本量与信号维数成比例；依赖论文中的状态演化条件。

**可复用机制** · 把优化轨迹当推断对象，先显式校正历史方向的相关性，再用任一步的去偏统计量估计信号。

<a id="paper-148429"></a>

## Gradient Descent on Two ReLU Neurons: Global Landscape and Bifurcation Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/148429) · [作者来源](https://openreview.net/forum?id=xtpMOeOcPq)

- **问题 / 瓶颈** · 总体损失下降难以揭示两个神经元何时学习共享特征与各自特征。
- **核心创新 / 方法** · 把两教师方向拆成平分方向与分裂方向，联合分析平方损失临界点与梯度流。
- **Baseline** · 理论分析，摘要未给独立基线。
- **Benchmark** · 两 ReLU 教师学生问题，跟踪总体损失地形与方向动态。
- **关键结果 / 消融** · 非零临界点为全局最小点或鞍点；学生先向平分方向聚拢至鞍点附近，再分化。
- **适用条件 / 局限** · 各向同性高斯输入、小随机初始化、总体梯度流及两神经元设定。

**可复用机制** · 用共享分量与特化分量分别诊断训练，检查早期同质化是否只是进入慢速分裂阶段。

<a id="paper-154735"></a>

## Gradient Descent’s Last Iterate is Often (slightly) Suboptimal

[官方论文页](https://neurips.cc/virtual/2026/poster/154735) · [作者来源](https://openreview.net/forum?id=BPdZSMMob3)

- **问题 / 瓶颈** · 标准 GD 或 SGD 末迭代的凸 Lipschitz 优化收敛带对数因子。
- **核心创新 / 方法** · 证明不预先指定停时的步长序列无法统一实现最优末迭代速率。
- **Baseline** · 标准步长与 Jain 等依赖预算的最优末迭代步长。
- **Benchmark** · 凸 Lipschitz 优化的末迭代误差关于步数的最坏情形。
- **关键结果 / 消融** · 即使无噪声 GD，任意时点的末迭代保证也无法避开额外的多对数因子。
- **适用条件 / 局限** · 结论针对该函数类与末迭代保证。

**可复用机制** · 区分固定预算与可随时停止的部署约束，不能直接移植固定预算步长的最优保证。

<a id="paper-153685"></a>

## Gradient-Free Editing for Attribute Invariance in Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/153685) · [作者来源](https://openreview.net/forum?id=JYwUlKcoxQ)

- **问题 / 瓶颈** · 图消息传递传播属性依赖，而部署后常无法重训或访问训练标签。
- **核心创新 / 方法** · 识别属性敏感且结构影响大的节点，定位激活中的低秩敏感方向，再求解子空间约束权重更新。
- **Baseline** · 摘要对比已有 GNN 编辑方法，未列名称。
- **Benchmark** · 评估属性不变性、预测效用与编辑耗时；数据集待核实。
- **关键结果 / 消融** · 摘要报告保持效用并加速约三个数量级。
- **适用条件 / 局限** · 依赖可定位的低秩敏感变化和有代表性的节点。

**可复用机制** · 将去属性问题转为局部子空间约束求解，以单次闭式更新取代全模型微调。

<a id="paper-155990"></a>

## Gradient-Guided Smoothing for LLM Safety Defense

[官方论文页](https://neurips.cc/virtual/2026/poster/155990) · [作者来源](https://openreview.net/forum?id=1LhCQwinaY)

- **问题 / 瓶颈** · 越狱上下文语义裕量较大时，普通随机平滑防御效果减弱。
- **核心创新 / 方法** · 在随机扰动上叠加上下文条件输入密度的梯度引导，增大扰动后的输入概率。
- **Baseline** · 普通随机平滑；其他逐项比较待核实。
- **Benchmark** · 四种越狱威胁与三个指令遵循基准，安全性及效用。
- **关键结果 / 消融** · 摘要报告安全改善且任务效用得以保持。
- **适用条件 / 局限** · 依赖上下文密度估计及其梯度；额外计算和适用模型待核实。

**可复用机制** · 平滑防御优先探索模型熟悉的输入邻域，避免纯噪声把采样继续推向稀疏区域。

<a id="paper-154992"></a>

## Gradient Regularized Newton Boosting Trees with Global Convergence

[官方论文页](https://neurips.cc/virtual/2026/poster/154992) · [作者来源](https://openreview.net/forum?id=9MjVpTTm7u)

- **问题 / 瓶颈** · 二阶树提升经验有效，但普通 Newton boosting 可能发散。
- **核心创新 / 方法** · 在受限弱学习器框架中加入与梯度范数平方根成比例的 L2 正则。
- **Baseline** · 普通 Newton boosting；经典有限维 Newton 理论。
- **Benchmark** · 数值实验检查发散与收敛；理论衡量迭代收敛速率。
- **关键结果 / 消融** · 在 Hessian Lipschitz 的凸损失下证明全局 O(1/k²) 收敛；普通版本在部分实验发散。
- **适用条件 / 局限** · 依赖受限方向及光滑性条件；普通版本的线性速率还需强凸与 Hessian 支配。

**可复用机制** · 根据当前梯度大小调节弱学习器的曲率正则，稳定受限函数空间里的二阶步。

<a id="paper-153255"></a>

## Gradient Routing Localizes and Removes Unintended Behaviors in RL

[官方论文页](https://neurips.cc/virtual/2026/poster/153255) · [作者来源](https://openreview.net/forum?id=Mc1ip92n6o)

- **问题 / 瓶颈** · 奖励惩罚和数据过滤可能引导策略绕开有系统性误差的监控器。
- **核心创新 / 方法** · GRAFT 将标记行为的更新局部化到专属参数，推理时通过消融关闭。
- **Baseline** · 奖励惩罚、依监控标签过滤。
- **Benchmark** · 多个 RL 环境，另将先进模型轨迹蒸馏到 Qwen3-32B；关注异常行为及监控规避。
- **关键结果 / 消融** · 摘要报告定位后可关掉目标行为，并在奖励惩罚出现规避的环境中维持效果。
- **适用条件 / 局限** · 需要能对行为产生部分有效标签的分类器与可拆分的参数。

**可复用机制** · 对于部分可信的反馈，将它用作参数路由信号，再通过参数消融检验行为是否隔离。

<a id="paper-156662"></a>

## Gradient Span Algorithms Make Predictable Progress in High Dimension

[官方论文页](https://neurips.cc/virtual/2026/poster/156662) · [作者来源](https://neurips.cc/virtual/2026/poster/156662)

- **问题 / 瓶颈** · 高维非凸训练中复杂随机地形与重复运行的相似曲线并存。
- **核心创新 / 方法** · 刻画梯度张成类算法在缩放高斯随机函数上的高维极限。
- **Baseline** · 既有随机二次函数和自旋玻璃的同类结果。
- **Benchmark** · 理论分析训练代价轨迹的渐近确定性。
- **关键结果 / 消融** · 证明该函数模型下梯度张成算法轨迹可表现为渐近确定的进展。
- **适用条件 / 局限** · 理论依赖缩放高斯随机函数及高维极限；实际模型需先用多种子检查。

**可复用机制** · 若固定超参下进展曲线已高度集中，优先把搜索预算分配给不同超参。

<a id="paper-148547"></a>

## GradTrack: Detecting Noisy Labels via Temporal Trajectories of Class-wise Gradient Misalignment

[官方论文页](https://neurips.cc/virtual/2026/poster/148547) · [作者来源](https://openreview.net/forum?id=x43qiqLUSG)

- **问题 / 瓶颈** · 损失、置信度与梯度幅值忽略梯度几何和时间信息。
- **核心创新 / 方法** · 估计干净样本的类梯度方向，逐轮排名类内梯度错位，再用混合模型判别排名轨迹。
- **Baseline** · 基于损失、置信度或梯度幅度的检测方式；具体方法待核实。
- **Benchmark** · 合成与真实标签噪声，包含实例依赖噪声；检测与下游训练表现。
- **关键结果 / 消融** · 摘要报告实例依赖噪声下检测表现较强，并可改善既有训练流程。
- **适用条件 / 局限** · 需要跨轮访问样本梯度，且类内能估计参考方向。

**可复用机制** · 通过跨轮梯度方向偏离判断标签异常，避免大梯度难例被单轮筛分误删。

<a id="paper-148635"></a>

## Gram-Calibrated Anchoring for Class-Incremental Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148635) · [作者来源](https://openreview.net/forum?id=wGCFSJasYK)

- **问题 / 瓶颈** · 增量训练反复重算原型代价高，标准余弦分类也忽略类别原型相关。
- **核心创新 / 方法** · 每任务到来时取冻结骨干类均值，推理用正则化 Gram 逆和坐标标准差修正。
- **Baseline** · 近期类别增量方法与余弦分类。
- **Benchmark** · ImageNet-R、ImageNet-A、CIFAR-100、CUB-200，多骨干的准确率与训练成本。
- **关键结果 / 消融** · 摘要报告有竞争力的准确率与显著下降的训练成本；只用单个 LoRA。
- **适用条件 / 局限** · 依赖适配后的原型漂移较小；无样本回放。

**可复用机制** · 把稳定类原型作为分类锚，利用原型间相关矩阵修正过度共享的分类证据。

<a id="paper-153287"></a>

## GRAM: Group-wise Rank-Aware Modal Merging via Subspace Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/153287) · [作者来源](https://openreview.net/forum?id=MOnKup7VWM)

- **问题 / 瓶颈** · 统一合并会因子空间不对齐丢弃任务相关方向。
- **核心创新 / 方法** · 根据主角度衡量任务向量几何相容性，每组独立做 SVD 合并。
- **Baseline** · 既有统一模型合并方法。
- **Benchmark** · Flan-T5 的 GLUE、CLIP 八项视觉任务、Qwen2-7B-Instruct 四种医疗 LoRA。
- **关键结果 / 消融** · 摘要报告用两组便持续改善既有合并结果。
- **适用条件 / 局限** · 需要可比较的微调权重，分组会增加部署模型数。

**可复用机制** · 先检验低秩更新是否共享子空间，再决定可共享模型的任务边界。

<a id="paper-155778"></a>

## GramStatTexNet: Efficient, Interpretable, and Neuro-Inspired Texture Analysis-by-Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/155778) · [作者来源](https://openreview.net/forum?id=2wrNMRgCc2)

- **问题 / 瓶颈** · 深层纹理表示难解释，传统手工纹理统计又难扩展。
- **核心创新 / 方法** · 把多尺度 Gabor 响应的 Gram 相关按滤波器族组织，据此分解合成保真度并学习紧凑嵌入。
- **Baseline** · 传统与深度纹理合成方法。
- **Benchmark** · 多类纹理和多个感知评价指标；具体项目待核实。
- **关键结果 / 消融** · 摘要报告在保持有竞争力的合成质量时，表示紧凑且可解释。
- **适用条件 / 局限** · 主要证据来自纹理；空间池化和时空扩展的适用范围待核实。

**可复用机制** · 用结构化相关统计保留每项特征的来源，以便逐族删减并定位感知质量的贡献。

<a id="paper-150019"></a>

## GRAPE: Graph-Augmented Prototype Explanations for Interactive Medical Image Diagnosis

[官方论文页](https://neurips.cc/virtual/2026/poster/150019) · [作者来源](https://openreview.net/forum?id=lMhOWbjimZ)

- **问题 / 瓶颈** · 医学原型分类器容易无提示地接受不匹配的人为反馈。
- **核心创新 / 方法** · 在选中区域比较模型主导概念和所输标签并提示冲突；另设图注意任务头和文本锚定。
- **Baseline** · MC-Dropout、原型基线和端到端基线。
- **Benchmark** · TBX11K、NIH ChestX-ray14；宏 F1、错误标注捕获、定位和延迟。
- **关键结果 / 消融** · 错误标注捕获 85% 对 51%；任务头在 TBX11K 的宏 F1 提升 13.8 个百分点；整套增加约 1 毫秒。
- **适用条件 / 局限** · 冲突提示依赖模型区域概念质量，不能视为临床真值。

**可复用机制** · 将区域内部的概念一致性作为反馈入库前的校验信号，避免错误监督被直接放大。

<a id="paper-150871"></a>

## Graph and Simplicial Complex Prediction Gaussian Process via Hodgelet Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/150871) · [作者来源](https://openreview.net/forum?id=ekcAe9KkIt)

- **问题 / 瓶颈** · 图输入的高斯过程难以直接纳入边、高阶单纯形属性和洞等拓扑信息。
- **核心创新 / 方法** · 把图输入扩展到单纯复形，并提取可学习的 Hodgelet 拓扑描述符供高斯过程预测。
- **Baseline** · 既有图输入高斯过程；具体对照待核实。
- **Benchmark** · 图级与单纯复形级预测及回归；数据和指标待核实。
- **关键结果 / 消融** · 摘要报告多个应用预测改进，具体幅度待核实。
- **适用条件 / 局限** · 需要能够建立合适的复形及高阶属性。

**可复用机制** · 将 Hodge 分解用作结构特征接口，让概率模型在拓扑层级上表达边与高阶关系。

<a id="paper-154833"></a>

## Graph Anomaly Detection as Dynamical Transport: Training-Free Scoring via Empirical Bayes

[官方论文页](https://neurips.cc/virtual/2026/poster/154833) · [作者来源](https://openreview.net/forum?id=Ac0FQJZfqu)

- **问题 / 瓶颈** · 结构可信度、谱权重与异常度通常纠缠，导致不同图上分数不稳定。
- **核心创新 / 方法** · 用经验贝叶斯拟合图精度和模板，在谱松弛的不同时间与端点容差下计算闭式输运成本，再无标签选择分数。
- **Baseline** · 静态平衡 Mahalanobis 分数与其他图异常检测方法。
- **Benchmark** · 11 个图异常基准，含最大 370 万节点的欺诈图；AUROC 与运行时间。
- **关键结果 / 消融** · 9 个基准并列或单独最佳 AUROC；最大图分解和计分约六分钟。
- **适用条件 / 局限** · 依赖图滤波模板和谱计算；分数选择要求估计零假设拟合与邻域稳定性。

**可复用机制** · 把异常度拆成背景图结构、动态尺度和统计检验，避免为所有图固定一套静态分数。

<a id="paper-154641"></a>

## Graph-Based Stochastic-Power-UCT: Monte-Carlo Graph Search with Power Mean Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/154641) · [作者来源](https://openreview.net/forum?id=C61SqbC0JZ)

- **问题 / 瓶颈** · 树搜索重复评估不同轨迹到达的同一状态；只凭状态合并会混入不同剩余时域的值。
- **核心创新 / 方法** · 在同一规划深度共享状态，跨深度分开存值；另用自适应时域控制全状态共享偏差。
- **Baseline** · 树式 Stochastic-Power-UCT 和图搜索基线。
- **Benchmark** · 随机规划基准，关注根值收敛与样本效率。
- **关键结果 / 消融** · 固定时域根值收敛 O(n^-1/2)，匹配树式方法且实验更省样本。
- **适用条件 / 局限** · 理论面向随机 MDP；无限时域扩展还需跨深度差异消失。

**可复用机制** · 用状态与剩余时域作为缓存键，在共享样本时保留价值所需的时间条件。

<a id="paper-155097"></a>

## Graph Cascades: Contagion-Based Mesoscopic Rewiring for Structure-Aware Graph Machine Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155097) · [作者来源](https://openreview.net/forum?id=8R0BMd5zmJ)

- **问题 / 瓶颈** · 局部邻接与全局注意力之间缺少对中尺度结构的直接利用。
- **核心创新 / 方法** · 将反复获得多跳扩散支持的节点对连为直接邻居，构造辅助图。
- **Baseline** · 多种 GNN 和稀疏图 Transformer 骨干。
- **Benchmark** · 节点分类基准，比较分类表现和新图边的结构属性。
- **关键结果 / 消融** · 异配图及中高平均度同配图效果较稳定，低度正则图和有结构瓶颈图增益较弱。
- **适用条件 / 局限** · 新边需要重复扩散证据；不能保证任意图都有收益。

**可复用机制** · 用多跳重复支持代替单路径可达性，减少把偶然远邻引入消息传递。

<a id="paper-155722"></a>

## Graph Distance Based on Cause-Effect Estimands with Latents

[官方论文页](https://neurips.cc/virtual/2026/poster/155722) · [作者来源](https://openreview.net/forum?id=3PbzWjbwZ4)

- **问题 / 瓶颈** · 存在潜在混杂时，相同数量的结构误差对效应估计的影响可能差异很大。
- **核心创新 / 方法** · 对有向无环混合图用 fixing 识别处理效应，并用符号验证器比较不同处理与结果对的估计量。
- **Baseline** · 已有因果图距离。
- **Benchmark** · 不同图扰动；关注因果效应估计量发生何种变化。
- **关键结果 / 消融** · 摘要展示度量与现有结构距离互补。
- **适用条件 / 局限** · 适用于指定混合图与可分析的处理结果对；依赖识别与符号比较。

**可复用机制** · 对齐结构学习的评测目标与下游决策，优先区分会改变目标效应的错误。

<a id="paper-152480"></a>

## Graph Energy Matching: Transport-Aligned Energy-Based Modeling for Graph Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152480) · [作者来源](https://openreview.net/forum?id=Sm423QKBUU)

- **问题 / 瓶颈** · 离散能量模型易在分布支持之外出现局部极小值。
- **核心创新 / 方法** · 用 JKO 运输视角学习置换不变势能，再按能量切换梯度引导运输与局部混合。
- **Baseline** · 离散扩散模型，具体名称待核实。
- **Benchmark** · 分子图生成及性质约束生成，具体指标待核实。
- **关键结果 / 消融** · 大多数所报指标达到或超过离散扩散对照。
- **适用条件 / 局限** · 目前摘要证据限于分子图，切换阈值需查正文。

**可复用机制** · 把往高概率区域移动和区内混合分为两个采样阶段，用共享势能决定何时切换。

<a id="paper-139037"></a>

## GraphInstruct: A Progressive Benchmark for Diagnosing Capability Gaps in LLM Graph Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/139037) · [作者来源](https://openreview.net/forum?id=ogKUVGdJZR)

- **问题 / 瓶颈** · 按图类型平均无法定位在哪个复杂度区间失效。
- **核心创新 / 方法** · 按六级复杂度及五个维度评测，并用失败约束反馈改写提示。
- **Baseline** · 12 个语言模型及多种提示策略，共 45 种配置。
- **Benchmark** · 800 条人工指令、1,582 个算法生成参考解，评估图生成约束满足。
- **关键结果 / 消融** · 约束组合区分度最高；所测迭代方法未改善领域语义约束，验证反馈改善目标模型表现。
- **适用条件 / 局限** · 结论限于所测图任务，检索是否改善仍待验证。

**可复用机制** · 若结构约束可通过迭代修复而语义约束长期停滞，分别评估验证反馈和外部知识补充。

<a id="paper-139174"></a>

## GraphIP–Bench: How Hard Is It to Steal a Graph Neural Network, and Can We Stop It?

[官方论文页](https://neurips.cc/virtual/2026/poster/139174) · [作者来源](https://openreview.net/forum?id=gVarjIBpLT)

- **问题 / 瓶颈** · 仅验证防护模型自身的水印，可能高估部署后的所有权保护。
- **核心创新 / 方法** · 在统一黑盒威胁模型中联合比较防护有效性和验证信号保留，控制数据划分和预算。
- **Baseline** · 比较水印、输出扰动与查询模式检测等防护。
- **Benchmark** · 十个公开图、三种图网络骨干及三类图学习任务，指标含任务效用、所有权验证和计算代价。
- **关键结果 / 消融** · 作者报告部分水印可在受保护模型上通过验证，而在防护压力测试后验证信号大幅衰减。
- **适用条件 / 局限** · 结论限于所评测的公开图、黑盒设置和防护实现。

**可复用机制** · 把防护信号在压力测试后的持续性作为独立验收指标，并和原模型效用一起报告。

<a id="paper-150743"></a>

## Graph Label Alignment: A Diagnostic Atlas for Graph Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/150743) · [作者来源](https://openreview.net/forum?id=fiy00bWoJN)

- **问题 / 瓶颈** · 池化基线高分可能掩盖基准不需要结构与特征交互。
- **核心创新 / 方法** · 分别用拓扑谱摘要、去边后的节点特征池化作两个监督探针，再构造边际匹配但角色特征耦合不同的测试。
- **Baseline** · 多个池化骨干。
- **Benchmark** · 真实图分类基准、异配自我图和合成 Twins 任务，指标为测试准确率。
- **关键结果 / 消融** · 高对齐解释大量简单基准表现，低对齐时标准池化持续遇到困难。
- **适用条件 / 局限** · 探针取决于所用摘要，低对齐本身不足以证明所有可能的边际模型都失败。

**可复用机制** · 构造只改变耦合关系的匹配边际对照，以检验模型是否真正使用交互。

<a id="paper-149829"></a>

## GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/149829) · [作者来源](https://openreview.net/forum?id=n0In1zdsw5)

- **问题 / 瓶颈** · 仅靠嵌入局部化可能得到低效预测集。
- **核心创新 / 方法** · 特征感知增密后用个性化 PageRank 核衡量结构接近性，结合特征与结构加权。
- **Baseline** · 以嵌入空间局部化的图共形方法，具体待核实。
- **Benchmark** · 多套图回归和分类数据，关注边际覆盖、测试条件覆盖。
- **关键结果 / 消融** · 作者报告提供边际覆盖保证并取得较好的测试条件覆盖。
- **适用条件 / 局限** · 保证的假设和低同质、强异配设置需查正文。

**可复用机制** · 先检查同质性与覆盖误差的关联，再决定校准近邻是否使用图扩散。

<a id="paper-156071"></a>

## Graph Learning from Label Proportions using Topology-Aware Pseudo Labeling and Aggregation

[官方论文页](https://neurips.cc/virtual/2026/poster/156071) · [作者来源](https://openreview.net/forum?id=0f6mA6p98z)

- **问题 / 瓶颈** · 图上实例依赖使独立样本的比例监督难以利用拓扑。
- **核心创新 / 方法** · 以同质性感知的代价做最优传输，得到节点软标签，再训练图网络。
- **Baseline** · 现有比例学习方法及变体。
- **Benchmark** · 六个同质图基准和 Covid 真实数据，任务为节点分类。
- **关键结果 / 消融** · 作者报告优于现有对照，并论证代价与节点分类目标对齐。
- **适用条件 / 局限** · 异配图表现待核实。

**可复用机制** · 将包级比例约束与邻接相关性结合，减少从聚合比例恢复伪标签时的歧义。

<a id="paper-153064"></a>

## GraphMemRL: Action-Native Reinforcement Learning for Persistent Graph Memory Construction

[官方论文页](https://neurips.cc/virtual/2026/poster/153064) · [作者来源](https://openreview.net/forum?id=OEtBtIA3pG)

- **问题 / 瓶颈** · 单查询不足以检索编辑所需证据，整轨迹监督难以定位局部更新价值。
- **核心创新 / 方法** · 面向编辑分解查询，以状态转移监督评分局部图编辑，并跨片段维护持久图。
- **Baseline** · 单整体查询和全轨迹优化范式，具名对照待核实。
- **Benchmark** · 长记忆问答，包括多跳、时序、知识更新，另看连通性和增长。
- **关键结果 / 消融** · 作者报告问答改善、图连通更好且增长更可控。
- **适用条件 / 局限** · 上下文预算与逐步监督成本待核实。

**可复用机制** · 将检索和奖励都对齐到一次写入动作，并在固定记忆预算下观察图结构增长。

<a id="paper-152847"></a>

## Graph-Regularized Sparse Autoencoders for LLM Safety Steering

[官方论文页](https://neurips.cc/virtual/2026/poster/152847) · [作者来源](https://openreview.net/forum?id=PvSZSLQLGc)

- **问题 / 瓶颈** · 稀疏自编码器将潜特征独立处理，可能忽略分布式安全行为。
- **核心创新 / 方法** · 对解码向量按神经元共激活图施加平滑，部署时以双门控制方向库。
- **Baseline** · 激活干预与黑盒防护，并与相同方向库及门控但去掉图正则的版本比较。
- **Benchmark** · JailbreakBench、HarmBench、XSTest，关注有害拒绝及正常请求误拒。
- **关键结果 / 消融** · Llama-3-8B 的图正则消融在前两套基准上分别提升选择性指标 20.1、16.8 点。
- **适用条件 / 局限** · 图构造和不同领域误拒的边界待核实。

**可复用机制** · 在固定运行控制器的条件下，用共激活结构正则化方向学习并独立测误拒。

<a id="paper-148152"></a>

## Graph Sparse Sampling: Breaking the Curse of the Horizon in Continuous MDP Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/148152) · [作者来源](https://openreview.net/forum?id=zuBW1RbCZQ)

- **问题 / 瓶颈** · 逐分支规划在长视距和连续空间中预算增长过快。
- **核心创新 / 方法** · 共享采样未来并以平滑备份计算多候选动作价值，形成可批处理的无分支图。
- **Baseline** · 树形稀疏采样与树搜索规划器。
- **Benchmark** · 连续控制仿真及不同规划视距；指标细节待核实。
- **关键结果 / 消融** · 所测长视距中优于树基线，特定条件下给出视距多项式的有限样本界。
- **适用条件 / 局限** · 界要求状态重叠、正则性和动作覆盖，暂仅仿真。

**可复用机制** · 先估计候选未来状态的重叠程度，再决定能否通过共享样本换取更长规划深度。

<a id="paper-149861"></a>

## Graph Topology Augmentation for Prioritized Sweeping in Non-stationary Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149861) · [作者来源](https://openreview.net/forum?id=midyPx9DqU)

- **问题 / 瓶颈** · 仅按残差排队要等已执行的备份传播误差。
- **核心创新 / 方法** · 在策略转移图上用正则化有向拉普拉斯势传播残差信息，以第二大特征值模调节权重。
- **Baseline** · 标准优先扫掠，置于精确 DP 和 Dyna 两类规划器。
- **Benchmark** · FourRooms 与 GARNET 表格域，考察重规划效率。
- **关键结果 / 消融** · 作者报告对被标准扫掠阻塞的状态给出非零优先级，并提高重规划效率。
- **适用条件 / 局限** · 暂限表格实验；转移图维护成本待核实。

**可复用机制** · 当变化信号仅从少量状态开始传播时，把结构扩散项纳入更新顺序。

<a id="paper-149147"></a>

## GraphUAT: Uncertainty Attribution in Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/149147) · [作者来源](https://openreview.net/forum?id=sV9yc7CpY9)

- **问题 / 瓶颈** · 置信度难指出究竟哪些节点特征和结构造成不确定。
- **核心创新 / 方法** · 蒸馏可分离两类不确定性的学生，再用针对性探针做特征与结构归因。
- **Baseline** · 原训练图模型作为教师，具名归因对照待核实。
- **Benchmark** · 多个图基准，测移除归因元素后的教师不确定性变化。
- **关键结果 / 消融** · 作者报告移除所定位元素后一致降低教师不确定性。
- **适用条件 / 局限** · 不确定性下降与准确率改善是独立问题，后者待核实。

**可复用机制** · 以原模型上的归因删减验证代理诊断，而非只检查学生指标。

<a id="paper-152072"></a>

## GRASP: Guided Residual Adapters with Sample-wise Partitioning

[官方论文页](https://neurips.cc/virtual/2026/poster/152072) · [作者来源](https://openreview.net/forum?id=VfoRDHdZvl)

- **问题 / 瓶颈** · 头尾样本梯度对齐较低，尾类生成质量与多样性下降。
- **核心创新 / 方法** · 确定性划分条件，按组更新 Transformer 前馈层的残差适配器，保留流匹配目标和采样器。
- **Baseline** · 全量微调、学习路由 MoE、少数类引导。
- **Benchmark** · MIMIC-CXR-LT 和 ImageNet-LT 等；指标含 FID、尾类覆盖、下游宏 F1。
- **关键结果 / 消融** · 报告总体 FID 最多下降 80%、尾类覆盖最多提升 44%，并能结合少数类采样。
- **适用条件 / 局限** · 需确认条件分组质量及各尾类覆盖；摘要数字为最大收益。

**可复用机制** · 以条件分组保证每个尾样本更新所属适配器，同时保留采样阶段的独立干预。

<a id="paper-153241"></a>

## Grassmannian Geodesic Steering: Rank-Preserving Subspace Control for Inference-Time Alignment of Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153241) · [作者来源](https://openreview.net/forum?id=MhWinGteUz)

- **问题 / 瓶颈** · 加法式干预可能降低有效秩，低维旋转难覆盖分布式行为。
- **核心创新 / 方法** · 通过对比差分协方差估计概念子空间，以 Grassmann 测地正交算子干预并动态门控强度。
- **Baseline** · 加法干预、低维旋转和免训练激活干预方法。
- **Benchmark** · LLaMA-3.1-8B、Qwen-2.5-7B，六项推理测评与 AdvBench。
- **关键结果 / 消融** · 报告有效秩退化比加法方法低两个数量级，每步额外耗时低于 1.5%。
- **适用条件 / 局限** · 概念对照样本构造和维度选择敏感性待核实。

**可复用机制** · 选择干预方向时同时评估对齐准确度、生成质量和谱退化。

<a id="paper-154812"></a>

## Greedy Alignment Principle for Optimizer Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/154812) · [作者来源](https://openreview.net/forum?id=Alx4pHbiDI)

- **问题 / 瓶颈** · 逐步梯度对齐启发式缺少用于优化器超参选择的统一目标。
- **核心创新 / 方法** · 把优化器写成因果滤波器，以滤波器和梯度自相关内积表示预期损失下降率，据此动态调动量。
- **Baseline** · SGD 动量及 Adam 或 AdamW 的人工扫参固定动量。
- **Benchmark** · 图像分类、语言模型微调、视觉 Transformer 微调；指标待核实。
- **关键结果 / 消融** · 作者报告动态规则持平或超过人工找到的最佳固定超参。
- **适用条件 / 局限** · 稳定界依赖梯度统计估计，更多优化器族待核实。

**可复用机制** · 用梯度自相关作为动量时标的可测依据，并以固定训练预算对比人工扫参。

<a id="paper-154294"></a>

## GReFEM: Multimodal LLMs as Zero-Shot Semantic Assistants for Physics-Guided 3D Mesh Refinement

[官方论文页](https://neurips.cc/virtual/2026/poster/154294) · [作者来源](https://openreview.net/forum?id=Enr88JG4iE)

- **问题 / 瓶颈** · 逐次求解 PDE 来布置细网格开销较高。
- **核心创新 / 方法** · orthoViews 选择更能暴露关键几何特征的视角；物理提示让多模态模型标出应力相关位置。
- **Baseline** · 等细化预算下比较调优的几何启发式。
- **Benchmark** · 多种 CAD 几何、载荷工况和多模态模型。
- **关键结果 / 消融** · 摘要称应力相关特征定位精度更高。
- **适用条件 / 局限** · 代理用途是定位；实际误差改善和可用工况边界待全文核实。

**可复用机制** · 将视角选择与细化策略分开，在同等单元预算下测定位精确率。

<a id="paper-152781"></a>

## GridDiffuser: Constraint-Guided Graph Diffusion for AC Optimal Power Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/152781) · [作者来源](https://openreview.net/forum?id=QONjqmSVsQ)

- **问题 / 瓶颈** · 单点预测难覆盖多种工况下的非凸可行解。
- **核心创新 / 方法** · 图扩散生成多个工况候选，在干净样本估计上迭代做 Levenberg–Marquardt 校正。
- **Baseline** · 确定性学习方法；求解速度对照 AC-IPOPT。
- **Benchmark** · 千节点级电网、逐实例 N-1 故障，比较潮流前后违例和速度。
- **关键结果 / 消融** · 摘要称相对确定性基线违例更少、相对 AC-IPOPT 更快。
- **适用条件 / 局限** · 需要可用于校正的约束；可行性保证待核。

**可复用机制** · 在扩散的干净估计上校正约束残差，并测增加候选数的边际收益。

<a id="paper-153337"></a>

## Grid Games: The Power Of Multiple Grids for Quantizing Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153337) · [作者来源](https://openreview.net/forum?id=M4Xj5w0EcJ)

- **问题 / 瓶颈** · 单一 4 位网格无法适配组间分布变化。
- **核心创新 / 方法** · 以尺度位标记分组所选网格；提出 NF4 加学习网格、双学习网格和 SFP4 三网格。
- **Baseline** · 单网格 FP4，包括 NVFP4、MXFP4 格式背景。
- **Benchmark** · 开放模型后训练量化和 Llama 式预训练，含权重与权重加激活两种设置。
- **关键结果 / 消融** · 自适应网格准确性更好；理论上超大组收益消失。
- **适用条件 / 局限** · 收益随组大小变化；吞吐和元数据成本待核。

**可复用机制** · 同时扫量化组大小与网格数，检查额外选择位的收益。

<a id="paper-149994"></a>

## GridProbe: Posterior-Probing for Adaptive Test-Time Compute in Long-Video VLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149994) · [作者来源](https://openreview.net/forum?id=lcdVMrJksq)

- **问题 / 瓶颈** · 全帧注意力昂贵，对比式选帧难处理否定和跨帧计数。
- **核心创新 / 方法** · 将帧排成网格，行列探针的峰值后验做外积，从重要性图偏度和峰度确定帧数。
- **Baseline** · 单次全帧推理及固定预算选帧思路。
- **Benchmark** · Video-MME-v2、LongVideoBench，平均准确率与 TFLOPs。
- **关键结果 / 消融** · 前者算力降 3.36 倍且准确率相差 1.6 个百分点以内；后者用 0.35 倍算力提高 0.9 点。
- **适用条件 / 局限** · 依赖冻结模型的后验；其他模型及多证据场景需验证。

**可复用机制** · 用低成本行列探测估算证据集中度，再决定昂贵模型读取多少帧。

<a id="paper-149734"></a>

## GRNAgent: A Multimodal Graph Reasoning Agent for Gene Regulatory Network Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/149734) · [作者来源](https://openreview.net/forum?id=nlaQh30azU)

- **问题 / 瓶颈** · 表达关联、可及性和基序支持覆盖不均且难直接对齐。
- **核心创新 / 方法** · 以转录因子为中心建候选边证据图，将证据类型化，先融合基序与可及性，再融合表达，最后联合注意。
- **Baseline** · 24 数据集对比 10 个方法，摘要未列具体名称。
- **Benchmark** · 全矩阵 AUPRC 与早期精度；另有留一转录因子、未见细胞类型设置。
- **关键结果 / 消融** · 采样评测 AUPRC 分别为 0.801 和 0.705。
- **适用条件 / 局限** · 依赖候选边和部分组学证据；消融与最终泛化范围待核。

**可复用机制** · 将先验支持与观测相关信号分开编码，再在固定候选边上做融合消融。

<a id="paper-150726"></a>

## Grokking or Glitching? How Low-Precision Drives Slingshot Loss Spikes

[官方论文页](https://neurips.cc/virtual/2026/poster/150726) · [作者来源](https://openreview.net/forum?id=fs99JEN6m5)

- **问题 / 瓶颈** · 长时间无正则训练的损失尖峰常被解释成内在优化现象。
- **核心创新 / 方法** · 高置信度下正确类梯度被舍入为零，错误类仍非零，破坏零和并使分类器与特征均值形成正反馈。
- **Baseline** · 对照解释是内在优化动力学；精度对照具体设置待核。
- **Benchmark** · 观察长时分类训练的梯度、均值范数和损失尖峰。
- **关键结果 / 消融** · 证明对应均值可指数增长；部分样本触发舍入误差时仍可能只有范数增长。
- **适用条件 / 局限** · 取决于浮点吸收阈值、置信度和实现。

**可复用机制** · 同时监测类别梯度和与特征均值，并用高精度交叉熵复跑验证数值归因。

<a id="paper-152856"></a>

## Grounded-Exo2Ego: Structured Semantic Grounding for Robust Exocentric-to-Egocentric Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152856) · [作者来源](https://openreview.net/forum?id=PsbYphBWj9)

- **问题 / 瓶颈** · 外视角到第一视角存在遮挡和从未观测区域，几何投影不完整。
- **核心创新 / 方法** · 双分支视频扩散分别接收投影到目标视角的三维重建和附着于几何的物体语义；补充清洗实拍及合成人体数据。
- **Baseline** · 近期外视角到第一视角方法，名称待核。
- **Benchmark** · EgoExo4D 及组件消融，指标定义待核。
- **关键结果 / 消融** · 报告优于近期方法，语义锚定和数据处理都有贡献。
- **适用条件 / 局限** · 依赖投影与标注，遮挡区域生成仍有不确定性。

**可复用机制** · 保留可靠几何作位置锚点，用分物体语义处理几何缺口。

<a id="paper-148826"></a>

## Grounded or Fabricated? Unsupervised Detection of LLM Hallucinations via Contextualized Influence on Response Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/148826) · [作者来源](https://openreview.net/forum?id=ur1ym0WRCP)

- **问题 / 瓶颈** · 多样本一致性检查成本高，监督检测依赖标注。
- **核心创新 / 方法** · 测量单独编码答案与结合问题编码答案的嵌入差异，小差异视作高风险信号。
- **Baseline** · 多回答一致性与有标签监督是主要对照路线。
- **Benchmark** · 跨任务检测效果与检测成本，数据集和指标待核。
- **关键结果 / 消融** · 摘要称效果相当或更优，成本低于多回答法。
- **适用条件 / 局限** · 问题影响不等于事实正确，阈值迁移和失败例待核。

**可复用机制** · 把问题条件下的嵌入偏移当成可校准的单回答风险特征。

<a id="paper-139101"></a>

## Ground False: Uncovering Errors in Formal Mathematics Benchmarks

[官方论文页](https://neurips.cc/virtual/2026/poster/139101) · [作者来源](https://openreview.net/forum?id=l0dHSybfie)

- **问题 / 瓶颈** · 形式数学评测默认参考命题正确，错误会扭曲模型比较。
- **核心创新 / 方法** · 用 Lean 检查可证性，语言模型判断忠实性，再经人工审核。
- **Baseline** · ProofNet 原版与 ProofNet-Verified；扩展到其他六套。
- **Benchmark** · ProofNet 367 条，统计失真和不可证比例，分析两个任务的评分偏差。
- **关键结果 / 消融** · 204 条不忠实，逾半数学上为假；扩展基准失真率为 4.8% 至 60.0%。
- **适用条件 / 局限** · 语言模型判断需人审，找不到证明本身不能证伪。

**可复用机制** · 发布形式题目标前分别记录可证性与忠实性，检查修订是否改变排名。

<a id="paper-155516"></a>

## Grounding Agent Reasoning with Structured Process Supervision for Multi-turn Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155516) · [作者来源](https://openreview.net/forum?id=519KXHiEy2)

- **问题 / 瓶颈** · 只按结果奖励时，推理与观测脱节后容易持续传播。
- **核心创新 / 方法** · ARC 对全局进度陈述和局部结果预测给予过程监督，过程与结果优势分别组归一化。
- **Baseline** · 结果式强化学习、自由形式过程奖励和各环境最强基线。
- **Benchmark** · ALFWorld、WebShop、WebArena 与轨迹一致性诊断。
- **关键结果 / 消融** · 三环境领先 6.4、3.5、9.6 点；失败轨迹 74% 存在推理与观测不一致。
- **适用条件 / 局限** · 要求下一步观测可验证预测，开放任务的监督成本待核。

**可复用机制** · 将过程奖励绑到可被环境证伪的预测，分开归一化稠密与稀疏信号。

<a id="paper-152499"></a>

## Grounding Driving VLA via Inverse Kinematics

[官方论文页](https://neurips.cc/virtual/2026/poster/152499) · [作者来源](https://openreview.net/forum?id=SgCKaaYRfX)

- **问题 / 瓶颈** · 驾驶轨迹模型可能忽略视觉并依赖文本或自车状态。
- **核心创新 / 方法** · 让语言模型预测未来视觉状态，再让交叉注意条件扩散以当前和未来画面为条件解码轨迹。
- **Baseline** · 现有驾驶 VLA；比较约 7B–8B 模型。
- **Benchmark** · NAVSIM-v2 与 nuScenes，评测轨迹规划和视觉依赖。
- **关键结果 / 消融** · 0.5B 模型达到接近较大模型的规划表现；转弯等动态场景受益更明显。
- **适用条件 / 局限** · 动作依赖未来视觉预测质量，跨台架迁移待核。

**可复用机制** · 以动作前后状态为边界做解码，并用视觉消融检查是否真正减少捷径。

<a id="paper-154493"></a>

## Grounding Multimodal Reasoning with Evidence-Ablated Negatives

[官方论文页](https://neurips.cc/virtual/2026/poster/154493) · [作者来源](https://openreview.net/forum?id=DBleeCZ9TP)

- **问题 / 瓶颈** · 结果奖励可能给猜对答案但没用到图像的策略正反馈。
- **核心创新 / 方法** · 用缩放图像信息增益和混合排序选题，遮盖关键图块生成负答，再在干净图输入上用有界辅助信号惩罚。
- **Baseline** · 强 RLVR 方法；名称待核。
- **Benchmark** · 困难多模态推理基准，考察表现和模态失衡。
- **关键结果 / 消融** · 摘要称改善模态失衡并超过对照。
- **适用条件 / 局限** · 须能识别判别图块，遮挡诱导的伪相关需另测。

**可复用机制** · 保留干净输入用于训练，把去证据反事实仅用于生成在线负例。

<a id="paper-153493"></a>

## Group-Aware Matrix Estimation and Latent Subspace Recovery

[官方论文页](https://neurips.cc/virtual/2026/poster/153493) · [作者来源](https://openreview.net/forum?id=KzAoc5hDss)

- **问题 / 瓶颈** · 单一全局低秩会抹去欠采样子群的潜子空间差异。
- **核心创新 / 方法** · 对重叠类别子矩阵施加核范数惩罚，在共享坐标中做凸估计。
- **Baseline** · 全局低秩、侧信息和现代插补基线。
- **Benchmark** · 合成、推荐、生态及神经数据，对比重建和局部子空间恢复。
- **关键结果 / 消融** · 结构化缺失下收益最大；给出与采样、秩和重叠相关的有限样本保证。
- **适用条件 / 局限** · 需可用类别标签并近似满足局部低秩。

**可复用机制** · 在群组异质时分别评估插补误差与子空间保真度，验证重叠正则收益。

<a id="paper-154085"></a>

## Group Distributionally Robust Optimization with Flexible Sample Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/154085) · [作者来源](https://openreview.net/forum?id=GKDd9FPubr)

- **问题 / 瓶颈** · 固定全组采样难部署，单样本迭代轮数多。
- **核心创新 / 方法** · 双人博弈联用随机梯度 FTRL 与随样本预算调整探索的有限反馈预测。
- **Baseline** · 每轮查询全部组与单样本两种固定策略。
- **Benchmark** · 理论分析任意逐轮样本量的高概率优化误差和固定预算样本复杂度。
- **关键结果 / 消融** · 误差界随各轮样本量增大而下降，固定预算下保持近最优样本复杂度。
- **适用条件 / 局限** · 实际收益及组间采样成本不等的情形待核。

**可复用机制** · 把动态可用数据量作为组选择器输入，按实际查询量比较最差组风险。

<a id="paper-155771"></a>

## Grouped Adaptive Head Mixing for Personalized Multi-Task Federated Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155771) · [作者来源](https://openreview.net/forum?id=32D5gvPRnB)

- **问题 / 瓶颈** · 异质任务共享参数易引起负迁移和成绩失衡。
- **核心创新 / 方法** · 分解局部 Bellman 残差，根据本地更新几何聚组，再动态混合组原型和本地头。
- **Baseline** · 个性化联邦多任务强化学习及集中多任务参考。
- **Benchmark** · MiniGrid 最多 12 个任务、MetaWorld 最多 50 个任务，报告相对改善和收敛任务比例。
- **关键结果 / 消融** · MiniGrid 相对提升最高 24.5%；收敛任务比例从 50.0% 升至 72.9%。
- **适用条件 / 局限** · 兼容性和不确定性靠代理量，极异构客户端的边界待核。

**可复用机制** · 共享决策头前按兼容性聚组，并以失配和估计误差动态调混合比例。

<a id="paper-149985"></a>

## Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149985) · [作者来源](https://openreview.net/forum?id=li8veKFGaF)

- **问题 / 瓶颈** · 稀疏奖励下逐轨迹估值方差大，难找关键步骤。
- **核心创新 / 方法** · 合并相同观测，用跨轨迹聚合估值，把动作放到状态转移边并全局标准化 TD 误差。
- **Baseline** · 提示式与强化学习基线，包括 GRPO。
- **Benchmark** · WebShop、ALFWorld、AppWorld，指标为成功率。
- **关键结果 / 消融** · 作者称相对 GRPO 的成功率改善最高 22.2%。
- **适用条件 / 局限** · 同观测可能对应不同隐藏状态，状态混叠需检验。

**可复用机制** · 仅在可判定状态等价时跨轨迹共用价值估计，测关键转移上的信用噪声。

<a id="paper-139134"></a>

## GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations

[官方论文页](https://neurips.cc/virtual/2026/poster/139134) · [作者来源](https://openreview.net/forum?id=j47R4xMYJL)

- **问题 / 瓶颈** · 双人记忆评测覆盖不了群体角色、个人认知与受众切换。
- **核心创新 / 方法** · 以图控制回帖结构，按人设和受众合成会话，再按提问人绑定挑战查询。
- **Baseline** · 多个领先记忆系统及 BM25。
- **Benchmark** · GroupMemBench 六类查询，包括知识更新、术语歧义与拒答。
- **关键结果 / 消融** · 最强系统 46.0%；知识更新 27.1%、术语歧义 37.7%；BM25 达到或超过多数方法。
- **适用条件 / 局限** · 合成会话与真实群聊的偏差待核。

**可复用机制** · 在压缩记忆时保留发言者、受众和原词，并用归属敏感的问题复验。

<a id="paper-153234"></a>

## Group of Skills: Group-Structured Skill Retrieval for Agent Skill Libraries

[官方论文页](https://neurips.cc/virtual/2026/poster/153234) · [作者来源](https://openreview.net/forum?id=MmJBYf16Bn)

- **问题 / 瓶颈** · 平铺技能或依赖包仍让智能体猜入口和使用条件。
- **核心创新 / 方法** · 从带类型技能图构造锚点组，跨组扩展，压缩到固定技能预算并渲染 START、SUPPORT、CHECK、AVOID。
- **Baseline** · 平铺技能访问和结构化检索参考。
- **Benchmark** · SkillsBench、ALFWorld，比较可见需求覆盖、奖励和智能体用时。
- **关键结果 / 消融** · 小预算保持覆盖，常改善奖励与时延。
- **适用条件 / 局限** · 依赖技能图质量；不同库的整理成本待核。

**可复用机制** · 在保持技能内容和智能体固定的对照下测角色标记的单独收益。

<a id="paper-154678"></a>

## Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity in Multi-Agent Debate

[官方论文页](https://neurips.cc/virtual/2026/poster/154678) · [作者来源](https://openreview.net/forum?id=BqTbDi43uU)

- **问题 / 瓶颈** · 个体置信度与困惑度不足以判断推理正确性，可能加剧盲从。
- **核心创新 / 方法** · DEAR 提取共识与分歧，用选择和行为智能体调整参考对象及生成行为。
- **Baseline** · 基于置信度、困惑度的个体评价。
- **Benchmark** · 多轮语言模型辩论；任务和指标待核实。
- **关键结果 / 消融** · 摘要未给出定量结果。
- **适用条件 / 局限** · 需要能估计群体不确定性，训练反馈和开销待核实。

**可复用机制** · 把同伴引用视为可控的交互结构，按分歧调整信息流。

<a id="paper-148445"></a>

## Growing a Neural Network in Breadth, Depth, and Time

[官方论文页](https://neurips.cc/virtual/2026/poster/148445) · [作者来源](https://openreview.net/forum?id=xl72oIaJ4k)

- **问题 / 瓶颈** · 固定架构难探索三种计算资源能否替代。
- **核心创新 / 方法** · 在卷积递归格构中为宽、深、时间设可微成本，与任务误差联合训练。
- **Baseline** · 摘要未列具体外部方法。
- **Benchmark** · 目标识别与遮挡输入；另比较计算步数和人类反应时间。
- **关键结果 / 消融** · 三种资源可互换；复杂任务使用更多资源，遮挡诱发更多递归步。
- **适用条件 / 局限** · 结论来自所用格构与识别实验。

**可复用机制** · 将网络形状和动态计算放在同一可微预算内，让不同输入使用不同递归深度。

<a id="paper-148490"></a>

## GSQ: Highly-Accurate Low-Precision Scalar Quantization for LLMs via Gumbel-Softmax Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/148490) · [作者来源](https://openreview.net/forum?id=xPoqKULr74)

- **问题 / 瓶颈** · 传统标量量化在极低位宽的精度落后于较难部署的向量方案。
- **核心创新 / 方法** · 用类别数匹配目标量化级数的 Gumbel-Softmax 联合学习每坐标指派与每组尺度。
- **Baseline** · GPTQ、AWQ；QTIP 作为精度前沿。
- **Benchmark** · Llama-3.1-8B/70B-Instruct、GGUF K-Quant 和 Kimi-K2.5；量化精度。
- **关键结果 / 消融** · 摘要报告在 2、3 比特时缩小与 QTIP 的大部分差距，并可回写同一 GGUF 格式。
- **适用条件 / 局限** · 保留标量网格与分组约束；精确校准开销待核实。

**可复用机制** · 分开考虑赋值优化与部署格式，在固定解码结构内搜索更好的离散指派。

<a id="paper-139231"></a>

## GT-Free OCR Metrics: A Reference-Free Evaluation Framework for Document OCR Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/139231) · [作者来源](https://openreview.net/forum?id=dSWBIbUTbe)

- **问题 / 瓶颈** · 逐元素人工真值难支撑持续质检。
- **核心创新 / 方法** · 把识别输出回渲染为图像，与遮罩原页做视觉比较，以学习或组合相似度排序。
- **Baseline** · 整页 CLIP 余弦相似度；有标签编辑距离和 TEDS 用于校验。
- **Benchmark** · OmniDocBench 1,355 页、五种输出模式；Spearman 相关。
- **关键结果 / 消融** · 组合方法平均 0.494，CLIP 为 0.339；公式单项峰值 0.605。
- **适用条件 / 局限** · 代理指标只能部分恢复 OCR 真值排名，受版式和渲染影响。

**可复用机制** · 将结构化输出投回输入空间做规模化一致性评估，并用少量标注校准代理效度。

<a id="paper-149359"></a>

## GT-HarmBench: Benchmarking AI Safety Risks Through the Lens of Game Theory

[官方论文页](https://neurips.cc/virtual/2026/poster/149359) · [作者来源](https://openreview.net/forum?id=qdCqebpQ1b)

- **问题 / 瓶颈** · 单体评测遗漏利害冲突和协调失败。
- **核心创新 / 方法** · 构建覆盖不同博弈结构的合作决策任务，并改变结构叙述及呈现顺序检验稳定性。
- **Baseline** · 单体安全评测；摘要未列逐项基线。
- **Benchmark** · 1,535 个测试情境、15 种模型；指标为社会有益决策。
- **关键结果 / 消融** · 高风险案例中约 38% 未选社会有益行动；博弈论干预改善最高 18%。
- **适用条件 / 局限** · 情境题的选择不等于长期真实交互行为。

**可复用机制** · 同一安全任务应跨激励结构、顺序和表述测量，避免把提示框定误判为稳定协调能力。

<a id="paper-150944"></a>

## Guaranteed Jailbreaking Defense via Disrupt-and-Rectify Smoothing

[官方论文页](https://neurips.cc/virtual/2026/poster/150944) · [作者来源](https://openreview.net/forum?id=e8vk31VuzR)

- **问题 / 瓶颈** · 仅扰动可能产生分布外提示而降低模型帮助性。
- **核心创新 / 方法** · 将校正阶段插入平滑防御，并分析防护成功概率与扰动强度的约束。
- **Baseline** · 仅扰动的平滑防御；具体对照待核实。
- **Benchmark** · 词元级和提示级威胁下测帮助性与安全性。
- **关键结果 / 消融** · 摘要报告两方面均优于既有防御，并给出概率界。
- **适用条件 / 局限** · 理论保证取决于给定假设及强度，具体条件待核实。

**可复用机制** · 将防御随机化与分布修复分开，以在实现防护的同时减少正常输入失真。

<a id="paper-150883"></a>

## Guaranteed Noisy CP Tensor Recovery via Riemannian Optimization on the Segre Manifold

[官方论文页](https://neurips.cc/virtual/2026/poster/150883) · [作者来源](https://openreview.net/forum?id=ehFJvIafhp)

- **问题 / 瓶颈** · 低 CP 秩张量的可行约束使噪声恢复难直接用欧氏步。
- **核心创新 / 方法** · 利用秩一张量的 Segre 几何构建逐步可行的黎曼梯度与 Gauss-Newton 更新。
- **Baseline** · 两种流形算法互比；其他对照待核实。
- **Benchmark** · 合成噪声线性测量；关注迭代误差与噪声下限。
- **关键结果 / 消融** · 梯度局部线性收敛；Gauss-Newton 先局部二次，近噪声下限转为线性。
- **适用条件 / 局限** · 需要局部收敛区域及适度噪声。

**可复用机制** · 根据距噪声下限的阶段决定二阶更新是否值得，同时利用结构化流形保证可行。

<a id="paper-156668"></a>

## Guaranteed Nonconvex Low-Rank Tensor Estimation via Scaled Gradient Descent

[官方论文页](https://neurips.cc/virtual/2026/poster/156668) · [作者来源](https://neurips.cc/virtual/2026/poster/156668)

- **问题 / 瓶颈** · 缺失与稀疏噪声使普通张量估计迭代在病态条件下低效。
- **核心创新 / 方法** · 在 t-product/t-SVD 下做任务特定谱初始化，再直接缩放更新张量因子。
- **Baseline** · 普通梯度迭代；数值对照名称待核实。
- **Benchmark** · 张量稳健主成分、补全与回归；关注收敛率和单步成本。
- **关键结果 / 消融** · 理论给出不依赖真值条件数的线性收敛，同时维持低单步开销。
- **适用条件 / 局限** · 分析依赖低秩、测量或噪声及初始化条件。

**可复用机制** · 优先在因子空间调整更新尺度，检验是否能消除条件数对迭代速度的影响。

<a id="paper-155025"></a>

## Guarding the Life Code: Preserving Membership Privacy in Genomic Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155025) · [作者来源](https://openreview.net/forum?id=96HcSezVOS)

- **问题 / 瓶颈** · 统一保护可能损失局部特征效用，隐私风险又集中在少量样本及局部。
- **核心创新 / 方法** · 根据局部审计信号定向降低训练泄漏，并对高风险样本使用更强标签平滑。
- **Baseline** · 全局防护与模型无关后处理。
- **Benchmark** · Mistral-DNA、Nucleotide Transformer；训练成员隐私与下游效用。
- **关键结果 / 消融** · 摘要报告隐私改善并维持微调效用。
- **适用条件 / 局限** · 只证实所测试模型及审计设定。

**可复用机制** · 当隐私风险高度不均时分别分配样本级与区域级保护强度。

<a id="paper-152204"></a>

## GUARD: Scalable Gradient-based Unlearning with Adversarial Robustness Defense

[官方论文页](https://neurips.cc/virtual/2026/poster/152204) · [作者来源](https://openreview.net/forum?id=UnifcmHbFu)

- **问题 / 瓶颈** · 只约束干净准确率会损害保留数据上的鲁棒性。
- **核心创新 / 方法** · 用小型鲁棒性见证集提供梯度投影约束和参数重要性信号。
- **Baseline** · 六个遗忘基线与重新训练参照。
- **Benchmark** · 六种设置，比较遗忘效果及保留集鲁棒准确率。
- **关键结果 / 消融** · 鲁棒准确率最高改善到 6.3 倍，接近重训参照。
- **适用条件 / 局限** · 见证集必须反映鲁棒性的关键方向；覆盖条件待核实。

**可复用机制** · 将保留侧鲁棒性作为独立编辑约束，把投影和可编辑参数选择放在同一代理集上。

<a id="paper-152964"></a>

## Guidance For Prior Change via Density Ratio Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/152964) · [作者来源](https://openreview.net/forum?id=P39BOfHJq6)

- **问题 / 瓶颈** · 摊销后验估计器受训练先验绑定；既有引导用高斯近似引入偏差。
- **核心创新 / 方法** · 学习密度比并构造测试时分数引导，避免原有反向核近似。
- **Baseline** · PriorGuide。
- **Benchmark** · 多项基于模拟的推断任务及行星光变曲线；C2ST 和 MMD。
- **关键结果 / 消融** · 多数任务优于 PriorGuide，在训练和目标先验重叠有限的情况下仍较稳健。
- **适用条件 / 局限** · 依赖能估出密度比；无重叠情形待核实。

**可复用机制** · 把先验更新实现为推理时密度比修正，减少每次改先验都重训生成模型的代价。

<a id="paper-153167"></a>

## Guiding Data Allocation for Robust Subpopulation Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/153167) · [作者来源](https://openreview.net/forum?id=NLzY8w4ead)

- **问题 / 瓶颈** · 盲目平衡子群成本高，而且不保证是唯一鲁棒配置。
- **核心创新 / 方法** · 理论比较不同子群配比，并沿鲁棒性改善方向逐步调整比例。
- **Baseline** · 直接将训练数据平衡到各组等量。
- **Benchmark** · 图像和文本基准的受控子群偏移实验；鲁棒表现。
- **关键结果 / 消融** · 存在与平衡相当的不平衡配比；梯度引导能更高效地改善鲁棒性。
- **适用条件 / 局限** · 需定义并识别子群，且能估计配比变化的效益。

**可复用机制** · 先比较边际收益再采购样本，避免把比例均匀当作数据分配的硬约束。

<a id="paper-152866"></a>

## Guiding Visual Autoregressive Models through Spectrum Weakening

[官方论文页](https://neurips.cc/virtual/2026/poster/152866) · [作者来源](https://openreview.net/forum?id=PoNh97Mzdl)

- **问题 / 瓶颈** · 无条件生成常依赖与扩散架构绑定的引导方法。
- **核心创新 / 方法** · 在内部表征通道上选取部分谱分量，并对谱重新归一化后作为弱预测。
- **Baseline** · 分类器自由引导与已有无条件引导；具体基线待核实。
- **Benchmark** · 栅格、随机顺序及逐尺度视觉自回归；离散连续及类别和文本条件。
- **关键结果 / 消融** · 摘要报告无条件质量改善并保持条件对齐，包含消融。
- **适用条件 / 局限** · 依赖可在内部表征安全削弱谱信息；最适频谱选择待核实。

**可复用机制** · 用可控的信息删减构建弱对照，让强弱预测对比在无需额外模型时形成引导。

<a id="paper-139607"></a>

## GUIGuard-Bench:  Toward a General Evaluation for Privacy-Preserving GUI Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139607) · [作者来源](https://openreview.net/forum?id=FnL0OI4r5R)

- **问题 / 瓶颈** · 静态图像隐私数据不能表达不同任务阶段的隐私与效用关系。
- **核心创新 / 方法** · 在真实 GUI 轨迹逐区域标注隐私类别、风险与必要性，拆开隐私识别、规划保真和遮蔽效用评估。
- **Baseline** · 不同保护方式；模型中举例 Claude Sonnet 4.6。
- **Benchmark** · Android 与 PC 的 241 条轨迹和 4,080 张截图。
- **关键结果 / 消融** · 模型易做截图含敏感信息判断，但细粒度定位和必要性判断仍弱；一种模型在 Android 保持了较多规划语义。
- **适用条件 / 局限** · 离线规划保真不等于在线成功，基准规模尚小。

**可复用机制** · 把信息最小化的成本按任务阶段量化，区别能遮掉的内容和完成任务所需内容。

<a id="paper-153725"></a>

## GUI-Libra: Data-Efficient Post-Training for Reliable Reasoning-and-Acting in Native GUI Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153725) · [作者来源](https://openreview.net/forum?id=JFNpUWpOmR)

- **问题 / 瓶颈** · 长推理监督可能损害定位，单示范会把其他有效动作当错。
- **核心创新 / 方法** · 混合推理后动作与直接动作监督并重加权动作词元；用有成功自适应缩放的 KL 约束强化后训练。
- **Baseline** · 4B 和 8B 基础模型；通用监督和离线优化方案。
- **Benchmark** · AndroidWorld、Online-Mind2Web、WebArena-Lite-v2；步准确率和任务完成。
- **关键结果 / 消融** · 两模型相对基础版在三个基准均提升；AndroidWorld 报告 +15.6% 和 +12.2%。
- **适用条件 / 局限** · 在线增益依赖 GUI 任务与奖励可验证性，其他环境待核实。

**可复用机制** · 在部分可验证的动作空间保留简洁动作训练信号，并控制离线奖励塑造强度。

<a id="paper-139804"></a>

## GUITAR: Structured Failure Diagnosis of GUI Agents via State Transitions

[官方论文页](https://neurips.cc/virtual/2026/poster/139804) · [作者来源](https://openreview.net/forum?id=3bg3fAhQJU)

- **问题 / 瓶颈** · 按步准确率无法归并等价界面，也会掩盖罕见关键环节。
- **核心创新 / 方法** · 构建功能状态转移图，统计状态和边的失败集中度，再用于瓶颈状态的推理指导。
- **Baseline** · 逐步准确率式评估。
- **Benchmark** · AndroidControl 和 Mind2Web 各三个任务；八个代理。
- **关键结果 / 消融** · 61.9% 的失败集中于 20% 的状态；基于瓶颈指导报告提升 2.8%。
- **适用条件 / 局限** · 依赖功能等价映射的质量，未必覆盖其他 GUI。

**可复用机制** · 用稳定功能状态而非像素变化做聚合单位，优先改善承载大量错误的转移。

<a id="paper-150279"></a>

## Gumbo: Gumbel Optimized High-Temperature Speculative Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/150279) · [作者来源](https://openreview.net/forum?id=jLWQiUQcDp)

- **问题 / 瓶颈** · 高温下贪心草案接受率低，直接引入非零温动态草案树会改变分布。
- **核心创新 / 方法** · 推广多草案耦合，按 Gumbel 分数扩展与重排动态树，验证无需草案分布。
- **Baseline** · EAGLE-3 推测采样器。
- **Benchmark** · 四种模型、五个数据集；接受长度和推理加速。
- **关键结果 / 消融** · 时间复杂度线性于词表；温度 1.0 时加速改善最高 26.7%。
- **适用条件 / 局限** · 依赖目标分布的验证机制，实际收益随温度和模型变化。

**可复用机制** · 将草案生成与正确性验证解耦，让候选更符合高温采样而保持目标分布。

<a id="paper-148930"></a>

## GVCC: Zero-Shot Video Compression via Codebook-Driven Stochastic Rectified Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/148930) · [作者来源](https://openreview.net/forum?id=uATPoYzBvE)

- **问题 / 瓶颈** · 确定性流采样没有逐步随机信道，极低码率的均值回归易过平滑。
- **核心创新 / 方法** · 将流采样转换为保持边缘分布的随机过程，传递量化的逐步创新量。
- **Baseline** · DCVC-RT 等视频压缩方法。
- **Benchmark** · UVG 三档码率最低约 0.003 bpp；LPIPS。
- **关键结果 / 消融** · 同码率相对 DCVC-RT 的 LPIPS 降低 65%。
- **适用条件 / 局限** · 感知保真不保证逐帧像素精确；依赖视频生成解码成本。

**可复用机制** · 传输对生成轨迹影响最大的随机增量，在极窄信道下恢复可接受的后验样本。

<a id="paper-149833"></a>

## GWScore: A structural diversity metric for consistent text-to-image generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149833) · [作者来源](https://openreview.net/forum?id=mxFOuNzT3H)

- **问题 / 瓶颈** · DreamSim 等相似度容易将姿态变化混同于身份变化。
- **核心创新 / 方法** · 用 Gromov-Wasserstein 距离比较生成图像的关系结构，量化布局与姿态多样性。
- **Baseline** · DreamSim 等身份一致性指标。
- **Benchmark** · 视觉叙事和主体一致生成方法；另测潜变量初始化对多样性的影响。
- **关键结果 / 消融** · 摘要确认可单独考察结构多样性，数值结果待核实。
- **适用条件 / 局限** · 依赖结构描述的稳定性，指标与人工判断的一致性待核实。

**可复用机制** · 把相对结构匹配用于多样性评价，与身份相似度形成两条独立的诊断轴。

<a id="paper-152249"></a>

## G-Zero: Self-Play for Open-Ended Generation from Zero Data

[官方论文页](https://neurips.cc/virtual/2026/poster/152249) · [作者来源](https://openreview.net/forum?id=USnGWfYVux)

- **问题 / 瓶颈** · 外部模型代理评分可能封顶或被钻空子。
- **核心创新 / 方法** · Hint-δ 衡量有无自生成提示的预测变化；出题者用 GRPO 寻找盲点，生成者用 DPO 吸收提示收益。
- **Baseline** · 以外部模型判断的自博弈为参照，具名对照待核实。
- **Benchmark** · 开放生成，具名任务和指标待核实。
- **关键结果 / 消融** · 理想化标准 DPO 版本有最佳迭代次优界，摘要未给出实测结果。
- **适用条件 / 局限** · 理论要求探索覆盖和低伪标签噪声，预测变化是否等同于任务质量待验证。

**可复用机制** · 将同一生成器的提示前后分布差异作为可测信号，并独立验证它与人工质量判断的关联。

<a id="paper-155050"></a>

## H2G: Hierarchy-Aware Hyperbolic Grouping for 3D Scenes

[官方论文页](https://neurips.cc/virtual/2026/poster/155050) · [作者来源](https://openreview.net/forum?id=8pIDwVyuXe)

- **问题 / 瓶颈** · 二维模型相似度缺乏可直接用于三维分组的层级监督。
- **核心创新 / 方法** · 以 Dasgupta 聚类目标构建树，再向 Lorentz 特征场蒸馏细层分配、粗层结构和最近公共祖先顺序。
- **Baseline** · 二维基础模型亲和度充当监督来源；具名对照待核实。
- **Benchmark** · 无标签三维场景分组，数据与指标待核实。
- **关键结果 / 消融** · 摘要给出建模能力，未给出定量结果。
- **适用条件 / 局限** · 依赖二维亲和度能支持合理聚类树，遮挡和噪声时的退化待核实。

**可复用机制** · 把语义亲和度转换成相对祖先次序来监督多粒度空间分组。

<a id="paper-139828"></a>

## HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/139828) · [作者来源](https://openreview.net/forum?id=2MmzwEyeO2)

- **问题 / 瓶颈** · 仅机器人在场的数据不覆盖同步、让行和手势指令。
- **核心创新 / 方法** · 按任务关系组织人类在场示范，让不同角色对应可评估的行为。
- **Baseline** · 仅机器人在场的数据。
- **Benchmark** · 48 项任务，7,000 余条示范、100 小时以上，关注同步、让行、手势落地和适配。
- **关键结果 / 消融** · 仅靠机器人数据未出现相关行为，人类在场训练展示了上述行为及对新任务的适配。
- **适用条件 / 局限** · 真实人群和场地的覆盖及定量结果待核实。

**可复用机制** · 把互动角色当作数据覆盖轴，避免仅统计任务或轨迹数量。

<a id="paper-148236"></a>

## HACO: Hedged Agent Computing for Reliable LLM Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/148236) · [作者来源](https://openreview.net/forum?id=zNkQ67Ps8c)

- **问题 / 瓶颈** · 固定角色分配忽略服务区域、网络与实例质量变化。
- **核心创新 / 方法** · 基于质量、可靠性与不确定性排序候选，累积估计可靠性至阈值，利用运行轨迹更新实例画像。
- **Baseline** · 固定角色绑定范式、穷举并行。
- **Benchmark** · 多个基准及运行环境降级实验，关注鲁棒性、质量、token 和延迟。
- **关键结果 / 消融** · 报告比穷举并行成本更低，并在变化条件下改善鲁棒性及质量。
- **适用条件 / 局限** · 相关故障下的可靠性估计方式待查。

**可复用机制** · 以调用成功率作为停止扩张并发候选的条件，避免始终固定开同样数量的副本。

<a id="paper-152185"></a>

## Hadamard Representation: Scaffolding Performance Across Model-free RL

[官方论文页](https://neurips.cc/virtual/2026/poster/152185) · [作者来源](https://openreview.net/forum?id=Uw6XLONJCr)

- **问题 / 瓶颈** · RL 学习中神经元休眠且存活特征冗余，饱和 tanh 还改变下游偏置。
- **核心创新 / 方法** · 每个隐藏层使用两个独立参数化输出的逐元素乘积。
- **Baseline** · DQN、PPO、PQN、SimbaV2、MR.Q 的现有实现及等参数宽层。
- **Benchmark** · 像素 Atari、状态连续控制及视觉连续控制。
- **关键结果 / 消融** · 五种算法中报告无须重新扫参便获改善，等参数增宽后优势仍在。
- **适用条件 / 局限** · 适用层位置、不同激活和计算开销待核实。

**可复用机制** · 把乘法交互与参数量分开消融，并同步跟踪休眠率和有效秩。

<a id="paper-152516"></a>

## HAI: Hierarchical Anchored Interaction for Multi-View Bimanual World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152516) · [作者来源](https://openreview.net/forum?id=SXueAPIsi0)

- **问题 / 瓶颈** · 统一动作条件导致预测错臂、场景漂移以及全局与腕部视图不一致。
- **核心创新 / 方法** · 按视角路由双臂动作块，先加块级意图并建模多视角，再注入逐帧动作，将动态特征与视角锚融合。
- **Baseline** · 双臂世界模型基线，具名实现待核实。
- **Benchmark** · AgiBot、DROID 的长视距预测及下游 VLA 成功率。
- **关键结果 / 消融** · 作者报告场景稳定、腕视图可控、视图一致性消融改善；下游成功率平均相对提升 67.2%。
- **适用条件 / 局限** · 实验针对双臂多视角，绝对成功率及其他构型待核实。

**可复用机制** · 把粗时标全局动作条件、细时标局部控制和静态场景记忆分开设计与消融。

<a id="paper-154568"></a>

## Half-Truths Break Similarity-Based Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/154568) · [作者来源](https://openreview.net/forum?id=Cdi1G7I9ds)

- **问题 / 瓶颈** · 正确描述附加错误关系后，双编码器反而可能给更高分。
- **核心创新 / 方法** · 将句子拆成实体和关系，对每个组成单元构造最小编辑反例并训练排序，保留检索实现。
- **Baseline** · 标准 CLIP 双编码器。
- **Benchmark** · 经核验 COCO 的半真例及常见组合基准，指标为偏好正确描述的比例和组合表现。
- **关键结果 / 消融** · 标准 CLIP 偏好正确描述 41.0%，关系子集 28.2%；CS-CLIP 半真例准确率 78.2%，组合基准平均提升 5.7 点。
- **适用条件 / 局限** · 对多种细节同时错配或不同语言的效果待核实。

**可复用机制** · 通过仅改一个局部概念的对照确认模型分数是否确实响应关系正确性。

<a id="paper-154310"></a>

## Hallucination as Commitment Failure: Larger LLMs Misfire Despite Knowing the Answer

[官方论文页](https://neurips.cc/virtual/2026/poster/154310) · [作者来源](https://openreview.net/forum?id=EcJCjzBU18)

- **问题 / 瓶颈** · 单个答案字符串概率可能低估模型对正确概念的支持。
- **核心创新 / 方法** · 在答案承诺时刻合并同义变体，并比较语义支持相匹配的正确与错误输出。
- **Baseline** · Qwen、Llama 的基础版与指令版，0.8B 至 72B。
- **Benchmark** · 跨规模生成幻觉，指标含正确概念支持、同义形式分布集中和多词生成诊断。
- **关键结果 / 消融** · 报告 16–47% 的指令模型幻觉已有较多正确概念概率，该比例随规模升高。
- **适用条件 / 局限** · 同义变体识别方法及适用任务待核实，摘要未验证具体纠正策略。

**可复用机制** · 区分模型没有正确概念和正确概念的质量分散在表达候选中，避免用同一种修复处理两类失败。

<a id="paper-155605"></a>

## Hallucination in World Models is Predictable and Preventable

[官方论文页](https://neurips.cc/virtual/2026/poster/155605) · [作者来源](https://openreview.net/forum?id=4KT2peVuUl)

- **问题 / 瓶颈** · 画面流畅的预测也可能偏离真实动作条件动力学。
- **核心创新 / 方法** · 分感知、动作边缘化和场景发散三个失效阶段建预测信号，用覆盖感知采样和以失效为好奇奖励的采集微调。
- **Baseline** · 标准采样或探索的具体对照待核实。
- **Benchmark** · MMBench2，427 小时、210 任务，带动作、奖励和实时仿真器；测失效预测和新环境适配。
- **关键结果 / 消融** · 报告三个信号可预测失效，最少 50 条环境轨迹可适配未见环境。
- **适用条件 / 局限** · 信号是否有效依赖训练覆盖和可观测性，最低轨迹数来自所测设置。

**可复用机制** · 采集策略复用同一套失效检测信号，并按失效阶段记录补采收益。

<a id="paper-139204"></a>

## HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139204) · [作者来源](https://openreview.net/forum?id=ejdHPDvwXJ)

- **问题 / 瓶颈** · 摘要、问答和 Agent 的幻觉定义不一致，难以跨任务对照。
- **核心创新 / 方法** · 在显式参考世界内按可观测声明的真假自动标注，并控制观测视图、时序及来源冲突规则。
- **Baseline** · 前沿与开放权重模型，比较扩展思考设置。
- **Benchmark** · 网格世界、国际象棋和终端任务，测直接感知、多步追踪、前向模拟和拒答等。
- **关键结果 / 消融** · 所测前沿模型在直接感知错误上较少，多步追踪和前向模拟仍困难，延长思考未普遍解决。
- **适用条件 / 局限** · 合成和半合成任务结论能否覆盖真实开放世界待核实。

**可复用机制** · 以能控制事实生成和观测权限的环境分解错误来源，检验缓解是否只影响某种错误。

<a id="paper-153080"></a>

## HALMES: Knowing When to Intervene in LVLM Hallucination Mitigation

[官方论文页](https://neurips.cc/virtual/2026/poster/153080) · [作者来源](https://openreview.net/forum?id=O8ShETkdl7)

- **问题 / 瓶颈** · 每步都校正可能破坏已经正确的生成。
- **核心创新 / 方法** · 从内部注意力识别幻觉前兆片段，仅对高风险片段触发原有对比解码。
- **Baseline** · 多个全阶段对比解码方法。
- **Benchmark** · 多种视觉语言模型与多个基准，检测幻觉改善及对正确输出的干扰。
- **关键结果 / 消融** · 摘要报告减少幻觉且减轻全阶段干预对正常输出的副作用，具体幅度待核实。
- **适用条件 / 局限** · 依赖能够读取注意力，跨模型门槛可迁移性待核实。

**可复用机制** · 把纠正器和触发策略分离，对比全程开启及按需开启，记录漏纠与误扰动。

<a id="paper-154108"></a>

## HALO: Heterogeneous-Aware LoRA Optimization via Rank Allocation and Client-Aware Projection

[官方论文页](https://neurips.cc/virtual/2026/poster/154108) · [作者来源](https://openreview.net/forum?id=GCoRDt8PdU)

- **问题 / 瓶颈** · 统一秩浪费资源，统一截断可能丢掉与本地损失有关的方向。
- **核心创新 / 方法** · 在 NTK 条件下导出秩充分条件，把乘积聚合参考投影到各客户端诱导子空间后重分解。
- **Baseline** · 同秩与异秩联邦 LoRA，朴素和 SVD 截断。
- **Benchmark** · 联邦微调实验，数据、网络和指标待核实。
- **关键结果 / 消融** · 摘要报告改善稳定性及性能，NTK 近似下控制截断残差且无额外通信。
- **适用条件 / 局限** · 理论依赖 NTK 近似，子空间计算成本和偏离近似后的影响待核实。

**可复用机制** · 聚合后按客户端更新目标重分配低秩子空间，并用本地截断残差衡量聚合损失。

<a id="paper-148613"></a>

## HALO-VGGT: Heterogeneity-Aware Lightweight Online Compression Allocator for Efficient VGGT

[官方论文页](https://neurips.cc/virtual/2026/poster/148613) · [作者来源](https://openreview.net/forum?id=wSMK90Tr3q)

- **问题 / 瓶颈** · 统一压缩率忽略注意力层、头以及输入间的敏感性差异。
- **核心创新 / 方法** · 采样查询键间隔作为敏感性代理，用分层配额调节既有剪枝、合并或稀疏化。
- **Baseline** · 统一配额或离线校准，以及已有合并和稀疏注意力。
- **Benchmark** · 多个数据集和骨干，衡量重建精度、速度。
- **关键结果 / 消融** · 摘要报告最高 4.20 倍加速，相较既有合并与稀疏方法最高额外 1.46 倍。
- **适用条件 / 局限** · 速度依赖视图规模和硬件，代理的额外开销待核实。

**可复用机制** · 复用既有压缩算子，只改预算分配并检验每个输入能否用更低成本守住质量。

<a id="paper-155955"></a>

## Halt Fast! Early Stopping for Certified Robustness

[官方论文页](https://neurips.cc/virtual/2026/poster/155955) · [作者来源](https://openreview.net/forum?id=1Zs088RXoL)

- **问题 / 瓶颈** · 一次性固定评测次数会浪费容易样本的推理预算。
- **核心创新 / 方法** · 元学习器提供图像特定先验，序贯 E 过程允许按风险门槛提前停止。
- **Baseline** · 固定样本量随机平滑认证。
- **Benchmark** · 图像鲁棒性认证，关注采样量与认证表现，具名设置待核实。
- **关键结果 / 消融** · 作者报告采样量减少约 20 倍且认证表现接近，保留统计保证。
- **适用条件 / 局限** · 有效性取决于构造有效的序贯过程，数据与威胁设定待核实。

**可复用机制** · 先用轻量预测估计难度，再以有效检验判定是否停止，避免用难度预测直接替代认证。

<a id="paper-151714"></a>

## HaM-World: Soft-Hamiltonian World Models with Selective Memory for Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/151714) · [作者来源](https://openreview.net/forum?id=Yc0mqMHlkt)

- **问题 / 瓶颈** · 长时想象滚动或分布偏移时潜动态不稳定。
- **核心创新 / 方法** · 将潜变量拆成正则坐标与上下文，接入 Mamba 历史；动力学将能量导出的向量场与可学残差及控制项组合。
- **Baseline** · 强世界模型基线，摘要未列名。
- **Benchmark** · 四项 DeepMind Control Suite 任务，AUC、滚动 MSE、12 种分布外扰动下回报及能量诊断。
- **关键结果 / 消融** · 平均 AUC 高 9.5%，长时滚动误差降至对照的 45%，12 个滚动指标领先 11 个。
- **适用条件 / 局限** · 摘要仅给出四个仿真任务，真实系统及非近似保守任务待核。

**可复用机制** · 用无控制时能量漂移和有控制时的能量变化区分结构先验与预测性能。

<a id="paper-149700"></a>

## HaNDF: Object-Conditioned Geometric Neural Hand Distance Fields

[官方论文页](https://neurips.cc/virtual/2026/poster/149700) · [作者来源](https://openreview.net/forum?id=o6Ags8RThf)

- **问题 / 瓶颈** · 无条件姿态先验难保留手与物体的相关构型。
- **核心创新 / 方法** · 在关节积流形上学习以物体为条件的距离场，将姿态投影到其零等值集；还可反向估计物体条件。
- **Baseline** · 无条件生成先验为背景；实验基线未列。
- **Benchmark** · 姿态细化、遮挡重建和交互合成；数据集和指标待核。
- **关键结果 / 消融** · 摘要报告先验适用于上述任务，未给数值。
- **适用条件 / 局限** · 需要可学习的交互构型与物体条件；接触真实性边界待核。

**可复用机制** · 显式建模条件可行集，使同一先验既能生成也能修正姿态。

<a id="paper-139358"></a>

## Handwriting decoding as a challenging motor task for EEG Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139358) · [作者来源](https://openreview.net/forum?id=UmBkSWTw9t)

- **问题 / 瓶颈** · 运动起点信息可能泄漏并高估手写解码能力。
- **核心创新 / 方法** · 用四字母解码比较有无已知运动起点，分别改变测试信号质量和训练样本量并对照专用模型。
- **Baseline** · 通用 EEG 基础模型与小型专用模型。
- **Benchmark** · 新手写 EEG 四字母分类，跨被试平均准确率和个体表现。
- **关键结果 / 消融** · 去掉起点信息后均值 41.3% 降至 32.4%；提升信号质量时最佳被试 45% 升至 78%；通用模型未领先专用模型。
- **适用条件 / 局限** · 结果限于这一手写设置，最佳个体收益不能外推到全体。

**可复用机制** · 将训练数据扩量与采集质量干预分开做，在线协议不允许使用不可用的事件时间。

<a id="paper-153384"></a>

## Handwritten Text Recognition Lives in the High-Pixel Variance Subspace

[官方论文页](https://neurips.cc/virtual/2026/poster/153384) · [作者来源](https://openreview.net/forum?id=LmcUzl4xPg)

- **问题 / 瓶颈** · 自然图像分类上的重建经验与手写识别相反。
- **核心创新 / 方法** · 投影输入并检查高低方差子空间的判别信号；匹配六种方法的编码器、数据和评测协议。
- **Baseline** · 像素 MIM、JEPA 式、图图和图文对比方法，以及全量微调监督对照。
- **Benchmark** · 五语种六个手写基准，字符错误率及位置探针。
- **关键结果 / 消融** · 像素方法在各基准和探针最优；编码器与高方差子空间的对齐在各方法内能预测错误率。
- **适用条件 / 局限** · 规律依赖判别信息位置，跨成像过程需重测。

**可复用机制** · 用子空间探针先验证重建保留的是任务信号还是无关细节。

<a id="paper-154482"></a>

## HAPS: Hierarchical LLM Routing with Joint Architecture and Parameter Search

[官方论文页](https://neurips.cc/virtual/2026/poster/154482) · [作者来源](https://openreview.net/forum?id=DFgCnynDxC)

- **问题 / 瓶颈** · 只选固定模型无法利用参数适配。
- **核心创新 / 方法** · 上层选架构，下层生成条件 LoRA，以共享参数生成器耦合两级并用奖励增强目标训练。
- **Baseline** · 强模型路由基线，名称待核。
- **Benchmark** · 多任务路由与共享、架构、效率消融，基准和指标待核。
- **关键结果 / 消融** · 摘要称持续超过路由基线；共享贡献需看消融数据。
- **适用条件 / 局限** · 需要能接入候选模型适配层，调用封闭接口的情形待核。

**可复用机制** · 在同成本下对比仅路由、仅动态适配及两级联合更新。

<a id="paper-150177"></a>

## HARC: Coupling Harmfulness and Refusal Capabilities for Robust Safety Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/150177) · [作者来源](https://openreview.net/forum?id=k78i4RMHGi)

- **问题 / 瓶颈** · 只在提示位置检查安全信号会漏掉生成时才显现的风险识别。
- **核心创新 / 方法** · 在残差流的安全相关子空间联合调整有害性识别与拒答表征，覆盖提示与答复位置。
- **Baseline** · 六种训练时与推理时安全基线。
- **Benchmark** · 五个模型家族、两种规模，对照稳健性、能力和过度拒答。
- **关键结果 / 消融** · 摘要称折中表现最佳且未增加过度拒答，数字待核。
- **适用条件 / 局限** · 迁移与能力保持结论限于所测模型和任务。

**可复用机制** · 对安全对齐同时验证输入判定与生成期间的响应，并用正常请求测误拒。

<a id="paper-148913"></a>

## Hard Attention Transformers and BSS-Machines

[官方论文页](https://neurips.cc/virtual/2026/poster/148913) · [作者来源](https://openreview.net/forum?id=uF9Zr3T0p8)

- **问题 / 瓶颈** · 逐步不离散化的递归 Transformer 缺少清楚的代数计算刻画。
- **核心创新 / 方法** · 在整数的有序环扩张上，将硬注意力递归模型分别与 BSS 机器及二次分支线性 BSS 机器建立等价。
- **Baseline** · 通用 BSS 计算模型及线性受限版本。
- **Benchmark** · 理论证明；无经验基准。
- **关键结果 / 消融** · 电路激活对应一般 BSS，换前馈网络则对应带二次分支的线性模型。
- **适用条件 / 局限** · 结论基于硬注意力、特定算术域和无逐步离散化定义。

**可复用机制** · 比较连续算法模拟能力时控制激活类型和数值域，避免将不同计算模型混为一谈。

<a id="paper-151167"></a>

## Harder the Task, Sparser the Representation: Sparsity as a Learning Signature of Capability in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151167) · [作者来源](https://openreview.net/forum?id=cXF3Nd4vQs)

- **问题 / 瓶颈** · 模型内部何时以集中方式表示陌生问题尚不清楚。
- **核心创新 / 方法** · 分析难度分组下末层隐藏态稀疏度，以及其随学习熟悉度变化；SG-ICL 据此检索示例。
- **Baseline** · 标准 CoT、Auto-CoT。
- **Benchmark** · 跨模型和领域的难度统计及 MATH-500。
- **关键结果 / 消融** · 难度升高对应数据集层面更稀疏的末层表示；SG-ICL 优于对照。
- **适用条件 / 局限** · 摘要明确趋势在单样本上可能不明显；泛化需校准。

**可复用机制** · 先分难度桶检验稀疏度校准，再判断它能否改善示例选择。

<a id="paper-155635"></a>

## Hardware-Friendly Token-Group Activation Quantization for Low-Bit Mamba Super-Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/155635) · [作者来源](https://openreview.net/forum?id=46hNfjRw3m)

- **问题 / 瓶颈** · 选择性扫描让空间 token 的最佳裁剪范围不同，运行时扫描后再分组不利于部署。
- **核心创新 / 方法** · 离线按扫描后舍入裁剪描述聚类，训练扫描前分组预测器，在线查裁剪边界；校准增加傅里叶幅相保真。
- **Baseline** · Mamba 和超分辨率后训练量化基线，速度对照 FP16。
- **Benchmark** · 跨位宽、骨干、超分辨率任务和 PTQ 协议；Jetson Orin Nano 延迟。
- **关键结果 / 消融** · 摘要称质量一致提高，设备速度为 FP16 的 2.23 倍。
- **适用条件 / 局限** · 预分组能否覆盖校准之外的新输入待核。

**可复用机制** · 用离线分组上界和运行前可用特征训练裁剪预测器，分开测质量与端侧延迟。

<a id="paper-153984"></a>

## Harmless in Pieces, Harmful in Motion: Detecting Multi-Agent Jailbreaks

[官方论文页](https://neurips.cc/virtual/2026/poster/153984) · [作者来源](https://openreview.net/forum?id=H4BgVHh3ID)

- **问题 / 瓶颈** · 只看单个请求或对话可能漏掉跨节点累积的整体风险。
- **核心创新 / 方法** · CITADEL 对智能体、工具和记忆维护运行状态，综合安全类别相似性、跨节点活动与时间变化发出监测信号。
- **Baseline** · 单智能体检测、轨迹监控及架构级防护。
- **Benchmark** · MA-SafeBench 及三个外部安全评测；误报率与监测耗时。
- **关键结果 / 消融** · 摘要报告误报率 2.1%、每事件额外耗时 28 毫秒，并报告安全评测风险下降。
- **适用条件 / 局限** · 依赖运行事件可观测及固定安全类别；实际部署阈值需复验。

**可复用机制** · 在测试中同时记录节点级和系统级告警，测额外覆盖、误报与耗时。

<a id="paper-153661"></a>

## Harmonic Torsional Diffusion for Flexible Protein-Ligand Docking

[官方论文页](https://neurips.cc/virtual/2026/poster/153661) · [作者来源](https://openreview.net/forum?id=JgekVKyVaW)

- **问题 / 瓶颈** · 直接用欧式表示容易忽略角度首尾等价。
- **核心创新 / 方法** · 作者在通用建模层面引入谐波表示以使生成更新符合周期状态空间。
- **Baseline** · 常规欧式角度处理是方法对照，具体基线待核。
- **Benchmark** · 论文以结构预测 benchmark 测几何精度和输出有效性。
- **关键结果 / 消融** · 摘要报告相对近期方法精度与有效性提高，无量化结果。
- **适用条件 / 局限** · 实验在专门结构任务上，跨领域迁移待验证。

**可复用机制** · 在非生物周期状态建模中与普通欧式头对比，单列角度接缝误差。

<a id="paper-155727"></a>

## HARMONY: Hierarchical Anchor Retrieval on Manifold for Oblivious-source Acoustic Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/155727) · [作者来源](https://openreview.net/forum?id=3OMsg8le1w)

- **问题 / 瓶颈** · 冻结特征把不同机器的正常分布混在一起，降低检索和评分可靠性。
- **核心创新 / 方法** · 用锚点把混合特征重分为紧凑 Voronoi 区域，并做分层检索。
- **Baseline** · 最强统一基线、基础特征基线和穷举检索。
- **Benchmark** · DCASE 2020、MIMII，平均 AUC 和单 CPU 检索速度。
- **关键结果 / 消融** · AUC 从 75.40% 到 90.00%；相对穷举检索快 7.8 倍、AUC 仅降 0.20%。
- **适用条件 / 局限** · 未知来源须在特征中保留可分结构，分布变化下待核。

**可复用机制** · 测试同一分区能否同时减少源混杂和检索计算，并单列增益。

<a id="paper-149186"></a>

## Harnessing Accurate and Automatic Trend Detection in Data Streams via Tbps-Level Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/149186) · [作者来源](https://openreview.net/forum?id=sFWnDg3gcY)

- **问题 / 瓶颈** · 手调参数联动且布隆过滤误报挤占检测资源。
- **核心创新 / 方法** · 用二值循环模型做趋势预筛，其置信度用于自动更新增长与衰减阈值。
- **Baseline** · 现有趋势检测和布隆过滤；具体名称未列。
- **Benchmark** · 真实数据流，误报、有效占用、F1 和线速。
- **关键结果 / 消融** · 误报减少 23%–44%，占用 47% 增至 70%，F1 提高 35%–68%。
- **适用条件 / 局限** · 结果针对测试数据流与设备，分布漂移适应性需核。

**可复用机制** · 测学习预筛对下游有效槽位的影响，并用固定阈值比较置信度反馈的贡献。

<a id="paper-156126"></a>

## Harnessing Agentic Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/156126) · [作者来源](https://openreview.net/forum?id=0CYtIw96St)

- **问题 / 瓶颈** · 固定搜索流程僵化，自由上下文迭代又容易漂移。
- **核心创新 / 方法** · 将累积候选和评估整理为过程状态，由上层调整后续搜索机制。
- **Baseline** · 五个演化基线；开放优化另与四个基线比较。
- **Benchmark** · 各推理及开放优化任务，在相同迭代预算下比较表现。
- **关键结果 / 消融** · 摘要报告比最强基线相对提升 26%；三个开放优化任务下领先对照。
- **适用条件 / 局限** · 具体任务和指标待全文核实；结论记录限良性研究任务。

**可复用机制** · 在良性合成优化中分离候选评分与搜索策略选择，用相同预算测上层调整的贡献。

<a id="paper-151645"></a>

## Harnessing Data Asymmetry in Manifold Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151645) · [作者来源](https://openreview.net/forum?id=Z4eWOG1BJ5)

- **问题 / 瓶颈** · 传统流形学习把不均匀采样带来的方向性差异对称化。
- **核心创新 / 方法** · 构造非对称差异并在 Finsler 空间嵌入，给出 Finsler t-SNE、Finsler UMAP。
- **Baseline** · 对称欧氏嵌入与既有非对称嵌入路线。
- **Benchmark** · 受控合成与大型真实数据，比较嵌入质量并检查密度层级。
- **关键结果 / 消融** · 摘要报告恢复传统流程遗漏的密度层级，嵌入质量更高。
- **适用条件 / 局限** · 方向性由选定差异度构造；质量指标与计算成本待核。

**可复用机制** · 先用具有已知密度层级的合成样本校准，再比较同一算法的对称与非对称差异。

<a id="paper-151124"></a>

## Harnessing Image Diffusion Prior for Photo-Realistic Video Restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/151124) · [作者来源](https://openreview.net/forum?id=conEYoQsmd)

- **问题 / 瓶颈** · 逐帧调用图像生成先验易产生纹理闪烁。
- **核心创新 / 方法** · 重新平衡噪声频带并沿运动对齐噪声，辅以自监督去噪编码器和解耦时间注意力。
- **Baseline** · 既有视频修复方法，名称待核实。
- **Benchmark** · 视频修复的感知质量、细节和时间一致性；数据集待核实。
- **关键结果 / 消融** · 摘要报告三方面均改善；组件级增益待核实。
- **适用条件 / 局限** · 依赖可靠运动估计，遮挡时的表现待核实。

**可复用机制** · 让随机潜变量随物体运动共享，比事后抑制所有随机细节更有针对性。

<a id="paper-155291"></a>

## Harnessing Textual Refusal Directions for Multimodal Safety

[官方论文页](https://neurips.cc/virtual/2026/poster/155291) · [作者来源](https://openreview.net/forum?id=6fF1hshpKK)

- **问题 / 瓶颈** · 直接把单模态拒答干预用于视觉输入可能增加误拒。
- **核心创新 / 方法** · 激活重定中心并在几何信赖域内自适应缩放，在首个生成位置选择干预层。
- **Baseline** · 文本拒答方向的直接迁移与既有对齐路线。
- **Benchmark** · 五个多模态模型；安全、效用及视频安全评测。
- **关键结果 / 消融** · 摘要报告持续提升安全性并保留效用。
- **适用条件 / 局限** · 依赖层选择、模态对齐和方向估计。

**可复用机制** · 先消除模态间表示偏移，再按可信范围施加共享的安全控制。

<a id="paper-138958"></a>

## Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/138958) · [作者来源](https://openreview.net/forum?id=tyh2XeFgOJ)

- **问题 / 瓶颈** · 统一记忆评测难回答具体任务该用何种记忆。
- **核心创新 / 方法** · 固定交互框架比较多类记忆后端，统一记录性能和效率。
- **Baseline** · 稠密、稀疏、结构化、层次、参数化等记忆。
- **Benchmark** · 三种骨干、四套问答和决策基准、26 个指标。
- **关键结果 / 消融** · 广泛检索帮助事实问答，但可能干扰序贯决策；长历史改变成本排序。
- **适用条件 / 局限** · 结论受共同框架、所测任务和后端实现影响。

**可复用机制** · 记忆检索覆盖度应由当前目标决定，并在不同历史长度上监控动作相关上下文的挤占。

<a id="paper-150693"></a>

## HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/150693) · [作者来源](https://openreview.net/forum?id=gDV5BRXpfO)

- **问题 / 瓶颈** · 画像信号只进入容量有限的重排提示，物品侧缺画像。
- **核心创新 / 方法** · 规则生成物品画像，在召回中使用分通道同质性，并用评论器门控单次画像更新。
- **Baseline** · 最强已发表推荐基线；具体名称待核实。
- **Benchmark** · Yelp、Amazon Books、MovieTV、Goodreads 的 Hit@1。
- **关键结果 / 消融** · 提升 6.9% 至 24.0%；摘要报告各组件消融贡献。
- **适用条件 / 局限** · 需要可提取可比较画像，反思更新有额外代价。

**可复用机制** · 将稳定双侧画像编码为召回信号，只把有增量价值的画像反思留给推理。

<a id="paper-155018"></a>

## Hawkeye: Hardware-Aware GPU Kernel Optimization with Minimal Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/155018) · [作者来源](https://openreview.net/forum?id=99gxreT4sW)

- **问题 / 瓶颈** · 逐工作负载给编码代理提供硬件优化示范，成本随平台和内核增长。
- **核心创新 / 方法** · 用硬件特性分类，每个平台每种策略写一项单元测试，作为内核生成时的反馈。
- **Baseline** · 专家 PyTorch、Triton 内核。
- **Benchmark** · Ampere、Hopper、Blackwell、MI350；多种低精度内核性能。
- **关键结果 / 消融** · 摘要报告每架构十个测试，生成内核达到或超过部分专家实现。
- **适用条件 / 局限** · 依赖测试覆盖硬件特性，对未覆盖策略的外推待核实。

**可复用机制** · 把监督从整段内核移到可组合硬件优化的验证规则，跨工作负载复用。

<a id="paper-151377"></a>

## HCInfer: An Efficient Inference System via Heterogeneous Error Compensation for Resource-Constrained Devices

[官方论文页](https://neurips.cc/virtual/2026/poster/151377) · [作者来源](https://openreview.net/forum?id=b3DYZ9pfMj)

- **问题 / 瓶颈** · 压缩牺牲准确度，整体卸载又可能降低吞吐。
- **核心创新 / 方法** · GPU 执行压缩主干，CPU 异步执行残差补偿，并按敏感性分配秩。
- **Baseline** · 压缩模型与全精度模型。
- **Benchmark** · 资源受限设备上的下游准确率和推理速度；具体硬件待核实。
- **关键结果 / 消融** · 相对压缩模型最高改善 5.2%，相对全精度最高加速 10.4 倍。
- **适用条件 / 局限** · 需补偿分支访问稀疏，异步管线能覆盖通信开销。

**可复用机制** · 按访问稀疏性而非只按参数量划分压缩组件的设备放置。

<a id="paper-156745"></a>

## HDCS: Hierarchy Discovery and Critic Shaping for Reinforcement Learning with Automaton Specification

[官方论文页](https://neurips.cc/virtual/2026/poster/156745) · [作者来源](https://openreview.net/forum?id=BGoRme2MfG)

- **问题 / 瓶颈** · 稀疏的非马尔可夫奖励难暴露子目标依赖。
- **核心创新 / 方法** · 先识别子目标层级，将其与任务 DFA 组成乘积自动机，再塑形 critic。
- **Baseline** · 代表性 DFA 强化学习和势函数塑形路线。
- **Benchmark** · 多个任务领域；关注完成任务的加速。
- **关键结果 / 消融** · 摘要报告部分设置加速两至三倍，并保留原任务最优策略。
- **适用条件 / 局限** · 依赖可表述的任务自动机和可发现的前置关系。

**可复用机制** · 把时间依赖写进状态结构，再在价值侧利用前置目标提高信号密度。

<a id="paper-139340"></a>

## HDL-RepoBench: Multi-Paradigm Repository-Level Code Completion for Hardware Design Languages

[官方论文页](https://neurips.cc/virtual/2026/poster/139340) · [作者来源](https://openreview.net/forum?id=VhzYiQ95Mx)

- **问题 / 瓶颈** · 软件仓库的检索与上下文经验未必适用硬件描述语言。
- **核心创新 / 方法** · 按语法和硬件语义标注完成目标，结合功能测试比较不同语言、结构深度与检索设置。
- **Baseline** · 无检索、软件仓库检索、通用模型。
- **Benchmark** · 三种硬件编码范式；功能通过率、EM/ES。
- **关键结果 / 消融** · 部分检索器不如无检索，超过 2,048 词元后准确度趋平，深度与表现非单调。
- **适用条件 / 局限** · 来自所测 HDL 和仓库分布，其他工具链需复测。

**可复用机制** · 面对新语言先诊断依赖结构是否匹配检索器，避免将更长上下文当作默认收益。

<a id="paper-148545"></a>

## Heads That Write, Not Just Point: Image Retrieval Heads in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148545) · [作者来源](https://openreview.net/forum?id=x59KtHPgHO)

- **问题 / 瓶颈** · 注意力指向目标图像不代表输出携带目标信息。
- **核心创新 / 方法** · 用图像 token 注意力选指针头，在值加权输出上训练轻量检索器选写入头，再按集合消融。
- **Baseline** · 随机头、仅指针或仅写入头及外部视觉语言检索器。
- **Benchmark** · ICIR-MCQ 与自然多图检索；关注头集合重叠和消融。
- **关键结果 / 消融** · 两套前百名仅重叠 35 至 44 个，重要头集中在交集。
- **适用条件 / 局限** · 依赖探针和任务设定；对其他模型的覆盖待核实。

**可复用机制** · 对注意力部件同时核对信息从哪里读入和记忆中实际写出了什么。

<a id="paper-148254"></a>

## Hearing is Believing? Evaluating and Analyzing Audio Language Model Sycophancy with SYAUDIO

[官方论文页](https://neurips.cc/virtual/2026/poster/148254) · [作者来源](https://openreview.net/forum?id=zGOpgI7plw)

- **问题 / 瓶颈** · 文本结论可能覆盖听到的证据，且噪声和语速改变表现。
- **核心创新 / 方法** · 用感知、推理、数学及伦理题，改变反馈和声学条件测迎合。
- **Baseline** · 微调前模型；具体比较待核实。
- **Benchmark** · SYAUDIO 4,319 题，有人工语音验证部分合成语音。
- **关键结果 / 消融** · 摘要报告音频特有迎合现象；监督微调降低误导敏感度。
- **适用条件 / 局限** · 受所测音频场景、合成语音及模型限制。

**可复用机制** · 同时测试错误反馈的抗扰性和正确信息的接受能力，避免仅靠压低模型顺从性优化。

<a id="paper-153222"></a>

## Hearing the Unspoken: Simulator-Induced Asymmetric-View Policy Optimization for Proactive Task-Oriented Dialogue

[官方论文页](https://neurips.cc/virtual/2026/poster/153222) · [作者来源](https://openreview.net/forum?id=MsVDpPS4yS)

- **问题 / 瓶颈** · 重加权被动策略的现有样本难教会其主动询问。
- **核心创新 / 方法** · 训练时让教师看到模拟器隐藏关注点，在线自蒸馏到仅见对话的策略，并用模拟状态变化分配轮次信用。
- **Baseline** · GRPO、其他强化学习基线及领先专有模型。
- **Benchmark** · 食品配送商户与骑手招募任务，并跨多个用户模拟器测试。
- **关键结果 / 消融** · 摘要报告优于强 RL 基线，达到或超过所比专有模型。
- **适用条件 / 局限** · 依赖模拟状态质量，真实人群或其他对话领域需另验。

**可复用机制** · 把不可部署的环境标注用于训练期教学，再单独检验去掉特权输入的策略。

<a id="paper-154862"></a>

## Hear, Localize, and Reason: Spatially Aware Scene Understanding for Audio-visual LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154862) · [作者来源](https://openreview.net/forum?id=AK3Ucj8EpF)

- **问题 / 瓶颈** · 将音频压成单声道语义会丢失声源几何。
- **核心创新 / 方法** · 在视听骨干接入双耳空间分支，逐阶段训练，末阶段监督多步空间推理。
- **Baseline** · 现有视听大模型和所用基础模型。
- **Benchmark** · HLR-AVSceneQA 的听觉识别、不同视点定位与声源对象关系。
- **关键结果 / 消融** · 摘要报告空间表现改善且保留语义感知。
- **适用条件 / 局限** · 需要可靠双耳观测，真实麦克风配置的泛化待核实。

**可复用机制** · 为多模态空间任务保留可定位的底层观测，并把定位和关系理解分开验收。

<a id="paper-139278"></a>

## HearSayBench: Can LLMs Navigate from Abstract Human Rights to Lived Lives?

[官方论文页](https://neurips.cc/virtual/2026/poster/139278) · [作者来源](https://openreview.net/forum?id=ZqbnpmPYvV)

- **问题 / 瓶颈** · 常规咨询基准假设用户有充分行动自由。
- **核心创新 / 方法** · 用经人工核验的情境对照法律承诺与个人实际可选行动。
- **Baseline** · 11 个前沿和开放权重模型。
- **Benchmark** · 400 个情境，覆盖 80 地区和社会、个人、环境三类阻碍。
- **关键结果 / 消融** · 摘要报告理解与结构推理间约 37% 的落差。
- **适用条件 / 局限** · 情境题不能直接证明真实咨询成效。

**可复用机制** · 即使回答正确复述了约束，也要单独测试建议是否能在约束下执行。

<a id="paper-156063"></a>

## HEART: Hyperspherical Embedding Alignment via Kent-Representation Traversal in Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156063) · [作者来源](https://openreview.net/forum?id=0jVJaUEE17)

- **问题 / 瓶颈** · 欧氏线性移位容易同时改变背景和无关属性。
- **核心创新 / 方法** · 用 Kent 分布描述概念的球面各向异性，在球面内做几何变换。
- **Baseline** · 欧氏文本嵌入编辑。
- **Benchmark** · 多个扩散架构上的主体替换和属性编辑；具体指标待核实。
- **关键结果 / 消融** · 摘要报告无需微调、反演或优化即可保持场景。
- **适用条件 / 局限** · 依赖文本编码空间和概念分布可被所选模型近似。

**可复用机制** · 根据表征的实际几何选编辑路径，避免将点差平移当作概念语义。

<a id="paper-149898"></a>

## HeatKV: Head-tuned KV-cache Compression for Visual Autoregressive Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/149898) · [作者来源](https://openreview.net/forum?id=mPOtDA3Wld)

- **问题 / 瓶颈** · 跨尺度 KV 缓存巨大，统一剪枝忽略各头的历史依赖。
- **核心创新 / 方法** · 在小型离线集统计各头对旧尺度的注意力并构造静态预算表。
- **Baseline** · 既有视觉自回归 KV 压缩方法。
- **Benchmark** · Infinity-2B；缓存、画质、文本对齐及人类感知。
- **关键结果 / 消融** · 摘要报告约两倍压缩比，质量相当或更好。
- **适用条件 / 局限** · 依赖离线统计在目标任务上的稳定性；仅列单一模型。

**可复用机制** · 缓存预算优先留给确实使用历史尺度的头，并在部署前校验不同输入下的排序。

<a id="paper-154575"></a>

## Heavy-Tailed Flow Matching via Random Clocks

[官方论文页](https://neurips.cc/virtual/2026/poster/154575) · [作者来源](https://openreview.net/forum?id=CXUjf5ukqP)

- **问题 / 瓶颈** · 标准高斯源与极端值频率不匹配。
- **核心创新 / 方法** · 给定随机时钟路径时使用高斯流，边缘化得到尺度混合；以截断对数签名编码时钟供速度场使用。
- **Baseline** · 高斯流匹配及其他重尾方法。
- **Benchmark** · 二维重尾混合、CIFAR10-LT、HRRR；覆盖、质量、尾部统计及函数调用次数。
- **关键结果 / 消融** · 摘要报告尾部恢复和模式覆盖改善，并保留较少采样步。
- **适用条件 / 局限** · 需为任务选合适的时钟分布，跨其他极端事件领域待核实。

**可复用机制** · 用可控制的尺度混合改变采样尾重，条件训练仍利用高斯结构。

<a id="paper-150667"></a>

## HEED: Density-Weighted Residual Alignment for Hybrid Vision-Language Model Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/150667) · [作者来源](https://openreview.net/forum?id=gNV0DzH5iz)

- **问题 / 瓶颈** · 混合架构的整体分数掩盖细字性能损失，均匀对齐被背景图块主导。
- **核心创新 / 方法** · 用图块自差异度代理信息量，增加高密度位置的残差对齐权重。
- **Baseline** · 均匀端到端蒸馏和教师。
- **Benchmark** · OCRBench v2、MMStar 等十项基准；宽上下文的吞吐和显存。
- **关键结果 / 消融** · 相较普通蒸馏 OCRBench v2 提高 8.7 分，十项平均提高 5.13 分。
- **适用条件 / 局限** · 权重代理需能识别任务关键信息；与具体蒸馏路径相关。

**可复用机制** · 先按局部信息量诊断教师学生偏移，再重加权那些虽稀少却决定答案的位置。

<a id="paper-138892"></a>

## HelpBench: Assessing the Ability of LLMs to Provide Privacy, Safety, and Security Advice

[官方论文页](https://neurips.cc/virtual/2026/poster/138892) · [作者来源](https://openreview.net/forum?id=ySxqajUUaa)

- **问题 / 瓶颈** · 通用问答分数掩盖模型对复杂高风险求助的定制不足。
- **核心创新 / 方法** · 以真实用户求助构建逐题规范，并用自动评分汇总多维表现。
- **Baseline** · 18 个现有语言模型。
- **Benchmark** · 450 道数字隐私、安全和设备防护求助题。
- **关键结果 / 消融** · 平均约 82%，复杂或高风险问题仍有改善空间。
- **适用条件 / 局限** · 取决于规范和自动评分质量；真实操作成效待核实。

**可复用机制** · 把风险等级与情境适配做成独立评测切面，避免平均分遮住最需可靠回复的案例。

<a id="paper-148497"></a>

## HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse

[官方论文页](https://neurips.cc/virtual/2026/poster/148497) · [作者来源](https://openreview.net/forum?id=xMqv6BYsZv)

- **问题 / 瓶颈** · 异构记忆接口让整体上下文反复编码，即使多数内容未变。
- **核心创新 / 方法** · 跨动作跟踪陈述、程序和工作记忆内容，保留兼容 KV，调和受更新影响的状态。
- **Baseline** · MemRL。
- **Benchmark** · ALFWorld、Habitat 及真实机器人，任务成功率和单步推理时间。
- **关键结果 / 消融** · 真机报告成功率 83.20%，单步时间从 2.94 降至 1.87 秒。
- **适用条件 / 局限** · 缓存位置与依赖变化下的兼容条件待核实。

**可复用机制** · 按内容变更跟踪缓存失效范围，在任务成功率约束下评估复用收益。

<a id="paper-139360"></a>

## HERO: A Heterogeneity-Aware Benchmark Library for Federated Continual Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/139360) · [作者来源](https://openreview.net/forum?id=UgjTgBmVgZ)

- **问题 / 瓶颈** · 数据分割、任务顺序及统计口径共同变化掩盖方法差异。
- **核心创新 / 方法** · 将任务拆分、客户端数据拆分和任务序列独立控制，HERO-Core 分别参数化偏斜和任务顺序不匹配。
- **Baseline** · 代表性联邦持续学习方法及同步任务设置。
- **Benchmark** · CIFAR-100、TinyImageNet，最终平均准确率、平均遗忘及后 10% 客户端准确率；另有 OGB-MolPCBA 域迁移案例。
- **关键结果 / 消融** · 均值掩盖尾部退化，异步顺序与同步设置支持不同策略。
- **适用条件 / 局限** · 图任务属于迁移案例，不同任务与域拆分的结论待核实。

**可复用机制** · 把系统异质性拆成可独立操纵的轴，避免将同步基准的排名外推到异步部署。

<a id="paper-139720"></a>

## HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data

[官方论文页](https://neurips.cc/virtual/2026/poster/139720) · [作者来源](https://openreview.net/forum?id=8YiaoJ83Yi)

- **问题 / 瓶颈** · 直接汇总银标有偏，少量金标估计方差又大。
- **核心创新 / 方法** · 复用历史金标对标注者校准，再将估计锚定到历史高精度协变量，在部分标注者重叠时仍可用。
- **Baseline** · 朴素银标汇总及稀疏金标估计的具体实现待核实。
- **Benchmark** · 模拟和真实生成模型评估数据，关注估计偏差与方差。
- **关键结果 / 消融** · 给出偏差方差改善条件并展示经验收益，幅度待核实。
- **适用条件 / 局限** · 依赖跨轮次校准可迁移性及协变量有效性，具体假设待核实。

**可复用机制** · 将历史数据用于两种独立校正，一种处理标注误差，一种处理抽样波动。

<a id="paper-153326"></a>

## Hessian-Dependent Sample Complexity in Zeroth-Order Stochastic Optimization: Suboptimality of Convex-Support Sampling and Optimal Sample Complexity

[官方论文页](https://neurips.cc/virtual/2026/poster/153326) · [作者来源](https://openreview.net/forum?id=M9Iy6jM9oZ)

- **问题 / 瓶颈** · 常规基于凸集的探测分布存在共同的海森相关复杂度瓶颈。
- **核心创新 / 方法** · 在球面截段的非凸并集采样构造谱分组梯度估计器。
- **Baseline** · 凸支持采样的零阶估计方法。
- **Benchmark** · 二阶光滑强凸函数族，比较海森相关简单遗憾与样本复杂度。
- **关键结果 / 消融** · 证明复杂度阶优于常规方案，在共享最优点海森矩阵的函数子类中给出匹配下界。
- **适用条件 / 局限** · 当前理论对象为强凸光滑函数，曲率获取及非凸推广待核实。

**可复用机制** · 把海森谱结构作为探测分布的设计变量，而非限于统一椭球或其他凸支持。

<a id="paper-148592"></a>

## HESTIA: A Hessian-Guided Differentiable Quantization-Aware Training Framework for Extremely Low-Bit LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148592) · [作者来源](https://openreview.net/forum?id=wbAS7CXyXl)

- **问题 / 瓶颈** · 直通估计的前后向不一致，小更新易停在量化边界内。
- **核心创新 / 方法** · 以相同码本的温控 Softmax 期望替代硬量化，按离线海森迹调节温度并退火回硬量化。
- **Baseline** · 三值量化感知训练及直通估计。
- **Benchmark** · Llama-3.2 1B、3B，零样本平均表现和额外训练时间。
- **关键结果 / 消融** · 相对平均增益分别为 5.39% 和 4.34%，训练额外开销约 0.2%，无额外推理成本。
- **适用条件 / 局限** · 已列数据针对三值和两个模型规模，其他码本和海森估计稳定性待核实。

**可复用机制** · 用连续松弛来对齐训练前后向，并分别消融算子松弛和温度调度信号。

<a id="paper-152031"></a>

## Heterogeneous Judge-Aware Ranking with Sensitivity, Disagreement, and Confidence

[官方论文页](https://neurips.cc/virtual/2026/poster/152031) · [作者来源](https://openreview.net/forum?id=W3mkBXvDwV)

- **问题 / 瓶颈** · 简单合并打分把系统性分歧当成噪声。
- **核心创新 / 方法** · 建立三项可识别分解，用带锚交替算法估计，并以固定评委重复判断构造不确定性。
- **Baseline** · 合并评委判断与仅建模敏感度的方法。
- **Benchmark** · 合成与真实多评委比较数据，考察排序恢复、近似平局和区间校准。
- **关键结果 / 消融** · 相较对照改善恢复、鲁棒性、校准及近似平局表现。
- **适用条件 / 局限** · 区间证据对应固定面板重复比较；辨识条件待核实。

**可复用机制** · 对接近打平的模型同时报告共识区间和评委分歧，避免平均胜率抹掉稳定偏好。

<a id="paper-154158"></a>

## Heterogeneous Parallelism for Multimodal Large Language Model Training

[官方论文页](https://neurips.cc/virtual/2026/poster/154158) · [作者来源](https://openreview.net/forum?id=FpEMaMSLx7)

- **问题 / 瓶颈** · 统一语言模型布局会限制编码器并行并引入多余通信。
- **核心创新 / 方法** · 各模块独立布局和设备放置，边界通信器正向变换激活、反向将梯度送回原布局。
- **Baseline** · 优化的同构布局、同设备异构和分设备异构。
- **Benchmark** · 多模态工作负载、GPU 规模和上下文长度，指标为 TFLOPs/s/GPU、token 吞吐及损失收敛。
- **关键结果 / 消融** · 同设备异构在短、长上下文分别最高提升 14.4%、41.8% TFLOPs/s/GPU，分设备 token 吞吐最多提升 13.0%。
- **适用条件 / 局限** · 取决于通信、模态规模和设备映射，收益为所测上限。

**可复用机制** · 按模块独立优化并行，再将前反向接口成本计入是否拆分部署的决策。

<a id="paper-155111"></a>

## Heuresis: Evaluating Search Strategies for Autonomous Machine Learning Research Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/155111) · [作者来源](https://openreview.net/forum?id=8JKGunjhLy)

- **问题 / 瓶颈** · 只追单项最好性能容易得到已经存在的方案。
- **核心创新 / 方法** · 用通用搜索原语对照五个质量多样性、进化及好奇搜索算法与贪心。
- **Baseline** · 贪心及五种已有搜索算法。
- **Benchmark** · 语言模型预训练与同策略强化学习；质量、多样性及 Gupta–Pruthi 新颖性评分。
- **关键结果 / 消融** · 所测高质量贪心方案均被判为直接复现；少量获验证的新方案来自兼顾多样性或好奇度的搜索。
- **适用条件 / 局限** · 结果限于两类任务和所用新颖性规则。

**可复用机制** · 将文献新颖性核查作为与性能评分独立的评价，避免把复现成绩计作研究发现。

<a id="paper-148440"></a>

## H-GenPO: Hierarchical Generative Policy Optimization via the Option-Critic Framework

[官方论文页](https://neurips.cc/virtual/2026/poster/148440) · [作者来源](https://openreview.net/forum?id=xmAWFBUpId)

- **问题 / 瓶颈** · 平坦生成策略每步重选，丰富动作分布不足以维持一致行为。
- **核心创新 / 方法** · 将在线生成式强化学习接入 Option-Critic，上层选离散选项，下层共享一个以选项嵌入为条件的流匹配策略。
- **Baseline** · 平坦生成策略、Option-Critic 及连续控制基线，具名实现待核实。
- **Benchmark** · Isaac Lab 八个标准连续控制和三个需协调切换模式的任务；评估平均排名与选项分化。
- **关键结果 / 消融** · 两类任务均报告平均排名最佳，无选项标签也涌现可解释的分化。
- **适用条件 / 局限** · 真实机器人和更长视距未由摘要确证。

**可复用机制** · 把跨时间承诺交给选项层，动作分布的表达能力保留在共享低层网络。

<a id="paper-153314"></a>

## Hidden Forgetting in Continual Multimodal Learning: When Accuracy Survives but Grounding Fails

[官方论文页](https://neurips.cc/virtual/2026/poster/153314) · [作者来源](https://openreview.net/forum?id=MDf0kUD4oe)

- **问题 / 瓶颈** · 答案仍正确时，依赖可能已转向更弱的视觉、OCR 或文本证据。
- **核心创新 / 方法** · 冻结旧检查点，反事实干预不同证据通道，匹配新旧依赖画像及预测且同时学习新任务。
- **Baseline** · 无回放、参数高效、路由和记忆辅助方法。
- **Benchmark** · CoIN、COAST、MCITlib 及证据敏感多模态流，测最终效果、遗忘和依赖漂移。
- **关键结果 / 消融** · 作者报告减少依赖漂移、主证据反转及隐藏遗忘，无额外推理开销。
- **适用条件 / 局限** · 训练期反事实成本及通道干预的有效性待核实。

**可复用机制** · 将答案一致与证据一致作为两个可干预的保留目标。

<a id="paper-148222"></a>

## Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking

[官方论文页](https://neurips.cc/virtual/2026/poster/148222) · [作者来源](https://openreview.net/forum?id=zSWN22jVAz)

- **问题 / 瓶颈** · 常规置信区间只计题目抽样误差，样本越多设计遗漏越突出。
- **核心创新 / 方法** · 分解抽样方差和设计敏感性，使用总评估误差预测等成本下的资源分配。
- **Baseline** · 忽略评委设计方差的标准误和置信区间。
- **Benchmark** · Chatbot Arena、MMLU；考察区间覆盖、答案键误差及人工投票一致率。
- **关键结果 / 消融** · 常规标准误小 40–60%，修正区间在 Arena 维持 95% 覆盖；同成本下 MMLU 误差减半。
- **适用条件 / 局限** · 有效性取决于试验覆盖的评委、提示及温度，跨设定需重估。

**可复用机制** · 先把预算用于比较评估设计，再决定加样本还是增加评委配置的重复。

<a id="paper-139751"></a>

## HiddenPathQA: A Benchmark for Knowledge Graph Question Answering When Questions Hide Their Paths

[官方论文页](https://neurips.cc/virtual/2026/poster/139751) · [作者来源](https://openreview.net/forum?id=6ixxExuYiN)

- **问题 / 瓶颈** · 逐跳方法依赖问题字面暴露金标关系。
- **核心创新 / 方法** · 同时呈现围绕主题实体的候选关系链，与整条问题做匹配。
- **Baseline** · ToG、PoG、FiDeLiS、R2-KG、KAPING、KARPA。
- **Benchmark** · HiddenPathQA 1,055 题、2–6 跳、四种骨干与划分组合，另做实体伪词测试。
- **关键结果 / 消融** · 强对照之上增加 8.8–17.9 点；实体替换揭示部分基线依赖记忆。
- **适用条件 / 局限** · 候选完整性与高分支图上的开销待核。

**可复用机制** · 将词面关系重合与实体记忆各做一次独立干预，判断逐跳还是整链评分更适用。

<a id="paper-139499"></a>

## Hidden Positives: Why Code Retrieval Benchmarks Underestimate Model Quality

[官方论文页](https://neurips.cc/virtual/2026/poster/139499) · [作者来源](https://openreview.net/forum?id=M2DNqP5kmA)

- **问题 / 瓶颈** · 代码检索把合法的替代实现当负例，扭曲模型比较。
- **核心创新 / 方法** · 以统一评审器和固定提示重标全部模型前十结果，另外用语义重排标注训练对。
- **Baseline** · 对照原标签协议和已有开放代码嵌入模型。
- **Benchmark** · 六个代码检索基准，统计相关候选漏标与 MRR@10。
- **关键结果 / 消融** · 模型评审认定相关项中 44%–87% 未在原标签中；7B 平均 MRR@10 领先 3.5 点。
- **适用条件 / 局限** · 评审模型自身偏差和前十范围以外的漏标仍待验证。

**可复用机制** · 比较多个检索器时汇总候选复标，再用人工抽样估计统一评审器的误判。

<a id="paper-154165"></a>

## Hidden Tails: Certifying Tail-Risk Claims under Selective Labels

[官方论文页](https://neurips.cc/virtual/2026/poster/154165) · [作者来源](https://openreview.net/forum?id=FnMwOr3VoG)

- **问题 / 瓶颈** · 观测损失一致也可能对应反转的总体 CVaR 排名。
- **核心创新 / 方法** · 在胜算比敏感性模型下推导锐界，并将指定阈值下的最低补标成本写成分数背包。
- **Baseline** · 仅评估已揭露标签及松弛稳健代理是问题背景。
- **Benchmark** · 理论推导，含交叉拟合有限样本保证和尾标签数下界。
- **关键结果 / 消融** · 证明重叠也无法识别排名，最坏补全与阈值优化可交换。
- **适用条件 / 局限** · 证书依赖敏感性模型和已有尾部标注量。

**可复用机制** · 决策系统风险审计报告敏感性区间，并优先揭露可能改变尾部证书的标签。

<a id="paper-150396"></a>

## Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring

[官方论文页](https://neurips.cc/virtual/2026/poster/150396) · [作者来源](https://openreview.net/forum?id=iM3BORT60x)

- **问题 / 瓶颈** · 将失败标签均摊到各步会淹没局部信号，动作重采样又昂贵。
- **核心创新 / 方法** · 联用轨迹间及轨迹内对比目标，由粗粒度标签学习有时间结构的异常分数。
- **Baseline** · 动作重采样、外部模型与均匀标签传播是对照路线，细节待核。
- **Benchmark** · LIBERO、VLABench 和实机，OpenVLA、π0、π0.5；监测准确性与及时性。
- **关键结果 / 消融** · 摘要报告多任务检测领先，保形预测可调准确性与及时性。
- **适用条件 / 局限** · 跨平台和未见故障泛化边界待核。

**可复用机制** · 按检测提前量和误报比较轨迹标签均摊与步级弱监督。

<a id="paper-149113"></a>

## Hider–Seeker Self-Play: Geometry-Verifiable Process Rewards for Long-Horizon Visual Search

[官方论文页](https://neurips.cc/virtual/2026/poster/149113) · [作者来源](https://openreview.net/forum?id=smof5snaBr)

- **问题 / 瓶颈** · 最终奖励太稀疏，语言评审难校验每步。
- **核心创新 / 方法** · Hider 重加权挑战轨迹，Seeker 获得几何可验证进展与覆盖反馈，轨迹长度和空间冗余另作约束。
- **Baseline** · 结果式 RLVR、语言模型步骤评审及先进基线，名称待核。
- **Benchmark** · 十一项多模态基准，含消融与零样本分布外迁移。
- **关键结果 / 消融** · 摘要称持续领先，并给出回退、探索分离与策略不变性保证。
- **适用条件 / 局限** · 依赖目标区域标注和能算几何进度的任务。

**可复用机制** · 当环境已有几何量时直接用它评价步骤，并独立约束预算与重复。

<a id="paper-154951"></a>

## Hide to Guide: Learning via Semantic Masking

[官方论文页](https://neurips.cc/virtual/2026/poster/154951) · [作者来源](https://openreview.net/forum?id=9hZDtNqGcn)

- **问题 / 瓶颈** · 示范泄漏关键内容时策略可复制获奖而不学过程。
- **核心创新 / 方法** · SMEPO 按语义遮掉通向验证目标的关键片段，保留分解与程序结构，奖励和强化学习目标照旧。
- **Baseline** · GRPO 及用截断控制示范长度的路线。
- **Benchmark** · 数学、代码和智能体搜索，比较准确率及训练耗时。
- **关键结果 / 消融** · 最高增加 3.2 点，训练最多快 4.2 倍。
- **适用条件 / 局限** · 依赖可识别的验证相关片段；遮盖漏项需审计。

**可复用机制** · 把提示量与可复制性解耦，在相同提示预算下对照随机遮盖。

<a id="paper-149574"></a>

## Hide to See: Reasoning-prefix Masking for Visual-anchored Thinking in VLM Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/149574) · [作者来源](https://openreview.net/forum?id=p82pGutdyc)

- **问题 / 瓶颈** · 紧凑模型可能从已有文本推理词复制线索。
- **核心创新 / 方法** · 学生使用逐词显著前缀遮盖，并依据师生分布差异逐渐扩大遮盖预算。
- **Baseline** · 近期 VLM、蒸馏与自蒸馏对照。
- **Benchmark** · 多模态推理基准和过程视觉利用分析。
- **关键结果 / 消融** · 摘要称优于对照并增强思考过程对视觉的使用。
- **适用条件 / 局限** · 遮盖的文本若真为必要推理条件，可能破坏学习；范围待核。

**可复用机制** · 用同预算随机遮盖作对照，再通过图像干预测视觉依赖。

<a id="paper-154222"></a>

## HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154222) · [作者来源](https://openreview.net/forum?id=FIXDBNuA60)

- **问题 / 瓶颈** · 表征漂移会导致专家路由干扰。
- **核心创新 / 方法** · 双注意力分别执行指令级专家检索与情境修正；键空间同任务对齐、跨任务分离。
- **Baseline** · 有回放和无回放持续学习方法。
- **Benchmark** · LIBERO 多套评测及异质任务、指令改写变体，考察 AUC、前向迁移与遗忘。
- **关键结果 / 消融** · 摘要报告 AUC 和前向迁移提高、遗忘低，高干扰时收益较明显。
- **适用条件 / 局限** · 依赖可用的任务信息和扩展专家容量，长期成本待核。

**可复用机制** · 用语言改写和任务顺序干预分别检查检索错误与专家适配错误。

<a id="paper-154138"></a>

## Hierarchical Agglomerative Clustering via Relaxed Representatives

[官方论文页](https://neurips.cc/virtual/2026/poster/154138) · [作者来源](https://openreview.net/forum?id=Fxc3acAsk6)

- **问题 / 瓶颈** · 传统代表式连接计算贵或会产生合并距离倒置。
- **核心创新 / 方法** · 放宽代表条件得到二次代价的 RMM* 和代表仍为样本的无倒置 RC*。
- **Baseline** · Minimax、Centroid 与其他聚类对照。
- **Benchmark** · 表格、生物与文本数据，比较聚类质量、成本与树状图倒置；另有理论近似验证。
- **关键结果 / 消融** · RMM* 质量接近 Minimax 且成本较小；RC* 消除倒置；两者对 k-center 有近似保证。
- **适用条件 / 局限** · 近似保证针对 k-center，其他准则需另测。

**可复用机制** · 将无倒置、有样本代表与实际耗时分别列为层次聚类选型指标。

<a id="paper-151722"></a>

## Hierarchical Concept Geometry in Language Representations Emerges from Word Co-occurrence

[官方论文页](https://neurips.cc/virtual/2026/poster/151722) · [作者来源](https://openreview.net/forum?id=YaqVTMzLmi)

- **问题 / 瓶颈** · 嵌入中的层级可能被误归因于专门内部机制。
- **核心创新 / 方法** · 以 WordNet 关系距离构造衰减的共现假设，推导 Gram 矩阵主特征向量的粗到细分裂。
- **Baseline** · word2vec 与 Gemma 2B 输出嵌入对照。
- **Benchmark** · 多个 WordNet 子树，比较谱切分与分类树。
- **关键结果 / 消融** · 理论给出谱层级组织，观测在两类嵌入均可见。
- **适用条件 / 局限** · 依赖共现正性及衰减，其他语言和关系需验证。

**可复用机制** · 解释模型概念几何之前先用共现统计建立可量化对照。

<a id="paper-150172"></a>

## Hierarchical Conformal Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/150172) · [作者来源](https://openreview.net/forum?id=k9Vms7prG3)

- **问题 / 瓶颈** · 传统集合忽略标签上下位关系。
- **核心创新 / 方法** · 限制候选为结构化节点组合，在保持覆盖保证和最优性的约束下优化集合。
- **Baseline** · 现有先进保形分类方法，名称待核。
- **Benchmark** · 音频、图像、文本和用户研究；检查覆盖率与人类偏好。
- **关键结果 / 消融** · 摘要报告优于对照，层次输出更符合人类偏好。
- **适用条件 / 局限** · 依赖已知标签树，结构失配及长尾覆盖待核。

**可复用机制** · 将细标签与粗类作为可选输出，分别比较覆盖和输出信息量。

<a id="paper-153644"></a>

## Hierarchical Cross-Class Part Alignment for Prototypical Part Networks via Hyperbolic Entailment

[官方论文页](https://neurips.cc/virtual/2026/poster/153644) · [作者来源](https://openreview.net/forum?id=Jn0nBdpogW)

- **问题 / 瓶颈** · 单层原型易把同一部件割裂成彼此无关的类内原型。
- **核心创新 / 方法** · 在双曲空间用蕴含锥约束父子原型，并用视觉基础模型产生的伪补丁 ID 做对比学习防冗余。
- **Baseline** · ProtoPNet 及既有双曲原型路线。
- **Benchmark** · CUB-200-2011、Stanford Cars，四类 ProtoPNet 和四种骨干；测分类和解释指标。
- **关键结果 / 消融** · 分类最多提升 10 点，部件层次 IoU 由 11% 到 75%。
- **适用条件 / 局限** · 依赖伪补丁标签质量，其他部件体系待核。

**可复用机制** · 比较共享与类内信息粒度时，用显式原型对应关系替代事后聚类。

<a id="paper-151418"></a>

## Hierarchical Denoising For Multi-Step Visual Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151418) · [作者来源](https://openreview.net/forum?id=apazc2xK3R)

- **问题 / 瓶颈** · 流式扩散缺少全局回看，双向去噪延迟高。
- **核心创新 / 方法** · 树状潜变量支持粗到细去噪，粗层规划、细层输出，并配稀疏层次注意。
- **Baseline** · 流式自回归扩散与双向扩散。
- **Benchmark** · 六种多步视觉任务及分布外样本，成功率、进度、每潜变量时延与数据效率。
- **关键结果 / 消融** · 成功率 34.22 到 60.29；进度 76.00 到 89.56；流式每潜变量 0.70 秒。
- **适用条件 / 局限** · 摘要实机证据仅展示潜力，任务规模与计划错误传播待核。

**可复用机制** · 用相同解码预算分离粗层假设和细层滚动，测中间状态一致性。

<a id="paper-154034"></a>

## Hierarchical Graph Representation Learning with Pooling-Induced Substructures

[官方论文页](https://neurips.cc/virtual/2026/poster/154034) · [作者来源](https://openreview.net/forum?id=Gj1n6ynavZ)

- **问题 / 瓶颈** · 节点聚合会遗失跨局部邻域的结构及其角色。
- **核心创新 / 方法** · 保留并编码由结构池化发现的子结构，结合 WL 表达性分析和可控结构强度评测。
- **Baseline** · 匹配的普通池化基线。
- **Benchmark** · 两种可控层次合成数据和真实图级评测，另量化层次模式。
- **关键结果 / 消融** · 有层次任务超过对照，结构简单任务表现相当。
- **适用条件 / 局限** · 收益依赖池化能发现有用子结构。

**可复用机制** · 先验证数据实际包含层次，再对比保留子结构与普通聚合。

<a id="paper-150192"></a>

## Hierarchical Regime-Conditioned Dynamics for Spatiotemporal Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/150192) · [作者来源](https://openreview.net/forum?id=k39QrQmBiI)

- **问题 / 瓶颈** · 现有时空图潜状态容易纠缠不同全局模式。
- **核心创新 / 方法** · 用离散全局模式主动约束连续实体演化，自监督联合预测和模式识别。
- **Baseline** · 时序图模型、潜动态模型及状态识别路线，具体名称待核。
- **Benchmark** · 有控制的合成与真实时空数据，比较工况恢复和预测。
- **关键结果 / 消融** · 摘要称可识别有意义模式并保持有竞争力的预测。
- **适用条件 / 局限** · 离散模式假设需与连续漂移等备择对照。

**可复用机制** · 对全局模式做干预，同时检验局部动态是否仍与真实轨迹相符。

<a id="paper-149193"></a>

## Hierarchical Semantic Tree Anchoring for CLIP-Based Class-Incremental Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149193) · [作者来源](https://openreview.net/forum?id=sCUuF8mN4k)

- **问题 / 瓶颈** · 普通 CLIP 增量学习容易细粒度特征漂移。
- **核心创新 / 方法** · 双曲空间保留父子语义关系，公共映射的更新受历史特征诱导的零空间限制。
- **Baseline** · 既有 CLIP 类增量方法，具体名称待核。
- **Benchmark** · 九套基准，预测表现、特征漂移和遗忘。
- **关键结果 / 消融** · 摘要称持续领先并减少漂移和遗忘。
- **适用条件 / 局限** · 依赖类别层次知识与历史特征，任务界限及存储成本待核。

**可复用机制** · 分别测结构锚点和更新约束对旧类边界与新类适应的贡献。

<a id="paper-154863"></a>

## Hierarchical Variational Policies for Reward-Guided Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154863) · [作者来源](https://openreview.net/forum?id=AJenxpWZXp)

- **问题 / 瓶颈** · 推理时逐样本搜索或优化开销大。
- **核心创新 / 方法** · 层次变分模型用随机策略提供大步长逐步控制，并允许半摊销补充少量在线优化。
- **Baseline** · 先进推理时扩展基线。
- **Benchmark** · 4 倍超分辨率及多个逆问题，比较感知质量和耗时。
- **关键结果 / 消融** · 超分辨率在感知质量改善时推理提速超过 5 倍。
- **适用条件 / 局限** · 依赖下游目标可用于训练，换奖励后的额外成本待核。

**可复用机制** · 随部署量对比摊销训练和在线控制成本，画质量延迟曲线。

<a id="paper-155510"></a>

## Hierarchical World Models with Implicit Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/155510) · [作者来源](https://openreview.net/forum?id=53he7g9wCc)

- **问题 / 瓶颈** · 端到端规划受累积误差与搜索复杂度限制，固定宏动作不够灵活。
- **核心创新 / 方法** · 高层在状态流形上采样可达转移，低层把转移还原成精确动作。
- **Baseline** · 单层世界模型 MPC、策略及扩散规划器。
- **Benchmark** · 三套导航与操作任务，含未见长时配置。
- **关键结果 / 消融** · 摘要报告相对先进规划器提高 38.5%，相对单层 MPC 提高 120%。
- **适用条件 / 局限** · 依赖可学的可达性和逆动力学，不能保证任意候选转移可执行。

**可复用机制** · 高层只约束局部物理可达性，再拼接计划，降低对训练中整段行为模式的依赖。

<a id="paper-149679"></a>

## HierFlow: Hierarchical Coupled Dual-Space Search for Automatic Agentic Workflow Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149679) · [作者来源](https://openreview.net/forum?id=oFWYxd9QWu)

- **问题 / 瓶颈** · 固定离线工作流难适应问题，联合枚举拓扑与代码也昂贵。
- **核心创新 / 方法** · 上层拓扑划定下层代码搜索域；下层轻量树搜索由门控触发，并把执行反馈送回拓扑。
- **Baseline** · 竞争性工作流生成基线，名称待核实。
- **Benchmark** · 问答、数学推理、代码生成的质量与效率。
- **关键结果 / 消融** · 摘要报告免额外训练即可提高质量效率折中。
- **适用条件 / 局限** · 子任务强耦合或门控代理失真时优势可能下降。

**可复用机制** · 用运行反馈打破先定骨架再填实现的单向流程，对需要的子任务才追加搜索。

<a id="paper-139579"></a>

## HierSVA: A Synthesis Pipeline, Dataset, and Benchmark for LLM-Driven Hierarchical Hardware Formal Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/139579) · [作者来源](https://openreview.net/forum?id=H9UpVBr5RW)

- **问题 / 瓶颈** · 可编译且可证明的断言可能覆盖不足或误报。
- **核心创新 / 方法** · 分开度量语法、证明、空泛性、忠实性、变异覆盖与形式核心覆盖。
- **Baseline** · 12 个模型，以及部分代理模式。
- **Benchmark** · BaseJump STL 342 个模块，深度 0 至 9；另有较深的 28 对模块和缺陷。
- **关键结果 / 消融** · 可评估运行的断言 82.1% 可非空泛证明，但形式核心覆盖仅 36.2%；深子集精确率 0.60。
- **适用条件 / 局限** · 基准来自单一硬件库；代理模式未评估一项忠实性指标。

**可复用机制** · 验证生成的规格时采用独立覆盖与负例检验，避免把工具接受率误当规格完整性。

<a id="paper-149761"></a>

## HIFC-IQA: Train-Free Cross-Domain Image Quality Assessment via Dual-Process Cognition

[官方论文页](https://neurips.cc/virtual/2026/poster/149761) · [作者来源](https://openreview.net/forum?id=nWRbNynKZi)

- **问题 / 瓶颈** · 合成失真与真实退化差异大，伪标签迭代成本高。
- **核心创新 / 方法** · 将语义和失真特征拆开，从合成库检索模糊质量中心，并与零样本视觉语言审美分支结合。
- **Baseline** · 无监督域适应画质评估方法。
- **Benchmark** · 合成到真实的跨域无参考画质；具体数据和指标待核实。
- **关键结果 / 消融** · 摘要报告免更新即可取得有竞争力的结果。
- **适用条件 / 局限** · 需要适当参考库及语义对齐，强域偏移时各分支贡献待核实。

**可复用机制** · 让稳定的失真参照与内容相关审美互补，避免语义先验压过退化信号。

<a id="paper-154752"></a>

## HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154752) · [作者来源](https://openreview.net/forum?id=BDwmB9cg99)

- **问题 / 瓶颈** · 离群值拉伸动态范围导致展开激活下溢，提高训练端精度反会加剧不匹配。
- **核心创新 / 方法** · 只在 rollout 矩阵乘法中加入硬件友好的稀疏残差补偿，并配合分层缩放。
- **Baseline** · 全 FP4、训练端升精度、BF16，另对比 MXFP4。
- **Benchmark** · Qwen2.5-3B、Qwen2.5-Math-7B 的 RL 后训练准确率。
- **关键结果 / 消融** · HiF4 对 BF16 的差距从 4.9% 降为 1.1%；MXFP4 从 13.6% 降至 5.3%。
- **适用条件 / 局限** · 格式和硬件稀疏支持影响收益，其他强化学习任务待核实。

**可复用机制** · 低精度训练先定位哪一端的误差改变了采样分布，再局部补偿并核验两端一致性。

<a id="paper-152215"></a>

## HiFloat4 Format for Language Model Pre-training on Ascend NPUs

[官方论文页](https://neurips.cc/virtual/2026/poster/152215) · [作者来源](https://openreview.net/forum?id=UhkVj158YU)

- **问题 / 瓶颈** · 四位动态范围窄，额外高精度稳定手段侵蚀效率。
- **核心创新 / 方法** · 让线性和专家 GEMM 使用分层缩放 HiF4，与 MXFP4 对比最低稳定化配置。
- **Baseline** · 全精度与 MXFP4。
- **Benchmark** · Ascend NPU 上的 OpenPangu-1B、Llama3-8B、Qwen3-MoE-30B；预训练损失与下游分数。
- **关键结果 / 消融** · HiF4 用一步稳定机制使相对损失差距低于 1%，MXFP4 用三步仍约为其两倍。
- **适用条件 / 局限** · 硬件、架构和规模以所测为限；训练吞吐待核实。

**可复用机制** · 把低比特表示的动态范围与训练稳定性联合设计，先用同等任务衡量格式本身带来的改进。

<a id="paper-148200"></a>

## High-Dimensional Conditional Independence Testing via Random Projection Aggregation

[官方论文页](https://neurips.cc/virtual/2026/poster/148200) · [作者来源](https://openreview.net/forum?id=zboZEFa5xo)

- **问题 / 瓶颈** · 高维非参数估计不稳定，单个投影又可能错过依赖。
- **核心创新 / 方法** · 独立投影被检变量，将标量检验的 p 值以 Bonferroni 规则聚合，另给分散信号的 top-r 版本。
- **Baseline** · 经典非参数 CI 与投影 GCM 基检验。
- **Benchmark** · 合成、图像值变量及结构学习任务；校准与功效。
- **关键结果 / 消融** · 渐近控制一类错误；可检测投影条件下二类错误上界随投影数指数下降。
- **适用条件 / 局限** · 依赖基检验有效且存在可检测方向。

**可复用机制** · 先以低维工具保持原假设，再通过多方向聚合弥补单次降维的漏检。

<a id="paper-154586"></a>

## High-Dimensional Learning Dynamics of Attention-Indexed Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154586) · [作者来源](https://openreview.net/forum?id=CU34scUsmz)

- **问题 / 瓶颈** · 直接优化注意力矩阵可能被无信息流形困住。
- **核心创新 / 方法** · 用高维注意力指标模型分析梯度流，比较共享因子分解与非共享因子分解。
- **Baseline** · 直接优化矩阵、共享与非共享注意力因子。
- **Benchmark** · 高维总体梯度流的弱恢复时间和对称性。
- **关键结果 / 消融** · 共享因子模型在该设定常数量级实现弱恢复；非共享模型取决于快时间尺度破缺。
- **适用条件 / 局限** · 属于总体损失与高维极限，不能外推到所有 Transformer。

**可复用机制** · 初始化比较应测早期信息方向是否被激活，不能只看参数张成的函数类。

<a id="paper-155594"></a>

## High-dimensional Limit of SGD for Diagonal Linear Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/155594) · [作者来源](https://openreview.net/forum?id=4RALRfN6bS)

- **问题 / 瓶颈** · 迭代统计难从原始高维 SGD 轨迹直接读出。
- **核心创新 / 方法** · 以随机微分方程近似对角线性网络 SGD，再用确定性偏微分方程传播风险和曲率等统计。
- **Baseline** · 数值模拟检验理论近似；外部基线待核实。
- **Benchmark** · 高维对角线性网络的风险、曲率和长期收敛。
- **关键结果 / 消融** · 适当参数化下以高概率指数收敛到零风险。
- **适用条件 / 局限** · 限定对角线性架构和合适参数化。

**可复用机制** · 把噪声与漂移拆开建模，利用低维可观测量比较更新规则在训练阶段的作用。

<a id="paper-151314"></a>

## High-Dimensional Robotic Reinforcement Learning with Developing Synergies

[官方论文页](https://neurips.cc/virtual/2026/poster/151314) · [作者来源](https://openreview.net/forum?id=bPifcfpxsk)

- **问题 / 瓶颈** · 冗余执行器空间探索低效，快速改解码器又会使潜动作语义漂移。
- **核心创新 / 方法** · 从随机潜动作映射起步，在策略优化中缓慢更新带结构正则的协同矩阵。
- **Baseline** · SAC、近期高维控制方法与通用潜动作瓶颈。
- **Benchmark** · 连续控制，包括高维人形与过驱动肌骨系统。
- **关键结果 / 消融** · 摘要报告优于 SAC；消融支持缓慢且结构化演化的作用。
- **适用条件 / 局限** · 适用于能压缩为紧凑协调结构的执行器任务。

**可复用机制** · 把策略探索放在低维坐标，缓慢学习到执行空间的映射以保持经验可用。

<a id="paper-149062"></a>

## High dimensional theory of two-phase optimizers

[官方论文页](https://neurips.cc/virtual/2026/poster/149062) · [作者来源](https://openreview.net/forum?id=t9Qd8Imsn2)

- **问题 / 瓶颈** · 通信减少的局部训练不一定等同于单机的信噪折中。
- **核心创新 / 方法** · 在高维回归分析 LA-DiLoCo，另研究内外动量叠加改变有效 Hessian 谱。
- **Baseline** · SGD、单工作者 LA、多工作者版本及有动量 SLA。
- **Benchmark** · 高维线性回归中的信噪和谱动态。
- **关键结果 / 消融** · 多工作者噪声更高但可调参缓解；双动量变换可加速，分析里 Nesterov 效应最大。
- **适用条件 / 局限** · 理论限定线性回归与所分析变体；大模型需另验。

**可复用机制** · 调同步和局部更新频率时同时监测噪声放大，而非只优化通信吞吐。

<a id="paper-154447"></a>

## High Entropy Regularization Leads to Symmetry Equivariant Policies in Dec-POMDPs

[官方论文页](https://neurips.cc/virtual/2026/poster/154447) · [作者来源](https://openreview.net/forum?id=DU3r4vMx02)

- **问题 / 瓶颈** · 独立策略各自学到不同约定，导致交叉配对不兼容。
- **核心创新 / 方法** · 以高熵正则推动对称等变的联合策略；训练后贪心化尝试恢复自博弈得分。
- **Baseline** · 独立 PPO、常规熵系数和不同训练种子。
- **Benchmark** · Hanabi、Overcooked、Yokai；自博弈与跨种子回报。
- **关键结果 / 消融** · 表格 softmax 理论下充分高熵收敛到同一等变策略，实测熵显著影响配对效果。
- **适用条件 / 局限** · 高熵极限未必给出最优等变策略；深度策略只获实验证据。

**可复用机制** · 需要与独立队友协调时，把打破约定分歧列为训练目标，再独立检查部署贪心化。

<a id="paper-151538"></a>

## Higher-Order Action Supervision Makes A Strong Policy Class

[官方论文页](https://neurips.cc/virtual/2026/poster/151538) · [作者来源](https://openreview.net/forum?id=ZusaOFN1fJ)

- **问题 / 瓶颈** · 只拟合动作标签忽略时间一致性，可能导致控制不稳。
- **核心创新 / 方法** · 在现有策略的零阶动作项旁加入一阶动作监督，不改变策略结构。
- **Baseline** · 原始离线 RL 框架和只用零阶动作监督的策略。
- **Benchmark** · OGBench、D4RL 连续控制，含低数据分布外测试。
- **关键结果 / 消融** · 摘要报告性能、稳健性与低数据泛化改善。
- **适用条件 / 局限** · 需要能估计可靠的相邻动作变化；真实硬件表现待核实。

**可复用机制** · 对相邻动作的变化单列训练误差，以避免逐时点预测准确却产生不稳定的动作序列。

<a id="paper-150453"></a>

## Higher-Order Cell Tracking Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/150453) · [作者来源](https://openreview.net/forum?id=hvvdcmMum3)

- **问题 / 瓶颈** · 分裂让节点嵌入混合不同谱系，共享节点的候选边又不一定同类。
- **核心创新 / 方法** · 以候选链接为 token，用三维几何先验控制边间注意力。
- **Baseline** · 含 LoRA 微调的竞争 Transformer 跟踪器。
- **Benchmark** · Cell Tracking Challenge 与细菌分裂基准；跟踪错误和标注效率。
- **关键结果 / 消融** · 400 条交互标注后报告跟踪错误减少 59%，对照改善 6.75%。
- **适用条件 / 局限** · 依赖分割和候选边召回；面向所测成像体系。

**可复用机制** · 若可学习标签定义在匹配边且端点邻接信息弱，直接在关联候选之间做结构化推理。

<a id="paper-154030"></a>

## High-Fidelity Boltzmann Samplingvia Physical Prior Lifted Continuous GFlowNets

[官方论文页](https://neurips.cc/virtual/2026/poster/154030) · [作者来源](https://openreview.net/forum?id=GmYzBqp2bI)

- **问题 / 瓶颈** · 直接在高维空间学习采样轨迹时，先验难利用且训练不稳。
- **核心创新 / 方法** · 用带参考分布和映射的参考空间表示先验，在其中采用参考加权轨迹平衡目标。
- **Baseline** · MCMC、扩散式 ASBS 和现有连续 GFlowNet 路线。
- **Benchmark** · 摘要列五类基准；此处提取合成 LJ-55 的误差与速度。
- **关键结果 / 消融** · 在 LJ-55 相对 ASBS 获更低误差，报告约 36 倍加速。
- **适用条件 / 局限** · 参考分布与映射的选择关系到覆盖，具体条件待核实。

**可复用机制** · 将参考变量用于连续采样训练，使轨迹匹配围绕已有结构学习而非从无信息初始分布起步。

<a id="paper-153009"></a>

## High Performance Differentially Private Fine-Tuning using Dataset Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/153009) · [作者来源](https://openreview.net/forum?id=OeKp0prARQ)

- **问题 / 瓶颈** · 对每个新模型使用 DP-SGD 会重复消耗预算。
- **核心创新 / 方法** · 用公共骨干提取激活统计，将统计差分隐私化后再合成训练数据。
- **Baseline** · 同算力 DP-SGD 与其他基于生成的私有方法。
- **Benchmark** · CIFAR-10、CIFAR-100；四档隐私预算和跨架构迁移。
- **关键结果 / 消融** · CIFAR-100 在 ε=1 时比同算力 DP-SGD 提高 5.8%，合成数据可跨视觉架构复用。
- **适用条件 / 局限** · 隐私后处理要求下游仅使用已发布产物；效用依赖公共表示。

**可复用机制** · 把隐私预算花在可共享统计上，以支持不重复访问私有库的下游训练。

<a id="paper-149977"></a>

## High-probability Convergence of Gradient Methods under Markovian Stochasticity

[官方论文页](https://neurips.cc/virtual/2026/poster/149977) · [作者来源](https://openreview.net/forum?id=lmm5OfBNv5)

- **问题 / 瓶颈** · 独立样本的集中结论不直接适用马尔可夫噪声。
- **核心创新 / 方法** · 构造小批梯度估计；有界方差下对加速更新加入裁剪，并以依赖集中界控制尾部。
- **Baseline** · 非凸 SGD 与凸加速方法的不同噪声假设；实验对照待核实。
- **Benchmark** · 马尔可夫随机性下的高概率收敛和预言机复杂度。
- **关键结果 / 消融** · 有界随机性可获非凸保证；裁剪支持有界方差下的凸情形。
- **适用条件 / 局限** · 理论依赖对应凸性、马尔可夫条件与估计器。

**可复用机制** · 评估在线训练可靠性时按混合依赖和噪声尾部选小批与裁剪，不套独立抽样置信界。

<a id="paper-149324"></a>

## High-Probability Minimax Adaptive Estimation in Besov Spaces via Online-to-Batch

[官方论文页](https://neurips.cc/virtual/2026/poster/149324) · [作者来源](https://openreview.net/forum?id=qzG736XgI9)

- **问题 / 瓶颈** · Besov 回归在噪声和正则度均未知时难取得自适应高概率界。
- **核心创新 / 方法** · 逐步处理噪声梯度，动态裁剪，并用平方损失结构及自归一化集中不等式做在线到批量转换。
- **Baseline** · 同类极小极大估计目标；具名对照待核实。
- **Benchmark** · 次指数噪声下的 Besov 回归，指标为积分平方误差与在线遗憾。
- **关键结果 / 消融** · 证明高概率极小极大最优率，且遗憾界按竞争者的 L1 范数缩放。
- **适用条件 / 局限** · 依赖次指数噪声和平方损失；其他损失的结论待核实。

**可复用机制** · 未知噪声时把裁剪水平设为可在线调整的量，再证明批量风险而非只报平均误差。

<a id="paper-150738"></a>

## High Probability Risk Control for Online Policy Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150738) · [作者来源](https://openreview.net/forum?id=fklVyus79k)

- **问题 / 瓶颈** · 策略影响后续数据分布，直接复用经验风险可能不可靠。
- **核心创新 / 方法** · 用 Sinkhorn 近似计算置换加权风险，以 Gaussian bootstrap 构造同时上界，选择上界低于容限的策略。
- **Baseline** · 标准重要性加权风险估计器及策略风险控制基线。
- **Benchmark** · 在线策略学习，指标为风险、估计方差及是否控制在目标容限。
- **关键结果 / 消融** · 估计器最坏方差不高于重要性加权，策略风险保证为渐近；摘要报告经验风险更低。
- **适用条件 / 局限** · 有限轮次覆盖、采样条件和计算成本待核实。

**可复用机制** · 把风险评估与选择分开，用同时有效的上界处理候选策略之间的选择偏差。

<a id="paper-152158"></a>

## HiLoc: A Hierarchical Representation Method for Spatial Localization in Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152158) · [作者来源](https://openreview.net/forum?id=V5T2vPmvxO)

- **问题 / 瓶颈** · 原始数字 token 邻近性不反映空间距离，细粒度单级分箱扩张词表。
- **核心创新 / 方法** · 用特殊 token 先输出粗网格再输出内部单元；分辨率用增加层级提升。
- **Baseline** · 文本坐标和单级量化位置 token。
- **Benchmark** · 检测与定位基准，小目标、高 IoU 门槛、复杂指代；训练数据包含 HiRef-500K。
- **关键结果 / 消融** · 作者报告在高精度和复杂指代设置表现较强。
- **适用条件 / 局限** · 层级错误传播及数据增益与编码增益的拆分待核实。

**可复用机制** · 以序列长度交换词表规模，并单独测粗层选错时的细定位误差。

<a id="paper-151571"></a>

## HiLoRA: Adaptive Hierarchical LoRA Routing for Training-Free Domain Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/151571) · [作者来源](https://openreview.net/forum?id=ZbObuTCYWv)

- **问题 / 瓶颈** · 无任务标签时激活整块固定数量 LoRA 可能浪费参数或分配不足。
- **核心创新 / 方法** · 按序列层的高斯似然选 LoRA 并分配秩一单元，再按 token 激活信息量高的分量。
- **Baseline** · 固定整块激活和需要额外训练的既有路由；具名对照待核实。
- **Benchmark** · 领域泛化，衡量准确率和推理吞吐。
- **关键结果 / 消融** · 摘要报告相对现有基线准确率增益最高达 70%，吞吐相近。
- **适用条件 / 局限** · 最大增益口径及高斯似然条件待核实。

**可复用机制** · 将适配器调度拆为粗粒度模块选择与细粒度预算分配两步。

<a id="paper-151828"></a>

## HIMMEL: Hierarchical Interleaved Multi-stream Motion Encoding for Long Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/151828) · [作者来源](https://openreview.net/forum?id=Xf9DEJzFEl)

- **问题 / 瓶颈** · 稠密解码昂贵且 token 多，稀疏取帧易漏运动。
- **核心创新 / 方法** · ViT 编码 I 帧，轻量适配器融合运动向量、残差和 I 帧上下文，并对比对齐冻结视觉空间。
- **Baseline** · 稠密 32 帧、MSE 对齐及不同流组成。
- **Benchmark** · Video-MME 准确率、上下文 token 和端到端单题时间。
- **关键结果 / 消融** · 61.2% 到 63.5%，token 用量约为对照的 1/3.6，2.75 秒降至 1.03 秒；InfoNCE 比 MSE 高 1.5 点。
- **适用条件 / 局限** · 依赖编码域信号的可访问性，跨编码格式、硬件耗时待核实。

**可复用机制** · 把场景语义与运动的采样率解耦，并实测解码而非只统计模型 token。

<a id="paper-153151"></a>

## Hindsight Relabeling is All You Need for Reach-Avoid Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153151) · [作者来源](https://openreview.net/forum?id=NUNqj0j1C6)

- **问题 / 瓶颈** · 将避让写进固定状态与代价函数会限制部署时的新区域约束。
- **核心创新 / 方法** · 用提示 token 表示目标和区域，从离线轨迹做避让条件的事后重标以训练决策 Transformer。
- **Baseline** · 离线目标条件强化学习及在测试条件下重训的对照。
- **Benchmark** · 17 个任务、环境和设置，测未见区域大小、数量的零样本归一化代价与到达率。
- **关键结果 / 消融** · 一个零样本设置归一化代价比最佳重训对照改善 35.7%，维持较高到达率。
- **适用条件 / 局限** · 依赖离线数据覆盖；单一设置的改善幅度不能外推。

**可复用机制** · 把可变约束作为条件输入，用离线轨迹重新标注可满足的条件来增加监督。

<a id="paper-153982"></a>

## Hint Tuning: Less Data Makes Better Reasoners

[官方论文页](https://neurips.cc/virtual/2026/poster/153982) · [作者来源](https://openreview.net/forum?id=H4dJe9Ql6C)

- **问题 / 瓶颈** · 长推理模型对容易题也使用冗长推理。
- **核心创新 / 方法** · 用无提示、短提示和完整推理三种条件自动构造难度监督。
- **Baseline** · 大量蒸馏数据与强化学习的做法；具名结果待核实。
- **Benchmark** · Qwen3-Thinking、DeepSeek-R1-Distill 的 4B–32B 版本，五个基准，衡量 token 和准确率。
- **关键结果 / 消融** · 约一千条自标注样本获得 24–66% token 减少，平均 31.5%，保持有竞争力的准确率。
- **适用条件 / 局限** · 要求有相匹配的指令模型，困难度代理跨模型通用性待核实。

**可复用机制** · 用最小充分提示长度构造可操作的难度标签，再评估生成成本和准确率的折中。

<a id="paper-155067"></a>

## Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop Question Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/155067) · [作者来源](https://openreview.net/forum?id=8ikJufFS3i)

- **问题 / 瓶颈** · 固定图和固定分解深度忽略语料实际能支持的查询粒度。
- **核心创新 / 方法** · 检索后检测当前节点是否解决，未解决时依依赖二分，再验证语义覆盖。
- **Baseline** · 图式 PropRAG 和迭代式 IRCoT。
- **Benchmark** · 三个多跳问答基准，含全语料检索，指标 EM 和 F1。
- **关键结果 / 消融** · 平均 57.9 EM、69.3 F1，较 PropRAG 高 5.6、3.9 点；全语料为 53.4 EM、65.2 F1。
- **适用条件 / 局限** · 终止判定质量、额外检索开销和语料变化下的鲁棒性待核实。

**可复用机制** · 让证据充分性控制查询树深度，并测提前终止造成的漏检。

<a id="paper-154068"></a>

## HIRaD: Hidden Interaction Inference from Predictive Radar Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/154068) · [作者来源](https://openreview.net/forum?id=GPulVqYgS1)

- **问题 / 瓶颈** · 稀疏毫米波回波中对象信息难分离，直接检测不稳定。
- **核心创新 / 方法** · 计算运动延续先验与观测后验的残差轨迹，将其压缩成语言对齐的瓶颈，并与节点级摘要共同提示冻结语言模型。
- **Baseline** · 雷达描述和交互识别的强基线及前缀、潜状态、残差轨迹消融。
- **Benchmark** · 弱对象可观察条件下的雷达描述和交互理解，指标待核实。
- **关键结果 / 消融** · 摘要报告优于基线，消融支持状态表示、残差和前缀作用。
- **适用条件 / 局限** · 假设物体约束在人体运动中留下足够信号，其他传感器和隐交互未确证。

**可复用机制** · 把观测校正量当作交互证据，与完整后验状态分开编码。

<a id="paper-155909"></a>

## HIST3R: Rectified State Decomposition from History for Streaming 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/155909) · [作者来源](https://openreview.net/forum?id=1vnqEsI3RD)

- **问题 / 瓶颈** · 只调整步幅无法消除单帧候选方向偏差。
- **核心创新 / 方法** · 用历史递归状态整流方向，再以观测和历史的视觉差异设定更新增益。
- **Baseline** · 现有免训练隐式记忆方法和 CUT3R 变体。
- **Benchmark** · ScanNet、TUM-Dynamics、7-Scenes、NRGBD，任务为位姿、重建和视频深度。
- **关键结果 / 消融** · 千帧 ATE 相对下降 23.87%、33.65%；五百帧两套重建基准分别报告相对改善 56.52%、33.96%。
- **适用条件 / 局限** · 后两项指标定义、额外缓存和相机运动分布待核实。

**可复用机制** · 将方向和步长作为两个互补消融轴，测试单帧错误是否会累积成长期偏向。

<a id="paper-154697"></a>

## Historical Relative Policy Optimization for Bootstrapping LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/154697) · [作者来源](https://openreview.net/forum?id=BgpQsVH3WO)

- **问题 / 瓶颈** · 只做组内归一化可能掩盖整体性能下降。
- **核心创新 / 方法** · 用历史最佳组均值的运行上界构造优势参照；完全无正信号时触发高奖励样本回放。
- **Baseline** · GRPO 变体。
- **Benchmark** · 多模型和推理基准，关注训练稳定、收敛速度和最终表现。
- **关键结果 / 消融** · 摘要报告三个维度均改善，幅度待核实。
- **适用条件 / 局限** · 历史奖励分布变动、罕见高值和回放偏差的影响待核实。

**可复用机制** · 把组间历史基准与组内相对优势分开跟踪，按零正例条件控制回放频次。

<a id="paper-153050"></a>

## History-Aware Conformal Prediction Sets for Censored Time-to-Event Outcomes

[官方论文页](https://neurips.cc/virtual/2026/poster/153050) · [作者来源](https://openreview.net/forum?id=OPFzq5afFw)

- **问题 / 瓶颈** · 仅用基线特征导致区间过宽，并忽略当前幸存者目标。
- **核心创新 / 方法** · 按时变混杂调整右删失权重，给幸存者构造共形预测集，并提出双稳健扩展。
- **Baseline** · 仅用基线协变量的生存预测区间比较器。
- **Benchmark** · 模拟和两个公开数据集，考察覆盖率与区间长度中位数。
- **关键结果 / 消融** · 模拟区间最高缩短 75% 且近名义覆盖，公开数据第五年预测最长缩短 60%。
- **适用条件 / 局限** · 基本方法依赖删失权重一致估计，覆盖为幸存者群体的渐近性质。

**可复用机制** · 明确区间服务于当前仍在风险集的人，再分开处理观测历史和选择性删失。

<a id="paper-152292"></a>

## Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/152292) · [作者来源](https://openreview.net/forum?id=U9JnXUgBes)

- **问题 / 瓶颈** · 对称距离抹掉可达方向差异。
- **核心创新 / 方法** · 以潜位移的线性泛函表示首达时间，并以首达时间回归锚定 HILP 式一致性。
- **Baseline** · HILP 式基础策略与既有离线导航方法。
- **Benchmark** · 离线迷宫运动中的多段导航；指标待核实。
- **关键结果 / 消融** · 作者报告导航优势，并给出在潜在线性闭合下的识别以及受瞬态谱半径影响的误差界。
- **适用条件 / 局限** · 依赖潜在线性闭合，证据以迷宫数据为主。

**可复用机制** · 用有向时间代价校准规划几何，同时检查复合路径上的局部误差是否被放大。

<a id="paper-153764"></a>

## Hodge Laplacian Quasi-Harmonic Flows for Option Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/153764) · [作者来源](https://openreview.net/forum?id=Ipo5Xh353j)

- **问题 / 瓶颈** · 节点拉普拉斯技能易集中在少数极值，而纯循环在树状支路近乎不活跃。
- **核心创新 / 方法** · 用一阶 Hodge 拉普拉斯的调和边流保持环流，在弱调和区加入最小模量的非调和特征向量。
- **Baseline** · 纯调和流选项及已有技能发现方法。
- **Benchmark** · 含树状附属结构的状态图，首达时间指标。
- **关键结果 / 消融** · 作者报告准调和选项改善首达时间分析和实验表现。
- **适用条件 / 局限** · 依赖可估计状态转移图及谱，扩大规模的成本和鲁棒性待查。

**可复用机制** · 设计技能时分开检查骨干环路与支路覆盖，避免循环运动看似丰富却从不访问死端。

<a id="paper-150937"></a>

## HOGWARTS: Mitigating Perspective Distortion for 6DoF Head Pose Estimation via Virtual Camera Space

[官方论文页](https://neurips.cc/virtual/2026/poster/150937) · [作者来源](https://openreview.net/forum?id=eBZJLTaCK2)

- **问题 / 瓶颈** · 画面边缘的透视畸变会与真实外观、姿态混淆，旋转增强还可能带来图像标签失配。
- **核心创新 / 方法** · 以共光心虚拟相机诱导单应变换，并用针孔模型补偿尺度变化后估计三维平移。
- **Baseline** · 既有人脸头姿方法与普通矩形裁剪路线。
- **Benchmark** · ARKitFace、BIWI，强畸变及跨域 6DoF 估计。
- **关键结果 / 消融** · 摘要报告在两类设置优于既有方法，数值待核。
- **适用条件 / 局限** · 需相机模型支持虚拟重投影，非针孔镜头适用性待核。

**可复用机制** · 将增强和标签一起变换到虚拟相机，再按目标距画面中心的距离检查误差。

<a id="paper-149361"></a>

## Holistic EvoLution via Intrinsic eXchange for Unified Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149361) · [作者来源](https://openreview.net/forum?id=qbmMJso3Wa)

- **问题 / 瓶颈** · 传统后训练依赖外部标注，两个能力缺少闭环反馈。
- **核心创新 / 方法** · 理解分支以似然增益奖励训练生成；生成分支提供重建证据并配合提示对齐训练理解。
- **Baseline** · Bagel 基线。
- **Benchmark** · 模型训练分辨率 512 像素，1024 像素测 T2I-CompBench、GenEval、DPG-Bench、WISE。
- **关键结果 / 消融** · 分别领先 5.6、7.1、1.54、0.02。
- **适用条件 / 局限** · 两支反馈可能共享偏差；独立外部评审和多轮稳定性待核。

**可复用机制** · 固定数据桥和训练预算，比双向交换、单向反馈与静态标注。

<a id="paper-154893"></a>

## Holistic Scaling Laws for Optimal Mixture-of-Experts Architecture Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154893) · [作者来源](https://openreview.net/forum?id=A8xK024UOt)

- **问题 / 瓶颈** · 只按每词元算力比较会混入参数膨胀效应。
- **核心创新 / 方法** · 用结构约束和隐层维度保序性质将高维架构搜索拆为三次和二次两阶段，再拟合规模规律。
- **Baseline** · 仅算力约束及固定非 MoE 变量的缩放方法为背景。
- **Benchmark** · 670 余 MoE，训练计算量 10^18 至 3×10^20 FLOPs。
- **关键结果 / 消融** · 作者称规模越大，近最优配置带越宽；搜索复杂度由十六次降为三次加二次。
- **适用条件 / 局限** · 结论依赖评测架构和硬件预算，域外套用待核。

**可复用机制** · 报告三项资源约束与近最优区间，在区间内按吞吐和显存选结构。

<a id="paper-154530"></a>

## Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154530) · [作者来源](https://openreview.net/forum?id=Cu9FVR16z6)

- **问题 / 瓶颈** · 重建仅覆盖已观测视角，通用视频扩散相机控制不够精确。
- **核心创新 / 方法** · 融合静态多视图与匹配源帧动态渲染的 RGB-D，并加入有效掩码、相机射线、三维跟踪词元。
- **Baseline** · 已有新视角视频合成方案，统一使用同一下游重建器。
- **Benchmark** · 留出目标视角的深度一致性、相机遵循及 VAE 中间特征读出。
- **关键结果 / 消融** · 更多几何信息改善相机遵循，生成深度更接近留出重建。
- **适用条件 / 局限** · 依赖源视频几何、跟踪和静动区分质量。

**可复用机制** · 用固定重建器区分像素合理性与几何一致性，逐项加几何约束。

<a id="paper-152255"></a>

## HoloGene: Learning to Lift Sliced Spatial Transcriptomics to Holistic 3D Gene Fields

[官方论文页](https://neurips.cc/virtual/2026/poster/152255) · [作者来源](https://openreview.net/forum?id=UPzmDuUKQ3)

- **问题 / 瓶颈** · 各向同性坐标编码忽略横向和轴向采样落差，切面批次差异可能冒充真实变化。
- **核心创新 / 方法** · 图自编码压缩表示，单独调制深度条件，并在同类上下文内对齐潜特征相关性。
- **Baseline** · 通用隐式神经表示和适配领域基线。
- **Benchmark** · 以留出的已测切面为参照，测重建、结构保留和切面特异泄漏。
- **关键结果 / 消融** · 作者称深度解耦改善轴向泛化，条件相关性对齐最能减少切面泄漏。
- **适用条件 / 局限** · 需预配准且伪标签可靠；稀疏方向真实突变的保留情况待核。

**可复用机制** · 对非生物切片重建也用留切面验证，并在相同正常结构下检查批次残留。

<a id="paper-153647"></a>

## HomeFlow: A Data Flywheel for Smart Home Agent Training with Verifiable Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153647) · [作者来源](https://openreview.net/forum?id=Jm1U7gkn7r)

- **问题 / 瓶颈** · 模糊意图和环境状态变化使轨迹质量难检验。
- **核心创新 / 方法** · Blueprint 编译状态条件，模拟器引导树搜索生成可验证轨迹，再做监督微调和逐步验证奖励。
- **Baseline** · GPT-5.5 及作者训练的 4B、8B 模型；逐组件对照待核。
- **Benchmark** · SmartHome-Bench 任务完成率。
- **关键结果 / 消融** · 4B 为 84.60%，8B 为 87.03%，后者高于 GPT-5.5 约 1.23 个百分点。
- **适用条件 / 局限** · 依赖模拟器状态与可编译任务；真实家庭场景未由摘要证实。

**可复用机制** · 固定意图分布对比无验证合成及状态验收合成，单列伪成功率。

<a id="paper-153857"></a>

## Homological Barriers to Stable Local Nash Dynamics in Quadratic Zero-Sum Games

[官方论文页](https://neurips.cc/virtual/2026/poster/153857) · [作者来源](https://openreview.net/forum?id=ICudniinwz)

- **问题 / 瓶颈** · 非凹博弈即使目标均衡可明确求出，也可能无法用连续规则全局稳定吸引。
- **核心创新 / 方法** · 在可缩状态空间上用同调论证带孔均衡集合的障碍，构造盒约束二次零和例并分析扰动。
- **Baseline** · 理论对照为连续、逐点固定均衡的确定性规则。
- **Benchmark** · 二次盒约束零和博弈、任意阶同调构造和小扰动族。
- **关键结果 / 消融** · 证明二次已足以出现障碍，且扰动后仍有正测度实例。
- **适用条件 / 局限** · 限于论文定义的稳定全局吸引与更新规则假设。

**可复用机制** · 遇到有环的目标集时区分局部收敛、吸引单个组件和吸引整个集合的要求。

<a id="paper-139314"></a>

## Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots

[官方论文页](https://neurips.cc/virtual/2026/poster/139314) · [作者来源](https://openreview.net/forum?id=XvDLyFw8OO)

- **问题 / 瓶颈** · 只比较固定响应的相似度，无法完整反映蜜罐在运行中的表现。
- **核心创新 / 方法** · 以多种后端为参照统一对照协议，另设控制任务监测评估组件的能力变化。
- **Baseline** · 规则型蜜罐。
- **Benchmark** · 16 项后端应用，比较模拟真实性、交互长度与运行成本。
- **关键结果 / 消融** · 低成本语言模型蜜罐的交互更长且更少被识别，配置调整会改变二者折中。
- **适用条件 / 局限** · 结果依赖后端和评测条件；实际部署外推待核。

**可复用机制** · 对防御模拟器在相同预算下做真实性与成本联合回归，保留规则参考。

<a id="paper-149865"></a>

## HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/149865) · [作者来源](https://openreview.net/forum?id=mev2NLpHq9)

- **问题 / 瓶颈** · 现有视觉 RLVR 数据少有贯穿全链的视觉证据。
- **核心创新 / 方法** · 组合逻辑依赖的实例级子问题，并以唯一数值答案结束；代理任务题型与下游不同。
- **Baseline** · 同模型有无 HopChain 训练数据，以及半多跳、单跳消融。
- **Benchmark** · 两个 Qwen3.5 规模，24 个多模态基准；另评长推理长度。
- **关键结果 / 消融** · 两种模型均改善 20 项；五代表基准的全链、半链、单跳平均分为 70.4、66.7、64.3。
- **适用条件 / 局限** · 依赖可靠实例标注与可验证最终答案。

**可复用机制** · 以等预算拆开多跳数量和前后依赖性，验证迁移来自组合训练。

<a id="paper-148354"></a>

## HOPE: Hand-Object Pressure Estimation from Monocular Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/148354) · [作者来源](https://openreview.net/forum?id=yVwONiM3oG)

- **问题 / 瓶颈** · 不同传感形态监督坐标不一致，单帧平面估计难支持动态接触。
- **核心创新 / 方法** · 将手套、平面传感与几何接触映射到手网格；持续顶点词元聚合单目视频，再用接触门控压力。
- **Baseline** · 接触专用及平面压力基线。
- **Benchmark** · OpenTouch、PressureVisionDB 和手物接触评测。
- **关键结果 / 消融** · 摘要报告可共同预测接触与压力，并从有手套监督迁移到裸手视频。
- **适用条件 / 局限** · 遮挡、网格估计误差和裸手压力真值验证待核。

**可复用机制** · 选不随传感器改变的物理坐标统一稀疏真值，用接触先验约束压力零点。

<a id="paper-155494"></a>

## HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/155494) · [作者来源](https://openreview.net/forum?id=5B4SMDYGLq)

- **问题 / 瓶颈** · 组合结构上的高阶传递扩展成本高。
- **核心创新 / 方法** · 直接从 Hasse 图分解提取位置和结构编码，以组合表示规模线性处理并保持置换等变性。
- **Baseline** · 高阶消息传递模型。
- **Benchmark** · 分子与拓扑学习基准，比较预测表现和速度。
- **关键结果 / 消融** · 摘要称质量达到或超过既有方法，运行更快。
- **适用条件 / 局限** · 线性复杂度按组合表示大小计，构造高阶域本身的成本待核。

**可复用机制** · 把结构构建成本与编码成本分开，验证无需传递时的效能。

<a id="paper-154836"></a>

## Horizon Adaptive Offline Policy Learning via Value Stitching

[官方论文页](https://neurips.cc/virtual/2026/poster/154836) · [作者来源](https://openreview.net/forum?id=Aak239DsQk)

- **问题 / 瓶颈** · 固定步数回推可能积累偏差，复杂多阶段任务各段所需跨度不同。
- **核心创新 / 方法** · 从数据直接监督给定未来状态与跨度的辅助价值，用拼接策略选回报最大的两项组合并递归合成。
- **Baseline** · 固定步备份、扩展时域及生成式价值的离线强化学习方法。
- **Benchmark** · OGBench 50 项任务，重点对照复杂长时决策。
- **关键结果 / 消融** · 摘要报告整体优于对照，长时复杂任务表现尤佳。
- **适用条件 / 局限** · 离线数据须覆盖可操作的子目标；分布外拼接错误待核。

**可复用机制** · 对照固定跨度与自适应跨度，按子目标有效性和任务阶段诊断备份错误。

<a id="paper-153911"></a>

## Horizon-Stream: Long-Horizon Attention for Streaming 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/153911) · [作者来源](https://openreview.net/forum?id=HlS4kqyNKV)

- **问题 / 瓶颈** · 固定窗口截断持久证据，统一历史更新会产生缓存饱和或注意峰。
- **核心创新 / 方法** · 线性注意按通道学习时间衰减，局部注意用时空旋转位置编码匹配，度量读出词元恢复尺度与刚性位姿。
- **Baseline** · 滑窗、无门控递推、普通因果注意是方法对照路线。
- **Benchmark** · 48 帧训练，测试序列超过 10,000 帧；测重建、时空成本与长序列稳定性。
- **关键结果 / 消融** · 摘要报告在常内存和线性时间下保持长程稳定，重建表现领先。
- **适用条件 / 局限** · 超长序列数据和回环条件需核对。

**可复用机制** · 对长程状态和局部匹配分别消融，单列尺度漂移、位姿抖动与内存。

<a id="paper-154154"></a>

## Horizontal Diffusion Models: Score-based Generative Modeling on Frame-Connection Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/154154) · [作者来源](https://openreview.net/forum?id=Fr0DlZvA04)

- **问题 / 瓶颈** · 流形生成常需要难以计算的全局测地结构。
- **核心创新 / 方法** · 通过 Levi-Civita 水平分布提升扩散与得分场，水平 KL 目标化为欧式得分匹配。
- **Baseline** · 依赖全局测地、平行移动或谱算子的流形生成路线。
- **Benchmark** · 参数曲面及科学数据，另分析与曲率有关的泛化界。
- **关键结果 / 消融** · 摘要称支持非平凡几何和拓扑并得到高保真结果。
- **适用条件 / 局限** · 需局部度量与联络；曲率较大时误差和开销待核。

**可复用机制** · 对比相同得分网络在局部几何提升与平面近似下的接缝及分布误差。

<a id="paper-148576"></a>

## HoTS: Homophily-Aware Temperature Scaling for Graph Neural Network Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/148576) · [作者来源](https://openreview.net/forum?id=woxrGUwgJ3)

- **问题 / 瓶颈** · 有相同分数但邻域结构不同的节点可能需要不同温度。
- **核心创新 / 方法** · 从上下文随机块模型分析温度与同配性的关系，再用三参数后处理调整节点温度。
- **Baseline** · 统一温度与八种图校准基线。
- **Benchmark** · 18 个节点分类基准、两个骨干；ECE 与选择性分类排名。
- **关键结果 / 消融** · 平均 ECE 4.66%，平均排名与置信排序最优。
- **适用条件 / 局限** · 解析近似适用于文中正信号同配条件，异配图需独立检验。

**可复用机制** · 把温度按邻域同配区间画出，即使分类预测不变，也按置信排序验证筛选效果。

<a id="paper-154488"></a>

## How Accurately Can a Gaussian Approximate Stochastic Approximation Iterates?

[官方论文页](https://neurips.cc/virtual/2026/poster/154488) · [作者来源](https://openreview.net/forum?id=DE5fL6A9eH)

- **问题 / 瓶颈** · 渐近正态无法直接给出短时迭代的可信尾界。
- **核心创新 / 方法** · 用离散 OU 过程近似重标度迭代，对多种步长建立递推协方差下的 Wasserstein-1 界。
- **Baseline** · 经典极限高斯近似为理论对照。
- **Benchmark** · 理论上界、匹配下界及仿真检验。
- **关键结果 / 消融** · 得到任意时间尾界、渐近正态收敛率并验证阶数锐性。
- **适用条件 / 局限** · 适用步长、噪声及稳定性条件需全文核查。

**可复用机制** · 在迭代预算固定时评估有限步和渐近协方差对风险阈值的差异。

<a id="paper-155691"></a>

## How are linear representations learned? Exact solutions to the dynamics of abstraction

[官方论文页](https://neurips.cc/virtual/2026/poster/155691) · [作者来源](https://openreview.net/forum?id=3fgBRPXZHw)

- **问题 / 瓶颈** · 已有线性表征研究多只观察训后状态。
- **核心创新 / 方法** · 求解最小线性网络的完整训练轨迹，并比较 erf 与 ReLU 的方向对齐动力学。
- **Baseline** · 线性理论、erf 与 ReLU 机制对照。
- **Benchmark** · 最小网络理论、DINOv3 与 Gemma 4 证据及线性探针泛化。
- **关键结果 / 消融** · 目标与数据几何共同决定线性终态；两种非线性均削弱后激活的抽象对齐。
- **适用条件 / 局限** · 精确动力学限最小设置，开放模型证据主要是规律检验。

**可复用机制** · 比较跨检查点和前后激活探针，避免把测量位点差异当作概念未形成。

<a id="paper-150706"></a>

## How Can SignSGD Outperform SGD? A Functional Scaling Law Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/150706) · [作者来源](https://openreview.net/forum?id=g7xKEe1njs)

- **问题 / 瓶颈** · 符号化梯度何时带来数据效率尚不明确。
- **核心创新 / 方法** · 将尺度律分为信号学习与噪声累积，识别曲率对齐噪声下的逆平方根预条件。
- **Baseline** · SGD；另讨论 Adam 与 RMSprop。
- **Benchmark** · 对角线性回归、合成实验及语言模型损失曲线。
- **关键结果 / 消融** · 困难任务中 signSGD 学得更快但忘噪更慢，容易任务相近。
- **适用条件 / 局限** · 严格推导依赖对角特征和幂律谱。

**可复用机制** · 调优化器时将信号拟合与噪声遗忘分别测量，避免单凭早期斜率决策。

<a id="paper-139218"></a>

## How Complete Should a Reference Be? A Benchmark Audit for Fluorescence Spot Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/139218) · [作者来源](https://openreview.net/forum?id=eBkHgucGKp)

- **问题 / 瓶颈** · 标注漏掉弱点可能改变模型排名。
- **核心创新 / 方法** · 重做宽松和严格参考，并模拟随机和结构化缺标，保持匹配协议固定。
- **Baseline** · 原始标注与传统、学习式检测器。
- **Benchmark** · FISH_spots，点匹配 F1、排序及第一名变化。
- **关键结果 / 消融** · 只改变参考标注就可能改变优胜模型，即使整体排名仍相关。
- **适用条件 / 局限** · 评估代表该数据及参考定义。

**可复用机制** · 把参考标签视作可扰动变量，测试选型在可接受标注口径下是否稳定。

<a id="paper-150878"></a>

## How Data Augmentation Shapes Neural Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/150878) · [作者来源](https://openreview.net/forum?id=eiZLHRQOAE)

- **问题 / 瓶颈** · 泛化分数不能表明增强如何改变内部表示。
- **核心创新 / 方法** · 将隐藏表示嵌入对尺度、平移、旋转和反射不变的形状空间。
- **Baseline** · 不同增强强度和类型、跨架构与种子。
- **Benchmark** · 表示距离、形状变化和集成收益；具体数据待核实。
- **关键结果 / 消融** · 增强类型沿不同方向改变表示，形状信息可预测有益集成。
- **适用条件 / 局限** · 依赖所用距离与表示提取方式。

**可复用机制** · 先消除无关几何变换，再按方向差异寻找互补模型。

<a id="paper-155951"></a>

## How Data Scales in Agentic Reinforcement Learning: Laws and Synthesis Strategies

[官方论文页](https://neurips.cc/virtual/2026/poster/155951) · [作者来源](https://openreview.net/forum?id=1aqj2GSNwA)

- **问题 / 瓶颈** · 代理强化学习的多类训练数据成本与规模效应差异大。
- **核心创新 / 方法** · 按轴拟合指数并估算合成效率折扣和失效比例，再做预算约束分配。
- **Baseline** · 主要扩大轨迹规模。
- **Benchmark** · Qwen3 4B/8B/14B；数学、代码和网页任务，GRPO 与 PPO。
- **关键结果 / 消融** · 跨配置轴排序稳定，预算配方报告至多 1.7 倍计算效率。
- **适用条件 / 局限** · 数据折扣需用目标任务校准。

**可复用机制** · 分轴测边际收益及合成占比上限，避免把轨迹规模当作唯一预算变量。

<a id="paper-154260"></a>

## How Deep Are Deep GPs, Really? A Sharp Threshold and a Non-Gaussian Limit for Compositional GPs

[官方论文页](https://neurips.cc/virtual/2026/poster/154260) · [作者来源](https://openreview.net/forum?id=F6fd33khoH)

- **问题 / 瓶颈** · 太宽的核使深层组合先验退化为常数。
- **核心创新 / 方法** · 求 RBF 组合 GP 的临界带宽并刻画阈值以下的极限。
- **Baseline** · 先前已知的退化带宽区间。
- **Benchmark** · 多维数模拟及极限分布形态。
- **关键结果 / 消融** · 临界带宽正比于维数平方根量级；下方极限非高斯且非退化。
- **适用条件 / 局限** · 针对给定向量值 GP 与 RBF 设定。

**可复用机制** · 在加深先验前先验证带宽位于非退化区，避免以层数替代核校准。

<a id="paper-148363"></a>

## How deep is your network? Deep vs. shallow learning of transfer operators

[官方论文页](https://neurips.cc/virtual/2026/poster/148363) · [作者来源](https://openreview.net/forum?id=yRDDCROSCe)

- **问题 / 瓶颈** · 深网络优化算子特征函数成本高且调参敏感。
- **核心创新 / 方法** · 固定随机隐藏层，只闭式求输出权重表示特征函数，集成估不确定性。
- **Baseline** · 先进深度算子学习方法。
- **Benchmark** · 随机动力系统等算子谱基准；精度与计算量。
- **关键结果 / 消融** · 摘要报告相似精度时计算量常降低约两个数量级。
- **适用条件 / 局限** · 依赖随机特征覆盖合适的函数空间。

**可复用机制** · 先将谱估计约化为随机基上的闭式拟合，再判断端到端深特征是否值得训练。

<a id="paper-155824"></a>

## How Diffusion Models Memorize

[官方论文页](https://neurips.cc/virtual/2026/poster/155824) · [作者来源](https://openreview.net/forum?id=2b5I5iwFrW)

- **问题 / 瓶颈** · 只在生成终点测相似度难定位隐私信号出现的时段。
- **核心创新 / 方法** · 比较去噪轨迹上条件与无条件后验均值的差异。
- **Baseline** · 普通提示与出现记忆的提示。
- **Benchmark** · 文本到图像扩散的逐步去噪轨迹；具体数据待核实。
- **关键结果 / 消融** · 摘要指出异常记忆轨迹可呈滞后先升后降。
- **适用条件 / 局限** · 结论依赖模型与引导设定；不能单凭曲线认定隐私泄漏。

**可复用机制** · 将双分支差异的时间变化作为内部防护审计信号。

<a id="paper-148769"></a>

## How Do Agentic LLMs Decide to Call Tools? A Scaffold Default Controlled by Suppression

[官方论文页](https://neurips.cc/virtual/2026/poster/148769) · [作者来源](https://openreview.net/forum?id=vBXDOH5EqA)

- **问题 / 瓶颈** · 角色、工具模式和任务文本混合，难解释代理为何调用。
- **核心创新 / 方法** · 只改请求动词构造对照，再分析残差表示和特征因果作用。
- **Baseline** · 执行与分析动词对照。
- **Benchmark** · Python、Java、C++ 共 1,500 对，300 对留出。
- **关键结果 / 消融** · 摘要报告脚手架使调用成为默认，部分分析词激活抑制信号。
- **适用条件 / 局限** · 局限于所测模板与工具任务。

**可复用机制** · 降低提示同时改动的变量，并分清调用的默认倾向与用户意图施加的抑制。

<a id="paper-152989"></a>

## How Does Cutout Benefit Out-of-Distribution Generalization?

[官方论文页](https://neurips.cc/virtual/2026/poster/152989) · [作者来源](https://openreview.net/forum?id=OocrKgTwpF)

- **问题 / 瓶颈** · 直接 Cutout 对领域泛化收益弱甚至有害。
- **核心创新 / 方法** · 用互信息链式法则拆目标：遮挡视图预测标签，完整图补获其缺失信息。
- **Baseline** · 原型式 OOD 学习和直接叠加 Cutout。
- **Benchmark** · 多项 OOD 基准；数据名称待核实。
- **关键结果 / 消融** · 摘要报告优于竞争基线。
- **适用条件 / 局限** · 需要遮挡仍留有标签信息，极端遮挡需重验。

**可复用机制** · 增强视图学习可见部分，完整视图承担被增强删除的信息，避免单视图承担完整监督。

<a id="paper-150798"></a>

## How does feature learning change the function space evolution?

[官方论文页](https://neurips.cc/virtual/2026/poster/150798) · [作者来源](https://openreview.net/forum?id=fKMJIDNPRC)

- **问题 / 瓶颈** · 固定核近似不易表达目标依赖的特征更新。
- **核心创新 / 方法** · 以目标依赖的尖峰高斯协方差近似更新后特征，从输入几何变换分析核谱。
- **Baseline** · 初始各向同性静态核。
- **Benchmark** · 高维两层网络；ReLU 的前导谱扰动。
- **关键结果 / 消融** · 总体谱衰减不变，目标对齐特征的前导特征值和方向会改变。
- **适用条件 / 局限** · 限定比例高维模型与早期更新。

**可复用机制** · 验证特征学习时优先检查与任务信号对齐的前导子空间。

<a id="paper-139075"></a>

## How Does Personalized Memory Shape LLM Behavior? Benchmarking Rational Preference Utilization in Personalized Assistants

[官方论文页](https://neurips.cc/virtual/2026/poster/139075) · [作者来源](https://openreview.net/forum?id=mgD9u9b1aC)

- **问题 / 瓶颈** · 不相关偏好会干扰当前意图。
- **核心创新 / 方法** · 以多粒度协议评估偏好推理，并将记忆选择建模为语用判断。
- **Baseline** · 针对偏好使用设计的基线，名称待核实。
- **Benchmark** · RPEval 及商业助手失败案例。
- **关键结果 / 消融** · 摘要报告方法解决所观测坏例的 80%。
- **适用条件 / 局限** · 所报告坏例修复不等于总体线上增益。

**可复用机制** · 构造有无相关偏好两类对照，考查系统能否拒用真实却不相关的记忆。

<a id="paper-151804"></a>

## How Does Pruning Change Decisions in Large Language Models?

[官方论文页](https://neurips.cc/virtual/2026/poster/151804) · [作者来源](https://openreview.net/forum?id=XtuLvmYlSD)

- **问题 / 瓶颈** · 困惑度或平均准确率难捕捉单样本决策翻转。
- **核心创新 / 方法** · 配对测置信、候选间隔及翻转，另对多个校准视图做最小最大后悔的掩码选择。
- **Baseline** · 幅值剪枝、Wanda、Wanda++、SparseGPT。
- **Benchmark** · 多个模型和 N:M 稀疏水平；近边界可靠性和平均困惑度。
- **关键结果 / 消融** · 剪枝降低间隔且增多正确转错误；困惑度改善不确保决策改善。
- **适用条件 / 局限** · 候选级测量依赖任务与构造。

**可复用机制** · 对压缩前后近决策边界样本做配对，以免平均指标掩盖可靠性退化。

<a id="paper-148203"></a>

## How does RL Post-training Induce Skill Composition? A Case Study on Countdown

[官方论文页](https://neurips.cc/virtual/2026/poster/148203) · [作者来源](https://openreview.net/forum?id=zb8jA9cOxq)

- **问题 / 瓶颈** · 长度外推容易被误解为技能组合。
- **核心创新 / 方法** · 将 Countdown 解拆为表达式树，按组合形态跟踪随训练变化的成功率。
- **Baseline** · 标准 pass@k 和只按长度分组。
- **Benchmark** · Countdown；初步扩展至形式证明。
- **关键结果 / 消融** · 先掌握浅且平衡的树形；同深度下右重形态长期脆弱。
- **适用条件 / 局限** · 严格证据主要来自 Countdown。

**可复用机制** · 分别改变组成规模和结构，让评测能定位遇到新组合时具体失灵的形态。

<a id="paper-150331"></a>

## How Do Language Models Compose Functions?

[官方论文页](https://neurips.cc/virtual/2026/poster/150331) · [作者来源](https://openreview.net/forum?id=iuShT9gVLr)

- **问题 / 瓶颈** · 能解两步子题并不保证组合，答对也不证明用了组合机制。
- **核心创新 / 方法** · 解码残差流是否显式包含中间实体，分析不同嵌入几何下的路径倾向。
- **Baseline** · 只验证两跳答案正确的输出评估。
- **Benchmark** · 两跳事实回忆和表示几何。
- **关键结果 / 消融** · 发现可检测中间实体与无可检测中间实体的两类机制。
- **适用条件 / 局限** · 探针未检出不等于表示绝对不存在；聚焦事实任务。

**可复用机制** · 将过程证据纳入组合能力验证，以区分可复用子步骤和任务特定捷径。

<a id="paper-154133"></a>

## How Do Language Models Understand Tables? A Mechanistic Analysis of Cell Location

[官方论文页](https://neurips.cc/virtual/2026/poster/154133) · [作者来源](https://openreview.net/forum?id=Fyw87Kl3h1)

- **问题 / 瓶颈** · 线性序列化掩盖了模型如何使用二维坐标。
- **核心创新 / 方法** · 通过激活修补发现分隔符计数的序数定位，并分析列索引表示。
- **Baseline** · 不同格式与所用可解释性对照；名称待核实。
- **Benchmark** · 原子单元格定位、多个格式及层次 HiTab。
- **关键结果 / 消融** · 三阶段机制在 HiTab 中仍可见；列索引可在线性子空间中表征。
- **适用条件 / 局限** · 机制适用范围受序列化格式、模型和任务限制。

**可复用机制** · 格式迁移时先检查行列索引可读性，再判断回答错误发生在定位还是内容传递。

<a id="paper-151382"></a>

## How Far Are VLMs from Privacy Awareness in the Physical World? An Empirical Study

[官方论文页](https://neurips.cc/virtual/2026/poster/151382) · [作者来源](https://openreview.net/forum?id=b1g2c9p7zS)

- **问题 / 瓶颈** · 文本评估不能代表现场感知、社交变化和行为选择。
- **核心创新 / 方法** · 在交互视听模拟中按三层递进测隐私知觉及决策。
- **Baseline** · 12 个视觉语言模型。
- **Benchmark** · ImmersedPrivacy 的杂乱场景、语境变化及指令冲突。
- **关键结果 / 消融** · 场景复杂度增加时表现下降；情境变化准确率均不超过 65%，最佳冲突案例兼顾率 51%。
- **适用条件 / 局限** · 基于模拟器，真实部署待验证。

**可复用机制** · 将系统知道的隐私规则与它实际选择的行为分开验收。

<a id="paper-148472"></a>

## How Far Is Too Far? Object Recognition Declines Monotonically with Semantic Distance

[官方论文页](https://neurips.cc/virtual/2026/poster/148472) · [作者来源](https://openreview.net/forum?id=xY4SuwZDLZ)

- **问题 / 瓶颈** · 离散的常见或异常背景划分难刻画干扰强度。
- **核心创新 / 方法** · 用语义不相似轴调节对象背景关系，并检查局部证据是否聚合到输出。
- **Baseline** · 35 个 CNN、ViT 和视觉语言模型。
- **Benchmark** · ImageNet-OOC1k；背景偏离轴上的识别准确率。
- **关键结果 / 消融** · 准确率普遍随偏离增加下降，空间重排最高改善 5.4 个百分点。
- **适用条件 / 局限** · 人工控制的数据与所测上下文不等同自然分布。

**可复用机制** · 当局部仍可识别对象时先修聚合，避免误把背景干扰理解成特征提取失败。

<a id="paper-152063"></a>

## How Fine-Tuning Objectives Shape Layer-Wise Information in LLM Hallucination Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/152063) · [作者来源](https://openreview.net/forum?id=Vlr7fHQiNH)

- **问题 / 瓶颈** · 相同骨干下分类头训练与序列评审重组表征的程度不同。
- **核心创新 / 方法** · 追踪训练中类别判别信号出现的位置并删去其上的冗余分层。
- **Baseline** · 全模型分类头与序列到序列评审。
- **Benchmark** · Qwen3-4B/8B，并迁移到 Llama-3.2-3B 和 Mistral-7B-v0.3。
- **关键结果 / 消融** · 裁去约 31% 网络后匹配或超过全模型二分类表现。
- **适用条件 / 局限** · 针对二分类任务，裁剪比例需在新任务验证。

**可复用机制** · 以训练过程中任务信息形成的层段定截断位置，不只依据终态层相似性。

<a id="paper-150830"></a>

## How Finite-Rank Bottleneck Shape the Low-Rank Adaptation Landscape

[官方论文页](https://neurips.cc/virtual/2026/poster/150830) · [作者来源](https://openreview.net/forum?id=eyfZvKjtnQ)

- **问题 / 瓶颈** · 样本量或局部线性化难解释低秩更新何时够用。
- **核心创新 / 方法** · 冻结激活诱导有限秩线性观测，迹范数选取低秩解，并用注意力不变性缩紧界。
- **Baseline** · 以 NTK 线性化为基础的既有理论。
- **Benchmark** · 解析界覆盖多头注意力及带权重衰减的因子目标。
- **关键结果 / 消融** · 最优解秩由瓶颈秩控制；微扰条件下超阈值因子驻点秩不足。
- **适用条件 / 局限** · 依赖冻结表征、正则与给定观测结构。

**可复用机制** · 按下游损失实际可分辨的更新自由度设秩，再用小规模秩扫确认经验阈值。

<a id="paper-151609"></a>

## How Hard Is It for Message-Passing GNNs to Simulate One Weisfeiler-Lehman Color-Refinement Step?

[官方论文页](https://neurips.cc/virtual/2026/poster/151609) · [作者来源](https://openreview.net/forum?id=ZHXIlyKr8l)

- **问题 / 瓶颈** · 单步局部颜色精化隐藏全局重标号，传统表达性比较不计资源。
- **核心创新 / 方法** · 区分固定参数与实例依赖模拟，分析确定性、零错及有界错的资源界。
- **Baseline** · 标准 WL、固定参数消息传递及更强有根端口感知模型。
- **Benchmark** · 无属性图的单步精化；深度、消息位数与随机位数。
- **关键结果 / 消融** · 大颜色集时有界错单层实现只需对数消息与随机位；小颜色集出现深宽折中。
- **适用条件 / 局限** · 结果限于所定义的精确模拟条件及图模型，实例参数未必易求。

**可复用机制** · 把表达能力和实现该表达能力的有限资源成本分开报告。

<a id="paper-149145"></a>

## How I learned to stop worrying and love StopGrads: Stationarity, Convergence, and a case study on Flow Map Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149145) · [作者来源](https://openreview.net/forum?id=sVQbbYHEsX)

- **问题 / 瓶颈** · 停止梯度会改变原目标的梯度、驻点和保证。
- **核心创新 / 方法** · 提出带闭式驻点刻画的截断梯度回归模板，并分析函数半梯度流对应的流映射。
- **Baseline** · 既有流映射截断梯度位置；具名实现待核实。
- **Benchmark** · 流映射学习；驻点、收敛及训练速度。
- **关键结果 / 消融** · 报告修改截断位置使训练约快 2.5 倍，并给出驻点和收敛分析。
- **适用条件 / 局限** · 闭式结论针对函数空间半梯度流，有限模型和规模外推待查。

**可复用机制** · 改梯度路径前先判断目标解是否改变，再测达到相同质量的计算成本。

<a id="paper-154841"></a>

## How Language Models Compress and Compare: Understanding  Selection with Token Covariance Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/154841) · [作者来源](https://openreview.net/forum?id=AW5VdyuenU)

- **问题 / 瓶颈** · 最终得分不能说明比较何时形成。
- **核心创新 / 方法** · 跟踪逐层 token 协方差，并定位指令、证据和候选的块结构，辅以瓶颈干预。
- **Baseline** · 模板改写、成对重排、候选集操控和不同检查点。
- **Benchmark** · 四个模型家族的 14 个模型、12 个结构选择基准；诊断谱和答案区分。
- **关键结果 / 消融** · 共享低秩瓶颈后，模型在后层恢复候选比较结构；瓶颈附近干预优先破坏后层比较。
- **适用条件 / 局限** · 证据主要针对结构化选择，其他生成任务待核实。

**可复用机制** · 将区分答案的时间点与表征瓶颈的时间点分开测量。

<a id="paper-155327"></a>

## How Long Does Infinite Width Last? Signal Propagation in Long-Range Linear Recurrences

[官方论文页](https://neurips.cc/virtual/2026/poster/155327) · [作者来源](https://openreview.net/forum?id=6SiRDlbWwF)

- **问题 / 瓶颈** · 循环深度和有限宽度同时增加时，常见无限宽理论可能失效。
- **核心创新 / 方法** · 从复高斯初始化导出有限宽隐藏态能量公式，并比较联合极限。
- **Baseline** · 无限宽预测及 Glorot 类初始化。
- **Benchmark** · 线性循环，考察隐藏态信号能量随时间和宽度的变化。
- **关键结果 / 消融** · 深度小于平方根量级时近似有效，达到该量级出现系统偏离，更长时有限宽效应占主导。
- **适用条件 / 局限** · 结果依赖线性递推和特定初始化，非线性门控模型待核实。

**可复用机制** · 报告时同时扫描宽度和处理长度，避免从固定长度下的宽度趋势推出长序列稳定性。

<a id="paper-149872"></a>

## How Much Evidence Should Retrieval-Augmented In-Context Learning Use Under Distribution Shift?

[官方论文页](https://neurips.cc/virtual/2026/poster/149872) · [作者来源](https://openreview.net/forum?id=mZD68mJapq)

- **问题 / 瓶颈** · 增大 top-k 能提高证据覆盖，但有限读者可能被冲突和冗长上下文干扰。
- **核心创新 / 方法** · 用有效证据覆盖区分有用证据、残余歧义及读者稳定性，并做密集 k 扫描。
- **Baseline** · 完美证据及打乱上下文对照。
- **Benchmark** · 问答、验证、自然语言推断；召回和准确率随 k 的关系。
- **关键结果 / 消融** · 召回持续升高时，准确率可饱和或下降；验证和推断出现更明显的干扰限制。
- **适用条件 / 局限** · 理论依赖局部线性及提示稳定性，控制器仅为诊断探针。

**可复用机制** · 检索预算基于下游性能而非召回率单独调参，用 oracle 和打乱对照定位瓶颈。

<a id="paper-155363"></a>

## How Much Information is Needed for Accurate Kalman Filtering?

[官方论文页](https://neurips.cc/virtual/2026/poster/155363) · [作者来源](https://openreview.net/forum?id=6AvVndMx4T)

- **问题 / 瓶颈** · 原始观测历史的任意随机编码是无限维问题。
- **核心创新 / 方法** · 证明后验均值足够，将间接率失真优化化为后验谱决定的高斯模糊。
- **Baseline** · 完整历史的任意编码器和数值验证。
- **Benchmark** · 线性高斯隐藏马尔可夫模型，指标为互信息与隐状态均方误差。
- **关键结果 / 消融** · 得到显式率失真函数和顺序学习风险下界，数值实验支持理论。
- **适用条件 / 局限** · 仅证明线性高斯与平方误差设置，非高斯后验可能需要额外统计量。

**可复用机制** · 先检验估计目标对应的充分统计量，再设计历史压缩。

<a id="paper-150418"></a>

## How Much Is One Recurrence Worth? Iso-Depth Scaling Laws for Looped Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150418) · [作者来源](https://openreview.net/forum?id=iBvm5lCnAJ)

- **问题 / 瓶颈** · 验证损失无法区分一般训练收益与循环容量收益。
- **核心创新 / 方法** · 在循环数 1、2、4、8 和多计算预算下拟合含循环等价指数的尺度律。
- **Baseline** · 等深度非循环模型、截断反传与超连接变体。
- **Benchmark** · 约 50 倍预训练计算跨度，指标为验证损失与等价指数。
- **关键结果 / 消融** · 标准指数 0.46，截断反传降至 0.38，而超连接升至 0.65。
- **适用条件 / 局限** · 指数为所测架构及计算范围的拟合量。

**可复用机制** · 单列循环等价指数与总体损失，识别训练变好但共享重用价值下降的方案。

<a id="paper-151430"></a>

## How New Strategies Emerge in RL Post-Training: A Controlled Study

[官方论文页](https://neurips.cc/virtual/2026/poster/151430) · [作者来源](https://openreview.net/forum?id=amAQ0bvrH7)

- **问题 / 瓶颈** · 仅看采样成功率无法分辨新程序与重加权。
- **核心创新 / 方法** · 已知语法分布下预训练基本化简，再以二元答案奖励后训练，并逐步审计串行和并行压缩。
- **Baseline** · 基础模型大预算采样、拒绝微调及预训练消融。
- **Benchmark** · 可观察重写语法中的保留样本，测有效捷径、复用和最终成功。
- **关键结果 / 消融** · RL 先强化基本操作，再积累可复用压缩；拒绝微调产生的捷径更多无效，且较早停滞。
- **适用条件 / 局限** · 仅在所测符号语法验证；程序化预训练是观察到的前提。

**可复用机制** · 对等比较探索量和探索有效性，并在轨迹层核验新策略是否在不同样本复用。

<a id="paper-152662"></a>

## How Selection Shapes Diversity in LLM Ecosystems

[官方论文页](https://neurips.cc/virtual/2026/poster/152662) · [作者来源](https://openreview.net/forum?id=RM3k5s1pJM)

- **问题 / 瓶颈** · 表面共存或分工可能对轻微扰动或新策略进入不稳。
- **核心创新 / 方法** · 将曝光分配建模为选择压力，用切向稳定和入侵指数诊断，并用小型模拟社交平台验证。
- **Baseline** · 不同选择强度和多样性支持设置。
- **Benchmark** · 模型代理生成、互评并竞争展示的模拟生态；集中度、稳定性和波动。
- **关键结果 / 消融** · 选择压力加剧集中并推动局部失稳；多样性支持仅在一定范围稳定分工，早期波动提示失稳。
- **适用条件 / 局限** · 实验证据为最小模拟平台，结论不可直接移到现实平台。

**可复用机制** · 对看似多样的终态做小扰动检查，防止仅凭静态聚类判定生态稳定。

<a id="paper-151033"></a>

## How Should Parallel Langevin Chains Share Noise?

[官方论文页](https://neurips.cc/virtual/2026/poster/151033) · [作者来源](https://openreview.net/forum?id=dTLaD3Us8h)

- **问题 / 瓶颈** · 独立噪声会造成可避免的集成均值方差。
- **核心创新 / 方法** · 逐步从独立高斯创新中减去链间均值并重标度，保留边缘噪声而消去集成噪声。
- **Baseline** · 同规模独立链集成。
- **Benchmark** · 二次目标、WDBC、Spambase、Adult 贝叶斯逻辑后验；均值方差及参考 MSE。
- **关键结果 / 消融** · 二次目标的有限时域线性均值中噪声精确抵消；真实基准的参考 MSE 缩小约 4–14 倍。
- **适用条件 / 局限** · 二次观测未必获益，随机初始化、小批量和非二次曲率会增加残余方差。

**可复用机制** · 先确定需要估计的统计量，再选跨链耦合，不把均值收益外推到所有观测。

<a id="paper-150612"></a>

## How to Instruct Your Robot: Dense Language Annotations Power Robot Policy Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150612) · [作者来源](https://openreview.net/forum?id=grxX3mAW7g)

- **问题 / 瓶颈** · 单一任务标签省略运动、场景、手臂状态和子目标。
- **核心创新 / 方法** · 重标已有片段为四类描述，训练指令器按任务和初始画面选择合适条件，异步生成。
- **Baseline** · 无标注、固定标注侧面和每任务 oracle。
- **Benchmark** · 百万余机器人操作、五万 EgoVerse 视频，考察 RoboCasa 成功率及组合任务和分布外场景。
- **关键结果 / 消融** · 指令器较无标注提升 5 个百分点，与 oracle 相差不超过 3 点；固定侧面无普遍优势。
- **适用条件 / 局限** · 依赖重标质量和执行时观测，多机器人或真机适用边界待核实。

**可复用机制** · 把标注的内容选择作为独立实验变量，用相同示范对照新标注能否替代补采。

<a id="paper-155300"></a>

## How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization

[官方论文页](https://neurips.cc/virtual/2026/poster/155300) · [作者来源](https://openreview.net/forum?id=6c5MRDWXkL)

- **问题 / 瓶颈** · 满足最大更新条件仍可能无法稳定迁移学习率。
- **核心创新 / 方法** · 建立三种共缩放场景的动态平均场理论，分析聚合中尺度依赖的观测量，推导 SGD 与 Adam 的 MSSP。
- **Baseline** · 最大更新参数化 μP。
- **Benchmark** · 宽度、专家宽度、数量与激活稀疏度的三种联动；比较学习率迁移和随规模性能。
- **关键结果 / 消融** · 摘要报告 MSSP 在三种场景恢复学习率迁移和随规模单调改善。
- **适用条件 / 局限** · 具体宽深范围和架构外泛化待核。

**可复用机制** · 同预算跨尺度比较聚合统计与最优学习率，区分最大更新与尺度稳定两种标准。

<a id="paper-139078"></a>

## How to Train a Surgeon? Benchmarking Generalist Agents in Surgical Scene Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/139078) · [作者来源](https://openreview.net/forum?id=mUEEwbzwMy)

- **问题 / 瓶颈** · 通用多模态模型的领域能力受数据和异质协议限制。
- **核心创新 / 方法** · 先统一手术场景子任务测试预训练能力，再用受限检索和视觉定位看推理工具能修复哪些缺口。
- **Baseline** · 通用开源与闭源多模态模型及其带工具版本。
- **Benchmark** · SURGKNOWBENCH 与 SURGAGENTGYM，拆分感知、流程推理和定位任务。
- **关键结果 / 消融** · 感知类缺口缩小，精确定位和专家级评判仍困难。
- **适用条件 / 局限** · 为离线能力诊断，临床适用性无法由摘要证明。

**可复用机制** · 验证工具调用价值时按能力缺口分别计分，防止平均增益掩盖未修复环节。

<a id="paper-155226"></a>

## How to Train Your Latent Diffusion Language Model Jointly With the Latent Space

[官方论文页](https://neurips.cc/virtual/2026/poster/155226) · [作者来源](https://openreview.net/forum?id=7KCjc4rgB6)

- **问题 / 瓶颈** · 直接联合编码器、去噪器和解码器会得到低质量扩散。
- **核心创新 / 方法** · 重塑预训练语言表示，组合解码 MSE、扩散向编码器预热、自适应时间采样和解码输入噪声。
- **Baseline** · 离散与连续扩散语言模型，以及朴素联合训练。
- **Benchmark** · OpenWebText、LM1B 文本生成，速度、质量及组件消融。
- **关键结果 / 消融** · 摘要称质量更好且快 2 至 13 倍，消融中各组件均有贡献。
- **适用条件 / 局限** · 所测文本域和速度口径需核实。

**可复用机制** · 训练潜空间时监控可去噪性和可解码性，并单独消融梯度接通时间。

<a id="paper-152528"></a>

## How Useful Is Cross-Domain Generalization for Training LLM Monitors?

[官方论文页](https://neurips.cc/virtual/2026/poster/152528) · [作者来源](https://openreview.net/forum?id=ST6y67U46v)

- **问题 / 瓶颈** · 跨任务微调可能让模型按熟悉域先验作答，忽略新提示。
- **核心创新 / 方法** · 用多个分类任务及各自提示训练，再混合通用指令训练以缓解泛化缺陷。
- **Baseline** · 提示分类及分类微调设置；比较是否混合指令训练。
- **Benchmark** · 相邻新域、同域新提示，以及显式思考分类和摘要迁移。
- **关键结果 / 消融** · 相邻任务有收益，同域换目标可能失败；适当混合能缓解。
- **适用条件 / 局限** · 效果依赖任务和混合配置；跨远域未由摘要证明。

**可复用机制** · 做域与指令的交叉测试，尤其保留同输入异标签规则以定位提示遵循退化。

<a id="paper-151178"></a>

## How well behaved is finite dimensional Diffusion Maps embedding?

[官方论文页](https://neurips.cc/virtual/2026/poster/151178) · [作者来源](https://openreview.net/forum?id=cQI5rogy6E)

- **问题 / 瓶颈** · 现有收敛结果不能直接说明嵌入的 reach 与密度。
- **核心创新 / 方法** · 在子流形假设下证明近均匀密度和 reach 等保留性质，并推导嵌入误差率。
- **Baseline** · 已有扩散映射收敛理论为背景。
- **Benchmark** · 理论分析有限样本的子流形嵌入。
- **关键结果 / 消融** · 给出误差阶为 (log n/n) 的 1/(8d+16) 次幂。
- **适用条件 / 局限** · 依赖子流形族条件，常数及可用维度待全文核实。

**可复用机制** · 用于几何下游任务时同时报告嵌入误差和几何稳定性，避免只用可视化印象。

<a id="paper-152464"></a>

## How You Move Tells What You'll Do: Trajectory-Conditioned Egocentric Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/152464) · [作者来源](https://openreview.net/forum?id=SuJgDJNedG)

- **问题 / 瓶颈** · 给定相同上下文有多个未来，直接回归会在模态之间折中。
- **核心创新 / 方法** · 从视频预测未来相机轨迹，再在动作对齐空间用轨迹引导动作规划，语言只用于塑造表示。
- **Baseline** · 视觉语言模型与结构化规划器。
- **Benchmark** · Ego-Exo4D、Ego4D GoalStep、EgoPER，另测 EPIC-Kitchens-100 和投篮结果。
- **关键结果 / 消融** · 轨迹优势随时域增长，使用仅 RGB 的位姿估计仍有效。
- **适用条件 / 局限** · 头部运动非所有任务皆指示意图，预测误差在部署中待核。

**可复用机制** · 在相同历史输入下分别对照真实轨迹、预测轨迹和文本，测收益是否随时域变化。

<a id="paper-139477"></a>

## HPC-Bench: A Comprehensive Benchmark for High Performance Computing Codes

[官方论文页](https://neurips.cc/virtual/2026/poster/139477) · [作者来源](https://openreview.net/forum?id=NXClsdFxLa)

- **问题 / 瓶颈** · 仅运行时间或正确率无法比较随机优化的可用性。
- **核心创新 / 方法** · 将 Fast@k 与 Speedup@k 绑定程序级正确性验证。
- **Baseline** · 三种代表性语言模型；具体名称待核。
- **Benchmark** · 114 个工作负载、16 类计算模式，含串行 CPU、OpenMP 和 CUDA。
- **关键结果 / 消融** · 提高加速要求会明显降低找到正确快速实现的概率。
- **适用条件 / 局限** · 依赖运行环境、计时稳定性与测试覆盖。

**可复用机制** · 横扫速度目标和采样预算，比较正确性门控后的候选收益。

<a id="paper-151076"></a>

## HRIL: Isolating Multimodal Synergy via Higher-Order Dependence

[官方论文页](https://neurips.cc/virtual/2026/poster/151076) · [作者来源](https://openreview.net/forum?id=d802JCOSRc)

- **问题 / 瓶颈** · 共享信息对比目标可能遗漏联合才出现的任务信息。
- **核心创新 / 方法** · 构造嵌入交叉矩张量，用 Tucker 分解表示非可分交互，再加防能量集中的正则。
- **Baseline** · 多模态对比方法。
- **Benchmark** · 合成与真实评测，重点看高协同任务。
- **关键结果 / 消融** · 摘要报告结果一致改善，协同主导时尤明显。
- **适用条件 / 局限** · 矩估计、模态数和低秩设置的成本与稳定性待核。

**可复用机制** · 用单模态不可解、组合可解的合成对照验证协同信息保存。

<a id="paper-139247"></a>

## HSCO-Bench: An Agent-Driven End-to-End Hardware-Software Co-design Benchmark for Systems-on-Chip

[官方论文页](https://neurips.cc/virtual/2026/poster/139247) · [作者来源](https://openreview.net/forum?id=cPhwxK5hja)

- **问题 / 瓶颈** · 单项软硬件性能掩盖端到端联调失败。
- **核心创新 / 方法** · 把分析、加速器集成、软件映射和板上有效原型纳入统一评估。
- **Baseline** · 五个前沿模型，名称待核。
- **Benchmark** · HSCO-Bench 在 AMD Virtex-7 VC707 上评估有效设计、加速与额外资源利用。
- **关键结果 / 消融** · 仅两模型生成有效原型，最高加速 16.22 倍，最高额外资源利用 23.67%。
- **适用条件 / 局限** · 单硬件环境与任务集合，资源利用不直接等同设计质量。

**可复用机制** · 将可构建性和资源约束下的可用加速拆开报告，避免只报少数成功样例。

<a id="paper-153703"></a>

## Human-AI Teaming Through the Lens of Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/153703) · [作者来源](https://openreview.net/forum?id=JOgSIyeb2b)

- **问题 / 瓶颈** · 校准的人与模型联合使用后不一定保持原校准特性。
- **核心创新 / 方法** · 给出基于特征划分的理论与实验，比较预测融合与交给单方预测。
- **Baseline** · 已有组合与委派方法。
- **Benchmark** · 理论分析和经验实验；数据集及指标待核。
- **关键结果 / 消融** · 融合可能损害人类校准；委派保持下游校准但可能要求很强的元分类器。
- **适用条件 / 局限** · 假定成员在特定特征划分上校准，真实审核反馈待核。

**可复用机制** · 同测委派准确率、成员分组校准与选择模型容量，避免只优化平均正确率。

<a id="paper-150298"></a>

## Human-Inspired, Task-Dimension-Guided Exploration for Efficient Learning and Transfer in High Dimensions

[官方论文页](https://neurips.cc/virtual/2026/poster/150298) · [作者来源](https://openreview.net/forum?id=jBYBXwoZOr)

- **问题 / 瓶颈** · 在所有候选项上直接探索效率低。
- **核心创新 / 方法** · 上下文老虎机先选奖励相关维度，再选其中的信息特征和最终物品。
- **Baseline** · 现有推荐探索基线；名称待核。
- **Benchmark** · MovieLens-20M、Last.fm、Amazon，比较探索效率和冷启动。
- **关键结果 / 消融** · 摘要称明显改善两项表现，且可视化呈现逐步收窄。
- **适用条件 / 局限** · 依赖可组织特征维度，非局部交互下的代价需测。

**可复用机制** · 同预算比较维度分层与直接选项探索，另测错误维度锁定的影响。

<a id="paper-139007"></a>

## HumanoidArena: Benchmarking Egocentric Hierarchical Whole-body Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/139007) · [作者来源](https://openreview.net/forum?id=r3Vj07V062)

- **问题 / 瓶颈** · 端到端任务成功可能掩盖高层策略对特定跟踪器的依赖。
- **核心创新 / 方法** · 统一第一视角高层动作接口，拆分扰动泛化与跟踪器迁移评估。
- **Baseline** · 代表性模仿学习和 VLA 策略，不同通用运动跟踪器。
- **Benchmark** · HumanoidArena 七种必须动腿的人物与场景交互，报告任务执行与迁移。
- **关键结果 / 消融** · 共享接口能支持多种任务，跨跟踪器迁移仍脆弱。
- **适用条件 / 局限** · 以仿真为主，真机上的接口可靠性待查。

**可复用机制** · 对每个低层跟踪器同时测动作可执行率和任务成功，避免将单后端成绩当作接口迁移。

<a id="paper-150291"></a>

## Humanoid Horizon: Extending Task Horizon in Whole-Body Loco-Manipulation via Parallel Training, Dynamic Starting, and Reward Gating

[官方论文页](https://neurips.cc/virtual/2026/poster/150291) · [作者来源](https://openreview.net/forum?id=jG3AhOucmP)

- **问题 / 瓶颈** · 早期易得奖励主导训练，后段专项更新又让前段退化。
- **核心创新 / 方法** · 并行阶段共享策略，以前序 rollout 终态刷新起点；之前放置物被移动时将后段奖励置零。
- **Baseline** · 现有长时全身移动操作基线。
- **Benchmark** · LHM-Humanoid，350 个训练场景、66 个留出场景，按阶段及物体数量测成功。
- **关键结果 / 消融** · 各阶段超过 80%，超过两个物体时比对照更稳定；另演示 DAgger 蒸馏。
- **适用条件 / 局限** · 摘要未证实真实人形部署，阶段划分和阈值的迁移待核。

**可复用机制** · 用实际阶段交接状态训练并测试，将已完成子目标保持率与当前任务成功分开。

<a id="paper-139307"></a>

## HumanScore: Benchmarking Human Motions in Generated Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/139307) · [作者来源](https://openreview.net/forum?id=YGSNuUj5dh)

- **问题 / 瓶颈** · 画面逼真仍可能有动作不连贯或生物力学异常。
- **核心创新 / 方法** · 用普通姿态估计提取七项运动学及生物力学指标，按运动类别和强度设计提示。
- **Baseline** · 六类视频生成模型；名称待核。
- **Benchmark** · 840 段视频，比较物理指标和人工评价。
- **关键结果 / 消融** · 作者称视觉可信度与动作保真有一致缺口，指标与人工评判相关。
- **适用条件 / 局限** · 依赖姿态估计可靠性；遮挡与非标准动作的误判待核。

**可复用机制** · 在模型回归测试中固定动作强度分布，单列动作和观感两组指标。

<a id="paper-154000"></a>

## Humans Correct Their Judgements Through Debate, but Weaker AI Models Not

[官方论文页](https://neurips.cc/virtual/2026/poster/154000) · [作者来源](https://openreview.net/forum?id=Gx1mnP7am3)

- **问题 / 瓶颈** · 人类在辩论中的信念更新不一定可迁移到能力较弱的模型。
- **核心创新 / 方法** · 比较单边咨询、双边辩论及多裁判讨论和投票，并改变先验提取与相关主张。
- **Baseline** · 先验直接判断、咨询协议、不同裁判模型。
- **Benchmark** · 507 位人类参与者和开闭源语言模型，测判断正确率。
- **关键结果 / 消融** · 人类由 41.3% 升至 57.6%，讨论达 62.2%；弱模型多场景无收益或下降。
- **适用条件 / 局限** · 依赖具体任务、裁判与辩论强度。

**可复用机制** · 在自动监督上线前分层测初始判断正误，检查错误纠正是否以新的误判为代价。

<a id="paper-138969"></a>

## HumanStereo: A Benchmark for Metric Facial Depth Estimation and Its Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/138969) · [作者来源](https://openreview.net/forum?id=tOPPmPEqR5)

- **问题 / 瓶颈** · 常规深度指标不能反映测量亚毫米结构的需求。
- **核心创新 / 方法** · 提出基于任务的绝对内点率及关键点三维距离误差，另用真实数据测瞳距。
- **Baseline** · 几何匹配器、RAFT-Stereo、IGEV++、MASt3R、FoundationStereo。
- **Benchmark** · 417k 合成立体对、128 个形象、109 种配置；另有真实验光数据。
- **关键结果 / 消融** · 最佳模型真实瞳距误差仍高于临床所需亚毫米水平一个数量级。
- **适用条件 / 局限** · 合成到真实分布差异及临床协议细节待核。

**可复用机制** · 面向精密测量部署时用关键点绝对误差和真实下游阈值验收。

<a id="paper-154021"></a>

## HuPER: A Human-Inspired Framework for Phonetic Perception

[官方论文页](https://neurips.cc/virtual/2026/poster/154021) · [作者来源](https://openreview.net/forum?id=Gq0mSArmWx)

- **问题 / 瓶颈** · 规范发音不等于实际发音，弱声学证据又常需语言约束。
- **核心创新 / 方法** · 以音素识别器修正规范字音为实际发音代理；推理按证据启用声学、参考或词汇约束。
- **Baseline** · 现有音素感知方法，逐项名称待核实。
- **Benchmark** · 五个英语基准及 95 个未见语言，含弱证据和障碍语音。
- **关键结果 / 消融** · 100 小时训练数据即达领先音素特征错误率，摘要报告零样本迁移。
- **适用条件 / 局限** · 词典和语言约束可能偏向规范发音。

**可复用机制** · 把符号转写当作可纠正先验，避免用它覆盖不标准但真实的声音。

<a id="paper-151555"></a>

## HybridCache: Enhancing Prefix Caching for Linear–Softmax Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151555) · [作者来源](https://openreview.net/forum?id=ZlPah7doRw)

- **问题 / 瓶颈** · 反复存储大递归状态不现实，粗分块又削弱逐词 KV 命中。
- **核心创新 / 方法** · 只选择性存短程头状态并复用已有长程头状态，用独立行列尺度压缩有结构的离群值。
- **Baseline** · 周期性递归状态保存与逐词 KV 缓存。
- **Benchmark** · 混合线性和 softmax 模型的现实服务负载。
- **关键结果 / 消融** · 摘要报告重算下降、吞吐改善且保持准确度。
- **适用条件 / 局限** · 需按模型核验记忆跨度与离群结构。

**可复用机制** · 拆分保存粒度和压缩尺度，先按组件更新特性提高缓存利用率。

<a id="paper-148875"></a>

## Hybrid Neural World Models for Physical Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/148875) · [作者来源](https://openreview.net/forum?id=uWsmvC2jq5)

- **问题 / 瓶颈** · 冲击、波前和接触处的代理误差可能无明显外部警告。
- **核心创新 / 方法** · 直接监督连续时域条件预测，并从网络前向提取每轨迹误差图，用其门控回退。
- **Baseline** · 经典求解器、深集成、误差头、梯度幅值和局部共形。
- **Benchmark** · 反应扩散、可压缩 Euler 及刚体碰撞；速度和误差。
- **关键结果 / 消融** · PDE 的 CPU 加速报告为 26 至 72 倍，默认回退约减半残余误差。
- **适用条件 / 局限** · 依赖代理误差图对目标动力学的校准能力。

**可复用机制** · 将风险侦测内置于代理，再以回退频率显式交换速度和精度。

<a id="paper-154293"></a>

## Hybrid Probabilistic Zonotopes for Identifiable and Refinable Predictive Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/154293) · [作者来源](https://openreview.net/forum?id=Eof9Xx15Ry)

- **问题 / 瓶颈** · 单个预测区间或混合高斯很难同时表示三种不确定性。
- **核心创新 / 方法** · 以二元、有界与随机生成元组合 zonotope，共享有界生成元连接跨步预测。
- **Baseline** · 同编码器高斯混合头与单共形区域。
- **Benchmark** · 代表性预测基准；细节待核实。
- **关键结果 / 消融** · 理论给出生成元在置换意义下可识别；观测一步可更新其余预测。
- **适用条件 / 局限** · 有界漂移共享假设需与任务匹配。

**可复用机制** · 把跨步关联放进共享漂移成分，令迟到的局部观测能细化完整预测。

<a id="paper-148710"></a>

## Hybrid Reinforcement Learning for One-step Degraded Infrared and Visible Image Fusion

[官方论文页](https://neurips.cc/virtual/2026/poster/148710) · [作者来源](https://openreview.net/forum?id=vdvW81Wcy2)

- **问题 / 瓶颈** · 多步扩散昂贵，单步蒸馏会丢细节。
- **核心创新 / 方法** · 把退化观测作为生成中间状态，在一步生成引入 Flow-GRPO 探索和粗细双层奖励。
- **Baseline** · 多步扩散及单步蒸馏。
- **Benchmark** · 退化红外与可见光融合；质量、效率。
- **关键结果 / 消融** · 摘要报告融合质量和效率改善，具体幅度待核实。
- **适用条件 / 局限** · 奖励需要兼顾全局语义和局部对象。

**可复用机制** · 保留最短生成路径，同时只在优化期恢复必要的探索自由度。

<a id="paper-149753"></a>

## HyCO: A Hybrid Neural Solver for Combinatorial Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149753) · [作者来源](https://openreview.net/forum?id=ncwBmlZFlv)

- **问题 / 瓶颈** · 序贯解前缀优势明显但误差随时域积累，全局求解会受剩余维数影响。
- **核心创新 / 方法** · 用策略熵和两求解器分歧触发从 RL 前缀切到条件扩散。
- **Baseline** · 单独 RL 与单独扩散求解器。
- **Benchmark** · 多项组合优化基准，衡量遗憾和最终解质。
- **关键结果 / 消融** · 给定误差缩放假设下存在唯一最优交接点，实验支持自适应切换。
- **适用条件 / 局限** · 两个求解器必须能交换一致的前缀状态，理论依赖给定误差曲线。

**可复用机制** · 比较两个求解器在不同剩余规模的边际误差，用不确定度指导交接。

<a id="paper-152435"></a>

## Hydra-DP3: Frequency-Aware Right-Sizing of 3D Diffusion Policies for Visuomotor Control

[官方论文页](https://neurips.cc/virtual/2026/poster/152435) · [作者来源](https://openreview.net/forum?id=TA5j0hwB2u)

- **问题 / 瓶颈** · 机械臂动作平滑，图像式解码器和长采样可能浪费计算。
- **核心创新 / 方法** · 按低频维度和高频残量界定误差，使用轻量混合解码器和两步 DDIM。
- **Baseline** · 此前三维扩散策略。
- **Benchmark** · RoboTwin2.0、Adroit、MetaWorld、真实任务和合成实验。
- **关键结果 / 消融** · 摘要报告使用既有策略不足 1% 的参数并显著降低时延。
- **适用条件 / 局限** · 依赖低频能量占优，接触等急变动作需另验。

**可复用机制** · 先测轨迹高频能量再配采样深度，可按任务做最小充分步数对照。

<a id="paper-149164"></a>

## HYDRA: Representation Harmonized Tokenization for Multimodal Generation and Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/149164) · [作者来源](https://openreview.net/forum?id=sNTc0XTEDc)

- **问题 / 瓶颈** · 生成须保留细节，理解需要抽象，两个目标可能冲突。
- **核心创新 / 方法** · 先用生成 ViT 表达结构，经低维生成语义瓶颈再扩展到语义 ViT。
- **Baseline** · 分离编码器、叠加视觉语义编码器以及离散量化方案。
- **Benchmark** · 重建 rFID、GenEval、DPG-Bench、WISE 与八项理解任务。
- **关键结果 / 消融** · 报告 rFID 0.08、GenEval 0.86，理解平均约提升十点。
- **适用条件 / 局限** · 瓶颈宽度与训练配方的敏感度待核实。

**可复用机制** · 先保留可重建的低层几何，再将语义压缩和扩展作为显式阶段。

<a id="paper-155676"></a>

## Hydra-X: Native Unified Multimodal Models with Holistic Visual Tokenizers

[官方论文页](https://neurips.cc/virtual/2026/poster/155676) · [作者来源](https://openreview.net/forum?id=3mwm6O3FZt)

- **问题 / 瓶颈** · 全时空交互和单步压缩可能破坏视频重建。
- **核心创新 / 方法** · 用帧级因果注意和分级压缩，再通过图像与视频教师监督轻型解压器；编辑在 tokenizer 潜空间交互。
- **Baseline** · 全时空注意、单步压缩和 LLM 语义层编辑。
- **Benchmark** · 7B 模型的图像视频理解、重建、生成和编辑。
- **关键结果 / 消融** · 摘要消融指出因果注意足够，全注意反而退化；潜空间编辑提高一致性。
- **适用条件 / 局限** · 依赖配套视觉教师，更多模型规模待核实。

**可复用机制** · 编辑时优先在能保留源局部结构的视觉潜空间对齐，不必把所有交互放到语义模型。

<a id="paper-150001"></a>

## HyFAD: Hybrid Time-Frequency Diffusion with Frequency-Aware Embedding for Time Series Imputation

[官方论文页](https://neurips.cc/virtual/2026/poster/150001) · [作者来源](https://openreview.net/forum?id=lWM3u6LGyO)

- **问题 / 瓶颈** · 单一扩散过程难兼顾长程趋势与细节。
- **核心创新 / 方法** · 时域扩散先给趋势，再以频域扩散精修，并给步骤加入频带相关嵌入。
- **Baseline** · DDPM 路线及已有填补方法。
- **Benchmark** · 多个时序填补任务；数据、指标待核实。
- **关键结果 / 消融** · 摘要报告性能改善，分频消融结果待核实。
- **适用条件 / 局限** · 依赖稳定频谱分解，极短窗口与突变需复测。

**可复用机制** · 用去噪时序表达从粗到细的职责分工，而非强迫每一步同时拟合所有尺度。

<a id="paper-153670"></a>

## Hyperagents

[官方论文页](https://neurips.cc/virtual/2026/poster/153670) · [作者来源](https://openreview.net/forum?id=Jdp9fbYYbz)

- **问题 / 瓶颈** · 只看单次任务收益不能证明更新策略可跨运行迁移。
- **核心创新 / 方法** · 在受控监督环境中比较任务改进轨迹和不同基线，另检验跨域迁移。
- **Baseline** · 不自改进、不开放探索的基线和既有系统。
- **Benchmark** · 多个任务域的随时间表现及跨域转移；具体细节待核实。
- **关键结果 / 消融** · 摘要报告相对基线改善，部分元级收益跨域累积。
- **适用条件 / 局限** · 外部有效性受受控环境、监督和任务限制。

**可复用机制** · 把短期任务分数、跨任务收益及监督下的安全约束列为独立验收维度。

<a id="paper-151003"></a>

## Hyperbolic Concept Bottleneck Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151003) · [作者来源](https://openreview.net/forum?id=dfLMID86Cd)

- **问题 / 瓶颈** · 平坦概念向量不能表达父子关系，干预可能不一致。
- **核心创新 / 方法** · 用双曲蕴含锥的包含边际定义激活，再用自适应尺度传播概念修正。
- **Baseline** · 欧氏事后概念瓶颈。
- **Benchmark** · 稀疏监督、层级一致、输入腐化鲁棒性。
- **关键结果 / 消融** · 摘要报告稀疏设定下可比约 20 倍训练数据的欧氏模型。
- **适用条件 / 局限** · 依赖可表征为层级的概念集合。

**可复用机制** · 将父子关系编码进激活和干预定义，避免独立调节导致非法概念组合。

<a id="paper-154612"></a>

## Hyperbolic Displacement-Constrained Adaptation for CLIP-Based Class-Incremental Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154612) · [作者来源](https://openreview.net/forum?id=CHvh1192IA)

- **问题 / 瓶颈** · 无回放的 CLIP 类增量训练会因适配残差叠加而遗忘。
- **核心创新 / 方法** · 单任务采用双曲低秩适配控制径向幅值，多任务再压缩合并后的残差。
- **Baseline** · 需要回放、原型或分布信息的 CLIP 增量路线。
- **Benchmark** · 五个类增量数据集；类别精度与遗忘，细项待核实。
- **关键结果 / 消融** · 摘要报告无需数据派生类别记忆即可改善表现。
- **适用条件 / 局限** · 多任务残差方向是否仍可靠需独立验证。

**可复用机制** · 优先约束适配引起的特征位移，而非额外存储旧数据统计。

<a id="paper-150947"></a>

## Hyperbolic Graph Neural Networks Under the Microscope: The Role of Geometry–Task Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/150947) · [作者来源](https://openreview.net/forum?id=e6asnq38T9)

- **问题 / 瓶颈** · 树状图的几何并不必然决定标签结构。
- **核心创新 / 方法** · 同时比较预测质量与表示失真，检验几何一致和不一致的设定。
- **Baseline** · 欧氏图模型。
- **Benchmark** · 几何回归、链路预测和节点分类。
- **关键结果 / 消融** · 链路预测表现出双曲优势，普通节点分类的优势大体消失。
- **适用条件 / 局限** · 优势取决于任务结构，不只取决于图的层次性。

**可复用机制** · 用目标是否需要保留输入距离来决定几何归纳偏置，并用欧氏对照验证。

<a id="paper-148771"></a>

## Hyperbolic Language Models: From Zipf to Compute-Optimal Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/148771) · [作者来源](https://openreview.net/forum?id=vB6z4gcTXY)

- **问题 / 瓶颈** · 欧氏输出的经验尺度律未必适用于双曲输出。
- **核心创新 / 方法** · 配对改变模型规模和词元预算，独立拟合数据和参数指数，并比较词频与输出半径。
- **Baseline** · 同条件欧氏语言模型。
- **Benchmark** · OpenWebText 的 20 个配对点及 WikiText-103、LAMBADA、PIQA。
- **关键结果 / 消融** · 报告最优数据参数比由 20.8 变为 8.4，20 个配对中 17 个占优。
- **适用条件 / 局限** · 外推到更大范围依赖尺度律及模型设定。

**可复用机制** · 输出层归纳偏置变更后，把数据预算表当成需重估的量。

<a id="paper-154114"></a>

## HyperFlow: Gradient-Free Test-Time Adaptation for Cross-Domain Few-Shot Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/154114) · [作者来源](https://openreview.net/forum?id=GACGdvulrX)

- **问题 / 瓶颈** · 逐任务反向传播成本高。
- **核心创新 / 方法** · 离线收集元任务微调轨迹，训练条件漂移网络；用常微分方程更新所选 PEFT 子空间。
- **Baseline** · 直接迁移、标准微调。
- **Benchmark** · Meta-Dataset、CD-FSL；准确率、显存和 FLOPs。
- **关键结果 / 消融** · 优于直接迁移，仅用标准微调约 1% 的 FLOPs、6 至 14% 峰值内存。
- **适用条件 / 局限** · 依赖元训练覆盖，离线收集更新轨迹有成本。

**可复用机制** · 将昂贵训练中学习到的更新规律压缩进轻量适配器，减少每任务部署成本。

<a id="paper-150850"></a>

## HyperGen: Learning Structure-Aware Spectral Flows for Hypergraph Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150850) · [作者来源](https://openreview.net/forum?id=etKi0VBHKP)

- **问题 / 瓶颈** · 超图谱不唯一决定节点和超边的关联矩阵。
- **核心创新 / 方法** · 构建带可学关联相位的 Hermitian 算子，流生成谱嵌入，并用去噪解码还原关联。
- **Baseline** · 超边启发式、投影式和现有生成方法。
- **Benchmark** · 多个超图基准；关联恢复、谱与几何结构。
- **关键结果 / 消融** · 摘要报告更准确的关联恢复和结构保持。
- **适用条件 / 局限** · 谱非唯一性仍由学习式解码处理，泛化需额外核验。

**可复用机制** · 在连续谱空间负责全局约束，在离散解码器单独建模原始关联歧义。

<a id="paper-148881"></a>

## Hypergraph Generation via Structured Stochastic Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/148881) · [作者来源](https://openreview.net/forum?id=uTrWNzumkt)

- **问题 / 瓶颈** · 两两投影丢失超边大小与重叠信息。
- **核心创新 / 方法** · 在松弛关联矩阵上将双侧热算子与 OU 过程结合，用正向线性高斯条件矩构造逆漂移标签。
- **Baseline** · 超图生成基线，具名待核实。
- **Benchmark** · 超图生成质量、理想模型精确性及有限时域稳定性；具名数据待核实。
- **关键结果 / 消融** · 报告强基线上的质量提升，并给出理想设置分析。
- **适用条件 / 局限** · 训练依赖关联合适松弛，离散恢复方式与有限容量误差待核实。

**可复用机制** · 设计结构感知加噪过程时兼顾条件标签闭式可算与终端分布易采样。

<a id="paper-154651"></a>

## Hypergraph Generation with Latent Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/154651) · [作者来源](https://openreview.net/forum?id=C27xHBHKGe)

- **问题 / 瓶颈** · 独立表示或固定结构假设难捕捉节点与超边耦合。
- **核心创新 / 方法** · 将超图分解为子图，由双视角 β-VAE 得到节点与超边潜变量，再以双向条件扩散生成。
- **Baseline** · 九种已有方法。
- **Benchmark** · 五个真实数据集，比较微观、中观、宏观结构和高阶相似度，含固定节点集重建。
- **关键结果 / 消融** · 摘要报告主要收益在中观及高阶保真，受限生成的重建最优。
- **适用条件 / 局限** · 拆分策略和约束类型能否推广待核实。

**可复用机制** · 将是否共享潜空间和是否交叉条件分开选择，并同时测局部结构和全局统计。

<a id="paper-148313"></a>

## Hypergraph Representation Learning with Hyperlink Random Effects

[官方论文页](https://neurips.cc/virtual/2026/poster/148313) · [作者来源](https://openreview.net/forum?id=ylbgDqHzRL)

- **问题 / 瓶颈** · 等长超边张量难覆盖通用超图，统一形成模型混淆实体交互和超边异质性。
- **核心创新 / 方法** · 以类别、高斯混合或评分随机效应建模超边形成，并用 EM 拟合。
- **Baseline** · 深度超图模型与等边长低秩模型；具名对照待核实。
- **Benchmark** · 合成潜结构恢复及真实超图数据。
- **关键结果 / 消融** · 给出可识别条件，模拟显示可恢复潜结构并表征异质交互。
- **适用条件 / 局限** · 随机效应设定、可辨识性条件及大规模开销待核实。

**可复用机制** · 用分层生成模型将群组形成的未观测差异与实体表示分开。

<a id="paper-154124"></a>

## Hyper Input Convex Neural Networks for Shape Constrained Learning and Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/154124) · [作者来源](https://openreview.net/forum?id=G69BisYSHp)

- **问题 / 瓶颈** · 现有 ICNN 可能难用深度提高凸函数逼近效率。
- **核心创新 / 方法** · 将 Maxout 与输入凸网络的设计结合以保持输入凸性。
- **Baseline** · ICNN、MLP 及神经最优传输基线。
- **Benchmark** · 凸回归、插值及高维最优传输，含合成与单细胞 RNA 数据。
- **关键结果 / 消融** · 证明近似二次函数所需参数更少，作者报告多个任务的预测改善。
- **适用条件 / 局限** · 理论优势针对二次函数；一般凸函数的资源界待核实。

**可复用机制** · 验证形状约束时同时测深度参数效率和传输任务性能。

<a id="paper-154296"></a>

## Hypernetworks for Dynamic Feature Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/154296) · [作者来源](https://openreview.net/forum?id=Emiobo4BDW)

- **问题 / 瓶颈** · 掩码嵌入需在多条采集路径间共享有限容量，可能损伤未见子集泛化。
- **核心创新 / 方法** · 用 Set Transformer 编码可见特征集合，再由超网络按需生成分类参数。
- **Baseline** · 掩码嵌入及已有动态特征选择方法。
- **Benchmark** · 合成与真实表格及图像，关注预算下性能和未见子集零样本泛化。
- **关键结果 / 消融** · 作者报告更小的结构复杂度界，和更强的未见子集性能。
- **适用条件 / 局限** · 按需参数生成的延迟及成本分布变化待核实。

**可复用机制** · 将预算采样策略和子集条件化预测器的影响拆开，专门留出未见掩码验证。

<a id="paper-150015"></a>

## HyperSkill: Multi-Modal Skill Learning on the Unit Hypersphere

[官方论文页](https://neurips.cc/virtual/2026/poster/150015) · [作者来源](https://openreview.net/forum?id=lOmo51p8Ne)

- **问题 / 瓶颈** · 离散量化欠缺技能邻近几何，且直通梯度有偏。
- **核心创新 / 方法** · 在球面上用 von Mises–Fisher 混合与测地排斥建多模态先验，以平方测地距离对齐示范技能和规划技能，低层用条件流匹配。
- **Baseline** · 向量量化技能和已有语言条件操作方法。
- **Benchmark** · LOReL、Kitchen，成功率和各模块消融。
- **关键结果 / 消融** · 作者报告达到所测最高成功率，消融支持各组件。
- **适用条件 / 局限** · 球面维度选择及真机迁移待核实。

**可复用机制** · 以同一可度量技能空间连接示范后验、高层先验和多样低层轨迹。

<a id="paper-151778"></a>

## Hyperspherical Local Margin Retraction for Zero-Shot Instance-Wise Machine Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/151778) · [作者来源](https://openreview.net/forum?id=Y6Xg1eyDpc)

- **问题 / 瓶颈** · 遗忘实例的个性化痕迹与保留类信息混杂。
- **核心创新 / 方法** · 以球面测地探针构造局部参考，只回缩与遗忘实例相关的边际超额。
- **Baseline** · 从头重训 oracle 及零样本遗忘基线。
- **Benchmark** · 多组数据与架构，测任务效用与成员推断风险。
- **关键结果 / 消融** · 摘要报告两种指标均更接近重训 oracle。
- **适用条件 / 局限** · 探针能否代表保留分布和对不同表示几何的适用性待核实。

**可复用机制** · 将完整遗忘梯度限制在有局部参考支持的差异方向，再对照完整重训。

<a id="paper-152624"></a>

## HyperTransport: Amortized Conditioning of T2I Generative Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152624) · [作者来源](https://openreview.net/forum?id=Rhug0gm51O)

- **问题 / 瓶颈** · 提示措辞不稳定，逐概念优化的成本随请求增加。
- **核心创新 / 方法** · 用最优传输损失训练超网络，将 CLIP 嵌入映射到可调强度干预，并可接收参考图。
- **Baseline** · 逐概念拟合和提示。
- **Benchmark** · DMD2、Nitro-1-PixArt 的 167 个未见概念；CLIP 指标、人评和 VLM 偏好。
- **关键结果 / 消融** · 生成单个干预比逐概念拟合快 3600–7000 倍，未见概念诱导匹配最强逐概念方法。
- **适用条件 / 局限** · 速度比仅对应干预生成，训练成本及跨骨干共享待核实。

**可复用机制** · 将条件表示与干预算子预测解耦，并用未见概念评估摊销是否泛化。

<a id="paper-150924"></a>

## HyperTree: Scalable Unsupervised Hierarchy Discovery in Hyperbolic Space

[官方论文页](https://neurips.cc/virtual/2026/poster/150924) · [作者来源](https://openreview.net/forum?id=eKnZ75qpqp)

- **问题 / 瓶颈** · 既有双曲层级模型多受规模或标注限制。
- **核心创新 / 方法** · 定义适用任意曲率的闭式最近公共祖先，优化有界、尺度不变的 Dasgupta 式目标。
- **Baseline** · 欧式层级方法与有监督双曲方法。
- **Benchmark** · 四个图像基准，含 ImageNet-1k、iNaturalist-2018、CIFAR-100、TinyImageNet；树纯度和维度。
- **关键结果 / 消融** · 摘要报告超过欧式对照，CIFAR-100 匹配监督基线，TinyImageNet 16 维超过监督对照。
- **适用条件 / 局限** · 大规模抽样复杂度保证和构树代价待核实。

**可复用机制** · 将层级树的质量、表征维度和数据规模同时纳入选型。

<a id="paper-153122"></a>

## HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/153122) · [作者来源](https://openreview.net/forum?id=NlRG5IrLFS)

- **问题 / 瓶颈** · 聚类成本和不规则小块会抵消稀疏注意力收益。
- **核心创新 / 方法** · 局限于三维局部窗口搜中心，锚步完整聚类，其间只更新部分 token，再做执行成本感知的簇合并。
- **Baseline** · 训练免费聚类稀疏注意力基线。
- **Benchmark** · 文生视频，端到端延迟和保真。
- **关键结果 / 消融** · 摘要报告端到端最高加速 2.13 倍，保真优于现有免训练对照。
- **适用条件 / 局限** · 依赖跨去噪步聚类稳定、特定 GPU 和算子实现。

**可复用机制** · 减少冗余更新后，按硬件瓦片执行成本检查稀疏率是否转化为实际速度。

<a id="paper-154142"></a>

## HyperVQ: Enabling Hyperprior Entropy Modeling for VQ-Based Generative Image Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/154142) · [作者来源](https://openreview.net/forum?id=FwTncDub2i)

- **问题 / 瓶颈** · 静态索引频率难适配内容，离散索引阻碍端到端码率梯度。
- **核心创新 / 方法** · 预测连续多元高斯，再以固定码本锚点的相对距离转换为分类分布。
- **Baseline** · 静态频率和 Huffman，以及多种 VQ 架构。
- **Benchmark** · 单尺度、大码本、残差 VQ；指标为码率节省及推理效率。
- **关键结果 / 消融** · 平均码率节省 18.5%，约为传统 Huffman 节省量的 7.28 倍。
- **适用条件 / 局限** · 空间密度建模的码本假设和相同重建质量下的差异待核实。

**可复用机制** · 从连续分布诱导可微离散概率，使编码器可按局部内容调码率。

<a id="paper-155387"></a>

## Hypothesis generation and updating in large language models

[官方论文页](https://neurips.cc/virtual/2026/poster/155387) · [作者来源](https://openreview.net/forum?id=62MnP5DLxA)

- **问题 / 瓶颈** · 对已有候选的准确选择可能掩盖无法自行提出或外推。
- **核心创新 / 方法** · 用数字游戏的三种探针估计假设后验，并与贝叶斯最优及人类对照。
- **Baseline** · 贝叶斯模型、人类及思考模式。
- **Benchmark** · 由少量正整数推断集合规则，比较后验预测、假设评判和生成。
- **关键结果 / 消融** · 作者报告评判比生成更准，思考模式更依赖先验；观察区规则性高也可能在域外外推不佳。
- **适用条件 / 局限** · 数字游戏是受控代理，实际科学任务仍待验证。

**可复用机制** · 把候选可发现性和候选可评判性作为不同验收标准，再用观察范围外的反例检查外推。

<a id="paper-152054"></a>

## HYVE: Hybrid Views for LLM Context Engineering over Machine Data

[官方论文页](https://neurips.cc/virtual/2026/poster/152054) · [作者来源](https://openreview.net/forum?id=VqKTNdjUqP)

- **问题 / 瓶颈** · 重复嵌套载荷会浪费上下文并降低模型处理稳定性。
- **核心创新 / 方法** · 识别重复模式，构造行列混合视图，并按需回表补数据或进行有限次数的语义总结。
- **Baseline** · 原始载荷直接输入是对照路线；其他名称待核。
- **Benchmark** · 问答、图表、异常检测和运维诊断，比较词元、质量与延迟。
- **关键结果 / 消融** · 词元下降 50%–90%；图表准确率最高相对提升 132%，延迟最多降 83%。
- **适用条件 / 局限** · 依赖可提取模式和正确的回表机制。

**可复用机制** · 分开测压缩视图的可答率及遗漏信息能否被准确恢复。

<a id="paper-155809"></a>

## I2V-DETACH: Source Grounding Detachment for Unauthorized Image-to-Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155809) · [作者来源](https://openreview.net/forum?id=2jiZgfYwnk)

- **问题 / 瓶颈** · 生成质量或时间一致性变差不足以说明源内容得到保护。
- **核心创新 / 方法** · 作者按源内容保持与输出质量分别评估图像保护机制。
- **Baseline** · 已有图像免疫方法。
- **Benchmark** · 多种图像到视频扩散架构，测源图保留和跨模型迁移。
- **关键结果 / 消融** · 摘要报告源内容保留下降且可跨模型迁移。
- **适用条件 / 局限** · 适用范围及保护强度待核，定量结论未见于摘要。

**可复用机制** · 比较不同保护方法时把源身份或内容留存与视频失真分开报告。

<a id="paper-149902"></a>

## IADR: Interface-Augmented Neural Operator for Phase-Field Mean-Curvature Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/149902) · [作者来源](https://openreview.net/forum?id=mMGBM26aqy)

- **问题 / 瓶颈** · 逐参数训练不经济，通用模型又可能丢失扩散反应结构。
- **核心创新 / 方法** · 保留目标网络的扩散反应分解，超网络依界面宽度生成其权重。
- **Baseline** · 单参数专家及通用神经算子。
- **Benchmark** · Allen–Cahn 曲率流，测试宽度、几何分布移位及多步滚动。
- **关键结果 / 消融** · 单模型在分布内匹配各专家，保持跨形状泛化和单步成本；给出 K 步误差界。
- **适用条件 / 局限** · 依赖方程结构已知，超出工作区间的表现待核。

**可复用机制** · 迁移到其他参数化模拟器时同时对照逐参数专家和显式参数拼接。

<a id="paper-150398"></a>

## ICAT: Incident-Case–Grounded Adaptive Testing for Physical-Risk Prediction in Embodied World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150398) · [作者来源](https://openreview.net/forum?id=iLQ4MUPnqw)

- **问题 / 瓶颈** · 视频预测可能漏掉关键危险信号或淡化后果。
- **核心创新 / 方法** · 用结构化事故证据约束测试案例，并按因果阶段与严重性分别评分。
- **Baseline** · 主流视频世界模型，名称待核。
- **Benchmark** · ICAT 事故案例评测，比较风险因素覆盖与严重度校准。
- **关键结果 / 消融** · 作者称模型常漏机制与触发条件，并误判严重程度。
- **适用条件 / 局限** · 以风险评估为限；事故记载覆盖和实际部署验证待核。

**可复用机制** · 在世界模型部署前单独做危险低估审查，避免用总体视频质量替代风险检验。

<a id="paper-152851"></a>

## iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity

[官方论文页](https://neurips.cc/virtual/2026/poster/152851) · [作者来源](https://openreview.net/forum?id=PtTQa5xo9Q)

- **问题 / 瓶颈** · 独立聚类查询键与固定稀疏比例会放大注意近似误差。
- **核心创新 / 方法** · 按点积交互聚类，以信噪比调稀疏日程，并合并不整齐的簇尾减少填充。
- **Baseline** · 独立特征聚类和固定比例稀疏路线。
- **Benchmark** · HunyuanVideo-T2V-13B 与 Wan2.1-T2V-14B，比加速与 PSNR。
- **关键结果 / 消融** · 分别快 2.03 和 1.55 倍，PSNR 为 31.017 和 29.301 dB。
- **适用条件 / 局限** · 依赖不同阶段的容错规律及硬件实现。

**可复用机制** · 等算力扫全程固定与阶段调度，另分开计内核填充开销。
