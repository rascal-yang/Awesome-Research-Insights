# NeurIPS 2026 论文卡 10

[会议索引](README.md)

<a id="paper-139457"></a>

## Principia: Relational Physics Tests for Video Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139457) · [作者来源](https://openreview.net/forum?id=OeH6Ijqffz)

- **问题 / 瓶颈** · 绝对度量受标定、帧率、尺寸影响。
- **核心创新 / 方法** · 测量成对物体之间在图像空间应满足的相对运动关系。
- **Baseline** · VBench，并对照视觉语言模型。
- **Benchmark** · Principia 八类现象，五种生成器的数千输出。
- **关键结果 / 消融** · VBench 均逾 0.7，Principia 均不超过 0.42。
- **适用条件 / 局限** · 依赖同场景共享规律和受控比较。

**可复用机制** · 世界模型评测可先找不受成像参数影响的相对量。

<a id="paper-154746"></a>

## Principled Design of Diffusion-based Optimizers for Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/154746) · [作者来源](https://openreview.net/forum?id=BJ9BmUd5tV)

- **问题 / 瓶颈** · 条件变化后反复调噪声和采样权重。
- **核心创新 / 方法** · 以新参数化获得不变性，在 RED-diff 框架内引入凸优化加速。
- **Baseline** · 基于 RED-diff。
- **Benchmark** · 图像重建、去模糊、超分辨率。
- **关键结果 / 消融** · 更快且图像质量改善，数值未报告。
- **适用条件 / 局限** · 迁移取决于问题是否满足相应不变性。

**可复用机制** · 将会随观测变换而变化的量吸收进参数化再共享超参。

<a id="paper-152868"></a>

## Principled Policy Optimization for LLMs via Self-Normalized Importance Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/152868) · [作者来源](https://openreview.net/forum?id=PnhgpXd7Ru)

- **问题 / 瓶颈** · 无 critic 方法面临高方差或目标偏移。
- **核心创新 / 方法** · 以自归一重要性估计构造带基线梯度。
- **Baseline** · PPO、GRPO、GSPO。
- **Benchmark** · 分析样本组偏差及奖励不确定性。
- **关键结果 / 消融** · 偏差按 O(1/G) 衰减，摘要称鲁棒性提升。
- **适用条件 / 局限** · 有限组仍有偏，依赖重要性估计条件。

**可复用机制** · 用渐近正确性和有限组方差共同选无 critic 更新。

<a id="paper-150834"></a>

## Prior-Anchored Local Statistical Representation Rectification for Low-Light Image Enhancement

[官方论文页](https://neurips.cc/virtual/2026/poster/150834) · [作者来源](https://openreview.net/forum?id=exQVJdz22G)

- **问题 / 瓶颈** · 暗光邻域反映退化而非内容。
- **核心创新 / 方法** · 以正常光高斯锚点为参照，恢复均值与方差偏移。
- **Baseline** · 既有增强网络，摘要未具名。
- **Benchmark** · 多种低光基准和网络架构。
- **关键结果 / 消融** · 恢复质量一致提高，数值未报告。
- **适用条件 / 局限** · 需可学习干净域先验。

**可复用机制** · 分离围绕参考结构的内容位移和观测不确定性。

<a id="paper-152230"></a>

## Prior as Geometry, Not Generator: Weak-Diffusion Test-Time Reconstruction for Dynamic MRI

[官方论文页](https://neurips.cc/virtual/2026/poster/152230) · [作者来源](https://openreview.net/forum?id=UbC0NrVCfU)

- **问题 / 瓶颈** · 直接生成易引入幻觉，单独测试时优化易拟合噪声。
- **核心创新 / 方法** · 门控扩散一致切向与观测支持的正交创新。
- **Baseline** · 仅扩散、TD-DIP 和加法组合。
- **Benchmark** · cine MRI，含高加速与外域先验。
- **关键结果 / 消融** · 各设置改善，外域先验和高加速优势更明显。
- **适用条件 / 局限** · 下降保证有明确局部条件，其他成像域待验。

**可复用机制** · 先验不可靠时按方向融合证据，并用测量决定允许偏离。

<a id="paper-148893"></a>

## PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148893) · [作者来源](https://openreview.net/forum?id=uPe7n5ieyf)

- **问题 / 瓶颈** · 全量微调会向狭窄数据分布偏移。
- **核心创新 / 方法** · 专家查询分别读取视觉语言场景先验及冻结运动先验。
- **Baseline** · 全量微调、π0.5 等 VLA。
- **Benchmark** · RoboTwin 2.0、LIBERO、两种实施体八项实机任务。
- **关键结果 / 消融** · Hard 比 π0.5 高 11 点，LIBERO 99.1%，仅更新全量微调参数的 25%。
- **适用条件 / 局限** · 需要可访问预训练专家；实机 OOD 仍低于 ID。

**可复用机制** · 将基础策略作为只读知识源，使下游保有查询广泛先验的路径。

<a id="paper-139319"></a>

## PRISM: A Benchmark for Programmatic Spatial-Temporal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/139319) · [作者来源](https://openreview.net/forum?id=XbNjlZYLho)

- **问题 / 瓶颈** · 程序跑通遗漏画面布局问题。
- **核心创新 / 方法** · 先验执行门，再测空间及辅助动态指标。
- **Baseline** · 七种 LLM。
- **Benchmark** · PRISM 10372 个双语教学指令代码对。
- **关键结果 / 消融** · 运行成功到空间通过的平均差约 41%。
- **适用条件 / 局限** · 实证为教学动画，其他结构化输出待验。

**可复用机制** · 评测可执行产物时把运行成功和目标语义达成分开。

<a id="paper-151138"></a>

## PRISM: Asymmetric Precision-Recall Optimization for Million-Scale Root Cause Analysis

[官方论文页](https://neurips.cc/virtual/2026/poster/151138) · [作者来源](https://openreview.net/forum?id=cjaVe5kjFu)

- **问题 / 瓶颈** · 多数背景让对称两两计算支配成本。
- **核心创新 / 方法** · 定义异常-正常 precision 和异常-异常 recall，连续松弛后组合核验。
- **Baseline** · 最强比较方法未具名。
- **Benchmark** · 四个公开基准和 513 万条工业数据。
- **关键结果 / 消融** · 平均 F1 为 0.90 对 0.65，在 2^110 属性空间内低于 1 秒。
- **适用条件 / 局限** · 异常集合小且可识别时收益更明显。

**可复用机制** · 按指标需要构造稀有事件的成对比较，而不是先构造全部样本对。

<a id="paper-153474"></a>

## Prism Attention: Proposal-Refined Index Sharing Mechanism for Efficient LLMs Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/153474) · [作者来源](https://openreview.net/forum?id=L5vrlNwsCo)

- **问题 / 瓶颈** · 全重算开销大，静态共享损失注意力。
- **核心创新 / 方法** · 锚层提出索引，在后续层围绕其边缘更新。
- **Baseline** · 静态跨层共享与逐层索引。
- **Benchmark** · 长上下文自回归稀疏解码。
- **关键结果 / 消融** · 摘要报告实验支持效率与适应性。
- **适用条件 / 局限** · 依赖高注意力 token 跨层稳定及边界局部漂移。

**可复用机制** · 先测跨层变化的空间分布，再决定局部索引更新范围。

<a id="paper-139756"></a>

## PRISM-Bench: A Benchmark of Puzzle-Based Visual Tasks with CoT Error Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/139756) · [作者来源](https://openreview.net/forum?id=6ZHbONMpgQ)

- **问题 / 瓶颈** · 最终答案不能区分生成和验证能力。
- **核心创新 / 方法** · 提供恰含一个错误的推理链，要求定位首错。
- **Baseline** · 比较前沿多模态模型。
- **Benchmark** · PRISM-Bench，符号、几何和类比视觉谜题。
- **关键结果 / 消融** · 流利生成与识错能力脱节，幅度未报告。
- **适用条件 / 局限** · 单错人工链未覆盖开放任务多重错误。

**可复用机制** · 让评审定位失效步骤，避免用答题准确率代替验证能力。

<a id="paper-153862"></a>

## PRISM:Disentangling Preference Distributions for Generative Ranking

[官方论文页](https://neurips.cc/virtual/2026/poster/153862) · [作者来源](https://openreview.net/forum?id=IBAEjexlXH)

- **问题 / 瓶颈** · 嵌入生成可能混合优劣响应。
- **核心创新 / 方法** · 分解类别条件 ELBO，再以类别分离或聚合匹配处理潜空间混叠。
- **Baseline** · 既有嵌入生成排序。
- **Benchmark** · 摘要围绕生成偏好对及排序。
- **关键结果 / 消融** · 两种变体均面向保持排序语义；幅度未报告。
- **适用条件 / 局限** · 依赖嵌入和标签能表达偏好类别。

**可复用机制** · 合成对比数据应显式约束判别边界两侧的可分性。

<a id="paper-152192"></a>

## PrismFlow: Residual Dynamics for Flow Matching in Time-Series Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152192) · [作者来源](https://openreview.net/forum?id=UrxwEBaiit)

- **问题 / 瓶颈** · 近邻状态相反速度在 MSE 下被平均。
- **核心创新 / 方法** · 用 Koopman 启发残差与置信度感知赢家更新。
- **Baseline** · 单一全局速度场。
- **Benchmark** · 多尺度和多模态时序生成，频谱、模式覆盖。
- **关键结果 / 消融** · 摘要报告局部动态改善，幅度未报告。
- **适用条件 / 局限** · 依赖可判定专家匹配及有限专家容量。

**可复用机制** · 以稳定共享场承载共性，把平均掉的动力学留给竞争式残差。

<a id="paper-154388"></a>

## PRISM: Primitive Routing via In-context Skill Mixing for Lifelong VLA

[官方论文页](https://neurips.cc/virtual/2026/poster/154388) · [作者来源](https://openreview.net/forum?id=DwiSjXGZ79)

- **问题 / 瓶颈** · 单一更新缺少明确技能边界及分阶段调用接口。
- **核心创新 / 方法** · 为技能族各存一个动作专家适配器，用视觉语言路由器按块调用。
- **Baseline** · 联合更新及匹配随机旋转。
- **Benchmark** · 复合操作任务和技能子空间分析。
- **关键结果 / 消融** · 复合 LoRA 约半数能量落在技能子空间，随机旋转时接近零。
- **适用条件 / 局限** · 路由与整合的独立任务贡献待核实。

**可复用机制** · 将技能参数重合度和在新任务中被选择的执行效果同时查证。

<a id="paper-153318"></a>

## PRISM: Principal Subspace Alignment for Parameter-Efficient Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/153318) · [作者来源](https://openreview.net/forum?id=MCPaZwUbx2)

- **问题 / 瓶颈** · 全层统一低秩忽略 Q–K 和 V–O 的相互作用。
- **核心创新 / 方法** · 每个矩阵按配对矩阵的谱基构造低秩更新。
- **Baseline** · 现有 PEFT。
- **Benchmark** · 合成收敛对照、算术、代码和视觉。
- **关键结果 / 消融** · 摘要报告更快收敛且下游优于对照。
- **适用条件 / 局限** · 维数、基更新频率和资源待核实。

**可复用机制** · 用同秩预算比较独立随机子空间和由下游搭档决定的敏感子空间。

<a id="paper-153153"></a>

## PRISM: Programming Interactive Scenes from Monocular Images for Embodied Simulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153153) · [作者来源](https://openreview.net/forum?id=NTuLcEoan7)

- **问题 / 瓶颈** · 视觉重建难显式赋予有效关节与碰撞结构。
- **核心创新 / 方法** · 将单图转成描述几何、关节和物性的程序，经物理引擎反馈迭代。
- **Baseline** · 开环程序和单目重建。
- **Benchmark** · 交互场景的物件、关系及仿真可用性。
- **关键结果 / 消融** · 摘要报告优于所测开环方法。
- **适用条件 / 局限** · 单图无法完全识别真实隐含物性，仿真合理性与现实保真应分开。

**可复用机制** · 对同一重建独立测渲染相似与可执行交互。

<a id="paper-151674"></a>

## Privacy Amplification Persists under Unlimited Synthetic Data Release

[官方论文页](https://neurips.cc/virtual/2026/poster/151674) · [作者来源](https://openreview.net/forum?id=Ysuab2V5oE)

- **问题 / 瓶颈** · 旧界假定模型维度比发布样本更多。
- **核心创新 / 方法** · 用充分统计量降维，并从 Fisher 信息界定 Rényi 散度。
- **Baseline** · 线性生成器的既有有限样本放大分析。
- **Benchmark** · 理论线性生成及无界发布数的隐私界。
- **关键结果 / 消融** · 证明部分条件下样本数量无界仍可有放大。
- **适用条件 / 局限** · 不代表任意生成器能无限发布，依赖线性与模型条件。

**可复用机制** · 将统计可识别性作为发布设计的审核变量。

<a id="paper-150901"></a>

## Privacy by Postprocessing the Discrete Laplace Mechanism

[官方论文页](https://neurips.cc/virtual/2026/poster/150901) · [作者来源](https://openreview.net/forum?id=eYwUlKuL6y)

- **问题 / 瓶颈** · 直接代入有偏，额外发布可能扩大隐私预算。
- **核心创新 / 方法** · 从离散 Laplace 输出构造无偏估计，并建立到连续 Laplace 和 Staircase 的分布变换。
- **Baseline** · 直接对噪声值取函数。
- **Benchmark** · 结构化函数的方差及计算。
- **关键结果 / 消融** · 可产生同隐私参数的目标机制，部分函数求解为线性或多项式时间。
- **适用条件 / 局限** · 一般函数可能指数复杂，方差仍需比较。

**可复用机制** · 保留单次离散发布，对不同统计量按方差和计算选择后处理。

<a id="paper-150803"></a>

## Privacy-Preserving Retrieval-Augmented Generation with Plausible Deniability

[官方论文页](https://neurips.cc/virtual/2026/poster/150803) · [作者来源](https://openreview.net/forum?id=fHPuHnOJfR)

- **问题 / 瓶颈** · 逐 token 保护随文本长度增加开销。
- **核心创新 / 方法** · 随机选文档组生成，并用答案级隐私检验核查多组可产生性。
- **Baseline** · 逐 token 隐私方案。
- **Benchmark** · 三项 QA 和三个语言模型；隐私、效用及速度。
- **关键结果 / 消融** · 给出差分隐私界，实测成员推断接近随机，快 17–33 倍。
- **适用条件 / 局限** · 文档分组和生成概率模型的适用条件待查。

**可复用机制** · 按答案级效用和信息释放边界设计评估，勿把字数当唯一风险量。

<a id="paper-155428"></a>

## Privacy Risk Scales with Effective Dimension in Federated Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155428) · [作者来源](https://openreview.net/forum?id=5j1BWwjOvX)

- **问题 / 瓶颈** · 相同会计配置下，跨模型规模的经验信息泄漏未必一致。
- **核心创新 / 方法** · 在高斯信道假设下度量更新轨迹互信息，依有效维度定噪。
- **Baseline** · 固定噪声。
- **Benchmark** · 视觉和语言联邦训练，测跨规模泄漏。
- **关键结果 / 消融** · 特定谱增长时泄漏按 d/log d 量级，尺度校准缓解漂移。
- **适用条件 / 局限** · 该信息指标与正式 DP 会计不同，结论依赖高斯及谱模型。

**可复用机制** · 在训练规模扫描中并列报告形式隐私参数和经验客户端信号。

<a id="paper-154273"></a>

## Privately Clipping Heavy-Tailed Data

[官方论文页](https://neurips.cc/virtual/2026/poster/154273) · [作者来源](https://openreview.net/forum?id=F3Hoi9uC0q)

- **问题 / 瓶颈** · 重尾向量被截后系统偏移，放松阈值增加隐私噪声
- **核心创新 / 方法** · 以被裁向量残差方向的一致性代理偏差，对照额外噪声方差选择阈值
- **Baseline** · 现有隐私阈值选择方法，名称未报告
- **Benchmark** · 多个数据集，详情未报告
- **关键结果 / 消融** · 理论给出重尾条件下一致性与偏差关系，摘要称实验优于对照
- **适用条件 / 局限** · 需要估计残差方向且选择本身也消耗隐私预算

**可复用机制** · 调隐私裁剪阈值时不要只看梯度范数分位数，也核对方向性偏差

<a id="paper-154676"></a>

## PrivateSeal: Low-Sensitivity Latent Directions for Diffusion-Resilient User-Specific Watermarking

[官方论文页](https://neurips.cc/virtual/2026/poster/154676) · [作者来源](https://openreview.net/forum?id=BrU1KQABN9)

- **问题 / 瓶颈** · 编辑和再生成易擦除用户级标记
- **核心创新 / 方法** · 在低敏感潜方向嵌入并以密钥投影验证
- **Baseline** · 面向再生成的同类水印，摘要未列名称
- **Benchmark** · W-Bench、跨模型与跨数据集；编辑和再生成鲁棒性
- **关键结果 / 消融** · 摘要称具有竞争力和迁移性，数值未报告
- **适用条件 / 局限** · 依赖潜空间及敏感方向估计

**可复用机制** · 溯源评测时对比标记在生成编辑前后的可验证性

<a id="paper-139070"></a>

## ProactBench: Beyond What The User Asked For

[官方论文页](https://neurips.cc/virtual/2026/poster/139070) · [作者来源](https://openreview.net/forum?id=n38rkZrrzQ)

- **问题 / 瓶颈** · 显式请求基准无法测主动理解暗示
- **核心创新 / 方法** · 用带信息差的规划者、用户和助手模拟三种对话阶段的触发
- **Baseline** · 16 个模型和六个标准基准
- **Benchmark** · 198 段对话、624 个触发点、24 种沟通风格
- **关键结果 / 消融** · 结束后主动帮助表现较难，六个标准基准预测力较弱
- **适用条件 / 局限** · 结果受对话模拟、风格覆盖与判分器影响

**可复用机制** · 对主动助手分别验收单条线索、多条线索与完成后跟进

<a id="paper-153423"></a>

## Proactive Instance Navigation with Comparative Judgment for Ambiguous User Queries

[官方论文页](https://neurips.cc/virtual/2026/poster/153423) · [作者来源](https://openreview.net/forum?id=LR1XtBSs7q)

- **问题 / 瓶颈** · 首次符合描述的实例可能与用户意图不同
- **核心创新 / 方法** · 先形成候选池，再问能区分候选的二元问题并剪枝
- **Baseline** · 相同最少输入的交互方法和详细描述的非交互方法
- **Benchmark** · CoIN-Bench、TextNav；成功率和回复长度
- **关键结果 / 消融** · CoIN 两项改善，TextNav 成功率领先，摘要未列具体值
- **适用条件 / 局限** · 依赖候选池覆盖目标且用户能答区分问题

**可复用机制** · 含糊指令在操作前先选择能排除一组假设的最短澄清问题

<a id="paper-151067"></a>

## Probabilistic Recursive Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/151067) · [作者来源](https://openreview.net/forum?id=dDjsb4dq8O)

- **问题 / 瓶颈** · 确定性循环只沿单一路径探索
- **核心创新 / 方法** · 以随机潜变量表示推理轨迹，用摊销变分推断训练
- **Baseline** · 确定性循环与递归模型
- **Benchmark** · 结构化推理和多解约束满足
- **关键结果 / 消融** · 摘要称两类任务改善，并演示无条件生成
- **适用条件 / 局限** · 尚无规模化任务数字或计算预算消融

**可复用机制** · 多解任务用潜轨迹采样对照仅增加递归层数

<a id="paper-150974"></a>

## Probabilistic Tiny Recursive Model

[官方论文页](https://neurips.cc/virtual/2026/poster/150974) · [作者来源](https://openreview.net/forum?id=ds7o8yEDK5)

- **问题 / 瓶颈** · 确定性递归可能陷入局部解，输入增强又依赖任务
- **核心创新 / 方法** · 深递归步加噪声并并行运行，用既有 Q 头选择结果
- **Baseline** · 原始 TRM 和前沿 LLM 结果
- **Benchmark** · Sudoku-Extreme 和 Pencil Puzzle Bench；准确率
- **关键结果 / 消融** · 前者 87.4% 至 98.75%，后者 65% 至 91%
- **适用条件 / 局限** · 需已有候选质量头，数字主要来自谜题

**可复用机制** · 不改模型参数，比较隐状态采样与输入扰动的预算效率

<a id="paper-155102"></a>

## Probability-Conserving Flow Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/155102) · [作者来源](https://openreview.net/forum?id=8QCD1PgPKI)

- **问题 / 瓶颈** · 固定引导可把样本推离已学习流形
- **核心创新 / 方法** · 用连续性方程将引导拆成散度与得分平行项，分别时变调节与衰减
- **Baseline** · 普通 CFG 及外推式引导
- **Benchmark** · 图像生成基准，摘要未列名称和具体指标
- **关键结果 / 消融** · 摘要称高引导下改善真实感并减少幻觉和过饱和
- **适用条件 / 局限** · 结论依赖论文的流形和连续性分析条件

**可复用机制** · 生成编辑中按去噪阶段调整条件强度，检查饱和度和伪影

<a id="paper-149095"></a>

## Probe-Guided Gradient Balancing for Multimodal Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149095) · [作者来源](https://openreview.net/forum?id=sx31kS8xCo)

- **问题 / 瓶颈** · 融合损失的统计容易被强模态支配
- **核心创新 / 方法** · 在各模态停止梯度的特征上训练小探针，以此引导弱模态有界梯度增强
- **Baseline** · 抑制主导模态及其他平衡方法
- **Benchmark** · 八基准、四领域、2 至 4 模态
- **关键结果 / 消融** · 高不平衡时改善，低不平衡时保持竞争力
- **适用条件 / 局限** · 探针准确性和梯度调节边界需受控

**可复用机制** · 先诊断单模态可学性，再选择增强弱分支或压低强分支

<a id="paper-151114"></a>

## Probing for Representation Manifolds in Superposition

[官方论文页](https://neurips.cc/virtual/2026/poster/151114) · [作者来源](https://openreview.net/forum?id=csOfiTnHi8)

- **问题 / 瓶颈** · 单方向探针难覆盖叠加表征的多种特征。
- **核心创新 / 方法** · 先学可线性预测的概念特征空间，再识别编码方向。
- **Baseline** · 线性回归探针。
- **Benchmark** · Llama 2-7B 的时间与空间概念。
- **关键结果 / 消融** · 时间流形干预可改变作品发行年份输出。
- **适用条件 / 局限** · 验证主要为时间和空间，线性可解码及可控不等于完整机制。

**可复用机制** · 对多维概念先估子空间再做因果干预。

<a id="paper-152444"></a>

## Probing Persona-Dependent Preferences in Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152444) · [作者来源](https://openreview.net/forum?id=T5XaD43ds8)

- **问题 / 瓶颈** · 不同角色行为是否由同一机制承担不清楚。
- **核心创新 / 方法** · 在残差流上用成对任务选择训练线性探针，跨角色迁移及干预。
- **Baseline** · 不同角色与提示。
- **Benchmark** · Gemma-3-27B、Qwen-3.5-122B 成对选择。
- **关键结果 / 消融** · 助手探针跨角色预测，Gemma 上操控选择。
- **适用条件 / 局限** · 干预证据限定在测试模型和选择设置。

**可复用机制** · 先检验角色变化是否沿共享方向调整，再考虑单独对齐各角色。

<a id="paper-139405"></a>

## Probing the Trajectories of Reasoning Traces in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139405) · [作者来源](https://openreview.net/forum?id=SqFPT2YE5W)

- **问题 / 瓶颈** · 只看最终答案无法判断中间轨迹何时有效。
- **核心创新 / 方法** · 按 token 百分位截断并回灌，比较派生答案分布。
- **Baseline** · 长度、形式和 token 控制及跨模型探针。
- **Benchmark** · 五模型，GPQA Diamond、MMLU-Pro、Omni-MATH-2。
- **关键结果 / 消融** · 进度增加时正确率和承诺上升；强模型可能纠错或被锚定。
- **适用条件 / 局限** · 截断协议可能与自然继续不同。

**可复用机制** · 用匹配等长控制识别推理前缀的实例特异信息。

<a id="paper-154346"></a>

## Probing Visual Planning in Image Editing Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154346) · [作者来源](https://openreview.net/forum?id=EHLQuJxU7e)

- **问题 / 瓶颈** · 视觉逐步生成耗时，视觉识别和逻辑混杂。
- **核心创新 / 方法** · 将规划输出变成单次图像变换，用程序生成抽象谜题。
- **Baseline** · 闭源、开源自回归与扩散编辑模型及人类效率。
- **Benchmark** · AMAZE 迷宫和皇后，像素保真和逻辑有效性。
- **关键结果 / 消融** · 零样本普遍弱，小规模微调可外推，最佳模型仍不及人类效率。
- **适用条件 / 局限** · 外推证据为抽象视觉谜题。

**可复用机制** · 给规划输出独立的逻辑验收，避免像素相似掩盖非法解。

<a id="paper-148180"></a>

## Problem-Dependent Dynamic Regret over a Predictor Class with One-Gradient Feedback

[官方论文页](https://neurips.cc/virtual/2026/poster/148180) · [作者来源](https://openreview.net/forum?id=zhLmhEjDZ0)

- **问题 / 瓶颈** · 预测器质量不恒定且每轮仅一条反馈。
- **核心创新 / 方法** · Hedge 汇聚预测器，几何学习率网格加乐观元学习。
- **Baseline** · 按路径长度最坏界和小损失界比较。
- **Benchmark** · 在线凸优化，动态遗憾。
- **关键结果 / 消融** · 最优预测器成本对数增长，同时保留小损失及最坏适配界。
- **适用条件 / 局限** · 有限预测器类及在线凸假设。

**可复用机制** · 让预测器信号只在能改善保证时接管梯度更新。

<a id="paper-154360"></a>

## ProbMedTOD: A Bayesian Network Guided Task-Oriented Dialogue System for Patient History Taking

[官方论文页](https://neurips.cc/virtual/2026/poster/154360) · [作者来源](https://openreview.net/forum?id=E9x9Hty6Qa)

- **问题 / 瓶颈** · 小模型难持续维护多轮假设。
- **核心创新 / 方法** · 从记录构建贝叶斯网络，后验跟踪交给网络，策略选择信息丰富问题。
- **Baseline** · 语言模型问诊代理。
- **Benchmark** · DDXPlus 和 MIMIC-IV Notes。
- **关键结果 / 消融** · 摘要称优于比较代理，幅度未报告。
- **适用条件 / 局限** · 实证为问诊，依赖图结构和参数覆盖。

**可复用机制** · 预算有限的主动调查代理可让符号后验负责状态，让生成器负责交互。

<a id="paper-149562"></a>

## ProCARE: Real-World Study Automation via Profile-Grounded Evidence Contracts

[官方论文页](https://neurips.cc/virtual/2026/poster/149562) · [作者来源](https://openreview.net/forum?id=pBuGfb2nFe)

- **问题 / 瓶颈** · 数据私有时间和粒度语义造成代码可运行但推断无效。
- **核心创新 / 方法** · 从数据画像生成证据契约，再把研究目标编成有类型中间表示，用验证和局部修复。
- **Baseline** · 强 LLM 代理。
- **Benchmark** · 36 个电子病历任务，运行性、语义一致和可追溯。
- **关键结果 / 消融** · 三方面改善，数值未报告。
- **适用条件 / 局限** · 依赖证据契约和确定性规则的覆盖。

**可复用机制** · 让数据约束贯穿生成、执行到解释，可独立检查每阶段。

<a id="paper-148323"></a>

## Procedural Memory Distillation: Online Reflection for Self-Improving Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148323) · [作者来源](https://openreview.net/forum?id=yghv7C3L8K)

- **问题 / 瓶颈** · 回合级验证丢失重复策略和失败。
- **核心创新 / 方法** · 存轨迹、反思教训及反复模式，自教师按记忆条件监督当前策略。
- **Baseline** · RLVR 和 SDPO 一类回合监督。
- **Benchmark** · 基于可验证奖励的在线训练。
- **关键结果 / 消融** · 推理阶段无需外置记忆；摘要所述收益待全文核对。
- **适用条件 / 局限** · 依赖在线轨迹质量和验证覆盖。

**可复用机制** · 将记忆用作可撤除的训练支架，保留策略本身的迭代能力。

<a id="paper-150157"></a>

## Procedural Refinement by LLM-driven Algorithmic Debugging for ARC-AGI-2

[官方论文页](https://neurips.cc/virtual/2026/poster/150157) · [作者来源](https://openreview.net/forum?id=kEvf2Ms1q9)

- **问题 / 瓶颈** · 只看输出错误无法分辨哪条假设失败。
- **核心创新 / 方法** · 将候选作为 Prolog 声明程序执行，用 SLD 推导树导引修正。
- **Baseline** · 对照不同模型及搜索深度广度。
- **Benchmark** · ARC-AGI-2 和 RAVEN 补充评估，Pass@2。
- **关键结果 / 消融** · 公共评估 Gemini-3-Flash 为 56.67%，GPT-5.5 xHigh 为 98.33%。
- **适用条件 / 局限** · 需可执行声明表示，公共成绩不能替代私有泛化。

**可复用机制** · 把程序追踪转成可读的假设依赖证据，再执行语义修正。

<a id="paper-150513"></a>

## Process-Aware LNS for Large-Scale MILP via Context-Enhanced Fine-Tuned LLM-driven Selector

[官方论文页](https://neurips.cc/virtual/2026/poster/150513) · [作者来源](https://openreview.net/forum?id=hXb3PI8MAB)

- **问题 / 瓶颈** · 固定算子不适应求解不同阶段。
- **核心创新 / 方法** · 离线训练多样算子，再用事后 oracle 轨迹微调选择器，输入历史表现和奖励。
- **Baseline** · Gurobi、经典及 LLM 驱动 LNS。
- **Benchmark** · 百万变量 MILP。
- **关键结果 / 消融** · 比相关 LLM 方法加速逾 6 倍。
- **适用条件 / 局限** · 涉及异步部署，速度不能归因于选择器单项；其他组合问题需复测。

**可复用机制** · 让元策略基于算子曾解决的困难选择下一次搜索动作。

<a id="paper-148573"></a>

## Process-conditioned Pretraining with Topographic Spatial Retrieval for Large EEG Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148573) · [作者来源](https://openreview.net/forum?id=wrHWTrf4Uv)

- **问题 / 瓶颈** · 不同电极配置和心理过程被混入统一表征。
- **核心创新 / 方法** · 映射统一通道区域模板，按协议切换残差分支并加权掩码重建。
- **Baseline** · 既有 EEG 基础模型。
- **Benchmark** · 九项 BCI 基准及通道丢弃消融。
- **关键结果 / 消融** · 摘要称总体有竞争力，幅度未报告。
- **适用条件 / 局限** · 需可用协议标记和可对齐空间坐标。

**可复用机制** · 把元数据用于无监督分支和空间掩码，再分别测传感器与过程迁移。

<a id="paper-151998"></a>

## ProCLIP: Progressive Vision-Language Alignment via LLM-based Embedder

[官方论文页](https://neurips.cc/virtual/2026/poster/151998) · [作者来源](https://openreview.net/forum?id=WH8ZDT099q)

- **问题 / 瓶颈** · 直接替换损害预训练跨模态结构。
- **核心创新 / 方法** · 先蒸馏原文本空间到 adapter，再以图像自蒸馏和实例及全局约束调优。
- **Baseline** · 原 CLIP 及替换文本编码器思路。
- **Benchmark** · 零样本识别、长文本与多语理解。
- **关键结果 / 消融** · 摘要称改善零样本准确率，幅度未报告。
- **适用条件 / 局限** · 依赖旧模型语义知识，继承可能延续原错误。

**可复用机制** · 换模态编码器时可分开安排几何迁移和新能力学习。

<a id="paper-139834"></a>

## ProcObject-10K: Benchmarking Object-Centric Procedural Understanding in Instructional Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/139834) · [作者来源](https://openreview.net/forum?id=1x54DkGsK7)

- **问题 / 瓶颈** · 模型可合理作答却无法定位对象状态变化。
- **核心创新 / 方法** · 从前提、演变、反事实、错误到就绪测状态推理与时间证据。
- **Baseline** · 13 种 MLLM、对象级伪监督微调。
- **Benchmark** · 10522 问答、1799 视频，含第一与第三视角，mIoU。
- **关键结果 / 消融** · 定位 mIoU 低于 45%；对象约束微调可迁移到视频问答和具身规划。
- **适用条件 / 局限** · 定位标签范围限制对开放推理的外推。

**可复用机制** · 为操作代理检验就绪判断时一并要求支撑该判断的时间片。

<a id="paper-149404"></a>

## ProCTI: Prototype-Refined Global Conditioning for Diffusion-Based Time Series Imputation

[官方论文页](https://neurips.cc/virtual/2026/poster/149404) · [作者来源](https://openreview.net/forum?id=qJv71MIpc5)

- **问题 / 瓶颈** · 窗口缺失或噪声大使局部扩散上下文失效。
- **核心创新 / 方法** · 学习数据集级原型并检索，与窗口条件一起引导反向扩散。
- **Baseline** · 既有局部条件扩散补全。
- **Benchmark** · 多时序数据集，随机及按属性缺失。
- **关键结果 / 消融** · 随机缺失总体更优，属性缺失具竞争力。
- **适用条件 / 局限** · 全局原型对漂移数据或稀有模式可能失配。

**可复用机制** · 按缺失机制比较局部与全局条件的互补信息。

<a id="paper-148302"></a>

## ProEdit: Inversion-based Editing From Prompts Done Right

[官方论文页](https://neurips.cc/virtual/2026/poster/148302) · [作者来源](https://openreview.net/forum?id=yr9AcyQrnt)

- **问题 / 瓶颈** · 源图一致性注入过强压制目标改变。
- **核心创新 / 方法** · 局部混合源和目标 KV，并偏移编辑区反演噪声。
- **Baseline** · RF-Solver、FireFlow、UniEdit 等集成方法。
- **Benchmark** · 图像与视频指令编辑。
- **关键结果 / 消融** · 摘要称保持背景且改善编辑，幅度未报告。
- **适用条件 / 局限** · 依赖正确局部区域和可修改采样接口。

**可复用机制** · 将保持区域与变化区域分开控制，并诊断失败来自注意力还是反演状态。

<a id="paper-152540"></a>

## PRO: Enabling Precise and Robust Text Watermark for Open-Source LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152540) · [作者来源](https://openreview.net/forum?id=SP0ojrw7bn)

- **问题 / 瓶颈** · 解码由用户控制，蒸馏水印可能与检测模板偏离。
- **核心创新 / 方法** · 联合训练水印策略和生成器，加入权重扰动正则。
- **Baseline** · 既有权重蒸馏水印。
- **Benchmark** · 多个开源 LLM，TPR、FPR、PPL、合并后 AUC。
- **关键结果 / 消融** · 1% FPR 下 TPR 0.92，0.5 比例合并 AUC 0.87 对 0.79。
- **适用条件 / 局限** · 结论限定测试模型及修改条件。

**可复用机制** · 若发布模型要有来源信号，应复测变体中的检测与质量。

<a id="paper-155115"></a>

## ProGraf: Profile-Guided Planning for Step-by-Step Generation of Structured Non-Natural Images

[官方论文页](https://neurips.cc/virtual/2026/poster/155115) · [作者来源](https://openreview.net/forum?id=8I8z7rkr9Q)

- **问题 / 瓶颈** · 固定分解或多步编辑会破坏已正确结构。
- **核心创新 / 方法** · 从重复采样建立组件能力画像，按画像分解，逐步验收并失败重规划。
- **Baseline** · 固定步骤和通用代理基线。
- **Benchmark** · 304 个几何、电路、流程图等，细粒度检查点。
- **关键结果 / 消融** · 困难子集恢复 43.7% 至 77.8% 的原失败任务，消融支持画像。
- **适用条件 / 局限** · 依赖可靠的结构验证和代表性失败样本。

**可复用机制** · 让分解计划基于生成器实际弱点，并仅提交通过验证的状态。

<a id="paper-149479"></a>

## Program-as-Weights: A Programming Paradigm for Fuzzy Functions

[官方论文页](https://neurips.cc/virtual/2026/poster/149479) · [作者来源](https://openreview.net/forum?id=ppCD0mb6ty)

- **问题 / 瓶颈** · 每次 API 生成消耗高且依赖外部服务。
- **核心创新 / 方法** · 4B 编译器从自然语言规格生成冻结小解释器的参数适配器。
- **Baseline** · 直接提示 Qwen3-32B。
- **Benchmark** · FuzzyBench 的模糊函数；内存与推理速度。
- **关键结果 / 消融** · 0.6B 解释器在所测表现匹配，对照约五十分之一内存，MacBook M3 约 30 token/秒。
- **适用条件 / 局限** · 需计编译、加载与无法覆盖的函数变化。

**可复用机制** · 在固定任务质量下算一次编译可摊销的调用量，并独立验收新函数泛化。

<a id="paper-151422"></a>

## Progressive Residual Warmup for Language Model Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/151422) · [作者来源](https://openreview.net/forum?id=aoiSdieuFb)

- **问题 / 瓶颈** · 深层依赖早层提供尚未稳定的表示。
- **核心创新 / 方法** · 每层乘从零升到一的标量，越深预热越长。
- **Baseline** · 不做残差分层预热。
- **Benchmark** · 多预训规模、初始化和归一化；稳定、收敛和下游。
- **关键结果 / 消融** · 摘要报告收敛更快且泛化改善。
- **适用条件 / 局限** · 最优深度曲线和任务预算尚待查。

**可复用机制** · 对比全局学习率预热和逐层残差预热的梯度分布，定位哪个层级需要延迟。

<a id="paper-150045"></a>

## Progressive Signal Calibration for Medical Image Segmentation: Diagnosing and Correcting Structural Misalignment in Training Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/150045) · [作者来源](https://openreview.net/forum?id=lClsEZgoUW)

- **问题 / 瓶颈** · 主要类稀释梯度，边界模糊的亚类传入噪声。
- **核心创新 / 方法** · 诊断梯度质量和类别定义，校准逐阶段监督。
- **Baseline** · 原有四类分割目标。
- **Benchmark** · 私有肾病理及三套公开数据；前景 mIoU。
- **关键结果 / 消融** · 私有数据的四种架构中，前景优先提高 7.87–16.05 点。
- **适用条件 / 局限** · 若应用本身要求亚类识别，需另行确认类别信息不会丢失。

**可复用机制** · 先验证监督粒度是否与业务验收一致，再决定重权或改变输出标签。

<a id="paper-155364"></a>

## Projected Neural Additive Models as Universal Approximators

[官方论文页](https://neurips.cc/virtual/2026/poster/155364) · [作者来源](https://openreview.net/forum?id=6AZvfOFUIP)

- **问题 / 瓶颈** · 原特征可加的模型无法表示乘积。
- **核心创新 / 方法** · 先线性投影，再对投影方向学习标量函数。
- **Baseline** · NAM 与 MLP。
- **Benchmark** · 多项式精确表达和光滑函数逼近。
- **关键结果 / 消融** · 证明通用逼近，并刻画精度随投影数量和输入维度的变化。
- **适用条件 / 局限** · 投影混合会削弱原变量逐项解释，理论不保证高维训练效率。

**可复用机制** · 明确解释对象是原变量还是方向，按可接受的混合程度选择表达力。

<a id="paper-151302"></a>

## ProMo3D: Probing Motion Cues in Frozen 3D Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151302) · [作者来源](https://openreview.net/forum?id=bSpkdwCVuy)

- **问题 / 瓶颈** · 直接为四维动态训练重型解码未必必要。
- **核心创新 / 方法** · 探测静动分离，固定参考 token 的相容性分数蒸馏成稠密掩码。
- **Baseline** · 三种冻结骨干及不同秩限制。
- **Benchmark** · 用 160 个 YouTube-VOS 视频训练，迁移到 DAVIS 等。
- **关键结果 / 消融** · 摘要报告运动线索集中低维子空间，并支持零样本迁移。
- **适用条件 / 局限** · 特定观察条件和骨干上可读不保证信号因果。

**可复用机制** · 在扩展监督前先测冻结表征是否可低成本读出任务关键量。

<a id="paper-154174"></a>

## Prompt–Activation Duality: Improving Activation Steering via Attention-Level Interventions

[官方论文页](https://neurips.cc/virtual/2026/poster/154174) · [作者来源](https://openreview.net/forum?id=Fi8p6Oc5Z5)

- **问题 / 瓶颈** · 被修改状态进入 KV 后重复复用，造成累积漂移。
- **核心创新 / 方法** · 提取系统提示对自注意的贡献并按 token 门控。
- **Baseline** · 普通残差方向干预。
- **Benchmark** · 多轮人格引导，衡量连贯漂移和第十轮特质。
- **关键结果 / 消融** · 平均漂移从 −18.6 到 −1.9，第十轮表达由 78.0 到 93.1。
- **适用条件 / 局限** · 限于所测风格和会话长度，跨能力影响待查。

**可复用机制** · 对同一引导强度检查当前轮与后续缓存行为，避免只优化首轮。

<a id="paper-150317"></a>

## Prompt-Driven Exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/150317) · [作者来源](https://openreview.net/forum?id=izyPP7UWKU)

- **问题 / 瓶颈** · 局部动作噪声难跳到完全不同策略。
- **核心创新 / 方法** · 把提示分布当作策略分布，按历史成功信息做后验采样。
- **Baseline** · 动作层探索。
- **Benchmark** · 提示条件强化任务，具名基准待核实。
- **关键结果 / 消融** · 摘要给出通过预训练语义先验获取结构化探索的机制。
- **适用条件 / 局限** · 前提是提示确实诱导有意义的策略变化。

**可复用机制** · 先测提示间行为分散和回报，再判断多提示开销能否提高有效探索。

<a id="paper-155086"></a>

## Proper Scoring Rules for Agentic Uncertainty Quantification

[官方论文页](https://neurips.cc/virtual/2026/poster/155086) · [作者来源](https://openreview.net/forum?id=8XnA3xBaF5)

- **问题 / 瓶颈** · 排序和压缩汇总不能检验逐步成功概率是否可靠
- **核心创新 / 方法** · 用序贯评分定义轨迹分数，并为结果删失给出近似
- **Baseline** · AUROC、AUPRC、风险覆盖、轨迹 ECE 与标量化 Brier
- **Benchmark** · StrategyQA、Tau2-Bench、HotpotQA、WebShop
- **关键结果 / 消融** · 重新校准可显著改变 TPS 而排序几乎不变
- **适用条件 / 局限** · 删失近似与结果是否可见及估计条件有关

**可复用机制** · 若概率用于移交或停机，验证前缀校准而非只验排序

<a id="paper-150731"></a>

## Property-Guided LLM Program Synthesis for Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/150731) · [作者来源](https://openreview.net/forum?id=fp1k5OEAzu)

- **问题 / 瓶颈** · 数值标签不能指出规划程序如何修正
- **核心创新 / 方法** · 发现违反性质即停，并把失败样例交给 LLM
- **Baseline** · 最强既有程序生成方法
- **Benchmark** · 十个规划领域，分布外任务
- **关键结果 / 消融** · 每域候选程序数平均仅约 1/7，并提升免搜索解题
- **适用条件 / 局限** · 需有可验证、对任务有预测力的性质

**可复用机制** · 在授权规划沙盒里把验证器改为输出可复现失败例

<a id="paper-148388"></a>

## ProPolar: Progressive Polar Decomposition for  Implicit Neural Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/148388) · [作者来源](https://openreview.net/forum?id=yDPx5pQqmV)

- **问题 / 瓶颈** · 早期高频更新可能挤占低频结构学习
- **核心创新 / 方法** · 以低秩子空间更新动量，后期扩秩并在扩秩期间保持峰值学习率
- **Baseline** · 竞争优化器，摘要未列名称
- **Benchmark** · 图像拟合、超分、NeRF，含匹配超参搜索预算
- **关键结果 / 消融** · 后期高频阶段增益最大，摘要未列幅度
- **适用条件 / 局限** · 依赖任务粗到细的谱学习行为

**可复用机制** · 根据重建频段的残差决定何时扩大优化子空间

<a id="paper-155190"></a>

## Proposing Better Rollouts for On-Policy Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/155190) · [作者来源](https://openreview.net/forum?id=7b0JDZvzTQ)

- **问题 / 瓶颈** · 纯学生采样可能集中到教师不支持的步骤
- **核心创新 / 方法** · 信赖域下形成教师与学生的几何混合，用单次前向提议策略近似
- **Baseline** · 普通 OPD 及近期变体
- **Benchmark** · 16 项数学、知识与医学推理基准；准确率和生成长度
- **关键结果 / 消融** · Qwen3-4B-Base 数学提升 6.91，平均生成长度少 41%
- **适用条件 / 局限** · 需可访问教师对相关动作的分布，并训练提议策略

**可复用机制** · 蒸馏中实测轨迹来源与质量的因果关系，单独比较生成长度

<a id="paper-154132"></a>

## Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154132) · [作者来源](https://openreview.net/forum?id=G2dezZZe2J)

- **问题 / 瓶颈** · 外部视觉判别器未必发现动态不一致
- **核心创新 / 方法** · 测受控潜扰动下的流残差，聚焦运动区域并用于候选排序或优化
- **Baseline** · VLM 评分和外部世界模型
- **Benchmark** · 文本到视频及图像到视频，Physics-IQ、VideoPhy2-hard 与人工偏好
- **关键结果 / 消融** · TurboWan2.2 两项从 32.2 至 37.5、45.6 至 55.0
- **适用条件 / 局限** · 生成器自身动力学偏差会影响评分，需要配外部检查

**可复用机制** · 比较内部动态一致性与外部评分的相关，再决定是否用于采样选择

<a id="paper-148767"></a>

## ProQuant: Progressive Quantization-aware Training for Edge MLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148767) · [作者来源](https://openreview.net/forum?id=vCwUxyqgph)

- **问题 / 瓶颈** · 低比特损失集中在视觉理解相关层
- **核心创新 / 方法** · 据视觉敏感因子选关键层，再逐步激活量化训练块
- **Baseline** · 现有量化方法与全精度模型
- **Benchmark** · 2B–8B MLLM 的多任务基准，示例 W4A8 Qwen3-VL-2B-Instruct
- **关键结果 / 消融** · 摘要报告平均准确率提升 6.6%，距全精度约 1%
- **适用条件 / 局限** · 需预估模态敏感性，摘要未列具体指标清单

**可复用机制** · 部署时在给定比特预算优先测跨模态关键层

<a id="paper-153925"></a>

## Prospective Coding Improves Learning in Deep Continuous-Time Recurrent Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/153925) · [作者来源](https://openreview.net/forum?id=HbgNRwBlhi)

- **问题 / 瓶颈** · 连续时间多层堆叠让输入和误差信号迟滞
- **核心创新 / 方法** · 局部双抽头输入配递归正交滤波器，可按对角 SSM 并行计算
- **Baseline** · 即时输入；空间反传与完整时间反传对照
- **Benchmark** · 音频任务，MFCC 与原始音频；验证准确率
- **关键结果 / 消融** · 空间反传下两者分别由 65.7% 到 84.9%、46.4% 到 61.0%
- **适用条件 / 局限** · 目前证据来自特定连续时间模型与音频验证

**可复用机制** · 在边缘传感的多层时序模型中先做延迟诊断，再对照轻量前瞻

<a id="paper-152351"></a>

## Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction–Reality Gaps

[官方论文页](https://neurips.cc/virtual/2026/poster/152351) · [作者来源](https://openreview.net/forum?id=TikYXZwMNh)

- **问题 / 瓶颈** · 纯事后奖励看不到决策当下的错误自评
- **核心创新 / 方法** · 停止梯度的惊讶权重放大预测偏差较大的 rollout 优势
- **Baseline** · GRPO、在线蒸馏及组合的原始版本
- **Benchmark** · 单轮可验证任务和多轮个人智能体，表现与校准
- **关键结果 / 消融** · 单轮多过度自信失败，多轮多低置信成功，两类均改善
- **适用条件 / 局限** · 依赖事前概率预测与有效反馈

**可复用机制** · 分别统计高信失败和低信成功，再决定是否用预测残差加权

<a id="paper-154744"></a>

## Proteus: Incremental Memory Activation for Long-Context Sequence Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/154744) · [作者来源](https://openreview.net/forum?id=BJtTMkeGhz)

- **问题 / 瓶颈** · 起始时开放全部记忆易被早期输入占满
- **核心创新 / 方法** · 先限制可用容量，再随上下文长度增量激活
- **Baseline** · Hope-Attention、SWLA、Comba、Titans 的静态容量版
- **Benchmark** · 多种长序列模型，任务和指标未报告
- **关键结果 / 消融** · 四种架构均改善，摘要未列数值
- **适用条件 / 局限** · 需可拆分激活的记忆容器，最优调度未确定

**可复用机制** · 在相同最大容量下比较静态与分阶段预算，测晚到信息保留

<a id="paper-153745"></a>

## Prototypes of the Mind: A Unified Framework for Probing the Visual Brain

[官方论文页](https://neurips.cc/virtual/2026/poster/153745) · [作者来源](https://openreview.net/forum?id=J3DGy43GZZ)

- **问题 / 瓶颈** · 脑编码与事后解释割裂。
- **核心创新 / 方法** · 稀疏视觉原型接线性体素读出并引导刺激干预。
- **Baseline** · 单任务编码与解释研究。
- **Benchmark** · 视觉刺激、fMRI、体素选择性。
- **关键结果 / 消融** · 定位概念与刺激区域，摘要未给量化差异。
- **适用条件 / 局限** · 线性读出与原型覆盖限制解释。

**可复用机制** · 共享原型既能定位输入证据又能控制对照刺激。

<a id="paper-155560"></a>

## Prototype Topology Consistency for Visible-Infrared Lifelong Person Re-Identification

[官方论文页](https://neurips.cc/virtual/2026/poster/155560) · [作者来源](https://openreview.net/forum?id=4fE0YqAObx)

- **问题 / 瓶颈** · RGB 和红外的类别拓扑不同，遗忘不对称。
- **核心创新 / 方法** · 保留相对历史原型分布，并对齐两模态类间拓扑矩阵。
- **Baseline** · 共享主干持续训练和跨模态监督。
- **Benchmark** · VI-LReID。
- **关键结果 / 消融** · 实验支持两模块，无需存旧样本；幅度未报告。
- **适用条件 / 局限** · 实证集中于人重识别。

**可复用机制** · 蒸馏相对原型关系可保留排名并让表征继续适配。

<a id="paper-149783"></a>

## ProtoVis-Nav: Prototypical Visual Imagination for Visual-Spatial Aligned UAV Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/149783) · [作者来源](https://openreview.net/forum?id=nKMNRDLDPk)

- **问题 / 瓶颈** · 语言直回归难判断动作在 3D 中的后果。
- **核心创新 / 方法** · 线性组合未来区域原型，作为航点输出条件。
- **Baseline** · OpenUAV 比较方法，摘要未具名。
- **Benchmark** · OpenUAV 视觉语言导航。
- **关键结果 / 消融** · 摘要报告改善，幅度未核。
- **适用条件 / 局限** · 要求训练中可监督下一位置的视觉特征。

**可复用机制** · 把想象结果作为动作解码的显式中间变量。

<a id="paper-150538"></a>

## Provable Explanations for Any-Order Neural Additive Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150538) · [作者来源](https://openreview.net/forum?id=hOaJ6pyv0j)

- **问题 / 瓶颈** · 限制交互阶数仍不足以保证可计算。
- **核心创新 / 方法** · 找交互稀疏或交互感知充分性下的可处理条件。
- **Baseline** · 标准 NAM 与解释算法。
- **Benchmark** · 解释长度、时间和预测精度。
- **关键结果 / 消融** · 常数阶仍有复杂性下界；可处理设置解释更短更快。
- **适用条件 / 局限** · 强充分性与通常定义不同，复杂性结论有适用条件。

**可复用机制** · 把解释计算预算写进模型允许的交互结构。

<a id="paper-154764"></a>

## Provable Joint Decontamination for Benchmarking Multiple Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154764) · [作者来源](https://openreview.net/forum?id=B7LVM4t8mA)

- **问题 / 瓶颈** · 独立清理会让模型间的样本集合不可比。
- **核心创新 / 方法** · 联合包络共形选择控制全局污染率。
- **Baseline** · max-p。
- **Benchmark** · 多个模型和评测基准，控制率和保留检验功效。
- **关键结果 / 消融** · 保持污染控制同时功效更高。
- **适用条件 / 局限** · 保证依赖声明的校准假设。

**可复用机制** · 跨模型决策按联合目标校准，不把逐模型阈值简单合并。

<a id="paper-154669"></a>

## Provable Pruning for Efficient 3D Gaussian Splatting via Coresets

[官方论文页](https://neurips.cc/virtual/2026/poster/154669) · [作者来源](https://openreview.net/forum?id=BuQHfat14R)

- **问题 / 瓶颈** · 不限制视图目标时无非平凡乘法核心集。
- **核心创新 / 方法** · 在规定射线或视图网格按敏感度构造带权子集。
- **Baseline** · 启发式剪枝。
- **Benchmark** · 3DGS 纯剪枝和短微调。
- **关键结果 / 消融** · 作者报告短微调或不微调有优势。
- **适用条件 / 局限** · 渲染保证依赖有效性和对数透射稳定性。

**可复用机制** · 压缩前先限定真实需要保留的可观测目标。

<a id="paper-148522"></a>

## Provable Quantization with Randomized Hadamard Transform

[官方论文页](https://neurips.cc/virtual/2026/poster/148522) · [作者来源](https://openreview.net/forum?id=xFz5PQluzT)

- **问题 / 瓶颈** · 完全随机旋转成本高。
- **核心创新 / 方法** · 推导随机 Hadamard 后误差，并分析带抖动的 TurboQuant。
- **Baseline** · 完全随机旋转。
- **Benchmark** · 单位向量，每坐标 b 位的均方误差。
- **关键结果 / 消融** · 带抖动误差渐近为 π√3/2 乘 4 的负 b 次方。
- **适用条件 / 局限** · 结论是量化等级增大下的误差，非完整推理验证。

**可复用机制** · 可用明确误差保证决定旋转是否值得在部署时计算。

<a id="paper-153879"></a>

## Provable Robustness against Backdoor Attacks via the Primal-Dual Perspective on Differential Privacy

[官方论文页](https://neurips.cc/virtual/2026/poster/153879) · [作者来源](https://openreview.net/forum?id=I4p58bdzvx)

- **问题 / 瓶颈** · 各组件独自有证书时没有端到端边界。
- **核心创新 / 方法** · 用差分隐私对偶联系平滑，为组件计算并数值组合防御保证。
- **Baseline** · 随机平滑、DP-SGD。
- **Benchmark** · MNIST、CIFAR-10 的认证实验。
- **关键结果 / 消融** · 显示可组合认证，幅度未报告。
- **适用条件 / 局限** · 依赖各组件满足证书假设，实证规模有限。

**可复用机制** · 组合防御应以端到端证书评估，而非比较各组件独立得分。

<a id="paper-154352"></a>

## Provable Selective Auto-labeling with Reliability Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/154352) · [作者来源](https://openreview.net/forum?id=EEhIsOCdWt)

- **问题 / 瓶颈** · 置信阈值欠缺有限样本保证。
- **核心创新 / 方法** · 共形校准自动标签评分后选取子集。
- **Baseline** · p 值阈值规则。
- **Benchmark** · 分类和开放生成，错误标注率及功效。
- **关键结果 / 消融** · 有限样本控错，阈值类中功效渐近最佳。
- **适用条件 / 局限** · 依赖共形校准条件及可判定标签错误。

**可复用机制** · 为半自动数据生成同时报告风险预算和接收覆盖率。

<a id="paper-151681"></a>

## Provable State Estimation with Recurrent Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151681) · [作者来源](https://openreview.net/forum?id=Yohg8DGnbT)

- **问题 / 瓶颈** · 预测准确不保证潜状态能恢复物理状态。
- **核心创新 / 方法** · 将循环模型视作 Neural ODE 离散化，给潜流收缩及可调增益。
- **Baseline** · 一般循环模型。
- **Benchmark** · 可注入潜表示与估计误差的理论分析。
- **关键结果 / 消融** · 给出平滑注入和指数收敛至小邻域的条件。
- **适用条件 / 局限** · 依赖收缩与观测系统假设，离散部署需验证。

**可复用机制** · 用稳定性条件和估计增益选择可作观测器的循环表示。

<a id="paper-152506"></a>

## Provable Test-Time Scaling for Beam Search in LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152506) · [作者来源](https://openreview.net/forum?id=ScEWzifyDZ)

- **问题 / 瓶颈** · 内部似然剪枝可能抛弃最优答案。
- **核心创新 / 方法** · 以置信过滤保留路径，并分析 token 与路径覆盖。
- **Baseline** · 普通 Beam Search。
- **Benchmark** · 长程语言推理，样本预算及遗憾。
- **关键结果 / 消融** · 理论样本改善一个覆盖系数因子，实验显示困难样本更稳。
- **适用条件 / 局限** · 依赖覆盖和奖励估计误差。

**可复用机制** · 把最优候选存活率作为削减推理预算的单独约束。

<a id="paper-153881"></a>

## Provably Accurate Shapley Value Estimation in High Dimensions via Sparse Leverage Sampling

[官方论文页](https://neurips.cc/virtual/2026/poster/153881) · [作者来源](https://openreview.net/forum?id=I4HOInnEud)

- **问题 / 瓶颈** · 高维全特征采样的查询成本高。
- **核心创新 / 方法** · 从回归表述出发做稀疏 leverage 抽样。
- **Baseline** · 稠密 Leverage SHAP。
- **Benchmark** · 合成与真实稀疏数据，估计误差和稳定性。
- **关键结果 / 消融** · 查询量随支持规模平方变化，实验不逊于稠密方案。
- **适用条件 / 局限** · 增益依赖真实有效特征稀疏。

**可复用机制** · 归因查询预算优先按有效维度估，而非原始特征总数。

<a id="paper-151212"></a>

## Provably Efficient Regularized Online RLHF with Generalized Bilinear Preferences

[官方论文页](https://neurips.cc/virtual/2026/poster/151212) · [作者来源](https://openreview.net/forum?id=c90ZvP0bAX)

- **问题 / 瓶颈** · 快速遗憾是否局限 KL 不清楚。
- **核心创新 / 方法** · 在广义双线性偏好中由强凸及反对称导出平方误差间隙界。
- **Baseline** · KL 型正则化分析。
- **Benchmark** · 在线 RLHF 理论。
- **关键结果 / 消融** · 贪心策略对偶间隙受估计误差平方控制。
- **适用条件 / 局限** · 依赖偏好结构和强凸性。

**可复用机制** · 需要替换 KL 时先检验能否保留足以支持快速收敛的几何。

<a id="paper-155519"></a>

## Provably Efficient Representation Learning for Low-Rank CMDPs

[官方论文页](https://neurips.cc/virtual/2026/poster/155519) · [作者来源](https://openreview.net/forum?id=4zzk1B7I8y)

- **问题 / 瓶颈** · 约束和探索下表示学习样本效率不足。
- **核心创新 / 方法** · 无模型原始对偶学习协调回报和违规。
- **Baseline** · 低秩 CMDP 相关方法。
- **Benchmark** · 理论累计违规和遗憾随轮数缩放。
- **关键结果 / 消融** · 两种界的 K 项为 K 的 3/4 次方。
- **适用条件 / 局限** · 依赖低秩和可行性参数。

**可复用机制** · 用违规与遗憾的联合界选择无模型受限学习。

<a id="paper-155431"></a>

## Provably Reliable Classifier Guidance via Cross-Entropy Control

[官方论文页](https://neurips.cc/virtual/2026/poster/155431) · [作者来源](https://openreview.net/forum?id=5i317VTcld)

- **问题 / 瓶颈** · 高分类精度无法保证梯度引导准确。
- **核心创新 / 方法** · 以分步条件 KL 和分类平滑性界定引导向量误差。
- **Baseline** · 非平滑分类器反例。
- **Benchmark** · 条件扩散引导的理论误差。
- **关键结果 / 消融** · KL 为 ε² 时均方误差近 O(dε)，非平滑时可爆炸。
- **适用条件 / 局限** · 平滑条件及分步分类保证需能检查。

**可复用机制** · 在将判别模型梯度用作控制信号前独立测试局部稳定性。

<a id="paper-152935"></a>

## Provably Safe, Yet Performant Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152935) · [作者来源](https://openreview.net/forum?id=PHVIRBgte1)

- **问题 / 瓶颈** · 显式合成不变集难扩展、软罚无证书。
- **核心创新 / 方法** · 以安全到达值函数训练备份，前向展开构成隐式集，再以可微投影训练。
- **Baseline** · 软约束和显式证书 RL。
- **Benchmark** · 最高 10 维状态的机器人控制。
- **关键结果 / 消融** · 给出框架安全保证并完成控制验证。
- **适用条件 / 局限** · 依赖系统动力学与备份可靠性。

**可复用机制** · 以可回退轨迹检验候选动作，在接近约束边界时保留安全余量。

<a id="paper-153973"></a>

## Proxy-Based Approximation of Shapley and Banzhaf Interactions

[官方论文页](https://neurips.cc/virtual/2026/poster/153973) · [作者来源](https://openreview.net/forum?id=H7HFOu71Yi)

- **问题 / 瓶颈** · 直接估计成本高，代理可能偏。
- **核心创新 / 方法** · 多项式求树交互，用样本复用调残差。
- **Baseline** · ProxySPEX、KernelSHAP-IQ。
- **Benchmark** · 数千特征及大小预算归因误差。
- **关键结果 / 消融** · 两种预算下误差更低，给出残差校正条件。
- **适用条件 / 局限** · 效率依赖代理和样本复用条件。

**可复用机制** · 高阶归因可把可计算结构与代理偏差修正分开。

<a id="paper-148929"></a>

## ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation

[官方论文页](https://neurips.cc/virtual/2026/poster/148929) · [作者来源](https://openreview.net/forum?id=uAUn3zAFt6)

- **问题 / 瓶颈** · 原表面可能透明、无纹理或变形。
- **核心创新 / 方法** · 从初始标记像素翻译出运动匹配的彩色多面体，再用经典求解器取姿态。
- **Baseline** · 需深度、3D 模型、掩码等的估计器。
- **Benchmark** · 单目物体或局部表面，含面部及相机跟踪。
- **关键结果 / 消融** · 扩展到复杂材料及野外场景，幅度未核。
- **适用条件 / 局限** · 要求代理匹配局部刚体运动，生成误差会向求解传播。

**可复用机制** · 把难感知的真实几何翻译成已知几何，再做解析状态估计。

<a id="paper-151922"></a>

## ProxySearch: Decoupled Inference-Time Scaling for Diffusion Models via Asymmetric Noise-Rank Transfer

[官方论文页](https://neurips.cc/virtual/2026/poster/151922) · [作者来源](https://openreview.net/forum?id=WsejbW6R22)

- **问题 / 瓶颈** · 粗代理上的好样本未必在完整生成中仍好。
- **核心创新 / 方法** · 比较多种蒸馏构造及骨干的排序，一般以可迁移统计预筛，再给教师全分辨率判断。
- **Baseline** · 完整教师多次 rollout 及未蒸馏的短步控制。
- **Benchmark** · DiT、MMDiT、UNet；Spearman 秩相关。
- **关键结果 / 消融** · 某些闭式图像统计最高 0.80，学习的语义评分不高于 0.12。
- **适用条件 / 局限** · 结果限于所测代理和评分器。

**可复用机制** · 把代理设计按分数类型分层校验，谨慎复用不可迁移的语义排序。

<a id="paper-148567"></a>

## PR-Smoother: Simulator-Preserving Non-Gaussian Smoothing for Data Assimilation

[官方论文页](https://neurips.cc/virtual/2026/poster/148567) · [作者来源](https://openreview.net/forum?id=wuKaCgAn8h)

- **问题 / 瓶颈** · 直接学替代模型可能破坏既有校准。
- **核心创新 / 方法** · 让既有模拟器进入变分族及证据界，仅学未来条件修正。
- **Baseline** · 替代动态或轨迹先验的平滑思路。
- **Benchmark** · 非高斯高维数据同化，联合估状态、参数和传感偏差。
- **关键结果 / 消融** · 摘要给出保留模拟器的显式轨迹后验。
- **适用条件 / 局限** · 质量受模拟器与修正族限制，定量差异待查。

**可复用机制** · 将系统动力学误差和观测条件平滑误差分开验收。

<a id="paper-150472"></a>

## Pruning and Distilling Mixture-of-Experts into Dense Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150472) · [作者来源](https://openreview.net/forum?id=hmvlyb1yQu)

- **问题 / 瓶颈** · 只减少专家仍保留难部署的稀疏架构。
- **核心创新 / 方法** · 比较专家效用、分组及尺度选择，将保留权重拼为固定 FFN。
- **Baseline** · 只剪专家及不同评分分组。
- **Benchmark** · Qwen3-30B-A3B，约 350 种配置。
- **关键结果 / 消融** · 摘要发现评分选择影响最大，并给出重多样性的方案。
- **适用条件 / 局限** · 单模型大规模消融，跨架构与实际吞吐待查。

**可复用机制** · 以同一部署显存约束对照去专家和转稠密，不用活跃参数数代替存储。

<a id="paper-150134"></a>

## PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/150134) · [作者来源](https://openreview.net/forum?id=kRdp6aSiHL)

- **问题 / 瓶颈** · 只在单个并行维度加速仍需多次去噪。
- **核心创新 / 方法** · 用一次前向构造多深度草稿，批量验证后接受最大的相容深度。
- **Baseline** · 仅空间并行和传统逐步去噪。
- **Benchmark** · 扩散语言模型，精度和推理成本。
- **关键结果 / 消融** · 摘要明确草稿生成无需新增模型调用。
- **适用条件 / 局限** · 提交和验证会产生额外批大小，净时延与失效率待查。

**可复用机制** · 记录草稿深度、接受率及每步提交率，再看加速来自哪里。

<a id="paper-151774"></a>

## Pseudo-Labeling for Unsupervised Domain Adaptation with Kernel GLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/151774) · [作者来源](https://openreview.net/forum?id=Y7TGuV7hZn)

- **问题 / 瓶颈** · 直接源域评估可能无法识别适合目标协变量的正规化。
- **核心创新 / 方法** · 源数据一半训练候选，另一部分学插补器，并用伪标目标样本比较模型。
- **Baseline** · 源域模型选择及现有协变量偏移方案。
- **Benchmark** · 核线性、逻辑及 Poisson 回归；目标风险。
- **关键结果 / 消融** · 给出按有效标注样本量的非渐近界。
- **适用条件 / 局限** · 需要目标与源有相关可学习结构，核选择和样本分割敏感性待查。

**可复用机制** · 将伪标签用来选模型，并评估插补误差是否造成不稳定排序。

<a id="paper-150843"></a>

## PULSE: Identifying Demonstration-Utility Features with Sparse Autoencoders

[官方论文页](https://neurips.cc/virtual/2026/poster/150843) · [作者来源](https://openreview.net/forum?id=evJ1mvKFLe)

- **问题 / 瓶颈** · 相似示例可能唤起不同机制。
- **核心创新 / 方法** · 以小标注发现集采样多组示范，将相对于零样本的效用差与稀疏特征激活差配对。
- **Baseline** · 外部查询示范相似度。
- **Benchmark** · 上下文学习的数据选择与稀疏特征诊断。
- **关键结果 / 消融** · 摘要给出正负效用方向的构建。
- **适用条件 / 局限** · 依赖发现集和可用 SAE，稀疏关联不是因果，净效果待查。

**可复用机制** · 用同样示范长度和标签预算比较内部探针及语义近邻。

<a id="paper-154673"></a>

## Pure Exploration Beyond Reward Feedback: The Role of Post-Action Context

[官方论文页](https://neurips.cc/virtual/2026/poster/154673) · [作者来源](https://openreview.net/forum?id=BtGXDXwVoF)

- **问题 / 瓶颈** · 只看标量奖励会浪费事后状态信息。
- **核心创新 / 方法** · 分别推导上下文独立中介与不独立时的最优识别复杂度。
- **Baseline** · 只观察所选臂奖励的识别。
- **Benchmark** · 随机多臂、固定置信的最优臂识别。
- **关键结果 / 消融** · 两情形均给出匹配的实例相关下界和渐近算法。
- **适用条件 / 局限** · 需要选臂后可稳定观测上下文，马尔可夫泛化待查。

**可复用机制** · 测试上下文是否能共享不同动作的统计量，再决定是否采用专门采样调度。

<a id="paper-139115"></a>

## pyCD: A Unified Benchmark for Reliable Evaluation of Cognitive Diagnosis Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139115) · [作者来源](https://openreview.net/forum?id=kGok2e0ST7)

- **问题 / 瓶颈** · 高响应预测 AUC 未必意味着掌握度或难度估计准
- **核心创新 / 方法** · 固定划分预处理等条件，分别评分预测、诊断和难度排序
- **Baseline** · 11 种诊断模型，经验难度和零样本 LLM
- **Benchmark** · 六公共数据集，含 Junyi 人工成对难度和 DOA
- **关键结果 / 消融** · 学习出的难度排序落后于经验准确率和仅看题目的零样本 LLM
- **适用条件 / 局限** · 来自教育诊断，人工测量和潜变量本身仍有误差

**可复用机制** · 世界模型暴露潜因子给规划前，用独立参考测因子，不能从预测准确率反推

<a id="paper-150623"></a>

## Pygmalion Effect in Vision: Image-to-Clay Translation for Reflective Geometry Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/150623) · [作者来源](https://openreview.net/forum?id=gjpj9pDLxF)

- **问题 / 瓶颈** · 镜面外观污染几何监督
- **核心创新 / 方法** · 将输入翻译为类似哑光黏土外观，保持共享高斯几何并分离渲染路径
- **Baseline** · 原光度 BRDF 支路与其他重建基线名称未报告
- **Benchmark** · 反光物体合成与真实数据；几何和光度指标
- **关键结果 / 消融** · 两类指标跨数据一致改善，摘要未列数字
- **适用条件 / 局限** · 伪视图应保留轮廓和空间对应

**可复用机制** · 遇到光照捷径，可对共享几何增加压低外观变化的辅助监督

<a id="paper-152660"></a>

## Q-ARVD: Quantizing Autoregressive Video Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152660) · [作者来源](https://openreview.net/forum?id=RMJiMyWid7)

- **问题 / 瓶颈** · 异质通道异常值会扩大正常通道的量化误差
- **核心创新 / 方法** · 校准时检测异常通道及数目，给异常与普通通道用不同尺度
- **Baseline** · 在 self-forcing 和 causal-forcing 视频扩散上比较现有量化
- **Benchmark** · INT8 部署；速度和模型大小
- **关键结果 / 消融** · 速度 1.30 倍，模型尺寸缩小 1.97 倍
- **适用条件 / 局限** · 依赖部署实现和异常分布

**可复用机制** · 为视频生成部署保留异常通道隔离对照，测误差是否随生成累积

<a id="paper-151910"></a>

## Q-Focus: Let the Question Guide What to See in Long Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/151910) · [作者来源](https://openreview.net/forum?id=Wy1TkJYSdQ)

- **问题 / 瓶颈** · 静态去冗余容易删去问答所需的局部上下文
- **核心创新 / 方法** · 先保全局语义，再用查询匹配视觉锚并沿相似性传播相关度
- **Baseline** · 多种现有 token 压缩以及各多模态骨干匹配预算
- **Benchmark** · LLaVA-OneVision、LLaVA-Video、Qwen3-VL 的长视频问答
- **关键结果 / 消融** · 保留 10% token 时两种 LLaVA 相对增 7.3% 和 6.6%
- **适用条件 / 局限** · 依赖相似性覆盖相关上下文，未证明所有隐式关系被保留

**可复用机制** · 低预算视频助手为当前问题动态分配视觉 token

<a id="paper-154571"></a>

## QGround: Condition-Wise Evidence Aggregation for 3D Grounding with 2D VLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/154571) · [作者来源](https://openreview.net/forum?id=CbyT2otOb4)

- **问题 / 瓶颈** · 整体匹配难判断相似物体究竟哪条描述不符
- **核心创新 / 方法** · 从自然物体视图按条件产生候选相对偏好并汇总
- **Baseline** · 整体表达匹配等候选判别方式
- **Benchmark** · ScanRefer、Nr3D；定位表现与区分性
- **关键结果 / 消融** · 总体定位改善，摘要未列幅度
- **适用条件 / 局限** · 取决于自然视图覆盖和条件拆解

**可复用机制** · 具身物体检索对位置、属性、关系保留逐条件评分

<a id="paper-150528"></a>

## Q-Residual Physics: Hamiltonian-Structured Quantum Residual Learning for Embodied Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/150528) · [作者来源](https://openreview.net/forum?id=hS2tnUR2oM)

- **问题 / 瓶颈** · 无约束残差难在摩擦或接触条件变化时迁移
- **核心创新 / 方法** · 将冲量、摩擦、滑移等模式组成 Hamiltonian 结构残差以纠正标称模型
- **Baseline** · 纯物理、神经残差、图残差和量子电路基线
- **Benchmark** · OMNIPUSH、ManiSkill2、RoboMimic、D4RL、Physion
- **关键结果 / 消融** · 摘要报告长程 rollout 误差降低 23.8%，接触切换预测提升 16.4%
- **适用条件 / 局限** · 摘要未给结构匹配对照细节，不能归因于量子实现

**可复用机制** · 将接触残差结构与模型实现拆开做匹配容量实验

<a id="paper-153242"></a>

## Quality-Diversity Optimization as Multi-Objective Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153242) · [作者来源](https://openreview.net/forum?id=Mh007MnyEG)

- **问题 / 瓶颈** · 单目标难同时保留不同的高质行为
- **核心创新 / 方法** · 把行为覆盖转为大量目标，并用集合标量化复用多目标协同搜索
- **Baseline** · 已有 QD 方法，摘要未列名称
- **Benchmark** · 多个质量多样性应用，指标未报告
- **关键结果 / 消融** · 摘要称有竞争力并继承部分理论保证
- **适用条件 / 局限** · 依赖行为描述空间与目标化方式

**可复用机制** · 机器人策略库可以按行为覆盖选择集合标量化目标

<a id="paper-150361"></a>

## Quantifying and Optimizing Path Uncertainty in Masked Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150361) · [作者来源](https://openreview.net/forum?id=idhb10oUCK)

- **问题 / 瓶颈** · 无固定解码顺序时输出质量高度依赖路径
- **核心创新 / 方法** · 以累计预测不确定性形成去噪熵，用于候选筛选或在线引导
- **Baseline** · 既有路径，摘要未列具体方式
- **Benchmark** · 推理、计划和代码基准准确率
- **关键结果 / 消融** · 摘要报告提升，未列具体幅度
- **适用条件 / 局限** · 熵是代理，跨任务的相关性仍需检验

**可复用机制** · 在同解码预算下测轨迹不确定性是否能区分高质量解

<a id="paper-150293"></a>

## Quantifying Centrality for Complex Data

[官方论文页](https://neurips.cc/virtual/2026/poster/150293) · [作者来源](https://openreview.net/forum?id=jEjnEqI3Wg)

- **问题 / 瓶颈** · 高维或非欧数据难按密度选择正常区域。
- **核心创新 / 方法** · 通过加权最优传输比较距离轮廓形成 C-score。
- **Baseline** · 欧式场景以真实密度作理论参照。
- **Benchmark** · 温度分布、手写数字、出租车轨迹等。
- **关键结果 / 消融** · 欧式极限与密度渐近等价，实证识别中心及边缘样本。
- **适用条件 / 局限** · 度量和传输代价需要符合任务。

**可复用机制** · 在轨迹或分布数据上可用相对距离结构挑代表样本。

<a id="paper-149032"></a>

## Quantifying Concentration Phenomena of Mean-Field Transformers in the Low-Temperature Regime

[官方论文页](https://neurips.cc/virtual/2026/poster/149032) · [作者来源](https://openreview.net/forum?id=tLcRuEazgY)

- **问题 / 瓶颈** · 尖锐注意力可能在不同深度出现不同集中状态。
- **核心创新 / 方法** · 把 token 当相互作用粒子，以权重诱导投影描述分布。
- **Baseline** · 比较不同温度和流动时间。
- **Benchmark** · 均场 Transformer 的 Wasserstein 距离与数值实验。
- **关键结果 / 消融** · 中期快速集中并亚稳，后期受 value 矩阵谱支配。
- **适用条件 / 局限** · 结论基于低温均场，有限真实模型需检验。

**可复用机制** · 调注意力温度时分层监测聚集，避免把中期现象外推到深层。

<a id="paper-149953"></a>

## Quantile Benchmarking Heterogeneous Web Corpora in Open LLM Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/149953) · [作者来源](https://openreview.net/forum?id=lwteHS4l8A)

- **问题 / 瓶颈** · 全局分数掩盖来源内部跨度及流行评测偏差。
- **核心创新 / 方法** · 对各来源的固定分位片做代理训练，再以共享下游指标比较。
- **Baseline** · 均匀混合和启发式 top-p。
- **Benchmark** · 40B token 消融与不同下游基准。
- **关键结果 / 消融** · 各任务来源排序不同，阈值优于两基线。
- **适用条件 / 局限** · 代理训练的排名未必跨规模或任务。

**可复用机制** · 别给不同来源共用一个阈值，先测各段对目标任务的边际价值。

<a id="paper-149618"></a>

## Quantile-Coupled Flow Matching for Distributional Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149618) · [作者来源](https://openreview.net/forum?id=okya6hL4Uh)

- **问题 / 瓶颈** · 任意配对不匹配分布 Bellman 的 Wasserstein 几何。
- **核心创新 / 方法** · 排序噪声和 Bellman 目标样本，近似一维单调最优传输。
- **Baseline** · 其他条件流匹配 critic。
- **Benchmark** · 回报分布 Wasserstein 精度。
- **关键结果 / 消融** · 提高分布精度并证明近似投影对齐。
- **适用条件 / 局限** · 排序机制用于一维回报，批有限时有近似误差。

**可复用机制** · 当目标理论依赖某距离时用匹配耦合训练，而非只改输出模型。

<a id="paper-149758"></a>

## Quantile Geometry Regularization for Distributional Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149758) · [作者来源](https://openreview.net/forum?id=nZTmdGMiNl)

- **问题 / 瓶颈** · 自举目标压窄分布。
- **核心创新 / 方法** · 用 Wasserstein 鲁棒分位估计推闭式目标校正，中位反对称保均值。
- **Baseline** · IQN 等分位分布式 RL。
- **Benchmark** · 风险敏感导航、Atari。
- **关键结果 / 消融** · 摘要报告优于现有分位方法。
- **适用条件 / 局限** · 鲁棒强度可能改变尾部校准，需按决策损失验证。

**可复用机制** · 用守恒均值的分位扰动保护风险敏感价值信号。

<a id="paper-138999"></a>

## Quantitative Assessment of Crystal Structure Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/138999) · [作者来源](https://openreview.net/forum?id=rtIvlv5N1r)

- **问题 / 瓶颈** · 阈值和单一几何指标遗漏多解及物理有效性。
- **核心创新 / 方法** · 区分结构预测设置，用方向不变、容多形的连续距离。
- **Baseline** · 七种 CSP 和两种 SICSP。
- **Benchmark** · OPAL-Bench 四数据集，无阈值几何和物理距离。
- **关键结果 / 消融** · 无模型全指标领先，几何表现与物理合理性关联不强。
- **适用条件 / 局限** · 物理指标需随生成任务定义。

**可复用机制** · 世界模型或结构生成应给多正确解，并将像素与有效性独立评分。

<a id="paper-151668"></a>

## Quantized Reasoning Models Think They Need to Think Longer, but They Do Not

[官方论文页](https://neurips.cc/virtual/2026/poster/151668) · [作者来源](https://openreview.net/forum?id=YulzlhXlgy)

- **问题 / 瓶颈** · 激进 PTQ 既降准又延长思考。
- **核心创新 / 方法** · 测中途正确但最终出错，并给过思考标记施加免训练 logit 惩罚。
- **Baseline** · 各模型量化前后及未干预。
- **Benchmark** · 五模型、三量化法、五个数学代码科学问答基准。
- **关键结果 / 消融** · 失败中最高 52% 中途答对，干预缩短 12% 至 23% 并保准确率。
- **适用条件 / 局限** · 标记和惩罚可能依赖模型语体。

**可复用机制** · 推理缩减需评测最终承诺，而非假设长链自然修正。

<a id="paper-149294"></a>

## Quantizing With Randomized Hadamard Transforms: Efficient Heuristic Now Proven

[官方论文页](https://neurips.cc/virtual/2026/poster/149294) · [作者来源](https://openreview.net/forum?id=rLkcrecPav)

- **问题 / 瓶颈** · 启发式变换难估何时接近随机旋转。
- **核心创新 / 方法** · 两次变换给坐标边际界，三次给协方差衰减，用线性矩测试决定次数。
- **Baseline** · 完全随机旋转、DRIVE、QUIC-FL。
- **Benchmark** · 坐标分布、压缩误差与复杂度。
- **关键结果 / 消融** · 两次在相应方案渐近匹配完全随机旋转。
- **适用条件 / 局限** · 单坐标接近高斯与联合分布保证不同。

**可复用机制** · 用轻量输入诊断自适应量化预处理成本。

<a id="paper-150445"></a>

## Quasi-Linear ICA for Motor Unit Decomposition during Dynamic Contractions

[官方论文页](https://neurips.cc/virtual/2026/poster/150445) · [作者来源](https://openreview.net/forum?id=hzu7eYXCns)

- **问题 / 瓶颈** · 固定 ICA 不适应用力移动造成的时变混合。
- **核心创新 / 方法** · 静态分离器前置低秩可逆变换，独立性和稳定性损失分开反传。
- **Baseline** · 经典线性 ICA。
- **Benchmark** · 动态收缩下表面肌电的运动单元分解。
- **关键结果 / 消融** · 保留分离步骤可识别性，摘要所述实证数值待核。
- **适用条件 / 局限** · 需近似低秩可逆失真和源统计条件。

**可复用机制** · 先补偿时变域扰动，再保留解析分离器的结构保证。

<a id="paper-149140"></a>

## Qubrio: High-Performance Quantum Compilation via Multi-Agent LLM Collaboration

[官方论文页](https://neurips.cc/virtual/2026/poster/149140) · [作者来源](https://openreview.net/forum?id=sXWcrsoU6J)

- **问题 / 瓶颈** · 单次生成难跟随硬件变化。
- **核心创新 / 方法** · 按操作阶段拆分，用布局、路由和优化代理及细粒度反馈。
- **Baseline** · 单次 LLM 和 PowerMove。
- **Benchmark** · 真实量子编译工作负载，运行时间和保真度。
- **关键结果 / 消融** · 两指标改善，并把部分发现迁入经典求解器。
- **适用条件 / 局限** · 依赖可验证的操作阶段和硬件反馈。

**可复用机制** · 用代理发现可写回常规求解器的规则，并独立验证规则收益。

<a id="paper-148788"></a>

## Query as a Resource: Activity-Cost Guided Remote Sensing Domain-Incremental Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/148788) · [作者来源](https://openreview.net/forum?id=v4SMwpRLeM)

- **问题 / 瓶颈** · 持续跨传感器更新会损害已有语义槽。
- **核心创新 / 方法** · 以域原型引导专家与提示，并按新旧域需求的活动成本门控 query。
- **Baseline** · 既有特征对齐与正则化方法。
- **Benchmark** · 多遥感数据集，RGB 与 SAR 等域增量检测。
- **关键结果 / 消融** · 报告适配与保留较平衡，幅度未报告。
- **适用条件 / 局限** · 需有可追踪的阶段和对象槽复用关系。

**可复用机制** · 增量感知中冻结高历史价值槽，让其余槽吸收新域。

<a id="paper-149578"></a>

## Query-Limited Community Recovery in Stochastic Block Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149578) · [作者来源](https://openreview.net/forum?id=p4JwxDfSjp)

- **问题 / 瓶颈** · 平衡均匀查询会把预算花在已可确定节点。
- **核心创新 / 方法** · 两阶段按图估计置信度，对边界节点追加查询。
- **Baseline** · 平衡非自适应均匀查询。
- **Benchmark** · 带噪邻居 oracle 的随机块模型，精确社区恢复。
- **关键结果 / 消融** · 部分条件下 n+o(n) 对 mn；已有子采样图时有次线性自适应优势。
- **适用条件 / 局限** · 需特定块模型和邻域访问。

**可复用机制** · 主动采图优先检验第一次恢复的不确定节点是否最值得追加观测。

<a id="paper-151351"></a>

## QueryStop: Dynamic Stop Signals for Efficient Streaming Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/151351) · [作者来源](https://openreview.net/forum?id=bBwetMwgJB)

- **问题 / 瓶颈** · 全局停止信号无法反映题目证据需求。
- **核心创新 / 方法** · 聚合与输入查询对齐的选定头，再预测信息充分。
- **Baseline** · 任务无关头特征。
- **Benchmark** · 四项基准、十一数据，比较停止 F1、充分率、准确率。
- **关键结果 / 消融** · 平均 F1 改善 3.52%，近似 token 节约下充分率从 87.12% 到 94.73%。
- **适用条件 / 局限** · 需访问注意力，跨骨干和证据顺序需查。

**可复用机制** · 固定读取预算测真正找到证据的比例，不把早退次数当成功。

<a id="paper-149377"></a>

## Quotient-Categorical Representations for Bellman-Compatible Average-Reward Distributional Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149377) · [作者来源](https://openreview.net/forum?id=qVHRXJt8X2)

- **问题 / 瓶颈** · 偏差函数加常数不变，直接把分布固定到绝对坐标会不适定。
- **核心创新 / 方法** · 构造商空间的类别投影算子，在线更新可联估平均增益。
- **Baseline** · 直接使用绝对实数坐标的分布 Bellman 表达。
- **Benchmark** · 独立和 Markov 抽样的理论递推。
- **关键结果 / 消融** · 算子非扩张且有不动点，所设条件下递推收敛。
- **适用条件 / 局限** · 依赖相应中心化、范数与抽样假设，应用边界待查。

**可复用机制** · 先固定可识别的相对量，再比较分布逼近和增益估计误差。

<a id="paper-150551"></a>

## QUTCC: Quantile Uncertainty Training and Conformal Calibration for Imaging Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/150551) · [作者来源](https://openreview.net/forum?id=hIqpI82zrU)

- **问题 / 瓶颈** · 均匀尺度忽略对比度、边缘及局部噪声。
- **核心创新 / 方法** · 用带分位嵌入的 U-Net 学整组条件分位数，再做空间自适应共形校准。
- **Baseline** · 单尺度和普通共形校准。
- **Benchmark** · 高维图像逆问题的区间宽度及覆盖。
- **关键结果 / 消融** · 摘要提出可在推理时高效给出自适应区间。
- **适用条件 / 局限** · 像素边际与全图覆盖不同，任务指标需核实。

**可复用机制** · 按像素位置与细节难度分组验收覆盖率，并报告区间宽度。

<a id="paper-148422"></a>

## Q-ViK: Question-Guided Visual KV Cache Eviction for Large Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148422) · [作者来源](https://openreview.net/forum?id=xvyNCwtt1q)

- **问题 / 瓶颈** · 预填充注意力和图像显著性不等于生成阶段实际用到。
- **核心创新 / 方法** · 用全缓存下的答案到视觉注意力聚合训练轻量打分，部署只在预填充后评分一次。
- **Baseline** · 图像冗余、显著性和预填充分数。
- **Benchmark** · 视觉语言长上下文，测缓存和答案；具名数据待查。
- **关键结果 / 消融** · 摘要给出不需部署生成前瞻的视觉淘汰机制。
- **适用条件 / 局限** · 教师注意力不是直接因果证据，域外问题需核实。

**可复用机制** · 对同一图像切换问题，测试缓存优先级是否随证据需求变化。

<a id="paper-154019"></a>

## RA$^2$: Retain-Anchored Attraction Preserves Forget-Adjacent Utility in LLM Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/154019) · [作者来源](https://openreview.net/forum?id=GqaU9oqqul)

- **问题 / 瓶颈** · 平均保留指标会漏掉邻域能力损伤。
- **核心创新 / 方法** · 用邻近保留表征锚定更新方向，并验证保留输出。
- **Baseline** · 现有遗忘方法。
- **Benchmark** · WMDP、MUSE，广泛及邻域效用。
- **关键结果 / 消融** · 在相近广泛效用下，作者报告邻域效用更高。
- **适用条件 / 局限** · 邻域定义及正式忘却保证需另验。

**可复用机制** · 在同等目标抑制下测附近良性能力，避免过度移除被看成好结果。

<a id="paper-150708"></a>

## RA-CFGCache: From Branch-Level Criteria to Guided-Risk Control under Classifier-Free Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/150708) · [作者来源](https://openreview.net/forum?id=g6toliY0op)

- **问题 / 瓶颈** · 单分支差异和局部误差不能代表最终样本偏差。
- **核心创新 / 方法** · 合成引导预测风险，再用传播感知系数重缩放。
- **Baseline** · 按独立分支或局部距离缓存。
- **Benchmark** · 带 CFG 的扩散推理，品质与加速。
- **关键结果 / 消融** · 摘要指出两类错配，并从风险估计直接决定缓存。
- **适用条件 / 局限** · 传播近似及不同引导强度下的可靠性待核实。

**可复用机制** · 同速度约束下对照引导残差和单分支残差的最终质量相关性。

<a id="paper-154327"></a>

## Radial-Angular Geometry for Reliable Update Diagnosis in Noisy-Label Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154327) · [作者来源](https://openreview.net/forum?id=ERuc5l7i70)

- **问题 / 瓶颈** · 同样高损失可能源于难例也可能错标。
- **核心创新 / 方法** · 用样本 Fisher 迹测能量，再比较观察标签与 EMA 教师产生的梯度。
- **Baseline** · 仅靠损失、置信和熵。
- **Benchmark** · 噪声标签学习；可靠更新检测。
- **关键结果 / 消融** · 摘要指出迹本身不识别方向，加入相对几何冲突后可分大而相容与大而冲突的更新。
- **适用条件 / 局限** · EMA 参考也可能有误，定量区分需查。

**可复用机制** · 保留困难但方向可靠的样本，别把单一梯度能量作为过滤阈值。

<a id="paper-151457"></a>

## RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn’t

[官方论文页](https://neurips.cc/virtual/2026/poster/151457) · [作者来源](https://openreview.net/forum?id=aUiKcKSG3t)

- **问题 / 瓶颈** · 标准基准不能充分区分最小检索和复杂记忆
- **核心创新 / 方法** · 对照简单时间排序检索、原子事实及块摘要，在机制任务上分开测试
- **Baseline** · Bridge、LangMem 和匹配读取器的强记忆基线
- **Benchmark** · LongMemEval-S、BEAM、EverMemBench 及 20 场景定向探针
- **关键结果 / 消融** · 原子事实在规则应用领先 45 个百分点，块摘要在模式归纳领先 33 个百分点
- **适用条件 / 局限** · 探针覆盖和读取器可能影响迁移

**可复用机制** · 用规则应用与模式归纳分别验收再决定是否加复杂记忆

<a id="paper-148691"></a>

## RAHF: Reward-Amplified Human Feedback for Closed-Loop Policy Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/148691) · [作者来源](https://openreview.net/forum?id=vlvxAFUKlx)

- **问题 / 瓶颈** · 闭环纠偏擅长当前场景但可能忘记通用驾驶经验
- **核心创新 / 方法** · 按反馈优势排序提案，训练分支以纠正闭环动作
- **Baseline** · DAgger、HG-DAgger、GRPO、AWR
- **Benchmark** · BridgeSim-NavHard 驾驶分与 HUGSIM 零样本转移
- **关键结果 / 消融** · 人类教师设置驾驶分 78.90，分支减少遗忘并可零样本转移
- **适用条件 / 局限** · 依赖可靠反馈和仿真环境，真实道路未验证

**可复用机制** · 从预训练策略上线迭代前，用冻结分支做跨场景遗忘回归

<a id="paper-154487"></a>

## RAIL: Representation-Aligned Imitation Learning for Student-Compatible Teacher Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/154487) · [作者来源](https://openreview.net/forum?id=DEj92qDbTo)

- **问题 / 瓶颈** · 学生无法复现教师依赖不可观察状态的行为
- **核心创新 / 方法** · 教师直接在师生共享空间学习，使动作兼容学生原始观察
- **Baseline** · 奖励塑形、学生事后微调及从原始观察直接 RL
- **Benchmark** · 多个控制环境和教师训练零样本迁移，名称未报告
- **关键结果 / 消融** · 摘要报告模仿差距减小且保持任务性能
- **适用条件 / 局限** · 共享空间仍可能丢失必要但无法从学生输入恢复的信息

**可复用机制** · 审计教师的可模仿性，再扩大示范数据

<a id="paper-152777"></a>

## RAM-Net: Linear-Time Sequence Modeling with Sparsely Addressable State

[官方论文页](https://neurips.cc/virtual/2026/poster/152777) · [作者来源](https://openreview.net/forum?id=QPjqzE6cUh)

- **问题 / 瓶颈** · 共享递归状态叠加不同 token 造成检索串扰
- **核心创新 / 方法** · 把状态分为独立槽，由键和查询映射到少量读写地址
- **Baseline** · Mamba2 及其他线性基线
- **Benchmark** · 长程细粒度检索、语言建模和常识推理
- **关键结果 / 消融** · 检索领先并每步访问比 Mamba2 少 32 倍状态元素
- **适用条件 / 局限** · 地址冲突与硬件不规则访问仍需确认

**可复用机制** · 长程细粒度回忆可把槽数与单步访问数分开调

<a id="paper-154003"></a>

## Random Attention Pattern Learning Enables Emergent Capabilities

[官方论文页](https://neurips.cc/virtual/2026/poster/154003) · [作者来源](https://openreview.net/forum?id=GuQoZH63Xh)

- **问题 / 瓶颈** · 平均预训练损失难反映何时学会特定注意模式
- **核心创新 / 方法** · 跟踪任务所需的注意力模式，以合成任务分离头配置影响
- **Baseline** · 不同 transformer 规模和 MLP-Mixer
- **Benchmark** · 实体间接识别、模式完成；合成线性映射和元胞自动机
- **关键结果 / 消融** · 合成任务中头数有效，头维度达最小容量后收益下降
- **适用条件 / 局限** · 机制证据部分来自合成任务，具体头分解需复核

**可复用机制** · 遇到学习拐点时先测任务所需稀疏关系是否已出现

<a id="paper-154099"></a>

## Random-Effects Centroids for Domain Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/154099) · [作者来源](https://openreview.net/forum?id=GFYiUzBsqE)

- **问题 / 瓶颈** · 单独训练各专家不能保证其平均好用
- **核心创新 / 方法** · 同时优化各源专家与其平均部署头
- **Baseline** · 已知域泛化方法及无质心目标消融
- **Benchmark** · 合成与 WILDS
- **关键结果 / 消融** · 摘要报告平均头要有质心项才有用
- **适用条件 / 局限** · 理论覆盖共同二阶矩设置，其他设置需核验

**可复用机制** · 多域专家最终要平均时，将聚合预测纳入训练目标

<a id="paper-148272"></a>

## Random-Set Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/148272) · [作者来源](https://openreview.net/forum?id=z55e3q7BpN)

- **问题 / 瓶颈** · softmax 点概率混淆分布外结构和普通低置信
- **核心创新 / 方法** · 在消息传递骨干上学习焦元证据，再用可信集合宽度估计不确定性
- **Baseline** · Classical Ensemble、GEBM、CaGCN、softmax 头
- **Benchmark** · Cora、Chameleon 留类 OOD 和 ROAD/nuScenes 跨数据路况图
- **关键结果 / 消融** · 两 OOD AUROC 为 88.84 和 84.18，nuScenes 节点准确从 0.418 增至 0.593
- **适用条件 / 局限** · 焦元选择依赖类重叠且按图数据验证

**可复用机制** · 安全感知输出可独立报告证据冲突，而非只给最佳标签置信

<a id="paper-154517"></a>

## Rank-Aware Differentially Private Release of Listwise Preferences for LLM Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/154517) · [作者来源](https://openreview.net/forum?id=D0Bw9TmdSJ)

- **问题 / 瓶颈** · 统一随机响应会损伤明确的强弱偏好
- **核心创新 / 方法** · 以指数机制采样固定大小分割，主要扰动边界项
- **Baseline** · 等预算本地差分隐私基线，含随机响应
- **Benchmark** · 下游 LLM 偏好对齐，具体任务未报告
- **关键结果 / 消融** · 同隐私预算下持续改善，幅度未报告
- **适用条件 / 局限** · 只释放二分信息，无法满足依赖完整排序的目标

**可复用机制** · 在固定隐私预算下优先保留对训练决策最稳定的排序信号

<a id="paper-150710"></a>

## Rank-Constrained Adaptation for Reliable Real-World Performance

[官方论文页](https://neurips.cc/virtual/2026/poster/150710) · [作者来源](https://openreview.net/forum?id=g5EV8VwQd4)

- **问题 / 瓶颈** · 全维适配在少量留出标签下不易稳定
- **核心创新 / 方法** · 由误分类概率拟合低维方向并只在其中学习 logit 增量
- **Baseline** · 不同群组先验可见性设置；具体适配基线未报告
- **Benchmark** · 七个真实数据集，最差群组性能
- **关键结果 / 消融** · 摘要报告最差群组改善且参数较省
- **适用条件 / 局限** · 适配集要保留少数组，错误方向可能随部署漂移

**可复用机制** · 按常错方向选择适配容量并以最差群组验收

<a id="paper-153714"></a>

## RankE: End-to-End Post-Training for Discrete Text-to-Image Generation with Decoder Co-Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/153714) · [作者来源](https://openreview.net/forum?id=JKAhKqd78L)

- **问题 / 瓶颈** · 策略 token 漂移使冻结解码器画质变差。
- **核心创新 / 方法** · 组相对偏好优化策略，奖励感知对抗训练解码器。
- **Baseline** · 冻结解码器的标准 RL。
- **Benchmark** · LlamaGen-XL、Janus-Pro，MS-COCO 30K，FID 和 CLIP。
- **关键结果 / 消融** · LlamaGen FID 15.21、CLIP 33.76，两者改善。
- **适用条件 / 局限** · 与连续表征生成的迁移待验。

**可复用机制** · 上游优化改变潜码分布时让下游解码器同步适配。

<a id="paper-153250"></a>

## Rank Is Not Capacity: Spectral Occupancy for Latent Graph Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153250) · [作者来源](https://openreview.net/forum?id=MdpohqZVhG)

- **问题 / 瓶颈** · 相同秩可能对应不同有效容量。
- **核心创新 / 方法** · 比较迹归一化正半定核谱与谱前缀。
- **Baseline** · 名义秩。
- **Benchmark** · 潜图模型的实现维度分析。
- **关键结果 / 消融** · 证明维度谱的局部规律及单调性。
- **适用条件 / 局限** · 依赖表示可由核谱刻画。

**可复用机制** · 用能量分配诊断实际使用的维度。

<a id="paper-151307"></a>

## Rank-Transformed Dissimilarity Profiles for High-Dimensional Classification

[官方论文页](https://neurips.cc/virtual/2026/poster/151307) · [作者来源](https://openreview.net/forum?id=bRnA8Byvs0)

- **问题 / 瓶颈** · 原始高维特征难直接估计。
- **核心创新 / 方法** · 将类内和类间相异度转为低维类别排名。
- **Baseline** · 常规分类器。
- **Benchmark** · 两类、多类、网络及高维小样本。
- **关键结果 / 消融** · 表现具竞争力；距离代理反映多阶矩差异。
- **适用条件 / 局限** · 依赖适宜的相异度。

**可复用机制** · 比较候选类时使用分布相对排序削弱量纲变化。

<a id="paper-148642"></a>

## RankVQ: Low-Rank Parameterized Commutative Vector Quantization for KV Cache Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/148642) · [作者来源](https://openreview.net/forum?id=wBu1wjG1xm)

- **问题 / 瓶颈** · KV 低位压缩难兼顾速度与精度。
- **核心创新 / 方法** · 低秩参数化交换式向量量化码本，构建后移除因子。
- **Baseline** · 直接可比的 KV 量化。
- **Benchmark** · LongBench、InfiniteBench、GSM8K。
- **关键结果 / 消融** · 压缩精度权衡更佳，1 位更明显。
- **适用条件 / 局限** · 依赖码本及低位内核兼容。

**可复用机制** · 把表达自由度放入离线码本学习而非在线解码。

<a id="paper-154742"></a>

## RANSAC Scoring Done Right

[官方论文页](https://neurips.cc/virtual/2026/poster/154742) · [作者来源](https://openreview.net/forum?id=BK5yH67CQC)

- **问题 / 瓶颈** · 固定阈值难跨噪声场景。
- **核心创新 / 方法** · 对候选划分以逆 Gamma 共轭先验积分尺度，再排序扫描划分。
- **Baseline** · RANSAC、MSAC、GaU、MAGSAC++。
- **Benchmark** · 约七万图像对，多种双视图任务。
- **关键结果 / 消融** · 小验证预算和超参失配下更稳。
- **适用条件 / 局限** · 依赖所设内点统计模型。

**可复用机制** · 把不稳定噪声参数作为潜变量积分，可减少验证依赖。

<a id="paper-151487"></a>

## RAO-Nav: Probing Omni-Language Models for Zero-shot Semantic Audio-Visual Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/151487) · [作者来源](https://openreview.net/forum?id=aGH4iWBX36)

- **问题 / 瓶颈** · 专训导航模型难跨多模态设置。
- **核心创新 / 方法** · 部署全模态模型并在解码空间引入 LNR。
- **Baseline** · 音视导航现有基线。
- **Benchmark** · 公共 SAVN 及全局指导设置。
- **关键结果 / 消融** · 无训练数据时优于对照，真实部署仍待验证。
- **适用条件 / 局限** · 依赖全模态基础模型和解码接口。

**可复用机制** · 把导航适配优先做成可独立对照的推理组件。

<a id="paper-152497"></a>

## RAOP: Step-Level Resource Orchestration for LLM Agents across Edge and Cloud

[官方论文页](https://neurips.cc/virtual/2026/poster/152497) · [作者来源](https://openreview.net/forum?id=SgWUf8rREQ)

- **问题 / 瓶颈** · 一次放置会改变后续缓存和负载。
- **核心创新 / 方法** · 将动态内生负载写成轨迹 MDP，用 GRPO 优化全轨迹成功率与延迟。
- **Baseline** · 短视放置。
- **Benchmark** · 重放真实模型和工具续程并重算物理时延。
- **关键结果 / 消融** · 分解短视放置遗憾来源；实测幅度待核。
- **适用条件 / 局限** · 重放和真实网络差异需复验。

**可复用机制** · 把工具请求揭示后的资源决策独立建模。

<a id="paper-154733"></a>

## RaPD: Resolution-Agnostic Pixel Diffusion via Semantics-Enriched Implicit Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/154733) · [作者来源](https://openreview.net/forum?id=BRLhAs1iAm)

- **问题 / 瓶颈** · 解码插值未改变生成潜空间限制。
- **核心创新 / 方法** · 语义引导训练连续神经图像场，按坐标查询渲染。
- **Baseline** · 离散潜空间和末端插值。
- **Benchmark** · 生成质量和分辨率扩展实验。
- **关键结果 / 消融** · 同一潜变量可变分辨率，扩散成本固定。
- **适用条件 / 局限** · 渲染本身仍随查询量变化。

**可复用机制** · 将画质扩展成本隔离到可独立预算的渲染端。

<a id="paper-148675"></a>

## RAPDrive: Shared-Latent Hybrid Decoding for Reasoning and Planning in Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/148675) · [作者来源](https://openreview.net/forum?id=vw3QZXzTta)

- **问题 / 瓶颈** · 文本逐词生成不适合长轨迹几何一致性。
- **核心创新 / 方法** · 共享 Transformer，文本自回归，运动槽掩码迭代去噪。
- **Baseline** · 非世界模型驾驶 VLA。
- **Benchmark** · NAVSIM、Bench2Drive。
- **关键结果 / 消融** · 监督版本更优，规划中心后训练进一步改善。
- **适用条件 / 局限** · 实证为驾驶；需连续轨迹实现。

**可复用机制** · 多输出间共享表示，但按各自结构选生成因子化。

<a id="paper-152988"></a>

## RAPTOR: Ridge-Adaptive Logistic Probes

[官方论文页](https://neurips.cc/virtual/2026/poster/152988) · [作者来源](https://openreview.net/forum?id=OpxC93zuD0)

- **问题 / 瓶颈** · 探针准确率不等于方向稳定。
- **核心创新 / 方法** · 岭逻辑探针验证调 L2，归一化权重作为概念向量。
- **Baseline** · 强探针基线，摘要未具名。
- **Benchmark** · 指令 LLM 与人写概念，准确率、方向稳定和训练成本。
- **关键结果 / 消融** · 精度持平或更好且训练较便宜。
- **适用条件 / 局限** · 干预展示主要为定性。

**可复用机制** · 探针应额外测重复训练的方向稳定性。

<a id="paper-150905"></a>

## Rare-Class Signal Suppression in Long-Tailed Multi-Expert Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/150905) · [作者来源](https://openreview.net/forum?id=eXqF5uD4aN)

- **问题 / 瓶颈** · 方向改善无法保证稀有信号进入参数。
- **核心创新 / 方法** · 校准损失放大尾部，再避免协调和融合抹去。
- **Baseline** · 改方向、简单聚合与能量平衡。
- **Benchmark** · 长尾多专家微调及受控对照。
- **关键结果 / 消融** · 放大后方向修改与简单聚合等效，能量平衡抹去放大。
- **适用条件 / 局限** · 结果依赖稀有类和专家设置。

**可复用机制** · 沿损失、聚合、推理三处检测稀有信号在哪步消失。

<a id="paper-153510"></a>

## Rare Events, Real Signals: Functional Ensembles as Units of Computation in Deep Spiking Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/153510) · [作者来源](https://openreview.net/forum?id=KnYG3WQcqz)

- **问题 / 瓶颈** · 平均激活可能掩盖携带类别信息的事件。
- **核心创新 / 方法** · 用跨层统计显著相关找局部功能群，分析共放电。
- **Baseline** · 权重置乱及噪声对照。
- **Benchmark** · 脉冲 ResNet 的激活和类别编码。
- **关键结果 / 消融** · 只有高共放电事件可靠编码类别，且置乱破坏结构。
- **适用条件 / 局限** · 相关性群组不等同因果回路，实证为 SNN。

**可复用机制** · 稀疏表示应按协同活动强度分层测信息。

<a id="paper-138883"></a>

## RASS: Risk-Audited Budget Selection for Compact NeRF Benchmark Subsets

[官方论文页](https://neurips.cc/virtual/2026/poster/138883) · [作者来源](https://openreview.net/forum?id=ytAbjAspfi)

- **问题 / 瓶颈** · 固定子集可能无法保持原均值和指标分布。
- **核心创新 / 方法** · 随机抽样并设误差容限，选 Wilson 下界达标的最小规模。
- **Baseline** · 全量基准及替代子集。
- **Benchmark** · NeRF 场景指标均值及分布。
- **关键结果 / 消融** · 48 场景通过声明的全局审计。
- **适用条件 / 局限** · 保全均值和分布不保证每个模型排序。

**可复用机制** · 缩短评测前先声明允许失真，再量化抽样失败概率。

<a id="paper-150084"></a>

## Rate-Constrained Edge Metadata for Sender–Receiver Generative Video Super-Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/150084) · [作者来源](https://openreview.net/forum?id=kqtZlt4mPS)

- **问题 / 瓶颈** · 仅接收端超分可能猜错细结构。
- **核心创新 / 方法** · 按结构难度发送紧凑 Canny 边缘元数据，计算总码率。
- **Baseline** · DOVE-5B 接收端超分。
- **Benchmark** · 五公开 VSR 基准与 MetaSPS 率失真。
- **关键结果 / 消融** · PSNR 平均加 1.03 dB、SSIM 加 0.055。
- **适用条件 / 局限** · 需可控发送端与可提取高质量边缘。

**可复用机制** · 按结构难恢复性分配侧信息，比盲目扩接收模型更可检验。

<a id="paper-148697"></a>

## Rationale-Guided Policy Optimization: Learning to Reason with Adaptive Rationale Scaffolding

[官方论文页](https://neurips.cc/virtual/2026/poster/148697) · [作者来源](https://openreview.net/forum?id=vitmYGWw3g)

- **问题 / 瓶颈** · 固定模仿约束探索且格式可能不同。
- **核心创新 / 方法** · 用参考理由辅助采样，仅把高奖励自生成答案转回无提示训练。
- **Baseline** · 离策略专家轨迹和拒绝采样。
- **Benchmark** · 纯文本及多模态推理。
- **关键结果 / 消融** · 摘要报告广泛改善，幅度待核。
- **适用条件 / 局限** · 依赖奖励判定及可靠理由。

**可复用机制** · 把专家监督当训练阶段可撤去脚手架。

<a id="paper-156749"></a>

## Rational Tuning of LLM Cascades via Probabilistic Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/156749) · [作者来源](https://openreview.net/forum?id=YCBVcGSZeR)

- **问题 / 瓶颈** · 独立精度忽略共同失败。
- **核心创新 / 方法** · 用参数化 Markov copula 描述联合表现后连续优化。
- **Baseline** · 贝叶斯优化阈值。
- **Benchmark** · 至少三模型的误差成本曲线，含不超过 30 样本。
- **关键结果 / 消融** · 曲线面积改善 4.3%，少样本 10.2%。
- **适用条件 / 局限** · 依赖误差依赖结构近似。

**可复用机制** · 回退路由应估后备模型在前级失败条件下的性能。

<a id="paper-151691"></a>

## RATS! Patches Talk Through Registers: Emergent Parts in Register Attention Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151691) · [作者来源](https://openreview.net/forum?id=Ylj622Nr12)

- **问题 / 瓶颈** · 单分类 token 的结构过粗。
- **核心创新 / 方法** · 经 patch→register→register→patch 路由。
- **Baseline** · 基线视觉 Transformer。
- **Benchmark** · 五分割基准、ADE20K、COCO。
- **关键结果 / 消融** · 五基准平均约 +12 mIoU，ADE20K +1.11。
- **适用条件 / 局限** · 寄存器语义一致性是经验现象。

**可复用机制** · 用有限共享中介约束空间 token 通信并审计学到的部件。

<a id="paper-150127"></a>

## RAVEL: Rare Concept Generation and Editing via Graph-driven Relational Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/150127) · [作者来源](https://openreview.net/forum?id=kU5GAMEqa5)

- **问题 / 瓶颈** · 只用单一名称易缺属性及关联。
- **核心创新 / 方法** · 图检索扩展关系证据，以多维对齐反馈迭代。
- **Baseline** · 现有文本到图像及编辑方法。
- **Benchmark** · MythoBench、Rare-Concept-1K、NovelBench。
- **关键结果 / 消融** · 多类评判改善，幅度待核。
- **适用条件 / 局限** · 取决于图检索和反馈可靠性。

**可复用机制** · 检索加入可区分的邻接关系，并按对应证据逐项检查图像。

<a id="paper-152432"></a>

## Raven: High-Recall Sequence Modeling via Sparse Memory Routing

[官方论文页](https://neurips.cc/virtual/2026/poster/152432) · [作者来源](https://openreview.net/forum?id=TAeR7iXyQR)

- **问题 / 瓶颈** · 稠密状态全量更新互扰，而滑窗会淘汰远端。
- **核心创新 / 方法** · 维护定量内存槽，每步只衰减并更新被路由到的子集。
- **Baseline** · 状态空间、线性注意与滑窗注意。
- **Benchmark** · 长距离召回及序列建模。
- **关键结果 / 消融** · 摘要给出按内容保留远端信息的方案。
- **适用条件 / 局限** · 冲突热点和槽数有限时需查。

**可复用机制** · 固定内存后比较位置淘汰、密集写与内容稀疏写。

<a id="paper-151748"></a>

## Raw-Routed Mixture of Adapters: A Causal Intervention for Routing Collapse in Time Series Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151748) · [作者来源](https://openreview.net/forum?id=YOHVtj0IBk)

- **问题 / 瓶颈** · 模式差异统计在进入路由器之前被去掉。
- **核心创新 / 方法** · 通过互信息分解和八种因果控制识别信息瓶颈。
- **Baseline** · 标准 MoE 路由修复与不同输入条件。
- **Benchmark** · 实例归一化时序骨干并复现于视觉。
- **关键结果 / 消融** · 先验信号比例对易坍缩性预测的 Spearman 为 −0.88。
- **适用条件 / 局限** · 依赖所测归一模式及路由任务。

**可复用机制** · 分别改变输入统计和负载均衡，不把信息丢失当作单纯优化失稳。

<a id="paper-151667"></a>

## RayTun3R: Online Camera Adaptation in 3D Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151667) · [作者来源](https://openreview.net/forum?id=YusfyNZLcm)

- **问题 / 瓶颈** · 内置针孔几何降低几何估计。
- **核心创新 / 方法** · 冻结主干，用短片段学习绝对和旋转编码残差，结合坐标矫正。
- **Baseline** · 无适配近针孔主干。
- **Benchmark** · 鱼眼深度及位姿，新片段迁移。
- **关键结果 / 消融** · 仅 10,752 个训练参数，摘要报告迁移改善。
- **适用条件 / 局限** · 依赖几何损失和短序列对相机的代表性。

**可复用机制** · 按相机变化设计轻量接口，再与全模型适配的资源比较。

<a id="paper-152929"></a>

## RB-LDC: Redundancy-Balanced Latent Coding for Robust Diffusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152929) · [作者来源](https://openreview.net/forum?id=PJDxN5JBij)

- **问题 / 瓶颈** · 压缩训练不保证各方向对加噪稳健。
- **核心创新 / 方法** · 将问题写成联合源信道编码，按谱和边际风险实施加权框架及注水分配。
- **Baseline** · 各向同性潜瓶颈。
- **Benchmark** · 理论风险及稀有分组容量分析。
- **关键结果 / 消融** · 理论指出敏感度异质时均匀冗余非极小极大最优。
- **适用条件 / 局限** · 真实语义敏感度估计和定量收益需查。

**可复用机制** · 测每一语义方向误差随噪声变化，不只比较压缩率。

<a id="paper-153563"></a>

## Readiness-Aware Sample Selection for Noisy Labels with Class Imbalance

[官方论文页](https://neurips.cc/virtual/2026/poster/153563) · [作者来源](https://openreview.net/forum?id=KRjwe8CvhI)

- **问题 / 瓶颈** · 统一预热会过早淘汰少数类。
- **核心创新 / 方法** · 对已具类区分特征的类别先筛，辅以针对相似错类的负学习。
- **Baseline** · 共同预热和统一置信筛选。
- **Benchmark** · 不均衡噪声标签数据；类别表现和选样质量。
- **关键结果 / 消融** · 摘要报告理论支持与经验改善。
- **适用条件 / 局限** · 需要独立判断成熟度，先验偏和长尾域外表现待核实。

**可复用机制** · 按类观测伪标精度和保留量，避免把学习慢当作错标。

<a id="paper-155483"></a>

## Reading, Not Thinking: Bridging the Modality Gap When Text Becomes Pixels

[官方论文页](https://neurips.cc/virtual/2026/poster/155483) · [作者来源](https://openreview.net/forum?id=5FTbX8n66m)

- **问题 / 瓶颈** · 渲染设置可造成假模态差异。
- **核心创新 / 方法** · 测试真实与合成文档及不同输入形式，人工分检四千余错误。
- **Baseline** · 纯文本输入和合成渲染。
- **Benchmark** · 七模型、七基准、五种模式。
- **关键结果 / 消融** · 真实文档有时与文字相当或更好；纯图输入输出长度缩短约 5–19 倍。
- **适用条件 / 局限** · 长度只是推理代理，不能依此断言具体因果。

**可复用机制** · 将内容读取、计算长度及正确率作为三项各自验收。

<a id="paper-155394"></a>

## Read It Back: Pretrained MLLMs Are Zero-shot Reward Models for Text-to-Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/155394) · [作者来源](https://openreview.net/forum?id=60UfWy2Mx4)

- **问题 / 瓶颈** · 直接评分和拆问可能依赖奖励标注或额外调参
- **核心创新 / 方法** · 冻结 MLLM 做图像条件教师强制，平均原提示词元对数似然，统一模型也可用自身理解支路
- **Baseline** · 既有 MLLM 奖励训练方式
- **Benchmark** · 两扩散模型、三 RL 算法、九 MLLM 骨干、五分布外基准
- **关键结果 / 消融** · 两变体均改善，规模更大的奖励器并非总是更佳
- **适用条件 / 局限** · 提示复原偏向可言语表达的细节，不能单独判断观感

**可复用机制** · 挑生成奖励器时同时查图文匹配信号和与策略的匹配

<a id="paper-153854"></a>

## Real2Sim in HOI: Toward Physically Plausible HOI Reconstruction from Monocular Videos

[官方论文页](https://neurips.cc/virtual/2026/poster/153854) · [作者来源](https://openreview.net/forum?id=IEWj0cJL3s)

- **问题 / 瓶颈** · 几何轨迹连贯仍可能导致接触和模拟 rollout 失败
- **核心创新 / 方法** · 按相对人体动作约束物体轨迹，再以运动学结果为模拟教师
- **Baseline** · 以往单目人-物重建
- **Benchmark** · 基准及自然视频；接触、对齐、稳定性及模拟准备度
- **关键结果 / 消融** · 摘要报告各维度改进，未列数字
- **适用条件 / 局限** · 物理投影仍受所用模拟器及参考轨迹误差约束

**可复用机制** · 视觉演示迁移验收使用接触与模拟执行指标

<a id="paper-139440"></a>

## RealDev-QA: Trajectory-Level Diagnosis for Developer RAG Under Real-World Noises

[官方论文页](https://neurips.cc/virtual/2026/poster/139440) · [作者来源](https://openreview.net/forum?id=PfvTJzO0lU)

- **问题 / 瓶颈** · 覆盖率和最终正确率掩盖首查误检向下游传播
- **核心创新 / 方法** · 标注依赖边与每步证据，并用包含真实干扰文档的轨迹归类失败
- **Baseline** · 不同系统与检索、自动及人工指标排名
- **Benchmark** · 1233 条多跳开发问答及逐步轨迹
- **关键结果 / 消融** · 超过 78% 的错轨首步缺金标准证据，首查精度超出总覆盖提供预测信号
- **适用条件 / 局限** · 来自开发问答，其他检索语料需重验

**可复用机制** · 多跳 RAG 单列起始检索质量和误证据恢复

<a id="paper-139504"></a>

## Realism VS Accuracy: Event Sequence Forecasting from a Generative Modeling Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/139504) · [作者来源](https://openreview.net/forum?id=LuWYNMlMDq)

- **问题 / 瓶颈** · 能拟合真实轨迹的模型不一定有最好的单预测
- **核心创新 / 方法** · 两套指标评生成样本，适当聚合真实度高的样本得到点预测
- **Baseline** · 统计预测方法和适配的生成模型
- **Benchmark** · 真实事件序列，分布真实度及预测准确性
- **关键结果 / 消融** · 无单模型两项都最好，样本聚合可得领先点预测
- **适用条件 / 局限** · 适用于论文的事件序列设置，具体基准口径未报告

**可复用机制** · 世界模型分别评可采样的分布与用于决策的聚合输出

<a id="paper-152931"></a>

## Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs

[官方论文页](https://neurips.cc/virtual/2026/poster/152931) · [作者来源](https://openreview.net/forum?id=PI2H51gjoE)

- **问题 / 瓶颈** · 完整推理无法支持高频闭环
- **核心创新 / 方法** · 轻量草稿与主动作专家并行验证，需时执行完整推理
- **Baseline** · 完整扩散 VLA 推理
- **Benchmark** · LIBERO 与真实输送带分拣；成功表现与延迟
- **关键结果 / 消融** · 完整轮 58.0ms，最快推测 7.8ms，任务平均 19.1ms
- **适用条件 / 局限** · 回退频率及验证开销随任务阶段和硬件变化

**可复用机制** · 部署时按动作阶段测可接受的草稿误差与回退成本

<a id="paper-148496"></a>

## Reasoning as Compression: Unifying Budget Forcing via the Conditional Information Bottleneck

[官方论文页](https://neurips.cc/virtual/2026/poster/148496) · [作者来源](https://openreview.net/forum?id=xN22FIniMr)

- **问题 / 瓶颈** · 统一长度罚会连必要推理一起压缩
- **核心创新 / 方法** · 将链条建模为相对于提示提供的条件信息，用语言先验测 token 惊讶度
- **Baseline** · 启发式长度惩罚及统一先验
- **Benchmark** · 多个模型和任务域；准确率与压缩程度
- **关键结果 / 消融** · 适度压缩时精度提升，大幅压缩时损失较小，数值未报告
- **适用条件 / 局限** · 与先验覆盖及概率校准有关

**可复用机制** · 训练短推理时对照码长和 token 数代理

<a id="paper-139400"></a>

## Reasoning-Aware IRT: Explainable Evaluation of Test-Time Scaling in Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139400) · [作者来源](https://openreview.net/forum?id=Szz5xYoydw)

- **问题 / 瓶颈** · 不同预算下原始分数会掩盖反转或过度思考
- **核心创新 / 方法** · 在项目反应模型引入预算响应及曲率，用广义 EM 拟合
- **Baseline** · 经典 IRT 和原始分数
- **Benchmark** · LiveBench 的 42 个模型；排名稳定性及留出正确性区分
- **关键结果 / 消融** · 两项改善，并识别预算划算与过度推理区间
- **适用条件 / 局限** · 依赖任务和模型的预算覆盖，参数估计需要多档预算

**可复用机制** · 对不同推理预算的模型用共同能力尺度作比较

<a id="paper-154145"></a>

## Reasoning-based Spatial Prior (RSP): Learning Spatial Priors from Multimodal LLMs for Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/154145) · [作者来源](https://openreview.net/forum?id=Fv4YeGg2aV)

- **问题 / 瓶颈** · 无监督注意力头可能并不对应定位线索
- **核心创新 / 方法** · 输入自适应融合头，用 SoftIoU 监督并调制 GroundingDINO 的可变形采样
- **Baseline** · 单独 MLLM、单独检测器与混合基线
- **Benchmark** · EgoIntention 和 RIO；常见与少见类别
- **关键结果 / 消融** · 摘要报告跨基线改善，未列数值
- **适用条件 / 局限** · 空间先验需要位置监督并依赖可获注意力

**可复用机制** · 将推理热图接入感知前，直接验收定位抗噪

<a id="paper-154933"></a>

## Reasoning Pathologies in Large Language Models: A Diagnostic Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/154933) · [作者来源](https://openreview.net/forum?id=9rcdHgSVwj)

- **问题 / 瓶颈** · 表面重复与真实状态退化未必对应
- **核心创新 / 方法** · 用状态转移诊断并对比改变状态与仅改写文本的干预
- **Baseline** · 普通诊断及通用干预
- **Benchmark** · 长链推理中的重复、漂移和提前承诺；诊断与修复效果
- **关键结果 / 消融** · 明显局部起点时定时干预较有效，但不普遍胜过对照
- **适用条件 / 局限** · 状态是抽象代理，改写本身也可能改变路径

**可复用机制** · 先测干预时机与失败起点的关系，再加固定重试

<a id="paper-139565"></a>

## ReasoningShield: Safety Moderation over Reasoning Traces of Large Reasoning Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139565) · [作者来源](https://openreview.net/forum?id=IHZnRdQHFQ)

- **问题 / 瓶颈** · 最终回答正常时中间内容仍可能不合规。
- **核心创新 / 方法** · 建立轨迹审核评测并训练轻量审核模型。
- **Baseline** · 既有回答审核工具。
- **Benchmark** · 推理轨迹与最终回答，F1。
- **关键结果 / 消融** · 审核 F1 相比回答下降最高 35.2%。
- **适用条件 / 局限** · 审核取决于可获得轨迹和定义的安全标签。

**可复用机制** · 分开测最终输出和内部轨迹审核的召回。

<a id="paper-139406"></a>

## Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/139406) · [作者来源](https://openreview.net/forum?id=SfKYInSDnR)

- **问题 / 瓶颈** · 答案级指标隐藏有效推理消失。
- **核心创新 / 方法** · 分别统计有效、空、缺失、截断轨迹及条件正确率。
- **Baseline** · 标准 SFT 与损失掩码策略。
- **Benchmark** · 开源推理模型的结构和回答指标。
- **关键结果 / 消融** · 有效轨迹可急降而条件正确率仍高。
- **适用条件 / 局限** · 结构有效不等于忠实。

**可复用机制** · 把推理协议完整性作为独立回归指标。

<a id="paper-156787"></a>

## Reasoning Under 1 Billion: Memory-Augmented Reinforcement Learning for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/156787) · [作者来源](https://neurips.cc/virtual/2026/poster/156787)

- **问题 / 瓶颈** · 弱底座随机探索难遇到有效推理。
- **核心创新 / 方法** · 用近邻情景记忆计算内在奖励。
- **Baseline** · 普通 CoT RL。
- **Benchmark** · 三个推理数据集，十亿参数以内模型。
- **关键结果 / 消融** · 摘要报告推理和泛化改善。
- **适用条件 / 局限** · 依赖记忆有成功覆盖。

**可复用机制** · 奖励同时利用已知有效模式并给新路径留空间。

<a id="paper-154790"></a>

## Reasoning via Test-Time Instance-Level Policy Gradient in Latent Space

[官方论文页](https://neurips.cc/virtual/2026/poster/154790) · [作者来源](https://openreview.net/forum?id=AxAnHnDri3)

- **问题 / 瓶颈** · 文本链可能不能探索所有表征。
- **核心创新 / 方法** · 固定权重，对潜状态用自生成奖励做策略梯度。
- **Baseline** · CoT、Best-of-N、训练法。
- **Benchmark** · GSM8K、MATH-500、AIME2024，LLaMA 和 Qwen。
- **关键结果 / 消融** · 数轮更新一般题可收敛，增加轮数可改善。
- **适用条件 / 局限** · 难题的预算和自奖励可靠性需检验。

**可复用机制** · 比较同预算下搜索文本分支与优化连续状态。

<a id="paper-151965"></a>

## Reasoning Warm-up: Scaling Label-free RL via Verifiable Surrogate Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/151965) · [作者来源](https://openreview.net/forum?id=WTnplymile)

- **问题 / 瓶颈** · 多数投票会奖励一致错误。
- **核心创新 / 方法** · 把可精确验证的辅助题放作热启动前缀并用其结果评分。
- **Baseline** · 一致性与多数投票伪奖励。
- **Benchmark** · 多项推理基准。
- **关键结果 / 消融** · 辅助成功后主任务成功概率明显提高。
- **适用条件 / 局限** · 代理奖励相关性须按任务测，不能视为主任务正确。

**可复用机制** · 选会触发相关推理状态而又便宜可验的热启动。

<a id="paper-153230"></a>

## Reasoning with Sampling: Cutting at Decision Points

[官方论文页](https://neurips.cc/virtual/2026/poster/153230) · [作者来源](https://openreview.net/forum?id=Mp3rA04Yjp)

- **问题 / 瓶颈** · 均匀切点多落在无关 token。
- **核心创新 / 方法** · 用下一 token 熵找决策点，作 Metropolis–Hastings 提议。
- **Baseline** · 均匀切点的幂分布采样。
- **Benchmark** · 实证熵突变与分岔，以及受控推理模型混合时间。
- **关键结果 / 消融** · 受控混合依赖决策数而非 token 数。
- **适用条件 / 局限** · 代理和理论分别需经验与结构假设。

**可复用机制** · 将重算预算集中在语义分支而非序列位置。

<a id="paper-152594"></a>

## Reasoning with Undecoded Tokens in Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152594) · [作者来源](https://openreview.net/forum?id=Rx75ZMFQKT)

- **问题 / 瓶颈** · 只预测当前 token 减少全局前瞻。
- **核心创新 / 方法** · 联合预测未解码位置，控制其数量；自回归用多 token 辅助训练。
- **Baseline** · 去除联合预测的扩散与普通自回归。
- **Benchmark** · 全局一致性相关的推理任务，质量和速度。
- **关键结果 / 消融** · 去除联合预测更快但下降质量，辅助自回归改善。
- **适用条件 / 局限** · 收益依赖任务进入全局约束的程度。

**可复用机制** · 把未输出位置当可预算的潜在草稿。

<a id="paper-149165"></a>

## Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149165) · [作者来源](https://openreview.net/forum?id=sNMKYsIWwn)

- **问题 / 瓶颈** · 低概率但关键的教师 token 被离策略剪切。
- **核心创新 / 方法** · 双参照解码转成学生常用表达并保语义。
- **Baseline** · 直接教师轨迹，GRPO 与 SFT。
- **Benchmark** · 三多模态主干、五视频推理基准。
- **关键结果 / 消融** · 不同主干一致改善，适用于 RL 和 SFT。
- **适用条件 / 局限** · 语义保真和风格拟合需分别检查。

**可复用机制** · 知识蒸馏先改写表达分布，避免丢掉教师关键因果步骤。

<a id="paper-151783"></a>

## Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners

[官方论文页](https://neurips.cc/virtual/2026/poster/151783) · [作者来源](https://openreview.net/forum?id=Y1oX1yuaWM)

- **问题 / 瓶颈** · 任务成功难揭示脑对齐来自哪部分。
- **核心创新 / 方法** · 比较人类行为、脑活动与模型内部状态，再对阶段做针对性干预。
- **Baseline** · 深度模型自由和有模型 RL、贝叶斯代理。
- **Benchmark** · 人类游戏学习，表现、行为匹配、脑活动预测。
- **关键结果 / 消融** · 脑预测逾 RL 基线一数量级，干预指向上下文状态表示。
- **适用条件 / 局限** · 人类脑测指标并非通用代理质量代理。

**可复用机制** · 把行为拟合的贡献拆为潜状态质量与决策机制。

<a id="paper-154264"></a>

## Rebalancing Reference Frame Dominance to Improve Motion in Image-to-Video Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154264) · [作者来源](https://openreview.net/forum?id=F5Ye7KS0H2)

- **问题 / 瓶颈** · 过强参考帧约束运动。
- **核心创新 / 方法** · 用标量调整初始去噪中生成帧到参考帧权重。
- **Baseline** · 原 I2V 模型。
- **Benchmark** · 多种 I2V 主干，运动和参考保真。
- **关键结果 / 消融** · 运动改善而保留画质，幅度未报告。
- **适用条件 / 局限** · 权重位置和适合范围需跨模型校准。

**可复用机制** · 把身份保持和动态幅度作为可调两目标，优先干预早期路径。

<a id="paper-150786"></a>

## Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR

[官方论文页](https://neurips.cc/virtual/2026/poster/150786) · [作者来源](https://openreview.net/forum?id=fPPlV9ktuR)

- **问题 / 瓶颈** · 正向教师蒸馏可能消灭新路径。
- **核心创新 / 方法** · 在正确 rollout 上强化教师意外的学生 token。
- **Baseline** · GRPO 与正向教师蒸馏。
- **Benchmark** · 可验证奖励推理。
- **关键结果 / 消融** · 摘要提出反向信号增强探索，数字待核。
- **适用条件 / 局限** · 需真实正确性判定，教师惊讶可能只反映风格。

**可复用机制** · 只在确认成功后奖励与教师不同的关键策略。

<a id="paper-157021"></a>

## [Re] Boosting the Visual Interpretability of CLIP via Adversarial Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/157021) · [作者来源](https://openreview.net/forum?id=uPXRBZfkYy)

- **问题 / 瓶颈** · 仅对抗微调的显著性不足。
- **核心创新 / 方法** · 用 Energy Pointing Game 损失约束 Simple Gradient。
- **Baseline** · 复现 ICLR 2025 CLIP 对抗微调。
- **Benchmark** · 显著图定位、零样本准确与鲁棒性。
- **关键结果 / 消融** · 定位提高，准确率和鲁棒性略降。
- **适用条件 / 局限** · 需对象目标监督，定位不能验证解释全部忠实度。

**可复用机制** · 将定位与分类权衡转为可调损失并分开报告。

<a id="paper-152270"></a>

## RECAP: Looking Once Is Not Enough for Vision-Language Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152270) · [作者来源](https://openreview.net/forum?id=UKko2Zrtpd)

- **问题 / 瓶颈** · 长轨迹远离视觉证据。
- **核心创新 / 方法** · 对脱梯度回看信号做优势估计、动态折扣与价值门控。
- **Baseline** · GRPO、VPPO、SFT 底座。
- **Benchmark** · 三视觉语言模型，HallusionBench 等。
- **关键结果 / 消融** · HallusionBench 较 SFT 提高 6.1 至 6.5 点。
- **适用条件 / 局限** · 需能测回看轨迹；注意不可作通用因果解释。

**可复用机制** · 用经遮蔽干预验证的证据时点传播终局奖励。

<a id="paper-149027"></a>

## RECIPE: Learning to Rank Complete Precursor Sets for Inorganic Retrosynthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/149027) · [作者来源](https://openreview.net/forum?id=tNsRvxgwYk)

- **问题 / 瓶颈** · 先按个体排序及阈值拼接忽略组合互补。
- **核心创新 / 方法** · 分开候选召回和可变大小集合评分。
- **Baseline** · Retrieval-Retro。
- **Benchmark** · 按年划分的无机逆合成，Combo@1、@20、MRR。
- **关键结果 / 消融** · 重排 Combo@1 提 11.30 点，@20 提 20.82 点。
- **适用条件 / 局限** · 集外试验仅 20 例，迁移需重测。

**可复用机制** · 在工具组或计划集的验收中以完整候选为训练单位。

<a id="paper-149970"></a>

## RECIPE: Procedural Planning via Grounding in Instructional Video

[官方论文页](https://neurips.cc/virtual/2026/poster/149970) · [作者来源](https://openreview.net/forum?id=lpkQB5Oy5S)

- **问题 / 瓶颈** · 直接产标注传播分段噪声且只给单轨迹。
- **核心创新 / 方法** · 以候选步骤与 ASR 的时间落地质量为 GRPO 奖励。
- **Baseline** · 底座、伪标签 SFT，VidAssist 组合。
- **Benchmark** · 七程序基准，六维参考评审及 Visual Planning。
- **关键结果 / 消融** · 宏准确域内加 7 至 8 点，零样本最高加 16 点。
- **适用条件 / 局限** · LLM 裁判与转录噪声仍有偏。

**可复用机制** · 难抽取干净标签时先问能否低成本核验候选。

<a id="paper-149955"></a>

## RecMem: Recurrent Memory Compression for Long-Sequence Recommendation

[官方论文页](https://neurips.cc/virtual/2026/poster/149955) · [作者来源](https://openreview.net/forum?id=lvtUjInAvY)

- **问题 / 瓶颈** · 旧交互全部删除会丢长期信号。
- **核心创新 / 方法** · 以遗忘门递归折叠序列块进固定记忆槽。
- **Baseline** · 同成本压缩截断。
- **Benchmark** · 长序列推荐，Recall@50+。
- **关键结果 / 消融** · 增 4 至 6 个百分点。
- **适用条件 / 局限** · 依赖槽容量和历史相关性。

**可复用机制** · 将保留预算分配给信息而非仅按时间剪截。

<a id="paper-138878"></a>

## Re:Cognize - A Framework For Open-Set Comic Character Re-Identification

[官方论文页](https://neurips.cc/virtual/2026/poster/138878) · [作者来源](https://openreview.net/forum?id=zGCbUayJh6)

- **问题 / 瓶颈** · 模型自标更新造成累积污染。
- **核心创新 / 方法** · 从识别更新比较推门控，只有页面支持时才纳入。
- **Baseline** · 五 Re-ID 主干、MECHA 和真值库。
- **Benchmark** · 三部漫画语料，开放身份跟踪。
- **关键结果 / 消融** · 恢复完美标签收益的约三分之一至三分之二。
- **适用条件 / 局限** · 页面证据是漫画场景，其他在线记忆需替代信号。

**可复用机制** · 记忆写入需要和模型当前预测不共因的确认信号。

<a id="paper-149776"></a>

## ReCoG: Relational Concept Graph for Training-Free Personalization

[官方论文页](https://neurips.cc/virtual/2026/poster/149776) · [作者来源](https://openreview.net/forum?id=nOdl6Bweyu)

- **问题 / 瓶颈** · 独立概念描述显得正确但不能区别近邻。
- **核心创新 / 方法** · 用有向关系图储存成对区分证据，检索后逐对比较。
- **Baseline** · 以独立概念描述增强的个性化。
- **Benchmark** · FINGER 易混淆概念集。
- **关键结果 / 消融** · 最接近的概念收益最大，幅度待核。
- **适用条件 / 局限** · 依赖参考概念和区分证据质量，候选多时配对代价增加。

**可复用机制** · 难例识别把知识库条目从单概念扩到成对区分依据。

<a id="paper-149075"></a>

## Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149075) · [作者来源](https://openreview.net/forum?id=t3zAm1SrXj)

- **问题 / 瓶颈** · 高质量且全程安全的示范或精确定义成本难获得。
- **核心创新 / 方法** · 在 DICE 式离线模仿加入安全支持约束。
- **Baseline** · 需要明确成本或单一专家示范的离线模仿。
- **Benchmark** · 离线安全和回报；具名基准待查。
- **关键结果 / 消融** · 摘要提出在安全覆盖内吸收高回报行为的机制。
- **适用条件 / 局限** · 示范支持不是形式完备的安全定义，覆盖不足影响新状态。

**可复用机制** · 评估应分安全支持识别误差及支持集内的回报改善。

<a id="paper-152472"></a>

## Reconsidering Positional Supervision in Masked Diffusion Language Model Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152472) · [作者来源](https://openreview.net/forum?id=SoXwBAJ8w9)

- **问题 / 瓶颈** · 并行解码的轻微错位也可能被硬位置监督放大。
- **核心创新 / 方法** · 控制解码时的移位量，并把 CTC 适配到监督微调。
- **Baseline** · 逐位置交叉熵及无移位解码。
- **Benchmark** · LLaDA-8B-Instruct、Arena-Hard。
- **关键结果 / 消融** · 仅约 1% 生成词元移一位即显著降胜率。
- **适用条件 / 局限** · CTC 训练收益、语法错误及因果边界待查。

**可复用机制** · 以局部错位压力测试定位失败，不把所有错误归因给 token 内容。

<a id="paper-139014"></a>

## Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139014) · [作者来源](https://openreview.net/forum?id=qHPOtzwRVy)

- **问题 / 瓶颈** · 像素重建高分不一定有利于控制。
- **核心创新 / 方法** · 用六种重建或语义编码器训练同类潜扩散，检查高维及压缩潜空间。
- **Baseline** · 标准 VAE 与预训练语义表示。
- **Benchmark** · BridgeV2；视觉、规划及下游策略和潜表征。
- **关键结果 / 消融** · 摘要报告两种表示均可有效训练，单视觉度量不足。
- **适用条件 / 局限** · 控制成绩依赖规划器和数据覆盖。

**可复用机制** · 用行动区分度、候选排序和实际策略成绩验收世界模型。

<a id="paper-139223"></a>

## RecoverBench: A Systematic Benchmark for Error Recovery in Robotic Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/139223) · [作者来源](https://openreview.net/forum?id=dvg6FAMUK7)

- **问题 / 瓶颈** · 掉落和错位抓取很难从完美示范测试反映。
- **核心创新 / 方法** · 从干净演示生成错误状态，保存模拟状态、环境指纹和随机性。
- **Baseline** · 干净任务及恢复监督前后。
- **Benchmark** · 六项操作、24 错误子型、1,360 场景。
- **关键结果 / 消融** · 摘要提出可用于确定性复现与额外恢复示范收集。
- **适用条件 / 局限** · 仿真错误分布与真实事故范围待查。

**可复用机制** · 为每类错误定义统一起点和恢复成功条件，分开比较预防和补救。

<a id="paper-149244"></a>

## ReCoVer: Resilient LLM Pre-Training System via Fault-Tolerant Collective and Versatile Workload

[官方论文页](https://neurips.cc/virtual/2026/poster/149244) · [作者来源](https://openreview.net/forum?id=rqxWoOlmvG)

- **问题 / 瓶颈** · 缩减迭代批量会偏离无故障的梯度轨迹。
- **核心创新 / 方法** · 故障隔离后保留步内进度，并按可用设备动态分配微批额度。
- **Baseline** · 失败中断恢复及限制并行模式的系统。
- **Benchmark** · 3D 并行和 HSDP 的预训故障。
- **关键结果 / 消融** · 摘要提出逐迭代随机梯度等价性，支持不同并行。
- **适用条件 / 局限** · 故障分布、负载不平衡与随机源管理待查。

**可复用机制** · 把恢复吞吐和训练统计不变性分开验证。

<a id="paper-154541"></a>

## Recursive Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154541) · [作者来源](https://openreview.net/forum?id=ColZtoh6As)

- **问题 / 瓶颈** · 盲目截断或压缩可能丢掉需要跨全文查的证据。
- **核心创新 / 方法** · 保留原输入供程序查询，自调用子问题后合并输出。
- **Baseline** · 上下文压缩、CodeAct 子调用、Claude Code。
- **Benchmark** · 四项长上下文任务，测质量、上下文规模和成本。
- **关键结果 / 消融** · 输入可超原窗口一数量级；作者报告 GPT-5 对压缩有 26% 的中位相对改善。
- **适用条件 / 局限** · 递归深度成本、错误合并与沙箱权限需核验。

**可复用机制** · 用同一成本记录真实读取片段和遗漏证据，而非只提高标称上下文长度。

<a id="paper-152379"></a>

## Recursively Trained Diffusion Models: Limiting Collapse Distribution and Spectral Characterization

[官方论文页](https://neurips.cc/virtual/2026/poster/152379) · [作者来源](https://openreview.net/forum?id=TX42ZoaFHi)

- **问题 / 瓶颈** · 即使分数精确，截断终点也会改变输出分布。
- **核心创新 / 方法** · 分析递归极限，表示成多尺度平滑版本的无穷混合，并用 Hermite 谱追踪。
- **Baseline** · 有限轮误差累积分析。
- **Benchmark** · 理想精确分数和抽样的理论递归。
- **关键结果 / 消融** · 证明几何收敛到唯一极限，细粒度非高斯模式衰减更强。
- **适用条件 / 局限** · 需要所设噪声及早停假设，真实训练中的主导性待查。

**可复用机制** · 按频带和合成代数追踪分布，区分求解近似与训练误差。

<a id="paper-152399"></a>

## Recursive Semantic Divergence for LLM Agent Consistency

[官方论文页](https://neurips.cc/virtual/2026/poster/152399) · [作者来源](https://openreview.net/forum?id=TNqJkEOsuA)

- **问题 / 瓶颈** · 任务完成率掩盖同条件下不同轨迹
- **核心创新 / 方法** · 根据独立 rollouts 学习未来语义分歧代理，并可用作微调奖励
- **Baseline** · 原奖励微调与 SFT
- **Benchmark** · Tau2-Bench 和 ToolSandbox；任务表现及进度变化
- **关键结果 / 消融** · 进度变异分别从 132% 到 91%、90% 到 44%
- **适用条件 / 局限** · 语义相似不代表正确，需保留多种正确策略

**可复用机制** · 当多次执行的结果一致性重要时，加入等初始状态的多次复测

<a id="paper-138942"></a>

## REDACTED-Tunes: An Open 1.4M-Track Dataset and Perceptual Benchmark for AI-Generated Music

[官方论文页](https://neurips.cc/virtual/2026/poster/138942) · [作者来源](https://openreview.net/forum?id=uq5nVvf2sX)

- **问题 / 瓶颈** · 评审可能把高质量误当作真实来源
- **核心创新 / 方法** · 收集感知判断并对照实际来源，分离审美与真假
- **Baseline** · 人工与各 LLM 判别配置
- **Benchmark** · 生成音乐感知评测；平衡准确率、来源及审美评分
- **关键结果 / 消融** · 判断为真的样本审美近高两分，独立于真实来源
- **适用条件 / 局限** · 来自特定音乐生成器和评测条件

**可复用机制** · 评测音视频时不要将真伪和偏好合为一个指标

<a id="paper-150771"></a>

## Reducing Credit Assignment Variance via Counterfactual Reasoning Paths

[官方论文页](https://neurips.cc/virtual/2026/poster/150771) · [作者来源](https://openreview.net/forum?id=fUJHl1y866)

- **问题 / 瓶颈** · 单一奖励均摊到每个步骤会增大估计方差
- **核心创新 / 方法** · 多推理轨迹之间作反事实近似，用差异形成逐步优势
- **Baseline** · 只用终局奖励的推理 RL
- **Benchmark** · 数学和代码推理基准；训练稳定性与表现
- **关键结果 / 消融** · 摘要报告稳定性和最终水平改善，未列幅度
- **适用条件 / 局限** · 轨迹差异并非真实因果替代，需控制生成成本

**可复用机制** · 给同题预算生成若干不同方案，用差异定位有用决策

<a id="paper-155851"></a>

## Re-evaluating Confidence Remasking in Masked Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155851) · [作者来源](https://openreview.net/forum?id=2QJmHBOmiB)

- **问题 / 瓶颈** · 重掩码在较特殊的解码设置可能得到夸大的修复收益
- **核心创新 / 方法** · 复测 WINO 在短块、非贪心设置的表现与多样性
- **Baseline** · 仅按置信去掩码
- **Benchmark** · 掩码扩散 LM 解码；准确和多样性指标
- **关键结果 / 消融** · 常用短块几无收益，增加随机性时能部分纠错却加剧多样性坍塌
- **适用条件 / 局限** · 只复核代表性方法，未覆盖所有重掩码方案

**可复用机制** · 固定实际部署块长并同时验收质量和多样性

<a id="paper-138902"></a>

## Re-evaluating Continual Learning with Few-Shot Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/138902) · [作者来源](https://openreview.net/forum?id=xycCkL63TF)

- **问题 / 瓶颈** · 要求完美旧任务记忆无法反映信息复用与新任务适应
- **核心创新 / 方法** · 短序列元学习前瞻配合旧任务回放，并报告每样本可塑性
- **Baseline** · 标准持续学习评估及独立前瞻或回放
- **Benchmark** · 持续图像分类序列；每样本可塑性
- **关键结果 / 消融** · 混合策略在稳定性与可塑性上更平衡，摘要未列数值
- **适用条件 / 局限** · 证据限图像分类，部署任务的新旧分布不同

**可复用机制** · 给在线模型设置少样本恢复回合，测单位标注带来的收益

<a id="paper-152877"></a>

## Re-examining Low Rank adaptation for private LLM fine-tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/152877) · [作者来源](https://openreview.net/forum?id=Phmae0oHes)

- **问题 / 瓶颈** · 各向同性隐私噪声会抬高弱奇异值
- **核心创新 / 方法** · 部分恢复更新谱的快速衰减，对比单纯限制更新子空间
- **Baseline** · DP-SGD 及 DP-LoRA 相关设置
- **Benchmark** · RoBERTa 的 GLUE 与 Qwen、Llama 的 E2E/DART，最高 4B
- **关键结果 / 消融** · 摘要报告样本效率改善且维持隐私保证
- **适用条件 / 局限** · 需使用保持差分隐私的恢复操作

**可复用机制** · 隐私优化在预算相同时记录谱和达到目标性能的样本量

<a id="paper-148568"></a>

## RefDecoder: Enhancing Visual Generation with Conditional Video Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/148568) · [作者来源](https://openreview.net/forum?id=wtsf0kmI37)

- **问题 / 瓶颈** · 只在去噪器中使用参考会丢失源图细节
- **核心创新 / 方法** · 将参考图特征与去噪后的 latent 在各上采样层共同处理
- **Baseline** · Wan 2.1、VideoVAE+ 等原解码器
- **Benchmark** · 三个重建基准和 VBench I2V；主体、背景一致性和质量
- **关键结果 / 消融** · 各一致性维度改善，摘要未列数值
- **适用条件 / 局限** · 依赖可配套训练的参考解码器，未报告时延变化

**可复用机制** · 换 I2V 组件时单独核对去噪损失与解码细节损失

<a id="paper-148399"></a>

## Reference-Guided Training: Adaptive Gradient Scaling via Per-Sample Loss Comparisons

[官方论文页](https://neurips.cc/virtual/2026/poster/148399) · [作者来源](https://openreview.net/forum?id=y7zQMhy4Gr)

- **问题 / 瓶颈** · 均匀损失易受异质或有噪标签影响
- **核心创新 / 方法** · 与固定参考比较逐样本误差，只限幅缩放梯度而不蒸馏预测
- **Baseline** · 普通经验风险最小化及不同参考配置
- **Benchmark** · 带合成噪声的分类与时间序列预测
- **关键结果 / 消融** · 噪声较大时收益更显著，与参考错误排序低相关时更有效
- **适用条件 / 局限** · 固定参考若同样犯错就难提供独立信息

**可复用机制** · 选择参考器时先测与学习器的误差秩相关

<a id="paper-154077"></a>

## RefineAny3D: Depth Refinement as Semantic Alignment for Monocular 3D Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/154077) · [作者来源](https://openreview.net/forum?id=GMa4R8shWk)

- **问题 / 瓶颈** · 直接输出数字深度难用视觉语言模型原有能力
- **核心创新 / 方法** · 把框投影与图像的相对大小转换为离散修正动作
- **Baseline** · 闭集、开词汇及自动标注检测器原始输出
- **Benchmark** · 新类别、场景和相机验证，基准名未报告
- **关键结果 / 消融** · 单步改正跨检测器均改善，具体幅度未报告
- **适用条件 / 局限** · 投影对深度的指示受框尺寸及相机标定影响

**可复用机制** · VLM 纠错可先问几何方向，再由几何模块计算连续量

<a id="paper-148736"></a>

## Refining Compositional Diffusion for Reliable Long-Horizon Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/148736) · [作者来源](https://openreview.net/forum?id=vQROb0Us1c)

- **问题 / 瓶颈** · 局部多模态分段的平均会形成不可执行的混合轨迹
- **核心创新 / 方法** · 用预训练模型重建误差引导高密度轨迹，并加重叠边界一致性
- **Baseline** · 现有组合扩散规划
- **Benchmark** · OGBench 长程移动、操作及像素观察
- **关键结果 / 消融** · 多种长程任务表现改善，摘要未列数字
- **适用条件 / 局限** · 重建误差仅为密度代理，不能代替外部可执行性

**可复用机制** · 规划器拼接短段时同时验收整段密度和边界连续性

<a id="paper-152356"></a>

## ReflectDrive-2: Reinforcement-Learning-Aligned Self-Editing for Discrete Diffusion Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/152356) · [作者来源](https://openreview.net/forum?id=TgXR6fi9CK)

- **问题 / 瓶颈** · 监督式自编辑在部署阶段的改进有限
- **核心创新 / 方法** · 同一掩码规划模型改写轨迹 token，终局梯度贯穿草拟和编辑
- **Baseline** · 只用监督训练的 AutoEdit
- **Benchmark** · NAVSIM；PDMS、Thor 推理时延
- **关键结果 / 消融** · 自编辑净收益由最高 0.3 增至 1.9 PDMS，平均 31.8ms
- **适用条件 / 局限** · 自动驾驶模拟评测且 oracle 最优不等同单次部署

**可复用机制** · 独立消融编辑器能力与端到端奖励是否真正改变编辑收益
