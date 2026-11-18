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
