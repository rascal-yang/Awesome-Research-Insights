# NeurIPS 2026 论文卡 7

[会议索引](README.md)

<a id="paper-155683"></a>

## IdealCache: Rethinking Cache Scheduling in Diffusion Transformers via Ideal Trajectories

[官方论文页](https://neurips.cc/virtual/2026/poster/155683) · [作者来源](https://openreview.net/forum?id=3jq55sxmcq)

- **问题 / 瓶颈** · 轨迹匹配会把未经缓存的参考输出当成质量上限。
- **核心创新 / 方法** · 从候选目标解构造轨迹集合，用图汇总后以约束最短路径找非均匀缓存日程。
- **Baseline** · 以参考去噪状态为目标的已有缓存方法。
- **Benchmark** · Qwen-Image、Qwen-Image-Edit、HunyuanVideo，比较质量与速度。
- **关键结果 / 消融** · 报告分别提速 6.35、5.84 和 4.32 倍，质量相当或更优。
- **适用条件 / 局限** · 候选目标和搜索成本、日程能否复用待核。

**可复用机制** · 在包含目标生成与日程搜索的完整耗时下对照逐步误差目标。

<a id="paper-152556"></a>

## IDEAL: In-DEpth ALignment Makes A Discrete Representation AutoEncoder

[官方论文页](https://neurips.cc/virtual/2026/poster/152556) · [作者来源](https://openreview.net/forum?id=SFMjikixfq)

- **问题 / 瓶颈** · 仅用深层语义特征会丢细节，量化使损失更严重。
- **核心创新 / 方法** · 量化表示同时学习浅层局部结构和深层语义对齐。
- **Baseline** · 已有表示自编码器及离散生成对照。
- **Benchmark** · ImageNet 重建 rFID 和自回归生成 gFID。
- **关键结果 / 消融** · rFID 0.61，较先前最好低 0.28；gFID 1.89。
- **适用条件 / 局限** · 依赖视觉教师层间互补性，其他分辨率和域待核。

**可复用机制** · 在相同码率下分别验证浅层对细节与深层对语义的贡献。

<a id="paper-153659"></a>

## IDEAL: Interaction Dynamics and Force-Aware Learning for Dual-Humanoid Collaborative Manipulation

[官方论文页](https://neurips.cc/virtual/2026/poster/153659) · [作者来源](https://openreview.net/forum?id=JhPYWytFsc)

- **问题 / 瓶颈** · 闭链交互与局部观测使只模仿运动难保持两人协同力。
- **核心创新 / 方法** · 从双人视频得到并校正参考运动，再根据刚体和接触约束建立力参考以指导强化学习。
- **Baseline** · 既有双人形模仿和协作路线，具体名称待核。
- **Benchmark** · 双人形协同操作，覆盖模拟和实体机器人。
- **关键结果 / 消融** · 摘要称可在两类环境完成稳健协作，未给数值或消融。
- **适用条件 / 局限** · 依赖视频重建、接触和动力学模型；人机近距离应用待验证。

**可复用机制** · 在普通协同搬运中分别测运动同步、载荷分担和滑移，筛查仅运动模仿的缺口。

<a id="paper-151393"></a>

## IDEA: Unwrapping Visual Black-box Models by Interaction Decomposition

[官方论文页](https://neurips.cc/virtual/2026/poster/151393) · [作者来源](https://openreview.net/forum?id=azDcnhfVNx)

- **问题 / 瓶颈** · 单一概念重要性不能识别上下文依赖。
- **核心创新 / 方法** · 黑盒事后分解概念与语境的预测信息，无须任务专用概念标注。
- **Baseline** · 传统标量概念重要性方法。
- **Benchmark** · 受控和真实视觉评测，判断交互模式是否可见。
- **关键结果 / 消融** · 作者称能揭示标量分数未呈现的依赖。
- **适用条件 / 局限** · 信息估计及概念边界对结果的影响待核。

**可复用机制** · 在概念跨背景配对时检查交互项，定位由背景共同驱动的预测。

<a id="paper-155537"></a>

## Idempotency Exposes Consistency Problems in Sparse Autoencoders

[官方论文页](https://neurips.cc/virtual/2026/poster/155537) · [作者来源](https://openreview.net/forum?id=4rnCZcVRKZ)

- **问题 / 瓶颈** · 低重建误差可能与活跃特征集不稳并存。
- **核心创新 / 方法** · 将解码结果重新编码，比较稀疏坐标、范数、输入缩放敏感性；另加入辅助幂等损失。
- **Baseline** · 常规稀疏自编码器及有无辅助损失。
- **Benchmark** · 多种稀疏自编码器、单潜变量复原、缩放敏感性。
- **关键结果 / 消融** · 多数模型离幂等很远，观察到范数增长与活跃集合变化；辅助损失可缓和。
- **适用条件 / 局限** · 幂等性与真实语义的关系及牺牲的重建质量待核。

**可复用机制** · 给特征字典加重编码回归，分报坐标变化、范数与重建。

<a id="paper-151829"></a>

## Identifiable alignment of unpaired representations

[官方论文页](https://neurips.cc/virtual/2026/poster/151829) · [作者来源](https://openreview.net/forum?id=XeeLVJHtXH)

- **问题 / 瓶颈** · GW 耦合不直接给唯一映射，仅匹配边缘分布也无法识别映射。
- **核心创新 / 方法** · 在度量测度空间上检查局部距离分布的单射性，将耦合化为凸线性规划，再估计地图。
- **Baseline** · GWOT、GAN 映射及监督对齐。
- **Benchmark** · 理论比较同源点无配对样本与独立样本，并与监督基线实证对照。
- **关键结果 / 消融** · 分情况证明有限样本与渐近可识别；算法达到或超过监督基线。
- **适用条件 / 局限** · 局部距离同构或采样噪声过大时可能缺少区分度。

**可复用机制** · 把可辨识诊断放到昂贵拟合前，避免将训练损失低误读成唯一对齐。

<a id="paper-150669"></a>

## Identification and Bounding of Joint Expectation over Potential Outcomes

[官方论文页](https://neurips.cc/virtual/2026/poster/150669) · [作者来源](https://openreview.net/forum?id=gMaaGOx3Yl)

- **问题 / 瓶颈** · 分别观察两个边缘结果不足以确定个体效应分布。
- **核心创新 / 方法** · 在同单调和反单调假设下识别联合函数期望；无此假设时为两类函数构造锐界。
- **Baseline** · 摘要未列命名估计基线；比较有无相依假设的识别范围。
- **Benchmark** · 模拟和真实数据示例，分析离散、连续和混合结果。
- **关键结果 / 消融** · 推导统一识别方式及个体效应矩的边界。
- **适用条件 / 局限** · 需要逐一核实函数类别及其假设；观察数据不能直接验证个体配对。

**可复用机制** · 同时报告可识别边缘、无依赖假设的区间、以及假设下的点估计。

<a id="paper-149969"></a>

## Identified-Set Geometry of Distributional Model Extraction under Top-K Censored API Access

[官方论文页](https://neurips.cc/virtual/2026/poster/149969) · [作者来源](https://openreview.net/forum?id=lqDgPjh2zT)

- **问题 / 瓶颈** · 只限制可见分数不能从分布恢复受限推断能力安全。
- **核心创新 / 方法** · 用理论刻画接口可观测信息下的分布不确定性，并用独立评测比较能力迁移风险。
- **Baseline** · 不同分数可见性和输出接口条件。
- **Benchmark** · Qwen3 数学推理设置，测分布误差与能力迁移。
- **关键结果 / 消融** · 摘要显示二者可显著分离；只看分布恢复会漏估风险。
- **适用条件 / 局限** · 证据限所测接口与数学教师模型。

**可复用机制** · 防御侧审计同时做两类检验，避免用单一分布指标作泄漏保证。

<a id="paper-149053"></a>

## Identifying and Mitigating Diversity Collapse in Zero-Shot Personalization with I2I Editing Models

[官方论文页](https://neurips.cc/virtual/2026/poster/149053) · [作者来源](https://openreview.net/forum?id=tDe4M34lN8)

- **问题 / 瓶颈** · 图像身份与提示对齐较强时，多种种子仍可能产生高度相似结果。
- **核心创新 / 方法** · 发现潜词元轨迹过度对齐，训练外仅干预早期生成潜词元的注意输出，保持图文条件词元。
- **Baseline** · FLUX.1 Kontext、FLUX.2 默认推理。
- **Benchmark** · 多主题与提示，测 Vendi、LPIPS、身份和文本吻合。
- **关键结果 / 消融** · Kontext 上 Vendi 1.546 到 2.066，LPIPS 0.475 到 0.621，条件保真小幅下降。
- **适用条件 / 局限** · 其他编辑架构及高保真身份场景待核。

**可复用机制** · 用固定条件、多种子试验画出多样性和保真度的折中。

<a id="paper-151974"></a>

## Identifying Latent Neural Dynamics with Recognition-Parameterized Gaussian Process Dynamical Systems

[官方论文页](https://neurips.cc/virtual/2026/poster/151974) · [作者来源](https://openreview.net/forum?id=WQv6IOqNHC)

- **问题 / 瓶颈** · 不同观测生成成分的错设会扭曲潜状态和动态估计。
- **核心创新 / 方法** · 以高斯过程非参数地建模状态转移，用识别参数化模型隐式连接观测。
- **Baseline** · 显式流场、观测映射和响应噪声的生成建模路线。
- **Benchmark** · 合成数据及真实神经记录，观察行为相关潜变量。
- **关键结果 / 消融** · 摘要报告发现有意义的行为相关状态和动态。
- **适用条件 / 局限** · 识别参数化和真实潜动态可验证程度待核。

**可复用机制** · 从生成观测族失配的模拟出发，比较识别方案是否减少潜轨迹偏差。

<a id="paper-151733"></a>

## Identifying Structural Biases from Causal Mechanism Shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/151733) · [作者来源](https://openreview.net/forum?id=YUeprsuXFc)

- **问题 / 瓶颈** · 独立同分布与无潜变量假设失效会误导因果发现。
- **核心创新 / 方法** · 将相关机制变化写成互信息判据，按节点分类偏差类型。
- **Baseline** · 现有结构偏差发现方法；名称待核。
- **Benchmark** · 合成与真实数据，评价受影响变量集及偏差类型。
- **关键结果 / 消融** · 摘要称能准确恢复受影响节点及类型并明显领先对照。
- **适用条件 / 局限** · 依赖多环境和识别条件，环境共同变化的影响待核。

**可复用机制** · 拟因果图前单列机制协变诊断，避免把跨环境关联直接当因果边。

<a id="paper-150886"></a>

## i-DEQ: A stable inertial Deep Equilibrium model for image restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/150886) · [作者来源](https://openreview.net/forum?id=efDZxWqk5d)

- **问题 / 瓶颈** · 原平衡模型推理成本高，训练和粗初始化下不稳定。
- **核心创新 / 方法** · 在显式非凸正则框架下为求解迭代引入动量，由理论给出收敛与加速条件。
- **Baseline** · 常规 DEQ 与已有恢复方法。
- **Benchmark** · 多种线性和非线性逆问题，比较重建、推理及初值敏感性。
- **关键结果 / 消融** · 恢复质量相当，推理时间约减半，作者称训练更稳。
- **适用条件 / 局限** · 受正则、迭代与收敛假设限制，其他问题待核。

**可复用机制** · 比较目标残差、解的质量与时延，检验动量是在省步数还是改变解。

<a id="paper-151442"></a>

## iDETR: Implicit DETR for Tiny Object Detection

[官方论文页](https://neurips.cc/virtual/2026/poster/151442) · [作者来源](https://openreview.net/forum?id=afWSKToToO)

- **问题 / 瓶颈** · 离散特征格点定位误差大，多尺度成本高。
- **核心创新 / 方法** · 隐式注意允许连续坐标采样，质心引导查询初始化；按注意头条件采样缩减开销。
- **Baseline** · 已有微小目标检测及多尺度路线。
- **Benchmark** · AI-TODv2，整体 AP、极小对象 AP、计算和内存。
- **关键结果 / 消融** · 整体 +0.2%、极小 +1.1% AP，计算降 37%；条件采样减少查询成本。
- **适用条件 / 局限** · 低分辨率是否丢失可复原信号取决于任务，跨域待核。

**可复用机制** · 等计算比较连续查询与增加特征分辨率，并按目标尺寸分桶。
