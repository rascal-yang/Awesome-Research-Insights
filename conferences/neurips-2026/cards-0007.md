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

<a id="paper-148764"></a>

## IFDECORATOR: Wrapping Instruction Following Reinforcement Learning with Verifiable Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/148764) · [作者来源](https://openreview.net/forum?id=vEcdUTiDxm)

- **问题 / 瓶颈** · 形式验证可能给走捷径的回答奖励。
- **核心创新 / 方法** · 用协作对抗数据过程调整难度，以 IntentCheck 门控，并以诊断独立评估异常。
- **Baseline** · 原始 Qwen2.5-32B-Instruct、GPT-4o；其他配置待核实。
- **Benchmark** · IFEval、FollowBench 和通用能力检查。
- **关键结果 / 消融** · 3,625 个训练例得到 IFEval 87.43%；FollowBench 改善 4.2%。
- **适用条件 / 局限** · 意图检查和诊断的错误率、可扩展性需核实。

**可复用机制** · 把训练任务难度和验证器忠实度分开调节，并保留独立的可靠性诊断。

<a id="paper-155215"></a>

## IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer

[官方论文页](https://neurips.cc/virtual/2026/poster/155215) · [作者来源](https://openreview.net/forum?id=7Q59ZVBlfK)

- **问题 / 瓶颈** · 仅维护几何难表示运动、消失与重现的实体。
- **核心创新 / 方法** · 逐帧因果建模复用历史上下文，在统一表示中增量更新运动、几何和对象身份。
- **Baseline** · 已有流式重建方法，具体名称待核实。
- **Benchmark** · 三维重建、位姿、空间实例追踪、开放词汇分割；InsScene4D-147K。
- **关键结果 / 消融** · 摘要报告多项优于既有流式方法，长动态序列可在线推理。
- **适用条件 / 局限** · 依赖跨时间一致的实例监督；极长序列开销待核实。

**可复用机制** · 让对象身份成为在线场景图的持久状态，避免在独立语义管线中逐帧重建关联。

<a id="paper-151662"></a>

## I Have a Stream: Making Self-Supervised Learning Work on Continuous Video

[官方论文页](https://neurips.cc/virtual/2026/poster/151662) · [作者来源](https://openreview.net/forum?id=YycCzzfac3)

- **问题 / 瓶颈** · 严格视频流不允许全局重排，标准 MAE 和对比等方法退化。
- **核心创新 / 方法** · 保留 MAE 目标，加入流感知正则和运动偏置的裁剪。
- **Baseline** · 流式的对比、蒸馏及 MAE，独立采样 MAE。
- **Benchmark** · WT++ 95 小时城市视频和多项迁移评估。
- **关键结果 / 消融** · 批内重复是主要障碍；StreamMAE 匹配所比独立采样 MAE。
- **适用条件 / 局限** · 结果基于连续城市视频及选定窗口协议。

**可复用机制** · 不打乱到达顺序时，先用批内有效观测多样性改善学习，再调跨批更新。

<a id="paper-155681"></a>

## IIDiff: Learning Cross-Domain Frequency Transitions with Diffusion Mixture-of-Experts

[官方论文页](https://neurips.cc/virtual/2026/poster/155681) · [作者来源](https://openreview.net/forum?id=3lbpq6bC01)

- **问题 / 瓶颈** · 固定频率专家不适配各域和各时步的频率变化。
- **核心创新 / 方法** · 逐步调整专家频率感受野，并据频率噪声分布估计瞬时变化以路由。
- **Baseline** · 频率专家混合和现有跨域生成基线。
- **Benchmark** · 四域 12 个时序集，KL 和 MMD。
- **关键结果 / 消融** · 摘要报告 KL 平均改善 27.59%，MMD 改善 6.00%。
- **适用条件 / 局限** · 需要稳定的频率变化估计，对不同采样率的稳健性待核实。

**可复用机制** · 路由同时依赖当前去噪阶段和观测域的频谱变化，避免专家只按静态域标签分工。

<a id="paper-152124"></a>

## Illusory Pattern Perception Drives Spurious Inference in Large Language Models

[官方论文页](https://neurips.cc/virtual/2026/poster/152124) · [作者来源](https://openreview.net/forum?id=VLcmdFfRQc)

- **问题 / 瓶颈** · 频率共现容易被模型解读为结构或因果。
- **核心创新 / 方法** · 把经典心理实验改成三类任务，对比人类和模型，并用稀疏自编码器分析。
- **Baseline** · 人类行为与多个语言模型。
- **Benchmark** · 三个模式错觉任务；分组关联和模糊事件解释。
- **关键结果 / 消融** · 模型往往强于人类地过度关联及编造因果；摘要指出若干内部特征相关。
- **适用条件 / 局限** · 内部特征关系不足以证明所有行为的因果机制。

**可复用机制** · 在评测中独立操纵真实依赖和边际频率，测模型是否凭频次误报关联。

<a id="paper-151849"></a>

## Image2Sim: Scaling Embodied Navigation via Generative Neural Simulator

[官方论文页](https://neurips.cc/virtual/2026/poster/151849) · [作者来源](https://openreview.net/forum?id=XQspWihxY2)

- **问题 / 瓶颈** · 扫描环境规模有限，纯合成环境可能跨域泛化不足。
- **核心创新 / 方法** · 用带位姿 RGB-D 提取三维特征高斯，再以几何条件单步像素流合成全景 RGB-D。
- **Baseline** · 扫描型和合成型环境，逐项对照待核实。
- **Benchmark** · 导航基准及零样本真实转移；论文生成近两万场景和逾千万训练样本。
- **关键结果 / 消融** · 摘要报告在主要基准改善且可迁移真实场景。
- **适用条件 / 局限** · 需要 RGB-D 与位姿质量；具体交互动力学边界待核实。

**可复用机制** · 让三维状态负责持续一致性，图像生成器只恢复感知细节，分别监督两部分。

<a id="paper-151641"></a>

## Image Generation for Automotive Lidar Open-vocabulary Semantic Segmentation

[官方论文页](https://neurips.cc/virtual/2026/poster/151641) · [作者来源](https://openreview.net/forum?id=Z5dOCGOl4Y)

- **问题 / 瓶颈** · 直接在文本空间匹配蒸馏得到的点特征存在模态差距。
- **核心创新 / 方法** · 从文本生成代表图像，用视觉骨干提图像特征，与已蒸馏的三维点特征匹配。
- **Baseline** · 依赖 CLIP 等图文匹配的方法。
- **Benchmark** · nuScenes、SemanticKITTI 零样本开放词汇分割。
- **关键结果 / 消融** · 摘要报告领先，具体分数待核实。
- **适用条件 / 局限** · 依赖合成原型代表性与二维到三维蒸馏质量。

**可复用机制** · 将类别定义投到已和目标传感器对齐的中间模态，避免直跨两个不对齐空间。

<a id="paper-151905"></a>

## Image Matting without Matting-Specific Annotations via Eikonal Fields

[官方论文页](https://neurips.cc/virtual/2026/poster/151905) · [作者来源](https://openreview.net/forum?id=X2jELwz645)

- **问题 / 瓶颈** · 抠图标注昂贵，粗二值分割不能表达软边界。
- **核心创新 / 方法** · 以粗前景作源，解基于图像与先验的 Eikonal 方程，转到达时间为置信加权监督。
- **Baseline** · 任务专用监督抠图方法。
- **Benchmark** · 20 项数据集指标组合；具体集合待核实。
- **关键结果 / 消融** · 13 项排名前二。
- **适用条件 / 局限** · 对粗前景和边界信号质量敏感。

**可复用机制** · 从可靠区域传播可达证据，并把不确定过渡带留为低置信监督。

<a id="paper-140042"></a>

## ImageNet FID is a Pass Check, Not a Finish Line

[官方论文页](https://neurips.cc/virtual/2026/poster/140042) · [作者来源](https://openreview.net/forum?id=cRKDUddr0V)

- **问题 / 瓶颈** · 接近的单一 FID 排名可能依赖评估参数。
- **核心创新 / 方法** · 固定每个生成器的输出，只改参考集、样本量和特征抽取器。
- **Baseline** · 常规 ImageNet 50K 与 Inception-v3 的 FID。
- **Benchmark** · 47 个生成器，另用 CLIP、DINOv2、VGG16 等。
- **关键结果 / 消融** · 相同输出在不同设置下得到不同排名。
- **适用条件 / 局限** · 结论集中于 ImageNet 类条件生成；不测人类偏好。

**可复用机制** · 用冻结样本排除采样变化，再以多协议交叉校验微小分数差是否稳健。

<a id="paper-149868"></a>

## Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering

[官方论文页](https://neurips.cc/virtual/2026/poster/149868) · [作者来源](https://openreview.net/forum?id=masWIidGAx)

- **问题 / 瓶颈** · 多图问题需要跨视角聚合，外部几何特征难直接体现可用结构。
- **核心创新 / 方法** · 把摘要词元解码为紧凑三维高斯表示，联合光度重建和下一个词元损失。
- **Baseline** · 跨视角像素匹配和注入外部三维几何的路线。
- **Benchmark** · 多个空间推理与三维理解基准，具体名称待核实。
- **关键结果 / 消融** · 摘要报告整体改善，重建也提高底层跨帧对应。
- **适用条件 / 局限** · 需要多视图重建监督，遮挡与少视角条件待核实。

**可复用机制** · 让结构化重建损失作用于少量潜变量，同时保留语言问题监督，检验几何是否迁移到下游。

<a id="paper-156043"></a>

## Imagine Before You Draw: Visual Prompt Engineering for Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/156043) · [作者来源](https://openreview.net/forum?id=0qIxwwc2xH)

- **问题 / 瓶颈** · 分离语义规划与扩散解码可能丢掉编辑所需原图细节。
- **核心创新 / 方法** · 先自回归生成语义计划词元，再在同一模型内部按计划和输入生成完整图像。
- **Baseline** · X-Omni、BLIP3o-Next 外部管线及内部生成框架。
- **Benchmark** · 类条件、文生图与编辑；保留 PSNR 和指令响应。
- **关键结果 / 消融** · 同参数规模的编辑保留 PSNR 26.76 对 19.92。
- **适用条件 / 局限** · 依赖中间词元及内部条件交互质量。

**可复用机制** · 中间计划降难度，原始输入保留细节；不要把计划作为解码器的唯一条件。

<a id="paper-150345"></a>

## Imagine, Don't Narrate: The Generative Bottleneck in World Models of Interaction Dynamics

[官方论文页](https://neurips.cc/virtual/2026/poster/150345) · [作者来源](https://openreview.net/forum?id=ipFW6QeUtY)

- **问题 / 瓶颈** · 自然语言输出可能丢掉模型已表示的状态并放大延迟。
- **核心创新 / 方法** · 用可观测真实潜变量的受控测试床比较表征预测和文字输出。
- **Baseline** · 三种 117M 至 350M 的生成模型与表征预测。
- **Benchmark** · LID-Bench 的潜变量误差、时域和运行效率。
- **关键结果 / 消融** · 摘要报告到五步文字呈现损失 89% 至 100% 的信号，表征预测更快且更准。
- **适用条件 / 局限** · 合成状态和任务的外部有效性需核查。

**可复用机制** · 以内部状态读出与末端输出的分离评估定位信息瓶颈。

<a id="paper-151209"></a>

## Imitation Dominates Reinforcement: Direct In-Context RL Is Closer to ICL Than RL

[官方论文页](https://neurips.cc/virtual/2026/poster/151209) · [作者来源](https://openreview.net/forum?id=c9GSAkKpkb)

- **问题 / 瓶颈** · 随着示例积累而提升，不代表模型在用奖励推理。
- **核心创新 / 方法** · 在保留主要上下文结构时移除或置乱奖励，并对比腐化、真实轨迹。
- **Baseline** · 真实轨迹奖励对、无奖励及置乱对照。
- **Benchmark** · 三个基准、六种模型的改进曲线。
- **关键结果 / 消融** · 改变奖励效果很小，部分腐化轨迹与真实轨迹等效。
- **适用条件 / 局限** · 针对直接传入轨迹奖励的设定，不涵盖所有推理时 RL。

**可复用机制** · 先验证增益是否真的可归因于反馈，再决定优化奖励还是演示分布。

<a id="paper-151602"></a>

## Imitation from Observations with Trajectory-Level Generative Embeddings

[官方论文页](https://neurips.cc/virtual/2026/poster/151602) · [作者来源](https://openreview.net/forum?id=ZKbWAjL1zV)

- **问题 / 瓶颈** · 离线次优数据与专家差异大时，单步动作支持约束易失败。
- **核心创新 / 方法** · 在次优轨迹上训练时序扩散，用该嵌入中的粒子熵估计优化专家轨迹似然。
- **Baseline** · 既有离线仅状态模仿方法。
- **Benchmark** · D4RL 行走与操作任务。
- **关键结果 / 消融** · 摘要报告匹配或超过既有方法。
- **适用条件 / 局限** · 依赖次优数据仍可提供可迁移时序空间。

**可复用机制** · 以轨迹级几何补充逐步支持判断，降低无专家动作时对单步预测的依赖。

<a id="paper-152450"></a>

## ImmuVis: Hyperconvolutional Foundation Models for Imaging Mass Cytometry

[官方论文页](https://neurips.cc/virtual/2026/poster/152450) · [作者来源](https://openreview.net/forum?id=T2RPhW9u1M)

- **问题 / 瓶颈** · 不同研究测量的成像标记物不同，固定输入通道违反实际分布。
- **核心创新 / 方法** · 以标记物嵌入调制超卷积，再用遮罩重建训练。
- **Baseline** · Transformer 备选模型和组件消融。
- **Benchmark** · IMC17M 的虚拟染色与分类；算力和校准。
- **关键结果 / 消融** · 摘要报告优于对照且算力更低，并采用异方差似然预测不确定性。
- **适用条件 / 局限** · 任意已支持标记子集与全新标记的效果需分开验证。

**可复用机制** · 让输入特征的语义身份决定卷积接口，使多个传感通道组合共享同个模型。

<a id="paper-149015"></a>

## Impacts of Aggregation on Model Diversity and Consumer Utility

[官方论文页](https://neurips.cc/virtual/2026/poster/149015) · [作者来源](https://openreview.net/forum?id=tTHBShRcR3)

- **问题 / 瓶颈** · 普通胜率可能奖励模型相互同质化，降低路由收益。
- **核心创新 / 方法** · 在有噪声的模型选择环境理论分析胜率，并用答案质量加权。
- **Baseline** · 普通胜率与无差异模型选择。
- **Benchmark** · 理论模型与基准数据分析；专门化及消费者效用。
- **关键结果 / 消融** · 加权胜率在论文条件下鼓励专门化并改善效用。
- **适用条件 / 局限** · 依赖质量权重与路由噪声的设定。

**可复用机制** · 评价被组合的组件时计入其擅长子域的质量幅度，避免只按总体排名激励。

<a id="paper-153488"></a>

## Imperfect Influence, Reliable Rankings: A Theory of TRAK for Data Attribution

[官方论文页](https://neurips.cc/virtual/2026/poster/153488) · [作者来源](https://openreview.net/forum?id=L0YFMm2CYO)

- **问题 / 瓶颈** · 核近似和留一风险近似的误差边界不清楚。
- **核心创新 / 方法** · 逐层分析 TRAK 近似引入的影响量误差及排序后果。
- **Baseline** · 留一风险及 TRAK 的近似组成。
- **Benchmark** · 模拟和实证归因；影响值及高低影响组的分离。
- **关键结果 / 消融** · 数值近似可有显著偏差，高低影响组仍能区分。
- **适用条件 / 局限** · 不能由组间分离推出细粒度相邻排名完全可靠。

**可复用机制** · 按用途检验归因稳定性，候选过滤与精确权重归因要用不同容错标准。

<a id="paper-154874"></a>

## Imperfect World Models are Exploitable

[官方论文页](https://neurips.cc/virtual/2026/poster/154874) · [作者来源](https://openreview.net/forum?id=AFrqAcX9ti)

- **问题 / 瓶颈** · 不完美世界模型可能颠倒真实环境中的策略优劣。
- **核心创新 / 方法** · 以策略相对偏好反转定义误导，分析大策略集并为放松判据导出安全时域。
- **Baseline** · 既有奖励投机的形式刻画。
- **Benchmark** · 理论分析策略集合与规划时域，无具体实验指标。
- **关键结果 / 消融** · 理论指出误导在大策略集几乎不可避免，放松版本可界定一定安全时域。
- **适用条件 / 局限** · 时域保证针对放松定义及给定形式条件。

**可复用机制** · 验证世界模型时检查策略排序的一致性，限制搜索远期真实价值难校准的轨迹。

<a id="paper-150321"></a>

## Implicit Bias in State Space Models and Linear Autoregressive Training

[官方论文页](https://neurips.cc/virtual/2026/poster/150321) · [作者来源](https://openreview.net/forum?id=iz9ERtKfxJ)

- **问题 / 瓶颈** · 共享参数被重复使用，各例的有效预测阶数不同。
- **核心创新 / 方法** · 将例子建模为共享参数的非齐次多项式预测器，并刻画有效阶最大间隔。
- **Baseline** · 齐次模型的隐式偏置理论。
- **Benchmark** · 线性状态空间和自回归训练的理论分析。
- **关键结果 / 消融** · 最小有效阶示例施加渐近硬边际约束，其他示例可能仅约束可行性。
- **适用条件 / 局限** · 依赖插值、方向收敛及有效阶条件。

**可复用机制** · 增加序列长度未必增加该样本影响力，按轨迹诱导的有效阶而非样本数诊断长度偏置。

<a id="paper-149406"></a>

## Implicit Bias of Mirror Flow in Homogeneous Neural Networks: Sparse and Dense Feature Learning

[官方论文页](https://neurips.cc/virtual/2026/poster/149406) · [作者来源](https://openreview.net/forum?id=qIshuUKij9)

- **问题 / 瓶颈** · 梯度流的极限间隔结果不足以刻画一般镜像流的动力学。
- **核心创新 / 方法** · 从凸对偶导出平衡关系，刻画支配间隔的渐近函数并分析速率和范数增长。
- **Baseline** · 经典梯度流与不同非齐次镜像映射。
- **Benchmark** · 合成数据及标准视觉任务，比较最大间隔、收敛及激活密度。
- **关键结果 / 消融** · 不同映射可通向同一最大间隔但激活稀疏性不同；存在很慢的收敛区间。
- **适用条件 / 局限** · 结论建立于齐次激活等条件，实测任务与速率细节待核实。

**可复用机制** · 终点指标相同也应比较表示形态和训练预算，避免过早截断得出隐式偏置结论。

<a id="paper-153972"></a>

## Implicit Drifting Policy: One-Step Action Generation via Conditional Expert Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/153972) · [作者来源](https://openreview.net/forum?id=H7VRIbdX6F)

- **问题 / 瓶颈** · 迭代采样有延迟，条件下示范稀疏使显式漂移估计病态。
- **核心创新 / 方法** · 比较观测近邻的专家动作几何与全局参照，自适应加权标量势，并检查终点是否靠近专家。
- **Baseline** · 显式漂移与现有一步生成基线。
- **Benchmark** · 二维、三维和真实操作任务，考察动作流形有效性与策略表现。
- **关键结果 / 消融** · 报告优于显式漂移，与强一步基线表现有竞争力。
- **适用条件 / 局限** · 观测近邻的质量及多模态动作覆盖限制待核实。

**可复用机制** · 以局部动作分布和全局参照的差异给一步策略提供隐式纠正信号。

<a id="paper-151746"></a>

## Implicit-Euler Value Iteration: Long-Horizon Planning via Stable Integration of the Bellman Residual Flow

[官方论文页](https://neurips.cc/virtual/2026/poster/151746) · [作者来源](https://openreview.net/forum?id=YPZmHZA1Ut)

- **问题 / 瓶颈** · 显式 Euler 解释揭示长有效时域下的步幅限制。
- **核心创新 / 方法** · 以隐式 Euler 离散 Bellman 残差流，在近似模型内规划并周期性查询真模型更新缺陷项。
- **Baseline** · 普通价值迭代及仅在近似模型上规划。
- **Benchmark** · 策略评估与控制的收缩率和迭代复杂度，另给表格 Dyna 变体。
- **关键结果 / 消融** · 任意正步幅收缩，每步因子为 1/(1+h(1−γ))；模型误差满足缩放条件时复杂度为有效时域的多对数。
- **适用条件 / 局限** · 真实 Bellman 查询或其采样替代是必要条件；大规模函数逼近需另验。

**可复用机制** · 把近似模型用作求解加速器，并让真残差决定最终固定点。

<a id="paper-154628"></a>

## Implicit Goal Conditioning via Value Disaggregation

[官方论文页](https://neurips.cc/virtual/2026/poster/154628) · [作者来源](https://openreview.net/forum?id=CB1gJdJWSh)

- **问题 / 瓶颈** · 串行子目标方法依赖测试时选择，也难覆盖非序列目标。
- **核心创新 / 方法** · 以各子目标价值的线性组合训练一个不随子目标改变的策略。
- **Baseline** · 子目标条件策略及自然对照；具名实现待核实。
- **Benchmark** · 长时域 RoboCasa、非序列目标和多目标任务，比较成功率。
- **关键结果 / 消融** · 作者报告持平或超过常见基线，并从成功率近零的行为克隆初始化解决困难任务。
- **适用条件 / 局限** · 价值组合权重、泛化和切换约束待核实。

**可复用机制** · 将子目标用于改善 critic 学习，独立检验策略端是否还需要子目标输入。

<a id="paper-156079"></a>

## Importance-Weighted Operator Learning Under Probability Measure Shifts

[官方论文页](https://neurips.cc/virtual/2026/poster/156079) · [作者来源](https://openreview.net/forum?id=0afkWPjBeM)

- **问题 / 瓶颈** · 通常重要权重依赖绝对连续，且可能无界。
- **核心创新 / 方法** · 从训练测试混合取得相对权重，用以函数为输入的核积分分类器估计。
- **Baseline** · 标准算子训练和绝对连续下的精确重要加权。
- **Benchmark** · 多种 PDE 基准与神经算子架构，测试分布偏移下误差。
- **关键结果 / 消融** · 报告偏移下提升；绝对连续下给出精确目标等式，相对权重则保持有界。
- **适用条件 / 局限** · 相对重权对应调整后的目标；实际依赖测试分布样本和估计质量。

**可复用机制** · 分别报告权重尾部、离散分辨率迁移和偏移下误差，以选平滑强度。

<a id="paper-149451"></a>

## Impossibility of Distribution-Free Predictive Inference for Individual Treatment Effects

[官方论文页](https://neurips.cc/virtual/2026/poster/149451) · [作者来源](https://openreview.net/forum?id=pyIv9zfcdd)

- **问题 / 瓶颈** · 标准可忽略性与重叠不足以辨识可预测的个体反事实差。
- **核心创新 / 方法** · 将覆盖问题连接到条件独立检验的难度，给出有限样本及渐近不可能性。
- **Baseline** · 仅依赖标准因果假设的分布无关覆盖目标。
- **Benchmark** · 连续协变量个体效应，指标为覆盖和期望区间长度。
- **关键结果 / 消融** · 要求分布无关覆盖的区间必须具有无限期望长度。
- **适用条件 / 局限** · 结论限于相应假设、目标及连续协变量，附加结构下可另行评估。

**可复用机制** · 在声称覆盖前，写明额外识别条件并把有限区间长度作为同时验收的标准。

<a id="paper-149740"></a>

## Improved Baselines with Representation Autoencoders

[官方论文页](https://neurips.cc/virtual/2026/poster/149740) · [作者来源](https://openreview.net/forum?id=nikMBZQUOk)

- **问题 / 瓶颈** · 编码器末层难保留重建细节，基线还可能需要训练第二个引导模型。
- **核心创新 / 方法** · 汇总冻结编码器末 k 层，用同一表示作为中层对齐目标，并重参数化 DiT 输出得到引导。
- **Baseline** · 原始 RAE、REPA 与 AutoGuidance。
- **Benchmark** · ImageNet-256 及文生图、导航世界模型；gFID、FDr 指标与达成指定 gFID 的轮数。
- **关键结果 / 消融** · 80 轮取得 gFID 1.06，达到无引导 gFID 2 用 35 轮，原 RAE 为 177 轮。
- **适用条件 / 局限** · 各改动的跨骨干收益及对齐系数待核实。

**可复用机制** · 把编码表征的重建能力与去噪器的中层监督分开消融，同一特征可能承担两种互补角色。

<a id="paper-155618"></a>

## Improved Leverage Score Sampling for Constrained Active Linear Regression

[官方论文页](https://neurips.cc/virtual/2026/poster/155618) · [作者来源](https://openreview.net/forum?id=4DVNqdoLKl)

- **问题 / 瓶颈** · 常规杠杆分数忽略约束或只用各向同性岭正则，浪费标签。
- **核心创新 / 方法** · 用外接椭球近似可行域，并以其形状矩阵构造椭球正则杠杆分数。
- **Baseline** · 标准和岭正则杠杆分数采样。
- **Benchmark** · 约束线性回归，测达到 1+ε 相对误差的响应查询量。
- **关键结果 / 消融** · 给出按各向异性有效维数缩放的复杂度，凸约束下改善 ε 依赖，并证明对应下界。
- **适用条件 / 局限** · 依赖已知设计矩阵和可计算的外椭球，非线性回归尚待核实。

**可复用机制** · 让标签预算偏向约束允许变化的方向，并以有效维数估计其潜在节省。

<a id="paper-148144"></a>

## Improved Robust Verifiable Federated Learning Based on Packed Secret Sharing

[官方论文页](https://neurips.cc/virtual/2026/poster/148144) · [作者来源](https://openreview.net/forum?id=zvSw7s379j)

- **问题 / 瓶颈** · 单个更新不可见，使验证稳健聚合规则变得困难。
- **核心创新 / 方法** · 重新设计打包秘密共享的降阶与点积验证，简化余弦相似度校验。
- **Baseline** · RFLPA、FLTrust 及 BGW 类计算。
- **Benchmark** · 高维联邦模型更新，关注协议正确性、通信轮次及恶意参与方鲁棒性。
- **关键结果 / 消融** · 作者报告减少通信轮次并保留 N/3 鲁棒性，支持高维更新的可行性。
- **适用条件 / 局限** · 依赖威胁模型及秘密共享设置，严格参数待核实。

**可复用机制** · 同时验证共享运算的正确性和剩余鲁棒界，再判断单个验证原语的通信优化是否有效。

<a id="paper-152218"></a>

## Improved State Mixing in Higher-order and Block Diagonal Linear Recurrent Networks

[官方论文页](https://neurips.cc/virtual/2026/poster/152218) · [作者来源](https://openreview.net/forum?id=UgQaUtjeXS)

- **问题 / 瓶颈** · 对角状态转移限制表达，密集循环计算成本高。
- **核心创新 / 方法** · 以高阶循环混合历史状态，或以块对角转移混合组内通道，并配合门控归一化和平行扫描。
- **Baseline** · 对角线性循环与线性状态空间模型。
- **Benchmark** · 合成序列与语言建模，比较预测效果、状态混合及吞吐。
- **关键结果 / 消融** · 作者报告结构混合改善效果，中等阶数或块尺寸保持有竞争力的吞吐。
- **适用条件 / 局限** · 大阶数或大块时的扫描成本、稳定性及硬件适用性待查。

**可复用机制** · 把时间轴和通道轴混合作为两个结构选项，依任务需求与吞吐分别消融。

<a id="paper-154921"></a>

## Improved techniques for fine-tuning flow models via adjoint matching: a deterministic control pipeline

[官方论文页](https://neurips.cc/virtual/2026/poster/154921) · [作者来源](https://openreview.net/forum?id=9ye0wbdavj)

- **问题 / 瓶颈** · 完整轨迹伴随计算成本高，奖励相关信号可能集中在末段。
- **核心创新 / 方法** · 把速度场控制回归到值梯度诱导目标，截取终端段计算，并允许灵活正则。
- **Baseline** · 完整伴随匹配及标准 KL 正则，具名对照待核实。
- **Benchmark** · SiT-XL/2、FLUX.2-Klein-4B，比较偏好对齐、多样性及模式保持。
- **关键结果 / 消融** · 报告截断节省计算且保持质量，对齐指标和多样性改善。
- **适用条件 / 局限** · 末段信号集中是所提设计的关键，早期高影响的任务需重验。

**可复用机制** · 在选择伴随预算前先比较沿轨迹的信号价值，并对齐成本后检查模式丢失。

<a id="paper-148140"></a>

## Improving Audit Realism with Inference-Time Compute and Deployment Scaffolds

[官方论文页](https://neurips.cc/virtual/2026/poster/148140) · [作者来源](https://openreview.net/forum?id=zzlztyx1yj)

- **问题 / 瓶颈** · 目标模型能识别被评测，可能让审计结果低估部署风险。
- **核心创新 / 方法** · 比较不同审计环境与实际部署记录，由独立评估判断真实感和评测意识。
- **Baseline** · Petri 默认审计配置及不同部署环境参考。
- **Benchmark** · Sonnet-4.6、Haiku-4.5、Opus-4.7，比较真实感胜率与自述评测意识。
- **关键结果 / 消融** · 代码场景下改变环境后 Sonnet-4.6 真实感胜率由 7% 到 18%，跨模型并非同样叠加。
- **适用条件 / 局限** · 真实感和自述是代理指标，不能替代部署风险验证。

**可复用机制** · 在将审计结果用于上线决定前，测部署与审计两类记录的可区分性。

<a id="paper-153775"></a>

## Improving Causal Explanations

[官方论文页](https://neurips.cc/virtual/2026/poster/153775) · [作者来源](https://openreview.net/forum?id=IkOHPX9dDS)

- **问题 / 瓶颈** · 不同归因方法可给出冲突解释。
- **核心创新 / 方法** · 定义四个要求，从自然总效应聚合反事实 Shapley 值并求紧界。
- **Baseline** · SHAP、LIME 和其他已有归因方法。
- **Benchmark** · 理论证明与实验佐证；数据和指标待核。
- **关键结果 / 消融** · 证明无因果假设时四个要求不能同时满足，新归因在条件下满足四项。
- **适用条件 / 局限** · 依赖可辩护的因果条件；区间宽时不能直接排序。

**可复用机制** · 出具归因时并列因果假设和区间，用敏感性分析甄别可稳定解释的变量。

<a id="paper-149052"></a>

## Improving Conditional Modeling via Inter-Class Likelihood-Ratio Maximization and Unifying Classifier-Free Guidance with Alignment Objectives

[官方论文页](https://neurips.cc/virtual/2026/poster/149052) · [作者来源](https://openreview.net/forum?id=tDqT2QD3Da)

- **问题 / 瓶颈** · 普通去噪分数匹配的类间区分不足。
- **核心创新 / 方法** · 微调时最大化类间似然比；推导 CFG 分数等价于样本自适应加权目标的最优解。
- **Baseline** · 普通 DSM 与推理期 CFG。
- **Benchmark** · 条件生成和无引导采样；具体数据及指标待核。
- **关键结果 / 消融** · 摘要称无引导质量明显改善，与 CFG 质量差距缩小。
- **适用条件 / 局限** · 受目标和模型分布条件限制，类别外迁移待核。

**可复用机制** · 同采样预算比较训练期分离目标与推理期引导，分别看质量和条件一致性。

<a id="paper-150565"></a>

## Improving Consistency in Retrieval Augmented Systems  With Group Similarity Rewards

[官方论文页](https://neurips.cc/virtual/2026/poster/150565) · [作者来源](https://openreview.net/forum?id=hCpmScyCoy)

- **问题 / 瓶颈** · 同义问题可能取回不同证据，生成结果反复变化。
- **核心创新 / 方法** · PS-GRPO 对改写组采样，以答案相似性给组奖励，并以近似降低配对成本。
- **Baseline** · 强检索增强和生成训练基线；名称待核。
- **Benchmark** · 短答、多跳、长答，分别测检索、生成和端到端一致性及准确性。
- **关键结果 / 消融** · 摘要称无需显式标准答案即可改善一致性和准确性。
- **适用条件 / 局限** · 相似性可能奖励一致的错误；需外部准确度与检索证据对照。

**可复用机制** · 改写输入、固定检索和变动检索分开测试，明确一致性问题来自哪一层。

<a id="paper-151902"></a>

## Improving constraint-based discovery with robust propagation and LLM priors

[官方论文页](https://neurips.cc/virtual/2026/poster/151902) · [作者来源](https://openreview.net/forum?id=X5adrFr97k)

- **问题 / 瓶颈** · 独立性检验误差会从初始碰撞结构传播，语言模型也会不稳定。
- **核心创新 / 方法** · 融合条件独立证据与语言先验建立高置信定向，再用 SPR 传播。
- **Baseline** · PC 及已有混合因果发现方法。
- **Benchmark** · 13 个真实基准，测结构准确性；另有理论可靠性条件。
- **关键结果 / 消融** · 摘要报告定向更准，给出理想检验下传播的正确性。
- **适用条件 / 局限** · 取决于骨架、分隔集合和种子质量；需检验错误先验影响。

**可复用机制** · 分别污染种子与分隔集合，比较碰撞优先和可信种子传播的级联误差。

<a id="paper-150848"></a>

## Improving Context-Shift Robustness of Convolutional Networks via Context-Regularized Cross-Entropy

[官方论文页](https://neurips.cc/virtual/2026/poster/150848) · [作者来源](https://openreview.net/forum?id=eu0NxAFRN2)

- **问题 / 瓶颈** · 模型利用非因果上下文，换背景即失准。
- **核心创新 / 方法** · 先用 ContrastiveCAMs 产生空间归因，再用 CR-CE 抑制上下文区域影响。
- **Baseline** · 普通交叉熵及已有空间归因途径。
- **Benchmark** · Waterbirds、Spawrious、ImageNet 与 ImageNet-BG、Hard-ImageNet。
- **关键结果 / 消融** · 摘要报告跨基准上下文偏移鲁棒性改善。
- **适用条件 / 局限** · 依赖能区分主体与上下文；部分任务上下文本身是有效信号。

**可复用机制** · 测主体、背景分别替换后的性能，并用等信息主体监督比较惩罚效果。

<a id="paper-151348"></a>

## Improving Diffusion Posterior Samplers with Lagged Temporal Corrections for Image Restoration

[官方论文页](https://neurips.cc/virtual/2026/poster/151348) · [作者来源](https://openreview.net/forum?id=bCS5vqUUqK)

- **问题 / 瓶颈** · 瞬时的数据一致估计波动会传到反向动态。
- **核心创新 / 方法** · 在后验采样残差框架下以二阶方式加入滞后时间修正。
- **Baseline** · DiffPIR、DDRM。
- **Benchmark** · 多个成像恢复任务，比较质量和去噪调用数；另做单步偏差方差分析。
- **关键结果 / 消融** · 无额外去噪调用而改善恢复。
- **适用条件 / 局限** · 收益依赖跨步估计误差结构，极稀疏采样或严重噪声待核。

**可复用机制** · 在等去噪调用下比较一阶与滞后二阶修正，监控反向步估计的抖动。

<a id="paper-149748"></a>

## Improving Flexible Image Tokenizers for Autoregressive Image Generation

[官方论文页](https://neurips.cc/virtual/2026/poster/149748) · [作者来源](https://openreview.net/forum?id=neJJASNqpr)

- **问题 / 瓶颈** · 嵌套尾部截断让早期词元信息过度集中，增加采样长度边际收益小。
- **核心创新 / 方法** · 冗余填充提高尾词元使用频率，视觉语义对齐从前到后逐渐减弱。
- **Baseline** · 固定长度和传统灵活词元器。
- **Benchmark** · ImageNet 256×256 自回归生成，具体指标待核。
- **关键结果 / 消融** · 摘要报告超越两类词元器。
- **适用条件 / 局限** · 其他分辨率、词元开销与两部分的独立收益待核。

**可复用机制** · 画随前缀长度增加的重建与生成曲线，检查尾端是否真正带来细节收益。

<a id="paper-152774"></a>

## Improving Function Space Flow Matching with Kernel Optimal Transport

[官方论文页](https://neurips.cc/virtual/2026/poster/152774) · [作者来源](https://openreview.net/forum?id=QT7iczCUkm)

- **问题 / 瓶颈** · 独立配对让桥接同时承担共性结构和实例残差，平坦欧式代价忽略路径几何。
- **核心创新 / 方法** · 保留神经算子骨干，以核希尔伯特空间的熵正则最优传输替换独立配对。
- **Baseline** · FFM、扩散、对抗模型和有限维 OT。
- **Benchmark** · 时间序列和 PDE 分布生成，MMD-RBF；另有目标良定性和网格截断理论。
- **关键结果 / 消融** · 摘要报告一致改善，函数几何核在 PDE 和路径数据上最好。
- **适用条件 / 局限** · 依赖核选择与数据正则性，训练时批内传输开销待核。

**可复用机制** · 固定网络与步数扫独立、欧式和函数核配对，报告分辨率变化下的稳定性。

<a id="paper-154485"></a>

## Improving General Role-Playing Agents via Psychology-Grounded Reasoning and Role-Aware Policy Optimization

[官方论文页](https://neurips.cc/virtual/2026/poster/154485) · [作者来源](https://openreview.net/forum?id=DF7xRhiXvd)

- **问题 / 瓶颈** · 角色特异表达与通用高分语句可能获得相同更新。
- **核心创新 / 方法** · RAPO 用角色描述与词元互信息在正负优势下非对称调权；另测试结构化角色推理。
- **Baseline** · GRPO 和既有角色推理。
- **Benchmark** · CoSER、CharacterBench、CharacterEval，多个模型规模。
- **关键结果 / 消融** · 摘要称角色推理优于已有提示路线，RAPO 一致优于 GRPO。
- **适用条件 / 局限** · 互信息代理可能放大词面角色线索，跨表述和通用能力待核。

**可复用机制** · 对角色或其他条件生成，用语义等效改写验证特异词权重是否学到条件本身。

<a id="paper-151051"></a>

## Improving Generative Adversarial Networks with Self-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/151051) · [作者来源](https://openreview.net/forum?id=dM03KyhkmA)

- **问题 / 瓶颈** · 标准 GAN 周期振荡，EMA 的优势只在部署时使用。
- **核心创新 / 方法** · 用感知损失将当前生成器向 EMA 生成器蒸馏，在简化博弈分析稳定性。
- **Baseline** · 常规 GAN 与仅推理使用 EMA。
- **Benchmark** · 多架构、数据和预训练微调，测 FID、random-FID 与优化轨迹。
- **关键结果 / 消融** · 证明 Dirac-GAN 局部稳定并减弱循环，实证提升生成质量。
- **适用条件 / 局限** · 局部理论不能必然外推深层 GAN，额外教师代价待核。

**可复用机制** · 在原 GAN 保持相同 EMA 更新，分别比较部署使用与训练期间教师的边际收益。

<a id="paper-152467"></a>

## Improving Guidance-Free Visual Generation via Self-Contrastive Alignment for Likelihood Estimation

[官方论文页](https://neurips.cc/virtual/2026/poster/152467) · [作者来源](https://openreview.net/forum?id=SsWOUYStqy)

- **问题 / 瓶颈** · 模仿 CFG 的单前向方法继承教师上限。
- **核心创新 / 方法** · 将模型自身在真实和生成样本上的对比信号重参数化纳入似然训练。
- **Baseline** · 模仿 CFG 的无引导方法，另对照结合 DPO。
- **Benchmark** · 扩散及自回归的类条件和文本到图像生成，质量与单次前向。
- **关键结果 / 消融** · 摘要称优于模仿 CFG 方法，与 DPO 有互补收益。
- **适用条件 / 局限** · 依赖自生成样本的代表性，定量质量和训练成本待核。

**可复用机制** · 对比蒸馏手工引导与直接拟合真实生成差异，并匹配推理预算。

<a id="paper-150649"></a>

## Improving LLM Final Representations with Inter-Layer Geometry

[官方论文页](https://neurips.cc/virtual/2026/poster/150649) · [作者来源](https://openreview.net/forum?id=gUPzBRGNCS)

- **问题 / 瓶颈** · 最后层可能漏信号，全层注意聚合又较贵。
- **核心创新 / 方法** · 把各层作为图节点，以稀疏规则 Cayley 图代替全连接图做聚合。
- **Baseline** · 仅最后层、择层、注意聚合、全连接图与 LoRA。
- **Benchmark** · 13 项任务、9 个模型及少样本，测预测与参数量。
- **关键结果 / 消融** · 准确率最高提升 40 个百分点，额外参数至多 0.1%。
- **适用条件 / 局限** · 需要访问中间层，具体任务增益和运行成本待核。

**可复用机制** · 在冻结骨干下同参数比较稀疏图、全连接图与末层，并消融图直径。

<a id="paper-148845"></a>

## Improving Neural Processes in the Low-Data Regime via Context-Subset Training and Self-Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/148845) · [作者来源](https://openreview.net/forum?id=uieGKHJk47)

- **问题 / 瓶颈** · 神经过程少任务训练会记忆任务，且子集预测不稳。
- **核心创新 / 方法** · 随机子集监督加教师全上下文分布前向 KL，网络结构与推理保持。
- **Baseline** · 普通神经过程，有无子集训练与蒸馏。
- **Benchmark** · 多种神经过程和预测任务，重点少元数据。
- **关键结果 / 消融** · 摘要报告更稳健且泛化更好；校准教师条件下不改渐近目标。
- **适用条件 / 局限** · 教师需校准，子集采法和跨任务偏移待核。

**可复用机制** · 对比同任务全信息教师与等上下文教师，测缩减上下文下的校准和误差。

<a id="paper-155969"></a>

## Improving Quantized Zeroth-Order Optimization through Reconstructed Low-Rank Structures

[官方论文页](https://neurips.cc/virtual/2026/poster/155969) · [作者来源](https://openreview.net/forum?id=1UKJD5PlWg)

- **问题 / 瓶颈** · 低比特抹去更新结构，零阶估计在量化时更不稳。
- **核心创新 / 方法** · 结构化矩阵分解扰动，采用二值聚合高斯方案控高阶矩，并重整量化尺度组。
- **Baseline** · 量化与全精度零阶方法。
- **Benchmark** · 多种 LLM 位宽含 INT2，另验证视觉 Transformer。
- **关键结果 / 消融** · 平均提升 2.0%–3.3%，给出收敛保证并缩小超低位宽差距。
- **适用条件 / 局限** · 低秩假设、量化设置和内存实际开销待核。

**可复用机制** · 以等内存与函数评估次数比较低秩和常规扰动，拆开位宽与梯度估计方差。

<a id="paper-151171"></a>

## Improving Self-Supervised Vision Transformers with Cross Distillation

[官方论文页](https://neurips.cc/virtual/2026/poster/151171) · [作者来源](https://openreview.net/forum?id=cSTY1Titxd)

- **问题 / 瓶颈** · CLS 注意力使全局语义梯度集中，低注意区域易产生密集预测错误。
- **核心创新 / 方法** · 对遮盖补丁目标混入少量教师 CLS 分布，维持骨干结构。
- **Baseline** · 标准补丁自蒸馏及全局图像预训练。
- **Benchmark** · 对齐的预训练设置，比较密集和图像级任务。
- **关键结果 / 消融** · 摘要报告两类任务均改善，梯度分析给出注意权重解释。
- **适用条件 / 局限** · 过多全局监督可能淡化局部信息，混合强度待核。

**可复用机制** · 按原 CLS 注意量分桶评估密集预测，检查收益是否集中于低注意区。

<a id="paper-150734"></a>

## Improving the Diffusability of Motion Tokenizer

[官方论文页](https://neurips.cc/virtual/2026/poster/150734) · [作者来源](https://openreview.net/forum?id=fnQkgTUCzX)

- **问题 / 瓶颈** · 提高重建容量未必带来生成收益，潜空间可能偏高频。
- **核心创新 / 方法** · 用预训练扩散作为评审抑制过高潜高频，通过平均速度预测做一步生成解码。
- **Baseline** · 现有动作 VAE 词元器及文本到动作扩散。
- **Benchmark** · 多种文本到动作评测，比较动作保真和文本对齐。
- **关键结果 / 消融** · 摘要称两类指标优于既有方法，未给定量。
- **适用条件 / 局限** · 高频也可承载真实快速动作，抑制强度和解码伪影需核。

**可复用机制** · 联合画潜频谱、重建、生成保真的关系，区分压高频与毁细节。

<a id="paper-149121"></a>

## Improving the Efficiency of Language Agent Teams with Adaptive Task Graphs

[官方论文页](https://neurips.cc/virtual/2026/poster/149121) · [作者来源](https://openreview.net/forum?id=sjSjyEGmnu)

- **问题 / 瓶颈** · 固定分工难适应新子任务，自由协作容易重复和冲突。
- **核心创新 / 方法** · 让团队共享子任务依赖、责任与进度，可随证据调整任务图。
- **Baseline** · MetaGPT、去中心化、领导者与执行者、静态分解。
- **Benchmark** · 多类协作和多种基础模型，对照准确率、用时、词元与冲突。
- **关键结果 / 消融** · 摘要称协调失败及开销减少，准确率相当或更好。
- **适用条件 / 局限** · 共享状态一致性成本和跨更长任务的可扩展性待核。

**可复用机制** · 固定模型和预算，在良性文件整理或分析中比较静态与动态任务依赖维护。

<a id="paper-151753"></a>

## Improving the Optimization Landscape of Matrix Completion with $\epsilon$-close Surrogates

[官方论文页](https://neurips.cc/virtual/2026/poster/151753) · [作者来源](https://openreview.net/forum?id=YJGa7iqmAu)

- **问题 / 瓶颈** · 部分观测的非凸优化可能缺乏合适等距条件。
- **核心创新 / 方法** · 向观测掩码零空间加 ε 级扰动，构造有受限等距性质的矩阵感知代理。
- **Baseline** · 原非凸矩阵补全和经典矩阵感知设定。
- **Benchmark** · 独立观测假设下的理论恢复分析，无摘要实证。
- **关键结果 / 消融** · 代理解与真值相距 O(ε)，并推导不显式要求采样率或不相干性的恢复保证。
- **适用条件 / 局限** · 依赖独立观测与代理结构；真实缺失机制和数值表现待核。

**可复用机制** · 选代理目标时同时约束观测保持与解偏差，并比较扰动大小对优化和误差的影响。
