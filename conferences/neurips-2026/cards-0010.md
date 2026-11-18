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

<a id="paper-153052"></a>

## Reflected Schrödinger Bridge Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/153052) · [作者来源](https://openreview.net/forum?id=OO3amJIfRg)

- **问题 / 瓶颈** · 常规桥不能保证样本留在数据域，反射桥训练贵。
- **核心创新 / 方法** · 用新采样和回归目标做部分免模拟训练。
- **Baseline** · 需整路径和高阶导数的反射 SDE。
- **Benchmark** · 高维图像数据集分布间耦合。
- **关键结果 / 消融** · 训练和推理额外耗时可忽略，生成持平或略升。
- **适用条件 / 局限** · 需域边界和适用的反射过程。

**可复用机制** · 把域约束放进随机动力学而非事后裁剪。

<a id="paper-148600"></a>

## Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148600) · [作者来源](https://openreview.net/forum?id=wXHjf6ebtj)

- **问题 / 瓶颈** · 生成过程中视觉证据衰减。
- **核心创新 / 方法** · 从高熵锚点优化掩码窗口 KL 代理。
- **Baseline** · GRPO 与强基线。
- **Benchmark** · 多个 LVLM，推理和通用基准。
- **关键结果 / 消融** · 摘要报告多主干改善。
- **适用条件 / 局限** · 代理及窗口需要校准。

**可复用机制** · 在视觉影响沿链传播的分岔处加入训练信号。

<a id="paper-154491"></a>

## Reflection with Action-Induced Visual Differences for Desktop GUI Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/154491) · [作者来源](https://openreview.net/forum?id=DCT0OXlKnj)

- **问题 / 瓶颈** · 大型界面变化细小分散。
- **核心创新 / 方法** · 两阶段解耦行动诱发差异与结果核验。
- **Baseline** · 现有反思流程。
- **Benchmark** · OSWorld-Verified、WindowsAgentArena。
- **关键结果 / 消融** · 反思准确率增 7.01%，任务成功增 5.86% 和 5.05%。
- **适用条件 / 局限** · 需稳定的操作前后观测。

**可复用机制** · 先让代理陈述可核验变化，再做行动结果判断。

<a id="paper-154998"></a>

## Reflective Prompted Policy Optimization: Trajectory-Grounded Revision and Salience Bias

[官方论文页](https://neurips.cc/virtual/2026/poster/154998) · [作者来源](https://openreview.net/forum?id=9JvWIy31sK)

- **问题 / 瓶颈** · 纯标量回报不能解释失败。
- **核心创新 / 方法** · 搜索 LLM 提议，评论 LLM 基于状态、动作和奖励修参数，并筛高方差编辑。
- **Baseline** · 无评论或无选择的消融。
- **Benchmark** · 十个环境；含优劣中位三轨迹对照。
- **关键结果 / 消融** · 分工和筛选带来收益，摘要未量化整体。
- **适用条件 / 局限** · 依赖低维策略和代表性轨迹。

**可复用机制** · 全局搜索和诊断修复分离，并用实测筛选修订。

<a id="paper-155820"></a>

## ReflectMT: Internalizing Reflection for Efficient and High-Quality Machine Translation

[官方论文页](https://neurips.cc/virtual/2026/poster/155820) · [作者来源](https://openreview.net/forum?id=2dn1HhrPeN)

- **问题 / 瓶颈** · 展开推理耗 token。
- **核心创新 / 方法** · 两阶段译后反思内化，推理直接翻译。
- **Baseline** · DeepSeek-R1 等多步推理模型。
- **Benchmark** · WMT24、自动与 GPT 评估。
- **关键结果 / 消融** · 相对比较 GPT 质量高 2.16 点，token 少 94.33%。
- **适用条件 / 局限** · 自动评委和单任务限制外推。

**可复用机制** · 对需要实时反馈的生成任务，先训练纠错再验首次输出。

<a id="paper-151635"></a>

## ReFlex: Faithful Panorama Reconstruction from a Single Image with Reflections

[官方论文页](https://neurips.cc/virtual/2026/poster/151635) · [作者来源](https://openreview.net/forum?id=Z78l73Ay0q)

- **问题 / 瓶颈** · 反射观测异质且不完整。
- **核心创新 / 方法** · 从 token 预测估空间可靠性，引导冻结扩散仅细化高不确定部分。
- **Baseline** · 现有全景重建方法。
- **Benchmark** · 单图反射重建保真度。
- **关键结果 / 消融** · 更高保真且不需视场或掩码标注。
- **适用条件 / 局限** · 依赖反射提供有效视野线索。

**可复用机制** · 对可信观测加保护，生成先验主要填补缺失。

<a id="paper-151529"></a>

## REFLEX: Reflective Evolution from LLM Experience

[官方论文页](https://neurips.cc/virtual/2026/poster/151529) · [作者来源](https://openreview.net/forum?id=ZzfhnQtTqh)

- **问题 / 瓶颈** · 统一调用掩盖突变理由且难累积技能。
- **核心创新 / 方法** · 批评者写结构诊断，行动者读取持久代码技能库生成子策略。
- **Baseline** · 单体进化编程。
- **Benchmark** · Lunar Lander、Acrobot、Pendulum、36 维阵列综合。
- **关键结果 / 消融** · 摘要报告样本效率优势。
- **适用条件 / 局限** · 依赖可渲染行为和可重用代码片段。

**可复用机制** · 在跨运行技能库区分诊断证据、修改和可复用代码。

<a id="paper-139603"></a>

## REFORM-3D: A Representation-Centric Evaluation Framework for 3D Medical Vision Foundation Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139603) · [作者来源](https://openreview.net/forum?id=G0jVZhQ2NL)

- **问题 / 瓶颈** · 下游得分混入适配性能。
- **核心创新 / 方法** · 固定解剖测试采集变化，双向 CT-MR 检索，病例隔离评新解剖。
- **Baseline** · 冻结特征与少量适配。
- **Benchmark** · REFORM-3D；稳定性、检索及器官泛化。
- **关键结果 / 消融** · 摘要提出三轴评测，具体数值待核。
- **适用条件 / 局限** · 病例和器官配对设置需符合目标域。

**可复用机制** · 迁移评测应把传感器变化、样本匹配、适配效果拆开。

<a id="paper-148877"></a>

## Reformulate LLM Reinforcement Learning for Stable Training under Black-box Discrepancy

[官方论文页](https://neurips.cc/virtual/2026/poster/148877) · [作者来源](https://openreview.net/forum?id=uVkQ6LV9Jd)

- **问题 / 瓶颈** · 引擎精度和实现偏差可引起 RL 崩溃。
- **核心创新 / 方法** · 把差异写进约束 MDP，用几何惩罚跟踪政策偏离。
- **Baseline** · 掩码与常规训练缓解。
- **Benchmark** · 多模型训练稳定与容差观察。
- **关键结果 / 消融** · 观察到容差区域；摘要未核实幅度。
- **适用条件 / 局限** · 需两端可观察的可比轨迹。

**可复用机制** · 将上线策略和更新策略的实际差异纳入优化。

<a id="paper-153767"></a>

## Reformulating KV Cache Eviction Problem for Long-Context LLM Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/153767) · [作者来源](https://openreview.net/forum?id=IomgdYliGM)

- **问题 / 瓶颈** · 局部注意权重忽略 value 和跨头效应。
- **核心创新 / 方法** · 估计注意与投影 value 的乘积、处理头间依赖并全模型选择。
- **Baseline** · 既有逐头驱逐。
- **Benchmark** · LongBench 和 Needle-In-A-Haystack，19 数据集。
- **关键结果 / 消融** · 摘要称仅 5% KV 时仍维持表现。
- **适用条件 / 局限** · 特定上下文与被测试配置，开销需实测。

**可复用机制** · 跨层预算需使用统一的输出影响度量。

<a id="paper-149558"></a>

## Reformulating Neural Operators in $d+1$ Dimensions for Embedding Evolution

[官方论文页](https://neurips.cc/virtual/2026/poster/149558) · [作者来源](https://openreview.net/forum?id=pD3kqLbub6)

- **问题 / 瓶颈** · 单纯扩嵌入代价大。
- **核心创新 / 方法** · 把 d 维物理算子扩成 d+1 维，包括嵌入维。
- **Baseline** · 已有神经算子。
- **Benchmark** · 十余 PDE，涵盖热方程和 3D Rayleigh–Taylor，relative L2。
- **关键结果 / 消融** · 比较中误差最低。
- **适用条件 / 局限** · 高维算子成本和非 PDE 迁移需测试。

**可复用机制** · 显式建模特征轴之间的演化，比只增加特征数量更可诊断。

<a id="paper-152804"></a>

## ReFPO: Reflow Regularization for Flow Matching Policy Gradients

[官方论文页](https://neurips.cc/virtual/2026/poster/152804) · [作者来源](https://openreview.net/forum?id=QGCmtNLIKF)

- **问题 / 瓶颈** · 流代理比率尖峰、离散化敏感。
- **核心创新 / 方法** · 把优势加权更新配合显式 Reflow 路径矫直。
- **Baseline** · FPO 及多步推理。
- **Benchmark** · GridWorld、MuJoCo Playground、Humanoid。
- **关键结果 / 消融** · 稳训练并增强单步表现。
- **适用条件 / 局限** · 实证为模拟控制。

**可复用机制** · 针对部署步数直接约束训练中流路径曲率。

<a id="paper-153878"></a>

## ReFree-S2V: Towards Realistic Co-Speech Video Generation via Reward-Free RL and Multilevel Speech Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/153878) · [作者来源](https://openreview.net/forum?id=I5DRYeUl99)

- **问题 / 瓶颈** · 口型准确与自然头动难兼备。
- **核心创新 / 方法** · 局部和全局语音表示配合不依赖预设奖励的流匹配训练。
- **Baseline** · 现有语音视频模型。
- **Benchmark** · 口型及头动表现。
- **关键结果 / 消融** · 摘要称改善，具体效果待核。
- **适用条件 / 局限** · 未给核心奖励替代细节及适用模型范围。

**可复用机制** · 按时间尺度拆语音条件，另测表情动态与同步。

<a id="paper-150490"></a>

## REGATE: Confidence-Calibrated Integration of Temporally-Aligned Exogenous Texts for Dynamic Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/150490) · [作者来源](https://openreview.net/forum?id=hi0wCR0EYw)

- **问题 / 瓶颈** · 直接注入会产生时间泄漏与误配。
- **核心创新 / 方法** · 提实体时间对齐的置信 token，经有界残差门融合。
- **Baseline** · 裸文本及现成文本嵌入。
- **Benchmark** · 动态文档与时序图任务。
- **关键结果 / 消融** · 方向一致下有稳定保证。
- **适用条件 / 局限** · 依赖真实发布时间、实体链接及校准。

**可复用机制** · 流式代理只给当时可获得且可信证据有限更新权。

<a id="paper-151868"></a>

## ReGDiff: Guided Diffusion in Regulated Latent Space for Exploring Metamaterial Voxel Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/151868) · [作者来源](https://openreview.net/forum?id=XHx4RRDPKz)

- **问题 / 瓶颈** · 追求新颖易生成无效几何。
- **核心创新 / 方法** · 训练潜空间做推斥与回落，推理加入短程排斥。
- **Baseline** · 体素生成基线。
- **Benchmark** · 桁架与壳体，可行性、新颖性、多样性。
- **关键结果 / 消融** · 摘要报告三项提高 8.9%、46.4%、128.6%。
- **适用条件 / 局限** · 依赖潜空间距离及领域可行性判据。

**可复用机制** · 围绕已知样本局部排斥，同时保留回到有效流形的机制。

<a id="paper-152784"></a>

## ReGen: Agentic Video World Modeling with Synergized Reasoning and Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/152784) · [作者来源](https://openreview.net/forum?id=QMvrZxy8W9)

- **问题 / 瓶颈** · 统一像素生成器长序列漂移。
- **核心创新 / 方法** · 动作状态规格连接流式规划与扩散，验收失败可重生成。
- **Baseline** · 现有视频世界模型。
- **Benchmark** · 逾两百万动作对齐片段，长程连贯性。
- **关键结果 / 消融** · 摘要报告叙事一致性提高。
- **适用条件 / 局限** · 依赖规格和评审有效，数据规模贡献需分辨。

**可复用机制** · 将状态转移与像素实现分开并闭环验收。

<a id="paper-148181"></a>

## ReGenHuman: Re-Generating Human Appearances for Realistic Full-Body Video Anonymization

[官方论文页](https://neurips.cc/virtual/2026/poster/148181) · [作者来源](https://openreview.net/forum?id=zgk8N9WGSM)

- **问题 / 瓶颈** · 直接遮盖或编辑损害画质或残留外观。
- **核心创新 / 方法** · 从保留的结构再生成一致外观。
- **Baseline** · 视频遮盖和编辑。
- **Benchmark** · 隐私、画质、实用性与视频问答。
- **关键结果 / 消融** · 摘要报告更优权衡及下游可用性。
- **适用条件 / 局限** · 需严格测其他身份线索，如步态。

**可复用机制** · 任务保留与身份隐私分别验证，不能以换脸代替匿名性。

<a id="paper-155954"></a>

## RegimeVGGT: Layer-Wise Spatially Preserving Redundancy Removal for Visual Geometry Grounded Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/155954) · [作者来源](https://openreview.net/forum?id=1a4VUxz0sm)

- **问题 / 瓶颈** · 统一削减忽略对齐及位姿的异质需求。
- **核心创新 / 方法** · 浅中深层分工，合并保显著几何，K/V 网格保位姿路径。
- **Baseline** · VGGT*。
- **Benchmark** · 等重建质量的速度测量。
- **关键结果 / 消融** · 免训练达 6.7 倍加速。
- **适用条件 / 局限** · 依赖 VGGT 的层功能分析。

**可复用机制** · 先做任务级因果消融，保护局部关键计算而非统一删层。

<a id="paper-153478"></a>

## Region-Normalized DPO for Medical Image Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/153478) · [作者来源](https://openreview.net/forum?id=L4rTdhTV8w)

- **问题 / 瓶颈** · 大量一致像素掩盖偏好差异。
- **核心创新 / 方法** · 在分歧区域归一化候选 mask 似然比。
- **Baseline** · 原始和鲁棒 DPO。
- **Benchmark** · 两医学分割任务、两主干、多个评委含 oracle。
- **关键结果 / 消融** · 增益在无噪偏好仍存在。
- **适用条件 / 局限** · 依赖可确定空间分歧；需验证不同大小区域。

**可复用机制** · 在局部编辑偏好中不要让共同部分稀释梯度。

<a id="paper-149369"></a>

## Register Anything Model for Generalizable and Robust Point Cloud Registration

[官方论文页](https://neurips.cc/virtual/2026/poster/149369) · [作者来源](https://openreview.net/forum?id=qZ0AeP1jSv)

- **问题 / 瓶颈** · 点密度、尺度与噪声跨域变化使单域配准器失效。
- **核心创新 / 方法** · 联合执行几何自适应体素化与归一化，接入粗到细的局部几何 Transformer。
- **Baseline** · 分别在各域训练的配准模型。
- **Benchmark** · 室内、室外和物体等 12 个配准基准，指标为内点率和配准召回率。
- **关键结果 / 消融** · 摘要报告两项指标达到当前最佳水平，并优于单域训练对照。
- **适用条件 / 局限** · 摘要未报告逐数据集数值和运行开销。

**可复用机制** · 多源点云先在标准分辨率上保留各自的局部物理结构，再用局部几何匹配减轻体素化噪声。

<a id="paper-152096"></a>

## Regret-Based $(\epsilon,\delta)$-optimal Stopping Criteria for Bayesian Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/152096) · [作者来源](https://openreview.net/forum?id=VY7fcL71Yf)

- **问题 / 瓶颈** · 固定评估预算可能消耗过多，也无法认证当前结果。
- **核心创新 / 方法** · 推导 GP-UCB 的更紧单轮遗憾界，达到容差即停止。
- **Baseline** · 固定预算 GP-UCB 及已有经验停止方案。
- **Benchmark** · 高斯过程贝叶斯优化与数值实验，摘要未列函数。
- **关键结果 / 消融** · 停止时以至少 1−δ 的概率获得 ε 最优解。
- **适用条件 / 局限** · 保证依赖 GP-UCB 和文中理论设定，适用范围与节省量未报告。

**可复用机制** · 给搜索过程附上可计算的质量证书，让下一次采样取决于现有解离目标还可能差多远。

<a id="paper-156767"></a>

## Regret minimization in Linear Bandits with offline data via extended D-optimal exploration.

[官方论文页](https://neurips.cc/virtual/2026/poster/156767) · [作者来源](https://openreview.net/forum?id=4WcK8gKgCi)

- **问题 / 瓶颈** · 离线样本总量掩盖动作特征中覆盖不足的方向。
- **核心创新 / 方法** · 离线在线分阶段淘汰，在每相位用扩展 D 最优设计选点。
- **Baseline** · 纯在线线性赌博机及已有离线数据利用方法。
- **Benchmark** · 随机线性赌博机，比较在线遗憾界及极小极大下界。
- **关键结果 / 消融** · 领先项随离线覆盖不足的有效维数而变，离线覆盖很差时退回纯在线遗憾率。
- **适用条件 / 局限** · 结果针对随机线性模型，实证未报告。

**可复用机制** · 复用历史日志时先看 Gram 矩阵的谱，用在线预算补足弱覆盖方向。

<a id="paper-155805"></a>

## Regret-Optimal Wasserstein-Robust Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/155805) · [作者来源](https://openreview.net/forum?id=2kzyCdrkUn)

- **问题 / 瓶颈** · 最小化 Wasserstein 球内最坏风险可能给出次优的超额风险。
- **核心创新 / 方法** · 推导条件数控制的小半径极限，并给出条件数降低估计过程。
- **Baseline** · 标准 Wasserstein DRO 及其他回归估计器。
- **Benchmark** · 多元线性回归和岭回归的理论及数值比较，指标为超额风险。
- **关键结果 / 消融** · 小半径下多种方法可达实例最优速率，固定半径且不满足低秩条件时 DRO 可能有维度相关损失。
- **适用条件 / 局限** · 结论依赖 2-Wasserstein 邻域及回归设定。

**可复用机制** · 扰动不够小时，再优化最坏风险前要确认代理目标是否同样控制相对该分布最优决策的损失。

<a id="paper-155015"></a>

## ReGuidance: Diffusion Steering with Strong Latent Initializations Solves Hard Inverse Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/155015) · [作者来源](https://openreview.net/forum?id=9Cq7vYEYym)

- **问题 / 瓶颈** · 强压缩或高噪观测下，直接奖励引导可能离开数据流形。
- **核心创新 / 方法** · 从候选解反向积分无条件概率流 ODE，得到确定性引导的初始化。
- **Baseline** · 多个逆问题方法提供初解，直接梯度引导为方法背景。
- **Benchmark** · 大区域修补、大倍率超分和线性或非线性高噪去模糊。
- **关键结果 / 消融** · 作者报告初解经处理后兼具更强真实感和观测一致性，并给出部分设定下的理论证明。
- **适用条件 / 局限** · 依赖预训练扩散先验及候选解，摘要未给推理成本。

**可复用机制** · 已有优化器能给一致但失真的初解时，可以先将它放回生成器的坐标系，再改善一致性与真实性。

<a id="paper-150245"></a>

## Regularization Paths for Continuous DAG Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150245) · [作者来源](https://openreview.net/forum?id=jeeqnxmgbl)

- **问题 / 瓶颈** · 连续 DAG 学习对稀疏系数敏感，网格搜索昂贵且难追踪边稳定性。
- **核心创新 / 方法** · 在支持集不变时推导矩阵动力系统，通过事件切换跨过路径分支。
- **Baseline** · NOTEARS、GOLEM、DAGMA 的网格搜索方案。
- **Benchmark** · 合成和真实结构学习任务，考察计算与结构稳定性。
- **关键结果 / 消融** · 摘要报告相对网格更省计算且结构更稳定。
- **适用条件 / 局限** · 跟踪非凸优化的驻点，摘要未报告全局最优保证。

**可复用机制** · 扫正则权重时沿同一解支连续追踪，并记录哪些边在支持集变化时出现或消失。

<a id="paper-154808"></a>

## Reinforce Adjoint Matching: Scaling RL Post-Training of Diffusion and Flow Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154808) · [作者来源](https://openreview.net/forum?id=AoBtAENiPy)

- **问题 / 瓶颈** · 逐步反传奖励或依赖特殊采样器会增加后训练开销。
- **核心创新 / 方法** · 用 KL 正则控制推导只倾斜干净端点分布，保留条件加噪律，再用 REINFORCE 奖励加权伴随匹配回归。
- **Baseline** · Flow-GRPO。
- **Benchmark** · Stable Diffusion 3.5M，GenEval、文字渲染、人类偏好与可组合性。
- **关键结果 / 消融** · 到达 Flow-GRPO 峰值 GenEval 准确率所需训练步数约为其 1/50。
- **适用条件 / 局限** · 步数对比未包含总计算，其他模型外推未报告。

**可复用机制** · 端点奖励固定时，将同一干净样本重新加噪成不同训练状态，以监督整条生成过程。

<a id="paper-151586"></a>

## Reinforced Evidence-Aware Long Video Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/151586) · [作者来源](https://openreview.net/forum?id=ZUmUvF2Vx9)

- **问题 / 瓶颈** · 关键视频证据稀疏，固定抽帧与普通检索都可能导致幻觉。
- **核心创新 / 方法** · 每步判断已观察内容是否足够，继续搜索或引用证据作答，以跨模态验证器打分。
- **Baseline** · Qwen2.5-VL-7B 基座及固定帧等长视频方案。
- **Benchmark** · Video-MME、MLVU、LongVideoBench、EgoSchema、VideoHallucer 与 ELV-Halluc。
- **关键结果 / 消融** · 作者报告 96 帧版本超过 768 帧基座的准确率和抗幻觉表现。
- **适用条件 / 局限** · 依赖视觉证据验证器，未报告验证器错误带来的影响。

**可复用机制** · 预算受限的视频智能体可学习在证据不足时继续观察，以引用证据能否被独立验证作为奖励。

<a id="paper-154908"></a>

## Reinforced Fast Weights via Next-Sequence Prediction

[官方论文页](https://neurips.cc/virtual/2026/poster/154908) · [作者来源](https://openreview.net/forum?id=A1sw6FviPQ)

- **问题 / 瓶颈** · 固定大小递归记忆要服务未来预测，单步训练不给持续可读性直接反馈。
- **核心创新 / 方法** · 按预测熵选择训练位置，生成多 token 序列，对整段打分后用 GRPO 更新。
- **Baseline** · 下一 token 预测监督微调。
- **Benchmark** · LaCT-760M、DeltaNet-1.3B，长文检索、长文问答与 LongBench。
- **关键结果 / 消融** · 作者报告一致超越下一 token 微调对照。
- **适用条件 / 局限** · 两个快权重模型，未报告等算力优势和必要消融。

**可复用机制** · 压缩记忆若需要长期保存有效信息，可从同一记忆状态预测整个后续片段，以序列成效提供信用。

<a id="paper-149385"></a>

## Reinforcement Learning for Code Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/149385) · [作者来源](https://openreview.net/forum?id=qRPKxKFqhP)

- **问题 / 瓶颈** · 直接把运行时间加入奖励会受到噪声、稀疏性与训练不稳定影响。
- **核心创新 / 方法** · 使用大型性能测试和校准沙箱，组合正确性与速度反馈，通过离线模拟选择配置并调整 GRPO。
- **Baseline** · 标准 RLVR。
- **Benchmark** · DMC-Optim 与 LCB，严格速度前十分位 pass@1 与正确样本速度胜率。
- **关键结果 / 消融** · 严格 pass@1 在 Qwen 2.5 7B 上由 18.1% 升至 27.7%，在 CWM 32B 上由 28.7% 升至 42.4%。
- **适用条件 / 局限** · 依赖可验证测试及稳定测量环境，独立模块收益未报告。

**可复用机制** · 将能否完成任务和完成得够不够快作为分层反馈，先校准测量再调奖励配方。

<a id="paper-154650"></a>

## Reinforcement Learning for Diffusion LLMs with Entropy-Guided Step Selection and Stepwise Advantages

[官方论文页](https://neurips.cc/virtual/2026/poster/154650) · [作者来源](https://openreview.net/forum?id=C2Jvfl4xzR)

- **问题 / 瓶颈** · 扩散语言模型序列似然难以计算，替代似然容易带来偏差。
- **核心创新 / 方法** · 将去噪过程建模为有限时域 MDP，用熵相关界选训练步骤并用一次去噪完成估计优势。
- **Baseline** · 已有扩散语言模型 RL 后训练。
- **Benchmark** · 编程、逻辑和数学推理，具体数据集与分数未报告。
- **关键结果 / 消融** · 作者报告在几乎所有评测上超过已有方法。
- **适用条件 / 局限** · 实际实现近似理论梯度，摘要未报告近似误差或长序列开销。

**可复用机制** · 对并行生成模型可围绕逐步去噪分配信用，用少量信息量高的阶段替代序列级似然。

<a id="paper-149595"></a>

## Reinforcement Learning for Long-Horizon Unordered Tasks: From Boolean to Coupled Reward Machines

[官方论文页](https://neurips.cc/virtual/2026/poster/149595) · [作者来源](https://openreview.net/forum?id=ovNLRgukle)

- **问题 / 瓶颈** · 布尔奖励机需要维护指数多个子任务完成组合。
- **核心创新 / 方法** · 用数字和议程奖励机表达剩余目标，为各目标附加耦合状态并做分解 Q 学习。
- **Baseline** · 现有奖励机学习基线。
- **Benchmark** · 四个离散及连续状态和动作空间领域，比较长程任务扩展性。
- **关键结果 / 消融** · 作者报告随无序子任务增多时扩展性更强，并证明分解算法保留全局最优保证。
- **适用条件 / 局限** · 依赖可表达的子任务结构，摘要未报告规模极限。

**可复用机制** · 当目标可任意顺序完成时，可把剩余目标定义为可更新的议程，并让价值函数保留目标间依赖。

<a id="paper-155273"></a>

## Reinforcement Learning from Rich Feedback with Distributional DAgger

[官方论文页](https://neurips.cc/virtual/2026/poster/155273) · [作者来源](https://openreview.net/forum?id=6ux7PyTXx9)

- **问题 / 瓶颈** · 逆 KL 与 JS 自蒸馏更新不保证策略单调改善
- **核心创新 / 方法** · 用分布式 DAgger 的正向交叉熵匹配教师，引出教师加权 RL 下界
- **Baseline** · RLVR 及自蒸馏
- **Benchmark** · 科学与数学推理、代码；Pass@N 等
- **关键结果 / 消融** · 摘要报告一致改善，未列幅度
- **适用条件 / 局限** · 单调保证受理论设定及教师收益条件约束

**可复用机制** · 有分布教师时做同 rollout 的散度消融

<a id="paper-152104"></a>

## Reinforcement World Model Learning for LLM-based Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152104) · [作者来源](https://openreview.net/forum?id=VUh75nf7CQ)

- **问题 / 瓶颈** · 词元预测会惩罚等价文本，判断器又可能被钻空子
- **核心创新 / 方法** · 在预训练嵌入空间评估下一状态语义匹配
- **Baseline** · 基础模型、任务成功 RL、专家数据训练和 LLM 判断器
- **Benchmark** · ALFWorld 与作者称 Bench 的另一测试；任务表现
- **关键结果 / 消融** · 加任务奖励时分别胜直接任务 RL 6.9 和 5.7 点
- **适用条件 / 局限** · 嵌入相近不保证环境状态等价

**可复用机制** · 为工具结果定义语义状态奖励同时验证关键字段

<a id="paper-152003"></a>

## Reinforcing Multimodal Reasoning Against Visual Degradation

[官方论文页](https://neurips.cc/virtual/2026/poster/152003) · [作者来源](https://openreview.net/forum?id=WECg95ixWE)

- **问题 / 瓶颈** · 无条件不变性会强化错误，重采污染输入成本大
- **核心创新 / 方法** · 复用干净轨迹，对最坏增强加词元 KL，并保留干净优势策略梯度
- **Baseline** · GRPO
- **Benchmark** · Qwen3-VL 4B/8B，七个基准，已见和未见视觉退化
- **关键结果 / 消融** · 两类鲁棒性加 2.4% 和 2.3%，干净准确率相当
- **适用条件 / 局限** · 在语义被真实遮蔽时不宜要求不变

**可复用机制** · 一致性正则应先以信息可恢复和标签正确作门控

<a id="paper-153917"></a>

## Reinforcing VLAs in Task-Agnostic World Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153917) · [作者来源](https://openreview.net/forum?id=HhIHL25t1u)

- **问题 / 瓶颈** · 新任务数据贵，模拟幻觉可误导奖励
- **核心创新 / 方法** · 用任务无关行为学习转移，以通用 VLM 给目标奖励，并用双噪声验证筛选
- **Baseline** · 摘要未列具体方法
- **Benchmark** · 模拟及真实执行；任务表现
- **关键结果 / 消融** · 摘要报告一致增益，未给数值
- **适用条件 / 局限** · 过滤和奖励都依赖世界模型的覆盖

**可复用机制** · 进入真实机器人前，对照想象过滤策略和实机成功率

<a id="paper-148959"></a>

## Reject, Resample, Repeat: Understanding Parallel Reasoning in Language Model Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/148959) · [作者来源](https://openreview.net/forum?id=tsudCyj5ju)

- **问题 / 瓶颈** · 序贯重采样可能放大近视评分偏差
- **核心创新 / 方法** · 分析 SMC 非渐近收敛并刻画 PRM 近似时的上限
- **Baseline** · 标准 SMC 和近视多粒子方法
- **Benchmark** · 采样误差与终局准确率
- **关键结果 / 消融** · 理论条件预测采样误差，但不一定预测最终准确
- **适用条件 / 局限** · 更强保证依赖近完美 PRM

**可复用机制** · 把采样器是否逼近预期分布与该分布是否提高解题分开

<a id="paper-148750"></a>

## Relational Feature Distillation for Lightweight 3D Point Cloud Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/148750) · [作者来源](https://openreview.net/forum?id=vK7LWQHktB)

- **问题 / 瓶颈** · 直接迁移绝对特征对轻量学生负担大
- **核心创新 / 方法** · 逐阶段进行关系蒸馏，推理移除投影头
- **Baseline** · 无 SRFD 的 TrimPT、LitePT-S
- **Benchmark** · ScanNet、ScanNet200、nuScenes；mIoU 和 mAP50
- **关键结果 / 消融** · ScanNet 76.6% mIoU、推理 5.84M 参数
- **适用条件 / 局限** · 依赖教师几何表征质量，摘要未列所有消融

**可复用机制** · 端侧 3D 模型先比较阶段关系和直接特征回归

<a id="paper-150993"></a>

## Relaxation-Aligned State Control for Test-Time Scaling in Generative Combinatorial Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150993) · [作者来源](https://openreview.net/forum?id=dkHKGHN1xC)

- **问题 / 瓶颈** · 同一个连续松弛信号不一定适合所有阶段
- **核心创新 / 方法** · 按问题使用对齐的状态引导细化，末端保留原 logits，等预算分枝
- **Baseline** · 既有测试时扩散求解策略
- **Benchmark** · TSP、ATSP、MIS、MVC；等运行时间质量
- **关键结果 / 消融** · 前两类质量时间取舍强，后两类有竞争力
- **适用条件 / 局限** · 状态和解码约束需按问题设计

**可复用机制** · 别为细化方便而覆写贪心解码所依赖的评分排序

<a id="paper-150064"></a>

## Relaxed On-Policy Distillation: Selective Credit Allocation for Scaling Reasoning Efficiently

[官方论文页](https://neurips.cc/virtual/2026/poster/150064) · [作者来源](https://openreview.net/forum?id=l0h1SzRI7H)

- **问题 / 瓶颈** · 近零信用冗余，罕见大负项可能压制可行思路
- **核心创新 / 方法** · 调节反馈施加位置、强度与训练阶段
- **Baseline** · 采样 token 在线蒸馏和近期后训练方法
- **Benchmark** · 多类推理，含跨词表和自蒸馏
- **关键结果 / 消融** · 摘要报告最高 12 倍样本效率
- **适用条件 / 局限** · 需识别何种负信号为有效纠错，摘要未给适用阈值

**可复用机制** · 在线蒸馏先画信用分布并对照尾部裁剪

<a id="paper-149528"></a>

## Relevance Is Not Necessity: Selecting the Necessary API Set for Tool-Using LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/149528) · [作者来源](https://openreview.net/forum?id=pTmL4oUWre)

- **问题 / 瓶颈** · 每个工具相关不等于集合最小足够
- **核心创新 / 方法** · 冻结上游轨迹后，以整集合确切匹配监督候选集选择器
- **Baseline** · 逐 API 边际排序
- **Benchmark** · 防泄漏 ToolBench G2/G3；验证器一致的集合恢复
- **关键结果 / 消融** · 不增加轨迹后 LLM 生成而改善集合恢复
- **适用条件 / 局限** · 依赖固定候选池和必要性验证器

**可复用机制** · 挑工具集合时同时测漏掉必需项和带入冗余项

<a id="paper-154871"></a>

## RelFlexformer: Efficient Attention Transformers for Integrable Relative Positional Encodings

[官方论文页](https://neurips.cc/virtual/2026/poster/154871) · [作者来源](https://openreview.net/forum?id=AHbhLrT1U0)

- **问题 / 瓶颈** · 规则网格加速不能直接处理任意散布坐标。
- **核心创新 / 方法** · 非均匀 FFT 实现可积相对位置核的注意力。
- **Baseline** · 结构化高效 RPE。
- **Benchmark** · 多套 3D 数据集。
- **关键结果 / 消融** · 注意力复杂度 O(L log L)，摘要报告质量改善。
- **适用条件 / 局限** · 要求调制可积，近似和实际速度需评测。

**可复用机制** · 把空间坐标和索引网格分开，使注意力重用空间频域结构。

<a id="paper-155343"></a>

## RelGS: Relation-Aware Gaussian Splatting for Open-Vocabulary 3D Scene Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/155343) · [作者来源](https://openreview.net/forum?id=6Jo2q08Opd)

- **问题 / 瓶颈** · 仅实例嵌入无法组合或多跳查询。
- **核心创新 / 方法** · 几何提出关系候选，语言模型验证语义，形成带权图。
- **Baseline** · 开放词汇 3D 场景方法。
- **Benchmark** · 词选择、指称分割、多跳及点分割。
- **关键结果 / 消融** · 摘要报告多任务强表现。
- **适用条件 / 局限** · 语言判定不能替代几何观测。

**可复用机制** · 将边的物理证据和语义验收分离，查询时可按置信分配预算。

<a id="paper-154996"></a>

## Reliability-Budgeted Edge–Cloud Adaptation for Continual Multimodal Dehazing on UAV

[官方论文页](https://neurips.cc/virtual/2026/poster/154996) · [作者来源](https://openreview.net/forum?id=9K2Ya77HTs)

- **问题 / 瓶颈** · 不停域漂移容易让弱监督退化。
- **核心创新 / 方法** · 共享冻结与更新头，用再加雾一致和红外边缘批评。
- **Baseline** · 常见在线去雾适配。
- **Benchmark** · 五个航拍数据集、多雾变化。
- **关键结果 / 消融** · 摘要报告持续改善。
- **适用条件 / 局限** · 需合理的成像退化模型和跨传感器配准。

**可复用机制** · 持续适配用固定参照和传感物理验收连接。

<a id="paper-156117"></a>

## Reliability-Coupled Manifold-Aware Diffusion for Missing-Modality Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/156117) · [作者来源](https://openreview.net/forum?id=0GkSxMZdx4)

- **问题 / 瓶颈** · 串接补全和分类会无视生成误差。
- **核心创新 / 方法** · 流形感知扩散补全和证据型推理联合传递可靠性。
- **Baseline** · 串行补全再推理。
- **Benchmark** · 缺失、噪声及随时间变化的可靠性条件。
- **关键结果 / 消融** · 摘要报告更稳定且能提供随时变化的可靠性估计。
- **适用条件 / 局限** · 生成置信度还需独立校准。

**可复用机制** · 不要把合成输入当真观测；保留其时间和模态级不确定性。

<a id="paper-151312"></a>

## Reliable Abstention under Adversarial Injections: Lower Bounds and New Upper Bounds

[官方论文页](https://neurips.cc/virtual/2026/poster/151312) · [作者来源](https://openreview.net/forum?id=bQuKG6tVNk)

- **问题 / 瓶颈** · 缺底层分布时可靠覆盖困难。
- **核心创新 / 方法** · 用少量能耐受污染的见证样本驱动势函数。
- **Baseline** · 分布 oracle 和分布无关界。
- **Benchmark** · 在线预测与弃权合计误差。
- **关键结果 / 消融** · 推导依结构复杂度改善的上界。
- **适用条件 / 局限** · 依赖推断维度等假设。

**可复用机制** · 用经过可靠性检查的证据集做拒答门，而非单置信分数。

<a id="paper-154913"></a>

## Reliable Chain-of-Thought via Prefix Consistency

[官方论文页](https://neurips.cc/virtual/2026/poster/154913) · [作者来源](https://openreview.net/forum?id=9zfyYpgXhy)

- **问题 / 瓶颈** · 多数回答易累积一致错误。
- **核心创新 / 方法** · 切断推理轨迹并重采样，用原答案复现率加权。
- **Baseline** · 标准多数投票。
- **Benchmark** · 五推理模型，四数学科学基准。
- **关键结果 / 消融** · 达到投票平台准确率的 token 最高省 21 倍，中位 4.6 倍。
- **适用条件 / 局限** · 一致不保证正确，取决于切点和样本数。

**可复用机制** · 测试推理扰动后候选能否自我复现，再决定票权。

<a id="paper-153600"></a>

## Reliable Clustering and Quantization via Distortion-Constrained Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/153600) · [作者来源](https://openreview.net/forum?id=KBzmOm0ugU)

- **问题 / 瓶颈** · 总失真小仍可牺牲个别代表。
- **核心创新 / 方法** · 最优传输分配约束每簇平均距离。
- **Baseline** · 原聚类和量化分配。
- **Benchmark** · 不同架构和训练设置，重建质量。
- **关键结果 / 消融** · 替换分配后质量一致改善。
- **适用条件 / 局限** · 需先设可行的簇失真阈值。

**可复用机制** · 用局部质量约束防止平均指标隐藏高误差子群。

<a id="paper-153948"></a>

## Reliable Federated Multi-View Learning via Conflict-Aware Evidence Calibration

[官方论文页](https://neurips.cc/virtual/2026/poster/153948) · [作者来源](https://openreview.net/forum?id=HMFQMoCE5C)

- **问题 / 瓶颈** · 单靠置信度可能放大不一致视角。
- **核心创新 / 方法** · 根据视角冲突自适应校准和融合。
- **Baseline** · 已有联邦多视角方案。
- **Benchmark** · 异构视角下准确性和可靠性。
- **关键结果 / 消融** · 摘要报告两项改善。
- **适用条件 / 局限** · 需证据冲突量可比较。

**可复用机制** · 跨客户端或模态不要默认高置信来源相容。

<a id="paper-153462"></a>

## ReLoop: Structured Modeling and Behavioral Verification for Reliable LLM-Based Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153462) · [作者来源](https://openreview.net/forum?id=L82BI6w4zr)

- **问题 / 瓶颈** · 代码可运行但公式可能不符语义。
- **核心创新 / 方法** · 将理解、建模、编程、检查分开，再用求解器行为核验。
- **Baseline** · 聊天底座及窄域 SFT。
- **Benchmark** · RetailOpt-190、MAMO-ComplexLP 等三基准。
- **关键结果 / 消融** · 组合题结构生成增 8.5 点，局部题行为核验增 4.4 点。
- **适用条件 / 局限** · 需有可预测的干预响应。

**可复用机制** · 在无真值时用变形关系测试工具产物的语义。

<a id="paper-153954"></a>

## Remembering What Matters: From Markovian to Subtask-Causal Memory in VLA Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/153954) · [作者来源](https://openreview.net/forum?id=HIcqPaIuYq)

- **问题 / 瓶颈** · 最近帧及相似帧会保留错误历史。
- **核心创新 / 方法** · 前置 DAG 约束候选，关键帧经图感知注意力注入冻结 VLA。
- **Baseline** · 共享 VLA 主干的窗口、压缩与检索。
- **Benchmark** · LIBERO、RMBench、SimplerEnv-Bridge、SafeLab 和 Franka。
- **关键结果 / 消融** · 长时及记忆依赖子集提升，消融支持两层互补。
- **适用条件 / 局限** · 依赖任务分段与依赖推断，低信心需回退。

**可复用机制** · 将记忆的任务相关性和感知证据质量分别筛选。

<a id="paper-150643"></a>

## Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/150643) · [作者来源](https://openreview.net/forum?id=gYBIdco0A1)

- **问题 / 瓶颈** · 保存不同描述可能浪费容量。
- **核心创新 / 方法** · 只有数据证实共享状态导致决策冲突才细化划分。
- **Baseline** · 以描述为中心的压缩。
- **Benchmark** · 在线记忆的率失真与遗憾分析。
- **关键结果 / 消融** · 证明近极小极大遗憾。
- **适用条件 / 局限** · 需要可辨认的决策冲突，初期探索有成本。

**可复用机制** · 以合并状态的动作代价来定压缩粒度。

<a id="paper-152348"></a>

## Remember with Confidence: Uncertainty Quantification for Spatio-temporal Memory with Probabilistic Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/152348) · [作者来源](https://openreview.net/forum?id=TjgsCOJn16)

- **问题 / 瓶颈** · 生成单描述会隐藏跨视角语义不确定。
- **核心创新 / 方法** · 按对象统计描述散度，对不确定对象选择高质视角再融合。
- **Baseline** · 固定预算和既有时空记忆。
- **Benchmark** · 具身 4D 记忆的对象可靠性与查询。
- **关键结果 / 消融** · 高质视角更可能降低不确定，摘要称记忆更可靠。
- **适用条件 / 局限** · 依赖视角可得性与描述模型。

**可复用机制** · 以跨观测的一致性给主动感知设优先级。

<a id="paper-154827"></a>

## Remember Your Trace: Memory-Guided Long-Horizon Agentic Framework for Consistent and Hierarchical Repository-Level Code Documentation

[官方论文页](https://neurips.cc/virtual/2026/poster/154827) · [作者来源](https://openreview.net/forum?id=Ae5q87uyOE)

- **问题 / 瓶颈** · 组件隔离写作会重复检索和产生冲突。
- **核心创新 / 方法** · 依赖及粒度顺序驱动遍历，RepoMemory 支持读写验证。
- **Baseline** · 开源和闭源文档基线。
- **Benchmark** · 仓库级说明，多指标。
- **关键结果 / 消融** · 摘要称表现最佳，未给幅度。
- **适用条件 / 局限** · 依赖构建可靠依赖及版本一致。

**可复用机制** · 长任务按信息依赖顺序运行，让共享证据参与后续产物验证。

<a id="paper-154842"></a>

## Render Structure Uncertainty for HTML Repair in  MLLM-based UI-to-Code Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154842) · [作者来源](https://openreview.net/forum?id=AW3Yb9jstt)

- **问题 / 瓶颈** · 视觉差分对多个子树和修复均可能成立。
- **核心创新 / 方法** · 匹配目标结构图及浏览器锚定结构图，生成局部补丁并全页渲染。
- **Baseline** · 基础 HTML 生成器。
- **Benchmark** · UI-to-code，布局一致性及结构错误。
- **关键结果 / 消融** · 摘要称局部结构错误下降。
- **适用条件 / 局限** · 需要浏览器和视觉结构提取，非可视功能仍需另验。

**可复用机制** · 对渲染结果的局部错因先保多假设，再以运行产物筛选。

<a id="paper-148500"></a>

## Rennala-NSGD: Asynchronous Stochastic Optimization Beyond Euclidean Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/148500) · [作者来源](https://openreview.net/forum?id=xMWhDplFaU)

- **问题 / 瓶颈** · 欧式等价转换引入无谓维度惩罚。
- **核心创新 / 方法** · 以非欧范数直接分析噪声并半异步更新。
- **Baseline** · 欧式中转的分析。
- **Benchmark** · 分布式优化 wall-clock 复杂度理论。
- **关键结果 / 消融** · 建立非欧异步时间保证。
- **适用条件 / 局限** · 依赖目标几何、随机噪声及工作器假设。

**可复用机制** · 选择非欧优化时同步重定义噪声预算。

<a id="paper-151651"></a>

## Renoise Consistency: Unlocking Efficient Self-Correction for Diffusion Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151651) · [作者来源](https://openreview.net/forum?id=Z2nVkaW60X)

- **问题 / 瓶颈** · 类自回归解码错误累积，抽样校正昂贵。
- **核心创新 / 方法** · 解码后按训练一致性重新加噪，再用自适应块草拟减前向。
- **Baseline** · 半自回归解码。
- **Benchmark** · 任务表现及前向步。
- **关键结果 / 消融** · 最高表现改善 9.00%，前向步数减 25.85%。
- **适用条件 / 局限** · 依赖训练噪声机制与内部表示。

**可复用机制** · 为纠错刻意回到训练中见过的状态。

<a id="paper-151643"></a>

## ReorgGS: Equivalent Distribution Reorganization for 3D Gaussian Splatting

[官方论文页](https://neurips.cc/virtual/2026/poster/151643) · [作者来源](https://openreview.net/forum?id=Z4xgDCwiYE)

- **问题 / 瓶颈** · 透明合成阻断背景梯度，重叠参数梯度共线。
- **核心创新 / 方法** · 从已收敛分布重采中心、估局部协方差并从低透明重新优化。
- **Baseline** · 仅重置透明度。
- **Benchmark** · 3DGS 的梯度可达性、重叠与后续优化。
- **关键结果 / 消融** · 摘要称可达性改善，数值待核。
- **适用条件 / 局限** · 需保持场景支持并控制重组引入的误差。

**可复用机制** · 保持表示的功能分布，同时改变参数化以解除优化病态。

<a id="paper-153066"></a>

## Rep2Text: Decoding Full Text from a Single LLM Token Representation

[官方论文页](https://neurips.cc/virtual/2026/poster/153066) · [作者来源](https://openreview.net/forum?id=OET7WYchkH)

- **问题 / 瓶颈** · 看精确复现会低估压缩表征信息。
- **核心创新 / 方法** · 训练文本解码器从最后 token 表征恢复序列。
- **Baseline** · 多来源和解码模型组合。
- **Benchmark** · 16 token 短序列及更长文本，含临床域外。
- **关键结果 / 消融** · 短序列约一半 token 恢复，长度增加后语义保留高于逐词。
- **适用条件 / 局限** · 训练可读不等同模型自然使用，隐私需按表示泄露单测。

**可复用机制** · 检测可共享嵌入时把逐词保密和语义保密拆开。

<a id="paper-154626"></a>

## RePercENT: Scaling Disentangled Representation Learning Beyond Two Modalities

[官方论文页](https://neurips.cc/virtual/2026/poster/154626) · [作者来源](https://openreview.net/forum?id=CBBmaDH8U5)

- **问题 / 瓶颈** · 二模态分解难扩，统一对齐丢独有因素。
- **核心创新 / 方法** · 对预提取嵌入优化成对解缠，联合求解共享及特有成分。
- **Baseline** · 双模态解耦和全对齐。
- **Benchmark** · 多模态和多任务，成分恢复。
- **关键结果 / 消融** · 摘要报告恢复改善并提供优化保证。
- **适用条件 / 局限** · 依赖分解可识别性及预提取嵌入是否保留信息。

**可复用机制** · 冻结主干后先审计共享、成对与专有成分再决定融合。

<a id="paper-153090"></a>

## RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space

[官方论文页](https://neurips.cc/virtual/2026/poster/153090) · [作者来源](https://openreview.net/forum?id=O3nA8awPs4)

- **问题 / 瓶颈** · 文生图中的语言模型通常只编码文本，去噪主干从零训练。
- **核心创新 / 方法** · 把带噪视觉表征投影到多模态语言模型，使用其输出给扩散 Transformer 提供条件。
- **Baseline** · 参数量匹配、用新初始化参数扩容的去噪 Transformer。
- **Benchmark** · 受控文生图对照，摘要未列数据集与指标。
- **关键结果 / 消融** · 在等参数对照中优于仅扩大去噪主干。
- **适用条件 / 局限** · 依赖与预训练模型相容的语义视觉表征，摘要未给算力对照。

**可复用机制** · 预训练视觉语言编码器也可以处理带噪语义表征，为去噪提供先验。

<a id="paper-148828"></a>

## Replay-buffer engineering for noise-robust quantum circuit optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/148828) · [作者来源](https://openreview.net/forum?id=uqQwtucEDc)

- **问题 / 瓶颈** · 固定 TD 误差优先级容易重复抽取不可靠的价值目标。
- **核心创新 / 方法** · ReaPER+ 随价值估计成熟逐步退火至可靠性采样。
- **Baseline** · 固定 PER、ReaPER、均匀回放和既有在线策略方法。
- **Benchmark** · 量子电路优化和 LunarLander-v3，考察样本效率、能量误差及 AUC。
- **关键结果 / 消融** · 量子设定样本效率至多提高 4 倍，LunarLander-v3 在摘要所述对照中 AUC 提高 9%。
- **适用条件 / 局限** · 摘要未给其他控制领域的复验及退火参数敏感性。

**可复用机制** · 价值估计初期侧重高误差经验，估计稳定后逐渐提升目标可信度在采样权重中的比重。

<a id="paper-154325"></a>

## Replicas-as-Variables: A Planner for Throughput-Optimal Routing in LLM Deployment

[官方论文页](https://neurips.cc/virtual/2026/poster/154325) · [作者来源](https://openreview.net/forum?id=EUSU1DpVqc)

- **问题 / 瓶颈** · 静态流水线对设备异构和组件负载差异的适应不足。
- **核心创新 / 方法** · 把稠密阶段和 MoE 专家副本数设为决策变量，同多路径流量一起优化，使用 MILP 求吞吐上界。
- **Baseline** · 静态并行与多种部署方案，摘要未列名称。
- **Benchmark** · 15 种部署设置，考察稳态吞吐并在真实异构机群验证。
- **关键结果 / 消融** · 14/15 设置吞吐最高，混合 GPU 下最高 3.1 倍。
- **适用条件 / 局限** · 通用问题为 NP 难，摘要未报告延时及调度成本。

**可复用机制** · 有异构设备和不均匀组件流量时，让组件副本数适配最繁忙路径，而非沿所有阶段复制同样份数。

<a id="paper-139568"></a>

## RepoMirage: Probing Repository Context Reasoning in Code Agents with Perturbations

[官方论文页](https://neurips.cc/virtual/2026/poster/139568) · [作者来源](https://openreview.net/forum?id=I2uNqwM1hm)

- **问题 / 瓶颈** · 端到端修复成功无法诊断跨文件上下文推理。
- **核心创新 / 方法** · 改变代理可见的仓库结构，再把暴露的结构难点编成显式任务，并检查探索轨迹。
- **Baseline** · 原始 SWE-Bench Verified 场景与结构优先原型 RepoAnchor。
- **Benchmark** · RepoMirage-Perturb 和 RepoMirage-Extend，评估成功率与探索轨迹。
- **关键结果 / 消融** · 作者报告在扩展对照中均分由 66.8% 降至 25.3%，更广探索并未有效转成结构信息。
- **适用条件 / 局限** · 结论来自仓库任务，摘要未验证其他信息环境。

**可复用机制** · 构造保持正确答案不变的证据布局变化，检验代理是否能定位并组织跨文档关系。

<a id="paper-138929"></a>

## Reporting Practice Matters: The Impact of Reference Choice on Chest X-ray Report Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/138929) · [作者来源](https://openreview.net/forum?id=vocvkC0AxO)

- **问题 / 瓶颈** · 参考报告体例和临床含义耦合，可能污染指标。
- **核心创新 / 方法** · 按医生参与建立的分类改写参考，同时保留临床解读。
- **Baseline** · 原参考报告，使用 GREEN 对比生成模型。
- **Benchmark** · MIMIC-CXR 上九个模型，另有 120 对经验证的参考报告。
- **关键结果 / 消融** · 压缩正常发现的参考描述后，Libra 从第一到第三，CheXOne 从第三到第一。
- **适用条件 / 局限** · 结果来自胸部影像报告，其他领域需自行验证含义守恒。

**可复用机制** · 固定事实、改写参考的格式和细节粒度，用排名稳定性检查生成质量指标。

<a id="paper-153104"></a>

## RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153104) · [作者来源](https://openreview.net/forum?id=Nux3SaJlm7)

- **问题 / 瓶颈** · 仅模仿成功轨迹缺少偏离后纠正的监督。
- **核心创新 / 方法** · 切出恢复片段重置历史，用对齐指令和成功参考的语义价值给失败前缀按可靠性衰减标注，训练价值条件策略。
- **Baseline** · 仅用成功轨迹的模仿是背景，具体比较方法未报告。
- **Benchmark** · FRBench 标准错误注入，仿真与真机双臂任务，指标含对抗条件成功率。
- **关键结果 / 消融** · 对抗成功率平均从 20% 到 75%，扩大真机测试最高 80%。
- **适用条件 / 局限** · 依赖规划器或人工的恢复轨迹及成功参考，摘要没给采集成本。

**可复用机制** · 把偏离状态本身重用为训练入口，保留其前段的有效进展，并在恢复策略输入中去掉无关失败历史。

<a id="paper-139682"></a>

## RepoZero: Can LLMs Generate a Code Repository from Scratch?

[官方论文页](https://neurips.cc/virtual/2026/poster/139682) · [作者来源](https://openreview.net/forum?id=AmuEj2d0Qm)

- **问题 / 瓶颈** · 仅测补丁或依赖主观评分无法规模化验证从零构建。
- **核心创新 / 方法** · 给 API 规格，要求跨语言重新实现，用原项目行为提供自动黑盒验证。
- **Baseline** · 补丁式基准和人工或模型质量评审是背景，另比较现有代理。
- **Benchmark** · RepoZero 项目级生成，以执行通过率衡量。
- **关键结果 / 消融** · 作者报告最强模型的通过率约 30% 至 55%。
- **适用条件 / 局限** · 只能覆盖可自动检查的约定行为，摘要未报告测试覆盖率。

**可复用机制** · 可执行规格不完整时，把成熟实现用作行为参照，并用跨语言要求减少照搬。

<a id="paper-152733"></a>

## Representation Forcing for Bottleneck-Free Unified Multimodal Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152733) · [作者来源](https://openreview.net/forum?id=QlWRlAlLYa)

- **问题 / 瓶颈** · 去掉外部 VAE 后，直接从像素同时学高级结构和低级细节会掉质。
- **核心创新 / 方法** · 解码器自回归预测视觉表征 token，保留在同一模型上下文中引导像素扩散。
- **Baseline** · VAE 统一模型和同类 VAE 版本。
- **Benchmark** · 图像生成和视觉理解，摘要未报告数据集或指标。
- **关键结果 / 消融** · 生成达到 VAE 对照水平，理解通常超出其 VAE 版本。
- **适用条件 / 局限** · 生成成本和外部表征监督需求未报告。

**可复用机制** · 视觉语义表征可作为同一模型生成的中间结果，使像素生成过程继承感知结构。

<a id="paper-154990"></a>

## Representation Fréchet Loss for Visual Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/154990) · [作者来源](https://openreview.net/forum?id=9OK87o8Wkf)

- **问题 / 瓶颈** · 小批次估算 Fréchet 距离难以直接用作训练目标。
- **核心创新 / 方法** · 用大样本估计表征分布的 Fréchet 距离，只在当前较小批次计算梯度。
- **Baseline** · 基础生成器和多步生成器，摘要未列教师蒸馏量化对照。
- **Benchmark** · ImageNet 256×256，Inception FID 及不同表征距离。
- **关键结果 / 消融** · 一步生成器 FID 0.72，且多步模型可转为一步模型，作者另报告 Inception FID 可误判质量。
- **适用条件 / 局限** · 结论依赖表征空间，摘要未报告缓存成本和多样性指标。

**可复用机制** · 分布级目标需要大量样本才稳定时，只让其中一小批承担反向传播。

<a id="paper-151906"></a>

## Representation Learning Enables Scalable Multitask Deep Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151906) · [作者来源](https://openreview.net/forum?id=WzURRKJgUx)

- **问题 / 瓶颈** · 世界模型方案将学习表征与在线规划捆绑，难辨扩展收益。
- **核心创新 / 方法** · MR.Q 将辅助预测目标接到可扩展 actor-critic，不在推理时规划。
- **Baseline** · 近期世界模型方法与多种深度强化学习基线。
- **Benchmark** · 多任务连续控制，比较表现、计算开销与墙钟时间。
- **关键结果 / 消融** · 摘要报告对照中更强且更快，消融指出预测表征对表现关键。
- **适用条件 / 局限** · 未报告规划可能不可替代的任务及逐任务分数。

**可复用机制** · 将预测模型用于改进策略的状态编码，即使最终控制器不依赖模型滚动。

<a id="paper-151596"></a>

## Representation Preconditioning for Efficient Diffusion Model Training

[官方论文页](https://neurips.cc/virtual/2026/poster/151596) · [作者来源](https://openreview.net/forum?id=ZNtVdfSWVX)

- **问题 / 瓶颈** · 从零学表示增加扩散训练负担，从头联合对齐也需要主干全程计算。
- **核心创新 / 方法** · ERW 先对早层进行表征预热，之后训练全模型并衰减对齐信号。
- **Baseline** · 从头联合对齐的扩散训练。
- **Benchmark** · SiT，ImageNet 256×256 和 512×512、MS-COCO，指标 FID。
- **关键结果 / 消融** · 计入预热仍提高收敛效率，SiT-XL/2 在 256 分辨率 350 epoch 达 FID 1.41，512 为 2.04。
- **适用条件 / 局限** · 依赖预训练视觉表征，摘要未给不同早层选择成本。

**可复用机制** · 可把昂贵联合训练中的辅助目标前置，以便主目标从已有结构初始化。

<a id="paper-151431"></a>

## Representation Rigidity in Face Embeddings: Orthogonal Identifiability and Backfill-Free Compatibility

[官方论文页](https://neurips.cc/virtual/2026/poster/151431) · [作者来源](https://openreview.net/forum?id=alci29b9Vd)

- **问题 / 瓶颈** · 模型升级后，新查询嵌入和旧向量库通常不兼容。
- **核心创新 / 方法** · 用少量配对向量作闭式 Procrustes 校准，把新查询映到旧空间。
- **Baseline** · 同模型检索为参考，对照同家族与跨架构及残差校正。
- **Benchmark** · 45 个人脸嵌入模型及 160 万图像 IFRT，考察 Rank-1。
- **关键结果 / 消融** · 同家族升级恢复至少 99.8% 的同模型 Rank-1。
- **适用条件 / 局限** · 强结论限于同类角度间隔人脸模型，跨架构需要进一步校正。

**可复用机制** · 索引迁移前先测配对点的正交刚性，有足够一致性时可只转换查询。

<a id="paper-157016"></a>

## Reproducibility study of "Bilinear MLPs enable weight-based mechanistic interpretability"

[官方论文页](https://neurips.cc/virtual/2026/poster/157016) · [作者来源](https://openreview.net/forum?id=Bnx3hf3mWp)

- **问题 / 瓶颈** · 双线性 MLP 的低秩特征可读性可能依赖数据复杂度。
- **核心创新 / 方法** · 复现原特征分解和截断，比较不同初始化、规模及新增 RGB 数据集。
- **Baseline** · Pearce 等原工作，无对抗训练版本亦作观察。
- **Benchmark** · MNIST、CIFAR-10 与 CIFAR-100，考察分类性能及特征向量解释性。
- **关键结果 / 消融** · 原分类结果与低秩现象可复现，MNIST 的对抗训练提升可读性，但两个 CIFAR 设置的特征向量难解释。
- **适用条件 / 局限** · 摘要未给统一量化可读性评分，结论不外推到其他架构。

**可复用机制** · 将权重截断仍保准确与权重特征能被解释分开验证，简单数据上的成功无法替代自然输入对照。

<a id="paper-157022"></a>

## Reproducibility study of FACTER: Fairness-Aware Conformal Thresholding and Prompt Engineering

[官方论文页](https://neurips.cc/virtual/2026/poster/157022) · [作者来源](https://openreview.net/forum?id=vX5mPaLdeQ)

- **问题 / 瓶颈** · 低有效率与性能地板可能掩盖校准造成的效用下降。
- **核心创新 / 方法** · 复用公开协议，同时记录公平性、目录映射后的排序性能及生成有效率。
- **Baseline** · Zero-Shot 与 FACTER 原报告。
- **Benchmark** · MovieLens-1M 和 Amazon Movies & TV，SNSR、CFR、NDCG@10、Recall@10、Valid@10。
- **关键结果 / 消融** · 复现公平违规减少，但初始与校准后效用均接近地板，无法验证效用保持。
- **适用条件 / 局限** · 作者列出生成词表、项目映射和协议差异作为可能成因，摘要未分离贡献。

**可复用机制** · 同时监测输出有效率与未干预效用，再把公平指标变化解释为可用系统上的改进。

<a id="paper-157633"></a>

## Reproducing FACTER: Fairness via Conformal Thresholding and Prompt Repair

[官方论文页](https://neurips.cc/virtual/2026/poster/157633) · [作者来源](https://neurips.cc/virtual/2026/poster/157633)

- **问题 / 瓶颈** · 方法会在与自身联动的自适应阈值下看似改善
- **核心创新 / 方法** · 同时重算固定阈值和总体公平，并加静态无样本公平提示
- **Baseline** · FACTER 在线迭代和静态 Fair Zero-Shot
- **Benchmark** · 受控排序的语义公平与阈值违规
- **关键结果 / 消融** · 动态阈值违规改善未稳定反映到固定阈值；静态提示语义结果相当
- **适用条件 / 局限** · 来自特定排序任务

**可复用机制** · 对调节器和测量器联合变化的结果补固定评估口径

<a id="paper-150681"></a>

## Requential Coding: Measuring Model Compressibility by Coding Data Instead of Parameters

[官方论文页](https://neurips.cc/virtual/2026/poster/150681) · [作者来源](https://openreview.net/forum?id=gIGw6hwmJz)

- **问题 / 瓶颈** · 参数量不能反映训练数据解释所需信息
- **核心创新 / 方法** · 用数据编码构造复杂度，并代入 PAC-Bayes 界
- **Baseline** · 4 比特 GPTQ 的理想无损基线
- **Benchmark** · CIFAR-5M、OpenWebText、FineWeb；码长、过拟合和泛化界
- **关键结果 / 消融** · 固定目标损失下码长随规模下降，并给非空界
- **适用条件 / 局限** · 依赖编码构造和模型损失目标

**可复用机制** · 数据受限训练中考虑比较目标性能下的编码复杂度

<a id="paper-150281"></a>

## RESBev: Making BEV Perception More Robust

[官方论文页](https://neurips.cc/virtual/2026/poster/150281) · [作者来源](https://openreview.net/forum?id=jKHbeYCp8K)

- **问题 / 瓶颈** · 单帧观测退化会破坏地图表征
- **核心创新 / 方法** · 用历史 BEV 时空相关预测干净语义特征，再修复当前表示
- **Baseline** · 原感知骨干与其他恢复方法，摘要未列名单
- **Benchmark** · nuScenes；干扰鲁棒、速度、参数和显存
- **关键结果 / 消融** · 自然干扰下性能改善，摘要未列幅度
- **适用条件 / 局限** · 短历史一致性假设可能在快速场景变化时失效

**可复用机制** · 先在地图语义层比较时序插补与原始图像修复

<a id="paper-153283"></a>

## Rescaled Asynchronous SGD: Optimal Distributed Optimization under Data and System Heterogeneity

[官方论文页](https://neurips.cc/virtual/2026/poster/153283) · [作者来源](https://openreview.net/forum?id=MPqNHW1Si4)

- **问题 / 瓶颈** · 更快工作器更新多，数据异质时目标偏置
- **核心创新 / 方法** · 使每个工作器在一个周期的累计学习率相同
- **Baseline** · 常用异步 SGD 和近期方法
- **Benchmark** · 固定计算模型理论和实测；收敛与耗时
- **关键结果 / 消融** · 主复杂度对齐下界，摘要称实验回到正确全局目标
- **适用条件 / 局限** · 依赖光滑性、有限异质和计算模型假设

**可复用机制** · 异构工作节点上不要让更新次数隐式决定训练数据权重

<a id="paper-139237"></a>

## RescueBench: Can Embodied Agents Save Lives in the Wild?

[官方论文页](https://neurips.cc/virtual/2026/poster/139237) · [作者来源](https://openreview.net/forum?id=d1QPUUrYxZ)

- **问题 / 瓶颈** · 仅看救援终局难区分较早认知瓶颈
- **核心创新 / 方法** · 按线索不确定性和空间层级分级，并检查各阶段
- **Baseline** · 七个方法、oracle 与人类
- **Benchmark** · RescueBench 五困难级，完成率和阶段诊断
- **关键结果 / 消融** · 最高难度无方法完成；探索首要，空间记忆为第二项独立瓶颈
- **适用条件 / 局限** · 证据来自设定工作流，未直接代表真实救援

**可复用机制** · 先做阶段断点再决定优化探索还是地图表示

<a id="paper-138928"></a>

## Reset Dependence Is Embodied: Training Protocol Changes Which Morphologies Appear Optimal

[官方论文页](https://neurips.cc/virtual/2026/poster/138928) · [作者来源](https://openreview.net/forum?id=w3aoxSAAcH)

- **问题 / 瓶颈** · 单一训练重置规则与机械形态交互改变排名
- **核心创新 / 方法** · 用多协议最小回报选择，并核对不同优化器上的排序
- **Baseline** · 单协议 oracle、不同重置及预设 SAC 核验
- **Benchmark** · 训练协议形态族交互；top-k 回报和置信下界
- **关键结果 / 消融** · 最小值筛选保留各单协议 oracle top-k 平均回报至少 91%
- **适用条件 / 局限** · 协议及形态族有限，真实机重置成本未验证

**可复用机制** · 在机体和控制联合优化中报告规则敏感性，并做跨协议重排

<a id="paper-153548"></a>

## Residual Calibration via Local Feature-Space Refinement

[官方论文页](https://neurips.cc/virtual/2026/poster/153548) · [作者来源](https://openreview.net/forum?id=KYfZmJEdo6)

- **问题 / 瓶颈** · 全局映射掩盖特征空间的误差差异
- **核心创新 / 方法** · 以全局输出作锚，从校准样本的非参数局部证据估修正
- **Baseline** · 原全局校准器及多种校准方法
- **Benchmark** · 不同设置及多视图输入，具体数据未报告
- **关键结果 / 消融** · 摘要报告多个校准器改善
- **适用条件 / 局限** · 局部估计依赖邻域覆盖和可靠特征，避免同一校准集上的乐观验收

**可复用机制** · 对长尾输入区域单独测校准误差再决定是否加局部修正

<a id="paper-152370"></a>

## Residual Expertise Is Not Decision Value

[官方论文页](https://neurips.cc/virtual/2026/poster/152370) · [作者来源](https://openreview.net/forum?id=TZTKPXkDDu)

- **问题 / 瓶颈** · 人类补充证据未必改变最优动作
- **核心创新 / 方法** · 分析新证据是否跨越奖励矩阵定义的决策边界，并量化边界遗憾
- **Baseline** · 按残余预测专长选择复核
- **Benchmark** · 理论分析及高代价不对称决策设置；边界遗憾
- **关键结果 / 消融** · 同一专家信号的价值随奖励矩阵改变
- **适用条件 / 局限** · 依赖实际成本模型和可估计的决策边界

**可复用机制** · 助手何时应移交人工，要以行动是否改变和错误成本为准

<a id="paper-148940"></a>

## Resilience Matters for Embodied Agents System: New Metrics, Systematic Evaluation, and Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/148940) · [作者来源](https://openreview.net/forum?id=u2TS1Rxun2)

- **问题 / 瓶颈** · 两条都成功的轨迹可能需要截然不同的恢复代价
- **核心创新 / 方法** · 用扰动稳定性、恢复及优雅退化分项诊断并指导调整
- **Baseline** · 原具身系统和多种压力设定
- **Benchmark** · 具身任务及语义扰动；恢复成本、稳定性、压力下完成
- **关键结果 / 消融** · 分项调整使恢复成本低 42.94%，稳定性高 19.87%，完成指标高 10.08%
- **适用条件 / 局限** · 摘要未列详细优化配置，多项韧性有取舍

**可复用机制** · 部署时按任务风险分别验收恢复效率与完成率

<a id="paper-148752"></a>

## Resilient Latent Readouts for Long-Context Question Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/148752) · [作者来源](https://openreview.net/forum?id=vHe2MR0CGu)

- **问题 / 瓶颈** · 局部文本可能丢掉前文语义影响
- **核心创新 / 方法** · 用模型内部注意力定位候选，按覆盖补证据，再打包位置一致的潜态
- **Baseline** · 全文、紧凑记忆以及相同位置文本对照
- **Benchmark** · LoCoMo、Loong，三个开源骨干；问答指标
- **关键结果 / 消融** · LoCoMo 九项中八项胜全文；全失定位场景最高领先文本对照 13.3 F1 点
- **适用条件 / 局限** · 潜态需兼容模型、位置编码和生成输入

**可复用机制** · 压缩记忆时控制检索位置，独立比较表征保留信息

<a id="paper-155194"></a>

## Resilient Semi-Supervised Inference with Heterogeneous Unlabeled Data

[官方论文页](https://neurips.cc/virtual/2026/poster/155194) · [作者来源](https://openreview.net/forum?id=7ZyMQkmbDz)

- **问题 / 瓶颈** · 预测辅助估计依赖两组同分布。
- **核心创新 / 方法** · 在预测纠偏中嵌入稳健校准，并自适应选择校准器。
- **Baseline** · 预测驱动推断等常规方案。
- **Benchmark** · 异质或污染的无标注数据，统计效率及稳健性。
- **关键结果 / 消融** · 给出一致性，实验有改善，幅度未报告。
- **适用条件 / 局限** · 校准和验证数据必须反映目标群。

**可复用机制** · 利用无标注集时先约束纠偏误差再追求样本效率。

<a id="paper-156789"></a>

## RESIST: Resilient Decentralized Learning Using Consensus Gradient Descent

[官方论文页](https://neurips.cc/virtual/2026/poster/156789) · [作者来源](https://openreview.net/forum?id=aNu8S9O6Ug)

- **问题 / 瓶颈** · 受损链路会扰乱一致更新。
- **核心创新 / 方法** · 将筛选和一致梯度迭代结合，检查共识步数。
- **Baseline** · 其他筛选与更新方案。
- **Benchmark** · 不同损失和扰动条件，通信成本和收敛。
- **关键结果 / 消融** · 消融显示固定通信预算增 J 可改善收敛并减少本地更新。
- **适用条件 / 局限** · 依赖网络和筛选假设。

**可复用机制** · 以达到鲁棒收敛的总预算选择本地更新与通信比例。

<a id="paper-152894"></a>

## ResKV: Residual-based Channel-wise Unstructured Pruning for KV Cache Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/152894) · [作者来源](https://openreview.net/forum?id=PcOi9GxwJj)

- **问题 / 瓶颈** · 直接通道剪枝忽略向量重复。
- **核心创新 / 方法** · 余弦聚类，残差剪枝及逐 token 量化，回读加中心。
- **Baseline** · 稠密 FlashAttention。
- **Benchmark** · 长上下文内存和吞吐及任务表现。
- **关键结果 / 消融** · 峰值内存减 45.6%，吞吐 4.27 倍。
- **适用条件 / 局限** · 重构及聚类开销依实现与输入。

**可复用机制** · 用共享代表吸收公共成分，再稀疏编码差异。

<a id="paper-149564"></a>

## ReSMap: Recasting Satellite Priors for Robust and Accurate Online HD Map Construction

[官方论文页](https://neurips.cc/virtual/2026/poster/149564) · [作者来源](https://openreview.net/forum?id=pBNwXqI5Q2)

- **问题 / 瓶颈** · 车载相机异常时在线地图失去观察。
- **核心创新 / 方法** · 显式冗余感知卫星和相机融合。
- **Baseline** · 常规在线建图。
- **Benchmark** · 正常及相机故障的 HD 地图构建。
- **关键结果 / 消融** · 摘要称故障设置表现领先。
- **适用条件 / 局限** · 依赖地理配准和卫星时效。

**可复用机制** · 融合评估加单通道失效切片，区别先验和可实际接管的冗余。

<a id="paper-155192"></a>

## Resolving Representation Ambiguity in Feedforward Novel View Synthesis Transformer via Semantic-Spatial Decoupling

[官方论文页](https://neurips.cc/virtual/2026/poster/155192) · [作者来源](https://openreview.net/forum?id=7aQyn669sE)

- **问题 / 瓶颈** · 单表示混合重建与语义目标。
- **核心创新 / 方法** · 分支 token，可选专门监督和双向调制。
- **Baseline** · 未解耦的前馈新视角合成。
- **Benchmark** · 仅解码器和编解码器结构。
- **关键结果 / 消融** · 一致改善，基础设计几乎无额外推理时延。
- **适用条件 / 局限** · 监督和调制是可选项，收益需单独测。

**可复用机制** · 把几何重建和语义任务的中间变量显式解耦。

<a id="paper-149622"></a>

## Resolving Time-Frequency Ridge Crossings via Frequency-Rate Lifting

[官方论文页](https://neurips.cc/virtual/2026/poster/149622) · [作者来源](https://openreview.net/forum?id=ojSIdIqCYx)

- **问题 / 瓶颈** · 二维时频同点无法区分实例。
- **核心创新 / 方法** · 三维提升并将变化率反馈到掩码查询。
- **Baseline** · 其他时频分解方法。
- **Benchmark** · 合成多啁啾及蝙蝠、电网、振动信号。
- **关键结果 / 消融** · 模拟交叉率从 78.6% 降至 0.9%。
- **适用条件 / 局限** · 两分量变化率也重合时可能仍混叠。

**可复用机制** · 状态量重合可用可靠导数分开单独轨迹。

<a id="paper-154217"></a>

## Resource-Aware Parameter-Efficient Model Adaptation for Onboard High-Dimensional Data

[官方论文页](https://neurips.cc/virtual/2026/poster/154217) · [作者来源](https://openreview.net/forum?id=FKPFY7IOQ2)

- **问题 / 瓶颈** · 小更新包难捕捉复杂域改动。
- **核心创新 / 方法** · 主低秩加非线性辅助分支，按矩阵梯度差异调训练。
- **Baseline** · LoRA 和全量微调。
- **Benchmark** · 四高光谱集三主干。
- **关键结果 / 消融** · 优于 LoRA，部分达到或超过全量。
- **适用条件 / 局限** · 实验为高光谱，需测端侧实际开销。

**可复用机制** · 预算受限时把线性共有方向与非线性偏差分开编码。

<a id="paper-150008"></a>

## Response Time Enhances Alignment with Heterogeneous Preferences

[官方论文页](https://neurips.cc/virtual/2026/poster/150008) · [作者来源](https://openreview.net/forum?id=lSacVQkH6p)

- **问题 / 瓶颈** · 每用户仅一次二选一可能无法识别群体均值。
- **核心创新 / 方法** · 用漂移扩散模型联合解释响应和时延。
- **Baseline** · 仅选择数据。
- **Benchmark** · 异质偏好的估计一致性分析。
- **关键结果 / 消融** · 即使匿名且每人一次，估计渐近收敛。
- **适用条件 / 局限** · 响应时间须适用行为假设，设备延迟等需测。

**可复用机制** · 对异质标注不要把时延当垃圾字段，可用作偏好强度代理。

<a id="paper-152832"></a>

## ReST-RL: Reinforcing LLM Reasoning through Unified Self-Training and Value-Guided Search

[官方论文页](https://neurips.cc/virtual/2026/poster/152832) · [作者来源](https://openreview.net/forum?id=Q5KwR2WUBr)

- **问题 / 瓶颈** · 单纯策略训练不能充分用过程信息。
- **核心创新 / 方法** · 用自采 MCTS 训练价值，再嵌进价值引导搜索。
- **Baseline** · 单策略训练和解码对照。
- **Benchmark** · 域外数学科学推理及端到端效率。
- **关键结果 / 消融** · 摘要报告准确性和成本权衡改善。
- **适用条件 / 局限** · 需要有足够可靠的终局和过程估值。

**可复用机制** · 把测试搜索轨迹变成可重复使用的价值数据。

<a id="paper-153812"></a>

## Rest-Tuning: Data-Efficient Adaptation of EEG Foundation Models to Individuals via Resting-State Signals

[官方论文页](https://neurips.cc/virtual/2026/poster/153812) · [作者来源](https://openreview.net/forum?id=IWqyUkyULe)

- **问题 / 瓶颈** · 人口模型与个体分布有偏移。
- **核心创新 / 方法** · 用 1–3 分钟静息 EEG 作任务无关适配，再供下游 LoRA。
- **Baseline** · 群体基础模型和任务适配。
- **Benchmark** · 个体 EEG BCI，表示距离及适配插值。
- **关键结果 / 消融** · 距离缩小，插值路径较平滑。
- **适用条件 / 局限** · 依赖静息记录代表可迁移个体偏差。

**可复用机制** · 个性化端侧可先用静息或背景数据校准传感器和个体差异。

<a id="paper-155814"></a>

## Retain-Neutral Surrogates for Min-Max Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/155814) · [作者来源](https://openreview.net/forum?id=2hVefCeDpP)

- **问题 / 瓶颈** · 只扩大遗忘变化可明显损伤保留目标。
- **核心创新 / 方法** · 固定扰动预算，最大化一阶遗忘增益且保留一阶改变量为零。
- **Baseline** · 普通 min-max 近似遗忘。
- **Benchmark** · 局部代理的保留和遗忘目标。
- **关键结果 / 消融** · 摘要给出保留正交代理，量化实证待核。
- **适用条件 / 局限** · 局部线性保留不保证大步安全。

**可复用机制** · 把应保护的目标梯度作为模型编辑方向约束。

<a id="paper-150899"></a>

## Rethinking Attention in Depth for Operator Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150899) · [作者来源](https://openreview.net/forum?id=ebPb7taENV)

- **问题 / 瓶颈** · 随深度表示分辨率坍缩。
- **核心创新 / 方法** · 门控混合层际增量，形成弱相关多核视角。
- **Baseline** · 已有 PDE 注意力求解器。
- **Benchmark** · 八 PDE 基准。
- **关键结果 / 消融** · 一致增益并给出泛化分析。
- **适用条件 / 局限** · 目前实证限算子学习。

**可复用机制** · 用门控增量而不堆叠浅层全量特征，保留互补交互尺度。

<a id="paper-148264"></a>

## Rethinking Bayesian Optimization for Co-Optimizing LLM Training Configurations

[官方论文页](https://neurips.cc/virtual/2026/poster/148264) · [作者来源](https://openreview.net/forum?id=z9znD1Pnfb)

- **问题 / 瓶颈** · 每次训练到收敛使 BO 搜索数极少。
- **核心创新 / 方法** · 按缩放律拟预测器，再把剩余预算用于联合 BO。
- **Baseline** · 全训练的 BO。
- **Benchmark** · 微调数据和模型配置及平均遗憾。
- **关键结果 / 消融** · 分析预算分配，作用是在相同预算扩展配置探索。
- **适用条件 / 局限** · 早期学习曲线外推准确性决定价值。

**可复用机制** · 配置搜索显式分配预算给代理校准和实际探索。

<a id="paper-154643"></a>

## Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/154643) · [作者来源](https://openreview.net/forum?id=C5h9gDqAsN)

- **问题 / 瓶颈** · 离线压缩码未对齐自回归生成。
- **核心创新 / 方法** · 条件退火流，每个 token 在特定噪声层编码前缀残差。
- **Baseline** · 既有动作 tokenizer。
- **Benchmark** · 三模拟基准，重构压缩、效率、任务成功。
- **关键结果 / 消融** · 各轴改善，摘要未核具体幅度。
- **适用条件 / 局限** · 实机及高频精细控制需单测。

**可复用机制** · 把动作码生成顺序写进 tokenizer 的建模语义。

<a id="paper-148979"></a>

## Rethinking Contrastive Loss in CLIP Post-training: A Complementary Framework with Frozen Text Encoder

[官方论文页](https://neurips.cc/virtual/2026/poster/148979) · [作者来源](https://openreview.net/forum?id=tjKgJbAYn9)

- **问题 / 瓶颈** · 遗忘可能被误判为负样本不足。
- **核心创新 / 方法** · 冻结文本端，以低温对齐、原表示锚和 DINOv2 关系蒸馏更新视觉端。
- **Baseline** · 单对比损失或原 CLIP。
- **Benchmark** · CLIP 后训练及下游 VLM 兼容。
- **关键结果 / 消融** · 温度适宜时对比损失是最强单目标。
- **适用条件 / 局限** · 适宜温度和锚强度需要校准。

**可复用机制** · 在改目标前检查尺度；用锚保持已有表示接口。

<a id="paper-148888"></a>

## Rethinking Contrastive Targets in Radiology Language-Image Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/148888) · [作者来源](https://openreview.net/forum?id=uRbyMugqG7)

- **问题 / 瓶颈** · 题材相似的未配对报告会成为假负例，批次越大偏差越大。
- **核心创新 / 方法** · 用合成任务隔离共享事实结构，再把临床陈述与图像相容的文本计作正例。
- **Baseline** · CLIP 式配对身份对比监督。
- **Benchmark** · CLEVR-Radiology、胸片和三维 CT，考察零样本和大批次训练稳定性。
- **关键结果 / 消融** · 消除峰后退化，且只相容性修正方案稳定至批次 2048。
- **适用条件 / 局限** · 依赖相容性判断，摘要未报告跨领域标注成本。

**可复用机制** · 增大对比预训练批次前，检查假负例是否随语义共享系统性增长。

<a id="paper-154194"></a>

## Rethinking Cross-Layer Information Routing in Diffusion Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/154194) · [作者来源](https://openreview.net/forum?id=FV5fsUXnll)

- **问题 / 瓶颈** · 传统残差随深度出现幅值膨胀、梯度衰减及块冗余。
- **核心创新 / 方法** · DAR 用可学习非增量路由聚合历史子层输出。
- **Baseline** · SiT-XL/2，也与 REPA 组合。
- **Benchmark** · ImageNet 256×256 的 FID 和训练迭代数，以及文生图微调。
- **关键结果 / 消融** · FID 由 9.67 到 7.56，匹配基线收敛质量的迭代数为其约 1/8.75。
- **适用条件 / 局限** · 摘要未报告逐层历史状态的显存与墙钟成本。

**可复用机制** · 不同去噪步需要不同深度信息时，可学习选择历史层，而无需所有信息都沿累加残差传递。

<a id="paper-139495"></a>

## Rethinking Dataset Distillation for Classification: Do Distilled Sets Outperform Coresets?

[官方论文页](https://neurips.cc/virtual/2026/poster/139495) · [作者来源](https://openreview.net/forum?id=MMwFjMKetz)

- **问题 / 瓶颈** · 数据蒸馏常混用标准训练和教师监督，使数据贡献难以识别。
- **核心创新 / 方法** · 比较七种蒸馏和三种核心集策略，统一三种训练协议，并检查分布覆盖。
- **Baseline** · 核心集和随机子集。
- **Benchmark** · ImageNet-1K、ImageNet-100 与 ImageNette，比较分类、覆盖和构建开销。
- **关键结果 / 消融** · 大规模设定中最强蒸馏方案与核心集相当或更差，构建成本更高。
- **适用条件 / 局限** · 针对现有分类蒸馏方法及所测协议。

**可复用机制** · 测少量训练数据的效用时，把数据生成、教师监督和模型训练分别控制。

<a id="paper-151740"></a>

## Rethinking Diffusion Decoding via Structural Commitment

[官方论文页](https://neurips.cc/virtual/2026/poster/151740) · [作者来源](https://openreview.net/forum?id=YSIZqo8hoL)

- **问题 / 瓶颈** · 逐 token 置信度难以捕捉跨位置动态依赖。
- **核心创新 / 方法** · SCCE 寻找近似闭合子集，权衡内部可信度和外部依赖泄漏后一起揭开。
- **Baseline** · 局部置信度并行解码。
- **Benchmark** · 扩散语言模型解码的准确率和效率，摘要未列数据集。
- **关键结果 / 消融** · 作者报告准确率与效率折中改善，实测每步附加开销很小。
- **适用条件 / 局限** · 闭合程度需近似，摘要未报告长序列开销。

**可复用机制** · 并行提交离散预测前，可按依赖闭合性分组，避免过早锁定彼此尚未一致的位置。

<a id="paper-149206"></a>

## Rethinking Expressivity and Efficiency in Test-Time Training

[官方论文页](https://neurips.cc/virtual/2026/poster/149206) · [作者来源](https://openreview.net/forum?id=s9Npo5C1Sz)

- **问题 / 瓶颈** · 通常逐 token 更新表达力强而硬件效率低，块近似丢失时序。
- **核心创新 / 方法** · E²-TTT 在块内精确聚合逐 token 系数。
- **Baseline** · 既有 TTT 和混合注意力基线。
- **Benchmark** · 最高 1.3B 的语言建模、检索、长文针检索及吞吐。
- **关键结果 / 消融** · 训练长度八倍时 passkey 准确率仍超过 90%，吞吐与高效块方法相当。
- **适用条件 / 局限** · 适用性依赖可精确聚合的更新规则，摘要未报告其他硬件开销。

**可复用机制** · 块化在线记忆时，先检查动态更新能否代数合成，再决定是否舍弃逐步信息。

<a id="paper-152569"></a>

## Rethinking Geometric Depth in Monocular 3D Object Detection: A Projection-Consistent Reformulation

[官方论文页](https://neurips.cc/virtual/2026/poster/152569) · [作者来源](https://openreview.net/forum?id=S8aGdjePrD)

- **问题 / 瓶颈** · 框高投影的简式即使用真实输入也会估计可见前表面深度，导致尺寸相关偏差。
- **核心创新 / 方法** · PCDepth 根据透视几何校正中心深度，并以 GeoAlign 增强轻量模型的属性感知。
- **Baseline** · 使用二维框高的标准投影公式及现有检测器。
- **Benchmark** · 四个基准，包括 KITTI、Omni3D Out，以 AP3D 等评估。
- **关键结果 / 消融** · 完整方法在 KITTI 上增益 1.44%、Omni3D Out 上增益 2.80%。
- **适用条件 / 局限** · 校正依赖尺寸和朝向，摘要未报告两项设计各自的增益。

**可复用机制** · 用理想真值输入检验几何公式是否预测了正确的参考点，再把系统性偏差写成显式校正。

<a id="paper-150576"></a>

## Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/150576) · [作者来源](https://openreview.net/forum?id=h9Je8c91Qi)

- **问题 / 瓶颈** · 只存离散事实会丢细节和事实间关系，固定提示也难适应对话。
- **核心创新 / 方法** · TriMem 保留三种粒度，通过回答质量反馈用 TextGrad 更新提示。
- **Baseline** · 已有长期记忆方法。
- **Benchmark** · LoCoMo、PerLTQA，多种 LLM 主干。
- **关键结果 / 消融** · 作者报告一致优于强记忆基线。
- **适用条件 / 局限** · 摘要未报告三层各自收益和维护开销。

**可复用机制** · 检索用紧凑事实，推理用聚合语义，要求高保真时回溯原文。

<a id="paper-150214"></a>

## Rethinking Incompleteness: Formalizing Protocol Divergence and Train-Once Learning for Robust IMVC

[官方论文页](https://neurips.cc/virtual/2026/poster/150214) · [作者来源](https://openreview.net/forum?id=ju9V3PfmHR)

- **问题 / 瓶颈** · 同样的缺失率下可供联合学习的完整样本数差距很大。
- **核心创新 / 方法** · 形式化协议差异，使用独立样本和只聚合已观测视图的掩码注意力训练单一模型。
- **Baseline** · 按不同缺失配置重新训练的基线。
- **Benchmark** · 七个不完整多视图聚类基准。
- **关键结果 / 消融** · 同缺失率下完整样本占比最多相差 50 倍，CRAFT 匹配或超越基线，训练开销约为其 1/8.8。
- **适用条件 / 局限** · 训练仍依赖完整数据，理论失败阈值针对部分重构目标。

**可复用机制** · 将跨模态缺失的鲁棒性落实在可处理任意可见集合的融合层，并按缺失结构设置对照。

<a id="paper-153158"></a>

## Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/153158) · [作者来源](https://openreview.net/forum?id=NS7JAOxOVv)

- **问题 / 瓶颈** · 少数去噪步的局部熵尖峰和幻觉相关，过早锁定 token 会丢候选语义。
- **核心创新 / 方法** · StepRefine 在异常步改用概率加权嵌入做连续细化，稳定时回到离散去噪。
- **Baseline** · 普通离散去噪。
- **Benchmark** · 多种多模态扩散语言模型及多模态基准，摘要未列名称。
- **关键结果 / 消融** · 作者报告多种模型上缓解幻觉。
- **适用条件 / 局限** · 熵尖峰是经验信号，附加迭代开销未报告。

**可复用机制** · 以相邻步骤的熵曲线判断何时保留软候选，避免为每一步都增加推理开销。

<a id="paper-152596"></a>

## Rethinking Knowledge Distillation for Diffusion Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152596) · [作者来源](https://openreview.net/forum?id=RwFzh7uPPD)

- **问题 / 瓶颈** · 更多教师数据不能保证传统前向 KL 蒸馏改善，且可能输给普通去噪。
- **核心创新 / 方法** · 离线吸收后转在线学生轨迹，按教师置信度加权并用信任域稳定目标。
- **Baseline** · 前向 KL 和原扩散去噪目标。
- **Benchmark** · MDLM-110M 教师与 Dream-7B 至 93M 学生，报告不同模型打分的困惑度。
- **关键结果 / 消融** · Dream 蒸馏学生的 Qwen-2.5 困惑度从前向 KL 的 25.23 降至 19.83。
- **适用条件 / 局限** · 小规模设定还用了额外散度，摘要未报告各部件单独收益。

**可复用机制** · 慢慢把蒸馏监督从教师采样分布移到学生实际走过的去噪状态，避免只在理想轨迹上学习。

<a id="paper-151695"></a>

## Rethinking Language Model Scaling under Transferable Hypersphere Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151695) · [作者来源](https://openreview.net/forum?id=Yiph6nL9MR)

- **问题 / 瓶颈** · 一阶优化的迁移规律未必适用于约束优化。
- **核心创新 / 方法** · HyperP 联合处理宽度、深度、数据和 MoE 粒度，并给出球面下衰减分析。
- **Baseline** · 强 Muon 基线。
- **Benchmark** · 按训练 FLOPs 扩展语言模型，跟踪计算效率和稳定性指标。
- **关键结果 / 消融** · 在 6×10²¹ FLOPs 时计算效率高 1.58 倍，报告数据学习率指数 0.32。
- **适用条件 / 局限** · 结论限于 Frobenius 球约束及所测规模。

**可复用机制** · 改变权重几何后分别重验深度缩放、权重衰减和学习率的功能。

<a id="paper-153444"></a>

## Rethinking Layer-wise Model Merging through Chain of Merges

[官方论文页](https://neurips.cc/virtual/2026/poster/153444) · [作者来源](https://openreview.net/forum?id=LGEP9eG2Ie)

- **问题 / 瓶颈** · 独立合并各层会让早层激活变化在下游累积成协变量偏移。
- **核心创新 / 方法** · CoM 逐层重算输入并回归合并权重，对可能退化的任务层动态加权。
- **Baseline** · 逐层独立模型合并方法。
- **Benchmark** · 异质任务的标准基准，摘要未列任务名和指标。
- **关键结果 / 消融** · 作者报告超过现有合并方法。
- **适用条件 / 局限** · 需要重算激活，摘要未报告校准数据量和成本。

**可复用机制** · 任何会改写早期表征的后处理都可用新激活重新校准后续层。

<a id="paper-154686"></a>

## Rethinking Learning from Label Proportions via Moment Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/154686) · [作者来源](https://openreview.net/forum?id=BjxyNdu4tO)

- **问题 / 瓶颈** · 单样本独立组包假设经常不成立。
- **核心创新 / 方法** · 在给定实例时标签条件独立，据 Poisson 多项式模型匹配多阶阶乘矩。
- **Baseline** · 假设随机组包的标签占比学习方法。
- **Benchmark** · 不同组包规则下的分类基准，摘要未列名称和指标。
- **关键结果 / 消融** · 作者报告有效且保持计算效率。
- **适用条件 / 局限** · 条件独立和包间独立仍需满足。

**可复用机制** · 弱监督统计的生成机制不适合随机组包时，可按真实计数分布改变匹配目标。

<a id="paper-151504"></a>

## Rethinking Long-Video Efficiency: A Joint Allocation Perspective on Frames, Pixels, and Front-End Latency

[官方论文页](https://neurips.cc/virtual/2026/poster/151504) · [作者来源](https://openreview.net/forum?id=a9xLyT4hG4)

- **问题 / 瓶颈** · 统一帧像素预算忽略视频解码时延和细节需求
- **核心创新 / 方法** · 低分视频走原视频路，高分图走原图路；选择可用关键帧元数据或查询相关性和多样性
- **Baseline** · 原分辨率基线、最强既有效率法
- **Benchmark** · 三长视频基准，匹配 token 预算及小时级前端延迟
- **关键结果 / 消融** · 平均较原基线高 10.6%、较效率法高 5.2%，前端最高快七倍
- **适用条件 / 局限** · 依赖视觉模型双流接口及视频编码

**可复用机制** · 预算联合调时间采样、空间分辨率与实际解码成本

<a id="paper-154754"></a>

## Rethinking LoRA Initialization for Robust Asymmetric Learning Rates

[官方论文页](https://neurips.cc/virtual/2026/poster/154754) · [作者来源](https://openreview.net/forum?id=BDO32ssOHO)

- **问题 / 瓶颈** · 标准初始化的尺度噪声会令高学习率比不稳定
- **核心创新 / 方法** · 调整初始化以额外抑制尺度噪声，同时保留初始适配器零输出
- **Baseline** · 标准 LoRA 初始化
- **Benchmark** · 多任务、秩及学习率倍数设置
- **关键结果 / 消融** · 稳定区扩大，高比例不再轻易崩溃；摘要未列幅度
- **适用条件 / 局限** · 宽度法则仅供有限预训练模型起点

**可复用机制** · 不要仅调实际更新倍数，应联合搜索初始化和两矩阵学习率

<a id="paper-152392"></a>

## Rethinking On-Policy Self-Distillation for Thinking Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152392) · [作者来源](https://openreview.net/forum?id=TQYJEnjfUC)

- **问题 / 瓶颈** · 给教师特权条件可能压缩学生回溯探索
- **核心创新 / 方法** · 比对普通与特权教师在自纠分支对词元的信号
- **Baseline** · 普通在线蒸馏与特权教师蒸馏
- **Benchmark** · 思考模型 rollout 质量、长度归一化后的验证回溯标记
- **关键结果 / 消融** · 特权蒸馏减少复核、回溯和保留态度标记
- **适用条件 / 局限** · 行为标记只是代理，尚需检查实际纠错成效

**可复用机制** · 对训练前后相同题的纠错轨迹做逐步信用诊断

<a id="paper-155478"></a>

## Rethinking Parallel Multi-Agent Systems: A Cost-Aware Framework for Efficient Coordination

[官方论文页](https://neurips.cc/virtual/2026/poster/155478) · [作者来源](https://openreview.net/forum?id=5ISO2WDCul)

- **问题 / 瓶颈** · 并行工作器重复探索并产生后期合并成本
- **核心创新 / 方法** · 从主会话分叉工作器并预先约定共享接口，层级确定性调度
- **Baseline** · Claude Code 与强多智能体基线
- **Benchmark** · 任务耗时与吞吐，摘要未列具体任务
- **关键结果 / 消融** · 平均吞吐 2.2 倍，墙钟加速 2.6 倍对 Claude Code
- **适用条件 / 局限** · 依赖任务可分割和上下文可分叉

**可复用机制** · 并行前将共同约定和复用上下文纳入成本估计

<a id="paper-153944"></a>

## Rethinking Projector Training in Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153944) · [作者来源](https://openreview.net/forum?id=HObX41utGv)

- **问题 / 瓶颈** · 配对图文训练成本高
- **核心创新 / 方法** · 在共享主子空间拟合两模态高斯统计并求最优传输映射
- **Baseline** · 用 50 万图文对的标准流程
- **Benchmark** · 六语言骨干、两视觉编码器、16 基准
- **关键结果 / 消融** · 七组合中三组合领先，其余平均差在 1.6 分内
- **适用条件 / 局限** · 全局统计未保证实例层语义对齐

**可复用机制** · 多模态模块初始化时对照数据驱动训练和统计匹配

<a id="paper-150039"></a>

## Rethinking Psychometric Evaluation of LLMs: When and Why Self-Reports Predict Behavior

[官方论文页](https://neurips.cc/virtual/2026/poster/150039) · [作者来源](https://openreview.net/forum?id=lEX44N0oQW)

- **问题 / 瓶颈** · 问卷自报容易受即时提示改变
- **核心创新 / 方法** · 对照自报、暗示下行为与跨情景稳定性
- **Baseline** · 普通与 persona 提示
- **Benchmark** · 人格自报、隐性偏差和奉承行为
- **关键结果 / 消融** · 人设提示增加自报一致性却未改善行为一致性
- **适用条件 / 局限** · 来自所测任务与人设量表

**可复用机制** · 部署 persona 时单列自报和压力条件下可观察行为

<a id="paper-148870"></a>

## Rethinking Ratio-Based Trust Regions for Policy Optimization in Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148870) · [作者来源](https://openreview.net/forum?id=uZ0Ls2oCg3)

- **问题 / 瓶颈** · 比率趋零时传统信赖设计可能缺纠正反馈
- **核心创新 / 方法** · 用乘法对称屏障保留纠正梯度并对近零比率增加罚
- **Baseline** · MAPPO、MASPO、灵活边界消融
- **Benchmark** · 八环境 47 项任务，含 PaxMen 和 AeroJAX
- **关键结果 / 消融** · 整体持平或更强，消融支持屏障几何作用
- **适用条件 / 局限** · 适用于所测多智能体设置，任务级方差未列

**可复用机制** · 大协作策略更新时测边界机制是否仍保留修正梯度

<a id="paper-156790"></a>

## Rethinking Reward Models for Multi-Domain Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/156790) · [作者来源](https://neurips.cc/virtual/2026/poster/156790)

- **问题 / 瓶颈** · 逐步评分误差随轨迹加长积累
- **核心创新 / 方法** · 从理论和长程推理实践比较过程聚合与终局生成验证
- **Baseline** · 过程奖励模型与终局验证器
- **Benchmark** · 多域测试时推理及包含自纠的长轨迹
- **关键结果 / 消融** · 理论与实证支持分步聚合误差随长度扩大
- **适用条件 / 局限** · 结论受过程评分质量及任务验证性影响

**可复用机制** · 候选筛选按轨迹长度分层，避免默认逐步评分更可靠

<a id="paper-149183"></a>

## Rethinking "RL Generalizes, SFT Memorizes": The Role of SFT Data

[官方论文页](https://neurips.cc/virtual/2026/poster/149183) · [作者来源](https://openreview.net/forum?id=sGr1f8yocs)

- **问题 / 瓶颈** · 训练量和数据来源差异可能被误归因于算法
- **核心创新 / 方法** · 对齐 rollout 预算，检查数据覆盖稀有解法的影响
- **Baseline** · RL 和匹配条件下的 SFT
- **Benchmark** · 推理泛化、解法覆盖，摘要未列任务名
- **关键结果 / 消融** · 匹配预算即可让 SFT 追平，叠加数据因素可超过 RL
- **适用条件 / 局限** · 发现受数据分布和生成可及性约束

**可复用机制** · 训练方法消融同时报告样本生成预算和长尾思路覆盖

<a id="paper-139009"></a>

## Rethinking SAE Evaluation: An Atomic Interpretable Unit Framework Reveals Hidden Polysemanticity and Redundancy

[官方论文页](https://neurips.cc/virtual/2026/poster/139009) · [作者来源](https://openreview.net/forum?id=qsqJBHB0Kb)

- **问题 / 瓶颈** · 均匀平均可掩盖高贡献特征多义或冗余
- **核心创新 / 方法** · 用原子可解释单元框架按功能贡献诊断
- **Baseline** · 常规 SAE 指标及跨模型对照
- **Benchmark** · 多模型族的特征解释性和冗余
- **关键结果 / 消融** · 部分常规评分看似单义，但高贡献特征更不清晰且冗余
- **适用条件 / 局限** · 归因依赖贡献估计与解释量表

**可复用机制** · 上线可解释性工具前加主导特征分层诊断

<a id="paper-154100"></a>

## Rethinking Softmax Attention: Polynomial Activations for Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/154100) · [作者来源](https://openreview.net/forum?id=GFLgVpdI1N)

- **问题 / 瓶颈** · 训练稳定常被归为概率归一。
- **核心创新 / 方法** · 理论和实验对照能控 Frobenius 范数的多项式激活。
- **Baseline** · softmax 注意力。
- **Benchmark** · 多个 Transformer 应用。
- **关键结果 / 消融** · 部分多项式非正、非归一仍有效。
- **适用条件 / 局限** · 需验证矩阵尺度随长度和深度变化。

**可复用机制** · 设计注意力替代时将算子范数和概率解释拆开。

<a id="paper-151964"></a>

## Rethinking State Tracking in Recurrent Models Through Error Control Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/151964) · [作者来源](https://openreview.net/forum?id=WUTtJ13Ih0)

- **问题 / 瓶颈** · 形式可表达未必能在长序列纠错。
- **核心创新 / 方法** · 用状态可读性比率预测仿射递归失效。
- **Baseline** · SSM、线性注意力等仿射结构。
- **Benchmark** · 群状态跟踪及解码阈值。
- **关键结果 / 消融** · 到阈值后跟踪崩溃，理论说明分离子空间误差无法纠正。
- **适用条件 / 局限** · 限制于保持状态表示的仿射网络。

**可复用机制** · 需要稳定状态记忆时单测外部噪声后错误是否收缩。

<a id="paper-152202"></a>

## Rethinking Structured Generation: Can Graph-Based Reasoning Resolve Ambiguity?

[官方论文页](https://neurips.cc/virtual/2026/poster/152202) · [作者来源](https://openreview.net/forum?id=Uo6FQhB7p7)

- **问题 / 瓶颈** · 单参考压制有效解释。
- **核心创新 / 方法** · 把候选写成实体关系图，用语义和关系一致性选择。
- **Baseline** · 标准单参考训练。
- **Benchmark** · 结构化生成、多级歧义。
- **关键结果 / 消融** · 准确、稳定、稳健均改善。
- **适用条件 / 局限** · 依赖候选覆盖和可评估关系。

**可复用机制** · 对计划和程序多解，用集合监督后再按约束重排。

<a id="paper-156791"></a>

## Rethinking the Mixture of Vision Encoders Paradigm for Enhanced Visual Understanding in Multimodal LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/156791) · [作者来源](https://openreview.net/forum?id=tgnTVmRybs)

- **问题 / 瓶颈** · 直接混合忽略编码器适配和长图块序列。
- **核心创新 / 方法** · 独立投影、适配后融合、动态分块及全局视野。
- **Baseline** · 其他视觉编码器混合方法。
- **Benchmark** · 11 视觉语言基准。
- **关键结果 / 消融** · 多数任务优于现有 MoVE。
- **适用条件 / 局限** · 计算与裁切策略需要跟分辨率对齐。

**可复用机制** · 先保留各主干表达习惯，再对齐对应空间局部。

<a id="paper-149274"></a>

## Rethinking the Readout: Unlocking Video Backbones for AI-Generated Video Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/149274) · [作者来源](https://openreview.net/forum?id=rXN1Faijz6)

- **问题 / 瓶颈** · 全局池化抹除补丁间运动。
- **核心创新 / 方法** · 在 patch 速度场上双流读出。
- **Baseline** · 图像主干和标准视频池化。
- **Benchmark** · AIGVDBench，冻结和全量训练。
- **关键结果 / 消融** · 冻结 AUC 95.28，仅加约 50 万参数。
- **适用条件 / 局限** · 生成检测易受来源域影响。

**可复用机制** · 时序任务保留局部运动再做低成本聚合。

<a id="paper-148467"></a>

## Rethinking the State Update Gate for Long-Sequence Recurrent 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/148467) · [作者来源](https://openreview.net/forum?id=xbkV9cLvUl)

- **问题 / 瓶颈** · 逐 token 门近似帧不变，记忆约三帧。
- **核心创新 / 方法** · 从连续内部特征差构造免训练帧级标量门。
- **Baseline** · TTT3R 类逐 token 门。
- **Benchmark** · 六基准覆盖位姿、深度、3D，最长 4541 帧。
- **关键结果 / 消融** · TUM ATE 降 51%，Bonn AbsRel 降 12.8%。
- **适用条件 / 局限** · 帧差不全等于新信息，剧烈干扰需测。

**可复用机制** · 先测有效记忆时域，再将关键帧权重连到状态更新。

<a id="paper-149503"></a>

## Rethinking Time Series Tokenization from a Frequency Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/149503) · [作者来源](https://openreview.net/forum?id=pexLx2W7yd)

- **问题 / 瓶颈** · 时域分块扭曲频率与季节性。
- **核心创新 / 方法** · 频域分区、频移及 Nyquist 采样。
- **Baseline** · 常见分块 tokenizer。
- **Benchmark** · 预测、分类、异常检测。
- **关键结果 / 消融** · 无需参数且多任务改善，数值待核。
- **适用条件 / 局限** · 依赖能有效表征的频带，局部突变需验证。

**可复用机制** · 当周期量重要时让 token 保持频带而非固定相邻时间跨度。

<a id="paper-152599"></a>

## Rethinking Training Targets, Architectures and Data Quality for Universal Speech Enhancement

[官方论文页](https://neurips.cc/virtual/2026/poster/152599) · [作者来源](https://openreview.net/forum?id=RvRtBJQkGQ)

- **问题 / 瓶颈** · 早反射目标损害听感和 ASR。
- **核心创新 / 方法** · 改用时间对齐消声信号，两阶段平衡失真和感知，并比较训练数据质量。
- **Baseline** · 早反射目标和大未清理语料。
- **Benchmark** · 通用语音增强，感知和识别。
- **关键结果 / 消融** · 好目标改善表现，未清理大数据限制去细小瑕疵。
- **适用条件 / 局限** · 不同麦克风声学需重测。

**可复用机制** · 恢复任务须验证所谓较干净目标是否仍保留不希望拟合的成分。

<a id="paper-152704"></a>

## Rethinking Vector Field Learning for Generative Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/152704) · [作者来源](https://openreview.net/forum?id=R12MIytQsT)

- **问题 / 瓶颈** · 向量场近类中心梯度消失并跨越轨迹。
- **核心创新 / 方法** · 用脱梯度距离项加吸引与排斥。
- **Baseline** · 标准流匹配及判别专模。
- **Benchmark** · 生成式分割实验。
- **关键结果 / 消融** · 收敛和类分离改善，缩小判别差距。
- **适用条件 / 局限** · 依赖类质心和距离定义。

**可复用机制** · 检查生成类场在邻界是否分离，按距离提高局部梯度。

<a id="paper-151683"></a>

## Rethinking Visual Attribution for Chest X-ray Reasoning in Large Vision Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151683) · [作者来源](https://openreview.net/forum?id=YoNjeiTDbj)

- **问题 / 瓶颈** · 专家框不一定对应模型实际依据。
- **核心创新 / 方法** · 反事实编辑先确认区域影响，再比较归因与解剖概念方法。
- **Baseline** · 11 种归因。
- **Benchmark** · 六 VLM，胸片问答，直接和推理输出。
- **关键结果 / 消融** · 常见归因定位模型证据失败。
- **适用条件 / 局限** · 编辑可能引入伪迹，筛后样本有偏。

**可复用机制** · 先做区域介入再拿标注做归因靶，区别专家合理性和模型因果性。

<a id="paper-153173"></a>

## Rethinking Visual Reasoning in Text-to-Image Reward Modeling

[官方论文页](https://neurips.cc/virtual/2026/poster/153173) · [作者来源](https://openreview.net/forum?id=NIlMvxosjw)

- **问题 / 瓶颈** · 常规偏好微调损伤视觉推理。
- **核心创新 / 方法** · 从视觉数据构造同一图的对照文本偏好。
- **Baseline** · HPSv3、常规人类偏好与持续学习。
- **Benchmark** · GenEval 组合生成，Best-of-N 和 RL。
- **关键结果 / 消融** · 生成分别提高 4.0% 与 5.5%，优于使用六倍偏好对的比较项。
- **适用条件 / 局限** · 配对需排除文字捷径和假负例。

**可复用机制** · 给奖励模型正交对照，区分审美排序与逐对象语义对齐。

<a id="paper-138901"></a>

## Rethinking XAI Evaluation: A Human-Centered Audit of Shapley Benchmarks in High-Stakes Settings

[官方论文页](https://neurips.cc/virtual/2026/poster/138901) · [作者来源](https://openreview.net/forum?id=y1PstYDXDq)

- **问题 / 瓶颈** · 稀疏和忠实代理无法预测使用效用。
- **核心创新 / 方法** · 对照 Shapley 变体的定量代理与专家操作。
- **Baseline** · 不同 Shapley 变体及无解释。
- **Benchmark** · 四风险数据集，3735 次专业欺诈案例审阅。
- **关键结果 / 消融** · 信心升而客观表现未改善。
- **适用条件 / 局限** · 实证为一种专业场景。

**可复用机制** · 部署解释前测是否增加过度自信，而非只测解释相似度。

<a id="paper-155661"></a>

## ReToken: One Token to Improve Vision–Language Models for Visual Retrieval

[官方论文页](https://neurips.cc/virtual/2026/poster/155661) · [作者来源](https://openreview.net/forum?id=3wq3a93YtO)

- **问题 / 瓶颈** · 全视觉 token 挤占显存且干扰。
- **核心创新 / 方法** · 单嵌入做查询，从预填充缓存选稀疏相关 token。
- **Baseline** · 原 Qwen3VL 等全上下文。
- **Benchmark** · Visual Haystacks、LVBench。
- **关键结果 / 消融** · 分别提升 12、8.5 点，视频为零样本。
- **适用条件 / 局限** · 依赖可保留预填充缓存和足够召回。

**可复用机制** · 先学习抽取视觉证据，再把长上下文容量留给推理。

<a id="paper-151873"></a>

## RETR: A Structure-Preserving RGB-Event Transformer for Robust 3D Lane Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151873) · [作者来源](https://openreview.net/forum?id=XFvlFrfW1M)

- **问题 / 瓶颈** · RGB 在困难光照下缺稳定观测。
- **核心创新 / 方法** · 以结构保留 Transformer 将 RGB 和事件合为 3D 车道几何。
- **Baseline** · 3D 车道检测方法。
- **Benchmark** · 两检测基准、复杂光照和路面。
- **关键结果 / 消融** · 两基准表现领先，困难切片改善。
- **适用条件 / 局限** · 依赖时间和空间配准，实证是车道。

**可复用机制** · 互补传感融合要验证是否保持空间几何，而非只加通道。

<a id="paper-150000"></a>

## Retrieval-Centric Deep Learning in Growing Nonparametric Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/150000) · [作者来源](https://openreview.net/forum?id=lYGqisD7No)

- **问题 / 瓶颈** · 定宽参数压缩可能浪费数据点信息。
- **核心创新 / 方法** · 每例追加键值表示，推理用核化注意力检索；分析固定网络优化器连接。
- **Baseline** · 定宽网络、MesaNet/DeltaNet 相关扩展。
- **Benchmark** · 经典图像分类和合成师生任务。
- **关键结果 / 消融** · 摘要报告样本效率有优势。
- **适用条件 / 局限** · 存储随样本增长，检索预算需测。

**可复用机制** · 在少样本设置把权重学习和显式保留训练例作为可比较选择。

<a id="paper-154257"></a>

## Retrieval from Within: An Intrinsic Capability of Attention-Based Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154257) · [作者来源](https://openreview.net/forum?id=F87kwK5CpT)

- **问题 / 瓶颈** · 外部检索和生成不共享表示。
- **核心创新 / 方法** · 以解码器查询给预编码证据片排序，复用选片。
- **Baseline** · 带独立检索器方案。
- **Benchmark** · 注意力内生证据检索。
- **关键结果 / 消融** · 摘要证明可引出此能力，量化待核。
- **适用条件 / 局限** · 预编码与生成需接口兼容。

**可复用机制** · 先验证基模型是否可同时用作证据过滤和消费。

<a id="paper-155146"></a>

## Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information

[官方论文页](https://neurips.cc/virtual/2026/poster/155146) · [作者来源](https://openreview.net/forum?id=7yVqyPZh09)

- **问题 / 瓶颈** · 平均注意力难筛因果头。
- **核心创新 / 方法** · 扫查询与聚合选择，选输出预测查询并累加真值区域。
- **Baseline** · 随机头遮蔽。
- **Benchmark** · 四 VLM、五指代表达基准。
- **关键结果 / 消融** · 遮前 20 头可降最多 80 个百分点。
- **适用条件 / 局限** · 依赖区域标签，注意头可跨任务但实证条件有限。

**可复用机制** · 剪视觉注意头前按输出用途做区域遮蔽验收。

<a id="paper-151927"></a>

## Retrieval Over Training: Similarity search-based Model Selection for Time Series Anomaly Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151927) · [作者来源](https://openreview.net/forum?id=WpZao8pAB7)

- **问题 / 瓶颈** · 单一检测器不覆盖多样序列，监督选择器域外易退化。
- **核心创新 / 方法** · 用无训练的相似检索估候选检测器适用度。
- **Baseline** · 既有模型选择方案。
- **Benchmark** · 时序异常检测和域外切分。
- **关键结果 / 消融** · 摘要称检索方案强且省，幅度待核。
- **适用条件 / 局限** · 依赖相似特征与候选算法性能相关。

**可复用机制** · 低标签域移时按历史相近例做工具路由。

<a id="paper-148700"></a>

## Retriever-Free Retrieval-Augmented Reasoning via Corpus-Traversing MCTS

[官方论文页](https://neurips.cc/virtual/2026/poster/148700) · [作者来源](https://openreview.net/forum?id=vi37A4okc6)

- **问题 / 瓶颈** · 独立检索器固定 top-k 与推理的细粒度需要脱节。
- **核心创新 / 方法** · 以语料遍历 MCTS 搜索可引用片段。
- **Baseline** · 四种带独立检索的多步推理方法。
- **Benchmark** · 五开放 QA 基准，单跳、多跳，EM 和 F1。
- **关键结果 / 消融** · 比较平均提高 14.4%。
- **适用条件 / 局限** · 索引拓扑和每查询搜索成本需要独立比较。

**可复用机制** · 把检索动作定义为逐步选择证据路径，以用后续答案评估搜索质量。

<a id="paper-154122"></a>

## Retrieve-then-Rerank Inference for Vocabulary-Based End-to-End Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/154122) · [作者来源](https://openreview.net/forum?id=G78WOdoS5c)

- **问题 / 瓶颈** · 在线联合给全部静态候选和动态场景编码，重复计算且精排昂贵。
- **核心创新 / 方法** · 缓存候选表示，按路线和动力学可达性检索，再以场景条件精排。
- **Baseline** · Hydra-MDP++。
- **Benchmark** · NAVSIM v2 和 navhard，EPDMS 及延迟。
- **关键结果 / 消融** · NAVSIM v2 达 86.1 EPDMS、23.9 ms，约快 6.8 倍。
- **适用条件 / 局限** · 依赖固定轨迹库和轻量检索保持候选覆盖。

**可复用机制** · 将场景无关的动作计划计算挪至离线，把昂贵上下文评分留给少数可行候选。

<a id="paper-154552"></a>

## Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs

[官方论文页](https://neurips.cc/virtual/2026/poster/154552) · [作者来源](https://openreview.net/forum?id=CiRFut5zi2)

- **问题 / 瓶颈** · 独立零样本试次无法利用已验证的局部成功经验。
- **核心创新 / 方法** · 按进度存储成功片段，检索后用轨迹一致性筛选，按置信度引导流匹配中间状态。
- **Baseline** · 冻结生成式 VLA 的原始部署流程。
- **Benchmark** · 仿真和真机操作，考察成功率及闭环稳定性。
- **关键结果 / 消融** · 作者报告长程和多阶段任务尤其受益。
- **适用条件 / 局限** · 需要可识别的成功事件以及相对稳定的环境，摘要未给数值。

**可复用机制** · 以历史动作作为可调强度的采样先验，保留生成策略对当前观测的修正能力。

<a id="paper-148557"></a>

## Retrieve What’s Missing: Coverage-Maximizing Retrieval for Consistent Long Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148557) · [作者来源](https://openreview.net/forum?id=x0gbPKK4uf)

- **问题 / 瓶颈** · 位姿或视场重叠太粗，完整三维重建维护昂贵。
- **核心创新 / 方法** · 用预训练深度估计构造目标视角覆盖图，逐个补充当前上下文未覆盖区域并缓存深度。
- **Baseline** · 基于位姿、视野重叠或显式三维的记忆检索是方法背景。
- **Benchmark** · RealEstate10K 和 DL3DV，几何一致性与延迟。
- **关键结果 / 消融** · 摘要报告长程一致性提高且维持较低延迟。
- **适用条件 / 局限** · 依赖深度先验和视角几何，摘要未报告动态场景边界。

**可复用机制** · 记忆检索可按边际覆盖增益取代逐条相似性排名，避免多条候选重复解释同一视野。

<a id="paper-151575"></a>

## Return to Basics: Very Simple Graph Contrastive Learning via Noise Cancellation Principle

[官方论文页](https://neurips.cc/virtual/2026/poster/151575) · [作者来源](https://openreview.net/forum?id=ZZZah2bobp)

- **问题 / 瓶颈** · 异配图上的复杂增强或负例采样未必改善特征噪声。
- **核心创新 / 方法** · 使用 GCN 获得结构表示、MLP 处理节点特征，无需数据增强和负例采样。
- **Baseline** · 已有图对比学习及 GCN-MLP 对照。
- **Benchmark** · 异配和同配图基准，考察性能及计算资源。
- **关键结果 / 消融** · 摘要报告异配任务达到既有最佳水平，同配也显示复杂度与鲁棒性优势。
- **适用条件 / 局限** · 具体数据集与增益未报告。

**可复用机制** · 同一数据已有原始信号和关系视图时，先验证这两者能否替代人工对比增强。

<a id="paper-153712"></a>

## Reusable Conditional Resampling via Flow Matching for Constraint-Based Causal Discovery

[官方论文页](https://neurips.cc/virtual/2026/poster/153712) · [作者来源](https://openreview.net/forum?id=JLCT3nT7eW)

- **问题 / 瓶颈** · 因果图搜索需做许多条件独立性检验，逐查询建模昂贵。
- **核心创新 / 方法** · FMCIT 用联合流匹配与条件补全生成随机化副本，PC 搜索只在预算内做高开销检验。
- **Baseline** · 查询特定的生成式检验及已有 PC 搜索作为方法背景。
- **Benchmark** · 合成和真实数据，高维非线性下的准确度与效率。
- **关键结果 / 消融** · 作者报告系统改善准确度与效率折中。
- **适用条件 / 局限** · 条件生成质量和筛选误差仍重要，摘要未给误差数值。

**可复用机制** · 有大量共享变量的条件统计查询时，先尝试复用联合分布模型，再用廉价筛选分配检验预算。

<a id="paper-155863"></a>

## Revealing Epistemic Uncertainty in MLLMs via Causal-Invariant Masking

[官方论文页](https://neurips.cc/virtual/2026/poster/155863) · [作者来源](https://openreview.net/forum?id=2LQvJtzsgM)

- **问题 / 瓶颈** · 只估计输入模糊性可能漏掉模型依赖表面相关造成的不确定。
- **核心创新 / 方法** · CIM 对照原预测和聚焦视图，以语义散度评估，EED 用嵌入漂移近似。
- **Baseline** · 既有多模态不确定量化方法。
- **Benchmark** · 多个幻觉与不确定性相关基准，摘要未列名称。
- **关键结果 / 消融** · 快速代理表现接近且摘要报告提速近 50%。
- **适用条件 / 局限** · 需要合适的证据掩码，摘要未报告选错区域的影响。

**可复用机制** · 保持任务证据而减少可能的捷径信息，观察输出含义是否稳定。

<a id="paper-154819"></a>

## Revealing the Gap in Human and VLM Scene Perception through Counterfactual Semantic Saliency

[官方论文页](https://neurips.cc/virtual/2026/poster/154819) · [作者来源](https://openreview.net/forum?id=AifzSQYpMJ)

- **问题 / 瓶颈** · 白盒归因不适用于闭源模型，被动指标难隔离物体作用。
- **核心创新 / 方法** · CSS 在反事实场景比较生成描述的语义变化，并与人的反应对照。
- **Baseline** · 人类心理物理实验，含 16,289 个有效响应。
- **Benchmark** · 场景描述中不同物体的语义作用，考察尺寸、位置与显著性。
- **关键结果 / 消融** · 模型较人更依赖大、居中或显著物体，对人物依赖较低。
- **适用条件 / 局限** · 物体消融需要控制编辑副作用，摘要未给跨分布验证。

**可复用机制** · 对闭源视觉系统可从输入端控制物体证据，再以语义差异量化其决策影响。

<a id="paper-152349"></a>

## Reverse to Advance: Teleoperation-Cost Effective Hard Policy Learning from Reversed Easy Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/152349) · [作者来源](https://openreview.net/forum?id=TjThMMz3Bw)

- **问题 / 瓶颈** · 正向精细操作难以示范，而逆过程易采，直接反转数据仍有噪声。
- **核心创新 / 方法** · 交替跑正反策略完成环境重置，用运动先验和价值优势筛反转样本，再迭代训练。
- **Baseline** · 基于反转的已有方法和强化学习对照。
- **Benchmark** · 两个仿真基准及真机，比较困难任务成功、数据效率和稳定性。
- **关键结果 / 消融** · 作者报告成功率、数据效率和稳定性改善。
- **适用条件 / 局限** · 需有安全可行的反向任务，且对应正向行为仍具有可执行性。

**可复用机制** · 处理动作方向不对称的任务时，把容易采的过程反转当作候选示范，再检查动力学和价值。

<a id="paper-150362"></a>

## Reversing the Roles of Signal and Noise: Modeling Noise in Astronomical Images without Paired Data

[官方论文页](https://neurips.cc/virtual/2026/poster/150362) · [作者来源](https://openreview.net/forum?id=idM55TPMck)

- **问题 / 瓶颈** · 结构噪声不能孤立观测，无法直接监督。
- **核心创新 / 方法** · 先学习干净信号的得分，以 Langevin 更新从粗糙噪声初估开始逐步校正。
- **Baseline** · 当代 TESS 流水线的滤波工具。
- **Benchmark** · TESS 天文图像杂散光与彗星观测窗口预测。
- **关键结果 / 消融** · 作者报告更干净的杂散光估计，并用几何条件预测窗口内污染。
- **适用条件 / 局限** · 假设加性分解和可学干净先验，摘要未报告跨仪器效果。

**可复用机制** · 难以建模噪声时可改为给候选残余信号打合理性分数，借助正向观测模型反推噪声。

<a id="paper-153961"></a>

## Revisiting Activation Steering Through an Optimization Lens

[官方论文页](https://neurips.cc/virtual/2026/poster/153961) · [作者来源](https://openreview.net/forum?id=HEjj1BD9e9)

- **问题 / 瓶颈** · 固定均值差方向忽略前层干预改变了后层激活。
- **核心创新 / 方法** · 把候选方向视为优化梯度，按顺序结合干预后的新方向。
- **Baseline** · ActAdd、Directional Ablation、Angular Steering 是方法背景。
- **Benchmark** · 不同语言模型体系和行为控制基准，摘要未列名称。
- **关键结果 / 消融** · 作者报告控制更强、更稳健且可与其他方法组合。
- **适用条件 / 局限** · 摘要未报告跨层计量成本和副作用。

**可复用机制** · 在多层控制中按干预后的真实表征重估局部方向，避免直接叠加未干预模型的静态修正。

<a id="paper-149886"></a>

## Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison

[官方论文页](https://neurips.cc/virtual/2026/poster/149886) · [作者来源](https://openreview.net/forum?id=mUKb5eCadx)

- **问题 / 瓶颈** · 跨视角补全在非共视区域退化为单目学习。
- **核心创新 / 方法** · 同时训练跨视角补全、掩码自编码和逐像素相对误差改善预测。
- **Baseline** · 相同架构和数据下的 CroCo。
- **Benchmark** · 零样本匹配、相对位姿、点图回归及从原始视频训练。
- **关键结果 / 消融** · 各任务一致优于 CroCo，原始视频训练匹配精选数据模型表现。
- **适用条件 / 局限** · 相对误差只代理共视，摘要没给对遮挡噪声的分析。

**可复用机制** · 对比有无辅助观测的预测误差，可从数据自身提取何处额外视角真正有用。

<a id="paper-153192"></a>

## Revisiting Diffusion Model Predictions Through Dimensionality

[官方论文页](https://neurips.cc/virtual/2026/poster/153192) · [作者来源](https://openreview.net/forum?id=NAHtkZBZqR)

- **问题 / 瓶颈** · 固定预测数据、噪声或速度难适配数据几何。
- **核心创新 / 方法** · 把预测目标统一为干净数据和噪声的连续线性组合，用 k-Diff 从数据学系数。
- **Baseline** · 固定的数据、噪声和速度预测目标。
- **Benchmark** · 像素和潜空间图像生成，不同模型和数据尺度。
- **关键结果 / 消融** · 作者报告一致优于固定目标，理论解释高外在维数相对内在维数时直接数据预测的优势。
- **适用条件 / 局限** · 内在维数难测，文中用学习代替测量，摘要无系数敏感性。

**可复用机制** · 选择生成训练目标时，把表征几何当成变量，允许优化目标在常见端点之间移动。

<a id="paper-157015"></a>

## Revisiting "Edit Away and My Face Will not Stay: Personal Biometric Defense against Malicious Generative Editing"

[官方论文页](https://neurips.cc/virtual/2026/poster/157015) · [作者来源](https://openreview.net/forum?id=5Q1gr80AXU)

- **问题 / 瓶颈** · 提示符合度不足以代表防御是否成功，挑选少量图例也可能误导。
- **核心创新 / 方法** · 在更多图像和提示组合上复现并比较保护质量。
- **Baseline** · 原 FaceLock 报告及其基线。
- **Benchmark** · 扩展图像与编辑提示组合和更难的人脸数据，考察复现趋势与原图质量。
- **关键结果 / 消融** · 作者未复现原趋势，只有少部分输出接近示例质量。
- **适用条件 / 局限** · 摘要未报告独立量化的保护和保真边界。

**可复用机制** · 对保护与效用冲突的系统报告联合结果，检验原输入可用且预期保护仍成立。

<a id="paper-156114"></a>

## Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/156114) · [作者来源](https://openreview.net/forum?id=0Hg7gv5gwK)

- **问题 / 瓶颈** · 高层语义描述难以约束执行，逐词推理容易累积错误
- **核心创新 / 方法** · 在训练中放入末端运动和图像轨迹等具体语言指导，部署不生成完整推理链
- **Baseline** · 高层推理监督及具竞争力的 VLA 基线
- **Benchmark** · LIBERO-Plus、VLABench 和真实机器人
- **关键结果 / 消融** · 成功率分别 86.9% 和 53.2%，实机语义歧义及长任务也改善
- **适用条件 / 局限** · 依赖大量具体动作监督，生态外硬件需重测

**可复用机制** · 消融训练推理监督与测试推理链，避免将两者收益混为一谈

<a id="paper-150119"></a>

## Revisiting Incremental Learning: A Three-Interface Diagnosis of Stability and Plasticity

[官方论文页](https://neurips.cc/virtual/2026/poster/150119) · [作者来源](https://openreview.net/forum?id=kX9Kbog4s6)

- **问题 / 瓶颈** · 旧任务精度下降常被直接归因于骨干遗忘
- **核心创新 / 方法** · 从多个接口诊断，再冻结骨干只调头检查可恢复量
- **Baseline** · 常规增量性能和头重对齐性能
- **Benchmark** · 增量模型、三个聚类度量、JLT
- **关键结果 / 消融** · 头重对齐后恢复量较大，表征仍有部分漂移
- **适用条件 / 局限** · 需要能用于头校准的样本

**可复用机制** · 报告冻结表征可恢复性能并保留全模型基线

<a id="paper-150610"></a>

## Revisiting the Adam–SGD Gap Beyond Single Factors

[官方论文页](https://neurips.cc/virtual/2026/poster/150610) · [作者来源](https://openreview.net/forum?id=gs38iA3FeE)

- **问题 / 瓶颈** · 单因素假说不能解释相反的相对排序
- **核心创新 / 方法** · 交叉改变词表频率、注意与激活，查批大小交叉点
- **Baseline** · Adam、SGD
- **Benchmark** · 多种受控数据架构条件，摘要未列完整基准
- **关键结果 / 消融** · 优势随分布和架构可消退或反转，批量增大可由 SGD 领先转为 Adam 领先
- **适用条件 / 局限** · 交叉点数值不能从摘要泛化

**可复用机制** · 在目标资源预算用至少两档批量联合选优化器

<a id="paper-151129"></a>

## Reviving the Discarded High-Resolution Feature for Transformer-Based Tiny Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151129) · [作者来源](https://openreview.net/forum?id=cmZXkyWcad)

- **问题 / 瓶颈** · 只看深层语义会丢失细小边界
- **核心创新 / 方法** · 恢复细粒度特征并允许查询同时访问局部细节和高层语义
- **Baseline** · 多种 DETR 骨干原配置
- **Benchmark** · AI-TOD-v2、VisDrone、SODA-D；AP
- **关键结果 / 消融** · 最佳变体分别增 1.4、1.6、1.5 AP
- **适用条件 / 局限** · 分辨率开销和跨任务收益未在摘要量化

**可复用机制** · 按目标尺寸分桶验收高分特征支路

<a id="paper-152372"></a>

## ReVMap: Vectorized Global Mapping via Connectivity-Aware Local Map Fusion

[官方论文页](https://neurips.cc/virtual/2026/poster/152372) · [作者来源](https://openreview.net/forum?id=TZ6rQlj9GO)

- **问题 / 瓶颈** · 局部定位误差会累积并造成连接错误
- **核心创新 / 方法** · 为局部矢量估不确定性，估连接并允许后续更新融合
- **Baseline** · 既有全局地图与局部预测方法，摘要未列名称
- **Benchmark** · nuScenes、Argoverse2；mGAP、miECM、局部 mAP
- **关键结果 / 消融** · nuScenes 三项为 36.1、43.4、58.0，Argoverse2 为 62.1、62.5、77.0
- **适用条件 / 局限** · 依赖局部定位可靠性和数据采样覆盖

**可复用机制** · 导航地图尽量允许后见观测修改早期不确定连边

<a id="paper-154792"></a>

## Reward Bias Substitution: Single-Axis Bias Mitigations Redirect Optimization Pressure

[官方论文页](https://neurips.cc/virtual/2026/poster/154792) · [作者来源](https://openreview.net/forum?id=Auv9cgHOSa)

- **问题 / 瓶颈** · 压低一个代理相关性可能把优化压力迁到另一轴
- **核心创新 / 方法** · 分离审核分布和优化分布，检查代理联动及条件相关
- **Baseline** · 已发表单轴去偏方法
- **Benchmark** · 四奖励模型、八模型族的人与模型判分偏差
- **关键结果 / 消融** · 三款模型 pooled 长度相关归零却在 prompt 内反向，两款真实奖励退化
- **适用条件 / 局限** · 依赖真实奖励和代理特征的可测程度

**可复用机制** · 给每个奖励更新配条件去偏与跨轴的回归检查

<a id="paper-152882"></a>

## Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/152882) · [作者来源](https://openreview.net/forum?id=PgTu2nTEh7)

- **问题 / 瓶颈** · 奖励随已熟练问题上正确样本数增长会加速锐化
- **核心创新 / 方法** · 将各 prompt 的固定预算分给正确轨迹
- **Baseline** · 常见推理 RL 及熵保持思路
- **Benchmark** · Qwen3-8B、Llama3.2-3B；AMC23、AIME24/25
- **关键结果 / 消融** · 最高分别增 12.50 和 10.00
- **适用条件 / 局限** · 依赖可靠正确性判定，初期无正确样本未获奖励

**可复用机制** · 按问题控制梯度集中度，分别监控学会概率与熵

<a id="paper-151928"></a>

## Reward-Conditioned Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151928) · [作者来源](https://openreview.net/forum?id=WpXOM0WTKa)

- **问题 / 瓶颈** · 固定奖励的策略难根据新偏好调整
- **核心创新 / 方法** · 给策略输入奖励参数，从名义交互中反事实重算多种奖励
- **Baseline** · 固定奖励及单任务策略
- **Benchmark** · 单任务、多任务和视觉设置；样本效率和零样本调整
- **关键结果 / 消融** · 名义目标效率与新参数适应均改善，数值未报告
- **适用条件 / 局限** · 必须能以共享轨迹重算目标奖励，未覆盖动作可达性变化

**可复用机制** · 拟定控制偏好参数后，先检查离线轨迹能否支持重标

<a id="paper-148702"></a>

## RewardFlow: Topology-Aware Reward Propagation on State Graphs  for Agentic RL with LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148702) · [作者来源](https://openreview.net/forum?id=vgqdqXYwsC)

- **问题 / 瓶颈** · 终局稀疏且逐轨迹分配忽略状态拓扑
- **核心创新 / 方法** · 归并轨迹状态并在图上传播终局信息
- **Baseline** · 各类智能体 RL 与最强基线
- **Benchmark** · 四智能体基准及 DeepResearch；成功率与准确率
- **关键结果 / 消融** · 摘要报告文本平均增 6.2%、视觉推理增 29.7%
- **适用条件 / 局限** · 依赖状态归并有效、结果奖励可靠

**可复用机制** · 把同一状态在多次轨迹中的后果作为密集信用校验

<a id="paper-148947"></a>

## Reward-free Pretraining for Reinforcement Learning via Occupancy Coverage Maximization

[官方论文页](https://neurips.cc/virtual/2026/poster/148947) · [作者来源](https://openreview.net/forum?id=tzOD9WpnO4)

- **问题 / 瓶颈** · 探索新区域可能造成已覆盖区域反复丢失
- **核心创新 / 方法** · 学习 resolvent 占用模型，加虚拟吸收态平衡已知状态覆盖与未知探索
- **Baseline** · 常见无奖励预训练方法
- **Benchmark** · 表格和像素稀疏导航；覆盖与下游初始化
- **关键结果 / 消融** · 更均匀覆盖且下游初始化更强
- **适用条件 / 局限** · 依赖占用预测，复杂真实场景未报告

**可复用机制** · 探索策略同时测覆盖广度和旧区域覆盖留存

<a id="paper-154025"></a>

## Reward Hacking in Rubric-Based Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154025) · [作者来源](https://openreview.net/forum?id=Gor618iz3H)

- **问题 / 瓶颈** · 代理奖励上升可能不代表整体质量上升。
- **核心创新 / 方法** · 用跨家族评委和无量表评价拆分误差，辅以策略对数概率诊断。
- **Baseline** · 弱与强训练验证器。
- **Benchmark** · 科学及医疗开放任务。
- **关键结果 / 消融** · 强验证减轻验证器被优化偏离，规则遗漏仍影响整体质量。
- **适用条件 / 局限** · 裁判比较仍非人类金标准。

**可复用机制** · 将训练评分、参考评分及总体质量分别画随训练变化的曲线。

<a id="paper-149798"></a>

## Reward Inflation: A Healthy Stimulus for Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149798) · [作者来源](https://openreview.net/forum?id=nGl0OxizaX)

- **问题 / 瓶颈** · 固定奖励可能使梯度衰减。
- **核心创新 / 方法** · 逐步放大奖励，另加自适应 Fed 调控制。
- **Baseline** · 固定奖励、固定膨胀。
- **Benchmark** · ALE、MuJoCo。
- **关键结果 / 消融** · 适度放大改善多任务并保护可塑性，自适应往往更好。
- **适用条件 / 局限** · 过强放大、值归一化互动及稳定性需实测。

**可复用机制** · 把奖励尺度当可塑性控制而非只看起始梯度。

<a id="paper-150638"></a>

## Reward Is Not a Universal Interface for Generative Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150638) · [作者来源](https://openreview.net/forum?id=gbYg6VGblU)

- **问题 / 瓶颈** · 统一奖励接口忽略采样因子化和可计算性。
- **核心创新 / 方法** · 按分支评分，按平滑、漂移等约束选剪切、锚和块预算。
- **Baseline** · 共享原始奖励输入方案。
- **Benchmark** · 自回归、离散并行、流扩散及混合模型。
- **关键结果 / 消融** · 改善质量或奖励风险权衡。
- **适用条件 / 局限** · 控制因素多，部署时须独立消融。

**可复用机制** · 同一任务目标下仍为异质生成分支分别控制更新几何。

<a id="paper-155004"></a>

## Reward Modeling for Multi-Agent Orchestration

[官方论文页](https://neurips.cc/virtual/2026/poster/155004) · [作者来源](https://openreview.net/forum?id=9HnmEMnWjg)

- **问题 / 瓶颈** · 需要重复运行子代理才能评价编排。
- **核心创新 / 方法** · 用执行中间产物造胜负对并训练 Bradley–Terry 奖励。
- **Baseline** · 依赖昂贵子代理 rollout 的方案。
- **Benchmark** · 数学、网页问答、多跳推理。
- **关键结果 / 消融** · 训练 token 效率最高 10 倍，测试时扩展准确率最高改善 8%。
- **适用条件 / 局限** · 依赖中间产物与真实成功的关系。

**可复用机制** · 把编排质量当超出最终答案的独立监督层。

<a id="paper-155927"></a>

## Reward Score Matching: Unifying Reward-based Fine-tuning for Flow and Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155927) · [作者来源](https://openreview.net/forum?id=1kkqc5AcDy)

- **问题 / 瓶颈** · 算法外观不同导致难确定核心组件。
- **核心创新 / 方法** · 以价值引导目标的 score matching 统一多种方法。
- **Baseline** · 既有流与扩散的奖励微调。
- **Benchmark** · 可微和黑盒奖励对齐。
- **关键结果 / 消融** · 据此设计更简洁方案，摘要未报告幅度。
- **适用条件 / 局限** · 等价只覆盖可写为该形式的方法。

**可复用机制** · 对齐方法消融优先控制估计器、时间权重及预算。

<a id="paper-150900"></a>

## Reward Shaping to Improve Language Model Query Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150900) · [作者来源](https://openreview.net/forum?id=ea5xEo2hw1)

- **问题 / 瓶颈** · 稀疏序列奖励采样效率差。
- **核心创新 / 方法** · 学习密集 token 奖励并用单循环优化。
- **Baseline** · 基于序列奖励的查询生成。
- **Benchmark** · 语言模型查询正确性。
- **关键结果 / 消融** · 给出次线性收敛，摘要报告优于基线。
- **适用条件 / 局限** · 学习密集奖励需验证是否保留语义正确性。

**可复用机制** · 训练外部查询工具时可单独量化密集反馈的增益。

<a id="paper-151660"></a>

## Reweighted Flow Matching via Unbalanced Optimal Transport for Label-free Long-tailed Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/151660) · [作者来源](https://openreview.net/forum?id=Z0OhxD9sBT)

- **问题 / 瓶颈** · 训练分布头部压制少数概念。
- **核心创新 / 方法** · 将 UOT 权重加入流匹配，比较不同阶校正。
- **Baseline** · 标准流匹配。
- **Benchmark** · 无标签长尾生成。
- **关键结果 / 消融** · 一阶理论恢复目标分布，高阶实证更护尾部。
- **适用条件 / 局限** · 目标分布和运输估计条件需检查。

**可复用机制** · 不能用类别计数时从匹配质量估可迁移重采权重。

<a id="paper-152119"></a>

## RGF: Recursive Generative Framework for the Edge-Cut Separable Problems

[官方论文页](https://neurips.cc/virtual/2026/poster/152119) · [作者来源](https://openreview.net/forum?id=VOCORbL6JY)

- **问题 / 瓶颈** · 全图联合解规模大。
- **核心创新 / 方法** · 利用边割分离性质递归生成和条件分解。
- **Baseline** · 最强 ML 近似法。
- **Benchmark** · 真实图最高 1100 万节点。
- **关键结果 / 消融** · 最高改善 2.13%，可处理所测千万节点图。
- **适用条件 / 局限** · 依赖割后条件独立性。

**可复用机制** · 任务分解前先锁定耦合变量，而非独立解完才拼接。

<a id="paper-155169"></a>

## R-GRec: Relation-Guided Generative Recommendation via Collaborative Graph Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/155169) · [作者来源](https://openreview.net/forum?id=7mugzY6bNM)

- **问题 / 瓶颈** · 只按下一项学难见类间拓扑。
- **核心创新 / 方法** · 辅助做邻居预测、拓扑对比及链接预测。
- **Baseline** · 传统、生成式及大模型推荐。
- **Benchmark** · 两个 Amazon 数据集。
- **关键结果 / 消融** · 两数据集领先且消融支持辅助项，无推理图成本。
- **适用条件 / 局限** · 图来自交互，有曝光偏。

**可复用机制** · 训练时把结构旁信号放进轻目标，部署保持序列接口。

<a id="paper-152884"></a>

## RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding

[官方论文页](https://neurips.cc/virtual/2026/poster/152884) · [作者来源](https://openreview.net/forum?id=PgNNLmDUZe)

- **问题 / 瓶颈** · 确定 top-k 能造好树却让草稿概率退化。
- **核心创新 / 方法** · 采样 token 用代理概率铺树、以真实概率校验。
- **Baseline** · EAGLE-3 等动态树。
- **Benchmark** · 多 LLM、多个生成基准。
- **关键结果 / 消融** · 接受率和加速比持续改善。
- **适用条件 / 局限** · 正确性依赖校验保持目标分布。

**可复用机制** · 同一候选可有独立的搜索优先级与最终接受权重。

<a id="paper-155818"></a>

## RICE-PO: Turning Retrieval Interactions into Credit Signals for Reasoning Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/155818) · [作者来源](https://openreview.net/forum?id=2fIYREq48r)

- **问题 / 瓶颈** · 内在步骤本身没有外部评分。
- **核心创新 / 方法** · 对高不确定查询做局部分支，用外部检索指标，并门控回传。
- **Baseline** · 终局奖励与一般策略优化。
- **Benchmark** · 推理检索代理。
- **关键结果 / 消融** · 摘要支持从工具反馈获得有效监督，幅度未报告。
- **适用条件 / 局限** · 工具指标和最终用户目标可能不一致。

**可复用机制** · 以可执行动作作反事实锚点，再决定是否给相邻思考步骤信用。

<a id="paper-153492"></a>

## Richer or More Gates? Fan-In Trade-offs in Learnable Logic Circuits

[官方论文页](https://neurips.cc/virtual/2026/poster/153492) · [作者来源](https://openreview.net/forum?id=KzXBuboGel)

- **问题 / 瓶颈** · 提高扇入指数挤占宽度。
- **核心创新 / 方法** · 比 sigmoid 和 softmax 选择机制，并分析雅可比。
- **Baseline** · 固定预算的不同扇入与选择机制。
- **Benchmark** · 28 任务和五真实数据集。
- **关键结果 / 消融** · 图像偏宽度，奇偶和算术偏高扇入；最优选择机制随任务反转。
- **适用条件 / 局限** · 规律针对所测逻辑门网络。

**可复用机制** · 选表达结构时需在同架构下额外测优化可达性。

<a id="paper-138936"></a>

## Rich Insights from Cheap Signals: Efficient Evaluations via Tensor Factorization

[官方论文页](https://neurips.cc/virtual/2026/poster/138936) · [作者来源](https://openreview.net/forum?id=vQQlWAbobs)

- **问题 / 瓶颈** · 细分提示后人力不足且自动判分偏移。
- **核心创新 / 方法** · 将自动评分和人评用张量分解整合。
- **Baseline** · 自动单评分及聚合评估。
- **Benchmark** · 提示子集榜单和模型人评估计。
- **关键结果 / 消融** · 可从自动器估新模型的人评结果，摘要未给误差。
- **适用条件 / 局限** · 需要低秩共享结构；新领域或新裁判需复验。

**可复用机制** · 人工样本优先覆盖校准张量中的关键切片。

<a id="paper-155552"></a>

## Riemannian Admissibility Flow for Offline-to-Online Safe Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155552) · [作者来源](https://openreview.net/forum?id=4hjf2AG9Vo)

- **问题 / 瓶颈** · 评价改进切换导致初始性能崩落。
- **核心创新 / 方法** · 在各向异性黎曼流形上约束概率运输。
- **Baseline** · 安全离线到在线方法。
- **Benchmark** · 代表性安全 RL 基准，任务和约束。
- **关键结果 / 消融** · 约束与任务表现具竞争力，缓和初始崩溃。
- **适用条件 / 局限** · 依赖可构安全几何和覆盖可行行为。

**可复用机制** · 把明显不可行动作的更新成本写进概率移动几何。

<a id="paper-154402"></a>

## Riemannian Bilevel Optimization under the Polyak–Łojasiewicz Condition

[官方论文页](https://neurips.cc/virtual/2026/poster/154402) · [作者来源](https://openreview.net/forum?id=DqfoM1UJnq)

- **问题 / 瓶颈** · 直接逆 Hessian 在非强凸下失效。
- **核心创新 / 方法** · 内蕴谱裁剪避免求逆和内环反传。
- **Baseline** · Hessian 逆、Neumann 系列。
- **Benchmark** · BCI IV-2a、UCI、MiniImageNet，Stiefel 等。
- **关键结果 / 消融** · 线性误差机器精度，梯度范数下降，随机误差近 1/B。
- **适用条件 / 局限** · 需黎曼 PL 条件。

**可复用机制** · 约束双层训练先诊断低层谱，再选稳定超梯度。

<a id="paper-155509"></a>

## Riemannian Lyapunov Framework: Optimization as Closed-Loop Control on Riemannian Manifolds

[官方论文页](https://neurips.cc/virtual/2026/poster/155509) · [作者来源](https://openreview.net/forum?id=548NwQAdhQ)

- **问题 / 瓶颈** · 噪声下瞬时损失下降不足以描述稳定性。
- **核心创新 / 方法** · 把优化写成受控系统，反步构造 Lyapunov 并实例化。
- **Baseline** · 三个优化设计轴的对照。
- **Benchmark** · 几何诊断、图像分类和语言建模。
- **关键结果 / 消融** · 有界扰动下降对齐时给最终有界，实证匹配。
- **适用条件 / 局限** · 依赖下降对齐和噪声有界。

**可复用机制** · 用稳定域而非单步损失比较噪声和动量机制。

<a id="paper-150239"></a>

## Riemannian Optimization for Low-Rank Adaptation via Desingularization

[官方论文页](https://neurips.cc/virtual/2026/poster/150239) · [作者来源](https://openreview.net/forum?id=jiYYPiWmCI)

- **问题 / 瓶颈** · 低秩约束含奇异点影响优化。
- **核心创新 / 方法** · 引入左右零空间投影做去奇异化。
- **Baseline** · 其他 PEFT。
- **Benchmark** · 多实验设置。
- **关键结果 / 消融** · 摘要称优于比较方法，幅度未报告。
- **适用条件 / 局限** · 计算与显存成本需配合具体秩和模型衡量。

**可复用机制** · 低秩学习可先改优化坐标而不改部署的低秩接口。

<a id="paper-154640"></a>

## RIFLE: Removal of Image Flicker-Banding via Latent Diffusion Enhancement

[官方论文页](https://neurips.cc/virtual/2026/poster/154640) · [作者来源](https://openreview.net/forum?id=C6YQkpxLpr)

- **问题 / 瓶颈** · 全局增强会损坏未受影响细节。
- **核心创新 / 方法** · 结构门控高频先验经 FiLM 注入，掩码损失集中到条纹。
- **Baseline** · 一般恢复方法。
- **Benchmark** · 配对真实频闪数据，长曝光作参考。
- **关键结果 / 消融** · 摘要报告细节恢复，效果幅度待核。
- **适用条件 / 局限** · 需可定位受损区；长曝光参考受运动影响。

**可复用机制** · 空间不均匀退化应分开约束修复强度与背景保真。

<a id="paper-148245"></a>

## Rigel3D: Rig-aware Latents for Animation-Ready 3D Asset Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/148245) · [作者来源](https://openreview.net/forum?id=zKGmCGx8bP)

- **问题 / 瓶颈** · 静态几何后装骨骼难让骨骼与几何匹配。
- **核心创新 / 方法** · 用耦合的表面和骨架潜表示生成绑定网格，以视觉语言嵌入标记关节。
- **Baseline** · 后置自动绑定方法。
- **Benchmark** · 大规模绑定资产，摘要未列数据和指标。
- **关键结果 / 消融** · 作者报告多指标优于现有绑定基线。
- **适用条件 / 局限** · 依赖绑定资产训练数据，摘要未给重定向成功率。

**可复用机制** · 把下游运动结构作为生成对象的一部分，而不是事后拟合到已生成形状。

<a id="paper-139732"></a>

## Right Results, Wrong Reasons: Auditing Behavioral Reliance in Motion Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/139732) · [作者来源](https://openreview.net/forum?id=7axaNwvSMD)

- **问题 / 瓶颈** · 轨迹误差不能回答预测具体依赖哪些周边代理。
- **核心创新 / 方法** · 逐一去除代理并测轨迹响应，将响应排序与人工因果标记和注意力对照。
- **Baseline** · 常用轨迹指标、注意力排序。
- **Benchmark** · Argoverse 2 和 Waymo Open Motion Dataset，五种不同架构。
- **关键结果 / 消融** · 作者报告当前精度评估不足以支持依赖性结论。
- **适用条件 / 局限** · 移除后的虚拟场景可能发生分布变化，摘要未给具体效应量。

**可复用机制** · 多对象预测的测评可增加输入级干预，分开检查预测准确性和依赖对象是否合理。

<a id="paper-152768"></a>

## RigidFormer: Learning Rigid Dynamics using Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/152768) · [作者来源](https://openreview.net/forum?id=QWRZoUcNGH)

- **问题 / 瓶颈** · 顶点消息传递依赖网格且长期接触误差会累积。
- **核心创新 / 方法** · 以物体中心 Transformer 处理点输入，借助可微 Kabsch 对齐回到刚体流形。
- **Baseline** · 基于网格的模拟方法。
- **Benchmark** · 刚体标准基准、不同点分辨率和跨数据集测试。
- **关键结果 / 消融** · 摘要报告更快，表现匹配或优于网格基线，可扩展到 200 多物体。
- **适用条件 / 局限** · 关节体扩展仍属初步，摘要未报告误差数值。

**可复用机制** · 对带明确约束的连续模拟，可以先推断更新，再用可微投影保证其符合所需状态结构。

<a id="paper-152889"></a>

## RigRecon: Efficient Rig-Aware Street Reconstruction via Dual-Path Spatio-Temporal Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/152889) · [作者来源](https://openreview.net/forum?id=PdpQ8Gxwy0)

- **问题 / 瓶颈** · 全局高分辨率注意力占用大，序列分块则要对齐尺度。
- **核心创新 / 方法** · 让低分辨率骨干利用标定融合多视角，再异步解码逐帧深度。
- **Baseline** · 全局注意力重建与分块对齐。
- **Benchmark** · 街景多相机的重建、深度和位姿估计。
- **关键结果 / 消融** · 作者报告以上任务达先进表现，并可单次前向处理超过 1000 张图像。
- **适用条件 / 局限** · 依赖相机标定，摘要未给分辨率和显存绝对量。

**可复用机制** · 跨观测共享的粗结构可用低分辨率推断，局部细节按需恢复。

<a id="paper-150906"></a>

## Ripple in Still Water: Zero-Shot Clustering in Heterogeneous Federated Learning with Wavelet Scattering Transform

[官方论文页](https://neurips.cc/virtual/2026/poster/150906) · [作者来源](https://openreview.net/forum?id=eXBYzZS6sZ)

- **问题 / 瓶颈** · 训练期按梯度聚类增加通信且难处理新客户端。
- **核心创新 / 方法** · 以数据小波散射谱表示做离线分组，再用簇专用训练。
- **Baseline** · 根据梯度、损失或迭代分簇的联邦方法。
- **Benchmark** · 五个受控和真实异质性基准。
- **关键结果 / 消融** · 摘要报告一致优于基线，且更真实划分差距更大。
- **适用条件 / 局限** · 依赖谱签名反映相关域差异，摘要未给分组误差和开销。

**可复用机制** · 客户端异质性可由训练前数据特征刻画时，分开设计域分组和优化器。

<a id="paper-153544"></a>

## RiSE: Residual Subspace Expert for Generalizable Text-Centric Image Forgery Localization

[官方论文页](https://neurips.cc/virtual/2026/poster/153544) · [作者来源](https://openreview.net/forum?id=KaKH1k0VkJ)

- **问题 / 瓶颈** · 全量更新可能引起低秩特征塌缩，单表示混合不同类别伪造痕迹。
- **核心创新 / 方法** · 在保留预训练表征的基础上学习专用残差子空间及专家选择。
- **Baseline** · 全量微调和既有文本图像篡改定位方法。
- **Benchmark** · 合成训练到真实篡改图像测试，摘要未列具体指标。
- **关键结果 / 消融** · 单专家提升 20.4% 且训练步少十倍，九专家报告提升 35.8%。
- **适用条件 / 局限** · 摘要未给归一化指标，适用性来自所测篡改任务。

**可复用机制** · 抗伪造检测应检查域外泛化，必要时用部分可训练残差保留通用视觉底座。

<a id="paper-139505"></a>

## RISE-Video: Can Video Generators Decode Implicit World Rules?

[官方论文页](https://neurips.cc/virtual/2026/poster/139505) · [作者来源](https://openreview.net/forum?id=LriqPuIS7K)

- **问题 / 瓶颈** · 外观逼真不足以说明模型遵守时间、空间和常识约束。
- **核心创新 / 方法** · 将隐式规则任务按类别人工标注，并使用多模态评审辅助检查。
- **Baseline** · 11 个文本图像到视频系统。
- **Benchmark** · 467 个样本、八类，评估规则推理、合理性及视觉质量。
- **关键结果 / 消融** · 摘要报告多个生成器在复杂隐式约束下普遍不足。
- **适用条件 / 局限** · 自动评审的人类一致性和类别分数未报告。

**可复用机制** · 把需要满足的世界约束写成单独观察项目，避免高视觉保真掩盖规则失败。

<a id="paper-148872"></a>

## Risk-Averse Online POMDP Planning via CVaR of the Immediate Cost with Performance Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/148872) · [作者来源](https://openreview.net/forum?id=uYhSEnNKIx)

- **问题 / 瓶颈** · 轨迹级风险目标可能掩盖信念内少量高代价状态。
- **核心创新 / 方法** · 对即时成本施加 CVaR，保留标准期望规划，并分析粒子近似误差。
- **Baseline** · 期望成本规划和价值函数层面的 CVaR。
- **Benchmark** · POMDP 理论分析及稀疏采样，摘要未列实证任务。
- **关键结果 / 消融** · 得到粒子代理到原 POMDP 的有限时误差界，风险中性时恢复标准规划。
- **适用条件 / 局限** · 覆盖信念内风险，依赖粒子近似和所给假设。

**可复用机制** · 感知歧义本身有风险时，可先在决策步内聚合危险尾部，再使用现成规划器。

<a id="paper-154864"></a>

## Risk-Aware Action Repetition via Expected Skip Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/154864) · [作者来源](https://openreview.net/forum?id=AJOzqhWj2Q)

- **问题 / 瓶颈** · 未成熟代理在重复后无法立即做最优控制，贪心自举放大乐观误差。
- **核心创新 / 方法** · 用正则控制下的预期后续价值评价动作持续时长。
- **Baseline** · 终止状态用贪心价值自举的 Skip-MDP。
- **Benchmark** · 格子世界、连续控制和安全相关基准。
- **关键结果 / 消融** · 作者报告更高样本效率及更校准的跳步。
- **适用条件 / 局限** · 摘要未给持续时长、样本改善和额外成本。

**可复用机制** · 评估延长开环动作前，后续价值应先匹配部署或训练时真正会执行的策略。

<a id="paper-154212"></a>

## Risk-Calibrated Context Selection for Healthcare Multi-Agent Handoff

[官方论文页](https://neurips.cc/virtual/2026/poster/154212) · [作者来源](https://openreview.net/forum?id=FLlWDrOo4c)

- **问题 / 瓶颈** · 仅优化相关性可能泄露接收者无权接触的信息。
- **核心创新 / 方法** · 契约遮盖越权条目，之后用带暴露成本和成功风险上界的子集选择。
- **Baseline** · LLM 作为选择器等方法。
- **Benchmark** · 合成交接、角色变化和 Claude Sonnet 4.5 的真实模型运行。
- **关键结果 / 消融** · 作者报告只有该方法在竞争性成功率下达到 α=0.15，真实模型出现校准迁移差距。
- **适用条件 / 局限** · 依赖契约正确，并可能需按工作流重新校准。

**可复用机制** · 将授权约束放在选择器之前执行，性能风险统计只作用于已经许可的候选。

<a id="paper-154732"></a>

## Risk-Controlled Post-Processing of Decision Policies

[官方论文页](https://neurips.cc/virtual/2026/poster/154732) · [作者来源](https://openreview.net/forum?id=BRnQhDXD2y)

- **问题 / 瓶颈** · 随机混合会为达到整体预算而不必要地改动原决策。
- **核心创新 / 方法** · 在交换性下校准基于条件风险降低的阈值。
- **Baseline** · 原策略及不看分数的随机混合。
- **Benchmark** · COVID-19 胸片诊断、LLM 路由与合成分类。
- **关键结果 / 消融** · 达到或接近风险预算时，保留更多原策略决策。
- **适用条件 / 局限** · 需要后备策略和相应校准数据，摘要未报告分布偏移保证。

**可复用机制** · 策略升级把风险下降作为干预分数，避免为整体合规而无差别切换。

<a id="paper-153521"></a>

## RL Excursions during Pre-training: How early is too early for on-policy learning?

[官方论文页](https://neurips.cc/virtual/2026/poster/153521) · [作者来源](https://openreview.net/forum?id=KjrYAUhYam)

- **问题 / 瓶颈** · 将后训练锐化现象外推到早期学习可能误判
- **核心创新 / 方法** · 对照插入 RL 的时序，并对两目标更新作并行平均
- **Baseline** · 先 SFT、先 RL 及其他组合
- **Benchmark** · 训练阶段、专项和通用能力，具体基准未报告
- **关键结果 / 消融** · 摘要称仅 SFT 后 RL 表现出既有锐化，并行平均整体领先
- **适用条件 / 局限** · 早期检查点与具体奖励设置限制外推

**可复用机制** · 要保留通用能力时在早期检查点对照 RL 与 SFT 的次序

<a id="paper-152090"></a>

## RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory

[官方论文页](https://neurips.cc/virtual/2026/poster/152090) · [作者来源](https://openreview.net/forum?id=VaEouLMkHw)

- **问题 / 瓶颈** · 相似事件往往只在发生时间上有区别
- **核心创新 / 方法** · 小模型定位时间证据，与语义检索双通道联合
- **Baseline** · 现有长期记忆方法
- **Benchmark** · LifeBench、LoCoMo；准确率
- **关键结果 / 消融** · 分别 61.52% 与 78.96%，摘要报告提升 8.82% 和 3.66%
- **适用条件 / 局限** · 时间线不全或事件时间含糊时会退化

**可复用机制** · 为重复事件按时间窗显式索引，并与纯向量检索对照

<a id="paper-152424"></a>

## RL-Inf: Tracking Non-local Training Data Influence for Online Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152424) · [作者来源](https://openreview.net/forum?id=TDeuf94Klk)

- **问题 / 瓶颈** · 一次更新的局部作用遗漏后续策略分布变化
- **核心创新 / 方法** · 将非局部数据影响用于在线样本筛选
- **Baseline** · PPO 和局部归因
- **Benchmark** · 标准控制及 RLHF 毒性缓解
- **关键结果 / 消融** · 摘要称训练效率和最终性能改善，未列数值
- **适用条件 / 局限** · 非局部影响估计的误差与额外成本需核查

**可复用机制** · 比较短期梯度收益与长期经验分布变化后再筛数据

<a id="paper-139631"></a>

## RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades

[官方论文页](https://neurips.cc/virtual/2026/poster/139631) · [作者来源](https://openreview.net/forum?id=ENBv2lHkyZ)

- **问题 / 瓶颈** · 短缺陷修复不能代表跨文件长任务
- **核心创新 / 方法** · 用已知版本升级构建任务，检查目标功能是否实现
- **Baseline** · 13 个前沿模型及既有修复基准
- **Benchmark** · 典型改动约 3700 行、51 文件，指标为任务解决率
- **关键结果 / 消融** · 最强 39.1%，最低 5.2%
- **适用条件 / 局限** · 代码规模和公开版本任务可能引入先验，需防泄漏

**可复用机制** · 验收长程编码时加入多模块升级并检查实际功能

<a id="paper-154097"></a>

## RoboExo: Structure-Guided Wrist-to-Exocentric Video Generation for Scalable Robot Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/154097) · [作者来源](https://openreview.net/forum?id=GHEHItQouU)

- **问题 / 瓶颈** · 单视角采集限制感知覆盖
- **核心创新 / 方法** · 用结构引导从腕部视频生成外部视角
- **Baseline** · 现有腕部到外部视角生成方法
- **Benchmark** · 已见及未见生成设置；LPIPS、FVD 和六机器人任务
- **关键结果 / 消融** · LPIPS 降 76%、FVD 降 64%，平均策略成功率报告提升 30%
- **适用条件 / 局限** · 生成视图可能改变接触等关键几何，需实机重验

**可复用机制** · 评估合成视图时将视觉保真与策略成功分开

<a id="paper-139850"></a>

## RoboWits: Unexpected Challenges for Robotic Creative Problem Solving

[官方论文页](https://neurips.cc/virtual/2026/poster/139850) · [作者来源](https://openreview.net/forum?id=0dyy3qodV0)

- **问题 / 瓶颈** · 在原任务微调成功不能说明应变
- **核心创新 / 方法** · 从种子任务构造有物理意义的变体并加入 oracle 规划对照
- **Baseline** · 预训练 VLA、机器人策略及 oracle 状态规划器
- **Benchmark** · RoboWits 的种子与变体任务
- **关键结果 / 消融** · 微调 VLA 能做部分种子任务，却难处理变体
- **适用条件 / 局限** · 依赖所构造变体覆盖，摘要未报数值

**可复用机制** · 部署前测试工具失效或材料变化时能否更换方案

<a id="paper-151610"></a>

## Robust Amortized Simulation-Based Inference via Learned Error Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151610) · [作者来源](https://openreview.net/forum?id=ZGDfWRoYTN)

- **问题 / 瓶颈** · 有系统偏差时单拟合观测会污染参数后验
- **核心创新 / 方法** · 用重要性加权自编码框架联合估后验和显式误差
- **Baseline** · 此前鲁棒模拟推断方法
- **Benchmark** · 多个模型失配基准与指标，细目未报告
- **关键结果 / 消融** · 摘要报告均有改进
- **适用条件 / 局限** · 仿真偏差与参数影响的可辨识性要核验

**可复用机制** · 转移前先分辨传感误差、模拟不准与真实动力学参数

<a id="paper-154510"></a>

## Robust and Efficient Finetuning of Vision Foundation Models via Implicit Ensembling

[官方论文页](https://neurips.cc/virtual/2026/poster/154510) · [作者来源](https://openreview.net/forum?id=D3CvENdsfQ)

- **问题 / 瓶颈** · 直接全量调参容易过拟合且耗显存
- **核心创新 / 方法** · 借动态指数滑动快照做隐式集成，仅稀疏更新少量参数
- **Baseline** · Mixout、Model Soups 和 PEFT
- **Benchmark** · 五视觉基准，协变量漂移及类不平衡
- **关键结果 / 消融** · 摘要称双设置均优于对照，无推理开销
- **适用条件 / 局限** · 需要可用稀疏核，跨模型内存改善未量化

**可复用机制** · 端侧视觉适配验收漂移和长尾，不只看同分布

<a id="paper-152517"></a>

## Robust and Hard-to-Remove GNN Watermarking via Topological Invariant Perception

[官方论文页](https://neurips.cc/virtual/2026/poster/152517) · [作者来源](https://openreview.net/forum?id=SXZrjQXtkB)

- **问题 / 瓶颈** · 人工触发模式在模型调整后易失。
- **核心创新 / 方法** · 训练辅助标量头识别私有图的归一代数连通性。
- **Baseline** · 触发式与解释式水印。
- **Benchmark** · 多节点和图分类，任务精度与溯源忠实度。
- **关键结果 / 消融** · 保持任务精度，对剪枝微调量化仍有检测。
- **适用条件 / 局限** · 所有权依赖私有载体与检验可靠性，蒸馏场景需单测。

**可复用机制** · 优先嵌入架构本身能稳定预测的辅助信号，再独立验任务影响。

<a id="paper-149248"></a>

## Robust and Scalable Collaborative Learning via Pull-Based Epidemic Communication

[官方论文页](https://neurips.cc/virtual/2026/poster/149248) · [作者来源](https://openreview.net/forum?id=rmeEtbylhS)

- **问题 / 瓶颈** · 全互联消息成本过高，中心协调不总可用。
- **核心创新 / 方法** · 用 pull 式传播减少通信并保高概率收敛。
- **Baseline** · 全连接通信方案。
- **Benchmark** · 去中心学习的准确率、通信量和稳健性。
- **关键结果 / 消融** · 消息 O(n log n)，精度近全连接。
- **适用条件 / 局限** · 依赖随机抽样和网络模型。

**可复用机制** · 在资源受限的协作学习中同步报告稳健性与总消息。

<a id="paper-150072"></a>

## Robust Approximate Nearest Neighbor Search for Any Dataset

[官方论文页](https://neurips.cc/virtual/2026/poster/150072) · [作者来源](https://openreview.net/forum?id=kxeeWaxYv9)

- **问题 / 瓶颈** · 近邻索引内部随机性可能不支持依赖过去输出的查询。
- **核心创新 / 方法** · 用分桶化简和同心环带保持亚线性，同时采用稳健决策。
- **Baseline** · 经典 LSH、带数据密度前提的稳健方案。
- **Benchmark** · 支持 LSH 的度量空间，查询上界。
- **关键结果 / 消融** · 理论给无需数据结构前提的亚线性查询。
- **适用条件 / 局限** · 仍需度量支持 LSH，摘要未给线上成本。

**可复用机制** · RAG 代理迭代查询时把自适应性写入检索保证。

<a id="paper-154903"></a>

## Robust-by-Design Distributional Learning from Contaminated Samples

[官方论文页](https://neurips.cc/virtual/2026/poster/154903) · [作者来源](https://openreview.net/forum?id=A4wtdukFKi)

- **问题 / 瓶颈** · 带噪成员分数直接训练生成器会拟合杂质。
- **核心创新 / 方法** · 将代理得分和审计残差融合，校正 MMD 核和。
- **Baseline** · 干净 oracle MMD、未校正估计。
- **Benchmark** · 污染回归、混合分布生成。
- **关键结果 / 消融** · 证明设计无偏性及一致性，实验趋近 oracle 并恢复干净分布。
- **适用条件 / 局限** · 要求设计明确的精确审计子集。

**可复用机制** · 预算有限时把人工核验用于目标中的偏差校正。

<a id="paper-148206"></a>

## Robust Concept Unlearning in Diffusion Models via Directional Stability Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/148206) · [作者来源](https://openreview.net/forum?id=zZK5DA5niu)

- **问题 / 瓶颈** · 名义擦除仍可能在条件变化后恢复。
- **核心创新 / 方法** · 对欲擦除概念的局部扩张施正则，减少对无关方向影响。
- **Baseline** · 现有擦除法。
- **Benchmark** · 多种擦除设置，恢复率及画质与提示对齐。
- **关键结果 / 消融** · 降低恢复同时大体保画质。
- **适用条件 / 局限** · 需可靠目标方向定义及防御性压力测试。

**可复用机制** · 局部编辑后应检查邻域内目标属性是否仍被稳定抑制。

<a id="paper-149585"></a>

## Robust Conditional Conformal Prediction via Branched Normalizing Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/149585) · [作者来源](https://openreview.net/forum?id=p0L1xLc9E7)

- **问题 / 瓶颈** · 边际覆盖可能隐藏条件失准。
- **核心创新 / 方法** · 双支可逆流分别匹配输入与输出集合。
- **Baseline** · 常规条件共形预测。
- **Benchmark** · 九数据集，多置信度下条件覆盖。
- **关键结果 / 消融** · 条件覆盖更稳，量化待核。
- **适用条件 / 局限** · 可逆运输的匹配精度决定效果。

**可复用机制** · 对输入和预测集合做一致坐标变化，而非仅重标置信。

<a id="paper-152633"></a>

## Robust Diffusion Models via Divergence-Induced Weighted Denoising

[官方论文页](https://neurips.cc/virtual/2026/poster/152633) · [作者来源](https://openreview.net/forum?id=RdBtgbn9Tb)

- **问题 / 瓶颈** · 平方残差易让污染样本支配训练。
- **核心创新 / 方法** · 用 f 散度导出的非线性权重调整去噪误差。
- **Baseline** · 普通 MSE 去噪。
- **Benchmark** · 污染下扩散训练与额外成本。
- **关键结果 / 消融** · 实证更稳，额外计算较小。
- **适用条件 / 局限** · 权重在稀有真实样本与污染间需校准。

**可复用机制** · 先区分大残差来自有效长尾还是异常，再采用鲁棒降权。

<a id="paper-154718"></a>

## Robust Domain Generalization under Divergent Marginal and Conditional Distributions

[官方论文页](https://neurips.cc/virtual/2026/poster/154718) · [作者来源](https://openreview.net/forum?id=BWnOtiERGq)

- **问题 / 瓶颈** · 只对齐特征可能使联合漂移界失效。
- **核心创新 / 方法** · 拆边际与条件风险项，特征单位归一并跨域元训练。
- **Baseline** · 常规域不变 DG。
- **Benchmark** · 标准 DG 和多域长尾识别。
- **关键结果 / 消融** · 两类任务中表现有竞争力。
- **适用条件 / 局限** · 留出域需覆盖有意义的漂移组合。

**可复用机制** · 分开估标签先验与感知条件漂移，避免只修一种。

<a id="paper-153543"></a>

## Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153543) · [作者来源](https://openreview.net/forum?id=KaLmKJYhgp)

- **问题 / 瓶颈** · 长自回归的历史帧偏差会累积。
- **核心创新 / 方法** · 历史潜变量锚到高斯原语，用渲染召回并按阶段存取偏差训练。
- **Baseline** · 动作控制视频生成。
- **Benchmark** · ScanNet、DL3DV、OmniWorldGame。
- **关键结果 / 消融** · 摘要报告长程领先。
- **适用条件 / 局限** · 高斯锚依赖几何支持，快速近似偏差未必代表所有错误。

**可复用机制** · 持久世界记忆需要在训练中模拟自身历史误差。

<a id="paper-153777"></a>

## Robust Flow Matching under Target Corruption and Label Noise

[官方论文页](https://neurips.cc/virtual/2026/poster/153777) · [作者来源](https://openreview.net/forum?id=IjeT9T6KVY)

- **问题 / 瓶颈** · 统一异常权重混淆目标污染和错标。
- **核心创新 / 方法** · 目标污染看中后期残差，标签噪声比较同轨迹不同类条件残差。
- **Baseline** · 标准流匹配与稳健训练。
- **Benchmark** · 可控污染与真实带噪标签。
- **关键结果 / 消融** · 两类场景提高稳健性，摘要未报幅度。
- **适用条件 / 局限** · 依赖备选类别和可辨时间步。

**可复用机制** · 生成去噪数据筛选按污染轴寻找可判别残差。

<a id="paper-139536"></a>

## RobustGenBench: A Benchmark for Robust Generalization to Adversarial and Common Perturbations, with Applications to Vision and Vision-Enabled Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139536) · [作者来源](https://openreview.net/forum?id=KDsuVST8by)

- **问题 / 瓶颈** · 各自评估协议使鲁棒泛化难比较。
- **核心创新 / 方法** · 统一分类集、分割和扰动协议。
- **Baseline** · TRADES、Classic AT、混合架构、GPT-4o mini、Gemini 3 Flash。
- **Benchmark** · RobustGenBench 六集。
- **关键结果 / 消融** · 基础规模卷积 TRADES 强，视觉 LLM 在干净与常见失真强，范数下优势不同。
- **适用条件 / 局限** · 分类实证不能代替交互部署验证。

**可复用机制** · 架构和训练选型应测不同扰动轴的排序稳定性。

<a id="paper-148741"></a>

## Robust Graph Diffusion Model

[官方论文页](https://neurips.cc/virtual/2026/poster/148741) · [作者来源](https://openreview.net/forum?id=vOiJjNCLXY)

- **问题 / 瓶颈** · 原图受损后半监督训练变脆弱。
- **核心创新 / 方法** · 扩散生成可融入原图的节点和边。
- **Baseline** · 原图 GNN。
- **Benchmark** · 半监督节点分类，图鲁棒性。
- **关键结果 / 消融** · 增强后多个设置更稳，摘要未报告幅度。
- **适用条件 / 局限** · 依赖合成边与原图语义匹配。

**可复用机制** · 结构辅助数据应在压力条件下验证，避免只增加节点数量。

<a id="paper-155374"></a>

## Robust Hopfield Decision Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/155374) · [作者来源](https://openreview.net/forum?id=67TZXbgymj)

- **问题 / 瓶颈** · 常规注意力可能直接消费偏离经验的数据。
- **核心创新 / 方法** · 用现代 Hopfield 迭代能量最小化替代 softmax 注意。
- **Baseline** · 普通 Decision Transformer 和训练正则方案。
- **Benchmark** · 受扰观测下的离线决策。
- **关键结果 / 消融** · 摘要提出向已学模式回归，量化结果待核。
- **适用条件 / 局限** · 陌生但有效状态可能被拉回旧吸引子。

**可复用机制** · 鲁棒决策可在动作前使用有收缩机制的记忆读取。

<a id="paper-149349"></a>

## Robust Importance Sampling for Rare Events via Constrained Gaussian Mixtures

[官方论文页](https://neurips.cc/virtual/2026/poster/149349) · [作者来源](https://openreview.net/forum?id=qj7n3ANylE)

- **问题 / 瓶颈** · 直接重要性提议容易冷启动或方差爆炸。
- **核心创新 / 方法** · 设计覆盖后以有限方差约束拟合高斯混合。
- **Baseline** · 粗 Monte Carlo、交叉熵、VI、SMC、Subset Simulation。
- **Benchmark** · 稀有事件估计的效率和稳健性。
- **关键结果 / 消融** · 证明有限方差条件，摘要称优于广泛基线。
- **适用条件 / 局限** · 依赖提议族及约束容许覆盖。

**可复用机制** · 估长尾故障率时把尾部覆盖与中心拟合当两项验收。

<a id="paper-148746"></a>

## Robust Instruction Compliance in Cooperative Multi-Agent Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148746) · [作者来源](https://openreview.net/forum?id=vMEXVo6MCM)

- **问题 / 瓶颈** · 不可打断宏动作使代理难响应人类。
- **核心创新 / 方法** · 接指令时对进行中宏动作自举，分离任务优化和临时覆盖。
- **Baseline** · 标准 actor–critic 与不可中断宏动作。
- **Benchmark** · 不同复杂度宏动作任务，指令遵守和原表现。
- **关键结果 / 消融** · 提高遵守同时保任务表现。
- **适用条件 / 局限** · 依赖可判的指令生效时机及中断代价。

**可复用机制** · 让人类干预重规划进入价值更新，避免奖励把中断错归因。

<a id="paper-150781"></a>

## Robust Latent Space Bayesian Optimization with Marginalized Kernel

[官方论文页](https://neurips.cc/virtual/2026/poster/150781) · [作者来源](https://openreview.net/forum?id=fRlRq8PSjh)

- **问题 / 瓶颈** · 点编码损失不确定性使候选取得不稳。
- **核心创新 / 方法** · 对 VAE 后验边缘化核，采集时用协方差几何。
- **Baseline** · 既有潜空间 BO。
- **Benchmark** · 机器人设计等，候选采集表现。
- **关键结果 / 消融** · 摘要称多数任务改善。
- **适用条件 / 局限** · 闭式核依赖后验形式；编码质量影响外推。

**可复用机制** · 预算少的设计搜索不应把随机编码当确定坐标。

<a id="paper-156004"></a>

## Robust Multi-view Clustering against Imperfect Information

[官方论文页](https://neurips.cc/virtual/2026/poster/156004) · [作者来源](https://openreview.net/forum?id=1FPjSicyVu)

- **问题 / 瓶颈** · 可靠配对和完整观测均可能缺少。
- **核心创新 / 方法** · 用实例置信与原型语义运输推对应后验。
- **Baseline** · 十种多视图聚类。
- **Benchmark** · 六个常用数据集，不完整与错误配对。
- **关键结果 / 消融** · 有竞争优势，幅度未核。
- **适用条件 / 局限** · 实例和原型歧义需校准。

**可复用机制** · 跨模态对齐允许软候选，避免把未知配对硬写进训练。

<a id="paper-154554"></a>

## Robust Nash Alignment under Preference Uncertainty

[官方论文页](https://neurips.cc/virtual/2026/poster/154554) · [作者来源](https://openreview.net/forum?id=CiLFISXIZl)

- **问题 / 瓶颈** · 单点偏好优化缺乏稳健保证。
- **核心创新 / 方法** · 用四方原始对偶代理游戏和乐观镜像下降上升。
- **Baseline** · 硬约束鲁棒目标。
- **Benchmark** · 代理对偶间隙、目标下界及理论分析。
- **关键结果 / 消融** · 证明 O(1/√T) 收敛及相等条件。
- **适用条件 / 局限** · 歧义集和截断会影响下界保守性。

**可复用机制** · 用可解释的不确定集合检验对齐方向的稳定性。

<a id="paper-139199"></a>

## Robustness of Internal Signals for Hallucination Detection in Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/139199) · [作者来源](https://openreview.net/forum?id=f0yvSUpbJA)

- **问题 / 瓶颈** · 内部打分可能利用后文更常幻觉而不看图。
- **核心创新 / 方法** · 分开文本和视觉来源，比较位置启发式及不同检测器集成。
- **Baseline** · 纯 token 位置及内部信号。
- **Benchmark** · VLM 幻觉及早晚出现切片。
- **关键结果 / 消融** · 位置可有竞争力，早出现时捷径弱；弱检测器可给集成增益。
- **适用条件 / 局限** · 实证依赖所选 VLM 与位置干预。

**可复用机制** · 把输出位置作为混杂项，单测检测器是否对视觉证据敏感。

<a id="paper-148793"></a>

## Robust Offline Reinforcement Learning against Out-of-Distribution Dynamics in Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/148793) · [作者来源](https://openreview.net/forum?id=v2pep2iQuH)

- **问题 / 瓶颈** · 分布外动力学可使动作价值重尾并发生系统偏差。
- **核心创新 / 方法** · TRUST 用带梯度正则的局部扰动近似最坏转移，并按重尾统计重加权。
- **Baseline** · 已有鲁棒离线强化学习方法。
- **Benchmark** · 三个真实驾驶数据集，考察域外表现。
- **关键结果 / 消融** · 摘要报告综合提升 41.21%，并给出目标近似误差界。
- **适用条件 / 局限** · 具体综合指标和扰动适用范围未报告。

**可复用机制** · 遇到分布外转移时先看价值目标尾部，而不是只用中位表现调整鲁棒性。

<a id="paper-150750"></a>

## Robust Policy Optimization to Prevent Catastrophic Forgetting

[官方论文页](https://neurips.cc/virtual/2026/poster/150750) · [作者来源](https://openreview.net/forum?id=fg8I6pwObp)

- **问题 / 瓶颈** · 标准 RLHF 的高奖励策略可在之后的训练中忘记已有行为。
- **核心创新 / 方法** · 在 KL 有界策略邻域上做最大最小优化，并修改 GRPO。
- **Baseline** · 常规 RLHF 和后续阶段才做保护的方案。
- **Benchmark** · 多种基座后续 SFT 与 RL，考察安全和数学准确率。
- **关键结果 / 消融** · 作者报告减轻安全退化并维持后续任务表现，也保持数学准确率。
- **适用条件 / 局限** · 摘要未给邻域的经验覆盖和最坏性能数值。

**可复用机制** · 多阶段训练先优化老目标对未来参数更新的稳定性，再引入新目标。

<a id="paper-153328"></a>

## RobustPruner: Decoupled Relevance and Uncertainty for Efficient Visual Token Pruning in MLLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/153328) · [作者来源](https://openreview.net/forum?id=M8tBI5LjWD)

- **问题 / 瓶颈** · 小目标和遮挡证据可能低置信但决定答案。
- **核心创新 / 方法** · 按问题预测相关性、用行列式点过程形成多样候选，再按不确定性细化，在解码器中段一次裁剪。
- **Baseline** · 既有视觉 token 裁剪和未裁剪模型。
- **Benchmark** · 三个开放多模态模型及多种视觉语言任务，考察准确性、速度代理与鲁棒性。
- **关键结果 / 消融** · Qwen-2.5-VL-7B 保留原表现 95.22%，预填 FLOPs 为原 50.97%，KV 缓存为 20.57%。
- **适用条件 / 局限** · GPU 内存仍为原 91.43%，摘要未给延迟绝对值。

**可复用机制** · 相关性低与价值不确定是两件事，可在裁剪前保留可能改变答案的边缘证据。

<a id="paper-154644"></a>

## Robust Residual Correction via Selective Deployment for Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/154644) · [作者来源](https://openreview.net/forum?id=C5U25I5APG)

- **问题 / 瓶颈** · 残差信号弱时，始终开启的非线性修正可能过拟合。
- **核心创新 / 方法** · 冻结预测基座，用岭回归保守层和条件非线性校正，另用验证集标定启用规则。
- **Baseline** · 冻结基座和始终启用的纠正。
- **Benchmark** · 多长序列数据集与骨干，以跨时距 MSE、MAE 和不降级率评价。
- **关键结果 / 消融** · 多数配置改善，Traffic 相对 MSE 降幅超 20%。
- **适用条件 / 局限** · 依赖验证集代表部署情形，摘要未给跨分布保证。

**可复用机制** · 后处理的学习和启用可分别验证，避免轻微的平均改善掩盖可预防的预测退化。

<a id="paper-149478"></a>

## Robust Satisficing Ensemble: Scalable Model Aggregation Under Distribution Shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/149478) · [作者来源](https://openreview.net/forum?id=ppKtrQWhKN)

- **问题 / 瓶颈** · 标准集成减少模型方差，但无法保证跨分布。
- **核心创新 / 方法** · 将稳健满意化与二次风险代理相结合，得到解析的内层最坏分布以更新集成权重。
- **Baseline** · GroupDRO、IRM、SRM。
- **Benchmark** · SST-5、TREC 标签偏移，CivilComments 和 HuffPost 子群或时间偏移。
- **关键结果 / 消融** · 作者报告多种偏移中优于鲁棒对照。
- **适用条件 / 局限** · 风险代理采用二次形式，算法收敛至驻点，摘要未给逐任务数值。

**可复用机制** · 用显式的不确定分布权衡模型组合，避免训练分布的最优加权直接决定部署时加权。

<a id="paper-139092"></a>

## RobustStress: Stress-Testing AI-Generated Text Detectors under Gradual Perturbations

[官方论文页](https://neurips.cc/virtual/2026/poster/139092) · [作者来源](https://openreview.net/forum?id=lb5EY9x2CQ)

- **问题 / 瓶颈** · 只测试一档扰动或单一数据域难发现脆弱性何时出现。
- **核心创新 / 方法** · 在不同强度、跨场景设置中评估已有检测器。
- **Baseline** · 既有文本检测器和干净场景。
- **Benchmark** · 生成文本检测的强度与分布交叉条件，摘要未列数据集和指标。
- **关键结果 / 消融** · 摘要报告多样退化模式及强度和域变化的协同恶化。
- **适用条件 / 局限** · 压力条件只能覆盖测试范围，摘要未提供通用阈值。

**可复用机制** · 用强度曲线和场景切换的组合替代单一稳健性分值，以发现交互效应。

<a id="paper-155571"></a>

## Robust Surrogate Modeling for Explainable Graph Neural Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/155571) · [作者来源](https://openreview.net/forum?id=4cPBjztcLN)

- **问题 / 瓶颈** · 软边掩码把训练时的无权图变成带权图，造成解释性梯度不可靠。
- **核心创新 / 方法** · 迭代定位解释子图，并重加权训练解释代理使其适应加权图。
- **Baseline** · 直接用原图网络做软掩码解释。
- **Benchmark** · 多个图基准、图网络主干及解释方法。
- **关键结果 / 消融** · 摘要报告解释质量一致提高。
- **适用条件 / 局限** · 代理忠实性依赖重加权训练，摘要未给运行开销。

**可复用机制** · 解释方法改变输入类型时，单独验证原模型在解释分布下的梯度是否可信。

<a id="paper-151606"></a>

## Robust Task-Aware State Estimation from Pre-trained Perception

[官方论文页](https://neurips.cc/virtual/2026/poster/151606) · [作者来源](https://openreview.net/forum?id=ZJGqecJnb8)

- **问题 / 瓶颈** · 最大概率状态决策脆弱，维护所有符号状态又太贵。
- **核心创新 / 方法** · PRaVaSS 根据特征置信度和任务约束近似联合状态，找出累积概率过阈值的最小集合。
- **Baseline** · 感知后仅采用最可能状态或维护完整信念。
- **Benchmark** · VLM 感知驱动的任务规划、复杂度和下游决策效果。
- **关键结果 / 消融** · 摘要报告多项式复杂度与正确性保证，并改善下游规划。
- **适用条件 / 局限** · 依赖合理的感知概率和结构化约束，摘要未报告校准敏感性。

**可复用机制** · 把部署选择具体化为需要保留多少状态假设，而非仅在单状态和全部假设间选。

<a id="paper-154690"></a>

## ROCKET: Rapid Optimization via Calibration-guided Knapsack-Enhanced Truncation for Efficient Model Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/154690) · [作者来源](https://openreview.net/forum?id=BiaBywmZp3)

- **问题 / 瓶颈** · 统一层压缩率无法适应敏感度，迭代恢复成本高。
- **核心创新 / 方法** · 多选背包分配压缩率，以激活权重敏感度稀疏化系数后闭式更新字典。
- **Baseline** · 矩阵分解、结构化稀疏与动态压缩方法。
- **Benchmark** · 多架构、20% 至 50% 压缩率的保留表现。
- **关键结果 / 消融** · 30% 压缩时无需再训练保留超过 90% 的表现。
- **适用条件 / 局限** · 依赖小校准集和局部重建误差，摘要未给实际部署提速。

**可复用机制** · 在统一全局成本约束下根据每层误差曲线选择配置，避免同率压缩所有模块。

<a id="paper-151797"></a>

## ROCKET: Residual-Oriented Multi-Layer Alignment for Spatially-Aware Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/151797) · [作者来源](https://openreview.net/forum?id=XvSZyjKLY8)

- **问题 / 瓶颈** · 单层监督遗漏分布在不同深度的空间特征，朴素逐层对齐会梯度冲突。
- **核心创新 / 方法** · 以同一层无关投影映射多个学生和三维教师层，再以稀疏激活平衡损失。
- **Baseline** · 单层、朴素多层和既有对齐方案。
- **Benchmark** · LIBERO、LIBERO-Plus、RoboTwin、真机拣选。
- **关键结果 / 消融** · 摘要报告 LIBERO 成功率 98.5%，训练约用对照计算预算的 4%。
- **适用条件 / 局限** · 依赖三维视觉教师，摘要未给预算核算和真机结果。

**可复用机制** · 当知识分布在多个残差层，可以跨层共享映射，减少每层学习彼此冲突的投影。

<a id="paper-155471"></a>

## Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime

[官方论文页](https://neurips.cc/virtual/2026/poster/155471) · [作者来源](https://openreview.net/forum?id=5MwSociabw)

- **问题 / 瓶颈** · 几乎全过或全失败的组提供很少对比信号，浪费轨迹预算。
- **核心创新 / 方法** · 回放自生成的成功或失败前缀平衡轨迹组，只优化新续写部分。
- **Baseline** · 常规在线 rollout。
- **Benchmark** · SWE-bench Verified 与 AIME 2025，考察得分、组奖励信息和墙钟。
- **关键结果 / 消融** · Qwen3-14B/32B 分别快 2.01 倍和 1.55 倍，14B 峰值由 0.274 至 0.295。
- **适用条件 / 局限** · 约 50% 结论针对文中的二元组奖励统计，复杂奖励下未验证。

**可复用机制** · 若二元成败比例持续偏斜，可调采样难度而非单纯增大组规模。

<a id="paper-154033"></a>

## ROLLVERIFY: BRIDGING EFFICIENCY AND ACCURACY IN LONG-TAIL ROLLOUT REINFORCEMENT LEARNING

[官方论文页](https://neurips.cc/virtual/2026/poster/154033) · [作者来源](https://openreview.net/forum?id=GlTTkoAAWX)

- **问题 / 瓶颈** · 部分轨迹提高吞吐，但陈旧样本会损伤在线目标。
- **核心创新 / 方法** · 用 OPS 评估部分轨迹策略偏移，分别做序列级和 token 级检验。
- **Baseline** · 完全在线以及训练时重加权的部分 rollout。
- **Benchmark** · 多种规模、架构和任务，比较效果与训练效率。
- **关键结果 / 消融** · 作者报告表现匹配在线训练且提高效率。
- **适用条件 / 局限** · 摘要未报告阈值和截断对长程反馈的影响。

**可复用机制** · 复用异步轨迹时保留经验证的一致前缀，把部分样本修复纳入数据选择。

<a id="paper-151948"></a>

## Root-Selecting Fixed-Point Inversion for Rectified Flows via Trajectory Straightness

[官方论文页](https://neurips.cc/virtual/2026/poster/151948) · [作者来源](https://openreview.net/forum?id=WdrqbDVAXt)

- **问题 / 瓶颈** · 局部残差相近的根有不同累积重建误差
- **核心创新 / 方法** · 保持逆方程并加入直度选择条件
- **Baseline** · 现有反演方法
- **Benchmark** · FLUX.1-dev、PIE-Bench；重建和编辑保真度
- **关键结果 / 消融** · 重建和保留源图编辑均改善，数值未报告
- **适用条件 / 局限** · 保证依赖局部非扩张性

**可复用机制** · 时间反演验收整条轨迹形状，避免只看局部残差

<a id="paper-140089"></a>

## RoPE Is Not a Proper Relative Position Embedding

[官方论文页](https://neurips.cc/virtual/2026/poster/140089) · [作者来源](https://openreview.net/forum?id=HKQWXNPs9b)

- **问题 / 瓶颈** · 注意力公式依赖相对偏移不保证长距离衰减
- **核心创新 / 方法** · 形式化距离衰减并检查 RoPE
- **Baseline** · 抽象的衰减型相对位置方法
- **Benchmark** · 理论属性，未报告实验基准
- **关键结果 / 消融** · 证明 RoPE 不具所定义距离衰减
- **适用条件 / 局限** · 该性质并非所有相对位置定义的必备条件

**可复用机制** · 验证长度外推时测注意强度随跨度变化，避免由公式直接推断

<a id="paper-152759"></a>

## RoSA: Rotational Sparse Adaptation for Memory-Efficient Fine-Tuning

[官方论文页](https://neurips.cc/virtual/2026/poster/152759) · [作者来源](https://openreview.net/forum?id=QZlXiCc3kK)

- **问题 / 瓶颈** · 即便 PEFT 遍布全模型也使反传较长
- **核心创新 / 方法** · 固定低层，轮转更新块；条件允许时缓存早期隐藏状态
- **Baseline** · 常见 PEFT 及不同可训练设置
- **Benchmark** · 多个 LLM 和任务；显存与性能
- **关键结果 / 消融** · 降低峰值显存并保持较强表现，幅度未报告
- **适用条件 / 局限** · 缓存收益取决于数据重复与同一时刻冻结边界

**可复用机制** · 同显存比较跨层低秩和分时轮转微调

<a id="paper-153254"></a>

## RoSeViT: Role-Separated Vision Transformers for ARC Visual Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/153254) · [作者来源](https://openreview.net/forum?id=McXZ63160k)

- **问题 / 瓶颈** · 单 token 流会混合高层规则和局部网格
- **核心创新 / 方法** · 用专门控制 token 聚合变换指令，分离计算工作空间
- **Baseline** · 密集 ViT，受控骨干替换
- **Benchmark** · ARC-1；准确率
- **关键结果 / 消融** · 受控替换 54.5 至 56.6，递归细化至 58.8
- **适用条件 / 局限** · ARC 网格规律明确，向自然视觉迁移未验证

**可复用机制** · 空间任务可单独维护全局变换与局部特征

<a id="paper-152079"></a>

## RotVLA: Rotational Latent Action for Vision-Language-Action Model

[官方论文页](https://neurips.cc/virtual/2026/poster/152079) · [作者来源](https://openreview.net/forum?id=VcnKuCNmo3)

- **问题 / 瓶颈** · 离散动作码本可能把目标退化为帧重建
- **核心创新 / 方法** · 在 SO(n) 表示潜动作，联合去噪并作为机器人动作的条件
- **Baseline** · 既有 VLA 和离散潜动作方法
- **Benchmark** · LIBERO、RoboTwin2.0 及真实操作；成功率
- **关键结果 / 消融** · LIBERO 98.2%，RoboTwin 清洁与随机化 89.6% 和 88.5%
- **适用条件 / 局限** · 旋转语义和数据规模需做匹配消融

**可复用机制** · 同时测潜动作组合性、跨形态迁移和真实动作控制

<a id="paper-139509"></a>

## Routeability Before Routing: Routeability Audit Protocol (RAP) and RouteabilityBench for Audited LLM Model Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/139509) · [作者来源](https://openreview.net/forum?id=LZ6PlPtTUt)

- **问题 / 瓶颈** · 评分粗粒度时模型常并列，单个最强模型可能已吃掉大部分空间
- **核心创新 / 方法** · 诊断模型组合的互补性、并列和多重检验
- **Baseline** · 单一最强模型及常用路由预测增强
- **Benchmark** · 66 LLM；Omni-MATH、GPQA、MMLU-Pro、IFEval
- **关键结果 / 消融** · 明确正收益集中在依赖组合的 Omni-MATH 设置
- **适用条件 / 局限** · 结论随备选模型及任务评分粒度改变

**可复用机制** · 上线选择器前先报告 oracle 与单模型可达差距

<a id="paper-149368"></a>

## Route-Consistent Adaptation for Stable Quantization of Mixture-of-Experts Models with Theoretical Guarantees

[官方论文页](https://neurips.cc/virtual/2026/poster/149368) · [作者来源](https://openreview.net/forum?id=qZ58ypkC3E)

- **问题 / 瓶颈** · 专家输出小扰动会引发离散换专家并逐层放大
- **核心创新 / 方法** · 回放少量全精度路由，用访问加权的谱收益分配低秩修正
- **Baseline** · 原低比特模型与现有量化方法
- **Benchmark** · Mixtral、DeepSeek、Qwen3 的 MXFP4；困惑度、准确、速度
- **关键结果 / 消融** · 精度改善，Qwen3-30B 保留大部分推理加速
- **适用条件 / 局限** · 依赖原始路由可取得且校准样本代表部署

**可复用机制** · 量化测试应报告专家重合率和最终质量

<a id="paper-148374"></a>

## Routers Learn the Geometry of Their Experts: Geometric Coupling in Sparse Mixture-of-Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/148374) · [作者来源](https://openreview.net/forum?id=yMEUNfh0H7)

- **问题 / 瓶颈** · 辅助负载损失可能损害特化
- **核心创新 / 方法** · 分析专家与路由器梯度耦合，以输入滚动均值的余弦实现替代
- **Baseline** · 辅助损失与无损失负载均衡
- **Benchmark** · 稀疏 MoE 的负载差异和困惑度
- **关键结果 / 消融** · 负载最平衡，但困惑度略增加
- **适用条件 / 局限** · 质心无法分离多簇专家分工

**可复用机制** · 对照质心路由即可测相同负载下更复杂路由是否有收益

<a id="paper-155918"></a>

## RPC-GS: Gaussian Splatting with native RPC Rendering for Satellite Imagery

[官方论文页](https://neurips.cc/virtual/2026/poster/155918) · [作者来源](https://openreview.net/forum?id=1pXVfZYbAY)

- **问题 / 瓶颈** · 透视近似在推扫影像中带来系统几何偏差。
- **核心创新 / 方法** · 在渲染中原生支持 RPC。
- **Baseline** · 透视或仿射替代。
- **Benchmark** · 卫星影像几何重建。
- **关键结果 / 消融** · 摘要指向几何误差降低，幅度未核。
- **适用条件 / 局限** · 依赖 RPC 传感参数和渲染实现。

**可复用机制** · 当成像模型有已知非线性时先测投影偏差再优化场景表示。

<a id="paper-151887"></a>

## RPFQ-ViT: Rotated Phase-Frame Quantization for Extremely Low-Bit Weights in Vision Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/151887) · [作者来源](https://openreview.net/forum?id=XB7p2Y3eXt)

- **问题 / 瓶颈** · 标量码本破坏投影几何。
- **核心创新 / 方法** · 二维相位面配可学旋转和锚点，少量缩放恢复模。
- **Baseline** · 普通标量 QAT。
- **Benchmark** · ImageNet-1K，匹配 300 epoch，三次；另测移动部署。
- **关键结果 / 消融** · ViT-B/16 W2/A4 Top-1 79.33%。
- **适用条件 / 局限** · 需要通道配对，对实际硬件收益须独立测。

**可复用机制** · 在方向敏感线性层先分离角度和尺度的量化误差。

<a id="paper-156750"></a>

## RPP: A Certified Poisoned-Sample Detection Framework for Backdoor Attacks under Dataset Imbalance

[官方论文页](https://neurips.cc/virtual/2026/poster/156750) · [作者来源](https://openreview.net/forum?id=WyPkotlgqQ)

- **问题 / 瓶颈** · 多数类偏差会让不平衡时检测退化。
- **核心创新 / 方法** · 仅以黑盒模型输出概率做随机扰动认证。
- **Baseline** · 12 种数据防御。
- **Benchmark** · MNIST、SVHN、CIFAR-10、TinyImageNet、ImageNet10，检测精度。
- **关键结果 / 消融** · 类别越不平衡时一般防御越弱，RPP 的检测优势更明显。
- **适用条件 / 局限** · 依赖访问输出概率和认证前提。

**可复用机制** · 污染防御不只测类别平衡切片，也测高不平衡下的检出与误报。

<a id="paper-156124"></a>

## RRL-HOI: Reflective Reinforcement Learning for Open-Vocabulary HOI Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/156124) · [作者来源](https://openreview.net/forum?id=0ETD6EefF3)

- **问题 / 瓶颈** · 边框、人物物体配对或交互语义可分别出错。
- **核心创新 / 方法** · 把定位配对动作及编辑一致性纳入 GRPO 验收。
- **Baseline** · 现有开放词汇 HOI。
- **Benchmark** · 两个标准 HOI 评估基准。
- **关键结果 / 消融** · 摘要报告比较实验，幅度未核。
- **适用条件 / 局限** · 依赖盒标注和结构化编辑接口。

**可复用机制** · 复杂视觉关系输出可按错误原语分配验证信号。

<a id="paper-153743"></a>

## RSPO: Reasoning-Supervised Policy Optimization for Long-Tail Autonomous Driving

[官方论文页](https://neurips.cc/virtual/2026/poster/153743) · [作者来源](https://openreview.net/forum?id=J3cKSlk1K3)

- **问题 / 瓶颈** · 理由通顺不保证最终决策沿用同一证据。
- **核心创新 / 方法** · 以可验证推理决策数据训练一致性目标。
- **Baseline** · 驾驶推理和决策比较方法。
- **Benchmark** · 开源驾驶基准派生长尾情境。
- **关键结果 / 消融** · 摘要称决策和推理均改善。
- **适用条件 / 局限** · 真实道路与不可验证状态仍待验证。

**可复用机制** · 长尾采样中分别验理由依据和选定动作是否一致。

<a id="paper-152998"></a>

## RSPReg: Reliability-aware Structural Prototype Learning for Point Cloud Registration

[官方论文页](https://neurips.cc/virtual/2026/poster/152998) · [作者来源](https://openreview.net/forum?id=OjR3vaQ1iv)

- **问题 / 瓶颈** · 局部模糊匹配破坏全局姿态。
- **核心创新 / 方法** · 以结构原型作先验，根据不确定性调匹配和位姿影响。
- **Baseline** · 既有点云注册。
- **Benchmark** · 3DMatch、3DLoMatch、KITTI、ETH，注册召回。
- **关键结果 / 消融** · 摘要报告最高召回。
- **适用条件 / 局限** · 原型跨域可靠性需校准。

**可复用机制** · 将几何原型作为可降权的匹配证据。

<a id="paper-156792"></a>

## RSQ: Learning from Important Tokens Leads to Better Quantized LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/156792) · [作者来源](https://openreview.net/forum?id=kBezrKXHVS)

- **问题 / 瓶颈** · 均权统计会被低任务价值 token 支配。
- **核心创新 / 方法** · 旋转削弱离群权重，缩放重要 token 后估二阶统计。
- **Baseline** · 基于 GPTQ，比较既有量化。
- **Benchmark** · LLaMA3、Mistral、Qwen2.5 多任务。
- **关键结果 / 消融** · 持续优于对照，覆盖多校准设置。
- **适用条件 / 局限** · 重要性规则需防止只过拟合校准任务。

**可复用机制** · 量化误差用决策相关性加权，而非平均所有 token。

<a id="paper-149417"></a>

## RSSA: Robust Semantic and Spatial Aligner for Collaborative Perception

[官方论文页](https://neurips.cc/virtual/2026/poster/149417) · [作者来源](https://openreview.net/forum?id=qCLfuRLXY4)

- **问题 / 瓶颈** · 多视角共享特征会因坐标误差失准。
- **核心创新 / 方法** · 语义加概率空间变换，训练时扰动相对位姿。
- **Baseline** · 既有 V2X 协作感知。
- **Benchmark** · 真实和模拟数据，干净及偏噪位姿。
- **关键结果 / 消融** · 两种位置配置均有改善。
- **适用条件 / 局限** · 依赖注入噪声与部署误差相符。

**可复用机制** · 多机器人融合应调空间置信并注入可预期位姿漂移。

<a id="paper-139584"></a>

## RTCBench: Evaluating Tool Use of Large Language Models Beyond Oracle Access

[官方论文页](https://neurips.cc/virtual/2026/poster/139584) · [作者来源](https://openreview.net/forum?id=GvqAoUUnsn)

- **问题 / 瓶颈** · 直接提供正确接口掩盖真实检索错误。
- **核心创新 / 方法** · 给模型检索权限而非 oracle 定义，按发现、选择和调用定位失败。
- **Baseline** · 不同规模模型及前沿闭源模型。
- **Benchmark** · RTCBench，检索增强工具调用。
- **关键结果 / 消融** · 发现与检索后 grounding 是两类独立问题。
- **适用条件 / 局限** · 工具目录与检索机制将影响排序。

**可复用机制** · 回归工具代理时保存发现率、调用对齐和执行成败三个指标。

<a id="paper-139103"></a>

## RTEB: An Overfitting-Resistant Benchmark for Embedding Model Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139103) · [作者来源](https://openreview.net/forum?id=ktfYzbgPfX)

- **问题 / 瓶颈** · 通用公开嵌入榜过拟合且分布宽。
- **核心创新 / 方法** · 以公私混合检索集评嵌入并分域报告。
- **Baseline** · BEIR、MTEB。
- **Benchmark** · 20 模型、48 集，六域四语，含 28 私有集。
- **关键结果 / 消融** · 与旧榜排序相关 0.38，代理代码最高仅 0.48 NDCG@10。
- **适用条件 / 局限** · 私有集需维持可持续独立审核。

**可复用机制** · 部署以实际查询分布复测，不直接以公开聚合榜选检索器。

<a id="paper-153092"></a>

## Rubato: Signature Attention for Irregular Multivariate Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/153092) · [作者来源](https://openreview.net/forum?id=O1QyK9MzL5)

- **问题 / 瓶颈** · 统一插值会抹掉局部或跨通道动态。
- **核心创新 / 方法** · 从原序列抽单通道动态及联合路径签名，用结构投影降成本。
- **Baseline** · 现有不规则时间序列模型。
- **Benchmark** · 多不规则时间序列基准。
- **关键结果 / 消融** · 实验优于强基线，理论投影偏差受控。
- **适用条件 / 局限** · 签名阶数和采样稀疏程度需选。

**可复用机制** · 单通道细节和全局共变用两种原生视图建模。

<a id="paper-149838"></a>

## Rubato: Transcribing Piano Music with Timestamps

[官方论文页](https://neurips.cc/virtual/2026/poster/149838) · [作者来源](https://openreview.net/forum?id=muSIGk8gSE)

- **问题 / 瓶颈** · 音乐转录错误可能来自符号格式而非听觉。
- **核心创新 / 方法** · 采用可时间戳化多声部文本 InterMo 端到端训练。
- **Baseline** · 音乐转录级联及真值 MIDI。
- **Benchmark** · 音频到钢琴谱，谱面准确性。
- **关键结果 / 消融** · 端到端优于即使用真值 MIDI 的级联。
- **适用条件 / 局限** · 钢琴之外的语法适用性待验。

**可复用机制** · 换掉输入错误后仍失败，优先修中间表示。

<a id="paper-150280"></a>

## RubiConv - Efficient Boundary-Respecting Convolutions

[官方论文页](https://neurips.cc/virtual/2026/poster/150280) · [作者来源](https://openreview.net/forum?id=jKgfNj6zXV)

- **问题 / 瓶颈** · 标准 FFT 难保护打包边界，理论加速落空。
- **核心创新 / 方法** · 执行尊重边界且适合硬件的打包卷积。
- **Baseline** · 标准 FFT、注意力。
- **Benchmark** · 打包长序列的吞吐。
- **关键结果 / 消融** · 摘要报告明显加速，幅度未核。
- **适用条件 / 局限** · 需要硬件及批形状匹配。

**可复用机制** · 检查数据管线是否破坏低复杂度算子可实现性。

<a id="paper-154753"></a>

## Rubric-Align: Safety Alignment through Dynamically Co-Evolving Rubrics

[官方论文页](https://neurips.cc/virtual/2026/poster/154753) · [作者来源](https://openreview.net/forum?id=BDgXsrFjIF)

- **问题 / 瓶颈** · 静态二元奖励难随领域变化。
- **核心创新 / 方法** · 将自然语言量表动态加入安全监督。
- **Baseline** · 静态二元奖励。
- **Benchmark** · 开放安全与垂域能力。
- **关键结果 / 消融** · 安全稳健改善，通用能力大体保持。
- **适用条件 / 局限** · 量表和裁判本身需独立校准。

**可复用机制** · 将安全验收写成可审计及可迭代条款，保留通用能力回归。

<a id="paper-139334"></a>

## RUBRIC-MME: Real-User Behavior-grounded Rubric for Multimodal Interaction Capability Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/139334) · [作者来源](https://openreview.net/forum?id=WVjslQScrQ)

- **问题 / 瓶颈** · 人工单轮探针掩盖真实反复交互缺陷。
- **核心创新 / 方法** · 用部署日志的分布统计构造可合成交互，设分层量表。
- **Baseline** · 预编写及单轮多模态评估。
- **Benchmark** · 连续视频和多图交互，轮次及多层能力。
- **关键结果 / 消融** · 可诊断不同交互层级，指标幅度待核。
- **适用条件 / 局限** · 合成行为是否拟真需持续检查。

**可复用机制** · 避免从个别对话照搬内容，保留情境、意图与轮次统计。

<a id="paper-154107"></a>

## RuleSmith: Multi-Agent LLMs for Automated Game Balancing

[官方论文页](https://neurips.cc/virtual/2026/poster/154107) · [作者来源](https://openreview.net/forum?id=GDFl7AUtqB)

- **问题 / 瓶颈** · 等量对局浪费在低前景规则。
- **核心创新 / 方法** · 多代理自博弈产生指标，BO 分配高潜候选更多样本。
- **Baseline** · 常规规则搜索。
- **Benchmark** · 游戏平衡、胜率差距。
- **关键结果 / 消融** · 持续找到近均衡且可解释参数。
- **适用条件 / 局限** · 语言代理打法可能不代表真实玩家。

**可复用机制** · 便宜代理可做候选筛，一定预算保留昂贵精验。

<a id="paper-153720"></a>

## Runtime Monitoring of Perception-Based Autonomous Systems via Embedding Temporal Logic

[官方论文页](https://neurips.cc/virtual/2026/poster/153720) · [作者来源](https://openreview.net/forum?id=JGbC5dLr5b)

- **问题 / 瓶颈** · 感知状态难直接转人工布尔事实。
- **核心创新 / 方法** · 设嵌入时序逻辑，用共形校准谓词。
- **Baseline** · 环境真值语义。
- **Benchmark** · 多个操作环境、复合时序行为。
- **关键结果 / 消融** · 监测和真值高度一致，幅度未报告。
- **适用条件 / 局限** · 校准数据及环境漂移决定安全边界。

**可复用机制** · 将感知不确定性纳入时序谓词，不只做单帧异常识别。

<a id="paper-154715"></a>

## Runtime Verification of Multiple Natural Language Criteria for Agent Governance

[官方论文页](https://neurips.cc/virtual/2026/poster/154715) · [作者来源](https://openreview.net/forum?id=BXJQ1dWtA8)

- **问题 / 瓶颈** · 逐个调用生成式评审难以满足运行时吞吐。
- **核心创新 / 方法** · 以标注的上下文、目标、规范和判定四元组训练模型，并行返回三值判定。
- **Baseline** · 较大生成式评审。
- **Benchmark** · CriteriaBank、DynaBench、合成治理及真实保险合规。
- **关键结果 / 消融** · VFM-4B 合成准确率 88.3%，单 H100 在 4K 上下文中验证千条规范少于 2 秒。
- **适用条件 / 局限** · 真实数据结果限所测领域，摘要未报告相关规则的联合误差。

**可复用机制** · 同一轨迹需检查很多独立规则时，可共享上下文编码并给每条规则单独输出判定。

<a id="paper-139253"></a>

## RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities

[官方论文页](https://neurips.cc/virtual/2026/poster/139253) · [作者来源](https://openreview.net/forum?id=buiRmXBL93)

- **问题 / 瓶颈** · 能识别片段存在风险并不等于能给出可靠审阅定位。
- **核心创新 / 方法** · 用可编译时间点的不同粒度代码与配对语义版本，独立评估检测、CWE 分类和定位。
- **Baseline** · 四个前沿模型。
- **Benchmark** · RustMizan 的 crate、文件和函数，考察二分类与行级 F1。
- **关键结果 / 消融** · 二分类为 56% 至 65%，行级 F1 约 20%。
- **适用条件 / 局限** · 限所测 Rust 样例，摘要未给其他语言外推证据。

**可复用机制** · 安全审阅工作流在自动采信告警前，验证模型能否给出可靠定位及其对表面变化的稳定性。

<a id="paper-152605"></a>

## RVLoss: Runoff Vote Loss for Self-Supervised LiDAR Scene Flow Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/152605) · [作者来源](https://openreview.net/forum?id=RsacOS2C69)

- **问题 / 瓶颈** · 逐点最近邻虽可构造伪标签，但大物体内预测可能互相矛盾。
- **核心创新 / 方法** · 由最近邻运动投票生成少量支配候选，并用决选式投票将刚性写入损失。
- **Baseline** · 采用其他损失的自监督场流模型。
- **Benchmark** · Argoverse2 2026 Challenge 及另外四个数据集。
- **关键结果 / 消融** · 相较其他损失训练方法提升约 20%，跨数据集一致改善。
- **适用条件 / 局限** · 摘要未列具体指标及非刚体条件。

**可复用机制** · 当局部伪标签有噪声时，可在已知结构组内先聚合少数一致假设再监督个体。

<a id="paper-154429"></a>

## RVR: Retrieve-Verify-Retrieve for Comprehensive Question Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/154429) · [作者来源](https://openreview.net/forum?id=DfGZJUo1mT)

- **问题 / 瓶颈** · 单次检索容易重复返回常见答案而忽略其余正确答案。
- **核心创新 / 方法** · 检索后由验证器选择文档，以已验证内容扩展后续查询。
- **Baseline** · 包括智能体搜索与现成检索器。
- **Benchmark** · QAMPARI、QUEST 和 WebQuestionsSP，考察完整召回。
- **关键结果 / 消融** · QAMPARI 完整召回至少增 10% 相对或 3 个百分点绝对。
- **适用条件 / 局限** · 依赖验证可靠性，摘要未给多轮时延和误差传播。

**可复用机制** · 追求答案覆盖而非单个正确答案时，下一轮以当前已覆盖证据为条件进行搜索。

<a id="paper-149820"></a>

## RxGS: Receiver-Generalizable 3D Gaussian Splatting for Radio-Frequency Data Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/149820) · [作者来源](https://openreview.net/forum?id=n4D3BLFY3r)

- **问题 / 瓶颈** · 每个射频接收器单独拟合既冗余又无法预测新接收位置。
- **核心创新 / 方法** · 先学共享三维高斯几何并冻结，再学习接收器条件的全局和散射体级辐射。
- **Baseline** · 每接收器训练独立模型。
- **Benchmark** · 多射频场景数据集和训练时未见的接收器。
- **关键结果 / 消融** · 最多降低训练成本 45 倍、推理成本 7.6 倍，表现匹配或超过对照。
- **适用条件 / 局限** · 只报告同场景新接收器，跨场景外推未报告。

**可复用机制** · 多观测条件学习先区分不变物理结构和随观察改变的场，再只重用前者。

<a id="paper-148986"></a>

## S2MDF: A Plug-And-Play Layer for Intersection-Free Multi-Object Signed Distance Fields

[官方论文页](https://neurips.cc/virtual/2026/poster/148986) · [作者来源](https://openreview.net/forum?id=teTTi6AXHC)

- **问题 / 瓶颈** · 软惩罚不能去除所有交叠且权重难调。
- **核心创新 / 方法** · 对向量值 SDF 施加硬约束，用轻量层在训练或后处理时执行，兼容线性插值网格化。
- **Baseline** · 软约束及多种组合式 SDF 方法。
- **Benchmark** · 多物体 SDF 的交叠和重建质量。
- **关键结果 / 消融** · 作者报告交叠压至数值精度且保留重建质量。
- **适用条件 / 局限** · 依赖组合式 SDF 和文中支持的网格化设定。

**可复用机制** · 物理几何约束若不能违反，可先构建兼容下游解码的投影层，替代反复调惩罚系数。

<a id="paper-152479"></a>

## S²MoE: Shared-Subspace Mixture of Sparse Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/152479) · [作者来源](https://openreview.net/forum?id=SmZteLWKCK)

- **问题 / 瓶颈** · 参数截断虽降任务干扰，也损失有用能力。
- **核心创新 / 方法** · 共享子空间容纳多任务信息，稀疏专家恢复被删信息，再用免训练子空间映射路由。
- **Baseline** · 现有模型合并方法。
- **Benchmark** · 视觉与语言基准，摘要未列名称。
- **关键结果 / 消融** · 分别报告至多 1.6% 和 1.2% 增益。
- **适用条件 / 局限** · 摘要未给专家激活成本、存储与截断强度敏感性。

**可复用机制** · 当共享低秩主干会删除任务专用能力时，可把可恢复的残余作为稀疏路由单元。

<a id="paper-149219"></a>

## S2T-RLHF: Hierarchical Credit Assignment for Stable Preference-Based RLHF

[官方论文页](https://neurips.cc/virtual/2026/poster/149219) · [作者来源](https://openreview.net/forum?id=s0T8MQbeRk)

- **问题 / 瓶颈** · 序列偏好太稀疏，而过细分派会放大噪声。
- **核心创新 / 方法** · 建立句到 token 两级信用分派，无需再训练奖励模型。
- **Baseline** · 已有序列及 token 粒度的偏好训练方法。
- **Benchmark** · 多个数据集和优化设置，比较稳定性、鲁棒性及对齐。
- **关键结果 / 消融** · 作者报告更稳健并维持竞争性偏好表现。
- **适用条件 / 局限** · 摘要未给优选粒度的触发条件或数值。

**可复用机制** · 奖励粒度应与信号可靠度匹配，先稳定粗粒度分配，再限制局部调整幅度。

<a id="paper-155501"></a>

## S3Former: Sequential, Structural, and Statistical Fusion for Continuous-Time Dynamic Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/155501) · [作者来源](https://openreview.net/forum?id=56lSllQiF5)

- **问题 / 瓶颈** · 节点记忆和邻居序列可能忽略候选对共享结构、活跃度及重复互动。
- **核心创新 / 方法** · 融合序列、配对子图和在线统计记忆，用配对记忆校正。
- **Baseline** · 依赖节点记忆或序列的时序图模型。
- **Benchmark** · 十个动态图库，直推和归纳链接预测。
- **关键结果 / 消融** · 摘要报告大多数数据表现最佳，消融支持三类设计。
- **适用条件 / 局限** · 摘要未给动态图维护成本。

**可复用机制** · 关系预测若受到配对历史支配，可以将局部配对统计单独建模并与节点表征融合。

<a id="paper-138995"></a>

## SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?

[官方论文页](https://neurips.cc/virtual/2026/poster/138995) · [作者来源](https://openreview.net/forum?id=ry9igOb4j3)

- **问题 / 瓶颈** · 单次 GUI 操作任务会漏掉真实工作流中的状态和依赖。
- **核心创新 / 方法** · 把可部署系统中的真实任务拆成加权校验点，独立统计完成与进度。
- **Baseline** · 代表性大语言模型电脑操作代理。
- **Benchmark** · 23 个系统、六领域和 106 项任务。
- **关键结果 / 消融** · 最佳模型端到端完成率低于 4%。
- **适用条件 / 局限** · 摘要未给评分权重的敏感度。

**可复用机制** · 长程任务应把部分进展和最终任务严格完成分开打分。

<a id="paper-139112"></a>

## SaaSBench: Exploring the Boundaries of Coding Agents in Long-Horizon Enterprise SaaS Engineering

[官方论文页](https://neurips.cc/virtual/2026/poster/139112) · [作者来源](https://openreview.net/forum?id=kL0sdKjzQO)

- **问题 / 瓶颈** · 最终分数可能将基础环境失败归因给复杂任务推理。
- **核心创新 / 方法** · 按构建、运行、验证等工程阶段设可执行校验节点。
- **Baseline** · 多种编程代理。
- **Benchmark** · 30 项企业 SaaS 工程任务、六领域和 5,370 个节点。
- **关键结果 / 消融** · 作者报告大量失败出现在进入深层逻辑前，包括提前停止和无效调试。
- **适用条件 / 局限** · 具体场景为异构企业工程，摘要未给可消除这些失败的受控修复。

**可复用机制** · 用阶段条件成功率定位代理瓶颈，避免把基础环境未建成的数据用于判断后续业务能力。

<a id="paper-150687"></a>

## Saddle-to-Saddle Dynamics in Self-Supervised Shortcut Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/150687) · [作者来源](https://openreview.net/forum?id=gFQwJ1LW7D)

- **问题 / 瓶颈** · 语义无关但范围大或信号强的特征可能比真正目标更早被学习。
- **核心创新 / 方法** · 分析特征交叉相关谱怎样控制训练鞍点间的学习顺序。
- **Baseline** · 不同范围和幅值的特征。
- **Benchmark** · 自监督快捷特征学习，摘要未给正式数据集。
- **关键结果 / 消融** · 观察与理论表明学习优先级受交叉相关矩阵特征值影响。
- **适用条件 / 局限** · 结论依赖所分析的自监督设置，摘要未给普遍干预结论。

**可复用机制** · 评估表示训练时记录特征出现顺序，避免把优先学习误当作语义重要。

<a id="paper-153882"></a>

## Safe Actions Can Form Unsafe Traces: Benchmarking and Shielding Compositional Emergent Risk in AI Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/153882) · [作者来源](https://openreview.net/forum?id=I49ieEOieb)

- **问题 / 瓶颈** · 单个动作各自合规时，跨长距离的状态组合仍会触发风险。
- **核心创新 / 方法** · 以受控长轨迹比较不同检测窗口和带历史聚合的风险盾。
- **Baseline** · 滑窗、累计阈值、整轨迹和既有安全方法。
- **Benchmark** · CER-Bench，440 项任务、5 到 500 步，考察安全差距与任务完成。
- **关键结果 / 消融** · 15 个代理均出现非零组合差距，作者报告风险盾优于对照且 63.3% 任务无需额外调用。
- **适用条件 / 局限** · 受控长轨迹未必代表所有部署，摘要未给全部误阻率。

**可复用机制** · 为有状态代理显式保存需联合判断的安全条件，并将误阻与持续防护一起验证。

<a id="paper-155479"></a>

## Safe Active Learning with Future Viability Guarantees in Time-Series Models

[官方论文页](https://neurips.cc/virtual/2026/poster/155479) · [作者来源](https://openreview.net/forum?id=5HOe7v27vl)

- **问题 / 瓶颈** · 当前一步安全仍可能进入无法继续的死端
- **核心创新 / 方法** · 高斯过程不确定性加递归误差界近似未来安全集
- **Baseline** · 现有安全主动学习方法，名称未报告
- **Benchmark** · 合成和真实时序基准，违规与死端
- **关键结果 / 消融** · 减少两类失败并维持学习表现，摘要未给数值
- **适用条件 / 局限** · 需可信的预测误差界和安全条件

**可复用机制** · 约束控制采样前检测候选是否存在后续安全路径

<a id="paper-151214"></a>

## SAFE-DRIFT: Data Selection for Supervised Fine-tuning with Controllable Off-Target Drifts

[官方论文页](https://neurips.cc/virtual/2026/poster/151214) · [作者来源](https://openreview.net/forum?id=c6eraD0tjd)

- **问题 / 瓶颈** · 只筛编码等目标收益会改变其他行为
- **核心创新 / 方法** · 在共享低维空间近似参考 Fisher 和目标梯度
- **Baseline** · 已有数据选择方法
- **Benchmark** · 代码和医学问答，指定非目标行为
- **关键结果 / 消融** · 目标表现有竞争力并减小漂移
- **适用条件 / 局限** · 依赖已定义旁路行为和共享子空间性质

**可复用机制** · 选数据时对固定的保留集设漂移约束

<a id="paper-151944"></a>

## Safe-Fair MACPO: Burden-Fair Constrained Policy Optimization for Safe Multi-Agent Reinforcement  Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151944) · [作者来源](https://openreview.net/forum?id=Wff0AXdNL4)

- **问题 / 瓶颈** · 总收益和零违规掩盖负担集中
- **核心创新 / 方法** · 将公平负担纳入约束优化并与恢复过程分开归因
- **Baseline** · 恢复控制及匹配预算方法
- **Benchmark** · HalfCheetah、Safety-Gym、VMAS；回报和 Jain 指数
- **关键结果 / 消融** · HalfCheetah Jain 从 0.903 至 0.977，同时零硬违规
- **适用条件 / 局限** · 摘要区分机械负担与社会公平，不能混用

**可复用机制** · 用阶段分项成本辨别公平改善是否只是恢复更多

<a id="paper-153109"></a>

## Safeguarding Mutual Correction in Source-Free Domain Adaptation via Cut Statistics

[官方论文页](https://neurips.cc/virtual/2026/poster/153109) · [作者来源](https://openreview.net/forum?id=NsHE6SsVpK)

- **问题 / 瓶颈** · 互纠会放大噪声，尤其在迁移中
- **核心创新 / 方法** · 基于 cut statistics 逐样本筛掉疑似误纠
- **Baseline** · 现有无源域适配方法
- **Benchmark** · 多个 SFDA 数据集，详细指标未报告
- **关键结果 / 消融** · 摘要称校正信号净收益并改进实证
- **适用条件 / 局限** · 理论依赖可靠性判定条件，摘要未列细节

**可复用机制** · 在不可取源数据时验收被修正样本的净正确数

<a id="paper-155682"></a>

## Safe Offline Reinforcement Learning using Behavior Regularisation and Latent Feasibility-Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/155682) · [作者来源](https://openreview.net/forum?id=3k39ZE89zf)

- **问题 / 瓶颈** · 分布外状态容易触发不安全动作，价值误差放大权重方差
- **核心创新 / 方法** · 行为正则保护数据支持，并在潜空间引导可行性
- **Baseline** · AWR 与现有离线安全方法
- **Benchmark** · DSRL；约束、回报及推理步数
- **关键结果 / 消融** · 满足约束且回报有竞争力，单步推理
- **适用条件 / 局限** · 安全结论依赖潜空间可行性估计及数据覆盖

**可复用机制** · 分别做数据偏离与安全约束消融

<a id="paper-139084"></a>

## Safe, or Simply Incapable? Rethinking Safety Evaluation for Phone-Use Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/139084) · [作者来源](https://openreview.net/forum?id=m5QXsXgA5p)

- **问题 / 瓶颈** · 最终无害混合了正确判断与能力不足
- **核心创新 / 方法** · 按是否具备执行所需能力分层，消融视觉再查错误
- **Baseline** · 正常输入和去视觉输入
- **Benchmark** · 手机任务的能力与安全结果
- **关键结果 / 消融** · 移除视觉后不可执行情况增多，能力有和无时失败原因不同
- **适用条件 / 局限** · 能力估计受屏幕交互与任务难度影响

**可复用机制** · 为安全性添加独立能力对照，避免把卡住当成拒绝

<a id="paper-148840"></a>

## Safe Score Matching: Diffusion Policies with Hamilton-Jacobi Reachability for Online Safe Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/148840) · [作者来源](https://openreview.net/forum?id=ulU0SYntCo)

- **问题 / 瓶颈** · 单一约束惩罚会在安全和任务收益间过度保守
- **核心创新 / 方法** · 用 Hamilton–Jacobi 安全价值划分区域，分别奖励优化和恢复
- **Baseline** · 原始对偶及可达性方法
- **Benchmark** · 高维飞行跟踪和避障控制的模拟任务
- **关键结果 / 消融** · 摘要报告保持安全并有竞争力
- **适用条件 / 局限** · 依赖可信的安全价值和动力学假设

**可复用机制** · 闭环执行时分别验收常规控制与边界恢复

<a id="paper-149672"></a>

## Safety Reconstructed: Generative Modeling via Masked Diffusion Builds Strong Safety Guardrails

[官方论文页](https://neurips.cc/virtual/2026/poster/149672) · [作者来源](https://openreview.net/forum?id=oIxNRF9huQ)

- **问题 / 瓶颈** · 单 verdict token 容易借局部及位置捷径。
- **核心创新 / 方法** · 用 LoRA 训练掩码扩散模型按安全类重建，再比较两类分数。
- **Baseline** · 更强主干上的判别式 guard。
- **Benchmark** · 七留出安全基准，平均排名和 ECE。
- **关键结果 / 消融** · 平均排名领先、校准改善。
- **适用条件 / 局限** · 需要两类评分，延迟和开放环境稳健性须测。

**可复用机制** · 防御审核可训练模型解释整段文本在各标签下是否合理。

<a id="paper-155090"></a>

## SAFTAC: Simulation-Augmented Fine-Tuning of Open-Source LLMs for Analog Circuit Design

[官方论文页](https://neurips.cc/virtual/2026/poster/155090) · [作者来源](https://openreview.net/forum?id=8VwAj1accS)

- **问题 / 瓶颈** · 静态样本无法教模型根据真实仿真改进。
- **核心创新 / 方法** · 先三阶段监督生成和纠错，再加执行模拟奖励。
- **Baseline** · 冻结模型及闭源强模型。
- **Benchmark** · 8626 项模拟电路任务，单次和两阶段生成。
- **关键结果 / 消融** · 较最强闭源模型分别提升 15.9% 和 7.8%。
- **适用条件 / 局限** · 结论依赖模拟器与规格覆盖。

**可复用机制** · 可执行设计任务把验收器反馈作为训练数据，分离首答与修复评估。

<a id="paper-152343"></a>

## SAGAS: Semantic-Aware Graph-Assisted Stitching for Offline Temporal Logic Planning

[官方论文页](https://neurips.cc/virtual/2026/poster/152343) · [作者来源](https://openreview.net/forum?id=Tllrv77zoO)

- **问题 / 瓶颈** · 固定无任务轨迹无完整示范或新交互。
- **核心创新 / 方法** · 联合符号合成和从片段学到的可达关系。
- **Baseline** · 离线模型无关规划方法。
- **Benchmark** · OGBench 运动域上构造的 LTL 套件。
- **关键结果 / 消融** · 生成可执行且成本较低的前缀与后缀。
- **适用条件 / 局限** · 片段覆盖及语义对齐限制新任务。

**可复用机制** · 有硬逻辑目标时先在可达图中查可执行连接，再生成低层轨迹。

<a id="paper-151519"></a>

## SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/151519) · [作者来源](https://openreview.net/forum?id=a3nWqajGnm)

- **问题 / 瓶颈** · 局部可行与稀疏奖励造成分支偏和错误累积。
- **核心创新 / 方法** · 用符号闭合分析指导结构先验。
- **Baseline** · 未加结构的探索。
- **Benchmark** · 长期形式推理，含 Andrews–Curtis。
- **关键结果 / 消融** · 该任务最高改善 8 倍。
- **适用条件 / 局限** · 需要可靠局部结构先验，开放任务待验证。

**可复用机制** · 探索优先剔除无后续闭合可能性的分支。

<a id="paper-150164"></a>

## SAGE: Scalable Automated Robustness Augmentation for LLM Knowledge Evaluation

[官方论文页](https://neurips.cc/virtual/2026/poster/150164) · [作者来源](https://openreview.net/forum?id=kCMpObGLxq)

- **问题 / 瓶颈** · 生成后筛低利用率且验收不稳定。
- **核心创新 / 方法** · 少量人类标注训练量表验证器，再作为变体生成器 RL 奖励。
- **Baseline** · 人工 HellaSwag-Pro、生成再验证。
- **Benchmark** · HellaSwag 与迁移 MMLU。
- **关键结果 / 消融** · 低成本达到人工集近似质量，迁移无需再微调。
- **适用条件 / 局限** · 验收器须发现语义变化和潜在提示泄漏。

**可复用机制** · 先学习哪些改写保知识目标，再优化生成器产有效扰动。

<a id="paper-153513"></a>

## SageSched: Efficient LLM Scheduling Confronting Demand Uncertainty and Hybridity

[官方论文页](https://neurips.cc/virtual/2026/poster/153513) · [作者来源](https://openreview.net/forum?id=KmvVWPeI4v)

- **问题 / 瓶颈** · 时间与负载有不确定性。
- **核心创新 / 方法** · 结合提示和历史推理结果轻量估分布。
- **Baseline** · 既有推理调度。
- **Benchmark** · 多设置的实际试验平台。
- **关键结果 / 消融** · 效率改善超过 28.7%。
- **适用条件 / 局限** · 长度预测不同模型及工作负载需校准。

**可复用机制** · 给尾部时延预算留概率余量。

<a id="paper-149194"></a>

## SAGE: Semantic-Agnostic Image Embedding for Generalized AI-Generated Image Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/149194) · [作者来源](https://openreview.net/forum?id=sCLdMcBvzN)

- **问题 / 瓶颈** · 文本语义与生成痕迹混入 CLIP 特征。
- **核心创新 / 方法** · 同提示重建造配对，去文本语义方向，并学推理无字幕锚。
- **Baseline** · 既有 CLIP 检测方法。
- **Benchmark** · CommunityForensics，跨生成器变化。
- **关键结果 / 消融** · 检测有竞争力，生成器间性能波动降低。
- **适用条件 / 局限** · caption 不能覆盖所有语义，重建也引入风格偏移。

**可复用机制** · 训练诊断器先用成对控制隔离任务无关因素。

<a id="paper-151158"></a>

## SAGE: Semantically Disentangled Representation Learning through Latent Geometry Constraint and Large Language Model

[官方论文页](https://neurips.cc/virtual/2026/poster/151158) · [作者来源](https://openreview.net/forum?id=cae6eqSMPc)

- **问题 / 瓶颈** · 独立性目标可能优先学习不具语义的因子。
- **核心创新 / 方法** · 用多模态模型标注语义，并以三角几何约束锚定潜轴。
- **Baseline** · 独立性导向解缠。
- **Benchmark** · 多个图像因素解缠基准。
- **关键结果 / 消融** · 证明谱可学阈值并报告多基准改善。
- **适用条件 / 局限** · 依赖自动语义可信和因素定义。

**可复用机制** · 需要可控旋钮时先定语义监督，再做独立性正则。

<a id="paper-150303"></a>

## SAGE: Semantic Ambiguity Guided Capacity Expansion for Retrieval-Augmented Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150303) · [作者来源](https://openreview.net/forum?id=j95jiSEi4O)

- **问题 / 瓶颈** · 全局图索引贵且简单问句退化。
- **核心创新 / 方法** · 以局部分离不足找节点，再用超网络产局部 scorer。
- **Baseline** · 稠密与结构增强检索器。
- **Benchmark** · 单跳、多跳检索和问答。
- **关键结果 / 消融** · 检索、问答及规模权衡改善。
- **适用条件 / 局限** · 局部歧义指标和合成查询需贴近真实检索。

**可复用机制** · 按候选可分性动态升级，不为全库支付复杂模型成本。

<a id="paper-148394"></a>

## SAG-Sep: Sparse Augmented Graphs and Onion-Guided Search for Rounded Capacity Cut Separation

[官方论文页](https://neurips.cc/virtual/2026/poster/148394) · [作者来源](https://openreview.net/forum?id=yAJk2oHY8u)

- **问题 / 瓶颈** · 迭代预测粗化成本过高。
- **核心创新 / 方法** · 编码 LP 稀疏增广图，以嵌套候选结构搜索。
- **Baseline** · NeuralSEP 类迭代分离。
- **Benchmark** · 容量割分离任务，推理和有效切面。
- **关键结果 / 消融** · 摘要支持结构和速度设计，数值未核。
- **适用条件 / 局限** · 依赖分数 LP 与切面嵌套近似。

**可复用机制** · 多个约束级共享编码，只在局部候选上执行离散搜索。

<a id="paper-155120"></a>

## SAIR: Cost-Efficient Multi-Stage ML Pipeline Autoscaling via In-Context Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155120) · [作者来源](https://openreview.net/forum?id=8GrzZnygOz)

- **问题 / 瓶颈** · 独立控制器会错过跨段瓶颈迁移。
- **核心创新 / 方法** · Pareto 奖励区分支配关系，用贝叶斯惊奇检索经验指导无梯度决策。
- **Baseline** · 现有自动伸缩控制器。
- **Benchmark** · 四条 ML 流水线、三种负载，P99 和费用。
- **关键结果 / 消融** · 全配置最优或并列，P99 最多降 50%。
- **适用条件 / 局限** · 具体资源收益依赖可调执行接口。

**可复用机制** · 线上先存有信息量的跨段决策，再用支配关系稳住成本时延权衡。

<a id="paper-139139"></a>

## SALART-VQA: Diagnosing Whether VLMs Understand Salient Artifacts in Generated Images

[官方论文页](https://neurips.cc/virtual/2026/poster/139139) · [作者来源](https://openreview.net/forum?id=iVvXeIwD1f)

- **问题 / 瓶颈** · 二元召回掩盖不会解释哪里异常。
- **核心创新 / 方法** · 分别问存在性、语义、空间和证据识别，测试弃权。
- **Baseline** · 20 个视觉语言模型。
- **Benchmark** · SalArt-VQA 的瑕疵及缺席切分。
- **关键结果 / 消融** · 最佳模型检测召回 99.37%，四问全对仅 53.26%。
- **适用条件 / 局限** · 合成瑕疵和标注范围影响迁移。

**可复用机制** · 把知道有问题、找到地方与说明依据做成独立关卡。

<a id="paper-150336"></a>

## Saliency-Aware Multi-Route Thinking: Grounding and Reasoning on Vision-Language Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/150336) · [作者来源](https://openreview.net/forum?id=irnUqOfepp)

- **问题 / 瓶颈** · 固定思考脚手架无法适应证据和工具建议冲突。
- **核心创新 / 方法** · 免训练搜索文本原则，并根据并行理由贴合证据度选。
- **Baseline** · 固定单路指导。
- **Benchmark** · 视觉语言代理的推理与 grounding。
- **关键结果 / 消融** · 摘要给机制，效果数字待核。
- **适用条件 / 局限** · 多路线带来推理成本，证据评分需校准。

**可复用机制** · 选择怎样用工具与选择答案可以成为两层推理。

<a id="paper-153988"></a>

## SALT: When More Rollouts Don’t Help in Group-Based Policy Optimization and How to Make Them Matter

[官方论文页](https://neurips.cc/virtual/2026/poster/153988) · [作者来源](https://openreview.net/forum?id=H3EiJWynbi)

- **问题 / 瓶颈** · 组归一后低秩带符号成分会抵消。
- **核心创新 / 方法** · 由批 Gram 分解共享与残差，抵消强时放大残差。
- **Baseline** · GRPO 式组更新。
- **Benchmark** · 多推理 RLVR 任务及模型规模。
- **关键结果 / 消融** · 几何和表现改善，奖励和采样保持。
- **适用条件 / 局限** · 主要方向估计随批大小和噪声变化。

**可复用机制** · 把每回合的采样量与实际更新的有效秩分开诊断。

<a id="paper-152865"></a>

## Salvation Lies Within: Proactive Prefix Re-forming for LLM-based Tagging

[官方论文页](https://neurips.cc/virtual/2026/poster/152865) · [作者来源](https://openreview.net/forum?id=PoQNrAiH0j)

- **问题 / 瓶颈** · 少量记录错位使缓存无法匹配。
- **核心创新 / 方法** · 重排共同记录，在 NPU 上做前缀再组织。
- **Baseline** · 现有推理实现。
- **Benchmark** · 镜像环境意图标签。
- **关键结果 / 消融** · 吞吐最高 2.1 倍，并控制精度。
- **适用条件 / 局限** · 需在顺序改变后做任务和个人记录隔离核验。

**可复用机制** · 对近似集合输入，先测等价排序再决定缓存规范化。

<a id="paper-150278"></a>

## SamaDICE: Safe Multi-Agent Reinforcement Learning with Stationary Distribution Correction Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/150278) · [作者来源](https://openreview.net/forum?id=jLb42822IZ)

- **问题 / 瓶颈** · 联合平稳密度修正规模随代理数膨胀。
- **核心创新 / 方法** · 单调混合局部势近似全局对偶变量，训练代理 Bellman 残差。
- **Baseline** · 最强安全离线 MARL。
- **Benchmark** · 多环境、不同成本预算；决策 Transformer。
- **关键结果 / 消融** · 回报更高且紧预算优势更明显。
- **适用条件 / 局限** · 依赖单调分解和离线数据覆盖。

**可复用机制** · 可分解代价下以局部势学习全局约束，而非枚举联合行为。

<a id="paper-153753"></a>

## SaMA:  Morpho Adaptation via Asymmetric Expansion of Kronecker Product

[官方论文页](https://neurips.cc/virtual/2026/poster/153753) · [作者来源](https://openreview.net/forum?id=Ixbo0KjNzZ)

- **问题 / 瓶颈** · 同预算低秩限制表达且不变方向妨碍优化。
- **核心创新 / 方法** · 对 Kronecker 完美换位因子放开共享块约束。
- **Baseline** · LoRA 和强 PEFT。
- **Benchmark** · 常识及算术推理。
- **关键结果 / 消融** · 有效秩理论随参数二次扩展，实证更省且更强。
- **适用条件 / 局限** · 实际矩阵尺度、吞吐及指令迁移需测。

**可复用机制** · 适配器选型比较有效秩与平坦方向，而不仅看参数总数。

<a id="paper-156793"></a>

## SAMAT: A Stereotype-Aware Multimodal Transformer for Interpretable Misogynistic Meme Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/156793) · [作者来源](https://openreview.net/forum?id=1DJBFS7rLW)

- **问题 / 瓶颈** · 隐式刻板印象需要整合语言和视觉语境。
- **核心创新 / 方法** · 以刻板印象知识对齐跨模态并生成检索支撑。
- **Baseline** · 多模态大模型比较方法。
- **Benchmark** · MEE 8000 解释，Macro-F1、SAS、CFS。
- **关键结果 / 消融** · F1 88.1%，SAS 0.78，CFS 0.68。
- **适用条件 / 局限** · 文化情境和标注偏见限制泛化。

**可复用机制** · 对上下文分类器明确区分标签命中、检索证据正确和解释可追溯。

<a id="paper-153223"></a>

## Same Concept, Different Directions: Cross-Modal Feature Heterogeneity in Sparse Autoencoders

[官方论文页](https://neurips.cc/virtual/2026/poster/153223) · [作者来源](https://openreview.net/forum?id=Ms7zhhKERy)

- **问题 / 瓶颈** · 同一概念在图像与文本下可能沿不同方向，仅对齐激活仍有错配。
- **核心创新 / 方法** · 训练保留模态特征几何的稀疏自编码器，事后对齐对应特征。
- **Baseline** · 假定跨模态方向共享、只对齐激活的方法。
- **Benchmark** · 重建、跨模态检索和概念控制。
- **关键结果 / 消融** · 摘要报告三类任务改善。
- **适用条件 / 局限** · 摘要未报告对齐成本、外推模态或各指标数值。

**可复用机制** · 解释联合嵌入时分别验证概念是否同义和特征方向是否相同。

<a id="paper-152744"></a>

## Same Signal, Opposite Meaning: Direction-Informed Adaptive Learning for LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/152744) · [作者来源](https://openreview.net/forum?id=QfZi417XB9)

- **问题 / 瓶颈** · 同一不确定信号在不同环境可能预测额外推理有益或有害。
- **核心创新 / 方法** · 用不依赖预设门控信号的探索收集反事实，拟合稀疏收益门。
- **Baseline** · 固定信号方向的推理预算门控。
- **Benchmark** · 六环境、三个基座，考察成功率和成本。
- **关键结果 / 消融** · 作者报告成功率与成本折中更优。
- **适用条件 / 局限** · 需要成对探索且按环境与主干标定，摘要未给单环境额外成本。

**可复用机制** · 不确定只指明任务可能困难，应该验证困难样本是否真的会因增加推理而受益。

<a id="paper-152895"></a>

## SAME: Stability-Aware Embedding Extraction in Mixture-of-Experts Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152895) · [作者来源](https://openreview.net/forum?id=PcLcfDARfL)

- **问题 / 瓶颈** · 相近文本若触发不稳定的路由，可能编码到较远的表示。
- **核心创新 / 方法** · 动态分配每层激活专家并下调不稳定路由专家的输出。
- **Baseline** · 既有 MoE 嵌入提取方案。
- **Benchmark** · 多个 MoE 主干上的文本语义相似性。
- **关键结果 / 消融** · 作者报告一致改善，且不增加推理开销。
- **适用条件 / 局限** · 摘要未给其他任务或专家预算敏感性。

**可复用机制** · 为检索等任务用生成主干抽嵌入时，应检查语义近邻的路由一致性。

<a id="paper-139412"></a>

## Same Words, Different Judgments: How Preferences Vary Across Modalities

[官方论文页](https://neurips.cc/virtual/2026/poster/139412) · [作者来源](https://openreview.net/forum?id=SDNH5wA9Vo)

- **问题 / 瓶颈** · 同语义呈现不代表评审偏好可跨模态替用。
- **核心创新 / 方法** · 对 100 个提示中相同内容进行文本和音频评审，比较评分一致性和偏好。
- **Baseline** · 同内容文本评审及合成标注。
- **Benchmark** · 两种模态及组内相关 ICC(2,k)，和跨模态一致性。
- **关键结果 / 消融** · 各模态约九位评审达到 ICC 约 0.80，但跨模态同意率接近随机。
- **适用条件 / 局限** · 所需人数来自特定任务与样本，不能直接外推。

**可复用机制** · 换模态时先验证评审标准、偏好方向和所需标注重复度。

<a id="paper-149576"></a>

## SAMoR: Motion Modelling for Articulated Objects of Any Skeleton and Topology

[官方论文页](https://neurips.cc/virtual/2026/poster/149576) · [作者来源](https://openreview.net/forum?id=p5UNbKdSNp)

- **问题 / 瓶颈** · 不同物种和机构的关节数、连通性不同，逐关节对应不可靠。
- **核心创新 / 方法** · 借助关节名称线索将运动聚合到八个部件 token，用于生成和局部编辑。
- **Baseline** · 适配的可变关节分词器与固定骨架专业模型。
- **Benchmark** · 跨拓扑重建和 HumanML3D，指标含归一化 MPJPE。
- **关键结果 / 消融** · 跨拓扑 MPJPE 为 0.0275，约为最强对照的 1/5.8。
- **适用条件 / 局限** · 依赖功能部件与命名线索，摘要未报告陌生骨架的标签成本。

**可复用机制** · 跨形态迁移优先匹配部件功能，再将共享动作编码还原到各自的骨架。

<a id="paper-155275"></a>

## Sample-Grained Approximate Unlearning with Provable Per-Sample Bounds

[官方论文页](https://neurips.cc/virtual/2026/poster/155275) · [作者来源](https://openreview.net/forum?id=6tfToV92DV)

- **问题 / 瓶颈** · 总体平均值可能掩盖部分样本没有正确遗忘。
- **核心创新 / 方法** · SALA 用低成本目标分布估计给现有近似遗忘方法加单样本优化。
- **Baseline** · 已有近似遗忘方法及重训练分布参照。
- **Benchmark** · 分类与生成，比较单样本分布差距和跨次运行稳定性。
- **关键结果 / 消融** · 组合方法最多减少 86.67% 分布差距。
- **适用条件 / 局限** · 低成本分布目标仍是估计，摘要未说明极端样本的保障。

**可复用机制** · 比较删除前后模型时分开记录被删与保留样本的预测分布，不只看总体指标。

<a id="paper-154259"></a>

## Sample Transform Cost-Based Training-Free Hallucination Detector for Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154259) · [作者来源](https://openreview.net/forum?id=F6wp9J9jVl)

- **问题 / 瓶颈** · 输出变长且含义可能接近，直接比较序列或文本相似度难度大。
- **核心创新 / 方法** · 以隐藏向量经验分布表征回答，用配对 Wasserstein 代价构造 AvgWD 和 EigenWD 信号。
- **Baseline** · 强免训练不确定性基线。
- **Benchmark** · 五个开源模型、四个基准，比较 AUROC。
- **关键结果 / 消融** · 作者报告具竞争性或更强。
- **适用条件 / 局限** · 依赖多次生成和隐藏状态，摘要未给延时。

**可复用机制** · 在变长输出上比较语义样本时，可直接看生成表征分布而不强制序列对齐。

<a id="paper-149799"></a>

## Sampling-Based Safe Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149799) · [作者来源](https://openreview.net/forum?id=nGAaqOxzHK)

- **问题 / 瓶颈** · 未知动力学下的精确最坏情况优化难以执行。
- **核心创新 / 方法** · SBSRL 在有限动力学样本上近似最坏约束，并用认知不确定性约束探索。
- **Baseline** · 显式探索奖励策略及精确最坏情况约束是方法背景。
- **Benchmark** · 仿真、真实实验与深度集成连续控制。
- **关键结果 / 消融** · 在正则条件下给出学习全过程高概率安全和近优样本复杂度；摘要报告实证安全且高效。
- **适用条件 / 局限** · 覆盖依赖动力学样本和模型假设。

**可复用机制** · 把预测模型的不确定性转成候选约束集合，探索前统一检验策略是否能承受这些动力学。

<a id="paper-151806"></a>

## SAMPPO: Structure-Aware Mirror Proximal Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/151806) · [作者来源](https://openreview.net/forum?id=XsY4dSF6yB)

- **问题 / 瓶颈** · 固定信任区叠加嘈杂优势会使近义候选间多样性塌缩。
- **核心创新 / 方法** · 对局部语义密度使用自适应镜像近端更新。
- **Baseline** · PPO、BAPO、DPO、SimPO。
- **Benchmark** · Llama-3-8B 和 Gemma-2-2B，含 HelpSteer 的偏好基准与多样性。
- **关键结果 / 消融** · 报告超过 PPO/BAPO，与直接偏好方法在对齐与多样性折中上有竞争力。
- **适用条件 / 局限** · 摘要未给局部密度估计成本和迁移范围。

**可复用机制** · 语言动作空间存在多个近义选项时，不宜对所有局部区域使用同样的概率移动幅度。

<a id="paper-148209"></a>

## Sandboxed Coding Agents are Competitive Omni-modal Task Solvers

[官方论文页](https://neurips.cc/virtual/2026/poster/148209) · [作者来源](https://openreview.net/forum?id=zYMvOwt5bN)

- **问题 / 瓶颈** · 整段输入上下文成本高，固定多模态流程又可能漏掉待查片段。
- **核心创新 / 方法** · 让代码代理按需处理转录文本、帧及其他模态信号。
- **Baseline** · 原生全模态模型和固定多模态代理。
- **Benchmark** · 多个音视频基准与 TerminalBench-O 的实际处理任务。
- **关键结果 / 消融** · 作者报告多项任务达到或超过原生方案。
- **适用条件 / 局限** · 依赖可用工具和模态转换，摘要未报告统一计算预算对照。

**可复用机制** · 按任务需要抽取模态证据，可在增加上下文前先尝试少量工具查询。

<a id="paper-139059"></a>

## Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?

[官方论文页](https://neurips.cc/virtual/2026/poster/139059) · [作者来源](https://openreview.net/forum?id=nWEGPx5sz8)

- **问题 / 瓶颈** · 重建和常用解释分数可能无法区分真特征与随机基线。
- **核心创新 / 方法** · 在有真值的合成设定测恢复，并对真实激活构造三类随机约束。
- **Baseline** · 四类 SAE 与保留部分性质的随机对照。
- **Benchmark** · 真值特征恢复、解释性、稀疏探针及因果编辑。
- **关键结果 / 消融** · 四类中三类只有 7% 至 9% 特征恢复率，约 71% 解释方差，随机对照的因果编辑为 0.73 对 0.72。
- **适用条件 / 局限** · 合成真值有限，指标与参数外推未报告。

**可复用机制** · 分解模型的价值需超过保留其表面性质的廉价空模型，单看重建分数不够。

<a id="paper-149959"></a>

## SAPO: Step-Level Skill-Augmented Policy Optimization for Multi-Turn LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/149959) · [作者来源](https://openreview.net/forum?id=lu0GI2GKoK)

- **问题 / 瓶颈** · 长期任务需要逐步技能分配及运行中改进
- **核心创新 / 方法** · 让技能通过语义分析演化，策略用逐步优势学习
- **Baseline** · 标准 RL、既有技能与经验增强
- **Benchmark** · ALFWorld、WebShop、七检索 QA 任务
- **关键结果 / 消融** · 分别 93.5%、76.3% 与平均 60.9%
- **适用条件 / 局限** · 依赖技能发现的可验证性及语义归纳质量

**可复用机制** · 在每步决策中暴露技能再测同预算的信用增益

<a id="paper-151173"></a>

## SARA: Step-Adaptive Rank Adjustment for Diffusion Inference Acceleration

[官方论文页](https://neurips.cc/virtual/2026/poster/151173) · [作者来源](https://openreview.net/forum?id=cRkKhecFAQ)

- **问题 / 瓶颈** · 固定秩不能跟上逐步谱变化
- **核心创新 / 方法** · 用模型输出来估计谱误差并即时调秩
- **Baseline** · 固定近似及求解器和缓存加速
- **Benchmark** · SDXL、SD3、Stable Audio Open、TangoFlux
- **关键结果 / 消融** · 可与缓存及求解器叠加加速，数值未报告
- **适用条件 / 局限** · 实效依赖骨干谱和设备运算形态

**可复用机制** · 推理低秩控制分别验收成像质量和实际墙钟

<a id="paper-151251"></a>

## SASA: Subspace-Aware Sparse Autoencoders for Effective Mechanistic Interpretability

[官方论文页](https://neurips.cc/virtual/2026/poster/151251) · [作者来源](https://openreview.net/forum?id=bl8HewYJVx)

- **问题 / 瓶颈** · 单方向特征不足以表示内在多维因素
- **核心创新 / 方法** · 块稀疏 top-s 门控配迹范数学习有效维度
- **Baseline** · 标准稀疏自编码器
- **Benchmark** · 表征拆分、单义性和解释性评测
- **关键结果 / 消融** · 摘要称改善三项并提高训练效率
- **适用条件 / 局限** · 组容量必须能容纳等效特征维度

**可复用机制** · 绘制解释特征随组维度的变化并排查重复

<a id="paper-151940"></a>

## SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking

[官方论文页](https://neurips.cc/virtual/2026/poster/151940) · [作者来源](https://openreview.net/forum?id=Wgm2AWIzrX)

- **问题 / 瓶颈** · 硬选择损失只看进出集合，忽略候选排序
- **核心创新 / 方法** · 端到端学习相对优先级，并用 FlashAttention 风格内核实现
- **Baseline** · 既有可训练稀疏注意力
- **Benchmark** · 不同注意力预算下任务准确率
- **关键结果 / 消融** · 在紧预算收益较明显，数值未报告
- **适用条件 / 局限** · 内核和显存效益须按实际硬件测量

**可复用机制** · 同样保留 token 数下优先测排序质量

<a id="paper-152408"></a>

## SAVE: Sparsity-Aware Influence Estimation for Vocabulary-Expanded LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152408) · [作者来源](https://openreview.net/forum?id=TKPDoEpPd9)

- **问题 / 瓶颈** · 能拼写新词不代表关联技能已整合
- **核心创新 / 方法** · 合并词行条件曲率与 LoRA 层的影响估计筛辅数据
- **Baseline** · 常规辅助数据或未修复的词扩展，摘要未列名称
- **Benchmark** · Lean 自动形式化、工具调用与通用保留
- **关键结果 / 消融** · 目标和相关迁移改善，广泛保留持平
- **适用条件 / 局限** · 需词元足够出现以估条件影响

**可复用机制** · 扩展工具词表后同时验收新词触发及关联能力

<a id="paper-154708"></a>

## Say the Same, Act Differently: Text-Orthogonal Action Subspaces in Reasoning Vision-Language-Action Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154708) · [作者来源](https://openreview.net/forum?id=BcZ4hfwBik)

- **问题 / 瓶颈** · 理由稳定并不保证计划或控制量稳定
- **核心创新 / 方法** · 对照文本相似度与动作轨迹变化，仅记录监测结论
- **Baseline** · 只用理由文本监测
- **Benchmark** · 驾驶 VLA 受控安全评估；理由和动作一致性
- **关键结果 / 消融** · 发现理由保持时动作仍可显著改变
- **适用条件 / 局限** · 摘要证据集中单车模和受控条件

**可复用机制** · 在仿真及授权条件中设置动作级异常回归

<a id="paper-148928"></a>

## Scaffold3D: SfM-Conditioned Pointmap Prediction for Multi-View 3D Reconstruction

[官方论文页](https://neurips.cc/virtual/2026/poster/148928) · [作者来源](https://openreview.net/forum?id=uB3FRnvIAd)

- **问题 / 瓶颈** · 少共同纹理时图像特征难建立对应
- **核心创新 / 方法** · 将稀疏 SfM 几何与图像 token 一起推断稠密点图
- **Baseline** · 纯重建及多视图几何条件模型
- **Benchmark** · 低和无重叠重建
- **关键结果 / 消融** · 两视图版本超过部分多视图条件法，数值未报告
- **适用条件 / 局限** · 依赖低质量 SfM 的处理能力，摘要未给边界

**可复用机制** · 先验证融合方式再增加条件视图

<a id="paper-149509"></a>

## Scalable Adaptation of 3D Geometric Foundation Models via Weak Supervision from Internet Video

[官方论文页](https://neurips.cc/virtual/2026/poster/149509) · [作者来源](https://openreview.net/forum?id=pcEDgJBGuB)

- **问题 / 瓶颈** · 只靠新视频一致性可能覆盖原有几何能力
- **核心创新 / 方法** · 用可微高斯渲染约束多视图，再用锚数据正则避免遗忘
- **Baseline** · 原 MV-DUSt3R、VGGT
- **Benchmark** · 7Scenes、TUM-RGBD、Matterport3D；Chamfer
- **关键结果 / 消融** · 摘要称误差降 20–42%
- **适用条件 / 局限** · 来自多组件共同效果，锚与渲染的独立收益需复核

**可复用机制** · 适配前留可核验几何分布作防遗忘约束

<a id="paper-155653"></a>

## Scalable Fair Learning via Cramér-von Mises Regularization

[官方论文页](https://neurips.cc/virtual/2026/poster/155653) · [作者来源](https://openreview.net/forum?id=41DVZ3vBAY)

- **问题 / 瓶颈** · 依赖度量开销可能使训练难扩展
- **核心创新 / 方法** · 用排序计算 Cramér–von Mises 惩罚
- **Baseline** · 依赖度量公平正则方法
- **Benchmark** · 表格与图像；公平效用及训练开销
- **关键结果 / 消融** · 每批复杂度 O(B log B)，效用折衷有竞争力
- **适用条件 / 局限** · 训练时可取受保护属性，部署公平仍需按条件验证

**可复用机制** · 对分布型公平约束比较批次开销与真实条件偏差

<a id="paper-150581"></a>

## Scalable Maximum Entropy Reinforcement Learning for Diffusion Policies via Adjoint Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/150581) · [作者来源](https://openreview.net/forum?id=h8DYJlF7Jt)

- **问题 / 瓶颈** · 扩散策略多步采样和反传成本高。
- **核心创新 / 方法** · 用随机最优控制中的伴随匹配做最大熵策略优化。
- **Baseline** · 既有扩散 RL。
- **Benchmark** · 在线 RL，回报与计算开销。
- **关键结果 / 消融** · 表现具竞争力且成本降低，幅度未报告。
- **适用条件 / 局限** · 实际稳定依赖论文扩展和任务。

**可复用机制** · 借随机控制更新生成策略，单独验采样和训练成本。

<a id="paper-153198"></a>

## Scalable Minimal-Change Learning for Controllable Image Editing

[官方论文页](https://neurips.cc/virtual/2026/poster/153198) · [作者来源](https://openreview.net/forum?id=N7RrgL2N5Y)

- **问题 / 瓶颈** · 常规奖励会允许无关大改。
- **核心创新 / 方法** · 多模态代理分步评判最小变化，免人工标注。
- **Baseline** · 现有可控编辑。
- **Benchmark** · 本地化和语义一致性。
- **关键结果 / 消融** · 减少无关改变，幅度未报告。
- **适用条件 / 局限** · 需验证评判器是否能解析区域。

**可复用机制** · 把编辑目标与改动范围做成两个可独立校准的奖励。

<a id="paper-151201"></a>

## Scalable Multi-Agent Contrastive Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151201) · [作者来源](https://openreview.net/forum?id=cCWvLZocDZ)

- **问题 / 瓶颈** · 标准稀疏奖励探索和深度扩展困难。
- **核心创新 / 方法** · 共享去中心 actor，集中 critic 做目标对比。
- **Baseline** · MA-SAC+HER。
- **Benchmark** · 多代理目标条件控制。
- **关键结果 / 消融** · 4 到 64 层困难任务最高加 25 点，基线增益不稳。
- **适用条件 / 局限** · 依赖可定义达成目标及共享参数。

**可复用机制** · 扩模型前沿用同深度预算测试目标和结构的交互。

<a id="paper-156059"></a>

## Scalable Neural Safety Certification via Monotonicity

[官方论文页](https://neurips.cc/virtual/2026/poster/156059) · [作者来源](https://openreview.net/forum?id=0mIVNtnfDp)

- **问题 / 瓶颈** · 普遍高维验证成本大。
- **核心创新 / 方法** · 使用 Max-Monotone 网络和迭代验证细化。
- **Baseline** · 一般神经屏障构造。
- **Benchmark** · 单调系统及上闭不安全集，查询复杂度。
- **关键结果 / 消融** · 满足划分假设时仅 O(n) 模拟查询。
- **适用条件 / 局限** · 成功终止才返证书，依赖单调性。

**可复用机制** · 选与物理偏序兼容的证书，直接减少搜索空间。

<a id="paper-154980"></a>

## Scalable Supervised Optimal Transport of Gaussian Mixture Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154980) · [作者来源](https://openreview.net/forum?id=9Si78VoQ43)

- **问题 / 瓶颈** · 点云匹配开销高。
- **核心创新 / 方法** · 学习成分地面度量并以对角协方差近似 GBW。
- **Baseline** · 逐点 OT 与完整协方差度量。
- **Benchmark** · 合成及应用数据，运输与近似误差。
- **关键结果 / 消融** · 协方差计算线性，有互信息误差界。
- **适用条件 / 局限** · 依赖混合拟合和轴相关性可控。

**可复用机制** · 先压成带分布统计的群，再运输并量近似风险。

<a id="paper-148846"></a>

## Scalable Token-Level Hallucination Detection in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148846) · [作者来源](https://openreview.net/forum?id=uiQy5sVoUd)

- **问题 / 瓶颈** · 答案级检查易漏中间错误。
- **核心创新 / 方法** · 以细粒训练协议和评测校准检测器。
- **Baseline** · QwQ-32B 等推理模型。
- **Benchmark** · 推理轨迹的逐 token 幻觉。
- **关键结果 / 消融** · 0.6B 检测器训练后优于大型推理模型。
- **适用条件 / 局限** · 需可靠局部错误标签。

**可复用机制** · 专门的小检测器应与大模型自评做按位置对照。

<a id="paper-149427"></a>

## Scalable Variational Bayesian Fine-Tuning of LLMs via Orthogonalized Low-Rank Adapters

[官方论文页](https://neurips.cc/virtual/2026/poster/149427) · [作者来源](https://openreview.net/forum?id=q8fHjSdu4t)

- **问题 / 瓶颈** · 确定性 LoRA 置信不够可用。
- **核心创新 / 方法** · 将正交低秩架构与变分贝叶斯最后一层结合。
- **Baseline** · 常规适配及不确定性方案。
- **Benchmark** · 常识推理，域内与域外。
- **关键结果 / 消融** · 泛化和不确定性改善，幅度未报告。
- **适用条件 / 局限** · 最后层近似不能完整覆盖主干不确定性。

**可复用机制** · 在冻结模型的预算内把适配与置信校准共同设计。

<a id="paper-152337"></a>

## ScaleBITS: Scalable Bitwidth Search for Hardware-Aligned Mixed-Precision LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/152337) · [作者来源](https://openreview.net/forum?id=TpYhEftiHb)

- **问题 / 瓶颈** · 全精度敏感性在已有量化失真后失配。
- **核心创新 / 方法** · 渐进估边际损失，按输入输出通道集中模式重排。
- **Baseline** · 固定全精度敏感性。
- **Benchmark** · 硬件对齐 LLM 位宽选择。
- **关键结果 / 消融** · 摘要支持结构与变化规律。
- **适用条件 / 局限** · 需实际内核能利用重排和分块。

**可复用机制** · 连续压缩中重算当前模型的边际损失。

<a id="paper-150846"></a>

## SCALECUA : Scaling Computer Use Agents with Verifiable Task Synthesis and Efficient Online RL

[官方论文页](https://neurips.cc/virtual/2026/poster/150846) · [作者来源](https://openreview.net/forum?id=euINf9lQ7V)

- **问题 / 瓶颈** · 固定任务池和均匀采样浪费验证成本。
- **核心创新 / 方法** · 构造可验证任务，动态追踪逐任务能力。
- **Baseline** · 既有在线 CUA RL。
- **Benchmark** · 电脑使用与样本效率。
- **关键结果 / 消融** · 摘要报告框架扩展，幅度未报告。
- **适用条件 / 局限** · 依赖隔离环境和可靠完成条件。

**可复用机制** · 课程按可进步的成功概率动态分配，而非按同难度静态抽样。

<a id="paper-149755"></a>

## Scale-Invariant Empirical-Bayes Laplace Approximation for ReLU Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/149755) · [作者来源](https://openreview.net/forum?id=nbQX2MRjCm)

- **问题 / 瓶颈** · 同函数的层尺度使经验贝叶斯不确定性不同。
- **核心创新 / 方法** · 规范化重缩放后再做 Laplace。
- **Baseline** · 标准 EB-Laplace。
- **Benchmark** · 函数等价重缩放对照。
- **关键结果 / 消融** · 消除实测变动。
- **适用条件 / 局限** · 限定所处理的正齐次缩放。

**可复用机制** · 先控制不改变预测的参数对称性再比较不确定性。

<a id="paper-154359"></a>

## Scale Where It Matters: Training-Free Localized Scaling for Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154359) · [作者来源](https://openreview.net/forum?id=EAcDRgtXAi)

- **问题 / 瓶颈** · 全图 Best-of-N 浪费 GPU。
- **核心创新 / 方法** · 用免训练局部推理时扩展，兼顾全局保真。
- **Baseline** · Best-of-N。
- **Benchmark** · SD2.1、SDXL、FLUX，局部质量与 GPU 成本。
- **关键结果 / 消融** · GPU 成本节省 2 至 4 倍。
- **适用条件 / 局限** · 局部判断和边界一致性需测。

**可复用机制** · 以区域问题引导额外计算而非重做整样本。

<a id="paper-153199"></a>

## Scaling Arbitrary Architectures and Optimizers with Automatic Parameterization

[官方论文页](https://neurips.cc/virtual/2026/poster/153199) · [作者来源](https://openreview.net/forum?id=N6J19VlnAM)

- **问题 / 瓶颈** · 人工逐算法推超参变化难扩。
- **核心创新 / 方法** · 跟踪原语，解超参幂指数的线性约束。
- **Baseline** · 人工推导。
- **Benchmark** · JAX 方案，循环 Transformer、线性注意和混合器等。
- **关键结果 / 消融** · 恢复规则并找递归次数、上下文等新关系。
- **适用条件 / 局限** · 约束覆盖取决于原语标签和近似。

**可复用机制** · 将缩放假设写成可重用的计算图属性。

<a id="paper-148175"></a>

## Scaling Causal Reasoning with Increasingly Complex Causal Simulators

[官方论文页](https://neurips.cc/virtual/2026/poster/148175) · [作者来源](https://openreview.net/forum?id=zis0Cmnshx)

- **问题 / 瓶颈** · 标注稀缺，固定生成器难扩。
- **核心创新 / 方法** · 构造多复杂度因果模拟课程，加入模型自生成和领域知识形式化。
- **Baseline** · 固定难度或不同监督量。
- **Benchmark** · 跨表示与因果推理泛化。
- **关键结果 / 消融** · 课程和数据量增长一致改善。
- **适用条件 / 局限** · 模拟器可能引入捷径，须独立域测。

**可复用机制** · 合成推理数据变化结构而不仅增加同分布样本。

<a id="paper-149457"></a>

## Scaling Full Conformal Image Classifiers

[官方论文页](https://neurips.cc/virtual/2026/poster/149457) · [作者来源](https://openreview.net/forum?id=pwt7abXpU8)

- **问题 / 瓶颈** · 每类别重复适配代价高。
- **核心创新 / 方法** · 轻量归纳共形剪标签，再全共形确保组合保证；LDA 用秩一更新。
- **Baseline** · 标准全共形。
- **Benchmark** · 图像分类覆盖和计算。
- **关键结果 / 消融** · 保形式覆盖并减少计算。
- **适用条件 / 局限** · 筛选与正式覆盖误差需联合计。

**可复用机制** · 候选剪枝建立可控漏盖预算，再给昂贵估计器。

<a id="paper-148161"></a>

## Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons

[官方论文页](https://neurips.cc/virtual/2026/poster/148161) · [作者来源](https://openreview.net/forum?id=zpewdRsVpA)

- **问题 / 瓶颈** · 单纯扩大隐状态无法分辨各能力瓶颈。
- **核心创新 / 方法** · ELM 层并列操控三种神经元功能。
- **Baseline** · 缩小不同功能轴的循环模型。
- **Benchmark** · SHD-Adding 与 Enwik8。
- **关键结果 / 消融** · 单增三轴均改善。
- **适用条件 / 局限** · 两基准不足覆盖控制与视频。

**可复用机制** · 将时间常数容量和单步非线性分成独立缩放轴。

<a id="paper-148475"></a>

## Scaling Laws for Multimodal Data Mixtures

[官方论文页](https://neurips.cc/virtual/2026/poster/148475) · [作者来源](https://openreview.net/forum?id=xX1gcyTLbF)

- **问题 / 瓶颈** · 单一配比可能掩盖单模态和跨模态权衡。
- **核心创新 / 方法** · MoE 低成本扫描模型规模、token 和混合比。
- **Baseline** · 不同配比和模型规模。
- **Benchmark** · 268 次实验，457M 至 8.3B、最多 150B token。
- **关键结果 / 消融** · 摘要构建跨规模数据混合规律，具体最优比例需全文。
- **适用条件 / 局限** · MoE 结果迁移到稠密架构需验。

**可复用机制** · 在跨模态预训练前用代理规模估混合分布的任务边际收益。

<a id="paper-148634"></a>

## Scaling Laws for SAE Training Data

[官方论文页](https://neurips.cc/virtual/2026/poster/148634) · [作者来源](https://openreview.net/forum?id=wGJ8YYzO5w)

- **问题 / 瓶颈** · 持续存储新激活昂贵，固定缓存可能限制数据覆盖。
- **核心创新 / 方法** · 实验区分多样性与重复次数，并拟合数据约束缩放律。
- **Baseline** · 不同缓存大小、重复量和 SAE 结构。
- **Benchmark** · Llama-3.1、Qwen3 多层和多类 SAE，评估重建、解释与探针。
- **关键结果 / 消融** · 作者报告激活存储减少 8 至 64 倍而质量损失很小。
- **适用条件 / 局限** · 需对目标模型与层重新确认饱和点。

**可复用机制** · 将缓存大小与训练 token 数分开调参，在数据多样性饱和后重放。

<a id="paper-152309"></a>

## Scaling Limits of Long-Context Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/152309) · [作者来源](https://openreview.net/forum?id=U2aowiLeMa)

- **问题 / 瓶颈** · 固定温度的表现可能随键数量和局部几何变化。
- **核心创新 / 方法** · 推导注意力在临界逆温度两侧的极限及输出。
- **Baseline** · 次临界、临界和超临界的理论对照。
- **Benchmark** · 长上下文极限及球面均匀键例子。
- **关键结果 / 消融** · 临界时多个近邻保持显著权重，超过临界时集中至一个最近键。
- **适用条件 / 局限** · 依赖所分析的键分布和理论极限，摘要没有实际模型校准数据。

**可复用机制** · 测试检索密度变化时，同时跟踪注意力有效邻居数和上下文长度。

<a id="paper-154846"></a>

## Scaling Linear Mode Connectivity and Merging to Billion Parameter Pretrained Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/154846) · [作者来源](https://openreview.net/forum?id=AT2vWyunMD)

- **问题 / 瓶颈** · 参数对称性使功能相近的网络也可能有较大的插值障碍。
- **核心创新 / 方法** · 在双向学习中对齐双方的等效权重变换到同一线性路径。
- **Baseline** · 原始插值及已有对齐方案。
- **Benchmark** · 预训练视觉 Transformer 和十亿参数 LLM，ImageNet top-1 和损失障碍。
- **关键结果 / 消融** · 视觉路径保留性能，语言模型只剩小损失障碍。
- **适用条件 / 局限** · 摘要未给对齐成本和跨架构支持情况。

**可复用机制** · 模型合并无需固定一方为坐标参照，可以让双方保持函数不变地调整参数表示。

<a id="paper-148948"></a>

## Scaling Multi-Teacher Distillation for Digital Pathology

[官方论文页](https://neurips.cc/virtual/2026/poster/148948) · [作者来源](https://openreview.net/forum?id=tz5T3eSFDA)

- **问题 / 瓶颈** · 简单压成同一表示可能抹掉教师互补信息。
- **核心创新 / 方法** · 用教师 token、定制注意力、专家和对比损失学习教师专用表征。
- **Baseline** · 既有多教师蒸馏方法。
- **Benchmark** · 数字病理编码器蒸馏，最多十位教师并评估下游聚合。
- **关键结果 / 消融** · 摘要报告教师数增加时扩展表现更好。
- **适用条件 / 局限** · 多个架构变更并用，摘要未给各组件数值和其他领域测试。

**可复用机制** · 蒸馏互补来源时，可以延迟融合，让学生保留可单独读取的来源条件表征。

<a id="paper-153888"></a>

## Scaling Neural Motor Decoding via Decoupled Behavioral Pretraining

[官方论文页](https://neurips.cc/virtual/2026/poster/153888) · [作者来源](https://openreview.net/forum?id=I0HCQLIKMJ)

- **问题 / 瓶颈** · 配对神经行为记录的成本阻碍规模扩张。
- **核心创新 / 方法** · 先直接学习动作动态，有神经记录时再通过交叉注意力引入神经活动。
- **Baseline** · 单会话监督及大量神经预训练模型。
- **Benchmark** · 多会话运动解码，考察跨受试者和任务。
- **关键结果 / 消融** · 摘要报告仅行为预训练超过单会话监督，与更大规模神经预训练有竞争力。
- **适用条件 / 局限** · 依赖行为数据接近目标运动，摘要未给任务外推范围。

**可复用机制** · 昂贵传感器样本稀少时，可先用便宜的目标序列训练解码动态，再仅用成对数据学传感接入。

<a id="paper-151523"></a>

## Scaling Optimization-Oriented Hypernetworks for Implicit Neural Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/151523) · [作者来源](https://openreview.net/forum?id=a2C8sbYUCs)

- **问题 / 瓶颈** · MLP 实现的参数规模随目标宽度四次增长。
- **核心创新 / 方法** · 保留优化式链式结构，以注意力替代超网 MLP 主体并显式对齐输出神经元轴。
- **Baseline** · 单次预测和 MLP 优化式超网。
- **Benchmark** · 五项二维与三维隐式表示生成任务，含 NeRF。
- **关键结果 / 消融** · 摘要报告优于对照，并在 MLP 版本耗尽显存的宽度运行。
- **适用条件 / 局限** · 摘要未给推理注意力开销和更广的超网任务结果。

**可复用机制** · 扩展权重生成器时优先将大张量轴显式 token 化，而不是用无结构稠密映射。

<a id="paper-148389"></a>

## Scaling Reward Modeling without Human Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/148389) · [作者来源](https://openreview.net/forum?id=yD1cdr9cGj)

- **问题 / 瓶颈** · 昂贵的人类偏好标注限制奖励模型训练。
- **核心创新 / 方法** · RBS 从网络语料中的前缀和后缀构造训练信号，所得模型也可作为中训初始化。
- **Baseline** · 同规模监督奖励模型与直接监督微调。
- **Benchmark** · RewardBench v1、v2 和多模型系列。
- **关键结果 / 消融** · 数学网络训练使用 1100 万 token，在 RewardBench v2 上平均最高提升 7.7 个点。
- **适用条件 / 局限** · 摘要未给前后缀构造的完整规则，其他语料有效性有限。

**可复用机制** · 奖励模型的标注预算有限时，可先测试通用序列信号能否形成可继续监督优化的初始化。

<a id="paper-149896"></a>

## Scaling Whole-Body Loco-Manipulation through Compositional Data Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/149896) · [作者来源](https://openreview.net/forum?id=mQGMIJEWTN)

- **问题 / 瓶颈** · 真实全身操作动作难采，合成任务若接触覆盖不足也难泛化。
- **核心创新 / 方法** · 组合稀疏人体动作、抓取锚点和接触过渡，并随机化抓取前姿态与物体轨迹。
- **Baseline** · OMOMO 及同等数量的动作捕捉数据。
- **Benchmark** · 人形全身操作，考察接触覆盖、穿透、跟踪成功和泛化。
- **关键结果 / 消融** · 约五倍接触覆盖，同样物体与数据量下的策略更泛化，训练成功超 90%。
- **适用条件 / 局限** · 摘要未给真机部署和接触精度的逐任务统计。

**可复用机制** · 合成操作数据先覆盖接触拓扑和转移，再随机化不改变任务的动作与物体参数。

<a id="paper-152970"></a>

## Scattered by Design: Why Per-Output Pruning Resists Structured Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/152970) · [作者来源](https://openreview.net/forum?id=P0XAEBRFU2)

- **问题 / 瓶颈** · 逐输出剪枝得到的零值通常分散，后续线性变换可能恢复不了。
- **核心创新 / 方法** · 测试旋转、分解和置换，分析行间掩码相关性和频谱。
- **Baseline** · 稠密矩阵接受同样变换。
- **Benchmark** · OPT 前馈层的结构稀疏增量。
- **关键结果 / 消融** · 没有一层增加结构稀疏，表现为结构化的变换在稠密矩阵上也相同。
- **适用条件 / 局限** · 只测试文中的剪枝和线性变换。

**可复用机制** · 验证压缩手段时用稠密输入作空对照，区分预留结构与变换本身造成的结构。

<a id="paper-139501"></a>

## SCDBench: A Benchmark for LLM-Based Smart Contract Decompilers

[官方论文页](https://neurips.cc/virtual/2026/poster/139501) · [作者来源](https://openreview.net/forum?id=M1QDaACV7f)

- **问题 / 瓶颈** · 编译成功无法证明生成源码等同原程序。
- **核心创新 / 方法** · 使用配对源代码和字节码，设置格式、编译、接口和语义验证。
- **Baseline** · 现有 LLM 反编译器。
- **Benchmark** · 600 个 Solidity 合约，分阶段执行检查。
- **关键结果 / 消融** · 摘要报告严格验证下高质量恢复仍少，并认为编译修复可改善结果。
- **适用条件 / 局限** · 仅限所测语言与检查点，无法证明完整语义等价。

**可复用机制** · 给代码转换系统设置编译之后的功能验收，并按失败阶段单独统计。

<a id="paper-153991"></a>

## SCDM: Scalable Causal Discovery in Nonlinear Temporal Systems with Meta-Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/153991) · [作者来源](https://openreview.net/forum?id=H2Bm4cicZc)

- **问题 / 瓶颈** · 逐目标穷举优化在高维时间系统昂贵。
- **核心创新 / 方法** · 每个目标变量作为任务，元训练只更新其中子集，训练后读出有向关系。
- **Baseline** · 穷举逐目标优化和已有时序因果方法。
- **Benchmark** · 受控合成、神经影像风格及真实高维时序，比较恢复和扩展性。
- **关键结果 / 消融** · 作者报告恢复有竞争力且更易扩展，在若干误差小于总体边际时可恢复图。
- **适用条件 / 局限** · 保证依赖人口边际和模型近似条件，摘要未给具体规模。

**可复用机制** · 共享结构的多目标发现问题可用任务子采样降低每步计算，并将最终图读取与训练分开。

<a id="paper-152870"></a>

## Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing

[官方论文页](https://neurips.cc/virtual/2026/poster/152870) · [作者来源](https://openreview.net/forum?id=Pko5Y47PI3)

- **问题 / 瓶颈** · 只缩减 token 或推理步无法利用不同驾驶场景间的参数冗余。
- **核心创新 / 方法** · 利用场景时间连续性和模型冗余选择活动层组合，端到端优化。
- **Baseline** · 未使用层路由的先进驾驶 VLA。
- **Benchmark** · Bench2Drive，考察推理计算、驾驶和语言能力。
- **关键结果 / 消融** · 推理计算降低 53.5%，驾驶和语言能力下降很小。
- **适用条件 / 局限** · 摘要未给真实硬件延时或罕见突变场景的上限。

**可复用机制** · 场景连续且难度变化时，可先测试按上下文调模型深度是否比固定计算更合算。

<a id="paper-153396"></a>

## SceneBind: Binding What and Where Across Vision, Audio, and Language

[官方论文页](https://neurips.cc/virtual/2026/poster/153396) · [作者来源](https://openreview.net/forum?id=LfcBS0p58e)

- **问题 / 瓶颈** · 全局嵌入可能识别出现了什么，却丢失对象位置关系。
- **核心创新 / 方法** · 在预训练语义编码上加入对象语义空间槽，以场景相似性和对象匹配联合评分。
- **Baseline** · 仅用全局语义嵌入及其他多模态检索方法。
- **Benchmark** · 双耳音频、图像和语言场景，评估检索、定位及零样本迁移。
- **关键结果 / 消融** · 摘要报告场景和空间检索达到先进水平，且能零样本迁移至视听定位。
- **适用条件 / 局限** · 使用双耳数据与对象结构，摘要未给槽位数和数据集敏感度。

**可复用机制** · 跨模态绑定应显式对齐对象和空间关系，再用全局相似性判断场景语义。

<a id="paper-139016"></a>

## SceneFactory: GPU-Accelerated Multi-Agent Driving Simulation with Physics-Based Vehicle Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/139016) · [作者来源](https://openreview.net/forum?id=qCvGezil5Y)

- **问题 / 瓶颈** · 简化运动学会漏掉湿路、悬挂和轮胎接触造成的失效。
- **核心创新 / 方法** · 以 GPU 批处理全物理多车仿真，对照道路摩擦条件及摩擦感知策略。
- **Baseline** · 简化运动学及不感知摩擦的策略。
- **Benchmark** · 多车驾驶仿真，比较到达和避免碰撞所需峰值减速度 DRAC。
- **关键结果 / 消融** · 湿地摩擦感知平均峰值 DRAC 由 58.7 至 27.8 m/s²，未牺牲到达率。
- **适用条件 / 局限** · 物理建模仍为仿真，摘要未报告真机转移。

**可复用机制** · 扩大仿真规模时先保留会改变安全决策的物理变量，并在相同目标完成下衡量风险。

<a id="paper-149694"></a>

## Scenes as Objects, Not Primitives : Instance-Structured 3D Tokenization from Unposed Views

[官方论文页](https://neurips.cc/virtual/2026/poster/149694) · [作者来源](https://openreview.net/forum?id=o8YA4STvSo)

- **问题 / 瓶颈** · 原始三维点元表示让物体身份和编辑操作依赖事后分组。
- **核心创新 / 方法** · 配对实例 token 和局部锚 token，后者解码三维高斯并接受场景重建和分割监督。
- **Baseline** · 逐场景优化的三维重建方法。
- **Benchmark** · 室内场景，无类别实例分割与对象编辑。
- **关键结果 / 消融** · 摘要报告实例分割更好，并能直接按 token 组移动、删除和插入。
- **适用条件 / 局限** · 未报告跨场景类别或编辑真实性定量结果。

**可复用机制** · 需要可编辑环境状态时，在三维表征里原生编码对象归属而非事后聚类。

<a id="paper-154773"></a>

## SceneScaffold: Active Scene-State Construction for Unified 3D Scene Understanding

[官方论文页](https://neurips.cc/virtual/2026/poster/154773) · [作者来源](https://openreview.net/forum?id=B3wsHZckwI)

- **问题 / 瓶颈** · 纯特征流难以保留物体关系和空间歧义
- **核心创新 / 方法** · 将交互信息和全局摘要组织进场景表示
- **Baseline** · 既有三维理解方法，摘要未列名称
- **Benchmark** · 三维定位、问答、稠密描述和关系诊断
- **关键结果 / 消融** · 关系密集与空间歧义场景获得收益，未报告幅度
- **适用条件 / 局限** · 依赖上游场景事实准确

**可复用机制** · 在机器人问答中分开序列化物体、关系和整体环境

<a id="paper-155121"></a>

## SCION: Scene Composition via Instanced Neural Primitives

[官方论文页](https://neurips.cc/virtual/2026/poster/155121) · [作者来源](https://openreview.net/forum?id=8GgH1fcIAV)

- **问题 / 瓶颈** · 独立基元记忆增加存储并限制对象级编辑
- **核心创新 / 方法** · 共享基元间的实例结构，并用对抗目标保留细节
- **Baseline** · 高斯场景压缩方法
- **Benchmark** · 场景率失真、对象编辑及动画
- **关键结果 / 消融** · 约 1.2 MB 仍有较高质量，支持无需再训的实例编辑
- **适用条件 / 局限** · 重复结构少或不相似时共享收益待核

**可复用机制** · 比较重复环境的对象原型和逐元素地图存储

<a id="paper-139704"></a>

## SciR: A Controllable Benchmark for Scientific Reasoning in LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/139704) · [作者来源](https://openreview.net/forum?id=9eWzeCmndp)

- **问题 / 瓶颈** · 总分不能区分题面误读与计算失败
- **核心创新 / 方法** · 参数化改变呈现和推理难度，给每个模型双轴轮廓
- **Baseline** · 推理模型、指令模型和可验证求解器流水线
- **Benchmark** · SciR 多范式科学推理
- **关键结果 / 消融** · 两轴累积降低表现，连外接求解器也受题面呈现影响
- **适用条件 / 局限** · 受所构造题型和呈现差异限制

**可复用机制** · 给工具 Agent 加条件提取专门回归，求解成功不替代提取诊断

<a id="paper-152049"></a>

## SCOPE-RL: Stable and Quantitative Control of Policy Entropy in RL Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152049) · [作者来源](https://openreview.net/forum?id=Vt62uaRwMd)

- **问题 / 瓶颈** · 过早坍塌和过度探索都会影响解题
- **核心创新 / 方法** · 从自适应温度正样本构建熵正则
- **Baseline** · 强推理 RL 方法，名称未报告
- **Benchmark** · 推理任务 Pass@1、Pass@k
- **关键结果 / 消融** · 两类通过率改善，收益随探索非单调
- **适用条件 / 局限** · 最佳熵水平依任务和模型而变

**可复用机制** · 比较至少三档熵预算并监控单样本质量和多样性

<a id="paper-153114"></a>

## ScopeSAE: Model-Scope Feature Discovery with Interpretable Layer Selection

[官方论文页](https://neurips.cc/virtual/2026/poster/153114) · [作者来源](https://openreview.net/forum?id=NnmH2t52Uc)

- **问题 / 瓶颈** · 任意单层会混入低行为价值维度
- **核心创新 / 方法** · 跨层选择预测相关子空间，以干预及 KL 微调检验来源
- **Baseline** · 单层 SAE 等层选择方法
- **Benchmark** · 有效特征数、解释性、使用率及冗余
- **关键结果 / 消融** · 摘要报告各项改善且干预支持子空间解释
- **适用条件 / 局限** · 预测相关性指标和模型需匹配

**可复用机制** · 给解释工具增加预测保持率与所选层的控制组

<a id="paper-148234"></a>

## SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/148234) · [作者来源](https://openreview.net/forum?id=zNtmWDi0vX)

- **问题 / 瓶颈** · 静态问题会过易或过难，评审标准也制约收益
- **核心创新 / 方法** · 协同训练挑战者与解题者，并拆测检索、归纳及评分
- **Baseline** · 固定挑战者消融及 GRPO 数据
- **Benchmark** · 约 9000 提示及七个留出短问答基准
- **关键结果 / 消融** · 留出最多提升 13.8 点，评分规则质量是自评瓶颈
- **适用条件 / 局限** · 需能检验评审可靠性及问题难度

**可复用机制** · 动态造任务同时提供冻结验证集，防止评审和策略共适配

<a id="paper-154022"></a>

## SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts

[官方论文页](https://neurips.cc/virtual/2026/poster/154022) · [作者来源](https://openreview.net/forum?id=GpzONizTSo)

- **问题 / 瓶颈** · 单步反应难预测探查动作如何暴露隐藏几何
- **核心创新 / 方法** · 用物体中心、动作条件 rollout 与树搜索评估候选路径
- **Baseline** · VLA、具身 Agent 与三维世界模型
- **Benchmark** · Reveal、Placement 与真实杂乱架场景
- **关键结果 / 消融** · 长程遮挡任务收益较明显，未报告数值
- **适用条件 / 局限** · 预测物体状态和接触误差会影响搜索

**可复用机制** · 把揭露状态的动作显式纳入操作规划候选

<a id="paper-139442"></a>

## ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping

[官方论文页](https://neurips.cc/virtual/2026/poster/139442) · [作者来源](https://openreview.net/forum?id=Pcl8A4aiiN)

- **问题 / 瓶颈** · 查阅规则不一定改变行为。
- **核心创新 / 方法** · 按许可状态评估行动，并用人类对照。
- **Baseline** · 闭源和开源代理及 180 人。
- **Benchmark** · 1626 个明确禁止和 269 个未禁止站点。
- **关键结果 / 消融** · 多数代理合规率低于 5%，合规判别亦可能过度拒绝。
- **适用条件 / 局限** · 站点与指令分布影响比例。

**可复用机制** · 将规则发现、规则执行和不当拒绝分开测。

<a id="paper-153485"></a>

## Scratchpad Patching: Decoupling Compute from Patch Size in Byte-Level Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/153485) · [作者来源](https://openreview.net/forum?id=L1cO6MnwfR)

- **问题 / 瓶颈** · 扩大 patch 会损失细预测所需中间信息。
- **核心创新 / 方法** · 块内插入短暂 scratchpad 聚合已知字节。
- **Baseline** · 逐字节基线，固定块长。
- **Benchmark** · 自然语言和代码，下游质量和缓存。
- **关键结果 / 消融** · 16 字节块接近基线，缓存 16 倍小、推理少 3 至 4 倍。
- **适用条件 / 局限** · 效果受块预测结构限制。

**可复用机制** · 高压缩序列分块可用局部临时状态补足预测细节。

<a id="paper-152925"></a>

## ScreenSearch: Uncertainty-Aware OS Exploration

[官方论文页](https://neurips.cc/virtual/2026/poster/152925) · [作者来源](https://openreview.net/forum?id=PN2v87IKXN)

- **问题 / 瓶颈** · 视觉相似可隐藏不同工作流。
- **核心创新 / 方法** · 用结构检索聚合状态，基于匹配动作的后果分歧做图搜索。
- **Baseline** · 不同提案先验和探索设置。
- **Benchmark** · 11 桌面应用，百万截图及逾三万去重状态。
- **关键结果 / 消融** · 强提案显著帮助新状态发现，幅度未核。
- **适用条件 / 局限** · 依赖工具界面结构可读取和可重置。

**可复用机制** · 用行为等价替代视觉相似作为状态合并的检验。

<a id="paper-149151"></a>

## SCTI: Self-Calibrated Trident Identification of Black-Box LLM Watermarks

[官方论文页](https://neurips.cc/virtual/2026/poster/149151) · [作者来源](https://openreview.net/forum?id=sSXd2zEa4O)

- **问题 / 瓶颈** · 固定阈值对提示与采样配置敏感。
- **核心创新 / 方法** · 用经验零分布和多种统计信号识别。
- **Baseline** · 固定参照及水印家族专用检测。
- **Benchmark** · 多种 LLM 和水印算法。
- **关键结果 / 消融** · 相比对照可靠性提高，幅度未报告。
- **适用条件 / 局限** · 依赖可多次查询和统计检验假设。

**可复用机制** · 遇未知部署水印时按测试对象校准误报。

<a id="paper-152153"></a>

## scTrilemma: Balancing Identity, Invariance, and Reconstruction in Single-Cell Representation Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/152153) · [作者来源](https://openreview.net/forum?id=V8h1VhYtud)

- **问题 / 瓶颈** · 去批次易吞真实身份或损失复原信息。
- **核心创新 / 方法** · 只以表达数据对 VAE 潜瓶颈路由。
- **Baseline** · 普通单细胞表示方法。
- **Benchmark** · CZ CELLxGENE Census 连续发布零样本。
- **关键结果 / 消融** · 批效应更低且身份和重构保留，幅度待核。
- **适用条件 / 局限** · 非单细胞任务未验证。

**可复用机制** · 以真实版本切分同时评估希望去除和必须保留的因素。

<a id="paper-154985"></a>

## SCULPT: Advancing Masked Discrete Diffusion for High-Resolution Image Synthesis.

[官方论文页](https://neurips.cc/virtual/2026/poster/154985) · [作者来源](https://openreview.net/forum?id=9Qv7b21CM4)

- **问题 / 瓶颈** · 词表扩大时单码训练太稀疏。
- **核心创新 / 方法** · 组交叉熵给真值近邻正权，融合算子省显存。
- **Baseline** · 标准掩码离散扩散。
- **Benchmark** · 高分辨率图像合成与显存。
- **关键结果 / 消融** · 摘要报告训练和生成改善，幅度未核。
- **适用条件 / 局限** · 码本距离需反映合理替换。

**可复用机制** · 离散 token 极稀疏时先检查相邻码是否可作为软目标。

<a id="paper-148235"></a>

## SDAE: Semantic-Diversity-Aware Exploration for Efficient Reinforcement Learning in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/148235) · [作者来源](https://openreview.net/forum?id=zNpVz55DTW)

- **问题 / 瓶颈** · 无差别多样性探索可能放大无用答案。
- **核心创新 / 方法** · 按到正样本语义质心距离调优势。
- **Baseline** · 强推理 RL 基线。
- **Benchmark** · 竞赛推理、AIME25 Pass@256。
- **关键结果 / 消融** · AIME25 改善 13.3%。
- **适用条件 / 局限** · 语义距离和成功锚质量需校准。

**可复用机制** · 探索多样性按是否正确分层奖励。

<a id="paper-150124"></a>

## SDFlow: Similarity-Driven Flow Matching for Time Series Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/150124) · [作者来源](https://openreview.net/forum?id=kVQQScjr8o)

- **问题 / 瓶颈** · 自回归误差随长度累积。
- **核心创新 / 方法** · 在冻结 VQ 表示上全程运输，以低秩锚建流并用类别后验作监督。
- **Baseline** · VQ 自回归。
- **Benchmark** · 长序列生成，Discriminative Score、Context-FID。
- **关键结果 / 消融** · 生成指标和推理速度改善。
- **适用条件 / 局限** · 依赖预训练 VQ 的表示与低秩结构。

**可复用机制** · 从序列展开切换全局传输时保留离散类别监督。

<a id="paper-152741"></a>

## SDHilb: Schrödinger Dynamics-Guided Neural Network with Adaptive Multi-Scale Hilbert Transform for Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/152741) · [作者来源](https://openreview.net/forum?id=QhvWgfIvTX)

- **问题 / 瓶颈** · 实值状态可能混淆相位与振幅。
- **核心创新 / 方法** · 自适应多尺度 Hilbert 映复状态，再用辛离散动力与参数复用。
- **Baseline** · 已有时间序列预测。
- **Benchmark** · 多尺度预测。
- **关键结果 / 消融** · 摘要给结构方案，量化结果待核。
- **适用条件 / 局限** · Hilbert 分解对边界和非振荡成分需验证。

**可复用机制** · 在多传感时序分离幅相表征后独立诊断误差。

<a id="paper-153156"></a>

## SD-LoRA: Training-Time Structural Distillation into LoRA for Few-Shot Vision-Language Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/153156) · [作者来源](https://openreview.net/forum?id=NT2wZRLD58)

- **问题 / 瓶颈** · 推理局部图增加延迟。
- **核心创新 / 方法** · 用 token 图蒸馏到 LoRA-CLIP。
- **Baseline** · CLIP-LoRA。
- **Benchmark** · 11 少样本基准，1/2/4/8/16-shot、迁移、校准。
- **关键结果 / 消融** · 分别提升 1.3/1.2/2.4/1.9/2.0%，无上线图计算。
- **适用条件 / 局限** · 依赖训练图保留局部任务证据。

**可复用机制** · 训练时加结构教师，部署读取普通适配器。

<a id="paper-155518"></a>

## SD-Search: Hindsight Self-Distillation for Search-Augmented Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/155518) · [作者来源](https://openreview.net/forum?id=50CwcISp9W)

- **问题 / 瓶颈** · 终局奖励不能区分单次检索质量。
- **核心创新 / 方法** · 同策略生成多轨迹，将查询和结局给教师，逐 token JS 蒸馏给学生。
- **Baseline** · 外部教师和额外子问题标注。
- **Benchmark** · 搜索增强推理。
- **关键结果 / 消融** · 摘要报告细粒度信用机制，增益待核。
- **适用条件 / 局限** · 同题多次采样且终局可靠，教师不能越权泄漏到推理。

**可复用机制** · 只在训练加入结局信息以学习当时该问什么。

<a id="paper-150783"></a>

## SDS-LoRA: Overcoming Anisotropic Gradient Scaling in Low-Rank Adaptation

[官方论文页](https://neurips.cc/virtual/2026/poster/150783) · [作者来源](https://openreview.net/forum?id=fQrxSvxZkd)

- **问题 / 瓶颈** · 低秩参数反传各向异性。
- **核心创新 / 方法** · 将奇异值与反传解耦。
- **Baseline** · LoRA 和全量梯度。
- **Benchmark** · 梯度有效秩和收敛。
- **关键结果 / 消融** · 理论支持常规 LoRA 依条件数退化。
- **适用条件 / 局限** · 不同初始化与实际计算成本待验。

**可复用机制** · 适配器既看正向低秩也看反向有效更新。

<a id="paper-155569"></a>

## SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision

[官方论文页](https://neurips.cc/virtual/2026/poster/155569) · [作者来源](https://openreview.net/forum?id=4cZVcqbvw1)

- **问题 / 瓶颈** · 全程单一散度和难度可能损坏学习。
- **核心创新 / 方法** · 按 token 熵分区，正向 KL 退火到逆向，难度按能力递增。
- **Baseline** · 固定散度和统一课程。
- **Benchmark** · 在策略蒸馏的学习度及监督效率。
- **关键结果 / 消融** · 约一半 token 跳过；摘要称组件互相依赖。
- **适用条件 / 局限** · 依赖熵是能力代理，课程决定 rollout 可读性。

**可复用机制** · 把是否监督、用何散度及何时引入难例一起调。

<a id="paper-151731"></a>

## SeaPilot: Mobile Agent with Self-refining Environment Alignment

[官方论文页](https://neurips.cc/virtual/2026/poster/151731) · [作者来源](https://openreview.net/forum?id=YWAfNSzOLA)

- **问题 / 瓶颈** · 逐步上云昂贵，只看首屏会做不存在的假设。
- **核心创新 / 方法** · 发起阶段提供足以规划的环境摘要。
- **Baseline** · 逐步上云、一轮式。
- **Benchmark** · 移动 UI，准确率、云 token、隐私成本。
- **关键结果 / 消融** · 较一轮提高 46.7%，较逐步少 23.6 倍 token 和 89.6% 隐私成本。
- **适用条件 / 局限** · 需验证上下文最小化和 app 状态更新。

**可复用机制** · 用一次结构摘要替代连续原始屏上传，并检查计划的环境前提。

<a id="paper-150226"></a>

## Search at the Cost of Sampling: Nearly-Instant Latent Space Bayesian Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/150226) · [作者来源](https://openreview.net/forum?id=jqZgN0DS0E)

- **问题 / 瓶颈** · 当候选评分便宜，常规 BO 本身耗时。
- **核心创新 / 方法** · 在高维潜球面用线性代理、近闭式建模和采集。
- **Baseline** · 现有潜空间 BO。
- **Benchmark** · 图像生成候选优化。
- **关键结果 / 消融** · 论文跨任务报告约百倍加速，表现持平或更好。
- **适用条件 / 局限** · 依赖潜变量近球及分数局部可线性拟合。

**可复用机制** · 先测高维潜空间几何，再决定是否以解析获取代替昂贵搜索。

<a id="paper-149784"></a>

## Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA

[官方论文页](https://neurips.cc/virtual/2026/poster/149784) · [作者来源](https://openreview.net/forum?id=nK3rqD3vLo)

- **问题 / 瓶颈** · 细粒度搜索进入错误片段后继续局部观察难以纠正。
- **核心创新 / 方法** · 以场景边界构造非均匀时间树，代理按证据改变深度或回到上层。
- **Baseline** · 先前长视频问答代理和去掉下钻或回溯的消融。
- **Benchmark** · Video-MME、MLVU、LVBench，准确率。
- **关键结果 / 消融** · 最高增加 7.1 个准确率点，两项消融均有明显下降。
- **适用条件 / 局限** · 依赖场景分段与回溯决策，摘要未给推理额外成本。

**可复用机制** · 长时序证据检索将局部扩展和退回更宽上下文同时设为可选动作。

<a id="paper-153611"></a>

## Search More, Think Less: Rethinking Long-Horizon Agentic Search for Efficiency and Generalization

[官方论文页](https://neurips.cc/virtual/2026/poster/153611) · [作者来源](https://openreview.net/forum?id=K5rru6CDQC)

- **问题 / 瓶颈** · 重复交替推理与搜索会占用互动和上下文预算。
- **核心创新 / 方法** · 并行获取证据，用统一合成训练覆盖确定性问答和开放研究。
- **Baseline** · Mirothinker-v1.0 等搜索代理。
- **Benchmark** · BrowseComp、GAIA、Xbench 和 DeepResearch Bench。
- **关键结果 / 消融** · BrowseComp 为 48.6%，至多 100 互动步下平均推理步比 Mirothinker 少 70.7% 且准确率提高。
- **适用条件 / 局限** · 推理步并非整体墙钟，摘要未给并行外部请求成本。

**可复用机制** · 把可独立执行的搜索并行化，合并证据后再决定下一项推理。

<a id="paper-150219"></a>

## Search-Tree Scaling in Parallel Monte Carlo Tree Search

[官方论文页](https://neurips.cc/virtual/2026/poster/150219) · [作者来源](https://openreview.net/forum?id=jsFzBHaEg4)

- **问题 / 瓶颈** · 把并行度当作纯系统参数会遗漏树形和最优探索的变化。
- **核心创新 / 方法** · 分析 MuZero 的 pUCT 树深增长，并实测线程数与最佳系数。
- **Baseline** · 串行、不同线程数与探索系数。
- **Benchmark** · 理论搜索树规模及并行实证，摘要未列任务。
- **关键结果 / 消融** · 在正则条件下最佳路径深度按 √n/log n 增长，线程翻倍时经验最佳系数约降低 0.19。
- **适用条件 / 局限** · 具体数值依赖文中实现和实验条件。

**可复用机制** · 扩展搜索吞吐时，不宜照抄串行搜索的探索强度。

<a id="paper-150488"></a>

## SearchV: Evolutionary Fine-Grained Visual-Token Skipping for Efficient Vision-Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150488) · [作者来源](https://openreview.net/forum?id=hiy8FQrDmX)

- **问题 / 瓶颈** · 孤立测某层重要度会遗漏层与路径之间相互影响。
- **核心创新 / 方法** · 以全局贡献评价完整跳过配置，用进化搜索分别调注意力和前馈路径。
- **Baseline** · 未跳过的 7B VLM 及局部加速方法。
- **Benchmark** · 多模态任务和计算预算，摘要未列数据集。
- **关键结果 / 消融** · 作者报告存在计算更低且准确率更高的配置。
- **适用条件 / 局限** · 摘要未报告搜索成本、迁移和评分噪声。

**可复用机制** · 组合式加速应先评估模块共同改变的后果，再按全局结果选择跳过路径。

<a id="paper-151301"></a>

## SEAR: Sample Efficient Action Chunking Reinforcement Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/151301) · [作者来源](https://openreview.net/forum?id=bTE6KrCVKn)

- **问题 / 瓶颈** · 长动作序列难采样且反应慢，短动作又使价值传播变慢。
- **核心创新 / 方法** · 使用因果 Transformer critic 与多时域目标，提高每条动作块的监督。
- **Baseline** · SimbaV2 及离线到在线 QC。
- **Benchmark** · MetaWorld 和 OGBench cube-triple。
- **关键结果 / 消融** · 摘要报告超过在线基线并改善 QC。
- **适用条件 / 局限** · 摘要未报告动作块长度敏感性和单步计算。

**可复用机制** · 把同一块轨迹当作多种时长决策的监督样本，兼顾价值传播与闭环反应速度。

<a id="paper-156048"></a>

## SecureClaw: Clawing Back Control of LLM Agents

[官方论文页](https://neurips.cc/virtual/2026/poster/156048) · [作者来源](https://openreview.net/forum?id=0omFi3ZiBf)

- **问题 / 瓶颈** · 模型内部指令可能改变，单靠提示无法保证权限。
- **核心创新 / 方法** · 敏感读取走可信网关，外部写入先预览并只提交已确认的规范化请求。
- **Baseline** · 共同测试环境中的其他代理防护。
- **Benchmark** · AgentDojo、AgentLeak 和 ASB，比较攻击成功、泄露及任务效用。
- **关键结果 / 消融** · 报告 ASB 攻击成功率 0%、AgentDojo 0.64%、AgentLeak 所测泄露 3.23%。
- **适用条件 / 局限** · 依赖网关和可信执行器，结果限于所测任务。

**可复用机制** · 把授权和实际副作用绑定，避免让推理模型自身作为最终权限边界。

<a id="paper-152696"></a>

## Securing AI Agents with Information-Flow Control

[官方论文页](https://neurips.cc/virtual/2026/poster/152696) · [作者来源](https://openreview.net/forum?id=R5k46rM7mR)

- **问题 / 瓶颈** · 模型本身不能可靠执行跨工具的信息流边界。
- **核心创新 / 方法** · Fides 使用动态标记和受控显隐原语规划与执行。
- **Baseline** · 不同信息流代理规划设计。
- **Benchmark** · AgentDojo 和 WASP，评估安全与任务效用。
- **关键结果 / 消融** · 作者报告在保证安全属性下可完成广泛任务。
- **适用条件 / 局限** · 依赖正确的数据标签和可信执行，摘要未给失败场景占比。

**可复用机制** · 授权策略既应约束敏感数据能去哪里，也应约束不可信内容能影响哪些动作。

<a id="paper-148866"></a>

## S-EDL: Eliciting Self-Evidence from Sequence Likelihoods for Semantic Calibration of LLMs

[官方论文页](https://neurips.cc/virtual/2026/poster/148866) · [作者来源](https://openreview.net/forum?id=ub8LNj7RrR)

- **问题 / 瓶颈** · 固定答案选项的信心损失不适用于开放生成。
- **核心创新 / 方法** · 从序列似然提取证据，对问题特定的语义类构造可微 Dirichlet 先验。
- **Baseline** · 固定选项校准及普通生成训练。
- **Benchmark** · 四个开放式基准与三个模型，比较语义校准误差和准确度。
- **关键结果 / 消融** · 摘要报告减少语义校准误差并提升准确度。
- **适用条件 / 局限** · 依赖语义类别构造质量，摘要未给误归类敏感性。

**可复用机制** · 在开放任务上校准所表达的含义，避免把等义串分配到不同正确性事件。

<a id="paper-153117"></a>

## SEED: Self-Speculative Decoding via Implicit Encoder–Decoder

[官方论文页](https://neurips.cc/virtual/2026/poster/153117) · [作者来源](https://openreview.net/forum?id=NnLRTrv3cO)

- **问题 / 瓶颈** · 每个草稿步完整前向会抵消高质量草稿的优势。
- **核心创新 / 方法** · 将解码器重解释为隐式编码解码结构，用验证表示生成后续草稿。
- **Baseline** · 早退和多 token 预测的自推测方法、EAGLE-3。
- **Benchmark** · 4B 级模型及多种生成基准，考察加速和生成质量。
- **关键结果 / 消融** · 平均加速最高 2.5 倍，比 EAGLE-3 快 17%。
- **适用条件 / 局限** · 摘要未给长上下文、硬件和批量普适性。

**可复用机制** · 优化交替生成和验证流程时，优先复用重计算阶段已产生的隐藏状态。

<a id="paper-150697"></a>

## Seed-Your-Motion: Householder Orthogonal Noise for Motion-Controllable Video Diffusion Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150697) · [作者来源](https://openreview.net/forum?id=gBQls8hssQ)

- **问题 / 瓶颈** · 空间扭曲初始噪声可能破坏高斯结构并需额外校正。
- **核心创新 / 方法** · 依据光流在潜通道内逐位置采用 Householder 正交变换。
- **Baseline** · 噪声扭曲的视频运动控制。
- **Benchmark** · 受控视频生成基准，考察质量和处理时间。
- **关键结果 / 消融** · 作者报告匹配或优于对照，处理快 2.7 倍。
- **适用条件 / 局限** · 依赖光流条件与高斯先验，摘要未给复杂遮挡对照。

**可复用机制** · 条件化随机潜变量时可通过保持先验的变换把控制信号编码进去。

<a id="paper-153642"></a>

## Seeing Across Skies and Streets: Feedforward 3D Reconstruction from Satellite, Drone, and Ground Images

[官方论文页](https://neurips.cc/virtual/2026/poster/153642) · [作者来源](https://openreview.net/forum?id=JoAwGwFb3o)

- **问题 / 瓶颈** · 俯视与地面图像之间缺少俯仰、横滚和高度线索。
- **核心创新 / 方法** · 从卫星、重叠无人机和地面图共同前向重建，无需已知相对位姿。
- **Baseline** · 前向三维基线与专用跨视角模型。
- **Benchmark** · CrossGeo 85 场景及 KITTI，测重建、6DoF 位姿和定位。
- **关键结果 / 消融** · 作者报告在 CrossGeo 一致更优，未在 KITTI 训练也超过多数所测专用指标。
- **适用条件 / 局限** · 需要中间视角与地面重叠。

**可复用机制** · 跨视角对应困难时，优先增加能同时提供重叠和三维线索的桥接视角。

<a id="paper-149456"></a>

## Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes

[官方论文页](https://neurips.cc/virtual/2026/poster/149456) · [作者来源](https://openreview.net/forum?id=pxblmE8t2f)

- **问题 / 瓶颈** · 部署时逐步滚动世界模型消耗大，纯反应式策略缺乏预见。
- **核心创新 / 方法** · 用动作条件未来预测给候选导航行为分配偏好，再蒸馏为快速策略。
- **Baseline** · 反应式和学习式导航对照。
- **Benchmark** · 多人场景导航，考察效率及人类对自然性的评价。
- **关键结果 / 消融** · 摘要报告导航更高效且被观察者认为更像人。
- **适用条件 / 局限** · 依赖世界模型预测的可靠性，摘要未给实机成本。

**可复用机制** · 当在线规划昂贵时，可以让世界模型只在策略学习中区分可预见的后果。

<a id="paper-153133"></a>

## Seeing Both the Forest and the Trees: Reusing Holistic 3D Priors for Part-Decomposed Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/153133) · [作者来源](https://openreview.net/forum?id=NdxaPh23ii)

- **问题 / 瓶颈** · 部件生成需同时利用整体结构和部件细节先验。
- **核心创新 / 方法** · 用交错注意力让预训练整体形状模型处理两种坐标帧。
- **Baseline** · 先前部件分解生成器。
- **Benchmark** · PartObjaverse-Tiny，评估部件形状、相干性及训练成本。
- **关键结果 / 消融** · 摘要报告较低训练成本下匹配或超过对照，并支持局部编辑。
- **适用条件 / 局限** · 验证限于较小数据集，依赖良好的整体形状先验。

**可复用机制** · 保留同一潜变量的对象级和部件级坐标解释，可复用整物体先验进行组合生成。

<a id="paper-152386"></a>

## Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners

[官方论文页](https://neurips.cc/virtual/2026/poster/152386) · [作者来源](https://openreview.net/forum?id=TU6XyrLcIu)

- **问题 / 瓶颈** · 单查资源清单、文本和源码会漏掉非文本风险
- **核心创新 / 方法** · 审核时联合分析文档、代码、视觉资料及引用资源的行为关联
- **Baseline** · 主要只覆盖文本和源码的既有扫描器
- **Benchmark** · 授权环境中的技能安全评测
- **关键结果 / 消融** · 摘要报告多模态扫描改善，未给数值
- **适用条件 / 局限** · 不能保证覆盖任意资源和运行条件

**可复用机制** · 在隔离环境中将视觉内容纳入发布前独立审核

<a id="paper-150559"></a>

## Seeing or Rationalizing? Scene-Evidence-Guided  Chain-of-Thought for Faithful 3D Multimodal  Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150559) · [作者来源](https://openreview.net/forum?id=hFFajpszNV)

- **问题 / 瓶颈** · 自然语言解释可以绕过真实几何
- **核心创新 / 方法** · 逐步绑定可核对证据，并用更换场景和近似诱饵检验
- **Baseline** · 多个原三维多模态模型
- **Benchmark** · 三维 QA、定位、MSQA、Beacon3D 与捷径压力测试
- **关键结果 / 消融** · 定位和解释验证指标均有提升，未报告数值
- **适用条件 / 局限** · 证据指针质量依赖可标注对象和可分关系

**可复用机制** · 更改空间条件时检查答案和理由是否同步响应

<a id="paper-148448"></a>

## Seeing Together, Acting Apart: Shared Environmental Understanding for Multi-Robot Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/148448) · [作者来源](https://openreview.net/forum?id=xjwxcKVFWO)

- **问题 / 瓶颈** · 独立视角观察有限，直接统一策略又可能破坏单机能力
- **核心创新 / 方法** · 融合部分第一视角为共享潜环境表示，控制仍由各机器人处理
- **Baseline** · 动作、历史及策略共享变体
- **Benchmark** · 单机导航、配对仿真和真实机器人
- **关键结果 / 消融** · 保留单机能力，协作和个体成功率提高
- **适用条件 / 局限** · 融合依赖时空坐标对齐和通信，摘要未量化负荷

**可复用机制** · 分别消融共享世界状态与共享控制器

<a id="paper-154994"></a>

## Seeing Together: Multi-Robot Cooperative Egocentric Spatial Reasoning with Multimodal Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/154994) · [作者来源](https://openreview.net/forum?id=9LAZdtxn3n)

- **问题 / 瓶颈** · 部署时未必有统一全局位姿测量
- **核心创新 / 方法** · 训练融合多路视频并做物理一致提示蒸馏，测试只需自视视频
- **Baseline** · 22 MLLM 及最强微调模型
- **Benchmark** · CoopSR、Habitat、iGibson、不同团队规模和实机
- **关键结果 / 消融** · 相对强对照提升 3.87% 和 7.12%
- **适用条件 / 局限** · 依赖同步视频，摘要未量化通信成本

**可复用机制** · 把训练位姿约束与部署位姿输入分开消融

<a id="paper-152566"></a>

## See, Read, Compare: Candidate-Aware Verification for Agent Test-Time Scaling

[官方论文页](https://neurips.cc/virtual/2026/poster/152566) · [作者来源](https://openreview.net/forum?id=SBCpjDSgYq)

- **问题 / 瓶颈** · 固定评分表和孤立成品会遗漏实际验证步骤
- **核心创新 / 方法** · 将各候选轨迹按定位、假设、干预和验证摘要，再线性复杂度锦标赛
- **Baseline** · 不执行代码的验证器
- **Benchmark** · SWE-bench Verified、Terminal-Bench 2 和混合生成器
- **关键结果 / 消融** · 胜过所比执行自由方法，未报告数值
- **适用条件 / 局限** · 不能替代真实测试，依赖轨迹摘要忠实

**可复用机制** · 高代价执行之前先对候选提交做证据配对筛选

<a id="paper-150379"></a>

## SeeSE3: The Emergence of 3D Space in Vision Features

[官方论文页](https://neurips.cc/virtual/2026/poster/150379) · [作者来源](https://openreview.net/forum?id=iW8SfqJzsb)

- **问题 / 瓶颈** · 预测深度准确不能说明潜空间遵循三维关系
- **核心创新 / 方法** · 以邻域对齐及几何适配器诊断，并用潜空间完成定位和测程
- **Baseline** · 图像中心的深度、法线探针作为现行方向对照
- **Benchmark** · 视觉里程计与定位，指标未报告
- **关键结果 / 消融** · 自监督特征呈现与欧氏空间相关的子空间
- **适用条件 / 局限** · 探针本身的自由度需要控制

**可复用机制** · 采用现成视觉表征前直接测试变换结构

<a id="paper-155884"></a>

## See to Believe: Segmentation by Reasoning with Visual Evidence

[官方论文页](https://neurips.cc/virtual/2026/poster/155884) · [作者来源](https://openreview.net/forum?id=277zFbS8lU)

- **问题 / 瓶颈** · 纯文本理由难验证哪一步定位错
- **核心创新 / 方法** · 在推导中加入区域锚词元，训练轨迹经多阶段核验
- **Baseline** · 常规显式或隐式推理分割及无锚消融
- **Benchmark** · ReasonSeg 等指代及推理分割
- **关键结果 / 消融** · ReasonSeg 提升 5.4 gIoU、6.7 cIoU，消融支持锚定
- **适用条件 / 局限** · 合成轨迹质量仍受判别验证器限制

**可复用机制** · 为视觉工具的中间结论提供独立位置证据

<a id="paper-153817"></a>

## SEGA: Spectral-Energy Guided Attention for Resolution Extrapolation in Diffusion Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/153817) · [作者来源](https://openreview.net/forum?id=IUujREirW0)

- **问题 / 瓶颈** · 均匀调 RoPE 会在结构和纹理间发生冲突
- **核心创新 / 方法** · 按去噪 latent 的空间频谱重新缩放不同位置频率
- **Baseline** · 既有无需训练的分辨率外推
- **Benchmark** · 多种目标分辨率的图像合成
- **关键结果 / 消融** · 结构与纹理同时改善，摘要未列幅度
- **适用条件 / 局限** · 依赖 DiT 位置编码和分辨率差

**可复用机制** · 分开验收全局形状和高频细节再调高分生成

<a id="paper-153238"></a>

## SEISMOS: A Statistical Signal Detection Framework for Semantic Chunking

[官方论文页](https://neurips.cc/virtual/2026/poster/153238) · [作者来源](https://openreview.net/forum?id=MiRf0wVbnB)

- **问题 / 瓶颈** · 全局相似阈值对文体及主题尺度敏感
- **核心创新 / 方法** · 用相邻句嵌入相似作为信号，检验无语义变化假设
- **Baseline** · 固定长、递归及生产语义分块
- **Benchmark** · 五个 BEIR 与留出 TREC-COVID
- **关键结果 / 消融** · 固定配置持续领先并迁移，摘要未列数值
- **适用条件 / 局限** · 邻近句相似可能漏掉跨章节照应

**可复用机制** · 固定检索器和预算，在不同文体上比较分块方法

<a id="paper-155878"></a>

## Selected-Tail Reliability in Verifier-Guided Best-of-$N$ Inference

[官方论文页](https://neurips.cc/virtual/2026/poster/155878) · [作者来源](https://openreview.net/forum?id=2A1ozLhi9p)

- **问题 / 瓶颈** · 平均裁判准确率会遗漏赢家偏差。
- **核心创新 / 方法** · 推导有限证据下的选中排序和分数乐观度，并设尾部认证预算。
- **Baseline** · 只看裁判平均质量。
- **Benchmark** · N 候选和 m 证据的理论分析。
- **关键结果 / 消融** · 公开分数偏差约按 √(log N/m) 变化。
- **适用条件 / 局限** · 真正效用伤害依赖公开与隐含分数失配。

**可复用机制** · 让采样上限随评委证据量增长，而非只随 GPU 扩展。

<a id="paper-150404"></a>

## Selection, Not Fusion: Radar-Modulated State Space Models for Radar-Camera Depth Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/150404) · [作者来源](https://openreview.net/forum?id=iI7mIVsbZn)

- **问题 / 瓶颈** · 外部分支混合可能引入噪声。
- **核心创新 / 方法** · 零初始化雷达对扫描步长和读出扰动，保留图像写入与动力学。
- **Baseline** · 预训练图像 Mamba 和额外特征混合。
- **Benchmark** · 雷达相机深度。
- **关键结果 / 消融** · 追加扫描外混合无额外增益。
- **适用条件 / 局限** · 依赖几何对齐和可靠雷达。

**可复用机制** · 从单模态等价起步，把辅助传感器用于状态选择。

<a id="paper-150272"></a>

## Selective Answering for Medical VQA via Parallel Independent Claim Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/150272) · [作者来源](https://openreview.net/forum?id=jPgQvPpJTX)

- **问题 / 瓶颈** · 统一自评会传播上一步错误。
- **核心创新 / 方法** · 分类型主张独立提示核实，确定汇总后答或拒。
- **Baseline** · 整体 VLM 判断。
- **Benchmark** · 两放射数据集，三种可复现受损设置。
- **关键结果 / 消融** · 提供可追溯拒答理由，效果幅度未核。
- **适用条件 / 局限** · 依赖拆分完整性和图像证据独立性。

**可复用机制** · 以确定规则组合证据，避免最后再用同模型覆盖分项。

<a id="paper-155118"></a>

## Selective Critique for Cost-Aware LLM Agents in Long-Horizon Decision Making

[官方论文页](https://neurips.cc/virtual/2026/poster/155118) · [作者来源](https://openreview.net/forum?id=8HBYtgJQ5y)

- **问题 / 瓶颈** · 逐步评审增加延迟和 token。
- **核心创新 / 方法** · 在可行动作上计算熵与前两名间隔并门控，在线吸收有帮助评审。
- **Baseline** · 固定或每步评审。
- **Benchmark** · 长程智能体，可靠性和成本。
- **关键结果 / 消融** · 摘要提出可降低依赖，效果数字待核。
- **适用条件 / 局限** · 需可定义可行动作集，概率可能失校准。

**可复用机制** · 评审预算优先给决策边界，并追踪内化后边界变化。

<a id="paper-151621"></a>

## Selective Disk Bispectrum: A Complete and Rotation Invariant Image Descriptor

[官方论文页](https://neurips.cc/virtual/2026/poster/151621) · [作者来源](https://openreview.net/forum?id=ZBFrV7kiwX)

- **问题 / 瓶颈** · 普通不变特征可能丢掉非角度内容。
- **核心创新 / 方法** · 构造选择性圆盘双谱及数值近似。
- **Baseline** · 经典旋转不变表示。
- **Benchmark** · 理论数值精度及旋转不变性。
- **关键结果 / 消融** · 摘要证明保留除朝向外的信息。
- **适用条件 / 局限** · 离散采样噪声与非圆支持需验证。

**可复用机制** · 按保留的等价类选不变表示，避免达成不变却失去判别。

<a id="paper-149575"></a>

## Selective Off-Policy Reference Tuning with Plan Guidance

[官方论文页](https://neurips.cc/virtual/2026/poster/149575) · [作者来源](https://openreview.net/forum?id=p7jgfBt3yz)

- **问题 / 瓶颈** · GRPO 同组全错时无有效相对奖励。
- **核心创新 / 方法** · 保持原 rollout，仅对需修复组加计划引导离策略参考更新。
- **Baseline** · GRPO。
- **Benchmark** · 三个底座八个域内外推理基准。
- **关键结果 / 消融** · 持续改善，结构权重逼近 oracle 有条件。
- **适用条件 / 局限** · 计划不准或过强将引入模仿偏差。

**可复用机制** · 只在无有效探索信号时补外部脚手架。

<a id="paper-151195"></a>

## Selective Rollout: Mid-Trajectory Termination for Multi-Sample Agent RL

[官方论文页](https://neurips.cc/virtual/2026/poster/151195) · [作者来源](https://openreview.net/forum?id=cFDtppAAdg)

- **问题 / 瓶颈** · 相同动作分支消耗重复预算。
- **核心创新 / 方法** · 以平均两两前缀编辑距离单阈值截断。
- **Baseline** · 继续完整 rollout。
- **Benchmark** · 多样采样代理 RL。
- **关键结果 / 消融** · 摘要提出单参数门；量化待核。
- **适用条件 / 局限** · 距离未必反映后续分岔，迟分岔任务需保护。

**可复用机制** · 动态停止前同时评估节省和错杀后来分支。
