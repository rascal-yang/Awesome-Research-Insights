# NeurIPS 2026 论文卡 13

[会议索引](README.md)

<a id="paper-150729"></a>

## Why Decoding Sharpens Without Resolving: Lock-in and Confusion in Autoregressive Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/150729) · [作者来源](https://openreview.net/forum?id=fqnkZh97lu)

- **问题 / 瓶颈** · token 概率尖锐可能来自早锁定或分支混淆。
- **核心创新 / 方法** · 在等价续写分支上分析条件后验。
- **Baseline** · 仅看 token 分布。
- **Benchmark** · 自回归推理及分支机制。
- **关键结果 / 消融** · 明确锁定与混淆两种制度。
- **适用条件 / 局限** · 结论依分支定义和可估后验。

**可复用机制** · 解码策略上线同时测路径分布与单步置信。

<a id="paper-148438"></a>

## Why Deterministic PRM Guidance Underperforms in Discrete Diffusion Reasoning

[官方论文页](https://neurips.cc/virtual/2026/poster/148438) · [作者来源](https://openreview.net/forum?id=xogwvIhOYH)

- **问题 / 瓶颈** · 无序遮罩输入不是 PRM 所熟悉的前缀。
- **核心创新 / 方法** · 诊断中间状态评分和平均池化。
- **Baseline** · 简单验证器重排及确定 PRM。
- **Benchmark** · 离散扩散推理。
- **关键结果 / 消融** · 匹配预算后确定引导优势有限，平均池化削弱。
- **适用条件 / 局限** · 其他 PRM 聚合和训练方法需测。

**可复用机制** · 先检查中间状态语义匹配再加复杂引导。

<a id="paper-152368"></a>

## Why DiT Models Underperform as Representation Learners without Long Skip Connections

[官方论文页](https://neurips.cc/virtual/2026/poster/152368) · [作者来源](https://openreview.net/forum?id=TaIg0lLzG9)

- **问题 / 瓶颈** · 生成主干不是都能读出优越表示。
- **核心创新 / 方法** · 控制跳接内容，识别噪声信息路径。
- **Baseline** · 原 DiT、不同跳接。
- **Benchmark** · 扩散特征表征学习。
- **关键结果 / 消融** · 长跳接的关键是传噪声而非任意信息。
- **适用条件 / 局限** · 其他架构/噪声日程需验。

**可复用机制** · 将可用于重建的旁路和有用语义分别测。

<a id="paper-151149"></a>

## Why Do DiT Editors Drift? Plug-and-Play Low Frequency Alignment in VAE Latent Space

[官方论文页](https://neurips.cc/virtual/2026/poster/151149) · [作者来源](https://openreview.net/forum?id=ceVqStm5S2)

- **问题 / 瓶颈** · 逐轮 DiT 变动累积成语义移位。
- **核心创新 / 方法** · 免训练校准 VAE latent 的低频项，分异 DiT 与 VAE 误差。
- **Baseline** · 普通 DiT 编辑。
- **Benchmark** · 多轮一致性及视觉保真。
- **关键结果 / 消融** · 两轴有改善。
- **适用条件 / 局限** · 强低频改动才是目标时需放开约束。

**可复用机制** · 先定位误差频带再保护非目标内容。

<a id="paper-149819"></a>

## Why Do Time Series Models Need Long Context Windows?

[官方论文页](https://neurips.cc/virtual/2026/poster/149819) · [作者来源](https://openreview.net/forum?id=n51PuFNKYi)

- **问题 / 瓶颈** · 长窗成本大，关键统计可能比完整历史短。
- **核心创新 / 方法** · 用候选生成过程的后验平均解释窗口效果。
- **Baseline** · 不同历史窗口和架构。
- **Benchmark** · 合成与真实预测时序。
- **关键结果 / 消融** · 摘要报告支持重新设计上下文。
- **适用条件 / 局限** · 依赖生成过程可辨认。

**可复用机制** · 长上下文可先用于估计统计状态，再压缩成预测条件。

<a id="paper-152913"></a>

## Why Geometric Continuity Emerges in Deep Neural Networks: Residual Connections and Rotational Symmetry Breaking

[官方论文页](https://neurips.cc/virtual/2026/poster/152913) · [作者来源](https://openreview.net/forum?id=PT9wd2ehVL)

- **问题 / 瓶颈** · 二者可能共同变化，机制难辨。
- **核心创新 / 方法** · 对照保留旋转的非线性及普通激活，测权重连续性。
- **Baseline** · 旋转保留激活。
- **Benchmark** · 残差网络与 Transformer 权重。
- **关键结果 / 消融** · 摘要指出对称破缺后才保持连续。
- **适用条件 / 局限** · 限所测激活和权重诊断。

**可复用机制** · 分析跨层迁移前测试坐标系是否有机制稳定下来。

<a id="paper-149300"></a>

## Why Heavy-Tailed Weights Predict Model Quality

[官方论文页](https://neurips.cc/virtual/2026/poster/149300) · [作者来源](https://openreview.net/forum?id=rEXrPkLsO4)

- **问题 / 瓶颈** · 经验谱分数可能只有相关性。
- **核心创新 / 方法** · 建边缘似然模型估可解释的最优尾重。
- **Baseline** · 经验重尾度量。
- **Benchmark** · 大型深度模型训练。
- **关键结果 / 消融** · 摘要报告可预测过拟合。
- **适用条件 / 局限** · 依赖先验和参数范围。

**可复用机制** · 仅用权重统计做监控时，先按训练阶段校准。

<a id="paper-153410"></a>

## Why Latent Actions Fail, and How to Prevent It

[官方论文页](https://neurips.cc/virtual/2026/poster/153410) · [作者来源](https://openreview.net/forum?id=LWmFD8ITV8)

- **问题 / 瓶颈** · 重建未来像素可诱导潜动作编码背景等不可控扰动。
- **核心创新 / 方法** · 在偏向可控信息的空间学潜动作。
- **Baseline** · 普通重建目标。
- **Benchmark** · 线性与非线性潜动作模型。
- **关键结果 / 消融** · 分析说明外因泄漏与常见补救的条件。
- **适用条件 / 局限** · 现实数据的可控子空间需单独验证。

**可复用机制** · 迁移动作表征时改变背景和对象外部运动，测潜动作是否保持。

<a id="paper-152121"></a>

## Why Learning Rediscovers the Closed-Form Diagonal Regularizer

[官方论文页](https://neurips.cc/virtual/2026/poster/152121) · [作者来源](https://openreview.net/forum?id=VMdJK3PCBi)

- **问题 / 瓶颈** · 表达空间太小会让学习仅重发现解析规则。
- **核心创新 / 方法** · 通过声学房间仿真对照逐谱模式及跨模式岭更新。
- **Baseline** · 闭式、逐房间最优与学习式对角正则。
- **Benchmark** · FEM 声学房间与不同观测窗口。
- **关键结果 / 消融** · 闭式近最优，跨模式耦合提供额外空间。
- **适用条件 / 局限** · 结果针对所测条件。

**可复用机制** · 可用闭式求解的受限族中先验证剩余误差是否只能靠更丰富表示消除。

<a id="paper-153556"></a>

## Why Muon Outperforms Adam: A Curvature Perspective

[官方论文页](https://neurips.cc/virtual/2026/poster/153556) · [作者来源](https://openreview.net/forum?id=KWe4ab5CCr)

- **问题 / 瓶颈** · 同样一阶收益可带来不同二阶损失。
- **核心创新 / 方法** · 用归一化方向锐度解释 Muon 与 Adam。
- **Baseline** · Adam。
- **Benchmark** · 局部二次分析和曲率分组实证。
- **关键结果 / 消融** · Muon 有较小二阶代价。
- **适用条件 / 局限** · 依赖本地曲率近似。

**可复用机制** · 优化器赢在步长或方向是不同机制，应分别测量。

<a id="paper-152425"></a>

## Why Pass@k Optimization Can Degrade Pass@1: Prompt Interference in LLM Post-Training

[官方论文页](https://neurips.cc/virtual/2026/poster/152425) · [作者来源](https://openreview.net/forum?id=TCynOWswES)

- **问题 / 瓶颈** · 优化多样本命中可能因提示间干扰拉低单发效果。
- **核心创新 / 方法** · 分析两目标更新方向并做数学与代码对照。
- **Baseline** · 只优化 pass@k 或 pass@1。
- **Benchmark** · 可验证推理及编程。
- **关键结果 / 消融** · 摘要指出可见取舍。
- **适用条件 / 局限** · 依赖任务分布与验证预算。

**可复用机制** · 若买不起重试，不能用多样本成功替代单次可靠性。

<a id="paper-152363"></a>

## Why Routers Freeze: Infinite Width Learning Dynamics for Mixture of Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/152363) · [作者来源](https://openreview.net/forum?id=TccaEvFVmc)

- **问题 / 瓶颈** · 专家变宽而路由有效学习率可能归零。
- **核心创新 / 方法** · 无限宽理论比较标准参数化等条件。
- **Baseline** · 标准参数化、软及 Top-K 路由。
- **Benchmark** · SGD、Adam 与有限宽训练。
- **关键结果 / 消融** · 标准参数化下理论路由一步后冻结，实测同趋势。
- **适用条件 / 局限** · 限固定专家数等设定。

**可复用机制** · 扩宽时分别跟踪路由和专家更新尺度。

<a id="paper-150811"></a>

## Why Speculative Decoding Works Better Than Predicted on Sparse MoE Models

[官方论文页](https://neurips.cc/virtual/2026/poster/150811) · [作者来源](https://openreview.net/forum?id=fC3FzfodMG)

- **问题 / 瓶颈** · 只看每步活跃权重低估时间重叠。
- **核心创新 / 方法** · 从路由重叠估独立专家数并预测加速。
- **Baseline** · 仅使用参数量的成本模型。
- **Benchmark** · 低批量稀疏 MoE 推测解码。
- **关键结果 / 消融** · 独立专家数误差低于 4%。
- **适用条件 / 局限** · 低批量和 GPU 行为依赖部署。

**可复用机制** · 以实际专家访存路径估验证成本。

<a id="paper-151626"></a>

## Why Struggle with Continuous Latents? Interpretable Discrete Latent Reasoning via Rendered Compression

[官方论文页](https://neurips.cc/virtual/2026/poster/151626) · [作者来源](https://openreview.net/forum?id=Z9x8Ex4A4f)

- **问题 / 瓶颈** · 连续状态缺少清晰行为锚。
- **核心创新 / 方法** · 把连续潜状态转成显式词元。
- **Baseline** · 普通连续潜推理。
- **Benchmark** · 潜推理语义及可控性。
- **关键结果 / 消融** · 摘要报告形成可解释的结构。
- **适用条件 / 局限** · 未给多任务准确和解码成本。

**可复用机制** · 中间监督需要稳定单位时可先比较离散化是否保留求解信息。

<a id="paper-155239"></a>

## Why Transformers Struggle with Distribution-Independent In-Context Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/155239) · [作者来源](https://openreview.net/forum?id=7Ci5cBtBUO)

- **问题 / 瓶颈** · 域内接近满分仍可在变分布时陡降。
- **核心创新 / 方法** · 比较受控回归任务、尺度和支持偏移。
- **Baseline** · 最小二乘与核方法。
- **Benchmark** · 不同多项式与训练分布。
- **关键结果 / 消融** · Transformer 出现传统基线没有的断崖。
- **适用条件 / 局限** · 证据主要在特定上下文任务。

**可复用机制** · 需要稳定外推时将显式拟合列为基线。

<a id="paper-148890"></a>

## WILD: Widely Linear Conditioning for Time Series Forecasting

[官方论文页](https://neurips.cc/virtual/2026/poster/148890) · [作者来源](https://openreview.net/forum?id=uQqn3Dq2Xm)

- **问题 / 瓶颈** · 单一频率可过度支配时序权重。
- **核心创新 / 方法** · 做数据相关频谱预处理，另可混合实虚部。
- **Baseline** · 普通时序骨干和消融。
- **Benchmark** · 时间序列预测。
- **关键结果 / 消融** · 消融指频谱重配是主因。
- **适用条件 / 局限** · 复数混合收益依任务而变。

**可复用机制** · 先诊断频域失衡，再考虑扩大注意力。

<a id="paper-149811"></a>

## Winning the Symmetry Lottery: Learning Invariance from Data Augmentations with Transformers

[官方论文页](https://neurips.cc/virtual/2026/poster/149811) · [作者来源](https://openreview.net/forum?id=nBGsp2c8X6)

- **问题 / 瓶颈** · 常用扩增无法保证任意对称性可学。
- **核心创新 / 方法** · 对照保角和非保角变换及不同子群。
- **Baseline** · 不同行为对称增广。
- **Benchmark** · Transformer 不变性学习。
- **关键结果 / 消融** · 更容易学保角及基本变换。
- **适用条件 / 局限** · 依赖模型与所测变换。

**可复用机制** · 假定架构可靠数据学不变性前，按目标对称族校验。

<a id="paper-151087"></a>

## Within-Model vs Between-Prompt Variability in Large Language Models for Creative Tasks

[官方论文页](https://neurips.cc/virtual/2026/poster/151087) · [作者来源](https://openreview.net/forum?id=d535njwZHX)

- **问题 / 瓶颈** · 单样本混合模型内随机性和提示设定差异
- **核心创新 / 方法** · 对比鼓励生成与限制格式的提示方差
- **Baseline** · 不同提示策略和模型规模
- **Benchmark** · 开放创意任务；组内与组间变动
- **关键结果 / 消融** · 限制性提示压缩输出分布，单样本不稳定
- **适用条件 / 局限** · 创意评分随评审方法而变

**可复用机制** · 模型选型同时报告样本内表现分布和提示敏感性

<a id="paper-148579"></a>

## WORD: Diffusion-Based Posterior Inference for Online Goal Recognition

[官方论文页](https://neurips.cc/virtual/2026/poster/148579) · [作者来源](https://openreview.net/forum?id=wkpsUDF7X4)

- **问题 / 瓶颈** · 点预测在早期暧昧环境容易高置信地误判
- **核心创新 / 方法** · 以扩散 posterior 追踪各种目标可能性
- **Baseline** · 过滤和分类式目标观察器
- **Benchmark** · 歧义环境；概率校准与自信但错误率等
- **关键结果 / 消融** · 摘要报告四指标共同改善
- **适用条件 / 局限** · 需确保候选目标空间覆盖且训练数据足够

**可复用机制** · 对机器人意图推断增加何时该等待含新信息的验证

<a id="paper-149004"></a>

## World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry

[官方论文页](https://neurips.cc/virtual/2026/poster/149004) · [作者来源](https://openreview.net/forum?id=tWNWfy455E)

- **问题 / 瓶颈** · 罕见状态上的轨迹难用当前训练数据判可信
- **核心创新 / 方法** · 利用前逆不对称与前向 rollout 做校验
- **Baseline** · 既有自改进世界模型
- **Benchmark** · MiniGrid、RoboMimic、ManiSkill 九项
- **关键结果 / 消融** · 两倍样本效率，下游性能多于 22% 提升
- **适用条件 / 局限** · 不保证逆向一致即真实动力学

**可复用机制** · 给新想象轨迹同时用外部动力学与逆向一致筛选

<a id="paper-139687"></a>

## WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis

[官方论文页](https://neurips.cc/virtual/2026/poster/139687) · [作者来源](https://openreview.net/forum?id=Ab6N5V6cP2)

- **问题 / 瓶颈** · 物体齐全时仍可能无法完成流程
- **核心创新 / 方法** · 由动作链和状态模式检验 3D 世界代码
- **Baseline** · 多种模拟生成器，摘要未列名单
- **Benchmark** · WorldCoder-Bench 上的物理任务
- **关键结果 / 消融** · 主要失败为状态模式漂移和交互链断裂
- **适用条件 / 局限** · 任务模板和模拟器规则限制推广

**可复用机制** · 为合成训练场景提供可执行交互轨迹的准入断言

<a id="paper-139051"></a>

## WorldMemArena: Evaluating Multimodal Agent Memory Through Action–World Interaction

[官方论文页](https://neurips.cc/virtual/2026/poster/139051) · [作者来源](https://openreview.net/forum?id=o06F424mDf)

- **问题 / 瓶颈** · 存得更多不代表操作中能用到
- **核心创新 / 方法** · 以动作和环境互动方式测试视觉证据与记忆
- **Baseline** · 写入、存储及带脚手架等记忆方法
- **Benchmark** · WorldMemArena，不同领域与真实轨迹
- **关键结果 / 消融** · 系统跨域不稳，视觉证据利用不足
- **适用条件 / 局限** · 摘要未报告全部结果数字，外推需选任务

**可复用机制** · 用实际行动回归检查过时状态的记忆是否更新

<a id="paper-150683"></a>

## World Models as Group Actions

[官方论文页](https://neurips.cc/virtual/2026/poster/150683) · [作者来源](https://openreview.net/forum?id=gHkKqoDxZm)

- **问题 / 瓶颈** · 画面真实不保证动作次序仍符合变换规则
- **核心创新 / 方法** · 以群作用一致性和鲁棒性衡量变换与 rollout
- **Baseline** · 原视频世界模型
- **Benchmark** · GAC、GAR 和视觉质量
- **关键结果 / 消融** · 结构指标改善，感知质量未下降
- **适用条件 / 局限** · 动作需有可刻画的群结构

**可复用机制** · 对可逆运动测试复合操作和长时漂移

<a id="paper-149768"></a>

## World Motion Models: Flexible Sequence Modeling of SE(3) Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/149768) · [作者来源](https://openreview.net/forum?id=nTTIRxpVbW)

- **问题 / 瓶颈** · 为每种运动任务训练独立模型难复用
- **核心创新 / 方法** · 在同一轨迹模型改变掩码，切换控制、运动学及重定向等
- **Baseline** · 各任务专用方法，摘要未列名称
- **Benchmark** · 六种三维视觉和机器人应用
- **关键结果 / 消融** · 摘要报告多任务强表现，未列数值
- **适用条件 / 局限** · 要求任务能写成 SE(3) 条件建模

**可复用机制** · 将动作未来、可见约束和补全统一成可核查接口

<a id="paper-153356"></a>

## WorldPrism: 3D Consistency for Video World Models via Bidirectional Cross-Space Verification

[官方论文页](https://neurips.cc/virtual/2026/poster/153356) · [作者来源](https://openreview.net/forum?id=M04rf81e1H)

- **问题 / 瓶颈** · 单平面运动无法检验稳定世界坐标。
- **核心创新 / 方法** · 跨空间双向一致作 RL 奖励，不改骨干。
- **Baseline** · 原视频生成器。
- **Benchmark** · 时空 3D 一致性。
- **关键结果 / 消融** · 摘要报告改进，幅度未核。
- **适用条件 / 局限** · 依赖运动估计和重建质量。

**可复用机制** · 世界模型奖励分别验像素动态与几何动态互证。

<a id="paper-138917"></a>

## WorldReasonBench: Human-Aligned Stress Testing of Video Generators as Future World-State Predictors

[官方论文页](https://neurips.cc/virtual/2026/poster/138917) · [作者来源](https://openreview.net/forum?id=x1JYbqADOo)

- **问题 / 瓶颈** · 视频逼真不说明符合给定行为。
- **核心创新 / 方法** · 用人类对齐的未来状态变化任务分层评。
- **Baseline** · 常规视频画质榜。
- **Benchmark** · WorldReasonBench。
- **关键结果 / 消融** · 摘要提出动作后果诊断，数字待核。
- **适用条件 / 局限** · 可能有多个合理未来。

**可复用机制** · 将外观、因果可行性和动作符合分开验。

<a id="paper-155980"></a>

## WorldSR: Harnessing World Knowledge Search for Grounded Image Super-Resolution

[官方论文页](https://neurips.cc/virtual/2026/poster/155980) · [作者来源](https://openreview.net/forum?id=1OU9zJwyi4)

- **问题 / 瓶颈** · 仅生成先验会编造细节。
- **核心创新 / 方法** · 检索实体对齐参考，多步筛选并缓存。
- **Baseline** · 既有生成超分。
- **Benchmark** · 真实超分，结构和视觉。
- **关键结果 / 消融** · 两轴持续改善。
- **适用条件 / 局限** · 参照误匹配可能改变内容。

**可复用机制** · 对补全域要有证据而非只提高感知锐度。

<a id="paper-149437"></a>

## World Tracing: Pixel-Aligned Geometry Beyond the Visible

[官方论文页](https://neurips.cc/virtual/2026/poster/149437) · [作者来源](https://openreview.net/forum?id=q5P5hkR2n3)

- **问题 / 瓶颈** · 仅可见表面无法输出完整几何。
- **核心创新 / 方法** · 像素对齐多层几何建不可见面。
- **Baseline** · 强重建和生成。
- **Benchmark** · 对象、场景及动态。
- **关键结果 / 消融** · 可见面和完整几何同时提高。
- **适用条件 / 局限** · 隐藏结构仍是条件推断，需标不确定。

**可复用机制** · 把观测约束和背面生成独立验。

<a id="paper-150951"></a>

## World–Value–Action Model: Implicit Planning for Vision–Language–Action Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/150951) · [作者来源](https://openreview.net/forum?id=e5WXe18VPv)

- **问题 / 瓶颈** · 直接动作预测不比较长期后果。
- **核心创新 / 方法** · 联合世界预测和轨迹价值评估。
- **Baseline** · 直接动作 VLA。
- **Benchmark** · 长时决策。
- **关键结果 / 消融** · 摘要提出理论和规划机制，量化待核。
- **适用条件 / 局限** · 价值误差或预测偏差会传递。

**可复用机制** · 单测世界模型计划能否改善行为，而非只有画面更准。

<a id="paper-155786"></a>

## WorldVLA: A Unified Vision-Language-Action and World Model

[官方论文页](https://neurips.cc/virtual/2026/poster/155786) · [作者来源](https://openreview.net/forum?id=2uT2MbEwuy)

- **问题 / 瓶颈** · 独立世界模型不保证服务控制。
- **核心创新 / 方法** · 动作约束未来图像，并以统一模型预测动作。
- **Baseline** · 独立 VLA 和世界模型。
- **Benchmark** · LIBERO、模拟及实机。
- **关键结果 / 消融** · LIBERO 97.4% 成功。
- **适用条件 / 局限** · 具体预训练和实机差异需核。

**可复用机制** · 在动作条件下评图像预测和下游策略互补。

<a id="paper-150851"></a>

## WorldVLN: Autoregressive World Action Model for Aerial Vision-Language Navigation

[官方论文页](https://neurips.cc/virtual/2026/poster/150851) · [作者来源](https://openreview.net/forum?id=etFmM8ijdJ)

- **问题 / 瓶颈** · 局部轨迹正确未必导致到达。
- **核心创新 / 方法** · 先让视频先验学导航动态，再 Action-aware GRPO。
- **Baseline** · 常规航空 VLN。
- **Benchmark** · 仿真与零样本实地无人机。
- **关键结果 / 消融** · 摘要报告可转实机，幅度未核。
- **适用条件 / 局限** · 真实风和闭环安全仍需监控。

**可复用机制** · 长程导航以动作条件状态展开评每段价值。

<a id="paper-155912"></a>

## WovenAnchor Matcher: Specialized Intra- and Inter-Image Context Modeling for Feature Matching

[官方论文页](https://neurips.cc/virtual/2026/poster/155912) · [作者来源](https://openreview.net/forum?id=1tYCWPWHHq)

- **问题 / 瓶颈** · 统一注意力难同时处理局部纹理和对应关系。
- **核心创新 / 方法** · 以专用双模块聚合半稠密上下文。
- **Baseline** · 统一或换不同模块的对照。
- **Benchmark** · 图像几何特征匹配。
- **关键结果 / 消融** · 去一模块均降准确率。
- **适用条件 / 局限** · 依赖数据含多视角覆盖。

**可复用机制** · 给局部一致和跨图定位用各自交互结构。

<a id="paper-152115"></a>

## WsiSSM: A Weakly Supervised Subset-Matching Framework for Unified Classification and Segmentation of Histopathology Whole Slide Images

[官方论文页](https://neurips.cc/virtual/2026/poster/152115) · [作者来源](https://openreview.net/forum?id=VQWwM5ssWe)

- **问题 / 瓶颈** · 只有全片标签难得到可用分割。
- **核心创新 / 方法** · 用 sparse CAM 和子集匹配建块间一致。
- **Baseline** · 全图分类和常规弱分割。
- **Benchmark** · 病理全切片。
- **关键结果 / 消融** · 摘要报告分类分割改善，量化待核。
- **适用条件 / 局限** · CAM 有定位偏差且局部解释有限。

**可复用机制** · 比较类别汇总前后的局部区域证据。

<a id="paper-150454"></a>

## WTF?! Simulation-Free Reinforcement Learning with Wasserstein-Tilted Flow Maps

[官方论文页](https://neurips.cc/virtual/2026/poster/150454) · [作者来源](https://openreview.net/forum?id=hvPxti2lt3)

- **问题 / 瓶颈** · 轨迹采样 RL 有较高计算与噪声。
- **核心创新 / 方法** · 最优运输代价将问题化为确定性流的最优控制。
- **Baseline** · 常规 flow-map 后训练。
- **Benchmark** · 无模拟的流生成对齐。
- **关键结果 / 消融** · 给等价控制目标，实证细节待核。
- **适用条件 / 局限** · 依赖底座 drift 和有效奖励。

**可复用机制** · 先验证保底座目标的运输几何再改采样策略。

<a id="paper-150879"></a>

## WURI: Watching Unfolding Risk in Agent Interactions

[官方论文页](https://neurips.cc/virtual/2026/poster/150879) · [作者来源](https://openreview.net/forum?id=ehughQGWpW)

- **问题 / 瓶颈** · 逐步裁判昂贵且末端太迟。
- **核心创新 / 方法** · 轻量前缀风险评分。
- **Baseline** · 每步 LLM 裁判、终局检测。
- **Benchmark** · 五种泛化设置，前缀 AUDC。
- **关键结果 / 消融** · 平均领先，三设置第一。
- **适用条件 / 局限** · 早期告警需分误报漏报。

**可复用机制** · 对运行时检测量发现时刻而非只量最终检出率。

<a id="paper-148447"></a>

## X2HDR: HDR Image Generation in a Perceptually Uniform Space

[官方论文页](https://neurips.cc/virtual/2026/poster/148447) · [作者来源](https://openreview.net/forum?id=xjyKFJeXLL)

- **问题 / 瓶颈** · 线性 RGB 不匹配旧 VAE。
- **核心创新 / 方法** · PU21 编码，冻结 VAE，仅 LoRA 去噪。
- **Baseline** · 线性 RGB 输入和 LDR。
- **Benchmark** · HDR 重构及生成保真。
- **关键结果 / 消融** · 编码后 VAE 表现近 LDR，线性输入显著损坏。
- **适用条件 / 局限** · 极端亮度及后处理需验证。

**可复用机制** · 跨域低层输入先对齐可见误差尺度，避免无谓重训。

<a id="paper-153215"></a>

## X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/153215) · [作者来源](https://openreview.net/forum?id=MzMWvUkNZw)

- **问题 / 瓶颈** · 独立蒸馏丢互信息。
- **核心创新 / 方法** · 交叉注意同时合成两流。
- **Baseline** · 现有数据集蒸馏。
- **Benchmark** · VGGSound、AVE，多个 SPC。
- **关键结果 / 消融** · VGGSound 10 样本每类 8.2% 到 24.0%，AVE 跨架构提升。
- **适用条件 / 局限** · 合成样本仍可能不保真实时延。

**可复用机制** · 压缩训练集先验声画配对关系。

<a id="paper-153433"></a>

## XBRIDGE: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication

[官方论文页](https://neurips.cc/virtual/2026/poster/153433) · [作者来源](https://openreview.net/forum?id=LNfGvRotT3)

- **问题 / 瓶颈** · 模型之间状态和词表不共形。
- **核心创新 / 方法** · 构造实体锚的免解码桥。
- **Baseline** · 文本或不对齐潜通信。
- **Benchmark** · 异构 LLM 代理。
- **关键结果 / 消融** · 摘要给机制，数字待核。
- **适用条件 / 局限** · 双方实体解析须对齐。

**可复用机制** · 比较潜通信与文本时测语义、成本和可追溯。

<a id="paper-151207"></a>

## XMNoise2Clean: Cross-Modal Denoising Under Sparse Data

[官方论文页](https://neurips.cc/virtual/2026/poster/151207) · [作者来源](https://openreview.net/forum?id=cAohOPn48C)

- **问题 / 瓶颈** · 源不可见的真实属性会给合成训练引入域差。
- **核心创新 / 方法** · 估计跨模态可预测性并在不同场景测试。
- **Baseline** · 不同模态与控制设置。
- **Benchmark** · 三个真实模态及一个代理实验。
- **关键结果 / 消融** · 收益通常随可预测性增大。
- **适用条件 / 局限** · 指标限所测生成和去噪。

**可复用机制** · 做跨模态合成前先寻找无法从输入推知的目标属性。

<a id="paper-148325"></a>

## xVGAE: A Hierarchical Variational Graph Autoencoder for Exchangeable Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/148325) · [作者来源](https://openreview.net/forum?id=yfPdA2AWpR)

- **问题 / 瓶颈** · 自回归生成昂贵且可能对节点编号敏感。
- **核心创新 / 方法** · 从可交换表示构造层次图自编码器并一次生成。
- **Baseline** · 序列化或迭代图生成。
- **Benchmark** · 图统计与生成速度。
- **关键结果 / 消融** · 摘要报告快多数量级并匹配核心统计。
- **适用条件 / 局限** · 依赖图分布的交换性。

**可复用机制** · 处理无序关系结构时应按无关排列设计潜变量。

<a id="paper-149203"></a>

## You CAN Teach an Old Model New Tricks: Domain Adaptation via Complementary Subspace Expansion

[官方论文页](https://neurips.cc/virtual/2026/poster/149203) · [作者来源](https://openreview.net/forum?id=sA9M7Ut7pf)

- **问题 / 瓶颈** · 累加式适配会改变原有嵌入坐标。
- **核心创新 / 方法** · 冻结旧表示并分离域增量。
- **Baseline** · 普通微调和加性侧适配。
- **Benchmark** · 域适应检索与旧索引保留。
- **关键结果 / 消融** · 支持多种运行预算控制。
- **适用条件 / 局限** · 收益依领域数据和索引匹配。

**可复用机制** · 若重建索引昂贵，优先测试新能力是否可分离为可选分支。

<a id="paper-155144"></a>

## You Can’t Have It Both Ways: Concept Entanglement Limits Diffusion Model Unlearning

[官方论文页](https://neurips.cc/virtual/2026/poster/155144) · [作者来源](https://openreview.net/forum?id=81WMbko8Qr)

- **问题 / 瓶颈** · 激活共享子空间限制选择性擦除。
- **核心创新 / 方法** · 用表征几何与消融确定纠缠代价。
- **Baseline** · 独立评价遗忘和效用的基准。
- **Benchmark** · 生成概念的遗忘与效用。
- **关键结果 / 消融** · 理论和经验支持存在权衡。
- **适用条件 / 局限** · 受概念表示和评测影响。

**可复用机制** · 在遗忘前明确接近概念，并对它们做成对保留测试。

<a id="paper-153784"></a>

## You Don’t Need Aligned Representations: Knowledge Distillation via Random Prototype Spaces

[官方论文页](https://neurips.cc/virtual/2026/poster/153784) · [作者来源](https://openreview.net/forum?id=IgI7pI0qVB)

- **问题 / 瓶颈** · 逐坐标蒸馏假设表示形状一致。
- **核心创新 / 方法** · 匹配整体原型概率和空间原型激活。
- **Baseline** · 基于对齐的蒸馏。
- **Benchmark** · ImageNet-100、ImageNet-1K 等。
- **关键结果 / 消融** · 摘要报告 ImageNet-1K 改善 1.34%。
- **适用条件 / 局限** · 依赖代理空间覆盖。

**可复用机制** · 用共享比较基准替代直接匹配异构隐藏坐标。

<a id="paper-151652"></a>

## Youdunit: Single-Call Counterfactual Necessity in Multi-Agent LLM Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/151652) · [作者来源](https://openreview.net/forum?id=Z2GhavtsII)

- **问题 / 瓶颈** · 随机采样会造成与干预无关的分歧。
- **核心创新 / 方法** · 固定其余随机轨迹条件，测近端调用的必要性。
- **Baseline** · 其他代理调用。
- **Benchmark** · 多代理状态追踪及归因。
- **关键结果 / 消融** · 摘要报告对照可验证随机共享机制。
- **适用条件 / 局限** · 单调用必要性不能解释多步联合。

**可复用机制** · 做因果排障时先隔离一处调用并保存可复现随机条件。

<a id="paper-154227"></a>

## You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/154227) · [作者来源](https://openreview.net/forum?id=FGnWADI4yz)

- **问题 / 瓶颈** · 任意延续增量会放大随机噪声。
- **核心创新 / 方法** · 从短程轨迹估秩一方向后再外推。
- **Baseline** · 更长 RLVR 训练及直接外推。
- **Benchmark** · 可验证奖励推理。
- **关键结果 / 消融** · 摘要报告滤掉随机更新噪声。
- **适用条件 / 局限** · 依赖轨迹近线性，不宜无条件延长。

**可复用机制** · 要节省强化训练可先验证更新方向的稳定性，再对投影做有限外推。

<a id="paper-139196"></a>

## Your Benchmark Is an Empirical Measure Over Difficulty

[官方论文页](https://neurips.cc/virtual/2026/poster/139196) · [作者来源](https://openreview.net/forum?id=fCQ7KtG95S)

- **问题 / 瓶颈** · 总体题量无法保证监控局部技能进步。
- **核心创新 / 方法** · 定义两个覆盖诊断并按目标难度改写。
- **Baseline** · 原固定基准。
- **Benchmark** · 25 个常用基准。
- **关键结果 / 消融** · BenchFill 降低局部覆盖差距。
- **适用条件 / 局限** · 依赖难度估计。

**可复用机制** · 模型接近基准上限时应增加缺乏区分度的难度区间。

<a id="paper-152683"></a>

## Your Embedding Model Is SMARTer Than You Think

[官方论文页](https://neurips.cc/virtual/2026/poster/152683) · [作者来源](https://openreview.net/forum?id=RCEh14DLLt)

- **问题 / 瓶颈** · 单一全局向量压掉可对齐片段。
- **核心创新 / 方法** · 利用对比梯度早已塑造的多向量结构。
- **Baseline** · 原单向量及标准多向量检索。
- **Benchmark** · 多模态检索。
- **关键结果 / 消融** · 摘要报告有效且可用于微调。
- **适用条件 / 局限** · 索引成本未报告。

**可复用机制** · 重训检索前先验证已有池化前表征是否具有局部作用。

<a id="paper-155284"></a>

## Your Hypergradient is Skewed: Antithetic Neumann Estimation for Bilevel Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/155284) · [作者来源](https://openreview.net/forum?id=6hdVJxlWcS)

- **问题 / 瓶颈** · Neumann 连乘会放大三阶误差。
- **核心创新 / 方法** · 用成对估计修正 Neumann 近似。
- **Baseline** · 普通 Neumann 和其他估计。
- **Benchmark** · 双层优化与预测指标。
- **关键结果 / 消融** · 摘要报告至多改善 27%。
- **适用条件 / 局限** · 依赖截断与内层条件数。

**可复用机制** · 梯度含多次随机变换时需要报告高阶误差，不止均值与方差。

<a id="paper-153139"></a>

## Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor’s Internal States

[官方论文页](https://neurips.cc/virtual/2026/poster/153139) · [作者来源](https://openreview.net/forum?id=NbI2sR01d3)

- **问题 / 瓶颈** · 额外评论家占用显存和推理。
- **核心创新 / 方法** · 训练轻量探针从提示和生成隐态估计期望奖励。
- **Baseline** · 额外价值模型或传统基线。
- **Benchmark** · 多项可验证任务。
- **关键结果 / 消融** · 摘要报告稳定和效率改善。
- **适用条件 / 局限** · 依赖表示含足够价值信息。

**可复用机制** · 先测已有中间状态能否提供可信价值，再决定增配模型。

<a id="paper-148520"></a>

## Your Self-Supervised Projection Head Captures Object Co-Occurrence Statistics

[官方论文页](https://neurips.cc/virtual/2026/poster/148520) · [作者来源](https://openreview.net/forum?id=xIeX3NaTxT)

- **问题 / 瓶颈** · 通常只保留主干，可能丢失关系信息。
- **核心创新 / 方法** · 比较多种冻结模型的投影前后语义统计。
- **Baseline** · 视觉主干与投影头。
- **Benchmark** · 自监督视觉模型及对象关系。
- **关键结果 / 消融** · 主干类别信号强，投影头偏共现。
- **适用条件 / 局限** · 限所测训练方式。

**可复用机制** · 若下游需要关系信息，直接测投影后表示而非依惯例丢弃。

<a id="paper-154216"></a>

## Your Teacher Can’t Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/154216) · [作者来源](https://openreview.net/forum?id=FKhBVYNfpr)

- **问题 / 瓶颈** · 学生偏移逐步累积，后段反向 KL 指导变弱。
- **核心创新 / 方法** · 增加前瞻组奖励以关注后续可信的分支。
- **Baseline** · 普通在线策略蒸馏。
- **Benchmark** · 7B 模型和 AIME-26。
- **关键结果 / 消融** · mean@8 增 2.57 点，39k token 下 AIME-26 增 4.92 点。
- **适用条件 / 局限** · 需要能读取教师置信，摘要未给跨任务预算。

**可复用机制** · 长推理蒸馏应关注教师在学生实际未来路径上的区分力。

<a id="paper-155811"></a>

## Z0-Inf: Zeroth Order Approximation for Data Influence

[官方论文页](https://neurips.cc/virtual/2026/poster/155811) · [作者来源](https://openreview.net/forum?id=2iqx5fDrTU)

- **问题 / 瓶颈** · 大模型难重复训练或计算二阶逆。
- **核心创新 / 方法** · 通过不直接求梯度的近似估计影响。
- **Baseline** · 重训及梯度影响估计。
- **Benchmark** · 含微调的大语言模型。
- **关键结果 / 消融** · 摘要报告更低运行开销。
- **适用条件 / 局限** · 精度与参数范围未报告。

**可复用机制** · 先用低成本影响估计筛选，再对关键样本做受控复核。

<a id="paper-150080"></a>

## Zero-Shot Instruction Following in RL via Structured LTL Representations

[官方论文页](https://neurips.cc/virtual/2026/poster/150080) · [作者来源](https://openreview.net/forum?id=ksQQI405BZ)

- **问题 / 瓶颈** · 平坦指令难表示嵌套时序关系
- **核心创新 / 方法** · 用层级网络表示 LTL 并用注意力读未来子任务
- **Baseline** · 现有零样本指令条件策略
- **Benchmark** · 多种复杂域，具体任务未报告
- **关键结果 / 消融** · 摘要报告更好泛化
- **适用条件 / 局限** · 需要可形式化指令，解析误差另验

**可复用机制** · 给机器人检查顺序、条件和嵌套组合各自的泛化

<a id="paper-155109"></a>

## Zeroth-Order Sharpness-Aware Learning with Exponential Tilting

[官方论文页](https://neurips.cc/virtual/2026/poster/155109) · [作者来源](https://openreview.net/forum?id=8LXSBQlinu)

- **问题 / 瓶颈** · 常规零阶优化不直接限制损失尖锐度
- **核心创新 / 方法** · 以指数加权构造无梯度的平坦性目标
- **Baseline** · 普通零阶方法和 SAM 变体
- **Benchmark** · 分类、选择题和生成
- **关键结果 / 消融** · 泛化优于普通零阶方法，摘要未列幅度
- **适用条件 / 局限** · 代价受评价调用数和噪声影响

**可复用机制** · 用同查询预算比较稳定性、精度和内存

<a id="paper-155054"></a>

## ZNO: Stable Rational Neural Operators in the Z-Domain for Discrete-Time Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/155054) · [作者来源](https://openreview.net/forum?id=8nSlUg4WxW)

- **问题 / 瓶颈** · 普通模型可能难稳健表示近单位圆模式
- **核心创新 / 方法** · 在 Z 域构建稳定有理算子，对照经典与状态空间方法
- **Baseline** · 传统滤波和状态空间估计
- **Benchmark** · 多种离散系统、长期记忆
- **关键结果 / 消融** · 近单位圆较强，其他部分由经典方法占优
- **适用条件 / 局限** · 依赖动态近似为稳定有理形式

**可复用机制** · 选控制世界模型前测频域响应，再用长程预测误差核验

<a id="paper-153380"></a>

## ZO-F2: Low-variance Fisher preconditioner via bilinear estimation for zeroth-order optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/153380) · [作者来源](https://openreview.net/forum?id=Ln6xIlpCy8)

- **问题 / 瓶颈** · 直接估曲率时查询噪声大
- **核心创新 / 方法** · 以低方差双线性 Fisher 估计做预条件，并查白化残差
- **Baseline** · 传统零阶训练与预条件方案
- **Benchmark** · 多模型黑盒从头训练；准确与计算
- **关键结果 / 消融** · 摘要报告两项改善且有理论界
- **适用条件 / 局限** · 实际收益取决于查询成本和估计假设

**可复用机制** · 为无梯度适配同时验收白化残差与达到目标的查询数
